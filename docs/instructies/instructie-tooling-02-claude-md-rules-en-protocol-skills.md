# Instructie — Tooling-02: CLAUDE.md-herstructurering + `.claude/rules/` + protocol-skills

Spoor: A | Track: `.claude/`-tooling (GEEN ontologie-release) | Baseline: v4.6.3 (ongewijzigd)
Bron: extensie-landschap-rapport 28-05-2026 (A.1 / D.3 / D.6-subset)
Uitvoerder: Tech-subagent (Claude Code) | Commit + push: Steven (handmatig)
Vooraf: Tooling-01 (hooks + permissions + D.1/D.2-skills) gecommit.

## §0. KADER EN FIREWALL

Doel: de always-on-context afslanken en herhaalde protocol-discipline van proza naar
aanroepbaar/path-geladen tillen. Géén autonomie-bouw.

**§0.5-FIREWALL (hard, ongewijzigd):** geen autonome commit/push-paden, geen green-gate-voor-
autonomie, geen agent teams/CI/auto-merge. De invariant "subagents committen NOOIT zelfstandig"
blijft hard. Bij aanschuring: escaleer, bouw niet.

**Invariant-bescherming (kritisch voor Deel A):** de always-on-invarianten MOGEN NIET verzwakken.
D9-framework-neutraliteit, "geen organisatienaam", NEN-parafrase-discipline, status-discipline
(CBW "in voorbereiding" / Cbb "concept"), BBN-correctie, en "subagents committen nooit zelfstandig"
blijven volledig in CLAUDE.md. Bij twijfel of iets invariant-of-reference is: LAAT HET IN CLAUDE.md
staan (bias naar behoud).

Geen ontologie-wijziging. Baseline blijft v4.6.3.

## §1. DEEL A — CLAUDE.md-herstructurering + `.claude/rules/`

### A.0 Pre-check
Verifieer dat `.claude/rules/` met `paths`-frontmatter wordt ondersteund in de actuele Claude Code-
versie (officiële docs). Indien NIET ondersteund → stop-conditie: meld het, en houd de inhoud in
CLAUDE.md of een skill in plaats van rules. Geen aanname.

### A.1 CLAUDE.md afslanken (conservatief)
- Houd in CLAUDE.md: alle always-on-invarianten (zie §0), de kern-rolverdeling, en verwijzingen.
- Verplaats UITSLUITEND aantoonbaar reference-materiaal naar `.claude/rules/` of skills:
  bv. gedetailleerde repo-structuur-beschrijving, Karpathy-laag-detail, optional-tooling-lijsten.
- Geen big-bang: verplaats alleen wat onmiskenbaar reference is.
- Lever in het rapport een expliciete **"verplaatst / gebleven"-tabel** zodat masterchat kan
  reviewen wat uit de always-on-laag is gehaald. Volledig reversibel.

### A.2 `.claude/rules/` aanmaken (path-geladen regels)
Minimaal twee path-scoped rules (uitbreidbaar):
1. `ontology-conformance.md` — `paths: ontology/*.ttl` — D1–D12 + D4.1-conformance-checklist
   (geen verbatim normtekst; alleen de design-decision-regels).
2. `report-structure.md` — `paths: output/reports/*` — patch-rapport-skelet-verwijzing (zie Deel B)
   + bron-typo-beleid (Protocol 13) + Protocol v1.3 §10.2-§10.5 (bottom-up, tabel-consistentie,
   helper-script-autoritatief, metrics-scope-annotatie).

Dit absorbeert de "reference-rules"-subset van D.6; de hook-subset van D.6 is al in Tooling-01 gedaan.

## §2. DEEL B — `/patch-rapport`-skill (D.3)

Action-skill `.claude/skills/patch-rapport/SKILL.md` die het §0–§15-skelet genereert (conform
de bestaande v4.6.2/v4.6.3-patch-rapport-structuur), met afgedwongen:
- §0 dwingend uit `output/verification/canonical_metrics_v*.json` (niet uit memorie — leerpunt v4.3.3)
- §9 geparkeerde-items-status (Protocol 10) + Deliverables-tabel met lokaties (Protocol 16)
- D-decision-conformiteit-check (D1–D12 + D4.1)
- koppeling met `/canonical-metrics` + `/shacl-split` (Tooling-01) voor de cijfer-secties
Geen NEN-verbatim-tekst. Test op trigger + skelet-generatie tegen v4.6.3-cijfers.

## §3. DEEL C — protocol-command (optioneel, lichtgewicht)

`/pre-sprint-inventarisatie` (Protocol 1) als action-command/skill: genereert het inventarisatie-
skelet (ABox-baseline, cluster-cardinaliteit, evidence-coverage, scope-bevestiging). Alléén bouwen
als Deel A+B niet te groot worden; anders deferren naar een volgende tooling-instructie. De volledige
17-protocol-mapping is bewust NIET in deze opdracht — alleen dit hoogst-herhaalde protocol.

## §4. DEEL D — optioneel, alleen op expliciete go van Steven: pad-neutralisatie (actiepunt 2)

Indien Steven dit aanvinkt: verplaats `allowed_local_path_prefixes` (en eventueel `allowed_persons`
+ `allowed_emails`) uit de versioned `disclosure-config.json` (→ lege arrays) naar
`disclosure-config.local.json` (gitignored). Test daarna dat disclosure-check nog groen draait met
de lokale config aanwezig. Dient de organisatie-neutraliteit-invariant. NIET uitvoeren zonder go.

## §5. Stop-condities (pauze + escalatie)
- `.claude/rules/` niet ondersteund in de actuele versie
- twijfel of een CLAUDE.md-regel invariant-of-reference is → laat staan + flag (niet gokken)
- een verplaatsing zou een always-on-invariant uit de always-on-laag halen
- §0.5-firewall-aanschuring
- onverwachte ontologie-drift (mag niet optreden)

## §6. Deliverables
1. Afgeslankte `CLAUDE.md` (versie-bump in de file zelf)
2. `.claude/rules/ontology-conformance.md` + `.claude/rules/report-structure.md`
3. `.claude/skills/patch-rapport/SKILL.md`
4. (optioneel) `.claude/commands|skills/pre-sprint-inventarisatie`
5. (optioneel, op go) gewijzigde `disclosure-config.json` + uitgebreide local-config-instructie
6. `output/reports/tooling-02-implementatierapport.md` — met de "verplaatst/gebleven"-tabel,
   skill-trigger-test, ontologie-ongewijzigd-bevestiging, Protocol-16-deliverables-tabel,
   Protocol-14-disclosure-check op nieuwe bestanden

## §7. Discipline
- Geen autonome commit — Steven inspecteert `git status`/`git diff` + commit (delen los committeerbaar)
- Schone working tree bij start (Tooling-01 + T3-Brein gecommit)
- Protocol 14 + parafrase-discipline op het rapport
- Géén ontologie-/beleids-/architectuurwijziging; baseline blijft v4.6.3
