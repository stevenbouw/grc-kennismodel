---
type: module
id: M14
title: M14 — AVG/GDPR (compl:)
status: active
date: 2026-05-13
related:
  - H31_toetsingskader-algoritmes
sources: []
chat-sources: []
confidence: high
---

# M14 — AVG / GDPR

## Bestand
`m14-avg-gdpr.ttl`

## Namespace
Hergebruikt `compl:` + `fw:AVG`.

## Wat het bevat

**Alleen de IB-raakvlakken van de AVG** — geen volledige AVG-implementatie. Scope vastgelegd op 16 maart 2026.

| Artikel | Onderwerp |
|---|---|
| Art. 5 lid 1 sub f | Integriteit en vertrouwelijkheid (security by design) |
| Art. 25 | Privacy by Design and by Default |
| Art. 32 | Beveiliging van de verwerking |
| Art. 33 | Melding van inbreuken aan toezichthouder |
| Art. 34 | Melding van inbreuken aan betrokkenen |

## Klassen

`compl:AVGRequirement` als specifieke subklasse van `compl:ComplianceRequirement`.

## Waarom alleen IB-raakvlak

AVG is privacy-wetgeving; alleen de artikelen met directe informatiebeveiligings-impact landen in dit GRC-kennismodel. Volledige AVG-modellering (consent, DPIA, transparantie, betrokkenen-rechten) hoort thuis in een privacy-management-systeem, niet in een IB-kennismodel.

Besluit: niet uitbreiden buiten IB-scope zonder masterchat-GO.

## Toekomst-relaties

- [[brain__architecture__H31_toetsingskader-algoritmes]] — Toetsingskader Algoritmes (AR) heeft een Privacy-perspectief dat naar M14 wijst
- Fase 4 maturity-model — AVG-conformiteit als één van de assessment-dimensies

## Bronlicentie

AVG = publiek EU-recht — vrij herbruikbaar.

— Einde M14.
