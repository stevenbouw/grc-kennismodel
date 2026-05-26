---
type: concept
title: SKOS-beoordelings-protocol — Methode voor per-paar match-type-evaluatie
status: living
date: 2026-05-26
related:
  - D04_skos-cross-framework
  - T1_skos-kwaliteitsanalyse-fase-1
  - H36_skos-exactmatch-ctrl-compl-audit
  - mapping-bron-disclaimer-effect
  - cross-bron-overlap
sources:
  - skos-beoordelings-protocol-v1_0
  - t1-eindrapport-v4_6_1
chat-sources: []
confidence: high
---

# SKOS-beoordelings-protocol — Methode voor per-paar match-type-evaluatie

## Wat het is

Een **herbruikbare methode** om voor SKOS-mapping-paren (`skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`, `skos:narrowMatch`, `skos:relatedMatch`) consistent en repliceerbaar te beoordelen of de gekozen match-type D4-conform is, of dat herclassificatie nodig is.

**Versie 1.0** vastgesteld 26 mei 2026 voor T1-sprint (zie [[brain__sprints__T1_skos-kwaliteitsanalyse-fase-1]]) en in productie gevalideerd op 28 ctrl:↔compl: `exactMatch`-paren (H36-cluster). Alle 28 paren leverden eenduidige beslissing op met hoog vertrouwen.

**Onderscheid:**

- **Operationeel document:** `docs/skos-beoordelings-protocol-v1_0.md` — autoritatieve instructie voor Tech-subagent (Stap 3 + Stap 4 in SKOS-kwaliteitsanalyse-sprints)
- **Dit concept-bestand:** methode-overzicht + architectuur-context + T2/T3-relevantie

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

Het protocol leverde 28× broadMatch met hoog vertrouwen. Doorslaggevend voor 1→1-paren binnen 28-set: **C2-toets binnen bredere 121-set ctrl:↔compl:-mappings**, niet alleen exactMatch-subset. Bevestigd patroon: ENISA-disclaimer-categorisch-effect ondergraaft `exactMatch` zelfs bij sluitende C1-C3 (zie [[brain__concepts__mapping-bron-disclaimer-effect]]).

## T2/T3-relevantie

Protocol is **herbruikbaar** voor andere SKOS-clusters in de 1.798-mappings-totaal:

| T2-kandidaat | Omvang | Karakteristiek |
|---|---:|---|
| Overige ctrl:↔compl: mappings (close + related + broad) | ~93 paren | Zelfde modules, andere predicate-types — protocol v1.0 direct toepasbaar |
| Cross-bron-overlap-105-paren (uit v4.5.0) | ~105 paren | Andere bron-context; kwaliteits-indicator |
| m17 COSO/COBIT-mappings | onbekend | Andere namespaces, andere bron-context |

T2-eerste-keuze: optie A (overige ctrl:↔compl:). Reden — protocol v1.0 is voor ctrl:↔compl:-context bewezen.

## Protocol-versie-roadmap

| Versie | Status | Inhoud |
|---|---|---|
| **v1.0** | huidig (vastgesteld 26 mei 2026) | Vier criteria + beslis-tabel + evidence-hiërarchie + cluster-discipline + twijfelgevallen-procedure |
| v1.1 | overweging bij T2-start | C2-toets binnen bredere mapping-cluster als primaire test; ENISA-disclaimer-handling expliciet; NEN-PK-werkverdeling als procedure-stap; werkende applier-vereiste |
| v2.0 | toekomst | Scope-uitbreiding naar non-SKOS-relaties indien nodig |

Protocol-v1.1-tekst wordt opgesteld door masterchat bij T2-voorbereiding, niet door Brein.

## Cross-references naar D-decisions

| D | Relatie |
|---|---|
| [[brain__decisions__D04_skos-cross-framework]] | Autoritatief — protocol opereert binnen D4; T1 verbeterde D4-conformance |

**D4-aanvulling-overweging open:** disclaimer-handling-regel kandidaat voor latere D4-uitbreiding. Niet T1-scope; masterchat-beslissing voor T2-voorbereiding. Zie [[brain__concepts__mapping-bron-disclaimer-effect]].

## Cross-references naar H-items

| H | Relatie |
|---|---|
| [[brain__architecture__H36_skos-exactmatch-ctrl-compl-audit]] | Afgehandelde aanleiding — 28 ctrl:↔compl: exactMatch-paren waarvan protocol gevalideerd |
| [[brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing]] | T1-Vraag D bevestigt SHACL-blinde vlek op ctrl:↔compl:-paren |

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-26 | living | Concept ontstaan uit T1-sprint Stap 2 — methode-protocol v1.0 vastgesteld; concept beschrijft methode in vault-context |

## Cross-references

- [[brain__sprints__T1_skos-kwaliteitsanalyse-fase-1]] — sprint waarin protocol v1.0 is vastgesteld en gevalideerd
- [[brain__decisions__D04_skos-cross-framework]] — D4 binnen welks protocol opereert
- [[brain__concepts__mapping-bron-disclaimer-effect]] — generaliseerbaar patroon uit T1
- [[brain__concepts__cross-bron-overlap]] — kwaliteits-indicator-concept dat raakt aan evidence-hiërarchie
- Operationeel document: `docs/skos-beoordelings-protocol-v1_0.md`

— Einde skos-beoordelings-protocol.
