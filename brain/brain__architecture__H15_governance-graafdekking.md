---
type: h-item
id: H15
title: Governance-graafdekking (Route P/Q/R)
status: parked
date: 2026-04-14
related:
  - D09_framework-neutraliteit
  - D10_coso-enterprise-governance
sources:
  - projectinstructie-v1.6
chat-sources:
  - https://claude.ai/chat/f527e7ab-bc17-44f4-a878-598e8ca7a632
confidence: medium
gaps:
  - "Inhoud van Route P/Q/R-opties niet volledig gereconstrueerd uit beschikbare bronnen"
---

# H15 — Governance-graafdekking

## Status

**Geparkeerd**. Onderdeel van contextdiepte-diagnostiek v4.3.0 (23 bevindingen H1–H23). Wacht op masterchat-architectuurkeuze.

## Probleem

Governance-relaties tussen frameworks zijn niet uniform afgedekt in de graaf. Vooral:

- COSO ICF/ERM (Laag 0) → COBIT (Laag 1) — wel direct via `fw:isComponentOf`
- COBIT → wet- en regelgeving (Laag 2) — gedeeltelijk
- Laag 2 → BIO 2.0 (Laag 3) — via `fw:stelVerplicht` en `fw:implementeert`
- BIO 2.0 → ISO 27001/27002 (Laag 4) — via owl:sameAs (D5) en `fw:baseertOp`
- Audit-laag (ENSIA, Laag 5) → onder-liggende lagen — onvolledig

De graaf is niet "loop-vrij" navigeerbaar vanuit elk perspectief — afhankelijk van waar je begint, raak je dood-eindes.

## Drie opties (Route P/Q/R)

Route-namen uit contextdiepte-diagnostiek; precieze inhoud onvolledig gereconstrueerd. Algemene richting:

- **Route P** — minimal: alleen ontbrekende kritieke relaties toevoegen, geen patroon-completion
- **Route Q** — patroon-completion: voor elk laag-paar dezelfde relatie-set garanderen
- **Route R** — semantische verrijking: aparte properties voor verschillende governance-relaties (verplicht / implementeert / toetst / dekt af)

## Waarom geparkeerd

Geen blocker voor v4.3.x of v4.4.0. Triggers voor herziening:

- Wanneer Fase 4 (M15-ENSIA uitbouw, v4.6.0) een complete audit-trail-graaf vereist
- Wanneer dashboard-export op governance-laag-navigatie wordt gebouwd
- Wanneer architectenkring (cruciale stakeholder) governance-relaties bevraagt

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-04-13 | open | Gevonden bij contextdiepte-diagnostiek v4.3.0 |
| 2026-04-14 | parked | Niet-blokkerend, deferred |

— Einde H15.
