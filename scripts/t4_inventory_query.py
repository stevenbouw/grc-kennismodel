#!/usr/bin/env python3
"""
T4 pre-sprint-inventarisatie — READ-ONLY analyse-helper (geen mutatie).
Stelt vast (Protocol 1): csf:Subcategory <-> ISO 27001-mappings, predicate-distributie,
provenance (overlap- vs divergentie-set), categorie-typen van de ISO-eindpunten.
Meet-laag: ONTOLOGIE-LAAG (rdflib parse, inference='none' — geen OWL-RL).
"""
import glob
from collections import defaultdict, Counter
import rdflib
from rdflib import Namespace, RDF
from rdflib.namespace import SKOS, RDFS

CSF  = Namespace("https://grc.example.org/csf/")
EXT  = Namespace("https://grc.example.org/extended/")
CTRL = Namespace("https://grc.example.org/control/")
COMPL= Namespace("https://grc.example.org/compliance/")
FW   = Namespace("https://grc.example.org/framework/")

SKOS_PREDS = [SKOS.exactMatch, SKOS.closeMatch, SKOS.broadMatch,
              SKOS.narrowMatch, SKOS.relatedMatch]
SRC_ATTR = EXT.sourceAttribution

g = rdflib.Graph()
for f in sorted(glob.glob("ontology/*.ttl")):
    g.parse(f, format="turtle")
print(f"# Modules geparsed: {len(glob.glob('ontology/*.ttl'))}  | triples (pre-inf): {len(g)}")

def local(uri):
    s = str(uri)
    return s.rsplit("/", 1)[-1] if "/" in s else s

def ns_of(uri):
    s = str(uri)
    for pfx, n in [("csf",CSF),("ext",EXT),("ctrl",CTRL),("compl",COMPL),("fw",FW)]:
        if s.startswith(str(n)): return pfx
    return "other"

def is_iso27001(uri):
    return local(uri).startswith("ISO27001")

# --- 1. Alle SKOS-mappings met csf-subject; isoleer csf <-> ISO27001 ---
csf_iso_pairs = []          # (subj, pred, obj)
csf_all_by_target_ns = Counter()
for pred in SKOS_PREDS:
    for s, o in g.subject_objects(pred):
        if ns_of(s) == "csf":
            csf_all_by_target_ns[(ns_of(o), local(pred))] += 1
            if is_iso27001(o):
                csf_iso_pairs.append((s, pred, o))
        # ook andersom (ISO27001-subject -> csf), volledigheid
        if is_iso27001(s) and ns_of(o) == "csf":
            csf_iso_pairs.append((s, pred, o))

print("\n## 1. csf-SKOS-mappings per doel-namespace::predicate (ontologie-laag)")
for k in sorted(csf_all_by_target_ns):
    print(f"   csf -> {k[0]:6s} :: {k[1]:12s} = {csf_all_by_target_ns[k]}")

print(f"\n## 1b. csf <-> ISO27001-mapping-paren totaal: {len(csf_iso_pairs)}")
pred_dist = Counter(local(p) for _, p, _ in csf_iso_pairs)
print("   predicate-distributie:", dict(pred_dist))

# --- 2. Categorie-type van ISO27001-eindpunten ---
print("\n## 2. Categorie-type ISO27001-eindpunten (rdf:type)")
iso_types = Counter()
iso_endpoints = set()
for s, p, o in csf_iso_pairs:
    iso = s if is_iso27001(s) else o
    iso_endpoints.add(iso)
for iso in iso_endpoints:
    for t in g.objects(iso, RDF.type):
        if t != rdflib.OWL.NamedIndividual:
            iso_types[local(t)] += 1
print("   distinct ISO27001-eindpunten in csf-mappings:", len(iso_endpoints))
print("   types:", dict(iso_types))

# --- 3. Provenance: sourceAttribution per mapping-eindpunt ---
# Attributie staat op individuals (subject/object), niet op de triple.
# We inspecteren beide eindpunten + tellen distinct attributions.
print("\n## 3. Provenance — sourceAttribution op de mapping-eindpunten")
attr_names = Counter()
overlap, single, none_attr = 0, 0, 0
pair_detail = []
for s, p, o in csf_iso_pairs:
    attrs = set(g.objects(s, SRC_ATTR)) | set(g.objects(o, SRC_ATTR))
    for a in attrs:
        attr_names[local(a)] += 1
    n = len(attrs)
    if n == 0: none_attr += 1
    elif n == 1: single += 1
    else: overlap += 1
    pair_detail.append((local(s), local(p), local(o), sorted(local(a) for a in attrs)))
print(f"   paren met >=2 distinct attributions (machine-detecteerbare overlap): {overlap}")
print(f"   paren met exact 1 attribution: {single}")
print(f"   paren met 0 attribution-triples op eindpunten: {none_attr}")
print("   voorkomende attribution-individuals (telt mapping-eindpunt-incidenties):")
for a, c in attr_names.most_common():
    print(f"      {a}: {c}")

# --- 4. sample mapping-detail (eerste 8) ---
print("\n## 4. Sample (eerste 8 csf<->ISO27001-paren) — subj | pred | obj | attrs")
for row in pair_detail[:8]:
    print(f"   {row[0]:16s} {row[1]:12s} {row[2]:16s} {row[3]}")

# --- 5. Hoe wordt bron-overlap feitelijk vastgelegd? comment-scan ---
print("\n## 5. Mapping-bron-vastlegging: comments met 'Sheet 8' / 'Reference Tool' / 'ADR'?")
import re
hits = Counter()
for f in ["ontology/m21-csf.ttl", "ontology/m09-iso27001-ext.ttl"]:
    txt = open(f, encoding="utf-8").read()
    for key in ["Sheet 8", "Sheet8", "Reference Tool", "ADR", "NOREA", "CSF Reference"]:
        hits[(f.split('/')[-1], key)] = len(re.findall(re.escape(key), txt))
for k, v in hits.items():
    if v: print(f"   {k[0]}: '{k[1]}' x{v}")
