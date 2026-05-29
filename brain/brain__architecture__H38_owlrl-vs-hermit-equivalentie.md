---
type: architecture
id: H38
title: H38 — OWL RL (owlrl-package) vs HermiT (Protégé) equivalentie — RESOLVED via v4.6.4 (range-fix + HermiT-her-run)
status: resolved
date: 2026-05-29
related:
  - D01_owl-2-dl-profiel
  - owl-rl-reasoning
  - H37_open-ontologies-mcp
  - H41_skos-axioma-set-handling
  - v4_6_4_csf-range-fix-dl-conformiteit
sources:
  - handover-tech-chat-to-subagent-v4_6_0
  - evaluatie-reasoner-toolchain-h37-h38-h41
  - patch-rapport-v4_6_4
chat-sources: []
confidence: high
---

# H38 — OWL RL vs HermiT equivalentie (RESOLVED via v4.6.4)

## Status

**Resolved (iteratie 16, 29 mei 2026)** — empirisch gesloten. Eerder parked (geregistreerd iteratie 12). H38 is afgehandeld via de reasoner-toolchain-evaluatie (DL-construct-census) + de HermiT-run die een reële divergentie vond + de v4.6.4-range-fix die haar oploste + de HermiT-her-run die consistentie bevestigde. Zie [[brain__sprints__v4_6_4_csf-range-fix-dl-conformiteit]].

## De volledige boog (blind spot → evaluatie → bevinding → fix → her-verificatie)

H38 is niet "weggeredeneerd" maar empirisch gesloten via vijf stappen — en de uitkomst is genuanceerder dan de oorspronkelijke verwachting (de evaluatie voorspelde housekeeping-only, maar de HermiT-run vond een reële divergentie):

1. **Blind spot** (iteratie 12, uit Fase 0 Tech-handover): sinds v4.0.0 geen HermiT-herrun op de modulaire baseline; OWL RL ≡ HermiT plausibel maar niet aangetoond.
2. **Evaluatie** (29 mei 2026, `evaluatie-reasoner-toolchain-h37-h38-h41.md` §1): DL-construct-census over de hele TBox markeerde **één** OWL RL-onvolledige constructie — `asset:AssetOrComponent owl:equivalentClass [ owl:unionOf (asset:Asset asset:AssetComponent) ]`. Die is **materialiseerbaarheids-compleet** onder OWL RL (lid→unie materialiseert: 0 → 118 instances; unie→lid is een disjunctieve conclusie die géén reasoner als ABox-triple toevoegt). Voorspelde HermiT-delta = uitsluitend housekeeping → oordeel HOLD, runbook geleverd.
3. **Bevinding** (HermiT-run v4.6.3, Protégé, projecteigenaar): de run meldde de merged graph **inconsistent** (`owl:Thing SubClassOf owl:Nothing`, **8 justificaties** = 4 CSF-Tiers × 2 properties). Een **reële OWL-RL/DL-divergentie** — niet de voorspelde housekeeping, maar een datatype-range-mismatch: `csf:riskGovernanceDescription` + `csf:riskManagementDescription` hadden `rdfs:range xsd:string` maar dragen `@en`-getagde waarden (`rdf:langString`). Een volledige DL-reasoner ziet dat als datatype-botsing; OWL RL controleert datatype-ranges niet streng (vandaar 0 `owl:Nothing` onder de canonieke owlrl-config — de fout bleef daar onzichtbaar).
4. **Fix** (v4.6.4): 2× `rdfs:range xsd:string` → `rdfs:Literal` in `m21-csf.ttl` (Optie A masterchat; `rdfs:Literal` omvat `xsd:string` én `rdf:langString`). Baseline-metrics ongewijzigd.
5. **Her-verificatie** (HermiT-her-run v4.6.4 op `output/verification/merged_asserted_v4_6_4.ttl`): **consistent, 0 `owl:Nothing`, geen justificaties**. De 8 v4.6.3-justificaties zijn verdwenen.

**Uitkomst:** eerste empirisch bewijs dat **OWL RL ≡ HermiT voor deze baseline** (na de range-fix). De enige inhoudelijke DL/RL-divergentie die ooit op deze ontologie is aangetroffen, was een *modelleer*-fout (datatype-range), geen aangetoonde OWL RL-*reasoner*-limitatie — relevant voor H37 (versterkt de toolchain-wissel-trigger niet).

## Methodologisch precedent

Dit is het **eerste geval waarin een HermiT-bevinding (DL-zijde) een concrete TBox-fix in de canonieke baseline stuurde**. Het bewijst de waarde van de H38-her-run-discipline: OWL RL bleef de fout missen, juist omdat het datatype-ranges niet streng controleert. De canonieke metrics zijn invariant onder de fix (puur DL-correctheid, geen telmetingswijziging) — een gewenste eigenschap. Geregistreerd als sprint-precedent in [[brain__sprints__v4_6_4_csf-range-fix-dl-conformiteit]].

## Oorspronkelijke vraagstelling (historie — vóór resolutie)

Hieronder de oorspronkelijke H38-formulering, bewaard als context.

## Wat het is

Sinds de modulaire split (v4.0.0) is **geen HermiT-herrun in Protégé uitgevoerd** op de modulaire baseline. Alle reasoning-validatie sindsdien gebeurt via het `owlrl`-Python-package (`DeductiveClosure(OWLRL_Semantics, axiomatic_triples=False, datatype_axioms=False)`).

De aanname dat `owlrl`-package en HermiT op deze ontologie **equivalente inferentie-resultaten** geven is plausibel (de ontologie zit binnen OWL 2 DL en de relevante constructies zijn binnen OWL RL-bereik), maar is **niet aantoonbaar** voor de huidige baseline. Het is een blind-spot, expliciet opgemerkt in het Fase 0 Tech-handover-rapport.

## Waarom dit een open vraag is

Twee redeneerlagen lopen door elkaar:

| Laag | Status | Risico |
|---|---|---|
| **D1 — OWL 2 DL-profiel** | Bewust gekozen (zie [[brain__decisions__D01_owl-2-dl-profiel]]) | Geen — D1 staat OWL 2 DL toe |
| **OWL RL als reasoner-keuze** | Pragmatisch (snelheid + determinisme) | Beperkt: OWL RL is subset van DL; sommige DL-inferenties worden niet gedaan |
| **HermiT als DL-validator** | Niet uitgevoerd sinds v4.0.0 | Hoog: geen empirische bevestiging dat OWL RL geen relevante inferentie mist |

H38 raakt D1 maar wijzigt D1 **niet** — alleen verificatie-actie ontbreekt. Bij significante ontology-groei kan een DL-inferentie opduiken die OWL RL mist en die wel relevant is voor sprint-doel.

## Trigger-criterium

| Trigger | Wanneer HermiT-herrun overwegen |
|---|---|
| Significante ontology-groei | Richtgetal: nieuwe module **of** >10% triple-toename in één sprint |
| DL-conformance-twijfel bij specifieke constructie | Bv. complexe property-chain, qualified cardinality, equivalentClass-cluster die OWL RL niet volledig sluit |
| H37-evaluatie start | Bij overweging van alternatieve reasoner is HermiT-resultaat baseline-referentie |
| 5-jaarlijkse health-check | Indien sinds vorige HermiT-run >2 jaar verstreken: routine-validatie waardevol |

## Aanpak bij activering (toekomst, niet nu)

1. v4.X.Y merged graph laden in Protégé
2. HermiT-reasoner activeren (Protégé default)
3. Inferred axioms exporteren naar TTL
4. Vergelijken met `owlrl`-output (triple-set-diff)
5. Per delta-triple beoordelen: kritiek voor model-semantiek of randverschijnsel?
6. Resultaat als kort verificatie-rapport in `output/reports/owlrl-hermit-vergelijking-v4_X_Y.md`

Verwachte uitkomst: substantiële overlap, kleine delta. Bij grote delta: scope-pauze + masterchat.

## Hangt samen met

- [[brain__decisions__D01_owl-2-dl-profiel]] — D1 staat OWL 2 DL toe; H38 betreft reasoner-keuze binnen D1, niet D1 zelf
- [[brain__concepts__owl-rl-reasoning]] — onderbouwing OWL RL als pragmatisch minimum
- [[brain__architecture__H37_open-ontologies-mcp]] — gerelateerde reasoner-toolchain-vraag (alternatieve DL-reasoner)
- [[brain__sprints__v4_0_0_modulaire-split]] — laatste sprint waarin HermiT-run is bevestigd

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-26 | parked | Geregistreerd in iteratie 12 polish-mini-sprint, oorspronkelijk uit Fase 0 Tech-handover-rapport (`handover-tech-chat-to-subagent-v4_6_0.md`) als methode-blind-spot |
| 2026-05-29 | **resolved** | Empirisch gesloten via reasoner-toolchain-evaluatie (DL-census: 1 materialiseerbaarheids-complete DL-constructie) + HermiT-run v4.6.3 (vond reële divergentie: datatype-range-mismatch, 8 justificaties) + v4.6.4-range-fix (`xsd:string` → `rdfs:Literal`) + HermiT-her-run v4.6.4 (consistent, 0 `owl:Nothing`, geen justificaties). Eerste empirisch bewijs OWL RL ≡ HermiT voor deze baseline. Masterchat-besluit (instructie Brein-cyclus iteratie 16) |

— Einde H38.
