---
type: decision
id: D04
title: SKOS voor cross-framework mappings
status: active
date: 2026-03-01
related:
  - D05_sameAs-strikt-ctrl-bio
  - D09_framework-neutraliteit
sources:
  - projectinstructie-v1.6
chat-sources:
  - https://claude.ai/chat/76420a5b-11ac-4f22-af7a-5e2404201bdd
confidence: medium
gaps:
  - "Exacte datum vaststelling onbekend; datum 2026-03-01 is conservatieve schatting"
---

# D04 — SKOS voor cross-framework mappings

## Beslissing

Cross-framework mappings worden gemodelleerd via **SKOS-properties** (`skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`, `skos:narrowMatch`, `skos:relatedMatch`).

Niet via owl:equivalentClass (te strikt), niet via custom properties (geen herbruikbare semantiek).

## Aanleiding

Cross-framework relaties zijn zelden 1:1 — een NIS2-eis dekt vaak meerdere ISO 27002-controls af, een NIST 800-53-control overlapt deels met BIO-overheidsmaatregelen. SKOS biedt vijf gradaties die deze nuance correct uitdrukken:

- `exactMatch` — semantisch identiek
- `closeMatch` — sterk overeenkomstig, niet identiek
- `broadMatch` / `narrowMatch` — hiërarchische relatie
- `relatedMatch` — thematisch verwant

## Implementatie

- Huidige staat v4.3.3: **346 SKOS-mappings** tussen frameworks
- Validatieniveau per mapping wordt onderscheiden in praktijk (officiële crosswalk / analytisch afgeleid / expert-gevalideerd) — geen formele OWL-property, wel als comment-conventie
- Geen tekst-reproductie uit NEN-licentie-bronnen; mappings zijn metadata, niet content

## Verschil met D5 (owl:sameAs)

D4 (SKOS) en D5 (owl:sameAs) lossen verschillende problemen op:

- **D5 owl:sameAs** = harde identiteit op individual-niveau (`ctrl:ISO27002_5_01` = `bio:ISO27002_5_01`) — propagatie van alle properties via OWL RL
- **D4 SKOS** = zachte semantische relatie tussen verschillende concepten, geen propagatie

Zie [[brain__decisions__D05_sameAs-strikt-ctrl-bio]] voor de strikte sameAs-discipline.

## Afgeleide consequenties

- SKOS-kwaliteitsanalyse op huidige 346 mappings is parallelle workstream
- Bij Fase 2 (CBW), Fase 3 (NIST CSF 2.0) en Fase 4 (M15-ENSIA) komen er substantieel meer SKOS-mappings bij — kwaliteitsstandaarden vóór adoptie

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| ±2026-03 | active | Vaststelling (datum reconstructie) |

— Einde D04.
