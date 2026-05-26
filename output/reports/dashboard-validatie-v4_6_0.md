# Dashboard-validatie v4.6.0

**Datum**: 2026-05-26
**Subagent**: Dashboard
**Scope**: read-only validatie inhaalslag-artefacten v4.6.0
**Werkwijze**: geen wijzigingen aan `dashboard/`-bestanden; uitsluitend inspectie + syntax/integriteits-checks; enige geschreven file is dit rapport.

## Samenvatting

| # | Check | Status |
|---|---|---|
| 1 | `dashboard/build_grc_explorer_v3.py` aanwezig + syntactisch valide | OK |
| 2 | `dashboard/grc-data-v4_6_0.json` aanwezig + valide JSON | OK |
| 3 | `dashboard/grc-data-v4_6_0.js` aanwezig + correcte wrapper + payload-overeenkomst | OK |
| 4 | `output/reports/patchnotitie-export-v4_6_0.md` aanwezig + build_v3-referenties | OK |
| 5 | `output/reports/skos-kwaliteitsanalyse-v4_6_0.md` aanwezig + sectie-structuur | OK |
| 6 | `output/verification/file_hashes_dashboard_v4_6_0.txt` aanwezig + consistent | OK |

Score: 6/6 OK, 0 afwijkingen.

---

## Check 1 — build_grc_explorer_v3.py

**Status**: OK

**Bevindingen**

- Bestand aanwezig: `dashboard/build_grc_explorer_v3.py`, 23.241 bytes, 590 regels, mtime 2026-05-26 10:07.
- Syntax-check via `python3 -m py_compile`: SYNTAX_OK (geen uitvoering — alleen byte-compile).
- Hoofd-functies (per `grep -nE "^def "`):
  - `bepaal_laag(uri_str)` — laag-classificatie (incl. nieuwe csf→4 en isms:maturity→5, conform patchnotitie §"Script-wijzigingen v2 → v3").
  - `get_prefix(uri_str)`, `get_local(uri_str)`, `make_id(uri_str)` — URI-utilities.
  - `get_literal(g, uri, prop, lang=None)`, `get_label(g, uri)`, `get_bilingual(g, uri, prop)` — RDF-literal-extractie inclusief @nl/@en.
  - `is_schema(g, uri)`, `get_types(g, uri)` — type-introspectie.
  - `get_iso27002_attributes(g, uri)` — domein-specifieke extractie.
  - `get_node_literals(g, uri)` — node-payload-bouw.
  - `edge_category(prop_uri_str)` — predicate-categorisatie (governance / csf-hierarchy / maturity / attribution / enrichment / other).
  - `compute_source_hash(ttl_files)` — provenance-hash voor source-set.
- Versie-discipline: aparte `build_v3`-file naast bestaande `build_grc_explorer_v2.py` (22.702 bytes, mtime 2026-04-14), conform versionering-conventie ("oude scripts behouden voor reproduceerbaarheid").

---

## Check 2 — grc-data-v4_6_0.json

**Status**: OK

**Bevindingen**

- Bestand aanwezig: `dashboard/grc-data-v4_6_0.json`, 2.603.655 bytes (~2,48 MB), mtime 2026-05-26 10:07.
- JSON-validatie via `json.load`: JSON_OK.
- Toplevel-keys: `["meta", "nodes", "edges"]`.
- `meta.ontology_version`: `"4.6.0"`.
- `meta.ontology_version_iri`: `https://grc.example.org/ontology/v4.6.0/`.
- `meta.generated`: `2026-05-22T06:44:01.781823+00:00`.
- `meta.source_files`: lijst met `grc-bridges.ttl`, `grc-core.ttl`, m01 t/m m12 zichtbaar in eerste 500 chars — consistent met v4.6.0-modulen-set.
- Node-count: **1.788**; edge-count: **7.249**.
- Steekproef-node (`bio:ISO27002_7_05`) bevat verwachte velden: `id`, `label`, `label_en`, `type`, `types`, `namespace`, `laag`, `laag_naam`, `uri`, `description{nl,en}`.
- Steekproef-edge bevat `source`, `target`, `relation`, `prop_uri`, `category` (`csf-hierarchy` in steekproef — bevestigt dat csf-categorie-mapping uit v3 actief is).

---

## Check 3 — grc-data-v4_6_0.js

**Status**: OK

**Bevindingen**

- Bestand aanwezig: `dashboard/grc-data-v4_6_0.js`, 2.108.563 bytes (~2,01 MB), mtime 2026-05-26 10:07.
- Wrapper-pattern (eerste regel + start payload):
  - Regel 1: `/* GRC Kennismodel v4.6.0 — gegenereerd door build_grc_explorer v3.0 */`
  - Daarna: `window.GRC_DATA = {"meta": {...}, ...};`
- Sluit af met `}]};` (geldige JS-statement-terminator).
- Naamgeving: `window.GRC_DATA` (niet `window.grcData`) — afwijkend van het voorbeeld in subagent-config maar intern consistent; mogelijk geconventioneerd in `grc-explorer-v2.html`/HTML-laag (niet binnen scope van deze validatie geverifieerd).
- Payload-overeenkomst met JSON (volledige diff via `json.loads`):
  - `meta.generated` identiek.
  - `nodes` lijst-equivalent (`payload['nodes'] == d['nodes']` → True).
  - `edges` lijst-equivalent (`payload['edges'] == d['edges']` → True).
  - Node-count en edge-count in JS-payload: 1.788 / 7.249 — exact gelijk aan JSON.
- Grootte-verschil JS vs JSON (~495 KB kleiner) is verklaarbaar door compactere JSON-serialisatie van `json.dumps` (geen indenting) versus mogelijk geïndenteerde JSON-file; geen integriteits-issue gezien volledige equivalentie van de geparseerde payload.

---

## Check 4 — patchnotitie-export-v4_6_0.md

**Status**: OK

**Bevindingen**

- Bestand aanwezig: `output/reports/patchnotitie-export-v4_6_0.md`, 5.768 bytes, mtime 2026-05-26 10:07.
- Build_v3-verwijzingen aangetroffen:
  - Regel 2: `**Script:** \`build_grc_explorer_v3.py\` (nieuwe versie — zie wijzigingslog)`.
  - Sectie `## Script-wijzigingen v2 → v3 (samenvatting)` (regel 84) bevat 11 expliciete delta-rijen tussen v2 en v3, o.a.:
    - `csf:`-namespace + `NS_PREFIX` (D3-revisie v4.5.0).
    - `bepaal_laag()` uitgebreid met csf→4, isms:maturity→5, ctrl:CBW→2.
    - Vier nieuwe constanten: `GOVERNANCE_PROPS` (uitgebreid), `CSF_HIERARCHY_PROPS`, `MATURITY_PROPS`, `ATTRIBUTION_PROPS`, `ENRICHMENT_PROPS`.
    - `LAAG_NAMEN[5]` → "Audit & Volwassenheid".
    - Predicate-consolidatie α (`law_article` → `compl:articleRef`; `csf_id` → `csf:csfIdentifier`).
- Hoofdsecties: Delta-overzicht, Impact per sprint (v4.3.2 t/m v4.6.0), Verificatie tegen canonical_metrics_v4_6_0, Script-wijzigingen, Twee architecturele bevindingen (B1 = Laag 5 naam, B2 = "other"-categorie 2.819 edges).
- Afsluitende regel bevestigt: "Pre-conditie 3 voor migratie naar Claude Code: VOLDAAN."

---

## Check 5 — skos-kwaliteitsanalyse-v4_6_0.md

**Status**: OK

**Bevindingen**

- Bestand aanwezig: `output/reports/skos-kwaliteitsanalyse-v4_6_0.md`, 7.034 bytes, mtime 2026-05-26 10:07.
- Hoofdsecties (via `grep "^#"`):
  - `# SKOS-kwaliteitsanalyse — GRC Kennismodel v4.6.0`
  - `## Managementsamenvatting`
  - `## C1 — Match-type verdeling`
  - `## C2 — Namespace-paar matrix`
  - `## C3 — Frameworks zonder uitgaande SKOS`
  - `## C4 — Cross-bron overlap detectie`
  - `## C5 — Concentratie-detectie`
  - `## Drie aandachtspunten voor opvolging`
  - `## Kanttekening bij 1.759 vs 1.798 SKOS-edges in export`
- Bevindingenstructuur is C1–C5 thematisch + expliciete aandachtspunten-sectie. Wijkt af van het standaard "§1–§6"-template uit de subagent-config (Mappings-overzicht / Categorie-distributie / Top-N problemen / Cross-bron / Aandachtspunten / Fix-voorstellen) maar dekt inhoudelijk vergelijkbare scope:
  - C1 ≈ Categorie-distributie / match-type verdeling.
  - C2 + C4 ≈ Cross-bron-overlap-analyse.
  - C3 + C5 ≈ Top-problemen.
  - "Drie aandachtspunten" ≈ Aandachtspunten voor masterchat-review.
- De expliciete "Kanttekening bij 1.759 vs 1.798 SKOS-edges in export" duidt op een edge-tellings-discrepantie tussen ontologie-mappings en geëxporteerde edges; geadresseerd in eigen sectie.
- A3-pre-conditie (CSF→ISO 27002-traversal, SPARQL-pattern open): niet binnen scope van deze validatie geverifieerd; subagent-config schrijft voor dat SKOS-analyse tot A3-resolutie beperkt blijft tot non-CSF-mappings. Of het rapport zich daaraan houdt is niet inhoudelijk getoetst (alleen sectie-structuur gevalideerd).

---

## Check 6 — file_hashes_dashboard_v4_6_0.txt

**Status**: OK

**Bevindingen**

- Bestand aanwezig: `output/verification/file_hashes_dashboard_v4_6_0.txt`, 458 bytes, mtime 2026-05-26 10:07.
- Aantal hash-regels: **5** (één trailing newline, geen lege content-regels).
- Format-consistentie: alle regels volgen `<64-hex-hash><dubbele spatie><pad>` — uniform SHA256 zonder algorithm-prefix.
- Inhoud (gevalideerd):
  ```
  c902cfc9...3ff7e9e  build_grc_explorer_v3.py
  8d9b5b7a...10d28f164  grc-data-v4_6_0.json
  44c2d24b...80fdf573  grc-data-v4_6_0.js
  9baf368f...f4bad083  patchnotitie-export-v4_6_0.md
  fe72a6ed...c5ee631c6  skos-kwaliteitsanalyse-v4_6_0.md
  ```
- Hash-verificatie: alle 5 hashes opnieuw berekend met `hashlib.sha256` over de actuele bestanden — **5/5 exact gelijk** aan de getoonde hashes. Geen drift tussen vermelde en feitelijke inhoud.
- Padding-conventie: paden zijn relatief (file-basenames zonder directory-prefix). Begrijpelijk in context (het bestand staat in `output/verification/` maar bevat een mix van paden uit `dashboard/` en `output/reports/`); een toekomstig verbeterpunt zou zijn om óf paden vanaf repo-root te tonen óf het bestand op te splitsen per directory. Geen blokkerende afwijking.

---

## Conclusie

**Go**. Alle zes checks slagen zonder blokkerende afwijkingen. De v4.6.0 dashboard-inhaalslag-artefacten zijn aanwezig, intern consistent (JS-payload = JSON-payload, hashes match feitelijke inhoud), en de patchnotitie documenteert de v2→v3 build-script-deltas expliciet.

**Aandachtspunten voor masterchat (niet-blokkerend, ter informatie)**

1. JS-wrapper gebruikt `window.GRC_DATA` (niet `window.grcData` zoals in subagent-config-voorbeeld). Functioneel ongelijk gevolg zolang `grc-explorer-v*.html` dezelfde naam consumeert; verifiëren of HTML-laag (buiten deze validatie-scope) consistent is met `GRC_DATA`.
2. SKOS-rapport-structuur (C1–C5 + aandachtspunten + kanttekening) wijkt af van het §1–§6-template in `.claude/agents/dashboard.md`. Inhoudelijk dekkend, maar overweging: ofwel template aanpassen aan de daadwerkelijk gehanteerde structuur, ofwel toekomstige SKOS-rapporten conform §1–§6 brengen.
3. `file_hashes_dashboard_v4_6_0.txt` bevat paden zonder directory-prefix terwijl de gehashte files in twee verschillende mappen leven (`dashboard/` en `output/reports/`). Klein leesbaarheids-/reproduceerbaarheids-puntje voor latere hash-bestanden.
4. Geen `grc-explorer-v4_6_0.html` aangetroffen in `dashboard/` — alleen `grc-explorer.html` (32 KB, mtime 2026-05-21) en `grc-explorer-v2.html` (40 KB, mtime 2026-05-21). Volgens subagent-conventie ("Versie-suffix verplicht voor alle drie bestanden") zou een `grc-explorer-v4_6_0.html` verwacht zijn. Buiten de zes opgedragen checks, maar opvallend genoeg om hier te noemen — masterchat kan besluiten of een v4.6.0-HTML-shell alsnog gevraagd wordt of dat de bestaande HTML's bewust naamloos-versie blijven.

— Einde rapport
