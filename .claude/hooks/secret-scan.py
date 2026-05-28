#!/usr/bin/env python3
"""secret-scan.py — PreToolUse hook voor Write/Edit.

Detecteert PAT/tokens/API-keys/private-key-patronen in tool_input voor Write
en Edit. Blokkeert via exit-code 2 + stderr-melding.

Directe les uit het PAT-incident voorgaande sessie. Patronen zijn conservatief
(false-positive risico geminimaliseerd); test- en placeholder-strings worden
expliciet uitgesloten (mock_/dummy_/example_/<...>-stijl).

Werking (Claude Code-hook-protocol):
- stdin: JSON met session_id, tool_name, tool_input, transcript_path
- exit 0: allow
- exit 2: block (stderr getoond aan model)
- andere exit: non-blocking error

Input-bron per tool:
- Write: tool_input.content + tool_input.file_path
- Edit:  tool_input.new_string + tool_input.file_path

§0.5-firewall: deze hook BLOKKEERT — bouwt geen autonome commit-paden, geen
green-gate, geen sunset-flag. Pure verdediging vóór hand-off aan Steven.
"""
from __future__ import annotations

import json
import re
import sys
from typing import Any

# ── Patronen ─────────────────────────────────────────────────────────────
# Hoge-zekerheid secret-patronen. Kort gehouden om false-positives te
# vermijden; uitbreidbaar zonder breaking change.

SECRET_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("GitHub PAT (classic)",        re.compile(r"\bghp_[A-Za-z0-9]{36}\b")),
    ("GitHub PAT (fine-grained)",   re.compile(r"\bgithub_pat_[A-Za-z0-9_]{82}\b")),
    ("GitHub OAuth token",          re.compile(r"\bgho_[A-Za-z0-9]{36}\b")),
    ("GitHub server-to-server",     re.compile(r"\b(?:ghs|ghu)_[A-Za-z0-9]{36}\b")),
    ("OpenAI/Anthropic-style key",  re.compile(r"\bsk-(?:ant-)?[A-Za-z0-9_\-]{20,}\b")),
    ("AWS access key id",           re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("Google API key",              re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b")),
    ("Slack token",                 re.compile(r"\bxox[abposr]-[A-Za-z0-9\-]{10,}\b")),
    ("Private-key PEM-header",      re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY-----")),
    ("JWT (3-segment)",             re.compile(r"\beyJ[A-Za-z0-9_\-]{10,}\.eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\b")),
]

# Placeholder/test-prefixen die we expliciet whitelisten op de match-regel.
PLACEHOLDER_HINTS = re.compile(
    r"(?i)(?:mock_|dummy_|example_|placeholder|test_token|fake_|<your[-_ ]|XXXX|EXAMPLE|REDACTED)"
)


def extract_payload(tool_name: str, tool_input: dict[str, Any]) -> tuple[str, str]:
    """Return (file_path, content_to_scan) per tool. Onbekende tools: ('','')."""
    file_path = str(tool_input.get("file_path", ""))
    if tool_name == "Write":
        return file_path, str(tool_input.get("content", ""))
    if tool_name == "Edit":
        return file_path, str(tool_input.get("new_string", ""))
    return file_path, ""


def scan(content: str) -> list[tuple[str, str]]:
    """Return lijst van (label, matched-snippet). Lege lijst = clean."""
    hits: list[tuple[str, str]] = []
    for label, pat in SECRET_PATTERNS:
        for m in pat.finditer(content):
            snippet = m.group(0)
            # Lijn waar de match staat, voor placeholder-context-check.
            start = content.rfind("\n", 0, m.start()) + 1
            end = content.find("\n", m.end())
            line = content[start: end if end != -1 else len(content)]
            if PLACEHOLDER_HINTS.search(line):
                continue
            # Toon verkorte snippet (eerste/laatste 6 chars) zodat de hook-output
            # zelf geen verbatim-secret in transcripts achterlaat.
            redacted = (
                snippet[:6] + "…" + snippet[-6:]
                if len(snippet) > 16
                else snippet[:4] + "…"
            )
            hits.append((label, redacted))
    return hits


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception as e:
        print(f"secret-scan: stdin-parse-fout ({e}); allow-by-default", file=sys.stderr)
        return 0

    tool_name = payload.get("tool_name", "")
    if tool_name not in {"Write", "Edit"}:
        return 0  # niets te scannen

    tool_input = payload.get("tool_input", {}) or {}
    file_path, content = extract_payload(tool_name, tool_input)
    if not content:
        return 0

    hits = scan(content)
    if not hits:
        return 0

    print("secret-scan: vermoedelijk secret in tool-input — BLOCK", file=sys.stderr)
    print(f"  bestand: {file_path}", file=sys.stderr)
    for label, redacted in hits:
        print(f"  hit: {label} ≈ {redacted}", file=sys.stderr)
    print(
        "  actie: verwijder secret of gebruik placeholder (mock_/dummy_/example_/<your-token>) "
        "en probeer opnieuw. Bij echte test-token: zet in env, niet in repo.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
