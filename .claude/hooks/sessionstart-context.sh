#!/usr/bin/env bash
# sessionstart-context.sh — SessionStart hook.
#
# Operationaliseert de "bij sessie-start"-leesvolgorde uit tech.md:
# injecteert de drie nieuwste brain__log.md-entries + huidige git status.
# Output gaat naar stdout en wordt door Claude Code als additionele
# system-context geïnjecteerd in de nieuwe sessie.
#
# §0.5-firewall: pure leesactie — geen schrijfacties, geen commit, geen gate.
#
# Werking (Claude Code-hook-protocol):
# - stdin: JSON met session_id, transcript_path, source
# - stdout: tekst die als additionele context wordt geïnjecteerd
# - exit 0: succes (ook bij geen-output)

set -u

REPO_ROOT="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
LOG_FILE="${REPO_ROOT}/brain/brain__log.md"

echo "=== SessionStart context (auto-injected by .claude/hooks/sessionstart-context.sh) ==="
echo

if [[ -f "${LOG_FILE}" ]]; then
  echo "── brain/brain__log.md — 3 nieuwste entries (top-of-file) ──"
  # Eerste 80 regels — typisch dekkend voor 3 entries (entries beginnen met '## ')
  awk '
    /^## / { entries++; if (entries > 3) exit }
    { print }
  ' "${LOG_FILE}" | head -120
  echo
else
  echo "(brain__log.md niet gevonden op ${LOG_FILE})"
  echo
fi

echo "── git status (kort) ──"
( cd "${REPO_ROOT}" && git status --short --branch 2>&1 || true )
echo

echo "── git log -5 ──"
( cd "${REPO_ROOT}" && git log --oneline -5 2>&1 || true )
echo

echo "=== einde SessionStart context ==="
exit 0
