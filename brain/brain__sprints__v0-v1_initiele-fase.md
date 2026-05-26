---
type: sprint
id: v0-v1
title: v0.x / v1.x — initiele fase
status: superseded
date: 2026-03-01
related:
  - v2_0_fix-release
sources: []
chat-sources: []
confidence: skelet-only
gaps:
  - "Exacte datums onbekend"
  - "Geen directe chats teruggevonden binnen project"
  - "Inhoud bekend alleen via retrospectieve referenties in v2.0-fixes-paragraaf en tech-chat 16 maart 2026"
  - "Onbekend of v0.1 ooit één samenhangend bestand was of parallel-ontwikkelde module-stubs"
---

# v0.x / v1.x — initiele fase

## Status

**Skelet-only reconstructie.** Geen directe bronchats teruggevonden binnen dit project. Wat hieronder staat is afgeleid uit retrospectieve referenties in latere documenten.

## Wat bekend is

- Eerste werkversies van het GRC Kennismodel, vóór v2.0
- **Module-niveau versionering** toegepast: vroege ontwerpkeuzes verwijzen naar bijv. "M3 v0.1" als afzonderlijke marker — modules werden iteratief opgebouwd, niet als één big-bang-release
- **Twee fundamentele problemen** die v2.0 ging fixen:
  - ISO 27002-controls bestonden onder twee namespaces (`ctrl:` in M2 en `bio:` in M8) zonder owl:sameAs-brug — cross-framework SPARQL-queries leverden geen resultaten
  - Ontologie-header was minimaal of incompleet (geen volledige `owl:Ontology`-declaratie, geen PROV-O, geen versionIRI)
- **Vroege modelleer-keuzes** zichtbaar in taxonomie-chat 16 maart 2026:
  - Risk-model met named individuals voor Likelihood/Impact (5-puntsschaal uit ISO 31000/27005)
  - Threat vs ThreatSource als aparte klassen (NIST 800-30-conventie)
  - `mitigatedBy` als cross-module property M3 → M2
  - `ResidualRisk` als subklasse van `Risk`
- **Namespace-conventie:** `https://grc.organisatie.nl/ontology/XXX#` met `#`-separator en organisatie-specifieke host

## Wat onbekend is

- Datums (vermoedelijk februari/maart 2026, vóór 16 maart)
- Aantal modules, klassen, individuals
- Of er sub-versies waren (v0.1, v0.2, v1.0, v1.1?)
- Of v1.x al gestart was met BIO 2.0 of pas in v2.0
- Welke modules in v0.1 al bestonden

## Belangrijke vroege modelleer-keuzes die nog steeds gelden

Veel keuzes uit deze fase staan ten grondslag aan latere D-decisions:

- [[brain__decisions__D01_owl-2-dl-profiel]] — OWL 2 DL profiel
- [[brain__decisions__D02_turtle-serialisatie]] — Turtle als werkformaat
- [[brain__decisions__D04_skos-cross-framework]] — SKOS-properties voor cross-framework mappings
- [[brain__decisions__D07_bio2-twee-klassen]] — `bio:BIOControl` + `bio:OverheidsMaatregel` als aparte klassen

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| ±2026-02/03 | active | Initiële werkversies |
| ±2026-03-16 (voorafgaand) | superseded | Opgevolgd door v2.0 fix-release |

— Einde v0.x/v1.x.
