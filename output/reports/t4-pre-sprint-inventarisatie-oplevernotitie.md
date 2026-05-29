# Oplevernotitie — T4 pre-sprint-inventarisatie

**Subagent:** Technisch (Claude Code)
**Datum:** 29 mei 2026
**Opdracht:** `docs/instructies/instructie-t4-pre-sprint-inventarisatie.md` (masterchat)
**Fase:** Protocol 1 — pre-sprint-inventarisatie, **READ-ONLY** (geen mutatie)
**Meet-laag:** ontologie-laag (rdflib parse, `inference='none'`)

---

## 1. Wat is opgeleverd

| Deliverable | Locatie |
|---|---|
| Inventarisatie-rapport (§0-§9) | `output/reports/t4-pre-sprint-inventarisatie.md` |
| Read-only helper-script | `scripts/t4_inventory_query.py` |
| Deze oplevernotitie | `output/reports/t4-pre-sprint-inventarisatie-oplevernotitie.md` |

Baseline-cijfers geciteerd uit bestaande `canonical_metrics_v4_6_3.json` + `shacl_results_v4_6_3.json` (geen her-meting nodig; SHACL A=0/B=0/COMBINED=290 — schone baseline bevestigd).

## 2. Kernbevindingen (vaststellingen — geen besluiten)

De instructie-framing ("105-overlap is vermoedelijk al correct; het werk zit in de divergentie") is **niet bevestigbaar zoals verwacht** — de inventarisatie legt een fundamenteler punt bloot: de overlap is niet uit het model afleidbaar. Drie scope-pauze-condities (instructie §5) getriggerd:

1. **Overlap ≠ 105 machine-meetbaar** (§5-A). Model-tellingen: csf↔ISO27001 mandatory clauses (eis, `ext:ISMSRequirement`) = 245 unie (m21 Sheet 8: 147 / m09 Reference Tool: 117 / intersectie 19); csf↔Annex A (measure, `bio:ISO27002` via D5-brug) = 494, uitsluitend in m21 (m09 = 0). De twee bronnen gebruikten verschillende ISO-target-resoluties → bron-overeenstemming verschijnt structureel niet als identieke triple. De 105 is een bron-niveau-getal uit v4.5.0, niet model-reproduceerbaar.
2. **Provenance niet machine-detecteerbaar** (§5-B). Attributie is bewust block-comment-niveau (masterchat v4.5.0 Stap 5-GO), geen per-triple `ext:sourceAttribution`. De concept-detection-query (`bron_count >= 2`) levert 0 op.
3. **Categorie gesplitst** (§5-C). Het ISO-eindpunt is zowel eis-categorie (clausules) als measure-categorie (Annex A); beide cross-category t.o.v. csf-outcomes. De instructie-§2-classificatievraag heeft geen enkelvoudig antwoord.

Plus: huidige predicate-status = **100% closeMatch** (conversie-default, expliciet niet OLIR-getypeerd; geen exactMatch → geen prima-facie schending). Beide XLSX-bronnen staan in `sources/` → her-afleiding 105 technisch mogelijk maar is aparte analyse-stap.

Vier beslispunten voor masterchat in rapport §9.1 (scope-eindpunt / overlap-definitie / cross-category-predicate / provenance-modellering).

## 3. Disclosure-check (vijf categorieën)

| # | Categorie | Resultaat |
|---|---|---|
| 1 | **Organisatienaam** | ✓ Schoon — 0 hits; geen organisatie genoemd |
| 2 | **Secrets** | ✓ Schoon — 0 hits |
| 3 | **NEN-verbatim >10 woorden** | ✓ Schoon — geen ISO-normtekst geciteerd; ISO-eindpunten alleen via clausule-/Annex-A-verwijzing + parafrase. NEN-aanraking expliciet vastgesteld als "parafrase volstaat" (rapport §4.3). **Belangrijkste categorie bij read-only-analyse (instructie §7) — bevestigd schoon.** |
| 4 | **Mutatie-bewaking** | ✓ `git status ontology/` leeg — geen TTL/applier/patch aangeraakt; geen herklassificatie. Alleen 2 nieuwe rapport-bestanden + 1 read-only helper-script untracked |
| 5 | **Status-/D-discipline** | ✓ Framework-neutraal (D9; CSF noch ISO als hub); cross-category-principe alleen als T3-precedent/v1.3.1-kandidaat genoemd, niet geformaliseerd; geen architectuurbeslissing genomen |

## 4. Scope-bewaking

Conform instructie: **vastgesteld, niet beslist.** Geen pilot, geen Stap 3, geen mutatie, geen scope-keuze. De drie scope-pauze-condities zijn als bevindingen in het rapport gemeld (§5) met expliciete beslispunten voor masterchat (§9.1), niet zelf opgelost. Sample-keuze (§6) is indicatief en scope-afhankelijk opengelaten (geen pre-pilot-uitkomst-classificatie, Protocol v1.3 §6 stop-conditie-4).

## 5. Git-context (voor Steven)

- **Repo-staat bij start:** lokaal ahead 1 (B7 dashboard-commit, niet van mij) + behind 1 (T4-instructie op origin/main). Ik heb **niet gemerged/gepulld** — divergente merge is een history-mutatie die onder de commit-invariant valt. De T4-instructie heb ik read-only uit `origin/main` gelezen (`git show`). **Jij beslist over de reconciliatie** (merge/rebase) en de commit.
- **Nieuwe bestanden (untracked):** `output/reports/t4-pre-sprint-inventarisatie.md`, `output/reports/t4-pre-sprint-inventarisatie-oplevernotitie.md`, `scripts/t4_inventory_query.py`.
- Subagent commit niet zelfstandig (§0.5-firewall). `git status`/`git diff` ter inspectie.

— Einde oplevernotitie T4.
