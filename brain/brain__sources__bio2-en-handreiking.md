---
type: source
title: BIO 2.0 + Handreiking BIO2-opmaat
status: living
date: 2026-05-13
related:
  - M08_bio20
  - M02_iso27002-control
  - bbn-correctie
sources: []
chat-sources: []
confidence: high
---

# BIO 2.0 + Handreiking BIO2-opmaat

## Twee bron-documenten, niet één

| Document | Bestand | Versie | Bevat |
|---|---|---|---|
| **BIO 2.0** | `20250924baselineinformatiebeveiligingoverheid2bio2v12deff.pdf` | v1.2, 24 sept 2025 | Het normenkader: 93 BIO-controls + 148 OverheidsMaatregelen |
| **Was-wordt + Handreiking + BIO 1.04** | `20260302waswordtlijstbio_bio2v13inexcel_hrbio2opmaat_bio1v104zvv20def.xlsx` | v1.3 def (2 maart 2026) | BIO 2.0 in Excel-formaat + Handreiking BIO2-opmaat + BIO 1.04-tabel |

Beide bestanden zijn nodig — BIO 2.0 PDF voor het normenkader zelf, Excel voor BBN-classificatie via de Handreiking-tab.

## BIO 2.0 v1.2 — eigenlijke kader

Beheerders: BZK / CIP (Centrum Informatiebeveiliging en Privacybescherming) + VNG, IPO, Unie van Waterschappen.

Structuur volgt ISO 27001 Bijlage A + ISO 27002: **93 controls** in clausules 5–8 (organisatorisch, mensen, fysiek, technisch) + 148 **OverheidsMaatregelen** als Rijks-specifieke aanvullingen.

Inhoudsmodel:
- BIO 2.0 classificeert via **ISO 27002-attributen** (control_type, info_security_properties, cybersecurity_concepts, operational_capabilities, security_domains)
- **Niet** via BBN-niveaus

## Handreiking BIO2-opmaat — transitie-document

Apart document, opgenomen in Excel-bron. Doel: gemeenten en organisaties helpen bij migratie van BIO 1.04 naar BIO 2.0. Hierin staan de **BBN-niveaus 1 en 2** (geen 3) — bedoeld als praktisch baselining-instrument, niet als BIO 2.0-classificatie.

Zie [[brain__concepts__bbn-correctie]] voor het inhoudelijke onderscheid en consequenties voor het kennismodel.

## Toepassing in ontologie

- M08 — BIO 2.0 als individuals
- M02 — ISO 27002-controls (zelfde 93, andere namespace `ctrl:`)
- `ext:hasHandreikingBBN` — Handreiking-specifieke property, **niet** een BIO 2.0-eigenschap
- 93 owl:sameAs D5-bruggen ctrl:↔bio: (zie [[brain__decisions__D05_sameAs-strikt-ctrl-bio]])

## Licentie

**Onbeperkt** — overheidspublicatie, vrij herbruikbaar, geen attributie-eis.

## Geplande v4.4.0-gebruik

- Sheet 9 mappings naar CBW/Cbb (via Excel)
- Route 5: ENISA-guidance attachment op 73 van 93 BIO-controls

— Einde BIO 2.0-bron.
