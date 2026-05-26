---
type: h-item
id: H29
title: Three Lines Model als M04-roles uitbreiding
status: future-consideration
date: 2026-05-09
related:
  - D04_skos-cross-framework
  - D09_framework-neutraliteit
sources:
  - projectinstructie-v1.6
chat-sources: []
confidence: medium
gaps:
  - "Vereist Analyse-opdracht 2.0 vóór formele scope-opname"
---

# H29 — Three Lines Model als M04-roles uitbreiding

## Status

**Toekomst-overweging.** Vereist Analyse-opdracht 2.0 (Analyse-chat) vóór formele scope-opname. Geen blocker voor Fase 1–3.

## Voorstel

Three Lines Model (IIA 2020) opnemen als internationale referentie-rolverdeling **gelijkwaardig naast** BVA-stelsel en COSO-rollen, conform [[brain__decisions__D09_framework-neutraliteit]]. Geen nieuwe module, geen nieuwe namespace — implementatie via SKOS-mappings tussen 3LoD-rollen en bestaande role-individuals in M04.

## Achtergrond

IIA's Three Lines Model (2020-revisie van het oudere Three Lines of Defence) is internationaal de standaardreferentie voor rolverdeling tussen:

- **First Line** — operationeel management, eigenaarschap van risico-respons
- **Second Line** — risk management, compliance, control functies
- **Third Line** — interne audit, onafhankelijke assurance

Drie rollen elk omsluiten meerdere concrete posities. De organisatie heeft BVA-stelsel (NL-specifiek) en COSO ICF/ERM (internationaal). Three Lines voegt een **operationeel-georiënteerde** internationale referentie toe die organisaties wereldwijd herkennen.

## Implementatie (concept)

```turtle
# Concept: drie nieuwe role-individuals als referentie-categorieën
roles:FirstLine rdf:type roles:Role, owl:NamedIndividual .
roles:SecondLine rdf:type roles:Role, owl:NamedIndividual .
roles:ThirdLine rdf:type roles:Role, owl:NamedIndividual .

# SKOS-mappings naar bestaande BVA en COSO-rollen
roles:BVA skos:relatedMatch roles:SecondLine .
roles:Auditor skos:relatedMatch roles:ThirdLine .
# ...etc.
```

**Verwachte impact:** ~6-12 nieuwe role-individuals, ~12-24 SKOS-mappings.

## Waarom geen nieuwe module

Three Lines Model is een rol-classificatie, geen apart framework met eigen controls of vereisten. Past goed binnen M04 dat al BVA-rollen, COSO-rollen, en generieke RACI-structuren bevat. Toevoeging als nieuwe module zou over-engineering zijn.

## Trigger voor uitvoering

- **Fase 4 (v4.6.0)** als onderdeel van M15-ENSIA uitbouw en volwassenheidsmodel — internationale audit-context vraagt om Three Lines-perspectief
- Of: aparte mini-sprint na Fase 3 als directie/audit-stakeholders Three Lines-referentie expliciet vragen

## Voor uitvoering nodig

Analyse-opdracht 2.0 (Analyse-chat) om:
- 3LoD-rolverdeling formeel te mappen op BVA + COSO + bestaande M04-rollen
- Conflicten te identificeren (bv. is BVA First of Second Line?)
- SKOS-mapping-niveau per paar te bepalen (exactMatch / closeMatch / relatedMatch)

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-09 | future-consideration | Opgenomen als H29 in projectinstructie v1.6 |

— Einde H29.
