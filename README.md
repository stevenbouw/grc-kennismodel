# GRC Kennismodel — v4.5.0 Eindoplevering

**Sprint:** v4.5.0 Fase 3 (M21 NIST CSF 2.0)
**Datum oplevering:** 19 mei 2026
**Basis:** v4.4.0-baseline (13 mei 2026)
**Status:** masterchat-eindreview pending

> **NB**: Dit is **v4.5.0**, niet v4.6.0. v4.6.0 = Fase 4 (M15-ENSIA + volwassenheidsmodel) is gepland conform projectinstructie v1.7 maar nog niet gebouwd.

---

## Eindcijfers (uit `verification/canonical_metrics_v4.5.0.json`)

| Metric | v4.4.0 | **v4.5.0** | Δ |
|---|---:|---:|---:|
| Pre-inferentie triples | 13.441 | **19.340** | +5.899 (+43,9%) |
| Post-inferentie triples (OWL RL) | 31.415 | **41.988** | +10.573 |
| Klassen | 189 | **193** | +4 |
| NamedIndividuals | 679 | **1.179** | +500 |
| ObjectProperties | 143 | **146** | +3 |
| DatatypeProperties | 93 | **94** | +1 |
| owl:sameAs | 98 | **98** | 0 (D5 + D11 ongewijzigd) |
| SKOS-mappings | 346 | **1.794** | +1.448 |
| Namespaces (D3-revisie) | 10 | **11** | +1 (`csf:`) |
| Modules (.ttl) | 22 | **23** | +1 (m21-csf.ttl NIEUW) |
| owl:Nothing post-inferentie | 0 | **0** ✓ | consistent |
| SHACL violations RUN 1 | 0 | **0** ✓ | conform |
| SHACL violations RUN 2 | 290 | **290** ✓ | identiek (bekende false-positives) |

Sprint-omvang: **~8,5× v4.4.0**.

---

## Structuur van deze oplevering

```
grc-kennismodel-v4_5_0/
├── README.md                   ← dit bestand
├── ontology/                   ← 22 .ttl-modules + 1 SPARQL-demo (de feitelijke ontologie)
│   ├── grc-core.ttl            ← root-ontologie (v4.5.0; D3 11 namespaces)
│   ├── grc-bridges.ttl         ← cross-module bridges
│   ├── grc-shacl.ttl           ← SHACL-shapes
│   ├── m01-framework.ttl       ← frameworks-individuals (incl. fw:NIST_CSF_2_0)
│   ├── m02-control.ttl         ← ISO 27002 controls (incl. D6 v1.x→v2.0-update)
│   ├── m03-risk.ttl … m18-assets.ttl  ← overige modules
│   ├── m21-csf.ttl             ← NIEUW: NIST CSF 2.0 Core + IEs + SKOS
│   └── m18-demo-sparql.rq      ← demo-query asset-module
├── verification/               ← reproduceerbare verificatie
│   ├── canonical_metrics_v4_5_0.py
│   ├── canonical_metrics_v4.5.0.json
│   ├── shacl_split_validate_v4_5_0.py
│   ├── shacl_results_v4.5.0.json
│   └── file_hashes_v4_5_0.txt  ← SHA256 alle 22 .ttl
├── reports/                    ← documentatie deze sprint
│   ├── patch-rapport-v4_5_0.md ← hoofdrapport (321 regels, 13 secties)
│   ├── inventarisatie-fase-3-precheck-v4_4_0.md  ← Stap 1 pre-sprint
│   └── concept-mapping-tabel-stap7-v4_5_0.md     ← Stap 7-preview (review-input)
└── build-scripts/              ← tooling die de ABox heeft gebouwd
    ├── csf_extract.py          ← CSWP 29 → JSON
    ├── stap3_build_ttl.py      ← Functions/Categories/Subcategories
    ├── stap4_build_ttl.py      ← Implementation Examples
    ├── stap5_build_ttl.py      ← Sheet 8 SKOS-mappings
    └── stap6_build_ttl.py      ← CSF Reference Tool IR-mappings
```

---

## Hoofd-toevoegingen v4.5.0

| Component | Aantal | Locatie |
|---|---:|---|
| CSF Functions | 6 | m21-csf.ttl |
| CSF Categories | 22 | m21-csf.ttl |
| CSF Subcategories | 106 | m21-csf.ttl |
| CSF Implementation Examples | 363 | m21-csf.ttl |
| skos:closeMatch CSF → ISO 27001/27002/BIO | 1.435 | m21 (sheet 8) + m08/m09/m11 (Reference Tool) |
| skos:relatedMatch CSF → COSO/COBIT | 13 | m17-coso-cobit.ttl |
| SourceAttribution-individuals (nieuw) | 2 | m21-csf.ttl |
| Mapping-coverage CSF Functions / Categories / Subcategories | **6/6 / 22/22 / 106/106 (100%)** | — |

---

## Reproduceren

```bash
cd verification/
python3 canonical_metrics_v4_5_0.py      # → canonical_metrics_v4.5.0.json
python3 shacl_split_validate_v4_5_0.py   # → shacl_results_v4.5.0.json
sha256sum -c file_hashes_v4_5_0.txt      # → moet OK rapporteren
```

Vereist: `rdflib >= 7.0`, `owlrl >= 7.0`, `pyshacl >= 0.25`. Workdir bij run = `ontology/`.

---

## Cross-bron-overlap-kwaliteits-indicator

Sheet 8 (ADR & NOREA CC-BY 4.0) en NIST CSF Reference Tool (Public Domain) leggen **105 keer dezelfde ISO 27001-mapping**. Twee onafhankelijke bronnen → bron-consistentie-bewijs voor SKOS-correctheid. Zie `reports/patch-rapport-v4_5_0.md` §8 punt 14.

---

## Volgende stappen (na masterchat-eindreview-GO)

1. **Brain-vault-update**: sprint-record v4.5.0, D3-revisie-bevestiging, 3 nieuwe H-items (H33/H34/H35)
2. **Projectinstructie v1.8**: methodologische leerpunten (zie patch-rapport §8 punten 1–6)
3. **v4.6.0 Fase 4** (toekomst): M15-ENSIA-uitbouw + volwassenheidsmodel — eerst evalueren of hergebruik van `biz:MaturityAssessment` zinvol is voor nieuwe `isms:MaturityAssessment`

---

*Workdir-state ten tijde van zip-creatie: `/home/claude/v433/`. Voor reproductie via filesystem: kopieer `ontology/` naar werkdirectory.*
