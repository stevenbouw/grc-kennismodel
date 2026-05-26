# GRC Kennismodel — Repo Root

> **Voor Claude Code:** dit is de vault-root van het GRC Kennismodel-project. Begin met `brain/brain__index.md` als entry-point voor het project en `brain/brain__log.md` voor recente sprints. Lees `docs/sprint-protocols.md` voor verplichte werkwijze tijdens sprints.

## Wat is dit

Karpathy-stijl digital brain + ontologie-werkfolder voor het GRC Kennismodel-project van de Rijksoverheidsorganisatie. De repo combineert:

- **Brain-vault** (~101 markdown-bestanden) — architectuur-beslissingen, sprints, modules, concepts, bronnen, workflows
- **Ontologie-modules** (22 .ttl-bestanden) — OWL 2 DL formele kennisbasis
- **Publiek-domein bronnen** — NIST, EU-recht, NL-recht, ADR/NOREA, overheidspublicaties
- **Scripts** — canonical metrics, SHACL-validatie
- **Dashboard** — grc-explorer HTML + build-pipeline + JSON-data
- **Docs** — sprint-instructies, sprint-protocollen, handovers, migratie-roadmap

**Huidige ontologie-baseline:** v4.6.0 (Fase 4 — M15-ENSIA + Volwassenheidsmodel), opgeleverd 21 mei 2026.
**Actuele projectinstructie:** `projectinstructie-v1.9.md` (in PK, niet in deze repo om licentie-redenen — zie sectie "Externe bronnen").

## Karpathy-pattern toepassing

De repo volgt het Karpathy LLM Wiki-patroon ([gist.github.com/karpathy/442a6bf555914893e9891c11519de94f](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), april 2026) met drie lagen:

| Karpathy-laag | Onze invulling |
|---|---|
| Raw sources (immutable) | `sources/` (publiek-domein) + claude.ai PK (NEN-restrictief) |
| The wiki (LLM-maintained) | `brain/` + `ontology/` + `output/` + `dashboard/` |
| The schema (config) | Dit CLAUDE.md + `docs/sprint-protocols.md` + `.claude/agents/*.md` |

Kerngedachte: **"compile once, keep current"**. Bronnen worden eenmaal verwerkt naar brain-vault + ontologie; de wiki blijft synchroon met realiteit zonder dat sources telkens herverwerkt worden. Subagents zijn wiki-onderhouders, geen RAG-systemen.

## Repo-structuur

```
grc-kennismodel/
├── brain/                    ~101 brain__*.md (vault)
├── ontology/                 22 .ttl-modules v4.6.0
├── sources/                  publiek-domein bronnen (zie sectie "Externe bronnen")
│   ├── adr-norea/
│   ├── ensia/
│   ├── eu-recht/
│   ├── nl-recht/
│   ├── nist/
│   └── overheid/
├── dashboard/                grc-explorer HTML + build-pipeline + JSON-data
│   ├── build_grc_explorer_v3.py
│   ├── grc-data-v4_6_0.json
│   ├── grc-data-v4_6_0.js
│   └── grc-explorer-v4_6_0.html
├── docs/
│   ├── sprint-protocols.md       verplichte werkwijze tijdens sprints
│   ├── migratie-roadmap.md       levend uitvoeringsdocument
│   ├── instructies/              masterchat → tech-subagent
│   └── handovers/                master-handover-documenten
├── scripts/                  canonical metrics + SHACL-validatie + utilities
├── output/
│   ├── reports/              patch-rapporten, inventarisaties, tussenrapporten, scope-pauzes, lint-rapporten
│   └── verification/         canonical_metrics_*.json + shacl_results_*.json + file_hashes_*.txt + bijbehorende Python-scripts
├── .claude/agents/           drie subagent-configs (Tech, Brein, Dashboard)
├── CLAUDE.md                 dit document
└── README.md                 publieke projectbeschrijving
```

**Let op**: `.claude/` map heeft punt-prefix (Unix-conventie). Op macOS-Finder verborgen tenzij Cmd+Shift+. wordt gedrukt.

## Dashboard-productlijnen (Spoor A vs Spoor B)

Twee parallelle dashboard-productlijnen met fundamenteel verschillende doelen:

- **`grc-explorer-*`** (Spoor A) — read-only ontologie-graaf-verkenner; data uit `grc-data-v[X_Y_Z].js`; Cytoscape.js-engine; beweegt mee met ontologie-versie. Actueel: `dashboard/grc-explorer-v4_6_0.html`.
- **`grc-dashboard-*`** (Spoor B) — operationele werkmap-prototype voor CRUD, audit-trail, kalender, RACI; data uit lokale SQL.js `.db`; Chart.js + SQL.js-engine; eigen versie-track. Actueel: `grc-dashboard-v3-2.html` (lokaal bij Steven, locatie in repo open punt).

Niet vermengen in één UI — verschillende doelen, datamodel en engine. Detail + discipline: zie `brain/brain__concepts__dashboard-productlijnen.md`. Scope-afbakening van H40 (UI-renderdekking) betreft uitsluitend Spoor A.

## Brain-vault organisatie

Files in `brain/` zijn **flat** met folder-structuur gecodeerd via `__`-separator (compatible met claude.ai Project Knowledge platte filelijst):

| Patroon | Inhoud | Aantal |
|---|---|---:|
| `brain__decisions__D{NN}_*.md` | D-decisions (immutable na vaststelling) | 12 + register |
| `brain__sprints__v{X_Y_Z}_*.md` | Sprint-files (immutable na release) | 14 + register |
| `brain__architecture__H{NN}_*.md` | H-items (open architectuur-vragen) | 11 + register |
| `brain__concepts__*.md` | Concepts / domein-glossary | 13 + register |
| `brain__modules__M{NN}_*.md` | Modules M01-M18 + M21 (living) | 19 + register |
| `brain__sources__*.md` | Input-bronnen + licentie + parsing-leidraad | 7 + register |
| `brain__workflow__*.md` | Chat-rollen, scope-discipline, sprint-protocollen | 6 + register |
| `brain__scope__*.md` | Bewuste uitsluitingen + hardverwijderd | 4 + register |

Plus root-files: `brain__index.md`, `brain__log.md`, `brain__smoke-tests.md`, `brain__archeology-report.md`, `brain__CLAUDE.md` (vault-spec), `brain__obsidian-migration-guide.md`.

Vault-spec voor brain-onderhoud: zie `brain/brain__CLAUDE.md`.

## Werk-conventies (verplicht voor alle subagents)

- **Communicatie in het Nederlands** — ontologie-annotaties bilinguaal @nl/@en (D6)
- **Organisatienaam wordt NOOIT genoemd** — altijd "de organisatie" of "Rijksoverheidsorganisatie"
- **Framework-neutraal** (D9) — alle frameworks gelijkwaardig; BIO 2.0 alleen als view-keuze in dashboard, niet architecturaal
- **Scope-discipline** — bij scope-afwijking PAUZE en rapport (Optie A/B/C); niet zelf interpreteren. Zie `docs/sprint-protocols.md` voor exacte triggers
- **D-decisions zijn immutable** — wijziging vereist masterchat-goedkeuring in claude.ai (via Steven als tussenmens)
- **Append-only log** — `brain/brain__log.md` nieuwste entry bovenaan, alleen append nooit edit
- **Sprint-protocollen verplicht** — alle 12 protocollen + 1 gedragsregel uit `docs/sprint-protocols.md` zijn niet-onderhandelbaar
- **Bron-attribuering** — bij gebruik externe bronmaterialen: `ext:sourceAttribution` declareren; SHA256 bij snapshot-bronnen

## Hoe te lezen (entry-points)

Bij een nieuwe vraag over het project:

1. **`brain/brain__index.md`** — masteroverzicht en huidige baseline
2. **`brain/brain__{folder}__-register.md`** — navigatie binnen specifiek domein (decisions/sprints/etc.)
3. **`brain/brain__log.md`** — chronologische context, laatste sprints

Voor specifieke onderwerpen: zoek op D-nummer, H-nummer, M-nummer, versienummer of framework-naam.

Voor werkwijze: **`docs/sprint-protocols.md`** is autoritatief.

## Operations

Karpathy's drie-operations-pattern (Ingest/Query/Lint), aangevuld met onze File-back-discipline.

### Ingest

Twee paden afhankelijk van scope:

| Pad | Trigger | Workflow |
|---|---|---|
| **Sprint-ingest** (groot) | Masterchat-instructie voor sprint-werk | Volledige sprint-cyclus via `docs/sprint-protocols.md`. Per ingest worden 8-15 brain-pagina's geraakt. |
| **Losse bron-ingest** (klein) | Nieuwe versie bestaande bron (bv. nieuwe ENSIA-handreiking) zonder TBox-impact | Bron in `sources/`; relevant `brain__sources__*.md` bijwerken; eventuele log-entry; geen volledige sprint. Bij twijfel of bron TBox-implicaties heeft: escaleer naar Steven voor masterchat-overleg. |

Bron-typo-beleid (sprint-protocol §1.9): typo's in nieuwe-individu rdfs:label corrigeren; typo's in referentie-targets behouden.

### Query

Wanneer een subagent (Tech/Brein/Dashboard) een vraag krijgt van masterchat (via Steven):

1. Start bij `brain__index.md` voor scope-bepaling
2. Drill via relevante register (decisions/sprints/H-items/concepts/modules/sources/workflow/scope)
3. Lees specifieke brain-bestanden
4. Synthesize antwoord met bron-citaties (welke brain-bestanden gebruikt)
5. Indien antwoord een blijkend nieuw inzicht oplevert dat algemeen relevant is: zie File-back hieronder

### Lint

Periodieke health-check van brain-vault. Niet sprint-gebonden, maar planbaar (suggestie: na elke 3 minor-releases of bij twijfel over coherentie).

Brein-subagent draait gestructureerde check:

- Contradicties tussen registers (bv. H-register zegt H36 active maar concepts-register noemt het closed)
- Stale H-items (open >6 maanden zonder trigger-update)
- Orphan brain-bestanden (geen inbound wikilinks vanuit register)
- Missing cross-references (D-decision X verwijst niet naar relevante H-items)
- Outdated baseline-cijfers in modules/sprints na latere correcties

Output: lint-rapport in `output/reports/lint-<datum>.md`. Bevat severity-tiered findings (🔴 errors / 🟡 warnings / 🔵 info) met concrete fix-voorstellen. Masterchat beslist welke fixes uitgevoerd worden.

### File-back

Belangrijke Q&A-inzichten uit masterchat-sessies (claude.ai) of subagent-query's (Claude Code) blijven niet hangen in chat-historie — ze landen terug in de brain-vault als concept-file of H-item.

**Regels:**

- Tech/Brein/Dashboard-subagent kan een **file-back-voorstel** doen ("dit antwoord lijkt nieuw inzicht — concept-file vereist?")
- File-back wordt nooit autonoom uitgevoerd door subagent — altijd masterchat-besluit via Steven
- File-back gebeurt typisch tijdens volgende Brein-cyclus (na sprint-afsluiting) of via Brein-tussentijdse activering bij urgentie
- File-back-criterium: inzicht komt twee of meer keer terug in conversaties zonder centrale documentatie

## Subagents (drie in deze repo)

Drie chats zijn naar Claude Code gemigreerd; vier blijven in claude.ai.

| Subagent | Rol | Config |
|---|---|---|
| **Tech** | Ontologie-engineering (OWL/SPARQL/SHACL/Turtle) | `.claude/agents/tech.md` |
| **Brein** | Brain-vault-onderhoud na elke minor-release | `.claude/agents/brein.md` |
| **Dashboard** | Visualisatie + grc-explorer.html + build-pipeline | `.claude/agents/dashboard.md` |

Aanroepen vanuit Claude Code: `claude --agent tech` of via Task-tool binnen een hoofdsessie.

Tech- en Dashboard-subagent-configs incorporeren expliciet de Karpathy LLM coding-discipline (vier principes uit [github.com/multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)): Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution. Beide chats doen actief code-werk; discipline-laag is daar relevant.

### Chats die in claude.ai blijven (geen subagent-config in deze repo)

| Chat | Reden niet migreren |
|---|---|
| **Master** | Strategisch sparren past niet in terminal-only Claude Code |
| **Documentatie** | Tekst-werk past bij conversationele chat |
| **Analyse** | Incidenteel exploratief werk |
| **Asset** | Afgerond sinds M18-oplevering (v4.2.0), stand-by |

Werkproces tussen Claude Code en claude.ai: Steven (projecteigenaar) is tussenmens bij scope-pauzes en architectuur-beslissingen. Subagent escaleert naar Steven; Steven raadpleegt Master-chat in claude.ai; Steven brengt besluit terug.

## Cross-chat-bewustzijn

De repo is **shared state** tussen alle Claude-sessies (subagents in Claude Code én chats in claude.ai). Werk-wijzigingen worden:

1. **In de vault/ontology/scripts/dashboard gepersisteerd** (file edits)
2. **`brain/brain__log.md` ge-update** (nieuwste entry bovenaan; alleen append)
3. **Via git gecommit** met betekenisvolle commit messages
4. **Bij sessie-start gelezen** door volgende subagent via `brain__log.md` + relevante registers

Geen externe coördinatie nodig — git history + `brain__log.md` vormen de timeline.

Voor sync met claude.ai PK: zie `docs/migratie-roadmap.md` sectie "Anthropic bug #33875 — mitigatie" (PAT + periodieke export-fallback).

## Sprint-werkproces (samenvatting)

Volledige procedure: zie `docs/sprint-protocols.md`. Korte samenvatting voor context:

1. Masterchat (claude.ai) schrijft sprint-instructie → `docs/instructies/instructie-v4.X.Y.md`
2. Steven pusht naar GitHub
3. Tech-subagent (Claude Code) leest instructie, raadpleegt `brain/brain__sources__*.md` voor parsing-leidraad
4. Tech-subagent voert sprint uit, levert patch-rapport → `output/reports/patch-rapport-v4_X_Y.md`
5. Bij scope-vraag of NEN-ISO-bron-behoefte: subagent **escaleert naar Steven** (niet zelf interpreteren)
6. Masterchat (claude.ai) review patch-rapport, GO/NO-GO
7. Brein-subagent (Claude Code) doet brain-update post-release
8. Steven pusht, sync naar PK

Stap 5 is de **scope-pauze-route**. Zie `docs/sprint-protocols.md` voor exacte triggers.

## Skills-ecosystem-positionering

Het Claude-ecosystem heeft vier extension-mechanismen die in deze repo verschillend worden ingezet:

| Mechanisme | Wat | Onze invulling |
|---|---|---|
| **CLAUDE.md** | Autoload-context per repo | Dit document + `brain/brain__CLAUDE.md` |
| **Subagents** | Specialized sub-instances voor task isolation | Tech, Brein, Dashboard (zie `.claude/agents/`) |
| **Skills** | On-demand workflows (SKILL.md + frontmatter); Claude beslist zelf wanneer aan te roepen | Geen eigen skills nu — externe kandidaten in evaluatie post-migratie (zie hieronder) |
| **MCP servers** | Externe tools via protocol | Geen actief nu — open-ontologies-MCP onder evaluatie (zie H-register) |

Externe skills/tools onder evaluatie voor post-migratie inzet:

### Tier 1 — GRC-domein

| Bron | Status | Use-case |
|---|---|---|
| [Sushegaad/Claude-Skills-Governance-Risk-and-Compliance](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance) | Te evalueren post-migratie | Kennis-injectie tijdens sprint-werk voor ISO 27001, NIST CSF, NIS2, ISO 42001 (M19), DORA, GDPR, ISO 27701 |
| [GRCEngClub/claude-grc-engineering](https://github.com/GRCEngClub/claude-grc-engineering) | Te evalueren post-migratie | Evidence collection, SCF crosswalks, OSCAL workflows. Past beter bij Spoor B / lab-test-fase |

**Caveat voor Tier 1**: skills zijn niet auditief geverifieerd. NEN-tekst, EU-Publications-Office en NIST.gov blijven autoritatieve bron. Skills dienen als snelle semantische context, niet als bron-vervanger.

### Tier 2 — Ontologie + brain-vault

| Bron | Status | Use-case |
|---|---|---|
| [fabio-rovai/open-ontologies (MCP)](https://github.com/fabio-rovai/open-ontologies) | H-item geregistreerd; te evalueren post-migratie | Alternatief voor rdflib+owlrl+pySHACL — Rust binary met Oxigraph + tableaux-reasoner. Sterker dan OWL RL voor OWL 2 DL. Niet vervangen, eerst evalueren |
| [kfchou/wiki-skills](https://github.com/kfchou/wiki-skills) | Te evalueren post-migratie | Karpathy LLM Wiki pattern voor periodieke brain-vault lint. Aanvulling op sprint-driven Brein-cyclus |

Beide Tier 2-skills te evalueren wanneer eerste post-migratie-sprint (v4.7.0) is voltooid en stabiele werkbasis bestaat.

## Externe bronnen (NIET in deze repo)

| Categorie | Locatie | Reden |
|---|---|---|
| NEN-restrictief (ISO 27001/27002/27005/31000/22301/22313) | claude.ai PK | Licentie verbiedt git-publicatie |
| Projectinstructie v1.9 | claude.ai PK | Autoritatief document; sync via PK |
| Patch-rapporten (historisch) | claude.ai PK + `output/reports/` (per release) | Historisch + actueel beide beschikbaar |
| Brain-vault-uploads pre-migratie | claude.ai PK | Migratie-bron — read-only referentie |

Subagent moet bij behoefte aan NEN-restrictieve bron **escaleren naar Steven** — niet via web zoeken, niet aannames doen.

## Optional tooling

Aanbevolen tools voor brain-vault-onderhoud en query — alle optioneel, geen verplichting:

| Tool | Doel | Wanneer relevant |
|---|---|---|
| **Obsidian** | Brain-vault-browsing met graph-view en wikilink-resolutie | Lokaal werken in vault; zie ook `brain/brain__obsidian-migration-guide.md` |
| **qmd** ([tobi/qmd](https://github.com/tobi/qmd)) | Hybride BM25 + vector search over markdown-vault | Wanneer brain >150 bestanden wordt en `brain__index.md` als entry-point ontoereikend wordt |
| **Dataview** (Obsidian-plugin) | Frontmatter-queries over brain-vault | Voor cross-cutting overzichten (bv. "alle H-items van status 'open' gesorteerd op datum") |
| **Mermaid** (in markdown) | Architectuur-diagrammen inline in brain-bestanden | Voor visuele toelichting van complexe relaties tussen modules/decisions |

Niet aanbevolen voor dit project (afwijkend van Karpathy-pattern):
- **Obsidian Web Clipper** — wij krijgen bronnen via formele kanalen, geen web-scraping
- **Marp** — wij maken geen presentaties uit brain-vault
- **Vector-database voor RAG** — Karpathy-pattern verwerpt RAG; index + register volstaat tot ~500 bestanden

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

— Einde CLAUDE.md
