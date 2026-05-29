#!/usr/bin/env python3
"""owlrl_hermit_diff.py — H38 triple-set-diff: owlrl-export vs HermiT-export.

EVALUATIE-script. Wijzigt niets aan de ontologie of de canonieke config.

Gebruik (door projecteigenaar, NA de Protégé/HermiT-export — zie runbook in
output/reports/evaluatie-reasoner-toolchain-h37-h38-h41.md §H38):

    python3 scripts/owlrl_hermit_diff.py \
        --owlrl  output/verification/owlrl_inferred_v4_6_3.ttl \
        --hermit <pad-naar-hermit-inferred-export>.ttl \
        [--base  ALL]          # trek de asserted merged graph van BEIDE af
                               # (isoleert puur-geïnfereerde triples; aanrader
                               #  als de HermiT-export de hele ontologie bevat)
        [--out   output/reports/owlrl-hermit-vergelijking-v4_6_3.md]

Methode-keuzes (bewust):
  - Diff op GROND-triples (subject+object zijn URIRef/Literal). Triples met
    blank nodes (TBox-restricties, lijst-cellen) worden NIET in de set-diff
    meegenomen omdat bnode-labels niet stabiel zijn tussen twee serialisaties;
    ze worden apart geteld en gerapporteerd als 'bnode-betrokken (niet
    set-vergelijkbaar)'.
  - 'Housekeeping' = semantisch inert (owl:Thing-typering, reflexieve
    subClassOf/equivalentClass/sameAs, type owl:Class/NamedIndividual op
    bekende termen). Deze worden apart geteld zodat de MODEL-SEMANTISCHE delta
    zichtbaar wordt zonder serialisatie-ruis.

Uitkomst: markdown-rapport + exit-code 0 (geen semantische delta) of 2
(semantische delta gevonden — scope-pauze-trigger per instructie §4).
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

from rdflib import Graph, URIRef, BNode, Literal, RDF, RDFS, OWL
from rdflib.namespace import SKOS

REPO_ROOT = Path(__file__).resolve().parents[1]
SHAPES_FILE = "grc-shacl.ttl"
OWL_THING = OWL.Thing


def merged_asserted_graph() -> Graph:
    g = Graph()
    wd = REPO_ROOT / "ontology"
    for fp in sorted(p for p in wd.iterdir()
                     if p.suffix == ".ttl" and p.name != SHAPES_FILE):
        g.parse(fp, format="turtle")
    return g


def ground_triples(g: Graph) -> set:
    """Triples zonder blank nodes (set-vergelijkbaar tussen serialisaties)."""
    out = set()
    for s, p, o in g:
        if isinstance(s, BNode) or isinstance(o, BNode):
            continue
        out.add((s, p, o))
    return out


def is_housekeeping(t: tuple) -> bool:
    s, p, o = t
    # owl:Thing-typering en alles met owl:Thing
    if o == OWL_THING or s == OWL_THING:
        return True
    # reflexieve relaties
    if p in (RDFS.subClassOf, OWL.equivalentClass, OWL.sameAs,
             RDFS.subPropertyOf, OWL.equivalentProperty) and s == o:
        return True
    # type owl:Class / owl:NamedIndividual / rdfs:Resource (structureel)
    if p == RDF.type and o in (OWL.Class, OWL.NamedIndividual, RDFS.Resource,
                               RDFS.Class, OWL.Thing):
        return True
    return False


def categorize(triples: set) -> dict:
    by_pred: Counter = Counter()
    semantic = []
    housekeeping = 0
    for t in triples:
        if is_housekeeping(t):
            housekeeping += 1
            continue
        by_pred[str(t[1])] += 1
        semantic.append(t)
    return {"semantic": semantic, "housekeeping": housekeeping,
            "by_predicate": dict(by_pred.most_common())}


def fmt(t: tuple) -> str:
    def short(x):
        sx = str(x)
        for ns, pfx in [
            ("https://grc.example.org/control/", "ctrl:"),
            ("https://grc.example.org/bio/", "bio:"),
            ("https://grc.example.org/asset/", "asset:"),
            ("https://grc.example.org/risk/", "risk:"),
            ("https://grc.example.org/isms/", "isms:"),
            ("https://grc.example.org/compliance/", "compl:"),
            ("https://grc.example.org/csf/", "csf:"),
            ("https://grc.example.org/framework/", "fw:"),
            ("https://grc.example.org/extended/", "ext:"),
            ("http://www.w3.org/2004/02/skos/core#", "skos:"),
            ("http://www.w3.org/2002/07/owl#", "owl:"),
            ("http://www.w3.org/2000/01/rdf-schema#", "rdfs:"),
            ("http://www.w3.org/1999/02/22-rdf-syntax-ns#", "rdf:"),
        ]:
            if sx.startswith(ns):
                return sx.replace(ns, pfx)
        return f"<{sx}>" if isinstance(x, URIRef) else f'"{sx}"'
    return f"{short(t[0])}  {short(t[1])}  {short(t[2])}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--owlrl", required=True, help="owlrl inferred TTL export")
    ap.add_argument("--hermit", required=True, help="HermiT inferred TTL export (Protégé)")
    ap.add_argument("--base", choices=["ALL"], default=None,
                    help="ALL = trek asserted merged graph van beide exports af")
    ap.add_argument("--out", default=str(
        REPO_ROOT / "output" / "reports" / "owlrl-hermit-vergelijking-v4_6_3.md"))
    args = ap.parse_args()

    g_rl = Graph(); g_rl.parse(args.owlrl, format="turtle")
    g_hm = Graph(); g_hm.parse(args.hermit, format="turtle")
    print(f"owlrl-export : {len(g_rl)} triples")
    print(f"hermit-export: {len(g_hm)} triples")

    rl = ground_triples(g_rl)
    hm = ground_triples(g_hm)

    if args.base == "ALL":
        base = ground_triples(merged_asserted_graph())
        rl = rl - base
        hm = hm - base
        print(f"(na --base ALL: owlrl-only-inferred={len(rl)}, hermit-only-inferred={len(hm)})")

    only_hermit = hm - rl   # wat HermiT WEL afleidt en owlrl NIET (de kern-vraag)
    only_owlrl = rl - hm
    common = rl & hm

    cat_h = categorize(only_hermit)
    cat_r = categorize(only_owlrl)

    bnode_rl = sum(1 for s, p, o in g_rl if isinstance(s, BNode) or isinstance(o, BNode))
    bnode_hm = sum(1 for s, p, o in g_hm if isinstance(s, BNode) or isinstance(o, BNode))

    semantic_delta = len(cat_h["semantic"])

    lines = []
    lines.append("# OWL RL vs HermiT — triple-set-diff v4.6.3 (H38)\n")
    lines.append(f"- owlrl-export: `{args.owlrl}` — {len(g_rl)} triples "
                 f"({bnode_rl} bnode-betrokken, niet set-vergelijkbaar)")
    lines.append(f"- hermit-export: `{args.hermit}` — {len(g_hm)} triples "
                 f"({bnode_hm} bnode-betrokken, niet set-vergelijkbaar)")
    lines.append(f"- base-aftrek: {args.base or 'geen'}\n")
    lines.append("## Grond-triple set-vergelijking (excl. bnodes)\n")
    lines.append(f"- Gemeenschappelijk: **{len(common)}**")
    lines.append(f"- Alleen owlrl: **{len(only_owlrl)}** "
                 f"(semantisch {len(cat_r['semantic'])}, housekeeping {cat_r['housekeeping']})")
    lines.append(f"- Alleen HermiT: **{len(only_hermit)}** "
                 f"(semantisch {semantic_delta}, housekeeping {cat_h['housekeeping']})\n")

    lines.append("## Model-semantische delta (HermiT \\ owlrl, excl. housekeeping)\n")
    if semantic_delta == 0:
        lines.append("**GEEN model-semantische triple die HermiT afleidt en OWL RL "
                     "mist.** OWL RL is op deze baseline materialiseerbaarheids-"
                     "equivalent aan HermiT (binnen grond-triple-scope).\n")
    else:
        lines.append(f"**{semantic_delta} model-semantische triples** alleen door "
                     f"HermiT afgeleid. Per predicaat:\n")
        for pred, n in cat_h["by_predicate"].items():
            lines.append(f"- `{pred}`: {n}")
        lines.append("\nSample (max 50):\n")
        for t in cat_h["semantic"][:50]:
            lines.append(f"- {fmt(t)}")
        lines.append("\n> ⚠️ Per instructie §4: substantiële model-semantisch "
                     "kritische delta = scope-pauze + Optie A/B/C naar masterchat. "
                     "Niet zelf reasoner-config wijzigen.")

    Path(args.out).write_text("\n".join(lines) + "\n")
    print(f"\n✓ Rapport: {args.out}")
    print(f"Model-semantische HermiT-only delta: {semantic_delta}")
    sys.exit(2 if semantic_delta > 0 else 0)


if __name__ == "__main__":
    main()
