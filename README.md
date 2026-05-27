# GRC Kennismodel

Een formele OWL 2 DL ontologie die alle voor een Nederlandse Rijksoverheidsorganisatie toepasselijke wet- en regelgeving, normen en best practices integreert tot één machine-leesbare kennisbron. Fungeert als de informatie-laag van het ISMS, ondersteund door een dashboard.

**Framework-neutraal** (D9): alle normen, wetten en kaders zijn gelijkwaardig gemodelleerd. Geen enkel framework heeft architecturaal privilege. BIO 2.0 is het operationele toepassings-perspectief voor dashboard + rapportage (verplicht Rijksoverheid-baseline), niet de architecturele kern.

---

## Status

| | |
|---|---|
| Versie | **v4.6.2** |
| Datum | 27 mei 2026 |
| Fase | Post-T2 SKOS-kwaliteitsanalyse — productie |
| Projectinstructie | v1.10 (27 mei 2026) |
| Werkverdeling | Tech / Brein / Dashboard in Claude Code; Master / Documentatie / Analyse / Asset in claude.ai |
| Repository-zichtbaarheid | Privé |

---

## Baseline v4.6.2

Uit `output/verification/canonical_metrics_v4_6_2.json` (canonical metrics OWL RL met `axiomatic_triples=False, datatype_axioms=False`):

| Metric | Waarde |
|---|---:|
| Pre-inferentie triples | 20.950 |
| Post-inferentie triples (OWL RL) | 44.907 |
| Klassen | 199 |
| NamedIndividuals | 1.383 |
| ObjectProperties | 149 |
| DatatypeProperties | 96 |
| owl:sameAs (93 D5 + 5 D11) | 98 |
| SKOS-mappings totaal | 1.798 |
| — `skos:exactMatch` | 18 |
| — `skos:closeMatch` | 1.457 |
| — `skos:broadMatch` | 131 |
| — `skos:narrowMatch` | 0 |
| — `skos:relatedMatch` | 192 |
| Modules (.ttl) | 22 data-modules + grc-core + grc-bridges + grc-shacl |
| SHACL SECTIE A (inference=none) | 0 violations |
| SHACL SECTIE B (inference=owlrl) | 0 violations |
| SHACL COMBINED (alle 7 shapes, owlrl) | 290 (bekende false-positives, stabiel sinds v4.3.0) |
| OWL-consistentie | 0 inconsistenties |

---

## Repo-structuur (post-migratie 26 mei 2026)

```
grc-kennismodel/
├── README.md                                 ← dit bestand
├── CLAUDE.md                                 ← root subagent-config voor Claude Code
├── ontology/                                 ← de ontologie zelf (22 .ttl + shapes + demo)
│   ├── grc-core.ttl                          ← root-ontologie (11 namespaces — D3)
│   ├── grc-bridges.ttl                       ← cross-module bridges (D5 + D11 sameAs)
│   ├── grc-shacl.ttl                         ← SHACL-shapes (7 totaal, gesplitst A/B)
│   ├── m01-framework.ttl  … m18-assets.ttl   ← data-modules (frameworks, controls, etc.)
│   ├── m10-nis2-ext.ttl                      ← T1+T2-gepatchte module (v4.6.2)
│   ├── m21-csf.ttl                           ← NIST CSF 2.0 (v4.5.0)
│   └── m18-demo-sparql.rq                    ← demo-query asset-module
├── docs/                                     ← autoritatieve documentatie
│   ├── projectinstructie-v1_10.md            ← AUTORITATIEF (huidige versie)
│   ├── projectinstructie-v1_8/9.md           ← historisch (referentie)
│   ├── skos-beoordelings-protocol-v1_2.md    ← T2-operationeel
│   ├── skos-beoordelings-protocol-v1_3.md    ← DRAFT (vaststelling pending T3/m14)
│   ├── sprint-protocols.md                   ← 17 sprint-protocollen (v1.3)
│   ├── migratie-roadmap.md                   ← Claude Code/GitHub-migratie
│   ├── instructies/                          ← sprint-instructies (T2-set: pre-sprint + pilot + stap3 + stap4)
│   └── handovers/                            ← chat-handovers tussen sessies
├── brain/                                    ← brain-vault (~120 markdown, flat-folder via __-encoding)
│   ├── brain__index.md                       ← ENTRY POINT
│   ├── brain__log.md                         ← iteratie-historie
│   ├── brain__CLAUDE.md                      ← Brein-subagent config
│   ├── brain__decisions__*.md                ← D1-D12 + D4.1 + D-register
│   ├── brain__architecture__*.md             ← H15-H41 + H-register
│   ├── brain__concepts__*.md                 ← kern-concepten + concept-register
│   ├── brain__sprints__*.md                  ← sprint-historie (per sprint + register)
│   ├── brain__modules__*.md                  ← per-module documentatie
│   ├── brain__sources__*.md                  ← bron-tracing
│   ├── brain__workflow__*.md                 ← werkproces-discipline
│   └── brain__scope__*.md                    ← scope-besluiten
├── output/                                   ← werkartefacten per sprint
│   ├── verification/                         ← canonical metrics + SHACL + file-hashes (per versie)
│   ├── scripts/                              ← appliers + helpers (per sprint)
│   ├── analysis/                             ← cluster-JSON's + onderzoek (per sprint)
│   └── reports/                              ← sprint-rapporten (pre-sprint / pilot / stap3 / patch-rapport)
└── sources/                                  ← bronmateriaal (publiek + CC-BY; geen NEN-restrictief)
    ├── eu-recht/                             ← NIS2, DORA, UV
    ├── nl-wetgeving/                         ← VIR, VIRBI, BVA, CIO-stelsel, CBW, Cbb
    ├── adr-norea/                            ← CBW-Excel (CC-BY 4.0)
    ├── nist/                                 ← CSF 2.0 + SP 800-53/39/30
    └── ensia/                                ← NOREA-handreiking
```

**NEN-restrictieve bronnen** (ISO 27001/27002/27005/31000/22301/22313) staan NIET in deze repo. Tech-subagent in Claude Code heeft lokale leestoegang via `user` (binnen 'user' persoonlijke NEN-licentie) — uitsluitend voor parafrase + clausule-verwijzing, geen verbatim-tekst > 10 woorden in repo-output.

---

## Quick-start

### Ontologie valideren

```bash
# Canonical metrics (rdflib + owlrl)
python3 output/verification/canonical_metrics_v4_6_2.py
# → output/verification/canonical_metrics_v4_6_2.json

# SHACL gesplitste validatie (rdflib + pyshacl)
python3 output/verification/shacl_split_validate_v4_6_2.py
# → output/verification/shacl_results_v4_6_2.json

# File-hashes verifiëren
sha256sum -c output/verification/file_hashes_v4_6_2.txt
```

Vereist: `rdflib >= 7.0`, `owlrl >= 7.0`, `pyshacl >= 0.25`.

**Verwacht resultaat:** 0 inconsistenties (OWL RL); SHACL SECTIE A=0, SECTIE B=0, COMBINED=290 (identiek aan v4.6.1).

### Brain-vault navigeren

1. Start bij `brain/brain__index.md` — overzicht + cross-references
2. Voor sprint-historie: `brain/brain__sprints__sprint-register.md`
3. Voor D-decisions: `brain/brain__decisions__D-register.md`
4. Voor H-items (architectuur-overwegingen): `brain/brain__architecture__H-register.md`
5. Voor concepten: `brain/brain__concepts__concept-register.md`

Brain-vault-bestanden gebruiken Obsidian-stijl `[[brain__*]]`-wikilinks voor cross-references.

---

## Documentatie — autoritatieve bronnen

| Document | Pad | Status |
|---|---|---|
| Projectinstructie | `docs/projectinstructie-v1_10.md` | autoritatief (27 mei 2026) |
| SKOS-beoordelings-protocol | `docs/skos-beoordelings-protocol-v1_2.md` | T2-operationeel |
| SKOS-beoordelings-protocol (volgende) | `docs/skos-beoordelings-protocol-v1_3.md` | DRAFT — vaststelling pending bij T3/m14-scoping |
| Sprint-protocollen | `docs/sprint-protocols.md` | 17 protocollen (v1.3) |
| Migratie-roadmap | `docs/migratie-roadmap.md` | Claude Code + GitHub-migratie (afgerond 26 mei 2026) |
| Patch-rapport v4.6.2 | `output/reports/patch-rapport-v4_6_2.md` | autoritatieve baseline-bron |
| Brain-vault entry | `brain/brain__index.md` | overzicht alle brain-bestanden |

---

## Sprint-historie (compact)

| Sprint | Datum | Hoofdzaak | Status |
|---|---|---|---|
| v3.x | mrt 2026 | Monolithische fase | superseded |
| v4.0–4.2 | apr 2026 | Modulaire splitsing + M18 asset-module + SoA-canonisering | superseded |
| v4.3.x | apr 2026 | D11 gap-sprint + D12 + predicate-consolidatie | superseded |
| v4.4.0 | 13 mei 2026 | Fase 2 — CBW + Cbb-uitbouw + UV-decompositie | superseded |
| v4.5.0 | 19 mei 2026 | Fase 3 — M21 NIST CSF 2.0 (6/22/106/363 + 1.435 mappings) | superseded |
| v4.6.0 | 21 mei 2026 | Fase 4 — M15-ENSIA-uitbouw + volwassenheidsmodel + CSF Tiers | superseded |
| **Migratie** | **26 mei 2026** | **Tech/Brein/Dashboard → Claude Code + GitHub-repo** | **afgerond** |
| v4.6.1 (T1) | 26 mei 2026 | SKOS-exactMatch-audit ctrl:↔compl: m10 — 28 herclassificaties | superseded |
| **v4.6.2 (T2)** | **27 mei 2026** | **SKOS-bidirectional-audit m10 — 65 herclassificaties (10 clusters → broadMatch)** | **productie** |

Volledige sprint-detail per sprint: `brain/brain__sprints__*.md`.

---

## Ontwerpbeslissingen + architectuur-items

**12 D-decisions + 1 sub-rule** (allen actief, niet wijzigbaar zonder masterchat-goedkeuring):

D1 OWL 2 DL · D2 Turtle · D3 11 namespaces · D4 SKOS cross-framework · **D4.1 Disclaimer-handling** (NIEUW 27 mei) · D5 owl:sameAs strikt ctrl:↔bio: · D6 tweetalige annotaties · D7 BIO 2.0 twee klassen · D8 canonieke SoA · D9 framework-neutraal · D10 COSO enterprise-governance · D11 asset-convergentie · D12 drie-laags compliance.

Volledig in `brain/brain__decisions__D-register.md`.

**H-items** (architectuur-overwegingen, geparkeerd of active):

H11-H21 (Spoor B / consistentie) · H25-H35 (post-v4.3.3 aandachtspunten) · H36 (SKOS-exactMatch-audit — **m10-component closed via T1+T2**; m14 open subtask) · H37 (open-ontologies MCP) · H38 (HermiT-equivalentie) · H39 (SHACL-blinde vlek SKOS-distributie) · H40 (UI-renderdekking) · **H41 (NIEUW 27 mei) — SKOS-axioma-set-handling in OWL-RL**.

Volledig in `brain/brain__architecture__H-register.md`.

---

## Licentie-bewustzijn

| Bron-categorie | Voorbeeld | Restrictie |
|---|---|---|
| NEN-restrictief | ISO 27001, 27002, 27005, 31000, 22301, 22313 | Alleen via gelicentieerde kanalen; geen tekst-reproductie in repo-output |
| CC-BY 4.0 | CBW-Excel (ADR & NOREA, sep 2025) | Geattribueerd via `ext:Attr_CBW_NIS2_Framework_2025_CC_BY_4_0` |
| Publiek domein | NIST CSF 2.0, SP 800-53/39/30, CSWP 29 | Vrij; geattribueerd via `ext:Attr_NIST_CSF_2_0_*` |
| Vrij met bronvermelding | ENSIA-handreiking (NOREA, dec 2024) | Geattribueerd via `ext:Attr_ENSIA_Logius_2024` |
| Publiek EU-recht | NIS2, DORA, UV (EU) 2024/2690, AVG | Vrij |
| Publiek NL-recht | VIR 2007, VIRBI 2025, BVA-stelsel, CIO-stelsel, CBW-concept, Cbb-concept | Vrij |
| Onbeperkt | BIO 2.0 (overheidspublicatie) | Vrij |

5 `SourceAttribution`-individuals in model per v4.6.2 (zie `brain/brain__concepts__provenance-en-attribuering.md`).

**Sprint-Protocol 14 (Pre-push disclosure-check)** verplicht vóór elke push — vijf categorieën check waaronder NEN-tekst-detectie (geen verbatim > 10 woorden).

---

## Project-context

- **Opdrachtgever**: Nederlandse Rijksoverheidsorganisatie (interne projectstuur; organisatie-naam niet vermeld per projectinstructie-discipline)
- **Projecteigenaar**: 'user', GRC-ontwerper in directe ondersteuning van de CSO
- **CSO**: formele project-sponsor
- **Formele Claude-toestemming**: verkregen 17 maart 2026
- **PID + CSO-GO architectuurdocument v1.2**: goedgekeurd 13 april 2026

---

## Volgende kandidaten

Geen vaste planning. Kandidaten in volgorde van architectuur-prioriteit:

1. **T3-sprint** — m14 (AVG/GDPR) ctrl:↔compl: paren (31 stuks, compl→ctrl-richting)
2. **Protocol v1.3 vaststelling** — bij T3 of m14-sprint-scoping
3. **Dashboard-inhaalslag** — v3 build scripts + v4.6.2-databestanden (5+ sprints achterstand)
4. **H33** — m11 substantiële SP 800-53-uitbreiding
5. **Spoor B-voorbereiding** — T&I lab-test

Zie `docs/projectinstructie-v1_10.md` §"OPENSTAANDE ITEMS" voor volledige lijst.

---

*Voor sprint-detail: `brain/brain__sprints__<sprint>.md`. Voor architectuur-vragen: brain-vault registers. Voor scope-pauze: masterchat (claude.ai).*
