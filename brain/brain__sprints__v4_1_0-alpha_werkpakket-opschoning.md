---
type: sprint
id: v4.1.0-alpha
title: v4.1.0-alpha — werkpakket opschoning
status: superseded
date: 2026-04-10
related:
  - v4_0_0_modulaire-split
  - v4_2_0_M18-asset-module
  - D06_tweetalige-annotaties-meeliftregel
  - BBN-correctie
sources:
  - opleveringsrapportage-v4_1_0-alpha
chat-sources: []
confidence: high
---

# v4.1.0-alpha — werkpakket opschoning

## Status

**Rijke reconstructie** uit `opleveringsrapportage-v4_1_0-alpha.md` (10 april 2026).

## Scope: acht acties

| Actie | Inhoud |
|---|---|
| **A** | BBN-properties consolideren naar `ext:hasHandreikingBBN` + typo-fix |
| **D** | ctrl:↔bio: naming-inconsistentie fixen (29 renames) |
| **C** | CBW-alias opruimen |
| **H2** | (toelichting onbekend) |
| **B** | (toelichting onbekend) |
| **F** | (toelichting onbekend) |
| **G** | D6 meeliftregel formeel vastleggen |
| **E** | Laag 5 scope-noot — 331 SKOS-mappings als kwaliteitsanalyse-startpunt, NIST-bulk expliciet Laag 5+ |

## Actie A — BBN-consolidatie (substantiele scope-uitbreiding)

Oorspronkelijke instructie was simpele typo-fix (`bio:BIO2OvheidsMaatregel` → `bio:OverheidsMaatregel`). Werkelijkheid bleek groter:

- Volledige parallelle set van **148 individuals** met type `ctrl:BIO2OvheidsMaatregel` (de typo-klasse) bestond in `ctrl:`-namespace naast canonieke `bio:`-set
- 0 inkomende verwijzingen — pure regressie-bagage
- Masterchat-keuze **Optie 1:** volledig verwijderen

**Resultaat:**

- Nieuwe property `ext:hasHandreikingBBN` (DatatypeProperty, domain `ctrl:Control`, range `xsd:integer`)
- `m02-control.ttl`: 149.362 → 94.703 bytes (−36%)
- 241 inline `bio:hasBBN "X"` (xsd:string) → `ext:hasHandreikingBBN X` (xsd:integer)
- Verwijderde reïficatie-klassen: `ctrl:BBN1`, `ctrl:BBN2`, `bio:BBNNiveau`, etc.
- Eindcount: **241 `ext:hasHandreikingBBN`** (154× BBN1 + 87× BBN2)

Zie [[brain__concepts__BBN-correctie]] voor de inhoudelijke achtergrond.

## Actie D — ctrl:↔bio: naming-canonisering

Canonieke vorm vastgesteld: `ISO27002_X_YY` met YY zero-padded naar 2 cijfers. 93/93 `ctrl:`-zijde was al canoniek; 86/93 `bio:`-zijde was canoniek, **7 afwijkers gefixt**.

| Oud | Nieuw |
|---|---|
| `bio:ISO27002_5_1` | `bio:ISO27002_5_10` |
| `bio:ISO27002_5_2` | `bio:ISO27002_5_20` |
| `bio:ISO27002_5_3` | `bio:ISO27002_5_30` |
| `bio:ISO27002_7_1` | `bio:ISO27002_7_10` |
| `bio:ISO27002_8_1` | `bio:ISO27002_8_10` |
| `bio:ISO27002_8_2` | `bio:ISO27002_8_20` |
| `bio:ISO27002_8_3` | `bio:ISO27002_8_30` |

**29 text-renames totaal** (22 in m08 + 7 in grc-bridges). 94 owl:sameAs-bridges intact, 0 broken.

**SHACL-pattern-constraint:** nieuw bestand `grc-shacl.ttl` aangemaakt met **3 NodeShapes**:

1. `ctrl:ISO27002NamingShape` — pattern `^https://grc\.example\.org/control/ISO27002_[5-8]_[0-9]{2}$`
2. `bio:ISO27002NamingShape` — pattern voor bio:
3. `ctrl:HandreikingBBNValueShape` — `sh:minInclusive 1, sh:maxInclusive 2`

**Eerste pySHACL-validatie: Conforms=True, 0 violations** ✓

## Actie C — CBW-alias opruimen

`fw:CyberBeveiligingswet owl:sameAs fw:CBW` verwijderd (redirect uit v4.0.0 BUG-01-fix). Toegevoegd: `skos:altLabel "Cyberbeveiligingswet"@nl` op `fw:CBW`. Bestaande `fw:status "in voorbereiding"@nl` behouden.

## Actie G — D6 meeliftregel

Formeel vastgelegd: bij elke wijziging in een moduulbestand worden alle Nederlandse-only `rdfs:comment` en `rdfs:label` in datzelfde bestand in dezelfde commit tweetalig gemaakt. **Edit-scope, niet bestand-scope** (deze nuance is fundamenteel — zie [[brain__decisions__D06_tweetalige-annotaties-meeliftregel]]).

## Validatie

- Parse-validatie (rdflib): 20 bestanden, alle groen
- pySHACL: 3 NodeShapes conform, 0 violations
- HermiT in Protégé: aanbevolen voor volgende sessie (niet uitgevoerd in deze sprint)

## Wat onbekend is

- Inhoud van Acties B, F, H2 (niet teruggevonden in head-100 van opleveringsrapport — vermoedelijk verderop in document)
- Of "alpha"-marker betekent dat er een v4.1.0-release zonder alpha-suffix was gepland (niet teruggevonden — vermoedelijk direct doorgesprongen naar v4.2.0)

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-04-08 | active | Masterchat-instructie (8 april) |
| 2026-04-10 | active | Oplevering werkpakket |
| 2026-04-13 | superseded | Opgevolgd door v4.2.0 M18-integratie |

— Einde v4.1.0-alpha.
