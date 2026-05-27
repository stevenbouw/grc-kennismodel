---
type: architecture
id: H36
title: H36 — ctrl→compl SKOS-mappings audit (m10 closed; m14 open subtask)
status: active
date: 2026-05-27
related:
  - v4_6_0_fase-4-ensia-en-volwassenheid
  - T1_skos-kwaliteitsanalyse-fase-1
  - T2-skos-bidirectional-audit-m10
  - skos-beoordelings-protocol
  - mapping-bron-disclaimer-effect
  - cluster-discipline-bewijslast
  - H41_skos-axioma-set-handling
  - skos-export-filter
  - sameAs-discipline
sources:
  - sessie-rapport-v2_0
  - patch-rapport-v4_6_0
  - t1-eindrapport-v4_6_1
  - patch-rapport-v4_6_1
  - patch-rapport-v4_6_2
  - t2-stap3-eindrapport
chat-sources: []
confidence: high
---

# H36 — ctrl→compl SKOS-mappings audit

## Status

**Active, met m10-component closed** *(iteratie 14)* — m10-scope volledig afgehandeld via T1-sprint (28 paren) + T2-sprint (65 mutaties op 118 paren over 10 clusters). m14-component (31 compl→ctrl-paren in `m14-avg-gdpr.ttl`, omgekeerde modelleringsconventie) blijft **open subtask** voor toekomstige T-sprint.

**Status-evolutie:**

| Datum | Status | Scope |
|---|---|---|
| 2026-05-26 (iteratie 12) | parked | 28 ctrl:↔compl: `exactMatch`-paren in m10 |
| 2026-05-26 (iteratie 13) | closed | T1 voltooide oorspronkelijke H36-scope (28 paren); open uitbreiding naar close/related/broad geregistreerd als T2-scope |
| **2026-05-27 (iteratie 14)** | **active (m10 closed)** | **T2 voltooide m10-scope volledig (93 m10-paren over T1+T2); m14-subtask resteert** |

Eerder geregistreerd post-v4.6.0 in polish-mini-sprint (iteratie 12) als parked, met trigger "SKOS-kwaliteitsanalyse-sprint". Trigger vervuld door T1 + T2.

## Wat het is

In de SKOS-laag van v4.6.0 bestaan **28 expliciete `skos:exactMatch`-relaties tussen `ctrl:`- en `compl:`-namespaces**. De vraag is of alle 28 paren semantisch verdedigbaar zijn als "exact" (D4-conformiteit) of dat enkele eigenlijk `skos:closeMatch` of `skos:relatedMatch` zouden moeten zijn.

Het cijfer 28 is afgeleid uit de bredere SKOS-kwaliteitsanalyse v4.6.0 — ctrl→compl is één van meerdere cross-namespace-clusters in de 1.798-mappings totaal-set.

## Waarom dit een open vraag is

D4 staat alle vier de SKOS-match-types toe (`exactMatch`, `closeMatch`, `relatedMatch`, `narrowMatch`/`broadMatch`), maar geeft geen mechanische procedure om per individueel paar de juiste graad te bepalen. Bij ctrl→compl-paren spelen specifiek:

| Aspect | Risico |
|---|---|
| Control-statement vs. compliance-vereiste hebben verschillende ontologische rol | "Exact" kan misleidend zijn als de tekst-overeenkomst niet matcht met semantische gelijkheid |
| Cumulatief effect over 1.798 mappings | Bij 5% mis-classificatie zou ~90 paren herbeoordeling vragen, niet alleen deze 28 |
| Audit-implicatie | Externe SKOS-audit (DCAT-AP, externe linked-data review) zou exactMatch strenger lezen dan de huidige praktijk |

## Trigger-criterium

| Trigger | Wanneer aandacht oppakken |
|---|---|
| SKOS-kwaliteitsanalyse formeel als sprint geagendeerd | Audit van alle 28 ctrl→compl-paren als onderdeel van bredere 1.798-review |
| Externe audit-vraag over SKOS-mapping-rigour | Per-paar verdediging vereist; nu zou dat improvisatie zijn |
| Spoor B-organisatie eist DCAT-AP-conforme publicatie | exactMatch heeft strengere semantische plicht in linked-data-publicatie-context |

## Aanpak bij activering (toekomst, niet nu)

Niet uitgewerkt — bij activering is een evaluatie-matrix per paar de natuurlijke vorm: per paar de bron-vergelijking + voorgestelde match-type + onderbouwing. Resultaat kan zijn: 0-3 paren herclassificeren, of bevestiging dat alle 28 exact zijn.

## Hangt samen met

- [[brain__decisions__D04_skos-cross-framework]] — D-decision die match-type-keuze definieert
- [[brain__concepts__skos-export-filter]] — meet-laag-onderscheid (1.798 ontologie vs 1.759 export); relevant omdat ctrl/compl-paren beide individual-niveau zijn en wel in JSON-export verschijnen
- [[brain__concepts__sameAs-discipline]] — owl:sameAs is strikt; SKOS is losser maar verdient zelfde rigour-aandacht
- [[brain__sprints__v4_6_0_fase-4-ensia-en-volwassenheid]] — sprint waarin 1.798-baseline is bevestigd

## Bredere context — 1.798 SKOS-totaal

H36 is potentieel het eerste sub-cluster van een grotere kwaliteits-review. Andere clusters kunnen later geregistreerd worden indien specifieke audit-aandacht ontstaat (bv. csf→ctrl, csf→nist-controls, BIO→ISO-Annex-A). Voor nu: alleen het 28-paar-cluster geregistreerd als concrete grootte met expliciete trigger.

## Uitkomst T1-sprint (26 mei 2026) — 28 exactMatch-paren

T1-sprint heeft alle 28 paren beoordeeld volgens [[brain__concepts__skos-beoordelings-protocol]] v1.0:

| Aspect | Resultaat |
|---|---|
| Beoordeelde paren | 28 (volledig — geen openstaande paren) |
| Uitkomst | **28× herclassificatie `exactMatch` → `broadMatch`** |
| Confidence per paar | 28× hoog |
| Evidence-niveau per paar | 28× niveau 1 (CBW-Excel reproduceert ENISA TIG v1.0 mapping-tabel) |
| Twijfelgevallen | 2 edge-cases (T1-021 + T1-023) opgelost via masterchat-NEN-PK-toets — beide → broadMatch |
| Patch | v4.6.1 toegepast op `m10-nis2-ext.ttl` (hash `78b8ee44...` → `cb2d567b...`) |
| Cluster-consistentie | 10 clusters, alle behandeld zonder half-half-cluster-uitkomsten |
| D4-conformance | Verbetering — `exactMatch` was te sterk geclaimd; ENISA TIG regel 285 stelt expliciet dat mapping géén equivalence-claim is |

**Belangrijkste bevinding voorbij H36:** ENISA-disclaimer-categorisch-effect — autoritatieve mapping-bron verbiedt equivalence-interpretatie via expliciete disclaimer. Vermoedelijk generaliseerbaar patroon. Zie [[brain__concepts__mapping-bron-disclaimer-effect]].

## Uitkomst T2-sprint (27 mei 2026) — 118 m10-paren close + related + broad

T2-sprint heeft de overige m10 ctrl→compl-mappings beoordeeld onder Protocol v1.2 (bidirectional). Zie [[brain__sprints__T2-skos-bidirectional-audit-m10]] voor sprint-context.

| Aspect | Resultaat |
|---|---|
| Beoordeelde paren m10 | 118 (volledig — incl. 28 reeds in T1 omgezet) |
| Patch-mutaties | **65** (32 closeMatch → broadMatch downgrade + 33 relatedMatch → broadMatch upgrade) |
| Behoud (al broadMatch) | 53 paren |
| Confidence per paar | 65× hoog (cluster-discipline-overerving) |
| Evidence-niveau cluster-niveau | Niveau 1 voor alle 10 clusters via CBW-Mapping-UV (reproductie ENISA TIG v1.0); D4.1-disclaimer-cluster-niveau-toepassing |
| Patch | v4.6.2 toegepast op `m10-nis2-ext.ttl` (hash `cb2d567b…` → `a4bfdc12…`) |
| Cluster-discipline-validatie | 10/10 clusters convergeren naar `broadMatch`; 0 NEN-aantoonbare uitzonderingen op 10 heuristiek-flags |
| Bidirectional-bewijs | 32 downgrade + 33 upgrade — symmetrische Protocol v1.2-toepassing |

**Cumulatieve m10-scope na T1+T2:** 28 + 65 = **93 m10-paren** gepatcht; alle 118 m10 ctrl→compl-paren convergeren naar `broadMatch` post-v4.6.2 (eindstand: exact 0 / close 0 / broad 118 / narrow 0 / related 0).

**Methode-protocol-progressie:** v1.0 (T1) → v1.2 (T2 operationeel) → v1.3 (DRAFT, vaststelling pending). Zie [[brain__concepts__skos-beoordelings-protocol]] §Protocol-versie-roadmap.

## Open subtask — m14 compl→ctrl-paren

T2-scope per masterchat-besluit **Optie C**: m10-only T2; m14 wordt aparte T-sprint.

| Aspect | Status |
|---|---|
| Module | `m14-avg-gdpr.ttl` |
| Aantal paren | 31 (alle compl→ctrl-richting; 27 relatedMatch + 2 closeMatch + 2 broadMatch — alle in m14-AVG-cluster) |
| Modelleringsconventie | compl: → ctrl: (omgekeerd t.o.v. m10's ctrl: → compl:) |
| AVG-cross-walk-bron | Ontbreekt in `sources/` — vereist bron-upload of evidence-niveau-2/3-tolerantie |
| Protocol-versie bij uitvoering | v1.3 (DRAFT) of v1.4 indien verdere verfijningen vóór m14-start |
| Symmetrie-toets | Vereist Protocol v1.2/v1.3-symmetrie-validatie op compl→ctrl-richting (mogelijk Protocol-aanvulling nodig) |
| Helper-script-uitbreiding | Cross-module label-bronnen + m14-specifieke heuristieken nodig |

Trigger voor activering: aparte T-sprint-scoping in verse masterchat-sessie post-T2. Niet nu uit te voeren.

## Andere m11- en ISO27001-cluster-kandidaten (informatief)

Voorbij m10 + m14 zijn er nog meer ctrl:↔compl:-mapping-clusters in andere modules die in toekomst onder dezelfde audit kunnen vallen:

- m11-cluster (NIST SP 800-53 ↔ andere frameworks) — kandidaat voor latere T-sprint
- m09-iso27001-ext (ISO 27001 ↔ compl:) — kandidaat voor latere T-sprint indien Spoor B-vraag opkomt

Niet als subtasks van H36 geregistreerd (verschillende modules + verschillende bron-context); kandidaten voor eigen H-items bij toekomstige relevant-wording.

## Architectuur-impact

| Impact-veld | Resultaat |
|---|---|
| D4 + D4.1 | D4 onveranderd; D4.1 toepassings-precedent uitgebreid van paar-niveau (T1) naar cluster-niveau (T2). Zie [[brain__decisions__D04_skos-cross-framework]] §D4.1 |
| H39 (SHACL-blinde-vlek) | Bevestigd op 118-paren-schaal; trigger-relevantie verder verhoogd |
| H41 (SKOS-axioma-set) | Nieuw geregistreerd als parked H-item op basis van T2-empirisch bewijs (Δ post-OWL-RL = 0 op 65 mutaties). Zie [[brain__architecture__H41_skos-axioma-set-handling]] |
| Methode-protocol | v1.2 operationeel bevestigd; v1.3-draft opgeleverd met 7 verfijning-voorstellen |
| Cluster-discipline-bewijslast | Empirisch gevalideerd via 0/10 succesvolle heuristiek-flag-uitzonderingen. Zie [[brain__concepts__cluster-discipline-bewijslast]] |

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-26 | parked | Geregistreerd in iteratie 12 polish-mini-sprint, eerder aangemerkt als "te registreren v1.10" in sessie-rapport v2.0 |
| 2026-05-26 | closed | Afgehandeld via T1-sprint — 28× exactMatch → broadMatch via patch v4.6.1; methode-protocol v1.0 als bijproduct vastgesteld |
| 2026-05-27 | **active (m10 closed)** | **T2-sprint voltooit m10-scope volledig (cumulatief 93 m10-paren via T1+T2). m14-subtask (31 compl→ctrl-paren) open voor toekomstige T-sprint. H-item blijft active wegens m14-component; m10-component administratief afgesloten** |

— Einde H36.
