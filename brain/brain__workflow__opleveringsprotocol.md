---
type: workflow
title: Opleveringsprotocol per release
status: living
date: 2026-05-13
related:
  - canonical-metrics
  - namedindividual-telmethode
  - gesplitste-shacl-validatie
sources:
  - projectinstructie-v1.6
chat-sources: []
confidence: high
---

# Opleveringsprotocol per release

## Principe

Bij elke minor- of patch-release (v4.X.Y) van de ontologie levert de technische chat **vijf vaste artefacten** plus het patch-rapport. Doel: meetmethode-consistentie tussen versies, reproduceerbaarheid, en heldere baseline-vergelijking.

## Verplichte artefacten per release

| # | Artefact | Inhoud |
|---|---|---|
| 1 | **22 ontologie-bestanden** | 18 modules + 2 infrastructure (grc-core, grc-bridges) + 1 shapes (grc-shacl) + 1 SPARQL (m18-demo) |
| 2 | `canonical_metrics_v[versie].py` | Meetmethode-script — afgeleid van v4.3.0 canonieke template, alleen versie-string aangepast |
| 3 | `canonical_metrics_v[versie].json` | Output van de meetmethode — **enige autoritatieve bron** voor kerntellingen |
| 4 | `shacl_split_validate_v[versie].py` | Gesplitste SHACL-validatie — afgeleid van v4.3.0 template |
| 5 | `shacl_results_v[versie].json` | RUN 1 (pre-inferentie) + RUN 2 (post-inferentie) uitkomsten |
| 6 | `file_hashes_v[versie].txt` | SHA256 van alle input-bestanden — verplicht versie-suffix sinds v4.3.3 |
| 7 | `patch-rapport-v[versie].md` | Sprint-document met §0-baseline, items, validatie, bevindingen |

## Patch-rapport-structuur

| § | Inhoud |
|---|---|
| §0 | Baseline-tabel: alle canonieke metrics deze versie + delta t.o.v. vorige. **Construeren direct uit canonical_metrics-JSON, niet uit memoire** ([[brain__concepts__namedindividual-telmethode]]) |
| §1+ | Per item: scope, uitvoering, validatie, eventuele scope-pauzes |
| §SHACL | Gesplitste SHACL-uitkomsten (RUN 1 + RUN 2) |
| §Bevindingen | Onverklaarde deltas, nieuwe geparkeerde items, leerpunten |
| §Bestandsintegriteit | Hash-vergelijking met vorige versie |
| §Aanbevelingen | Voor masterchat-acceptatie + volgende sprint |

## Validatie-gates — vier-uit-vier groen

Pre-acceptatie checklist:

1. **Parse-check** — alle 22 bestanden parsen foutloos met rdflib
2. **OWL RL reasoner** — 0 inconsistenties, 0 disjointness-violations, expected sameAs-propagatie
3. **Gesplitste SHACL** — RUN 1 = 0 violations, RUN 2 = 0 violations (mod. bekende false-positives)
4. **SPARQL smoke-tests** — Q1 (cross-framework controls), Q2 of Q3 (domain-specific) leveren verwachte resultaten

Eén-uit-vier rood = niet opleveren. Verschillen verklaren in §Bevindingen.

## Semantische invariantie-check

Bij refactoring of consolidatie moeten **zes metrics voorspelbaar zijn** (delta = bekend en uitlegbaar):

- `classes` (186)
- `named_individuals` (637)
- `object_properties` (140)
- `datatype_properties` (84)
- `owl:sameAs` pre-inf (98)
- `asset:appliesToAssetType` (428 expliciet / 973 inferred)

Onverwachte delta → pauzeren en onderzoeken vóór doorgaan ([[brain__workflow__scope-discipline]]).

## Hash-vergelijking als reproduceerbaarheidsgarantie

`file_hashes_v[versie].txt` bevat SHA256 van alle bron-bestanden. Bij latere reconstructie:

```bash
sha256sum -c file_hashes_v4_3_3.txt
```

Hash-mismatch = input-corpus is veranderd. Acceptabel alleen met expliciete masterchat-uitleg in §Bevindingen.

## Migratierapport bij chat-omgevingsovergang

Bij context-limiet in een tech-chat: migratierapport opstellen vóór nieuwe chat gestart wordt. Voorbeeld: `migratierapport-technisch-v4_3_3.md` brieft opvolger over staat, conventies, en volgende sprint.

## Cross-references

- [[brain__concepts__canonical-metrics]] — meetmethode-discipline
- [[brain__concepts__gesplitste-shacl-validatie]] — SHACL-validatie-mechanisme
- [[brain__workflow__scope-discipline]] — pauzes documenteren in patch-rapport

— Einde opleveringsprotocol.
