---
type: log
title: GRC Kennismodel Brain — Chronologisch logboek
status: living
date: 2026-05-26
---

# GRC Kennismodel Brain — Chronologisch logboek

Per Karpathy's pattern: chronologisch operationeel record. Append-only. **Nieuwste entry bovenaan.**

---

## 2026-05-26 — Iteratie 12: post-v4.6.0 polish-mini-sprint (H36–H40 + pre-push-protocol + productlijn-concept)

**Eerste post-migratie Brein-cyclus** uitgevoerd via brein-subagent in Claude Code (Anthropic). Polish-mini-sprint na v4.6.0 + Fase 0 GitHub-MCP-setup leverden vijf H-kandidaten en twee structurele documentatie-acties op die administratieve schuld waren geworden. Deze iteratie klaart het bord vóór de eerste post-migratie-test-sprint (T1).

**Karakter:** uitsluitend administratieve verwerking van besluiten die elders al waren genomen (masterchat + handovers). Geen architectuur-wijzigingen, geen ontologie-impact, geen D-decision-mutaties. 11 bestanden geraakt: 6 nieuw + 5 update.

**WP1 — vijf H-items registreren (H36–H40):**

- [[brain__architecture__H36_skos-exactmatch-ctrl-compl-audit]] *(nieuw)* — 28 ctrl→compl `skos:exactMatch`-pairs, audit-vraag voor SKOS-kwaliteitsanalyse-sprint of externe audit. Status: parked. Trigger: SKOS-kwaliteitsanalyse-sprint. Bron: sessie-rapport v2.0 §9.1.
- [[brain__architecture__H37_open-ontologies-mcp]] *(nieuw)* — open-ontologies MCP-server (Rust + Oxigraph + tableaux) als toolchain-alternatief voor rdflib + owlrl + pySHACL. Status: parked. Trigger: aangetoonde OWL RL-limitatie of >50.000 triples (huidig 44.907). Bron: sessie-rapport v1.0.
- [[brain__architecture__H38_owlrl-vs-hermit-equivalentie]] *(nieuw)* — geen HermiT-run sinds v4.0.0 op modulaire baseline; OWL RL ≡ HermiT-aanname niet aantoonbaar. Raakt D1, wijzigt D1 niet. Status: parked. Trigger: >10% triple-toename of nieuwe module of DL-conformance-twijfel. Bron: Fase 0 Tech-handover-rapport.
- [[brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing]] *(nieuw)* — 290 SHACL RUN 2 false-positives nog niet individueel uitgesplitst; masking-risico bij shape-wijziging. Status: parked. Trigger: rustige sprint als sanity-check of sprint die SHACL-shapes wijzigt. Bron: Fase 0 Tech-handover-rapport.
- [[brain__architecture__H40_dashboard-ui-renderdekking]] *(nieuw)* — grc-explorer-UI rendert <10% van JSON-export-velden; rdfs:comment + SourceAttribution + classificatie-attributen onzichtbaar. Status: parked. Trigger: UI-moderniseringssprint post-Fase 4. Scope: uitsluitend Spoor A explorer (zie WP3). Bron: Fase 0 Dashboard-handover-rapport.
- [[brain__architecture__H-register]] *(update)* — vijf nieuwe rijen onder Parked-categorie; nieuwe sectie "Nieuw geregistreerd in iteratie 12"; H-items-per-D-decision-tabel uitgebreid met toolchain-cluster (H37, H38), validatie-cluster (H39), dashboard-cluster (H40), D4 (H36), D1 (H38 — geen D1-wijziging).

**WP2 — pre-push disclosure-check als werkflow-regel:**

- `docs/sprint-protocols.md` *(update)* — Protocol 14 toegevoegd tussen Protocol 13 (Bron-typo-beleid) en GR (Property-semantiek-discipline). Aanleiding: PAT-blunder voorgaande sessie + handovers ongetoetst gepusht in Fase 0. Reikwijdte: alle subagents + Steven, vóór elke push van documenten met chat-historie of subagent-output. Niet retroactief. Versie 1.0 → 1.1.
- [[brain__workflow__opleveringsprotocol]] *(update)* — korte verwijzing naar Protocol 14 toegevoegd vóór Cross-references-sectie + wikilink naar sprint-protocollen.

**WP3 — productlijn-scheiding documenteren (Optie C):**

- [[brain__concepts__dashboard-productlijnen]] *(nieuw)* — `grc-explorer-*` (Spoor A — ontologie-graaf-verkenner, Cytoscape, beweegt mee met ontologie-versie) versus `grc-dashboard-*` (Spoor B — operationele werkmap, SQL.js + Chart.js, eigen versie-track). Discipline-paragraaf "niet vermengen". Cross-references naar [[brain__architecture__H40_dashboard-ui-renderdekking]], [[brain__concepts__skos-export-filter]], [[brain__concepts__namedindividual-telmethode]]. **Open punt**: locatie Spoor B-prototype in repo (Optie A eigen repo / B sources/spoor-b/ / C dashboard/spoor-b/) — wacht op masterchat-beslissing, Brein-subagent neemt geen eigen voorkeur in.
- [[brain__concepts__concept-register]] *(update)* — nieuwe rij in snelle navigatie + nieuwe cluster "Product-scope-discipline" + D-cross-reference-tabel + sprint-cross-reference-tabel.
- `CLAUDE.md` *(update)* — nieuwe korte sectie "Dashboard-productlijnen (Spoor A vs Spoor B)" tussen repo-structuur en brain-vault-organisatie (4-6 regels). Verwijst naar concept-bestand voor detail. Versie 1.3 → 1.4.

**WP4 — register-coherentie + log-iteratie 12:**

- [[brain__log]] *(deze entry)* — nieuwste entry bovenaan, iteratie 12.
- [[brain__index]] *(update)* — vault-staat-tabel rij iteratie 12 + totaal brain-bestanden bijgewerkt + "Volgende fase"-sectie heroverwogen (Brein-cyclus-pre-conditie nu voldaan; klaar voor T1-test-sprint).

**File-count iteratie 12:**

| WP | Nieuw | Update | Totaal |
|---|---:|---:|---:|
| WP1 H-items | 5 | 1 (H-register) | 6 |
| WP2 pre-push | 0 | 2 (sprint-protocols.md + opleveringsprotocol) | 2 |
| WP3 productlijn | 1 | 2 (concept-register + CLAUDE.md) | 3 |
| WP4 log + index | 0 | 2 (log + index) | 2 |
| **Totaal** | **6** | **7** | **13** |

**Cross-referentie-verificatie:**

- Alle vijf H-bestanden hebben `related:`-frontmatter die naar bestaande bestanden wijst (H36 → D4, skos-export-filter, sameAs-discipline; H37 → owl-rl-reasoning, canonical-metrics; H38 → D01, owl-rl-reasoning, H37; H39 → gesplitste-shacl-validatie, sameAs-discipline; H40 → skos-export-filter, namedindividual-telmethode, dashboard-productlijnen).
- H40 verwijst naar `dashboard-productlijnen` — concept bestaat (geen forward-reference-rot).
- `dashboard-productlijnen` verwijst naar H40 — H40 bestaat (geen forward-reference-rot).
- Concept-register heeft drie nieuwe consistent-bijgewerkte tabellen (snelle navigatie + clusters + D-cross-references + sprint-cross-references).
- H-register heeft H36-H40 in zowel Parked-status-tabel als nieuwe "iteratie 12"-sectie als per-D-decision-tabel.
- `CLAUDE.md` §Dashboard-productlijnen verwijst naar `brain/brain__concepts__dashboard-productlijnen.md` (bestaat).
- `docs/sprint-protocols.md` Protocol 14 is benoemd in overzichts-tabel (#14) én uitgewerkt in eigen sectie én vermeld in wijzigingsgeschiedenis (v1.0 → v1.1).

**Belangrijkste open punten voor masterchat:**

1. **Locatie Spoor B-prototype in repo** (WP3 — A/B/C-keuze, niet door Brein gedaan)
2. **Eventuele restpunten** uit sessie-rapport v2.0 die niet in deze cyclus zijn meegenomen — Brein heeft strikt de briefing gevolgd; aanvullende WP's zijn aan masterchat

**Karakter-bevestiging:** geen architectuurbeslissingen genomen; geen ontologie-impact; geen D-mutaties; geen ramp om scope. Discipline-conform.

**Pre-push disclosure-check** (Protocol 14, vandaag vastgelegd in WP2) is **op deze iteratie zelf toegepast**: log-entry, index-update, H-bestanden, concept-bestand, CLAUDE.md-sectie — geen organisatie-naam, geen persoonsnamen anders dan Steven, geen credentials, geen lokale paden.

**Volgende:** Steven inspecteert WP1-WP4 en commit handmatig (per WP of cumulatief — Brein-voorstel staat in eindrapport-output). Daarna eerste post-migratie-test-sprint (T1) kan aanvangen.

---

## 2026-05-21 — Iteratie 11b: v4.6.0-update detail (modules, sources, workflow)

**Tweede batch van iteratie 11** — vervolg op 11a (kern). 10 bestanden opgeleverd: 0 nieuw + 10 vervangen. Iteratie 11 nu volledig afgerond. Brain klaar voor migratie naar Claude Code + GitHub.

**Module-updates (5):**

- [[brain__modules__M01_framework]] — `fw:ENSIA` gepromoot van fw:Guideline → fw:GRCFramework (verplaatst uit m15) + `ext:Attr_ENSIA_Logius_2024` SourceAttribution. Vier-cluster D9-bewijs in M01 zichtbaar (NIS2/CBW + CBW/Cbb + NIST CSF + ENSIA-toetst-BIO)
- [[brain__modules__M06_isms]] — Volwassenheidsmodel-cluster: 5 isms-klassen + 3 OP + 5 Levels (NBA-LIO/NOREA-schaal) + 32 Capabilities (23 Cbw + 9 ISMS) + 160 LevelDescriptions + `ext:Attr_NBA_LIO_NOREA` SourceAttribution (SHA256). Triple-impact-decompositie (5+8 per element ipv 4+6 — rdf:type-dubbele-telling)
- [[brain__modules__M07_business]] — biz:MaturityAssessment-cluster ONGEWIJZIGD. Sectie "Parallelle clusters — niet samenvoegen" + V1-keuze-onderbouwing met vier conflict-redenen + SPARQL-aandachtspunt met namespace-onderscheid
- [[brain__modules__M15_ensia]] — Promotie uit stub. Hybride locatie A3+B3+C2 uitgelegd. Behoud NB-comment + 8 ext:hasAuditDomain + 2 skos:relatedMatch in M15. Issuers BZK/NOREA/VNG bevestigd; fw:Logius NIET als issuer (property-semantiek-discipline)
- [[brain__modules__M21_nist-csf-2-0-planned]] — Tiers-cluster v4.6.0: csf:CSFTier-klasse + 2 DP + 4 Tier-individuals + 4 SKOS Tier↔Level. EERSTE concrete D6-symmetrische toepassing v1.9 (riskGovernance/Management-Description @en-only). Naam-discipline CSFTier vs risk:RiskManagementTier

**Source-updates (2):**

- [[brain__sources__cbw-excel]] — Sheet 6 verwerking (1.440 triples, 32 Capabilities + 160 LevelDescriptions, +44% boven raming verklaarbaar). Eigen SourceAttribution voor Sheet 6 (NBA-LIO/NOREA-volwassenheidsmodel) náást de bestaande voor Sheet 3/8/9 (ADR/NOREA). 4 typo-correcties Cbw_05/11/12/14. ADR/NOREA bron-kwaliteits-patroon cumulatief over drie sprints
- [[brain__sources__source-register]] — 5 SourceAttribution-individuals tabel (2 nieuw v4.6.0: NBA-LIO-NOREA + ENSIA-Logius). Bronnen-overzicht per sprint. Twee nieuwe licentie-categorieën in tabellen: "Vrij gebruik met bronvermelding" (ENSIA-handreiking) + "CC-BY 4.0 via Sheet 6"

**Workflow-updates (2):**

- [[brain__workflow__sprint-protocollen]] — Cumulatieve tabel van 12 protocollen + 1 gedragsregel. Vier NIEUWE protocollen v1.9 (Protocol B-multi-module-discipline, Ramings-baseline rdf:type-dubbele-telling, Instructie-consistentie code-block vs toelichting, Bron-typo-beleid patroon-criterium). Eén nieuwe gedragsregel (Property-semantiek-discipline)
- [[brain__workflow__zes-chat-architectuur]] — Update naar 7-chat-architectuur (Brein-chat geactiveerd na v4.5.0). Filename behouden (`zes-chat-architectuur.md`), inhoud beschrijft 7 chats. Post-migratie-perspectief uitgewerkt (Tech/Brein/Dashboard naar Claude Code + GitHub; Master/Documentatie/Analyse/Asset blijven claude.ai)

**Log (1):**

- [[brain__log]] (deze) — iteratie 11b entry

**Karakter:**

Iteratie 11b is **detail-update** — alle module-specifieke, source-specifieke en workflow-specifieke wijzigingen die uit v4.6.0 + projectinstructie v1.9 volgen.

**Belangrijkste verfijningen uit v4.6.0 + v1.9:**

1. D9 vierde verificatie-cluster ENSIA-detail in M01 en M15 zichtbaar
2. Volwassenheidsmodel-cluster volledig gedocumenteerd in M06 + parallel-onderhoud van M07
3. CSF Tiers met D6-symmetrische toepassing (eerste concrete @en-only normatieve descriptions)
4. Vier nieuwe sprint-protocollen formeel met v4.6.0-toepassings-bewijs
5. 7-chat-architectuur met expliciete Brein-chat-rol en post-migratie-perspectief
6. Cumulatief ADR/NOREA bron-kwaliteits-patroon over drie sprints zichtbaar in source-register

**Brain-staat na iteratie 11 (compleet):**

| Folder | Files | Wijziging in iteratie 11 |
|---|---:|---|
| Root | 7 | log + index vervangen |
| decisions/ | 13 | D6 + D9 vervangen + register vervangen |
| sprints/ | 14 | +v4.6.0 nieuw + register vervangen |
| architecture/ | 12 | onveranderd (geen nieuwe H-items v4.6.0) |
| concepts/ | 13 | +parallelle-maturity-clusters nieuw + register vervangen |
| modules/ | 19 | M01/M06/M07/M15/M21 vervangen + register vervangen |
| sources/ | 8 | cbw-excel + register vervangen |
| workflow/ | 6 | sprint-protocollen + zes-chat-architectuur vervangen |
| scope/ | 5 | onveranderd |
| **Totaal** | **~100** | **20 wijzigingen** (2 nieuw + 18 vervangen) |

**Volgende:** vault-zip v4.6.0 wordt na deze iteratie aangeleverd voor migratie naar Claude Code + GitHub. Brain is volledig consistent met v4.6.0-baseline + projectinstructie v1.9 én klaar voor productie-test in eerste post-migratie-sprint (v4.7.0).

**Belangrijk:** iteratie 11 is **de laatste iteratie in claude.ai PK voor de Brein-chat**. Vanaf v4.7.0 (post-migratie) wordt brain-onderhoud uitgevoerd via de brein-subagent in Claude Code, met git als audit trail.

---

## 2026-05-21 — Iteratie 11a: v4.6.0 + v1.9-update kern

**Eerste batch van iteratie 11** — verwerking van v4.6.0 Fase 4 (M15-ENSIA + Volwassenheidsmodel) + projectinstructie v1.9 in de brain. 10 bestanden opgeleverd (2 nieuw + 8 vervangen). Batch 11b volgt na verificatie.

**Aanleiding:** v4.6.0 Fase 4 opgeleverd 21 mei 2026 — laatste geplande Spoor A-sprint vóór migratie naar Claude Code + GitHub. Schaal-multiplier 2,7× v4.4.0 (onder oorspronkelijke prognose dankzij hergebruik bestaande m15-structuur). +1.610 triples, +204 individuals, 5 modules gewijzigd.

**Nieuwe (2):** sprint v4.6.0, parallelle-maturity-clusters concept. **Vervangen (8):** D6, D9, D-register, sprint-register, module-register, concept-register, index, log iteratie 11a.

---

## 2026-05-19 — Iteratie 10b: v4.5.0-update detail (modules, sources, concepts, nieuw cross-bron-overlap)

Tweede batch van iteratie 10 — vervolg op 10a. 14 bestanden: 1 nieuw (cross-bron-overlap) + 13 vervangen.

---

## 2026-05-19 — Iteratie 10a: v4.5.0-update kern (sprint v4.5.0 + 3 H-items + D3-uitbreiding)

11 bestanden (5 nieuw + 6 vervangen). Nieuwe: sprint v4.5.0, H33, H34, H35.

---

## 2026-05-13 — Iteratie 9b: v1.7-update detail

Tweede batch iteratie 9. 10 bestanden (1 nieuw + 9 vervangen).

---

## 2026-05-13 — Iteratie 9a: v1.7-update kern (sprint v4.4.0 + D-updates + H32)

11 bestanden (2 nieuw + 9 vervangen).

---

## 2026-05-13 — Iteratie 8: Migratie-prep + future-concepts

7 bestanden.

---

## 2026-05-13 — Iteratie 7: Index-update + smoke-tests

3 bestanden.

---

## 2026-05-13 — Iteratie 6: Sources + Workflow + Scope

19 bestanden in drie folders.

---

## 2026-05-13 — Iteratie 5: Modules

20 nieuwe bestanden M01-M18 + M21-stub + register.

---

## 2026-05-13 — Iteratie 4: Concepts

10 bestanden: 9 concepts + register.

---

## 2026-05-13 — Iteratie 3: H-items + D-correcties

11 bestanden.

---

## 2026-05-13 — Iteratie 2: Sprint-files v0.x → v4.3.3 + register

12 bestanden.

---

## 2026-05-13 — Iteratie 1: D-decisions D1–D12 + register

12 bestanden.

---

## 2026-05-13 — Iteratie 0: vault-foundation

4 bestanden initiële opzet.

---

*(Iteratie 1.5 = archeologie-rapport, niet als log-entry maar als apart document [[brain__archeology-report]].)*
