---
type: workflow
title: Opzet / Bestaan / Werking — audit-discipline
status: living
date: 2026-05-13
related:
  - H30_gitc-auditkader
  - M15_ensia
sources: []
chat-sources: []
confidence: medium
gaps:
  - "Formele toepassing in ontologie nog niet vastgesteld; gepland Fase 4"
---

# Opzet / Bestaan / Werking — audit-discipline

## Wat het is

**Driedeling** uit Nederlandse audit-praktijk voor beoordeling van interne beheersmaatregelen (controls):

| Niveau | Wat het meet | Voorbeeld-vraag |
|---|---|---|
| **Opzet** | Is de control ontworpen om het beoogde risico af te dekken? | Beschrijft het beleid de verwachte handelingen? |
| **Bestaan** | Is de control op een specifiek moment geïmplementeerd? | Bestaat het beleid daadwerkelijk en is het in gebruik? |
| **Werking** | Functioneert de control effectief over een periode? | Wordt het beleid consistent gevolgd? Werkt het in de praktijk? |

Een control kan **opzet=OK** zijn maar **bestaan=NEE** (mooi beleid op papier, nooit uitgerold). Of **bestaan=JA** maar **werking=NEE** (uitgerold maar niet nageleefd).

## Waarom relevant voor kennismodel

Het GRC Kennismodel is bedoeld als **informatie-laag van het ISMS** voor o.a. de interne auditafdeling. Audit-uitspraken vereisen traceerbaarheid op opzet/bestaan/werking-niveau per control. Status quo:

- Compliance-status in dashboard (rood/oranje/groen) heeft impliciet werking-perspectief
- Geen expliciete modellering van het onderscheid in v4.3.3
- Spoor B (organisatie-data) vereist deze discipline voor concrete control-status

## Geplande toepassing

**Fase 4 (v4.6.0)** in combinatie met:

- [[brain__architecture__H30_gitc-auditkader]] — GITC-auditkader voor financial-reporting-relevante IT-audit
- [[brain__modules__M15_ensia]] — ENSIA-uitbouw + maturity-model
- Mogelijk nieuwe property `audit:hasAssessment` met `audit:opzet`, `audit:bestaan`, `audit:werking` als data-properties (xsd:string of enum: NOK/PARTIAL/OK)

## Combineerbaarheid met maturity-model

`isms:MaturityAssessment` (gepland v4.6.0) en opzet/bestaan/werking zijn **complementair**, niet overlappend:

- **Maturity** beoordeelt de **volwassenheid** van de control-implementatie (1-5 niveau)
- **Opzet/bestaan/werking** beoordeelt de **status** van de control (3 dimensies)

Een control op niveau 4 (Managed) kan toch werking=NOK hebben in een specifieke periode (incidenten). Een control op niveau 2 (Repeatable) heeft per definitie werking=PARTIAL of OK.

## Modelleer-overweging

Twee opties bij Fase 4-implementatie:

**Optie A — drie aparte properties:**

```turtle
audit:Assessment_Control_X audit:opzet "OK"^^xsd:string ;
                          audit:bestaan "OK"^^xsd:string ;
                          audit:werking "PARTIAL"^^xsd:string ;
                          audit:assessmentDate "2026-04-01"^^xsd:date .
```

**Optie B — één property met enum-status:**

```turtle
audit:Assessment_Control_X audit:opzetBestaanWerking "OK_OK_PARTIAL"^^xsd:string .
```

Optie A is expressiever en queryable; Optie B is compacter. Masterchat-keuze bij Fase 4.

## Cross-references

- [[brain__architecture__H30_gitc-auditkader]] — GITC heeft opzet/bestaan/werking-traceerbaarheid als kernvereiste
- [[brain__modules__M15_ensia]] — ENSIA-audit-kader gebruikt deze discipline
- [[brain__concepts__drie-laags-compliance]] — audit-perspectief op Compliance-architectuur

— Einde opzet/bestaan/werking.
