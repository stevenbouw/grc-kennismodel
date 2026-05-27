#!/usr/bin/env python3
"""
t2-cluster-overerving-helper.py — T2 Stap 3 cluster-overerving-helper

Genereert per NIS2-letter-cluster een JSON met cluster-leden, huidige
predicate, cluster-doel-predicate (vast op skos:broadMatch voor alle
10 veel<->1 clusters per Protocol v1.2 §3.1 rij 6) en mutatie-richting.

Uitvoering vanuit grc-kennismodel-root:
    python3 output/scripts/t2-cluster-overerving-helper.py

READ-ONLY: leest m10-nis2-ext.ttl, schrijft 10 cluster-JSON's +
1 overview-JSON naar output/analysis/. Geen TTL-mutaties.

Heuristieken voor exception_screening_flag (Protocol v1.2 §3.3 + instructie §4.4):
- Subject-cluster-grootte >= 3 (multi-mapping naar meerdere NIS2-letters)
- Subject-label bevat brede-policy-termen (policy / roles / governance /
  management / framework / responsibilities)
- Voor evidence-niveau-4-of-onbekend zou extra signaal nuttig zijn; in
  Stap 3 wordt evidence-niveau handmatig vastgesteld per cluster-lid.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

import rdflib

REPO_ROOT = Path(__file__).resolve().parents[2]
TTL_PATH = REPO_ROOT / "ontology" / "m10-nis2-ext.ttl"
LABELS_TTL_PATH = REPO_ROOT / "ontology" / "m02-control.ttl"
OUT_DIR = REPO_ROOT / "output" / "analysis"

SKOS = rdflib.Namespace("http://www.w3.org/2004/02/skos/core#")
CTRL_NS = "https://grc.example.org/control/"
COMPL_NS = "https://grc.example.org/compliance/"

CLUSTER_LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
PREDICATES = ["exactMatch", "closeMatch", "broadMatch", "narrowMatch", "relatedMatch"]

# Pilot-paren uit T2 Stap 2 (pilot-rapport §1.1/§4.x).
# (subject_local, object_local) -> pilot_id
PILOT_PAIRS: dict[tuple[str, str], str] = {
    ("ISO27002_5_09", "NIS2_Art21_i"): "T2-S01",
    ("ISO27002_5_28", "NIS2_Art21_b"): "T2-S02",
    ("ISO27002_5_03", "NIS2_Art21_a"): "T2-S03",
    ("ISO27002_5_08", "NIS2_Art21_a"): "T2-S04",
    ("ISO27002_5_05", "NIS2_Art21_a"): "T2-S05",
    ("ISO27002_8_27", "NIS2_Art21_e"): "T2-S06-alt",
    ("ISO27002_5_15", "NIS2_Art21_j"): "T2-S07-alt",
    ("ISO27002_5_30", "NIS2_Art21_c"): "T2-S08-alt",
}

# Brede-policy-keywords voor exception_screening_flag heuristiek.
BROAD_POLICY_KEYWORDS = (
    # Engels (uit ISO 27002:2022-EN-labels)
    "policy",
    "policies",
    "roles",
    "responsibilit",
    "governance",
    "management responsib",
    "framework",
    # Nederlands (uit NL-labels in m02-control.ttl)
    "beleid",
    "managementverant",
    "verantwoordelijk",
    "kader",
)


def short_local(uri: str, ns: str) -> str:
    return uri.replace(ns, "")


def classify_mutation(current: str, target: str) -> tuple[str, bool]:
    """Bepaal mutatie-richting + patch_required.

    Protocol v1.2 §3.2 sterkte-ordening:
        exactMatch > closeMatch > broadMatch ~ narrowMatch > relatedMatch
    broadMatch <-> narrowMatch = richtings-correctie (niet sterkte).
    """
    if current == target:
        return "behoud", False

    strength = {
        "exactMatch": 4,
        "closeMatch": 3,
        "broadMatch": 2,
        "narrowMatch": 2,
        "relatedMatch": 1,
    }
    c_strength = strength.get(current, 0)
    t_strength = strength.get(target, 0)

    if {current, target} == {"broadMatch", "narrowMatch"}:
        return "richtings-correctie", True
    if t_strength > c_strength:
        return "upgrade", True
    if t_strength < c_strength:
        return "downgrade", True
    return "twijfel", True


def load_triples() -> tuple[list[dict], dict[str, int]]:
    """Laad alle ctrl:* skos:* compl:NIS2_Art21_* triples uit m10."""
    g = rdflib.Graph()
    g.parse(str(TTL_PATH), format="turtle")

    pairs: list[dict] = []
    subject_cluster_size: dict[str, int] = defaultdict(int)

    for pred_name in PREDICATES:
        pred = SKOS[pred_name]
        for s, o in g.subject_objects(pred):
            s_str = str(s)
            o_str = str(o)
            if not (s_str.startswith(CTRL_NS) and o_str.startswith(COMPL_NS)):
                continue
            o_local = short_local(o_str, COMPL_NS)
            if not o_local.startswith("NIS2_Art21_"):
                continue
            s_local = short_local(s_str, CTRL_NS)
            pairs.append(
                {
                    "subject": s_local,
                    "object": o_local,
                    "current_predicate": f"skos:{pred_name}",
                }
            )
            subject_cluster_size[s_local] += 1

    return pairs, dict(subject_cluster_size)


def get_subject_label(g: rdflib.Graph, subject_local: str) -> str:
    """Haal Nederlandstalig rdfs:label op voor heuristiek."""
    subject_iri = rdflib.URIRef(CTRL_NS + subject_local)
    for label in g.objects(subject_iri, rdflib.RDFS.label):
        if isinstance(label, rdflib.Literal) and (label.language or "nl") == "nl":
            return str(label)
    # fallback: pak eerste beschikbare label
    for label in g.objects(subject_iri, rdflib.RDFS.label):
        return str(label)
    return ""


def screen_exception(
    subject_local: str,
    label: str,
    subject_cluster_size: int,
    current_predicate: str,
    target_predicate: str,
) -> tuple[bool, str | None]:
    """Heuristiek voor exception_screening_flag.

    Vlag alleen kandidaten waar individuele NEN-aantoonbare uitzondering
    plausibel is. Niet-bindend; Tech reviewt elke flag.
    """
    if current_predicate == target_predicate:
        return False, None

    label_lower = label.lower()
    rationale_parts: list[str] = []

    has_policy_kw = any(kw in label_lower for kw in BROAD_POLICY_KEYWORDS)
    big_subject_cluster = subject_cluster_size >= 3

    if has_policy_kw:
        rationale_parts.append(
            f"label bevat brede-policy-term (suggereert mogelijk closeMatch-kandidaat): \"{label}\""
        )
    if big_subject_cluster:
        rationale_parts.append(
            f"subject-cluster-grootte {subject_cluster_size} (multi-mapping naar meerdere NIS2-letters)"
        )

    if rationale_parts:
        return True, "; ".join(rationale_parts)
    return False, None


def build_cluster_json(
    letter: str,
    cluster_members: list[dict],
    g: rdflib.Graph,
    subject_cluster_size: dict[str, int],
) -> dict:
    cluster_id = f"compl:NIS2_Art21_{letter}"
    target = "skos:broadMatch"
    rationale = "veel<->1 object-cluster, Protocol v1.2 §3.1 rij 6"

    members_out: list[dict] = []
    for entry in sorted(cluster_members, key=lambda x: x["subject"]):
        subj = entry["subject"]
        obj = entry["object"]
        current = entry["current_predicate"]
        mutation, patch_required = classify_mutation(current.split(":")[-1], target.split(":")[-1])
        label = get_subject_label(g, subj)
        pilot_id = PILOT_PAIRS.get((subj, obj))
        flag, flag_rationale = screen_exception(
            subj, label, subject_cluster_size[subj], current, target
        )
        members_out.append(
            {
                "subject": f"ctrl:{subj}",
                "object": f"compl:{obj}",
                "subject_label_nl": label,
                "current_predicate": current,
                "cluster_target_predicate": target,
                "mutation_direction": mutation,
                "patch_required": patch_required,
                "exception_screening_flag": flag,
                "exception_screening_rationale": flag_rationale,
                "is_pilot_pair": pilot_id is not None,
                "pilot_id": pilot_id,
                "subject_cluster_size": subject_cluster_size[subj],
            }
        )

    counts = {
        "total": len(members_out),
        "behoud": sum(1 for m in members_out if m["mutation_direction"] == "behoud"),
        "downgrade": sum(1 for m in members_out if m["mutation_direction"] == "downgrade"),
        "upgrade": sum(1 for m in members_out if m["mutation_direction"] == "upgrade"),
        "richtings_correctie": sum(
            1 for m in members_out if m["mutation_direction"] == "richtings-correctie"
        ),
        "patch_required": sum(1 for m in members_out if m["patch_required"]),
        "exception_flags": sum(1 for m in members_out if m["exception_screening_flag"]),
        "pilot_pairs": sum(1 for m in members_out if m["is_pilot_pair"]),
    }

    return {
        "cluster_id": cluster_id,
        "cluster_letter": letter,
        "cluster_size": len(members_out),
        "cluster_target_predicate": target,
        "rationale": rationale,
        "counts": counts,
        "members": members_out,
    }


def main() -> int:
    if not TTL_PATH.exists():
        print(f"FOUT: {TTL_PATH} niet gevonden — run vanuit repo-root", file=sys.stderr)
        return 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    pairs, subject_cluster_size = load_triples()
    print(f"Totaal m10-paren (ctrl->compl:NIS2_Art21_*): {len(pairs)}")
    assert len(pairs) == 118, f"Verwacht 118, kreeg {len(pairs)}"

    g = rdflib.Graph()
    g.parse(str(TTL_PATH), format="turtle")
    # m02-control.ttl bevat de ISO27002-individual-labels (m10 declareert ze
    # slechts als skos-mapping-subject). Voor de brede-policy-keyword-heuristiek
    # laden we m02 erbij.
    if LABELS_TTL_PATH.exists():
        g.parse(str(LABELS_TTL_PATH), format="turtle")

    by_cluster: dict[str, list[dict]] = defaultdict(list)
    for entry in pairs:
        letter = entry["object"].split("_")[-1]
        by_cluster[letter].append(entry)

    overview: dict = {
        "source_ttl": "ontology/m10-nis2-ext.ttl",
        "total_pairs_m10": len(pairs),
        "cluster_target_predicate_all": "skos:broadMatch",
        "rationale_all": (
            "Alle 10 NIS2-art.21-letter-clusters zijn veel<->1 object-clusters; "
            "Protocol v1.2 §3.1 rij 6 levert deterministisch skos:broadMatch als "
            "cluster-doel-predicate (structureel feit uit C2-cardinaliteit, geen "
            "voorspelling van Stap 3-uitkomst)."
        ),
        "clusters": {},
        "totals": {
            "behoud": 0,
            "downgrade": 0,
            "upgrade": 0,
            "richtings_correctie": 0,
            "patch_required": 0,
            "exception_flags": 0,
            "pilot_pairs": 0,
        },
    }

    for letter in CLUSTER_LETTERS:
        members = by_cluster.get(letter, [])
        cluster_data = build_cluster_json(letter, members, g, subject_cluster_size)
        out_path = OUT_DIR / f"t2-cluster-{letter}.json"
        out_path.write_text(json.dumps(cluster_data, indent=2, ensure_ascii=False) + "\n")
        print(f"  cluster-{letter}: size={cluster_data['cluster_size']:>2d}  "
              f"behoud={cluster_data['counts']['behoud']:>2d}  "
              f"downgrade={cluster_data['counts']['downgrade']:>2d}  "
              f"upgrade={cluster_data['counts']['upgrade']:>2d}  "
              f"flags={cluster_data['counts']['exception_flags']:>2d}  "
              f"-> {out_path.relative_to(REPO_ROOT)}")

        overview["clusters"][f"compl:NIS2_Art21_{letter}"] = {
            "cluster_size": cluster_data["cluster_size"],
            "counts": cluster_data["counts"],
        }
        for k in overview["totals"]:
            overview["totals"][k] += cluster_data["counts"][k]

    overview_path = OUT_DIR / "t2-cluster-overview.json"
    overview_path.write_text(json.dumps(overview, indent=2, ensure_ascii=False) + "\n")
    print(f"\nOverview: {overview_path.relative_to(REPO_ROOT)}")
    print("\nTotalen over alle 10 clusters:")
    for k, v in overview["totals"].items():
        print(f"  {k}: {v}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
