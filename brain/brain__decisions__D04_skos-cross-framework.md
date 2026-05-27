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
  - cluster-discipline-bewijslast
  - H36_skos-exactmatch-ctrl-compl-audit
  - H41_skos-axioma-set-handling
  - T1_skos-kwaliteitsanalyse-fase-1
  - T2-skos-bidirectional-audit-m10
sources:
  - projectinstructie-v1.6
  - projectinstructie-v1_9
  - projectinstructie-v1_10
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

### Toepassings-precedent — uitbreiding naar cluster-niveau (T2, 27 mei 2026)

T2-sprint heeft D4.1-toepassing op **cluster-niveau** geoperationaliseerd voor 118 m10-paren over 10 NIS2-art.21-letter-clusters. Toepassings-regel (per patch-rapport v4.6.2 §1 + Stap 3-rapport §6.6):

> Wanneer alle cluster-leden dezelfde bron-stack delen (homogene clusters), volstaat **één D4.1-bevestiging per cluster** — niet per-paar-werk. Voor heterogene clusters (mix van bronnen) blijft per-paar-toets vereist.

T2-empirisch bewijs:
- Alle 10 m10-clusters deelden één D4.1-context: ENISA TIG R285 + CBW-Mapping-UV R3-erf (T1-bekend, pre-sprint-inventarisatie §5)
- Per-paar-D4.1-check op cluster-niveau = één bevestiging per cluster, niet 11,8 keer per cluster (efficiëntiewinst t.o.v. naïeve per-paar-aanpak)
- Cluster-doel-predicate `broadMatch` per cluster bevestigd; alle 65 mutaties (32 downgrade + 33 upgrade) volgen bidirectional uit cluster-discipline (Protocol v1.2 §3.1 rij 6)
- 0 NEN-aantoonbare uitzonderingen op 10 heuristiek-flags (zie [[brain__concepts__cluster-discipline-bewijslast]])

**Reikwijdte-vermelding:** cluster-niveau-toepassing geldt alleen bij homogene clusters (bron-stack-identiek over alle cluster-leden). Bij heterogene clusters (toekomstig m14-sprint, cross-bron-overlap-sprint) blijft per-paar-D4.1-toets de werkbasis.

Zie [[brain__sprints__T2-skos-bidirectional-audit-m10]] voor sprint-context.

## Hangt samen met

- [[brain__concepts__mapping-bron-disclaimer-effect]] — concept-beschrijving van het generaliseerbare patroon
- [[brain__concepts__skos-beoordelings-protocol]] — operationele methode voor SKOS-predicate-keuze (C1-C4 + bidirectional-symmetrie)
- [[brain__concepts__cluster-discipline-bewijslast]] — bewijslast-asymmetrie bij cluster-uitzonderingen
- [[brain__architecture__H36_skos-exactmatch-ctrl-compl-audit]] — afgehandelde aanleiding (T1) + m10-component closed via T2
- [[brain__architecture__H41_skos-axioma-set-handling]] — gerelateerd architectuur-item (geparkeerd post-T2)
- [[brain__sprints__T1_skos-kwaliteitsanalyse-fase-1]] — bron-sprint D4.1-vaststelling
- [[brain__sprints__T2-skos-bidirectional-audit-m10]] — bron-sprint cluster-niveau-toepassings-precedent
- [[brain__decisions__D05_sameAs-strikt-ctrl-bio]] — complementaire keuze: `owl:sameAs` voor strikte identiteit (ctrl:↔bio:)
- [[brain__decisions__D11_sameAs-asset-convergentie]] — idem voor asset-laag

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| ±2026-03 | active | Vaststelling (datum reconstructie) |
| 2026-05-27 | active | D4.1 toegevoegd: disclaimer-handling bij autoritatieve mapping-bronnen. Aanleiding T1-sprint (ENISA TIG regel 285). Reikwijdte: blokkeert `skos:exactMatch` alleen; close/related/broad/narrow blijven valide. Geen retroactieve audit (Optie A) — geldt vanaf vaststelling. |
| 2026-05-27 | active | D4.1-toepassings-precedent uitgebreid naar cluster-niveau na T2-sprint (118 paren over 10 m10-clusters). Bij homogene cluster-bron-stack volstaat één D4.1-bevestiging per cluster; heterogene clusters vereisen per-paar-toets. D4-tekst zelf onveranderd; alleen precedent-uitbreiding gedocumenteerd. |

— Einde D04.
