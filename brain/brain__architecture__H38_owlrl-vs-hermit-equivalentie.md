---
type: architecture
id: H38
title: H38 — OWL RL (owlrl-package) vs HermiT (Protégé) equivalentie niet geverifieerd sinds v4.0.0
status: parked
date: 2026-05-26
related:
  - D01_owl-2-dl-profiel
  - owl-rl-reasoning
  - H37_open-ontologies-mcp
sources:
  - handover-tech-chat-to-subagent-v4_6_0
chat-sources: []
confidence: high
---

# H38 — OWL RL vs HermiT equivalentie niet geverifieerd sinds v4.0.0

## Status

**Parked** — geregistreerd post-v4.6.0 in polish-mini-sprint (iteratie 12). Trigger: significante ontology-groei of DL-conformance-twijfel bij specifieke constructie.

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

— Einde H38.
