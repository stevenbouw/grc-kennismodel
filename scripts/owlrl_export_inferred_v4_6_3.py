#!/usr/bin/env python3
"""owlrl_export_inferred_v4_6_3.py — H38-evaluatie, owlrl-ZIJDE (subagent-uitvoerbaar).

EVALUATIE-script, geen productie-config-wijziging. Gebruikt EXACT de canonieke
OWL RL-configuratie (axiomatic_triples=False, datatype_axioms=False) — identiek aan
canonical_metrics_v4_6_3.py. Schrijft NIET naar canonical_metrics-output.

Doel (H38, Stap 1 uit instructie §2):
  1. Merge de 21 data-modules (grc-shacl.ttl uitgesloten) — exact zoals canonical.
  2. Pas canonieke OWL RL-closure toe.
  3. Exporteer de inferred merged graph naar TTL, zodat een triple-set-diff tegen
     een HermiT-export (Protégé, lokale-Mac-actie van projecteigenaar) mogelijk is
     met owlrl_hermit_diff.py.
  4. Maak een 'DL-construct-census': tel de OWL 2-constructies in de TBox die
     BUITEN het OWL RL-profiel vallen of waar OWL RL en een volledige DL-reasoner
     (HermiT) kunnen afwijken. Dit maakt de verwachte HermiT-delta analytisch
     voorspelbaar VOORDAT de HermiT-run beschikbaar is.

Outputs (output/verification/, niet-canoniek):
  - owlrl_inferred_v4_6_3.ttl        (inferred merged graph, voor diff)
  - owlrl_dl_census_v4_6_3.json      (DL-construct-census + verwachtings-analyse)

Vereist: rdflib >=7.0, owlrl >=7.0
"""
from __future__ import annotations

import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from rdflib import Graph, URIRef, BNode, Literal, RDF, RDFS, OWL
from rdflib.namespace import SKOS
import owlrl

REPO_ROOT = Path(__file__).resolve().parents[1]
WORKDIR = Path(os.environ.get("GRC_WORKDIR", REPO_ROOT / "ontology"))
SHAPES_FILE = "grc-shacl.ttl"
OUT_TTL = REPO_ROOT / "output" / "verification" / "owlrl_inferred_v4_6_3.ttl"
OUT_JSON = REPO_ROOT / "output" / "verification" / "owlrl_dl_census_v4_6_3.json"


def build_merged_graph(workdir: Path) -> Graph:
    g = Graph()
    for fp in sorted(p for p in workdir.iterdir()
                     if p.suffix == ".ttl" and p.name != SHAPES_FILE):
        g.parse(fp, format="turtle")
    return g


def apply_canonical_owlrl(g: Graph) -> None:
    """EXACT de canonieke configuratie. Niet wijzigen."""
    owlrl.DeductiveClosure(
        owlrl.OWLRL_Semantics,
        axiomatic_triples=False,
        datatype_axioms=False,
    ).expand(g)


def dl_construct_census(g: Graph) -> dict:
    """Tel OWL 2-constructies die het OWL RL- vs DL-verschil bepalen.

    OWL RL ondersteunt GEEN volledige redenering over o.a.:
      - owl:someValuesFrom in superklasse-positie (existentiële conclusies)
      - owl:unionOf in subklasse-positie / owl:complementOf (negatie)
      - owl:oneOf (enumeraties) volledige classificatie
      - owl:maxQualifiedCardinality / owl:qualifiedCardinality (qualified card.)
      - owl:hasKey volledige redenering
      - complexe property-chains in alle richtingen
    OWL RL DOET WEL: subClassOf, subPropertyOf, domain/range, sameAs-propagatie,
      inverseOf, Symmetric/Transitive/Functional-property, allValuesFrom (beperkt),
      someValuesFrom in subklasse-positie (existential->type), disjointness.

    Census telt voorkomens; per construct geeft 'rl_complete' aan of OWL RL hier
    volledig is (True) of mogelijk afwijkt van DL/HermiT (False).
    """
    def count_pred(pred) -> int:
        return len(list(g.triples((None, pred, None))))

    def count_type(cls) -> int:
        return len(set(g.subjects(RDF.type, cls)))

    # Restriction-fillers: tel someValuesFrom/allValuesFrom/cardinaliteiten
    some_vals = count_pred(OWL.someValuesFrom)
    all_vals = count_pred(OWL.allValuesFrom)
    has_value = count_pred(OWL.hasValue)
    min_card = count_pred(OWL.minCardinality)
    max_card = count_pred(OWL.maxCardinality)
    exact_card = count_pred(OWL.cardinality)
    min_qcard = count_pred(OWL.minQualifiedCardinality)
    max_qcard = count_pred(OWL.maxQualifiedCardinality)
    exact_qcard = count_pred(OWL.qualifiedCardinality)

    union_of = count_pred(OWL.unionOf)
    intersection_of = count_pred(OWL.intersectionOf)
    complement_of = count_pred(OWL.complementOf)
    one_of = count_pred(OWL.oneOf)
    has_key = count_pred(OWL.hasKey)
    property_chain = count_pred(OWL.propertyChainAxiom)
    inverse_of = count_pred(OWL.inverseOf)

    equivalent_class = count_pred(OWL.equivalentClass)
    equivalent_prop = count_pred(OWL.equivalentProperty)
    disjoint_with = count_pred(OWL.disjointWith)
    all_disjoint = count_type(OWL.AllDisjointClasses)
    disjoint_union = count_pred(OWL.disjointUnionOf)

    symmetric = count_type(OWL.SymmetricProperty)
    transitive = count_type(OWL.TransitiveProperty)
    functional = count_type(OWL.FunctionalProperty)
    inverse_functional = count_type(OWL.InverseFunctionalProperty)
    asymmetric = count_type(OWL.AsymmetricProperty)
    irreflexive = count_type(OWL.IrreflexiveProperty)
    reflexive = count_type(OWL.ReflexiveProperty)

    # equivalentClass met blanknode-target (klasse-expressie) vs named (alias)
    eqc_to_bnode = sum(1 for _, _, o in g.triples((None, OWL.equivalentClass, None))
                       if isinstance(o, BNode))
    eqc_to_named = sum(1 for _, _, o in g.triples((None, OWL.equivalentClass, None))
                       if isinstance(o, URIRef))

    # someValuesFrom in superklasse-positie: subClassOf -> restriction met someValuesFrom
    # (existentiële conclusie — OWL RL niet volledig). Benadering: restricties met
    # someValuesFrom die object zijn van rdfs:subClassOf.
    svf_in_super = 0
    for restr in g.subjects(OWL.someValuesFrom, None):
        # is deze restrictie een superklasse (object van subClassOf)?
        if any(g.triples((None, RDFS.subClassOf, restr))):
            svf_in_super += 1

    census = {
        "restriction_fillers": {
            "someValuesFrom": {"count": some_vals, "rl_complete": False,
                "note": "Existentiële conclusie in superklasse-positie: OWL RL leidt geen nieuwe anonieme instances af; HermiT wel (consistentie-niveau)."},
            "someValuesFrom_in_superclass_position": {"count": svf_in_super, "rl_complete": False,
                "note": "Subset van someValuesFrom die als superklasse fungeert — primaire RL/DL-divergentiebron."},
            "allValuesFrom": {"count": all_vals, "rl_complete": True,
                "note": "OWL RL ondersteunt allValuesFrom in subklasse-positie (universele propagatie)."},
            "hasValue": {"count": has_value, "rl_complete": True},
            "minCardinality": {"count": min_card, "rl_complete": False,
                "note": "min-cardinaliteit >0 vereist existentiële afleiding — OWL RL onvolledig."},
            "maxCardinality": {"count": max_card, "rl_complete": True,
                "note": "max-cardinaliteit gebruikt OWL RL voor sameAs/inconsistentie-detectie."},
            "cardinality": {"count": exact_card, "rl_complete": False},
            "minQualifiedCardinality": {"count": min_qcard, "rl_complete": False},
            "maxQualifiedCardinality": {"count": max_qcard, "rl_complete": True},
            "qualifiedCardinality": {"count": exact_qcard, "rl_complete": False},
        },
        "class_expressions": {
            "unionOf": {"count": union_of, "rl_complete": False,
                "note": "unionOf in superklasse-positie (disjunctie-redenering) buiten OWL RL."},
            "intersectionOf": {"count": intersection_of, "rl_complete": True,
                "note": "intersectionOf in subklasse-positie ondersteund door OWL RL."},
            "complementOf": {"count": complement_of, "rl_complete": False,
                "note": "Negatie/complement buiten OWL RL-expressiviteit."},
            "oneOf": {"count": one_of, "rl_complete": False,
                "note": "Enumeratie-classificatie onvolledig in OWL RL."},
            "disjointUnionOf": {"count": disjoint_union, "rl_complete": False},
        },
        "property_axioms": {
            "inverseOf": {"count": inverse_of, "rl_complete": True},
            "propertyChainAxiom": {"count": property_chain, "rl_complete": True,
                "note": "OWL RL ondersteunt property-chains (subPropertyOf chain)."},
            "hasKey": {"count": has_key, "rl_complete": False},
            "equivalentProperty": {"count": equivalent_prop, "rl_complete": True},
            "SymmetricProperty": {"count": symmetric, "rl_complete": True},
            "TransitiveProperty": {"count": transitive, "rl_complete": True},
            "FunctionalProperty": {"count": functional, "rl_complete": True},
            "InverseFunctionalProperty": {"count": inverse_functional, "rl_complete": True},
            "AsymmetricProperty": {"count": asymmetric, "rl_complete": True},
            "IrreflexiveProperty": {"count": irreflexive, "rl_complete": True},
            "ReflexiveProperty": {"count": reflexive, "rl_complete": False,
                "note": "Reflexiviteit genereert self-triples; OWL RL beperkt."},
        },
        "class_axioms": {
            "equivalentClass_total": {"count": equivalent_class},
            "equivalentClass_to_named": {"count": eqc_to_named, "rl_complete": True,
                "note": "Named alias — bidirectionele subClassOf, OWL RL volledig."},
            "equivalentClass_to_bnode_expression": {"count": eqc_to_bnode, "rl_complete": False,
                "note": "equivalentClass naar klasse-expressie (restrictie/union): classificatie mogelijk DL-only."},
            "disjointWith": {"count": disjoint_with, "rl_complete": True,
                "note": "OWL RL detecteert disjointness-schending (inconsistentie)."},
            "AllDisjointClasses": {"count": all_disjoint, "rl_complete": True},
        },
    }

    # Aggregatie: som van constructies waar rl_complete=False (divergentie-risico)
    divergence_constructs = []
    for group, items in census.items():
        for name, info in items.items():
            if isinstance(info, dict) and info.get("rl_complete") is False and info.get("count", 0) > 0:
                divergence_constructs.append({
                    "construct": f"{group}.{name}",
                    "count": info["count"],
                    "note": info.get("note", ""),
                })
    census["_divergence_risico_constructs"] = sorted(
        divergence_constructs, key=lambda x: -x["count"])
    census["_divergence_construct_count_total"] = sum(
        c["count"] for c in divergence_constructs)

    return census


def main():
    print(f"=== owlrl_export_inferred_v4_6_3 (H38, owlrl-zijde) — "
          f"{datetime.now(timezone.utc).isoformat()} ===")
    print(f"Workdir: {WORKDIR}")

    g = build_merged_graph(WORKDIR)
    pre_triples = len(g)
    print(f"Pre-inference triples (merged, excl. shapes): {pre_triples}")

    # DL-census op de PRE-inference graph (TBox-constructies, asserted)
    print("→ DL-construct-census (pre-inference TBox)...")
    census = dl_construct_census(g)
    print(f"  Divergentie-risico constructies (rl_complete=False, count>0): "
          f"{len(census['_divergence_risico_constructs'])} soorten, "
          f"{census['_divergence_construct_count_total']} voorkomens")

    print("→ Canonieke OWL RL-closure toepassen...")
    apply_canonical_owlrl(g)
    post_triples = len(g)
    print(f"Post-inference triples: {post_triples} (Δ +{post_triples - pre_triples})")

    print(f"→ Inferred graph exporteren naar TTL...")
    OUT_TTL.parent.mkdir(parents=True, exist_ok=True)
    g.serialize(destination=str(OUT_TTL), format="turtle")
    print(f"  ✓ {OUT_TTL} ({post_triples} triples)")

    payload = {
        "meta": {
            "purpose": "H38-evaluatie owlrl-zijde — DL-construct-census + inferred-TTL-export voor diff tegen HermiT",
            "measured_at_utc": datetime.now(timezone.utc).isoformat(),
            "config": {"profile": "OWL RL canoniek",
                       "axiomatic_triples": False, "datatype_axioms": False},
            "workdir": str(WORKDIR),
            "pre_inference_triples": pre_triples,
            "post_inference_owlrl_triples": post_triples,
            "post_minus_pre": post_triples - pre_triples,
            "inferred_ttl_export": str(OUT_TTL),
            "tool_versions": {
                "rdflib": __import__("rdflib").__version__,
                "owlrl": __import__("owlrl").__version__,
            },
        },
        "dl_construct_census": census,
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    print(f"  ✓ {OUT_JSON}")

    print("\n--- DIVERGENTIE-RISICO (OWL RL vs HermiT, voorspelling) ---")
    if not census["_divergence_risico_constructs"]:
        print("  GEEN OWL RL-onvolledige constructies aangetroffen met count>0.")
        print("  → Verwachting: HermiT-delta uitsluitend RDF/OWL-housekeeping (geen model-semantische delta).")
    else:
        for c in census["_divergence_risico_constructs"]:
            print(f"  {c['count']:>4}  {c['construct']}")


if __name__ == "__main__":
    main()
