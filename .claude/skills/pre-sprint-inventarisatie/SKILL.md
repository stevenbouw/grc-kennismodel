---
name: pre-sprint-inventarisatie
description: Generate the canonical §0-§9 pre-sprint-inventarisatie skeleton (Protocol 1) for a new T-sprint in output/reports/tX-pre-sprint-inventarisatie.md. Enforces: §2 ABox-baseline uit canonical_metrics_v(Y-1).json (niet uit memorie — leerpunt v4.3.3 / Protocol v1.3 §10.4), §3+§4 metrics-scope-annotatie (Protocol v1.3 §10.5), §6 sample-keuze zonder pre-pilot-uitkomst (Protocol v1.3 §6 stop-conditie-4), bottom-up bouw (Protocol v1.3 §10.2). READ-ONLY skelet-generator — geen ABox-mutatie, geen auto-execute, geen autonome scope-keuze. Use when starting a new T-sprint na masterchat-scope-vaststelling en vóór Stap-2-pilot.
---

# pre-sprint-inventarisatie — canoniek §0-§9-skelet (Protocol 1)

Genereert het pre-sprint-inventarisatie-skelet voor T-sprints. Codificeert Protocol 1 + Protocol v1.3 §6 (sample-keuze) + §10.2-§10.5 (rapport-discipline) + Protocol v1.3 §2.2-§2.4 (cluster-cardinaliteit + evidence-niveau).

§0.5-firewall: dit is een SKELET-GENERATOR, geen sprint-uitvoerder. Geen ABox-mutaties, geen auto-execute, geen autonome scope-keuze. Masterchat blijft scope-vaststeller; Tech vult het skelet read-only.

## Wanneer aanroepen

- Bij start van een nieuwe T-sprint (T4, T5, T6, ...)
- Na masterchat-scope-instructie en vóór Stap-2-pilot
- Bij her-inventarisatie als sprint-scope wijzigt tijdens uitvoering

## Vereiste input (van masterchat-instructie)

- Sprint-naam (T4 / T5 / ...)
- Scope-module(s) (`m11-bio` / `m14-avg-gdpr` / `m16-nis2` / `m17-dora` / ...)
- Audit-richting (`ctrl→compl` of `compl→ctrl` of `ctrl→ctrl` cross-framework)
- Baseline-versie (`v4.X.(Y-1)` — bv. v4.6.3 voor T4)

## Dependencies (referentieel — niet auto-uitvoeren)

| Bron | Rol |
|---|---|
| `/canonical-metrics` skill + `output/verification/canonical_metrics_v(Y-1).json` | ABox-baseline §2 |
| `/shacl-split` skill + `output/verification/shacl_results_v(Y-1).json` | SHACL-baseline (drift-bewaking) |
| `docs/skos-beoordelings-protocol-v1_3.md` | Sample-keuze + werkflow-discipline |
| `brain/brain__decisions__D-register.md` + `/ontology-conformance` skill | D1-D12 + D4.1-context |
| `docs/sprint-protocols.md` | Protocol 1 + Protocol 13 + Protocol 16 + Protocol 17 |

## Bottom-up bouw-volgorde (Protocol v1.3 §10.2)

| Volgorde | Sectie | Reden |
|---|---|---|
| 1 | §2 ABox-baseline (JSON-citaten) | Feitelijke fundament |
| 2 | §3 Cluster-cardinaliteit per module | Volgt uit §2 |
| 3 | §4 Evidence-coverage pre-check | Volgt uit §3 |
| 4 | §5 Risico-inventarisatie + stop-condities | Volgt uit §3-§4 |
| 5 | §6 Sample-keuze-voorstel | Volgt uit §3-§5 |
| 6 | §7 Verwachte uitkomst (indicatief) | Synthese §2-§6 |
| 7 | §8 GO/NO-GO-criteria | Synthese §2-§7 |
| 8 | §9 Hand-off + Deliverables-tabel | Eindstaat |
| 9 | §1 Scope-bevestiging LAATST | Afgeleid (markeer §1-vroeg-invul "INITIEEL — TE BEVESTIGEN IN §3-§5-ITERATIE") |
| 10 | §0 Frontmatter LAATST | Synthese-veld |

## Canoniek §-skelet voor de gegenereerde inventarisatie

```markdown
---
type: report
subtype: pre-sprint-inventarisatie
sprint: T<N>
baseline_from: v4.X.(Y-1)
date: YYYY-MM-DD
status: final-awaiting-masterchat-review
mode: READ-ONLY
related:
  - skos-beoordelings-protocol-v1_3
  - <relevante H-items / D-decisions / modules>
scope: "<sprint-naam> pre-sprint-inventarisatie — <kort doel>"
---

# T<N> Pre-sprint-inventarisatie-rapport

## §1. Scope-bevestiging (sprint-doel + instructie-§-naar-doel-mapping)

**INITIEEL — bottom-up te bevestigen via §3-§5-iteratie.**

| Aspect | Bevinding | Bron |
|---|---|---|
| Sprint-scope-module(s) | <m14-avg-gdpr / ...> | masterchat-instructie §<N> |
| Audit-richting | <compl→ctrl / ...> | masterchat-instructie §<N> |
| Totaal in-scope-paren | <N> | §3.1 helper-script-output |
| Baseline | v4.X.(Y-1) | `canonical_metrics_v(Y-1).json` |
| Predicate-types in scope | <closeMatch / broadMatch / relatedMatch / ...> | §2.2 |

## §2. ABox-baseline (UIT canonical_metrics JSON — NIET uit memorie)

### §2.1 Globale telling vorige baseline
<tabel uit `output/verification/canonical_metrics_v(Y-1).json`>

| Metric | v(Y-1) | Scope |
|---|---:|---|
| triples (pre-inference) | N | global |
| owl:Class | N | global |
| owl:NamedIndividual | N | global |
| skos_mappings_total | N | global |
| skos.exactMatch | N | global |
| skos.closeMatch | N | global |
| skos.broadMatch | N | global |
| skos.relatedMatch | N | global |
| D5 ctrl↔bio | N (=93 target) | D5-conformance |
| D11 asset-brug | N (=5 target) | D11-conformance |

### §2.2 SKOS-predicate-tellingen — module-in-scope
<tabel uit canonical_metrics_v(Y-1).json `skos_mapping_pairs`-veld of aparte SPARQL>

(Protocol v1.3 §10.5: scope-annotatie verplicht — bv. "m14-only" / "compl→ctrl-richting only")

### §2.3 Richting-consistentie
<bevestig 100% scope-richting; flag tegen-richting indien aanwezig>

## §3. Cluster-cardinaliteit per module-in-scope (Protocol v1.3 §2.2)

### §3.1 Subject-zijde clusters
<bv. AVG-artikelen, ISO-controls, etc. — N clusters; per cluster grootte>

### §3.2 Object-zijde clusters
<verplicht expliciet: 1↔veel-patroon / veel↔1-patroon — Protocol v1.3 §3.1 selecteert cluster-doel-predicate-pad anders>

### §3.3 Heterogeniteit-overzicht
<homogeen vs heterogeen per cluster — Protocol v1.3 §3.3>

## §4. Evidence-coverage pre-check (Protocol v1.3 §2.4 + Protocol 17)

### §4.1 Bron-overzicht
<per cluster: welke bronnen geven evidence — ISO 27002 / 27701 / CBW / AVG / etc.>

### §4.2 Evidence-niveau-1-pre-stap
<Protocol v1.3 §2.4: aantal paren met directe niveau-1 evidence vóór per-paar-toetsing>

### §4.3 Bron-toegankelijkheid (Protocol 17 NEN-werkverdeling)
| Bron | Lokale toegang | Locatie |
|---|---|---|
| ISO 27002:2022 | ✅ / ❌ | `/Users/stevenbouwmeester/grc-sources-licensed/...` |
| ISO 27701:2025 | ✅ / ❌ | ... |
| ... | ... | ... |

(Bij ❌: scope-pauze of masterchat-bron-aanlevering — Protocol 17)

## §5. Risico-inventarisatie + stop-condities-voorstel (Protocol v1.3 §6)

### §5.1 Methodische risico's
<bv. SHACL-blinde vlek, evidence-niveau-asymmetrie, cross-category-risico>

### §5.2 Stop-condities-voorstel
- Stop-conditie A: <bv. helper-script-discrepantie >5% met handmatige raming>
- Stop-conditie B: <evidence-niveau-3 percentage >X%>
- Stop-conditie C: <D-conformance-vermoeden>
- Stop-conditie D: <SHACL drift A>0 of B>0>

## §6. Sample-keuze-voorstel (Protocol v1.3 §6)

### §6.1 Sample-grootte + spreiding
<5-10 paren met spreiding over: predicate-types, cluster-soorten, evidence-niveaus, subject/object-anchor-varianten>

### §6.2 Sample-paren-tabel
| # | Subject | Predicate (current) | Object | Cluster | Evidence-niveau (pre-pilot raming) | Onderbouwing keuze |
|---|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... | ... |

(Protocol v1.3 §6 stop-conditie-4: GEEN pre-pilot-uitkomst-classificatie per paar — alleen evidence-niveau raming, geen predicate-mutatie-voorstel)

### §6.3 Spreidings-verantwoording
<expliciet: hoe sample alle relevante variatie dekt>

## §7. Verwachte uitkomst (indicatief — GEEN pre-classificatie-mandaat)

<bv. "verwachten X behoud, Y mutatie-kandidaten, op basis van cluster-analyse §3 + evidence-pre-check §4 — uitkomst per paar wordt in pilot vastgesteld">

Protocol v1.3 §6 stop-conditie-4-discipline: indien §7 een PER-PAAR-uitkomst suggereert → corrigeer naar AGGREGATE indicatie.

## §8. GO/NO-GO-criteria (expliciet — masterchat-eindbesluit)

| # | Criterium | Status (pre-pilot) |
|---|---|---|
| 1 | Scope (N paren) bevestigd in §1 | ✅ / ⚠️ |
| 2 | ABox-baseline cijfers consistent (§2) | ✅ |
| 3 | Cluster-cardinaliteit gemeten (§3) | ✅ |
| 4 | Evidence-pre-check uitgevoerd (§4) | ✅ |
| 5 | Risico-/stop-condities expliciet (§5) | ✅ |
| 6 | Sample-keuze onderbouwd (§6) | ✅ |
| 7 | Geen onbevestigde scope-aannamen | ✅ / ⚠️ |
| 8 | Bron-toegankelijkheid voldoende (§4.3) | ✅ / ⚠️ |

Bij ⚠️: scope-pauze of toelichting in §5 + §9.

## §9. Hand-off + Deliverables-tabel (Protocol 16) + verwijzingen

### §9.1 Hand-off-checklist
- [ ] Wat klaarligt voor masterchat-besluit
- [ ] Verwachte vervolgstappen (Stap 2 pilot, Stap 3 hoofd-uitvoering, ...)
- [ ] Open vragen / aandachtspunten

### §9.2 Deliverables (Protocol 16)
| Type | Lokatie | Beschrijving |
|---|---|---|
| Inventarisatie | `output/reports/t<N>-pre-sprint-inventarisatie.md` | Dit document |
| ABox-baseline | `output/verification/canonical_metrics_v(Y-1).json` | Bron §2 |
| SHACL-baseline | `output/verification/shacl_results_v(Y-1).json` | Drift-referentie |

### §9.3 Verwijzingen
- Sprint-instructie: `docs/instructies/instructie-t<N>-...md`
- Protocol v1.3: `docs/skos-beoordelings-protocol-v1_3.md`
- D-register: `brain/brain__decisions__D-register.md`
- Voorgaande T-sprints: `output/reports/t<N-1>-...`

— Einde pre-sprint-inventarisatie T<N>.
```

## Afgedwongen disciplines

- **§2 dwingend uit JSON**: open `canonical_metrics_v(Y-1).json`, citeer rechtstreeks `global_pre_inference.*`. Niet uit memorie (leerpunt v4.3.3 / Protocol v1.3 §10.4 helper-script-autoritatief).
- **§3+§4 metrics-scope-annotatie**: Protocol v1.3 §10.5 — elke tabel-titel of -caption noemt scope expliciet (`m14-only`, `compl→ctrl`, `cumulatief T-X+T-(X-1)`, ...).
- **§6 sample-keuze**: GEEN pre-pilot-uitkomst-classificatie per paar (Protocol v1.3 §6 stop-conditie-4). Alleen evidence-niveau-raming, geen predicate-mutatie-voorstel.
- **§1 vroeg-invullen**: markeer "INITIEEL — TE BEVESTIGEN IN §3-§5-ITERATIE" bij bottom-up bouw.
- **Bron-typo-beleid (Protocol 13)**: typo in nieuwe-individu rdfs:label corrigeren; typo in referentie-target behouden.
- **NEN-parafrase (Protocol 17)**: NEN-tekst NOOIT verbatim in rapport; alleen parafrase + clausule-verwijzing.

## Mapping naar sprint-specifieke vraag-thema's (T2/T3-precedent)

De §0-§9 zijn de GENERIEKE inventarisatie-secties. Masterchat-instructies voor sprints leggen vaak sprint-specifieke vraag-thema's op (bv. T2/T3 "Vraag A-F"). Mapping:

| Generieke skill-§ | T2/T3-precedent (Vraag A-F-format) |
|---|---|
| §1 Scope-bevestiging | T-Vraag A (Scope-bevestiging) + T-§1 Samenvatting |
| §2 ABox-baseline | impliciet binnen T-Vraag A + canonical_metrics-citaten in T-tabellen |
| §3 Cluster-cardinaliteit | T-Vraag B (Cluster-structuur) |
| §4 Evidence-coverage | T-Vraag C (Bron-structuur) + T-Vraag D (Evidence-coverage per paar) + T-Vraag E (Bron-toegankelijkheid) |
| §5 Risico-inventarisatie | T-Vraag F (Methode-check) + T-Tech-observaties |
| §6 Sample-keuze | T-Pilot-sample-aanbeveling |
| §7 Verwachte uitkomst | impliciet binnen T-§1 Samenvatting |
| §8 GO/NO-GO | T-Hand-off-checklist (deel) |
| §9 Hand-off + Deliverables | T-Hand-off-checklist (deel) + T-Verwijzingen |

**Werkwijze:** als masterchat een sprint-specifieke vraag-A-F-format voorschrijft, voer de inventarisatie uit in dat format MAAR borg dat alle §0-§9-secties (semantisch) gedekt zijn. Skill-§-secties zijn de canonieke CHECKLIST; sprint-format mag afwijken zolang alle §-content aanwezig is.

## Wat de skill NIET doet

- Geen ABox-mutaties
- Geen autonome scope-keuze (masterchat-werk)
- Geen auto-execute van canonical-metrics of SHACL-scripts (alleen referentie)
- Geen autonome commit (Steven commit handmatig — §0.5-firewall)
- Geen invulling van inhoudelijke §3.x / §4.x / §6.x — dat is sprint-specifiek werk
- Geen NEN-verbatim-tekst — Protocol 17 parafrase-discipline geldt
- Geen pre-pilot-uitkomst-classificatie per paar (Protocol v1.3 §6 stop-conditie-4)

## Cross-references

- Canonical metrics: `.claude/skills/canonical-metrics/`
- SHACL split: `.claude/skills/shacl-split/`
- Patch-rapport: `.claude/skills/patch-rapport/`
- Rapport-discipline (Protocol v1.3 §10.x + Protocol 13/14/16): `.claude/skills/report-structure/`
- D-conformance checklist: `.claude/skills/ontology-conformance/`
- Sprint-protocollen (autoritatief): `docs/sprint-protocols.md`
- Protocol v1.3 (volledige tekst): `docs/skos-beoordelings-protocol-v1_3.md`
- T-precedenten: `output/reports/t1-presprint-inventarisatie-v4_6_0.md`, `t2-pre-sprint-inventarisatie.md`, `t3-pre-sprint-inventarisatie.md`
