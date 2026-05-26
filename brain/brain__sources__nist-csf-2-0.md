---
type: source
title: NIST Cybersecurity Framework 2.0 (Public Domain)
status: living
date: 2026-05-19
related:
  - v4_5_0_fase-3-nist-csf-2-0
  - cross-bron-overlap
  - provenance-en-attribuering
sources:
  - NIST_CSWP_29
  - CSF_2_0Implementation_Examples
  - csf2
chat-sources: []
confidence: high
---

# NIST Cybersecurity Framework 2.0

## Bron-identificatie

| Aspect | Detail |
|---|---|
| Officiële titel | NIST Cybersecurity Framework (CSF) 2.0 |
| Uitgever | National Institute of Standards and Technology (NIST) |
| Publicatie-datum | 26 februari 2024 |
| Licentie | **Public Domain** — geen attributie-eis, vrij herbruikbaar |
| Bestand-bronnen in PK | `NIST_CSWP_29.pdf`, `CSF_2_0Implementation_Examples.xlsx`, `csf2.xlsx` |

## Drie distincte bron-artefacten

CSF 2.0 wordt in v4.5.0 uit **drie afzonderlijke NIST-bronnen** geconstrueerd:

| Bron | Wat het levert | Module-landing |
|---|---|---|
| **NIST CSWP 29** | CSF Core (6 Functions + 22 Categories + 106 Subcategories + statements) | M21 — Stap 3 |
| **CSF 2.0 Implementation Examples** | 363 IE-individuals (gemiddeld 3,42 per Subcategory) | M21 — Stap 4 |
| **CSF Reference Tool** | Mappings naar SP 800-53 R5 (en andere kaders) | M11 + M08 + M09 — Stap 6 |

Twee `ext:SourceAttribution`-individuals voor traceability:

```turtle
ext:Attr_NIST_CSF_2_0_Core_2024 rdf:type ext:SourceAttribution ;
  ext:hasLicenseLabel "Public Domain" ;
  ext:hasSourceTitle "NIST CSWP 29 + Implementation Examples" ;
  ext:hasPublisher "NIST" ;
  ext:hasSourceVersion "2.0" ;
  ext:hasSourceDate "2024-02-26" .

ext:Attr_NIST_CSF_2_0_Reference_Tool_2026 rdf:type ext:SourceAttribution ;
  ext:hasLicenseLabel "Public Domain" ;
  ext:hasSourceTitle "NIST CSF Reference Tool" ;
  ext:hasPublisher "NIST" ;
  ext:hasSourceVersion "2026" ;
  ext:hasSourceDate "2026-xx-xx" .
```

## OLIR-format-leerpunt (Stap 6)

**Aanname**: Reference Tool zou OLIR (Online Informative References) JSON-formaat leveren.
**Werkelijkheid**: Reference Tool gebruikt eigen formaat, niet OLIR.
**Gevolg**: Stap 6 fallback naar Reference Tool-eigen export-formaat.

Leerpunt geformaliseerd: **bron-verificatie vóór TBox-declaratie** + voorgenomen toevoeging aan projectinstructie v1.8 als sprint-protocol-element "bron-verificatie vóór raming-opstelling".

Zie [[brain__workflow__sprint-protocollen]] voor de discipline.

## Bron-eigen ontwerp-kenmerken

| Kenmerk | Detail |
|---|---|
| Subcategory-numbering-gaps | `RC.CO-01` en `RC.CO-02` bestaan niet; RC.CO begint bij `-03` (NIST-eigen ontwerp, geen modelfout) |
| GOVERN als nieuwe Function (v2.0) | Niet in CSF v1.x; toegevoegd in v2.0 — relevant voor [[brain__modules__M02_iso27002-control]] D6-update |
| Implementation Examples-distributie | 1-10 per Subcategory, gemiddeld 3,42, max 10 (`GV.SC-05`) |

## Cross-bron-overlap met sheet 8

**105 mappings** komen overeen tussen Sheet 8 (ADR & NOREA) en CSF Reference Tool (NIST). Twee onafhankelijke bronnen → **SKOS-kwaliteits-validatie**. Geen technisch dedup-feit maar een **bron-consistentie-bewijs**.

Zie [[brain__concepts__cross-bron-overlap]] voor de architectuur-betekenis.

## Cross-references

- [[brain__sprints__v4_5_0_fase-3-nist-csf-2-0]] — sprint van integratie
- [[brain__modules__M21_nist-csf-2-0-planned]] — landing-module
- [[brain__concepts__cross-bron-overlap]] — kwaliteits-indicator-pattern
- [[brain__concepts__provenance-en-attribuering]] — SourceAttribution-discipline
- [[brain__sources__source-register]] — overzicht licentie-categorieën

— Einde NIST CSF 2.0 source.
