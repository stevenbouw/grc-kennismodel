---
type: concept
title: SKOS-beoordelings-protocol — Methode voor bidirectional match-type-evaluatie
status: living
date: 2026-05-28
related:
  - D04_skos-cross-framework
  - T1_skos-kwaliteitsanalyse-fase-1
  - T2-skos-bidirectional-audit-m10
  - T3-skos-bidirectional-audit-m14
  - H36_skos-exactmatch-ctrl-compl-audit
  - H41_skos-axioma-set-handling
  - mapping-bron-disclaimer-effect
  - cluster-discipline-bewijslast
  - cross-category-mappings
  - cross-bron-overlap
sources:
  - skos-beoordelings-protocol-v1_0
  - skos-beoordelings-protocol-v1_2
  - skos-beoordelings-protocol-v1_3
  - t1-eindrapport-v4_6_1
  - patch-rapport-v4_6_2
  - t2-stap3-eindrapport
  - t2-pilot-rapport
  - patch-rapport-v4_6_3
  - t3-pilot-rapport
  - t3-stap3-eindrapport
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
- **v1.3 DRAFT → FINAL** vastgesteld door masterchat 28 mei 2026 tijdens T3-scoping; in productie gevalideerd op 31 m14-paren over 5 AVG-clusters (2 mutaties cross-category broadMatch → relatedMatch)
- **v1.3.1** kandidaat-uitbreiding voor formalisering cross-category-mappings-principe (T3-leerpunt — masterchat-werk bij volgende sprint-scoping)

**Onderscheid:**

- **Operationeel document:** `docs/skos-beoordelings-protocol-v1_3.md` (FINAL) — autoritatieve instructie voor Tech-subagent
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

## T3-toepassing — 2 cross-category-mutaties op m14 AVG/GDPR (Protocol v1.3 FINAL)

Protocol v1.3 FINAL (vastgesteld door masterchat 28 mei 2026 tijdens T3-scoping) in productie gevalideerd op 31 m14-paren over 5 AVG-clusters in compl→ctrl-richting. Per patch-rapport v4.6.3 + T3 Stap 3-eindrapport:

| Aspect | Waarde |
|---|---:|
| Beoordeelde paren m14 | 31 |
| Patch-mutaties | 2 (T3-001 + T3-002, beide broadMatch → relatedMatch op Art5_1f-cluster) |
| Behoud relatedMatch (cross-category-rationale) | 27 |
| Behoud closeMatch (retrieval-interchangeability-uitzondering) | 2 (T3-014 + T3-026) |
| Clusters | 5 AVG-subject-clusters (Art5_1f, Art25, Art32, Art33, Art34) |
| Cluster-convergentie naar narrowMatch | 0/5 (cross-category-rationale blokkeert structureel) |
| Confidence-distributie | 27 hoog + 4 middel + 0 laag |
| Evidence-niveau-verdeling | 10 niveau-1 + 7 niveau-2 + 14 niveau-3 (via ISO 27701:2025 Annex D + F twee-staps-keten) |
| D4.1-disclaimer-status | inactief (bindende T3-steer 1; AVG = publiek EU-recht) |

**Cross-category-rationale als T3-leerpunt** (kandidaat v1.3.1-precedent): wanneer subject en object van een SKOS-mapping in ontologisch verschillende categorieën zitten (bv. control ↔ legal-obligation), is `relatedMatch` de associatieve basislijn. broad/narrowMatch is een categorie-fout in de meeste gevallen omdat operationele implementatie-relatie geen conceptuele subsumptie impliceert. closeMatch-uitzondering op retrieval-interchangeability blijft mogelijk binnen specifieke domeinen.

Concept-niveau verankering: [[brain__concepts__cross-category-mappings]] *(nieuw iteratie 15)* — gemarkeerd als kandidaat v1.3.1-precedent; formalisering in Protocol-tekst is masterchat-werk bij volgende sprint-scoping.

**Bidirectional-audit-symmetrie bevestigd in cross-category-context:** Protocol v1.3 §3.1-§3.2 bleek symmetrisch toepasbaar op m14 compl→ctrl-richting (omgekeerd van m10's ctrl→compl). Pilot detecteerde de SKOS-formal-broadMatch-richtings-anomalie vroegtijdig (richting `A skos:broadMatch B` ≡ B is broader than A — omgekeerd aan modeller-bedoeling); masterchat-besluit Optie C (relatedMatch) opereert symmetrisch en lost richtings-kwestie definitief op zonder cross-category-fout.

**Bindende T3-steers (instructie-vastgesteld, alle 31 paren succesvol):**

1. Geen D4.1-disclaimer-logica (AVG = publiek EU-recht; geen non-equivalence-disclaimer)
2. Geen cluster-convergentie-aanname (per-paar getoetst; cluster-cardinaliteit informatief)
3. Semantische basislijn = relatedMatch (voor 23 van 24 niet-closeMatch-paren bevestigd; T3-001 + T3-002 per masterchat-besluit gemuteerd)
4. Evidence-hantering: niveau-1/2/3-keten als bestaans-bewijs, niet als predicate-type-bewijs
5. closeMatch-toets expliciet (T3-026; behoud verdedigbaar analoog T3-014)

## Cluster-discipline-bewijslast — zie eigen concept

De bewijslast-asymmetrie voor cluster-uitzonderingen is operationeel cruciaal voor symmetrische toepassing. Streng bewijs vereist voor zowel sterker- als zwakker-mapping-uitzondering; geen bewijs voor cluster-default. Empirisch gevalideerd in T2: 10 heuristiek-flags, 0 succesvolle uitzonderingen.

Volledige domein-uitleg + drie scenario's: zie [[brain__concepts__cluster-discipline-bewijslast]] *(nieuw iteratie 14)*.

## T4 + verdere kandidaten

Protocol is **herbruikbaar** voor andere SKOS-clusters in de 1.798-mappings-totaal:

| Kandidaat | Omvang | Karakteristiek |
|---|---:|---|
| ~~m14-AVG/GDPR-cluster~~ | ~~31 paren~~ | **afgehandeld in T3 (v4.6.3)** — cross-category-rationale-precedent |
| Cross-bron-overlap-105-paren (uit v4.5.0) | ~105 paren | Andere bron-context; kwaliteits-indicator (heterogene bron-stack → per-paar-D4.1-toets) |
| m17 COSO/COBIT-mappings | onbekend | Andere namespaces, andere bron-context |
| m11 NIST SP 800-53-cluster | onbekend | M11-cluster (H33/H34 trigger-relevant) |
| m09 ISO 27001-cluster | onbekend | Spoor B-vraag-relevant |
| m16 VIRBI-mappings | onbekend | Mogelijk cross-category indien VIRBI ↔ control of ↔ legal-obligation |
| m12 DORA-mappings | onbekend | Mogelijk cross-category indien DORA-obligation ↔ ISO 27002-control |
| Framework-niveau SKOS (fw:↔fw:) | beperkt | Buiten H36-scope; eigen H-item bij relevant-wording |

**Eerstvolgende keuze:** T4-scope-bepaling in verse masterchat-sessie post-T3 (m14-subtask afgehandeld; H36 fully closed).

## Protocol-versie-roadmap

| Versie | Status | Inhoud + operationele context |
|---|---|---|
| v1.0 | superseded | Vier criteria + beslis-tabel + downgrade-georiënteerd. Toegepast in T1 (28 paren). |
| v1.1 | DRAFT (nooit operationeel) | Downgrade-georiënteerd met C2-cluster-uitbreiding; vervangen door v1.2 vóór T2-start. |
| v1.2 | superseded | Bidirectional toetsing + §3.1 predicate-doel-tabel + §3.2 sterkte-ordening + §3.3 symmetrische cluster-discipline + §6 sample-keuze + §7 werkverdeling + §10 zeven leerpunten-categorieën. Toegepast in T2 (118 paren over 10 clusters). |
| **v1.3 FINAL** | **autoritatief** | Zeven verfijningen t.o.v. v1.2 (zie hieronder). DRAFT → FINAL vastgesteld door masterchat 28 mei 2026 tijdens T3-scoping. Toegepast in T3 (31 paren over 5 AVG-clusters cross-category). |
| **v1.3.1** | **kandidaat (masterchat-werk)** | Mogelijke aanvulling §3.4 of §3.3-uitbreiding voor cross-category-mappings-principe (T3-leerpunt). Zie [[brain__concepts__cross-category-mappings]]. Formalisering = masterchat-werk bij volgende sprint-scoping; Tech/Brein voert geen autonome Protocol-tekst-wijziging uit. |
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

**v1.3 FINAL-vaststelling 28 mei 2026:** masterchat heeft tijdens T3-scoping Protocol v1.3 als FINAL bevestigd, na succesvolle T3-pilot-toepassing (Stap 2). Tijdens T3 ontdekt cross-category-rationale-principe is gedocumenteerd als T3-leerpunt; formele opname in Protocol-tekst (v1.3.1) blijft masterchat-werk bij volgende sprint-scoping.

## Cross-references naar D-decisions

| D | Relatie |
|---|---|
| [[brain__decisions__D04_skos-cross-framework]] | Autoritatief — protocol opereert binnen D4; T1 verbeterde D4-conformance; T2 levert D4.1-cluster-niveau-toepassings-precedent |

**D4.1 vastgesteld 27 mei 2026** (post-T1, formeel als sub-regel onder D4). T2 leverde toepassings-precedent op cluster-niveau (één bevestiging per homogene cluster). Zie [[brain__decisions__D04_skos-cross-framework]] §D4.1 + [[brain__concepts__mapping-bron-disclaimer-effect]].

## Cross-references naar H-items

| H | Relatie |
|---|---|
| [[brain__architecture__H36_skos-exactmatch-ctrl-compl-audit]] | Aanleiding — T1 closed-component, T2 m10-component closed; **T3 m14-component closed; H36 fully closed (cumulatief 149 paren)** |
| [[brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing]] | T1+T2+T3 bevestigen SHACL-blinde vlek op ctrl:↔compl:-paren bidirectional (28 + 118 + 31 paren) |
| [[brain__architecture__H41_skos-axioma-set-handling]] | T2-geactiveerd H-item — T3 levert eerste cross-category-bewijs (informatief). Protocol v1.3 §12 noemt H41-kandidaat-status expliciet als out-of-scope voor SKOS-beoordelings-protocol |

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-26 | living | Concept ontstaan uit T1-sprint Stap 2 — methode-protocol v1.0 vastgesteld; concept beschrijft methode in vault-context |
| 2026-05-27 | living | T2-toepassings-bewijs toegevoegd (Protocol v1.2 productie op 118 paren over 10 clusters); v1.3-draft-status + zeven verfijningen gedocumenteerd; bidirectional-audit-symmetrie als sub-aspect verankerd; cluster-discipline-bewijslast als apart concept uitgesplitst; v1.3-werkflow-discipline §10.2-§10.5 als gedragsregel in projectinstructie v1.10 |
| 2026-05-28 | living | T3-toepassings-bewijs toegevoegd (Protocol v1.3 FINAL in productie op 31 m14-paren over 5 AVG-clusters cross-category); v1.3 DRAFT → FINAL door masterchat 28 mei 2026; cross-category-rationale als kandidaat v1.3.1-precedent gedocumenteerd via apart concept; bindende T3-steers (5) gedocumenteerd; T4-kandidaten-tabel bijgewerkt (m14 afgehandeld; m16, m12, framework-niveau bijgevoegd) |

## Cross-references

- [[brain__sprints__T1_skos-kwaliteitsanalyse-fase-1]] — sprint waarin protocol v1.0 is vastgesteld en gevalideerd
- [[brain__sprints__T2-skos-bidirectional-audit-m10]] — sprint waarin protocol v1.2 in productie is bevestigd en v1.3-draft is opgeleverd
- [[brain__sprints__T3-skos-bidirectional-audit-m14]] — sprint waarin protocol v1.3 FINAL in cross-category-context in productie is bevestigd
- [[brain__decisions__D04_skos-cross-framework]] — D4 binnen welks protocol opereert + D4.1-toepassings-precedent op cluster-niveau + cross-category-rationale-precedent op m14
- [[brain__concepts__mapping-bron-disclaimer-effect]] — generaliseerbaar patroon uit T1, geformaliseerd als D4.1, op cluster-niveau toegepast in T2 (inactief in T3-context)
- [[brain__concepts__cluster-discipline-bewijslast]] — bewijslast-asymmetrie voor cluster-uitzonderingen (nieuw iteratie 14)
- [[brain__concepts__cross-category-mappings]] — cross-category-rationale als T3-precedent (nieuw iteratie 15; kandidaat v1.3.1-precedent)
- [[brain__concepts__cross-bron-overlap]] — kwaliteits-indicator-concept dat raakt aan evidence-hiërarchie
- Operationeel document: `docs/skos-beoordelings-protocol-v1_3.md` (FINAL, T3-autoritatief) + `docs/skos-beoordelings-protocol-v1_2.md` (T2-historie) + `docs/skos-beoordelings-protocol-v1_0.md` (T1-historie)

— Einde skos-beoordelings-protocol.
