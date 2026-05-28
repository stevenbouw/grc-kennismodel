---
name: applier-template
description: Template-architectuur voor een ontologie-patch-applier (Protocol 15 — Tech levert werkbare applier). Codificeert de canonical pattern uit T1+T2+T3-precedenten (apply_patch_v4_6_1.py / _v4_6_2.py / _v4_6_3.py) met dry-run-default, --apply-flag, backup-vóór-write, hard-coded MUTATIONS-set uit eindrapport, idempotentie-check, per-mutatie-logging, en file-hash-verificatie. Use when preparing a patch-applier voor T-sprint Stap 3 of minor-release patch. Levert ARCHITECTUUR + CHECKLIST, geen verbatim code-kopie.
---

# applier-template — ontologie-patch-applier (Protocol 15)

Codificeert de canonical applier-architectuur uit T1+T2+T3-precedenten. §0.5-firewall: dit is een TEMPLATE-skill, geen auto-execute. Genereert architectuur + checklist; Tech schrijft + Steven inspecteert + draait handmatig (eerst dry-run, daarna `--apply`).

## Wanneer aanroepen

- Bij voorbereiding van ontologie-patch in T-sprint Stap 3 (SKOS-mutaties / predicate-substituties)
- Bij minor-release patch met ABox- of SKOS-mutaties
- Bij elke sprint waar mutaties op .ttl-bestand worden uitgevoerd (Protocol 15 verplicht: Tech levert werkbare applier, geen alleen-specificatie)

## Verplichte template-elementen (Protocol 15 + T1/T2/T3-precedent)

| # | Element | Toelichting |
|---|---|---|
| 1 | **Dry-run-modus default** | Aanroep zonder flags = read-only rapport (welke mutaties zouden plaatsvinden, met counts). Geen file-mutatie. |
| 2 | **`--apply`-flag voor productie** | Expliciete opt-in voor write. Default veilig. |
| 3 | **Backup vóór write** | Pre-write kopie: `<module>.<ext>.v<vorige>.bak` of vergelijkbaar. Restore-pad expliciet in script-docstring. |
| 4 | **Hard-coded MUTATIONS-set** | Mutaties als constant-list bovenaan; bron = eindrapport (T3 Stap 3-eindrapport / patch-rapport-§6.x). Geen runtime-discovery. |
| 5 | **Integratie-test ingebakken** | Aantal mutaties matcht specificatie + geen onbedoelde nevenwijzigingen + (optioneel) file-hash van resultaat matcht verwachting uit canonical-metrics. |
| 6 | **Eén applier voor alle mutatie-types in scope** | Upgrade + downgrade + richtings-correctie in één script — geen aparte scripts per type. Type-veld in MUTATIONS-record. |
| 7 | **Per-mutatie-logging** | Per mutatie: subject-IRI, predicate-from, predicate-to (+ richting / type-veld). Stdout + optioneel log-file. |
| 8 | **Idempotentie-check** | Rerun van applier (na succesvolle eerste run) detecteert dat mutaties al toegepast zijn en faalt netjes met heldere melding. Voorkomt dubbel-toepassing. |
| 9 | **Faal-veilig-exit** | Bij elke mismatch (specificatie ↔ werkelijkheid) exit-code ≠ 0 + duidelijke stderr. Geen "doe-toch-maar"-pad. |

## Canoniek architectuur-skelet

```python
#!/usr/bin/env python3
"""
apply_patch_v4_X_Y.py — <korte-naam-mutaties> patch v4.X.Y (T<N>-sprint, <module>).

<N> mutaties op `ontology/<module>.ttl` volgend uit T<N> Stap 3-eindrapport en
het masterchat-besluit op de pilot-escalatie (T<N> §X.Y → Optie <A/B/C>):

    T<N>-001  <subj>  <predicate-from>  <obj>  → <predicate-to>
    T<N>-002  <subj>  <predicate-from>  <obj>  → <predicate-to>
    ...

Grond: <kort de architectonische rationale — bv. cross-category-relatie is associatief
niet subsumptief / predicate-symmetrie-correctie / etc.>

Twee modi:
    DRY-RUN (default — geen file-mutatie, alleen rapport):
        python3 scripts/apply_patch_v4_X_Y.py

    PRODUCTIE (alleen na bevestiging van eindrapport-classificatie):
        python3 scripts/apply_patch_v4_X_Y.py --apply

Veilig: maakt backup vóór wijziging; faalt netjes als getallen niet kloppen.
Volgt Protocol 15 (Tech levert werkbare applier).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
TTL_PATH = REPO_ROOT / "ontology" / "<module>.ttl"
BACKUP_PATH = REPO_ROOT / "ontology" / "<module>.ttl.v4_X_(Y-1).bak"

# Mutatie-set — hard-coded uit T<N> Stap 3-eindrapport.
MUTATIONS = [
    {
        "pair_id": "T<N>-001",
        "subject": "<ns>:<subj>",
        "object": "<ns>:<obj>",
        "current_predicate": "skos:<from>",
        "target_predicate": "skos:<to>",
        "type": "<downgrade|upgrade|richtings-correctie>",
        "rationale": "<korte-bron-verwijzing-eindrapport-§>",
    },
    # ...
]


def apply_one_mutation(content: str, m: dict) -> tuple[str, int]:
    """Vervang één mutatie. Return (nieuw-content, aantal-vervangingen)."""
    # Regex per mutatie-type. Voorbeeld voor SKOS-predicate-substitutie:
    pattern = rf"({re.escape(m['subject'])}\s+){re.escape(m['current_predicate'])}(\s+{re.escape(m['object'])})"
    replacement = rf"\g<1>{m['target_predicate']}\g<2>"
    new_content, n = re.subn(pattern, replacement, content)
    return new_content, n


def run(apply_mode: bool) -> int:
    if not TTL_PATH.exists():
        print(f"FATAL: {TTL_PATH} niet gevonden", file=sys.stderr)
        return 2

    content = TTL_PATH.read_text(encoding="utf-8")
    total_planned = len(MUTATIONS)

    # PRE-CHECK + DRY-RUN-RAPPORT
    print(f"=== apply_patch v4.X.Y — {'PRODUCTIE' if apply_mode else 'DRY-RUN'} ===")
    print(f"Module: {TTL_PATH.relative_to(REPO_ROOT)}")
    print(f"Geplande mutaties: {total_planned}")

    found_per_mutation: list[tuple[dict, int]] = []
    for m in MUTATIONS:
        # Tel huidige voorkomens van source-pattern
        pattern_current = rf"{re.escape(m['subject'])}\s+{re.escape(m['current_predicate'])}\s+{re.escape(m['object'])}"
        n_current = len(re.findall(pattern_current, content))
        # Idempotentie-check: tel target-pattern
        pattern_target = rf"{re.escape(m['subject'])}\s+{re.escape(m['target_predicate'])}\s+{re.escape(m['object'])}"
        n_target = len(re.findall(pattern_target, content))
        found_per_mutation.append((m, n_current))
        status = "PENDING" if n_current == 1 else ("ALREADY APPLIED" if n_target == 1 else "MISMATCH")
        print(f"  {m['pair_id']:>10} {m['subject']:>30} {m['current_predicate']:>16} → {m['target_predicate']:>16}  [{status}]")

    # Validate alle mutaties exact 1 voorkomen (PENDING) hebben — anders fail
    n_pending = sum(1 for _, n in found_per_mutation if n == 1)
    n_already = sum(1 for m, n in found_per_mutation if n == 0
                    and len(re.findall(rf"{re.escape(m['subject'])}\s+{re.escape(m['target_predicate'])}\s+{re.escape(m['object'])}", content)) == 1)
    n_mismatch = total_planned - n_pending - n_already

    if n_mismatch > 0:
        print(f"\nFATAL: {n_mismatch} mutaties hebben een MISMATCH-status. Geen file-mutatie.", file=sys.stderr)
        return 2

    if n_already == total_planned:
        print(f"\n✓ Alle {total_planned} mutaties zijn al toegepast (idempotentie). Geen actie.")
        return 0

    if not apply_mode:
        print(f"\nDRY-RUN: {n_pending} mutaties zouden worden toegepast.")
        print("Run opnieuw met --apply om door te voeren.")
        return 0

    # PRODUCTIE: backup + write
    print(f"\n→ Backup naar {BACKUP_PATH.relative_to(REPO_ROOT)}")
    BACKUP_PATH.write_text(content, encoding="utf-8")

    new_content = content
    for m in MUTATIONS:
        new_content, n = apply_one_mutation(new_content, m)
        if n != 1:
            print(f"FATAL: mutatie {m['pair_id']} toegepast {n}× (verwacht 1). Restore vereist.", file=sys.stderr)
            return 2

    TTL_PATH.write_text(new_content, encoding="utf-8")
    print(f"\n✓ {total_planned} mutaties toegepast op {TTL_PATH.relative_to(REPO_ROOT)}")
    print(f"✓ Backup: {BACKUP_PATH.relative_to(REPO_ROOT)}")
    print(f"\nVervolg: draai /canonical-metrics + /shacl-split en valideer §0 + §7 in patch-rapport.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="T<N> v4.X.Y SKOS-patch applier (<module>)")
    parser.add_argument("--apply", action="store_true",
                        help="Productie-modus: voer mutaties daadwerkelijk uit (default: dry-run)")
    args = parser.parse_args()
    return run(apply_mode=args.apply)


if __name__ == "__main__":
    sys.exit(main())
```

## Lokatie-conventie

| Versie | Lokatie | Status |
|---|---|---|
| v4.6.1 (T1) | `apply_patch_v4_6_1.py` (repo-root) | Eerste applier — locatie afwijkend van convention |
| v4.6.2 (T2) | `output/scripts/apply_patch_v4_6_2.py` | Afwijking gemarkeerd in eindrapport |
| v4.6.3 (T3) | `scripts/apply_patch_v4_6_3.py` | **Canonieke locatie** vanaf T3 |
| v4.6.4+ (T4...) | `scripts/apply_patch_v4_X_Y.py` | Volg T3-locatie |

T1/T2-afwijkingen zijn historisch. Vanaf T4: `scripts/apply_patch_v4_X_Y.py`.

## Verplichte integratie-test vóór `--apply`

Workflow:

1. **Dry-run draaien**: `python3 scripts/apply_patch_v4_X_Y.py`
2. **Verificeer output**:
   - Aantal PENDING-mutaties = aantal in eindrapport
   - Geen MISMATCH-status
   - Per-mutatie-line is leesbaar + verwacht
3. **Tijdelijke gepatchte kopie** (Protocol 15 §3 integratie-test):
   - Copy `<module>.ttl` naar `/tmp/<module>.test.ttl`
   - Run applier op tijdelijke kopie
   - Verifieer hash-mutatie + count-effect
4. **Indien stap 3 OK**: draai op productie met `--apply`
5. **Direct na**: `/canonical-metrics` + `/shacl-split` voor patch-rapport §0 + §7

## Afgedwongen disciplines

- **Geen runtime-discovery** van mutaties — alles hard-coded uit eindrapport (Protocol v1.3 §10.4 helper-script-autoritatief)
- **Backup vóór write** — geen "vergeten" tussenpad
- **Idempotentie-check** — rerun na succesvolle apply detecteert "already applied" + faalt netjes
- **Geen NEN-verbatim-tekst** in script-docstrings (Protocol 17 — parafrase + clausule-verwijzing)
- **Faal-veilig-exit** — bij mismatch exit ≠ 0 + duidelijke stderr; geen "best-effort"-pad
- **Logging per mutatie** — subject + predicate-from → predicate-to (+ type)

## Wat de skill NIET doet

- Geen autonome `--apply` (Steven inspecteert + draait handmatig)
- Geen autonome commit (Steven commit handmatig — §0.5-firewall)
- Geen runtime-mutatie-discovery uit ontologie
- Geen NEN-verbatim-tekst in script-output of docstrings
- Geen "best-effort"-fallback bij mismatch — strikt fail-safe
- Geen multi-module-batch (één applier per module-in-scope per release)

## Bron-precedenten (verwijzen, niet kopiëren)

| Precedent | Lokatie | Bijzonderheden |
|---|---|---|
| T1 (v4.6.1) | `apply_patch_v4_6_1.py` (repo-root) | Eerste applier; locatie afwijkend |
| T2 (v4.6.2) | `output/scripts/apply_patch_v4_6_2.py` | Locatie afwijkend (gemarkeerd in T2-eindrapport) |
| T3 (v4.6.3) | `scripts/apply_patch_v4_6_3.py` | **Canoniek voorbeeld**: 2 mutaties, dry-run-default, --apply-flag, backup, MUTATIONS-list, fail-safe-exit |

Architectuur-pattern + checklist hierboven; geen verbatim code-kopie.

## Cross-references

- Protocol 15 (Tech levert werkbare applier): `docs/sprint-protocols.md` §15
- Patch-rapport (§3 Mutatie-uitvoering): `.claude/skills/patch-rapport/`
- Canonical metrics (post-apply verificatie): `.claude/skills/canonical-metrics/`
- SHACL split (post-apply verificatie): `.claude/skills/shacl-split/`
- Pre-sprint-inventarisatie (mutatie-set bron): `.claude/skills/pre-sprint-inventarisatie/`
