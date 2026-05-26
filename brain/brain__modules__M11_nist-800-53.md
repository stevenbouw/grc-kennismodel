---
type: module
id: M11
title: M11 — NIST SP 800-53 R5 (ctrl:)
status: active
date: 2026-05-19
related:
  - H33_m11-sp800-53-substantiele-uitbreiding
  - H34_m11-enhancement-modellering
  - v4_5_0_fase-3-nist-csf-2-0
sources:
  - NIST_SP_800-53r5
  - sp800-53r5-to-iso-27001-mapping
chat-sources: []
confidence: high
---

# M11 — NIST SP 800-53 R5

## Bestand
`m11-nist-800-53.ttl`

## Namespace
`ctrl: <https://grc.example.org/control/>` (gedeeld met M02)

## Wat het bevat

NIST Special Publication 800-53 Revision 5 — security and privacy controls. **Modelbeperking**: 124 controls uit ~1000 totaal.

| Inhoud | Aantal v4.5.0 |
|---|---:|
| `ctrl:NIST_*`-individuals | 124 |
| **csf-mappings landing (v4.5.0)** | csf-subjects: 98 |
| SKOS-mappings naar ISO 27001 / BIO | (via sheet 8 + CSF Reference Tool) |

## v4.5.0-uitbreiding — csf-mappings landing + 2 nieuwe H-items

In v4.5.0 Stap 6 zijn `skos:closeMatch`-triples vanuit `csf:Subcategory`-individuals geland op `ctrl:NIST_*`. Bron: CSF Reference Tool (NIST, na OLIR-formaat-fallback).

### Twee nieuwe geparkeerde modelbeperkingen

| H-item | Aard | Trigger-criterium |
|---|---|---|
| [[brain__architecture__H33_m11-sp800-53-substantiele-uitbreiding]] | Breedte — 108 unique unresolved SP 800-53-targets in Stap 6 | Spoor B-organisatie heeft >50 niet-gemapte controls nodig |
| [[brain__architecture__H34_m11-enhancement-modellering]] | Diepte — 17 unique enhancements ontbreken (bv. AC-2(1), CM-07(02)) | Serieus SP 800-53-gebruik met enhancement-audit-behoefte |

**G1 "bij twijfel niet leggen"** correct toegepast — geen sneeuwbal-mappings naar inferred targets. Documentatie in patch-rapport-v4_5_0 §8 punten 17-18.

### NIST Reference Tool-conventie

75× letterlijke `"ISO/IEC 27001:2022: Mandatory Clause: None"`-lines waar geen mapping bestaat. G1-correct niet gelegd.

## Cross-references

- [[brain__sources__nist-800-53-39-30]] — bron-detail
- [[brain__architecture__H33_m11-sp800-53-substantiele-uitbreiding]] — modelbeperking-breedte
- [[brain__architecture__H34_m11-enhancement-modellering]] — modelbeperking-diepte
- [[brain__sprints__v4_5_0_fase-3-nist-csf-2-0]] — csf-mappings landing + H33/H34-registratie
- [[brain__modules__M21_nist-csf-2-0-planned]] — herkomst csf-mappings

— Einde M11.
