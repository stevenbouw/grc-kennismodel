---
type: index
id: sprint-register
title: Sprint-register — Chronologisch overzicht
status: living
date: 2026-05-28
---

# Sprint-register — Chronologisch overzicht

Ontologie-evolutie van v0.x tot v4.6.3. **T1 is eerste post-migratie productie-sprint** (26 mei 2026); **T2 is tweede post-migratie productie-sprint** (27 mei 2026); **T3 is derde post-migratie productie-sprint** (28 mei 2026). v4.6.0 was laatste geplande Spoor A-sprint vóór migratie naar Claude Code + GitHub.

## Major milestones

| Sprint | Datum | Status | Belangrijkste inhoud |
|---|---|---|---|
| v0–v1 | initieel | superseded | Initiële fase (skelet-only) |
| v2.0 | 2026-02 | superseded | Fix-release, D5 sameAs ctrl:↔bio: vastgelegd |
| v3.0 | 2026-03 | superseded | Monolithisch model |
| v4.0.0 | 2026-03-27 | superseded | Modulaire split (22 bestanden) |
| v4.1.0-alpha | 2026-04-10 | superseded | Werkpakket-opschoning + D6 meeliftregel (Actie G) + BBN-consolidatie (Actie A) |
| v4.2.0 | 2026-04-13 | superseded | M18 asset-module + 10e namespace + ReportingRisk + TBB ConceptScheme |
| v4.2.2 | 2026-04-13 | superseded | SoA-canonisering Route A — D8 vastgelegd |
| v4.3.0 | 2026-04-13 | superseded | Gap-sprint D11 asset-convergentie + 5 sameAs-bruggen |
| v4.3.1 | 2026-04-20 | superseded | Patch-bump H18/H22 + B₂ SoAEntry-label-fix + §10.2-meetcorrectie |
| v4.3.2 | 2026-04-21 | superseded | Smart-quotes, ext:NIS2Requirement-asymmetrie hersteld |
| v4.3.3 | 2026-04-22 | superseded | D12 drie-laags-compliance + predicate-consolidatie α |
| v4.4.0 | 2026-05-13 | superseded | Fase 2: CBW + Cbb + UV-decompositie + Sheet 9 + 3 nieuwe klassen + 3 nieuwe properties |
| v4.5.0 | 2026-05-19 | superseded | Fase 3: M21 NIST CSF 2.0 + D3-revisie naar 11 namespaces + 1.448 SKOS-mappings + 8 modules gewijzigd |
| v4.6.0 | 2026-05-21 | superseded | Fase 4: M15-ENSIA-uitbouw + Volwassenheidsmodel (isms-cluster naast biz) + CSF Tiers + 5 modules gewijzigd |
| T1 (v4.6.1) | 2026-05-26 | superseded | SKOS-kwaliteitsanalyse Fase 1 — H36-cluster (28× exactMatch → broadMatch) in m10-nis2-ext; methode-protocol v1.0 vastgesteld; eerste post-migratie productie-sprint |
| T2 (v4.6.2) | 2026-05-27 | superseded | SKOS-bidirectional-audit m10 — 65 mutaties (32 downgrade + 33 upgrade) over 10 NIS2-clusters; alle clusters convergeren naar broadMatch; methode-protocol v1.2 operationeel; v1.3-draft opgeleverd; H41 nieuw + H36 m10-component closed; tweede post-migratie productie-sprint |
| **T3 (v4.6.3)** | **2026-05-28** | **active** | **SKOS-bidirectional-audit m14 AVG/GDPR — 2 mutaties (T3-001 + T3-002, beide broadMatch → relatedMatch op Art5_1f-cluster); 29 behoud + 2 closeMatch (T3-014 + T3-026 retrieval-interchangeability); Protocol v1.3 FINAL toegepast; cross-category-rationale als kandidaat v1.3.1-precedent; H36 fully closed; H39 versterkt bidirectional; derde post-migratie productie-sprint** |

## Detail per sprint

| Sprint | File |
|---|---|
| v0–v1 | [[brain__sprints__v0-v1_initiele-fase]] |
| v2.0 | [[brain__sprints__v2_0_fix-release]] |
| v3.0 | [[brain__sprints__v3_0_monolithisch]] |
| v4.0.0 | [[brain__sprints__v4_0_0_modulaire-split]] |
| v4.1.0-alpha | [[brain__sprints__v4_1_0-alpha_werkpakket-opschoning]] |
| v4.2.0 | [[brain__sprints__v4_2_0_M18-asset-module]] |
| v4.2.2 | [[brain__sprints__v4_2_2_soa-canonisering-route-a]] |
| v4.3.0 | [[brain__sprints__v4_3_0_gap-sprint-d11]] |
| v4.3.1 | [[brain__sprints__v4_3_1_patch-bump]] |
| v4.3.2 | [[brain__sprints__v4_3_2_smart-quotes-en-asymmetrie]] |
| v4.3.3 | [[brain__sprints__v4_3_3_d12-en-predicate-consolidatie]] |
| v4.4.0 | [[brain__sprints__v4_4_0_fase-2-cbw-cbb]] |
| v4.5.0 | [[brain__sprints__v4_5_0_fase-3-nist-csf-2-0]] |
| v4.6.0 | [[brain__sprints__v4_6_0_fase-4-ensia-en-volwassenheid]] |
| T1 (v4.6.1) | [[brain__sprints__T1_skos-kwaliteitsanalyse-fase-1]] |
| T2 (v4.6.2) | [[brain__sprints__T2-skos-bidirectional-audit-m10]] |
| **T3 (v4.6.3)** | **[[brain__sprints__T3-skos-bidirectional-audit-m14]]** |

## v4.6.3 baseline-metrics (huidige active — patch-release na T3)

Cijfers per patch-rapport v4.6.3 §0.1, gemeten op `canonical_metrics_v4_6_3.json`.

| Metric | Waarde | Δ t.o.v. v4.6.2 |
|---|---:|---:|
| Pre-inferentie triples | 20.950 | 0 |
| Post OWL RL | 44.907 | 0 |
| Klassen | 199 | 0 |
| NamedIndividuals | 1.383 | 0 |
| ObjectProperties | 149 | 0 |
| DatatypeProperties | 96 | 0 |
| owl:sameAs | 98 | 0 |
| SKOS-mappings | 1.798 | 0 |
| — `skos:exactMatch` | 18 | 0 |
| — `skos:closeMatch` | 1.457 | 0 |
| — `skos:broadMatch` | 129 | **−2** |
| — `skos:relatedMatch` | 194 | **+2** |
| — `skos:narrowMatch` | 0 | 0 |
| Namespaces | 11 | 0 |
| Modules | 22 (1 gewijzigd: m14-avg-gdpr) | 0 |
| SHACL SECTIE A / SECTIE B / COMBINED | 0 / 0 / 290 | 0 / 0 / 0 |

**Predicate-substitutie zonder triple-totaal-impact** — 2 mappings van predicate veranderd in `m14-avg-gdpr.ttl` (beide compl:AVG_Art5_1f broadMatch → relatedMatch op ctrl:ISO27002_5_01 + ISO27002_5_12). m14-eindstand compl→ctrl: exact 0 / close 2 / broad 0 / narrow 0 / related 29. m14-hash `47daeb7e…` → `874565ba…`; 21 andere modules + `grc-shacl.ttl` byte-identiek aan v4.6.2.

### v4.6.2 baseline-metrics (vorige active — patch-release na T2)

| Metric | Waarde | Δ t.o.v. v4.6.1 |
|---|---:|---:|
| Pre-inferentie triples | 20.950 | 0 |
| Post OWL RL | 44.907 | 0 |
| Klassen | 199 | 0 |
| NamedIndividuals | 1.383 | 0 |
| ObjectProperties | 149 | 0 |
| DatatypeProperties | 96 | 0 |
| owl:sameAs | 98 | 0 |
| SKOS-mappings | 1.798 | 0 |
| — `skos:exactMatch` | 18 | 0 |
| — `skos:closeMatch` | 1.457 | **−32** |
| — `skos:broadMatch` | 131 | **+65** |
| — `skos:relatedMatch` | 192 | **−33** |
| — `skos:narrowMatch` | 0 | 0 |
| Namespaces | 11 | 0 |
| Modules | 22 (1 gewijzigd: m10-nis2-ext) | 0 |
| SHACL SECTIE A / SECTIE B / COMBINED | 0 / 0 / 290 | 0 / 0 / 0 |

**Predicate-substitutie zonder triple-totaal-impact** — 65 mappings van predicate veranderd in `m10-nis2-ext.ttl` (32 closeMatch → broadMatch + 33 relatedMatch → broadMatch). m10-eindstand ctrl→compl: exact 0 / close 0 / broad 118 / narrow 0 / related 0.

### v4.6.1 baseline-metrics (vorige active — patch-release na T1)

| Metric | Waarde | Δ t.o.v. v4.6.0 |
|---|---:|---:|
| Pre-inferentie triples | 20.950 | 0 |
| Post OWL RL | 44.907 | 0 |
| Klassen | 199 | 0 |
| NamedIndividuals | 1.383 | 0 |
| ObjectProperties | 149 | 0 |
| DatatypeProperties | 96 | 0 |
| owl:sameAs | 98 | 0 |
| SKOS-mappings | 1.798 | 0 |
| — `skos:exactMatch` | 18 | **−28** |
| — `skos:broadMatch` | 66 | **+28** |
| Namespaces | 11 | 0 |
| Modules | 22 (1 gewijzigd: m10-nis2-ext) | 0 |
| SHACL RUN 1 / RUN 2 | 0 / 290 | 0 / 0 |

**Predicate-mutatie zonder triple-totaal-impact** — 28 mappings van `exactMatch` naar `broadMatch` in `m10-nis2-ext.ttl`.

### v4.6.0 baseline-metrics (vorige active — gewijzigd 21 mei 2026)

| Metric | Waarde | Δ t.o.v. v4.5.0 |
|---|---:|---:|
| Pre-inferentie triples | 20.950 | **+1.610 (+8,3%)** |
| Post OWL RL | 44.907 | +2.919 |
| Klassen | 199 | +6 (5 isms + 1 csf) |
| NamedIndividuals | 1.383 | **+204** |
| ObjectProperties | 149 | +3 |
| DatatypeProperties | 96 | +2 |
| owl:sameAs | 98 | 0 |
| SKOS-mappings | 1.798 | +4 |
| Namespaces | 11 | 0 |
| Modules | 22 (5 gewijzigd) | 0 |

## Sprint-multiplier-mijlpalen

| Sprint | Pre-inf Δ triples | Multiplier t.o.v. v4.4.0 |
|---|---:|---:|
| v4.3.3 | +52 | 0,07× |
| v4.4.0 | +702 | 1× (referentie) |
| v4.5.0 | +5.899 | 8,5× |
| v4.6.0 | +1.610 | 2,7× |
| T1 (v4.6.1) | 0 | 0× (kwaliteits-sprint — predicate-substitutie, 28 mutaties) |
| T2 (v4.6.2) | 0 | 0× (kwaliteits-sprint — predicate-substitutie, 65 mutaties) |
| **T3 (v4.6.3)** | **0** | **0× (kwaliteits-sprint — predicate-substitutie, 2 mutaties)** |

v4.6.0 onder oorspronkelijke prognose (5-7×) dankzij hergebruik bestaande m15-structuur en pre-sprint-discipline. T1 + T2 + T3 zijn kwaliteits-sprints (predicate-substitutie binnen behouden SKOS-totaal van 1.798) — triple-multiplier 0× is conform sprint-type. T2-mutatie-multiplier t.o.v. T1: 2,32× (65/28). **T3-mutatie-multiplier t.o.v. T2: 0,03×** (2/65) — smal mutatie-spectrum maar breed methodisch leerpunt (cross-category-principe als kandidaat v1.3.1-precedent). Per patch-rapport v4.6.3 §8.

## Cross-references naar D-decisions

| Sprint | D vastgelegd | D verfijnd / toegepast |
|---|---|---|
| v2.0 | D5 (sameAs ctrl:↔bio:) | — |
| v4.0.0 | — | D1, D2 toegepast |
| v4.1.0-alpha | D6 (meeliftregel) | — |
| v4.2.0 | D3 (10 namespaces, +asset:) | D7 (BIO 2.0 klassen) |
| v4.2.2 | D8 (canonieke SoA) | — |
| v4.3.0 | D11 (asset-convergentie) | — |
| v4.3.3 | D12 (drie-laags-compliance) | — |
| v4.4.0 | — | D9 cluster 1+2, D12 verfijning, D6 vertaling-scope v1.7 |
| v4.5.0 | — | D3 uitbreiding (csf:), D9 cluster 3 (CSF Optie B), D6 m02-toepassing |
| v4.6.0 | — | D6 symmetrische uitbreiding v1.9 (CSF Tier @en-only), D9 cluster 4 (ENSIA) |
| T1 (v4.6.1) | — | D4 conformance-verbetering (exactMatch was te sterk geclaimd voor 28 ctrl:↔compl:-paren; ENISA-disclaimer-categorisch-effect); D4.1 vastgesteld 27 mei 2026 |
| T2 (v4.6.2) | — | D4.1 toepassings-precedent uitgebreid naar cluster-niveau (118 paren over 10 m10-clusters; één D4.1-bevestiging per homogene cluster); D4-bidirectional bewijs op productie-schaal |
| **T3 (v4.6.3)** | — | **D4 cross-category-rationale als toepassings-precedent (control ↔ legal-obligation = associatief, niet subsumptief) op 31 m14-paren over 5 AVG-clusters; D4.1 inactief in T3 (bindende T3-steer 1; AVG = publiek EU-recht); closeMatch-uitzondering op retrieval-interchangeability methodologisch consistent toegepast (T3-014 + T3-026)** |

## Geplande sprints

| Sprint | Datum | Voorgenomen scope |
|---|---|---|
| T4 | TBD (verse masterchat-sessie post-T3) | SKOS-kwaliteitsanalyse vervolg — kandidaten: cross-bron-overlap-105-paren (v4.5.0), m17 COSO/COBIT, m11 NIST SP 800-53, m09 ISO 27001, m16 VIRBI, m12 DORA, framework-niveau SKOS (fw:↔fw:) |
| Protocol v1.3.1-Brein-cyclus | TBD | Formalisering cross-category-mappings-principe als §3.4 of §3.3-aanvulling op SKOS-beoordelings-protocol (T3-leerpunt; kandidaat-precedent) |

## Sprint-protocollen die zijn ontstaan / verfijnd per sprint

Cumulatief sinds v4.4.0. Geformaliseerd in projectinstructie v1.7 (basis), v1.8 (uitbreiding), v1.9 (vier nieuwe).

| Protocol | Sprint-bron |
|---|---|
| Protocol B — Pre-sprint-inventarisatie | v4.4.0 + cumulatief |
| Bron-verificatie vóór TBox-declaratie | v4.4.0 |
| Bron-verificatie vóór raming-opstelling | v4.5.0 |
| Bron-bereikbaarheid in uitvoerings-omgeving | v4.5.0 |
| Precedent-discipline bij nieuw framework-cluster | v4.5.0 |
| Raming-discipline bij aggregatie-mappings | v4.4.0 + v4.5.0 |
| Patch-rapport §9 verplicht | v4.4.0 |
| Brain-vault-update verplicht na elke minor-release | v1.8 |
| **Pre-sprint multi-module-discipline** (v1.9) | v4.6.0 §8.1 |
| **Ramings-baseline rdf:type-dubbele-telling** (v1.9) | v4.6.0 §8.4 |
| **Instructie-consistentie code-block vs toelichting** (v1.9) | v4.6.0 §8.2 |
| **Bron-typo-beleid patroon-criterium** (v1.9) | v4.6.0 §8.6 |
| **Pre-push disclosure-check** (Protocol 14) | iteratie 12 |
| **Tech levert werkbare applier** (Protocol 15) | T1 §8 leerpunt 5 |
| **Lokatie verificatie-scripts in patch-rapport** (Protocol 16) | T1 §8 leerpunt 6 |
| **NEN-werkverdeling Tech↔Masterchat** (Protocol 17) | T1 §8 leerpunt 4 |

## Cross-references

- [[brain__decisions__D-register]] — gerelateerde D-decisions
- [[brain__architecture__H-register]] — H-items per sprint ontstaan
- [[brain__index]] — masterindex met huidige baseline
- [[brain__workflow__sprint-protocollen]] — sprint-protocollen volledig

— Einde sprint-register.
