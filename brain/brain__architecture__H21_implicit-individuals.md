---
type: h-item
id: H21
title: 421 implicit individuals (consistentie-keuze)
status: parked
date: 2026-04-14
related:
  - v4_3_0_gap-sprint-d11
sources:
  - projectinstructie-v1.6
chat-sources:
  - https://claude.ai/chat/f527e7ab-bc17-44f4-a878-598e8ca7a632
confidence: medium
gaps:
  - "Specifieke individuals niet volledig geïnventariseerd"
---

# H21 — 421 implicit individuals

## Status

**Geparkeerd**. Onderdeel van contextdiepte-diagnostiek v4.3.0 (23 bevindingen H1–H23). Consistentie-vraag, geen functioneel probleem.

## Probleem

Het model bevat naar schatting 421 individuals die wel `rdf:type` hebben naar een klasse, maar geen expliciete `owl:NamedIndividual`-declaratie. Onder OWL RL wordt `owl:NamedIndividual` geïnferreerd — geen probleem voor reasoning. Wel inconsistent met de praktijk van expliciete declaratie zoals toegepast op recente subjects (bv. 15 `compl:REQ_NIS2_*`-individuals in v4.3.3).

## Drie opties

- **Optie A — niets doen.** OWL RL infereert het. Tellingen kunnen gebruiken `len(set(g.subjects(RDF.type, OWL.NamedIndividual)))` post-inferentie. Acceptabel maar betekent dat pre-inference NamedIndividual-count lager is dan post-inference.
- **Optie B — alle 421 expliciet maken.** Consistent met v4.3.3-precedent. Eenmalige bulk-toevoeging, daarna geldt regel "elke nieuwe individual krijgt expliciete declaratie".
- **Optie C — selectief expliciet maken.** Alleen individuals die conceptueel "named" zijn (bv. controls, frameworks), niet voor systematische resultaten (bv. risico-instances die mogelijk dynamisch gegenereerd worden).

## Waarom geparkeerd

Geen blocker. Triggers voor herziening:

- Wanneer pre-inference parsing in externe tooling (Protégé-export, dashboard) inconsistenties oplevert
- Wanneer canonical metrics-discrepantie tussen pre/post-inference NamedIndividual-count verklaring vereist
- Wanneer SHACL-shape over volledige NamedIndividual-set wordt geschreven

In v4.3.3 is **NamedIndividual-telmethode formeel geformaliseerd:** canonical_metrics-JSON als enige autoritatieve bron, telmethode gedocumenteerd. Dit lost de praktische meet-issue op, maar het architecturale principe blijft open.

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-04-13 | open | Gevonden bij contextdiepte-diagnostiek v4.3.0 |
| 2026-04-14 | parked | Niet-blokkerend, telmethode geformaliseerd in v4.3.3 als praktische workaround |

— Einde H21.
