---
type: index
id: brain-index
title: GRC Kennismodel Brain — Masterindex
status: living
date: 2026-05-28
---

# GRC Kennismodel Brain — Masterindex

Karpathy-conforme "LLM Wiki" voor het GRC Kennismodel-project. Inhoud-gedreven, append-only logbook, type-getagged frontmatter, wikilinks als grep-anchors. Ontworpen voor menselijke navigatie en voor LLM-retrieval via Project Knowledge én Claude Code (post-migratie).

## Vault-staat — 15 iteraties voltooid

| Iteratie | Datum | Inhoud | Files |
|---|---|---|---:|
| 0 | 2026-05-13 | Vault-foundation + D9 canoniek voorbeeld | 4 |
| 1 | 2026-05-13 | D-decisions D1–D12 + register | 13 |
| 1.5 | 2026-05-13 | Archeologie-rapport | 1 |
| 2 | 2026-05-13 | Sprint-files v0.x → v4.3.3 + register | 12 |
| 3 | 2026-05-13 | H-items + H-register + D-correcties | 11 |
| 4 | 2026-05-13 | Concepts (domein-glossary) + register | 10 |
| 5 | 2026-05-13 | Module-files M01-M18 + M21-stub + register | 20 |
| 6 | 2026-05-13 | Sources + Workflow + Scope + 3 registers | 19 |
| 7 | 2026-05-13 | Index-update + smoke-tests + log-update | 3 |
| 8 | 2026-05-13 | Migratie-prep (CLAUDE.md, guide, script) + 2 future-concepts | 7 |
| 9 | 2026-05-13 | v1.7-update: v4.4.0 baseline + 3 D-updates + H32 + module/source/workflow-updates | 21 (in 2 batches) |
| 10 | 2026-05-19 | v4.5.0-update: Fase 3 NIST CSF 2.0 + D3-uitbreiding + 3 nieuwe H-items + nieuw cross-bron-overlap-concept | 25 (in 2 batches) |
| 11 | 2026-05-21 | v4.6.0-update + v1.9: Fase 4 ENSIA + Volwassenheidsmodel + parallelle-maturity-clusters concept | 20 (in 2 batches) |
| 12 | 2026-05-26 | Post-v4.6.0 polish-mini-sprint: H36-H40 (parked) + Protocol 14 pre-push-disclosure + dashboard-productlijnen-concept | 13 (6 nieuw + 7 update) |
| 13 | 2026-05-26 | Post-T1-Brein-cyclus: T1-sprint registreren + methode-protocol-concept + mapping-bron-disclaimer-effect-concept + H36 closed + H39 versterkt + Protocollen 15/16/17 formeel | 11 (3 nieuw + 8 update) |
| 14 | 2026-05-27 | Post-T2-Brein-cyclus: T2-sprint registreren + cluster-discipline-bewijslast-concept + H41 nieuw + H36 m10-component closed (m14 open subtask) + H39 versterkt T2 + D4.1-cluster-niveau-precedent + Protocol v1.3-draft-status documenteren + bidirectional-audit-symmetrie als sub-aspect | 13 (3 nieuw + 10 update) |
| **15** | **2026-05-28** | **Post-T3-Brein-cyclus: T3-sprint registreren + cross-category-mappings-concept (kandidaat v1.3.1-precedent) + commit-push-werkverdeling-workflow (masterchat-commit-autonomie) + H36 fully closed (m14 afgehandeld) + H39 versterkt T3 bidirectional + H41 T3-bevestiging informatief + Protocol v1.3 FINAL-status + M14 SKOS-distributie post-patch + errata-correctie t3-stap3-eindrapport + patch-rapport-v4.6.3** | **14 (3 nieuw + 11 update)** |
| **Totaal brain-bestanden** | | | **~115** |

Plus ±20 bron-documenten als upload (patch-rapporten incl. v4.6.1 + v4.6.2 + v4.6.3, projectinstructie v1.9 + v1.10, T2/T3-rapporten, ontologie-PDFs).

## Folder-structuur

Project Knowledge is flat — folder-structuur is **gecodeerd in de bestandsnaam** via `__`-separator:

```
brain__CLAUDE.md                              ← vault-spec (claude.ai)
CLAUDE.md                                     ← Claude Code-anchor (post-migratie)
brain__index.md                               ← dit document
brain__log.md                                 ← chronologisch logboek
brain__archeology-report.md                   ← iteratie-1.5 fundament
brain__smoke-tests.md                         ← vault-functionaliteit-tests
brain__obsidian-migration-guide.md            ← migratie-stappenplan (iteratie 8)

brain__decisions__D{NN}_{slug}.md            ← 12 D-decisions
brain__sprints__v{X_Y_Z}_{slug}.md          ← 17 sprint-files (incl. v4.6.0 + T1 iteratie 13 + T2 iteratie 14 + T3 iteratie 15)
brain__architecture__H{NN}_{slug}.md         ← 17 H-items (H36 fully closed iteratie 15; H41 parked T3-bevestiging informatief)
brain__concepts__{slug}.md                   ← 19 concept-files (incl. cross-category-mappings iteratie 15 — kandidaat v1.3.1-precedent)
brain__modules__M{NN}_{slug}.md              ← 19 modules (M14 SKOS-distributie post-T3 toegevoegd)
brain__sources__{slug}.md                    ← 8 source-files (5 SourceAttributions in model)
brain__workflow__{slug}.md                   ← 7 workflow-files (incl. commit-push-werkverdeling iteratie 15)
brain__scope__{slug}.md                      ← 4 bewust-uitgesloten elementen
```

## Status-overzicht ontologie v4.6.3 (huidige baseline — patch-release na T3)

| Metric | Waarde | Δ t.o.v. v4.6.2 |
|---|---:|---:|
| Versie | **v4.6.3** | — |
| Datum | 2026-05-28 | — |
| Modules | 19 active + 0 stub | 0 (1 module gewijzigd: m14-avg-gdpr) |
| Pre-inferentie triples | 20.950 | 0 |
| Post-OWL-RL triples | 44.907 | 0 |
| Klassen | 199 | 0 |
| NamedIndividuals | 1.383 | 0 |
| ObjectProperties | 149 | 0 |
| DatatypeProperties | 96 | 0 |
| `owl:sameAs` | 98 (93 D5 + 5 D11) | 0 |
| **SKOS-mappings totaal** | **1.798** | **0** |
| — `skos:exactMatch` | 18 | 0 |
| — `skos:closeMatch` | 1.457 | 0 |
| — `skos:broadMatch` | 129 | **−2** |
| — `skos:relatedMatch` | 194 | **+2** |
| — `skos:narrowMatch` | 0 | 0 |
| Namespaces | 11 | 0 |
| SHACL SECTIE A | 0 violations | 0 |
| SHACL SECTIE B | 0 violations | 0 |
| SHACL COMBINED | 290 false-positives | 0 (identiek aan v4.6.2-baseline) |

**Predicate-substitutie zonder triple-totaal-impact** — T3-sprint patcht alleen predicates van 2 compl:↔ctrl:-mappings in `m14-avg-gdpr.ttl` (beide compl:AVG_Art5_1f broadMatch → relatedMatch op ctrl:ISO27002_5_01 + 5_12). m14-eindstand compl→ctrl: exact 0 / close 2 / broad 0 / narrow 0 / related 29. Eén module hash gewijzigd (`47daeb7e…` → `874565ba…`); 21 andere modules + `grc-shacl.ttl` byte-identiek aan v4.6.2.

## v4.6.3 wijzigingen — kort (T3-sprint)

Eén module gewijzigd: `m14-avg-gdpr.ttl`. 2× SKOS-predicate-substitutie (downgrade broadMatch → relatedMatch) op Art5_1f-cluster (T3-001 + T3-002) via directe instructie-uitvoering masterchat-besluit Optie C op pilot-escalatie. 27 behoud relatedMatch + 2 behoud closeMatch (T3-014 + T3-026 op retrieval-interchangeability). Protocol v1.3 DRAFT → **FINAL** vastgesteld door masterchat 28 mei 2026 tijdens T3-scoping. Cross-category-rationale (control ↔ legal-obligation = associatief, niet subsumptief) als T3-leerpunt + **kandidaat v1.3.1-precedent** vastgelegd in nieuw concept [[brain__concepts__cross-category-mappings]] (formalisering = masterchat-werk). H36 **fully closed** (cumulatief 149 ctrl:↔compl:-paren over T1+T2+T3). H39 versterkt bidirectional (T3 bevestigt blinde-vlek op compl→ctrl). H41 informatief uitgebreid (eerste cross-category-bewijs Δ post-OWL-RL = 0). D4.1 inactief in T3-context (AVG = publiek EU-recht). Werkflow-wijziging: masterchat mag voortaan zelf committen + pushen — subagents NOOIT zelfstandig (invariant). Zie [[brain__workflow__commit-push-werkverdeling]].

### v4.6.2 vorige baseline (T2-sprint, 27 mei 2026)

Eén module gewijzigd: `m10-nis2-ext.ttl`. 65× SKOS-predicate-substitutie (32 downgrade + 33 upgrade) voor m10 ctrl:↔compl:-paren over 10 NIS2-art.21-letter-clusters op basis van [[brain__concepts__skos-beoordelings-protocol]] v1.2 (bidirectional). Evidence-niveau 1 op cluster-niveau via CBW-Mapping-UV (reproductie ENISA TIG v1.0). D4 + D4.1-conformance op cluster-niveau-toepassings-precedent uitgebreid. Methode-protocol v1.3 als DRAFT opgeleverd. H41 nieuw geregistreerd (parked, SKOS-axioma-set-handling). H36 m10-component closed (m14 open subtask). H39 versterkt op 118-paren-schaal.

### v4.6.1 vorige baseline (T1-sprint, 26 mei 2026)

Eén module gewijzigd: `m10-nis2-ext.ttl` (hash `78b8ee44...` → `cb2d567b...`). 28× herclassificatie `skos:exactMatch` → `skos:broadMatch` voor ctrl:↔compl:-paren (H36-cluster) op basis van methode-protocol v1.0. D4-conformance verbeterd; D4.1 vastgesteld 27 mei 2026. Drie sprint-protocollen 15/16/17 geformaliseerd uit T1-leerpunten.

### v4.6.0 vorige baseline (gewijzigd 21 mei 2026 — Fase 4)

5 modules gewijzigd: grc-core (versie-bump), M01 (fw:ENSIA als GRCFramework), M06 (volwassenheidsmodel-cluster), M15 (oude fw:Guideline-blok verwijderd), M21 (CSFTier + Tier↔Level mappings). Volwassenheidsmodel-cluster als nieuwe isms-cluster naast biz:MaturityAssessment-cluster (NIET samenvoegen). ENSIA gepromoot naar fw:GRCFramework (D9 vierde verificatie-cluster). 5 SourceAttributions in model (+2: NBA-LIO-NOREA + ENSIA-Logius). Vier nieuwe sprint-protocollen formeel in projectinstructie v1.9.

## Volgende fase — Productie-fase actief (T1 + T2 + T3 voltooid; H36 fully closed)

v4.6.0 was laatste geplande Spoor A-sprint voor Fase 1-4 scope. Migratie naar Claude Code + GitHub voltooid via Fase 0 + polish-mini-sprint (iteratie 12). **T1-sprint (v4.6.1, 26 mei 2026)** + **T2-sprint (v4.6.2, 27 mei 2026)** + **T3-sprint (v4.6.3, 28 mei 2026)** zijn eerste, tweede en derde post-migratie productie-sprints — werkflow volledig gevalideerd op single-cluster (T1), productie-schaal multi-cluster (T2) én cross-category (T3).

Status iteratie 15:
- ✓ Master-handover-document v1.0 in PK
- ✓ docs/sprint-protocols.md uitgebreid (v1.0 → v1.3 met Protocollen 14/15/16/17 + werkflow-discipline)
- ✓ Brein-cyclus iteratie 12 voltooid (H36-H40 + productlijn-concept)
- ✓ T1-sprint voltooid (H36 oorspronkelijk closed via patch v4.6.1; methode-protocol v1.0 vastgesteld)
- ✓ Brein-cyclus iteratie 13 voltooid (T1-registratie + 2 nieuwe concepten + 3 sprint-protocollen)
- ✓ T2-sprint voltooid (65 mutaties op 118 paren over 10 clusters via patch v4.6.2; methode-protocol v1.2 in productie bevestigd; v1.3 DRAFT opgeleverd; D4.1 vastgesteld; H41 nieuw)
- ✓ Brein-cyclus iteratie 14 voltooid (T2-registratie + cluster-discipline-bewijslast-concept + H41 + H36 m10-closed + bidirectional-audit-symmetrie sub-aspect + D4.1-cluster-niveau-precedent)
- ✓ T3-sprint voltooid (2 mutaties op 31 m14-paren via patch v4.6.3; methode-protocol v1.3 FINAL vastgesteld 28 mei; cross-category-rationale als kandidaat v1.3.1-precedent; H36 fully closed)
- ✓ Brein-cyclus iteratie 15 voltooid (T3-registratie + cross-category-mappings-concept + commit-push-werkverdeling-workflow + H36 fully closed + H39 versterkt T3 + H41 informatief + M14 SKOS-distributie + errata-correctie rapporten)
- Open: Dashboard-inhaalslag 7 sprints (parallel, niet-blokkerend; nu incl. v4.6.3)
- Open: PAT + export-fallback configureren (projecteigenaar)
- Open: locatie Spoor B-prototype `grc-dashboard-v3-2.html` in repo (Optie A/B/C — wacht op masterchat sinds iteratie 12)
- Open: Protocol v1.3.1-formalisering cross-category-mappings-principe (masterchat-werk bij volgende sprint-scoping)
- Open: confidence-verhoging mapping-bron-disclaimer-effect naar high (vereist tweede onafhankelijke bron-bevestiging — NIST OLIR of ISO Annex F)
- Open: projectinstructie-bijwerking voor commit-push-werkverdeling-update (28-05-2026); masterchat-taak bij volgende versie-cut (v1.11)

**Volgende activiteit:** T4-scope-bepaling in verse masterchat-sessie. T4-kandidaten: cross-bron-overlap-105-paren (v4.5.0), m17 COSO/COBIT, m11 NIST SP 800-53, m09 ISO 27001, m16 VIRBI, m12 DORA, framework-niveau SKOS. UI-moderniseringssprint (H40) en HermiT-equivalentie-verificatie (H38) blijven alternatieve kandidaten. Protocol v1.3.1-formalisering kandidaat (cross-category-mappings-principe) is brein-cyclus + masterchat-werk; geen sprint nodig.

## Snelle entry-points per gebruiks-scenario

### "Ik wil weten waarom we iets zo doen"
→ Start met **decisions/** (D1–D12, incl. D6 symmetrische uitbreiding v1.9 en D9 vier verificatie-clusters) of **concepts/** (uitleg & synthese, incl. parallelle-maturity-clusters).

### "Ik wil weten wat we gisteren / vorige sprint hebben gedaan"
→ Start met **sprints/** (chronologisch, v4.6.0 als laatste) of **brain__log.md** (operationeel).

### "Ik wil weten welke architectuur-vragen open staan"
→ Start met **architecture/H-register.md** — open: H25, H26, H27, H32, H33, H34, H35 (allen onveranderd). Resolved (iteratie 15): **H36** (fully closed via T1+T2+T3, cumulatief 149 ctrl:↔compl:-paren). Parked: H37 (open-ontologies-MCP), H38 (HermiT-equivalentie), H39 (SHACL false-positive-uitsplitsing — versterkt door T1+T2+T3 bidirectional), H40 (dashboard-explorer-renderdekking), H41 (iteratie 14, SKOS-axioma-set-handling onder OWL-RL; T3-bevestiging informatief iteratie 15).

### "Ik wil weten waarom we iets juist NIET doen"
→ Start met **scope/** (bewuste uitsluitingen) of geparkeerde H-items.

### "Ik wil weten hoe het project werkt qua proces"
→ Start met **workflow/** (rolverdeling — nu 7 chats incl. Brein, scope-discipline, oplevering, sprint-protocollen — 4 nieuwe v1.9).

### "Ik wil weten welke bronnen we gebruiken en met welke licentie"
→ Start met **sources/source-register.md** (5 SourceAttributions in model post-v4.6.0).

### "Ik wil weten wat er in module X zit"
→ Start met **modules/M{NN}_{slug}.md** (M15 niet meer stub, M21 incl. Tiers).

### "Hoe werkt het volwassenheidsmodel?"
→ Start met **concepts/parallelle-maturity-clusters.md** voor het onderscheid biz vs isms — kritisch voor toekomstige uitbreidingen.

## Concept-D-Sprint-H-koppeling (snelle traceerbaarheid)

| Concept | Primaire D | Sprint van vastlegging | Open H-vragen |
|---|---|---|---|
| Framework-neutraliteit | D9 *(VIER clusters per v4.6.0)* | 17 mrt 2026 + v4.4.0 + v4.5.0 + v4.6.0 | — |
| owl:sameAs-discipline | D5 + D11 | v2.0 + v4.3.0 | — |
| Drie-laags-compliance | D12 *(verfijning v4.4.0)* | v4.3.3 + v4.4.0 | H25, H26, H27, H32 |
| BBN-correctie | (—) | v4.1.0-alpha | — |
| OWL RL reasoning | D1 | v4.3.0 | — |
| Gesplitste SHACL | (methode) | v4.2.0 → v4.3.0 | — |
| Canonical metrics | (discipline) | v4.3.0 | — |
| NamedIndividual-telmethode | (formalisering) | v4.3.3 | H21 |
| Provenance & attribuering | (discipline) | v4.1.0-alpha → v4.4.0 → v4.5.0 → **v4.6.0 (5 SourceAttributions)** | — |
| Scope-discipline | (iteratie 8) | v4.2.2 → v4.3.3 | — |
| Meeliftregel-edit-scope | D6 *(symmetrische uitbreiding v1.9)* | v4.1.0-alpha + v1.7 + v4.5.0 + v4.6.0 | — |
| Cross-bron-overlap | (kwaliteits-indicator) | v4.5.0 (S5∩S6 = 105) | — |
| **Parallelle-maturity-clusters** *(iteratie 11)* | **(V1-uitkomst Optie B)** | **v4.6.0 Stap 2** | **— (toekomst-overweging: brug-mapping)** |
| **SKOS-beoordelings-protocol** *(iteratie 13, T2-update iteratie 14, T3-update iteratie 15)* | **D4 + D4.1** | **T1 Stap 2 (v1.0) + T2 (v1.2 productie op 118 paren / 10 clusters) + T3 (v1.3 FINAL, vastgesteld masterchat 28 mei, productie op 31 m14-paren cross-category)** | **— (H36 fully closed via T1+T2+T3); v1.3.1-formalisering pending** |
| **Mapping-bron-disclaimer-effect** *(iteratie 13, T2-update iteratie 14, T3-context iteratie 15)* | **D4.1 (formeel sinds 27 mei 2026)** | **T1 §6 + §8 (ENISA TIG R285) + T2 cluster-niveau-precedent + T3 inactief-precedent (AVG = publiek EU-recht)** | **— (D4.1 vastgesteld); confidence-verhoging naar high vereist tweede bron** |
| **Cluster-discipline-bewijslast** *(iteratie 14)* | **D4 + D4.1 (operationeel binnen cluster-discipline §3.3)** | **T2 Stap 3-leerpunt §6.5 + patch-rapport §6.3** | **— (gevalideerd via 0/10 succesvolle uitzonderingen)** |
| **Cross-category-mappings** *(iteratie 15, kandidaat v1.3.1-precedent)* | **D4 (kandidaat-aanvulling)** | **T3 Stap 3-eindrapport §5 + patch-rapport v4.6.3 §13.1 — empirisch precedent op 31 m14-paren / 5 AVG-clusters (control ↔ legal-obligation = associatief)** | **— (formalisering = masterchat-werk bij volgende sprint-scoping; H36 fully closed)** |

## Vault-conventies

| Conventie | Detail |
|---|---|
| Frontmatter-velden | `type` + `title` + `status` + `date` + `related` + `sources` + `chat-sources` (verplicht; mag `[]` zijn met `gaps:`) + `confidence` |
| Wikilinks | `[[...]]` als grep-anchors |
| Log-discipline | Append-only, nieuwste entry bovenaan, één bestand alleen-vervangen bij elke iteratie |
| Tweetaligheid | D6 meeliftregel + vertaling-scope (v1.7 + v1.9 symmetrisch) |
| Organisatie-naam | NOOIT — altijd "de organisatie" of "Rijksoverheidsorganisatie" |

## Status van het meta-project (brain-vault zelf)

| Aspect | Status |
|---|---|
| Vault-opzet | Voltooid na 15 iteraties (incl. v4.6.0-update + v1.9 + iteratie 12 polish-mini-sprint + iteratie 13 post-T1-cyclus + iteratie 14 post-T2-cyclus + iteratie 15 post-T3-cyclus) |
| Productief gebruik | Brain bewees productie-waarde tijdens v4.5.0 + v4.6.0-sprints + T1-sprint + T2-sprint + T3-sprint. Iteratie 15 is vierde post-migratie Brein-cyclus en derde reguliere sprint-afsluitings-cyclus. Werkflow volledig gevalideerd op cross-category-context (control ↔ legal-obligation, T3) |
| Migratie-prep | Voltooid — brain-vault in GitHub-repo, brein-subagent in Claude Code, vier post-migratie Brein-cycli succesvol afgerond |
| Smoke-tests | 5/5 PASS (geldig voor v4.3.3-baseline; nieuwe v4.6.3-baseline kan in latere cyclus hertest) |

## Cross-references

- [[brain__CLAUDE]] — vault-spec (claude.ai-versie)
- [[brain__log]] — chronologisch operationeel logboek
- [[brain__archeology-report]] — fundament-assessment iteratie 1.5
- [[brain__smoke-tests]] — vault-functionaliteit-tests
- [[brain__obsidian-migration-guide]] — migratie naar lokale Obsidian
- [[brain__decisions__D-register]]
- [[brain__sprints__sprint-register]]
- [[brain__architecture__H-register]]
- [[brain__concepts__concept-register]]
- [[brain__modules__module-register]]
- [[brain__sources__source-register]]
- [[brain__workflow__workflow-register]]
- [[brain__scope__scope-register]]

— Einde masterindex.
