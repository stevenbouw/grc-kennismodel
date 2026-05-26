---
type: sprint
id: v4.2.0
title: v4.2.0 — M18 Asset-module + asset: namespace
status: superseded
date: 2026-04-13
related:
  - v4_1_0-alpha_werkpakket-opschoning
  - v4_2_2_soa-canonisering-route-a
  - D03_10-namespaces
sources:
  - opleveringsrapportage-m18-v4_2_0
  - opleveringsrapportage-v4_2_1
chat-sources: []
confidence: high
---

# v4.2.0 — M18 Asset-module

## Status

**Rijke reconstructie** uit `opleveringsrapportage-m18-v4_2_0.md` (13 april 2026).

## Scope: M18-integratie (9 stappen)

| Stap | Inhoud |
|---|---|
| 1 | Opname van 6 nieuwe M18-bestanden |
| 2 | M01-patch BVA Te Beschermen Belangen (TBB) geïntegreerd |
| 3 | `grc-core.ttl` — nieuwe `asset:`-namespace + 4 imports + versiebump |
| 4 | Wederzijdse `rdfs:seeAlso` M04/M06 ↔ M18 |
| 5 | Versiebump in M18-bestanden |
| 6 | Reasoner-validatie + ontdekking SHACL-modus-interactie |
| 7 | Gesplitste SHACL-validatie geformaliseerd |
| 8 | SPARQL smoke tests |
| 9 | Opleveringsrapport |

## Nieuwe namespace: `asset:`

`@prefix asset: <https://grc.example.org/asset/> .` toegevoegd aan `grc-core.ttl`. Eerste keer dat de namespace-count van 9 naar 10 gaat — voorloper van de definitieve [[brain__decisions__D03_10-namespaces]]-vaststelling.

## Vijf nieuwe M18-bestanden

| Bestand | Triples | Inhoud |
|---|---:|---|
| `m18-assets.ttl` | 214 | TBox: 5 hoofdklassen + sub-taxonomie + 6 properties + 7 SKOS-mappings |
| `m18-mappings-iso27002.ttl` | 137 | ISO 27002:2022 → asset-type (128 mappings) |
| `m18-mappings-bio2-controls.ttl` | 11 | BIO 2.0 ISO27002-controls (inferentie-strategie, stub) |
| `m18-mappings-bio2-overheidsmaatregelen.ttl` | 309 | BIO 2.0 Overheidsmaatregelen → asset-type (300 mappings) |
| `m18-shapes.ttl` | 77 | 4 SHACL-shapes voor M18 |
| `m18-demo-sparql.rq` | n/a | Demo-SPARQL (niet-RDF, los bewaard) |

## M01-patch: BVA Te Beschermen Belangen (TBB)

`m01-framework.ttl`: 620 → 692 triples (+72 = exact patch-content). 7 TBB-concepten in `fw:BVATeBeschermenBelangen` ConceptScheme met `dcterms:isPartOf fw:BesluitBVAStelsel`.

## Wederzijdse rdfs:seeAlso

**`m06-isms.ttl`** (+111 triples):

- `isms:Procedure rdfs:seeAlso asset:Procedure` (stub-comment tweetalig)
- `isms:InformationAsset rdfs:seeAlso asset:InformationAsset` (stub-comment tweetalig)
- D6-meelift: 9 categorie/SoA-comments + 5 PDCA/scope-labels + 93 SoA-toepasselijkheidsbesluit-comments naar tweetalig

**`m04-roles.ttl`** (+3 triples):

- `roles:Role rdfs:seeAlso asset:HumanAsset`
- D6-meelift: 2 NL-only items tweetalig

## Bevinding A — Reasoner-modus-interactie (basis voor gesplitste SHACL)

Tijdens stap 7 (validatie) ontdekt: gecombineerde SHACL-modus levert false-positives op SECTIE A-shapes wegens D5-sameAs-propagatie. **Gesplitste validatie-aanpak vastgesteld:**

- **SECTIE A** (`inference='none'`) — `ctrl:`/`bio:`-NamingShapes + HandreikingBBNValueShape
- **SECTIE B** (`inference='owlrl'`) — alle M18-shapes

Onder gecombineerde modus: 186 false-positive violations. Onder gesplitste modus: 0 violations in beide secties.

Dit principe wordt later in v4.3.0 uitgebreid voor de D11-sameAs-impact (asset:NamespaceShape verplaatst).

## Bevinding B — 108 SoA-control-titel-labels niet vertaald (D6-uitzondering)

`m06-isms.ttl` bevat 108 SoA-control-titels die niet uit de ontologie zelf vertaalbaar zijn (afhankelijk van NEN-bron). Bewuste deeloplevering: D6-meeliftregel wordt **scope-bounded** toegepast — labels die externe vertaling vereisen blijven NL-only met explicate comment. Precedent voor edit-scope-interpretatie van D6.

## v4.2.1 — directe M18-consolidatie (zelfde dag)

Nog op **13 april 2026** uitgevoerd: **M18 5 bestanden → 1 bestand** (`m18-assets.ttl` consolidatie). Pure bestandsorganisatie, geen contentwijziging.

- Triple-delta data graph: −32 (gediagnostiseerd: 3 verdwenen ontology-declaraties × ~10 metadata-triples)
- Alle zes semantische invariantie-metrics identiek aan v4.2.0
- v4.2.0: 24 data + 1 shapes = 25 .ttl-bestanden
- v4.2.1: 20 data + 1 shapes = 21 .ttl-bestanden (−4)

Zie ook `risk-koppeling-nulmeting-v4.2.1.md` — risk-coupling baseline measurement identificeerde **gaps G1–G9** als input voor v4.3.0.

## Eindstaat v4.2.0 / v4.2.1

| Metric | v4.2.0 | v4.2.1 |
|---|---:|---:|
| owl:Class | 182 | 182 |
| NamedIndividual | 615 | 615 |
| ObjectProperty | 138 | 138 |
| DatatypeProperty | 85 | 85 |
| owl:sameAs | 93 | 93 |
| asset:appliesToAssetType | 428 | 428 |

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-04-13 | active | v4.2.0 oplevering (M18-integratie) |
| 2026-04-13 | active | v4.2.1 oplevering (M18-consolidatie + nulmeting) |
| 2026-04-13 | superseded | Opgevolgd door v4.2.2 SoA-canonisering |

— Einde v4.2.0.
