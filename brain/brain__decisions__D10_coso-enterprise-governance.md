---
type: decision
id: D10
title: COSO ICF/ERM als enterprise-governance-laag (Laag 0)
status: active
date: 2026-03-17
related:
  - D09_framework-neutraliteit
sources:
  - projectinstructie-v1.6
chat-sources:
  - https://claude.ai/chat/76420a5b-11ac-4f22-af7a-5e2404201bdd
confidence: high
---

# D10 — COSO ICF/ERM als enterprise-governance-laag

## Beslissing

**COSO ICF** (Internal Control Framework) en **COSO ERM** (Enterprise Risk Management) worden opgenomen als **Laag 0 — enterprise-governance** boven COBIT 2019.

Het hiërarchisch normenkader wordt:

```
Laag 0 — Enterprise governance:    COSO ICF + COSO ERM
Laag 1 — IT-governance:            COBIT 2019, BVA-stelsel, CIO-stelsel
Laag 2 — Wet- en regelgeving:      NIS2, VIR 2007, VIRBI 2025, AVG, CBW, DORA, Cbb
Laag 3 — Operationeel kader:       BIO 2.0
Laag 4 — Normen:                   ISO 27001/27002/27005/31000/22301, NIST 800-53
Laag 5 — Audit & verantwoording:   ENSIA
```

## Aanleiding

In v0.x/v1.x ontbrak een bovenliggende enterprise-laag. COBIT 2019 was de hoogste laag, maar COBIT zelf is een IT-governance-framework — niet een enterprise-governance-framework. Het bestuur stuurt op enterprise-niveau (financieel, strategisch, operationeel), waarbij IT slechts één dimensie is.

COSO biedt het generieke enterprise-kader; COBIT is de IT-invulling daarvan. Door COSO als Laag 0 op te nemen wordt het kennismodel ook bruikbaar voor niet-IT-compliance-vragen (financiële controle, ERM in brede zin).

## Implementatie

- Module M17 (COSO/COBIT) voegt COSO ICF en COSO ERM toe als framework-individuals
- COBIT 2019 verwijst via `fw:isComponentOf` naar COSO als bovenliggende laag (specifiek: COBIT MEA02 → COSO ICF; COBIT EDM03 + APO12 → COSO ERM)
- Vijf COSO ICF-componenten en vijf COSO ERM-pillars (Strategic/Operational/Reporting/Compliance/Performance) als sub-individuals
- Klasse-classificatie: COSO valt onder `fw:BestPractice` (consistent met COBIT — Optie A van M17-architectuurkeuze)

## Afgeleide consequenties

- Pakt de "enterprise governance"-leemte uit Laag 0 gat
- COSO-componenten zijn referentie-individuals; geen volledige ABox-populatie (Spoor B-werk)
- Bestuur-rapportages kunnen straks via Laag 0 worden ingestoken in plaats van direct op BIO 2.0
- Architectuur-test van [[brain__decisions__D09_framework-neutraliteit]] geldt: COSO is gelijkwaardig naast COBIT, niet "boven" als architecturaal centrum — alleen normatief als enterprise-laag

## Wat het niet betekent

- D10 betekent niet dat COBIT vervangen is — COBIT blijft Laag 1, COSO biedt complementaire enterprise-view
- D10 betekent niet dat de organisatie COSO formeel implementeert als bestuurstool — het is een referentie-kader in het model
- D10 betekent niet dat Three Lines Model (IIA 2020) is afgewezen — H29 reserveert dat als latere uitbreiding

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-03-17 | active | Vaststelling in masterchat (besluit gelijktijdig met [[brain__decisions__D09_framework-neutraliteit]]) |

— Einde D10.
