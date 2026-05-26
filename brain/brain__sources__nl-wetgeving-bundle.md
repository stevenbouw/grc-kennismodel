---
type: source
title: NL wet- en regelgeving bundle
status: living
date: 2026-05-13
related:
  - M16_virbi-ext
  - M04_roles
  - M10_nis2-ext
sources: []
chat-sources: []
confidence: high
---

# Nederlandse wet- en regelgeving bundle

## Zeven NL-bron-documenten

Allemaal **publiek NL-recht** — vrij herbruikbaar, geen auteursrechtelijke restrictie.

| Bestand | Bron | Status | Module |
|---|---|---|---|
| `VIR_2007.pdf` | Voorschrift Informatiebeveiliging Rijksdienst 2007 (5 artikelen) | Van kracht | M01 (fw:VIR_2007) |
| `VIRBI_2025.pdf` | Voorschrift Informatiebeveiliging Bijzondere Informatie 2025 | Van kracht | M16 (kernverplichting) |
| `stcrt20267416n1.pdf` | Staatscourant 2026, nr. 7416 — VIRBI-wijziging | Van kracht | M16 (update-bron) |
| `BVAstelsel.pdf` | Besluit BVA-stelsel Rijksdienst 2021 — Beveiligingsambtenaren | Van kracht | M04 (BVA-rollen) |
| `Besluit_CIOstelsel_2026.pdf` | Besluit CIO-stelsel 2026 | Van kracht | M04 + M18 (CIO-rol + art. 1o componenten) |
| `TK_Bijlage_1_Cyberbeveiligingsbesluit_amvb.pdf` | Cyberbeveiligingsbesluit (Cbb) — AMvB onder CBW | **Concept t.b.v. Tweede Kamer**, niet vastgesteld | M10 (gepland v4.4.0) |
| (n.v.t. — wet-tekst) | Cyberbeveiligingswet (CBW) | **In voorbereiding**, niet van kracht | M10 (gepland v4.4.0) |

## Status-discipline

**CBW** wordt in alle documenten gemarkeerd als **"in voorbereiding"** — de Nederlandse implementatie heeft de NIS2-transpositiedeadline gemist. **Cbb** als **"concept t.b.v. Tweede Kamer, nog niet vastgesteld"** — inwerkingtreding bij koninklijk besluit.

Statuswijzigingen moeten gemonitord worden via Spoor C (governance-beheer). Dit hoort niet in Spoor A (technische ontologie-opbouw) — wel impact op modelleer-conventies (status-markering, "in voorbereiding"-tags).

## Geen organisatienaam-conventie

Alle modellering blijft generiek — gebruik "de organisatie" of "Rijksoverheidsorganisatie", nooit specifieke organisatie-namen. Dit is een architectuur-invariant (organisatie-neutraal model).

## Cross-references

- M01 — VIR 2007, BVA-stelsel, CIO-stelsel als `fw:`-individuals
- M04 — BVA en CIO-stelsel-rollen
- M16 — VIRBI 2025 als kernverplichting
- M10 — NIS2 + (gepland) CBW + Cbb
- M18 — `asset:InformationSystem` strikt per CIO-stelsel 2026 art. 1o componenten

## Correctie-note 26 mrt 2026

VIR 2007 heeft slechts **5 artikelen**. Foutieve early references naar "VIR Art. 5 BVA" en "VIR Art. 9 rapportage" zijn geherclassificeerd naar Besluit BVA-stelsel.

— Einde NL wetgeving bundle.
