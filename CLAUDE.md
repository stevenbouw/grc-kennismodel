# GRC Kennismodel — Repo Root

> **Voor Claude Code:** dit is de vault-root van het GRC Kennismodel-project. Begin met `brain/brain__index.md` als entry-point voor het project en `brain/brain__log.md` voor recente sprints. Lees `docs/sprint-protocols.md` voor verplichte werkwijze tijdens sprints.

## Wat is dit

Karpathy-stijl digital brain + ontologie-werkfolder voor het GRC Kennismodel-project. De repo combineert: brain-vault (~101 markdown-bestanden), ontologie-modules (22 .ttl-bestanden, OWL 2 DL), publiek-domein bronnen (NIST / EU-recht / NL-recht / ADR-NOREA / overheid), scripts (canonical metrics + SHACL-validatie), dashboard (grc-explorer + build-pipeline), docs (sprint-instructies + protocollen + handovers + migratie-roadmap).

**Huidige ontologie-baseline:** v4.6.3 (T3 m14 AVG/GDPR SKOS-audit, 28 mei 2026).
**Actuele projectinstructie:** `docs/projectinstructie-v1_10.md` (27 mei 2026). Eerdere versies (`v1_8`, `v1_9`) blijven beschikbaar in `docs/` als historische referentie.

Kerngedachte (Karpathy LLM-Wiki-pattern): **"compile once, keep current"**. Bronnen worden eenmaal verwerkt naar brain-vault + ontologie; de wiki blijft synchroon met realiteit zonder dat sources telkens herverwerkt worden. Subagents zijn wiki-onderhouders, geen RAG-systemen. Detail + drie-lagen-pattern: zie `.claude/skills/repo-reference/SKILL.md`.

## Werk-conventies (always-on invarianten — voor alle subagents)

Deze zes regels gelden ZONDER UITZONDERING. Niet onderhandelbaar, niet per sprint, niet via subagent-autonomie.

- **Communicatie in het Nederlands** — ontologie-annotaties bilinguaal @nl/@en (D6)
- **Organisatienaam wordt NOOIT genoemd** — altijd "de organisatie" of "Rijksoverheidsorganisatie"
- **Framework-neutraal** (D9) — alle frameworks gelijkwaardig; BIO 2.0 alleen als view-keuze in dashboard, niet architecturaal
- **NEN-parafrase-discipline** — NEN-tekst NOOIT verbatim in repo / commit / Turtle / rapport-output; alleen parafrase + clausule-verwijzing (Protocol 17)
- **Status-discipline** — CBW "in voorbereiding", Cbb "concept", overige bronnen status-conform; geen anachronistische status-toekenning
- **BBN-correctie** — Handreiking BBN-waarden conform actuele canonieke meting (zie `output/verification/canonical_metrics_v*.json`); geen geheugen-tellingen
- **Subagents committen NOOIT zelfstandig** — Steven inspecteert `git status`/`git diff` en commit handmatig. Codificeerd in `.claude/settings.json` als hard deny op `Bash(git commit:*)` / `Bash(git push:*)`. §0.5-firewall: geen autonome commit-paden, geen green-gate, geen sunset-flag

Plus operationele discipline:
- **Scope-discipline** — bij scope-afwijking PAUZE + rapport (Optie A/B/C); niet zelf interpreteren. Triggers in `docs/sprint-protocols.md` §15
- **D-decisions zijn immutable** — wijziging vereist masterchat-goedkeuring in claude.ai (via Steven)
- **Append-only log** — `brain/brain__log.md` nieuwste entry bovenaan, alleen append nooit edit
- **Sprint-protocollen verplicht** — alle protocollen + gedragsregel uit `docs/sprint-protocols.md` zijn niet-onderhandelbaar
- **Bron-attribuering** — bij externe bronmaterialen: `ext:sourceAttribution` declareren; SHA256 bij snapshot-bronnen

## Dashboard-productlijnen (Spoor A vs Spoor B)

Twee parallelle dashboard-productlijnen met fundamenteel verschillende doelen — niet vermengen in één UI:

- **`grc-explorer-*`** (Spoor A) — read-only ontologie-graaf-verkenner; data uit `grc-data-v[X_Y_Z].js`; Cytoscape.js; beweegt mee met ontologie-versie. Actueel: `dashboard/grc-explorer-v4_6_0.html`.
- **`grc-dashboard-*`** (Spoor B) — operationele werkmap-prototype (CRUD, audit-trail, kalender, RACI); data uit lokale SQL.js `.db`; Chart.js + SQL.js; eigen versie-track. Actueel: `grc-dashboard-v3-2.html` (bewust lokaal, niet in repo).

Scope-afbakening van H40 (UI-renderdekking) betreft uitsluitend Spoor A. Detail + discipline: `brain/brain__concepts__dashboard-productlijnen.md`.

## Repo-structuur (samenvatting)

| Top-level | Inhoud |
|---|---|
| `brain/` | ~101 brain__*.md (vault, flat met `__`-separator-conventie) |
| `ontology/` | 22 .ttl-modules (huidig: v4.6.3) — TBox + ABox + SHACL-shapes |
| `sources/` | Publiek-domein bronnen (`adr-norea/`, `ensia/`, `eu-recht/`, `nl-recht/`, `nist/`, `overheid/`) |
| `dashboard/` | grc-explorer HTML + build-pipeline + JSON/JS-data (Spoor A) |
| `docs/` | sprint-protocols.md, migratie-roadmap.md, instructies/, handovers/ |
| `scripts/` | utilities (canonical metrics + SHACL-validatie staan in `output/verification/`) |
| `output/reports/` | patch-rapporten, inventarisaties, tussenrapporten, scope-pauzes, lint-rapporten |
| `output/verification/` | `canonical_metrics_v*.{py,json}` + `shacl_split_validate_v*.py` + `shacl_results_v*.json` + `file_hashes_v*.txt` |
| `.claude/agents/` | drie subagent-configs (tech / brein / dashboard) |
| `.claude/hooks/` | defensieve hooks (secret-scan, disclosure-check, versie-suffix, sessionstart) |
| `.claude/skills/` | action + reference skills (canonical-metrics, shacl-split, patch-rapport, ontology-conformance, report-structure, repo-reference) |
| `.claude/settings.json` | permissions + hooks-config |

Volledig boom-diagram + brain-vault-tabel met aantallen: zie `.claude/skills/repo-reference/SKILL.md` (description-triggered).

## Hoe te lezen (entry-points)

Bij een nieuwe vraag over het project:

1. `brain/brain__index.md` — masteroverzicht en huidige baseline
2. `brain/brain__{folder}__-register.md` — navigatie binnen specifiek domein (decisions / sprints / H-items / concepts / modules / sources / workflow / scope)
3. `brain/brain__log.md` — chronologische context, laatste sprints

Voor specifieke onderwerpen: zoek op D-nummer, H-nummer, M-nummer, versienummer of framework-naam. Voor werkwijze: **`docs/sprint-protocols.md`** is autoritatief. Voor patch-rapport-skelet: skill `/patch-rapport`. Voor canonical metrics + SHACL: skills `/canonical-metrics` + `/shacl-split`.

## Subagents (drie in deze repo)

Drie chats zijn naar Claude Code gemigreerd; vier blijven in claude.ai.

| Subagent | Rol | Config |
|---|---|---|
| **Tech** | Ontologie-engineering (OWL/SPARQL/SHACL/Turtle) | `.claude/agents/tech.md` |
| **Brein** | Brain-vault-onderhoud na elke minor-release | `.claude/agents/brein.md` |
| **Dashboard** | Visualisatie + grc-explorer.html + build-pipeline | `.claude/agents/dashboard.md` |

Aanroepen vanuit Claude Code: `claude --agent tech` of via Task-tool. Tech- en Dashboard-configs incorporeren de Karpathy LLM coding-discipline (Think Before Coding / Simplicity First / Surgical Changes / Goal-Driven Execution).

### Chats die in claude.ai blijven (geen subagent-config in deze repo)

- **Master** — strategisch sparren (terminal-only past niet)
- **Documentatie** — tekst-werk (conversationeel)
- **Analyse** — incidenteel exploratief
- **Asset** — afgerond sinds M18-oplevering (v4.2.0), stand-by

Werkproces tussen Claude Code en claude.ai: Steven (projecteigenaar) is tussenmens bij scope-pauzes en architectuur-beslissingen. Subagent escaleert naar Steven; Steven raadpleegt Master-chat in claude.ai; Steven brengt besluit terug.

## Cross-chat-bewustzijn

De repo is shared state tussen alle Claude-sessies (subagents Claude Code én chats claude.ai). Werk-wijzigingen worden:

1. In de vault/ontology/scripts/dashboard gepersisteerd (file edits)
2. `brain/brain__log.md` ge-update (append-only, nieuwste entry bovenaan)
3. Via git gecommit (Steven handmatig) met betekenisvolle commit messages
4. Bij sessie-start gelezen door volgende subagent via `brain__log.md` + relevante registers + SessionStart-hook (`.claude/hooks/sessionstart-context.sh`)

Geen externe coördinatie nodig — git history + `brain__log.md` vormen de timeline.

Voor sync met claude.ai PK: zie `docs/migratie-roadmap.md` sectie "Anthropic bug #33875 — mitigatie".

## Sprint-werkproces (samenvatting)

Volledige procedure: `docs/sprint-protocols.md`. Korte samenvatting:

1. Masterchat (claude.ai) schrijft sprint-instructie → `docs/instructies/instructie-v4.X.Y.md`
2. Steven pusht naar GitHub
3. Tech-subagent (Claude Code) leest instructie, raadpleegt `brain/brain__sources__*.md` voor parsing-leidraad
4. Tech-subagent voert sprint uit, levert patch-rapport → `output/reports/patch-rapport-v4_X_Y.md`
5. Bij scope-vraag of NEN-ISO-bron-behoefte: subagent **escaleert naar Steven** (niet zelf interpreteren)
6. Masterchat (claude.ai) review patch-rapport, GO/NO-GO
7. Brein-subagent (Claude Code) doet brain-update post-release
8. Steven pusht, sync naar PK

Stap 5 is de scope-pauze-route. Triggers in `docs/sprint-protocols.md` §15.

## Externe bronnen (NIET in deze repo)

| Categorie | Locatie | Reden |
|---|---|---|
| NEN-restrictief (ISO 27001/27002/27005/31000/22301/22313) | claude.ai PK + `/Users/stevenbouwmeester/grc-sources-licensed/` (lokaal, gitignored) | Licentie verbiedt git-publicatie |
| Patch-rapporten (historisch) | claude.ai PK + `output/reports/` (per release) | Historisch + actueel beide beschikbaar |
| Brain-vault-uploads pre-migratie | claude.ai PK | Migratie-bron — read-only referentie |

Subagent moet bij behoefte aan NEN-restrictieve bron **escaleren naar Steven** als lokale `grc-sources-licensed/`-toegang niet voldoende is — niet via web zoeken, niet aannames doen.

## Reference (verplaatst naar skills)

Het volgende is bewust UIT deze always-on-context gehaald — vraag of lees gericht wanneer relevant:

- **Karpathy LLM-Wiki drie-lagen-pattern** (raw sources / wiki / schema) — `.claude/skills/repo-reference/SKILL.md`
- **Volledig repo-boom-diagram met sub-folders** — `.claude/skills/repo-reference/SKILL.md`
- **Brain-vault organisatie-tabel met patronen + aantallen** — `.claude/skills/repo-reference/SKILL.md`
- **Operations-pattern Ingest/Query/Lint/File-back-detail** — `.claude/skills/repo-reference/SKILL.md`
- **Skills-ecosystem-positionering (4 mechanismen + Tier 1/2-tabellen)** — `.claude/skills/repo-reference/SKILL.md`
- **Optional tooling (Obsidian / qmd / Dataview / Mermaid)** — `.claude/skills/repo-reference/SKILL.md`

Path-scoped reference (auto-load bij relevante paden):
- **D1–D12 + D4.1-conformance-checklist** — `.claude/skills/ontology-conformance/SKILL.md` (`paths: ontology/*.ttl`)
- **Patch-rapport-skelet + bron-typo-beleid + Protocol v1.3 §10.2-§10.5** — `.claude/skills/report-structure/SKILL.md` (`paths: output/reports/*`)

Action-skills:
- **`/canonical-metrics`** — canonieke meet-procedure (Tooling-01)
- **`/shacl-split`** — gesplitste SHACL-validatie A/B/COMBINED (Tooling-01)
- **`/patch-rapport`** — §0-§15-skelet-generator (Tooling-02)

## Spoor B-overweging (toekomst)

GitHub.com is cloud-hosted. Voor Spoor A (huidige fase, geen organisatie-data) acceptabel. Bij Spoor B-overgang (lab-test bij Technologie & Innovatie of latere productie-fase met organisatie-data) heroverwegen naar GitLab-on-prem of organisatie-interne git. Niet nu oplossen; bewust geaccepteerd.

## Versionering van CLAUDE.md

Dit document wijzigt alleen bij wijzigingen in repo-structuur, subagent-architectuur of werk-conventies. Niet bij elke sprint of brain-update.

| Datum | Versie | Wijziging |
|---|---|---|
| 2026-05-21 | 1.0 | Initiële versie door Brein-chat |
| 2026-05-22 | 1.1 | Correcties masterchat: projectinstructie-verwijzing naar v1.9; tabel-formatting hersteld; subagents-lijst teruggebracht naar drie (Tech/Brein/Dashboard) conform migratie-roadmap; expliciete vermelding van vier claude.ai-only chats; toevoeging Spoor B-overweging |
| 2026-05-22 | 1.2 | Vijf toevoegingen na pre-migratie-check: (1) Karpathy drie-lagen-pattern + "compile once, keep current"-framing; (2) Operations-sectie met Ingest/Query/Lint/File-back; (3) File-back-discipline expliciet; (4) Optional tooling-sectie; (5) Skills-ecosystem-positionering met Tier 1+2 post-migratie kandidaten. Tech+Dashboard-subagent-configs incorporeren Karpathy LLM coding-principes (multica-ai). |
| 2026-05-22 | 1.3 | Repo-structuur-update na Steven's structuur-aanmaak: `dashboard/` als toplevel toegevoegd; `output/reports/` + `output/verification/` sub-structuur; `sources/` sub-folders expliciet getoond (adr-norea/ensia/eu-recht/nl-recht/nist/overheid); `docs/migratie-roadmap.md` op toplevel (niet in handovers); macOS-Finder-note over `.claude/` punt-prefix. |
| 2026-05-26 | 1.4 | Iteratie 12 polish-mini-sprint: nieuwe korte sectie "Dashboard-productlijnen (Spoor A vs Spoor B)" tussen repo-structuur en brain-vault-organisatie. Verwijst naar nieuw concept-bestand `brain__concepts__dashboard-productlijnen.md` voor detail. Geen wijziging aan andere secties. |
| 2026-05-27 | 1.5 | Projectinstructie-referenties bijgewerkt na v1.10-publicatie (27 mei 2026): "Actuele projectinstructie"-regel verwijst naar `docs/projectinstructie-v1_10.md` (was v1.9 in PK); rij "Projectinstructie v1.9" verwijderd uit Externe bronnen-tabel (projectinstructie staat sinds v1.8 in `docs/`, niet meer extern). |
| 2026-05-28 | 1.6 | Tooling-02 herstructurering — always-on-laag afgeslankt (~293 → ~140 regels). Verplaatst naar `.claude/skills/repo-reference/`: Karpathy drie-lagen-pattern detail, volledige repo-boom, brain-vault-organisatie-tabel met aantallen, Operations Ingest/Query/Lint/File-back detail, skills-ecosystem 4-mechanismen + Tier 1/2-tabellen, optional tooling-lijst. Nieuwe path-scoped skills: `ontology-conformance` (`paths: ontology/*.ttl`) + `report-structure` (`paths: output/reports/*`). Nieuwe action-skill: `/patch-rapport`. Always-on-invarianten samengevoegd tot één expliciete Werk-conventies-sectie incl. "subagents committen NOOIT zelfstandig" (codificering uit Tooling-01). Verplaatst/gebleven-tabel in `output/reports/tooling-02-implementatierapport.md`. Baseline-versie bijgewerkt naar v4.6.3 (T3 m14 AVG/GDPR). |

— Einde CLAUDE.md
