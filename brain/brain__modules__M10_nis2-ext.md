---
type: module
id: M10
title: M10 — NIS2 extensie + CBW-controls (compl: + ext: + ctrl:)
status: active
date: 2026-05-13
related:
  - D12_drie-laags-compliance
  - drie-laags-compliance
  - H25_compl-articleRef-domain-spanning
  - H26_OBL-laag-gap-NIS2
  - H32_obl-laag-asymmetrie
  - v4_3_3_d12-en-predicate-consolidatie
  - v4_4_0_fase-2-cbw-cbb
sources:
  - CELEX3A32022L25553ANL3ATXT
  - OJ3AL_2024026903AEN3ATXT
  - Cbw_NIS2_Control_Framework
chat-sources: []
confidence: high
---

# M10 — NIS2 extensie + CBW-controls

## Bestand
`m10-nis2-ext.ttl`

## Namespaces
Hergebruikt `compl:` voor NIS2-eisen + `ext:NIS2Requirement`-subklasse + **`ctrl:` voor CBW-controls** *(v4.4.0)* + **`ext:SourceAttribution`** *(v4.4.0)*.

## Wat het bevat

NIS2 (EU 2022/2555) als toetskader — Nederlandse implementatie via CBW (in voorbereiding) en Cbb (concept t.b.v. TK). **Uitgebreid in v4.4.0 met 26 CBW-controls** (control-tak, niet compliance-tak).

| Inhoud | Aantal v4.4.0 |
|---|---:|
| `compl:RegulatoryObligation`-individuals (NIS2_Art21_a..j) | 10 |
| Plain `ext:NIS2Requirement`-subjects | 6 (NIS2_Art{18,19,20,22,23,24}) |
| `compl:articleRef "art. N"`-asserties | 6 |
| Cross-frame SKOS-mappings | 118 (naar ISO 27001, BIO 2.0, COBIT) |
| `compl:requirementText@en` | 6 |
| **`ctrl:CBWControl`-klasse** *(v4.4.0, nieuw — eerste TBox-element in m10!)* | Subklasse van `ctrl:Control` |
| **26 CBW-Control-individuals** *(v4.4.0, nieuw)* | Type: `ctrl:CBWControl` |
| **1 `ext:SourceAttribution`** *(v4.4.0, nieuw)* | `ext:Attr_CBW_NIS2_Framework_2025_CC_BY_4_0` |

## v4.4.0-uitbreiding — CBW-controls

### Belangrijke architectuur-keuze: control-tak, niet compliance-tak

Correctie op v1.6-aanname: CBW-controls horen in de **control-tak** (`ctrl:CBWControl ⊑ ctrl:Control`), niet in de compliance-tak. Rationale: het zijn beheersmaatregelen (technische/organisatorische maatregelen), niet wettelijke verplichtingen.

```turtle
ctrl:CBWControl rdfs:subClassOf ctrl:Control .

ctrl:CBW_Control_01 rdf:type ctrl:CBWControl ;
                    rdfs:label "..."@nl ;
                    ext:hasControlStatement "..."@nl ;
                    ext:hasUVInterpretation "..."@nl ;
                    ext:sourceAttribution ext:Attr_CBW_NIS2_Framework_2025_CC_BY_4_0 .
```

### Eerste TBox-element in M10

Tot v4.3.3 bevatte M10 alleen ABox-content (individuals + asserties). Met `ctrl:CBWControl` introduceert v4.4.0 het **eerste TBox-element in M10** — een TBox-klasse-declaratie. Dit is een nieuwe categorie wijziging voor deze module.

### Properties op CBW-controls

| Property | Type | Doel |
|---|---|---|
| `ext:hasControlStatement` | DatatypeProperty | Het beheersmaatregel-statement uit CBW-Excel sheet 3 |
| `ext:hasUVInterpretation` | DatatypeProperty | ADR/NOREA's UV-decompositie (Uitvoeringsverordening 2024/2690-interpretatie) per CBW-control |
| `ext:sourceAttribution` | ObjectProperty | Verwijzing naar `ext:SourceAttribution`-individual voor CC-BY 4.0-attribuering |

### Route 5 herdefiniëring

`ext:hasUVInterpretation` vervangt het oorspronkelijk geplande `ext:hasENISAGuidance`. Zie [[brain__sources__cbw-excel]] voor de fundamentele Route 5-correctie: CBW-Excel bevat geen ENISA-tekst maar ADR/NOREA's eigen UV-decompositie.

## D12-toepassing — onveranderd

NIS2 is **eerste framework** waarop de drie-laags-architectuur is toegepast. Zie [[brain__concepts__drie-laags-compliance]]. CBW-controls (v4.4.0-uitbreiding) zijn **niet** D12-individuals — ze zitten in de control-tak.

```turtle
compl:NIS2_Art21_a rdf:type compl:RegulatoryObligation .  # Laag 1
compl:OBL_NIS2_Art21 rdf:type compl:LegalObligation ;     # Laag 2 (in M05)
                     compl:articleRef "art. 21" .
compl:REQ_NIS2_Art21_a rdf:type ext:NIS2Requirement ;     # Laag 3 (in M05)
                       compl:articleRef "art. 21" .
ctrl:CBW_Control_01 rdf:type ctrl:CBWControl .            # control-tak (v4.4.0)
```

## Cross-references

- [[brain__decisions__D12_drie-laags-compliance]] — patroon-interpretatie (NIS2 volledig drie-laags, CBW/Cbb in M05 legal-only)
- [[brain__architecture__H26_OBL-laag-gap-NIS2]] — art. 18, 19, 22, 24 hebben geen OBL-laag (bewuste keuze of gap?)
- [[brain__sprints__v4_3_3_d12-en-predicate-consolidatie]] — predicate-consolidatie α uitgevoerd hier (Item 3a/3b)
- [[brain__sprints__v4_4_0_fase-2-cbw-cbb]] — sprint waar 26 CBW-controls + `ctrl:CBWControl`-klasse + `ext:SourceAttribution` zijn toegevoegd
- [[brain__sources__cbw-excel]] — bron + Route 5-herdefinitie

## Bronlicentie

- NIS2 = publiek EU-recht — vrij herbruikbaar
- CBW-controls + UV-interpretaties uit CBW-Excel = **CC-BY 4.0** (ADR & NOREA) — attributie via `ext:sourceAttribution`

— Einde M10.
