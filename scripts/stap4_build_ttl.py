#!/usr/bin/env python3
"""Stap 4 v4.5.0 builder: 363 Implementation Examples naar m21-csf.ttl."""
import json
from pathlib import Path

examples = json.loads(Path("/home/claude/csf_examples.json").read_text())


def sub_to_iri(sub_code: str) -> str:
    return f"csf:{sub_code.replace('.', '_').replace('-', '_')}"


def example_iri(sub_code: str, ex_num: int) -> str:
    return f"{sub_to_iri(sub_code)}_Ex{ex_num}"


def ttl_literal(s, lang=None):
    assert '"' not in s, f"Unexpected double quote in: {s[:50]}"
    return f'"{s}"@{lang}' if lang else f'"{s}"'


ttl = ["""
# =============================================================================
# v4.5.0 Fase 3 — Stap 4: Implementation Examples
# Datum: 2026-05-19
# =============================================================================
# 363 Implementation Examples uit CSF_2_0-Implementation_Examples.xlsx Sheet1.
# Daadwerkelijk geparsed: 363 (XLSX bevat 386 rijen; 22 zijn Function/Category-
# headers zonder Example-data; 1 is column-header).
#
# Per IE-individual:
#   - rdf:type csf:ImplementationExample, owl:NamedIndividual
#   - rdfs:label "<Subcat>.Ex<N>"@nl/@en (taal-neutrale ID-form)
#   - rdfs:comment @en (letterlijke Example-tekst uit NIST CSF 2.0 — geen NL-vertaling
#     conform D6 vertaling-scope-uitbreiding: lange normatieve tekst @en-only)
#   - csf:csfIdentifier "<Subcat>.Ex<N>" (bv. GV.OC-01.Ex1)
#   - csf:exemplifies <Subcategory-individual>
#   - ext:isComponentOf fw:NIST_CSF_2_0
#   - ext:sourceAttribution ext:Attr_NIST_CSF_2_0_Core_2024
#
# IRI-conventie: csf:<FUNC>_<CAT>_<NN>_Ex<N> — geen zfill op N (max=10 voor GV.SC-05).
"""]

ttl.append(f"\n# --- {len(examples)} Implementation Examples ---\n")
for e in examples:
    iri = example_iri(e["subcategory_code"], e["example_num"])
    parent_iri = sub_to_iri(e["subcategory_code"])
    label_str = f"{e['subcategory_code']}.{e['example_id']}"
    full_id = e["full_id"]
    
    ttl.append(f"""{iri}
    rdf:type csf:ImplementationExample , owl:NamedIndividual ;
    rdfs:label {ttl_literal(label_str, 'nl')} , {ttl_literal(label_str, 'en')} ;
    rdfs:comment {ttl_literal(e['text'], 'en')} ;
    csf:csfIdentifier {ttl_literal(full_id)} ;
    csf:exemplifies {parent_iri} ;
    ext:isComponentOf fw:NIST_CSF_2_0 ;
    ext:sourceAttribution ext:Attr_NIST_CSF_2_0_Core_2024 .
""")

block = "\n".join(ttl)
m21_path = Path("/home/claude/v433/m21-csf.ttl")
current = m21_path.read_text()
m21_path.write_text(current + block)
print(f"✓ Block appended to m21-csf.ttl ({len(block):,} chars)")
print(f"  Implementation Examples: {len(examples)}")
print(f"  Highest Ex-num: {max(e['example_num'] for e in examples)}")
