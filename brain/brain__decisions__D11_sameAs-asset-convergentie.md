---
type: decision
id: D11
title: owl:sameAs asset-convergentie (ster-patroon)
status: active
date: 2026-04-13
related:
  - D05_sameAs-strikt-ctrl-bio
  - D09_framework-neutraliteit
sources:
  - projectinstructie-v1.6
  - patch-rapport-v4_3_0
chat-sources:
  - https://claude.ai/chat/f527e7ab-bc17-44f4-a878-598e8ca7a632
confidence: high
---

# D11 — owl:sameAs asset-convergentie (ster-patroon)

## Beslissing

Asset-klassen uit drie namespaces worden gebrugd via **`owl:sameAs`** in een **ster-patroon** met `asset:` als canoniek centrum.

| # | Bridge | Bron-klasse | Doel-klasse |
|---|---|---|---|
| 1 | Top-level | `asset:Asset` | `risk:Asset` |
| 2 | Informatie (risk) | `asset:InformationAsset` | `risk:InformationAsset` |
| 3 | Informatie (isms) | `asset:InformationAsset` | `isms:InformationAsset` |
| 4 | Personeel | `asset:HumanAsset` | `risk:HumanAsset` |
| 5 | Fysiek | `asset:PhysicalAsset` | `risk:PhysicalAsset` |

**5 bruggen totaal.** Drie potentiële relaties bewust niet gebrugd (open masterchat-vragen — zie afgeleide consequenties), plus één relatie zonder M18-equivalent (`risk:ServiceAsset`).

## Aanleiding

In v4.2.x bestonden asset-concepten parallel in M03 (risk), M06 (isms) en M18 (asset). SPARQL-queries die "alle informatie-assets" zochten, vonden alleen `asset:InformationAsset`-leden, niet de `risk:`- of `isms:`-tegenhangers. Dit ondermijnde de framework-neutraliteit van [[brain__decisions__D09_framework-neutraliteit]] op asset-niveau.

D11 brugt de vijf evidente klasse-equivalenties; resterende cases worden bewust níet gebrugd om over-koppeling te voorkomen.

## Implementatie

```turtle
asset:Asset            owl:sameAs risk:Asset .
asset:InformationAsset owl:sameAs risk:InformationAsset .
asset:InformationAsset owl:sameAs isms:InformationAsset .
asset:HumanAsset       owl:sameAs risk:HumanAsset .
asset:PhysicalAsset    owl:sameAs risk:PhysicalAsset .
```

- Asserties in `grc-bridges.ttl` (gecentraliseerd, naast D5)
- Onder OWL RL propageert dit naar 98 `isms:InformationAsset`-leden (concrete instance-impact)
- Pure RDFS-inferentie is onvoldoende — D11-propagatie blijft dan onzichtbaar
- Pre-inference Query Q1 (Risk → asset via asset:Asset-klasse): 0 hits. Post-OWL RL: 11 hits.

## SHACL-impact (afgeleide consequentie)

- `asset:NamespaceShape` moest verplaatst van SECTIE B → SECTIE A (inference='none') wegens sameAs-propagatie — analoog aan D5-precedent voor `ctrl:`/`bio:`-NamingShapes
- False-positives onder gecombineerde SHACL-modus stegen van 186 (D5 alleen) naar 290 (D5 + D11)
- Validatie in SECTIE A en SECTIE B beide leveren 0 violations onder correcte modus

## Niet-gelegde bruggen (open masterchat-vragen)

Vier potentiële bruggen bewust níet gelegd:

| # | Relatie | Reden niet-brug |
|---|---|---|
| 5 (in v4.3.0 telling) | `asset:InformationSystem` ↔ `risk:SystemAsset` | `risk:SystemAsset` is breder: informatiesysteem, applicatie, infrastructuurcomponent OF ICT-dienst. `asset:InformationSystem` strikt samengesteld per CIO-stelsel 2026 art. 1o. SameAs zou applicaties/diensten forceren tot samengestelde systemen. |
| 6 | `risk:ServiceAsset` | Geen M18-equivalent (`asset:Service` bestaat niet) |
| 7 | `isms:PrimaryAsset` | Overlapt meerdere `asset:`-klassen (Information, Process), niet 1-op-1 |
| 8 | `isms:SupportingAsset` | Overlapt Human, Physical, Software, Facility tegelijk |

## Wat het niet betekent

- D11 betekent niet dat álle parallelle klassen in alle namespaces moeten worden gebrugd — alleen waar identiteit semantisch klopt
- D11 betekent niet dat de drie namespaces (`asset:`, `risk:`, `isms:`) worden gemerged — ze blijven scheiden, alleen specifieke klassen worden geïdentificeerd
- D11 betekent niet uitbreiding naar `ctrl:`↔`bio:`-stijl ABox-bruggen — D11 is klasse-niveau, D5 is instance-niveau

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-04-13 | active | Vaststelling in v4.3.0 G1-sprint |

## Correctie-note

Eerdere versie van deze file (iteratie 1) bevatte foutieve bridge-tabel met `asset:Personnel`-en `asset:Process`-bruggen. Gecorrigeerd op basis van primaire bron `patch-rapport-v4_3_0.md` §1.2 in iteratie 3.

— Einde D11.
