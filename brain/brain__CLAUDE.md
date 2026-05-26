---
type: workflow
id: vault-spec
title: CLAUDE.md — Vault-spec voor GRC Kennismodel Brain
status: living
date: 2026-05-13
version: 1.0
---

# CLAUDE.md — GRC Kennismodel Brain (vault-spec)

> Karpathy LLM Wiki pattern, aangepast voor claude.ai Project Knowledge.
> Versie: 1.0 (13 mei 2026) — gegenereerd in iteratie 0.

## Wat dit is

Deze vault is het project-geheugen voor het **GRC Kennismodel** van de Rijksoverheidsorganisatie. Het is een door de LLM onderhouden, mens-leesbare collectie markdown-bestanden die D-decisions, sprint-log, H-items, concepts, modules, sources en workflow-conventies vastlegt.

Geen organisatie-context, geen CV/loopbaan, geen persoonlijke materialen — **alleen project-werk** binnen scope GRC Kennismodel.

Karpathy-quote als richtsnoer: *"Obsidian is the IDE. The LLM is the programmer. The wiki is the codebase."* In Optie A draait deze vault op claude.ai Project Knowledge (read-only voor de LLM, manuele upload door de gebruiker); bij Optie C-overgang verhuist hij naar een lokale Obsidian-vault met Claude Code als wiki-maintainer.

## Scope-grens

In de vault:

- D-decisions (D1–D12 en toekomstige)
- Sprint-log (v0.1 onwards, doorlopend)
- H-items (open architectuur-vragen, parkeerlijst, toekomst-overwegingen)
- Concepts / domein-glossary
- Modules M01–M18 (+ gepland M21)
- Sources (input-bronnen, hun rol en licentie)
- Normenkader-hiërarchie Laag 0–5
- Chat-rolverdeling, scope-discipline, technische conventies
- Missie/visie/toepassingen, licentie-bewustzijn, hardverwijderde elementen, scope-uitsluitingen
- Management-communicatie *als artefact* (elevator pitch, etc.), niet de organisatie-context erachter

Niet in de vault:

- CV, loopbaan, sollicitatie-materiaal
- Persoonlijke context
- Organisatie-info buiten het kennismodel-werk

## Folder-structuur (filename-encoded)

Project Knowledge in claude.ai is een platte filelijst. Daarom wordt de folder-structuur **in de bestandsnaam gecodeerd** met `__` (dubbele underscore) als pad-separator.

| Bestandsnaam (Project Knowledge) | Pad in Obsidian-vault (Optie C) |
|---|---|
| `brain__CLAUDE.md` | `brain/CLAUDE.md` |
| `brain__index.md` | `brain/_index.md` |
| `brain__log.md` | `brain/_log.md` |
| `brain__decisions__D09_*.md` | `brain/decisions/D09_*.md` |
| `brain__sprints__v4_3_3_*.md` | `brain/sprints/v4_3_3_*.md` |
| `brain__architecture__H25_*.md` | `brain/architecture/H25_*.md` |
| `brain__concepts__*.md` | `brain/concepts/*.md` |
| `brain__modules__M08_*.md` | `brain/modules/M08_*.md` |
| `brain__sources__*.md` | `brain/sources/*.md` |
| `brain__workflow__*.md` | `brain/workflow/*.md` |
| `brain__scope__*.md` | `brain/scope/*.md` |

Categorieën:

- **decisions/** — D-register, één file per D. Immutable na vaststelling; alleen `status` mag wijzigen (active → superseded).
- **sprints/** — Eén file per versie. Immutable na release.
- **architecture/** — H-items. Living tot resolution.
- **concepts/** — Domein-glossary. Living.
- **modules/** — M01–M18 + M21-planned. Living per sprint.
- **sources/** — Input-bronnen. Wat het is, licentie, hoe het in het model landt.
- **workflow/** — Chat-rollen, scope-discipline, technische conventies.
- **scope/** — Buiten-scope (UCF, etc.) en hardverwijderd (ext:articleNumber, etc.).

## Frontmatter-schema (verplicht)

Elke .md-file begint met YAML-frontmatter:

```yaml
---
type: decision | sprint | h-item | concept | module | source | workflow | scope | index | log
id: D12                           # voor decisions/h-items/modules/sprints
title: Drie-laags compliance-architectuur
status: active | parked | superseded | hardverwijderd | living
date: 2026-04-22                  # datum van vaststelling of laatste wezenlijke wijziging
related:                          # wikilinks naar verwante files
  - D09_framework-neutraliteit
  - H25_compl-articleRef-domain-spanning
sources:                          # bron-context (chats, project-knowledge-files)
  - projectinstructie-v1.6
  - patch-rapport-v4_3_3
chat-sources:                     # verplicht aanwezig (mag [] zijn) — Karpathy-provenance
  - https://claude.ai/chat/<uri>
confidence: high | medium | low | skelet-only   # verplicht bij reconstructie
gaps:                                            # verplicht bij confidence low/skelet-only EN bij chat-sources: []
  - "Datum onbekend"
---

**Verplichte velden:** `type`, `title`, `status`, `date`, `chat-sources` (mag leeg zijn).
**Verplicht-bij-conditie:** `id` (voor decision/h-item/module/sprint), `confidence` (bij reconstructie), `gaps` (bij low/skelet-only of lege chat-sources), `related` (wanneer cross-references bestaan), `sources` (wanneer project-knowledge-bron beschikbaar is).
```

Frontmatter-velden zijn machine-leesbaar (YAML); de body is mens-leesbare markdown.

## Naming conventions

- D-files: `D{NN}_{slug}.md` → `D09_framework-neutraliteit.md`
- Sprint-files: `v{X}_{Y}_{Z}_{slug}.md` → `v4_3_3_d12-en-predicate-consolidatie.md` (puntjes door underscores)
- H-files: `H{NN}_{slug}.md`
- Module-files: `M{NN}_{slug}.md`
- Concept-files: `{slug}.md`
- Source-files: `{slug}.md`
- Workflow-files: `{slug}.md`
- Scope-files: `{slug}.md`

Slugs in lowercase met hyphens. Geen spaties, geen umlauten, geen apostrofs.

## Wikilink-conventie

Cross-references in body gebruik `[[file-naam-zonder-extension]]`. In Project Knowledge (Optie A) zijn dit grep-ankers voor `project_knowledge_search`; in Obsidian (Optie C) renderen ze als clickable links + graph view.

Voorbeeld: "Deze beslissing is een direct gevolg van [[brain__decisions__D09_framework-neutraliteit]] en heeft implicaties voor [[brain__architecture__H25_compl-articleRef-domain-spanning]]."

## Provenance-eisen

Elke factuele claim die niet-triviaal of betwistbaar is, krijgt een bron — primair in `sources:` of `chat-sources:` frontmatter, secundair inline. De wiki moet altijd terug-traceerbaar zijn naar het bronmateriaal.

Voor reconstructie van vroege sprints (v0.1 → v3.x) waar onzekerheid bestaat, wordt `confidence` expliciet en worden `gaps:` benoemd.

## Update-cyclus

| Wat | Wie | Wanneer |
|---|---|---|
| Nieuwe D-decision | Masterchat → schrijft .md | Direct na vaststelling in masterchat |
| Sprint-afronding | Masterchat → schrijft sprint-file + appendt `brain__log.md` | Bij elke release |
| H-item update | Masterchat → wijzigt H-file | Bij elke H-status-wijziging |
| Module-update | Masterchat → wijzigt module-file | Bij elke sprint die module raakt |
| Concept-toevoeging | Masterchat → nieuwe concept-file | Wanneer een term meer dan twee keer voorkomt zonder centrale definitie |

**Workflow Optie A (huidig):**

1. Masterchat genereert of wijzigt batch markdown-files
2. `present_files` voor download
3. Gebruiker uploadt naar Project Knowledge (oude versie verwijderen indien aanwezig)
4. Volgende chat-sessie: Masterchat verifieert via `project_knowledge_search` dat de update zichtbaar is

**Workflow Optie C (toekomst):**

1. Claude Code (lokaal) wijzigt files direct in `brain/`
2. Git commit per sprint
3. Optioneel: sync naar Project Knowledge zodat alle zes chats erbij kunnen

## Karpathy-conformiteit voor Optie C-overgang

Deze vault is van dag 1 ontworpen voor Karpathy's LLM Wiki-patroon:

- Folder-structuur (encoded in filenames) is direct compatible
- Frontmatter en wikilinks zijn standaard Obsidian-conventies
- `CLAUDE.md` (deze file) is de Karpathy-spec voor Claude Code
- Geen claude.ai-specifieke hacks die later ontmanteld moeten

Bij Optie C-overgang: filename-decode → folder-structuur (oneliner bash), aanvullende `/wiki-ingest`-, `/wiki-lint`-, `/wiki-query`-skills installeren, vault openen in Obsidian.

## Maximale grootte per file

Per Karpathy's guidance werkt een wiki onder ~500 articles prima met markdown + keyword search. Doelen per file-type:

- D-files: <300 woorden
- Sprint-files: <500 woorden
- H-files: <400 woorden
- Concept-files: <400 woorden
- Module-files: <500 woorden
- Source-files: <300 woorden

Als een file te groot wordt: splits in sub-pagina's met wikilinks.

## Versionering van deze spec

`CLAUDE.md` zelf is geen immutable file. Wijzigingen vereisen masterchat-goedkeuring; bij elke wijziging wordt `date:` en `version:` in frontmatter ge-update en een entry in `brain__log.md` geappendeerd.

— Einde CLAUDE.md
