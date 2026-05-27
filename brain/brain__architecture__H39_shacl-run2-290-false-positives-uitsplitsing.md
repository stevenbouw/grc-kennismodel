---
type: architecture
id: H39
title: H39 — 290 SHACL RUN 2 false-positives niet individueel uitgesplitst per violation
status: parked
date: 2026-05-27
related:
  - gesplitste-shacl-validatie
  - sameAs-discipline
  - T1_skos-kwaliteitsanalyse-fase-1
  - T2-skos-bidirectional-audit-m10
sources:
  - handover-tech-chat-to-subagent-v4_6_0
  - t1-presprint-inventarisatie-v4_6_0
  - t1-eindrapport-v4_6_1
  - patch-rapport-v4_6_2
chat-sources: []
confidence: high
---

# H39 — 290 SHACL RUN 2 false-positives niet individueel uitgesplitst

## Status

**Parked** — geregistreerd post-v4.6.0 in polish-mini-sprint (iteratie 12). Trigger: rustige sprint als sanity-check, of sprint die SHACL-shapes wijzigt.

**Versterking T1 (26 mei 2026):** T1-pre-sprint-inventarisatie Vraag D bevestigde **SHACL-blinde vlek op alle 28 ctrl:↔compl:-paren** uit H36-cluster — geen enkele shape valideerde op deze relaties. Predicate-mutatie in patch v4.6.1 (28× `exactMatch` → `broadMatch`) raakte daarom geen shape; RUN 1/RUN 2 identiek aan v4.6.0-baseline. Zie [[brain__sprints__T1_skos-kwaliteitsanalyse-fase-1]] en T1-pre-sprint-inventarisatie Vraag D.

**Versterking T2 (27 mei 2026):** T2-sprint bevestigt SHACL-blinde-vlek op **118-paren-schaal**. Per patch-rapport v4.6.2 §7.3:

> *"Geen shape in `ontology/grc-shacl.ttl` valideert direct op ctrl:↔compl:-mapping-distributie. De 65 SKOS-predicate-substituties raken daarom geen shape — SHACL-uitkomsten zijn structureel ongevoelig voor T2-mutaties. H39 (SHACL-blinde vlek) blijft active geparkeerd voor latere shape-uitbreiding indien gewenst."*

Driemetingen (per patch-rapport v4.6.2 §7.1): SECTIE A = 0, SECTIE B = 0, COMBINED = 290 — Δ = 0 vs v4.6.1-baseline. De 65 mutaties bevestigen empirisch dat SHACL-shapes structureel geen ctrl:↔compl:-mapping-distributie valideren. Trigger-relevantie verder verhoogd (eerder bij T1: 28-paren-schaal; nu bij T2: 118-paren-schaal). Zie [[brain__sprints__T2-skos-bidirectional-audit-m10]] en patch-rapport v4.6.2 §7.

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
| 2026-05-26 | parked (versterkt) | T1-pre-sprint-inventarisatie Vraag D bevestigt SHACL-blinde vlek op 28 ctrl:↔compl:-paren — predicate-mutatie raakt geen shape. Trigger-relevantie verhoogd voor T2 |
| 2026-05-27 | parked (versterkt T2) | T2-sprint bevestigt SHACL-blinde-vlek op 118-paren-schaal (per patch-rapport v4.6.2 §7.3). 65 SKOS-predicate-mutaties → Δ SHACL = 0 in alle drie metingen (SECTIE A / B / COMBINED). Trigger-relevantie verder verhoogd |

— Einde H39.
