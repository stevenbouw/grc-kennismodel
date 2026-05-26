#!/usr/bin/env python3
"""
apply_patch_v4_6_1.py — SKOS-herclassificatie patch v4.6.1 (scenario C)

Vervangt 28 ctrl:ISO27002_* skos:exactMatch compl:NIS2_Art21_*
door skos:broadMatch in ontology/m10-nis2-ext.ttl.

Uitvoering vanuit grc-kennismodel-root:
    python3 apply_patch_v4_6_1.py

Veilig: maakt backup vóór wijziging; faalt netjes als getallen niet kloppen.
"""

from pathlib import Path
import re
import sys

# 28 paren — scenario C (26 zekere + 2 edge-cases)
PAIRS = [
    # Cluster a (1)
    ("ctrl:ISO27002_5_01", "compl:NIS2_Art21_a"),
    # Cluster b (4)
    ("ctrl:ISO27002_5_24", "compl:NIS2_Art21_b"),
    ("ctrl:ISO27002_5_25", "compl:NIS2_Art21_b"),
    ("ctrl:ISO27002_5_26", "compl:NIS2_Art21_b"),
    ("ctrl:ISO27002_5_27", "compl:NIS2_Art21_b"),
    # Cluster c (3)
    ("ctrl:ISO27002_5_29", "compl:NIS2_Art21_c"),
    ("ctrl:ISO27002_5_30", "compl:NIS2_Art21_c"),
    ("ctrl:ISO27002_8_13", "compl:NIS2_Art21_c"),
    # Cluster d (4)
    ("ctrl:ISO27002_5_19", "compl:NIS2_Art21_d"),
    ("ctrl:ISO27002_5_20", "compl:NIS2_Art21_d"),
    ("ctrl:ISO27002_5_21", "compl:NIS2_Art21_d"),
    ("ctrl:ISO27002_5_22", "compl:NIS2_Art21_d"),
    # Cluster e (5)
    ("ctrl:ISO27002_8_25", "compl:NIS2_Art21_e"),
    ("ctrl:ISO27002_8_26", "compl:NIS2_Art21_e"),
    ("ctrl:ISO27002_8_27", "compl:NIS2_Art21_e"),
    ("ctrl:ISO27002_8_28", "compl:NIS2_Art21_e"),
    ("ctrl:ISO27002_8_29", "compl:NIS2_Art21_e"),
    # Cluster f (2)
    ("ctrl:ISO27002_5_35", "compl:NIS2_Art21_f"),
    ("ctrl:ISO27002_5_36", "compl:NIS2_Art21_f"),
    # Cluster g (1)
    ("ctrl:ISO27002_6_03", "compl:NIS2_Art21_g"),
    # Cluster h (1) — edge-case
    ("ctrl:ISO27002_8_24", "compl:NIS2_Art21_h"),
    # Cluster i (6)
    ("ctrl:ISO27002_5_09", "compl:NIS2_Art21_i"),
    ("ctrl:ISO27002_5_15", "compl:NIS2_Art21_i"),
    ("ctrl:ISO27002_5_16", "compl:NIS2_Art21_i"),
    ("ctrl:ISO27002_5_18", "compl:NIS2_Art21_i"),
    ("ctrl:ISO27002_6_01", "compl:NIS2_Art21_i"),
    ("ctrl:ISO27002_6_02", "compl:NIS2_Art21_i"),
    # Cluster j (1) — edge-case
    ("ctrl:ISO27002_8_05", "compl:NIS2_Art21_j"),
]

assert len(PAIRS) == 28, f"Verwacht 28 paren, code heeft er {len(PAIRS)}"

INPUT = Path("ontology/m10-nis2-ext.ttl")
BACKUP = Path("ontology/m10-nis2-ext.ttl.v4_6_0.bak")

if not INPUT.exists():
    sys.exit(f"FOUT: {INPUT} niet gevonden — run vanuit grc-kennismodel-root")

# Backup vóór wijziging
if not BACKUP.exists():
    BACKUP.write_text(INPUT.read_text())
    print(f"✓ Backup gemaakt: {BACKUP}")
else:
    print(f"⚠  Backup bestaat al: {BACKUP} (niet overschreven)")

content = INPUT.read_text()
exact_before = content.count("skos:exactMatch")
print(f"\nPre-patch m10: {exact_before} totaal skos:exactMatch")

# Per paar: gerichte vervanging
# Pattern: subject + iets-binnen-blok + skos:exactMatch + obj
# [^.]*? blijft binnen één Turtle-blok (blokken eindigen met .)
mutations = 0
not_found = []
multiple = []

for subject, obj in PAIRS:
    pattern = re.compile(
        rf'({re.escape(subject)}[^.]*?)skos:exactMatch(\s+{re.escape(obj)}\b)'
    )
    new_content, n = pattern.subn(r'\1skos:broadMatch\2', content)
    if n == 1:
        content = new_content
        mutations += 1
    elif n == 0:
        not_found.append((subject, obj))
    else:
        multiple.append((subject, obj, n))

# Resultaat
print(f"\nMutaties uitgevoerd: {mutations} / 28")

if not_found:
    print("\n✗ Niet gevonden (in m10):")
    for s, o in not_found:
        print(f"   {s} → {o}")

if multiple:
    print("\n!  Meerdere matches per paar (handmatig checken):")
    for s, o, n in multiple:
        print(f"   {s} → {o} ({n} matches)")

if mutations != 28:
    sys.exit("\n✗ STOP: niet alle 28 mutaties succesvol. Bestand NIET overschreven.")

# Sanity-check totaal
exact_after = content.count("skos:exactMatch")
expected_after = exact_before - 28

if exact_after != expected_after:
    sys.exit(
        f"\n✗ STOP: exactMatch-telling klopt niet "
        f"({exact_after} vs verwacht {expected_after}). Bestand NIET overschreven."
    )

# Schrijf weg
INPUT.write_text(content)

print(f"\n{'=' * 60}")
print(f"✓ Patch v4.6.1 toegepast (scenario C — alle 28 broadMatch)")
print(f"{'=' * 60}")
print(f"  m10 skos:exactMatch: {exact_before} → {exact_after} (Δ −28)")
print(f"  Backup beschikbaar:  {BACKUP}")
print(f"\nVolgende stappen:")
print(f"  1. python3 output/verification/canonical_metrics_v4_6_1.py")
print(f"  2. python3 output/verification/shacl_split_validate_v4_6_1.py")
print(f"  3. shasum -a 256 ontology/m10-nis2-ext.ttl")
print(f"     # Verwacht hash: cb2d567b184877e111800cc0a8af1e38d6d6f74ddca0477ee1a52df1d8afa2f1")
print(f"\nBij groene checks: commit + push conform eerdere instructie.")
print(f"Bij rode check: vergelijk met backup ({BACKUP}) en escalleer naar masterchat.")
