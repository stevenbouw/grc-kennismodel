---
type: decision
id: D04
title: SKOS voor cross-framework mappings
status: active
date: 2026-03-01
last_revised: 2026-05-28
related:
  - D05_sameAs-strikt-ctrl-bio
  - D09_framework-neutraliteit
  - D11_sameAs-asset-convergentie
  - mapping-bron-disclaimer-effect
  - skos-beoordelings-protocol
  - cluster-discipline-bewijslast
  - cross-category-mappings
  - H36_skos-exactmatch-ctrl-compl-audit
  - H41_skos-axioma-set-handling
  - T1_skos-kwaliteitsanalyse-fase-1
  - T2-skos-bidirectional-audit-m10
  - T3-skos-bidirectional-audit-m14
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

### D4.1 inactief in T3-context — m14 AVG/GDPR (28 mei 2026)

T3-sprint heeft D4.1 als **inactief** vastgesteld voor m14 AVG/GDPR-scope. Bindende T3-steer 1 (instructie-vastgesteld door masterchat): geen D4.1-disclaimer-logica op alle 31 m14-paren. Onderbouwing:

- AVG = publiek EU-recht (geen autoritatieve mapping-bron met non-equivalence-disclaimer in evidence-stack)
- ISO 27701:2025 Annex D + Annex F = SKOS-mapping-keten zonder D4.1-relevante disclaimer
- m14 had bij T3-start 0 exactMatch-paren — D4.1 zou semantisch alleen exactMatch-doelvalidatie blokkeren, en die overweging is in T3 niet aan de orde

D4.1-validatie-historie m14-scope toegevoegd als **inactief-precedent**: per-paar-toets niet nodig wanneer D4.1-context structureel ontbreekt (geen autoritatieve mapping-bron met disclaimer in evidence-stack). Zie patch-rapport v4.6.3 §12.

### Cross-category-rationale als toepassings-precedent op m14 (28 mei 2026)

T3-sprint heeft op productie-schaal (31 m14-paren) bewijs geleverd voor een D4-werkings-principe dat T1+T2 niet konden onthullen: **wanneer subject en object van een SKOS-mapping in ontologisch verschillende categorieën zitten (bv. control ↔ legal-obligation), is `relatedMatch` de associatieve basislijn — niet `broad/narrowMatch`.** Operationele werking in T3:

- Cluster-doel-default per Protocol §3.1 rij 7 (narrowMatch in 1↔veel-subject-cluster) wordt op cross-category-niveau systematisch overstemd door C3-falen op conceptuele subsumptie
- broadMatch is in m14 niet houdbaar in compl→ctrl-richting (SKOS-formal-semantics omgekeerd aan modeller-bedoeling én cross-category-categorie-fout); masterchat-besluit Optie C verschoof beide Art5_1f broadMatch-paren naar relatedMatch
- closeMatch-uitzondering op retrieval-interchangeability blijft mogelijk (T3-014 + T3-026; beide confidence middel)

D4-validatie-historiek-uitbreiding: T1 (paar-niveau D4.1-vaststelling) → T2 (cluster-niveau D4.1-precedent) → **T3 (cross-category-rationale-precedent; D4.1 inactief)**. Concept-niveau verankering: [[brain__concepts__cross-category-mappings]] *(nieuw iteratie 15)* — gemarkeerd als kandidaat v1.3.1-precedent; formalisering in Protocol-tekst is masterchat-werk bij volgende sprint-scoping (Brein voert geen autonome D4-tekst-wijziging uit; alleen toepassings-precedent vastgelegd).

Zie [[brain__sprints__T3-skos-bidirectional-audit-m14]] voor sprint-context.

## Hangt samen met

- [[brain__concepts__mapping-bron-disclaimer-effect]] — concept-beschrijving van het generaliseerbare patroon
- [[brain__concepts__skos-beoordelings-protocol]] — operationele methode voor SKOS-predicate-keuze (C1-C4 + bidirectional-symmetrie)
- [[brain__concepts__cluster-discipline-bewijslast]] — bewijslast-asymmetrie bij cluster-uitzonderingen
- [[brain__concepts__cross-category-mappings]] — cross-category-rationale als T3-precedent (control ↔ legal-obligation = associatief)
- [[brain__architecture__H36_skos-exactmatch-ctrl-compl-audit]] — afgehandelde aanleiding (T1) + m10-component closed via T2 + m14-subtask closed via T3 (fully closed)
- [[brain__architecture__H41_skos-axioma-set-handling]] — gerelateerd architectuur-item (geparkeerd post-T2; T3-bevestiging informatief)
- [[brain__sprints__T1_skos-kwaliteitsanalyse-fase-1]] — bron-sprint D4.1-vaststelling
- [[brain__sprints__T2-skos-bidirectional-audit-m10]] — bron-sprint cluster-niveau-toepassings-precedent
- [[brain__sprints__T3-skos-bidirectional-audit-m14]] — bron-sprint cross-category-rationale-precedent + D4.1-inactief-precedent
- [[brain__decisions__D05_sameAs-strikt-ctrl-bio]] — complementaire keuze: `owl:sameAs` voor strikte identiteit (ctrl:↔bio:)
- [[brain__decisions__D11_sameAs-asset-convergentie]] — idem voor asset-laag

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| ±2026-03 | active | Vaststelling (datum reconstructie) |
| 2026-05-27 | active | D4.1 toegevoegd: disclaimer-handling bij autoritatieve mapping-bronnen. Aanleiding T1-sprint (ENISA TIG regel 285). Reikwijdte: blokkeert `skos:exactMatch` alleen; close/related/broad/narrow blijven valide. Geen retroactieve audit (Optie A) — geldt vanaf vaststelling. |
| 2026-05-27 | active | D4.1-toepassings-precedent uitgebreid naar cluster-niveau na T2-sprint (118 paren over 10 m10-clusters). Bij homogene cluster-bron-stack volstaat één D4.1-bevestiging per cluster; heterogene clusters vereisen per-paar-toets. D4-tekst zelf onveranderd; alleen precedent-uitbreiding gedocumenteerd. |
| 2026-05-28 | active | D4-validatie-historie m14-scope toegevoegd na T3-sprint (31 paren over 5 AVG-clusters). Twee toepassings-precedenten: (a) D4.1 inactief in T3 (bindende T3-steer 1; AVG = publiek EU-recht zonder non-equivalence-disclaimer; 0 exactMatch-doel-overweging); (b) cross-category-rationale als toepassings-precedent (control ↔ legal-obligation = associatief, niet subsumptief; 2 broadMatch-paren → relatedMatch via masterchat-besluit Optie C; closeMatch-uitzondering op retrieval-interchangeability gehandhaafd voor T3-014 + T3-026). D4-tekst zelf onveranderd; alleen precedent-uitbreiding gedocumenteerd. Cross-category-formalisering blijft masterchat-werk (kandidaat v1.3.1-precedent). |

— Einde D04.
