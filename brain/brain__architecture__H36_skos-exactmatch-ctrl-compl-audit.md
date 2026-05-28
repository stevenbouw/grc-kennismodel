---
type: architecture
id: H36
title: H36 — ctrl:↔compl: SKOS-mappings audit (fully closed via T1+T2+T3)
status: closed
date: 2026-05-28
related:
  - v4_6_0_fase-4-ensia-en-volwassenheid
  - T1_skos-kwaliteitsanalyse-fase-1
  - T2-skos-bidirectional-audit-m10
  - T3-skos-bidirectional-audit-m14
  - skos-beoordelings-protocol
  - cross-category-mappings
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
  - patch-rapport-v4_6_3
  - t3-stap3-eindrapport
chat-sources: []
confidence: high
---

# H36 — ctrl:↔compl: SKOS-mappings audit

## Status

**Fully closed** *(iteratie 15)* — m10-scope volledig afgehandeld via T1-sprint (28 paren) + T2-sprint (65 mutaties op 118 paren over 10 clusters); m14-scope volledig afgehandeld via T3-sprint (2 mutaties op 31 paren over 5 AVG-clusters). H36 als geheel afgesloten — cumulatief **149 ctrl:↔compl:-paren** over T1+T2+T3 beoordeeld onder Protocol v1.0/v1.2/v1.3 FINAL.

**Status-evolutie:**

| Datum | Status | Scope |
|---|---|---|
| 2026-05-26 (iteratie 12) | parked | 28 ctrl:↔compl: `exactMatch`-paren in m10 |
| 2026-05-26 (iteratie 13) | closed | T1 voltooide oorspronkelijke H36-scope (28 paren); open uitbreiding naar close/related/broad geregistreerd als T2-scope |
| 2026-05-27 (iteratie 14) | active (m10 closed) | T2 voltooide m10-scope volledig (93 m10-paren over T1+T2); m14-subtask resteert |
| **2026-05-28 (iteratie 15)** | **fully closed** | **T3 voltooide m14-scope (31 paren over 5 AVG-clusters); H36 als geheel afgesloten** |

Eerder geregistreerd post-v4.6.0 in polish-mini-sprint (iteratie 12) als parked, met trigger "SKOS-kwaliteitsanalyse-sprint". Trigger vervuld door T1 + T2 + T3.

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

## Uitkomst T3-sprint (28 mei 2026) — m14 closed (31 compl→ctrl-paren)

T3-sprint heeft de m14-subtask afgehandeld onder Protocol v1.3 FINAL. Zie [[brain__sprints__T3-skos-bidirectional-audit-m14]] voor sprint-context.

| Aspect | Resultaat |
|---|---|
| Beoordeelde paren m14 | 31 (volledig — alle compl→ctrl-paren in `m14-avg-gdpr.ttl`) |
| Patch-mutaties | **2** (T3-001 + T3-002, beide `compl:AVG_Art5_1f skos:broadMatch ctrl:ISO27002_*` → `skos:relatedMatch`; directe instructie-uitvoering masterchat-besluit Optie C op pilot-escalatie) |
| Behoud relatedMatch (cross-category-rationale) | 27 paren |
| Behoud closeMatch (retrieval-interchangeability) | 2 paren (T3-014 Art32 → 5.01 + T3-026 Art33 → 5.24) |
| Confidence per paar | 27 hoog + 4 middel + 0 laag (errata 28-05: T3-002 hoog post-besluit, analoog T3-001) |
| Evidence-niveau-verdeling | 10 niveau-1 + 7 niveau-2 + 14 niveau-3 (via ISO 27701:2025 Annex D + Annex F twee-staps-keten) |
| Patch | v4.6.3 toegepast op `m14-avg-gdpr.ttl` (hash `47daeb7e…` → `874565ba…`) |
| Cross-category-rationale | Cluster-doel-default §3.1 rij 7 (narrowMatch in 1↔veel-subject-cluster) systematisch overstemd door C3-falen op conceptuele subsumptie; control ↔ legal-obligation = associatief, niet subsumptief |
| D4.1-status | **inactief** in T3 (bindende T3-steer 1; AVG = publiek EU-recht zonder non-equivalence-disclaimer) |
| closeMatch-uitzondering | Op retrieval-interchangeability binnen governance/policy- respectievelijk incident-planning-domein (T3-014 + T3-026; beide confidence middel; methodologisch consistent toegepast) |

**Cumulatieve scope-completion T1+T2+T3:** 28 + 65 + 2 = **95 mutaties** binnen **149 ctrl:↔compl:-paren beoordeeld** (28 + 118 + 31 = 177; min overlap T1⊂T2 op exactMatch-set zelfde 28; netto unieke paren-volume = 28 + 90 + 31 = 149).

| Module | Richting | Paren | Mutaties | Sprints |
|---|---|---:|---:|---|
| m10-nis2-ext | ctrl → compl | 118 (cumulatief T1+T2) | 93 (28 T1 + 65 T2) | T1 (v4.6.1) + T2 (v4.6.2) |
| m14-avg-gdpr | compl → ctrl | 31 | 2 | T3 (v4.6.3) |
| **Totaal H36-scope** | **bidirectional** | **149** | **95** | **T1+T2+T3** |

**Methode-protocol-progressie:** v1.0 (T1) → v1.2 (T2 operationeel) → v1.3 DRAFT → **v1.3 FINAL (T3 operationeel; vaststelling 28 mei 2026 door masterchat tijdens T3-scoping)**. Cross-category-rationale = kandidaat v1.3.1-precedent. Zie [[brain__concepts__skos-beoordelings-protocol]] en [[brain__concepts__cross-category-mappings]].

## Andere m11- en ISO27001-cluster-kandidaten (informatief)

Voorbij m10 + m14 zijn er nog meer ctrl:↔compl:-mapping-clusters in andere modules die in toekomst onder dezelfde audit kunnen vallen:

- m11-cluster (NIST SP 800-53 ↔ andere frameworks) — kandidaat voor latere T-sprint
- m09-iso27001-ext (ISO 27001 ↔ compl:) — kandidaat voor latere T-sprint indien Spoor B-vraag opkomt

Niet als subtasks van H36 geregistreerd (verschillende modules + verschillende bron-context); kandidaten voor eigen H-items bij toekomstige relevant-wording.

## Architectuur-impact

| Impact-veld | Resultaat |
|---|---|
| D4 + D4.1 | D4 onveranderd; D4.1 toepassings-precedent uitgebreid van paar-niveau (T1) naar cluster-niveau (T2). T3 toevoegt: D4.1 inactief in cross-category-context (AVG = publiek EU-recht zonder non-equivalence-disclaimer); cross-category-rationale als nieuwe D4-toepassings-precedent op m14. Zie [[brain__decisions__D04_skos-cross-framework]] §D4.1 + cross-category-rationale-sectie |
| H39 (SHACL-blinde-vlek) | Bevestigd op 118-paren-schaal in T2 (ctrl→compl); T3 bevestigt op 31-paren-schaal in tegengestelde richting (compl→ctrl) — blinde-vlek nu bidirectional vastgesteld |
| H41 (SKOS-axioma-set) | Nieuw geregistreerd in T2; T3 levert derde sprint-bewijs Δ post-OWL-RL = 0 op 2 SKOS-mutaties — declared-evidence informatief uitgebreid; status ongewijzigd |
| Methode-protocol | v1.2 (T2) → v1.3 FINAL (T3 operationeel; masterchat-vastgesteld 28 mei 2026 tijdens T3-scoping). Cross-category-rationale = kandidaat v1.3.1-precedent. Zie [[brain__concepts__cross-category-mappings]] |
| Cluster-discipline-bewijslast | Empirisch gevalideerd in T2 (0/10 succesvolle heuristiek-flag-uitzonderingen). T3 toont structurele blokkering op cross-category-niveau (0/0 cluster-convergentie naar narrowMatch). Zie [[brain__concepts__cluster-discipline-bewijslast]] + [[brain__concepts__cross-category-mappings]] |

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-26 | parked | Geregistreerd in iteratie 12 polish-mini-sprint, eerder aangemerkt als "te registreren v1.10" in sessie-rapport v2.0 |
| 2026-05-26 | closed | Afgehandeld via T1-sprint — 28× exactMatch → broadMatch via patch v4.6.1; methode-protocol v1.0 als bijproduct vastgesteld |
| 2026-05-27 | active (m10 closed) | T2-sprint voltooit m10-scope volledig (cumulatief 93 m10-paren via T1+T2). m14-subtask (31 compl→ctrl-paren) open voor toekomstige T-sprint. H-item blijft active wegens m14-component; m10-component administratief afgesloten |
| **2026-05-28** | **fully closed** | **T3-sprint voltooit m14-scope (31 paren over 5 AVG-clusters; 2 mutaties broadMatch → relatedMatch via masterchat-besluit Optie C op pilot-escalatie; 27 behoud relatedMatch + 2 behoud closeMatch op retrieval-interchangeability). H36 als geheel afgesloten; cumulatief 149 ctrl:↔compl:-paren over T1+T2+T3. Cross-category-rationale als T3-leerpunt en kandidaat v1.3.1-precedent gedocumenteerd (formalisering = masterchat-werk)** |

— Einde H36.
