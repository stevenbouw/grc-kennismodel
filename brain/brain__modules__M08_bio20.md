---
type: module
id: M08
title: M08 — BIO 2.0 (bio:)
status: active
date: 2026-05-19
related:
  - D05_sameAs-strikt-ctrl-bio
  - D07_bio2-twee-klassen
  - bbn-correctie
  - v4_4_0_fase-2-cbw-cbb
  - v4_5_0_fase-3-nist-csf-2-0
sources:
  - 20250924baselineinformatiebeveiligingoverheid2bio2v12deff
  - 20260302waswordtlijstbio_bio2v13inexcel_hrbio2opmaat_bio1v104zvv20def
  - Cbw_NIS2_Control_Framework
chat-sources: []
confidence: high
---

# M08 — BIO 2.0

## Bestand
`m08-bio20.ttl`

## Namespace
`bio: <https://grc.example.org/bio/>`

## Wat het bevat

Volledige BIO 2.0 — operationeel kader van de Rijksoverheid. Twee klassen conform [[brain__decisions__D07_bio2-twee-klassen]].

| Inhoud | Aantal v4.5.0 |
|---|---:|
| `bio:BIOControl`-individuals (= 93 ISO 27002-controls) | 93 |
| `bio:OverheidsMaatregel`-individuals (Rijks-specifiek) | 148 |
| `ext:hasHandreikingBBN`-assertions | 241 (154× BBN1 + 87× BBN2) |
| Sheet 9 mappings (CBW-Excel, v4.4.0) | 183 unieke RDF-triples op 81 BIO-Controls |
| **csf-mappings landing (v4.5.0)** | **494 mappings vanuit csf: → bio:ISO27002_*** |

## v4.5.0-uitbreiding — csf-mappings landing

In v4.5.0 Stap 5 zijn 494 `skos:closeMatch`-triples vanuit `csf:Subcategory`-individuals geland op `bio:ISO27002_*` (Annex A controls). Bron: Sheet 8 van CBW-Excel (CC-BY 4.0).

**Route:** via D5 sameAs-brug `ctrl:↔bio:`. Mappings worden uitgevoerd op bio:-zijde omdat dat de Annex A-specifieke representatie is. csf-namespace subjects in M08: **121** (in canonical_metrics).

**v4.4.0-update (in herinnering):** Sheet 9 mappings van CBW-Excel geland (290 sheet-relaties → 183 unieke triples, 37% dedup). Zie [[brain__sources__cbw-excel]].

## Naamgevingsconventie

Canoniek `ISO27002_X_YY` met YY zero-padded.

## Bronlicentie

| Bron | Licentie | Toepassing |
|---|---|---|
| BIO 2.0 v1.2 (24 sept 2025) | Onbeperkt (overheidspublicatie) | Klassen + individuals |
| Handreiking BIO2-opmaat | Onbeperkt | BBN-asserties |
| CBW NIS2 Control Framework v1.0 | CC-BY 4.0 | Sheet 9 + Sheet 8 mappings *(v4.4.0 + v4.5.0)* |

## Cross-references

- [[brain__sources__cbw-excel]] — Sheet 9 (v4.4.0) + Sheet 8 (v4.5.0) bron
- [[brain__sources__bio2-en-handreiking]] — BIO 2.0 + Handreiking bron-detail
- [[brain__sprints__v4_5_0_fase-3-nist-csf-2-0]] — csf-mappings landing
- [[brain__modules__M21_nist-csf-2-0-planned]] — herkomst csf-mappings

— Einde M08.
