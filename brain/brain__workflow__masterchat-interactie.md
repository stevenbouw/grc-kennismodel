---
type: workflow
title: Masterchat-interactie — communicatieprotocol
status: living
date: 2026-05-13
related:
  - zes-chat-architectuur
  - scope-discipline
  - opleveringsprotocol
sources:
  - projectinstructie-v1.6
chat-sources: []
confidence: high
---

# Masterchat-interactie

## Principe

Master = strategische coördinatie, scope-beslissingen, projectinstructie-onderhoud, GO/NO-GO. Specialisten = uitvoering, technische correctheid, signaleren. **Heldere taakverdeling** vermijdt scope-creep en zorgt dat architectuurbeslissingen consistent worden vastgelegd.

## Wat tech-chat / specialisten zelf beslissen

- Specifieke implementatie-keuzes binnen instructie-scope
- Edit-techniek (str_replace vs Python-script)
- Verificatie-SPARQL-formuleringen
- Format van validatie-output
- Welk turtle-prettify-niveau

## Wat ALTIJD aan Master wordt voorgelegd

- **D-beslissingen** — alle wijzigingen aan D1-D12 of nieuwe D-decisions
- **Scope-uitbreidingen** — buiten instructie-scope (Optie A/B/C-protocol)
- **Conflicten** tussen instructie en werkelijkheid
- **Volgorde-wijzigingen** in sprint
- **Architectuur-aanrakingspunten** (sameAs, disjointness, naming, namespaces)
- **Nieuwe properties of klassen** die niet in instructie staan

## Communicatie-richting

| Richting | Triggers |
|---|---|
| Master → Specialist | Sprint-instructie, GO op scope-pauzes, scope-keuzes |
| Specialist → Master | Scope-pauzes, oplevering, vragen over architectuur-impact |
| Specialist ↔ Specialist | Alleen via Master (geen directe specialistische handover) |

## Instructie-verwachtingen

Goede sprint-instructie van Master bevat:

1. **Scope-afbakening** — wat wel/niet
2. **Specifieke wijzigingen** — bestanden, klassen, properties, individuals
3. **Verwachte impact** — triple-aantallen, klassen-count
4. **Validatie-vereisten** — welke metrics moeten blijven, welke veranderen
5. **Afgeleide consequenties** — SHACL-impact, disjointness-impact, meeliftregel-impact (sinds v4.3.3-leerpunt)

Leerpunt (bevinding G v4.3.0): bij D-beslissingen met sameAs, disjointness of naming-conventies vooraf afgeleide consequenties-sectie opnemen. Reduceert reactieve pauzes.

## Numerieke claims — geen ongeverifieerde aannames

Patroon-leerpunt uit v4.3.3:

> Geen numerieke claims in instructies zonder grep-verificatie, of telling aan tech-chat overlaten.

Voorbeeld v4.3.3: instructie zei "6 NIS2-subjects te migreren". Werkelijkheid was 20 (6 NIS2 + 14 DORA). Beter: instructie zegt "alle subjects met `ext:articleNumber`, tellen via SPARQL en rapporteer voor GO".

## Master-houding bij aankomst opleveringsrapport

1. **Lezen** — geen actie
2. **Verifiëren** §0-baseline matcht canonical_metrics-JSON
3. **Bevestigen** — bij volledig OK
4. **Doorvragen** — bij onverklaarde delta's of bevindingen
5. **Nieuwe instructie** — voor volgende sprint pas na vorige is afgesloten

## Specialist-houding bij aankomst nieuwe instructie

1. **Lezen, geen actie**
2. **Vergelijken** met geheugen uit vorige sprint — past het?
3. **Vragen vóór uitvoering** — bij dubbelzinnigheid
4. **Pre-execution confirmation** vóór output op documentatie-taken
5. **Sample-first** vóór full-batch op repetitief werk

## Cross-references

- [[brain__workflow__zes-chat-architectuur]] — rolverdeling
- [[brain__workflow__scope-discipline]] — Optie A/B/C-protocol
- [[brain__workflow__opleveringsprotocol]] — wat in oplevering aan Master

— Einde masterchat-interactie.
