---
type: scope
title: M20 ISO 9001 (Quality Management) — niet in scope
status: excluded
date: 2026-05-13
related:
  - module-register
sources:
  - projectinstructie-v1.6
chat-sources: []
confidence: high
---

# M20 ISO 9001 — niet in scope

## Beslissing

ISO 9001:2015 — Quality Management System — is **niet in scope** voor het GRC Kennismodel.

## Wat ISO 9001 is

Internationale standaard voor kwaliteitsmanagement-systemen. Sterk gerelateerd aan procesbeheersing, klantgerichtheid, continue verbetering. Heeft Harmonized Structure (HS / Annex SL) gemeen met ISO 27001 (M09), ISO 22301 (M13) en ISO 42001 (M19).

## Waarom buiten scope

**Kwaliteitsmanagement valt buiten de GRC-Information Security-focus.** De missie van het kennismodel is:

> Integraal compliance-overzicht over informatiebeveiliging, fysieke beveiliging, personeelsveiligheid, bedrijfscontinuïteit en aanpalende privacy-aspecten — als informatie-laag van het ISMS.

ISO 9001 dekt **breder kwaliteitsmanagement** dan IB-raakvlak — vergelijkbaar met AVG-uitsluiting buiten IB-context (zie [[brain__modules__M14_avg-gdpr]]).

## Verschil met "deferred" (M19)

M19 ISO 42001 = **deferred** (kan later) — AI-management heeft IB-raakvlakken via algoritme-toetsing.

M20 ISO 9001 = **excluded** (niet gepland) — kwaliteitsmanagement is een aparte discipline naast IB.

## Harmonized Structure-overweging

Hoewel ISO 9001 buiten scope is, maakt de gedeelde HS toekomstige integratie **mechanisch eenvoudig** indien ooit nodig:

- `ext:QMSRequirement` als subklasse van `compl:ComplianceRequirement`
- Clausules 4-10 als individuals
- `ext:alignsWithHSClause` brugt naar bestaande `ext:HSClause_*`

Dit verandert echter niets aan de scope-beslissing — ook al is opname technisch eenvoudig, het hoort architecturaal niet in het GRC-IB-kennismodel.

## Trigger voor heroverweging

**Niet voorzien.** Heropname zou een fundamentele scope-uitbreiding van het kennismodel betekenen (van GRC-IB naar GRC-breed). Dat vereist:

- Nieuwe missie-formulering door CISO/CSO
- Master-beslissing over scope-uitbreiding
- Mogelijk nieuw project / fork van huidige kennismodel

Tot die tijd: niet opnemen, ook niet als referentiekader.

## Cross-references

- [[brain__modules__M14_avg-gdpr]] — vergelijkbaar IB-raakvlak-principe
- [[brain__modules__module-register]] — uitsluitingen-sectie

— Einde M20 niet in scope.
