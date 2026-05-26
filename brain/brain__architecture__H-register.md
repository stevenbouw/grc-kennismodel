---
type: index
id: H-register
title: H-register — Architectuur-vragen (open / parked / resolved / future)
status: living
date: 2026-05-19
---

# H-register — Architectuur-vragen

H-items zijn geregistreerde architectuur-vragen, beslis-punten of onderwerpen die over de tijd evolueren. In tegenstelling tot D-decisions (immutable) hebben H-items een **levende status** die per sprint kan verschuiven.

## Status-overzicht

| Categorie | Aantal | H-items |
|---|---:|---|
| Open | 6 | H25, H26, H27, **H33, H34, H35** *(nieuw v4.5.0)* |
| Parked | 2 | H15, H21 |
| Future-consideration | 3 | H29, H30, H31 |
| Newly registered v4.4.0 | 1 | H32 |
| Resolved | 4 | H9, H10, H18, H22 |
| Unknown / not yet documented | 3 | H16, H17, H23 |

**Totaal**: 9 expliciet uitgewerkte open + parked + future + asymmetrie-item + 3 nieuwe v4.5.0 + 4 resolved (genoemd) + 3 unknown.

## Open items — vereisen GRC-inhoudelijke analyse of trigger-criterium

| H | Onderwerp | Aandachts-update v4.5.0 |
|---|---|---|
| H25 | `compl:articleRef`-domain-spanning over D12-lagen | Onveranderd — alle Stap 5/6/7-mappings via skos:* zonder compl:articleRef-betrokkenheid |
| H26 | OBL-laag gap voor NIS2 art. 18, 19, 22, 24 | Onveranderd — geen GRC-inhoudelijke analyse uitgevoerd |
| H27 | Voorwaardelijke γ-migratie `compl:articleRef` → `compl:articleIdentifier` | Onveranderd — geen trigger geactiveerd |
| H32 | OBL-laag modelleringsasymmetrie (3 OBL_NIS2 vs 35 overige LegalObligations) | Onveranderd — geen Spoor B-data |
| **H33** *(v4.5.0)* | m11 substantiële uitbreiding SP 800-53 (124/~1000 in model; 108 unique unresolved Stap 6) | **Open** — Trigger: Spoor B >50 niet-gemapte controls nodig |
| **H34** *(v4.5.0)* | m11 enhancement-modellering (17 unique enhancements in Stap 6) | **Open** — Trigger: serieus SP 800-53-gebruik met enhancement-audit-behoefte |
| **H35** *(v4.5.0)* | Cbb 5.28-typo-interpretatie (sheet 8 UV 10.4 — vermoedelijk A.5.28) | **Open** — Confidence: medium; Trigger: bron-correctie of latere sprint-interpretatieve-correctie |

## Parked items

| H | Onderwerp | Detail |
|---|---|---|
| H15 | Governance-graafdekking (Route P/Q/R) | [[brain__architecture__H15_governance-graafdekking]] |
| H21 | 421 implicit individuals (consistentie-keuze) | [[brain__architecture__H21_implicit-individuals]] |

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

## Nieuw geregistreerd in iteratie 10 (v4.5.0) ✨

| H | Onderwerp | Detail |
|---|---|---|
| **H33** | **m11 substantiële uitbreiding SP 800-53** (breedte) | [[brain__architecture__H33_m11-sp800-53-substantiele-uitbreiding]] |
| **H34** | **m11 enhancement-modellering** (diepte) | [[brain__architecture__H34_m11-enhancement-modellering]] |
| **H35** | **Cbb 5.28-typo-interpretatie** (sheet 8 UV 10.4) | [[brain__architecture__H35_cbb-528-typo-interpretatie]] |

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

## H-items per D-decision

| D | H-items |
|---|---|
| D5 | (geen open H-items) |
| D11 | (geen open H-items) |
| D12 | H25, H26, H27, H32 |
| D9 | (architectuur-test gebruikt door H29/H30/H31 future-consideration) |
| **(M11-cluster)** | **H33, H34** *(geen directe D, maar M11-module-betrokken)* |
| **(M21-bron-cluster)** | **H35** *(bron-interpretatie, kandidaat voor latere correctie)* |

## Cross-references

- [[brain__decisions__D-register]] — D-decisions
- [[brain__sprints__sprint-register]] — sprints waarin H-items zijn ontstaan / gewijzigd
- [[brain__concepts__concept-register]] — concepts die raken aan H-items
- [[brain__index]] — masterindex

— Einde H-register.
