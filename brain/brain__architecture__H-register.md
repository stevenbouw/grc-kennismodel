---
type: index
id: H-register
title: H-register — Architectuur-vragen (open / parked / resolved / future)
status: living
date: 2026-06-04
---

# H-register — Architectuur-vragen

H-items zijn geregistreerde architectuur-vragen, beslis-punten of onderwerpen die over de tijd evolueren. In tegenstelling tot D-decisions (immutable) hebben H-items een **levende status** die per sprint kan verschuiven.

## Status-overzicht

| Categorie | Aantal | H-items |
|---|---:|---|
| Open | 6 | H25, H26, H27, H33, H34, H35 |
| Active (gedeeltelijk closed) | 0 | — *(H36 fully closed iteratie 15)* |
| Parked | 6 | H15, H21, H37, H39, H40, H41 |
| Future-consideration | 3 | H29, H30, H31 |
| Newly registered v4.4.0 | 1 | H32 |
| Resolved | 6 | H9, H10, H18, H22, **H36** *(iteratie 15)*, **H38** *(iteratie 16 — OWL RL ≡ HermiT via v4.6.4)* |
| Unknown / not yet documented | 3 | H16, H17, H23 |
| **Kandidaat-H-items (masterchat-benoemd, niet geactiveerd)** | **3** | **H42, H43, H44** *(dashboard-landschap, besluitnotitie 29 mei — ter registratie, niet geactiveerd; zie iteratie-16-sectie)* |

**Totaal**: 6 open + 0 active-partial + 6 parked + 3 future + 1 v4.4.0-asymmetrie + 6 resolved (genoemd) + 3 unknown + 3 kandidaat (niet geactiveerd).

**Iteratie 16-mutatie (post-v4.6.4 + reasoner-evaluatie):** **H38 verschoof van parked naar resolved** — OWL RL ≡ HermiT empirisch bevestigd voor deze baseline na de v4.6.4-range-fix (volledige boog: blind spot → DL-census → HermiT-vondst datatype-range-mismatch → fix → her-verificatie consistent). H37 + H41 blijven **parked**, verrijkt met evaluatie-uitkomst (beide HOLD). Drie kandidaat-H-items (H42/H43/H44) door masterchat benoemd in de dashboard-landschap-besluitnotitie — ter registratie, niet geactiveerd. Daarnaast een csf↔ISO27001 cross-category-predicaat-vraag uit T4 als **kandidaat-precedent zonder formeel H-nummer** (zie iteratie-16-sectie).

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
| **H37** *(iteratie 12, evaluatie-uitkomst iteratie 16)* | **open-ontologies MCP-server als rdflib-alternatief — desk-evaluatie 29 mei: HOLD, geen van 4 triggers actief (44.907 < 50k; H38 resolved; pre-1.0 v0.1.11). Trigger-herijking gedocumenteerd** | [[brain__architecture__H37_open-ontologies-mcp]] |
| **H39** *(iteratie 12, versterkt iteratie 13+14+15)* | **290 SHACL RUN 2 false-positives niet individueel uitgesplitst — T1+T2+T3 bevestigen blinde vlek op ctrl:↔compl: bidirectional (28 + 118 + 31 paren)** | [[brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing]] |
| H40 *(iteratie 12, lege-huls-aangrenzing iteratie 17)* | Dashboard-explorer-UI rendert <10% van JSON-velden — Q-M4: latent/parked (demo-waarde uit dashboard, niet explorer; besluitnotitie 29 mei). **Iteratie 17:** lege-huls-kernprobleem (Spoor B kader-kiezer toont placeholders i.p.v. controls/beschrijvingen/eisen) als **aangrenzend Spoor-B-vraagstuk** vastgelegd; H40-scope blijft Spoor A-explorer-UI. Open besluit Pad 1 (ontologie-export verrijken) vs Pad 2 (demo-seed verrijken) — bij Steven/masterchat | [[brain__architecture__H40_dashboard-ui-renderdekking]] |
| **H41** *(iteratie 14, T3-bevestiging it. 15, impact gekwantificeerd it. 16)* | **SKOS-axioma-set-handling onder OWL-RL — skos:S46 + S47 niet geladen; T2 + T3 leveren empirisch Δ=0 op 65 + 2 mutaties; reasoner-evaluatie kwantificeert hypothetische activering = +2.831 triples (+6,3%), 12 D4-schendende cross-namespace exactMatch-claims, SHACL 0. Activering = nieuwe D-decision** | [[brain__architecture__H41_skos-axioma-set-handling]] |

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

## Status-mutaties in iteratie 16 (post-v4.6.4 + reasoner-toolchain-evaluatie) ✨

| H | Mutatie | Bron |
|---|---|---|
| **H38** | parked → **resolved** — OWL RL ≡ HermiT empirisch bevestigd voor deze baseline. De reasoner-toolchain-evaluatie (DL-construct-census: één materialiseerbaarheids-complete DL-constructie) voorspelde housekeeping-only; de HermiT-run v4.6.3 vond echter een **reële divergentie** (datatype-range-mismatch op 2 CSF-description-properties, 8 justificaties); v4.6.4 fixte de range (`xsd:string` → `rdfs:Literal`); de HermiT-her-run v4.6.4 bevestigde consistent (0 `owl:Nothing`, geen justificaties). Eerste sprint waarin een HermiT-bevinding een TBox-fix in de canonieke baseline stuurde | [[brain__sprints__v4_6_4_csf-range-fix-dl-conformiteit]] + `evaluatie-reasoner-toolchain-h37-h38-h41.md` + `patch-rapport-v4_6_4.md` |
| **H37** | parked (ongewijzigd, evaluatie-uitkomst toegevoegd) — desk-evaluatie van open-ontologies-MCP (Rust + Oxigraph + tableaux + MCP, MIT, pre-1.0 v0.1.11): oordeel **HOLD**. Geen van 4 triggers actief: H38 toont geen reasoner-limitatie; 44.907 < 50k; pre-1.0; SKOS-impact (H41) hanteerbaar/SHACL-neutraal. Trigger-herijking gedocumenteerd | `evaluatie-reasoner-toolchain-h37-h38-h41.md` §3 |
| **H41** | parked (ongewijzigd, impact gekwantificeerd) — control-run bewijst mechanistisch dat post-inferentie SKOS-groei (+956) 100% `owl:sameAs`-propagatie is, 0% SKOS-axiomas (verklaart T1/T2/T3's Δ=0). Hypothetische activering = +2.831 triples (+6,3%), 12 cross-namespace exactMatch-claims die D4 schenden + SKOS/sameAs-identiteit vermengen; SHACL-impact 0. **Masterchat-regel: toekomstige activering = nieuwe D-decision** (reasoner-/SKOS-axioma-configuratie), niet impliciet | `evaluatie-reasoner-toolchain-h37-h38-h41.md` §2 |

**Kandidaat-H-items uit dashboard-landschap-besluitnotitie (29 mei — masterchat-benoemd, NIET geactiveerd):**

| Kandidaat | Onderwerp | Status |
|---|---|---|
| H42 | SKOS-distributie-visualisatie in explorer | parked-kandidaat, koppelen aan H40 (Spoor A) |
| H43 | Versie-templating-discipline explorer-HTML (Bouwsteen A) | parked-kandidaat |
| H44 | Spoor-A↔B-koppel-architectuur (P1+P3+K1..K4) | parked-kandidaat, formaliseren bij Spoor-B-operationeel |

> Deze drie nummers zijn **door masterchat toegekend** in de besluitnotitie ("ter registratie, niet geactiveerd") — Brein registreert ze conform, declareert ze niet zelf. Detail: [[brain__concepts__dashboard-productlijnen]] + brein-rapport iteratie 16.

**csf↔ISO27001 cross-category-predicaat-vraag (T4 — kandidaat-precedent ZONDER formeel H-nummer):** masterchat heeft dit als *kandidaat* benoemd; Brein legt het empirisch precedent + de open vraag vast (analoog aan cross-category-mappings in iteratie 15), maar declareert **geen formeel H-nummer** zonder expliciete masterchat-instructie. Drie open subvragen: (a) relatedMatch vs closeMatch retrieval-interchangeability voor csf↔ISO, (b) v1.3.1-formalisering, (c) de 699-vs-494-reconciliatie (T4-rapport §2.2 vs §3.1-B onverklaard). Zie [[brain__concepts__cross-category-mappings]] + [[brain__concepts__cross-bron-overlap]].

## Status-mutaties in iteratie 17 (v7-dashboardwerksessie + lag-correctie) ✨

| H | Mutatie | Bron |
|---|---|---|
| **H40** | parked (lege-huls-aangrenzing iteratie 17 toegevoegd) — Het v7-IA-herinrichtings-resultaat (3 juni) bevat een gelaagde kader-kiezer waarvan de detail-content nog placeholders zijn (geen onderliggende controls/beschrijvingen/eisen zichtbaar). Dit is een **aangrenzend Spoor-B-vraagstuk**, niet H40 zelf (H40-scope-afbakening Spoor A blijft hard). Open besluit Pad 1 (ontologie-export verrijken via build-script) vs Pad 2 (demo-seed verrijken voor BIO 2.0 + ISO 27001/27002; geadviseerd nu). Eventueel nieuw H-item bij masterchat-besluit; Brein declareert geen H-nummer zelfstandig | [[brain__concepts__spoor-b-revival]] §"Besluit 1 — Lege-huls" + `patch-rapport-dashboard-ia-herinrichting.md` + `docs/handovers/overdrachtsrapport.md` §5.4 |
| **H29** | future-consideration (organisatiestructuur-koppeling iteratie 17 toegevoegd) — Het tweede open besluit uit de v7-werkstroom is "organisatiestructuur in dashboard" (A generiek / B echte functionele structuur geanonimiseerd — geadviseerd / C volledig echt — gevoelig). De interne-beheersingsfunctie sluit direct aan op het Three Lines Model (H29) + CIO/BVA-RACI (Laag 0+1 governance-kaders, in v7-3 onder Governance-kiezer beschikbaar). Optie B levert realistisch modelwerk voor M04 (roles/RACI). Optie C raakt §0.5-/disclosure-discipline + always-on invariant "organisatienaam NOOIT" — alleen via expliciet masterchat-besluit | [[brain__concepts__spoor-b-revival]] §"Besluit 2 — Organisatiestructuur" + `docs/handovers/overdrachtsrapport.md` §5.5 |

**Geen nieuwe H-items gedeclareerd in iteratie 17.** Brein-discipline: nieuwe H-items zijn masterchat-werk. De lege-huls en organisatiestructuur-vraagstukken zijn vooralsnog **aangrenzend** vastgelegd bij H40 resp. H29, plus als open besluiten in [[brain__concepts__spoor-b-revival]]. Bij eventueel masterchat-besluit kan een nieuw H-item alsnog overwogen worden — of werk kan als sprint-scope landen zonder formeel H-nummer.

**Lag-leerpunt iteratie 17 (vastgelegd in [[brain__log]] iteratie 17):** de v7-werkstroom (2–3 juni) is niet door een Brein-cyclus afgerond toen ze plaatsvond. Tussen iteratie 16 (29 mei) en deze iteratie 17 (4 juni) liep de vault achter op de werkelijke stand — `bootstrap-masterchat-v7.md` en `docs/handovers/overdrachtsrapport.md` beschrijven die latere stand al, maar de brain-vault niet. Brein-cyclus hoort na elke betekenisvolle sessie (ook Spoor B), niet alleen na een ontologie-release.

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
| **H38** *(iteratie 16)* | **OWL RL ≡ HermiT empirisch bevestigd voor deze baseline na v4.6.4-range-fix. Boog: blind spot → DL-census (1 materialiseerbaarheids-complete constructie) → HermiT-run vond reële divergentie (datatype-range-mismatch, 8 justificaties) → fix (`xsd:string` → `rdfs:Literal`) → her-verificatie consistent (0 owl:Nothing). Eerste sprint waarin HermiT een TBox-fix stuurde. Zie [[brain__architecture__H38_owlrl-vs-hermit-equivalentie]] + [[brain__sprints__v4_6_4_csf-range-fix-dl-conformiteit]]** |

**H36 status-correctie iteratie 14 (historie):** H36 was in iteratie 13 als resolved opgenomen; iteratie 14 verschoof terug naar "active (m10 closed, m14 open subtask)" omdat T2 scope-breedte zichtbaar maakte (m14-component nog niet behandeld).

**H36 status-correctie iteratie 15:** T3-sprint sluit m14-subtask volledig af; H36 nu definitief resolved. Cross-category-rationale als T3-leerpunt + kandidaat v1.3.1-precedent gedocumenteerd in concept-bestand (formalisering = masterchat-werk).

## Unknown

| H | Status |
|---|---|
| H16, H17, H23 | Vermelden in andere context maar geen aparte file |

## H-items per D-decision / cluster

| D / cluster | H-items |
|---|---|
| D1 | **H38** *(reasoner-keuze binnen D1, geen D1-wijziging; **resolved iteratie 16** — OWL RL ≡ HermiT bevestigd, D1 versterkt)* |
| D4 | **H36** *(fully closed via T1+T2+T3 iteratie 15)*, **H41** *(SKOS-axioma-set-handling, geparkeerd iteratie 14; impact gekwantificeerd iteratie 16; toekomstige activering = nieuwe D-decision)* |
| D5 | (geen open H-items) |
| D11 | (geen open H-items) |
| D12 | H25, H26, H27, H32 |
| D9 | (architectuur-test gebruikt door H29/H30/H31 future-consideration) |
| **(M11-cluster)** | **H33, H34** *(geen directe D, maar M11-module-betrokken)* |
| **(M21-bron-cluster)** | **H35** *(bron-interpretatie, kandidaat voor latere correctie)* |
| **(toolchain-cluster)** | **H37 (parked, HOLD), H41 (parked, gekwantificeerd)** *(rdflib + reasoner-evaluatie + SKOS-axioma-set)*; **H38 resolved iteratie 16** |
| **(validatie-cluster)** | **H39** *(SHACL false-positive-uitsplitsing, versterkt door T1+T2+T3 bidirectional)* |
| **(dashboard-cluster)** | **H40** *(grc-explorer-render-dekking, Spoor A; Q-M4 latent/parked; lege-huls-aangrenzing Spoor B iteratie 17)*; **kandidaten H42, H43, H44** *(masterchat-benoemd, niet geactiveerd)*; **H29** *(Three Lines Model; organisatiestructuur-koppeling iteratie 17)* |

## Cross-references

- [[brain__decisions__D-register]] — D-decisions
- [[brain__sprints__sprint-register]] — sprints waarin H-items zijn ontstaan / gewijzigd
- [[brain__concepts__concept-register]] — concepts die raken aan H-items
- [[brain__concepts__dashboard-productlijnen]] — concept dat H40 scope-afbakent (Spoor A explorer vs Spoor B dashboard)
- [[brain__index]] — masterindex

— Einde H-register.
