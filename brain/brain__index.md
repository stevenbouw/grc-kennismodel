---
type: index
id: brain-index
title: GRC Kennismodel Brain — Masterindex
status: living
date: 2026-05-26
---

# GRC Kennismodel Brain — Masterindex

Karpathy-conforme "LLM Wiki" voor het GRC Kennismodel-project. Inhoud-gedreven, append-only logbook, type-getagged frontmatter, wikilinks als grep-anchors. Ontworpen voor menselijke navigatie en voor LLM-retrieval via Project Knowledge én Claude Code (post-migratie).

## Vault-staat — 12 iteraties voltooid

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
| **12** | **2026-05-26** | **Post-v4.6.0 polish-mini-sprint: H36-H40 (parked) + Protocol 14 pre-push-disclosure + dashboard-productlijnen-concept** | **13 (6 nieuw + 7 update)** |
| **Totaal brain-bestanden** | | | **~107** |

Plus ±15 bron-documenten als upload (patch-rapporten incl. v4.5.0 + v4.6.0, projectinstructie v1.9, ontologie-PDFs).

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
brain__sprints__v{X_Y_Z}_{slug}.md          ← 14 sprint-files (incl. v4.6.0)
brain__architecture__H{NN}_{slug}.md         ← 16 H-items (incl. H33-H35 + H36-H40 iteratie 12)
brain__concepts__{slug}.md                   ← 15 concept-files (incl. skos-export-filter + dashboard-productlijnen)
brain__modules__M{NN}_{slug}.md              ← 19 modules (M15 uitgebreid, M21 incl. Tiers)
brain__sources__{slug}.md                    ← 8 source-files (5 SourceAttributions in model)
brain__workflow__{slug}.md                   ← 6 workflow-files (incl. sprint-protocollen)
brain__scope__{slug}.md                      ← 4 bewust-uitgesloten elementen
```

## Status-overzicht ontologie v4.6.0 (huidige baseline)

| Metric | Waarde | Δ t.o.v. v4.5.0 |
|---|---:|---:|
| Versie | **v4.6.0** | — |
| Datum | 2026-05-21 | — |
| Modules | 19 active + 0 stub | M15 niet meer stub |
| Pre-inferentie triples | 20.950 | **+1.610 (+8,3%)** |
| Post-OWL-RL triples | 44.907 | +2.919 |
| Klassen | 199 | +6 (5 isms + 1 csf:CSFTier) |
| NamedIndividuals | 1.383 | **+204** |
| ObjectProperties | 149 | +3 (isms) |
| DatatypeProperties | 96 | +2 (csf) |
| `owl:sameAs` | 98 (93 D5 + 5 D11) | 0 (onveranderd) |
| **SKOS-mappings** | **1.798** | **+4 (Tier↔Level)** |
| Namespaces | 11 | 0 (onveranderd) |
| SHACL RUN 1 | 0 violations | 0 |
| SHACL RUN 2 | 290 false-positives (combined-mode) | 0 (identiek aan v4.4.0 + v4.5.0) |

## v4.6.0 wijzigingen — kort

5 modules gewijzigd: grc-core (versie-bump), M01 (fw:ENSIA als GRCFramework), M06 (volwassenheidsmodel-cluster), M15 (oude fw:Guideline-blok verwijderd), M21 (CSFTier + Tier↔Level mappings). Volwassenheidsmodel-cluster als nieuwe isms-cluster naast biz:MaturityAssessment-cluster (NIET samenvoegen). ENSIA gepromoot naar fw:GRCFramework (D9 vierde verificatie-cluster). 5 SourceAttributions in model (+2: NBA-LIO-NOREA + ENSIA-Logius). Vier nieuwe sprint-protocollen formeel in projectinstructie v1.9. Geen nieuwe H-items.

## Volgende fase — Post-migratie productie-fase

v4.6.0 is **laatste geplande Spoor A-sprint** voor de bedoelde Fase 1-4 scope. Migratie naar Claude Code + GitHub voltooid via Fase 0 + polish-mini-sprint (iteratie 12, 26 mei 2026).

Pre-condities migratie — status iteratie 12:
- ✓ Master-handover-document v1.0 in PK
- ✓ docs/sprint-protocols.md geport (v1.0 → v1.1 met Protocol 14 pre-push-disclosure)
- ✓ Brein-cyclus iteratie 12 voltooid (H36-H40 + productlijn-concept + log/index-update)
- Open: Dashboard-inhaalslag 5 sprints (parallel, niet-blokkerend)
- Open: PAT + export-fallback configureren (projecteigenaar)
- Open: locatie Spoor B-prototype `grc-dashboard-v3-2.html` in repo (Optie A/B/C — wacht op masterchat)

**Eerste post-migratie-sprint:** T1-test-sprint, scope tbd. Kandidaten: SKOS-kwaliteitsanalyse formeel als sprint (1.798 mappings — sluit aan bij H36), ENISA TIG-PDF-integratie, Spoor B-voorbereiding (T&I lab-test), UI-moderniseringssprint (sluit aan bij H40), HermiT-equivalentie-verificatie (sluit aan bij H38).

## Snelle entry-points per gebruiks-scenario

### "Ik wil weten waarom we iets zo doen"
→ Start met **decisions/** (D1–D12, incl. D6 symmetrische uitbreiding v1.9 en D9 vier verificatie-clusters) of **concepts/** (uitleg & synthese, incl. parallelle-maturity-clusters).

### "Ik wil weten wat we gisteren / vorige sprint hebben gedaan"
→ Start met **sprints/** (chronologisch, v4.6.0 als laatste) of **brain__log.md** (operationeel).

### "Ik wil weten welke architectuur-vragen open staan"
→ Start met **architecture/H-register.md** — open: H25, H26, H27, H32, H33, H34, H35 (allen onveranderd in v4.6.0). Parked (iteratie 12): H36 (SKOS-rigour), H37 (open-ontologies-MCP), H38 (HermiT-equivalentie), H39 (SHACL false-positive-uitsplitsing), H40 (dashboard-explorer-renderdekking).

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
| Vault-opzet | Voltooid na 12 iteraties (incl. v4.6.0-update + v1.9 + iteratie 12 polish-mini-sprint) |
| Productief gebruik | Brain bewees productie-waarde tijdens v4.5.0 én v4.6.0-sprints (sprint-protocollen toegepast, leerpunten naar projectinstructie geformaliseerd). Iteratie 12 toont post-migratie Brein-cyclus werkt zoals voorzien |
| Migratie-prep | Voltooid — brain-vault in GitHub-repo, brein-subagent in Claude Code, eerste post-migratie Brein-cyclus afgerond |
| Smoke-tests | 5/5 PASS (geldig voor v4.3.3-baseline; nieuwe v4.6.0-baseline kan na T1-test-sprint hertest) |

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
