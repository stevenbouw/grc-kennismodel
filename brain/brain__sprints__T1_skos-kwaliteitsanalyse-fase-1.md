---
type: sprint
id: T1
title: T1 — SKOS-kwaliteitsanalyse Fase 1 (H36-cluster)
status: active
date: 2026-05-26
baseline_from: v4.6.0
baseline_to: v4.6.1
related:
  - v4_6_0_fase-4-ensia-en-volwassenheid
  - D04_skos-cross-framework
  - H36_skos-exactmatch-ctrl-compl-audit
  - H39_shacl-run2-290-false-positives-uitsplitsing
  - skos-beoordelings-protocol
  - parallelle-maturity-clusters
sources:
  - t1-eindrapport-v4_6_1
  - patch-rapport-v4_6_1
  - t1-presprint-inventarisatie-v4_6_0
  - t1-pilot-rapport-stap3-v4_6_0
  - t1-stap4-rapport-v4_6_0
  - skos-beoordelings-protocol-v1_0
chat-sources: []
confidence: high
---

# T1 — SKOS-kwaliteitsanalyse Fase 1 (H36-cluster)

## Status

**Eerste post-migratie productie-sprint** — opgeleverd 26 mei 2026. Patch-release v4.6.0 → v4.6.1. H36-cluster afgehandeld via 28 SKOS-herclassificaties `exactMatch` → `broadMatch` in `m10-nis2-ext.ttl`. Methode-protocol v1.0 vastgesteld als herbruikbare T2/T3-output. Sprint-duur ~5 uur (raming 3-4 uur, +25% door tooling-incident in patch-toepassing).

Sprint-type: **T1 test-sprint** — eerste werkflow-validatie na migratie van Tech/Brein/Dashboard naar Claude Code + GitHub. Bewees in productie dat het Karpathy-pattern + sprint-protocollen-discipline werkt zoals voorzien.

## Scope: H36-cluster — 28 ctrl:↔compl: exactMatch-paren

Pre-sprint-inventarisatie bevestigde:
- 28 paren in `m10-nis2-ext.ttl` (één module)
- Subject-zijde: 28× `ctrl:ISO27002Control`
- Object-zijde: 28× `compl:RegulatoryObligation`
- Geen D5-collisions
- Geen SHACL-shape valideerde op deze paren (Vraag D — bevestigt [[brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing]]-relevantie)

Bredere context: 28 `exactMatch` is 23% van **121 totale ctrl:↔compl:-mappings** (28 exact + 32 close + 60 related + 27 broad in v4.6.0-baseline). Deze 121-set-cardinaliteit werd doorslaggevend bij beoordeling — zie methode-protocol.

## Sprint-uitvoering — vijf stappen

| Stap | Inhoud | Doorlooptijd | Output |
|---|---|---|---|
| 1 | Pre-sprint-inventarisatie (Protocol B) — 5 vragen A-E, read-only | ~15 min | `output/reports/t1-presprint-inventarisatie-v4_6_0.md` |
| 2 | Methode-protocol v1.0 + Steven sign-off op 5 beslis-punten | ~30 min | `docs/skos-beoordelings-protocol-v1_0.md` |
| 3 | Pilot van 5 paren — alle 5 → broadMatch met hoog vertrouwen + evidence-niveau 1 via CBW-Excel | ~75 min | `output/reports/t1-pilot-rapport-stap3-v4_6_0.md` |
| 4 | Resterende 23 paren via cluster-representant + cluster-discipline + 2 edge-cases | ~2 uur | `output/reports/t1-stap4-rapport-v4_6_0.md` |
| 5 | Masterchat-NEN-PK-toets edge-cases T1-021 en T1-023 + scenario-keuze | ~20 min | scenario C — alle 28 broadMatch |
| 6 | Patch-toepassing v4.6.1 (Steven) incl. tooling-incident applier | ~25 min | `output/reports/patch-rapport-v4_6_1.md` |

**Vijf overhandigings-momenten Tech↔Masterchat:** alle succesvol bereikt binnen één werkdag.

## Uitkomst — 28× broadMatch

| Cluster | NIS2-clause | Paren | Pilot/Cluster | Confidence |
|---|---|---:|---|---|
| a | Risicoanalyse + beleidsregels | 1 | pilot (T1-001) | hoog |
| b | Incidentbehandeling | 4 | pilot (T1-010) + 3 cluster | hoog |
| c | Continuïteit + back-up | 3 | representant (T1-014) + 2 cluster | hoog |
| d | Toeleveringsketen | 4 | representant (T1-006) + 3 cluster | hoog |
| e | Verwerving + ontwikkeling | 5 | pilot (T1-024) + 4 cluster | hoog |
| f | Doeltreffendheid-beoordeling | 2 | representant (T1-016) + 1 cluster | hoog |
| g | Cyberhygiëne + opleiding | 1 | pilot (T1-020) | hoog |
| h | Cryptografie | 1 | edge-case (T1-023) — NEN-PK-toets | hoog |
| i | Personeel + toegang + activa | 6 | pilot (T1-002) + 5 cluster | hoog |
| j | Multi-factor auth | 1 | edge-case (T1-021) — NEN-PK-toets | hoog |
| **Totaal** | | **28** | | **28× broadMatch** |

Volledige paren-lijst staat in `output/reports/t1-eindrapport-v4_6_1.md` §3.2.

## Triple-impact v4.6.0 → v4.6.1

| Metric | v4.6.0 | v4.6.1 | Δ |
|---|---:|---:|---:|
| Pre-inf triples | 20.950 | 20.950 | 0 |
| Post-inf triples | 44.907 | 44.907 | 0 |
| `skos:exactMatch` | 46 | 18 | **−28** |
| `skos:broadMatch` | 38 | 66 | **+28** |
| SKOS-totaal | 1.798 | 1.798 | 0 |
| `owl:Nothing` post-inf | 0 | 0 | 0 |
| `owl:sameAs` (D5+D11) | 98 | 98 | 0 |
| SHACL RUN 1 / RUN 2 | 0 / 290 | 0 / 290 | 0 / 0 |
| Klassen / NamedIndividuals / OP / DP | onveranderd | onveranderd | 0 |

**Predicate-mutatie zonder triple-totaal-impact** — 28 triples van predicate veranderd, geen triple toegevoegd of verwijderd. Eén module geraakt (`m10-nis2-ext.ttl` hash `78b8ee44...` → `cb2d567b...`). 21 andere modules + `grc-shacl.ttl` bytewise identiek aan v4.6.0.

## Drie belangrijke bevindingen

### 1. Evidence-niveau-1-bron via CBW-Excel

CBW-Excel sheet "Mapping Uitvoeringsverordening" (`sources/adr-norea/`) bleek **ENISA TIG v1.0 mapping-tabel te reproduceren** — autoritatieve bron NIS2 ↔ ISO 27002:2022 mapping op clausule-niveau. Bewijsketen NIS2-richtlijn (EU) 2022/2555 art.21 → UV (EU) 2024/2690 considerans (3) → UV-Annex → ENISA TIG v1.0 juni 2025 → CBW-Excel-reproductie. Tilt evidence-niveau van 3/4 naar 1 voor alle 28 paren.

### 2. ENISA-disclaimer-categorisch-effect

ENISA TIG regel 285: *"The mapping should not be interpreted as a measure of equivalency among different standards or frameworks."* Autoritatieve bron erkent relatie maar verbiedt equivalence-interpretatie expliciet. Ondergraaft `skos:exactMatch` als juiste SKOS-keuze zelfs bij volledig sluitende C1-C3-toets. `broadMatch`/`closeMatch` is D4-conforme interpretatie.

**Generaliseerbaarheid:** vermoedelijk patroon-standaard voor cross-norm-mapping-bronnen (NIST OLIR, ISO Annex F, andere mapping-publicaties). D4-aanvulling-overweging open voor T2-voorbereiding — zie [[brain__concepts__mapping-bron-disclaimer-effect]] *(iteratie 13)*.

### 3. NEN-PK-werkverdeling Tech ↔ Masterchat als nieuw werkflow-patroon

NEN-restrictieve bronnen (ISO 27002:2022) zijn niet lokaal beschikbaar in Tech-omgeving. Tech kan C1/C3 niet hard maken zonder ISO-tekst-toegang. Werkverdeling die in T1 werkte:

- **Tech (Claude Code):** ABox-extractie, label-vergelijking, 121-set-cardinaliteit, UV-decompositie
- **Masterchat (claude.ai):** NEN-tekst-toetsing via project knowledge, bilaterale containment, edge-case-judgement

Geformaliseerd in [[brain__workflow__sprint-protocollen]] Protocol 17 *(iteratie 13)*.

## H-impact

| H | Status vóór T1 | Status na T1 | Mutatie |
|---|---|---|---|
| [[brain__architecture__H36_skos-exactmatch-ctrl-compl-audit]] | parked | **closed** | afgehandeld via 28 broadMatch + patch v4.6.1 |
| [[brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing]] | parked | parked + versterkt | T1-inventarisatie Vraag D bevestigde SHACL-blinde vlek op alle 28 ctrl:↔compl: paren |
| H15, H21, H25-H35, H37, H38, H40 | per H-register | ongewijzigd | — |

**Kandidaat-nieuw H-item (NIET geregistreerd):** SKOS-axioma-set / `skos:S46` symmetrie — owlrl-package laadt geen SKOS-axiomas, dus `skos:exactMatch is owl:SymmetricProperty` wordt niet geïnferreerd. Alle 28 mappings asymmetrisch gemodelleerd (0 inverse). Status: T1-werkflow-leerpunt. Trigger voor herregistratie: overstap-besluit owlrl-incl-SKOS.

## D-impact — D4-conformance verbetering

Alle 12 D-decisions blijven conform. **D4 specifiek verbeterd:** `exactMatch` was te sterk geclaimd voor 28 paren waar autoritatieve bron (ENISA TIG) equivalence expliciet ontkent. Herclassificatie naar `broadMatch` is D4-conforme interpretatie.

| D | Conformance | Detail |
|---|---|---|
| D1 OWL 2 DL | ✓ ongewijzigd | Geen TBox-wijziging |
| D2 Turtle-serialisatie | ✓ ongewijzigd | Enige m10-wijziging |
| D3 11 namespaces | ✓ ongewijzigd | Geen nieuwe namespace |
| **D4 SKOS cross-framework** | ✓ **verbetering** | exactMatch was te sterk; broadMatch D4-conform |
| D5–D12 | ✓ ongewijzigd | Geen impact |

**D4-aanvulling-overweging open:** ENISA-disclaimer-categorisch-effect als generaliseerbare regel. Niet T1-scope; masterchat-beslissing op moment van T2/T3.

## Methode-protocol v1.0 — herbruikbaar voor T2/T3

Zie [[brain__concepts__skos-beoordelings-protocol]] voor concept-overzicht. Operationeel document blijft `docs/skos-beoordelings-protocol-v1_0.md`. Vier-criteria-set (C1 definitioneel, C2 cardinaliteit, C3 inclusie-richting, C4 bron-evidence) + beslis-tabel + evidence-hiërarchie + cluster-discipline + twijfelgevallen-procedure. In productie gevalideerd op 28 paren.

Aanbevelingen voor v1.1-evolutie bij T2-start:
- C2-toets binnen bredere mapping-cluster (121-set), niet alleen exactMatch-subset (28-set)
- ENISA-disclaimer-soort-handling als D4-overweging
- NEN-PK-werkverdeling als expliciete procedure-stap
- Tech levert werkende applier (geen alleen-specificatie)

## Werkflow-validatie T1-test-doel

| Werkflow-aspect | Bevinding |
|---|---|
| Pre-sprint-inventarisatie (Protocol B) | werkte als gepland; 0 stop-condities |
| Sample-first met cluster-spreiding | werkte; pilot leverde structureel inzicht |
| Cluster-discipline | werkte; geen half-half-cluster-behandeling |
| Edge-case-escalatie naar masterchat | werkte; twee-zijdige analyse-format effectief |
| NEN-PK-werkverdeling Tech↔Masterchat | werkte; nieuw werkflow-patroon vastgesteld |
| Vijf overhandigings-momenten | alle vijf bereikt; sprint binnen één dag voltooid |
| Protocol 14 pre-push disclosure-check | eerste productie-toepassing; ~3 min per rapport; geen vondsten |

Drie concrete sprint-protocol-uitbreidingen geformaliseerd in [[brain__workflow__sprint-protocollen]] iteratie 13:
- Protocol 15 — Tech levert werkbare applier (niet alleen specificatie)
- Protocol 16 — Lokatie verificatie-scripts expliciet in patch-rapport §9
- Protocol 17 — NEN-werkverdeling Tech↔Masterchat

## Sprint-duur-evaluatie

| Stap | Geraamd | Werkelijk |
|---|---:|---:|
| Stap 1 inventarisatie | 15 min | 15 min |
| Stap 2 protocol-draft + sign-off | 30 min | ~30 min |
| Stap 3 pilot | 75 min | ~75 min |
| Stap 4 resterende 23 + patch-voorbereiding | 75-90 min | ~2 uur |
| Stap 5 NEN-PK-toets | n.v.t. | ~20 min |
| Stap 6 patch-toepassing | n.v.t. | ~25 min (incl. applier-incident) |
| **Totaal** | **~3-4 uur** | **~5 uur** |

T2/T3-planning: ~5-6 uur als realistische sprint-duur voor analoge scope (~30 paren).

## Productie-fase actief

T1 markeert formele start van productie-fase. Migratie + polish (iteratie 12) + T1 zijn alle voltooid. v4.6.1 is autoritatief voor brain-vault-baseline.

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-26 | active | Oplevering T1-sprint — H36-cluster afgehandeld via 28× broadMatch; patch v4.6.1; methode-protocol v1.0 vastgesteld; productie-fase actief |

## Cross-references

- [[brain__sprints__v4_6_0_fase-4-ensia-en-volwassenheid]] — voorganger (v4.6.0-baseline waarop T1 patcht)
- [[brain__decisions__D04_skos-cross-framework]] — D-decision waarbinnen T1 opereert; D4-conformance specifiek verbeterd
- [[brain__architecture__H36_skos-exactmatch-ctrl-compl-audit]] — H-item afgehandeld in deze sprint
- [[brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing]] — versterkt door T1-inventarisatie Vraag D
- [[brain__concepts__skos-beoordelings-protocol]] — methode-concept (nieuw iteratie 13)
- [[brain__concepts__mapping-bron-disclaimer-effect]] — ENISA-disclaimer-patroon (nieuw iteratie 13)
- [[brain__concepts__parallelle-maturity-clusters]] — architectuur-context (D9-cluster van v4.6.0)
- [[brain__workflow__sprint-protocollen]] — drie nieuwe protocollen 15/16/17 geformaliseerd uit T1-leerpunten
- [[brain__modules__M10_nis2-ext]] — module waarop patch v4.6.1 is toegepast

— Einde T1.
