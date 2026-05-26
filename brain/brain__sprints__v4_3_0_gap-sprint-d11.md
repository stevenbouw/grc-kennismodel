---
type: sprint
id: v4.3.0
title: v4.3.0 — gap-sprint G1/G2/G4/G5 + D11
status: superseded
date: 2026-04-13
related:
  - v4_2_2_soa-canonisering-route-a
  - v4_3_1_patch-bump
  - D11_sameAs-asset-convergentie
sources:
  - patch-rapport-v4_3_0
chat-sources:
  - https://claude.ai/chat/f527e7ab-bc17-44f4-a878-598e8ca7a632
confidence: high
---

# v4.3.0 — gap-sprint G1/G2/G4/G5 + D11

## Status

**Rijke reconstructie** uit `patch-rapport-v4_3_0.md` (13 april 2026, niet 14 april zoals aanvankelijk gedacht — patch-rapport-datum is leidend).

## Aanleiding: risk-coupling nulmeting v4.2.1

Risk-coupling nulmeting identificeerde **2 structurele gaten + 3 kleinere items**:

| Gap | Inhoud |
|---|---|
| **G1** | asset:↔risk: ontbrekende brug — geen owl:sameAs tussen parallelle asset-klassen |
| **G2** | Geen directe `SoAEntry → Risk` property — alleen via control-relaties |
| **G4** | Risk-taxonomie miste `ReportingRisk` (financial reporting context) |
| **G5** | `risk:Impact` had geen Engelse `Consequence`-altLabel (ISO 27005:2024 conformiteit) |

Masterchat besloot gerichte gap-sprint.

## G1 — Asset-convergentie via owl:sameAs (D11 formeel)

**Equivalentie-matrix** geanalyseerd op 8 parallelle asset-klassen. **5 bruggen toegevoegd**, **4 relaties bewust niet gebrugd**.

### Toegevoegde 5 bruggen (ster-patroon met asset: als centrum)

```turtle
asset:Asset            owl:sameAs risk:Asset .
asset:InformationAsset owl:sameAs risk:InformationAsset .
asset:InformationAsset owl:sameAs isms:InformationAsset .
asset:HumanAsset       owl:sameAs risk:HumanAsset .
asset:PhysicalAsset    owl:sameAs risk:PhysicalAsset .
```

### Niet-gebrugd (4 open masterchat-vragen)

| # | Bron-klasse | Reden niet-brug |
|---|---|---|
| 5 | `asset:InformationSystem` ↔ `risk:SystemAsset` | risk: is breder (incl. ICT-dienst) |
| 6 | `risk:ServiceAsset` | Geen M18-equivalent |
| 7 | `isms:PrimaryAsset` | Overlapt meerdere asset:*-klassen (Information, Process) |
| 8 | `isms:SupportingAsset` | Overlapt Human, Physical, Software, Facility tegelijk |

D11 formeel vastgelegd in [[brain__decisions__D11_sameAs-asset-convergentie]]. Plaats: nieuwe sectie in `grc-bridges.ttl` onder de bestaande 93 D5-bruggen.

### Semantische winst — Query Q1 bewijs

| Modus | Resultaten |
|---|---:|
| Pre-inference | 0 |
| Post-OWL RL inference | 11 |

Zonder D11 was er geen semantische overlap; met D11 propageren D11-targets via owl:sameAs.

## G2 — `isms:forRisk` ObjectProperty

Toegevoegd aan `m06-isms.ttl`. Maakt directe SoAEntry → Risk-koppeling mogelijk (optioneel, 0..*).

## G4 (Optie B) — `risk:ReportingRisk` + AllDisjointClasses 4→5

Nieuwe klasse `risk:ReportingRisk` toegevoegd aan `m03-risk.ttl`. Opgenomen in `owl:AllDisjointClasses` — uitbreiding 4 → 5 leden.

**Optie B** gekozen boven Optie A (subclass-only) om disjointness-consistentie te behouden.

## G5 — `skos:altLabel "Consequence"@en` op `risk:Impact`

ISO 27005:2024 introduceerde "consequence" als equivalent voor "impact". Eén SKOS-mapping toegevoegd.

## SHAPE Optie A — `asset:NamespaceShape` verplaatst SECTIE B → A

D11 introduceert owl:sameAs-propagatie naar `asset:NamespaceShape`. Onder OWL RL leverde dit false-positive violations. Oplossing: shape verplaatsen naar SECTIE A (`inference='none'`) — analoog aan eerder D5-precedent voor `ctrl:`/`bio:`-NamingShapes.

**Combined-modus false-positives:** 186 (D5 alleen) → **290** (D5 + D11) — een logisch gevolg, niet een nieuw probleem.

## Drie masterchat-scope-besluiten tijdens uitvoering

- **G4 Optie B** — disjointness-uitbreiding voor nieuwe subklasse
- **D6 Optie A** — meeliftregel scope-conform aan bevinding B
- **SHAPE Optie A** — NamespaceShape SECTIE B → A wegens sameAs-propagatie
- **G1 niet-gelegde bruggen** — bij twijfel niet leggen (4 bewust open gelaten)

## Contextdiepte-diagnostiek

Bij v4.3.0-oplevering tegelijk: contextdiepte-diagnostiek met **23 bevindingen H1–H23**. Eerste momentum voor H-register als parallel-werkstroom naast D-register.

## Canonieke meetmethode

Vanaf v4.3.0 verplicht bij elke release:

- `canonical_metrics_v[versie].py` met OWL RL settings: `axiomatic_triples=False`, `datatype_axioms=False`
- `shacl_split_validate_v[versie].py` met RUN 1 (pre) + RUN 2 (post)
- Patch-rapport bevat baseline-vergelijking met vorige versie

## Net-delta

**+27 triples** pre-inferentie. **+5 owl:sameAs**, +1 ObjectProperty, +1 klasse, +1 SKOS-altLabel.

## Eindstaat v4.3.0

- Vijf bestanden gewijzigd: `grc-core.ttl`, `grc-bridges.ttl`, `m03-risk.ttl`, `m06-isms.ttl`, `grc-shacl.ttl`
- Alle zes invariantie-metrics buiten doel-deltas identiek
- Gesplitste SHACL: SECTIE A = 0, SECTIE B = 0 ✓

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-04-13 | active | v4.3.0 oplevering met D11 |
| 2026-04-20 | superseded | Opgevolgd door v4.3.1 patch-bump |

— Einde v4.3.0.
