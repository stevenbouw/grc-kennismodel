# Instructie — T3 Stap 3 (hoofd-uitvoering): m14 AVG/GDPR SKOS-audit

Sprint: T3 | Stap: 3 (hoofd-uitvoering + patch) | Baseline: v4.6.2 | Doel-baseline: v4.6.3
Protocol: skos-beoordelings-protocol-v1.3 (FINAL)
Voorafgaand: pilot-rapport `output/reports/t3-pilot-rapport.md` (6/6 behoud, GO masterchat)

## Masterchat-besluit op pilot-escalatie (§5.2 pilot-rapport)

De broadMatch-richtings-bevinding is besloten als **Optie C — downgrade naar `relatedMatch`**
(NIET Optie B/narrowMatch). Gronden: control ↔ legal-obligation is een cross-category-relatie
die associatief is, niet subsumptief (Tech's eigen §3.3/§4.1/§4.4-rationale). `relatedMatch`
is symmetrisch en lost de compl→ctrl-richtingskwestie definitief op, en maakt het Art5_1f-cluster
consistent met de 5 zuster-relatedMatch-paren.

**Concreet: muteer beide m14-broadMatch-paren → `relatedMatch`:**
- T3-001 `compl:AVG_Art5_1f` broadMatch `ctrl:ISO27002_5_01` → `relatedMatch`
- T3-002 `compl:AVG_Art5_1f` broadMatch `ctrl:ISO27002_5_12` → `relatedMatch`

m10 en andere modules NIET heropenen (m10-broadMatch is formeel correct; geen retroactieve audit).

## Scope Stap 3

- Beoordeel de 25 resterende m14-paren (alle behalve de 6 pilot-paren) per-paar onder Protocol v1.3.
- Pilot-uitkomsten staan vast: T3-002 → relatedMatch (mutatie, zie boven); T3-008/T3-024/T3-028/T3-031
  behoud relatedMatch; T3-014 behoud closeMatch.
- Onder de 25 resterende valt T3-001 (broadMatch → relatedMatch per besluit) en T3-026
  (Art33 → 5.24 closeMatch — toets analoog aan T3-014: verdedigbaar behoud of downgrade?).

## Methode (ongewijzigd t.o.v. pilot)

1. Bindende T3-steers 1-5 blijven gelden (geen D4.1, geen cluster-convergentie-aanname,
   semantische basislijn relatedMatch, evidence-keten = bestaans-bewijs niet predicate-bewijs,
   closeMatch-toets op interchangeability).
2. Cross-category-rationale is leidend: control ↔ AVG-artikel = relatedMatch tenzij
   retrieval-interchangeability aantoonbaar (→ closeMatch). broad/narrowMatch niet toepassen
   tussen control en wettelijke verplichting.
3. Per-paar alle 13 velden conform Protocol v1.3 §5.

## Verwachte uitkomst (indicatief, geen pre-classificatie-mandaat)

m14-eindstand bij bevestiging: 2 closeMatch + 0 broadMatch + 29 relatedMatch.
Mutaties t.o.v. v4.6.2: 2 (T3-001 + T3-002 broadMatch → relatedMatch). Triple-neutraal.
SKOS-distributie-Δ globaal: broadMatch −2 (131→129), relatedMatch +2 (192→194).

## Stop-condities (pauze + escalatie)

- ≥3 paren confidence "laag" → pauze
- totaal voorgestelde mutaties >4 (m14-scope) → pauze; wijkt af van bevestigings-sprint-verwachting
- T3-026 of een ander paar dwingt tot een methode-vraag die het cross-category-principe raakt → escaleer

## Deliverables (Protocol 15 + 16)

1. `output/reports/t3-stap3-eindrapport.md` — per-paar-beoordeling 25 paren + cumulatief m14-overzicht
2. Werkbare applier `scripts/apply_patch_v4_6_3.py` (dry-run + `--apply`), één applier voor de 2 mutaties
3. `canonical_metrics_v4_6_3.{py,json}` + `shacl_split_validate_v4_6_3.py` → `shacl_results_v4_6_3.json`
   + `file_hashes_v4_6_3.txt`
4. `output/reports/patch-rapport-v4_6_3.md` — §0 uit canonical_metrics JSON; §9 Deliverables-tabel
   met relatieve lokaties; verwachte: alleen `m10`? NEE — alleen `ontology/m14-avg-gdpr.ttl` gewijzigd
   (let op: T3 raakt m14, niet m10). Alle andere modules + grc-shacl.ttl byte-identiek.
5. SHACL verwacht ongewijzigd (A=0, B=0, COMBINED=290) — m14 ctrl↔compl-mappings worden niet
   door een shape gevalideerd (H39-blinde-vlek, bevestigd in inventarisatie §8.4).

## Discipline

- Protocol 14 pre-push disclosure-check (5 categorieën incl. NEN-tekst >10 woorden)
- Parafrase + clausule-verwijzing; geen verbatim NEN-tekst >10 woorden
- Geen autonome commit — Steven inspecteert git status/diff en commit handmatig
- T3-leerpunt vastleggen: cross-category-principe (§4.4 pilot) als kandidaat v1.3.1-precedent
  voor Brein-cyclus na T3-afsluiting (niet nu formaliseren)
