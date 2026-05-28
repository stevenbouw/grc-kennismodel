---
name: shacl-split
description: Run the SHACL validation in the canonical split form for the GRC Kennismodel — SECTIE A (inference='none') + SECTIE B (inference='owlrl') + COMBINED reference run. Use when a sprint asks to validate the ontology against SHACL shapes, distinguish genuine violations from the 290 known COMBINED false-positives, or sanity-check that shape-conformance hasn't drifted from baseline.
---

# shacl-split — gesplitste SHACL-validatie

Codificeert de meetmethode achter `output/verification/shacl_split_validate_v4_X_Y.py`. Splitst de SHACL-validatie expliciet zodat OWA/CWA-ruis (290 bekende false-positives onder COMBINED) niet wordt verward met echte shape-violations.

## Wanneer activeren

- Sprint-instructie vraagt SHACL-verificatie / patch-rapport-validatie
- Pre- of post-patch validatie van shape-conformance
- Drift-detectie op SECTIE A/B-violations (verwacht 0/0 — alles >0 = onderzoek)
- COMBINED-meting voor referentie en regressie-bewaking

## De splitsing

| Sectie | Shapes | Inference | Verwacht |
|---|---|---|---|
| **SECTIE A** | `ctrl:ISO27002NamingShape`, `bio:ISO27002NamingShape`, `ctrl:HandreikingBBNValueShape`, `asset:NamespaceShape` | `none` | **0 violations** |
| **SECTIE B** | `asset:AppliesToAssetTypeRangeShape`, `asset:BVASymmetryShape`, `asset:OrphanClassShape` | `owlrl` | **0 violations** |
| **COMBINED** | volledige shapes-set | `owlrl` | **290 false-positives** (baseline v4.6.x) |

**SECTIE A draait MET `inference='none'`.** Het zijn naming/value-shapes op concrete individuals; OWL RL closure produceert hier false-positives doordat afgeleide types via subClassOf-inheritance shape-evaluation triggeren op afgeleide klassen. Met `none` valideren we de shapes alleen op de directe assertions — wat overeenkomt met de bedoeling van naming/value-shapes.

**SECTIE B draait MET `inference='owlrl'`.** Range- en symmetrie-shapes vereisen juist de afgeleide triples (bv. een sameAs-keten moet eerst gemerged worden voor symmetrie-check). Subset-shapes-graph wordt gebouwd via traversal van behouden shape-IRIs incl. blanknode-property-shapes.

**COMBINED** = volledige shapes-set + `owlrl`. Levert 290 false-positives op SECTIE A-shapes onder OWL RL closure. Dit is een **bekend OWA/CWA-fenomeen**, geen modeldefect — zie [arXiv 2507.12286](https://arxiv.org/abs/2507.12286) voor de theoretische onderbouwing. De 290 vormen de drift-baseline.

## Subset-shapes-graph constructie

```python
def build_subset_shapes(full_shapes: Graph, keep_shape_iris: set[str]) -> Graph:
    subset = Graph()
    for prefix, ns in full_shapes.namespaces():
        subset.bind(prefix, ns)
    visited = set()
    to_visit = [URIRef(iri) for iri in keep_shape_iris]
    while to_visit:
        node = to_visit.pop()
        if node in visited:
            continue
        visited.add(node)
        for p, o in full_shapes.predicate_objects(node):
            subset.add((node, p, o))
            if not isinstance(o, URIRef) and o not in visited:
                to_visit.append(o)
    return subset
```

CBD-achtige traversal: behoudt alle triples bereikbaar vanuit de meegegeven shape-IRIs incl. blanknode-property-shapes. T1-precedent leverde dit niet; v4.6.2-instructie §5.1 voegde het toe voor expliciete SECTIE B-meting.

## Violation-telling

```python
def count_violations(report_text: str) -> tuple[bool, int, dict[str, int]]:
    rg = Graph()
    rg.parse(data=report_text, format="turtle")
    violations = list(rg.subjects(SH.resultSeverity, SH.Violation))
    per_shape: Counter = Counter()
    for v in violations:
        for shape in rg.objects(v, SH.sourceShape):
            per_shape[str(shape)] += 1
    return len(violations) == 0, len(violations), dict(per_shape)
```

`conforms` = True alleen bij 0 violations. Per-source-shape-breakdown geeft drift-locatie.

## Werkstappen — sprint-toepassing

1. **Kopieer** vorige `shacl_split_validate_v4_X_(Y-1).py` naar `shacl_split_validate_v4_X_Y.py`
2. **Update** twee plekken:
   - Module-docstring: versie-label + verwachte mutaties t.o.v. vorige baseline
   - `OUTPUT_PATH`: nieuwe versie-suffix
3. **Draai** vanuit repo-root: `python3 output/verification/shacl_split_validate_v4_X_Y.py`
4. **Verifieer** kernsamenvatting:
   - SECTIE A (none): **0** (drift-vrij)
   - SECTIE B (owlrl): **0** (drift-vrij)
   - COMBINED (owlrl): **290** (baseline; delta_vs_v4_6_x = 0)
5. **Bij afwijking**: onderzoek per-shape-breakdown in JSON; scope-pauze indien onverklaarbaar
6. **Lever** script + JSON via Protocol 16 (Deliverables-tabel)

## Drift-interpretatie

| Observatie | Betekenis |
|---|---|
| A=0, B=0, COMBINED=290 | **Drift-vrij** — baseline gehandhaafd |
| A=0, B=0, COMBINED=290±k | k kleine afwijking: nieuwe individuals onder shapes met OWA/CWA-gevoeligheid. Verklaarbaar uit patch-scope = OK |
| A>0 of B>0 | **Echte violations** — sprint-uitvoering vroegtijdig stoppen, patch herbeoordelen |
| COMBINED ≪ 290 | Vermoedelijk shape-set ingekrompen of inference-instellingen gewijzigd — onderzoek |

## Wat deze skill NIET doet

- Geen ontologie-mutaties
- Geen canonical-metrics-meting (zie skill `canonical-metrics`)
- Geen autonome commit (Steven commit handmatig — Protocol §0.5-firewall)
- Geen reasoner-vergelijking (alleen pySHACL + owlrl)
- Geen NEN-tekst-handling

## Cross-references

- Script-template: `output/verification/shacl_split_validate_v4_6_3.py`
- Output-voorbeeld: `output/verification/shacl_results_v4_6_3.json`
- Shapes-bron: `ontology/grc-shacl.ttl`
- Open architectuur-vraag: H39 (290 false-positives uitsplitsing) — `brain/brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing.md`
- OWA/CWA-onderbouwing: arXiv 2507.12286
- Tech-agent-config: `.claude/agents/tech.md` (Tooling-sectie "Gesplitste SHACL-validatie verplicht")
