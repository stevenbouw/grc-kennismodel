---
type: index
id: concept-register
title: Concept-register — Domein-glossary GRC Kennismodel
status: living
date: 2026-05-26
---

# Concept-register — Domein-glossary

Overzicht van alle concept-files. Concepts zijn **levende uitlegdocumenten** (in tegenstelling tot D-decisions die immutable zijn na vaststelling, en sprint-files die immutable zijn na release).

## Snelle navigatie

| Concept | Wat het uitlegt | Hangt samen met |
|---|---|---|
| [[brain__concepts__framework-neutraliteit]] | Architectuur-invariant: alle frameworks gelijkwaardig (4 verificatie-clusters v4.6.0) | D9, D10, D11, D12 |
| [[brain__concepts__sameAs-discipline]] | Strikt gebruik van owl:sameAs (98 asserties, D5+D11) | D5, D11, gesplitste-SHACL |
| [[brain__concepts__bbn-correctie]] | BBN is Handreiking-eigenschap, niet BIO 2.0-eigenschap | D7, v4.1.0-alpha |
| [[brain__concepts__drie-laags-compliance]] | Drie-laags compliance-architectuur (D12) — patroon, niet starre symmetrie | D12, H25, H26, H27, H32 |
| [[brain__concepts__owl-rl-reasoning]] | Waarom OWL RL minimum is + canonieke settings | D1, sameAs, canonical-metrics |
| [[brain__concepts__gesplitste-shacl-validatie]] | SECTIE A vs SECTIE B, 290 false-positives onder combined | sameAs, OWL-RL |
| [[brain__concepts__canonical-metrics]] | Meetmethode-discipline per release | NamedIndividual-telmethode, OWL-RL |
| [[brain__concepts__namedindividual-telmethode]] | Canonieke teldefinitie (v4.3.3-formalisering) | canonical-metrics, H21 |
| [[brain__concepts__provenance-en-attribuering]] | Bron-discipline + licentie-bewustzijn (5 SourceAttributions v4.6.0) | canonical-metrics, sources |
| [[brain__concepts__scope-discipline]] | Werk-invariant: scope-afwijkingen altijd melden | D9, workflow/scope-discipline |
| [[brain__concepts__meeliftregel-edit-scope]] | D6-onderscheid edit-scope versus bestand-scope | D6, scope-discipline |
| [[brain__concepts__cross-bron-overlap]] | SKOS-kwaliteits-indicator: 2+ onafhankelijke bronnen, zelfde mapping | provenance, sources |
| [[brain__concepts__parallelle-maturity-clusters]] *(iteratie 11)* ✨ | **biz vs isms maturity-clusters — twee parallelle modellen, niet samenvoegen** | v4.6.0, M06, M07 |
| [[brain__concepts__skos-export-filter]] *(v4.6.0)* ✨ | **Ontologie-laag (1.798) vs dashboard-laag (1.759) — twee meet-conventies, beide kloppen** | canonical-metrics, namedindividual-telmethode |

## Clusters

### Architectuur-fundamenten
- framework-neutraliteit (D9 — 4 verificatie-clusters per v4.6.0)
- sameAs-discipline (D5 + D11)
- drie-laags-compliance (D12)
- **parallelle-maturity-clusters (v4.6.0)** ✨

### Bron- en correctie-context
- bbn-correctie (Handreiking-onderscheid)
- provenance-en-attribuering (bron-discipline, 5 SourceAttributions)
- cross-bron-overlap (kwaliteits-indicator)

### Meet- en validatie-discipline
- owl-rl-reasoning
- gesplitste-shacl-validatie
- canonical-metrics
- namedindividual-telmethode
- **skos-export-filter (v4.6.0)** ✨

### Werk-discipline
- scope-discipline
- meeliftregel-edit-scope

## Cross-references naar D-decisions

| Concept | Primaire D | Andere D's |
|---|---|---|
| framework-neutraliteit | D9 | D10, D11, D12 |
| sameAs-discipline | D5 | D11, D4 |
| bbn-correctie | (geen directe D) | D7 |
| drie-laags-compliance | D12 | D9 |
| owl-rl-reasoning | D1 | D5, D11 |
| gesplitste-shacl-validatie | (geen directe D — methode) | D5, D11 |
| canonical-metrics | (geen directe D — discipline) | — |
| namedindividual-telmethode | (geen directe D — formalisering v4.3.3) | — |
| provenance-en-attribuering | (geen directe D — discipline) | — |
| scope-discipline | (geen directe D — werk-invariant) | D9 |
| meeliftregel-edit-scope | D6 | scope-discipline |
| cross-bron-overlap | (geen directe D — emergente kwaliteits-indicator) | provenance |
| **parallelle-maturity-clusters** | **(geen directe D — V1-architectuur-uitkomst)** | **D9 (twee gelijkwaardige clusters)** |
| **skos-export-filter** | **(geen directe D — measurement-conventie-verfijning)** | **D1, D4, D11 (alle getoetst, geen schending)** |

## Cross-references naar sprints waar concepten zijn ontstaan / verfijnd

| Concept | Sprint | Inhoud |
|---|---|---|
| framework-neutraliteit | 17 mrt 2026 + v4.4.0 + v4.5.0 + **v4.6.0 ENSIA-cluster** | Initieel besluit + cumulatieve verificatie op 4 clusters |
| sameAs-discipline | v2.0 (D5) + v4.3.0 (D11) | Incrementele uitbouw |
| bbn-correctie | v4.1.0-alpha | Actie A |
| drie-laags-compliance | v4.3.3 + v4.4.0 | D12 + patroon-verfijning |
| owl-rl-reasoning | v4.3.0 | Canonieke meetmethode |
| gesplitste-shacl-validatie | v4.2.0 → v4.3.0 | Discovery + uitbreiding |
| canonical-metrics | v4.3.0 | Initiële formalisering |
| namedindividual-telmethode | v4.3.3 | Reconciliatie |
| provenance-en-attribuering | v4.1.0-alpha + v1.6 + v4.5.0 + **v4.6.0 (5 SourceAttributions)** | Incrementele uitbouw |
| scope-discipline | v4.2.2 → v4.3.3 | Werkpatroon-evolutie |
| meeliftregel-edit-scope | v4.1.0-alpha + v1.7 + v4.5.0 + **v4.6.0 symmetrische uitbreiding** | Formele vastlegging + concrete toepassingen |
| cross-bron-overlap | v4.5.0 (S5 ∩ S6 = 105) | Concept ontstaan uit observatie |
| **parallelle-maturity-clusters** | **v4.6.0 (V1-uitkomst Optie B)** | **Concept ontstaan uit Fase 4 V1-evaluatie** |
| **skos-export-filter** | **v4.6.0 (tech-inspectie 39 tripels)** | **Concept ontstaan uit ontologie-laag vs dashboard-laag meet-discrepantie** |

## Concepts versus workflows

| Onderwerp | Concept-file | Workflow-file |
|---|---|---|
| Scope-discipline | [[brain__concepts__scope-discipline]] (waarom) | [[brain__workflow__scope-discipline]] (hoe) |

## Toekomstige concepts (kandidaten — wachten op trigger)

- `route-patroon` — H24 Route 1/2/3/5-systematiek (Fase 2-context)
- `audit-trail` — concept achter audit:-namespace-uitbreidingen (wachten op trigger)
- `agentic-ai-laag` — visie-niveau, post-migratie-implementatie

— Einde concept-register.
