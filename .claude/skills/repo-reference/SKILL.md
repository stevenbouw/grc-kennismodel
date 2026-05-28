---
name: repo-reference
description: Reference material for the GRC Kennismodel repo — Karpathy LLM-Wiki three-layer pattern, full repo folder tree, brain-vault organization with file counts per category, Karpathy Operations pattern (Ingest/Query/Lint/File-back) detail, Claude skills-ecosystem positioning (4 mechanisms + Tier 1/2 evaluation candidates), optional tooling (Obsidian / qmd / Dataview / Mermaid). Use when asked about folder layout, brain-vault file counts, available skills, external tool recommendations, or how this repo maps onto the Karpathy pattern. Material was moved out of CLAUDE.md (Tooling-02) to keep the always-on context lean.
---

# repo-reference — GRC Kennismodel repo reference

Verplaatst uit CLAUDE.md tijdens Tooling-02 (28 mei 2026) om de always-on-context af te slanken. Inhoud is reference, geen invariant. Invarianten (organisatienaam, D9-neutraliteit, NEN-parafrase, status-discipline, BBN-correctie, geen autonome commit) blijven in CLAUDE.md zelf.

## 1. Karpathy LLM-Wiki drie-lagen-pattern

De repo volgt het Karpathy LLM-Wiki-patroon ([gist.github.com/karpathy/442a6bf555914893e9891c11519de94f](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), april 2026) met drie lagen:

| Karpathy-laag | Onze invulling |
|---|---|
| Raw sources (immutable) | `sources/` (publiek-domein) + claude.ai PK (NEN-restrictief) + `/Users/stevenbouwmeester/grc-sources-licensed/` (lokaal, gitignored) |
| The wiki (LLM-maintained) | `brain/` + `ontology/` + `output/` + `dashboard/` |
| The schema (config) | `CLAUDE.md` + `docs/sprint-protocols.md` + `.claude/agents/*.md` + `.claude/settings.json` + `.claude/hooks/` + `.claude/skills/` |

Kerngedachte: **"compile once, keep current"**. Bronnen worden eenmaal verwerkt naar brain-vault + ontologie; de wiki blijft synchroon met realiteit zonder dat sources telkens herverwerkt worden. Subagents zijn wiki-onderhouders, geen RAG-systemen.

## 2. Volledig repo-boom-diagram

```
grc-kennismodel/
├── brain/                    ~101 brain__*.md (vault)
├── ontology/                 22 .ttl-modules (huidig: v4.6.3)
├── sources/                  publiek-domein bronnen
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
│   ├── projectinstructie-v1_10.md  actuele projectinstructie
│   ├── instructies/              masterchat → tech-subagent
│   └── handovers/                master-handover-documenten
├── scripts/                  utilities
├── output/
│   ├── reports/              patch-rapporten, inventarisaties, tussenrapporten,
│   │                         scope-pauzes, lint-rapporten, tooling-rapporten
│   └── verification/         canonical_metrics_*.{py,json} +
│                             shacl_split_validate_*.{py,json} +
│                             file_hashes_*.txt
├── .claude/
│   ├── agents/               tech.md + brein.md + dashboard.md
│   ├── hooks/                secret-scan, disclosure-check, versie-suffix-check,
│   │                         sessionstart-context + disclosure-config(.local)
│   ├── skills/               canonical-metrics, shacl-split, patch-rapport,
│   │                         ontology-conformance, report-structure, repo-reference
│   ├── settings.json         versioned permissions + hooks-config
│   └── settings.local.json   lokale overrides (gitignored)
├── CLAUDE.md                 always-on autoload-context
└── README.md                 publieke projectbeschrijving
```

**Let op**: `.claude/` map heeft punt-prefix (Unix-conventie). Op macOS-Finder verborgen tenzij Cmd+Shift+. wordt gedrukt.

## 3. Brain-vault organisatie

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

Vault-spec voor brain-onderhoud: `brain/brain__CLAUDE.md`.

## 4. Operations — Karpathy Ingest/Query/Lint + File-back

### 4.1 Ingest

Twee paden afhankelijk van scope:

| Pad | Trigger | Workflow |
|---|---|---|
| Sprint-ingest (groot) | Masterchat-instructie voor sprint-werk | Volledige sprint-cyclus via `docs/sprint-protocols.md`. Per ingest worden 8-15 brain-pagina's geraakt. |
| Losse bron-ingest (klein) | Nieuwe versie bestaande bron (bv. nieuwe ENSIA-handreiking) zonder TBox-impact | Bron in `sources/`; relevant `brain__sources__*.md` bijwerken; eventuele log-entry; geen volledige sprint. Bij twijfel of bron TBox-implicaties heeft: escaleer naar Steven. |

Bron-typo-beleid (sprint-protocol §1.9 / Protocol 13): typo's in nieuwe-individu rdfs:label corrigeren; typo's in referentie-targets behouden.

### 4.2 Query

Wanneer een subagent (Tech/Brein/Dashboard) een vraag krijgt van masterchat (via Steven):

1. Start bij `brain__index.md` voor scope-bepaling
2. Drill via relevante register (decisions/sprints/H-items/concepts/modules/sources/workflow/scope)
3. Lees specifieke brain-bestanden
4. Synthesize antwoord met bron-citaties (welke brain-bestanden gebruikt)
5. Indien antwoord nieuw inzicht oplevert dat algemeen relevant is: zie File-back hieronder

### 4.3 Lint

Periodieke health-check van brain-vault. Niet sprint-gebonden, maar planbaar (suggestie: na elke 3 minor-releases of bij twijfel over coherentie).

Brein-subagent draait gestructureerde check:

- Contradicties tussen registers (bv. H-register zegt H36 active maar concepts-register noemt het closed)
- Stale H-items (open >6 maanden zonder trigger-update)
- Orphan brain-bestanden (geen inbound wikilinks vanuit register)
- Missing cross-references (D-decision X verwijst niet naar relevante H-items)
- Outdated baseline-cijfers in modules/sprints na latere correcties

Output: lint-rapport in `output/reports/lint-<datum>.md`. Severity-tiered findings (🔴 errors / 🟡 warnings / 🔵 info) met concrete fix-voorstellen. Masterchat beslist welke fixes uitgevoerd worden.

### 4.4 File-back

Belangrijke Q&A-inzichten uit masterchat-sessies (claude.ai) of subagent-query's (Claude Code) blijven niet hangen in chat-historie — ze landen terug in de brain-vault als concept-file of H-item.

Regels:

- Tech/Brein/Dashboard-subagent kan een **file-back-voorstel** doen ("dit antwoord lijkt nieuw inzicht — concept-file vereist?")
- File-back wordt nooit autonoom uitgevoerd door subagent — altijd masterchat-besluit via Steven
- File-back gebeurt typisch tijdens volgende Brein-cyclus (na sprint-afsluiting) of via Brein-tussentijdse activering bij urgentie
- File-back-criterium: inzicht komt twee of meer keer terug in conversaties zonder centrale documentatie

## 5. Skills-ecosystem-positionering

Het Claude-ecosystem heeft vier extension-mechanismen die in deze repo verschillend worden ingezet:

| Mechanisme | Wat | Onze invulling |
|---|---|---|
| **CLAUDE.md** | Autoload-context per repo | `CLAUDE.md` (root) + `brain/brain__CLAUDE.md` |
| **Subagents** | Specialized sub-instances voor task isolation | Tech, Brein, Dashboard (zie `.claude/agents/`) |
| **Skills** | On-demand workflows (SKILL.md + frontmatter); Claude beslist zelf wanneer aan te roepen op basis van `description` (en optioneel `paths`) | Eigen skills: canonical-metrics, shacl-split, patch-rapport, ontology-conformance (path-scoped), report-structure (path-scoped), repo-reference (deze) |
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

## 6. Optional tooling

Aanbevolen tools voor brain-vault-onderhoud en query — alle optioneel, geen verplichting:

| Tool | Doel | Wanneer relevant |
|---|---|---|
| **Obsidian** | Brain-vault-browsing met graph-view en wikilink-resolutie | Lokaal werken in vault; zie `brain/brain__obsidian-migration-guide.md` |
| **qmd** ([tobi/qmd](https://github.com/tobi/qmd)) | Hybride BM25 + vector search over markdown-vault | Wanneer brain >150 bestanden wordt en `brain__index.md` als entry-point ontoereikend wordt |
| **Dataview** (Obsidian-plugin) | Frontmatter-queries over brain-vault | Voor cross-cutting overzichten (bv. "alle H-items van status 'open' gesorteerd op datum") |
| **Mermaid** (in markdown) | Architectuur-diagrammen inline in brain-bestanden | Voor visuele toelichting van complexe relaties tussen modules/decisions |

Niet aanbevolen voor dit project (afwijkend van Karpathy-pattern):
- **Obsidian Web Clipper** — wij krijgen bronnen via formele kanalen, geen web-scraping
- **Marp** — wij maken geen presentaties uit brain-vault
- **Vector-database voor RAG** — Karpathy-pattern verwerpt RAG; index + register volstaat tot ~500 bestanden

## Cross-references

- Always-on-invarianten: `CLAUDE.md` §"Werk-conventies"
- Path-scoped ontologie-regels: `.claude/skills/ontology-conformance/SKILL.md`
- Path-scoped rapport-skelet: `.claude/skills/report-structure/SKILL.md`
- Action-skills voor verificatie: `.claude/skills/canonical-metrics/`, `.claude/skills/shacl-split/`
- Action-skill voor patch-rapport: `.claude/skills/patch-rapport/`
