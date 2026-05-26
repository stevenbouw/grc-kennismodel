---
type: workflow
title: Obsidian-migratie — Stappenplan PK → lokale vault
status: living
date: 2026-05-13
related:
  - CLAUDE
sources: []
chat-sources: []
confidence: high
---

# Obsidian-migratie — Stappenplan PK → lokale vault

## Doel

Deze gids beschrijft hoe je de GRC Kennismodel Brain van **Project Knowledge** (Claude.ai) naar een **lokale Obsidian-vault** migreert. De migratie is **één-malig**; daarna werk je in de lokale vault verder met Claude Code als primaire AI-assistent.

## Wanneer migreren

Trigger-condities die migratie zinvol maken:

| Trigger | Waarom |
|---|---|
| Versie-beheer nodig (git) | Rollback bij fouten, history-tracking, samenwerken |
| Vaak buiten Claude.ai werken | Lokale toegang zonder browser/account |
| Top-10 retrieval-limiet hindert | Grep, dataview, full-text-search op vault-niveau |
| Vault willen delen of forken | Lokale vault is portable |
| Brain integreren in eigen tooling | Standaard markdown + frontmatter = makkelijk te parsen |

**Geen migratie zinvol als:**
- Brain wordt alleen incidenteel geraadpleegd binnen Claude.ai
- Geen comfort met terminal / Node.js / Python
- Geen behoefte aan git-versiebeheer

## Prerequisites

| Vereiste | Versie | Installatie |
|---|---|---|
| Python | 3.10+ | https://python.org of `brew install python` |
| Git | 2.30+ | https://git-scm.com of `brew install git` |
| Obsidian | 1.5+ | https://obsidian.md |
| Node.js (voor Claude Code) | 20+ LTS | https://nodejs.org |
| Claude Code | Latest | `npm install -g @anthropic-ai/claude-code` |

Zie [[CLAUDE]] voor algemene vault-conventies na migratie.

## Stappenplan — overzicht

```
1. Download brain-bestanden uit Project Knowledge
2. Initialiseer lokale doel-folder + git-repo
3. Draai migratie-script (migrate_brain_to_obsidian.py)
4. Verifieer output via migration-report.txt
5. Open vault in Obsidian → installeer aanbevolen plugins
6. Installeer Claude Code → wijs naar vault
7. Smoke-test in nieuwe omgeving
```

Totale tijdsinvestering: 30-90 minuten, afhankelijk van vertrouwdheid met tooling.

## Stap 1 — Download brain uit Project Knowledge

Project Knowledge biedt geen bulk-download. Twee opties:

### Optie 1A — Handmatig (zeker, traag)

Per brain-bestand: in PK-UI openen → kopiëren naar lokaal markdown-bestand → naam intact houden (`brain__folder__slug.md`). Voor ±88 bestanden duurt dit 30-45 minuten.

### Optie 1B — Via Master-chat-export (sneller, batch)

In Master-chat-sessie:
1. Vraag: *"Genereer alle brain-bestanden in /mnt/user-data/outputs/ zodat ik ze kan downloaden."*
2. Master gebruikt `project_knowledge_search` + `create_file` om alle inhoud naar outputs te schrijven
3. Download het hele `outputs/`-folder via de Claude.ai-UI

Plaats alle gedownloade `brain__*.md` bestanden in één lokale **bron-folder**, bv. `~/Downloads/grc-brain-source/`.

## Stap 2 — Initialiseer doel-folder

Kies een locatie voor de lokale Obsidian-vault, bv. `~/Documents/grc-brain/`:

```bash
mkdir -p ~/Documents/grc-brain
cd ~/Documents/grc-brain
git init
git config user.name "<jouw naam>"
git config user.email "<je@email.nl>"
```

## Stap 3 — Draai migratie-script

```bash
# Plaats migrate_brain_to_obsidian.py op je systeem (download uit iteratie 8)
python3 migrate_brain_to_obsidian.py \
    --source ~/Downloads/grc-brain-source \
    --target ~/Documents/grc-brain \
    --create-claude-md \
    --report
```

Het script doet automatisch:

1. **Filename-transformatie:** `brain__folder__slug.md` → `folder/slug.md` (folders worden aangemaakt indien nodig)
2. **Wikilink-update:** `[[brain__folder__slug]]` → `[[slug]]` (Obsidian resolveert padloos)
3. **Root-files:** `brain__index.md`, `brain__log.md`, `brain__CLAUDE.md`, etc. komen op vault-root
4. **CLAUDE.md aanmaken** indien `--create-claude-md` (Claude Code-anchor; vervangt brain__CLAUDE.md inhoudelijk)
5. **Migration-report.txt:** lijst van alle transformaties + ontbrekende files + wikilink-conflicten

Verwachte output:

```
[1/88] decisions/D01_owl-2-dl-profiel.md ✓
[2/88] decisions/D02_turtle-serialisatie.md ✓
...
[88/88] workflow/workflow-register.md ✓

Wikilink-updates: 412 (alle bestanden gescand)
Conflicten: 0
Ontbrekende cross-refs: 0
Rapport: migration-report.txt
```

## Stap 4 — Verifieer output

```bash
# Folder-structuur check
tree -L 2 ~/Documents/grc-brain

# Aantal bestanden per folder
find ~/Documents/grc-brain -name "*.md" | awk -F/ '{print $(NF-1)}' | sort | uniq -c
```

Verwachte counts (na iteratie 7-staat):

| Folder | Files |
|---|---:|
| (root) | 5 (CLAUDE, index, log, archeology-report, smoke-tests) |
| decisions/ | 13 |
| sprints/ | 12 |
| architecture/ | 9 |
| concepts/ | 11 (na iteratie 8 inclusief scope-discipline + meeliftregel) |
| modules/ | 20 |
| sources/ | 8 |
| workflow/ | 6 |
| scope/ | 5 |
| **Totaal** | **89** |

Controleer ook `migration-report.txt` op:
- "Conflicten: 0" — geen duplicate filenames
- "Ontbrekende cross-refs: 0" — alle wikilinks resolveren

Eerste git-commit:

```bash
cd ~/Documents/grc-brain
git add .
git commit -m "Initial migration from Project Knowledge (iteratie 8)"
```

## Stap 5 — Open in Obsidian

1. Start Obsidian
2. **Open folder as vault** → kies `~/Documents/grc-brain`
3. Verifieer dat wikilinks werken: open `index.md`, klik op een willekeurige `[[link]]`
4. Check graph view (cmd/ctrl+G): je zou een dichte graaf moeten zien met clusters per folder

### Aanbevolen Obsidian-plugins

Via Settings → Community plugins → Browse:

| Plugin | Doel | Configuratie-hint |
|---|---|---|
| **Dataview** | Query-able tabellen over frontmatter | Default config volstaat |
| **Templater** | Templates voor nieuwe files | Maak templates per type (decision/sprint/H-item) |
| **Outliner** | Betere nested lists | Default config |
| **Tag Wrangler** | Tag-management indien je tags toevoegt | Optioneel |
| **Git** | Auto-commit, sync naar remote | Stel auto-commit interval in op 15-30 min |

### Aanbevolen Workspace-layout

- **Left sidebar:** File explorer + tags
- **Right sidebar:** Outline + Backlinks
- **Bottom:** Open notes per folder via "Open vault in new tab"

### Dataview-voorbeeld-queries

In `index.md` of een nieuwe `dashboard.md`:

````markdown
## Alle open H-items

```dataview
TABLE status, date
FROM "architecture"
WHERE status = "open"
SORT date DESC
```

## Alle sprints (chronologisch)

```dataview
TABLE date, status
FROM "sprints"
SORT date DESC
```

## Modules per laag

```dataview
TABLE related
FROM "modules"
WHERE id != null
SORT id ASC
```
````

## Stap 6 — Installeer Claude Code

```bash
npm install -g @anthropic-ai/claude-code
cd ~/Documents/grc-brain
claude
```

Claude Code leest automatisch `CLAUDE.md` bij sessie-start en gebruikt het als instructie-anchor. Vraag bij eerste sessie:

> "Lees CLAUDE.md en index.md en geef me een samenvatting van de vault-staat."

Verifieer dat Claude Code de structuur begrijpt en aangeeft welke folders welke inhoud bevatten.

## Stap 7 — Smoke-test in nieuwe omgeving

Draai de 10 smoke-tests uit `smoke-tests.md` opnieuw, deze keer via Claude Code in plaats van Project Knowledge. Vergelijk antwoorden met verwachte uitkomsten.

Verschil met PK:
- Claude Code heeft **volledige file-system-toegang** — kan grep, file-trees, etc.
- Geen top-10 retrieval-limiet — Claude Code leest specifiek welke files relevant zijn
- Wel: Claude Code laadt niet automatisch alles. Per vraag bepaalt het welke files te lezen.

Bij eerste sessie: vraag expliciet *"Lees eerst architecture/H-register.md voordat je deze vraag beantwoordt"* om Claude Code te trainen op de vault-conventies.

## Troubleshooting

### Wikilinks resolveren niet

- Check of de target-file bestaat in een andere folder met dezelfde naam
- Obsidian instellingen → "Files & Links" → "New link format" op `Shortest path when possible`
- Bij duplicate filenames: gebruik volledige pad in wikilink, bv. `[[modules/M01_framework]]`

### Migratie-script faalt op specifieke file

- Check filename voor speciale tekens (spaties, slashes binnen `__`-segmenten)
- Open de file handmatig, check frontmatter-validiteit (geen tabs in plaats van spaties)
- Run script met `--verbose` voor detail-logging

### Claude Code leest CLAUDE.md niet

- Verifieer dat je in de vault-root bent (`pwd` toont `~/Documents/grc-brain`)
- Check dat `CLAUDE.md` op vault-root staat (niet in een subfolder)
- Restart Claude Code-sessie

### Git-conflicts bij synchronisatie

- Vault is **single-user** ontworpen. Multi-user sync via git werkt, maar conflicts op `log.md` kunnen ontstaan
- Discipline: log.md alleen wijzigen via Master-rol (één persoon per moment)
- Bij conflict: handmatig mergen, behoud chronologische volgorde nieuwste-bovenop

## Post-migratie — eerste sessie checklist

- [ ] CLAUDE.md leesbaar voor Claude Code
- [ ] index.md toont juiste folder-counts
- [ ] log.md heeft iteratie 8 entry op top
- [ ] 88+ markdown-files in vault (zie verwachte counts)
- [ ] Alle wikilinks resolveren (geen rode links in Obsidian)
- [ ] Smoke-test 1 (open H-items) levert juiste uitkomst
- [ ] Smoke-test 7 (UCF-uitsluiting) levert juiste uitkomst
- [ ] Eerste git-commit gemaakt
- [ ] Aanbevolen Obsidian-plugins geïnstalleerd

Bij vinkjes 8/8: brain is operationeel in Optie C-modus.

## Onderhoudsritme post-migratie

Identiek aan Project Knowledge-werkwijze (zie [[CLAUDE]]) — alleen via Claude Code in plaats van Claude.ai-UI:

- Nieuwe sprint: sprint-file + log-entry + sprint-register update + git commit
- Nieuwe D-decision: D-file + D-register update + log-entry + git commit
- Periodiek: smoke-tests draaien

## Rollback-pad

Mocht migratie problemen geven en je wil terug naar PK:

1. Project Knowledge zelf is **niet gewijzigd** door de migratie — de brain staat daar nog steeds
2. Lokale vault gewoon laten staan of verwijderen
3. Werk hervat in PK zoals vóór iteratie 8

Geen risico om iteratie 8 uit te voeren.

---

**Einde migratie-gids.**
