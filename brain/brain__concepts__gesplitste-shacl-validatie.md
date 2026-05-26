---
type: concept
title: Gesplitste SHACL-validatie
status: living
date: 2026-05-13
related:
  - sameAs-discipline
  - owl-rl-reasoning
  - D05_sameAs-strikt-ctrl-bio
  - D11_sameAs-asset-convergentie
sources:
  - opleveringsrapportage-m18-v4_2_0
  - patch-rapport-v4_3_0
chat-sources: []
confidence: high
---

# Gesplitste SHACL-validatie

## Wat het is

SHACL-shapes worden in het GRC Kennismodel **in twee secties** gevalideerd, elk met een andere inferentie-modus:

| Sectie | Modus | Inhoud | Shapes (huidige staat) |
|---|---|---|---:|
| **SECTIE A** | `inference='none'` (pre-inferentie) | Naming/uniciteit-shapes die de geschreven IRIs controleren | 4 |
| **SECTIE B** | `inference='owlrl'` (post-inferentie) | Semantische shapes die afgeleide content valideren | 3 |

Gecombineerde validatie (één modus voor beide secties) levert **290 false-positives** op SECTIE A-shapes. Gesplitste validatie levert **0 violations** in beide secties.

## Waarom gesplitst nodig is

Het probleem ontstaat door **owl:sameAs-propagatie onder OWL RL**:

1. D5 (93 ctrl:↔bio: bruggen) propageert: `ctrl:ISO27002_5_01` krijgt automatisch het bio-IRI als alternatieve naam.
2. D11 (5 asset:↔risk:/isms: bruggen) propageert: namespace-membership wordt onder inferentie cross-namespace zichtbaar.

Bij gecombineerde modus controleert SHACL pattern-shapes (bv. `ctrl:ISO27002NamingShape`) op alle leden van `ctrl:Control` — inclusief de via sameAs geïnferreerde `bio:`-leden die niet voldoen aan het `ctrl:`-pattern. **186 false-positives onder D5 alleen, 290 onder D5 + D11.**

Pre-inferentie zien deze shapes alleen de werkelijk geschreven IRIs en valideren correct (0 violations).

## Welke shapes waar?

**SECTIE A (pre-inferentie, `inference='none'`):**

- `ctrl:ISO27002NamingShape` — pattern bewaakt geschreven ctrl:-IRIs
- `bio:ISO27002NamingShape` — pattern bewaakt geschreven bio:-IRIs
- `ctrl:HandreikingBBNValueShape` — waardenbereik 1/2 op `ext:hasHandreikingBBN`
- `asset:NamespaceShape` (verplaatst SECTIE B → A in v4.3.0 wegens D11)

**SECTIE B (post-inferentie, `inference='owlrl', advanced=True`):**

- `asset:AppliesToAssetTypeRangeShape` (M18-1)
- `asset:BVASymmetryShape` (M18-3)
- `asset:OrphanClassShape` (M18-4)

Eerder M18-2 (`asset:NamespaceShape`) zat in SECTIE B; verplaatst naar A in v4.3.0 wegens D11-sameAs-propagatie.

## Canonieke invocatie

Verplicht bij elke release via `shacl_split_validate_v[versie].py`:

```python
from pyshacl import validate

# RUN 1 — SECTIE A
conforms_A, _, _ = validate(
    data_graph=g,
    shacl_graph=g_shapes_A,
    inference='none',
    allow_warnings=False
)

# RUN 2 — SECTIE B
conforms_B, _, _ = validate(
    data_graph=g,
    shacl_graph=g_shapes_B,
    inference='owlrl',
    advanced=True,
    allow_warnings=False
)
```

Uitkomst-verwachting:

- **RUN 1:** 0 violations
- **RUN 2:** 0 violations (los van bekende 290 false-positives wanneer SECTIE A-shapes per ongeluk in RUN 2 zouden draaien)

## Praktische waarschuwing

Wanneer een nieuwe SHACL-shape wordt toegevoegd, moet **vooraf** worden bepaald in welke sectie hij hoort. Trigger-criteria:

- **Sectie A:** als de shape de **letterlijk geschreven** IRI-structuur, naming, of literal-waarden controleert
- **Sectie B:** als de shape op **semantische relaties** controleert die uit reasoning volgen (subclass-membership, property-instances)

Bij twijfel: voorkeur Sectie A. Een shape die per ongeluk in B zit terwijl hij in A hoort, produceert false-positives. Andersom werkt soms wel maar mist mogelijk inferentie-relaties.

## Hangt samen met

- [[brain__concepts__sameAs-discipline]] — directe oorzaak van de noodzaak tot splitsing
- [[brain__concepts__owl-rl-reasoning]] — reasoning-modus
- [[brain__concepts__canonical-metrics]] — gesplitste SHACL is onderdeel van canonieke meetmethode

— Einde gesplitste SHACL-validatie.
