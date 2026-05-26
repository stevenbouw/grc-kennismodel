---
type: index
id: H-register
title: H-register — Architectuur-vragen (open / parked / resolved / future)
status: living
date: 2026-05-26
---

# H-register — Architectuur-vragen

H-items zijn geregistreerde architectuur-vragen, beslis-punten of onderwerpen die over de tijd evolueren. In tegenstelling tot D-decisions (immutable) hebben H-items een **levende status** die per sprint kan verschuiven.

## Status-overzicht

| Categorie | Aantal | H-items |
|---|---:|---|
| Open | 6 | H25, H26, H27, H33, H34, H35 |
| Parked | 7 | H15, H21, **H36, H37, H38, H39, H40** *(nieuw iteratie 12)* |
| Future-consideration | 3 | H29, H30, H31 |
| Newly registered v4.4.0 | 1 | H32 |
| Resolved | 4 | H9, H10, H18, H22 |
| Unknown / not yet documented | 3 | H16, H17, H23 |

**Totaal**: 6 open + 7 parked + 3 future + 1 v4.4.0-asymmetrie + 4 resolved (genoemd) + 3 unknown.

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

## Parked items

| H | Onderwerp | Detail |
|---|---|---|
| H15 | Governance-graafdekking (Route P/Q/R) | [[brain__architecture__H15_governance-graafdekking]] |
| H21 | 421 implicit individuals (consistentie-keuze) | [[brain__architecture__H21_implicit-individuals]] |
| **H36** *(iteratie 12)* | **28 ctrl→compl exactMatch-pairs audit (SKOS-rigour)** | [[brain__architecture__H36_skos-exactmatch-ctrl-compl-audit]] |
| **H37** *(iteratie 12)* | **open-ontologies MCP-server als rdflib-alternatief** | [[brain__architecture__H37_open-ontologies-mcp]] |
| **H38** *(iteratie 12)* | **OWL RL vs HermiT equivalentie niet geverifieerd sinds v4.0.0** | [[brain__architecture__H38_owlrl-vs-hermit-equivalentie]] |
| **H39** *(iteratie 12)* | **290 SHACL RUN 2 false-positives niet individueel uitgesplitst** | [[brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing]] |
| **H40** *(iteratie 12)* | **Dashboard-explorer-UI rendert <10% van JSON-velden** | [[brain__architecture__H40_dashboard-ui-renderdekking]] |

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
| **H36** | **28 ctrl→compl exactMatch-pairs audit** | [[brain__architecture__H36_skos-exactmatch-ctrl-compl-audit]] |
| **H37** | **open-ontologies MCP-server als rdflib-alternatief** | [[brain__architecture__H37_open-ontologies-mcp]] |
| **H38** | **OWL RL vs HermiT equivalentie niet geverifieerd sinds v4.0.0** | [[brain__architecture__H38_owlrl-vs-hermit-equivalentie]] |
| **H39** | **290 SHACL RUN 2 false-positives niet individueel uitgesplitst** | [[brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing]] |
| **H40** | **Dashboard-explorer-UI rendert <10% van JSON-velden** | [[brain__architecture__H40_dashboard-ui-renderdekking]] |

Vijf items komen voort uit het sessie-rapport v2.0 (H36) plus de twee Fase 0 handover-rapporten van mei 2026 (H38, H39 uit Tech-handover; H40 uit Dashboard-handover) en sessie-rapport v1.0 (H37, skills/plugins-roadmap). Geen architectuur-besluit gewijzigd — alleen administratieve registratie van geparkeerde vragen.

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

## Unknown

| H | Status |
|---|---|
| H16, H17, H23 | Vermelden in andere context maar geen aparte file |

## H-items per D-decision / cluster

| D / cluster | H-items |
|---|---|
| D1 | **H38** *(reasoner-keuze binnen D1, geen D1-wijziging)* |
| D4 | **H36** *(SKOS-match-type-rigour binnen D4)* |
| D5 | (geen open H-items) |
| D11 | (geen open H-items) |
| D12 | H25, H26, H27, H32 |
| D9 | (architectuur-test gebruikt door H29/H30/H31 future-consideration) |
| **(M11-cluster)** | **H33, H34** *(geen directe D, maar M11-module-betrokken)* |
| **(M21-bron-cluster)** | **H35** *(bron-interpretatie, kandidaat voor latere correctie)* |
| **(toolchain-cluster)** | **H37, H38** *(rdflib + reasoner-evaluatie-vragen)* |
| **(validatie-cluster)** | **H39** *(SHACL false-positive-uitsplitsing)* |
| **(dashboard-cluster)** | **H40** *(grc-explorer-render-dekking, Spoor A)* |

## Cross-references

- [[brain__decisions__D-register]] — D-decisions
- [[brain__sprints__sprint-register]] — sprints waarin H-items zijn ontstaan / gewijzigd
- [[brain__concepts__concept-register]] — concepts die raken aan H-items
- [[brain__concepts__dashboard-productlijnen]] — concept dat H40 scope-afbakent (Spoor A explorer vs Spoor B dashboard)
- [[brain__index]] — masterindex

— Einde H-register.
