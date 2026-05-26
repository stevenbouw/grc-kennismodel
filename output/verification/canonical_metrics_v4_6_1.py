#!/usr/bin/env python3
"""
canonical_metrics_v4_6_1.py — Canonieke meetmethode GRC Kennismodel v4.6.1
=========================================================================

Versie-suffix-conventie (sinds v4.3.3-leerpunt).

Doel
----
Reproduceerbare meting van alle structurele metrics op de v4.6.1-ontologie
(scenario C: 28 exactMatch ctrl:→compl:NIS2_Art21_* → broadMatch). Wordt
gebruikt om de patch v4.6.1 te valideren en mutaties tegen v4.6.0 baseline
te vergelijken.

Werkwijze
---------
1. Parse alle data-modules (.ttl) afzonderlijk → per-module statistiek.
2. Merge in één graph → globale statistiek (pre-inferentie).
3. Pas OWL RL inferentie toe → globale statistiek (post-inferentie).
4. Per namespace, per module, per SKOS-paar: tellingen.
5. Tweetaligheid, TBox-vs-ABox vulling, integriteitschecks, D-conformance.

Verschil t.o.v. v4_6_0-script
-----------------------------
- WORKDIR-default verwijst naar deze repo-root (relatieve `ontology/`-resolve)
  i.p.v. de hardgecodeerde `/home/claude/v433`-vault uit eerdere release.
- JSON-uitvoer wordt geschreven naar `output/verification/canonical_metrics_v4_6_1.json`.
- Versie-label = "v4.6.1".

Verwachte mutaties scenario C vs baseline v4.6.0
------------------------------------------------
- skos_mappings_total: 1798 ongewijzigd (predicate-mutatie binnen totaal)
- skos_mappings_breakdown.exactMatch: 46 -> 18 (-28)
- skos_mappings_breakdown.broadMatch: 38 -> 66 (+28)
- pre-inference triples: 20950 ongewijzigd
- klassen/individuals/sameAs ongewijzigd
- Post-inference: SKOS-inferentie-totalen volgen patroon

Vereist: rdflib >=7.0, owlrl >=7.0
"""

from __future__ import annotations

import json
import os
import sys
import hashlib
from collections import defaultdict, Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from rdflib import Graph, URIRef, Literal, BNode, RDF, RDFS, OWL, Namespace
from rdflib.namespace import SKOS, DCTERMS, XSD
import owlrl

# ── Configuratie ───────────────────────────────────────────────────────

# Default: repo-root/ontology/. Overridebaar via env var GRC_WORKDIR.
REPO_ROOT = Path(__file__).resolve().parents[2]
WORKDIR = Path(os.environ.get("GRC_WORKDIR", REPO_ROOT / "ontology"))
OUTPUT_PATH = REPO_ROOT / "output" / "verification" / "canonical_metrics_v4_6_1.json"

SHAPES_FILE = "grc-shacl.ttl"
SPARQL_FILE = "m18-demo-sparql.rq"  # niet meegeteld in metrics

NAMESPACES = {
    "fw":    "https://grc.example.org/framework/",
    "ctrl":  "https://grc.example.org/control/",
    "risk":  "https://grc.example.org/risk/",
    "roles": "https://grc.example.org/roles/",
    "compl": "https://grc.example.org/compliance/",
    "isms":  "https://grc.example.org/isms/",
    "biz":   "https://grc.example.org/business/",
    "bio":   "https://grc.example.org/bio/",
    "ext":   "https://grc.example.org/extended/",
    "asset": "https://grc.example.org/asset/",
    "csf":   "https://grc.example.org/csf/",
}
GRC_BASE = "https://grc.example.org/"

SKOS_MAPPING_PROPS = [
    SKOS.exactMatch, SKOS.closeMatch, SKOS.broadMatch,
    SKOS.narrowMatch, SKOS.relatedMatch,
]


# ── Helpers ────────────────────────────────────────────────────────────

def get_prefix(uri: str) -> str | None:
    for pfx, ns in NAMESPACES.items():
        if uri.startswith(ns):
            return pfx
    return None


def file_hash(p: Path) -> str:
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()


def count_class_assertions(g: Graph, cls: URIRef) -> int:
    return len(set(g.subjects(RDF.type, cls)))


# ── 1. Per-module parse ────────────────────────────────────────────────

def per_module_metrics(workdir: Path) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    files = sorted(p for p in workdir.iterdir()
                   if p.suffix == ".ttl" and p.name != SHAPES_FILE)
    for fp in files:
        g = Graph()
        try:
            g.parse(fp, format="turtle")
        except Exception as e:
            out[fp.name] = {"error": str(e)}
            continue

        ns_counter: Counter = Counter()
        for s in set(g.subjects()):
            if isinstance(s, URIRef):
                pfx = get_prefix(str(s))
                if pfx:
                    ns_counter[pfx] += 1

        labels_nl = labels_en = labels_unt = 0
        for s, p, o in g.triples((None, RDFS.label, None)):
            if isinstance(o, Literal):
                if o.language == "nl": labels_nl += 1
                elif o.language == "en": labels_en += 1
                else: labels_unt += 1
        comments_nl = comments_en = comments_unt = 0
        for s, p, o in g.triples((None, RDFS.comment, None)):
            if isinstance(o, Literal):
                if o.language == "nl": comments_nl += 1
                elif o.language == "en": comments_en += 1
                else: comments_unt += 1

        out[fp.name] = {
            "triples": len(g),
            "classes": count_class_assertions(g, OWL.Class),
            "named_individuals": count_class_assertions(g, OWL.NamedIndividual),
            "object_properties": count_class_assertions(g, OWL.ObjectProperty),
            "datatype_properties": count_class_assertions(g, OWL.DatatypeProperty),
            "annotation_properties": count_class_assertions(g, OWL.AnnotationProperty),
            "skos_concepts": count_class_assertions(g, SKOS.Concept),
            "subjects_per_namespace": dict(ns_counter),
            "labels_nl": labels_nl,
            "labels_en": labels_en,
            "labels_untagged": labels_unt,
            "comments_nl": comments_nl,
            "comments_en": comments_en,
            "comments_untagged": comments_unt,
            "sha256": file_hash(fp),
        }
    return out


def build_merged_graph(workdir: Path) -> Graph:
    g = Graph()
    files = sorted(p for p in workdir.iterdir()
                   if p.suffix == ".ttl" and p.name != SHAPES_FILE)
    for fp in files:
        g.parse(fp, format="turtle")
    return g


def global_metrics(g: Graph, label: str) -> dict[str, Any]:
    skos_counts = {}
    skos_total = 0
    for prop in SKOS_MAPPING_PROPS:
        n = len(list(g.triples((None, prop, None))))
        skos_counts[str(prop).split("/")[-1].split("#")[-1]] = n
        skos_total += n

    lbl_lang = Counter()
    cmt_lang = Counter()
    for _, _, o in g.triples((None, RDFS.label, None)):
        if isinstance(o, Literal):
            lbl_lang[o.language or "_untagged"] += 1
    for _, _, o in g.triples((None, RDFS.comment, None)):
        if isinstance(o, Literal):
            cmt_lang[o.language or "_untagged"] += 1

    return {
        "label": label,
        "triples": len(g),
        "owl_Class": count_class_assertions(g, OWL.Class),
        "owl_NamedIndividual": count_class_assertions(g, OWL.NamedIndividual),
        "owl_ObjectProperty": count_class_assertions(g, OWL.ObjectProperty),
        "owl_DatatypeProperty": count_class_assertions(g, OWL.DatatypeProperty),
        "owl_AnnotationProperty": count_class_assertions(g, OWL.AnnotationProperty),
        "owl_sameAs": len(list(g.triples((None, OWL.sameAs, None)))),
        "skos_Concept": count_class_assertions(g, SKOS.Concept),
        "skos_mappings_total": skos_total,
        "skos_mappings_breakdown": skos_counts,
        "rdfs_label_total": sum(lbl_lang.values()),
        "rdfs_label_per_lang": dict(lbl_lang),
        "rdfs_comment_total": sum(cmt_lang.values()),
        "rdfs_comment_per_lang": dict(cmt_lang),
        "rdfs_seeAlso": len(list(g.triples((None, RDFS.seeAlso, None)))),
    }


def apply_owl_rl(g: Graph) -> None:
    owlrl.DeductiveClosure(
        owlrl.OWLRL_Semantics,
        axiomatic_triples=False,
        datatype_axioms=False,
    ).expand(g)


def per_namespace_metrics(g: Graph) -> dict[str, dict[str, int]]:
    out = {pfx: {"classes": 0, "named_individuals": 0,
                 "object_properties": 0, "datatype_properties": 0,
                 "subjects": 0, "objects": 0}
           for pfx in NAMESPACES}

    subj_seen: dict[str, set] = {pfx: set() for pfx in NAMESPACES}
    obj_seen: dict[str, set] = {pfx: set() for pfx in NAMESPACES}
    for s, p, o in g:
        if isinstance(s, URIRef):
            pfx = get_prefix(str(s))
            if pfx: subj_seen[pfx].add(s)
        if isinstance(o, URIRef):
            pfx = get_prefix(str(o))
            if pfx: obj_seen[pfx].add(o)
    for pfx in NAMESPACES:
        out[pfx]["subjects"] = len(subj_seen[pfx])
        out[pfx]["objects"] = len(obj_seen[pfx])

    for cls_iri, key in [
        (OWL.Class, "classes"),
        (OWL.NamedIndividual, "named_individuals"),
        (OWL.ObjectProperty, "object_properties"),
        (OWL.DatatypeProperty, "datatype_properties"),
    ]:
        for s in g.subjects(RDF.type, cls_iri):
            if isinstance(s, URIRef):
                pfx = get_prefix(str(s))
                if pfx: out[pfx][key] += 1
    return out


def skos_pair_metrics(g: Graph) -> dict[str, dict[str, int]]:
    pair_counts: dict[tuple[str, str, str], int] = defaultdict(int)
    for prop in SKOS_MAPPING_PROPS:
        prop_local = str(prop).split("/")[-1].split("#")[-1]
        for s, _, o in g.triples((None, prop, None)):
            spfx = get_prefix(str(s)) if isinstance(s, URIRef) else "_blank"
            opfx = get_prefix(str(o)) if isinstance(o, URIRef) else "_external"
            if isinstance(o, URIRef) and not opfx:
                opfx = "_external_uri"
            spfx = spfx or "_other"
            opfx = opfx or "_other"
            pair_counts[(spfx, opfx, prop_local)] += 1
    out = {}
    for (s, o, m), n in sorted(pair_counts.items()):
        key = f"{s}->{o}::{m}"
        out[key] = n
    return out


def tbox_abox_per_namespace(g: Graph) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for pfx, ns in NAMESPACES.items():
        classes = {s for s in g.subjects(RDF.type, OWL.Class)
                   if isinstance(s, URIRef) and str(s).startswith(ns)}
        cls_with_inst = 0
        for c in classes:
            if any(g.subjects(RDF.type, c)):
                cls_with_inst += 1

        obj_props = {s for s in g.subjects(RDF.type, OWL.ObjectProperty)
                     if isinstance(s, URIRef) and str(s).startswith(ns)}
        dat_props = {s for s in g.subjects(RDF.type, OWL.DatatypeProperty)
                     if isinstance(s, URIRef) and str(s).startswith(ns)}
        all_props = obj_props | dat_props
        props_used = sum(1 for p in all_props if any(g.triples((None, p, None))))

        out[pfx] = {
            "classes_declared": len(classes),
            "classes_with_instances": cls_with_inst,
            "classes_unused_pct": round(
                100 * (1 - cls_with_inst / len(classes)) if classes else 0, 1
            ),
            "properties_declared": len(all_props),
            "properties_used": props_used,
            "object_properties": len(obj_props),
            "datatype_properties": len(dat_props),
        }
    return out


def integrity_checks(g: Graph) -> dict[str, Any]:
    findings: dict[str, Any] = {}

    grc_subjects = {s for s in set(g.subjects())
                    if isinstance(s, URIRef) and str(s).startswith(GRC_BASE)}
    no_type = [str(s) for s in grc_subjects
               if not any(g.triples((s, RDF.type, None)))]
    findings["grc_subjects_zonder_type"] = {"count": len(no_type), "sample": no_type[:10]}

    op_no_dom, op_no_rng = [], []
    for p in g.subjects(RDF.type, OWL.ObjectProperty):
        if not isinstance(p, URIRef): continue
        if not str(p).startswith(GRC_BASE): continue
        if not any(g.triples((p, RDFS.domain, None))):
            op_no_dom.append(str(p))
        if not any(g.triples((p, RDFS.range, None))):
            op_no_rng.append(str(p))
    dp_no_dom, dp_no_rng = [], []
    for p in g.subjects(RDF.type, OWL.DatatypeProperty):
        if not isinstance(p, URIRef): continue
        if not str(p).startswith(GRC_BASE): continue
        if not any(g.triples((p, RDFS.domain, None))):
            dp_no_dom.append(str(p))
        if not any(g.triples((p, RDFS.range, None))):
            dp_no_rng.append(str(p))
    findings["object_properties_zonder_domain"] = {"count": len(op_no_dom), "sample": op_no_dom[:10]}
    findings["object_properties_zonder_range"]  = {"count": len(op_no_rng), "sample": op_no_rng[:10]}
    findings["datatype_properties_zonder_domain"] = {"count": len(dp_no_dom), "sample": dp_no_dom[:10]}
    findings["datatype_properties_zonder_range"]  = {"count": len(dp_no_rng), "sample": dp_no_rng[:10]}

    used_as_obj = {o for o in set(g.objects())
                   if isinstance(o, URIRef) and str(o).startswith(GRC_BASE)}
    has_subject = {s for s in set(g.subjects())
                   if isinstance(s, URIRef) and str(s).startswith(GRC_BASE)}
    dangling = sorted(str(u) for u in (used_as_obj - has_subject))
    findings["dangling_grc_references"] = {"count": len(dangling), "sample": dangling[:20]}

    cls_decls: Counter = Counter()
    for s in g.subjects(RDF.type, OWL.Class):
        if isinstance(s, URIRef): cls_decls[s] += 1
    dup_cls = [(str(s), n) for s, n in cls_decls.items() if n > 1]
    findings["duplicate_owl_Class_decls"] = {"count": len(dup_cls), "sample": dup_cls[:10]}

    leaked = set()
    for node in set(g.subjects()) | set(g.objects()) | set(g.predicates()):
        if isinstance(node, URIRef) and str(node).startswith(GRC_BASE):
            if not get_prefix(str(node)):
                leaked.add(str(node))
    findings["namespace_leakage"] = {"count": len(leaked), "sample": sorted(leaked)[:20]}

    empty_lbl = sum(1 for _, _, o in g.triples((None, RDFS.label, None))
                    if isinstance(o, Literal) and str(o).strip() == "")
    empty_cmt = sum(1 for _, _, o in g.triples((None, RDFS.comment, None))
                    if isinstance(o, Literal) and str(o).strip() == "")
    findings["empty_rdfs_labels"]  = empty_lbl
    findings["empty_rdfs_comments"] = empty_cmt

    sameas_pairs: list[tuple[str, str]] = []
    for s, _, o in g.triples((None, OWL.sameAs, None)):
        if isinstance(s, URIRef) and isinstance(o, URIRef):
            sameas_pairs.append((str(s), str(o)))
    pair_ns: Counter = Counter()
    for s, o in sameas_pairs:
        a = get_prefix(s) or "?"
        b = get_prefix(o) or "?"
        pair_ns[f"{a}<->{b}"] += 1
    findings["owl_sameAs_per_ns_pair"] = dict(pair_ns)

    return findings


def d_decision_conformance(g: Graph) -> dict[str, Any]:
    out: dict[str, Any] = {}

    used_ns: Counter = Counter()
    for s in set(g.subjects()):
        if isinstance(s, URIRef):
            pfx = get_prefix(str(s))
            if pfx: used_ns[pfx] += 1
    out["D3_namespaces_used"] = dict(used_ns)

    d5 = 0
    for s, _, o in g.triples((None, OWL.sameAs, None)):
        if isinstance(s, URIRef) and isinstance(o, URIRef):
            sp, op = get_prefix(str(s)), get_prefix(str(o))
            if {sp, op} == {"ctrl", "bio"}:
                d5 += 1
    out["D5_ctrl_bio_sameAs_count"] = d5
    out["D5_target_count"] = 93
    out["D5_conform"] = (d5 == 93)

    bio2_in_ctrl = [str(s) for s in set(g.subjects())
                    if isinstance(s, URIRef)
                    and str(s).startswith(NAMESPACES["ctrl"])
                    and "BIO2" in str(s)]
    out["D7_ctrl_BIO2_overblijfselen"] = {"count": len(bio2_in_ctrl), "sample": bio2_in_ctrl[:5]}

    soa_classes = list(g.subjects(RDF.type,
                       URIRef(NAMESPACES["isms"] + "StatementOfApplicability")))
    soa_entries = list(g.subjects(RDF.type,
                       URIRef(NAMESPACES["isms"] + "SoAEntry")))
    out["D8_SoA_containers"] = [str(s) for s in soa_classes]
    out["D8_SoAEntry_count"] = len(soa_entries)

    d11 = 0
    d11_pairs = []
    for s, _, o in g.triples((None, OWL.sameAs, None)):
        if isinstance(s, URIRef) and isinstance(o, URIRef):
            sp, op = get_prefix(str(s)), get_prefix(str(o))
            if {sp, op} & {"asset"} and {sp, op} & {"risk", "isms"}:
                d11 += 1
                d11_pairs.append((str(s), str(o)))
    out["D11_asset_brug_count"] = d11
    out["D11_target_count"] = 5
    out["D11_conform"] = (d11 == 5)
    out["D11_pairs"] = d11_pairs

    bbn_prop = URIRef(NAMESPACES["ext"] + "hasHandreikingBBN")
    bbn_values: Counter = Counter()
    for _, _, o in g.triples((None, bbn_prop, None)):
        if isinstance(o, Literal):
            bbn_values[str(o)] += 1
    out["ext_hasHandreikingBBN_values"] = dict(bbn_values)
    out["ext_hasHandreikingBBN_total_assertions"] = sum(bbn_values.values())

    return out


def main():
    print(f"=== canonical_metrics_v4_6_1 — {datetime.now(timezone.utc).isoformat()} ===\n")
    print(f"Workdir: {WORKDIR}")
    files = sorted(WORKDIR.iterdir())
    print(f"Bestanden: {len(files)}\n")

    print("→ Per-module parse...")
    per_mod = per_module_metrics(WORKDIR)
    print(f"  {len(per_mod)} modules verwerkt")

    print("→ Globale graph mergen...")
    g = build_merged_graph(WORKDIR)
    print(f"  Pre-inference triples: {len(g)}")
    pre = global_metrics(g, "pre_inference")

    print("→ OWL RL inferentie toepassen...")
    g_inf = Graph()
    for fp in sorted(p for p in WORKDIR.iterdir()
                     if p.suffix == ".ttl" and p.name != SHAPES_FILE):
        g_inf.parse(fp, format="turtle")
    apply_owl_rl(g_inf)
    print(f"  Post-inference triples: {len(g_inf)}")
    post = global_metrics(g_inf, "post_inference_owlrl")

    print("→ Per-namespace tellingen...")
    per_ns_pre = per_namespace_metrics(g)
    per_ns_post = per_namespace_metrics(g_inf)

    print("→ SKOS-mapping paren...")
    skos_pairs = skos_pair_metrics(g)

    print("→ TBox/ABox vulling...")
    tbox_abox = tbox_abox_per_namespace(g)

    print("→ Integriteitschecks...")
    integrity = integrity_checks(g)

    print("→ D-conformiteit...")
    d_conf = d_decision_conformance(g)

    nothing_count = len(list(g_inf.subjects(RDF.type, OWL.Nothing)))

    output = {
        "meta": {
            "version_label": "v4.6.1",
            "measured_at_utc": datetime.now(timezone.utc).isoformat(),
            "workdir": str(WORKDIR),
            "tool_versions": {
                "rdflib": __import__("rdflib").__version__,
                "owlrl": __import__("owlrl").__version__,
                "pyshacl": __import__("pyshacl").__version__,
            },
            "file_count_data_modules": sum(
                1 for f in WORKDIR.iterdir()
                if f.suffix == ".ttl" and f.name != SHAPES_FILE),
        },
        "per_module": per_mod,
        "global_pre_inference": pre,
        "global_post_inference_owlrl": post,
        "owl_Nothing_assertions_post_inference": nothing_count,
        "per_namespace_pre": per_ns_pre,
        "per_namespace_post": per_ns_post,
        "skos_mapping_pairs": skos_pairs,
        "tbox_abox_per_namespace": tbox_abox,
        "integrity_checks": integrity,
        "d_decision_conformance": d_conf,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    print(f"\n✓ JSON-bundel: {OUTPUT_PATH}")
    print(f"\n--- KERNSAMENVATTING ---")
    print(f"Triples pre-inference:   {pre['triples']:>6}")
    print(f"Triples post-inference:  {post['triples']:>6}")
    print(f"owl:Class:               {pre['owl_Class']:>6}")
    print(f"owl:NamedIndividual:     {pre['owl_NamedIndividual']:>6}")
    print(f"owl:ObjectProperty:      {pre['owl_ObjectProperty']:>6}")
    print(f"owl:DatatypeProperty:    {pre['owl_DatatypeProperty']:>6}")
    print(f"owl:sameAs:              {pre['owl_sameAs']:>6}")
    print(f"  D5 ctrl<->bio:         {d_conf['D5_ctrl_bio_sameAs_count']:>6}")
    print(f"  D11 asset<->risk/isms: {d_conf['D11_asset_brug_count']:>6}")
    print(f"SKOS mappings totaal:    {pre['skos_mappings_total']:>6}")
    print(f"  exactMatch:            {pre['skos_mappings_breakdown']['exactMatch']:>6}")
    print(f"  broadMatch:            {pre['skos_mappings_breakdown']['broadMatch']:>6}")
    print(f"owl:Nothing post-inf:    {nothing_count:>6}  ({'OK' if nothing_count == 0 else 'INCONSISTENT'})")


if __name__ == "__main__":
    main()
