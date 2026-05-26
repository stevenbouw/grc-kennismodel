---
type: concept
title: NamedIndividual-telmethode
status: living
date: 2026-05-13
related:
  - canonical-metrics
  - H21_implicit-individuals
sources:
  - patch-rapport-v4_3_3
chat-sources:
  - https://claude.ai/chat/7ec4a4dc-7230-4135-96f4-c791e7271656
confidence: high
---

# NamedIndividual-telmethode

## Wat het is

De canonieke methode om `owl:NamedIndividual`-instances te tellen in het GRC Kennismodel:

```python
len(set(g.subjects(RDF.type, OWL.NamedIndividual)))
```

**Toepassing:** per-module-geparste graph, **pre-inference**, zonder impliciete rdflib-assertions.

Geldig voor canonical_metrics-scripts vanaf v4.3.3. Eindstaat v4.3.3: **637 NamedIndividuals**.

## Waarom formele definitie nodig

Tijdens v4.3.3-oplevering deed zich een **tellingsdiscrepantie** voor:

- Patch-rapport §0 baseline: **607 → 622**
- `canonical_metrics_v4_3_3.json`: **637**

Verschil van 15. Reconciliatie toonde aan: het patch-rapport was **uit memoire** opgesteld en reproduceerde daarmee een eerdere telling van *expliciet-bron-gedeclareerde* NamedIndividuals (subjects die zowel `rdf:type X` als `rdf:type owl:NamedIndividual` letterlijk in een module hebben staan). De canonical_metrics-meting telt alle subjects die — pre-inferentie, zonder rdflib-assertions — een `rdf:type owl:NamedIndividual`-triple hebben, ongeacht of die expliciet in het bestand staat of via Turtle-syntaxis-shorthand wordt afgeleid.

Sinds v4.3.3:

> **Canonical_metrics-JSON is enige autoritatieve bron** voor NamedIndividual-count. Patch-rapporten construeren §0-tabellen voortaan rechtstreeks uit JSON, niet uit memoire.

## Subtiliteiten bij telling

### Pre-inference versus post-inference

Onder OWL RL infereert de reasoner `owl:NamedIndividual` voor elk subject met een `rdf:type`-relatie naar een named class. Dit blaast de count met honderden op. Voor canonical metrics:

> **Pre-inference telling** — gebaseerd op wat letterlijk in de Turtle-bestanden staat (na rdflib-parsing), niet wat OWL RL infereert.

### Per-module versus gemergde graph

Verschillende meetbenaderingen leveren verschillende getallen:

| Methode | Wat het telt | Bias |
|---|---|---|
| Per-module geparst | Alleen subjects die in een module expliciet zijn gedeclareerd | Onderschatting (mist Turtle-syntax-shorthand) |
| Gemergd, pre-inference | Alle expliciete + Turtle-syntactisch afgeleide subjects | Autoritatief |
| Gemergd, post-OWL RL | Alle inferred NamedIndividuals | Overdreven hoog |

Canonical metrics gebruikt **gemergd + pre-inference** als autoriteit.

### `len(set(...))` versus simpele count

Het `set()`-gebruik dedupliceert. Een subject met twee `rdf:type owl:NamedIndividual`-triples (uit verschillende modules) telt als één. Dit is correct gedrag.

## Hangt samen met H21

[[brain__architecture__H21_implicit-individuals]] — bekend dat het model ~421 individuals heeft die wel `rdf:type` naar een klasse hebben maar geen expliciete `owl:NamedIndividual`-declaratie. Onder OWL RL wordt dit geïnferreerd. De canonical_metrics-telling **registreert deze impliciete individuals** (via Turtle-syntaxis-shorthand) wanneer ze in vorm `subject rdf:type SomeClass , owl:NamedIndividual` staan; maar **niet** wanneer alleen `subject rdf:type SomeClass` staat zonder co-typing.

Het H21-aantal is dus een bovengrens van wat onder volle inferentie zou worden afgeleid; canonical metrics telt alleen de expliciet of via shorthand gedeclareerde.

## Concrete trajectorie van de count

| Versie | Datum | Count | Reden delta |
|---|---|---:|---|
| v4.3.2 | ±21 april 2026 | 622 | Baseline |
| v4.3.3 | 22 april 2026 | 637 | +15 expliciete `owl:NamedIndividual`-declaraties op `compl:REQ_NIS2_*`-subjects |

Eerdere versies hebben hun eigen canonical_metrics-JSONs — die zijn autoritatief voor die versie.

## Procedurele consequentie

Bij elke nieuwe sprint:

1. Run `canonical_metrics_v[versie].py`
2. Construeer patch-rapport-§0-tabel direct uit JSON-output
3. **Niet uit memoire** of eerdere tellingen
4. Vermeld in patch-rapport expliciet "bron: canonical_metrics_v[versie].json"

## Hangt samen met

- [[brain__concepts__canonical-metrics]] — overkoepelende meetmethode
- [[brain__architecture__H21_implicit-individuals]] — onderliggende vraag over hoeveel individuals impliciet zouden zijn
- [[brain__concepts__skos-export-filter]] — verwante Class-vs-Individual-onderscheiding in dashboard-export-laag (v4.6.0)

— Einde NamedIndividual-telmethode.
