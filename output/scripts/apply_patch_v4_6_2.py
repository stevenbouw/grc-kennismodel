#!/usr/bin/env python3
"""
apply_patch_v4_6_2.py — SKOS-herclassificatie patch v4.6.2 (T2-sprint)

Cluster-niveau patch op ontology/m10-nis2-ext.ttl. Past de patch-vereiste
mutaties uit T2 Stap 3 cluster-overerving toe: alle ctrl:* SKOS-mappings
naar compl:NIS2_Art21_* convergeren naar skos:broadMatch (per cluster-doel
uit Protocol v1.2 §3.1 rij 6, veel<->1 object-cluster).

Mutatie-set wordt uit output/analysis/t2-cluster-{a..j}.json gelezen.
Inclusief pilot-mutaties (5 paren uit Stap 2: T2-S02, T2-S03, T2-S05,
T2-S07-alt; T2-S08-alt wordt door TTL-werkelijkheid als behoud
geclassificeerd — zie t2-stap3-eindrapport §6.4). Plus Stap 3-mutaties
(cluster-overerving van resterende paren).

Twee modi:
    DRY-RUN (default — geen file-mutatie, alleen rapport):
        python3 output/scripts/apply_patch_v4_6_2.py

    PRODUCTIE (alleen na masterchat-GO in Stap 4):
        python3 output/scripts/apply_patch_v4_6_2.py --apply

Veilig: maakt backup vóór wijziging; faalt netjes als getallen niet kloppen.
Volgt T1-precedent apply_patch_v4_6_1.py + Protocol 15 (Tech levert werkbare
applier).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TTL_PATH = REPO_ROOT / "ontology" / "m10-nis2-ext.ttl"
BACKUP_PATH = REPO_ROOT / "ontology" / "m10-nis2-ext.ttl.v4_6_1.bak"
ANALYSIS_DIR = REPO_ROOT / "output" / "analysis"
CLUSTER_LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


def load_mutations() -> list[dict]:
    """Lees patch-vereiste mutaties uit cluster-JSON's.

    Returns lijst van mutatie-records met subject, object, current, target,
    direction, cluster_letter, pilot_id.
    """
    mutations: list[dict] = []
    for letter in CLUSTER_LETTERS:
        path = ANALYSIS_DIR / f"t2-cluster-{letter}.json"
        if not path.exists():
            sys.exit(
                f"FOUT: {path} ontbreekt — run eerst "
                f"output/scripts/t2-cluster-overerving-helper.py"
            )
        data = json.loads(path.read_text())
        for m in data["members"]:
            if not m["patch_required"]:
                continue
            mutations.append(
                {
                    "subject": m["subject"],
                    "object": m["object"],
                    "current_predicate": m["current_predicate"],
                    "target_predicate": m["cluster_target_predicate"],
                    "mutation_direction": m["mutation_direction"],
                    "cluster_letter": letter,
                    "is_pilot_pair": m["is_pilot_pair"],
                    "pilot_id": m["pilot_id"],
                    "exception_screening_flag": m["exception_screening_flag"],
                }
            )
    return mutations


def apply_one_mutation(
    content: str, subject: str, obj: str, current: str, target: str
) -> tuple[str, int]:
    """Vervang gerichte predicate in TTL-blok van subject naar object.

    Pattern: subject + arbitraire inhoud binnen Turtle-blok (geen punt
    op statement-niveau) + huidige predicate + whitespace + object.
    Volgt T1-precedent apply_patch_v4_6_1.py.
    """
    cur_local = current.split(":")[-1]
    tgt_local = target.split(":")[-1]
    pattern = re.compile(
        rf"({re.escape(subject)}[^.]*?)skos:{cur_local}(\s+{re.escape(obj)}\b)"
    )
    new_content, n = pattern.subn(rf"\1skos:{tgt_local}\2", content)
    return new_content, n


def run(apply_mode: bool) -> int:
    if not TTL_PATH.exists():
        print(f"FOUT: {TTL_PATH} niet gevonden — run vanuit repo-root", file=sys.stderr)
        return 1

    mutations = load_mutations()
    total_planned = len(mutations)

    # Tellingen per mutatie-richting
    by_direction: dict[str, int] = {}
    by_cluster: dict[str, int] = {}
    pilot_count = 0
    exception_flag_count = 0
    for m in mutations:
        by_direction[m["mutation_direction"]] = by_direction.get(m["mutation_direction"], 0) + 1
        by_cluster[m["cluster_letter"]] = by_cluster.get(m["cluster_letter"], 0) + 1
        if m["is_pilot_pair"]:
            pilot_count += 1
        if m["exception_screening_flag"]:
            exception_flag_count += 1

    print(f"{'=' * 70}")
    print(f"apply_patch_v4_6_2.py — modus: {'PRODUCTIE' if apply_mode else 'DRY-RUN'}")
    print(f"{'=' * 70}")
    print(f"Bron: output/analysis/t2-cluster-*.json")
    print(f"Doel TTL: {TTL_PATH.relative_to(REPO_ROOT)}")
    print()
    print(f"Patch-vereiste mutaties totaal: {total_planned}")
    print(f"  Pilot-paren in mutatie-set:    {pilot_count}")
    print(f"  Uitzondering-flag (review):    {exception_flag_count}")
    print()
    print("Per mutatie-richting:")
    for direction in ("upgrade", "downgrade", "richtings-correctie", "twijfel"):
        if by_direction.get(direction):
            print(f"  {direction:24s}: {by_direction[direction]:>3d}")
    print()
    print("Per cluster:")
    for letter in CLUSTER_LETTERS:
        cnt = by_cluster.get(letter, 0)
        print(f"  compl:NIS2_Art21_{letter}: {cnt:>3d}")
    print()

    content = TTL_PATH.read_text()

    # Pre-counts
    pre_counts = {
        p: content.count(f"skos:{p}")
        for p in ("exactMatch", "closeMatch", "broadMatch", "narrowMatch", "relatedMatch")
    }
    print("Pre-patch m10 skos-predicate counts (model-breed in m10):")
    for p, c in pre_counts.items():
        print(f"  skos:{p:14s}: {c:>3d}")
    print()

    applied = 0
    not_found: list[dict] = []
    multiple: list[dict] = []
    detail_log: list[str] = []

    for m in mutations:
        new_content, n = apply_one_mutation(
            content,
            m["subject"],
            m["object"],
            m["current_predicate"],
            m["target_predicate"],
        )
        if n == 1:
            content = new_content
            applied += 1
            tag = f"[{m['pilot_id']}]" if m["pilot_id"] else f"[cluster-{m['cluster_letter']}]"
            detail_log.append(
                f"  OK  {tag:18s} {m['subject']:25s} {m['current_predicate']:20s} "
                f"-> {m['target_predicate']:20s} {m['object']}"
            )
        elif n == 0:
            not_found.append(m)
            detail_log.append(
                f"  XX  NOT FOUND  {m['subject']:25s} {m['current_predicate']:20s} "
                f"-> {m['object']}"
            )
        else:
            multiple.append({**m, "matches": n})
            detail_log.append(
                f"  !!  MULTIPLE ({n}) {m['subject']:25s} {m['current_predicate']:20s} "
                f"-> {m['object']}"
            )

    print(f"Mutatie-toepassing-detail:")
    for line in detail_log:
        print(line)
    print()
    print(f"Toegepast: {applied} / {total_planned}")
    if not_found:
        print(f"Niet gevonden: {len(not_found)}")
    if multiple:
        print(f"Meerdere matches (ambigu): {len(multiple)}")

    if applied != total_planned:
        print()
        print("FOUT: niet alle mutaties toepasbaar. Bestand NIET overschreven.", file=sys.stderr)
        return 2

    # Post-counts verificatie
    post_counts = {
        p: content.count(f"skos:{p}")
        for p in ("exactMatch", "closeMatch", "broadMatch", "narrowMatch", "relatedMatch")
    }
    print()
    print("Post-patch m10 skos-predicate counts (verwacht):")
    for p, c in post_counts.items():
        delta = c - pre_counts[p]
        sign = "+" if delta > 0 else ""
        print(f"  skos:{p:14s}: {c:>3d}  (Δ {sign}{delta})")

    # Sanity: total predicates conserved
    pre_total = sum(pre_counts.values())
    post_total = sum(post_counts.values())
    if pre_total != post_total:
        print(
            f"FOUT: totaal-predicates niet behouden ({pre_total} -> {post_total})",
            file=sys.stderr,
        )
        return 3

    if not apply_mode:
        print()
        print("DRY-RUN voltooid. Geen file-mutatie uitgevoerd.")
        print("Voor productie-toepassing (Stap 4 na masterchat-GO):")
        print("    python3 output/scripts/apply_patch_v4_6_2.py --apply")
        return 0

    # PRODUCTIE: backup + write
    if not BACKUP_PATH.exists():
        BACKUP_PATH.write_text(TTL_PATH.read_text())
        print(f"\nBackup gemaakt: {BACKUP_PATH.relative_to(REPO_ROOT)}")
    else:
        print(f"\nBackup bestaat al: {BACKUP_PATH.relative_to(REPO_ROOT)} (niet overschreven)")

    TTL_PATH.write_text(content)
    print(f"Patch v4.6.2 toegepast op {TTL_PATH.relative_to(REPO_ROOT)}")
    print()
    print("Vervolg in Stap 4:")
    print("  1. python3 output/verification/canonical_metrics_v4_6_2.py")
    print("  2. python3 output/verification/shacl_split_validate_v4_6_2.py")
    print("  3. shasum -a 256 ontology/m10-nis2-ext.ttl")
    print("  4. patch-rapport-v4_6_2.md opstellen + commit + push")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="T2 v4.6.2 SKOS-patch applier")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Productie-modus (default: dry-run). Vereist masterchat-GO Stap 4.",
    )
    args = parser.parse_args()
    return run(apply_mode=args.apply)


if __name__ == "__main__":
    raise SystemExit(main())
