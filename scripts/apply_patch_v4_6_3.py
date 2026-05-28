#!/usr/bin/env python3
"""
apply_patch_v4_6_3.py — SKOS-herclassificatie patch v4.6.3 (T3-sprint, m14).

Twee mutaties op `ontology/m14-avg-gdpr.ttl` volgend uit T3 Stap 3-eindrapport
en het masterchat-besluit op de pilot-escalatie (T3 §5.2 → Optie C):

    T3-001  compl:AVG_Art5_1f  broadMatch  ctrl:ISO27002_5_01  → relatedMatch
    T3-002  compl:AVG_Art5_1f  broadMatch  ctrl:ISO27002_5_12  → relatedMatch

Grond: control ↔ legal-obligation is een cross-category-relatie die associatief
is, niet subsumptief. relatedMatch is symmetrisch en lost de compl→ctrl-
richtingskwestie van broadMatch definitief op, en maakt het Art5_1f-cluster
consistent met de 5 zuster-relatedMatch-paren. m10-broadMatch is formeel correct
in ctrl→compl-richting; geen retroactieve audit (zie pilot-rapport §5.2 + T3
Stap 3-eindrapport).

Pad-keuze: instructie-t3-stap3.md plaatst dit script in `scripts/`. v4.6.2-
precedent (`output/scripts/apply_patch_v4_6_2.py`) heeft een afwijkende locatie;
deze afwijking is in het T3 Stap 3-eindrapport gemarkeerd als instructie-volgend.

Twee modi:
    DRY-RUN (default — geen file-mutatie, alleen rapport):
        python3 scripts/apply_patch_v4_6_3.py

    PRODUCTIE (alleen na bevestiging van eindrapport-classificatie):
        python3 scripts/apply_patch_v4_6_3.py --apply

Veilig: maakt backup vóór wijziging; faalt netjes als getallen niet kloppen.
Volgt T1+T2-precedent (Protocol 15: Tech levert werkbare applier).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
TTL_PATH = REPO_ROOT / "ontology" / "m14-avg-gdpr.ttl"
BACKUP_PATH = REPO_ROOT / "ontology" / "m14-avg-gdpr.ttl.v4_6_2.bak"

# Mutatie-set — hard-coded uit T3 Stap 3-eindrapport (2 mutaties).
MUTATIONS = [
    {
        "pair_id": "T3-001",
        "subject": "compl:AVG_Art5_1f",
        "object": "ctrl:ISO27002_5_01",
        "current_predicate": "skos:broadMatch",
        "target_predicate": "skos:relatedMatch",
        "mutation_direction": "downgrade",
    },
    {
        "pair_id": "T3-002",
        "subject": "compl:AVG_Art5_1f",
        "object": "ctrl:ISO27002_5_12",
        "current_predicate": "skos:broadMatch",
        "target_predicate": "skos:relatedMatch",
        "mutation_direction": "downgrade",
    },
]


def apply_one_mutation(
    content: str, subject: str, obj: str, current: str, target: str
) -> tuple[str, int]:
    """Vervang gerichte predicate in TTL-blok van subject naar object.

    Pattern: subject + arbitraire inhoud binnen Turtle-blok (geen punt
    op statement-niveau) + huidige predicate + whitespace + object.
    Volgt T1+T2-precedent.
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

    total_planned = len(MUTATIONS)

    print("=" * 70)
    print(f"apply_patch_v4_6_3.py — modus: {'PRODUCTIE' if apply_mode else 'DRY-RUN'}")
    print("=" * 70)
    print(f"Doel TTL: {TTL_PATH.relative_to(REPO_ROOT)}")
    print()
    print(f"Patch-vereiste mutaties totaal: {total_planned}")
    print()
    print("Per mutatie-richting:")
    by_direction: dict[str, int] = {}
    for m in MUTATIONS:
        by_direction[m["mutation_direction"]] = by_direction.get(m["mutation_direction"], 0) + 1
    for direction, n in by_direction.items():
        print(f"  {direction:24s}: {n:>3d}")
    print()

    content = TTL_PATH.read_text()

    # Pre-counts m14 (alleen deze module)
    pre_counts = {
        p: content.count(f"skos:{p}")
        for p in ("exactMatch", "closeMatch", "broadMatch", "narrowMatch", "relatedMatch")
    }
    print("Pre-patch m14 skos-predicate counts (m14-only):")
    for p, c in pre_counts.items():
        print(f"  skos:{p:14s}: {c:>3d}")
    print()

    applied = 0
    not_found: list[dict] = []
    multiple: list[dict] = []
    detail_log: list[str] = []

    for m in MUTATIONS:
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
            detail_log.append(
                f"  OK  [{m['pair_id']}] {m['subject']:22s} {m['current_predicate']:18s} "
                f"-> {m['target_predicate']:18s} {m['object']}"
            )
        elif n == 0:
            not_found.append(m)
            detail_log.append(
                f"  XX  NOT FOUND  [{m['pair_id']}] {m['subject']:22s} "
                f"{m['current_predicate']:18s} -> {m['object']}"
            )
        else:
            multiple.append({**m, "matches": n})
            detail_log.append(
                f"  !!  MULTIPLE ({n}) [{m['pair_id']}] {m['subject']:22s} "
                f"{m['current_predicate']:18s} -> {m['object']}"
            )

    print("Mutatie-toepassing-detail:")
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
    print("Post-patch m14 skos-predicate counts (verwacht):")
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

    # Sanity: verwachte Δ
    expected = {
        "broadMatch": -2,
        "relatedMatch": +2,
        "exactMatch": 0,
        "closeMatch": 0,
        "narrowMatch": 0,
    }
    for p, d_expected in expected.items():
        d_actual = post_counts[p] - pre_counts[p]
        if d_actual != d_expected:
            print(
                f"FOUT: Δ skos:{p} = {d_actual:+d}, verwacht {d_expected:+d}",
                file=sys.stderr,
            )
            return 4

    if not apply_mode:
        print()
        print("DRY-RUN voltooid. Geen file-mutatie uitgevoerd.")
        print("Voor productie-toepassing:")
        print("    python3 scripts/apply_patch_v4_6_3.py --apply")
        return 0

    # PRODUCTIE: backup + write
    if not BACKUP_PATH.exists():
        BACKUP_PATH.write_text(TTL_PATH.read_text())
        print(f"\nBackup gemaakt: {BACKUP_PATH.relative_to(REPO_ROOT)}")
    else:
        print(f"\nBackup bestaat al: {BACKUP_PATH.relative_to(REPO_ROOT)} (niet overschreven)")

    TTL_PATH.write_text(content)
    print(f"Patch v4.6.3 toegepast op {TTL_PATH.relative_to(REPO_ROOT)}")
    print()
    print("Vervolg:")
    print("  1. python3 output/verification/canonical_metrics_v4_6_3.py")
    print("  2. python3 output/verification/shacl_split_validate_v4_6_3.py")
    print("  3. shasum -a 256 ontology/m14-avg-gdpr.ttl")
    print("  4. patch-rapport-v4_6_3.md opstellen + commit + push (handmatig)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="T3 v4.6.3 SKOS-patch applier (m14)")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Productie-modus (default: dry-run). Vereist eindrapport-classificatie.",
    )
    args = parser.parse_args()
    return run(apply_mode=args.apply)


if __name__ == "__main__":
    raise SystemExit(main())
