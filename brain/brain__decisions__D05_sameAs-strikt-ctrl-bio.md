---
type: decision
id: D05
title: owl:sameAs strikt voor ctrl:↔bio: brug
status: active
date: 2026-03-16
related:
  - D04_skos-cross-framework
  - D07_bio2-twee-klassen
  - D11_sameAs-asset-convergentie
  - sameAs-discipline
sources:
  - projectinstructie-v1.6
chat-sources:
  - https://claude.ai/chat/7b0a059c-d625-4942-9dbd-55e99c89e71c
confidence: high
---

# D05 — owl:sameAs strikt voor ctrl:↔bio: brug

## Beslissing

`owl:sameAs` wordt **strikt** gebruikt voor de brug tussen `ctrl:ISO27002_*` en `bio:ISO27002_*`-individuals. Huidige staat v4.3.3: **93 asserties** (initieel 94 in v2.0, gecorrigeerd naar 93 unieke tijdens v4.1.0 Actie D naming-canonisering).

Geen uitbreiding van sameAs naar andere namespaces zonder masterchat-GO. D11 voegt later (13 april 2026) een tweede, scope-bounded sameAs-use toe voor asset-convergentie — zie [[brain__decisions__D11_sameAs-asset-convergentie]].

## Aanleiding

In v0.x/v1.x bestonden ISO 27002:2022-controls onder twee verschillende namespaces (`ctrl:` in M2 en `bio:` in M8). Cross-framework SPARQL-queries leverden geen resultaten omdat de reasoner geen brug zag. In v2.0 (fix-release) zijn 94 sameAs-asserties toegevoegd: 86 directe matches plus 7 handmatige ID-notatie-mappings (bv. `ctrl:_5_10 ↔ bio:_5_1`). In v4.1.0 Actie D zijn de 7 niet-canonieke `bio:`-namen gestandardiseerd naar `_YY`-padding, waardoor de 94e (een ID-mapping) overbodig werd en de set naar 93 unieke ging.

## Implementatie

- Asserties in `grc-bridges.ttl` (gecentraliseerd)
- Patroon: `ctrl:ISO27002_X_YY owl:sameAs bio:ISO27002_X_YY .` (93×)
- OWL RL of sterker reasoning verplicht — pure RDFS-inferentie ziet de brug niet
- 128 BIO-mappings (D5-derived) blijven onzichtbaar zonder OWL RL

## Strikte discipline

Niet uitbreiden naar:
- `risk:` ↔ `ctrl:` of `bio:` (geen identiteit; semantische verschillen)
- Cross-framework framework-individuals (`fw:BIO_2_0` ≠ `fw:ISO_IEC_27002_2022`)
- Control-objectives versus implementations

Voor relaties zonder identiteit: gebruik [[brain__decisions__D04_skos-cross-framework]] (SKOS-properties).

## Afgeleide consequenties

- **SHACL-impact:** `ctrl:ISO27002NamingShape` en `bio:ISO27002NamingShape` moeten in SECTIE A (`inference='none'`) draaien, anders 186 false-positive violations door sameAs-propagatie
- **Disjointness:** `ctrl:Control` en `bio:BIOControl` zijn NIET disjoint (sameAs-vereiste)
- [[brain__decisions__D11_sameAs-asset-convergentie]] volgt hetzelfde strikte patroon, scope-bounded

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| ±2026-03-15 | active | Vaststelling in v2.0 fix-release (94 asserties) |
| 2026-04-10 | active | Naming-canonisering tijdens v4.1.0 Actie D — set naar 93 unieke |

— Einde D05.
