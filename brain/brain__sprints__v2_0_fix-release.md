---
type: sprint
id: v2.0
title: v2.0 — fix-release
status: superseded
date: 2026-03-15
related:
  - v0-v1_initiele-fase
  - v3_0_monolithisch
  - D05_sameAs-strikt-ctrl-bio
sources: []
chat-sources:
  - https://claude.ai/chat/7b0a059c-d625-4942-9dbd-55e99c89e71c
confidence: medium
gaps:
  - "Exacte datum vaststelling onbekend; pre-16 maart 2026 (taxonomie-chat refereert er al naar)"
  - "Mogelijk meer fixes dan de drie gedocumenteerde"
---

# v2.0 — fix-release

## Status

**Medium reconstructie.** Drie categorieën fixes ten opzichte van v0.1/v1.x gedocumenteerd in taxonomie-chat 16 maart 2026.

## Scope

Drie fixes ten opzichte van v0.1/v1.x.

### Fix 1 — owl:sameAs namespace-brug (M2 ↔ M8)

**Probleem:** ISO 27002:2022-controls bestonden onder twee verschillende namespaces (`ctrl:` in M2 en `bio:` in M8). Cross-framework SPARQL-queries Q10–Q12 leverden geen resultaten omdat de reasoner geen brug zag.

**Oplossing:** **94 owl:sameAs-axioma's** toegevoegd:

- 86 directe matches (`ctrl:ISO27002_X_YY owl:sameAs bio:ISO27002_X_YY`)
- 7 handmatige ID-notatie-mappings (bv. `ctrl:_5_10 ↔ bio:_5_1`)

Patroon: `ctrl:ISO27002_5_01 owl:sameAs bio:ISO27002_5_01 .` (×93 + 1 dubbel via 7 ID-mappings = 94 totaal in v2.0; later in v4.1.0 Actie D gestandardiseerd naar 93 unieke met canonieke `_YY`-padding).

Dit is de oorsprong van [[brain__decisions__D05_sameAs-strikt-ctrl-bio]].

### Fix 2A — Ontologie-header

Volledige `owl:Ontology`-declaratie toegevoegd:

- Ontologie-URI `<https://grc.organisatie.nl/ontology/>`
- `dcterms`-metadata (created, modified, source)
- `owl:versionIRI`
- PROV-O provenance (`prov:wasAttributedTo`, `prov:generatedAtTime`)
- `owl:versionInfo "2.0.0"`

### Fix 2B — BVC-rol

`roles:BVC` (Beveiligingscoördinator) als expliciete OWL-klasse én named individual gemodelleerd:

- `roles:BVC rdfs:subClassOf roles:SpecialistRole`
- Grondslag: Besluit BVA-stelsel Rijksdienst 2021

## Namespace-conventie in v2.0

Nog steeds `#`-separator en `grc.organisatie.nl`-host: `https://grc.organisatie.nl/ontology/framework#`. De migratie naar slash-separator + `grc.example.org`-host komt later in v3.0 / v4.0 stap 0.

## Wat onbekend is

- Datum vaststelling (vermoedelijk begin maart 2026)
- Mogelijke Fix 3 / Fix 4 die niet in de teruggevonden documenten staat
- Was er een v2.1 of v2.5 tussen v2.0 en v3.0?

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| ±2026-03-15 | active | Vaststelling fix-release |
| ±2026-03-19 | superseded | Opgevolgd door v3.0 monolithisch |

— Einde v2.0.
