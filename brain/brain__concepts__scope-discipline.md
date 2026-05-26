---
type: concept
title: Scope-discipline
status: living
date: 2026-05-13
related:
  - framework-neutraliteit
sources:
  - projectinstructie-v1.6
chat-sources: []
confidence: high
---

# Scope-discipline

## Wat het is

**Scope-discipline** is de werk-invariant van dit project dat zegt: **scope-afwijkingen altijd melden, nooit zelf interpreteren**. Het ontstaat als reactie op de risico's van semi-autonoom werken — een tech-chat (of Claude Code-sessie) die zelf inschat dat "kleine afwijking, doe maar door" kan onbedoeld architectuur-impact creëren.

Drie elementen:

| Element | Wat | Waarom |
|---|---|---|
| **Pauzeer-trigger** | Concrete criteria voor wanneer pauze nodig is | Verschil tussen routine-werk en architectuur-aanrakingspunt |
| **Optie A/B/C-rapportage** | Gestructureerd voorstel met 2-3 keuzes + voor/tegen | Master krijgt beslissings-relevante info, niet detail-overload |
| **Wacht-op-GO-discipline** | Geen vooruitlopen op verwachte uitkomst | Voorkomt sneeuwbaleffecten bij verkeerde aannames |

## Waarom het werkt

Drie observaties uit de v4.2.2 → v4.3.3-sprint-cyclus die de discipline rechtvaardigen:

1. **Werkelijke scope wijkt vaak af van verwachte scope.** v4.3.3 verwachtte 6 NIS2-subjects voor predicate-consolidatie; werkelijkheid bleek 20 (6 NIS2 + 14 DORA). Zonder pauze had de tech-chat óf alleen 6 gedaan (incomplete migratie) óf zelf 20 zonder Master-input (potentieel D9-schending zonder validatie).

2. **D9-symmetrie-keuzes zijn geen tech-detail.** De keuze "behandelen we NIS2 en DORA gelijkwaardig in deze consolidatie?" is een framework-neutraliteits-vraag — D9-impact. Tech-chat-niveau, maar Master-beslissings-niveau.

3. **Verwacht-versus-werkelijk-gat is normaal.** Bij vrijwel elke sprint vanaf v4.2.2 is een scope-pauze nodig geweest. Niet als uitzondering, maar als ingebouwde controle.

## Vier pauzeer-trigger-categorieën

| Trigger | Voorbeeld |
|---|---|
| **Inventaris-discrepantie** | Instructie-verwachting matcht niet met werkelijkheid (bv. v4.3.3: 0 verwacht buiten m10, 14 in m12 werkelijk) |
| **Onbekende scope-uitbreiding** | Nieuwe entiteiten of relaties buiten instructie-scope |
| **Architectuur-aanrakingspunt** | Mogelijke D-beslissing-impact niet in instructie genoemd |
| **Telling-discrepantie** | Observed versus expected significant verschillend |

## Wat het niet is

- **Geen verlamming.** Routine-edits binnen instructie-scope (typo-fixes, format-correcties) gaan zonder pauze. Discipline is voor **scope-afwijkingen**, niet voor elke micro-keuze.
- **Geen ontheffing.** Pauze creëren is geen excuus om elke beslissing uit te besteden. Tech-chat behoudt eigen verantwoordelijkheid voor implementatie-keuzes binnen scope.
- **Geen rigide protocol.** Het is een **gewoonte**, geen checklist. Als Master en tech-chat goed afgestemd zijn, herkennen beiden direct wanneer pauze nodig is.

## Hoe het evolueerde

| Fase | Werkwijze |
|---|---|
| v0.x – v4.2.1 | Geen expliciete discipline. Tech-chat nam zelf scope-beslissingen — soms goed, soms te ver. |
| v4.2.2 (G9 SoAEntry-canonisering) | Eerste expliciete masterchat-pauze met Optie A/B-rapportage. Werkte. |
| v4.3.0 (gap-sprint) | Vijf scope-pauzes opeenvolgend — discipline bevestigd als werkpatroon. |
| v4.3.3 | Patroon-leerpunt: vooraf "afgeleide consequenties"-sectie in instructies opnemen om reactieve pauzes te reduceren. |
| Projectinstructie v1.5+ | Discipline expliciet opgenomen onder "SCOPE-DISCIPLINE (kritische werkwijze)". |

## Relatie tot andere disciplines

- [[brain__concepts__framework-neutraliteit]] — D9-architectuur-test is een van de aanrakingspunten die scope-pauze rechtvaardigen
- [[brain__concepts__canonical-metrics]] — telling-discrepanties zijn een pauzeer-trigger
- [[brain__workflow__scope-discipline]] — operationele werkwijze (de "hoe")
- [[brain__workflow__masterchat-interactie]] — wat aan Master / wat zelf — de scope-discipline geeft de grens

## Verschil tussen dit concept-file en de workflow-file

- **Dit (`concepts/`)** — uitleg van wat scope-discipline is en waarom het werkt
- **Workflow (`workflow/scope-discipline.md`)** — operationele instructies (vier-stappen-protocol, Optie A/B/C-template, gedocumenteerde besluiten)

Beide hebben hun plek. Concept = waarom; workflow = hoe.

— Einde scope-discipline (concept).
