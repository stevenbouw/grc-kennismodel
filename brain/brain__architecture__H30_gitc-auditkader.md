---
type: h-item
id: H30
title: GITC als auditkader-individual in Laag 5
status: future-consideration
date: 2026-05-09
related:
  - H31_toetsingskader-algoritmes
  - D09_framework-neutraliteit
sources:
  - projectinstructie-v1.6
chat-sources: []
confidence: medium
gaps:
  - "Vereist Analyse-opdracht 2.0 vóór formele scope-opname"
---

# H30 — GITC als auditkader-individual in Laag 5

## Status

**Toekomst-overweging.** Vereist Analyse-opdracht 2.0 vóór formele scope-opname. Geplande trigger: Fase 4 of later, na Toetsingskader Algoritmes-analyse.

## Voorstel

GITC (General IT Controls, ADR-toetsingskader) opnemen als **auditkader-individual** in Laag 5 (`audit:GITC_ADR`). Doel: ADR-toetsingskader voor financial-reporting-relevante IT-audit met **opzet/bestaan/werking-traceerbaarheid** per control.

## Achtergrond

GITC zijn de General IT Controls die door de Auditdienst Rijk (ADR) worden gebruikt bij financial reporting-relevante IT-audits. Onderwerpen:

- Toegangsbeheer
- Change management
- Backup en recovery
- Software Development Life Cycle (SDLC)
- IT operations
- Monitoring

GITC bundelt een **subset van bestaande BIO/ISO 27002-controls** in een specifieke audit-context. Het is geen autonome control-bibliotheek — het is een audit-perspectief op bestaande controls.

## Implementatie (concept, Optie 2 uit masterchat-discussie)

Niet: aparte controls voor GITC modelleren (zou duplicate-risico geven). Wel: kader-individual met relaties naar bestaande controls:

```turtle
audit:GITC_ADR rdf:type fw:GRCFramework, owl:NamedIndividual ;
    rdfs:label "GITC — General IT Controls (ADR)"@nl, "GITC — General IT Controls (ADR)"@en ;
    fw:toetst ctrl:ISO27002_5_15 ,  # Access control
              ctrl:ISO27002_8_28 ,  # Change management
              ctrl:ISO27002_8_13 ,  # Backup
              # ...etc.
              .

# Status per control via opzet/bestaan/werking-properties (gepland Fase 4 + isms:MaturityAssessment)
audit:GITC_ADR audit:onderzoekt audit:GITC_Onderwerp_Toegangsbeheer .
audit:GITC_Onderwerp_Toegangsbeheer audit:bevat ctrl:ISO27002_5_15 .
```

## Combineerbaarheid

Combineerbaar met **isms:MaturityAssessment** zodra Fase 4 (v4.6.0) is uitgevoerd. Per GITC-control kan dan opzet/bestaan/werking-status worden geregistreerd binnen het maturity-framework.

## Trigger voor uitvoering

- **Na Fase 4 of later**, nadat:
  1. Toetsingskader Algoritmes-analyse is voltooid ([[brain__architecture__H31_toetsingskader-algoritmes]]) — beide hebben hetzelfde patroon
  2. isms:MaturityAssessment-klasse bestaat
  3. ADR (of organisatie) een concrete behoefte heeft aan GITC-tracking in het kennismodel

## Voor uitvoering nodig

Analyse-opdracht 2.0 om:
- GITC-controls in bestaande BIO/ISO 27002-set te lokaliseren
- Te bepalen welke onderwerp-categorieën nodig zijn (zes uit ADR-standaard)
- Opzet/bestaan/werking-property-structuur te ontwerpen

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-09 | future-consideration | Opgenomen als H30 in projectinstructie v1.6 |

— Einde H30.
