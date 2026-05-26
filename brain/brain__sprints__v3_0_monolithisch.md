---
type: sprint
id: v3.0
title: v3.0 — monolithisch grc-ontologie-v3.ttl
status: superseded
date: 2026-03-19
related:
  - v2_0_fix-release
  - v4_0_0_modulaire-split
sources:
  - GRC-Kennismodel-Migratierapport-v1
  - GRC-Kennismodel-Migratierapport-v2_0
chat-sources:
  - https://claude.ai/chat/5ca3214f-1949-42ef-be10-10d2e91d648e
confidence: high
---

# v3.0 — monolithisch grc-ontologie-v3.ttl

## Status

**Rijke reconstructie.** Volledig gedocumenteerd in refactor-briefing 19 maart 2026.

## Karakteristiek

v3.0 is de **laatste monolithische versie** vóór de modulaire refactor naar v4.0.0. Eén bestand met de hele ontologie.

| Aspect | Waarde |
|---|---|
| Bestand | `grc-ontologie-v3.ttl` (één file) |
| Omvang | 13.292 regels Turtle, 618 KB |
| owl:Class | 157 |
| owl:NamedIndividual | 572 |
| owl:ObjectProperty | 119 |
| SKOS-mappings | 179 |
| owl:sameAs | 94 |
| Modules | M1–M13 (impliciet binnen monoliet) |
| Namespaces | 9 |
| TBox completeness | ~87% |
| ABox completeness | ~49% |

## Belangrijke v3.0-toepassings-fase (maart–begin april 2026)

In de weken na v3.0-vaststelling vonden enkele inhoudelijke aanpassingen plaats binnen dezelfde versie-stempel:

**26 maart 2026 — ISO 27001/27002/BIO relatieverduidelijking** (masterchat-besluit):

- Nieuwe property `fw:geeftRichtlijnenVoor` toegevoegd
- ISO 27002 → ISO 27001 relatie expliciet: `fw:ISO_IEC_27002_2022 fw:geeftRichtlijnenVoor fw:ISO_IEC_27001_2022`
- `rdfs:comment` op `fw:ISO_IEC_27002_2022` uitgebreid met explicatie: "ISO 27002:2022 bevat dezelfde 93 controls als ISO 27001:2022 Bijlage A, maar voorzien van implementatierichtlijnen"
- 27 HermiT-inconsistenties opgelost via xsd:string-fix (data-properties met taalgetagde waarden) — correctieve patch zonder versie-bump

## Bekende bugs in v3.0 (later opgelost in v4.0.0 stap 2)

- **BUG-01** — duplicate `fw:CBW` en `fw:CyberBeveiligingswet` (twee individuals voor hetzelfde framework)
- **BUG-02 t/m BUG-05** — ontbrekende `rdf:type`-declaraties op vier framework-individuals: `fw:NIS2_Directive`, `fw:ISO_IEC_27001_2022`, `fw:BIO_2_0`, `fw:ISO_IEC_27005_2022`
- **BUG-06** — BBN-properties op `bio:OverheidsMaatregel` verwezen onterecht naar BIO 2.0 als bron (moeten verwijzen naar Handreiking BIO2-opmaat)

## Namespace-host (open historische vraag)

In de 19/3-refactor-briefing staan de namespaces al als `https://grc.example.org/XXX/` (slash-separator) — maar in de v2.0-fixes-context staan ze nog als `https://grc.organisatie.nl/ontology/XXX#`. De host-migratie heeft dus **tussen v2.0 en v3.0** plaatsgevonden, of vlak vóór de v4.0.0-refactor in stap 0.

In het patch-rapport van v4.0.0 staat namespace-migratie expliciet als "Stap 0" — dus migratie was technisch deel van v4.0.0-refactor, terwijl de v3.0-briefing van 19/3 de eindstaat al weergaf. Inconsistentie in historische documentatie; geen modelimpact.

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| ±2026-03-17 | active | v3.0 vaststelling |
| 2026-03-19 | active | Refactor-briefing v3 → v4 opgesteld |
| 2026-03-26 | active | ISO/BIO relatieverduidelijking (binnen v3.0) |
| ±2026-04 | superseded | Opgevolgd door v4.0.0 modulaire split |

— Einde v3.0.
