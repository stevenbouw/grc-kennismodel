---
type: source
title: ISO-normen bundle (NEN-restrictief)
status: living
date: 2026-05-13
related:
  - M02_iso27002-control
  - M09_iso27001-ext
  - M13_iso22301
  - M03_risk
  - provenance-en-attribuering
sources: []
chat-sources: []
confidence: high
---

# ISO-normen bundle — NEN-restrictief

## Zes ISO-normen onder NEN-licentie

Alle via NEN Connect-licentie (Rijksoverheid 2016-2020, verlengd) — **geen tekst-reproductie in het model**.

| Bestand | Norm | Module |
|---|---|---|
| `NEN-EN-ISO_IEC_27002_2022_nl.pdf` | ISO/IEC 27002:2022 — Information security controls | M02 |
| `NENENISO_IEC_27001_2023_nl2.pdf` | ISO/IEC 27001:2022 (NL-versie 2023) — ISMS requirements | M09 |
| `NENENISO_IEC_27005_2024_en.pdf` | ISO/IEC 27005:2024 — Information security risk management | M03 |
| `NENISO_31000__C11_2019_nl.pdf` | ISO 31000:2018+C11:2019 — Risk management guidelines | M03 |
| `NENENISO_22301_2019_A1_2024_en.pdf` | ISO 22301:2019+A1:2024 — Business continuity management requirements | M13 |
| `NENENISO_22313_2020_nl.pdf` | ISO 22313:2020 — Business continuity management guidance | M13 |

## NEN-restrictieve licentie

NEN is **Stichting Koninklijk Nederlands Normalisatie Instituut** — beheert publicatie en verspreiding van Nederlandse implementaties van internationale normen. Beperkingen:

- **Geen verbatim reproductie** van normentekst, behalve via gelicentieerde kanalen
- **Geen openbare publicatie** van substantiële parafraseringen
- Klasse-structuur, clausule-nummering, control-identifiers zijn **feitelijk** (niet auteursrechtelijk beschermd)
- Korte fragmenten (titels, korte definities) onder fair use / citaatrecht toegestaan

## Wat wel/niet in ontologie

| Wat | Toegestaan? |
|---|---|
| Control-identifiers (5.01, 5.02, ...) | Ja — feitelijk |
| Control-titels (rdfs:label) | Ja — korte fragmenten |
| Volledige control-beschrijvingen | **Nee** — verbatim verboden |
| Implementation guidance | **Nee** — verbatim verboden |
| Clausule-nummers en namen | Ja — feitelijk |
| Klasse-structuur (HSClause) | Ja — feitelijk |

## Praktische gevolgen

Bij Route 3 (BIO Control-statement + Doel uit BIO-Excel) is gebruik gemaakt van BIO 2.0 (onbeperkt) in plaats van direct ISO 27002 — **bewuste licentie-keuze**. BIO 2.0 reproduceert de ISO 27002-controls op vergelijkbare wijze maar onder overheidspublicatie-status.

Route 1 / 1-light (ISO-guidance parafrasering) is geparkeerd naar v5.x — substantiële parafrasering valt buiten NEN-licentie.

## Cross-references

- [[brain__concepts__provenance-en-attribuering]] — licentie-bewustzijn-discipline
- [[brain__scope__route-1-iso-guidance-parafrasering-geparkeerd]] — geparkeerde route

— Einde ISO-normen bundle.
