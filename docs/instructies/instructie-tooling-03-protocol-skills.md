# Instructie — Tooling-03: `/pre-sprint-inventarisatie` (+ optioneel `/applier-template`)

Spoor: A | Track: `.claude/skills/` (GEEN ontologie-release) | Baseline: v4.6.3 (ongewijzigd)
Bron: extensie-landschap-rapport 28-05-2026 (D.6-action-skills-subset) + Tooling-02-rapport §6 + §12
Uitvoerder: Tech-subagent (Claude Code) | Commit + push: Steven (handmatig)
Vooraf: Tooling-02 gecommit + gepusht.

## §0. KADER EN FIREWALL

Doel: de meest-herhaalde T-sprint-stappen van proza naar aanroepbaar tillen. Daarmee is de
protocol-skill-laag dekkend voor canonical metrics / SHACL-split / patch-rapport / inventarisatie
(+ optioneel applier-template) — de hoofdwerkzaamheden van elke kwaliteitsanalyse-sprint.

**§0.5-FIREWALL (hard, ongewijzigd):** geen autonomie-bouw. /pre-sprint-inventarisatie is een
*generator van een leesbaar skelet*, niet een autonome sprint-uitvoerder. Geen auto-execute,
geen ABox-mutaties, geen autonome scope-keuzes — masterchat blijft de scope vaststellen.

Geen ontologie-wijziging. Baseline blijft v4.6.3. Geen wijziging aan CLAUDE.md of bestaande skills.

## §1. DEEL A — `/pre-sprint-inventarisatie`-skill (Protocol 1)

### A.1 Lokatie + activatie

- Lokatie: `.claude/skills/pre-sprint-inventarisatie/SKILL.md`
- Activatie: description-triggered (geen `paths:`)
- Aanroep: door Tech bij start van een nieuwe T-sprint, na masterchat-scope-vaststelling

### A.2 Skill-inhoud (verplichte secties)

**Wanneer aanroepen:** bij elke T-sprint na masterchat-scope-instructie en vóór Stap-2-pilot.
Vereist als input: sprint-naam (T4, T5, ...), scope-module(s) (m11/m14/m16/m17/...), audit-richting
(ctrl→compl of compl→ctrl), baseline-versie (v(Y-1)).

**Dependencies (referentieel):** `/canonical-metrics` voor ABox-baseline, `/shacl-split` voor
SHACL-baseline, Protocol v1.3 voor sample-keuze + werkflow-discipline, D-decisions register.

**Bouw-volgorde:** bottom-up conform Protocol v1.3 §10.2 — details (§2-§5) eerst, scope-bevestiging
en GO-criteria (§1, §8) laatst. Markeer §1 vroeg-invullen als "INITIEEL, TE BEVESTIGEN IN §3-§5-ITERATIE".

**Canoniek §-skelet voor de gegenereerde inventarisatie:**

| § | Sectie | Bron / discipline |
|---|---|---|
| §0 | Frontmatter (sprint, baseline, datum, scope-module, audit-richting) | Input + Protocol 16 |
| §1 | Sprint-scope-bevestiging (instructie-§-naar-doel-mapping) | Masterchat-instructie; INITIEEL → bevestigen |
| §2 | ABox-baseline | UIT `output/verification/canonical_metrics_v(Y-1).json` — NIET uit memorie (leerpunt v4.3.3) |
| §3 | Cluster-cardinaliteit per module-in-scope (object-cluster + subject-cluster, multi-mapping-flag) | SPARQL/script-output; Protocol v1.3 §2.2 |
| §4 | Evidence-coverage-pre-check (sources/-doorzoek + lokale NEN-toegang per cluster) | Protocol v1.3 §2.4 evidence-niveau-1-pre-stap; Protocol 17 (NEN-werkverdeling) |
| §5 | Risico-inventarisatie + stop-condities-voorstel | Protocol v1.3 §6 |
| §6 | Sample-keuze-voorstel (5-10 paren, spreiding-richtlijnen) | Protocol v1.3 §6 sample-keuze |
| §7 | Verwachte uitkomst (indicatief, GEEN pre-classificatie-mandaat) | Protocol v1.3 §6 stop-conditie-4 |
| §8 | GO/NO-GO-criteria expliciet | Masterchat-eindbesluit |
| §9 | Hand-off + Deliverables-tabel (Protocol 16) + verwijzingen | Protocol 16 |

**Afgedwongen disciplines:**

- §2 dwingend uit canonical_metrics JSON (Protocol v1.3 §10.4 helper-script-autoritatief)
- §3+§4 metrics-scope-annotatie (Protocol v1.3 §10.5 — m10-only / m14-only / cross-module)
- §6 geen pre-pilot-uitkomst-verwachting per paar (Protocol v1.3 §6)
- §1 expliciet markeren als "INITIEEL, TE BEVESTIGEN" bij bottom-up bouw
- Bron-typo-beleid (Protocol 13) op alle ABox-citaten
- Geen NEN-verbatim-tekst (Protocol 17 parafrase-discipline)

### A.3 Trigger-test verplicht

Test door skelet te genereren voor T3 (sprint waarvoor de werkelijke inventarisatie bestaat:
`output/reports/t3-pre-sprint-inventarisatie.md`) en vergelijken op:

- §-structuur: 1:1 match met §0-§9
- ABox-baseline: cijfers uit canonical_metrics_v4_6_2.json (T3-baseline) corresponderen
- Cluster-cardinaliteit: m14-cluster-tellingen reproduceerbaar
- Geen NEN-verbatim-tekst

Verwacht: skill-skelet is structureel consistent met de hand-gemaakte T3-inventarisatie.
Inhoudelijke verschillen (parafrase-keuzes etc.) zijn acceptabel; structurele afwijking is stop-conditie.

## §2. DEEL B — `/applier-template`-skill (optioneel, Protocol 15)

**Alleen bouwen als Deel A niet uitloopt** (Tooling-02-precedent: Deel C deferraal-discipline).

### B.1 Lokatie + activatie

- Lokatie: `.claude/skills/applier-template/SKILL.md`
- Activatie: description-triggered
- Aanroep: door Tech bij voorbereiding van een patch-applier (T-sprint Stap 3 / minor-release patch)

### B.2 Skill-inhoud

**Wanneer aanroepen:** bij elke ontologie-patch waar mutaties op ABox-/SKOS-niveau worden uitgevoerd.

**Verplichte template-elementen** (uit Protocol 15 + T1/T2/T3-precedent):

- Dry-run-modus (default)
- `--apply`-flag voor productie-modus
- Integratie-test ingebakken: aantal mutaties matcht specificatie, geen onbedoelde
  nevenwijzigingen, file-hash van resultaat matcht canonical-metrics-verwachting
- Eén applier voor alle mutatie-types in scope (upgrade + downgrade + richtings-correctie),
  geen aparte scripts per type
- Logging per mutatie (subject-IRI, predicate-from, predicate-to)
- Idempotentie-check (rerun zonder veranderingen)

**Bron-precedenten** (verwijzen, niet kopiëren):

- T1: `scripts/apply_patch_v4_6_1.py`
- T2: `scripts/apply_patch_v4_6_2.py`
- T3: `scripts/apply_patch_v4_6_3.py`

Geen verbatim code-kopie; alleen de architectuur-pattern + checklist.

### B.3 Trigger-test

Genereer template-skelet en vergelijk structureel met `apply_patch_v4_6_3.py`. Structurele match
vereist (dry-run + --apply + integratie-test + logging). Code-inhoud-verschil acceptabel.

## §3. Stop-condities (pauze + escalatie naar masterchat)

- /pre-sprint-inventarisatie trigger-test toont structurele afwijking van T3-precedent
- Sub-element uit Protocol v1.3 §6 sample-keuze blijkt niet codificeerbaar als skill-tekst
  (te veel context-afhankelijk per sprint)
- Deel A loopt uit → Deel B deferren naar Tooling-04 (volg Tooling-02-precedent)
- §0.5-firewall-aanschuring (geen "auto-execute"-bouw onder welke framing dan ook)
- Onverwachte ontologie-drift in B.3-sanity (mag niet optreden — geen ontologie-werk in scope)

## §4. Deliverables
1. `.claude/skills/pre-sprint-inventarisatie/SKILL.md`
2. (optioneel, Deel B) `.claude/skills/applier-template/SKILL.md`
3. `output/reports/tooling-03-implementatierapport.md` met:
   - §0 firewall-bevestiging + scope-conformiteit
   - §1 /pre-sprint-inventarisatie skill-content-samenvatting
   - §2 trigger-test-resultaten tegen T3-precedent (§-match + cijfer-match)
   - §3 (optioneel) /applier-template skill + trigger-test tegen v4.6.3-applier
   - §4 ontologie-drift-sanity (verwacht: geen drift, geen ontologie-werk in scope)
   - §5 Protocol-14-disclosure-check op alle nieuwe bestanden
   - §6 Protocol-16 deliverables-tabel
   - §7 commit-suggestie(s)
   - §8 stop-condities (verwachting: geen getriggerd)
   - §9 verdere overwegingen voor eventuele Tooling-04 (indien relevant)

## §5. Discipline

- Geen autonome commit — Steven inspecteert `git status`/`git diff` + commit handmatig
- Schone working tree bij start (Tooling-02 gecommit)
- Protocol 14 + parafrase-discipline op het rapport zelf
- Géén ontologie-/beleids-/architectuurwijziging; baseline blijft v4.6.3
- Géén CLAUDE.md-wijziging in deze opdracht; alleen `.claude/skills/`-additions
