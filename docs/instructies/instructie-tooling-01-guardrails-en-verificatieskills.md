# Instructie — Tooling-01: defensieve hooks + permissions + verificatie-skills

Spoor: A | Track: `.claude/`-tooling (GEEN ontologie-release) | Baseline: v4.6.3 (ongewijzigd)
Bron: extensie-landschap-rapport 28-05-2026 (A.5 subset / A.8 / D.1 / D.2 / C.6)
Uitvoerder: Tech-subagent (Claude Code) | Commit + push: Steven (handmatig)

## §0. KADER EN FIREWALL — lees dit eerst

Doel: maak **bestaande discipline deterministisch** onder het huidige mens-commit-regime.
Dit is NADRUKKELIJK NIET het bouwen van autonomie.

**§0.5-FIREWALL (hard).** De autonomie-koers is door masterchat geparkeerd. Bouw daarom NIET:
- geen "green-gate die autonoom committen/pushen toestaat"
- geen commit-/push-blokkade-met-sunset-env-flag (de anticipatie op autonomie)
- geen auto-merge, geen agent teams, geen CI-pijplijn
- niets dat een subagent zelfstandig laat committen/pushen

De invariant blijft hard: **subagents committen NOOIT zelfstandig; Steven inspecteert + commit handmatig.**
Als je een natuurlijke plek ziet om autonomie toe te voegen: ESCALEER naar masterchat, bouw het niet.

Geen ontologie-wijziging. `ontology/` + `grc-shacl.ttl` blijven byte-identiek aan v4.6.3.
Dit is `.claude/`-infrastructuur + verificatie-tooling.

## §1. DEEL A — defensieve hooks + permissions (los committeerbaar)

### A.1 Permissions (`.claude/settings.json`)
Codificeer de bestaande proza-rolscheiding uit `.claude/agents/*.md` als harde deny-regels:
- tech-subagent: `deny` write op `dashboard/**` en `.claude/**`
- dashboard-subagent: `deny` write op `ontology/**` en `.claude/**`
- brein-subagent: `deny` write op `ontology/**` en `dashboard/**`
- alle subagents: `deny` op `git commit` en `git push` (handhaaft de bestaande invariant — dit is
  GEEN §0.5-anticipatie maar het hard maken van wat nu al de regel is; géén env-flag/sunset)

### A.2 Defensieve hooks (`.claude/settings.json` → hooks + `.claude/hooks/`-scripts)
Bouw uitsluitend deze, allemaal in dienst van het huidige regime (draaien binnen de Tech-sessie
vóór hand-off aan Steven — vervangen NIET de menselijke commit):
1. **Secret-scan** (PreToolUse op Write/Edit + pre-hand-off): detecteert PAT/tokens/API-keys/
   private-key-patronen; bij hit → block + melding. Directe les uit het PAT-incident. Gebruik een
   lokaal scan-script of `grc-kennismodel:run_secret_scanning` waar passend.
2. **Disclosure-check Protocol 14, categorieën 1-4 (deterministisch)**: organisatienaam,
   persoonsnamen ≠ Steven, lokale paden buiten repo (+ NEN-licentie-pad uitgezonderd),
   credentials/TLD/e-mail. Command-hook met regex. **Categorie 5 (NEN-tekst >10 woorden) blijft
   Tech-handmatige beoordeling** — bouw daar GEEN LLM-hook voor in deze opdracht (te complex; later).
3. **Versie-suffix-check** (PostToolUse op Write naar `output/**`): waarschuwt als een deliverable
   geen versie-suffix-conventie volgt (bv. `*_v4_6_3.*`).
4. **SessionStart-context-injectie**: injecteert 3 nieuwste `brain__log.md`-entries + `git status`
   — operationaliseert de bestaande "bij sessie-start"-leesvolgorde uit `tech.md`.

### A.3 Testdiscipline (verplicht vóór activering)
Een slecht afgestelde PreToolUse-hook kan de workflow blokkeren. Per hook: dry-run/test op een
scratch-scenario (één bekend-goed + één bekend-fout geval), verifieer geen false-positive op
legitieme edits. Lever de testresultaten in het rapport. Activeer pas na groene test.

## §2. DEEL B — verificatie-skills D.1 + D.2 (los committeerbaar)

Bouw via skill-creator (C.6) indien beschikbaar; anders hand-authored SKILL.md per de officiële
skills-conventie. Skills dragen GEEN NEN-verbatim-tekst (alleen methode + clausule-verwijzing).

### B.1 `/canonical-metrics` (D.1)
Reference+action-skill die de canonieke meetmethode codificeert: `owlrl.DeductiveClosure(
OWLRL_Semantics, axiomatic_triples=False, datatype_axioms=False)`, NamedIndividual-telmethode
(`len(set(g.subjects(RDF.type, OWL.NamedIndividual)))`), de zes invariantie-metrics, versie-suffix-
conventie, en "§0 uit JSON, niet uit memorie" (leerpunt v4.3.3). Wrapt het bestaande
`canonical_metrics_v*.py`-patroon tot herbruikbare workflow.

### B.2 `/shacl-split` (D.2)
Action-skill die SECTIE A (`inference='none'`) en SECTIE B (`inference='owlrl'`) gescheiden draait
en de bekende 290 COMBINED-false-positives expliciet als verwacht OWA/CWA-fenomeen markeert
(onderbouwing: arXiv 2507.12286 — niet als modeldefect). Wrapt het bestaande
`shacl_split_validate_v*.py`-patroon.

### B.3 Trigger-test
Test (skill-creator-eval of handmatig) dat beide skills betrouwbaar triggeren en de juiste output
geven op v4.6.3 — verwacht: metrics identiek aan canonical_metrics_v4_6_3.json; SHACL A=0/B=0/
COMBINED=290. Dit dient meteen als ontologie-drift-sanity-check (bevestig: ontologie ongewijzigd).

## §3. Stop-condities (pauze + escalatie naar masterchat)
- skill-creator niet beschikbaar én hand-authoring blijkt onverwacht complex
- een hook-ontwerp kan legitieme workflow blokkeren zonder schone mitigatie
- een permission-deny zou een bestaande, noodzakelijke workflow breken
- je merkt dat een gevraagd onderdeel tegen de §0.5-firewall aanschuurt
- onverwachte ontologie-drift in de B.3-sanity-check (mag NIET optreden)

## §4. Deliverables
1. `.claude/settings.json` (permissions + hooks-config)
2. `.claude/hooks/*`-scripts (secret-scan, disclosure-1-4, versie-suffix, sessionstart)
3. `.claude/skills/canonical-metrics/SKILL.md` (+ eventueel scripts)
4. `.claude/skills/shacl-split/SKILL.md` (+ eventueel scripts)
5. `output/reports/tooling-01-implementatierapport.md` — wat gebouwd, testresultaten per hook +
   skill-trigger-test, bevestiging ontologie-ongewijzigd (v4.6.3-metrics identiek), §9 Deliverables-
   tabel met lokaties (Protocol 16), Protocol-14-disclosure-check op alle nieuwe bestanden

## §5. Discipline
- Geen autonome commit — Steven inspecteert `git status`/`git diff` + commit per deel (A en B
  apart committeerbaar)
- Start ná de T3-Brein-cyclus-commit (schone working tree; ander pad maar voorkom verwarring)
- Protocol 14 + parafrase-discipline op het implementatierapport zelf
- Géén ontologie-, beleids- of architectuurwijziging; baseline blijft v4.6.3
