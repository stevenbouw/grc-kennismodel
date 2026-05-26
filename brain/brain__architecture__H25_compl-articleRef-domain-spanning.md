---
type: h-item
id: H25
title: D12 + compl:articleRef-domain-spanning
status: open
date: 2026-04-22
related:
  - D12_drie-laags-compliance
  - H27_gamma-migratie-articleIdentifier
  - v4_3_3_d12-en-predicate-consolidatie
sources:
  - patch-rapport-v4_3_3
  - projectinstructie-v1.6
chat-sources:
  - https://claude.ai/chat/7ec4a4dc-7230-4135-96f4-c791e7271656
confidence: high
---

# H25 — D12 + compl:articleRef-domain-spanning

## Status

**Open architectuur-vraag** post-v4.3.3. Semantisch grijze zone tussen Obligation-tak en ComplianceRequirement-tak van [[brain__decisions__D12_drie-laags-compliance]].

## Probleem

`compl:articleRef` heeft `rdfs:domain compl:Obligation`. Onder OWL RL propageert dit op alle 51 articleRef-dragers, **inclusief 20 ComplianceRequirement-subjects** (6 NIS2 + 14 DORA).

Per D12 zijn `compl:Obligation` (laag 1+2) en `compl:ComplianceRequirement` (laag 3) verschillende concepten. De `articleRef`-property hoort architectureel bij beide lagen (een eis verwijst naar een artikel, een verplichting verwijst naar een artikel), maar de domain-declaratie forceert via inferentie dat ComplianceRequirements ook Obligations zijn.

**Stap 3d v4.3.3 (proof-of-non-clash):** verificatie via bestaande `NIS2_Art21_a`-precedent toonde geen disjointness-clash. Dus geen OWL-inconsistentie. Maar wel semantisch onzuiver.

## Twee opties bij architectuurbeslissing

**Optie 1 — Domain-versoepeling:**

```turtle
compl:articleRef rdfs:domain [
  owl:unionOf ( compl:Obligation compl:ComplianceRequirement )
] .
```

Voordeel: domain wordt expressief, geen ongewenste inferentie meer. Nadeel: union-domain is een meer complexe OWL-constructie; lichte readability-impact.

**Optie 2 — γ-migratie naar `compl:articleIdentifier` (zonder restrictieve domain):**

Vervangt `compl:articleRef` door `compl:articleIdentifier` met geen domain-restrictie (of `xsd:string` als data property zonder domain). Zie [[brain__architecture__H27_gamma-migratie-articleIdentifier]].

## Hangt samen met

Als H27 wordt uitgevoerd vervalt H25 — `articleIdentifier` heeft geen domain-clash. Beslissing-volgorde:

1. Eerst beslissen of H27 wordt uitgevoerd (op basis van trigger-criteria, niet pre-emptief)
2. Als H27 nee: dan H25 Optie 1 (domain-versoepeling)
3. Als H27 ja: dan vervalt H25

## Waarom open

Geen blocker voor v4.4.0. Mogelijk eerst kijken of CBW/Cbb-uitbouw (Fase 2) extra articleRef-uses op `LegalObligation`-subjects toevoegt, voor breder beeld.

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-04-22 | open | Geïdentificeerd tijdens v4.3.3-uitvoering (Stap 3d verificatie) |

— Einde H25.
