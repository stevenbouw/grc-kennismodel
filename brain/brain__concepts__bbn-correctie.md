---
type: concept
title: BBN-correctie (Handreiking versus BIO 2.0)
status: living
date: 2026-05-13
related:
  - D07_bio2-twee-klassen
  - v4_1_0-alpha_werkpakket-opschoning
sources:
  - opleveringsrapportage-v4_1_0-alpha
chat-sources: []
confidence: high
---

# BBN-correctie (Handreiking BIO2-opmaat versus BIO 2.0)

## Wat het is

**BBN (BasisBeveiligingsNiveau)** is een classificatie-systeem (waarden 1 of 2) dat sommige BIO-controls en overheidsmaatregelen toewijst aan een minimum-niveau van beveiliging. BBN-niveaus zijn **geen eigenschap van BIO 2.0** — ze komen uit een **transitie-document**: de **Handreiking BIO2-opmaat**.

In het GRC Kennismodel:

- BBN-waarden worden gemodelleerd via `ext:hasHandreikingBBN` (DatatypeProperty, range `xsd:integer`)
- Toegestane waarden: **1 of 2** (geen 3 — alleen Handreiking gebruikt 1 en 2)
- Domein: `ctrl:Control` (geldt zowel voor `bio:BIOControl` als `bio:OverheidsMaatregel`)

**Huidige staat v4.3.3:** 241 assertions (154× BBN1 + 87× BBN2) op 148 OverheidsMaatregelen + 93 BIOControls.

## Waarom de correctie nodig was

In v0.x / v1.x / v2.0 stonden BBN-properties **rechtstreeks op BIO 2.0-individuals**, met name `bio:hasBBN` als string-property en reïficatie-klassen `bio:BBN1`, `bio:BBN2`, `bio:BBNNiveau`. Dat suggereerde dat BBN een BIO 2.0-eigenschap was.

**Dit is inhoudelijk onjuist.** BIO 2.0 zelf gebruikt geen BBN-classificatie — BIO 2.0 classificeert via **ISO 27002-attributen** (control_type, information_security_properties, cybersecurity_concepts, operational_capabilities, security_domains). BBN-niveaus zijn een aanvullende, *transitionele* classificatie uit de Handreiking BIO2-opmaat (de migratie-handleiding van BIO 1.04 → BIO 2.0).

Op **17 maart 2026** is dit gecorrigeerd in masterchat: BBN is een Handreiking-eigenschap, niet een BIO 2.0-eigenschap. Implementatie volgde in v4.1.0-alpha Actie A (10 april 2026).

## Hoe de implementatie eruitziet

Vóór v4.1.0-alpha:

```turtle
bio:OverheidsMaatregel_X bio:hasBBN "1"^^xsd:string ;
                        rdf:type bio:BBN1 .
```

Vanaf v4.1.0-alpha:

```turtle
bio:OverheidsMaatregel_X ext:hasHandreikingBBN 1 .
```

`ext:hasHandreikingBBN` is een DatatypeProperty in `grc-core.ttl` met:

- `rdfs:domain ctrl:Control` (dekt BIOControls én OverheidsMaatregelen)
- `rdfs:range xsd:integer`
- `dcterms:source "Handreiking BIO2-opmaat v2.5"`
- Tweetalige `rdfs:comment` met scope-toelichting

SHACL-bewaking: `ctrl:HandreikingBBNValueShape` (`sh:minInclusive 1, sh:maxInclusive 2`) voorkomt dat toekomstige edits per ongeluk BBN3 of 0 toevoegen.

## Architectuur-relevantie

De BBN-correctie illustreert een patroon dat herhaaldelijk terugkomt:

- **Bron-discipline:** elke property moet traceerbaar zijn naar zijn echte bron (zie [[brain__concepts__provenance-en-attribuering]])
- **Geen verbloeming van juridische status:** een document is geen ander document, ook al lijken hun controls op elkaar (vergelijk [[brain__decisions__D07_bio2-twee-klassen]])
- **Externe consumers checken naming:** dashboards of SPARQL-queries die op `bio:hasBBN` bouwden, moeten naar `ext:hasHandreikingBBN` worden gemigreerd

## Hangt samen met

- [[brain__sprints__v4_1_0-alpha_werkpakket-opschoning]] — Actie A waarin de correctie is uitgevoerd
- [[brain__decisions__D07_bio2-twee-klassen]] — gerelateerd concept: BIO 2.0 is geen ISO 27002

— Einde BBN-correctie.
