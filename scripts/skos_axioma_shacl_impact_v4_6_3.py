#!/usr/bin/env python3
"""skos_axioma_shacl_impact_v4_6_3.py — H41 stap 3: SHACL-impact SKOS-axiomas.

EVALUATIE-script. Wijzigt niets aan de canonieke SHACL-baseline. Meet of het
activeren van SKOS-axiomas (vergelijkenderwijs) de combined-mode violation-count
verschuift t.o.v. de bekende 290-false-positive-baseline (v4.6.2 == v4.6.3).

Drie runs (allemaal full shapes-set, advanced=True):
  1. COMBINED baseline    : data + shapes, inference='owlrl'        -> verwacht 290
  2. COMBINED + SKOS-axiomas: (data + SKOS-axioma-graph) + shapes, inference='owlrl'
  3. Δ per sourceShape

Output: output/verification/skos_axioma_shacl_impact_v4_6_3.json (niet-canoniek).
"""
from __future__ import annotations

import json
import os
from collections import Counter
from pathlib import Path
from datetime import datetime, timezone

from rdflib import Graph, URIRef
from rdflib.namespace import Namespace
from pyshacl import validate

REPO_ROOT = Path(__file__).resolve().parents[1]
WORKDIR = Path(os.environ.get("GRC_WORKDIR", REPO_ROOT / "ontology"))
SHAPES_FILE = WORKDIR / "grc-shacl.ttl"
OUT_JSON = REPO_ROOT / "output" / "verification" / "skos_axioma_shacl_impact_v4_6_3.json"
SH = Namespace("http://www.w3.org/ns/shacl#")

SKOS_AXIOMS_TTL = """
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
skos:exactMatch   a owl:SymmetricProperty , owl:TransitiveProperty .
skos:closeMatch   a owl:SymmetricProperty .
skos:relatedMatch a owl:SymmetricProperty .
skos:broadMatch   owl:inverseOf skos:narrowMatch .
skos:exactMatch   rdfs:subPropertyOf skos:closeMatch .
"""


def build_data() -> Graph:
    g = Graph()
    for fp in sorted(p for p in WORKDIR.iterdir()
                     if p.suffix == ".ttl" and p.name != "grc-shacl.ttl"):
        g.parse(fp, format="turtle")
    return g


def count_violations(report_text: str):
    rg = Graph()
    rg.parse(data=report_text, format="turtle")
    viols = list(rg.subjects(SH.resultSeverity, SH.Violation))
    per_shape: Counter = Counter()
    for v in viols:
        for shape in rg.objects(v, SH.sourceShape):
            per_shape[str(shape)] += 1
    return len(viols), dict(per_shape)


def run(data: Graph, shapes: Graph):
    _, rpt, _ = validate(data, shacl_graph=shapes, inference='owlrl',
                         advanced=True, serialize_report_graph='turtle',
                         meta_shacl=False)
    return count_violations(rpt)


def main():
    print(f"=== skos_axioma_shacl_impact_v4_6_3 (H41 stap 3) — "
          f"{datetime.now(timezone.utc).isoformat()} ===")
    shapes = Graph(); shapes.parse(SHAPES_FILE, format="turtle")

    print("→ Run 1: COMBINED baseline (verwacht 290)...")
    data1 = build_data()
    n1, per1 = run(data1, shapes)
    print(f"  violations: {n1}")

    print("→ Run 2: COMBINED + SKOS-axiomas...")
    data2 = build_data()
    data2.parse(data=SKOS_AXIOMS_TTL, format="turtle")
    n2, per2 = run(data2, shapes)
    print(f"  violations: {n2}")

    all_shapes = set(per1) | set(per2)
    delta_per_shape = {s: per2.get(s, 0) - per1.get(s, 0) for s in all_shapes}
    delta_per_shape = {s: d for s, d in sorted(delta_per_shape.items(),
                       key=lambda kv: -abs(kv[1])) if d != 0}

    payload = {
        "meta": {
            "purpose": "H41 SHACL-impact SKOS-axiomas — vergelijkend, geen baseline-wijziging",
            "measured_at_utc": datetime.now(timezone.utc).isoformat(),
            "baseline_known_false_positives": 290,
            "tool_versions": {"rdflib": __import__("rdflib").__version__,
                              "pyshacl": __import__("pyshacl").__version__},
        },
        "combined_baseline": {"violations_total": n1,
                              "delta_vs_known_290": n1 - 290,
                              "violations_per_shape": per1},
        "combined_with_skos_axioms": {"violations_total": n2,
                                      "violations_per_shape": per2},
        "delta_skos_axioms_minus_baseline": {
            "violations_total": n2 - n1,
            "per_shape": delta_per_shape},
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    print(f"\n✓ {OUT_JSON}")
    print(f"\n--- KERNSAMENVATTING ---")
    print(f"COMBINED baseline       : {n1} (Δ vs bekende 290 = {n1 - 290})")
    print(f"COMBINED + SKOS-axiomas : {n2} (Δ vs baseline = {n2 - n1})")
    if delta_per_shape:
        print("Δ per shape:")
        for s, d in delta_per_shape.items():
            print(f"   {d:+5d}  {s}")
    else:
        print("Geen shape-niveau-verschuiving.")


if __name__ == "__main__":
    main()
