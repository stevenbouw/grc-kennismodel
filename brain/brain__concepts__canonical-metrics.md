---
type: concept
title: Canonical metrics — meetmethode-discipline
status: living
date: 2026-05-13
related:
  - namedindividual-telmethode
  - owl-rl-reasoning
  - gesplitste-shacl-validatie
sources:
  - patch-rapport-v4_3_3
  - migratierapport-technisch-v4_3_3
chat-sources: []
confidence: high
---

# Canonical metrics — meetmethode-discipline

## Wat het is

Bij elke release (minor en patch) draait de technische chat **twee verplichte scripts** en levert hun uitkomsten op als onderdeel van het patch-rapport:

| Script | Output | Doel |
|---|---|---|
| `canonical_metrics_v[versie].py` | `canonical_metrics_v[versie].json` | Kerntellingen (triples, klassen, individuals, properties, sameAs, SKOS) |
| `shacl_split_validate_v[versie].py` | `shacl_results_v[versie].json` | RUN 1 + RUN 2 SHACL-validatie-uitkomsten |

Plus `file_hashes_v[versie].txt` (SHA256 van alle input-bestanden) voor reproduceerbaarheid. Versie-suffix verplicht sinds v4.3.3.

## Waarom canoniek

Drie problemen die de discipline oplost:

### 1. Onverklaarde deltas tussen versies

Elke patch-rapport bevat baseline-vergelijking met de vorige versie op **alle canonieke metrics**. Onverklaarde deltas zijn een rode vlag. Voorbeeld v4.2.1: `−32` triples in data graph, **volledig gediagnostiseerd** als 3 verdwenen ontology-declaraties × ~10 metadata-triples. Zonder canonieke discipline zou dit als "ruis" zijn afgedaan.

### 2. Meting versus memoire

In v4.3.3 deed zich een tellingsdiscrepantie voor tussen patch-rapport (607 → 622 NamedIndividuals) en `canonical_metrics_v4.3.3.json` (637). Reconciliatie toonde aan dat het patch-rapport **uit memoire** was opgesteld, niet uit het JSON-bestand. Sindsdien:

> **Canonical_metrics-JSON is enige autoritatieve bron** voor kerntellingen. Patch-rapport-baseline-tabellen worden direct uit JSON gebouwd, niet uit memoire.

### 3. Consistente settings

OWL RL-reasoner-instellingen zijn cruciaal — verkeerde instellingen leveren verschillende tellingen. Canonieke configuratie (zie [[brain__concepts__owl-rl-reasoning]]):

```python
owlrl.DeductiveClosure(
    owlrl.OWLRL_Semantics,
    axiomatic_triples=False,
    datatype_axioms=False
).expand(g)
```

Beide `False`-instellingen zijn **niet onderhandelbaar** in canonical metrics-context.

## Welke metrics worden getrackt

Per release-vergelijking:

**Triples:**
- Pre-inferentie (gemergde data graph, excl. shapes)
- Post-OWL RL (inferred graph)
- Shapes-graph

**Klassen, individuals, properties:**
- `owl:Class` count
- `owl:NamedIndividual` count (zie [[brain__concepts__namedindividual-telmethode]])
- `owl:ObjectProperty` count
- `owl:DatatypeProperty` count

**Cross-framework structuur:**
- `owl:sameAs` count (D5 + D11 = 93 + 5 = 98)
- SKOS-mappings totaal (346)
- Per-namespace SKOS-distributie

**D-conformance:**
- D5: ctrl ↔ bio sameAs-count moet 93 zijn
- D8: SoAEntry-count moet 93 zijn
- D11: asset-bridges-count moet 5 zijn
- `ext:hasHandreikingBBN` totaal (241), met BBN1/BBN2-verdeling

**Integriteit-checks:**
- Dangling references (3, bekend sinds v4.3.0)
- Namespace leakage (21, bekend sinds v4.3.0)
- Duplicate owl:Class declaraties (0)
- Empty rdfs:labels (0)
- Empty rdfs:comments (0)

## Semantische invariantie-check

Bij refactoring of consolidatie (zoals v4.2.1 M18-merge) moeten **zes metrics voorspelbaar zijn**:

- klassen
- NamedIndividuals
- ObjectProperties
- DatatypeProperties
- owl:sameAs
- `asset:appliesToAssetType` (428 expliciet, 973 inferred onder OWL RL)

Ontology-metadata-triples mogen wel verschillen tussen versies. Semantische data niet.

## File-hashes als reproduceerbaarheidsgarantie

`file_hashes_v[versie].txt` bevat SHA256 van alle bron-bestanden. Bij latere reconstructie:

```bash
sha256sum -c file_hashes_v4_3_3.txt
```

Een hash-mismatch betekent: het input-corpus is veranderd. Daarmee zou een opnieuw-uitgevoerde canonical_metrics niet exact dezelfde uitkomst geven — wat alleen acceptabel is met expliciete masterchat-uitleg.

## Hangt samen met

- [[brain__concepts__namedindividual-telmethode]] — specifieke telmethode-formalisering binnen canonical metrics
- [[brain__concepts__owl-rl-reasoning]] — invocatie-settings die metrics bepalen
- [[brain__concepts__gesplitste-shacl-validatie]] — andere helft van de meetmethode

— Einde canonical metrics.
