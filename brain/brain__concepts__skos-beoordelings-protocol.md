---
type: concept
title: SKOS-beoordelings-protocol — Methode voor bidirectional match-type-evaluatie
status: living
date: 2026-05-27
related:
  - D04_skos-cross-framework
  - T1_skos-kwaliteitsanalyse-fase-1
  - T2-skos-bidirectional-audit-m10
  - H36_skos-exactmatch-ctrl-compl-audit
  - H41_skos-axioma-set-handling
  - mapping-bron-disclaimer-effect
  - cluster-discipline-bewijslast
  - cross-bron-overlap
sources:
  - skos-beoordelings-protocol-v1_0
  - skos-beoordelings-protocol-v1_2
  - skos-beoordelings-protocol-v1_3
  - t1-eindrapport-v4_6_1
  - patch-rapport-v4_6_2
  - t2-stap3-eindrapport
  - t2-pilot-rapport
chat-sources: []
confidence: high
---

# SKOS-beoordelings-protocol — Methode voor bidirectional match-type-evaluatie

## Wat het is

Een **herbruikbare methode** om voor SKOS-mapping-paren (`skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`, `skos:narrowMatch`, `skos:relatedMatch`) consistent en repliceerbaar te beoordelen of de gekozen match-type D4-conform is, of dat herclassificatie nodig is. Het protocol is **bidirectional** sinds v1.2 — toetst zowel downgrade (te sterk geclaimd) als upgrade (te zwak geclaimd) als richtings-correctie (broadMatch ↔ narrowMatch) als behoud.

**Versie-evolutie:**

- **v1.0** vastgesteld 26 mei 2026 voor T1-sprint, downgrade-georiënteerd; in productie gevalideerd op 28 `exactMatch`-paren (H36-cluster, allen → broadMatch)
- **v1.1** DRAFT (downgrade-georiënteerd, nooit operationeel — vervangen door v1.2)
- **v1.2** vastgesteld 27 mei 2026 voor T2-sprint, bidirectional; in productie gevalideerd op 118 m10-paren over 10 NIS2-clusters (65 mutaties: 32 downgrade + 33 upgrade)
- **v1.3** DRAFT 27 mei 2026, vaststelling pending bij eerstvolgende sprint-scoping (T3 of m14)

**Onderscheid:**

- **Operationeel document:** `docs/skos-beoordelings-protocol-v1_3.md` (DRAFT) + `docs/skos-beoordelings-protocol-v1_2.md` (T2-autoritatief) — autoritatieve instructie voor Tech-subagent
- **Dit concept-bestand:** methode-overzicht + architectuur-context + T-sprint-toepassings-precedenten + roadmap

Bij conflict tussen beide: operationeel document prevaleert.

## Kern — vier criteria + beslis-tabel + cluster-discipline

Een `skos:exactMatch` is verdedigbaar **alleen wanneer alle vier criteria gelden**:

| Criterium | Toets |
|---|---|
| **C1** Definitionele overlap | A dekt volledige reikwijdte van B én B dekt volledige reikwijdte van A volgens bron-definities |
| **C2** Cardinaliteit | Geen veel-op-één of één-op-veel binnen mapping-set; check **óók buiten de huidige subset** (bv. binnen bredere ctrl:↔compl: 121-set, niet alleen exactMatch-28-set) |
| **C3** Inclusie-richting | Bilaterale containment A ⊆ B EN B ⊆ A volgens definitie-content |
| **C4** Bron-bewijs | Autoritatieve mapping-bron ondersteunt "exact" expliciet (evidence-niveau ≤ 2) |

Bij failure op één of meer criteria volgt **herclassificatie volgens beslis-tabel**:

| Failure-modus | Aard | Herclassificatie |
|---|---|---|
| C1: A enger dan B | Definitionele subset | `A skos:broadMatch B` |
| C1: Partiële overlap zonder subset | Thematische verwantschap | `A skos:closeMatch B` |
| C1: Zwakke definitionele overlap | Domein-overlap minimaal | `A skos:relatedMatch B` |
| C2: veel→1 cluster | Cardinaliteit-failure | Per A: `A skos:broadMatch B` |
| C2: 1→veel cluster | Cardinaliteit-failure | Per B: `A skos:narrowMatch B` |
| C3: A enger dan B | Subset expliciet | `A skos:broadMatch B` |
| C3: A breder dan B | Subset expliciet | `A skos:narrowMatch B` |
| C4: evidence-niveau 3-4 + C1-C3 niet sluitend | Onvoldoende bron-bewijs | Twijfelgevallen-lijst → masterchat-escalatie |

## Evidence-hiërarchie

| Niveau | Bron-type | Voorbeeld |
|---|---|---|
| 1 | Expliciete mapping in autoritatief mapping-document | ENISA TIG v1.0 (via CBW-Excel); NIST OLIR; ISO Annex F |
| 2 | Norm-tekst identiek aan beide kanten | Zelden cross-norm; vaker binnen één framework |
| 3 | Definitie-overlap via rdfs:comment of bron-tekst | rdfs:comment-vergelijking in module |
| 4 | Onderwerp-titel-overlap | rdfs:label-vergelijking (zwakste, vaak misleidend) |

**T1-empirie:** evidence-niveau 1 was haalbaar voor alle 28 paren via CBW-Excel sheet "Mapping Uitvoeringsverordening" (reproductie van ENISA TIG v1.0). Voor T2/T3 wordt **standaard `sources/`-doorzoek op cross-walk-Excels** aanbevolen als pre-Stap-3-actie.

## Cluster-discipline (verplicht)

Bij C2-failure is herclassificatie **systematisch binnen het cluster**. Alle paren in dezelfde veel→1-cluster krijgen dezelfde behandeling tenzij voor een specifiek paar een individuele uitzondering aantoonbaar is. Bewijslast voor uitzondering: expliciete motivering met evidence-niveau 1-bron of escalatie naar twijfelgevallen.

Voorkomt half-half cluster-behandelingen die downstream inconsistenties veroorzaken (T1-leerpunt 1: cluster-representant-aanpak leverde 18 cluster-volger-paren in ~30 min in plaats van ~3 uur).

## Twijfelgevallen-procedure

Paren gaan naar twijfelgevallen-lijst (escalatie naar masterchat) wanneer:

- Evidence-niveau 3-4 én C1/C3-toets niet sluitend
- Cardinaliteit-twijfel: paar lijkt 1→1 binnen subset maar heeft buiten-set-mappings die patroon ondergraven
- Cross-norm-interpretatie nodig: NEN-restrictieve bron vereist (Tech kan niet toetsen)
- Tech-confidence "laag" op één of meer criteria
- Individuele uitzondering claim binnen cluster

**Format (verplicht):** twee-zijdige analyse (pro-broadMatch én pro-exactMatch-behoud) zonder Tech-voorstel. Masterchat verzorgt NEN-tekst-toetsing via project knowledge en beslist (T1-leerpunt 4: NEN-PK-werkverdeling; zie [[brain__workflow__sprint-protocollen]] Protocol 17).

## T1-toepassing — alle 28 paren broadMatch

Het protocol v1.0 leverde 28× broadMatch met hoog vertrouwen. Doorslaggevend voor 1→1-paren binnen 28-set: **C2-toets binnen bredere 121-set ctrl:↔compl:-mappings**, niet alleen exactMatch-subset. Bevestigd patroon: ENISA-disclaimer-categorisch-effect ondergraaft `exactMatch` zelfs bij sluitende C1-C3 (zie [[brain__concepts__mapping-bron-disclaimer-effect]]).

## T2-toepassing — 65 bidirectional mutaties over 10 clusters (Protocol v1.2)

Protocol v1.2 (bidirectional uitbreiding) in productie gevalideerd op 118 m10-paren over 10 NIS2-art.21-letter-clusters. Per patch-rapport v4.6.2 + Stap 3-eindrapport:

| Aspect | Waarde |
|---|---:|
| Beoordeelde paren m10 | 118 |
| Patch-mutaties | 65 (32 downgrade + 33 upgrade) |
| Behoud (al broadMatch) | 53 |
| Clusters convergent → broadMatch | 10/10 |
| Heuristiek-flags | 10 (op 6 cluster-leden) |
| NEN-aantoonbare uitzonderingen | 0 |
| Confidence-distributie | 65× hoog |
| Evidence-niveau cluster-niveau | 10× niveau 1 (CBW-Mapping-UV reproduceert ENISA TIG v1.0) |
| D4.1-disclaimer-cluster-niveau-toepassing | 10× (één bevestiging per cluster bij homogene bron-stack) |

**Bidirectional symmetrie-bewijs:** zowel upgrades als downgrades treden op binnen één cluster (bv. NIS2_a met 4 downgrade + 4 upgrade + 4 behoud). Geen downgrade-bias zoals v1.1-draft veronderstelde. Drie verschillende mutatie-richtingen convergeren naar één cluster-doel-predicate. Protocol v1.2's §3.1 predicate-doel-tabel + §3.2 sterkte-ordening symmetrisch toepasbaar.

## Bidirectional-audit-symmetrie *(sub-aspect Protocol v1.2 §3.1-§3.2)*

Onder v1.0 was het protocol downgrade-georiënteerd (te sterke `exactMatch`-claims neutraliseren). v1.2 maakt het protocol symmetrisch: dezelfde predicate-doel-tabel toetst zowel onder- als overclaim.

**Predicate-sterkte-ordening (Protocol v1.2 §3.2):**

```
sterkste   exactMatch
           closeMatch
           broadMatch  ≈  narrowMatch    (parallel, niet onderling vergelijkbaar)
zwakste    relatedMatch
```

**Mutatie-richting-classificatie:**

| Huidige → Doel | Richting |
|---|---|
| Sterker → zwakker (bv. closeMatch → broadMatch) | **downgrade** |
| Zwakker → sterker (bv. relatedMatch → broadMatch) | **upgrade** |
| broadMatch ↔ narrowMatch (subset-richting omgekeerd) | **richtings-correctie** |
| Huidige = doel | **behoud** |
| Geen verdedigbare relatie | **verwijderen** (zeldzaam) |

**T2-empirisch bewijs voor symmetrie:**

- 32 downgrade (closeMatch → broadMatch) — Protocol v1.2 detecteert overclaim
- 33 upgrade (relatedMatch → broadMatch) — Protocol v1.2 detecteert onderclaim
- 0 richtings-correctie / verwijdering / twijfel
- Per-cluster-distributie toont alle drie mutatie-richtingen tegelijk (NIS2_a: 4+4+4; NIS2_e: 7+4+6; NIS2_i: 12+11+9)

**Confidence-observatie (Protocol v1.2 → v1.3-criterium):** upgrade-paren krijgen geen lagere confidence dan downgrade-paren bij cluster-discipline-overerving. Pilot leverde middel-confidence op upgrade-paren (T2-S05, T2-S08-alt) waar cluster-overerving spanning had met individuele beoordeling; Stap 3 leverde uitsluitend hoge confidence omdat cluster-overerving consistent gold zonder spanning.

**Symmetrie-toepassing buiten T2-context:** symmetrie geldt structureel, ook in toekomstige m14-sprint (compl→ctrl-richting). Asymmetrie zou alleen optreden bij D4.1-disclaimer-toetsing (D4.1 blokkeert alleen `exactMatch`, andere upgrades zijn niet door D4.1 beperkt).

## Cluster-discipline-bewijslast — zie eigen concept

De bewijslast-asymmetrie voor cluster-uitzonderingen is operationeel cruciaal voor symmetrische toepassing. Streng bewijs vereist voor zowel sterker- als zwakker-mapping-uitzondering; geen bewijs voor cluster-default. Empirisch gevalideerd in T2: 10 heuristiek-flags, 0 succesvolle uitzonderingen.

Volledige domein-uitleg + drie scenario's: zie [[brain__concepts__cluster-discipline-bewijslast]] *(nieuw iteratie 14)*.

## T3 + m14-relevantie

Protocol is **herbruikbaar** voor andere SKOS-clusters in de 1.798-mappings-totaal:

| Kandidaat | Omvang | Karakteristiek |
|---|---:|---|
| m14-AVG/GDPR-cluster | 31 paren (compl→ctrl-richting) | Omgekeerde modelleringsconventie t.o.v. m10; AVG-cross-walk-bron ontbreekt in `sources/`; vereist Protocol-symmetrie-validatie + helper-script-uitbreiding |
| Cross-bron-overlap-105-paren (uit v4.5.0) | ~105 paren | Andere bron-context; kwaliteits-indicator (heterogene bron-stack → per-paar-D4.1-toets) |
| m17 COSO/COBIT-mappings | onbekend | Andere namespaces, andere bron-context |
| m11 NIST SP 800-53-cluster | onbekend | M11-cluster (H33/H34 trigger-relevant) |
| m09 ISO 27001-cluster | onbekend | Spoor B-vraag-relevant |

**Eerstvolgende keuze:** m14-T-sprint (open subtask van H36) of nieuwe T3-scope-bepaling — masterchat-besluit post-T2.

## Protocol-versie-roadmap

| Versie | Status | Inhoud + operationele context |
|---|---|---|
| v1.0 | superseded | Vier criteria + beslis-tabel + downgrade-georiënteerd. Toegepast in T1 (28 paren). |
| v1.1 | DRAFT (nooit operationeel) | Downgrade-georiënteerd met C2-cluster-uitbreiding; vervangen door v1.2 vóór T2-start. |
| v1.2 | autoritatief tijdens T2 | Bidirectional toetsing + §3.1 predicate-doel-tabel + §3.2 sterkte-ordening + §3.3 symmetrische cluster-discipline + §6 sample-keuze + §7 werkverdeling + §10 zeven leerpunten-categorieën. Toegepast in T2 (118 paren over 10 clusters). |
| **v1.3** | **DRAFT** | Zeven verfijningen t.o.v. v1.2 (zie hieronder). Vaststelling pending bij eerstvolgende sprint-scoping (T3 of m14). |
| v2.0 | toekomst | Scope-uitbreiding naar non-SKOS-relaties indien nodig |

**Zeven Protocol v1.3-verfijningen** (per `docs/skos-beoordelings-protocol-v1_3.md` §0 + §13.1):

1. §2.1 C1 "partieel"-grens — operationele test verfijnd met drie-uitkomst-classificatie + T2-precedenten (bilateraal / partieel / gefaald)
2. §2.2 C2 + subject-cluster — object-cluster-cardinaliteit prevaleert bij multi-mapping; subject-cluster informatief (uitzondering-screening-flag), niet beslissend
3. §3.3 Cluster-discipline-bewijslast — bewijslast-asymmetrie expliciet (zie [[brain__concepts__cluster-discipline-bewijslast]])
4. §5.1 Cluster-representant-keuze-criteria — formele sub-sectie (was impliciet in v1.2)
5. §5.2 Confidence-criterium — expliciete drempels hoog/middel/laag
6. §10.2-§10.5 Werkflow-discipline — bottom-up rapport-bouw + interne tabel-consistentie + helper-script-autoritatief + metrics-tabel-scope-annotatie
7. §11 Protocol-versie-historie — sign-off-log + versie-toepassings-overzicht

**v1.3-werkflow-discipline §10.2-§10.5** is als gedragsregel opgenomen in **projectinstructie v1.10**. Operationeel relevant voor instructie-schrijvers (interne tabel-consistentie + scope-annotatie verplicht) en Tech-subagent (bottom-up rapport-bouw + helper-script-autoritatief).

v1.3-vaststelling vereist masterchat-besluit bij eerstvolgende sprint-scoping. Tot vaststelling blijft v1.2 autoritatief voor lopende-sprint-context.

## Cross-references naar D-decisions

| D | Relatie |
|---|---|
| [[brain__decisions__D04_skos-cross-framework]] | Autoritatief — protocol opereert binnen D4; T1 verbeterde D4-conformance; T2 levert D4.1-cluster-niveau-toepassings-precedent |

**D4.1 vastgesteld 27 mei 2026** (post-T1, formeel als sub-regel onder D4). T2 leverde toepassings-precedent op cluster-niveau (één bevestiging per homogene cluster). Zie [[brain__decisions__D04_skos-cross-framework]] §D4.1 + [[brain__concepts__mapping-bron-disclaimer-effect]].

## Cross-references naar H-items

| H | Relatie |
|---|---|
| [[brain__architecture__H36_skos-exactmatch-ctrl-compl-audit]] | Aanleiding — T1 closed-component, T2 m10-component closed (cumulatief 93 m10-paren); m14-subtask open |
| [[brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing]] | T1+T2 bevestigen SHACL-blinde vlek op ctrl:↔compl:-paren (28 + 118 paren) |
| [[brain__architecture__H41_skos-axioma-set-handling]] | T2-geactiveerd H-item — Protocol v1.3 §12 noemt H41-kandidaat-status expliciet als out-of-scope voor SKOS-beoordelings-protocol |

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-26 | living | Concept ontstaan uit T1-sprint Stap 2 — methode-protocol v1.0 vastgesteld; concept beschrijft methode in vault-context |
| 2026-05-27 | living | T2-toepassings-bewijs toegevoegd (Protocol v1.2 productie op 118 paren over 10 clusters); v1.3-draft-status + zeven verfijningen gedocumenteerd; bidirectional-audit-symmetrie als sub-aspect verankerd; cluster-discipline-bewijslast als apart concept uitgesplitst; v1.3-werkflow-discipline §10.2-§10.5 als gedragsregel in projectinstructie v1.10 |

## Cross-references

- [[brain__sprints__T1_skos-kwaliteitsanalyse-fase-1]] — sprint waarin protocol v1.0 is vastgesteld en gevalideerd
- [[brain__sprints__T2-skos-bidirectional-audit-m10]] — sprint waarin protocol v1.2 in productie is bevestigd en v1.3-draft is opgeleverd
- [[brain__decisions__D04_skos-cross-framework]] — D4 binnen welks protocol opereert + D4.1-toepassings-precedent op cluster-niveau
- [[brain__concepts__mapping-bron-disclaimer-effect]] — generaliseerbaar patroon uit T1, geformaliseerd als D4.1, op cluster-niveau toegepast in T2
- [[brain__concepts__cluster-discipline-bewijslast]] — bewijslast-asymmetrie voor cluster-uitzonderingen (nieuw iteratie 14)
- [[brain__concepts__cross-bron-overlap]] — kwaliteits-indicator-concept dat raakt aan evidence-hiërarchie
- Operationeel document: `docs/skos-beoordelings-protocol-v1_3.md` (DRAFT) + `docs/skos-beoordelings-protocol-v1_2.md` (T2-autoritatief) + `docs/skos-beoordelings-protocol-v1_0.md` (T1-historie)

— Einde skos-beoordelings-protocol.
