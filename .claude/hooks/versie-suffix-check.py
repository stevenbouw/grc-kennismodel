#!/usr/bin/env python3
"""versie-suffix-check.py — PostToolUse hook voor Write naar output/**.

Waarschuwt (non-blocking) als een deliverable in output/verification/ of
output/reports/ geen versie-suffix `vX_Y_Z` volgt. Patroon-conventie sinds
v4.3.3-leerpunt (zie tech.md §Output-conventies + sprint-protocols §18).

Niet alle output/-bestanden hebben versie-suffix nodig (handovers, generieke
rapporten, tooling-rapporten). Daarom: WARN, geen BLOCK. Steven kan daarna
beslissen of hernoemen nodig is.

Categorieën waarvoor versie-suffix WEL verwacht:
- output/verification/*
- output/reports/inventarisatie-*
- output/reports/tussenrapport-*
- output/reports/patch-rapport-*
- output/reports/scope-pauze-*
- output/reports/brein-rapport-*
- output/reports/patchnotitie-export-*
- output/reports/skos-kwaliteitsanalyse-*

Geen versie-suffix verwacht (skip):
- output/reports/dashboard-*.md (Spoor B en algemeen)
- output/reports/tooling-*.md (infrastructuur, niet ontologie-versie-gebonden)
- output/reports/lint-*.md (datum-suffix in plaats van versie)
- output/reports/extensie-*.md, skill-eval-*.md (verkenning)
- output/reports/handover*.md
- output/reports/T2-*.md, T3-*.md (transitie/pilot tijdens iteratie 14)

§0.5-firewall: pure observatie/waarschuwing — geen autonome rename, geen
commit-actie, geen gate.

Exit-codes: ALTIJD 0 (waarschuwing via stderr, geen block).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

VERSION_SUFFIX_RE = re.compile(r"v\d+_\d+_\d+")
DATE_SUFFIX_RE = re.compile(r"\d{4}-\d{2}-\d{2}")

EXPECT_VERSION_PREFIXES = (
    "output/verification/",
    "output/reports/inventarisatie-",
    "output/reports/tussenrapport-",
    "output/reports/patch-rapport-",
    "output/reports/scope-pauze-",
    "output/reports/brein-rapport-",
    "output/reports/patchnotitie-export-",
    "output/reports/skos-kwaliteitsanalyse-",
)

SKIP_PREFIXES = (
    "output/reports/dashboard-",
    "output/reports/tooling-",
    "output/reports/lint-",
    "output/reports/extensie-",
    "output/reports/skill-eval-",
    "output/reports/handover",
    "output/reports/T2-",
    "output/reports/T3-",
)


def relative_to_repo(file_path: str) -> str | None:
    try:
        repo_root = Path(__file__).resolve().parents[2]
        return str(Path(file_path).resolve().relative_to(repo_root))
    except Exception:
        return None


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception as e:
        print(f"versie-suffix-check: stdin-parse-fout ({e})", file=sys.stderr)
        return 0

    if payload.get("tool_name", "") != "Write":
        return 0

    tool_input: dict[str, Any] = payload.get("tool_input", {}) or {}
    file_path = str(tool_input.get("file_path", ""))
    if not file_path:
        return 0

    rel = relative_to_repo(file_path)
    if not rel or not rel.startswith("output/"):
        return 0

    if any(rel.startswith(p) for p in SKIP_PREFIXES):
        return 0

    if not any(rel.startswith(p) for p in EXPECT_VERSION_PREFIXES):
        return 0

    name = Path(rel).name
    if VERSION_SUFFIX_RE.search(name):
        return 0
    if DATE_SUFFIX_RE.search(name) and rel.startswith("output/reports/lint-"):
        return 0

    print(
        f"versie-suffix-check: WAARSCHUWING — '{rel}' lijkt een versie-suffix "
        f"(vX_Y_Z) te missen (conventie sinds v4.3.3). Hernoem indien van toepassing.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
