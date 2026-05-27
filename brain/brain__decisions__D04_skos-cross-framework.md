---
type: decision
id: D04
title: SKOS voor cross-framework mappings
status: active
date: 2026-03-01
last_revised: 2026-05-27
related:
  - D05_sameAs-strikt-ctrl-bio
  - D09_framework-neutraliteit
  - D11_sameAs-asset-convergentie
  - mapping-bron-disclaimer-effect
  - skos-beoordelings-protocol
  - H36_skos-exactmatch-ctrl-compl-audit
  - T1_skos-kwaliteitsanalyse-fase-1
sources:
  - projectinstructie-v1.6
  - projectinstructie-v1_9
chat-sources:
  - https://claude.ai/chat/76420a5b-11ac-4f22-af7a-5e2404201bdd
confidence: high
gaps:
  - "Exacte datum initiële vaststelling onbekend; datum 2026-03-01 is conservatieve schatting"
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

## D4.1 — Disclaimer-handling bij autoritatieve mapping-bronnen

*Vastgesteld 27 mei 2026, post-T1.*

Wanneer een autoritatieve mapping-bron tussen frameworks (bv. ENISA TIG, NIST OLIR, ISO Annex F) een expliciete **non-equivalence-disclaimer** bevat — waarin staat dat de mapping niet als equivalence of gelijkstelling geïnterpreteerd mag worden — geldt:

**a)** `skos:exactMatch` is **niet verdedigbaar** voor mappings binnen deze bron, ongeacht of C1 (definitionele overlap), C2 (cardinaliteit), en C3 (inclusie-richting) sluitend voldoen. De disclaimer ondergraaft de equivalence-claim die `skos:exactMatch` semantisch impliceert.

**b)** Voor diezelfde bron blijven `skos:closeMatch`, `skos:relatedMatch`, `skos:broadMatch` en `skos:narrowMatch` **valide opties**, mits ze passen bij de inhoudelijke relatie tussen subject en object. De disclaimer ondersteunt deze keuzes juist — geen van deze predicates claimt equivalence.

**c)** D4.1 geldt vanaf vaststelling. **Geen retroactieve audit** van bestaande mappings. Bij T2/T3 of bij gerichte sub-sprint kan een audit van resterende `skos:exactMatch`-mappings (post-T1: 18 in totaal in de ontologie) volgen indien aanleiding.

### Concrete bron-voorbeelden

| Bron | Disclaimer-locatie | Status |
|---|---|---|
| ENISA TIG v1.0 (juni 2025) | Regel 285 | **Bevestigd** — T1-sprint H36-cluster |
| NIST OLIR | Niet geverifieerd | Kandidaat — verifiëren bij T2 of latere sprint |
| ISO Annex F (27001:2022) | Niet geverifieerd | Kandidaat — verifiëren bij eerstvolgende ISO-mapping-sprint |

### Aanleiding D4.1

T1-sprint (26 mei 2026) — H36-cluster (28 ctrl:↔compl: SKOS-exactMatch-paren). ENISA TIG v1.0 bleek autoritatieve evidence-niveau-1-bron voor de 28 paren, maar regel 285 ondergroef de equivalence-claim categorisch. Resultaat: alle 28 paren herclassificatie naar `skos:broadMatch`. T1-eindrapport §6 + §8 leerpunt 2 leverde de aanbeveling tot D4-aanvulling.

## Hangt samen met

- [[brain__concepts__mapping-bron-disclaimer-effect]] — concept-beschrijving van het generaliseerbare patroon
- [[brain__concepts__skos-beoordelings-protocol]] — operationele methode voor SKOS-predicate-keuze (C1-C4)
- [[brain__architecture__H36_skos-exactmatch-ctrl-compl-audit]] — afgehandelde aanleiding (T1)
- [[brain__sprints__T1_skos-kwaliteitsanalyse-fase-1]] — bron-sprint
- [[brain__decisions__D05_sameAs-strikt-ctrl-bio]] — complementaire keuze: `owl:sameAs` voor strikte identiteit (ctrl:↔bio:)
- [[brain__decisions__D11_sameAs-asset-convergentie]] — idem voor asset-laag

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| ±2026-03 | active | Vaststelling (datum reconstructie) |
| 2026-05-27 | active | D4.1 toegevoegd: disclaimer-handling bij autoritatieve mapping-bronnen. Aanleiding T1-sprint (ENISA TIG regel 285). Reikwijdte: blokkeert `skos:exactMatch` alleen; close/related/broad/narrow blijven valide. Geen retroactieve audit (Optie A) — geldt vanaf vaststelling. |

— Einde D04.
