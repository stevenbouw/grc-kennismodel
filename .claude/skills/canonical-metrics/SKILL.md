---
name: canonical-metrics
description: Run the canonical metrics measurement for the GRC Kennismodel ontology — OWL RL closure with axiomatic_triples=False + datatype_axioms=False, NamedIndividual count via set-of-subjects, six invariance metrics, version-suffix output. Use when a sprint asks to (re)compute v4.X.Y baseline metrics, verify pre/post-patch deltas, or sanity-check that the ontology hasn't drifted.
---

# canonical-metrics — GRC Kennismodel canonieke meetmethode

Codificeert de meetmethode achter `output/verification/canonical_metrics_v4_X_Y.py`. Geen ontologie-tekst, geen NEN-citaten — alleen methode + meetdiscipline.

## Wanneer activeren

- Sprint-instructie vraagt verificatie / patch-rapport §0 te vullen
- Pre- of post-patch baseline-meting (vorige → nieuwe versie vergelijken)
- Sanity-check op ongewijzigde ontologie (drift-detectie)
- Nieuwe versie krijgt eigen `canonical_metrics_v4_X_Y.py` (versie-suffix-conventie sinds v4.3.3)

## Invariante meet-instellingen

```python
import owlrl
owlrl.DeductiveClosure(
    owlrl.OWLRL_Semantics,
    axiomatic_triples=False,
    datatype_axioms=False,
).expand(graph)
```

Deze drie flags zijn de canonieke combinatie. **Wijzig nooit** zonder masterchat-besluit. Zonder `axiomatic_triples=False` lekt het OWL-vocabulary in de telling; zonder `datatype_axioms=False` lekken xsd-axioma's.

## NamedIndividual-telling

```python
from rdflib import RDF, OWL
named_individuals = len(set(g.subjects(RDF.type, OWL.NamedIndividual)))
```

**Niet** `len(list(...))` — dat overtelt bij multi-typing (een individual met meerdere `rdf:type OWL.NamedIndividual` triples telt anders dubbel). Set-of-subjects is canoniek.

Hetzelfde patroon voor `owl:Class`, `owl:ObjectProperty`, `owl:DatatypeProperty`, `owl:AnnotationProperty`, `skos:Concept`.

## Zes invariantie-metrics

Per release worden minimaal deze zes vergeleken tussen oude en nieuwe versie. Gelijkblijven = invariant (drift-vrij); afwijking = expliciet declareren in patch-rapport §0.

1. `global_pre_inference.triples`
2. `global_pre_inference.owl_Class`
3. `global_pre_inference.owl_NamedIndividual`
4. `global_pre_inference.owl_ObjectProperty`
5. `global_pre_inference.owl_sameAs`
6. `global_pre_inference.skos_mappings_total`

Plus de SKOS-breakdown (`exactMatch / closeMatch / broadMatch / narrowMatch / relatedMatch`) voor predicaat-mutaties die het totaal ongewijzigd laten (zoals T3 v4.6.3: broadMatch −2 / relatedMatch +2, totaal ongewijzigd).

## Versie-suffix-conventie (sinds v4.3.3)

| Bestand | Patroon |
|---|---|
| Script | `output/verification/canonical_metrics_v4_X_Y.py` |
| Output | `output/verification/canonical_metrics_v4_X_Y.json` |

**Nooit** zonder versie-suffix (`canonical_metrics.py` zonder versie is fout). Leerpunt v4.3.3 — eerdere scripts werden overschreven en historische metingen waren onreproduceerbaar.

## §0-discipline — uit JSON, niet uit memorie

Patch-rapport §0 (tellingen-vergelijking) wordt **uitsluitend** gevuld vanuit de JSON-output van het script. Niet uit chat-memorie, niet uit "vorige meting in mijn hoofd". Reden: discrepantie-incident v4.3.3 — patch-rapport §0 was uit memorie, JSON had andere cijfers, debug kostte een halve sprint.

Workflow:
1. Draai `python3 output/verification/canonical_metrics_v4_X_Y.py`
2. Open `output/verification/canonical_metrics_v4_X_Y.json`
3. Citeer rechtstreeks uit JSON in patch-rapport §0
4. Vergelijk met vorige versie-JSON voor delta-tabel

## Werkstappen — sprint-toepassing

1. **Kopieer** vorige `canonical_metrics_v4_X_(Y-1).py` naar `canonical_metrics_v4_X_Y.py`
2. **Update** drie plekken in de nieuwe file:
   - Module-docstring: versie-label + verwachte mutaties t.o.v. vorige baseline
   - `OUTPUT_PATH`: nieuwe versie-suffix
   - `meta.version_label` in output-dict: nieuwe label
3. **Draai** vanuit repo-root: `python3 output/verification/canonical_metrics_v4_X_Y.py`
4. **Verifieer** kernsamenvatting op stdout matcht verwachting
5. **Open** JSON, vul patch-rapport §0 invariantie-tabel
6. **Lever** beide bestanden via Protocol 16 (Deliverables-tabel met expliciete lokatie)

## Wat deze skill NIET doet

- Geen ontologie-mutaties
- Geen SHACL-validatie (zie skill `shacl-split`)
- Geen file-hash-vergelijking (apart `file_hashes_v4_X_Y.txt`-flow)
- Geen autonome commit (Steven commit handmatig — Protocol §0.5-firewall)
- Geen NEN-tekst-handling

## Cross-references

- Script-template: `output/verification/canonical_metrics_v4_6_3.py`
- Output-voorbeeld: `output/verification/canonical_metrics_v4_6_3.json`
- Discipline: `docs/sprint-protocols.md` §16 (Deliverables-lokatie), §18 (file-naming)
- Tech-agent-config: `.claude/agents/tech.md` (Tooling-sectie)
- D-conformance: D5 (ctrl↔bio sameAs = 93), D11 (asset-brug = 5) — zie `d_decision_conformance` in JSON
