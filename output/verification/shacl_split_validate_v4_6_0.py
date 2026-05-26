#!/usr/bin/env python3
"""shacl_split_validate_v4.6.0.py — gesplitste SHACL-validatie."""
import sys, json
from pathlib import Path
from rdflib import Graph
from pyshacl import validate

WORKDIR = Path("/home/claude/v433")
SHAPES_FILE = WORKDIR / "grc-shacl.ttl"

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
n_violations_a = text_a.count("sh:violation") + text_a.count("Severity: sh:Violation")
# Better count via report graph:
from rdflib.namespace import Namespace
SH = Namespace("http://www.w3.org/ns/shacl#")
report_g = Graph()
report_g.parse(data=report_a, format='turtle')
violations_a = list(report_g.subjects(SH.resultSeverity, SH.Violation))
print(f"Violations in RUN 1: {len(violations_a)}")
results["run1_none"] = {
    "conforms": conforms_a,
    "violations": len(violations_a),
}

# RUN 2 — SECTIE B: inference='owlrl'
print("\n--- RUN 2: inference='owlrl' (verwacht 0 violations op SECTIE B; SECTIE A geeft false-positives) ---")
conforms_b, report_b, text_b = validate(
    data, shacl_graph=shapes, inference='owlrl', advanced=True,
    serialize_report_graph='turtle', meta_shacl=False,
)
print(f"Conforms: {conforms_b}")
report_g2 = Graph()
report_g2.parse(data=report_b, format='turtle')
violations_b = list(report_g2.subjects(SH.resultSeverity, SH.Violation))
print(f"Violations in RUN 2 (totaal): {len(violations_b)}")

# Verdeel violations RUN 2 over shape-IDs
from collections import Counter
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

# Save
Path("/home/claude/shacl_results_v4.6.0.json").write_text(json.dumps(results, indent=2))
print(f"\n✓ Saved /home/claude/shacl_results_v4.6.0.json")
