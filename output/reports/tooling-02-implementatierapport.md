# Tooling-02 implementatierapport — CLAUDE.md-herstructurering + path-scoped skills + /patch-rapport + disclosure-config-restructure

| Veld | Waarde |
|---|---|
| Spoor | A |
| Track | `.claude/`-tooling + CLAUDE.md (geen ontologie-release) |
| Baseline | v4.6.3 (ongewijzigd) |
| Bron-instructie | `docs/instructies/instructie-tooling-02-claude-md-rules-en-protocol-skills.md` |
| Uitvoerder | Tech-subagent (Claude Code) |
| Datum | 2026-05-28 |
| Vooraf | Tooling-01 gecommit + gepusht (`3fb1da0..37090c4`) |
| Commit + push | Steven (handmatig — Protocol §7) |

## §0. Kader-bevestiging en §0.5-firewall-conformiteit

Doel: always-on-context afslanken en protocol-discipline van proza naar aanroepbaar/path-geladen tillen, met behoud van alle invarianten. Geen autonomie-bouw.

§0.5-firewall-conformiteit:

| §0.5-verbod | Status | Toelichting |
|---|---|---|
| Geen autonome commit/push-paden | OK | Geen wijziging aan `.claude/settings.json`-deny-rules; "subagents committen NOOIT zelfstandig" is in CLAUDE.md §"Werk-conventies" expliciet hardgemaakt als zevende invariant. |
| Geen green-gate-voor-autonomie | OK | Geen nieuwe permissions; geen agent-context-bypass; geen sunset-flag. |
| Geen agent teams / CI / auto-merge | OK | Alleen skills (description + path-triggered) en CLAUDE.md-edit. Geen orchestratie. |
| Geen ontologie-/beleids-/architectuurwijziging | OK | `ontology/` + `grc-shacl.ttl` byte-identiek aan v4.6.3 (§6 drift-check). |
| Always-on-invarianten verzwakt? | NEE | Zes invariant-regels expliciet in §"Werk-conventies" + extra "subagents committen NOOIT zelfstandig" als zevende. Bias naar behoud toegepast bij twijfel-grensgevallen (Karpathy-concept, dashboard-productlijnen, Spoor B). |

Geen natuurlijke autonomie-route aangetroffen tijdens uitvoering; bij twijfel-grensgeval is BEHOUDEN gekozen.

## §1. Vooraf — Deel D-uitvoering (pad-neutralisatie)

Tooling-02-instructie §4 noemt Deel D als optioneel ("alleen op expliciete go van Steven"). Aan de start van deze opdracht stond een editing-state van `.claude/hooks/disclosure-config.json` in de werkboom:
- JSON-syntax was invalide (bare identifiers zonder quotes)
- Bevatte feitelijke organisatie-naam (cat1 Protocol 14) in versioned file → Δ-risico bij push
- Steven was niet in `allowed_persons` / `allowed_emails` opgenomen → zou Steven zelf blokkeren bij valide JSON

Scope-pauze gehouden vóór Tooling-02 §1-§3 te starten. Steven gekozen voor **"Activeer Deel D nu (aanbevolen)"**. Daarna uitgevoerd:

| Bestand | Vóór | Na |
|---|---|---|
| `.claude/hooks/disclosure-config.json` (versioned) | Org-naam + 4 personen + allowed-paden, invalide JSON | Alle org/persoon/allowed-velden = lege arrays; allowed_local_path_prefixes ook leeg; alleen scan_scopes behouden. Valide JSON. |
| `.claude/hooks/disclosure-config.local.json` (gitignored) | Voorbeeld-content | Echte waarden: zes organisatie-naam-varianten (incl. casing-variant + afkorting + één typo), één organisatie-email-domein, twee persoonsnamen ≠ Steven, Steven + vier aliassen in `allowed_persons`, Steven's e-mail in `allowed_emails`, twee `allowed_local_path_prefixes` |
| `.claude/hooks/disclosure-config.local.json.example` | 4-velden voorbeeld | 7-velden voorbeeld inclusief allowed_persons/emails/local_path_prefixes (sluit aan op nieuwe leeg-versioned-baseline) |

Test-resultaten Deel D (4 tests):

| # | Scenario | Verwacht | Resultaat |
|---|---|---|---|
| D1 | JSON-syntax-valide alle 3 bestanden | OK | OK ✅ |
| D2 | Bekend-goed (Steven + Bouwmeester + repo-pad + NEN-pad + steven_bouw@live.nl) | exit 0 | exit 0 ✅ |
| D3 | Bekend-fout (org-naam + persoon + buiten-repo-pad + org-email) | exit 2 + cat1+cat2+cat3+cat4-hits | exit 2 + 5 hits ✅ |
| D4 | Typo-variant + afkorting + tweede geblokte persoonsnaam (geredacteerd in dit rapport per Protocol 14) | exit 2 + cat1×2 + cat2 | exit 2 + 3 hits ✅ |

Organisatie-neutraliteit invariant geborgd: versioned `disclosure-config.json` bevat nu UITSLUITEND lege placeholders + scan_scopes; geen identificeerbare organisatie-data. Verwijdering of corruptie van `disclosure-config.local.json` veroorzaakt grasvolle degradatie (cat3 stil + cat1/cat2/cat4 zonder match-termen).

## §2. Deel A.0 — pre-check `.claude/rules/`-support

Verificatie via `claude-code-guide`-subagent tegen officiële docs.

**Uitkomst:** `.claude/rules/` als path-scoped folder met `paths`-frontmatter is **niet** officieel ondersteund in de actuele Claude Code-versie. Het canonieke mechanisme voor path-scoped activatie is **skills met `paths`-frontmatter** (`.claude/skills/<name>/SKILL.md` met `paths: <glob>`).

Per Tooling-02 §A.0 stop-conditie ("Indien NIET ondersteund → stop-conditie: meld het, en houd de inhoud in CLAUDE.md of een skill in plaats van rules. Geen aanname.") → fallback toegepast: alle A.2-inhoud naar **skills** verplaatst, niet naar `.claude/rules/`.

Bron-docs: [code.claude.com/docs/en/skills.md](https://code.claude.com/docs/en/skills.md) (frontmatter-reference → `paths`-veld).

## §3. Deel A.1 — CLAUDE.md afslanken

| Metric | Vóór | Na | Δ |
|---|---:|---:|---:|
| Regels | 293 | 168 | −125 (−43%) |
| Tabellen | 9 | 3 | −6 |
| §-secties | 18 | 13 | −5 |

Behoudslens: bias naar BEHOUDEN; alleen aantoonbaar reference verplaatst.

### §3.1 Verplaatst / gebleven-tabel

| Sectie / inhoud | Pre | Post | Toelichting |
|---|---|---|---|
| Title + voor-Claude-Code-note | Behouden | Behouden | Entry-point |
| Wat is dit (intro) | Behouden uitgebreid | Behouden ingekort | Kerngedachte + baseline-verwijzing |
| **Karpathy drie-lagen-tabel + uitleg** | In CLAUDE.md | **`.claude/skills/repo-reference/SKILL.md` §1** | Reference (concept-blijfsel als 1 regel) |
| **Repo-structuur boom-diagram** | In CLAUDE.md (volledig) | **`.claude/skills/repo-reference/SKILL.md` §2** + samenvattings-tabel in CLAUDE.md | Reference (top-level tabel als index) |
| Dashboard-productlijnen (Spoor A vs B) | Behouden | Behouden | Concept-onderscheid, near-invariant |
| **Brain-vault organisatie-tabel met aantallen** | In CLAUDE.md (volledig) | **`.claude/skills/repo-reference/SKILL.md` §3** | Reference |
| **Werk-conventies (verplicht)** | In CLAUDE.md (7 punten) | Behouden + uitgebreid: zes invariant-regels expliciet + "subagents committen NOOIT zelfstandig" als zevende + operationele discipline | Invariant-uitbreiding conform §0 instructie |
| Hoe te lezen (entry-points) | Behouden | Behouden + verwijzing naar nieuwe skills | Workflow |
| **Operations (Ingest/Query/Lint/File-back) detail** | In CLAUDE.md (volledig) | **`.claude/skills/repo-reference/SKILL.md` §4** | Reference (Karpathy-pattern detail) |
| Subagents (3) tabel | Behouden | Behouden | Invariant-rolverdeling |
| Chats claude.ai-only | Behouden | Behouden | Workflow-context |
| Cross-chat-bewustzijn | Behouden | Behouden + SessionStart-hook-verwijzing | Workflow + nieuwe Tooling-01-context |
| Sprint-werkproces samenvatting | Behouden | Behouden | Workflow |
| **Skills-ecosystem-positionering (4 mechanismen + Tier 1/2)** | In CLAUDE.md (volledig) | **`.claude/skills/repo-reference/SKILL.md` §5** | Reference |
| Externe bronnen (NEN-restrictief) | Behouden | Behouden + lokale `grc-sources-licensed/`-pad expliciet | Invariant-noot |
| **Optional tooling (Obsidian / qmd / Dataview / Mermaid)** | In CLAUDE.md (volledig) | **`.claude/skills/repo-reference/SKILL.md` §6** | Reference |
| Reference-verwijzingen-sectie | (nieuw) | Behouden | Nieuwe sectie: linkt naar verplaatste skills + path-scoped skills + action-skills |
| Spoor B-overweging | Behouden | Behouden | Strategie-noot |
| Versionering-tabel | Behouden | Behouden + nieuwe regel v1.6 | Audit-trail append-only |

### §3.2 Invariant-verzwakkings-audit (kritisch)

Per §0 instructie: "always-on-invarianten MOGEN NIET verzwakken". Audit:

| Invariant (uit §0 instructie) | Status na herstructurering |
|---|---|
| D9-framework-neutraliteit | Behouden als bullet 3 in §"Werk-conventies" |
| "Geen organisatienaam" | Behouden als bullet 2 in §"Werk-conventies"; bovendien gecodificeerd via disclosure-check cat1 |
| NEN-parafrase-discipline | **Toegevoegd** als bullet 4 in §"Werk-conventies" (was eerder alleen in Protocol 17, niet always-on) |
| Status-discipline (CBW "in voorbereiding" / Cbb "concept") | **Toegevoegd** als bullet 5 in §"Werk-conventies" (was alleen brain-vault) |
| BBN-correctie | **Toegevoegd** als bullet 6 in §"Werk-conventies" (was alleen brain-vault) |
| Subagents committen NOOIT zelfstandig | **Toegevoegd** als bullet 7 + gecodificeerd in `.claude/settings.json` (Tooling-01) |

**Nettoresultaat: invarianten VERSTERKT, niet verzwakt** — drie eerder-impliciete-invarianten zijn nu expliciet always-on, plus codificatie van de subagent-commit-invariant.

## §4. Deel A.2 — path-scoped skills (i.p.v. `.claude/rules/`)

### §4.1 `repo-reference` (description-triggered)

| Veld | Waarde |
|---|---|
| Lokatie | `.claude/skills/repo-reference/SKILL.md` (187 regels) |
| Activatie | description-triggered (geen `paths:`) |
| Inhoud | §1 Karpathy drie-lagen + §2 Repo-boom + §3 Brain-vault-organisatie + §4 Operations Ingest/Query/Lint/File-back + §5 Skills-ecosystem (4 mech + Tier 1/2) + §6 Optional tooling |
| Bron | Verplaatst uit CLAUDE.md tijdens herstructurering |

### §4.2 `ontology-conformance` (path-scoped)

| Veld | Waarde |
|---|---|
| Lokatie | `.claude/skills/ontology-conformance/SKILL.md` (78 regels) |
| Activatie | `paths: ontology/*.ttl, ontology/**/*.ttl` |
| Inhoud | D1-D12 verkorte conventies + D4.1 cross-category-rationale + pre-edit-checklist + post-edit-verificatie + conformance-output-tabel + vermijdingen |
| Bron-verwijzingen | `brain/brain__decisions__D-register.md` per D-decision |

D4.1 expliciet opgenomen: T3-precedent v4.6.3 (cross-category control↔legal-obligation = relatedMatch, NIET broadMatch/narrowMatch). Geen NEN-verbatim-tekst.

### §4.3 `report-structure` (path-scoped)

| Veld | Waarde |
|---|---|
| Lokatie | `.claude/skills/report-structure/SKILL.md` (119 regels) |
| Activatie | `paths: output/reports/*, output/reports/**/*` |
| Inhoud | File-naming-conventie + verwijzing naar /patch-rapport-skill (skelet) + Protocol 13 bron-typo-beleid + Protocol v1.3 §10.2 bottom-up + §10.3 tabel-consistentie + §10.4 helper-script-autoritatief + §10.5 metrics-scope-annotatie + pre-hand-off checklist |
| Bron-verwijzingen | `docs/sprint-protocols.md`, `docs/skos-beoordelings-protocol-v1_3.md` |

## §5. Deel B — `/patch-rapport`-skill (D.3)

| Veld | Waarde |
|---|---|
| Lokatie | `.claude/skills/patch-rapport/SKILL.md` (259 regels) |
| Activatie | description + action (genereer §0-§15-skelet) |
| Inhoud | Wanneer aanroepen + dependencies + bottom-up bouw-volgorde + canoniek §0-§15-skelet + afgedwongen disciplines (§0 uit JSON, §7 uit shacl_results JSON, §9 expliciete lokaties, §12 D-conformance via /ontology-conformance, §0+§4+§6 scope-annotatie) + trigger-test tegen v4.6.3 + cross-references |

### §5.1 Trigger-test tegen v4.6.3-cijfers

**Test 1 — §-koppen-match:**

| Niveau | Skill | v4.6.3-rapport | Match |
|---|---:|---:|---|
| Top-level `## §N.` | 16 (§0-§15) | 16 (§0-§15) | ✅ 1:1 |

**Test 2 — cijfer-match tegen `canonical_metrics_v4_6_3.json`:**

| Metric | Skill | JSON-baseline | Match |
|---|---:|---:|---|
| triples (pre-inference) | 20950 | 20950 | ✅ |
| owl:NamedIndividual | 1383 | 1383 | ✅ |
| owl:sameAs | 98 | 98 | ✅ |
| skos_mappings_total | 1798 | 1798 | ✅ |
| skos.broadMatch | 129 | 129 | ✅ |
| skos.relatedMatch | 194 | 194 | ✅ |
| D5 ctrl↔bio | 93 | 93 | ✅ |
| D11 asset-brug | 5 | 5 | ✅ |

**Test 3 — SHACL-cijfer-match tegen `shacl_results_v4_6_3.json`:**

| Sectie | Skill | JSON-baseline | Match |
|---|---:|---:|---|
| SECTIE A (none) | 0 | 0 | ✅ |
| SECTIE B (owlrl) | 0 | 0 | ✅ |
| COMBINED (owlrl) | 290 | 290 | ✅ |

**Conclusie: 16/16 sectie-match + 8/8 cijfer-match + 3/3 SHACL-match. Skill is consistent met v4.6.3-baseline.**

## §6. Deel C — `/pre-sprint-inventarisatie` (gedeferd)

Per instructie §3 "Alléén bouwen als Deel A+B niet te groot worden; anders deferren naar een volgende tooling-instructie".

Deel A.1 (CLAUDE.md −125 regels + verplaats-tabel) + Deel A.2 (3 skills, 384 regels totaal) + Deel B (1 skill, 259 regels) + Deel D pre-step + rapport vormen al een substantieel pakket. Deel C deferren is conservatief; instructie sanctioneert dit expliciet ("anders deferren").

Voorgesteld voor een Tooling-03 of latere instructie: `/pre-sprint-inventarisatie`-skill als action-skill voor Protocol 1, met velden:
- ABox-baseline (uit canonical_metrics_v_(Y-1).json)
- Cluster-cardinaliteit per module
- Evidence-coverage-status (lokale NEN-toegang per cluster)
- Scope-bevestiging-checklist (instructie-§-naar-doel-mapping)

Niet gebouwd in deze opdracht. Geen functionaliteit ontbreekt; Protocol 1-werk verloopt nu via `docs/sprint-protocols.md` §1.

## §7. Ontologie-drift-sanity-check (B.3-equivalent)

Re-run van beide v4.6.3-scripts vanuit repo-root, gevolgd door byte-vergelijking met baseline-JSON's (na neutralisatie van `meta.measured_at_utc` + `meta.tool_versions`).

| Script | Resultaat |
|---|---|
| `canonical_metrics_v4_6_3.py` | Pre-inference triples 20950 ; owl:Class 199 ; NamedIndividual 1383 ; sameAs 98 ; SKOS-total 1798 ; broadMatch 129 ; **identiek aan baseline** |
| `shacl_split_validate_v4_6_3.py` | A=0 / B=0 / COMBINED=290 ; **identiek aan baseline** |

**Ontologie ongewijzigd. Geen drift t.o.v. v4.6.3-baseline.**

Na de drift-check zijn de baseline-JSON's gerestored vanuit `/tmp`-snapshot (re-run produceerde inhoudelijk identieke output met nieuwere timestamp, wat git als modified zag). Working tree na restore: alleen Tooling-02-deliverables als wijziging.

## §8. Protocol-14-disclosure-check op alle nieuwe + gewijzigde bestanden

Automatische run van `.claude/hooks/disclosure-check.py` (productie-versie met nieuwe versioned + local config) op zeven Tooling-02-bestanden:

| Bestand | exit-code | Resultaat |
|---|---|---|
| `CLAUDE.md` | 0 | clean ✅ |
| `.claude/hooks/disclosure-config.json` | 0 | clean ✅ |
| `.claude/hooks/disclosure-config.local.json.example` | 0 | clean (placeholder-namen) ✅ |
| `.claude/skills/repo-reference/SKILL.md` | 0 | clean ✅ |
| `.claude/skills/ontology-conformance/SKILL.md` | 0 | clean ✅ |
| `.claude/skills/report-structure/SKILL.md` | 0 | clean ✅ |
| `.claude/skills/patch-rapport/SKILL.md` | 0 | clean ✅ |

**Geen Protocol-14-categorie-vondsten op de Tooling-02-deliverables. Push-ready.**

Dit rapport zelf wordt ook getoetst zodra het wordt geschreven (PreToolUse-hook draait automatisch). Categorie 5 (NEN-tekst >10 woorden): geen NEN-bron geconsulteerd in deze opdracht; skills bevatten alleen methode-beschrijving + D-decision-verwijzingen.

## §9. Deliverables (Protocol 16 — expliciete lokatie)

| Type | Lokatie | Beschrijving |
|---|---|---|
| CLAUDE.md | `CLAUDE.md` | Afgeslankt van 293 → 168 regels; zes always-on-invarianten expliciet + zevende (subagents committen NOOIT zelfstandig); verwijzingen naar verplaatste content |
| Reference-skill | `.claude/skills/repo-reference/SKILL.md` | Karpathy + repo-boom + brain-vault-organisatie + Operations + Skills-ecosystem + Optional tooling |
| Path-scoped skill | `.claude/skills/ontology-conformance/SKILL.md` | D1-D12 + D4.1-checklist (`paths: ontology/*.ttl`) |
| Path-scoped skill | `.claude/skills/report-structure/SKILL.md` | Rapport-discipline + Protocol 13 + Protocol v1.3 §10.2-§10.5 (`paths: output/reports/*`) |
| Action-skill | `.claude/skills/patch-rapport/SKILL.md` | §0-§15-skelet-generator met afgedwongen JSON-bron + Protocol 16 + D-conformance |
| Config (versioned) | `.claude/hooks/disclosure-config.json` | Alle org/persoon/allowed-velden → lege arrays; alleen scan_scopes behouden |
| Config (gitignored) | `.claude/hooks/disclosure-config.local.json` | Werkelijke org-/persoon-/pad-waarden — NIET committen |
| Config (versioned) | `.claude/hooks/disclosure-config.local.json.example` | Voorbeeld-template uitgebreid met allowed_persons/emails/local_path_prefixes |
| Rapport | `output/reports/tooling-02-implementatierapport.md` | Dit document |

## §10. Commit-suggestie (delen los committeerbaar — instructie §7)

**Commit A** — disclosure-config restructure (Deel D — pre-step):
```
chore(.claude/hooks): disclosure-config — versioned naar placeholders + local override (Deel D)

- disclosure-config.json: alle org/persoon/allowed-velden → lege arrays
  (alleen scan_scopes behouden); JSON-syntax-valide; org-neutraliteit-invariant
- disclosure-config.local.json blijft gitignored met werkelijke waarden
- disclosure-config.local.json.example uitgebreid met allowed_persons/emails/
  local_path_prefixes (aligned met nieuwe leeg-versioned-baseline)
- Tests Deel D: 4/4 groen (JSON-syntax + 1 good + 2 bad scenarios)

Ref: docs/instructies/instructie-tooling-02-claude-md-rules-en-protocol-skills.md §4
```

**Commit B** — CLAUDE.md herstructurering + reference-skill (Deel A.1 + repo-reference):
```
docs: CLAUDE.md afslanken + .claude/skills/repo-reference/ (Tooling-02 Deel A.1)

- CLAUDE.md: 293 → 168 regels (−43%). Karpathy-drie-lagen-detail, repo-boom,
  brain-vault-organisatie-tabel, Operations Ingest/Query/Lint/File-back-detail,
  skills-ecosystem 4-mech + Tier 1/2, optional tooling: verplaatst naar skill.
- Always-on-invarianten EXPLICIET in §"Werk-conventies": NL, geen org-naam,
  D9-neutraal, NEN-parafrase, status-discipline, BBN-correctie, subagents
  committen NOOIT zelfstandig (zevende, gecodificeerd in .claude/settings.json).
- Drie eerder-impliciete-invarianten (NEN-parafrase, status, BBN) zijn nu
  always-on → invarianten NETTO VERSTERKT, niet verzwakt.
- Skill repo-reference: description-triggered; 6 secties = verplaatste content.

Ref: docs/instructies/instructie-tooling-02-claude-md-rules-en-protocol-skills.md §1
```

**Commit C** — path-scoped skills (Deel A.2):
```
chore(.claude/skills): ontology-conformance + report-structure (path-scoped)

- A.0 pre-check: .claude/rules/ + paths-frontmatter NIET ondersteund in actuele
  Claude Code (verificatie via claude-code-guide-subagent tegen officiële docs:
  code.claude.com/docs/en/skills.md). Fallback per §A.0 stop-conditie: skills
  i.p.v. rules.
- ontology-conformance/SKILL.md (paths: ontology/*.ttl): D1-D12 + D4.1
  cross-category-rationale-precedent + pre-edit-checklist + post-edit-verificatie
- report-structure/SKILL.md (paths: output/reports/*): file-naming-conventie +
  Protocol 13 bron-typo + Protocol v1.3 §10.2-§10.5 (bottom-up / tabel-
  consistentie / helper-script-autoritatief / metrics-scope-annotatie)
- Geen NEN-verbatim-tekst in beide skills

Ref: docs/instructies/instructie-tooling-02-claude-md-rules-en-protocol-skills.md §A.2
```

**Commit D** — /patch-rapport skill (Deel B):
```
chore(.claude/skills): /patch-rapport — §0-§15-skelet (Tooling-02 Deel B)

- patch-rapport/SKILL.md: canoniek §0-§15-skelet conform v4.6.2/v4.6.3-precedent
- Afgedwongen disciplines:
  - §0 uit canonical_metrics JSON (leerpunt v4.3.3 — niet uit memorie)
  - §7 uit shacl_results JSON
  - §9 Deliverables-tabel met expliciete lokaties (Protocol 16)
  - §12 D-conformance via /ontology-conformance-skill (D1-D12 + D4.1)
  - §0+§4+§6 metrics-tabel-scope-annotatie (Protocol v1.3 §10.5)
- Bottom-up bouw-volgorde voorgeschreven (Protocol v1.3 §10.2)
- Koppeling met /canonical-metrics + /shacl-split + /ontology-conformance
- Trigger-test tegen v4.6.3: 16/16 sectie-match + 8/8 cijfer-match + 3/3 SHACL
- Geen NEN-verbatim-tekst

Ref: docs/instructies/instructie-tooling-02-claude-md-rules-en-protocol-skills.md §2
```

**Commit E** — implementatierapport:
```
docs(tooling): Tooling-02 implementatierapport — CLAUDE.md slim + path-scoped skills + /patch-rapport + Deel D

- §0: §0.5-firewall-conformiteit + invariant-bescherming
- §1: Deel D (pad-neutralisatie) als pre-step uitgevoerd na scope-pauze
- §2: A.0 pre-check — .claude/rules/ niet ondersteund; skills als fallback
- §3: CLAUDE.md verplaatst/gebleven-tabel + invariant-audit (NETTO VERSTERKT)
- §4: 3 path-scoped + reference skills (repo-reference, ontology-conformance,
  report-structure)
- §5: /patch-rapport skill + trigger-test (16/16 + 8/8 + 3/3 groen)
- §6: Deel C gedeferd per instructie-§3
- §7: ontologie ongewijzigd (canonical + SHACL identiek aan v4.6.3-baseline)
- §8: Protocol 14 disclosure-check op 7 deliverables: clean
- §9: Deliverables-tabel (Protocol 16)
- §10: commit-suggesties (5 commits los), stop-condities (geen getriggerd)

Ref: docs/instructies/instructie-tooling-02-claude-md-rules-en-protocol-skills.md
```

Steven kan ook minder commits maken (bv. B+C+D samen, of alles als 1 commit). Suggestie hierboven volgt het instructie-§7-principe "delen los committeerbaar".

## §11. Stop-condities — niet getriggerd

Geen van de §5-stop-condities uit de instructie heeft zich voorgedaan:

- `.claude/rules/` niet ondersteund → afgehandeld via fallback (skills); geen blokkade
- Twijfel invariant-vs-reference → bias naar BEHOUDEN toegepast; zes invarianten + zevende expliciet
- Verplaatsing zou een always-on-invariant uit de always-on-laag halen → niet voorgekomen; invarianten NETTO VERSTERKT
- §0.5-firewall-aanschuring → niet voorgekomen
- Ontologie-drift in B.3-equivalent → niet opgetreden (§7)

## §12. Verdere overwegingen (uit eigen observatie, niet binnen sprint-scope)

Drie observaties die buiten deze opdracht vallen maar in een Tooling-03 nuttig kunnen zijn — geen actie nu:

1. **`/pre-sprint-inventarisatie`-skill** (instructie §3-Deel C, gedeferd). Concrete scope ligt klaar in §6 hierboven.
2. **Skill-creator integratie**: `.claude/skills/`-bestanden zijn nu hand-authored. Bij Tooling-03 zou skill-creator (Anthropic's skill-init-tool, indien beschikbaar) overwogen kunnen worden voor uniforme frontmatter-validatie. YAGNI nu — 5 skills hand-authored = werkbaar.
3. **CLAUDE.md-min vs CLAUDE.md-pro**: huidige 168 regels zit comfortabel binnen Claude Code's autoload-context-budget; verdere afslanking heeft afnemend rendement. Bij groei van het project (Spoor B / extra subagents) opnieuw kijken.

— Einde rapport.
