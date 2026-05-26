#!/usr/bin/env python3
"""shacl_split_validate_v4_6_1.py — gesplitste SHACL-validatie v4.6.1.

Gebruikt repo-root resolutie i.p.v. hardcoded /home/claude/v433-pad.
Output-bestand: output/verification/shacl_results_v4_6_1.json.

SECTIE A (RUN 1, inference='none'):
  ctrl/bio ISO27002NamingShape, HandreikingBBNValueShape, asset:NamespaceShape
  → verwacht 0 violations
SECTIE B (RUN 2, inference='owlrl'):
  AppliesToAssetTypeRangeShape, BVASymmetryShape, OrphanClassShape
  → verwacht 290 false-positives op SECTIE A-shapes (bekend fenomeen baseline)

Predicate-mutatie 28× exactMatch → broadMatch raakt geen van bovenstaande
shapes (SHACL-blinde vlek op ctrl:↔compl:-mappings, conform Vraag D
inventarisatie). Verwachting: identieke violation-counts t.o.v. v4.6.0.
"""
import sys
import json
import os
from collections import Counter
from pathlib import Path

from rdflib import Graph
from rdflib.namespace import Namespace
from pyshacl import validate

REPO_ROOT = Path(__file__).resolve().parents[2]
WORKDIR = Path(os.environ.get("GRC_WORKDIR", REPO_ROOT / "ontology"))
SHAPES_FILE = WORKDIR / "grc-shacl.ttl"
OUTPUT_PATH = REPO_ROOT / "output" / "verification" / "shacl_results_v4_6_1.json"

SH = Namespace("http://www.w3.org/ns/shacl#")

# Bouw data-graph
data = Graph()
for fp in sorted(p for p in WORKDIR.iterdir()
                 if p.suffix == ".ttl" and p.name != "grc-shacl.ttl"):
    data.parse(fp, format="turtle")

shapes = Graph()
shapes.parse(SHAPES_FILE, format="turtle")

print(f"Data triples: {len(data)}, Shapes triples: {len(shapes)}")

results = {}

# RUN 1 — SECTIE A: inference='none'
print("\n--- RUN 1: inference='none' (verwacht 0 violations op SECTIE A) ---")
conforms_a, report_a, text_a = validate(
    data, shacl_graph=shapes, inference='none', advanced=True,
    serialize_report_graph='turtle', meta_shacl=False,
)
print(f"Conforms: {conforms_a}")
report_g = Graph()
report_g.parse(data=report_a, format='turtle')
violations_a = list(report_g.subjects(SH.resultSeverity, SH.Violation))
print(f"Violations in RUN 1: {len(violations_a)}")
v_per_shape_a: Counter = Counter()
for v in violations_a:
    for shape in report_g.objects(v, SH.sourceShape):
        v_per_shape_a[str(shape)] += 1
results["run1_none"] = {
    "conforms": conforms_a,
    "violations": len(violations_a),
    "violations_per_shape": {k: v for k, v in v_per_shape_a.items()},
}

# RUN 2 — SECTIE B: inference='owlrl'
print("\n--- RUN 2: inference='owlrl' (verwacht 290 false-positives op SECTIE A) ---")
conforms_b, report_b, text_b = validate(
    data, shacl_graph=shapes, inference='owlrl', advanced=True,
    serialize_report_graph='turtle', meta_shacl=False,
)
print(f"Conforms: {conforms_b}")
report_g2 = Graph()
report_g2.parse(data=report_b, format='turtle')
violations_b = list(report_g2.subjects(SH.resultSeverity, SH.Violation))
print(f"Violations in RUN 2 (totaal): {len(violations_b)}")

v_per_shape: Counter = Counter()
for v in violations_b:
    for shape in report_g2.objects(v, SH.sourceShape):
        v_per_shape[str(shape)] += 1
print("Violations RUN 2 per sourceShape:")
for s, n in v_per_shape.most_common():
    print(f"  {n:>4}  {s}")
results["run2_owlrl"] = {
    "conforms": conforms_b,
    "violations_total": len(violations_b),
    "violations_per_shape": {k: v for k, v in v_per_shape.items()},
}

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_PATH.write_text(json.dumps(results, indent=2))
print(f"\n✓ Saved {OUTPUT_PATH}")
