#!/usr/bin/env python3
"""
import-from-ontology.py — Spoor B bouwsteen B7: import-pijplijn A -> B.

Extraheert STRUCTUUR (frameworks, controls, M04-rollen) uit de Spoor A
ontologie-export (grc-data-v*.json) en levert een idempotente,
non-destructieve SQL-INSERT-bundle voor de Spoor B SQL.js-werkmap
(grc-dashboard-v3-2.html). Patroon C (O2): structuur uit de ontologie;
operationele velden (eigenaar/deadline/voortgang) blijven in Spoor B.

Bron-versie-waarheid (masterchat-besluit 2026-05-29, Optie A):
  De enige beschikbare export is grc-data-v4_6_0.json. v4.6.3 verschilt
  van v4.6.0 alleen in twee SKOS-predicate-substituties (m14, broad->related),
  zonder TBox- of individual-wijziging. De structuur (frameworks/controls/
  rollen) is dus identiek. Daarom labelen we eerlijk:
    "ontologie-structuur v4.6.0 - SKOS-status t/m v4.6.3"
  Scriptnaam volgt de bron (versie-geparametriseerd), niet de instructie-string.

Discipline (canonical applier-pattern, vgl. /applier-template):
  - dry-run is DEFAULT (analyseert + schrijft SQL-bundle, muteert geen DB)
  - --apply --db <pad>  muteert een SQLite-DB (idempotent + non-destructief)
  - --self-test          bouwt een wegwerp-DB en bewijst idempotentie + orphan
  - provenance: meta.source_files_hash uit de export als anker
  - non-destructief: verwijderde IRIs -> orphan-markeren, NOOIT hard-deleten
  - per-tabel-logging van toegevoegd/bijgewerkt/orphan

Gebruik:
  python3 import-from-ontology.py
      # dry-run: leest dashboard/grc-data-v4_6_0.json, schrijft
      #          dashboard/structure-import-v4_6_0.sql, muteert niets
  python3 import-from-ontology.py --apply --db pad/naar.db
      # past de import toe op een bestaande SQL.js-database
  python3 import-from-ontology.py --self-test
      # zelf-verificatie zonder externe bestanden te raken
"""

import argparse
import json
import os
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SOURCE = os.path.join(HERE, "grc-data-v4_6_0.json")

# --- Extractie-conventies (deterministisch op OWL-type, geen IRI-regex) ----

# Frameworks: namespace 'fw', maar GEEN helper-domeinen.
FRAMEWORK_SKIP_TYPES = {"FrameworkDomain"}

# Controls: vier OWL-control-types -> stabiel framework_id dat aansluit op de
# bestaande v3-2-seed-frameworks (zodat 'controls per framework' blijft kloppen).
CONTROL_TYPE_TO_FRAMEWORK = {
    "BIOControl": "BIO-2.0",
    "ISO27002Control": "ISO-27002-2022",
    "NISTControl": "NIST-800-53-R5",
    "CBWControl": "CBW",
}

# Rollen: alleen echte rol-types uit ns 'roles' (GRCActivity/RACIType zijn
# geen rollen en worden overgeslagen).
ROLE_TYPES = {
    "OperationalRole", "SpecialistRole", "OwnerRole", "AuditRole",
    "GovernanceRole", "ManagementRole", "BVC",
}

# Structuur-kolommen die B7 toevoegt (K1 iri + non-destructieve provenance).
# owl_klasse bestaat al op frameworks/rollen; ensure_columns voegt 'm alleen
# toe waar hij ontbreekt (controls) — PRAGMA-geguard, dus idempotent.
EXTRA_COLUMNS = [
    ("iri", "TEXT"),
    ("herkomst", "TEXT DEFAULT 'handmatig'"),
    ("bron_versie", "TEXT"),
    ("orphan", "INTEGER DEFAULT 0"),
    ("owl_klasse", "TEXT"),
]


def local_part(node_id):
    """ 'bio:ISO27002_7_05' -> 'ISO27002_7_05' (control_nr-vulling, NOT NULL)."""
    return node_id.split(":", 1)[1] if ":" in node_id else node_id


def extract(export):
    """Verdeel de export-nodes in frameworks / controls / rollen."""
    nodes = export["nodes"]
    frameworks, controls, rollen, skipped = [], [], [], {"fw_domein": 0, "roles_nonrol": 0}

    for n in nodes:
        ns, typ = n.get("namespace"), n.get("type")
        uri = n.get("uri")
        label = n.get("label") or local_part(n["id"])
        desc = (n.get("description") or {}).get("nl") if isinstance(n.get("description"), dict) else None

        if ns == "fw":
            if typ in FRAMEWORK_SKIP_TYPES:
                skipped["fw_domein"] += 1
                continue
            frameworks.append({"id": n["id"], "naam": label, "iri": uri, "owl_klasse": typ})
        elif typ in CONTROL_TYPE_TO_FRAMEWORK:
            controls.append({
                "id": n["id"], "framework_id": CONTROL_TYPE_TO_FRAMEWORK[typ],
                "control_nr": local_part(n["id"]), "titel": label,
                "beschrijving": desc, "iri": uri, "owl_klasse": typ,
            })
        elif ns == "roles":
            if typ in ROLE_TYPES:
                rollen.append({"id": n["id"], "functienaam": label, "iri": uri, "owl_klasse": typ})
            else:
                skipped["roles_nonrol"] += 1

    return frameworks, controls, rollen, skipped


# --- Schema-migratie (PRAGMA-geguard => idempotent) ------------------------

def ensure_columns(conn, table):
    have = {row[1] for row in conn.execute(f"PRAGMA table_info({table})")}
    added = []
    for col, decl in EXTRA_COLUMNS:
        if col not in have:
            conn.execute(f"ALTER TABLE {table} ADD COLUMN {col} {decl}")
            added.append(col)
    return added


def ensure_meta_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS ontologie_import_meta(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_file TEXT, source_version TEXT, skos_status_tm TEXT,
            structuur_label TEXT, source_hash TEXT,
            n_frameworks INTEGER, n_controls INTEGER, n_rollen INTEGER,
            geimporteerd_op TEXT DEFAULT(datetime('now')))""")


# --- Idempotente, non-destructieve upsert per tabel ------------------------

def sync_table(conn, table, rows, cols, bron_versie):
    """
    Non-destructief sync-patroon:
      1) markeer alle eerder-geimporteerde rijen tentatief als orphan=1
      2) upsert de huidige bron-rijen -> orphan=0, herkomst='ontologie'
      3) rijen die in stap 2 niet geraakt zijn blijven orphan=1 (verwijderd
         in de bron, maar NOOIT hard-gedeletet)
    Handmatige rijen (herkomst='handmatig') blijven altijd ongemoeid.
    """
    conn.execute(f"UPDATE {table} SET orphan=1 WHERE herkomst='ontologie'")
    insert_cols = cols + ["iri", "herkomst", "bron_versie", "orphan"]
    placeholders = ",".join("?" for _ in insert_cols)
    set_clause = ",".join(f"{c}=excluded.{c}" for c in cols)
    sql = (f"INSERT INTO {table}({','.join(insert_cols)}) VALUES({placeholders}) "
           f"ON CONFLICT(id) DO UPDATE SET {set_clause},"
           f"iri=excluded.iri,herkomst='ontologie',bron_versie=excluded.bron_versie,orphan=0")
    added = updated = 0
    for r in rows:
        existed = conn.execute(f"SELECT 1 FROM {table} WHERE id=?", (r["id"],)).fetchone()
        conn.execute(sql, [r[c] for c in cols] + [r["iri"], "ontologie", bron_versie, 0])
        if existed:
            updated += 1
        else:
            added += 1
    orphan = conn.execute(
        f"SELECT COUNT(*) FROM {table} WHERE herkomst='ontologie' AND orphan=1").fetchone()[0]
    return {"toegevoegd": added, "bijgewerkt": updated, "orphan": orphan}


def apply_import(conn, frameworks, controls, rollen, meta):
    ensure_meta_table(conn)
    migr = {t: ensure_columns(conn, t) for t in ("frameworks", "controls", "rollen")}
    bron_versie = meta["source_version"]
    log = {
        "frameworks": sync_table(conn, "frameworks", frameworks, ["id", "naam", "owl_klasse"], bron_versie),
        "controls": sync_table(conn, "controls", controls,
                               ["id", "framework_id", "control_nr", "titel", "beschrijving", "owl_klasse"], bron_versie),
        "rollen": sync_table(conn, "rollen", rollen, ["id", "functienaam", "owl_klasse"], bron_versie),
    }
    conn.execute(
        "INSERT INTO ontologie_import_meta(source_file,source_version,skos_status_tm,"
        "structuur_label,source_hash,n_frameworks,n_controls,n_rollen) VALUES(?,?,?,?,?,?,?,?)",
        (meta["source_file"], meta["source_version"], meta["skos_status_tm"],
         meta["structuur_label"], meta["source_hash"], len(frameworks), len(controls), len(rollen)))
    return migr, log


# --- SQL-bundle-generator (artefact voor de v3-2 JS-consument) -------------

def sql_literal(v):
    if v is None:
        return "NULL"
    return "'" + str(v).replace("'", "''") + "'"


def generate_sql_bundle(frameworks, controls, rollen, meta):
    L = []
    L.append("-- ════════════════════════════════════════════════════════════")
    L.append("-- B7 ontologie-structuur-import — Spoor B (grc-dashboard-v3-2)")
    L.append(f"-- Bron        : {meta['source_file']}")
    L.append(f"-- Structuur   : {meta['structuur_label']}")
    L.append(f"-- Provenance  : source_files_hash={meta['source_hash']}")
    L.append(f"-- Telling     : {len(frameworks)} frameworks · {len(controls)} controls · {len(rollen)} rollen")
    L.append("-- Idempotent + non-destructief: re-run = zelfde eindstaat;")
    L.append("--   verwijderde IRIs -> orphan=1, nooit hard-delete.")
    L.append("-- LET OP: de iri/herkomst/bron_versie/orphan-kolommen worden door de")
    L.append("--   v3-2-importfunctie PRAGMA-geguard toegevoegd (zie ensure_columns).")
    L.append("-- ════════════════════════════════════════════════════════════")
    L.append("BEGIN TRANSACTION;")
    L.append("CREATE TABLE IF NOT EXISTS ontologie_import_meta(id INTEGER PRIMARY KEY AUTOINCREMENT,"
             "source_file TEXT,source_version TEXT,skos_status_tm TEXT,structuur_label TEXT,"
             "source_hash TEXT,n_frameworks INTEGER,n_controls INTEGER,n_rollen INTEGER,"
             "geimporteerd_op TEXT DEFAULT(datetime('now')));")

    def emit(table, rows, cols):
        L.append(f"\n-- {table}: tentatief orphan, dan upsert")
        L.append(f"UPDATE {table} SET orphan=1 WHERE herkomst='ontologie';")
        insert_cols = cols + ["iri", "herkomst", "bron_versie", "orphan"]
        set_clause = ",".join(f"{c}=excluded.{c}" for c in cols)
        for r in rows:
            vals = [sql_literal(r[c]) for c in cols] + [
                sql_literal(r["iri"]), "'ontologie'", sql_literal(meta["source_version"]), "0"]
            L.append(f"INSERT INTO {table}({','.join(insert_cols)}) VALUES({','.join(vals)}) "
                     f"ON CONFLICT(id) DO UPDATE SET {set_clause},"
                     f"iri=excluded.iri,herkomst='ontologie',bron_versie=excluded.bron_versie,orphan=0;")

    emit("frameworks", frameworks, ["id", "naam", "owl_klasse"])
    emit("controls", controls, ["id", "framework_id", "control_nr", "titel", "beschrijving", "owl_klasse"])
    emit("rollen", rollen, ["id", "functienaam", "owl_klasse"])

    L.append("\nINSERT INTO ontologie_import_meta(source_file,source_version,skos_status_tm,"
             "structuur_label,source_hash,n_frameworks,n_controls,n_rollen) VALUES("
             f"{sql_literal(meta['source_file'])},{sql_literal(meta['source_version'])},"
             f"{sql_literal(meta['skos_status_tm'])},{sql_literal(meta['structuur_label'])},"
             f"{sql_literal(meta['source_hash'])},{len(frameworks)},{len(controls)},{len(rollen)});")
    L.append("COMMIT;")
    return "\n".join(L) + "\n"


def build_meta(source_path, export):
    m = export.get("meta", {})
    src_version = m.get("ontology_version", "?")
    return {
        "source_file": os.path.basename(source_path),
        "source_version": src_version,
        "skos_status_tm": "4.6.3",
        "structuur_label": f"ontologie-structuur v{src_version} - SKOS-status t/m v4.6.3",
        "source_hash": m.get("source_files_hash", ""),
    }


# --- v3-2-schema (alleen voor --self-test) ---------------------------------

V32_SCHEMA = [
    "CREATE TABLE frameworks(id TEXT PRIMARY KEY,naam TEXT NOT NULL,versie TEXT,uitgevende_instantie TEXT,"
    "jurisdictie TEXT,bindend INTEGER DEFAULT 0,owl_klasse TEXT,module TEXT,toepasselijk INTEGER DEFAULT 1,"
    "notitie TEXT,aangemaakt_op TEXT DEFAULT(datetime('now')),gewijzigd_op TEXT DEFAULT(datetime('now')))",
    "CREATE TABLE controls(id TEXT PRIMARY KEY,framework_id TEXT,control_nr TEXT NOT NULL,titel TEXT NOT NULL,"
    "domein TEXT,beschrijving TEXT,toepasselijk INTEGER DEFAULT 1,uitsluitingsmotivering TEXT,"
    "implementatiestatus TEXT,eigenaar_rol TEXT,eigenaar_naam TEXT,documentatie TEXT,notitie TEXT,"
    "nis2_ref TEXT,dora_ref TEXT,bio_ref TEXT,nist_ref TEXT,aangemaakt_op TEXT DEFAULT(datetime('now')),"
    "gewijzigd_op TEXT DEFAULT(datetime('now')))",
    "CREATE TABLE rollen(id TEXT PRIMARY KEY,functienaam TEXT NOT NULL,stelsel TEXT,"
    "wettelijk_verplicht INTEGER DEFAULT 0,grondslag TEXT,bezet_door_naam TEXT,bezet_door_email TEXT,"
    "bezet_sinds TEXT,rapporteert_aan TEXT,owl_klasse TEXT,notitie TEXT,aangemaakt_op TEXT DEFAULT(datetime('now')))",
]


def self_test(source_path):
    print("── SELF-TEST ─────────────────────────────────────────────")
    export = json.load(open(source_path, encoding="utf-8"))
    frameworks, controls, rollen, _ = extract(export)
    meta = build_meta(source_path, export)
    conn = sqlite3.connect(":memory:")
    for ddl in V32_SCHEMA:
        conn.execute(ddl)
    # bestaande handmatige seed-rij (mag NOOIT geraakt worden)
    conn.execute("INSERT INTO frameworks(id,naam,owl_klasse) VALUES('NIS2','NIS2 (handmatig)','fw:Demo')")

    apply_import(conn, frameworks, controls, rollen, meta)
    c1 = {t: conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0] for t in ("frameworks", "controls", "rollen")}
    apply_import(conn, frameworks, controls, rollen, meta)  # tweede run
    c2 = {t: conn.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0] for t in ("frameworks", "controls", "rollen")}

    assert c1 == c2, f"NIET idempotent: {c1} != {c2}"
    hand = conn.execute("SELECT naam,herkomst FROM frameworks WHERE id='NIS2'").fetchone()
    assert hand == ("NIS2 (handmatig)", "handmatig"), f"handmatige rij aangetast: {hand}"

    # non-destructief: simuleer verwijderde IRI in de bron
    reduced = controls[:-1]
    removed_id = controls[-1]["id"]
    apply_import(conn, frameworks, reduced, rollen, meta)
    still_there = conn.execute("SELECT orphan FROM controls WHERE id=?", (removed_id,)).fetchone()
    assert still_there is not None, "verwijderde IRI is hard-gedeletet (mag niet)"
    assert still_there[0] == 1, "verwijderde IRI niet als orphan gemarkeerd"

    print(f"  idempotent      : OK  {c1}")
    print(f"  handmatige rij  : OK  ongemoeid ({hand[0]})")
    print(f"  non-destructief : OK  verwijderde control '{removed_id}' -> orphan=1, niet gedeletet")
    print("── SELF-TEST GESLAAGD ────────────────────────────────────")


def main():
    ap = argparse.ArgumentParser(description="B7 ontologie-structuur-import (dry-run default).")
    ap.add_argument("--source", default=DEFAULT_SOURCE, help="ontologie-export JSON")
    ap.add_argument("--sql-out", default=None, help="pad voor de SQL-bundle (dry-run)")
    ap.add_argument("--apply", action="store_true", help="muteer een SQLite-DB i.p.v. dry-run")
    ap.add_argument("--db", default=None, help="doel-DB voor --apply")
    ap.add_argument("--self-test", action="store_true", help="zelf-verificatie")
    args = ap.parse_args()

    if args.self_test:
        self_test(args.source)
        return

    if not os.path.exists(args.source):
        sys.exit(f"FOUT: bron niet gevonden: {args.source}")
    export = json.load(open(args.source, encoding="utf-8"))
    frameworks, controls, rollen, skipped = extract(export)
    meta = build_meta(args.source, export)

    print(f"Bron        : {meta['source_file']}  ({meta['structuur_label']})")
    print(f"Provenance  : source_files_hash={meta['source_hash']}")
    print(f"Geextraheerd: {len(frameworks)} frameworks · {len(controls)} controls · {len(rollen)} rollen")
    print(f"Overgeslagen: {skipped['fw_domein']} fw-domeinen · {skipped['roles_nonrol']} niet-rol (ns roles)")

    if args.apply:
        if not args.db or not os.path.exists(args.db):
            sys.exit("FOUT: --apply vereist een bestaande --db <pad>")
        conn = sqlite3.connect(args.db)
        with conn:
            migr, log = apply_import(conn, frameworks, controls, rollen, meta)
        conn.close()
        print("\n── TOEGEPAST (idempotent, non-destructief) ──")
        for t in ("frameworks", "controls", "rollen"):
            print(f"  {t:11s}: +{log[t]['toegevoegd']} nieuw · ~{log[t]['bijgewerkt']} bijgewerkt · {log[t]['orphan']} orphan"
                  + (f"  [kolommen toegevoegd: {migr[t]}]" if migr[t] else ""))
    else:
        sver = meta["source_version"].replace(".", "_")
        out = args.sql_out or os.path.join(HERE, f"structure-import-v{sver}.sql")
        bundle = generate_sql_bundle(frameworks, controls, rollen, meta)
        with open(out, "w", encoding="utf-8") as f:
            f.write(bundle)
        # JS-wrapper: maakt de bundle laadbaar onder file:// (zoals grc-data-*.js
        # window.GRC_DATA zet) — <script src> werkt lokaal waar fetch() faalt.
        js_out = os.path.join(HERE, f"structure-import-v{sver}.js")
        with open(js_out, "w", encoding="utf-8") as f:
            f.write("// Gegenereerd door import-from-ontology.py — niet handmatig bewerken.\n")
            f.write("window.STRUCTURE_IMPORT = " + json.dumps({
                "sql": bundle,
                "meta": meta,
                "telling": {"frameworks": len(frameworks), "controls": len(controls), "rollen": len(rollen)},
            }, ensure_ascii=False) + ";\n")
        rel = os.path.dirname(HERE)
        print(f"\nDRY-RUN: SQL-bundle  -> {os.path.relpath(out, rel)}")
        print(f"         JS-wrapper  -> {os.path.relpath(js_out, rel)}  (window.STRUCTURE_IMPORT)")
        print("Geen DB gemuteerd. Gebruik --apply --db <pad> om toe te passen, of --self-test.")


if __name__ == "__main__":
    main()
