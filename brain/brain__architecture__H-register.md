---
type: index
id: H-register
title: H-register — Architectuur-vragen (open / parked / resolved / future)
status: living
date: 2026-05-28
---

# H-register — Architectuur-vragen

H-items zijn geregistreerde architectuur-vragen, beslis-punten of onderwerpen die over de tijd evolueren. In tegenstelling tot D-decisions (immutable) hebben H-items een **levende status** die per sprint kan verschuiven.

## Status-overzicht

| Categorie | Aantal | H-items |
|---|---:|---|
| Open | 6 | H25, H26, H27, H33, H34, H35 |
| Active (gedeeltelijk closed) | 0 | — *(H36 fully closed iteratie 15)* |
| Parked | 7 | H15, H21, H37, H38, H39, H40, H41 |
| Future-consideration | 3 | H29, H30, H31 |
| Newly registered v4.4.0 | 1 | H32 |
| Resolved | 5 | H9, H10, H18, H22, **H36** *(iteratie 15 — fully closed via T1+T2+T3)* |
| Unknown / not yet documented | 3 | H16, H17, H23 |

**Totaal**: 6 open + 0 active-partial + 7 parked + 3 future + 1 v4.4.0-asymmetrie + 5 resolved (genoemd) + 3 unknown.

**Iteratie 15-mutatie:** H36 verschoof van "active (m10 closed, m14 open subtask)" (iteratie 14) naar **fully closed** (resolved) omdat T3-sprint de m14-subtask volledig afhandelde (31 compl→ctrl-paren in `m14-avg-gdpr.ttl`, 2 mutaties via masterchat-besluit Optie C op pilot-escalatie). H36-totaal cumulatief 149 ctrl:↔compl:-paren over T1+T2+T3. H39 versterkt: SHACL-blinde-vlek nu bidirectional vastgesteld (eerder ctrl→compl in T1+T2; nu ook compl→ctrl in T3). H41 informatief uitgebreid met T3-bevestiging (status ongewijzigd; eerste cross-category-context-bewijs).

**Iteratie 14-mutatie (historie):** H36 verschoof van "closed" (iteratie 13) terug naar "active (m10 closed, m14 open subtask)" omdat T2-sprint de scope verbreedde van 28 exactMatch-paren naar volledig m10-cluster (118 paren). T2 voltooide m10; m14-subtask (31 compl→ctrl-paren) is op masterchat-besluit afgesplitst naar toekomstige T-sprint. Tegelijkertijd is H41 nieuw geregistreerd (parked) op basis van T2-empirisch bewijs voor SKOS-axioma-set-handling onder OWL-RL.

## Open items — vereisen GRC-inhoudelijke analyse of trigger-criterium

| H | Onderwerp | Aandachts-update v4.6.0 / iteratie 12 |
|---|---|---|
| H25 | `compl:articleRef`-domain-spanning over D12-lagen | Onveranderd |
| H26 | OBL-laag gap voor NIS2 art. 18, 19, 22, 24 | Onveranderd |
| H27 | Voorwaardelijke γ-migratie `compl:articleRef` → `compl:articleIdentifier` | Onveranderd |
| H32 | OBL-laag modelleringsasymmetrie (3 OBL_NIS2 vs 35 overige LegalObligations) | Onveranderd |
| H33 | m11 substantiële uitbreiding SP 800-53 (124/~1000 in model) | Onveranderd — Trigger: Spoor B >50 niet-gemapte controls |
| H34 | m11 enhancement-modellering (17 unique enhancements in Stap 6) | Onveranderd — Trigger: SP 800-53-gebruik met enhancement-audit |
| H35 | Cbb 5.28-typo-interpretatie (sheet 8 UV 10.4) | Onveranderd — Confidence: medium; Trigger: bron-correctie of latere sprint |

## Active (gedeeltelijk closed)

*(Geen items in deze categorie sinds iteratie 15 — H36 verschoof naar resolved)*

## Parked items

| H | Onderwerp | Detail |
|---|---|---|
| H15 | Governance-graafdekking (Route P/Q/R) | [[brain__architecture__H15_governance-graafdekking]] |
| H21 | 421 implicit individuals (consistentie-keuze) | [[brain__architecture__H21_implicit-individuals]] |
| H37 *(iteratie 12)* | open-ontologies MCP-server als rdflib-alternatief | [[brain__architecture__H37_open-ontologies-mcp]] |
| H38 *(iteratie 12)* | OWL RL vs HermiT equivalentie niet geverifieerd sinds v4.0.0 | [[brain__architecture__H38_owlrl-vs-hermit-equivalentie]] |
| **H39** *(iteratie 12, versterkt iteratie 13+14+15)* | **290 SHACL RUN 2 false-positives niet individueel uitgesplitst — T1+T2+T3 bevestigen blinde vlek op ctrl:↔compl: bidirectional (28 + 118 + 31 paren)** | [[brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing]] |
| H40 *(iteratie 12)* | Dashboard-explorer-UI rendert <10% van JSON-velden | [[brain__architecture__H40_dashboard-ui-renderdekking]] |
| **H41** *(iteratie 14, T3-bevestiging iteratie 15 informatief)* | **SKOS-axioma-set-handling onder OWL-RL — skos:S46 + S47 niet geladen; T2 + T3 leveren productie-schaal empirisch bewijs (Δ post-OWL-RL = 0 op 65 + 2 SKOS-mutaties; T3 is eerste cross-category-bewijs)** | [[brain__architecture__H41_skos-axioma-set-handling]] |

## Future-consideration

Vereisen Analyse-opdracht 2.0 vóór formele scope-opname:

| H | Onderwerp | Detail |
|---|---|---|
| H29 | Three Lines Model (IIA 2020) als M04-uitbreiding | [[brain__architecture__H29_three-lines-model]] |
| H30 | GITC (General IT Controls) als Laag 5-auditkader | [[brain__architecture__H30_gitc-auditkader]] |
| H31 | Toetsingskader Algoritmes (AR) als Laag 5-auditkader | [[brain__architecture__H31_toetsingskader-algoritmes]] |

## Nieuw geregistreerd v4.4.0 (onveranderd)

| H | Onderwerp | Detail |
|---|---|---|
| H32 | OBL-laag modelleringsasymmetrie (3 OBL_NIS2 vs 35 overige LegalObligations) | [[brain__architecture__H32_obl-laag-asymmetrie]] |

## Nieuw geregistreerd in iteratie 10 (v4.5.0)

| H | Onderwerp | Detail |
|---|---|---|
| H33 | m11 substantiële uitbreiding SP 800-53 (breedte) | [[brain__architecture__H33_m11-sp800-53-substantiele-uitbreiding]] |
| H34 | m11 enhancement-modellering (diepte) | [[brain__architecture__H34_m11-enhancement-modellering]] |
| H35 | Cbb 5.28-typo-interpretatie (sheet 8 UV 10.4) | [[brain__architecture__H35_cbb-528-typo-interpretatie]] |

## Nieuw geregistreerd in iteratie 12 (post-v4.6.0 polish-mini-sprint) ✨

| H | Onderwerp | Detail |
|---|---|---|
| H36 *(closed iteratie 13)* | 28 ctrl→compl exactMatch-pairs audit — afgehandeld via T1 | [[brain__architecture__H36_skos-exactmatch-ctrl-compl-audit]] |
| **H37** | **open-ontologies MCP-server als rdflib-alternatief** | [[brain__architecture__H37_open-ontologies-mcp]] |
| **H38** | **OWL RL vs HermiT equivalentie niet geverifieerd sinds v4.0.0** | [[brain__architecture__H38_owlrl-vs-hermit-equivalentie]] |
| **H39** *(versterkt iteratie 13)* | **290 SHACL RUN 2 false-positives niet individueel uitgesplitst** | [[brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing]] |
| **H40** | **Dashboard-explorer-UI rendert <10% van JSON-velden** | [[brain__architecture__H40_dashboard-ui-renderdekking]] |

Vijf items komen voort uit het sessie-rapport v2.0 (H36) plus de twee Fase 0 handover-rapporten van mei 2026 (H38, H39 uit Tech-handover; H40 uit Dashboard-handover) en sessie-rapport v1.0 (H37, skills/plugins-roadmap). H36 is afgehandeld in T1 (iteratie 13); H39 versterkt door T1-pre-sprint-inventarisatie Vraag D.

## Status-mutaties in iteratie 13 (post-T1) ✨

| H | Mutatie | Bron |
|---|---|---|
| **H36** | parked → **closed** — 28× exactMatch → broadMatch via patch v4.6.1; methode-protocol v1.0 vastgesteld | [[brain__sprints__T1_skos-kwaliteitsanalyse-fase-1]] |
| **H39** | parked (versterkt) — T1-Vraag D bevestigt SHACL-blinde vlek op ctrl:↔compl:-paren | T1-pre-sprint-inventarisatie + [[brain__sprints__T1_skos-kwaliteitsanalyse-fase-1]] |

**Kandidaat-H41 NIET geregistreerd (iteratie 13):** SKOS-axioma-set / `skos:S46` symmetrie-afwezigheid (owlrl-package laadt geen SKOS-axiomas). Status: T1-werkflow-leerpunt. Trigger voor latere herregistratie: overstap-besluit owlrl-incl-SKOS-axioma-reasoning.

## Status-mutaties in iteratie 14 (post-T2) ✨

| H | Mutatie | Bron |
|---|---|---|
| H36 | closed → active (m10 closed, m14 open subtask) — T2 voltooide m10-scope volledig (cumulatief 93 m10-paren via T1+T2); m14 (31 compl→ctrl-paren) blijft open subtask voor toekomstige T-sprint | [[brain__sprints__T2-skos-bidirectional-audit-m10]] |
| H39 | parked (versterkt T2) — T2 bevestigt SHACL-blinde-vlek op 118-paren-schaal (per patch-rapport v4.6.2 §7.3). Δ SHACL = 0 in alle drie metingen | [[brain__sprints__T2-skos-bidirectional-audit-m10]] + patch-rapport v4.6.2 |
| H41 *(nieuw)* | parked — SKOS-axioma-set-handling onder OWL-RL formeel geregistreerd. T1-kandidaat-overweging wordt geactiveerde H-item door T2-empirisch bewijs (Δ post-OWL-RL = 0 op 65 SKOS-mutaties) + masterchat-besluit per projectinstructie v1.10 | [[brain__sprints__T2-skos-bidirectional-audit-m10]] + projectinstructie v1.10 |

**Reikwijdte-vermelding (iteratie 14):** H36-status-revisie (closed → active) reflecteert dat T1-sprint slechts één deelscope van H36 afhandelde (28 exactMatch-paren). T2 maakte expliciet dat H36 als geheel breder is dan oorspronkelijk geregistreerd; m14-subtask geeft H-item een levende status totdat AVG-cross-walk-sprint H36 volledig sluit.

## Status-mutaties in iteratie 15 (post-T3) ✨

| H | Mutatie | Bron |
|---|---|---|
| **H36** | active (m10 closed, m14 open subtask) → **fully closed (resolved)** — T3 voltooide m14-scope (31 compl→ctrl-paren in `m14-avg-gdpr.ttl`, 2 mutaties broadMatch → relatedMatch via masterchat-besluit Optie C; 27 behoud relatedMatch + 2 behoud closeMatch op retrieval-interchangeability). H36 als geheel afgesloten; cumulatief 149 ctrl:↔compl:-paren over T1+T2+T3. Cross-category-rationale als T3-leerpunt + kandidaat v1.3.1-precedent gedocumenteerd | [[brain__sprints__T3-skos-bidirectional-audit-m14]] + patch-rapport v4.6.3 |
| **H39** | parked (versterkt T3 — bidirectional vastgesteld) — T3 bevestigt SHACL-blinde-vlek op compl→ctrl-richting (m14, 31 paren). 2 SKOS-predicate-mutaties → Δ SHACL = 0. Blinde-vlek nu bidirectional vastgesteld over T1+T2+T3 | [[brain__sprints__T3-skos-bidirectional-audit-m14]] + patch-rapport v4.6.3 |
| **H41** | parked (T3-bevestiging informatief) — derde sprint-bewijs op cross-category-context; eerste cross-category-bewijs voor H41. Δ post-OWL-RL = 0 bevestigd over drie sprint-contexten (exactMatch-omzetting T1, close/related/broad bidirectional T2, broad/related cross-category T3). Status ongewijzigd | [[brain__sprints__T3-skos-bidirectional-audit-m14]] + patch-rapport v4.6.3 |

**Reikwijdte-vermelding (iteratie 15):** H36-status-revisie (active → fully closed) reflecteert dat T3 de m14-subtask volledig afhandelde en daarmee de H36-totaal-scope (ctrl:↔compl:-mappings audit over m10 + m14) is afgesloten. Eventuele andere ctrl:↔compl:-mapping-clusters (m11, m09 etc.) zijn buiten H36-scope geregistreerd en kandidaat voor eigen H-items bij toekomstige relevant-wording.

## Spoor B automatisch geparkeerd

ABox-lege schalen wachten op organisatie-data:

| H | Domein |
|---|---|
| H11 | risk: namespace ABox |
| H12 | roles: namespace ABox |
| H13 | isms: namespace ABox |
| H19 | asset: namespace ABox |
| H20 | aanvullende asset-instanties |
| H14 | 3 sample-controls zonder compl:satisfiedBy |

## Resolved items (gemarkeerd, niet apart uitgewerkt)

| H | Onderwerp |
|---|---|
| H9 | resolved tijdens monolithisch v3.0 |
| H10 | resolved tijdens v4.0.0 modulaire split |
| H18 | IRI-afwijking + nieuwe klasse — scope-completion v4.3.1 |
| H22 | gerelateerd aan v4.3.1 patch-bump |
| **H36** *(iteratie 15)* | **ctrl:↔compl: SKOS-mappings audit fully closed via T1+T2+T3 (cumulatief 149 paren over m10 + m14; 95 mutaties). Zie [[brain__architecture__H36_skos-exactmatch-ctrl-compl-audit]]** |

**H36 status-correctie iteratie 14 (historie):** H36 was in iteratie 13 als resolved opgenomen; iteratie 14 verschoof terug naar "active (m10 closed, m14 open subtask)" omdat T2 scope-breedte zichtbaar maakte (m14-component nog niet behandeld).

**H36 status-correctie iteratie 15:** T3-sprint sluit m14-subtask volledig af; H36 nu definitief resolved. Cross-category-rationale als T3-leerpunt + kandidaat v1.3.1-precedent gedocumenteerd in concept-bestand (formalisering = masterchat-werk).

## Unknown

| H | Status |
|---|---|
| H16, H17, H23 | Vermelden in andere context maar geen aparte file |

## H-items per D-decision / cluster

| D / cluster | H-items |
|---|---|
| D1 | **H38** *(reasoner-keuze binnen D1, geen D1-wijziging)* |
| D4 | **H36** *(fully closed via T1+T2+T3 iteratie 15)*, **H41** *(SKOS-axioma-set-handling, geparkeerd iteratie 14; T3-bevestiging iteratie 15)* |
| D5 | (geen open H-items) |
| D11 | (geen open H-items) |
| D12 | H25, H26, H27, H32 |
| D9 | (architectuur-test gebruikt door H29/H30/H31 future-consideration) |
| **(M11-cluster)** | **H33, H34** *(geen directe D, maar M11-module-betrokken)* |
| **(M21-bron-cluster)** | **H35** *(bron-interpretatie, kandidaat voor latere correctie)* |
| **(toolchain-cluster)** | **H37, H38, H41** *(rdflib + reasoner-evaluatie + SKOS-axioma-set)* |
| **(validatie-cluster)** | **H39** *(SHACL false-positive-uitsplitsing, versterkt door T1+T2)* |
| **(dashboard-cluster)** | **H40** *(grc-explorer-render-dekking, Spoor A)* |

## Cross-references

- [[brain__decisions__D-register]] — D-decisions
- [[brain__sprints__sprint-register]] — sprints waarin H-items zijn ontstaan / gewijzigd
- [[brain__concepts__concept-register]] — concepts die raken aan H-items
- [[brain__concepts__dashboard-productlijnen]] — concept dat H40 scope-afbakent (Spoor A explorer vs Spoor B dashboard)
- [[brain__index]] — masterindex

— Einde H-register.
