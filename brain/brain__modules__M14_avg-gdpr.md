---
type: module
id: M14
title: M14 — AVG/GDPR (compl:)
status: active
date: 2026-05-28
related:
  - H31_toetsingskader-algoritmes
  - H36_skos-exactmatch-ctrl-compl-audit
  - T3-skos-bidirectional-audit-m14
  - skos-beoordelings-protocol
  - cross-category-mappings
  - D04_skos-cross-framework
sources:
  - patch-rapport-v4_6_3
  - t3-stap3-eindrapport
chat-sources: []
confidence: high
---

# M14 — AVG / GDPR

## Bestand
`m14-avg-gdpr.ttl`

## Namespace
Hergebruikt `compl:` + `fw:AVG`.

## Wat het bevat

**Alleen de IB-raakvlakken van de AVG** — geen volledige AVG-implementatie. Scope vastgelegd op 16 maart 2026.

| Artikel | Onderwerp |
|---|---|
| Art. 5 lid 1 sub f | Integriteit en vertrouwelijkheid (security by design) |
| Art. 25 | Privacy by Design and by Default |
| Art. 32 | Beveiliging van de verwerking |
| Art. 33 | Melding van inbreuken aan toezichthouder |
| Art. 34 | Melding van inbreuken aan betrokkenen |

## Klassen

`compl:AVGRequirement` als specifieke subklasse van `compl:ComplianceRequirement`.

## Waarom alleen IB-raakvlak

AVG is privacy-wetgeving; alleen de artikelen met directe informatiebeveiligings-impact landen in dit GRC-kennismodel. Volledige AVG-modellering (consent, DPIA, transparantie, betrokkenen-rechten) hoort thuis in een privacy-management-systeem, niet in een IB-kennismodel.

Besluit: niet uitbreiden buiten IB-scope zonder masterchat-GO.

## Toekomst-relaties

- [[brain__architecture__H31_toetsingskader-algoritmes]] — Toetsingskader Algoritmes (AR) heeft een Privacy-perspectief dat naar M14 wijst
- Fase 4 maturity-model — AVG-conformiteit als één van de assessment-dimensies

## SKOS-mapping-stand post-T3 (v4.6.3)

T3-sprint (28 mei 2026) heeft alle 31 compl→ctrl-paren in `m14-avg-gdpr.ttl` beoordeeld onder Protocol v1.3 FINAL. Eindstand m14 compl→ctrl SKOS-distributie:

| Predicate | v4.6.2 | v4.6.3 | Δ |
|---|---:|---:|---:|
| `skos:exactMatch` | 0 | 0 | 0 |
| `skos:closeMatch` | 2 | 2 | 0 |
| `skos:broadMatch` | 2 | **0** | **−2** |
| `skos:narrowMatch` | 0 | 0 | 0 |
| `skos:relatedMatch` | 27 | **29** | **+2** |
| **Totaal compl→ctrl m14** | **31** | **31** | **0** |

**Per-cluster-stand v4.6.3:**

| AVG-cluster | Cluster-grootte | close | broad | related | Heterogeniteit |
|---|---:|---:|---:|---:|---|
| AVG_Art5_1f (Integriteit en vertrouwelijkheid) | 7 | 0 | 0 | 7 | homogeen (na T3) |
| AVG_Art25 (Privacy by design and by default) | 6 | 0 | 0 | 6 | homogeen |
| AVG_Art32 (Beveiliging van de verwerking) | 12 | 1 | 0 | 11 | heterogeen (T3-014 closeMatch op Art32 → 5.01) |
| AVG_Art33 (Melding inbreuk toezichthouder) | 4 | 1 | 0 | 3 | heterogeen (T3-026 closeMatch op Art33 → 5.24) |
| AVG_Art34 (Mededeling inbreuk betrokkene) | 2 | 0 | 0 | 2 | homogeen |

**T3-mutaties (beide downgrade broadMatch → relatedMatch):**

- T3-001: `compl:AVG_Art5_1f skos:relatedMatch ctrl:ISO27002_5_01` (was broadMatch — masterchat-besluit Optie C)
- T3-002: `compl:AVG_Art5_1f skos:relatedMatch ctrl:ISO27002_5_12` (was broadMatch — masterchat-besluit Optie C)

**Cross-category-rationale (T3-leerpunt):** control ↔ legal-obligation is een cross-category-relatie die inherent associatief (`relatedMatch`) is, niet subsumptief. closeMatch-uitzondering op retrieval-interchangeability gehandhaafd voor T3-014 (governance/policy) + T3-026 (incident-planning). Zie [[brain__concepts__cross-category-mappings]] *(nieuw iteratie 15)*.

**File-hash m14-avg-gdpr.ttl:** v4.6.2 `47daeb7e6f37080b5f88b6d4d594a0401e5f1e32356d330d9cbc0b287251d353` → v4.6.3 `874565bade04c1657841298d4b035fa9c7f06f46a8d76ce9efba8ecfb35e1864`.

## Bronlicentie

AVG = publiek EU-recht — vrij herbruikbaar.

Evidence-bronnen T3 (uit ISO 27701:2025 Annex D + Annex F twee-staps-keten + ISO 27002:2022 §-clausules + AVG EUR-Lex CELEX:32016R0679; via lokale NEN-licentie-toegang Protocol 17 v1.3 Tech-autonomie).

— Einde M14.
