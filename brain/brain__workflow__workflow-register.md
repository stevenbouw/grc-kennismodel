---
type: index
id: workflow-register
title: Workflow-register — Werkwijze GRC Kennismodel-project
status: living
date: 2026-05-13
---

# Workflow-register — Werkwijze GRC Kennismodel-project

Overzicht van werkdisciplines en proces-conventies die het project beheersbaar houden. Zes workflow-files in totaal (incl. sprint-protocollen v1.7).

## Snelle navigatie

| Workflow | Wat het regelt | Status |
|---|---|---|
| [[brain__workflow__zes-chat-architectuur]] | Master/Tech/Doc/Dashboard/Asset/Analyse — rolverdeling + doorverwijs-discipline | living |
| [[brain__workflow__scope-discipline]] | Werkwijze bij scope-afwijkingen (Optie A/B/C-rapport, pauze-protocol) | living |
| [[brain__workflow__opleveringsprotocol]] | Opzet/bestaan/werking-formaat per release + canonieke artefacten | living |
| [[brain__workflow__masterchat-interactie]] | Wat aan Master / wat zelf — grens-discipline | living |
| [[brain__workflow__opzet-bestaan-werking]] | Drie-niveau-audit-conventie (opzet → bestaan → werking) | living |
| [[brain__workflow__sprint-protocollen]] *(v1.7)* | Vijf nieuwe sprint-protocollen formeel: pre-sprint-inventarisatie + schema-meta-rapport + bron-verificatie + raming-discipline + patch-rapport §9 | living |

## Clusters per fase van het werk

### Pre-sprint (vóór het werk begint)

- [[brain__workflow__sprint-protocollen]] — Protocol B (inventarisatie) + bron-verificatie
- [[brain__workflow__masterchat-interactie]] — GO/NO-GO

### Tijdens-sprint (tijdens het werk)

- [[brain__workflow__zes-chat-architectuur]] — wie doet wat
- [[brain__workflow__scope-discipline]] — wat te doen bij afwijking
- [[brain__workflow__sprint-protocollen]] — raming-discipline tijdens aggregatie

### Post-sprint (na het werk)

- [[brain__workflow__opleveringsprotocol]] — release-artefacten
- [[brain__workflow__opzet-bestaan-werking]] — kwaliteits-niveau-bewijs
- [[brain__workflow__sprint-protocollen]] — Protocol C (schema-meta-rapport-herziening) + patch-rapport §9

## v1.7-uitbreiding: vijf nieuwe protocollen

Per projectinstructie v1.7 zijn vijf werkdisciplines formeel geldend gemaakt. Zie [[brain__workflow__sprint-protocollen]] voor uitwerking.

| Protocol | Aard | Eerste toepassings-bewijs |
|---|---|---|
| Pre-sprint-inventarisatie (Protocol B) | Verplicht bij structurele wijziging | v4.4.0: 5/5 signalen → Route 5-correctie |
| Schema-meta-rapport (Protocol C) | Eenmalig + herziening per minor-release | v4.3.3-eerste; niet geüpdatet v4.4.0 |
| Bron-verificatie vóór TBox-declaratie | Verplicht bij externe-naam-verwijzing | v4.4.0: `ext:hasENISAGuidance`-correctie gemarkeerd |
| Raming-discipline bij aggregatie | Verplicht bij grain-mismatch | v4.4.0: 290→183 (37% dedup) Sheet 9 mapping |
| Patch-rapport §9 verplicht | Per release | v4.4.0: eerste exemplaar |

## Cross-references

- [[brain__concepts__scope-discipline]] — concept-niveau-uitleg (waarom)
- [[brain__concepts__meeliftregel-edit-scope]] — D6-conventie (vertaling-scope-uitbreiding v1.7)
- [[brain__concepts__provenance-en-attribuering]] — bron-discipline (CC-BY-attributie)
- [[brain__sprints__sprint-register]] — geschiedenis-overzicht waarin disciplines zijn ontstaan
- [[brain__decisions__D-register]] — D-decisions die werkwijze ondersteunen
- [[brain__index]] — masterindex

## Wat NIET in workflow zit

| Onderwerp | Waar dan wel |
|---|---|
| Ontologie-conventies (naming, namespaces) | [[brain__decisions__D-register]] (D2, D3, D5 etc.) |
| Bron-licentie-discipline | [[brain__sources__source-register]] + [[brain__concepts__provenance-en-attribuering]] |
| Module-conventies | [[brain__modules__module-register]] |
| Karakter-beleid (organisatie-naam etc.) | Projectinstructie v1.7 (`gedeelde gedragsregels`) |

— Einde workflow-register.
