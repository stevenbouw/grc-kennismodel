---
type: log
title: GRC Kennismodel Brain — Chronologisch logboek
status: living
date: 2026-05-21
---

# GRC Kennismodel Brain — Chronologisch logboek

Per Karpathy's pattern: chronologisch operationeel record. Append-only. **Nieuwste entry bovenaan.**

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
