#!/usr/bin/env python3
"""skos_axioma_variant_v4_6_3.py — H41 VERGELIJKENDE meting (geen omschakeling).

EVALUATIE-script. De canonieke config (canonical_metrics_v4_6_3.py) blijft
ONGEMOEID. Dit script draait een SKOS-axioma-geladen VARIANT náást de canonieke
baseline en meet het verschil. Output gaat naar een NIET-canoniek JSON-bestand.
Het wijzigt geen TTL, geen baseline, geen productie-default.

Meet (H41, Stap 2 uit instructie §2):
  1. Baseline = merged graph + canonieke OWL RL (axiomatic_triples=False,
     datatype_axioms=False). MOET 44907 post-inferentie-triples reproduceren.
  2. Variant  = merged graph + EXPLICIETE SKOS-axioma-graph + dezelfde canonieke
     OWL RL-config. Surgische injectie van W3C SKOS-Reference property-
     karakteristieken (S46 symmetrie, S47 transitiviteit), NIET axiomatic_triples=True.
  3. Δ post-OWL-RL triples + Δ per SKOS-predicaat (baseline vs variant).
  4. sameAs-disentangle: welk deel van de post-inferentie SKOS-toename in de
     BASELINE komt van owl:sameAs-propagatie (D5/D11), niet van SKOS-axiomas?
  5. Cross-namespace-transitiviteits-check: ontstaan in de variant nieuwe
     mapping-ketens over >=3 namespaces (bv. CSF -> ISO -> BIO)? Gewenst/ongewenst?

Output (output/verification/, niet-canoniek):
  - skos_axioma_variant_v4_6_3.json

Vereist: rdflib >=7.0, owlrl >=7.0
"""
from __future__ import annotations

import json
import os
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

from rdflib import Graph, URIRef, BNode, Literal, RDF, RDFS, OWL
from rdflib.namespace import SKOS
import owlrl

REPO_ROOT = Path(__file__).resolve().parents[1]
WORKDIR = Path(os.environ.get("GRC_WORKDIR", REPO_ROOT / "ontology"))
SHAPES_FILE = "grc-shacl.ttl"
OUT_JSON = REPO_ROOT / "output" / "verification" / "skos_axioma_variant_v4_6_3.json"

NAMESPACES = {
    "fw": "https://grc.example.org/framework/",
    "ctrl": "https://grc.example.org/control/",
    "risk": "https://grc.example.org/risk/",
    "roles": "https://grc.example.org/roles/",
    "compl": "https://grc.example.org/compliance/",
    "isms": "https://grc.example.org/isms/",
    "biz": "https://grc.example.org/business/",
    "bio": "https://grc.example.org/bio/",
    "ext": "https://grc.example.org/extended/",
    "asset": "https://grc.example.org/asset/",
    "csf": "https://grc.example.org/csf/",
}
SKOS_PROPS = [SKOS.exactMatch, SKOS.closeMatch, SKOS.broadMatch,
              SKOS.narrowMatch, SKOS.relatedMatch]

# W3C SKOS-Reference property-karakteristieken (S46/S47 e.d.) — expliciete
# axioma-graph in Turtle. Surgisch: alleen mapping-property-semantiek, geen
# brede axiomatic_triples.
SKOS_AXIOMS_TTL = """
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

# S46 — symmetrie
skos:exactMatch   a owl:SymmetricProperty .
skos:closeMatch   a owl:SymmetricProperty .
skos:relatedMatch a owl:SymmetricProperty .

# S47 — transitiviteit (exactMatch is symmetrisch EN transitief)
skos:exactMatch   a owl:TransitiveProperty .

# broad/narrow zijn elkaars inverse
skos:broadMatch   owl:inverseOf skos:narrowMatch .

# subPropertyOf-hierarchie (SKOS-Reference): exactMatch =< closeMatch
skos:exactMatch   rdfs:subPropertyOf skos:closeMatch .
"""


def get_prefix(uri: str):
    for pfx, ns in NAMESPACES.items():
        if uri.startswith(ns):
            return pfx
    return None


def build_merged_graph() -> Graph:
    g = Graph()
    for fp in sorted(p for p in WORKDIR.iterdir()
                     if p.suffix == ".ttl" and p.name != SHAPES_FILE):
        g.parse(fp, format="turtle")
    return g


def canonical_owlrl(g: Graph) -> None:
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics,
                           axiomatic_triples=False,
                           datatype_axioms=False).expand(g)


def skos_breakdown(g: Graph) -> dict:
    out = {}
    total = 0
    for p in SKOS_PROPS:
        n = len(list(g.triples((None, p, None))))
        out[str(p).split("#")[-1]] = n
        total += n
    out["_total"] = total
    return out


def skos_pairs_crossns(g: Graph) -> dict:
    """SKOS-mapping-tellingen per (subj-ns -> obj-ns)::predicaat."""
    pc = defaultdict(int)
    for p in SKOS_PROPS:
        loc = str(p).split("#")[-1]
        for s, _, o in g.triples((None, p, None)):
            sp = get_prefix(str(s)) if isinstance(s, URIRef) else "_bnode"
            op = get_prefix(str(o)) if isinstance(o, URIRef) else "_lit"
            pc[f"{sp}->{op}::{loc}"] += 1
    return dict(sorted(pc.items()))


def sameas_disentangle(pre_skos_total: int, base_post_skos_total: int) -> dict:
    """Isoleer de owl:sameAs-propagatie-bijdrage aan de baseline SKOS-toename.

    CONTROL-run: identieke merged graph maar met alle owl:sameAs-triples
    VERWIJDERD vóór OWL RL. Het verschil tussen baseline-post-SKOS en
    control-post-SKOS = de sameAs-toerekenbare toename.

    (De eerdere 'touching sameAs participant'-meting was vervuild doordat OWL RL
    owl:sameAs reflexief maakt — elke node wordt dan formeel sameAs-deelnemer.)
    """
    g = build_merged_graph()
    # verwijder asserted owl:sameAs (D5 + D11) vóór inferentie
    sameas_triples = list(g.triples((None, OWL.sameAs, None)))
    n_removed = len(sameas_triples)
    for t in sameas_triples:
        g.remove(t)
    canonical_owlrl(g)
    control_post_skos = skos_breakdown(g)
    sameas_contrib = base_post_skos_total - control_post_skos["_total"]
    inference_total = base_post_skos_total - pre_skos_total
    return {
        "asserted_sameAs_removed": n_removed,
        "control_post_skos_total_no_sameAs": control_post_skos["_total"],
        "control_post_skos_breakdown_no_sameAs": control_post_skos,
        "baseline_post_skos_total": base_post_skos_total,
        "pre_inference_skos_total": pre_skos_total,
        "inference_added_skos_total": inference_total,
        "sameAs_attributable_skos": sameas_contrib,
        "sameAs_pct_of_inference": round(100 * sameas_contrib / inference_total, 1)
            if inference_total else 0.0,
    }


def new_skos_triples(g_base: Graph, g_var: Graph, prop: URIRef,
                     max_samples: int = 40) -> dict:
    """Welke GROND-mapping-triples voor prop bestaan in variant maar niet baseline?
    Categoriseer per (subj-ns -> obj-ns); toon cross-namespace samples."""
    def ground_set(g):
        return {(s, o) for s, _, o in g.triples((None, prop, None))
                if isinstance(s, URIRef) and isinstance(o, URIRef)}
    new = ground_set(g_var) - ground_set(g_base)
    per_pair = Counter()
    cross_ns = []
    for s, o in new:
        sp, op = get_prefix(str(s)), get_prefix(str(o))
        per_pair[f"{sp}->{op}"] += 1
        if sp and op and sp != op:
            cross_ns.append((str(s), str(o), f"{sp}->{op}"))
    return {"new_triples_total": len(new),
            "per_ns_pair": dict(per_pair.most_common()),
            "cross_namespace_new": len(cross_ns),
            "cross_namespace_sample": [
                {"subject": s, "object": o, "ns": ns}
                for s, o, ns in cross_ns[:max_samples]]}


def cross_ns_chains(g: Graph, prop: URIRef, min_namespaces: int = 3,
                    max_samples: int = 25) -> dict:
    """Vind mapping-ketens A->B->C waar >=min_namespaces verschillende namespaces
    voorkomen. Werkt op de (al dan niet geinfereerde) graph voor predicaat prop."""
    adj = defaultdict(set)
    for s, _, o in g.triples((None, prop, None)):
        if isinstance(s, URIRef) and isinstance(o, URIRef):
            adj[s].add(o)
    chains = []
    for a in adj:
        for b in adj.get(a, ()):
            for c in adj.get(b, ()):
                if c in (a, b):
                    continue
                nss = {get_prefix(str(x)) for x in (a, b, c)}
                nss.discard(None)
                if len(nss) >= min_namespaces:
                    chains.append((str(a), str(b), str(c), sorted(nss)))
    # dedup
    uniq = {tuple(ch[:3]): ch for ch in chains}
    chains = list(uniq.values())
    return {"count": len(chains),
            "sample": [{"a": a, "b": b, "c": c, "namespaces": ns}
                       for a, b, c, ns in chains[:max_samples]]}


def main():
    print(f"=== skos_axioma_variant_v4_6_3 (H41 vergelijking) — "
          f"{datetime.now(timezone.utc).isoformat()} ===")

    # --- BASELINE (canoniek) ---
    print("→ BASELINE: merged graph + canonieke OWL RL...")
    g_base = build_merged_graph()
    pre_triples = len(g_base)
    pre_skos = skos_breakdown(g_base)
    canonical_owlrl(g_base)
    base_post_triples = len(g_base)
    base_post_skos = skos_breakdown(g_base)
    print(f"  pre={pre_triples}, post={base_post_triples} "
          f"(MOET 44907 zijn: {'OK' if base_post_triples == 44907 else 'AFWIJKING!'})")

    print("→ sameAs-disentangle (control-run zonder owl:sameAs)...")
    sameas_share = sameas_disentangle(pre_skos["_total"], base_post_skos["_total"])
    print(f"  Inferentie voegde +{sameas_share['inference_added_skos_total']} SKOS toe; "
          f"daarvan {sameas_share['sameAs_attributable_skos']} toerekenbaar aan "
          f"owl:sameAs ({sameas_share['sameAs_pct_of_inference']}%)")

    # baseline cross-ns chains (zonder SKOS-axiomas — referentie)
    base_chains_close = cross_ns_chains(g_base, SKOS.closeMatch)
    base_chains_exact = cross_ns_chains(g_base, SKOS.exactMatch)

    # --- VARIANT (SKOS-axiomas geladen) ---
    print("→ VARIANT: merged graph + expliciete SKOS-axioma-graph + canonieke OWL RL...")
    g_var = build_merged_graph()
    g_var.parse(data=SKOS_AXIOMS_TTL, format="turtle")
    var_pre_triples = len(g_var)
    canonical_owlrl(g_var)
    var_post_triples = len(g_var)
    var_post_skos = skos_breakdown(g_var)
    print(f"  pre(+axioms)={var_pre_triples}, post={var_post_triples}")
    print(f"  Δ post-inferentie triples (variant - baseline) = "
          f"{var_post_triples - base_post_triples}")

    var_chains_close = cross_ns_chains(g_var, SKOS.closeMatch)
    var_chains_exact = cross_ns_chains(g_var, SKOS.exactMatch)

    # Concrete nieuw-gematerialiseerde mapping-triples (variant \ baseline)
    print("→ Nieuw-gematerialiseerde mapping-triples extraheren...")
    new_exact = new_skos_triples(g_base, g_var, SKOS.exactMatch)
    new_close = new_skos_triples(g_base, g_var, SKOS.closeMatch)
    new_related = new_skos_triples(g_base, g_var, SKOS.relatedMatch)
    new_narrow = new_skos_triples(g_base, g_var, SKOS.narrowMatch)

    # Δ per predicaat
    skos_delta = {}
    for k in base_post_skos:
        skos_delta[k] = var_post_skos.get(k, 0) - base_post_skos.get(k, 0)

    payload = {
        "meta": {
            "purpose": "H41 vergelijkende meting — SKOS-axioma-impact, GEEN config-omschakeling",
            "measured_at_utc": datetime.now(timezone.utc).isoformat(),
            "canonical_config": {"axiomatic_triples": False, "datatype_axioms": False},
            "variant_config": "canonieke OWL RL + expliciete SKOS-axioma-graph (S46/S47 + broad/narrow inverse + exact<=close subPropertyOf)",
            "skos_axioms_injected_ttl": SKOS_AXIOMS_TTL.strip(),
            "tool_versions": {"rdflib": __import__("rdflib").__version__,
                              "owlrl": __import__("owlrl").__version__},
        },
        "baseline": {
            "pre_inference_triples": pre_triples,
            "pre_inference_skos": pre_skos,
            "post_inference_triples": base_post_triples,
            "reproduces_canonical_44907": base_post_triples == 44907,
            "post_inference_skos": base_post_skos,
            "sameAs_attributable_skos": sameas_share,
            "cross_ns_chains_closeMatch": base_chains_close,
            "cross_ns_chains_exactMatch": base_chains_exact,
        },
        "variant_skos_axioms": {
            "pre_inference_triples_incl_axioms": var_pre_triples,
            "post_inference_triples": var_post_triples,
            "post_inference_skos": var_post_skos,
            "cross_ns_chains_closeMatch": var_chains_close,
            "cross_ns_chains_exactMatch": var_chains_exact,
            "_chain_note": "cross_ns_chains = aantal 3-hop bereikbaarheids-PADEN over >=3 namespaces; illustratief voor entanglement, NIET gelijk aan nieuwe triples. Nieuwe TRIPLES staan in new_materialized_triples.",
            "new_materialized_triples": {
                "exactMatch": new_exact,
                "closeMatch": new_close,
                "relatedMatch": new_related,
                "narrowMatch": new_narrow,
            },
        },
        "delta_variant_minus_baseline": {
            "post_inference_triples": var_post_triples - base_post_triples,
            "skos_per_predicate": skos_delta,
            "cross_ns_chains_closeMatch": var_chains_close["count"] - base_chains_close["count"],
            "cross_ns_chains_exactMatch": var_chains_exact["count"] - base_chains_exact["count"],
        },
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    print(f"\n✓ {OUT_JSON}")
    print("\n--- KERNSAMENVATTING H41 ---")
    print(f"Baseline post-inf triples : {base_post_triples}")
    print(f"Variant  post-inf triples : {var_post_triples}  "
          f"(Δ +{var_post_triples - base_post_triples})")
    print(f"SKOS Δ per predicaat (variant - baseline):")
    for k, v in skos_delta.items():
        if k != "_total":
            print(f"   {k:<14} {v:+d}")
    print(f"   {'TOTAAL':<14} {skos_delta['_total']:+d}")
    print(f"Cross-ns closeMatch PADEN: baseline {base_chains_close['count']} "
          f"-> variant {var_chains_close['count']} (bereikbaarheid, geen triples)")
    print(f"Cross-ns exactMatch PADEN: baseline {base_chains_exact['count']} "
          f"-> variant {var_chains_exact['count']}")
    print(f"NIEUWE exactMatch-triples: {new_exact['new_triples_total']} "
          f"(waarvan cross-namespace: {new_exact['cross_namespace_new']})")
    print(f"NIEUWE closeMatch-triples: {new_close['new_triples_total']} "
          f"(cross-ns: {new_close['cross_namespace_new']})")
    print(f"NIEUWE narrowMatch-triples: {new_narrow['new_triples_total']} "
          f"(cross-ns: {new_narrow['cross_namespace_new']})")
    print(f"sameAs-toerekenbaar van inferentie-SKOS (baseline): "
          f"{sameas_share['sameAs_pct_of_inference']}%")


if __name__ == "__main__":
    main()
