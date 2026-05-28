# Tooling-01 implementatierapport — defensieve hooks + permissions + verificatie-skills

| Veld | Waarde |
|---|---|
| Spoor | A |
| Track | `.claude/`-tooling (geen ontologie-release) |
| Baseline | v4.6.3 (ongewijzigd) |
| Bron-instructie | `docs/instructies/instructie-tooling-01-guardrails-en-verificatieskills.md` |
| Uitvoerder | Tech-subagent (Claude Code) |
| Datum | 2026-05-28 |
| Commit + push | Steven (handmatig — Protocol §5 + §0.5-firewall) |

## §0. Kader-bevestiging en §0.5-firewall-conformiteit

Doel van deze opdracht: bestaande discipline deterministisch maken onder het huidige mens-commit-regime. Geen autonomie-bouw.

Conformiteit aan §0.5-firewall — wat NIET is gebouwd, ondanks dat de gelegenheid voorkwam:

| §0.5-verbod | Status | Toelichting |
|---|---|---|
| Geen "green-gate die autonoom committen toestaat" | OK | `Bash(git commit:*)` en `Bash(git push:*)` zijn in `.claude/settings.json` als `deny` opgenomen. Geen tegen-mechanisme dat dit ontsluit. |
| Geen commit-/push-blokkade-met-sunset-env-flag | OK | De deny-regels hebben geen env-flag-override en geen vervaldatum. Permanent voor Claude Code-context. |
| Geen auto-merge, geen agent teams, geen CI-pijplijn | OK | Alleen lokale, defensieve hooks (PreToolUse / PostToolUse / SessionStart). Geen CI, geen GitHub Actions-additions, geen orchestratie. |
| Niets dat een subagent zelfstandig laat committen/pushen | OK | Permission-deny + ontbreken van enige commit-helper. De hooks BLOKKEREN; ze openen niets. |
| Geen ontologie-wijziging | OK | Werking geverifieerd in §3 (B.3 trigger-test): canonical metrics + SHACL identiek aan v4.6.3-baseline. |

Géén natuurlijke escalatie-route richting autonomie aangetroffen tijdens uitvoering. Geen subagent-zelf-commit-functionaliteit gebouwd of voorbereid.

## §1. Deel A — defensieve hooks + permissions

### §1.1 Permissions (`.claude/settings.json`)

Toegevoegd:

- `deny`: `Bash(git commit:*)`, `Bash(git commit *)`, `Bash(git push:*)`, `Bash(git push *)`
  — codificeert de bestaande regel "subagents committen NOOIT zelfstandig" als harde Claude Code-deny. Steven commit handmatig vanuit zijn shell (buiten Claude Code) zonder hinder.
- `ask`: destructieve git-acties (`reset`, `restore`, `checkout`, `rebase`, `merge`) + `rm -r`/`rm -rf` — vragen expliciete toestemming i.p.v. silently allowen.
- `allow`: read-only operaties + `python3 *` (verificatie-scripts) + niet-destructieve git-verbose (`status`, `diff`, `log`, `fetch`, `pull`, `branch`).

**Per-subagent path-denies** (tech: `dashboard/**` + `.claude/**`; brein: `ontology/**` + `dashboard/**`; dashboard: `ontology/**` + `.claude/**`): NIET geïmplementeerd in `settings.json` om twee redenen:

1. Claude Code's permission-deny-patronen werken project-wide, niet per-subagent. `Write(dashboard/**)` als global-deny breekt de dashboard-subagent zelf.
2. Per-subagent-discriminatie zou een PreToolUse-hook vereisen die agent-context inspecteert. Dat valt buiten de A.2-hook-set (4 expliciete hooks); een 5e hook toevoegen zou scope-creep zijn.

Mitigatie: de rolscheiding blijft proza in `.claude/agents/*.md` (per tech.md §"Lees- en schrijfrechten"), zoals voorheen. Dit is **niet** verzwakt t.o.v. de pre-implementatie-staat. Aanbeveling voor opvolger-instructie: overweeg agent-context-aware PreToolUse-hook **alleen** als incidenten optreden die het rechtvaardigen (anders: YAGNI).

### §1.2 Defensieve hooks (`.claude/hooks/`)

Vier scripts + één config:

| Hook | Bestand | Type | Matcher | Rol |
|---|---|---|---|---|
| Secret-scan | `secret-scan.py` (120 regels) | PreToolUse | `Write\|Edit` | Detecteert PAT/tokens/API-keys/PEM-private-key/JWT/AWS-id/Google-key/Slack-token in tool-input. Block (exit 2) bij hit, met redacted snippet. Placeholder-context (`mock_/dummy_/example_/<your-...>/XXXX/EXAMPLE/REDACTED`) whitelisten op regel-niveau. |
| Disclosure-check | `disclosure-check.py` (219 regels) + `disclosure-config.json` (26 regels) | PreToolUse | `Write\|Edit` | Protocol 14 categorieën 1-4: organisatienaam, persoonsnamen ≠ Steven, lokale paden buiten repo (allow-list: repo + NEN-licentie-pad), e-mail-domeinen + organisatie-TLD's. Categorie 5 (NEN-tekst >10 woorden) **bewust uitgesloten** — handmatige Tech-beoordeling per A.2. Config-driven via versioned `disclosure-config.json` (placeholders) + gitignored `disclosure-config.local.json` (echte waarden). |
| Versie-suffix-check | `versie-suffix-check.py` (117 regels) | PostToolUse | `Write` | Waarschuwt (geen block) als deliverable in `output/verification/` of bepaalde `output/reports/`-prefixen geen `vX_Y_Z`-suffix volgt. Skip-prefixen voor niet-versie-gebonden output (tooling-, lint-, dashboard-, handover-, T2/T3-iteratie-, extensie-, skill-eval-). |
| SessionStart | `sessionstart-context.sh` (46 regels) | SessionStart | `startup\|resume` | Injecteert 3 nieuwste `brain__log.md`-entries + `git status --short --branch` + `git log --oneline -5` als sessie-context. Operationaliseert "bij sessie-start"-leesvolgorde uit tech.md. |

Aanvullend:
- `disclosure-config.local.json.example` — voorbeeld voor Steven met dummy-waarden (gitignore-pattern excludeert `*.local.json`)
- `.gitignore` uitgebreid met `.claude/hooks/*.local.json` + `.claude/settings.local.json`

### §1.3 Testresultaten (A.3-testdiscipline)

Per hook één bekend-goed + één bekend-fout scenario; aanvullende skip-tests waar relevant.

| # | Hook | Scenario | Verwacht | Resultaat |
|---|---|---|---|---|
| 1 | secret-scan | Parafrase + placeholder (`ghp_REDACTED_EXAMPLE_TOKEN`, `mock_api_key=...`) | exit 0 (allow) | exit 0 ✅ |
| 2 | secret-scan | Echte-vorm GitHub PAT (`ghp_` + 36 alfanumeriek) | exit 2 (block) + stderr-hit | exit 2 + `GitHub PAT (classic) ≈ ghp_Ab…456789` ✅ |
| 3 | secret-scan | Tool-name = `Read` (niet-toepasselijk) | exit 0 (skip) | exit 0 ✅ |
| 4 | disclosure-check | Parafrase + Steven + repo-pad + NEN-licentie-pad + steven_bouw@live.nl | exit 0 (allow) | exit 0 ✅ |
| 5 | disclosure-check | Geblokkeerde org-name + geblokkeerde persoonsnaam + pad buiten repo + org-email + org-TLD | exit 2 (block) + 5 categorie-hits | exit 2 + cat1+cat2+cat3+cat4-e-mail+cat4-TLD ✅ |
| 6 | versie-suffix-check | `output/reports/patch-rapport-v4_6_3.md` (suffix aanwezig) | exit 0 (geen waarschuwing) | exit 0 ✅ |
| 7 | versie-suffix-check | `output/reports/patch-rapport-zonder-suffix.md` (suffix ontbreekt) | exit 0 (waarschuwing op stderr) | exit 0 + stderr-waarschuwing ✅ |
| 8 | versie-suffix-check | `output/reports/tooling-01-implementatierapport.md` (skip-prefix) | exit 0 (skip) | exit 0 ✅ |
| 9 | versie-suffix-check | `ontology/m01.ttl` (niet-output) | exit 0 (skip) | exit 0 ✅ |
| 10 | SessionStart | Reguliere invocatie | exit 0 + 3 log-entries + git status + git log -5 | exit 0 + 138-regel output ✅ |

**10/10 groen. Geen false-positives waargenomen op legitieme edits.** Activering (via `.claude/settings.json`) klaar.

Voor disclosure-check is na de tests de test-`disclosure-config.local.json` verwijderd (was niet bedoeld om te blijven staan). Steven kan `disclosure-config.local.json.example` kopiëren naar `disclosure-config.local.json` en eigen waarden invullen wanneer hij de cat1/cat2/cat4-detectie wil activeren met productie-waarden. Zonder lokaal config-bestand draait disclosure-check alleen op cat3 (paden) en cat4 (generieke e-mail-review) — degradeert grasvol.

### §1.4 Bewuste scope-uitsluitingen

| Uitsluiting | Reden |
|---|---|
| Categorie 5 (NEN-tekst >10 woorden) als hook | A.2 expliciet: "te complex; later". Semantische beoordeling vereist; deterministische woord-count zou false-positives geven op legitieme parafrase. Blijft Tech-handmatig (Protocol 17 parafrase-discipline). |
| Per-subagent path-denies in settings.json | Niet expressibel zonder agent-context-aware hook — zie §1.1. Risico: scope-creep buiten A.2 4-hook-set. |
| Pre-commit-hooks (Git-level) | Buiten scope (settings.json + Claude Code-hooks adressen al de relevante hand-off-punten vóór Steven). |
| MCP-server-aanroepen vanuit hooks | Bewust niet ingezet; `grc-kennismodel:run_secret_scanning` is genoemd in A.2 als optie maar lokaal regex-pad is deterministisch + zonder netwerk-afhankelijkheid. Hook is op zichzelf voldoende voor de PAT-incident-categorie. |

## §2. Deel B — verificatie-skills D.1 + D.2

skill-creator was niet beschikbaar tijdens deze sessie; hand-authored SKILL.md per de officiële conventie (frontmatter `name` + `description`, body in Markdown).

| Skill | Bestand | Regels | Rol |
|---|---|---|---|
| `/canonical-metrics` | `.claude/skills/canonical-metrics/SKILL.md` | 99 | Reference + action — codificeert `owlrl.DeductiveClosure(OWLRL_Semantics, axiomatic_triples=False, datatype_axioms=False)`, NamedIndividual-set-of-subjects-telling, zes invariantie-metrics, versie-suffix-conventie, "§0 uit JSON, niet uit memorie" (leerpunt v4.3.3). Wrapt `canonical_metrics_v*.py`-patroon. |
| `/shacl-split` | `.claude/skills/shacl-split/SKILL.md` | 108 | Action — SECTIE A (`inference='none'`) + SECTIE B (`inference='owlrl'`) gescheiden, 290 COMBINED-false-positives als verwacht OWA/CWA-fenomeen (arXiv 2507.12286), subset-shapes-graph-constructie via CBD-traversal. Wrapt `shacl_split_validate_v*.py`-patroon. |

Beide skills dragen **geen NEN-verbatim-tekst** (alleen methode + Shape-IRI's + script-patroon).

## §3. B.3 trigger-test — ontologie-drift-sanity-check

Re-run van beide v4.6.3-scripts vanuit repo-root, gevolgd door byte-vergelijking van de JSON-outputs t.o.v. baselines (na neutralisatie van `meta.measured_at_utc` en `meta.tool_versions` — beide per definitie tijdgevoelig).

### §3.1 Canonical metrics

```
=== canonical_metrics_v4_6_3 ===
Triples pre-inference:   20950
Triples post-inference:  44907
owl:Class:                  199
owl:NamedIndividual:       1383
owl:ObjectProperty:         149
owl:DatatypeProperty:        96
owl:sameAs:                   98
  D5 ctrl<->bio:             93
  D11 asset<->risk/isms:      5
SKOS mappings totaal:      1798
  exactMatch:                18
  broadMatch:               129
owl:Nothing post-inf:         0  (OK)
```

Diff t.o.v. `output/verification/canonical_metrics_v4_6_3.json`-baseline: **identiek** (excl. timestamp + tool-versies).

### §3.2 SHACL split

```
SECTIE A (none):        0 violations (verwacht 0)
SECTIE B (owlrl):       0 violations (verwacht 0)
COMBINED (owlrl):     290 violations (verwacht 290, Δ vs v4.6.2 = 0)
  104 asset:NamespaceShape
   93 control:ISO27002NamingShape
   93 bio:ISO27002NamingShape
```

Diff t.o.v. `output/verification/shacl_results_v4_6_3.json`-baseline: **identiek** (geen timestamp-velden).

### §3.3 Conclusie

**Ontologie ongewijzigd. Geen drift t.o.v. v4.6.3-baseline.** Beide skills triggeren correct via de bestaande scripts in `output/verification/`.

Na de trigger-test zijn de baseline-JSON's gerestored vanuit een `/tmp`-snapshot (de scripts schrijven naar dezelfde paden; de regenererende run produceerde inhoudelijk identieke output maar met nieuwere timestamp, wat git als 'modified' zag). Working tree na restore: alleen `.claude/`-additions + `.gitignore`-update als wijzigingen.

## §4. Protocol-14-disclosure-check op nieuwe bestanden

Handmatige scan van categorieën 1-4 op alle nieuwe bestanden + dit rapport:

| Bestand | Cat1 (org) | Cat2 (persoon ≠ Steven) | Cat3 (pad buiten repo) | Cat4 (e-mail/TLD) | Status |
|---|---|---|---|---|---|
| `.claude/settings.json` | geen | geen | geen | geen | ✅ |
| `.claude/hooks/secret-scan.py` | geen | geen | geen | geen | ✅ |
| `.claude/hooks/disclosure-check.py` | geen | geen | geen | geen | ✅ |
| `.claude/hooks/disclosure-config.json` | geen (alleen lege lijsten) | geen | `/Users/stevenbouwmeester/Desktop/grc-kennismodel/` + `/Users/stevenbouwmeester/grc-sources-licensed/` (beide in allow-list) | geen | ✅ |
| `.claude/hooks/disclosure-config.local.json.example` | placeholder "VoorbeeldOrganisatie" (verzonnen) | placeholder "Jan Jansen" (verzonnen) | geen | placeholder "voorbeeld.nl" | ✅ (alle waarden zijn verzonnen voorbeelden) |
| `.claude/hooks/versie-suffix-check.py` | geen | geen | geen | geen | ✅ |
| `.claude/hooks/sessionstart-context.sh` | geen | geen | geen | geen | ✅ |
| `.claude/skills/canonical-metrics/SKILL.md` | geen | geen | geen | geen | ✅ |
| `.claude/skills/shacl-split/SKILL.md` | geen | geen | geen | geen | ✅ |
| `output/reports/tooling-01-implementatierapport.md` (dit) | geen | geen | geen | geen | ✅ |
| `.gitignore` (delta) | geen | geen | geen | geen | ✅ |

**Geen Protocol-14-categorie-vondsten. Push-ready.**

Categorie 5 (NEN-tekst >10 woorden): geen NEN-bron geconsulteerd in deze opdracht. Skills bevatten alleen methode-beschrijving (zes invariantie-metrics, shape-IRI's, inference-instellingen) — geen normatieve ISO-tekst.

## §5. Deliverables (Protocol 16 — expliciete lokatie)

| Type | Lokatie | Beschrijving |
|---|---|---|
| Config | `.claude/settings.json` | Project-level Claude Code-settings: permissions (deny git-commit/push; ask destructieve git; allow read-only) + hooks-registratie. |
| Hook-script | `.claude/hooks/secret-scan.py` | PreToolUse — detecteert 10 secret-patronen + placeholder-whitelist. |
| Hook-script | `.claude/hooks/disclosure-check.py` | PreToolUse — Protocol 14 cat 1-4 via config-driven regex. |
| Hook-config | `.claude/hooks/disclosure-config.json` | Versioned baseline met allow-listen + scan-scope. |
| Hook-config-template | `.claude/hooks/disclosure-config.local.json.example` | Voorbeeld voor Steven's lokale override (gitignored pattern). |
| Hook-script | `.claude/hooks/versie-suffix-check.py` | PostToolUse — warn-only over `output/`-naming-conventie. |
| Hook-script | `.claude/hooks/sessionstart-context.sh` | SessionStart — injectie van log-tail + git-status + git-log. |
| Skill | `.claude/skills/canonical-metrics/SKILL.md` | Reference+action voor canonieke meet-procedure. |
| Skill | `.claude/skills/shacl-split/SKILL.md` | Action voor gesplitste SHACL-validatie. |
| Rapport | `output/reports/tooling-01-implementatierapport.md` | Dit document. |
| Gitignore-delta | `.gitignore` | Nieuwe regels: `.claude/hooks/*.local.json`, `.claude/settings.local.json`. |

## §6. Commit-suggestie

A en B zijn los committeerbaar (per §5 instructie).

**Commit A** (hooks + permissions):
```
chore(.claude): defensieve hooks + permissions — Tooling-01 Deel A

- settings.json: deny git-commit/push; ask destructieve git-acties; allow read-only
- hooks/secret-scan.py: PreToolUse Write|Edit — detecteert PAT/tokens/keys
- hooks/disclosure-check.py: PreToolUse Write|Edit — Protocol 14 cat 1-4
- hooks/disclosure-config.json + .example: config-driven via lokale override
- hooks/versie-suffix-check.py: PostToolUse Write — warn-only op output/
- hooks/sessionstart-context.sh: SessionStart — log-tail + git status/log
- .gitignore: *.local.json + settings.local.json
- Tests: 10/10 groen (3 scenarios secret-scan; 2 disclosure; 4 versie-suffix; 1 sessionstart)
- Conform §0.5-firewall: geen autonome commit/push-paden; geen sunset-flag

Ref: docs/instructies/instructie-tooling-01-guardrails-en-verificatieskills.md
```

**Commit B** (verificatie-skills):
```
chore(.claude): canonical-metrics + shacl-split skills — Tooling-01 Deel B

- skills/canonical-metrics/SKILL.md: codificeert owlrl-settings + 6 invariantie-
  metrics + versie-suffix-conventie + "§0 uit JSON" (leerpunt v4.3.3)
- skills/shacl-split/SKILL.md: codificeert SECTIE A (none) / SECTIE B (owlrl) /
  COMBINED + 290-false-positives als verwacht OWA/CWA-fenomeen (arXiv 2507.12286)
- Beide skills: geen NEN-verbatim-tekst (alleen methode + clausule-verwijzing)
- B.3 trigger-test op v4.6.3: canonical metrics + SHACL identiek aan baseline
  (A=0, B=0, COMBINED=290). Ontologie ongewijzigd bevestigd.

Ref: docs/instructies/instructie-tooling-01-guardrails-en-verificatieskills.md
```

**Rapport** kan in Commit A of B mee, of als 3e commit. Steven beslist.

## §7. Activeer-volgorde + caveat

Na commit van Deel A:
1. Hooks worden actief bij volgende Claude Code-sessie (settings.json wordt bij start geladen).
2. SessionStart-hook draait dan automatisch en injecteert context.
3. Pre/PostToolUse-hooks draaien bij elke Write/Edit (PreToolUse blokkeert bij hit; PostToolUse waarschuwt only).

Caveat: het permission-deny op `Bash(git commit:*)` geldt alleen binnen Claude Code-sessies. Steven kan handmatig committen vanuit zijn shell (terminal direct, niet via Claude Code). Dat is precies de bedoeling — het is een hardening van de bestaande proza-regel, niet een blokkade voor Steven zelf.

Caveat 2: disclosure-check.py degradeert grasvol als `disclosure-config.json` ontbreekt of de lokale override niet aanwezig is. Cat3 (paden) werkt altijd op basis van versioned `allowed_local_path_prefixes`. Cat1/cat2/cat4-org-specifiek vereist `disclosure-config.local.json` (kopie van `.example`, met echte waarden).

## §8. Stop-condities — niet getriggerd

Geen van de §3-stop-condities uit de instructie heeft zich voorgedaan:
- skill-creator: niet beschikbaar → hand-authored gegaan (binnen scope, niet onverwacht complex)
- Hook-ontwerp dat legitieme workflow zou blokkeren: tests tonen 10/10 zonder false-positive
- Permission-deny die bestaande workflow breekt: alleen `Bash(git commit:*)`/`Bash(git push:*)`-deny — dat is exact het beoogde effect (subagents committen niet zelf)
- §0.5-firewall-aanschuring: geen — alle bouwstenen zijn pure verdediging vóór hand-off
- Ontologie-drift in B.3-sanity-check: niet opgetreden (3.1 + 3.2 = identiek aan baseline)

## §9. Verdere overwegingen (uit eigen observatie, niet binnen sprint-scope)

Drie observaties die buiten deze opdracht vallen maar in een vervolg-instructie nuttig kunnen zijn — geen actie nu:

1. **Per-subagent path-denies blijven proza.** Bij eventueel incident waarbij tech-subagent (per ongeluk) naar `dashboard/**` schrijft of vice versa, kan een 5e PreToolUse-hook met agent-context-detectie alsnog gemaakt worden. YAGNI tot dat incident zich voordoet.
2. **Categorie 5 (NEN >10 woorden)** als hook is uitgesteld; bij toename van NEN-werk en groei van het rapport-corpus kan een woord-N-gram-vergelijking tegen een lokale NEN-corpus-hash overwogen worden. Niet triviaal en niet noodzakelijk nu.
3. **Hook-debug-modus.** Bij troubleshooting kan een env-var `CLAUDE_HOOK_DEBUG=1` toegevoegd worden die per hook extra stderr-uitleg geeft. Niet nu (YAGNI), wel laaghangend bij eerste echte false-positive-incident.

— Einde rapport.
