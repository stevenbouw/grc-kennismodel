---
type: workflow
title: Zeven-chat-architectuur — rolverdeling tussen Claude-sessies
status: living
date: 2026-05-21
related:
  - masterchat-interactie
  - opleveringsprotocol
  - sprint-protocollen
sources:
  - projectinstructie-v1.9
chat-sources: []
confidence: high
---

# Zeven-chat-architectuur

> **Filename-noot:** filename behoudt `zes-chat-architectuur.md` uit eerdere iteraties (PK-conventie). Inhoud beschrijft per v4.6.0 / projectinstructie v1.9 **zeven chats** (Brein-chat toegevoegd na v4.5.0). Hernoemen zou extra upload-cyclus vereisen zonder functionele meerwaarde.

## Beslissing

Het GRC Kennismodel-project gebruikt **zeven gescheiden Claude-chats binnen één Project**, elk met een specifieke rol. Architectuur-beslissingen via Master; implementatie via specialistische chats met gestructureerde briefings.

## De zeven chats

| Chat | Rol | Doet wel | Doet niet |
|---|---|---|---|
| **Master** | Projectadviseur & GRC-architect | Strategie, sparring, architectuurbeslissingen, prioritering, GO/NO-GO | Geen Turtle/SPARQL, geen documenten, geen dashboard-code |
| **Technisch** | Ontologie-expert (OWL/SPARQL) | Turtle, SPARQL, SHACL, reasoner-validatie, diagnostiek | Geen strategie, beleid, UI-code |
| **Documentatie** | Beleidsadviseur & schrijver | PID, managementcommunicatie, beleid (NL) | Geen ontologie-code, dashboard-code |
| **Dashboard** | Full-stack developer & visualisatie | HTML/JS dashboards, D3/Chart.js, SPARQL, export-scripts | Geen ontologie-wijzigingen, beleidsdocumenten |
| **Asset** | M18-specialist | M18 TBox, mappings, SHACL (afgerond; stand-by) | Geen wijzigingen in andere modules |
| **Analyse** | Framework-analist | Externe frameworks analyseren, opties formuleren, aanbevelingen | Geen Turtle, geen architectuurbeslissingen, geen beleid |
| **Brein** ✨ *(geactiveerd na v4.5.0)* | Brain-vault-onderhoud | Aanmaken/updaten brain__*-bestanden o.b.v. patch-rapport; cross-referentie-bewaking; autonoom bepalen welke bestanden bijwerken | Geen architectuurbeslissingen, geen ontologie-wijzigingen, geen beleid, geen strategische interpretatie |

## Wat veranderde t.o.v. v1.7 (zes-chat-architectuur)

Tot v1.7 was de architectuur zes chats. **Brein-chat is geactiveerd per v1.8** als 7e chat — sprint-protocol verplicht vanaf projectinstructie v1.8: brain-vault-update na elke minor-release.

| Aspect | v1.7 (6 chats) | v1.8+ (7 chats) |
|---|---|---|
| Brain-onderhoud | Ad-hoc, geen vaste rol | Eigen chat met gestructureerde werkwijze |
| Activeringsmoment | Pas bij behoefte | Standaard na opstellen nieuwe projectinstructie-versie |
| Output | Wisselend gestructureerd | Brain-vault met cross-referentie-coherentie tussen registers |

## Werkwijze per chat-rol

### Master-chat

- **Strategisch sparren** met projecteigenaar
- **Architectuur-beslissingen** voorbereiden, opties (A/B/C) formuleren
- **GO/NO-GO** momenten begeleiden bij scope-pauzes
- **D-decisions** bewaken (immutable na vaststelling)
- **Cross-chat-coördinatie** via brain__log.md

Zie [[brain__workflow__masterchat-interactie]] voor de detail-werkwijze.

### Tech-chat

- **Pre-sprint-inventarisatie (Protocol B)** uitvoeren
- **Turtle/.ttl-bewerkingen** in modules
- **SPARQL-queries** + **SHACL-shapes** onderhouden
- **Canonical metrics** runnen per release
- **Gesplitste SHACL-validatie** uitvoeren
- **Patch-rapport** opstellen per release

### Documentatie-chat

- **PID + beleidsteksten** schrijven (Nederlands)
- **Change-rapporten** + **management-samenvattingen**
- **Projectinstructie-updates** versie-naar-versie
- **Communicatie** naar bestuur/auditafdeling

### Dashboard-chat

- **grc-explorer.html** + Cytoscape.js
- **build_grc_explorer_v2.py** export-script
- **SPARQL-query-koppeling** voor dataextractie

### Asset-chat (stand-by)

**Afgerond sinds M18-oplevering** (v4.2.0). Wordt alleen actief bij M18-specifieke wijzigingen.

### Analyse-chat (incidenteel)

Per opdracht inzetbaar voor:
- Framework lezen en analyseren (PDF, web-bron)
- Opties formuleren voor scope-opname (A/B/C)
- SKOS-mapping-kandidaten identificeren
- Aanbeveling formuleren met onderbouwing

Per opdracht briefing aan master-chat. NIET zelf architectuur-beslissingen nemen.

### Brein-chat (verplicht na elke minor-release)

**Input:** patch-rapport van afgesloten sprint + nieuwe projectinstructie-versie.

**Werkwijze:** autonoom op basis van patch-rapport bepalen welke brain-bestanden aangemaakt/bijgewerkt moeten worden. Iteratie-werk in 1-2 batches.

**Output:** bijgewerkte brain-vault met cross-referentie-coherentie tussen registers.

**Activeringsmoment:** na opstellen van nieuwe projectinstructie-versie (standaard). Uitzonderingen mogelijk (bv. tussentijdse correctie).

## Coördinatie tussen chats

**Architectuurbeslissingen** gaan via Master-chat. **Implementatie** via specialistische chats. Geen directe communicatie tussen specialistische chats — alles loopt via Master of via de brain-vault als shared state.

### Shared state mechanismen

| Mechanisme | Functie |
|---|---|
| `brain__log.md` | Chronologische timeline — elke chat leest dit bij sessie-start |
| Per-folder registers (D, sprint, H, module, concept, source, workflow) | Huidige staat per domein |
| Project Knowledge | Patch-rapporten + projectinstructie + bron-PDFs |

## Post-migratie-perspectief

**Tech, Brein en Dashboard migreren** na huidige fase naar Claude Code + GitHub repo (zie `migratie-roadmap.md` in PK). Master, Documentatie, Analyse en Asset blijven claude.ai.

**Werkproces post-migratie:**

```
1. Masterchat (claude.ai) schrijft sprint-instructie
2. Push naar GitHub repo
3. Tech-subagent (Claude Code) voert uit
4. Push patch-rapport naar GitHub
5. Masterchat (claude.ai) review (via GitHub PK-connector)
6. Brein-subagent (Claude Code) doet brain-update
7. Push naar GitHub
8. PK auto-sync of handmatige sync
```

Steven (projecteigenaar) is tussenmens bij scope-pauzes Claude Code → claude.ai.

## Cross-references

- [[brain__workflow__masterchat-interactie]] — master-chat detail-werkwijze
- [[brain__workflow__opleveringsprotocol]] — sprint-afsluiting + brain-update
- [[brain__workflow__sprint-protocollen]] — protocol-discipline per chat
- [[brain__workflow__scope-discipline]] — generieke werkwijze bij scope-afwijking
- [[brain__workflow__workflow-register]] — workflow-overzicht

— Einde zeven-chat-architectuur.
