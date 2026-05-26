---
type: architecture
id: H39
title: H39 — 290 SHACL RUN 2 false-positives niet individueel uitgesplitst per violation
status: parked
date: 2026-05-26
related:
  - gesplitste-shacl-validatie
  - sameAs-discipline
sources:
  - handover-tech-chat-to-subagent-v4_6_0
chat-sources: []
confidence: high
---

# H39 — 290 SHACL RUN 2 false-positives niet individueel uitgesplitst

## Status

**Parked** — geregistreerd post-v4.6.0 in polish-mini-sprint (iteratie 12). Trigger: rustige sprint als sanity-check, of sprint die SHACL-shapes wijzigt.

## Wat het is

Sinds v4.3.0 wordt het RUN 2-resultaat van de gesplitste SHACL-validatie ([[brain__concepts__gesplitste-shacl-validatie]]) gerapporteerd als **"290 false-positives onder `inference='owlrl'`"**. Dit cijfer is consistent over v4.3.0 → v4.4.0 → v4.5.0 → v4.6.0 en wordt geclassificeerd als bekende false-positives op basis van **shape-categorie-analyse**.

Een **individuele uitsplitsing** (welke 290 specifieke triples, welke shape-IRIs, hoe verdeeld over shape-categorieën) is echter **nooit gemaakt**. De classificatie steunt op categorie-redenering, niet op per-violation-bewijs.

## Waarom dit een open vraag is

Het risico is dat een **nieuwe echte violation** zou kunnen verdwijnen in de 290-aanname:

| Scenario | Risico-omvang |
|---|---|
| 290 blijft 290 bij sprint-toevoeging | Geen probleem — categorie-stabiel |
| 290 → 291 bij sprint-toevoeging | Bekend probleem detecteerbaar (delta zichtbaar in SHACL-output) |
| 290 → 290 bij sprint die SHACL-shapes wijzigt | **Onzichtbaar risico** — één echte violation kan één eerdere false-positive verdringen, getal blijft 290, masking treedt op |
| Externe SHACL-audit vraagt per-violation-verdediging | Geen documentatie beschikbaar; ad-hoc uitsplitsing onder tijdsdruk |

Het derde scenario is de eigenlijke driver — bij sprints die shapes raken (toevoegen, wijzigen, verwijderen) kan de getal-stabiliteit een vals gevoel van veiligheid geven.

## Trigger-criterium

| Trigger | Wanneer per-violation-uitsplitsing maken |
|---|---|
| Rustige sprint als sanity-check | Bv. tussen twee inhoudelijke sprints — eenmalige baseline-documentatie |
| Sprint die SHACL-shapes wijzigt | **Verplicht** — eerst baseline-uitsplitsing van huidige 290, dan shape-wijziging, dan re-validatie + delta-analyse |
| Externe SHACL-audit aangekondigd | Per-violation-verdediging vooraf opstellen |
| 290 → ander getal zonder verklaarbare oorzaak | Onmiddellijke uitsplitsing voor reconciliatie |

## Aanpak bij activering (toekomst, niet nu)

1. SHACL RUN 2 draaien met verbose output (per-violation IRIs)
2. Per violation: shape-IRI + focus-node + path + value extractie
3. Aggregeren per shape-categorie: hoeveel violations uit welke shape
4. Per categorie verdedigen waarom het een false-positive is (verwijzing naar OWL RL-inferentie-pad)
5. Resultaat als `output/reports/shacl-run2-uitsplitsing-v4_X_Y.md` met 290 rijen + shape-categorie-samenvatting
6. Toekomstige sprints vergelijken delta-violations met deze baseline

## Hangt samen met

- [[brain__concepts__gesplitste-shacl-validatie]] — SECTIE A vs SECTIE B, 290 false-positives onder combined
- [[brain__concepts__sameAs-discipline]] — owl:sameAs-propagatie onder OWL RL is een belangrijke false-positive-bron
- [[brain__workflow__opleveringsprotocol]] — verplichte SHACL-artefacten per release
- [[brain__sprints__v4_3_0_gap-sprint-d11]] — sprint waarin gesplitste-SHACL is geformaliseerd

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-26 | parked | Geregistreerd in iteratie 12 polish-mini-sprint, oorspronkelijk uit Fase 0 Tech-handover-rapport als methode-blind-spot sinds v4.3.0 |

— Einde H39.
