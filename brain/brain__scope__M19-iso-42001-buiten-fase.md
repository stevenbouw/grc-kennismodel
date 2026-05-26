---
type: scope
title: M19 ISO 42001 (AI Management) — niet in scope Fase 1-3
status: deferred
date: 2026-05-13
related:
  - H31_toetsingskader-algoritmes
  - module-register
sources:
  - projectinstructie-v1.6
chat-sources: []
confidence: high
---

# M19 ISO 42001 — niet in scope Fase 1-3

## Beslissing

ISO/IEC 42001:2023 — AI Management System — is **niet in scope** voor Fasen 1, 2 en 3 van het GRC Kennismodel. Mogelijk Fase 4 of later na expliciete masterchat-evaluatie.

## Wat ISO 42001 is

Eerste internationale managementsysteem-norm voor **Artificial Intelligence**. Gepubliceerd december 2023. Structuur conform Harmonized Structure (HS / Annex SL) — clausules 4-10 vergelijkbaar met ISO 27001 en ISO 22301.

## Waarom niet in Fase 1-3

- **Fase 1 (v4.0-4.3.x)** — Foundation-fase, focus op IB-controls en wet/regelgeving-mapping
- **Fase 2 (v4.4.0)** — CBW + Cbb-uitbouw + ENISA-guidance
- **Fase 3 (v4.5.0)** — NIST CSF 2.0 integratie (M21)

Geen van deze fasen heeft AI-management als directe scope. De organisatie verwerkt AI-gerelateerde risico's via bestaande GRC-controls, niet via een aparte AI-managementsysteem-laag.

## Mogelijk in Fase 4+

Trigger voor heroverweging:

- Wanneer Algoritmekader BZK (in ontwikkeling per september 2025) duidelijker vorm krijgt
- Wanneer [[brain__architecture__H31_toetsingskader-algoritmes]] een M19-relatie vereist voor Ethiek-perspectief
- Wanneer de organisatie ISO 42001-certificering overweegt

## Harmonized Structure maakt toekomstige opname mechanisch

Omdat ISO 42001 dezelfde HS-structuur deelt als ISO 27001 (M09) en ISO 22301 (M13), is toekomstige integratie **mechanisch**:

- `ext:AIMSRequirement` als subklasse van `compl:ComplianceRequirement`
- Clausules 4-10 als individuals
- `ext:alignsWithHSClause` brugt naar bestaande `ext:HSClause_*`-individuals

Geen nieuwe namespace nodig, geen nieuwe property-uitvinding — past in bestaande architectuur.

## Verwacht effort bij opname

Indicatief (geen masterchat-bevestiging):

- Klassen: ~3-5 nieuwe
- Individuals: ~30-50 (vergelijkbaar met M09/M13)
- SKOS-mappings: naar M09 (ISO 27001), M14 (AVG/GDPR), mogelijk H31 (Toetsingskader Algoritmes)
- Triples: ~150-250

## Cross-references

- [[brain__architecture__H31_toetsingskader-algoritmes]] — kan AI-management-perspectief vereisen
- [[brain__modules__module-register]] — uitsluitingen-sectie

— Einde M19 niet in scope.
