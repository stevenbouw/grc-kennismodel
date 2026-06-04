# GRC Kennismodel

Een formele OWL 2 DL ontologie die alle voor een Nederlandse Rijksoverheidsorganisatie toepasselijke wet- en regelgeving, normen en best practices integreert tot één machine-leesbare kennisbron. Fungeert als de informatie-laag van het ISMS, ondersteund door een dashboard.

**Framework-neutraal** (D9): alle normen, wetten en kaders zijn gelijkwaardig gemodelleerd. Geen enkel framework heeft architecturaal privilege. BIO 2.0 is het operationele toepassings-perspectief voor dashboard + rapportage (verplicht Rijksoverheid-baseline), niet de architecturele kern.

> **Nieuw hier?** Begin bij **`docs/START-HIER.md`** — een korte wegwijzer die je in leesvolgorde naar de juiste documenten leidt (overdrachtsrapport → projectinstructie → brain-vault → masterchat-startprompt).

---

## Status

| | |
|---|---|
| Ontologie-versie | **v4.6.4** (stabiel) |
| Datum | 4 juni 2026 |
| Fase | **Spoor B-dashboardwerk actief** (v7: reskin + DORA-correctie + IA-herinrichting) — ontologie-baseline v4.6.4 ongewijzigd |
| Projectinstructie | **v1.12** (4 juni 2026) |
| Brain-vault | iteratie 17 (4 juni 2026) |
| Werkverdeling | Tech / Brein / Dashboard in Claude Code; Master / Documentatie / Analyse / Asset in claude.ai |
| Repository-zichtbaarheid | Privé |

**Actuele stand (Spoor B):** het operationele dashboard (`dashboard/grc-dashboard-v3-2.html`) is in de v7-werksessie (2–3 juni 2026) gereskind naar een warm-papier-thema, DORA-gecorrigeerd ("referentiekader · n.v.t.") en IA-heringericht van 5 naar 4 tabs (Overzicht · Governance · Compliance · Risk) met een gelaagde, D9-conforme kader-kiezer. Offline-werkend, WCAG 2.1 AA (axe 0). **Open kernprobleem:** de kader-kiezer toont nog placeholders i.p.v. echte controls/beschrijvingen/eisen ("lege huls") — besluit nodig over Pad 1 (ontologie-export verrijken) vs Pad 2 (demo-seed verrijken). Tweede open besluit: organisatiestructuur in het dashboard (A/B/C). Zie `docs/projectinstructie-v1_12.md` §"OPENSTAANDE ITEMS".

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

> De v7-dashboardsessie (2–3 juni) raakte de ontologie **niet**: alle wijzigingen zaten in de dashboard-HTML + demo-seed. De baseline-metrics hierboven gelden onverkort.

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
│   ├── START-HIER.md                         ← wegwijzer voor wie het project (opnieuw) oppakt
│   ├── projectinstructie-v1_12.md            ← AUTORITATIEF (huidige versie, 4 juni 2026)
│   ├── projectinstructie-v1_8/9/10/11.md     ← historisch (referentie)
│   ├── skos-beoordelings-protocol-v1_3.md    ← FINAL (T3)
│   ├── skos-beoordelings-protocol-v1_0..2.md ← historisch (referentie)
│   ├── sprint-protocols.md                   ← 18 sprint-protocollen + v1.3-werkflow-disciplines
│   ├── migratie-roadmap.md                   ← Claude Code/GitHub-migratie
│   ├── instructies/                          ← sprint-instructies + besluitnotities (incl. dashboard-reskin/IA + Brein-iteratie-17)
│   └── handovers/                            ← chat-handovers (overdrachtsrapport.md = breed startpunt; bootstrap-masterchat-v7.md = Master-startprompt)
├── brain/                                    ← brain-vault (~117 markdown, flat-folder via __-encoding)
│   ├── brain__index.md                       ← ENTRY POINT
│   ├── brain__log.md                         ← iteratie-historie (iteratie 17)
│   ├── brain__CLAUDE.md                      ← Brein-subagent config
│   ├── brain__decisions__*.md                ← D1-D12 + D4.1 + D-register
│   ├── brain__architecture__*.md             ← H-items + H-register
│   ├── brain__concepts__*.md                 ← kern-concepten + concept-register (incl. spoor-b-revival met v7-werkstroom)
│   ├── brain__sprints__*.md                  ← sprint-historie (per sprint + register)
│   ├── brain__modules__*.md                  ← per-module documentatie
│   ├── brain__sources__*.md                  ← bron-tracing
│   ├── brain__workflow__*.md                 ← werkproces-discipline
│   └── brain__scope__*.md                    ← scope-besluiten
├── dashboard/                                ← Spoor B operationele werkmap
│   ├── grc-dashboard-v3-2.html               ← operationeel dashboard (v7: warm-papier, 4 tabs, gelaagde kader-kiezer)
│   ├── design-tokens-grc-dashboard.css       ← visuele tokens (warm-papier; contrast-ramp default)
│   └── vendor/                               ← lokaal gevendorde libs (SQL.js, Chart.js, fonts — offline)
├── output/                                   ← werkartefacten per sprint
│   ├── verification/                         ← canonical metrics + SHACL + file-hashes + HermiT-merge (per versie)
│   ├── scripts/                              ← appliers + helpers (per sprint)
│   ├── analysis/                             ← cluster-JSON's + onderzoek (per sprint)
│   └── reports/                              ← sprint-rapporten (pre-sprint / pilot / stap3 / patch-rapport / dashboard)
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

### Dashboard lokaal bekijken (Spoor B)

Het dashboard gebruikt SQL.js en laadt niet vanaf een `file://`-pad — draai een lokale webserver:

```bash
cd dashboard
python3 -m http.server 8100
# open http://127.0.0.1:8100/grc-dashboard-v3-2.html
```

Volledig offline (geen externe requests); representatieve demo-data, geen organisatiedata.

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
| Wegwijzer | `docs/START-HIER.md` | ingang voor (nieuwe) beheerders |
| Projectinstructie | `docs/projectinstructie-v1_12.md` | autoritatief (4 juni 2026) |
| Breed startpunt (overdracht) | `docs/handovers/overdrachtsrapport.md` | beginner-gericht startdocument |
| Master-startprompt | `docs/handovers/bootstrap-masterchat-v7.md` | actuele masterchat-bootstrap |
| SKOS-beoordelings-protocol | `docs/skos-beoordelings-protocol-v1_3.md` | FINAL (T3) |
| Sprint-protocollen | `docs/sprint-protocols.md` | 18 protocollen + v1.3-werkflow-disciplines |
| Patch-rapport v4.6.4 | `output/reports/patch-rapport-v4_6_4.md` | autoritatieve baseline-bron |
| Dashboard-reskin + DORA-correctie | `output/reports/patch-rapport-dashboard-reskin-overzicht.md` | v7 (2 juni) |
| Dashboard-IA-herinrichting | `output/reports/patch-rapport-dashboard-ia-herinrichting.md` | v7 (3 juni) |
| Brain-vault entry | `brain/brain__index.md` | overzicht alle brain-bestanden (iteratie 17) |

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
| Migratie | 26 mei 2026 | Tech/Brein/Dashboard → Claude Code + GitHub-repo | afgerond |
| v4.6.1 (T1) | 26 mei 2026 | SKOS-exactMatch-audit ctrl:↔compl: m10 — 28 herclassificaties | superseded |
| v4.6.2 (T2) | 27 mei 2026 | SKOS-bidirectional-audit m10 — 65 herclassificaties | superseded |
| v4.6.3 (T3) | 28 mei 2026 | SKOS-bidirectional-audit m14 AVG/GDPR — 2 mutaties + Protocol v1.3 FINAL | superseded |
| Reasoner-evaluatie | 29 mei 2026 | H37 + H38 + H41 (alle HOLD; H38 → resolved) | afgerond |
| v4.6.4 (CSF-range-fix) | 29 mei 2026 | DL-conformiteits-fix (2 range-correcties m21) + HermiT-her-run | **productie (stabiel)** |
| Dashboard-revival (Spoor B) | 29 mei 2026 | B7 ontologie-import + Q-M5 vendoring + B9 WCAG + verse-load-fixes | afgerond |
| T4-inventarisatie | 29 mei 2026 | csf↔ISO27001 cross-bron-overlap | afgesloten (Optie B, geparkeerd) |
| **Dashboard-reskin + DORA-correctie (Spoor B)** | **2 juni 2026** | **warm-papier-thema + Overzicht herbouwd + contrast-ramp default + DORA → "referentie · n.v.t."** | **afgerond** |
| **IA-herinrichting (Spoor B)** | **3 juni 2026** | **5→4 tabs (Overzicht · Governance · Compliance · Risk) + gelaagde kader-kiezer (D9) + modalDelete-fix** | **afgerond** |
| **Brein-cyclus iteratie 17** | **4 juni 2026** | **v7-dashboardsessie achteraf officieel gemaakt (geheugen-lag gedicht)** | **afgerond** |

Volledige sprint-detail per sprint: `brain/brain__sprints__*.md`.

---

## Ontwerpbeslissingen + architectuur-items

**12 D-decisions + 1 sub-rule** (allen actief, niet wijzigbaar zonder masterchat-goedkeuring):

D1 OWL 2 DL *(per v4.6.4 versterkt: OWL RL ≡ HermiT empirisch bevestigd, H38 resolved)* · D2 Turtle · D3 11 namespaces · D4 SKOS cross-framework · D4.1 Disclaimer-handling · D5 owl:sameAs strikt ctrl:↔bio: · D6 tweetalige annotaties · D7 BIO 2.0 twee klassen · D8 canonieke SoA · D9 framework-neutraal *(dashboard-kader-kiezer = D9-conform perspectief-mechanisme)* · D10 COSO enterprise-governance · D11 asset-convergentie · D12 drie-laags compliance.

Volledig in `brain/brain__decisions__D-register.md`.

**H-items** (architectuur-overwegingen, geparkeerd of resolved):

H25-H35 (post-v4.3.3 aandachtspunten) · **H36 RESOLVED** (ctrl↔compl SKOS-audit, fully closed via T1+T2+T3) · H37 (open-ontologies MCP — HOLD) · **H38 RESOLVED** (OWL RL ≡ HermiT bevestigd via v4.6.4) · H39 (SHACL-290-uitsplitsing — parked) · H40 (UI-renderdekking Spoor A — parked; **lege-huls-aangrenzing v7, Pad 1/2-besluit open**) · H41 (SKOS-axioma-set-handling — parked, activering = nieuwe D-decision) · H29 (Three Lines Model — future-consideration; **organisatiestructuur-koppeling v7, A/B/C-besluit open**) · H42/H43/H44 (dashboard-landschap-kandidaten, niet geactiveerd).

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

De eerstvolgende activiteit is een van de twee open Spoor-B-besluiten uit de v7-sessie:

1. **Lege-huls-besluit (Pad 1 vs Pad 2)** — de kader-kiezer toont placeholders i.p.v. echte controls/beschrijvingen/eisen. Pad 1 = ontologie-export verrijken (drie lagen, zuiver, kost tijd); Pad 2 = demo-seed verrijken voor BIO 2.0 + ISO 27001/27002 (snel, demo-klaar — geadviseerd nu). Gekoppeld aan H40.
2. **Organisatiestructuur-besluit (A/B/C)** — A generiek / B echte functionele structuur geanonimiseerd (geadviseerd) / C volledig echt (gevoelig, raakt §0.5). Gekoppeld aan H29.

Daarna (geen vaste planning): Protocol v1.3.1-formalisering (cross-category, 2 precedenten) · csf↔ISO27001 cross-category-sprint (eerst 699-vs-494-reconciliatie) · resterende SKOS-kwaliteitsanalyse (m17/m11/m16/fw-niveau) · H33/H34 (m11 NIST SP 800-53) · m01-verificatie (D.7-skill) · explorer-inhaalslag Spoor A.

Zie `docs/projectinstructie-v1_12.md` §"OPENSTAANDE ITEMS" voor de volledige lijst.

---

*Voor sprint-detail: `brain/brain__sprints__<sprint>.md`. Voor architectuur-vragen: brain-vault registers. Voor scope-pauze: masterchat (claude.ai).*
