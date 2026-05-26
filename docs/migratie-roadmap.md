# MIGRATIE-ROADMAP — CLAUDE CODE + GITHUB

**Versie:** 1.2
**Datum:** 22 mei 2026
**Status:** voorbereiding (uitvoering nadert; pre-migratie-check lopend)
**Type:** Levend document — wordt bijgewerkt bij elke besluit-wijziging zonder projectinstructie te raken
**Verhouding tot projectinstructie:** dit document beschrijft uitvoerings-roadmap; projectinstructie (v1.9 actueel) beschrijft werkwijze en conventies. Conflict tussen beide: projectinstructie prevaleert.

---

## 0. Aanleiding

Sinds toevoeging van de brain-vault (begin v4.x) is token-gebruik in claude.ai substantieel gestegen. Onderzoek (Brein-chat, mei 2026): bij elke turn in elke chat doorzoekt PK de volledige content voor relevante chunks. Met ~99 brain__*.md plus 30+ bron-documenten kost dit substantieel meer dan vóór brain-introductie. De 7-chat-architectuur versterkt dit effect — dezelfde brain wordt in elke chat opgehaald.

Hybride architectuur: file-heavy chats migreren naar Claude Code; strategisch-sparrende chats blijven in claude.ai.

---

## 1. Chat-architectuur post-migratie

| Chat | Bestemming | Status besluit |
|---|---|---|
| Master | claude.ai (blijft) | Besloten |
| Tech | Claude Code | Besloten |
| Brein | Claude Code | Besloten |
| Dashboard | Claude Code | Besloten |
| Documentatie | claude.ai (blijft) | Besloten |
| Analyse | claude.ai (blijft) | Besloten |
| Asset | claude.ai (blijft, stand-by) | Besloten |

**Migratie-volgorde**: Tech → Brein → Dashboard.

---

## 2. Bron-architectuur — Optie D (besloten)

Hybride op licentie-basis:
- **In GitHub repo `sources/`**: publiek-domein bronnen (NIST, EU-recht, NL-recht, ADR/NOREA CC-BY 4.0, overheid, ENISA)
- **Blijft in claude.ai PK**: NEN-restrictief (ISO 27001/27002/27005/31000/22301/22313)
- **brain__sources__-bestanden** als parsing-leidraad per bron (path, hash, conventies, edge cases)

---

## 3. Repo-structuur (besloten)

```
grc-kennismodel/
├── brain/                ~101 brain__*.md
├── ontology/             22 .ttl-modules v4.6.0
├── sources/              publiek-domein bronnen
├── docs/
│   ├── sprint-protocols.md
│   ├── instructies/
│   ├── handovers/
│   └── migratie-roadmap.md
├── scripts/
├── output/
├── .claude/agents/       drie subagent-configs (Tech/Brein/Dashboard)
└── CLAUDE.md
```

---

## 4. Werkproces per sprint na migratie

Standaard 12-staps-flow: masterchat schrijft instructie → push GitHub → Tech-subagent voert uit → patch-rapport → masterchat review → Brein-update. Steven is tussenmens bij scope-pauzes.

---

## 5. Pre-condities voor migratie-start

| # | Pre-conditie | Verantwoordelijke | Status |
|---|---|---|---|
| 1 | Master-handover-document | Masterchat | ✓ VOLDAAN (20 mei 2026) |
| 2a | Brain-vault bijgewerkt v4.6.0+v1.9 | Brein-chat | ✓ VOLDAAN (21 mei 2026) |
| 2b | `docs/sprint-protocols.md` | Masterchat | **In aanmaak** (deliverable B na CLAUDE.md v1.2) |
| 2c | Drie subagent-configs Tech/Brein/Dashboard | Masterchat | **In aanmaak** (deliverable C na sprint-protocols.md) |
| 2d | Root CLAUDE.md correcties (v1.0 → v1.2) | Masterchat | ✓ VOLDAAN (22 mei 2026, v1.2) |
| 3 | Dashboard-inhaalslag afgerond | Dashboard-chat | ✓ VOLDAAN (21 mei 2026) |
| 4 | PAT + export-fallback geconfigureerd | Steven | OPEN |

---

## 6. Anthropic bug #33875 — mitigatie

PAT + periodieke export-fallback (besloten 20 mei 2026). Géén organization-repo voor Spoor A.

---

## 7. Architecturale risico's (besloten geaccepteerd)

1. Inter-chat-coherentie fragieler — mitigatie: GitHub als single-source-of-truth + masterchat-review-stap
2. Sprint-protocollen porteren — mitigatie: pre-conditie 2b + subagent-configs
3. Spoor B-overgang (cloud-vs-on-prem) — mitigatie: heroverwegen bij eerste Spoor B-stap

---

## 8. Timing en planning (geactualiseerd 22 mei 2026)

| Datum | Activiteit | Wie | Status |
|---|---|---|---|
| 20 mei 2026 | Migratie-roadmap v1.0 opgesteld | Masterchat | ✓ |
| 20-21 mei 2026 | Master-handover-document | Masterchat | ✓ |
| 21 mei 2026 | Dashboard-inhaalslag | Dashboard-chat | ✓ |
| 21 mei 2026 | Brein-output: brain-update + 2 CLAUDE.md | Brein-chat | ✓ |
| 22 mei 2026 | Pre-migratie-check pre-condities 2b/2c/2d | Masterchat | LOPEND |
| 22 mei 2026 | CLAUDE.md v1.2 opgeleverd | Masterchat | ✓ |
| Volgende | `docs/sprint-protocols.md` opstellen (deliverable B) | Masterchat | Pending |
| Daarna | Drie subagent-configs (deliverable C) | Masterchat | Pending |
| Bij GO check | PAT + export-fallback configureren | Steven | Open |
| Daarna | GitHub-repo aanmaken | Steven | Pending |
| Eerste week na migratie | Tech-subagent eerste test-sprint | Steven + Tech-subagent | Pending |

---

## 9. Dashboard-inhaalslag — afgerond ✓ (21 mei 2026)

**Opgeleverd**:
- `build_grc_explorer_v3.py` — 11 namespaces, csf:-cluster, maturity-cluster, attribution-edges
- `grc-data-v4_6_0.json` + `.js`
- `patchnotitie-export-v4_6_0.md` — alle 5 sprint-impacts gedocumenteerd
- `skos-kwaliteitsanalyse-v4_6_0.md` — 5 secties + 3 aandachtspunten

**SKOS-rapport-vondsten** (voor opvolging):
- A1 (→ H36 in v1.10): 28 ctrl→compl exactMatch-pairs — semantische audit
- A2: narrowMatch overwegen voor BIO→ISO 27002 — Spoor B-trigger
- A3: SPARQL-query-pattern documenteren vóór Dashboard-subagent productief

---

## 10. Open items en aandachtspunten (geactualiseerd 22 mei 2026)

| Item | Status |
|---|---|
| Subagent-config-inhoud per chat (concrete tekst) | **In aanmaak** — masterchat deliverable C |
| Scope-pauze-escalatie-protocol Claude Code → Steven → claude.ai | **Wordt onderdeel** van docs/sprint-protocols.md + subagent-configs |
| Patch-rapport-review-momentum behoud (Steven niet bottleneck) | Open — eerste post-migratie-sprint evalueren |
| Spoor B-migratie-architectuur (cloud-vs-on-prem) | TOEKOMST |
| Documentatie-chat ooit migreren? | NEE NU |
| A3 (v1.1) — SPARQL-query-pattern CSF→ISO 27002 | Open — pre-conditie Dashboard-subagent productief |
| **A4 (NIEUW v1.2)** — Tier 1 GRC-skills evalueren post-migratie | Open — zie §11 |
| **A5 (NIEUW v1.2)** — Tier 2 ontologie+wiki-skills evalueren post-migratie | Open — zie §11 |
| **A6 (NIEUW v1.2)** — H37 open-ontologies MCP formeel registreren in volgende Brein-cyclus | Open — zie §12 |

---

## 11. Externe skills/tools — post-migratie evaluatie (NIEUW v1.2)

Vier externe skills/tools geïdentificeerd voor evaluatie. **Géén pre-conditie voor migratie**. Evaluatie na eerste post-migratie-sprint (v4.7.0) wanneer stabiele werkbasis bestaat.

### Tier 1 — GRC-domein

| Bron | Use-case | Evaluatie-moment |
|---|---|---|
| [Sushegaad/Claude-Skills-GRC](https://github.com/Sushegaad/Claude-Skills-Governance-Risk-and-Compliance) | Kennis-injectie tijdens sprint-werk: ISO 27001, NIST CSF, NIS2, ISO 42001 (M19), DORA, GDPR, ISO 27701 | Bij eerste sprint die framework-skill nuttig kan maken (vroegste kandidaat: M19 ISO 42001) |
| [GRCEngClub/claude-grc-engineering](https://github.com/GRCEngClub/claude-grc-engineering) | Evidence collection, SCF crosswalks, OSCAL workflows | Bij Spoor B-overgang (lab-test T&I) |

**Caveat Tier 1**: skills zijn niet auditief geverifieerd. NEN-tekst, EU-Publications-Office, NIST.gov blijven autoritatieve bron. Skills dienen voor snelle semantische context, niet als bron-vervanger.

### Tier 2 — Ontologie + brain-vault

| Bron | Use-case | Evaluatie-moment |
|---|---|---|
| [fabio-rovai/open-ontologies (MCP)](https://github.com/fabio-rovai/open-ontologies) | Rust MCP-server met 39 tools, Oxigraph triple store, OWL2-DL tableaux reasoner, SHACL. Alternatief voor rdflib+owlrl+pySHACL | Formeel geregistreerd als H37 (zie §12) |
| [kfchou/wiki-skills](https://github.com/kfchou/wiki-skills) | Karpathy LLM Wiki pattern als Claude Code plugin: wiki-lint, wiki-audit, wiki-update | Bij eerste planbare lint-cyclus post-migratie (Karpathy-pattern Operations §Lint) |

Evaluatie-resultaat documenteren via apart rapport (Analyse-opdracht 2.0 of masterchat-besluit) met opties (vervangen / aanvullen / niet toepassen).

---

## 12. H37 — open-ontologies MCP-server (NIEUW v1.2)

**Formele registratie aankondiging.** H37 wordt opgenomen in brain-vault tijdens volgende Brein-cyclus (na v4.7.0 of bij tussentijdse Brein-activering).

| Veld | Inhoud |
|---|---|
| **H-nummer** | H37 |
| **Titel** | Open-ontologies MCP-server als alternatief voor rdflib-toolchain |
| **Status** | Open — wachtend op post-migratie evaluatie |
| **Type** | Toekomst-uitbreiding (architectuur) |
| **Datum registratie** | 22 mei 2026 (deze roadmap) |
| **Beschrijving** | Huidige Tech-toolchain: rdflib + owlrl + pySHACL (Python, OWL RL reasoner). Kandidaat-alternatief: [fabio-rovai/open-ontologies](https://github.com/fabio-rovai/open-ontologies) — Rust MCP-server met Oxigraph triple store, native OWL2-DL tableaux reasoner, SHACL, SPARQL, versioning. Single binary, geen JVM. **Sterker reasoner** (tableaux vs OWL RL) — relevant voor D11 asset-convergentie en complexere OWL 2 DL constructs. **Snellere** bij grotere graafs. **MCP-native** — directere integratie met Claude Code-subagent. |
| **Trigger voor besluit** | Eerste post-migratie-sprint waar reasoner-limitatie van OWL RL aantoonbaar knelt, óf bij ontology-groei voorbij ~50.000 pre-inf triples |
| **Risico's** | Toolchain-wijziging midden in project; verlies van bewezen rdflib-discipline; SHA256-conventies en canonical_metrics-scripts moeten aangepast |
| **Niet-blokkerend** | Huidige rdflib-toolchain werkt; geen acute knelpunten |

Volgende Brein-cyclus migreert deze H-item-stub naar volledige `brain__architecture__H37_open-ontologies-mcp.md` met frontmatter, related-links en cross-references.

---

## 13. Niet-doen-tot-GO

- GitHub-repo aanmaken vóór alle 4 pre-condities voldaan
- Claude Code-sessies in productie-context vóór pre-migratie-check positief afgerond
- Tier 1+2 skills installeren vóór eerste stabiele post-migratie-sprint
- Tech-chat of Dashboard-chat in claude.ai informeren over migratie (geen context-vervuiling)

---

## 14. Wijzigingsgeschiedenis

| Datum | Versie | Wijziging |
|---|---|---|
| 20 mei 2026 | 1.0 | Initiële versie |
| 21 mei 2026 | 1.1 | Pre-conditie 3 voldaan. Pre-conditie 2 in afronding. Nieuw open item A3 (SPARQL CSF→ISO 27002). Nieuwe §11 pre-migratie-check. |
| 22 mei 2026 | 1.2 | CLAUDE.md v1.2 opgeleverd (pre-conditie 2d). Pre-conditie 2a bevestigd voldaan na Brein-output-validatie. Pre-condities 2b/2c gesplitst en in aanmaak. Nieuwe §11 Externe skills/tools post-migratie evaluatie (Tier 1+2). Nieuwe §12 H37 formele registratie open-ontologies MCP. Nieuwe open items A4/A5/A6. Timing-tabel bijgewerkt. |

---

**Einde migratie-roadmap v1.2.**
