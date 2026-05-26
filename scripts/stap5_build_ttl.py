#!/usr/bin/env python3
"""Stap 5 v4.5.0 builder: sheet 8 ISO+CSF mappings → SKOS-triples in m21-csf.ttl."""
import openpyxl
import re
import json
from collections import Counter, defaultdict
from pathlib import Path
from rdflib import Graph, Namespace, RDF, OWL

# === STAP A: Inlees + parse rauwe data ===
wb = openpyxl.load_workbook("/mnt/project/Cbw_NIS2_Control_Framework.xlsx", data_only=True)
ws = wb['Mapping Uitvoeringsverordening']
raw = []
for r in range(7, ws.max_row + 1):
    uv_id = ws.cell(row=r, column=2).value
    iso = ws.cell(row=r, column=4).value
    csf = ws.cell(row=r, column=5).value
    if uv_id:
        raw.append({
            "uv_id": str(uv_id).strip(),
            "iso_raw": str(iso).strip() if iso else "",
            "csf_raw": str(csf).strip() if csf else "",
        })
print(f"Datarijen: {len(raw)}")

# === STAP B: ISO-notatie-normalisatie ===
GREEK_ALPHA = "\u0391"
LATIN_A = "A"
normalize_log = []

def normalize_iso_ref(s: str):
    original = s
    s = s.replace(GREEK_ALPHA, LATIN_A)
    s = re.sub(r'^A(\d)', r'A.\1', s)
    s = re.sub(r'A\.\s+(\d)', r'A.\1', s)
    s = re.sub(r'(\d)\s+\.', r'\1.', s)
    s = s.strip()
    return s, (original != s)

parsed = []
for row in raw:
    iso_refs = []
    if row["iso_raw"]:
        for part in re.split(r'[,;]\s*', row["iso_raw"]):
            p = part.strip()
            if p:
                norm, changed = normalize_iso_ref(p)
                if changed:
                    normalize_log.append({"uv_id": row["uv_id"], "before": p, "after": norm})
                iso_refs.append(norm)
    csf_refs = re.findall(r'[A-Z]{2}\.[A-Z]{2}-\d{2,3}', row["csf_raw"])
    parsed.append({"uv_id": row["uv_id"], "iso_refs": iso_refs, "csf_refs": csf_refs})

print(f"Normalisaties: {len(normalize_log)}")
norm_counter = Counter()
for n in normalize_log:
    if GREEK_ALPHA in n["before"]:
        norm_counter["Greek_Alpha_to_Latin_A"] += 1
    elif re.match(r'^A\d', n["before"]):
        norm_counter["Missing_dot_after_A"] += 1
    else:
        norm_counter["Spurious_whitespace"] += 1
for k, v in norm_counter.most_common():
    print(f"  {k}: {v}")

# === STAP D: Resolve targets ===
def resolve_iso_target(ref: str):
    m_annex = re.match(r'^A\.(\d+)\.(\d+)$', ref)
    if m_annex:
        x, y = m_annex.groups()
        return f"bio:ISO27002_{x}_{y.zfill(2)}", "bio_annexA", "ok"
    m_clause = re.match(r'^(\d+)(?:\.(\d+))?(?:\.(\d+))?$', ref)
    if m_clause:
        parts = [g for g in m_clause.groups() if g is not None]
        return "ext:ISO27001_" + "_".join(parts), "ext_clause", "ok"
    return None, "unknown", "unresolved"

# Bouw bestaande IRI-set
g_tgt = Graph()
g_tgt.parse("m09-iso27001-ext.ttl", format="turtle")
g_tgt.parse("m08-bio20.ttl", format="turtle")
existing_iris = {str(s) for s in g_tgt.subjects(RDF.type, OWL.NamedIndividual)}

# Bouw csf:Subcategory-IRI-set (voorkom dangling subjects voor CSF v1.x-naming in sheet 8)
g_csf = Graph()
g_csf.parse("m21-csf.ttl", format="turtle")
CSF_NS = Namespace("https://grc.example.org/csf/")
existing_csf_subs = {str(s) for s in g_csf.subjects(RDF.type, CSF_NS.Subcategory)}
print(f"Existing csf:Subcategory-IRIs: {len(existing_csf_subs)}")

# === STAP E: Bouw paren ===
mappings_raw = []
unresolved = []
for p in parsed:
    if not p["csf_refs"] or not p["iso_refs"]:
        continue
    for csf in p["csf_refs"]:
        for iso in p["iso_refs"]:
            target, ttype, status = resolve_iso_target(iso)
            m = {"uv_id": p["uv_id"], "csf": csf, "iso_ref": iso,
                 "target": target, "type": ttype, "status": status}
            mappings_raw.append(m)
            if status != "ok":
                unresolved.append((p["uv_id"], csf, iso, "format-not-recognized"))

unique_pairs = set()
unique_mappings = []
csf_not_in_core = set()  # voor signaal
for m in mappings_raw:
    if m["status"] != "ok":
        continue
    # Check CSF-subject bestaat als csf:Subcategory
    csf_iri_full = "https://grc.example.org/csf/" + m["csf"].replace(".", "_").replace("-", "_")
    if csf_iri_full not in existing_csf_subs:
        csf_not_in_core.add(m["csf"])
        unresolved.append((m["uv_id"], m["csf"], m["iso_ref"], f"csf-subject-missing: {m['csf']} (niet in CSF 2.0 Core; mogelijk v1.x-naming)"))
        continue
    if m["target"].startswith("ext:"):
        iri_full = "https://grc.example.org/extended/" + m["target"][4:]
    elif m["target"].startswith("bio:"):
        iri_full = "https://grc.example.org/bio/" + m["target"][4:]
    else:
        continue
    if iri_full not in existing_iris:
        unresolved.append((m["uv_id"], m["csf"], m["iso_ref"], f"target-missing: {m['target']}"))
        continue
    key = (m["csf"], m["target"])
    if key in unique_pairs:
        continue
    unique_pairs.add(key)
    unique_mappings.append(m)

dedup_pct = (len(mappings_raw) - len(unique_mappings)) / len(mappings_raw) * 100 if mappings_raw else 0
print(f"\n=== Statistieken ===")
print(f"  Raw paren:        {len(mappings_raw)}")
print(f"  Unieke (csf,tgt): {len(unique_pairs)}")
print(f"  Unresolved:       {len(unresolved)}")
print(f"  Dedup:            {dedup_pct:.1f}%")

type_counts = Counter(m["type"] for m in unique_mappings)
print(f"\n  Verdeling per target-type:")
for t, c in type_counts.most_common():
    print(f"    {t}: {c}")

if unresolved:
    print(f"\n  Unresolved (eerste 6):")
    for u in unresolved[:6]:
        print(f"    UV {u[0]}: csf={u[1]}, iso={u[2]} → {u[3]}")

# === STAP F: TTL ===
ttl = [f"""
# =============================================================================
# v4.5.0 Fase 3 — Stap 5: Sheet 8 SKOS-mappings (CSF ↔ ISO 27001 / BIO)
# Datum: 2026-05-19
# Bron: CBW/NIS2 Control Framework (ADR & NOREA, versie 1.0, 30 september 2025, CC-BY 4.0)
#       Tabblad 'Mapping Uitvoeringsverordening' — 49 UV-onderwerpen
# Match-type: skos:closeMatch (besluit 5)
# =============================================================================
# Bron-attribuering via blok-comment (ext:Attr_CBW_NIS2_Framework_2025_CC_BY_4_0,
# geen per-triple ext:sourceAttribution-link — consistent met v4.4.0 Stap 5-precedent
# en masterchat-voorkeur Stap 5-GO v4.5.0).
#
# ISO-target-resolutie:
#   - Hoofdtekst-clausule X.Y[.Z]  →  ext:ISO27001_X[_Y[_Z]]
#   - Annex A-control A.X.Y        →  bio:ISO27002_<X>_<YY zfill> (D5 sameAs-brug naar ctrl:)
#
# ISO-notatie-normalisatie ({len(normalize_log)} wijzigingen, tabel in patch-rapport §8):
#   - {norm_counter.get('Greek_Alpha_to_Latin_A', 0)}× Greek Alpha (Α, U+0391) → Latin A
#   - {norm_counter.get('Missing_dot_after_A', 0)}× missing dot after A (A5.7 → A.5.7)
#   - {norm_counter.get('Spurious_whitespace', 0)}× spurious whitespace ('A. 5.30' → 'A.5.30')
#
# Statistieken:
#   - Raw paren (multi):         {len(mappings_raw)}
#   - Unieke (csf,target):       {len(unique_pairs)}
#   - Dedup-reductie:            {dedup_pct:.1f}%
#   - Unresolved:                {len(unresolved)}
"""]

by_csf = defaultdict(list)
for m in unique_mappings:
    by_csf[m["csf"]].append(m["target"])

ttl.append(f"\n# --- {len(unique_pairs)} skos:closeMatch (gegroepeerd per CSF-Subcategory) ---\n")
for csf_code in sorted(by_csf.keys()):
    targets = sorted(set(by_csf[csf_code]))
    csf_iri = f"csf:{csf_code.replace('.', '_').replace('-', '_')}"
    targets_formatted = " ,\n        ".join(targets)
    ttl.append(f"""{csf_iri} skos:closeMatch
        {targets_formatted} .
""")

block = "\n".join(ttl)
m21_path = Path("/home/claude/v433/m21-csf.ttl")
current = m21_path.read_text()
m21_path.write_text(current + block)
print(f"\n✓ Block appended to m21-csf.ttl ({len(block):,} chars)")

Path("/home/claude/csf_step5_log.json").write_text(json.dumps({
    "normalisations": normalize_log,
    "unresolved": unresolved,
    "stats": {
        "raw_pairs": len(mappings_raw),
        "unique_pairs": len(unique_pairs),
        "dedup_pct": round(dedup_pct, 1),
        "by_type": dict(type_counts),
    }
}, indent=2, ensure_ascii=False))
print("✓ Saved log")
