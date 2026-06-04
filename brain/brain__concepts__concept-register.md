---
type: index
id: concept-register
title: Concept-register — Domein-glossary GRC Kennismodel
status: living
date: 2026-06-04
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
| [[brain__concepts__dashboard-productlijnen]] *(iteratie 12, Q-M-update iteratie 16, v7-stand iteratie 17)* ✨ | **Spoor A explorer (ontologie-graaf) vs Spoor B dashboard (operationeel) — twee productlijnen, niet vermengen. Q-M1..Q-M6-besluiten + Q-M2-reversal (v3-2 mag in repo). Iteratie 17: Spoor B v7-stand — 4 tabs + gelaagde kader-kiezer (D9-conform) + warm-papier-thema** | H40, skos-export-filter, spoor-b-revival, framework-neutraliteit, CLAUDE.md Spoor B-overweging |
| [[brain__concepts__spoor-b-revival]] *(iteratie 16, v7-werkstroom iteratie 17)* ✨ | **Spoor B-revival grc-dashboard-v3-2 — (29 mei) B7-wiring + bron-split 1A (wStruct/wOper) + Q-M5 lokaal vendoren + B9 WCAG 47→0; drie Spoor B-bron-besluiten + twee vervolgpunten. **(2–3 jun) v7-werkstroom**: reskin Overzicht + warm-papier-thema + DORA-correctie ("referentiekader · n.v.t.") + IA-herinrichting 5→4 tabs + gelaagde kader-kiezer (D9-conform). Twee OPEN besluiten: lege-huls (Pad 1/2) + organisatiestructuur (A/B/C)** | dashboard-productlijnen, H40, H29, skos-export-filter, framework-neutraliteit |
| [[brain__concepts__skos-beoordelings-protocol]] *(iteratie 13, T2-update iteratie 14, T3-update iteratie 15)* ✨ | **Bidirectional methode voor SKOS-match-type-evaluatie — vier criteria + predicate-doel-tabel + sterkte-ordening + cluster-discipline + bidirectional-audit-symmetrie. v1.0 (T1) → v1.2 (T2 operationeel) → v1.3 FINAL (T3 cross-category)** | D4 + D4.1, T1, T2, T3, H36, H41, mapping-bron-disclaimer-effect, cluster-discipline-bewijslast, cross-category-mappings |
| [[brain__concepts__mapping-bron-disclaimer-effect]] *(iteratie 13, T2-update iteratie 14, T3-context iteratie 15)* ✨ | **Autoritatieve mapping-bronnen met non-equivalence-disclaimer ondergraven `skos:exactMatch` zelfs bij sluitende C1-C3 — D4.1-toepassing op cluster-niveau bij homogene bron-stack (T2-precedent); inactief in T3 (AVG = publiek EU-recht zonder disclaimer)** | D4 + D4.1, T1, T2, T3, skos-beoordelings-protocol, cluster-discipline-bewijslast |
| [[brain__concepts__cluster-discipline-bewijslast]] *(iteratie 14)* ✨ | **Bewijslast-asymmetrie voor uitzonderingen binnen veel↔1-clusters — sterker mapping én zwakker mapping vereisen streng NEN-bewijs; cluster-default geen aanvullende bewijslast. T2-empirie: 0/10 succesvolle heuristiek-flag-uitzonderingen. T3-context: complementair aan cross-category-rationale (cluster-discipline binnen één categorie; cross-category tussen categorieën)** | D4 + D4.1, T1, T2, T3, skos-beoordelings-protocol, mapping-bron-disclaimer-effect, cross-category-mappings |
| [[brain__concepts__cross-category-mappings]] *(iteratie 15, kandidaat v1.3.1-precedent)* ✨ | **Cross-category-rationale: wanneer subject en object van een SKOS-mapping ontologisch verschillende categorieën zijn (control ↔ legal-obligation), is `relatedMatch` de associatieve basislijn. broad/narrowMatch is categorie-fout; closeMatch-uitzondering op retrieval-interchangeability. T3-empirie: 0/5 cluster-convergentie naar narrowMatch op 31 m14-paren. Kandidaat-formalisering = masterchat-werk** | D4, T3, skos-beoordelings-protocol, cluster-discipline-bewijslast, H36 |

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

### Product-scope-discipline
- **dashboard-productlijnen (iteratie 12, Q-M-update iteratie 16, v7-stand iteratie 17)** ✨ — Spoor A explorer vs Spoor B dashboard, niet vermengen; Q-M-architectuurbesluiten + Q-M2-reversal; v7-stand: 4 tabs + gelaagde kader-kiezer (D9-conform)
- **spoor-b-revival (iteratie 16, v7-werkstroom iteratie 17)** ✨ — (29 mei) B7-wiring + bron-split 1A + Q-M5 vendoring + B9 WCAG; (2–3 jun) reskin + DORA-correctie + IA-herinrichting; twee OPEN besluiten (lege-huls + organisatiestructuur)

### SKOS-kwaliteits-methode (T1+T2+T3-cluster)
- **skos-beoordelings-protocol (iteratie 13, T2-update iteratie 14, T3-update iteratie 15)** ✨ — bidirectional methode voor match-type-evaluatie; v1.0 (T1) → v1.2 (T2 operationeel) → v1.3 FINAL (T3 cross-category)
- **mapping-bron-disclaimer-effect (iteratie 13, T2-update iteratie 14, T3-context iteratie 15)** ✨ — autoritatieve mapping-bron met non-equivalence-disclaimer ondergraaft `exactMatch`; D4.1-cluster-niveau-toepassing bij homogene bron-stack; inactief in T3-context
- **cluster-discipline-bewijslast (iteratie 14)** ✨ — bewijslast-asymmetrie voor cluster-uitzonderingen; T2-empirisch bewijs 0/10 succesvolle uitzonderingen; complementair aan cross-category-rationale
- **cross-category-mappings (iteratie 15, kandidaat v1.3.1-precedent)** ✨ — cross-category-rationale; control ↔ legal-obligation = associatief (relatedMatch); T3-empirisch precedent op 31 m14-paren; formalisering = masterchat-werk

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
| **dashboard-productlijnen** | **(geen directe D — product-scope-onderscheid)** | **(geen — productlijn-scheiding raakt geen D-decision direct; Q-M3 bevestigt discipline)** |
| **spoor-b-revival** | **(geen directe D — Spoor B-prototype-werk, geen ontologie-mutatie)** | **D9 framework-neutraal in dashboard bevestigd; geen D-schending** |
| **skos-beoordelings-protocol** | **D4 + D4.1** | **(geen andere — opereert binnen D4 + D4.1; T2-cluster-niveau-precedent; T3-cross-category-precedent)** |
| **mapping-bron-disclaimer-effect** | **D4.1 (formeel sinds 27 mei 2026)** | **(D4.1-toepassings-precedent cluster-niveau via T2; D4.1 inactief in T3-context — AVG = publiek EU-recht)** |
| **cluster-discipline-bewijslast** | **(geen directe D — methode-bewijslast-aspect)** | **D4 + D4.1 (operationeel binnen cluster-discipline §3.3; complementair aan cross-category-rationale)** |
| **cross-category-mappings** | **D4 (kandidaat v1.3.1-aanvulling)** | **(opereert binnen D4; cross-category-rationale-precedent via T3 m14)** |

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
| **dashboard-productlijnen** | **iteratie 12 (post-v4.6.0 polish-mini-sprint); iteratie 16 (Q-M-besluiten + Q-M2-reversal)** | **Concept ontstaan uit sessie-rapport v2.0 §2.1 + §9.2; iteratie 16 verwerkt de zes Q-M-architectuurbesluiten + de Q-M2-reversal (v3-2 mag in repo)** |
| **spoor-b-revival** | **iteratie 16 (29 mei 2026 — geen ontologie-sprint)** | **Concept ontstaan uit dashboard-tussenrapport B7-wiring + dashboard-rapport Q-M5/B9 + besluitnotitie Q-M. Legt Spoor B-revival + drie bron-besluiten + twee vervolgpunten vast (Brein-registratie; dashboard-code niet aangeraakt)** |
| **skos-beoordelings-protocol** | **T1 (v4.6.1, 26 mei) + T2 (v4.6.2, 27 mei) + T3 (v4.6.3, 28 mei)** | **Methode-concept vastgesteld in T1 Stap 2 (v1.0); v1.2 in T2 in productie gevalideerd op 118 paren over 10 clusters; v1.3 DRAFT opgeleverd post-T2; v1.3 FINAL vastgesteld 28 mei door masterchat tijdens T3-scoping; v1.3 in productie gevalideerd op 31 m14-paren cross-category** |
| **mapping-bron-disclaimer-effect** | **T1 (v4.6.1) + T2 (v4.6.2) + T3-context (v4.6.3)** | **Concept ontstaan uit T1 §6 + §8 leerpunt 2 (ENISA TIG regel 285); D4.1 vastgesteld 27 mei 2026; T2-cluster-niveau-toepassings-precedent; T3-context inactief (AVG = publiek EU-recht zonder non-equivalence-disclaimer)** |
| **cluster-discipline-bewijslast** | **T2 (v4.6.2)** | **Concept ontstaan uit T2 Stap 3-leerpunt §6.5 + patch-rapport §6.3; empirisch gevalideerd via 0/10 succesvolle heuristiek-flag-uitzonderingen** |
| **cross-category-mappings** | **T3 (v4.6.3, 28 mei 2026)** | **Concept ontstaan uit T3 Stap 3-eindrapport §5 + patch-rapport v4.6.3 §13.1; empirisch precedent op 31 m14-paren over 5 AVG-clusters (control ↔ legal-obligation = associatief, niet subsumptief). Kandidaat v1.3.1-precedent (formalisering = masterchat-werk)** |

## Concepts versus workflows

| Onderwerp | Concept-file | Workflow-file |
|---|---|---|
| Scope-discipline | [[brain__concepts__scope-discipline]] (waarom) | [[brain__workflow__scope-discipline]] (hoe) |

## Toekomstige concepts (kandidaten — wachten op trigger)

- `route-patroon` — H24 Route 1/2/3/5-systematiek (Fase 2-context)
- `audit-trail` — concept achter audit:-namespace-uitbreidingen (wachten op trigger)
- `agentic-ai-laag` — visie-niveau, post-migratie-implementatie

— Einde concept-register.
