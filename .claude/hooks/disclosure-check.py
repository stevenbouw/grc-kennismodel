#!/usr/bin/env python3
"""disclosure-check.py — PreToolUse hook voor Write/Edit.

Codificeert Protocol 14 categorieën 1-4 als deterministische regex-check:
1. Organisatienaam (configurabel via disclosure-config*.json)
2. Persoonsnamen ≠ Steven (configurabel)
3. Lokale paden buiten repo (allow-list: repo zelf + NEN-licentie-pad)
4. E-mail-domeinen + organisatie-specifieke TLD's

Categorie 5 (NEN-tekst-fragment >10 woorden) is BEWUST UITGESLOTEN — vereist
semantische beoordeling en blijft Tech-handmatige toets per instructie A.2.

Configuratie:
- `.claude/hooks/disclosure-config.json` — versioned baseline (placeholders +
  allow-listen + scan-scope)
- `.claude/hooks/disclosure-config.local.json` — gitignored override met de
  feitelijke organisatie-namen/-tlds/-domains. Lokale entries vervangen
  versioned entries (geen merge — bewust simpel).

§0.5-firewall: deze hook BLOKKEERT — geen autonome unlock, geen env-flag-
sunset, geen green-gate.

Exit-codes:
- 0: clean of niet-toepasselijk
- 2: vondst → block + stderr met categorie + redacted snippet
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
HOOKS_DIR = Path(__file__).resolve().parent
CONFIG_PATH = HOOKS_DIR / "disclosure-config.json"
CONFIG_LOCAL_PATH = HOOKS_DIR / "disclosure-config.local.json"


def load_config() -> dict[str, Any]:
    cfg: dict[str, Any] = {}
    if CONFIG_PATH.exists():
        try:
            cfg = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"disclosure-check: config-parse-fout ({e}); allow-by-default", file=sys.stderr)
            return {}
    if CONFIG_LOCAL_PATH.exists():
        try:
            local = json.loads(CONFIG_LOCAL_PATH.read_text(encoding="utf-8"))
            # Lokale entries overschrijven versioned entries (geen merge).
            for k, v in local.items():
                if not k.startswith("_"):
                    cfg[k] = v
        except Exception as e:
            print(f"disclosure-check: local-config-parse-fout ({e}); val terug op versioned", file=sys.stderr)
    return cfg


def extract_payload(tool_name: str, tool_input: dict[str, Any]) -> tuple[str, str]:
    file_path = str(tool_input.get("file_path", ""))
    if tool_name == "Write":
        return file_path, str(tool_input.get("content", ""))
    if tool_name == "Edit":
        return file_path, str(tool_input.get("new_string", ""))
    return file_path, ""


def in_scope(file_path: str, cfg: dict[str, Any]) -> bool:
    scopes = cfg.get("scan_scopes", {}) or {}
    skip_paths = scopes.get("skip_paths", []) or []
    rel = file_path
    try:
        rel = str(Path(file_path).resolve().relative_to(REPO_ROOT))
    except Exception:
        pass
    for skip in skip_paths:
        if rel == skip or rel.startswith(skip.rstrip("/") + "/"):
            return False
    include_ext = scopes.get("include_extensions", []) or []
    if not include_ext:
        return True
    return Path(file_path).suffix.lower() in {e.lower() for e in include_ext}


# ── Categorie-checks ─────────────────────────────────────────────────────

EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b")
LOCAL_PATH_RE = re.compile(r"/Users/[A-Za-z0-9._\-]+/[A-Za-z0-9._\-/]*")


def check_cat1_org_names(content: str, cfg: dict[str, Any]) -> list[tuple[str, str]]:
    hits: list[tuple[str, str]] = []
    names = cfg.get("organization_names", []) or []
    for name in names:
        if not name:
            continue
        if re.search(rf"\b{re.escape(name)}\b", content, re.IGNORECASE):
            hits.append(("cat1: organisatienaam", _redact(name)))
    return hits


def check_cat2_person_names(content: str, cfg: dict[str, Any]) -> list[tuple[str, str]]:
    hits: list[tuple[str, str]] = []
    blocked = cfg.get("person_names_to_block", []) or []
    allowed = {a.lower() for a in (cfg.get("allowed_persons", []) or [])}
    for name in blocked:
        if not name or name.lower() in allowed:
            continue
        if re.search(rf"\b{re.escape(name)}\b", content, re.IGNORECASE):
            hits.append(("cat2: persoonsnaam ≠ Steven", _redact(name)))
    return hits


def check_cat3_local_paths(content: str, cfg: dict[str, Any]) -> list[tuple[str, str]]:
    hits: list[tuple[str, str]] = []
    allowed = cfg.get("allowed_local_path_prefixes", []) or []
    for m in LOCAL_PATH_RE.finditer(content):
        path = m.group(0)
        if any(path.startswith(prefix) for prefix in allowed):
            continue
        hits.append(("cat3: lokaal pad buiten repo", _redact(path)))
    # Dedup
    seen: set[tuple[str, str]] = set()
    out: list[tuple[str, str]] = []
    for h in hits:
        if h not in seen:
            seen.add(h)
            out.append(h)
    return out


def check_cat4_emails_tlds(content: str, cfg: dict[str, Any]) -> list[tuple[str, str]]:
    hits: list[tuple[str, str]] = []
    allowed_emails = {e.lower() for e in (cfg.get("allowed_emails", []) or [])}
    allowed_persons = {a.lower() for a in (cfg.get("allowed_persons", []) or [])}
    org_domains = [d.lower() for d in (cfg.get("organization_email_domains", []) or [])]
    org_tlds = [t.lower() for t in (cfg.get("organization_tlds", []) or [])]
    for m in EMAIL_RE.finditer(content):
        email = m.group(0)
        e_low = email.lower()
        if e_low in allowed_emails:
            continue
        local, _, domain = e_low.partition("@")
        if local in allowed_persons:
            continue
        if any(domain == d or domain.endswith("." + d) for d in org_domains):
            hits.append(("cat4: organisatie-e-mail", _redact(email)))
            continue
        # Whitelist publieke voorbeelden die in protocol-docs voorkomen.
        if domain in {"example.org", "example.com", "claude.ai", "anthropic.com",
                       "github.com", "noreply.github.com"}:
            continue
        hits.append(("cat4: e-mail (review)", _redact(email)))
    # Organisatie-specifieke TLD-detectie (los van e-mail).
    for tld in org_tlds:
        if not tld:
            continue
        if re.search(rf"\b[A-Za-z0-9._\-]+\.{re.escape(tld)}\b", content, re.IGNORECASE):
            hits.append(("cat4: organisatie-TLD", _redact(f"*.{tld}")))
    return hits


def _redact(s: str) -> str:
    if len(s) <= 6:
        return s[:2] + "…"
    return s[:3] + "…" + s[-3:]


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception as e:
        print(f"disclosure-check: stdin-parse-fout ({e}); allow-by-default", file=sys.stderr)
        return 0

    tool_name = payload.get("tool_name", "")
    if tool_name not in {"Write", "Edit"}:
        return 0

    tool_input = payload.get("tool_input", {}) or {}
    file_path, content = extract_payload(tool_name, tool_input)
    if not content:
        return 0

    cfg = load_config()
    if not cfg:
        # Config ontbreekt — degradeer naar allow met waarschuwing.
        print("disclosure-check: config ontbreekt — geen scan uitgevoerd", file=sys.stderr)
        return 0

    if file_path and not in_scope(file_path, cfg):
        return 0

    hits: list[tuple[str, str]] = []
    hits += check_cat1_org_names(content, cfg)
    hits += check_cat2_person_names(content, cfg)
    hits += check_cat3_local_paths(content, cfg)
    hits += check_cat4_emails_tlds(content, cfg)

    if not hits:
        return 0

    print("disclosure-check: Protocol-14-categorie geraakt — BLOCK", file=sys.stderr)
    print(f"  bestand: {file_path}", file=sys.stderr)
    for label, redacted in hits:
        print(f"  hit: {label} ≈ {redacted}", file=sys.stderr)
    print(
        "  actie: parafraseer, anonimiseer naar 'de organisatie', of haal regel weg. "
        "Bij vals-positief: voeg term toe aan allowed_* in disclosure-config.local.json.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
