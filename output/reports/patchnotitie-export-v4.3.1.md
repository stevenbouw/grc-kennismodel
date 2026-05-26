# Export patchnotitie — v4.3.0 → v4.3.1
**Script:** `build_grc_explorer_v2.py` (ongewijzigd — alleen herrun op nieuwe snapshot)
**Datum:** 20 april 2026
**Basis:** v4.3.1-snapshot (20 TTL-bestanden, 12.681 triples)
**Source hash (SHA256, gecombineerd):** `da62d483e45e757cd31f294a11610439...`
*Per-bestandshashes: zie `file_hashes.txt` v4.3.1 (geproduceerd door technische chat)*

---

## Bevestiging vier patchpunten

**(a) 186 extra `rdfs:label`-triples zichtbaar** — de export telt nu 2.344 `rdfs:label`-triples (v4.3.0: 2.046, delta +298). De 298 nieuwe labels bestaan uit 102 @nl en 196 @en, waarvan de 186 control-EN-labels het grootste blok vormen (toegevoegd via besluit B/B₂ in v4.3.1). Nulcontrole H4: 0 nodes met IRI-fragment als fallback-label (onveranderd correct).

**(b) 7 extra HSClause-nodes aanwezig** — `ext:HSClause`-individuals zijn nu vindbaar als nodes in laag 9 (ISMS/Bedrijf/Overig), conform hun `ext:`-namespace. Alle 7 gedeclareerd met `rdfs:label@nl`: HSClause_4_Context, _5_Leadership, _6_Planning, _7_Support, _8_Operation, _9_PerformanceEvaluation, _10_Improvement. Totaal individuals: 1.043 (v4.3.0: 1.036, +7).

**(c) SoAEntry_5_02 afkappingsbug opgelost** — label is nu volledig: `"SoA-entry: Rollen en verantwoordelijkheden bij informatiebeveiliging"@nl` en `"SoA entry: Information security roles and responsibilities"@en`. In v4.3.0 was dit label afgekapt door een duplicate-triple-conflict (besluit B₂); dat is gecorrigeerd.

**(d) Geen nieuwe export-anomalieën** — governance-graaf stabiel (147 edges, alle 10 properties actief), SKOS-count ongewijzigd (307 individual-niveau, 346 model-totaal), equivalence-count ongewijzigd (93). Triple-count 12.681 sluit exact aan op canonical metrics v4.3.1.

---

## Delta-overzicht v4.3.0 → v4.3.1

| Metric | v4.3.0 | v4.3.1 | Delta |
|---|---:|---:|---:|
| Triples geladen | 12.354 | **12.681** | +327 |
| Individuals (nodes) | 1.036 | **1.043** | +7 |
| rdfs:label totaal | 2.046 | **2.344** | +298 |
| Edges totaal | 3.671 | **3.712** | +41 |
| Governance-edges | 147 | **147** | 0 |
| SKOS-edges | 307 | **307** | 0 |
| Equivalence-edges | 93 | **93** | 0 |

---

**Werkpakket H1–H8 formeel gesloten.**
Stand-by tot UI-modernisering wordt geactiveerd.
