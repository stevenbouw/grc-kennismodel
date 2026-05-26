---
type: h-item
id: H31
title: Toetsingskader Algoritmes (Algemene Rekenkamer)
status: future-consideration
date: 2026-05-09
related:
  - H30_gitc-auditkader
  - D09_framework-neutraliteit
sources:
  - projectinstructie-v1.6
chat-sources: []
confidence: medium
gaps:
  - "Vereist Analyse-opdracht 2.0 vóór formele scope-opname"
  - "Algoritmekader BZK (rijksbreed kader in ontwikkeling) moet ge-alignd worden"
---

# H31 — Toetsingskader Algoritmes (Algemene Rekenkamer)

## Status

**Toekomst-overweging.** Vereist Analyse-opdracht 2.0 en cross-reference met Algoritmekader BZK. Trigger: Fase 4 of 5.

## Voorstel

Toetsingskader Algoritmes (Algemene Rekenkamer) opnemen als **auditkader-individual** in Laag 5, **zelfde patroon als [[brain__architecture__H30_gitc-auditkader]]**: niet als autonome control-bibliotheek, wel als kader-individual met relaties naar bestaande controls in BIO/AVG/GITC.

## Achtergrond

De Algemene Rekenkamer publiceerde een Toetsingskader Algoritmes met vijf perspectieven:

1. **Sturing en verantwoording** — governance van algoritme-gebruik
2. **Data** — data-kwaliteit, herleidbaarheid, bias-detectie
3. **Privacy** — AVG-conformiteit, dataminimalisatie
4. **General IT controls (GITC)** — toegangsbeheer, change management, etc.
5. **Ethische principes** — fairness, transparantie, menselijke controle

Het kader leunt expliciet op andere kaders:
- Perspectief 3 → AVG (M14)
- Perspectief 4 → GITC ([[brain__architecture__H30_gitc-auditkader]])
- Perspectief 5 → mogelijk M19 ISO 42001 (AI Management) wanneer dat in scope komt

## Implementatie (concept)

```turtle
audit:ToetsingskaderAlgoritmes_AR rdf:type fw:GRCFramework, owl:NamedIndividual ;
    rdfs:label "Toetsingskader Algoritmes (Algemene Rekenkamer)"@nl ;
    audit:bevatPerspectief
        audit:Perspectief_Sturing ,
        audit:Perspectief_Data ,
        audit:Perspectief_Privacy ,
        audit:Perspectief_GITC ,
        audit:Perspectief_Ethiek .

# Per perspectief: relaties naar bestaande controls/kaders
audit:Perspectief_Privacy fw:dektAf fw:AVG .
audit:Perspectief_GITC fw:dektAf audit:GITC_ADR .  # zie H30
```

## Cruciale voor-onderzoek-stap

**Alignment met Algoritmekader BZK.** Per september 2025 is BZK een rijksbreed kader in ontwikkeling. Dat kader kan:

- Toetsingskader AR vervangen of vervangen
- Beide naast elkaar laten bestaan met verschillende doelgroepen
- Een nieuwe rijksbrede norm worden waar AR-Toetsingskader naar verwijst

Modeleer-keuzes hangen sterk af van waar BZK uitkomt. Premature modellering kan tot dubbelwerk leiden.

## Trigger voor uitvoering

- **Fase 4 of 5**, nadat:
  1. Algoritmekader BZK een vastere vorm heeft (status 2026 onbekend — Spoor C-monitoring)
  2. H30 (GITC) is geanalyseerd of geïmplementeerd
  3. M14 (AVG) afdoende is uitgewerkt om Privacy-perspectief te dragen
  4. Eventueel M19 ISO 42001 in scope is gekomen voor Ethiek-perspectief

## Voor uitvoering nodig

Analyse-opdracht 2.0 om:
- AR Toetsingskader Algoritmes structuur formeel te mappen
- Cross-reference met Algoritmekader BZK uit te voeren
- Overlap met bestaande kaders (AVG, GITC, mogelijk ISO 42001) te identificeren
- Te beoordelen of "audit:" of "fw:" namespace passender is

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-09 | future-consideration | Opgenomen als H31 in projectinstructie v1.6 |

— Einde H31.
