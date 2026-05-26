"""
build_grc_explorer_v3.py — GRC Kennismodel v4.6.0
Extraheert individuals, relaties en laag-toewijzingen uit TTL-bestanden
en schrijft grc-data-v4_6_0.js voor grc-explorer.html.

Wijzigingen t.o.v. v2 (build_grc_explorer_v2.py, baseline v4.3.1):

  v4.3.2/v4.3.3:
    - compl:articleRef opgenomen als compliance-edge-categorie
      (vervangt ext:articleNumber in predicate-consolidatie α)

  v4.4.0:
    - ctrl:CBWControl-individuals → laag 2 (Wet/regelgeving)
    - compl:SupplierExclusionOrder → laag 2
    - fw:uitgewerktIn + fw:werktUit toegevoegd aan GOVERNANCE_PROPS
    - ext:hasUVInterpretation opgenomen als enrichment-categorie

  v4.5.0:
    - csf: namespace toegevoegd (11e namespace)
    - csf:Function / Category / Subcategory / ImplementationExample / CSFTier → laag 4
    - CSF-hierarchie-properties: csf:partOfFunction, csf:partOfCategory,
      csf:exemplifies → categorie "csf-hierarchy"
    - ext:isComponentOf nu ook CSF-component-relaties (520 triples)

  v4.6.0:
    - isms:MaturityCapability + subklassen → laag 5 (Audit/Volwassenheid)
    - isms:MaturityCapabilityLevel + isms:CapabilityLevelDescription → laag 5
    - isms:forCapability + isms:atMaturityLevel + isms:hasLevelDescription
      → categorie "maturity"
    - ext:sourceAttribution → categorie "attribution"
    - fw:hasAuditDomain toegevoegd aan GOVERNANCE_PROPS
    - Laag 5-naam uitgebreid: "Audit & Volwassenheid"
    - LAAG_NAMEN[5] bijgewerkt

Auteur: GRC Dashboard-chat
Datum:  21 mei 2026
"""

import os
import json
import hashlib
from datetime import datetime, timezone
from rdflib import Graph, Namespace, RDF, RDFS, OWL, URIRef, Literal
from rdflib.namespace import SKOS, XSD

# ── Namespaces (11, conform D3 v1.9) ────────────────────────────────────────

FW    = Namespace("https://grc.example.org/framework/")
CTRL  = Namespace("https://grc.example.org/control/")
RISK  = Namespace("https://grc.example.org/risk/")
ROLES = Namespace("https://grc.example.org/roles/")
COMPL = Namespace("https://grc.example.org/compliance/")
ISMS  = Namespace("https://grc.example.org/isms/")
BIZ   = Namespace("https://grc.example.org/business/")
BIO   = Namespace("https://grc.example.org/bio/")
EXT   = Namespace("https://grc.example.org/extended/")
ASSET = Namespace("https://grc.example.org/asset/")
CSF   = Namespace("https://grc.example.org/csf/")      # NIEUW v4.5.0

NS_PREFIX = {
    str(FW):    "fw",
    str(CTRL):  "ctrl",
    str(RISK):  "risk",
    str(ROLES): "roles",
    str(COMPL): "compl",
    str(ISMS):  "isms",
    str(BIZ):   "biz",
    str(BIO):   "bio",
    str(EXT):   "ext",
    str(ASSET): "asset",
    str(CSF):   "csf",             # NIEUW v4.5.0
}

GRC_BASE = "https://grc.example.org/"

# Types die schema/TBox zijn — niet exporteren als nodes
SCHEMA_TYPES = {
    OWL.Class, OWL.ObjectProperty, OWL.DatatypeProperty,
    OWL.AnnotationProperty, OWL.TransitiveProperty, OWL.SymmetricProperty,
    OWL.AsymmetricProperty, OWL.FunctionalProperty,
    OWL.InverseFunctionalProperty, OWL.Restriction, OWL.Ontology,
    RDF.Property, RDFS.Class,
    URIRef("http://www.w3.org/ns/shacl#NodeShape"),
    URIRef("http://www.w3.org/ns/shacl#PropertyShape"),
    SKOS.ConceptScheme,
}

# TBox-predicaten — nooit als edges exporteren
TBOX_PREDICATES = {
    RDFS.domain, RDFS.range, RDFS.subClassOf, RDFS.subPropertyOf,
    OWL.equivalentClass, OWL.disjointWith, OWL.complementOf,
    OWL.inverseOf, OWL.onProperty, OWL.allValuesFrom, OWL.someValuesFrom,
    OWL.hasValue, OWL.unionOf, OWL.intersectionOf, OWL.oneOf,
    RDF.type,
}

# ── Governance-properties ─────────────────────────────────────────────────────

GOVERNANCE_PROPS = {
    str(FW.stelVerplicht):         "fw:stelVerplicht",
    str(FW.geeftRichtlijnenVoor):  "fw:geeftRichtlijnenVoor",
    str(FW.geeftITInvullingAan):   "fw:geeftITInvullingAan",
    str(FW.dektAf):                "fw:dektAf",
    str(FW.toetst):                "fw:toetst",
    str(FW.transposedBy):          "fw:transposedBy",
    str(FW.isTranspositieVan):     "fw:isTranspositieVan",
    str(FW.supersedes):            "fw:supersedes",
    str(FW.alignsWith):            "fw:alignsWith",
    str(FW.uitgewerktIn):          "fw:uitgewerktIn",       # NIEUW v4.4.0
    str(FW.werktUit):              "fw:werktUit",           # NIEUW v4.4.0
    str(FW.hasAuditDomain):        "fw:hasAuditDomain",     # NIEUW v4.6.0
    str(EXT.isComponentOf):        "ext:isComponentOf",
    str(CTRL.belongsToFramework):  "ctrl:belongsToFramework",
}

SKOS_PROPS = {
    str(SKOS.exactMatch):   "skos:exactMatch",
    str(SKOS.closeMatch):   "skos:closeMatch",
    str(SKOS.broadMatch):   "skos:broadMatch",
    str(SKOS.narrowMatch):  "skos:narrowMatch",
    str(SKOS.relatedMatch): "skos:relatedMatch",
}

EQUIVALENCE_PROPS = {
    str(OWL.sameAs): "owl:sameAs",
}

# CSF-hierarchie-properties (NIEUW v4.5.0)
CSF_HIERARCHY_PROPS = {
    str(CSF.partOfFunction):  "csf:partOfFunction",
    str(CSF.partOfCategory):  "csf:partOfCategory",
    str(CSF.exemplifies):     "csf:exemplifies",
}

# Maturity-properties (NIEUW v4.6.0)
MATURITY_PROPS = {
    str(ISMS.forCapability):      "isms:forCapability",
    str(ISMS.atMaturityLevel):    "isms:atMaturityLevel",
    str(ISMS.hasLevelDescription):"isms:hasLevelDescription",
}

# Attribution-property (NIEUW v4.6.0)
ATTRIBUTION_PROPS = {
    str(EXT.sourceAttribution): "ext:sourceAttribution",
}

# Enrichment-properties (NIEUW v4.4.0)
ENRICHMENT_PROPS = {
    str(EXT.hasUVInterpretation): "ext:hasUVInterpretation",
}

# Overige inter-individual categorieën
ISMS_PROPS = {
    str(ISMS.hasSoA), str(ISMS.containsEntry), str(ISMS.implementsControl),
    str(ISMS.forSoA), str(ISMS.forRisk),
}
RISK_PROPS  = {str(RISK.mitigatedBy), str(RISK.hasRisk), str(RISK.affectsAsset)}
ASSET_PROPS = {str(ASSET.appliesToAssetType), str(ASSET.hasAssetOwner)}
COMPL_PROPS = {str(COMPL.satisfiedBy), str(COMPL.requiresControl)}

# ── Normenkader-lagen ─────────────────────────────────────────────────────────

LAAG_NAMEN = {
    0: "COSO/Enterprise",
    1: "IT-governance",
    2: "Wet/regelgeving",
    3: "Operationeel (BIO)",
    4: "Normen (ISO/NIST/CSF)",
    5: "Audit & Volwassenheid",   # UITGEBREID v4.6.0: ook volwassenheidsmodel
    9: "ISMS/Bedrijf/Overig",
}

# Lokale namen die isms:-maturity-cluster aanduiden → laag 5
ISMS_MATURITY_TOKENS = (
    "maturity", "capability", "leveldescription", "level_"
)

def bepaal_laag(uri_str):
    local       = get_local(uri_str)
    local_upper = local.upper()
    local_lower = local.lower()
    pfx         = get_prefix(uri_str)

    # Laag 0: COSO / ERM
    if pfx == "fw" and any(k in local_upper for k in ("COSO", "ERM")):
        return 0

    # Laag 1: COBIT / BVA / CIO / roles
    if pfx == "fw" and any(k in local_upper for k in ("COBIT", "BVA", "CIO")):
        return 1
    if pfx == "roles":
        return 1

    # Laag 2: compliance / NIS2 / VIR / CBW / DORA / CBWControl / SupplierExclusion
    if pfx == "compl":
        return 2
    if pfx == "fw" and any(k in local_upper for k in
                           ("NIS2", "VIR", "VIRBI", "AVG", "CBW", "DORA", "CBB")):
        return 2
    if pfx == "ctrl" and "CBW" in local_upper:         # ctrl:CBWControl-individuals
        return 2

    # Laag 3: BIO
    if pfx == "bio":
        return 3
    if pfx == "fw" and "BIO" in local_upper:
        return 3

    # Laag 4: ISO / NIST / IEC / ctrl: / CSF
    if pfx == "ctrl":
        return 4
    if pfx == "csf":                                    # NIEUW v4.5.0
        return 4
    if pfx == "fw" and any(k in local_upper for k in ("ISO", "NIST", "IEC")):
        return 4

    # Laag 5: ENSIA + volwassenheidsmodel (isms:Maturity* / isms:Capability* / isms:Level*)
    if pfx == "fw" and "ENSIA" in local_upper:
        return 5
    if pfx == "isms" and any(tok in local_lower for tok in ISMS_MATURITY_TOKENS):
        return 5

    # Overig
    return 9

# ── Helpers ───────────────────────────────────────────────────────────────────

def get_prefix(uri_str):
    for ns, pfx in NS_PREFIX.items():
        if uri_str.startswith(ns):
            return pfx
    return None

def get_local(uri_str):
    for ns in NS_PREFIX:
        if uri_str.startswith(ns):
            return uri_str[len(ns):]
    return uri_str.split("/")[-1].split("#")[-1]

def make_id(uri_str):
    pfx   = get_prefix(uri_str)
    local = get_local(uri_str)
    return f"{pfx}:{local}" if pfx else local

def get_literal(g, uri, prop, lang=None):
    for val in g.objects(uri, prop):
        if not isinstance(val, Literal):
            continue
        if lang is None:
            return str(val)
        if val.language == lang:
            return str(val)
    return None

def get_label(g, uri):
    """
    Label-opzoek met fallback-keten:
    1. rdfs:label@nl  2. rdfs:label@en  3. ctrl:hasControlTitle@nl
    4. ctrl:hasControlTitle@en  5. rdfs:label (geen taal)
    6. skos:prefLabel  7. IRI-lokale naam
    """
    for lang in ("nl", "en"):
        v = get_literal(g, uri, RDFS.label, lang)
        if v:
            return v, lang
    for lang in ("nl", "en"):
        v = get_literal(g, uri, CTRL.hasControlTitle, lang)
        if v:
            return v, lang
    v = get_literal(g, uri, RDFS.label)
    if v:
        return v, None
    v = get_literal(g, uri, SKOS.prefLabel)
    if v:
        return v, None
    return get_local(str(uri)), None

def is_schema(g, uri):
    return bool(set(g.objects(uri, RDF.type)) & SCHEMA_TYPES)

def get_types(g, uri):
    skip = SCHEMA_TYPES | {OWL.NamedIndividual}
    return [get_local(str(t)) for t in g.objects(uri, RDF.type)
            if isinstance(t, URIRef) and t not in skip]

def get_bilingual(g, uri, prop):
    nl = get_literal(g, uri, prop, "nl")
    en = get_literal(g, uri, prop, "en")
    if nl or en:
        return {"nl": nl, "en": en}
    return None

def get_iso27002_attributes(g, uri):
    attr_props = {
        "control_type":           CTRL.hasControlType,
        "security_properties":    CTRL.hasSecurityProperty,
        "cybersecurity_concept":  CTRL.hasCybersecurityConcept,
        "operational_capability": CTRL.hasOperationalCapability,
        "security_domain":        CTRL.hasSecurityDomain,
        "theme":                  CTRL.hasTheme,
    }
    result = {}
    for key, prop in attr_props.items():
        vals = [get_local(str(o)) if isinstance(o, URIRef) else str(o)
                for o in g.objects(uri, prop)]
        if vals:
            result[key] = sorted(vals)
    return result if result else None

def get_node_literals(g, uri):
    """Verzamelt alle relevante literal-velden per node."""
    out = {}
    desc = get_bilingual(g, uri, RDFS.comment)
    if desc:
        out["description"] = desc
    ctrl_id = get_literal(g, uri, CTRL.hasControlID)
    if ctrl_id:
        out["control_id"] = ctrl_id
    ct_nl = get_literal(g, uri, CTRL.hasControlTitle, "nl")
    ct_en = get_literal(g, uri, CTRL.hasControlTitle, "en")
    if ct_nl or ct_en:
        out["control_title"] = {k: v for k, v in
                                [("nl", ct_nl), ("en", ct_en)] if v}
    attrs = get_iso27002_attributes(g, uri)
    if attrs:
        out["attributes"] = attrs
    for val in g.objects(uri, EXT.hasHandreikingBBN):
        if isinstance(val, Literal):
            try:
                out["bbn"] = int(val)
            except (ValueError, TypeError):
                pass
            break
    req = get_bilingual(g, uri, COMPL.requirementText)
    if req:
        out["requirement_text"] = req
    clause = get_literal(g, uri, EXT.clauseNumber)
    if clause:
        out["iso_clause"] = clause
    # compl:articleRef vervangt ext:articleNumber sinds predicate-consolidatie α (v4.3.3)
    article = get_literal(g, uri, COMPL.articleRef)
    if article:
        out["law_article"] = article
    family = get_literal(g, uri, EXT.controlFamilyCode)
    if family:
        out["control_family_code"] = family
    # CSF-specifieke velden (NIEUW v4.5.0) — csf:csfIdentifier op alle 501 CSF-individuals
    csf_id = get_literal(g, uri, CSF.csfIdentifier)
    if csf_id:
        out["csf_id"] = csf_id
    return out

# ── Edge-categorie ────────────────────────────────────────────────────────────

def edge_category(prop_uri_str):
    if prop_uri_str in GOVERNANCE_PROPS:      return "governance"
    if prop_uri_str in SKOS_PROPS:            return "skos"
    if prop_uri_str in EQUIVALENCE_PROPS:     return "equivalence"
    if prop_uri_str in CSF_HIERARCHY_PROPS:   return "csf-hierarchy"   # NIEUW v4.5.0
    if prop_uri_str in MATURITY_PROPS:        return "maturity"         # NIEUW v4.6.0
    if prop_uri_str in ATTRIBUTION_PROPS:     return "attribution"      # NIEUW v4.6.0
    if prop_uri_str in ENRICHMENT_PROPS:      return "enrichment"       # NIEUW v4.4.0
    if prop_uri_str in ISMS_PROPS:            return "isms"
    if prop_uri_str in RISK_PROPS:            return "risk"
    if prop_uri_str in ASSET_PROPS:           return "asset"
    if prop_uri_str in COMPL_PROPS:           return "compliance"
    if prop_uri_str.startswith(str(ROLES)):   return "roles"
    return "other"

# ── Source-hash ───────────────────────────────────────────────────────────────

def compute_source_hash(ttl_files):
    h = hashlib.sha256()
    for f in sorted(ttl_files):
        with open(f, "rb") as fh:
            h.update(fh.read())
    return h.hexdigest()

# ── Laden ─────────────────────────────────────────────────────────────────────

ttl_files = sorted(f for f in os.listdir(".")
                   if f.endswith(".ttl") and f != "grc-shacl.ttl")
print(f"Laden van {len(ttl_files)} Turtle-bestanden (grc-shacl.ttl uitgesloten)...")
g = Graph()
for ttl in ttl_files:
    try:
        g.parse(ttl, format="turtle")
        print(f"  ✓ {ttl}")
    except Exception as e:
        print(f"  ✗ {ttl}: {e}")
print(f"Totaal: {len(g)} triples\n")

# Ontologieversie — primair uit grc-core.ttl
version_info = None
version_iri  = None
for s, p, o in g.triples((None, OWL.versionInfo, None)):
    if isinstance(o, Literal) and str(o).startswith("4."):   # filter "concept-v1" e.d.
        version_info = str(o)
        break
for s, p, o in g.triples((None, OWL.versionIRI, None)):
    if isinstance(o, URIRef) and "4.6" in str(o):
        version_iri = str(o)
        break
if not version_info:
    version_info = "4.6.0"
print(f"Ontologieversie: {version_info}")

source_hash = compute_source_hash(ttl_files)
print(f"Source hash (SHA256): {source_hash[:16]}...\n")

# ── Individuals verzamelen ────────────────────────────────────────────────────

individuals = set()
for s in g.subjects(RDF.type, OWL.NamedIndividual):
    if str(s).startswith(GRC_BASE):
        individuals.add(s)
for s, p, o in g.triples((None, RDF.type, None)):
    if not isinstance(s, URIRef): continue
    if not str(s).startswith(GRC_BASE): continue
    if o in SCHEMA_TYPES or o == OWL.NamedIndividual: continue
    if set(g.objects(s, RDF.type)) & SCHEMA_TYPES: continue
    individuals.add(s)

print(f"Individuals na schema-filtering: {len(individuals)}")

# ── Nodes bouwen ──────────────────────────────────────────────────────────────

nodes    = []
node_ids = set()

for uri in individuals:
    uri_str = str(uri)
    nid     = make_id(uri_str)
    label, label_lang = get_label(g, uri)
    label_en = get_literal(g, uri, RDFS.label, "en") or \
               get_literal(g, uri, CTRL.hasControlTitle, "en")
    types = get_types(g, uri)
    pfx   = get_prefix(uri_str) or "other"
    laag  = bepaal_laag(uri_str)

    node = {
        "id":        nid,
        "label":     label,
        "label_en":  label_en,
        "type":      types[0] if types else "Individual",
        "types":     types,
        "namespace": pfx,
        "laag":      laag,
        "laag_naam": LAAG_NAMEN[laag],
        "uri":       uri_str,
    }
    node.update(get_node_literals(g, uri))
    nodes.append(node)
    node_ids.add(nid)

print(f"Nodes gebouwd: {len(nodes)}")

# ── Edges bouwen ──────────────────────────────────────────────────────────────

discovered_props = {}
for s, p, o in g:
    if p in TBOX_PREDICATES: continue
    if not (isinstance(s, URIRef) and isinstance(o, URIRef)): continue
    if not (str(s).startswith(GRC_BASE) and str(o).startswith(GRC_BASE)): continue
    ps = str(p)
    if ps not in discovered_props:
        discovered_props[ps] = get_local(ps)

print(f"Properties ontdekt (na TBox-filter): {len(discovered_props)}")

edges            = []
cat_counts_build = {}
seen_edges       = set()

for prop_uri, prop_label in discovered_props.items():
    prop = URIRef(prop_uri)
    cat  = edge_category(prop_uri)
    for s, o in g.subject_objects(prop):
        if not (isinstance(s, URIRef) and isinstance(o, URIRef)): continue
        sid = make_id(str(s))
        oid = make_id(str(o))
        if sid not in node_ids or oid not in node_ids: continue
        key = (sid, oid, prop_uri)
        if key in seen_edges: continue
        seen_edges.add(key)
        edges.append({
            "source":   sid,
            "target":   oid,
            "relation": prop_label,
            "prop_uri": prop_uri,
            "category": cat,
        })
        cat_counts_build[cat] = cat_counts_build.get(cat, 0) + 1

print(f"Edges totaal: {len(edges)}")

# ── Statistieken ──────────────────────────────────────────────────────────────

laag_counts = {}
for n in nodes:
    l = n["laag"]
    laag_counts[l] = laag_counts.get(l, 0) + 1

print("\nNodes per laag:")
for l in sorted(laag_counts):
    print(f"  Laag {l} ({LAAG_NAMEN[l]}): {laag_counts[l]}")
print("\nEdges per categorie:")
for c in sorted(cat_counts_build, key=lambda x: -cat_counts_build[x]):
    print(f"  {c}: {cat_counts_build[c]}")

# ── JSON-output ───────────────────────────────────────────────────────────────

now_iso = datetime.now(timezone.utc).isoformat()

skos_count       = cat_counts_build.get("skos", 0)
governance_count = cat_counts_build.get("governance", 0)
equivalence_count= cat_counts_build.get("equivalence", 0)

output = {
    "meta": {
        "generated":            now_iso,
        "ontology_version":     version_info,
        "ontology_version_iri": version_iri or f"https://grc.example.org/ontology/v{version_info}/",
        "source_files":         ttl_files,
        "source_files_count":   len(ttl_files),
        "source_files_hash":    source_hash,
        "script_version":       "build_grc_explorer v3.0",
        "triples_loaded":       len(g),
        "individuals":          len(nodes),
        "edges":                len(edges),
        "skos_mappings":        skos_count,
        "governance_edges":     governance_count,
        "equivalence_edges":    equivalence_count,
        "laag_counts":          {LAAG_NAMEN[l]: c for l, c in sorted(laag_counts.items())},
        "edge_category_counts": cat_counts_build,
    },
    "nodes": nodes,
    "edges": edges,
}

with open("grc-data-v4_6_0.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

with open("grc-data-v4_6_0.js", "w", encoding="utf-8") as f:
    f.write("/* GRC Kennismodel v4.6.0 — gegenereerd door build_grc_explorer v3.0 */\n")
    f.write("window.GRC_DATA = ")
    json.dump(output, f, ensure_ascii=False)
    f.write(";\n")

print(f"\n✓ grc-data-v4_6_0.json geschreven")
print(f"✓ grc-data-v4_6_0.js  geschreven")

# ── Verificatie ───────────────────────────────────────────────────────────────

print("\n── Verificatie bekende individuals ──────────────────────────────────────")
VERIFY = ["BIO_2_0", "NIS2_Directive", "ISO_IEC_27001_2022", "VIR_2007", "ENSIA",
          "GOVERN", "Level_1", "Tier_1_Partial"]   # juiste namen v4.5.0/v4.6.0
id_map = {n["id"].split(":", 1)[-1]: n for n in nodes}

for target in VERIFY:
    found = id_map.get(target)
    if found:
        out_e = [e for e in edges if e["source"] == found["id"]]
        in_e  = [e for e in edges if e["target"] == found["id"]]
        print(f"  ✓ {target}: laag={found['laag']} ({found['laag_naam']}), "
              f"type={found['type']}, edges={len(out_e)}↑/{len(in_e)}↓")
    else:
        matches = [n["id"] for n in nodes if target.lower() in n["id"].lower()][:3]
        print(f"  ✗ {target} — niet gevonden. Mogelijke matches: {matches}")

# Literal-coverage
print("\n── Literal-coverage ─────────────────────────────────────────────────────")
lit_fields = ["description","control_id","attributes","bbn","requirement_text",
              "iso_clause","law_article","control_family_code","csf_id"]
for field in lit_fields:
    count = sum(1 for n in nodes if field in n)
    print(f"  {field}: {count} nodes")

# H4-check: nul IRI-fragmenten als fallback-label
ctrl_nodes = [n for n in nodes if n["namespace"] == "ctrl"]
iri_fb = [n for n in ctrl_nodes
          if n["label"] == n["id"].split(":", 1)[-1] and "_" in n["label"]]
print(f"\n── H4 label-check ───────────────────────────────────────────────────────")
print(f"  ctrl:-nodes: {len(ctrl_nodes)}")
print(f"  IRI-fragment fallbacks: {len(iri_fb)} (doel: 0)")
csf_nodes = [n for n in nodes if n["namespace"] == "csf"]
csf_iri_fb = [n for n in csf_nodes
              if n["label"] == n["id"].split(":", 1)[-1] and "_" in n["label"]]
print(f"  csf:-nodes: {len(csf_nodes)}")
print(f"  csf: IRI-fragment fallbacks: {len(csf_iri_fb)}")
