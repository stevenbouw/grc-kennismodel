---
type: scope
title: Route 1 / 1-light — ISO-guidance parafrasering — geparkeerd
status: parked
date: 2026-04-20
related:
  - iso-normen-bundle
  - provenance-en-attribuering
sources:
  - projectinstructie-v1.6
chat-sources: []
confidence: high
---

# Route 1 / 1-light — ISO-guidance parafrasering — geparkeerd

## Beslissing

Route 1 en Route 1-light voor context-integratie van ISO-guidance (uit H24-routes) zijn **geparkeerd naar v5.x** of later. Geen actieve scope tot fundamentele licentie-heroverweging.

## Wat Route 1 / 1-light zou zijn

Onderdeel van H24 — context-integratie BIO/ISO-guidance. **Vijf routes** geïdentificeerd in v4.3.0-diagnostiek:

| Route | Wat | Status |
|---|---|---|
| **Route 1** | Volledige ISO 27002-implementation guidance parafraseren in model | **Geparkeerd v5.x** |
| **Route 1-light** | Korte parafraseringen / kernpunten per control | **Geparkeerd v5.x** |
| Route 2 | ISO-clausule-verwijzing (alleen referenties, geen tekst) | GO, gepland Fase 2 |
| Route 3 | BIO Control-statement + Doel uit BIO-Excel | GO, gepland Fase 2 |
| Route 5 | ENISA-guidance via CBW-Excel (CC-BY 4.0) | GO, gepland Fase 2 |

Route 4 bestaat niet als formeel item (nummergap).

## Waarom geparkeerd

**NEN-licentie-restrictie.** ISO 27002:2022 is NEN-restrictief ([[brain__sources__iso-normen-bundle]]). Substantiële parafrasering van implementation guidance valt buiten gelicentieerde gebruik — ook al is parafrasering "in eigen woorden", de juridische scheidslijn is onduidelijk.

Bewuste licentie-keuze: liever **andere bronnen** gebruiken die wel onder gunstige licentie vallen:
- BIO 2.0 (Route 3) — overheidspublicatie, onbeperkt
- ENISA-guidance (Route 5) — CC-BY 4.0, attributie

Daarmee dekt het model 73 van 93 BIO-controls met externe guidance, zonder NEN-licentie-risico.

## Wat ontbreekt door deze keuze

20 ISO 27002-controls hebben geen implementation guidance in het kennismodel via Route 2/3/5. Deze controls hebben wel:

- Control-titel (Route 2 — ISO-clausule-verwijzing)
- Mapping naar BIO 2.0 / NIST 800-53 / NIS2 (cross-framework)
- Maar geen verrijkende implementation-tekst in het model zelf

Voor diepere implementation-detail moet de gebruiker terug naar de ISO 27002 NEN-publicatie.

## Trigger voor heroverweging — v5.x

Heroverweging vereist:

1. **Licentie-clearance** — onderzoek met NEN over toelaatbaarheid van implementation-detail-modellering
2. **OR**: alternatieve bron met IB-equivalent (bv. uitgebreide CIS Benchmarks of NIST 800-53-implementation-detail)
3. **OR**: organisatie schaft NEN-enterprise-licentie aan die intern hergebruik toestaat

Tot die tijd: status `parked`, niet actief.

## Cross-references

- [[brain__sources__iso-normen-bundle]] — NEN-licentie-discipline
- [[brain__concepts__provenance-en-attribuering]] — licentie-bewustzijn
- [[brain__sources__enisa-guidance]] — Route 5 alternatief

— Einde Route 1 geparkeerd.
