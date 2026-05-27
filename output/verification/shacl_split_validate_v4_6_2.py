#!/usr/bin/env python3
"""shacl_split_validate_v4_6_2.py — gesplitste SHACL-validatie v4.6.2.

Output-bestand: output/verification/shacl_results_v4_6_2.json.

SECTIE A (RUN 1, inference='none'):
  ctrl/bio ISO27002NamingShape, HandreikingBBNValueShape, asset:NamespaceShape
  -> verwacht 0 violations
SECTIE B (RUN 2, inference='owlrl'):
  AppliesToAssetTypeRangeShape, BVASymmetryShape, OrphanClassShape
  -> verwacht 290 false-positives op SECTIE A-shapes (bekend fenomeen baseline,
     identiek aan v4.6.1)

T2-patch v4.6.2 muteert 65 SKOS-predicates in m10-nis2-ext.ttl (32 closeMatch
-> broadMatch downgrades + 33 relatedMatch -> broadMatch upgrades). Geen van
de actieve shapes valideert direct op ctrl:<->compl:-mapping-distributie
(SHACL-blinde vlek op deze cluster, conform T1 Vraag D-inventarisatie en
T2 §3.2 stop-conditie-analyse). Verwachting: identieke violation-counts
t.o.v. v4.6.1.
"""
import sys
import json
import os
from collections import Counter
from pathlib import Path

from rdflib import Graph, URIRef
from rdflib.namespace import Namespace, RDF
from pyshacl import validate

REPO_ROOT = Path(__file__).resolve().parents[2]
WORKDIR = Path(os.environ.get("GRC_WORKDIR", REPO_ROOT / "ontology"))
SHAPES_FILE = WORKDIR / "grc-shacl.ttl"
OUTPUT_PATH = REPO_ROOT / "output" / "verification" / "shacl_results_v4_6_2.json"

SH = Namespace("http://www.w3.org/ns/shacl#")

# Shape-classificatie (T1-precedent + v4.6.2-instructie §5.1)
SECTION_A_SHAPES = {
    "https://grc.example.org/control/ISO27002NamingShape",
    "https://grc.example.org/bio/ISO27002NamingShape",
    "https://grc.example.org/control/HandreikingBBNValueShape",
    "https://grc.example.org/asset/NamespaceShape",
}
SECTION_B_SHAPES = {
    "https://grc.example.org/asset/AppliesToAssetTypeRangeShape",
    "https://grc.example.org/asset/BVASymmetryShape",
    "https://grc.example.org/asset/OrphanClassShape",
}


def build_subset_shapes(full_shapes: Graph, keep_shape_iris: set[str]) -> Graph:
    """Maak een subset shapes-graph met alleen de gespecificeerde sh:NodeShape's.

    Behoudt alle triples die uitgaan van of bereikbaar zijn via de meegegeven
    shape-IRI's (incl. property-shape-blanks). T1-precedent leverde dit niet;
    v4.6.2 voegt het toe voor expliciete SECTIE B-meting conform instructie §5.1.
    """
    subset = Graph()
    # Kopieer namespace-prefixen
    for prefix, ns in full_shapes.namespaces():
        subset.bind(prefix, ns)
    # Kopieer alle triples die uitgaan van behouden shape-IRI's,
    # inclusief geneste blanknode-property-shapes via CBD-achtige traversal.
    visited = set()
    to_visit = [URIRef(iri) for iri in keep_shape_iris]
    while to_visit:
        node = to_visit.pop()
        if node in visited:
            continue
        visited.add(node)
        for p, o in full_shapes.predicate_objects(node):
            subset.add((node, p, o))
            # Volg blank nodes voor property-shapes
            if not isinstance(o, URIRef) and o not in visited:
                to_visit.append(o)
    return subset


def count_violations(report_text: str) -> tuple[bool, int, dict[str, int]]:
    """Parse een SHACL-rapport en tel violations per source-shape."""
    rg = Graph()
    rg.parse(data=report_text, format="turtle")
    violations = list(rg.subjects(SH.resultSeverity, SH.Violation))
    per_shape: Counter = Counter()
    for v in violations:
        for shape in rg.objects(v, SH.sourceShape):
            per_shape[str(shape)] += 1
    # Conformance: alleen True als er 0 violations zijn.
    return len(violations) == 0, len(violations), dict(per_shape)


# Bouw data-graph (21 .ttl-modules; grc-shacl.ttl uitgesloten)
data = Graph()
for fp in sorted(p for p in WORKDIR.iterdir()
                 if p.suffix == ".ttl" and p.name != "grc-shacl.ttl"):
    data.parse(fp, format="turtle")

shapes = Graph()
shapes.parse(SHAPES_FILE, format="turtle")

print(f"Data triples: {len(data)}, Shapes triples: {len(shapes)}")

# Subset shapes-graphs voor expliciete SECTIE A / SECTIE B metingen
shapes_a = build_subset_shapes(shapes, SECTION_A_SHAPES)
shapes_b = build_subset_shapes(shapes, SECTION_B_SHAPES)
print(f"SECTIE A shapes triples: {len(shapes_a)} ({len(SECTION_A_SHAPES)} shapes)")
print(f"SECTIE B shapes triples: {len(shapes_b)} ({len(SECTION_B_SHAPES)} shapes)")

results = {}

# --- SECTIE A: inference='none' (T1-precedent RUN 1) ---
print("\n--- SECTIE A: inference='none' (verwacht 0 violations) ---")
_, report_a_text, _ = validate(
    data, shacl_graph=shapes_a, inference='none', advanced=True,
    serialize_report_graph='turtle', meta_shacl=False,
)
conforms_a, n_a, per_shape_a = count_violations(report_a_text)
print(f"Conforms: {conforms_a}")
print(f"Violations: {n_a}")
results["section_a_none"] = {
    "description": "SECTIE A (ctrl/bio ISO27002NamingShape, HandreikingBBNValueShape, asset:NamespaceShape) onder inference='none'",
    "inference": "none",
    "shapes": sorted(SECTION_A_SHAPES),
    "conforms": conforms_a,
    "violations": n_a,
    "violations_per_shape": per_shape_a,
}

# --- SECTIE B: inference='owlrl' (subset shapes, expliciet v4.6.2-instructie §5.1) ---
print("\n--- SECTIE B: inference='owlrl' (verwacht 0 violations) ---")
_, report_b_text, _ = validate(
    data, shacl_graph=shapes_b, inference='owlrl', advanced=True,
    serialize_report_graph='turtle', meta_shacl=False,
)
conforms_b, n_b, per_shape_b = count_violations(report_b_text)
print(f"Conforms: {conforms_b}")
print(f"Violations: {n_b}")
results["section_b_owlrl"] = {
    "description": "SECTIE B (AppliesToAssetTypeRangeShape, BVASymmetryShape, OrphanClassShape) onder inference='owlrl'",
    "inference": "owlrl",
    "shapes": sorted(SECTION_B_SHAPES),
    "conforms": conforms_b,
    "violations": n_b,
    "violations_per_shape": per_shape_b,
}

# --- COMBINED: inference='owlrl' (T1-precedent RUN 2) ---
print("\n--- COMBINED: inference='owlrl' (verwacht 290 bekende false-positives) ---")
_, report_c_text, _ = validate(
    data, shacl_graph=shapes, inference='owlrl', advanced=True,
    serialize_report_graph='turtle', meta_shacl=False,
)
conforms_c, n_c, per_shape_c = count_violations(report_c_text)
print(f"Conforms: {conforms_c}")
print(f"Violations totaal: {n_c}")
print("Violations per sourceShape:")
for s, n in sorted(per_shape_c.items(), key=lambda kv: -kv[1]):
    print(f"  {n:>4}  {s}")
results["combined_owlrl"] = {
    "description": "Volledige shapes-set onder inference='owlrl' (T1-precedent RUN 2)",
    "inference": "owlrl",
    "shapes": sorted(SECTION_A_SHAPES | SECTION_B_SHAPES),
    "conforms": conforms_c,
    "violations_total": n_c,
    "violations_per_shape": per_shape_c,
    "baseline_v4_6_1": 290,
    "delta_vs_v4_6_1": n_c - 290,
}

# T1-precedent-veld voor backward-compat met v4.6.1-rapport-structuur
results["run1_none"] = {
    "conforms": conforms_a,
    "violations": n_a,
    "violations_per_shape": per_shape_a,
}
results["run2_owlrl"] = {
    "conforms": conforms_c,
    "violations_total": n_c,
    "violations_per_shape": per_shape_c,
}

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_PATH.write_text(json.dumps(results, indent=2))
print(f"\nSaved {OUTPUT_PATH}")
print(f"\n--- KERNSAMENVATTING ---")
print(f"SECTIE A (none):       {n_a:>4} violations (verwacht 0)")
print(f"SECTIE B (owlrl):      {n_b:>4} violations (verwacht 0)")
print(f"COMBINED (owlrl):      {n_c:>4} violations (verwacht 290, Δ vs v4.6.1 = {n_c - 290})")
