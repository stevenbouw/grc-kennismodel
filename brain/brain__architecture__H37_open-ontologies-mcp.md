---
type: architecture
id: H37
title: H37 — open-ontologies MCP-server als alternatief voor rdflib-toolchain
status: parked
date: 2026-05-26
related:
  - owl-rl-reasoning
  - canonical-metrics
  - H38_owlrl-vs-hermit-equivalentie
  - H41_skos-axioma-set-handling
sources:
  - sessie-rapport-v1_0
  - evaluatie-reasoner-toolchain-h37-h38-h41
chat-sources: []
confidence: medium
---

# H37 — open-ontologies MCP-server als alternatief voor rdflib-toolchain

## Status

**Parked, ongewijzigd** — geregistreerd post-v4.6.0 in polish-mini-sprint (iteratie 12). Trigger: aangetoonde OWL RL-limitatie, of ontology-omvang nadert ~50.000 triples. Desk-evaluatie uitgevoerd 29 mei 2026 (zie hieronder) — oordeel **HOLD**; geen van de vier triggers actief. Status blijft parked.

## Evaluatie-uitkomst (29 mei 2026 — desk-evaluatie, HOLD)

De reasoner-toolchain-evaluatie (`output/reports/evaluatie-reasoner-toolchain-h37-h38-h41.md` §3) toetste H37 als **desk-evaluatie** op de publieke projectpagina (`github.com/fabio-rovai/open-ontologies`) — niet geïnstalleerd, niet geïntegreerd. De scope-pauze-conditie "installatie nodig om te oordelen" deed zich **niet** voor.

**Karakterisering tool (publieke bron):** Rust (edition 2024, single binary, geen JVM) + Oxigraph 0.4 (in-memory, SPARQL 1.1) + native OWL2-DL tableaux (SHOIQ) + OWL-RL + RDFS; MCP-server met 70+ `onto_`-tools; SHACL aanwezig; SKOS-reasoning niet specifiek geclaimd. Volwassenheid **v0.1.11** (25 mrt 2026), 4 releases, **125 ★ / 19 forks, geen 1.0**. Licentie **MIT**. Benchmark-claim o.a. LUBM-reasoning 15 ms vs HermiT 24.490 ms @ 50k axiomas.

**Trigger-herijking (de vier H37-triggers, getoetst):**

| Trigger | Status na evaluatie |
|---|---|
| Concrete OWL RL-limitatie aangetoond | **Niet** — H38-census: enige DL-constructie materialiseerbaarheids-compleet; 0 `owl:Nothing`. De v4.6.4-vondst was een *modelleer*-fout (datatype-range), géén OWL RL-reasoner-limitatie |
| Ontology > ~50.000 triples | **Niet (nadert)** — 44.907 post-OWL-RL; pre-inferentie 20.950. Drempel in zicht, niet bereikt |
| H38 toont substantiële delta | **Niet** — H38 resolved; OWL RL ≡ HermiT na range-fix |
| MCP-ecosystem-volwassenheid (stabiele 1.0) | **Niet** — v0.1.11, geen 1.0, beperkte adoptie (125 ★) |

**Cross-item:** H38 (resolved) ontneemt H37 de "aangetoonde OWL RL-limitatie"-trigger; H41 (hanteerbare, SHACL-neutrale SKOS-impact) ontneemt H37 een SKOS-versterkende trigger. Aanvullende migratie-/black-box-kosten (canonical_metrics_*/shacl_split_*-scripts herschrijven + her-baselinen) tegenover een toolchain die bewezen voldoet. **Geen NO-GO:** technisch serieuze tool; herwaardeer bij (a) >~50k triples, (b) Spoor B-overgang, of (c) een 1.0-release met bredere adoptie. Geen installatie zonder apart masterchat-besluit.

## Wat het is

De vraag of een community-MCP-server voor OWL-ontologieën (kandidaat: [fabio-rovai/open-ontologies](https://github.com/fabio-rovai/open-ontologies) — Rust binary met Oxigraph + tableaux-reasoner) meerwaarde biedt boven de huidige Python-toolchain (`rdflib` + `owlrl` + `pySHACL`).

Specifieke meerwaarde-kandidaten:

| Aspect | Huidige toolchain | open-ontologies-MCP (claim) |
|---|---|---|
| Reasoner | OWL RL (subset van OWL 2 DL) | Tableaux-reasoner (volledige OWL 2 DL) |
| Triplestore | rdflib in-memory | Oxigraph (persistent, SPARQL-Update-capable) |
| Performance | ~8-12s closure op v4.6.0 merged graph | Onbekend; Rust-binary potentieel sneller |
| Protégé-output-integratie | Indirect (Protégé exporteert TTL, rdflib leest) | Onbekend; MCP-interface naar Claude Code |
| Project-fit | Bewezen op v4.0.0-v4.6.0 | Niet getest op deze ontologie |

## Waarom dit een open vraag is

OWL RL is bewust gekozen als pragmatisch reasoning-niveau (zie [[brain__concepts__owl-rl-reasoning]]) — sneller, deterministischer, dekt het overgrote deel van de relevante inferenties. Een sterker reasoner is alleen waardevol bij **aangetoonde** OWL RL-limitatie op deze ontologie. Speculatieve overschakeling zou:

- Nieuwe black-box-laag introduceren (Rust-binary vs Python-package waar we de code kennen)
- Migratie-kosten meebrengen (canonical_metrics-scripts herschrijven)
- Performance-onzekerheid creëren (niet getest op 44.907 post-RL triples)

Niet vervangen op basis van "krachtiger is beter" — eerst evalueren wanneer concrete trigger zich voordoet.

## Trigger-criterium

| Trigger | Wanneer evaluatie starten |
|---|---|
| Concrete OWL RL-limitatie aangetoond | Bv. een geldige DL-inferentie die OWL RL mist en relevante impact heeft op een sprint-doel |
| Ontology overschrijdt ~50.000 triples | Huidig 44.907 post-RL — drempel nadert maar nog niet bereikt. Bij ~50k is performance-evaluatie relevant |
| H38 (HermiT-equivalentie) toont substantiële delta | Indien OWL RL en HermiT op v4.6.0 substantieel afwijken: aanleiding tot derde-reasoner-vergelijking |
| MCP-ecosystem-volwassenheid | Indien open-ontologies-MCP stabiele 1.0-release krijgt met breder gebruik in vergelijkbare projecten |

## Confidence: medium

Het onderwerp is helder (alternatieve toolchain bestaat); de meerwaarde voor dit specifieke project is onbekend zonder evaluatie. Geen claim dat open-ontologies-MCP "beter" is — wel dat het bestaat en evaluatie-waardig is bij relevante trigger.

## Hangt samen met

- [[brain__concepts__owl-rl-reasoning]] — waarom OWL RL het minimum is in huidige toolchain
- [[brain__concepts__canonical-metrics]] — meet-discipline die toolchain-onafhankelijk reproduceerbaar moet zijn
- [[brain__architecture__H38_owlrl-vs-hermit-equivalentie]] — gerelateerde reasoner-vergelijkings-vraag
- `CLAUDE.md` §"Skills-ecosystem-positionering" — Tier 2-evaluatie-kandidaat (post-migratie)

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-26 | parked | Geregistreerd in iteratie 12 polish-mini-sprint, oorspronkelijk uit sessie-rapport v1.0 (post-migratie skills/plugins-roadmap) |
| 2026-05-29 | parked (ongewijzigd) | Desk-evaluatie uitgevoerd (reasoner-toolchain-evaluatie §3): Rust + Oxigraph + tableaux + MCP, MIT, pre-1.0 v0.1.11. Oordeel **HOLD** — geen van 4 triggers actief; 44.907 < 50k; H38 resolved (geen reasoner-limitatie). Trigger-herijking gedocumenteerd. Geen installatie zonder masterchat-besluit |

— Einde H37.
