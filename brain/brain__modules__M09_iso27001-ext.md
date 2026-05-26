---
type: module
id: M09
title: M09 — ISO 27001:2022 extensie (ext:)
status: active
date: 2026-05-19
related:
  - v4_5_0_fase-3-nist-csf-2-0
sources:
  - NENENISO_IEC_27001_2023_nl2
chat-sources: []
confidence: high
---

# M09 — ISO 27001:2022 extensie

## Bestand
`m09-iso27001-ext.ttl`

## Namespace
`ext: <https://grc.example.org/extended/>`

## Wat het bevat

ISO 27001:2022 hoofdtekst-clausules (4-10) als individuals, complementair aan de Annex A-controls die in `bio:ISO27002_*` zijn gemodelleerd.

| Inhoud | Aantal v4.5.0 |
|---|---:|
| `ext:ISO27001_*`-individuals (hoofdtekst-clausules) | 48 |
| HSClause-mappings (Harmonized Structure / Annex SL) | (variabel) |
| **csf-mappings landing (v4.5.0)** | csf-subjects: 65 |

## v4.5.0-uitbreiding — csf-mappings landing

In v4.5.0 Stap 5 zijn `skos:closeMatch`-triples vanuit `csf:Subcategory`-individuals geland op `ext:ISO27001_*` (hoofdtekst-clausules). Bron: Sheet 8 van CBW-Excel.

Onderscheid t.o.v. M08:
- **M08 / bio:**: 494 mappings → Annex A-controls (via ctrl:↔bio: sameAs-brug)
- **M09 / ext:**: 147 mappings → hoofdtekst-clausules (direct, geen brug nodig)

Totaal Sheet 8: 494 + 147 = 641 unieke mappings.

## Cross-references

- [[brain__sources__iso-normen-bundle]] — NEN-licentie-context
- [[brain__sources__cbw-excel]] — Sheet 8-bron
- [[brain__sprints__v4_5_0_fase-3-nist-csf-2-0]] — csf-mappings landing
- [[brain__modules__M21_nist-csf-2-0-planned]] — herkomst csf-mappings

— Einde M09.
