---
type: module
id: M13
title: M13 — ISO 22301 BCM (ext:)
status: active
date: 2026-05-13
related: []
sources:
  - NENENISO_22301_2019_A1_2024_en
  - NENENISO_22313_2020_nl
chat-sources: []
confidence: high
---

# M13 — ISO 22301 BCM

## Bestand
`m13-iso22301.ttl`

## Namespace
Hergebruikt `ext:` voor BCMRequirement.

## Wat het bevat

ISO 22301:2019 Business Continuity Management System + ISO 22313:2020 (toelichting/guidance). Clausules 4–10 conform Harmonized Structure.

| Inhoud | Aantal |
|---|---:|
| `ext:BCMRequirement`-subjects (clausules 4–10) | meerdere per clausule |
| Klassen | `ext:BCMRequirement` subClassOf `compl:ComplianceRequirement` |
| HS-alignment | via `ext:alignsWithHSClause` (analoog aan M09) |

## Harmonized Structure (HS / Annex SL)

ISO 22301 deelt HS met ISO 27001 (M09) en toekomstig ISO 42001 (M19, buiten Fase 1-3) en ISO 9001 (M20, niet in scope). Maakt cross-norm-uitlijning mogelijk via dezelfde `ext:HSClause`-individuals.

## Cross-references

- M09 (ISO 27001 ext) — deelt HS-mechanisme
- M06 (ISMS) — sommige BCM-controls overlappen met ISMS-procedures

## Bronlicentie

ISO 22301 en ISO 22313 zijn NEN-restrictief — geen verbatim tekst-reproductie. Klasse-structuur en clausule-IDs zijn feitelijk.

## Status

Active, maar relatief beperkt uitgewerkt. Bedrijfscontinuïteit is onderdeel van de scope van het kennismodel (zie missie); diepere uitwerking afhankelijk van Spoor B.

— Einde M13.
