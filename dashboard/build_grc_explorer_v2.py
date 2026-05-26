"""
build_grc_explorer_v2.py — GRC Kennismodel v4.3.0
Extraheert individuals, relaties en laag-toewijzingen uit TTL-bestanden
en schrijft grc-data-v4.3.0.js voor grc-explorer.html.

Fixes t.o.v. v1 (build_grc_explorer.py):
  H1 — fw:implementeert + fw:baseertOp verwijderd (bestaan niet in model)
  H2 — 8 ontbrekende governance-properties toegevoegd
  H3 — dubbele GOVERNANCE_PROPS declaratie verwijderd
  H4 — ctrl:hasControlTitle@nl/en als fallback voor rdfs:label
  H5 — literal-export toegevoegd (description, control_id, attributes,
        bbn, requirement_text, iso_clause, law_article)
  H6 — TBox-relaties (rdfs:domain, rdfs:range, rdfs:subClassOf) uitgesloten;
        ctrl:belongsToFramework toegevoegd als 'framework'-categorie
  H7 — draait op v4.3.0-snapshot (20 TTL-bestanden incl. grc-core + grc-bridges)
  H8 — versie-header in output (generated, ontology_version, source_files_hash,
        script_version)

Auteur: GRC Dashboard-chat
Datum:  14 april 2026
"""

import os
import json
import hashlib
from datetime import datetime, timezone
from rdflib import Graph, Namespace, RDF, RDFS, OWL, URIRef, Literal
from rdflib.namespace import SKOS, XSD

# ── Namespaces ───────────────────────────────────────────────────────────────

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

# Predicaten die TBox-relaties zijn — NOOIT als edges exporteren [H6]
TBOX_PREDICATES = {
    RDFS.domain, RDFS.range, RDFS.subClassOf, RDFS.subPropertyOf,
    OWL.equivalentClass, OWL.disjointWith, OWL.complementOf,
    OWL.inverseOf, OWL.onProperty, OWL.allValuesFrom, OWL.someValuesFrom,
    OWL.hasValue, OWL.unionOf, OWL.intersectionOf, OWL.oneOf,
    RDF.type,
}

# ── Governance-properties — H1/H2/H3 fix ────────────────────────────────────
# Correcte set: 9 bestaande properties, fw:implementeert + fw:baseertOp
# verwijderd (bestaan niet in model — 0 triples, 0 declaraties).

GOVERNANCE_PROPS = {
    str(FW.stelVerplicht):         "fw:stelVerplicht",
    str(FW.geeftRichtlijnenVoor):  "fw:geeftRichtlijnenVoor",
    str(FW.geeftITInvullingAan):   "fw:geeftITInvullingAan",
    str(FW.dektAf):                "fw:dektAf",
    str(FW.toetst):                "fw:toetst",
    str(FW.transposedBy):          "fw:transposedBy",
    str(FW.supersedes):            "fw:supersedes",
    str(FW.alignsWith):            "fw:alignsWith",
    str(EXT.isComponentOf):        "ext:isComponentOf",
    str(CTRL.belongsToFramework):  "ctrl:belongsToFramework",  # H6 toevoeging
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

# Overige inter-individual relations
ISMS_PROPS = {
    str(ISMS.hasSoA), str(ISMS.containsEntry), str(ISMS.implementsControl),
    str(ISMS.forSoA), str(ISMS.forRisk),
}
RISK_PROPS = {
    str(RISK.mitigatedBy), str(RISK.hasRisk), str(RISK.affectsAsset),
}
ASSET_PROPS = {
    str(ASSET.appliesToAssetType), str(ASSET.hasAssetOwner),
}
COMPL_PROPS = {
    str(COMPL.satisfiedBy), str(COMPL.requiresControl),
}

# ── Normenkader-lagen ────────────────────────────────────────────────────────

LAAG_NAMEN = {
    0: "COSO/Enterprise",
    1: "IT-governance",
    2: "Wet/regelgeving",
    3: "Operationeel (BIO)",
    4: "Normen (ISO/NIST)",
    5: "Audit (ENSIA)",
    9: "ISMS/Bedrijf/Overig",
}

def bepaal_laag(uri_str):
    local_upper = get_local(uri_str).upper()
    pfx = get_prefix(uri_str)

    if pfx == "fw":
        if any(k in local_upper for k in ("COSO", "ERM")):       return 0
        if any(k in local_upper for k in ("COBIT", "BVA", "CIO")): return 1
        if any(k in local_upper for k in ("NIS2", "VIR", "VIRBI", "AVG", "CBW", "DORA")): return 2
        if "BIO" in local_upper:                                   return 3
        if any(k in local_upper for k in ("ISO", "NIST", "IEC")): return 4
        if "ENSIA" in local_upper:                                 return 5
    if pfx == "roles": return 1
    if pfx == "compl": return 2
    if pfx == "bio":   return 3
    if pfx == "ctrl":  return 4
    return 9

# ── Helpers ──────────────────────────────────────────────────────────────────

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
    pfx = get_prefix(uri_str)
    local = get_local(uri_str)
    return f"{pfx}:{local}" if pfx else local

def get_literal(g, uri, prop, lang=None):
    """Haal een literal op; optioneel gefilterd op taal."""
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
    Label-opzoek met fallback-keten [H4]:
    1. rdfs:label@nl
    2. rdfs:label@en
    3. ctrl:hasControlTitle@nl  ← nieuw (fixes 93 ISO 27002-controls)
    4. rdfs:label (geen taal)
    5. skos:prefLabel
    6. lokale IRI-naam
    """
    for lang in ("nl", "en"):
        v = get_literal(g, uri, RDFS.label, lang)
        if v:
            return v, lang
    v = get_literal(g, uri, CTRL.hasControlTitle, "nl")
    if v:
        return v, "nl"
    v = get_literal(g, uri, CTRL.hasControlTitle, "en")
    if v:
        return v, "en"
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

# ── Literal-export helpers [H5] ───────────────────────────────────────────────

def get_bilingual(g, uri, prop):
    """Geeft {'nl': ..., 'en': ...} terug; None als beide ontbreken."""
    nl = get_literal(g, uri, prop, "nl")
    en = get_literal(g, uri, prop, "en")
    if nl or en:
        return {"nl": nl, "en": en}
    return None

def get_iso27002_attributes(g, uri):
    """Exporteert de 6 ISO 27002:2022-attributen als object met lijsten."""
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
        vals = []
        for o in g.objects(uri, prop):
            if isinstance(o, URIRef):
                vals.append(get_local(str(o)))
            elif isinstance(o, Literal):
                vals.append(str(o))
        if vals:
            result[key] = sorted(vals)
    return result if result else None

def get_node_literals(g, uri):
    """
    Verzamelt alle relevante literal-velden voor een node [H5].
    Retourneert dict; lege velden worden weggelaten.
    """
    out = {}

    # Beschrijving
    desc = get_bilingual(g, uri, RDFS.comment)
    if desc:
        out["description"] = desc

    # Control-ID (ISO 27002 + BIO controls)
    ctrl_id = get_literal(g, uri, CTRL.hasControlID)
    if ctrl_id:
        out["control_id"] = ctrl_id

    # ctrl:hasControlTitle apart bewaren voor label_en (kan bij H4 al labels zijn)
    ct_nl = get_literal(g, uri, CTRL.hasControlTitle, "nl")
    ct_en = get_literal(g, uri, CTRL.hasControlTitle, "en")
    if ct_nl or ct_en:
        out["control_title"] = {}
        if ct_nl: out["control_title"]["nl"] = ct_nl
        if ct_en: out["control_title"]["en"] = ct_en

    # ISO 27002-attributen
    attrs = get_iso27002_attributes(g, uri)
    if attrs:
        out["attributes"] = attrs

    # BBN (Handreiking BIO2-opmaat) — ext:hasHandreikingBBN, xsd:integer, waarden 1 of 2
    for val in g.objects(uri, EXT.hasHandreikingBBN):
        if isinstance(val, Literal):
            try:
                bbn_int = int(val)
                out["bbn"] = bbn_int
            except (ValueError, TypeError):
                pass
            break

    # Compliance requirement-tekst
    req = get_bilingual(g, uri, COMPL.requirementText)
    if req:
        out["requirement_text"] = req

    # ISO clausule-nummer (ISO 27001, ISO 22301)
    clause = get_literal(g, uri, EXT.clauseNumber)
    if clause:
        out["iso_clause"] = clause

    # Wetsartikel-nummer (NIS2, VIRBI, AVG, VIR)
    article = get_literal(g, uri, EXT.articleNumber)
    if article:
        out["law_article"] = article

    # Control family code (NIST 800-53)
    family = get_literal(g, uri, EXT.controlFamilyCode)
    if family:
        out["control_family_code"] = family

    return out

# ── Edge-categorie [H6] ───────────────────────────────────────────────────────

def edge_category(prop_uri_str):
    if prop_uri_str in GOVERNANCE_PROPS:  return "governance"
    if prop_uri_str in SKOS_PROPS:        return "skos"
    if prop_uri_str in EQUIVALENCE_PROPS: return "equivalence"
    if prop_uri_str in ISMS_PROPS:        return "isms"
    if prop_uri_str in RISK_PROPS:        return "risk"
    if prop_uri_str in ASSET_PROPS:       return "asset"
    if prop_uri_str in COMPL_PROPS:       return "compliance"
    if prop_uri_str.startswith(str(ROLES)): return "roles"
    return "other"

# ── Source-hash berekenen [H8] ────────────────────────────────────────────────

def compute_source_hash(ttl_files):
    """SHA256 van gesorteerde concatenatie van alle input-TTL-bestanden."""
    h = hashlib.sha256()
    for f in sorted(ttl_files):
        with open(f, "rb") as fh:
            h.update(fh.read())
    return h.hexdigest()

# ── Laden [H7] ────────────────────────────────────────────────────────────────

ttl_files = sorted(f for f in os.listdir(".") if f.endswith(".ttl"))
print(f"Laden van {len(ttl_files)} Turtle-bestanden...")
g = Graph()
for ttl in ttl_files:
    try:
        g.parse(ttl, format="turtle")
        print(f"  ✓ {ttl}")
    except Exception as e:
        print(f"  ✗ {ttl}: {e}")
print(f"Totaal: {len(g)} triples\n")

# Ontologieversie uitlezen uit grc-core.ttl [H8]
GRC_CORE_URI = URIRef("https://grc.example.org/ontology/")
version_info = None
for s, p, o in g.triples((None, OWL.versionInfo, None)):
    if isinstance(o, Literal):
        version_info = str(o)
        break
version_iri = None
for s, p, o in g.triples((None, OWL.versionIRI, None)):
    if isinstance(o, URIRef):
        version_iri = str(o)
        break
if not version_info:
    version_info = "4.3.0"  # hardcode fallback als owl:versionInfo ontbreekt
print(f"Ontologieversie: {version_info}")

# Source hash [H8]
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
    if o in SCHEMA_TYPES: continue
    if o == OWL.NamedIndividual: continue
    if set(g.objects(s, RDF.type)) & SCHEMA_TYPES: continue
    individuals.add(s)

print(f"Individuals na schema-filtering: {len(individuals)}")

# ── Nodes bouwen [H4 + H5] ────────────────────────────────────────────────────

nodes = []
node_ids = set()

for uri in individuals:
    uri_str = str(uri)
    nid = make_id(uri_str)
    label, label_lang = get_label(g, uri)

    # label_en apart zoeken
    label_en = get_literal(g, uri, RDFS.label, "en")
    if not label_en:
        label_en = get_literal(g, uri, CTRL.hasControlTitle, "en")

    types = get_types(g, uri)
    pfx = get_prefix(uri_str) or "other"
    laag = bepaal_laag(uri_str)

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

    # Literal-velden toevoegen [H5]
    literals = get_node_literals(g, uri)
    node.update(literals)

    nodes.append(node)
    node_ids.add(nid)

print(f"Nodes gebouwd: {len(nodes)}")

# ── Edges bouwen [H6] ─────────────────────────────────────────────────────────

# Alle inter-individual properties ontdekken, met uitsluiting van TBox-predicaten
discovered_props = {}
for s, p, o in g:
    if p in TBOX_PREDICATES:
        continue  # H6: TBox-relaties altijd overslaan
    if (isinstance(s, URIRef) and isinstance(o, URIRef) and
            str(s).startswith(GRC_BASE) and str(o).startswith(GRC_BASE)):
        ps = str(p)
        if ps not in discovered_props:
            discovered_props[ps] = get_local(ps)

print(f"Properties ontdekt (na TBox-filter): {len(discovered_props)}")

edges = []
skos_count = 0
governance_count = 0
equivalence_count = 0
seen_edges = set()

for prop_uri, prop_label in discovered_props.items():
    prop = URIRef(prop_uri)
    cat = edge_category(prop_uri)
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
        if cat == "skos":       skos_count += 1
        if cat == "governance": governance_count += 1
        if cat == "equivalence": equivalence_count += 1

print(f"Edges totaal: {len(edges)}")
print(f"  governance: {governance_count}")
print(f"  skos:       {skos_count}")
print(f"  equivalence: {equivalence_count}")

# ── Statistieken ──────────────────────────────────────────────────────────────

laag_counts = {}
for n in nodes:
    l = n["laag"]
    laag_counts[l] = laag_counts.get(l, 0) + 1

cat_counts = {}
for e in edges:
    c = e["category"]
    cat_counts[c] = cat_counts.get(c, 0) + 1

print("\nNodes per laag:")
for l in sorted(laag_counts):
    print(f"  Laag {l} ({LAAG_NAMEN[l]}): {laag_counts[l]}")
print("\nEdges per categorie:")
for c in sorted(cat_counts):
    print(f"  {c}: {cat_counts[c]}")

# ── JSON-output [H8] ─────────────────────────────────────────────────────────

now_iso = datetime.now(timezone.utc).isoformat()

output = {
    "meta": {
        "generated":           now_iso,
        "ontology_version":    version_info,
        "ontology_version_iri": version_iri or f"https://grc.example.org/ontology/v{version_info}/",
        "source_files":        ttl_files,
        "source_files_count":  len(ttl_files),
        "source_files_hash":   source_hash,
        "script_version":      "build_grc_explorer v2.0",
        "triples_loaded":      len(g),
        "individuals":         len(nodes),
        "edges":               len(edges),
        "skos_mappings":       skos_count,
        "governance_edges":    governance_count,
        "equivalence_edges":   equivalence_count,
        "laag_counts":         {LAAG_NAMEN[l]: c for l, c in sorted(laag_counts.items())},
        "edge_category_counts": cat_counts,
    },
    "nodes": nodes,
    "edges": edges,
}

# JSON
with open("grc-data-v4.3.0.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

# JS voor standalone browser-gebruik (geen server nodig)
with open("grc-data-v4.3.0.js", "w", encoding="utf-8") as f:
    f.write("/* GRC Kennismodel v4.3.0 — gegenereerd door build_grc_explorer v2.0 */\n")
    f.write("window.GRC_DATA = ")
    json.dump(output, f, ensure_ascii=False)
    f.write(";\n")

print(f"\n✓ grc-data-v4.3.0.json geschreven")
print(f"✓ grc-data-v4.3.0.js  geschreven")

# ── Verificatie ───────────────────────────────────────────────────────────────

VERIFY = ["BIO_2_0", "NIS2_Directive", "ISO_IEC_27001_2022", "VIR_2007", "ENSIA"]
print("\n── Verificatie 5 bekende individuals ────────────────────────────────────")
id_map = {n["id"].split(":", 1)[-1]: n for n in nodes}
node_map = {n["id"]: n for n in nodes}

for target in VERIFY:
    found = id_map.get(target)
    if found:
        out_e = [e for e in edges if e["source"] == found["id"]]
        in_e  = [e for e in edges if e["target"] == found["id"]]
        has_lit = [k for k in ("description","control_id","attributes","bbn",
                               "requirement_text","iso_clause","law_article")
                   if k in found]
        print(f"  ✓ {target}")
        print(f"      label:    {found['label']}")
        print(f"      laag:     {found['laag']} ({found['laag_naam']})")
        print(f"      edges:    {len(out_e)} uitgaand, {len(in_e)} inkomend")
        print(f"      literals: {has_lit if has_lit else '(geen)'}")
    else:
        matches = [n["id"] for n in nodes if target.lower() in n["id"].lower()]
        print(f"  ✗ {target} — niet gevonden. Mogelijke matches: {matches[:5]}")

# ── H1/H2 verificatie: governance-properties ─────────────────────────────────
print("\n── H1/H2 verificatie governance-properties ──────────────────────────────")
for cat_name, cat_edges in [("governance", [e for e in edges if e["category"]=="governance"])]:
    props_used = {}
    for e in cat_edges:
        p = e["relation"]
        props_used[p] = props_used.get(p, 0) + 1
    print(f"  Governance-edges per property:")
    for p, c in sorted(props_used.items(), key=lambda x: -x[1]):
        print(f"    {p}: {c}")

# ── H5 verificatie: literal coverage ─────────────────────────────────────────
print("\n── H5 verificatie literal-coverage ─────────────────────────────────────")
lit_fields = ["description","control_id","attributes","bbn",
              "requirement_text","iso_clause","law_article","control_family_code"]
for field in lit_fields:
    count = sum(1 for n in nodes if field in n)
    print(f"  {field}: {count} nodes")

# ── H4 verificatie: ISO 27002-control labels ──────────────────────────────────
print("\n── H4 verificatie: ISO 27002-control labels ─────────────────────────────")
ctrl_nodes = [n for n in nodes if n["namespace"] == "ctrl"]
iri_fallbacks = [n for n in ctrl_nodes if "_" in n["label"] and n["label"] == n["id"].split(":",1)[-1]]
print(f"  ctrl:-nodes: {len(ctrl_nodes)}")
print(f"  nodes met IRI-fragment als label (fallback): {len(iri_fallbacks)}")
sample_ctrl = [n for n in ctrl_nodes if n.get("control_id")][:3]
for n in sample_ctrl:
    print(f"    {n['id']}: '{n['label']}' (id={n.get('control_id','?')})")
