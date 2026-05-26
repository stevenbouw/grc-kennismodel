---
type: module
id: M16
title: M16 — VIRBI extensie (fw:)
status: active
date: 2026-05-13
related: []
sources:
  - VIRBI_2025
  - stcrt20267416n1
chat-sources: []
confidence: high
---

# M16 — VIRBI extensie

## Bestand
`m16-virbi-ext.ttl`

## Namespace
Hergebruikt `fw:` voor framework + `compl:` voor verplichtingen.

## Wat het bevat

VIRBI 2025 — **Voorschrift Informatiebeveiliging Bijzondere Informatie**. Kernverplichting voor de organisatie omdat deze gerubriceerde / staatsgeheim-informatie verwerkt.

| Inhoud | Toelichting |
|---|---|
| `fw:VIRBI_2025`-individual | Voorschrift in Laag 2 |
| Compliance-verplichtingen | Fysieke beveiliging, personeelsveiligheid (VGB), compartmentalisatie, crypto |
| Bron-document update | `stcrt20267416n1.pdf` (Staatscourant) — recente wijzigingen |
| Rubriceringsniveaus | DEPVERTROUWELIJK, STAATSGEHEIM CONFIDENTIEEL/GEHEIM/ZEER GEHEIM |

## Waarom kernverplichting, niet aanvullend

De organisatie verwerkt informatie die onder VIRBI valt. Daarom is VIRBI **geen optionele aanvulling** maar een verplichte kaderlaag-2-norm naast BIO 2.0. Heeft consequenties voor:

- **Fysieke beveiliging** — zones, compartimentalisatie
- **Personeelsveiligheid** — Verklaring Geen Bezwaar (VGB), screening niveau A/B/C
- **Crypto** — minimaal toegestane algoritmen per rubriceringsniveau
- **Informatiebeheer** — gerubriceerde-info-tracking

## D-relaties

- [[brain__decisions__D09_framework-neutraliteit]] — VIRBI gelijkwaardig naast BIO 2.0, niet ondergeschikt
- v0.x-correctie 26 mrt 2026: foutieve "VIR Art. 5 BVA" en "VIR Art. 9 rapportage" zijn geherclassificeerd naar Besluit BVA-stelsel (M04/M05), niet VIRBI

## Bronlicentie

VIRBI 2025 = publiek NL-recht — vrij herbruikbaar.

— Einde M16.
