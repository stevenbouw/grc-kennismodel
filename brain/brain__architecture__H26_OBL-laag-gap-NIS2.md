---
type: h-item
id: H26
title: OBL-laag gap NIS2 (art. 18, 19, 22, 24)
status: open
date: 2026-04-22
related:
  - D12_drie-laags-compliance
  - v4_3_3_d12-en-predicate-consolidatie
sources:
  - patch-rapport-v4_3_3
  - projectinstructie-v1.6
chat-sources:
  - https://claude.ai/chat/7ec4a4dc-7230-4135-96f4-c791e7271656
confidence: high
---

# H26 — OBL-laag gap NIS2 (art. 18, 19, 22, 24)

## Status

**Open architectuur-vraag** post-v4.3.3. Inhoudelijke GRC-analyse vereist, niet technisch op te lossen.

## Probleem

Onder [[brain__decisions__D12_drie-laags-compliance]] zou je verwachten dat elk NIS2-artikel met een `compl:REQ_NIS2_*`-individual ook een `compl:OBL_NIS2_*`-individual heeft (laag 2 legal obligation). In v4.3.3 is dat niet zo:

| Artikel | REQ_*-laag | OBL_*-laag |
|---|---|---|
| Art. 18 | ✓ (1 REQ) | ✗ ontbreekt |
| Art. 19 | ✓ (1 REQ) | ✗ ontbreekt |
| Art. 20 | ✓ (2 REQ) | ✓ |
| Art. 21 | ✓ (10 REQ — Art21_a..j) | ✓ |
| Art. 22 | ✓ (1 REQ) | ✗ ontbreekt |
| Art. 23 | ✓ (3 REQ) | ✓ |
| Art. 24 | ✓ (1 REQ) | ✗ ontbreekt |

Drie `OBL_NIS2_*`-individuals bestaan (art. 20, 21, 23). Gap voor art. 18, 19, 22, 24.

## Vraag: bewuste keuze of vergeten?

Twee mogelijke interpretaties:

**Interpretatie A — bewuste keuze.** Niet elk artikel rechtvaardigt een laag-2-individual; alleen artikelen die een zelfstandig juridisch concept introduceren dat onafhankelijk van specifieke eisen bestaat. Bv. art. 21 introduceert "cybersecurity risk management measures"-concept; art. 18 (algemene bepaling), art. 19 (governance-aanwijzing), art. 22 (toezicht), art. 24 (handhaving) zijn meer procedureel dan juridisch concept-introducerend.

**Interpretatie B — gap door iteratieve opbouw.** Niet alle artikelen zijn even systematisch gemodelleerd; de OBL-laag is incrementeel toegevoegd waar onmiddellijk behoefte was.

## Onderzoeksvraag

Per artikel een GRC-inhoudelijke analyse:
- Vertegenwoordigt het juridisch een obligation-laag-concept?
- Of is het alleen een informatie-/melding-/procedure-verplichting?

Antwoord bepaalt of OBL-laag wordt aangevuld of formeel als "deze artikelen hebben geen OBL-laag, en dat is correct" wordt gedocumenteerd.

## Waarom open

Vereist juridische / GRC-domein-analyse. Niet pure ontologie-werk. Mogelijk aanpakken bij Fase 2 (CBW/Cbb-uitbouw) waar vergelijkbare per-artikel-keuzes gemaakt moeten worden.

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-04-22 | open | Geïdentificeerd tijdens v4.3.3-D12-formalisering |

— Einde H26.
