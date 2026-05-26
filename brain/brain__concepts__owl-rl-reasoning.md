---
type: concept
title: OWL RL reasoning
status: living
date: 2026-05-13
related:
  - D01_owl-2-dl-profiel
  - sameAs-discipline
  - canonical-metrics
  - gesplitste-shacl-validatie
sources:
  - projectinstructie-v1.6
chat-sources: []
confidence: high
---

# OWL RL reasoning

## Wat het is

**OWL RL** (Rule Language) is een profiel van OWL 2 dat polynomial-time complete reasoning ondersteunt via een vaste regelset. In het GRC Kennismodel is OWL RL het **minimum reasoning-niveau** voor alle correctheids-validatie en query-evaluatie.

Canonieke invocatie via Python/rdflib:

```python
import owlrl
owlrl.DeductiveClosure(
    owlrl.OWLRL_Semantics,
    axiomatic_triples=False,
    datatype_axioms=False
).expand(g)
```

De twee `False`-instellingen zijn **autoritatief** — zie sectie "Waarom deze instellingen".

## Waarom OWL RL minimum is

Het GRC Kennismodel gebruikt twee constructies waarvoor pure RDFS-inferentie onvoldoende is:

### 1. owl:sameAs-propagatie

Onder [[brain__decisions__D05_sameAs-strikt-ctrl-bio]] en [[brain__decisions__D11_sameAs-asset-convergentie]] worden klassen en instances via `owl:sameAs` geïdentificeerd. Properties propageren dan beide kanten op.

**Bewijs:** Q1 — Risk → asset via asset:Asset-klasse:

| Modus | Resultaten |
|---|---:|
| Pre-inference | 0 |
| Post OWL RL | 11 |

Zonder OWL RL ziet de reasoner de D11-bruggen niet → query is dood.

### 2. Property-restricties met inverseOf, domain, range

Voorbeelden uit het model:
- `isms:containsEntry owl:inverseOf isms:forSoA` (v4.3.1) propageert tot **+93 inferred** `containsEntry`-asserties
- `compl:articleRef rdfs:domain compl:Obligation` propageert types op alle 51 articleRef-dragers (zie [[brain__architecture__H25_compl-articleRef-domain-spanning]])
- Disjointness-controle (`owl:AllDisjointClasses`) levert alleen onder OWL RL of sterker de juiste 0-violations terug

## Waarom deze instellingen exact

**`axiomatic_triples=False`:** voorkomt dat OWL RL alle axiomatische triples uit OWL-vocabulary zelf toevoegt aan de graph. Die zouden de telmetrics opblazen zonder semantische waarde toe te voegen.

**`datatype_axioms=False`:** voorkomt dat OWL RL XSD-datatype-axiomas afleidt (bv. `xsd:integer rdfs:subClassOf xsd:decimal`). Levert dezelfde reden: ongewenste tellingsverstoring.

Zonder deze instellingen klopt geen enkele baseline-vergelijking. Daarom zijn ze **canoniek** geformaliseerd sinds v4.3.0 (zie [[brain__concepts__canonical-metrics]]).

## Sterker dan OWL RL: HermiT en Pellet

Voor diepere consistentie-validatie in Protégé worden HermiT of Pellet gebruikt (full OWL 2 DL reasoners). Deze ondersteunen complexe constructies die OWL RL niet doet (bv. complete classificatie onder negation, complex role hierarchies).

Status: HermiT-herrun in Protégé is niet uitgevoerd sinds v4.0.0 — staat in toekomst-overig.

## Praktische gevolgen

- **Validatie altijd onder OWL RL** — geen RDFS-inferentie als kortere weg
- **Canonical metrics-scripts** gebruiken de canonieke invocatie hierboven
- **SHACL-validatie** gesplitst tussen pre-inference (SECTIE A) en post-OWL-RL (SECTIE B), zie [[brain__concepts__gesplitste-shacl-validatie]]
- **SPARQL-queries voor diagnostiek** worden expliciet pre/post-inference vergeleken om sameAs-impact te tonen

## Hangt samen met

- [[brain__decisions__D01_owl-2-dl-profiel]] — model zelf is OWL 2 DL; reasoning ten minste OWL RL
- [[brain__concepts__sameAs-discipline]] — sameAs werkt alleen onder OWL RL
- [[brain__concepts__canonical-metrics]] — meetmethode-discipline gebruikt deze invocatie
- [[brain__concepts__gesplitste-shacl-validatie]] — directe consequentie

— Einde OWL RL reasoning.
