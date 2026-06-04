# GRC Kennismodel

Een formele OWL 2 DL ontologie die alle voor een Nederlandse Rijksoverheidsorganisatie toepasselijke wet- en regelgeving, normen en best practices integreert tot één machine-leesbare kennisbron. Fungeert als de informatie-laag van het ISMS, ondersteund door een dashboard.

**Framework-neutraal** (D9): alle normen, wetten en kaders zijn gelijkwaardig gemodelleerd. Geen enkel framework heeft architecturaal privilege. BIO 2.0 is het operationele toepassings-perspectief voor dashboard + rapportage (verplicht Rijksoverheid-baseline), niet de architecturele kern.

---

## Status

| | |
|---|---|
| Versie | **v4.6.4** |
| Datum | 29 mei 2026 |
| Fase | Post-T1/T2/T3 SKOS-kwaliteitsanalyse + DL-conformiteits-fix — productie |
| Projectinstructie | v1.11 (29 mei 2026) |
| Werkverdeling | Tech / Brein / Dashboard in Claude Code; Master / Documentatie / Analyse / Asset in claude.ai |
| Repository-zichtbaarheid | Privé |

---

## Baseline v4.6.4

Uit `output/verification/canonical_metrics_v4_6_4.json` (canonical metrics OWL RL met `axiomatic_triples=False, datatype_axioms=False`):

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
| — `skos:broadMatch` | 129 |
| — `skos:narrowMatch` | 0 |
| — `skos:relatedMatch` | 194 |
| Modules (.ttl) | 22 .ttl-modules + grc-shacl.ttl + 1 demo-SPARQL |
| SHACL SECTIE A (inference=none) | 0 violations |
| SHACL SECTIE B (inference=owlrl) | 0 violations |
| SHACL COMBINED (alle 7 shapes, owlrl) | 290 (bekende false-positives, stabiel sinds v4.3.0) |
| OWL-consistentie (OWL RL) | 0 inconsistenties |
| DL-consistentie (HermiT) | consistent — 0 owl:Nothing, geen justificaties (her-geverifieerd v4.6.4) |

**v4.6.4 = DL-conformiteits-fix.** Alle canonieke metrics zijn identiek aan v4.6.3; de fix verving alleen het *object* van 2 `rdfs:range`-triples in `m21-csf.ttl` (`xsd:string` → `rdfs:Literal` op de twee CSF-Tier-description-properties) + een version-bump in `grc-core.ttl`. OWL RL controleert datatype-ranges niet streng → de metrics zijn invariant; de fix is puur DL-correctheid. Een datatype-range-mismatch is onzichtbaar onder de canonieke OWL RL-metrics maar fataal onder HermiT (H38 resolved).

---

## Repo-structuur (post-migratie 26 mei 2026)

```
grc-kennismodel/
├── README.md                                 ← dit bestand
├── CLAUDE.md                                 ← root subagent-config voor Claude Code
├── .claude/                                  ← Tooling-laag (hooks + permissions + skills, incl. D.7 grc-domein)
├── ontology/                                 ← de ontologie zelf (22 .ttl + shapes + demo)
│   ├── grc-core.ttl                          ← root-ontologie (11 namespaces — D3; version-triple v4.6.4)
│   ├── grc-bridges.ttl                       ← cross-module bridges (D5 + D11 sameAs)
│   ├── grc-shacl.ttl                         ← SHACL-shapes (7 totaal, gesplitst A/B)
│   ├── m01-framework.ttl  … m18-assets.ttl   ← data-modules (frameworks, controls, etc.)
│   ├── m10-nis2-ext.ttl                      ← T1+T2-gepatchte module (eindstand ctrl→compl: 118 broadMatch)
│   ├── m14-avg-gdpr.ttl                      ← T3-gepatchte module (2 mutaties)
│   ├── m21-csf.ttl                           ← NIST CSF 2.0 (v4.5.0; v4.6.4 range-fix CSF-Tier-descriptions)
│   └── m18-demo-sparql.rq                    ← demo-query asset-module
├── docs/                                     ← autoritatieve documentatie
│   ├── projectinstructie-v1_11.md            ← AUTORITATIEF (huidige versie)
│   ├── projectinstructie-v1_8/9/10.md        ← historisch (referentie)
│   ├── skos-beoordelings-protocol-v1_3.md    ← FINAL (T3)
│   ├── skos-beoordelings-protocol-v1_0..2.md ← historisch (referentie)
│   ├── sprint-protocols.md                   ← 18 sprint-protocollen + v1.3-werkflow-disciplines
│   ├── migratie-roadmap.md                   ← Claude Code/GitHub-migratie
│   ├── instructies/                          ← sprint-instructies + besluitnotities
│   └── handovers/                            ← chat-handovers tussen sessies
├── brain/                                    ← brain-vault (~117 markdown, flat-folder via __-encoding)
│   ├── brain__index.md                       ← ENTRY POINT
│   ├── brain__log.md                         ← iteratie-historie (iteratie 16)
│   ├── brain__CLAUDE.md                      ← Brein-subagent config
│   ├── brain__decisions__*.md                ← D1-D12 + D4.1 + D-register
│   ├── brain__architecture__*.md             ← H-items + H-register
│   ├── brain__concepts__*.md                 ← kern-concepten + concept-register
│   ├── brain__sprints__*.md                  ← sprint-historie (per sprint + register)
│   ├── brain__modules__*.md                  ← per-module documentatie
│   ├── brain__sources__*.md                  ← bron-tracing
│   ├── brain__workflow__*.md                 ← werkproces-discipline
│   └── brain__scope__*.md                    ← scope-besluiten
├── dashboard/                                ← Spoor B operationele werkmap (grc-dashboard-v3-2.html) + vendor/
├── output/                                   ← werkartefacten per sprint
│   ├── verification/                         ← canonical metrics + SHACL + file-hashes + HermiT-merge (per versie)
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

**NEN-restrictieve bronnen** (ISO 27001/27002/27005/31000/22301/22313) staan NIET in deze repo. Tech-subagent in Claude Code heeft lokale leestoegang via persoonlijke NEN-licentie — uitsluitend voor parafrase + clausule-verwijzing, geen verbatim-tekst > 10 woorden in repo-output.

---

## Quick-start

### Ontologie valideren

```bash
# Canonical metrics (rdflib + owlrl)
python3 output/verification/canonical_metrics_v4_6_4.py
# → output/verification/canonical_metrics_v4_6_4.json

# SHACL gesplitste validatie (rdflib + pyshacl)
python3 output/verification/shacl_split_validate_v4_6_4.py
# → output/verification/shacl_results_v4_6_4.json

# File-hashes verifiëren
sha256sum -c output/verification/file_hashes_v4_6_4.txt
```

Vereist: `rdflib >= 7.0`, `owlrl >= 7.0`, `pyshacl >= 0.25`.

**Verwacht resultaat:** 0 inconsistenties (OWL RL); SHACL SECTIE A=0, SECTIE B=0, COMBINED=290 (identiek aan v4.6.0-baseline).

**DL-conformiteits-vangnet:** OWL RL ziet datatype-ranges niet streng. Voor volledige DL-conformiteit een periodieke HermiT-her-run draaien op `output/verification/merged_asserted_v4_6_4.ttl` (Protégé) — v4.6.4 her-geverifieerd consistent (0 owl:Nothing).

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
| Projectinstructie | `docs/projectinstructie-v1_11.md` | autoritatief (29 mei 2026) |
| SKOS-beoordelings-protocol | `docs/skos-beoordelings-protocol-v1_3.md` | FINAL (T3) |
| Sprint-protocollen | `docs/sprint-protocols.md` | 18 protocollen + v1.3-werkflow-disciplines |
| Migratie-roadmap | `docs/migratie-roadmap.md` | Claude Code + GitHub-migratie (afgerond 26 mei 2026) |
| Patch-rapport v4.6.4 | `output/reports/patch-rapport-v4_6_4.md` | autoritatieve baseline-bron |
| Reasoner-toolchain-evaluatie | `output/reports/evaluatie-reasoner-toolchain-h37-h38-h41.md` | H37/H38/H41 |
| Brain-vault entry | `brain/brain__index.md` | overzicht alle brain-bestanden (iteratie 16) |

---

## Sprint-historie (compact)

| Sprint | Datum | Hoofdzaak | Status |
|---|---|---|---|
| v3.x | mrt 2026 | Monolithische fase | superseded |
| v4.0–4.2 | apr 2026 | Modulaire splitsing + M18 asset-module + SoA-canonisering | superseded |
| v4.3.x | apr 2026 | D11 gap-sprint + D12 + predicate-consolidatie | superseded |
| v4.4.0 | 13 mei 2026 | Fase 2 — CBW + Cbb-uitbouw + UV-decompositie | superseded |
| v4.5.0 | 19 mei 2026 | Fase 3 — M21 NIST CSF 2.0 (6/22/106/363 + mappings) | superseded |
| v4.6.0 | 21 mei 2026 | Fase 4 — M15-ENSIA-uitbouw + volwassenheidsmodel + CSF Tiers | superseded |
| **Migratie** | **26 mei 2026** | **Tech/Brein/Dashboard → Claude Code + GitHub-repo** | **afgerond** |
| v4.6.1 (T1) | 26 mei 2026 | SKOS-exactMatch-audit ctrl:↔compl: m10 — 28 herclassificaties | superseded |
| v4.6.2 (T2) | 27 mei 2026 | SKOS-bidirectional-audit m10 — 65 herclassificaties | superseded |
| v4.6.3 (T3) | 28 mei 2026 | SKOS-bidirectional-audit m14 AVG/GDPR — 2 mutaties + Protocol v1.3 FINAL | superseded |
| Reasoner-evaluatie | 29 mei 2026 | H37 + H38 + H41 (alle HOLD; H38 → resolved) | afgerond |
| **v4.6.4 (CSF-range-fix)** | **29 mei 2026** | **DL-conformiteits-fix (2 range-correcties m21) + HermiT-her-run** | **productie** |
| Dashboard-revival (Spoor B) | 29 mei 2026 | B7 ontologie-import + Q-M5 vendoring + B9 WCAG + verse-load-fixes | afgerond |
| T4-inventarisatie | 29 mei 2026 | csf↔ISO27001 cross-bron-overlap | afgesloten (Optie B, geparkeerd) |

Volledige sprint-detail per sprint: `brain/brain__sprints__*.md`.

---

## Ontwerpbeslissingen + architectuur-items

**12 D-decisions + 1 sub-rule** (allen actief, niet wijzigbaar zonder masterchat-goedkeuring):

D1 OWL 2 DL *(per v4.6.4 versterkt: OWL RL ≡ HermiT empirisch bevestigd, H38 resolved)* · D2 Turtle · D3 11 namespaces · D4 SKOS cross-framework · D4.1 Disclaimer-handling · D5 owl:sameAs strikt ctrl:↔bio: · D6 tweetalige annotaties · D7 BIO 2.0 twee klassen · D8 canonieke SoA · D9 framework-neutraal · D10 COSO enterprise-governance · D11 asset-convergentie · D12 drie-laags compliance.

Volledig in `brain/brain__decisions__D-register.md`.

**H-items** (architectuur-overwegingen, geparkeerd of resolved):

H25-H35 (post-v4.3.3 aandachtspunten) · **H36 RESOLVED** (ctrl↔compl SKOS-audit, fully closed via T1+T2+T3) · H37 (open-ontologies MCP — HOLD) · **H38 RESOLVED** (OWL RL ≡ HermiT bevestigd via v4.6.4) · H39 (SHACL-290-uitsplitsing — parked) · H40 (UI-renderdekking Spoor A — parked) · H41 (SKOS-axioma-set-handling — parked, activering = nieuwe D-decision) · H42/H43/H44 (dashboard-landschap-kandidaten, niet geactiveerd).

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

5 `SourceAttribution`-individuals in model per v4.6.4 (zie `brain/brain__concepts__provenance-en-attribuering.md`).

**Sprint-Protocol 14 (Pre-push disclosure-check)** verplicht vóór elke push — vijf categorieën check waaronder NEN-tekst-detectie (geen verbatim > 10 woorden). Deterministisch geborgd via `.claude/hooks/`.

---

## Project-context

- **Opdrachtgever**: Nederlandse Rijksoverheidsorganisatie (interne projectstuur; organisatie-naam niet vermeld per projectinstructie-discipline)
- **Projecteigenaar**: GRC-adviseur in directe ondersteuning van de CISO
- **CSO**: formele project-sponsor
- **Formele Claude-toestemming**: verkregen 17 maart 2026
- **PID + CSO-GO architectuurdocument v1.2**: goedgekeurd 13 april 2026

---

## Volgende kandidaten

Geen actieve sprint. Kandidaten (Steven kiest; geen vaste planning):

1. **T4-vervolg — csf↔ISO27001 cross-category-sprint** — vereist masterchat-scope-besluit (scope-eindpunt, overlap-definitie, cross-category-predicaat, provenance); eerst de 699-vs-494-reconciliatie oplossen.
2. **Protocol v1.3.1-formalisering (cross-category)** — twee precedenten (m14 + csf↔ISO27001).
3. **Andere SKOS-kwaliteitsanalyse-T-sprint** — m17 COSO/COBIT, m11 NIST SP 800-53, m16 VIRBI, of framework-niveau.
4. **H33/H34 — m11 NIST SP 800-53 uitbreiding** (124/~1000 in model + enhancement-modellering).
5. **Dashboard build-script-inhaalslag** — Spoor A explorer + Spoor B build-script naar v4.6.4-snapshot (meest demo-relevant).
6. **m01-verificatie** — bevestigen dat `fw:relatedTo`/`alignsWith`/`supersedes` echt in m01 staan (D.7-skill-vooronderstelling).
7. **Documentatie-debt-restant** — `skos-beoordelings-protocol-v1_3.md` §7.3; brain-sprint-protocollen lint naar 18.

Zie `docs/projectinstructie-v1_11.md` §"OPENSTAANDE ITEMS" voor de volledige lijst.

---

*Voor sprint-detail: `brain/brain__sprints__<sprint>.md`. Voor architectuur-vragen: brain-vault registers. Voor scope-pauze: masterchat (claude.ai).*
