---
type: concept
title: Cross-category-mappings — SKOS-rationale bij cross-category-paren (T3-precedent, kandidaat v1.3.1)
status: living
date: 2026-05-28
candidate_status: kandidaat-v1.3.1-precedent
related:
  - D04_skos-cross-framework
  - T3-skos-bidirectional-audit-m14
  - skos-beoordelings-protocol
  - cluster-discipline-bewijslast
  - mapping-bron-disclaimer-effect
  - cross-bron-overlap
  - H36_skos-exactmatch-ctrl-compl-audit
sources:
  - patch-rapport-v4_6_3
  - t3-stap3-eindrapport
  - t3-pilot-rapport
  - skos-beoordelings-protocol-v1_3
  - t4-pre-sprint-inventarisatie
chat-sources: []
confidence: high
---

# Cross-category-mappings — SKOS-rationale bij cross-category-paren

> **Status:** **kandidaat v1.3.1-precedent** voor SKOS-beoordelings-protocol. Formalisering in Protocol-tekst is masterchat-werk bij volgende sprint-scoping. Tech/Brein voert geen autonome Protocol-tekst-wijziging uit. Dit concept-bestand legt het principe als T3-empirisch precedent vast in de brain-vault — niet als formele protocol-aanvulling.

## Wat het is

Wanneer subject en object van een SKOS-mapping in **ontologisch verschillende categorieën** zitten (bv. control ↔ legal-obligation, control ↔ standard-clause), is de basislijn-predicate `skos:relatedMatch` (associatief). `skos:broadMatch` / `skos:narrowMatch` tussen cross-category-paren is een **categorie-fout** in de meeste gevallen, omdat operationele implementatie-relatie geen conceptuele subsumptie impliceert. Een control "valt onder" een verplichting maar is niet "een soort verplichting" — het is een operationele invulling.

**Uitzondering naar `closeMatch`** is mogelijk bij **retrieval-interchangeability**: wanneer de control de canonieke implementatie-equivalent is van de verplichting in een GRC-audit-context (een audit-vraag "welke control implementeert deze verplichting?" zou de control als directe primaire match terug moeten geven).

`skos:exactMatch` is in cross-category-context structureel uitgesloten — twee verschillende ontologische categorieën kunnen niet semantisch identiek zijn ongeacht definitionele overlap.

## Operationele werking (Protocol §3.1 + §3.3-context)

Cluster-discipline-default-toepassing per Protocol §3.1 wordt op cross-category-niveau **overstemd door C3-falen op conceptuele subsumptie**:

| Cluster-cardinaliteit | Cluster-doel-default §3.1 | Cross-category-overstemming |
|---|---|---|
| veel↔1 (subject-cluster ≥2, object singleton) | rij 6 `broadMatch` | cross-category-fout indien subject ↔ object categorisch verschillen — overstemd naar `relatedMatch` |
| 1↔veel (subject singleton, object-cluster ≥2) | rij 7 `narrowMatch` | cross-category-fout indien subject ↔ object categorisch verschillen — overstemd naar `relatedMatch` |
| veel↔veel | per-paar | cross-category-rationale prevaleert per paar |
| 1↔1 | per-paar | `relatedMatch` basislijn; `closeMatch` mogelijk bij retrieval-interchangeability |

Cross-category-rationale opereert **vóór cluster-discipline-default-toepassing zou kunnen plaatsvinden** — structurele eigenschap van cross-category-mappings, niet een per-paar-uitzondering. Cluster-discipline-§3.3 bewijslast-asymmetrie ([[brain__concepts__cluster-discipline-bewijslast]]) blijft van kracht binnen een cross-category-cluster (bv. ter ondersteuning van consistentie binnen Art5_1f-cluster relatedMatch×7), maar wordt op meta-niveau overschreven door cross-category-rationale.

## T3-empirisch bewijs (m14 AVG/GDPR, 28 mei 2026)

T3-sprint heeft op productie-schaal (31 m14-paren over 5 AVG-clusters) bewijs geleverd:

| Aspect | Waarde |
|---|---:|
| Beoordeelde paren | 31 |
| Cluster-convergentie naar narrowMatch (verwacht via §3.1 rij 7) | **0/5 clusters** |
| Relatedmatch-behoud op cross-category-basis | 27 paren |
| broadMatch-behoud | 0 paren (alle 2 ex-broadMatch → relatedMatch via masterchat-besluit Optie C) |
| closeMatch-uitzondering op retrieval-interchangeability | 2 paren (T3-014 + T3-026) |
| exactMatch-overweging | 0 paren (D4.1-vooraf-check inactief; cross-category structureel uitgesloten) |

**Distinctie van T2 (m10 NIS2)** — methodisch tegenovergesteld:

| Module | Cluster-richting | Cluster-doel-default §3.1 | Cluster-convergentie | Categorie-relatie |
|---|---|---|---:|---|
| m10 (T2) | veel↔1 (ctrl→NIS2) | broadMatch (rij 6) | 100% (alle 10 clusters) | control ↔ control-eis (zelfde categorie operationeel) |
| **m14 (T3)** | **1↔veel (compl→ctrl)** | **narrowMatch (rij 7)** | **0% (geen cluster)** | **control ↔ legal-obligation (cross-category)** |

m10's convergentie was **framework-specifiek** (ISO 27002 ↔ NIS2 zijn beide control/eisen-niveau, operationeel zelfde categorie). m14's non-convergentie is **categorie-specifiek** (cross-category-asymmetrie blokkeert cluster-projectie).

## closeMatch-uitzondering — retrieval-interchangeability

`closeMatch` tussen cross-category-paren is verdedigbaar wanneer de control de **canonieke implementatie-equivalent** is van de verplichting binnen GRC-audit-context. Twee m14-paren onder T3:

| Paar | Cluster | Object | Rationale | Confidence |
|---|---|---|---|---|
| T3-014 | Art32 | ISO27002_5_01 Beleidsregels IB | Governance/policy-canoniciteit — audit-vraag "welke control implementeert Art. 32 passende-maatregelen-eis?" levert 5.01 als directe primaire match | middel (niveau-2 evidence) |
| T3-026 | Art33 | ISO27002_5_24 Plannen incidentbeheer | Incident-planning-canoniciteit — audit-vraag "welke control implementeert Art. 33 meldings-planningsplicht?" levert 5.24 als directe primaire match | middel (niveau-3 evidence; conceptuele basis sterker dan T3-014) |

**Distinctie van niet-houdbare interchangeability:** T3-028 (Art33 → 5.26 Response to incidents) en T3-030 (Art34 → 5.26) zijn closeMatch-kandidaten die afgewezen werden — 5.26 is reactief (incident-response in algemene zin), niet primaire-match voor specifieke meldings-verplichtingen. Predicate-keuze blijft `relatedMatch` (cross-category-basislijn) met confidence middel wegens scope-asymmetrie.

## Cross-category-paren — inscope-voorbeelden + toekomstige projectie

| Categorie-paar | T-sprint-precedent | Status |
|---|---|---|
| **control ↔ legal-obligation** | T3 (m14 ISO 27002 ↔ AVG; 31 paren bewezen) | empirisch precedent gevestigd |
| **outcome ↔ requirement** (csf:Subcategory ↔ ISO 27001 mandatory clause) | T4-inventarisatie (245 unie, `ext:ISMSRequirement`) | **kandidaat-precedent (geen formeel H-nummer)** |
| **outcome ↔ measure** (csf:Subcategory ↔ ISO 27001 Annex A control) | T4-inventarisatie (494, `bio:ISO27002` via D5-brug) | **kandidaat-precedent (geen formeel H-nummer)** |
| control ↔ standard-clause | (open — bv. ISO 27002 ↔ ISO 27001 Annex A; mogelijk niet T-sprint-scope) | toekomstige overweging |
| control ↔ wettelijke verplichting in andere modules | m16 VIRBI? m12 DORA? | toekomstige Brein-overweging |
| framework ↔ framework (fw:↔fw:) | beperkt huidig (Sectie 4 m14 + m01/m07) | niet primair cross-category |
| control ↔ NIS2-control-eis | m10 (T2) — geen cross-category | n.v.t. (zelfde categorie operationeel) |

## Niet-cross-category-paren — wat blijft binnen cluster-discipline-default

Cluster-discipline-default per Protocol §3.1 + §3.3 blijft volledig van toepassing op **binnen-categorie-mappings**:

- m10 ctrl→compl-richting via T2: ctrl:ISO27002 ↔ compl:NIS2_a-j — beide zijn control/eisen-niveau (ENISA TIG ↔ NIS2-art.21-letters formuleren control-eisen). 100% cluster-convergentie naar broadMatch bevestigd in T2 over 10 clusters.
- m11 ctrl:NIST_SP800_53 ↔ ctrl:ISO27002 (binnen control-categorie) — cluster-discipline-default van toepassing
- bio: ↔ ctrl: (D5-sameAs, niet SKOS — buiten cross-category-overweging)

Cross-category-rationale en cluster-discipline-default zijn **complementair**, niet conflicterend: cluster-discipline-default opereert binnen één categorie; cross-category-rationale opereert tussen categorieën.

## csf↔ISO27001 — tweede cross-category-kandidaat-precedent (T4, 29 mei 2026 — ZONDER formeel H-nummer)

De T4-pre-sprint-inventarisatie (`output/reports/t4-pre-sprint-inventarisatie.md`, READ-ONLY) bracht een **tweede** cross-category-context in beeld: csf:Subcategory (outcome) ↔ ISO 27001. Masterchat heeft dit als **kandidaat** benoemd; Brein legt het empirisch precedent + de open vraag vast (analoog aan hoe dit concept zelf in iteratie 15 als kandidaat is vastgelegd), maar **declareert geen formeel H-nummer** zonder expliciete masterchat-instructie.

**Wat er ligt (model-meetbaar, T4):** 739 csf↔ISO27001 closeMatch-mappings, beide eindpunt-typen **cross-category** t.o.v. csf-outcomes, géén prima-facie defect (0 exactMatch → geen prima-facie schending). Het ISO-eindpunt is **gesplitst** in twee categorieën:

| ISO-eindpunt | Representatie | Categorie | csf↔X karakter | n |
|---|---|---|---|---:|
| Mandatory clauses 4-10 | `ext:ISO27001_*` (`ext:ISMSRequirement`) | eis-categorie | outcome ↔ requirement (cross-category) | 245 (unie) |
| Annex A-controls | `bio:ISO27002_*` (D5-brug → ctrl:) | measure-categorie | outcome ↔ control (cross-category) | 494 (m21-only) |

Beide zijn prima facie cross-category t.o.v. `csf:Subcategory` → de T3-relatedMatch-basislijn is hier de natuurlijke kandidaat. Maar de huidige predicate-status is **100% closeMatch** (conversie-default uit de import, géén OLIR-getypeerd per-paar-oordeel) — dezelfde spanning closeMatch-vs-relatedMatch die T3 bij m14 oploste, nu op grotere schaal (potentieel mutatie-bereik tot 739 closeMatch → relatedMatch, mits per-paar de retrieval-interchangeability-uitzondering wordt getoetst).

**Drie open subvragen (masterchat-werk, NIET door Brein/Tech te beslissen):**

| # | Subvraag | Toelichting |
|---|---|---|
| (a) | `relatedMatch` vs `closeMatch` retrieval-interchangeability voor csf↔ISO | Geldt de cross-category-relatedMatch-basislijn (T3-precedent) hier, of blijft closeMatch verdedigbaar via retrieval-interchangeability per paar? csf-outcomes hebben mogelijk bredere interchangeability dan AVG-artikelen |
| (b) | v1.3.1-formalisering | Een formele cross-category-§3.4 zou csf↔ISO direct beslisbaar maken; blijft masterchat-werk (zie hieronder) |
| (c) | **699-vs-494-reconciliatie** | T4-rapport §2.2 (csf→bio closeMatch = **699**) vs §3.1-B (m21 Annex A = **494**) is **onverklaard** in het rapport. Het verschil (205) moet gereconcilieerd worden vóór een eventuele pilot — mogelijk telt §2.2 csf→bio over alle bron-attributies terwijl §3.1-B alleen Sheet 8-Annex-A telt, maar dat is niet vastgesteld |

**Distinctie van het m14-precedent:** m14 (T3) was control ↔ legal-obligation (1↔veel, 31 paren, AVG = publiek EU-recht zonder disclaimer). csf↔ISO27001 is outcome ↔ requirement én outcome ↔ measure (twee eindpunt-categorieën, 739 paren, gesplitste categorie, ISO 27001 deels NEN-restrictief maar parafrase-volstaand). Het cross-category-principe is hetzelfde; de cardinaliteit, schaal en bron-context verschillen. Zie [[brain__concepts__cross-bron-overlap]] voor de overlap-detectie-nuance (105 = bron-niveau, niet machine-reproduceerbaar).

## Kandidaat-formalisering — Protocol v1.3.1 (NIET nu uitvoeren)

Mogelijke v1.3.1-aanvulling op Protocol §3.3 of nieuwe §3.4:

> **Cross-category-mappings:** wanneer subject en object van een SKOS-mapping in ontologisch verschillende categorieën zitten (bv. control ↔ legal-obligation, control ↔ standard-clause), is de basislijn-predicate `skos:relatedMatch` (associatief). `skos:broadMatch` / `skos:narrowMatch` tussen cross-category-paren is een categorie-fout in de meeste gevallen omdat operationele implementatie-relatie geen conceptuele subsumptie impliceert. Uitzondering naar `skos:closeMatch` is mogelijk bij retrieval-interchangeability — wanneer de control de canonieke implementatie-equivalent is van de verplichting in een GRC-audit-context. Cluster-discipline §3.3 default-toepassing wordt op cross-category-niveau overstemd door C3-falen op conceptuele subsumptie. `skos:exactMatch` is in cross-category-context structureel uitgesloten.

**Status:**

- Niet uitgevoerd in T3 (Tech-subagent voert geen autonome Protocol-tekst-wijziging uit; D4 + Protocol-vaststelling = masterchat-werk)
- **Niet uitgevoerd in Brein-cyclus iteratie 15** (formalisering blijft masterchat-werk; Brein legt het principe als T3-empirisch precedent vast in dit concept-bestand)
- Aanbevolen voor masterchat-besluit bij volgende sprint-scoping of v1.3.1-protocol-revisie

## D-cross-references

| D | Relatie |
|---|---|
| [[brain__decisions__D04_skos-cross-framework]] | Cross-category-rationale opereert binnen D4. T3 m14-toepassings-precedent toegevoegd aan D4-validatie-historie als cross-category-precedent. D4-tekst zelf onveranderd; alleen precedent-uitbreiding. |

**D4.1 onafhankelijk van cross-category-principe:** D4.1 blokkeert `exactMatch` wanneer autoritatieve mapping-bron non-equivalence-disclaimer bevat. Cross-category-rationale blokkeert `exactMatch` wanneer subject ↔ object categorisch verschillen. Beide kunnen onafhankelijk werken; cross-category-blokkade is structureel, D4.1-blokkade is bron-context-afhankelijk.

## H-cross-references

| H | Relatie |
|---|---|
| [[brain__architecture__H36_skos-exactmatch-ctrl-compl-audit]] | T3 m14-component (afgehandeld via cross-category-rationale + closeMatch-uitzondering); H36 fully closed |

## Concept-cross-references

- [[brain__concepts__skos-beoordelings-protocol]] — methode-concept waaronder cross-category-rationale een aanvulling vormt (kandidaat v1.3.1)
- [[brain__concepts__cluster-discipline-bewijslast]] — complementair: opereert binnen één categorie; cross-category-rationale opereert tussen categorieën
- [[brain__concepts__mapping-bron-disclaimer-effect]] — onafhankelijk maar parallel blokkade-mechanisme voor exactMatch (D4.1 vs cross-category)

## Sprint-cross-references

- [[brain__sprints__T3-skos-bidirectional-audit-m14]] — empirisch precedent op 31 m14-paren over 5 AVG-clusters
- [[brain__sprints__T2-skos-bidirectional-audit-m10]] — distinctie-precedent (binnen-categorie cluster-discipline-conform 10/10)
- T4-pre-sprint-inventarisatie (`output/reports/t4-pre-sprint-inventarisatie.md`) — tweede cross-category-kandidaat (csf↔ISO27001, 739 paren, gesplitste categorie); inventarisatie-only, geparkeerd (Optie B); kandidaat-precedent zonder formeel H-nummer
- [[brain__concepts__cross-bron-overlap]] — T4-overlap-detectie-nuance (105 = bron-niveau, niet machine-reproduceerbaar)

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-28 | living (kandidaat v1.3.1-precedent) | Concept ontstaan uit T3-sprint Stap 3-eindrapport §5 + patch-rapport v4.6.3 §13.1. Empirisch precedent vastgelegd op 31 m14-paren (control ↔ legal-obligation cross-category). Formele Protocol-tekst-wijziging als kandidaat v1.3.1-aanvulling gemarkeerd; formalisering = masterchat-werk bij volgende sprint-scoping (NIET Brein-taak in iteratie 15) |
| 2026-05-29 | living (kandidaat v1.3.1-precedent) | **Tweede cross-category-kandidaat-precedent toegevoegd: csf↔ISO27001** (T4-inventarisatie, 739 paren, gesplitste categorie outcome↔requirement + outcome↔measure). Drie open subvragen vastgelegd: (a) relatedMatch-vs-closeMatch retrieval-interchangeability, (b) v1.3.1-formalisering, (c) 699-vs-494-reconciliatie (T4-rapport §2.2 vs §3.1-B onverklaard). **Geen formeel H-nummer** zonder masterchat-instructie (Brein-discipline, analoog iteratie 15). cross-category-paren-tabel uitgebreid |

— Einde cross-category-mappings.
