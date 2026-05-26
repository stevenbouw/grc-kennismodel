---
type: decision
id: D3
title: D3 — 11 namespaces voor ontologie
status: active
date: 2026-05-19
related:
  - v4_2_0_M18-asset-module
  - v4_5_0_fase-3-nist-csf-2-0
sources:
  - patch-rapport-v4_5_0
chat-sources: []
confidence: high
---

# D3 — 11 namespaces voor ontologie

## Beslissing

De ontologie gebruikt **elf namespaces** voor logische scheiding van model-onderdelen. Elke namespace heeft een vaste IRI-pattern en wordt strikt toegepast — geen mengvormen, geen overlap-individuals.

| Prefix | IRI | Doel | Toegevoegd in |
|---|---|---|---|
| `fw:` | `https://grc.example.org/framework/` | Framework-individuals | Initieel |
| `ctrl:` | `https://grc.example.org/control/` | Generieke controls (ISO 27002, NIST 800-53, CBW) | Initieel |
| `risk:` | `https://grc.example.org/risk/` | Risico-model | Initieel |
| `roles:` | `https://grc.example.org/roles/` | Rollen + RACI | Initieel |
| `compl:` | `https://grc.example.org/compliance/` | Drie-laags compliance (D12) | Initieel |
| `isms:` | `https://grc.example.org/isms/` | ISMS + canonieke SoA (D8) | Initieel |
| `biz:` | `https://grc.example.org/business/` | Business-context | Initieel |
| `bio:` | `https://grc.example.org/bio/` | BIO 2.0 (D5+D7) | Initieel |
| `ext:` | `https://grc.example.org/extended/` | Cross-framework uitbreidingen + SourceAttribution | Initieel |
| `asset:` | `https://grc.example.org/asset/` | Asset-taxonomie (D11) | v4.2.0 |
| **`csf:`** | **`https://grc.example.org/csf/`** | **NIST CSF 2.0 (M21)** | **v4.5.0** ✨ |

## Datum

- **Initieel:** 10 namespaces inclusief asset:
- **v4.2.0** (13 april 2026) — `asset:` toegevoegd voor M18
- **v4.5.0** (19 mei 2026) — `csf:` toegevoegd voor M21 NIST CSF 2.0 — **eerste expansie sinds v4.2.0**

## Waarom een aparte csf:-namespace (v4.5.0)

NIST CSF 2.0 had op twee andere manieren gemodelleerd kunnen worden:

| Alternatief | Reden voor afwijzing |
|---|---|
| **A — In `ext:` opnemen** | CSF-individuals zouden vermengen met SourceAttributions en andere cross-framework-properties; conceptuele vervuiling |
| **B — In `fw:` opnemen** | `fw:` is voor framework-individuals (CSF zelf is daar), niet voor CSF-componenten (Functions/Categories/Subcategories) |

Aparte `csf:`-namespace houdt CSF-componenten **als eigen cluster** zichtbaar in queries en SHACL-shapes, terwijl `fw:NIST_CSF_2_0` als kader-individual op zijn juiste plek staat.

## D9-compatibel

Toevoeging van `csf:` is **conform D9 framework-neutraliteit**: csf: is een 11e gelijkwaardige namespace náást de bestaande, niet een centraal organiserend kader. CSF Functions zijn outcomes; ze worden gemapt naar bestaande beheersmaatregelen via SKOS-mappings, niet als organisatie-principe gebruikt.

Zie [[brain__decisions__D09_framework-neutraliteit]] voor de D9-discipline. Zie [[brain__sprints__v4_5_0_fase-3-nist-csf-2-0]] voor de M21-implementatie (Optie B — gemapt referentiekader).

## D3-toepassings-status v4.5.0

Per `D3_namespaces_used` in canonical_metrics_v4_5_0.json:

| Namespace | Subjects |
|---:|---:|
| `csf:` | 505 |
| `ext:` | 280 |
| `bio:` | 252 |
| `ctrl:` | 205 |
| `isms:` | 201 |
| `compl:` | 150 |
| `risk:` | 128 |
| `fw:` | 99 |
| `biz:` | 98 |
| `roles:` | 75 |
| `asset:` | 25 |

`csf:` is direct na introductie de **grootste namespace per subjectcount** (door 363 IE-individuals). Geen architectuur-probleem — IEs zijn bewust granulaire individuals.

## Wat het niet betekent

- **Geen verplichte volgorde** in namespace-declaraties in `.ttl`-bestanden (Turtle-conventie volgt vrije volgorde)
- **Geen verplichting** dat elke namespace in elk bestand wordt gebruikt — alleen waar relevant
- **Geen statische limiet** op 11 — bij toekomstige fase-uitbreidingen (ISO 42001, ISO 9001) kunnen verdere namespaces toegevoegd worden, mits D9-conform

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| Initieel | active | 10 namespaces gedefinieerd (asset: nog niet) |
| 2026-04-13 | active | v4.2.0 — `asset:` als 10e namespace toegevoegd |
| 2026-05-19 | active | v4.5.0 — `csf:` als 11e namespace toegevoegd voor M21 NIST CSF 2.0 |

## Hangt samen met

- [[brain__decisions__D04_skos-cross-framework-mappings]] — SKOS-mappings bridge cross-namespace
- [[brain__decisions__D09_framework-neutraliteit]] — csf:-toevoeging conform D9
- [[brain__modules__M21_nist-csf-2-0-planned]] — module die csf: gebruikt
- [[brain__sprints__v4_2_0_M18-asset-module]] — sprint waar asset: werd toegevoegd (10e)
- [[brain__sprints__v4_5_0_fase-3-nist-csf-2-0]] — sprint waar csf: werd toegevoegd (11e)

— Einde D3.
