---
type: concept
title: Cluster-discipline-bewijslast — bewijslast-asymmetrie voor uitzonderingen binnen veel↔1-clusters
status: living
date: 2026-05-27
related:
  - skos-beoordelings-protocol
  - mapping-bron-disclaimer-effect
  - D04_skos-cross-framework
  - T1_skos-kwaliteitsanalyse-fase-1
  - T2-skos-bidirectional-audit-m10
sources:
  - skos-beoordelings-protocol-v1_2
  - skos-beoordelings-protocol-v1_3
  - t2-stap3-eindrapport
  - patch-rapport-v4_6_2
chat-sources: []
confidence: high
---

# Cluster-discipline-bewijslast — bewijslast-asymmetrie voor uitzonderingen binnen veel↔1-clusters

## Wat het is

Bij toepassing van het [[brain__concepts__skos-beoordelings-protocol]] op cluster-niveau (Protocol v1.2 §3.3 cluster-discipline) ontstaat een **asymmetrische bewijslast** voor individuele uitzonderingen op het cluster-doel-predicate. Dit concept beschrijft welke bewijslast geldt voor welke uitzondering-richting, met empirisch bewijs uit T2-sprint (118 paren over 10 clusters, 10 heuristiek-flags, 0 succesvolle uitzonderingen).

Formele vastlegging in [[brain__concepts__skos-beoordelings-protocol]] Protocol v1.3 §3.3 (DRAFT). Dit concept-bestand levert de domein-uitleg + T2-empirie + ontwerp-rationale.

## Bewijslast-asymmetrie — drie scenario's

Wanneer een paar binnen een veel↔1-cluster (object-cluster-cardinaliteit ≥2) zit met cluster-doel-predicate `broadMatch`, gelden drie uitzondering-richtingen met verschillende bewijslast:

| Uitzondering-richting | Bewijslast | Praktische haalbaarheid |
|---|---|---|
| **Naar sterker mapping** (bv. closeMatch in plaats van broadMatch) | **Streng**: vereist bilaterale containment-aantoonbaarheid via NEN-tekst (C1 bilateraal + C3 bilateraal) | Structureel zeer moeilijk omdat object-cluster-cardinaliteit ≥2 betekent dat object niet bilateraal A=B kan zijn met meerdere A's |
| **Naar zwakker mapping** (bv. relatedMatch in plaats van broadMatch) | **Streng**: vereist NEN-bewijs dat C3 (subset-relatie A⊂B) faalt; alleen thematische verwantschap | Operationeel zeldzaam want cluster-lidmaatschap impliceert reeds enige subset-relatie |
| **Behoud cluster-default** (broadMatch zoals cluster) | **Geen aanvullende bewijslast** | Cluster-discipline §3.3 prevaleert; default-toepassing geldt totdat tegenbewijs wordt geleverd |

**Asymmetrie-bewijs:** de bewijslast voor *afwijking* is in beide richtingen streng; de bewijslast voor *conformiteit* is nihil. Dit is bewuste ontwerpkeuze om cluster-coherentie te beschermen tegen willekeurige micromanagement van individuele cluster-leden.

## T2-empirisch bewijs

T2-sprint (27 mei 2026) leverde productie-schaal validatie van de bewijslast-asymmetrie. Cluster-overerving-helper-script (`output/scripts/t2-cluster-overerving-helper.py`) flagde 10 heuristiek-screening-kandidaten op 6 cluster-leden (sommige in meerdere clusters):

| Subject | Aantal clusters | Heuristiek-trigger | NEN-uitzondering aangetoond? |
|---|---:|---|---|
| ISO27002_5_02 | 2 (NIS2_a, NIS2_i) | label "Rollen en verantwoordelijkheden" — brede-policy-keyword | nee (beide clusters) |
| ISO27002_5_04 | 3 (NIS2_a, NIS2_f, NIS2_g) | label "Managementverantwoordelijkheden" + subject-cluster 3 | nee (alle 3 clusters) |
| ISO27002_5_36 | 1 (NIS2_a) | label "Naleving van beleid" — brede-policy-keyword | nee |
| ISO27002_6_05 | 1 (NIS2_i) | label "Verantwoordelijkheden na beëindiging" — brede-policy-keyword | nee |
| ISO27002_8_03 | 3 (NIS2_h, NIS2_i, NIS2_j) | subject-cluster 3 (multi-mapping) | nee (alle 3 clusters) |
| **Totaal** | **10 flags / 6 leden** | | **0 succesvolle uitzonderingen** |

Per t2-stap3-eindrapport §4: na ISO 27002:2022-tekstlezing zijn alle 10 flags cluster-conform bevonden. Geen enkele heuristiek-flag leverde NEN-aantoonbare individuele afwijking op.

**Conclusie:** de heuristiek werkt als **prioriteits-mechanisme** voor manuele review (efficient signaling), niet als **beslis-mechanisme**. Cluster-discipline §3.3 prevaleert in alle gevallen.

## Cluster-cardinaliteit als blokkade voor sterker mapping

Per t2-stap3-eindrapport §4 (slot):

> *"Voor cluster-uitzondering naar sterker mapping (bv. closeMatch) is bilaterale equivalentie-onderbouwing vereist; veel↔1-cluster-cardinaliteit (cluster-grootte ≥7 in alle 10 T2-clusters) maakt 1↔1-in-cluster-criterium structureel onmogelijk. Geen enkele NEN-uitzondering is plausibel zonder cluster-cardinaliteit-vermindering, wat geen scope van T2 is."*

**Structurele blokkade:** zolang de object-cluster-grootte ≥2 is, kan C2 (cardinaliteit 1↔1 in cluster) niet sluitend voldoen voor één cluster-lid. closeMatch vereist C2 1↔1; veel↔1-cluster maakt closeMatch dus per definitie niet-houdbaar binnen dezelfde cluster-context.

**Operationele implicatie:** cluster-uitzondering naar sterker mapping is alleen mogelijk wanneer een cluster-lid bewezen niet thuishoort in het cluster (bv. door cluster-cardinaliteit-revisie of bron-data-correctie). Dit valt buiten reguliere SKOS-audit-scope en vereist masterchat-judgement.

## Cluster-cardinaliteit als motivering voor zwakker-mapping-blokkade

Symmetrische redenering aan de zwakker-mapping-zijde: cluster-lidmaatschap impliceert dat A_i ⊂ B (engere control binnen bredere norm) — anders zou A_i niet in het cluster zitten. Bij relatedMatch-claim (`A relatedMatch B` = thematische verwantschap zonder subset-relatie) moet bewijslast worden geleverd dat C3 faalt — dat A_i géén subset-relatie heeft met B ondanks cluster-lidmaatschap.

Operationeel zeldzaam:
- Cluster-lidmaatschap volgt typisch uit autoritatieve mapping-bron (bv. ENISA TIG R285, CBW-Mapping-UV) die per definitie enige relatie erkent
- Thematische-verwantschap-zonder-subset-relatie zou expliciete NEN-onderbouwing vereisen waaruit blijkt dat A_i in een ander conceptueel domein zit dan B-cluster-aspecten
- T2 leverde 0 zulke gevallen op 10 flags

## Heuristiek-screening als prioriteits-mechanisme, niet beslis-mechanisme

T2 hanteerde twee heuristiek-flags (per t2-stap3-eindrapport §2.2):

1. **Brede-policy-keyword in label** — woorden als "policy", "roles", "responsibilit", "governance", "beleid", "kader", "managementverant" suggereren dat het subject mogelijk een bredere governance-control is die overlapt met cluster-doel-norm
2. **Subject-cluster-grootte ≥3** — multi-mapping naar meerdere NIS2-letters suggereert dat het subject bredere thematische reikwijdte heeft dan strikt-cluster-conform

**Heuristiek-resultaat T2:** 10 flags, 0 succesvolle uitzonderingen. Heuristiek-precisie = 0% op cluster-uitzondering-aspect, maar 100% effectief als prioriteits-signaal voor manuele review (alle flags kregen aandacht voor NEN-toets; geen flag werd genegeerd).

**Implicatie voor toekomstige sprints:** heuristiek-flags zijn nuttig om manuele NEN-review-effort gericht in te zetten, maar mogen geen confidence-vermindering opleveren voor de cluster-default-toepassing.

## Werkflow-discipline rond bewijslast

Per Protocol v1.3 §3.3 (DRAFT):

1. **Default**: cluster-doel-predicate uit Protocol v1.2/v1.3 §3.1 predicate-doel-tabel rij 6 (veel↔1) of rij 7 (1↔veel)
2. **Heuristiek-screening**: helper-script flagt kandidaten voor manuele review
3. **NEN-toets per flag**: lokale ISO/NIS2-bron-lezing (Protocol 17 v1.3 Tech-autonomie)
4. **Bewijslast-toets**:
   - Voor sterker mapping: bilaterale containment-aantoonbaarheid vereist (zeer streng)
   - Voor zwakker mapping: C3-falen-aantoonbaarheid vereist (streng)
   - Voor cluster-default: geen aanvullende bewijslast
5. **Documentatie**: per flag noteren waarom cluster-default van toepassing blijft (of, indien uitzondering aangetoond, expliciete NEN-onderbouwing)
6. **Confidence-aanduiding** (Protocol v1.3 §5.2): cluster-discipline-overerving levert typisch hoge confidence indien geen NEN-onderbouwing voor uitzondering

## Cross-references naar D-decisions

| D | Relatie |
|---|---|
| [[brain__decisions__D04_skos-cross-framework]] | Cluster-discipline opereert binnen D4 + D4.1; bewijslast-asymmetrie raakt geen D-decision direct, maar versterkt D4.1-operationaliteit op cluster-niveau |

## Cross-references naar concepten

- [[brain__concepts__skos-beoordelings-protocol]] — moeder-concept (cluster-discipline-bewijslast is sub-aspect van Protocol v1.3 §3.3)
- [[brain__concepts__mapping-bron-disclaimer-effect]] — gerelateerd: D4.1-bewijslast-toepassing op cluster-niveau (één bevestiging per cluster bij homogene bron-stack)

## Cross-references naar sprints

- [[brain__sprints__T1_skos-kwaliteitsanalyse-fase-1]] — eerste cluster-discipline-toepassing (28 paren in één H36-cluster)
- [[brain__sprints__T2-skos-bidirectional-audit-m10]] — productie-schaal validatie (118 paren over 10 clusters, 10 heuristiek-flags, 0 uitzonderingen)

## Toekomst-overweging

Bij heterogene clusters (mix van bronnen, mix van predicate-types in oorspronkelijke staat) kan bewijslast-balans verschuiven. T2 was homogeen (alle 10 clusters dezelfde bron-stack: ENISA TIG R285 + CBW-Mapping-UV R3-erf). Voor m14-sprint (compl→ctrl-richting, AVG-cross-walk-bron ontbreekt) of cross-bron-overlap-sprint (T3-kandidaat) kan een bredere bewijslast-toets nodig zijn. Concept kan dan worden uitgebreid met heterogene-cluster-bewijslast-sub-sectie.

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-27 | living (confidence high) | Concept ontstaan uit T2-sprint Stap 3-leerpunt §6.5 + patch-rapport v4.6.2 §6.3. Bewijslast-asymmetrie geformaliseerd in Protocol v1.3 §3.3 (DRAFT). 100% T2-empirisch bewijs (0/10 succesvolle heuristiek-flag-uitzonderingen) |

— Einde cluster-discipline-bewijslast.
