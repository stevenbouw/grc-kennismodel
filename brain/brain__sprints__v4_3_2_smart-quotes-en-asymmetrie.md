---
type: sprint
id: v4.3.2
title: v4.3.2 — smart quotes + NIS2Requirement-asymmetrie
status: superseded
date: 2026-04-21
related:
  - v4_3_1_patch-bump
  - v4_3_3_d12-en-predicate-consolidatie
sources: []
chat-sources:
  - https://claude.ai/chat/7ec4a4dc-7230-4135-96f4-c791e7271656
confidence: medium
gaps:
  - "Exacte datum onbekend; tussen v4.3.1 (20 april) en v4.3.3 (22 april) — vermoedelijk 21 april"
  - "Geen apart patch-rapport in project knowledge — reconstructie uit userMemories en grc-core-history-comments"
---

# v4.3.2 — smart quotes + NIS2Requirement-asymmetrie

## Status

**Medium reconstructie** uit userMemories en `grc-core.ttl` history-comments (zoals geciteerd in tech-chat 13 mei 2026).

## Scope: drie items

### Item 1 — Smart quotes vervangen door ASCII

Twee subjects in `m02-control.ttl` gebruikten typografische smart quotes (U+2018/U+2019, gedetecteerd tijdens v4.3.1 Besluit A bij labelextractie maar daar verbatim overgenomen):

- `ctrl:ISO27002_7_07`
- `ctrl:ISO27002_8_01`

Vervangen door ASCII apostrof (U+0027). **D5-brug-completion vereist:** spiegels in `isms:SoAEntry_7_07` + `_8_01` (m06) én via D5 sameAs-brug `bio:ISO27002_7_07` + `_8_01` (m08) ook gecorrigeerd. Anders zou OWL RL-reasoning duplicaten ontdekken (twee verschillende strings voor dezelfde sameAs-equivalente individuals).

**Totaal:** 10 triples gewijzigd. **Netto delta: 0** (vervangingen, geen toevoegingen).

### Item 2 — `ext:NIS2Requirement`-klasse asymmetrie hersteld

Patroon-completion: bestaande classen `ext:DORARequirement`, `ext:ISMSRequirement`, `ext:BCMRequirement` waren al subklasse van `compl:ComplianceRequirement`. NIS2 ontbrak.

**Uitgevoerd:**

- Klasse `ext:NIS2Requirement` toegevoegd aan `grc-core.ttl` (subClassOf `compl:ComplianceRequirement`)
- 21 NIS2-subjects geretypeerd: 6 in `m10-nis2-ext.ttl` + 15 in `m05-compliance.ttl`

**Klassen-count:** 185 → **186**.

Voorbereiding voor [[brain__decisions__D12_drie-laags-compliance]] dat in v4.3.3 wordt geformaliseerd.

### Item 3 — §10.2-meetcorrectie (administratief)

SPARQL-verificatie 0 hits op "556" in model-annotaties; projectinstructie v1.5 bevat canonieke waarde **973** (`asset:appliesToAssetType` inferred). Geen model-wijziging — alleen documentatie-correctie.

## Eindstaat v4.3.2

- owl:Class: 185 → **186** (+1)
- NamedIndividual: 615 → 622 (rondom v4.3.2 — exacte delta-allocatie tussen sprints onduidelijk)
- 0 net-delta op smart quotes (vervangingen)
- 0 inconsistenties, gesplitste SHACL groen

## Wat onbekend is

- Of er nog een Item 4 of 5 was die niet in userMemories of grc-core-history is doorgekomen
- Mogelijk ook andere kleine cleanup-items meegelift via D6

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| ±2026-04-21 | active | v4.3.2 oplevering |
| 2026-04-22 | superseded | Opgevolgd door v4.3.3 |

— Einde v4.3.2.
