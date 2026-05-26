---
type: workflow
title: Scope-discipline — Optie A/B/C-protocol
status: living
date: 2026-05-13
related:
  - masterchat-interactie
  - opleveringsprotocol
sources:
  - projectinstructie-v1.6
chat-sources: []
confidence: high
---

# Scope-discipline — Optie A/B/C-protocol

## Principe

**Scope-afwijkingen altijd melden, nooit zelf interpreteren.** Een van de belangrijkste leerpunten uit de v4.2.2 → v4.3.3 sprint-cyclus. Geld voor tech-chat én voor specialistische chats — bij onverwachte scope-impact: pauze + rapporteer + wacht op GO.

## Pauzeer-trigger-categorieën

Vier patronen die directe pauze rechtvaardigen:

| Trigger | Voorbeeld |
|---|---|
| **Inventaris-discrepantie** | Instructie-verwachting matcht niet met werkelijkheid (bv. v4.3.3 §3.3 verwachtte 0 articleNumber-uses buiten m10; werkelijkheid 14 in m12) |
| **Onbekende scope-uitbreiding** | Nieuwe entiteiten of relaties die verder gaan dan instructie |
| **Architectuur-aanrakingspunt** | Mogelijke D-beslissing-impact niet expliciet in instructie |
| **Telling-discrepantie** | Observed vs. expected significant verschillend |

## Pauzeer-protocol — vier stappen

1. **Pauzeren vóór wijziging** — geen edits, geen voor-uit-werk "ik denk dat..."
2. **Rapporteren aan Master** met opties (A/B/C) en korte voor/tegen per optie
3. **Wachten op GO** — geen vooruitlopen
4. **Uitvoeren + documenteren** in opleveringsrapport / patch-rapport

## Optie A/B/C-format

Structurele rapportage met **2-3 opties** (niet meer; keuze-overload vermijden):

```
## Scope-pauze: <onderwerp>

**Wat ik observeer:** <feitelijke waarneming, met getallen>

**Wat instructie zei:** <citaat instructie>

**Voorgestelde opties:**

- **Optie A:** <minste verandering> 
  - Voor: <pluspunten>
  - Tegen: <minpunten>
  - Triple-impact: <getal>
  
- **Optie B:** <middenweg>
  - Voor / Tegen / Triple-impact
  
- **Optie C:** <grootste verandering, scope-creep>
  - Voor / Tegen / Triple-impact

**Mijn voorkeur:** <optie + 1-zin-motivatie>
**Wacht op GO van Master.**
```

## Gedocumenteerde scope-besluiten

Voorbeelden uit recente sprints (allemaal correct gepauzeerd):

| # | Sprint | Scope-pauze | Master-keuze |
|---|---|---|---|
| 1 | v4.2.2 | G9 canoniseringsspiegel (108 SoAEntry vs 93) | Route A — canoniseren naar 93 |
| 2 | v4.3.0 | G4 disjointness-uitbreiding | Optie B — incl. nieuwe ReportingRisk |
| 3 | v4.3.0 | D6 meeliftregel scope-grens | Optie A — edit-scope, niet bestand-scope |
| 4 | v4.3.0 | SHAPE-modus voor asset:NamespaceShape | Optie A — SECTIE B → A |
| 5 | v4.3.0 | G1 niet-gelegde D11-bruggen | Bij twijfel niet leggen — 4 bewust open |
| 6 | v4.3.1 | H18 IRI-afwijking + nieuwe klasse | Optie 1A/2B + scope-completion |
| 7 | v4.3.1 | B₂ — oude SoAEntry-labels behouden of vervangen | Vervangen i.p.v. toevoegen |
| 8 | Analyse 1.0 | Cbb-concept scope-uitbreiding | Keurig gemarkeerd, GO masterchat |
| 9 | v4.3.3 | Item 3 — DORA-scope-uitbreiding (20 uses vs 6 verwacht) | Optie A — D9-symmetrie |
| 10 | v4.3.3 | Stap 3d compl:articleRef-domain-verificatie | GROEN via proof-of-non-clash; doorgeschoven naar H25 |

## Wat scope-discipline NIET is

- **Niet:** elke kleine afwijking pauzeren. Bv. typo-fixes binnen edit-scope mag direct.
- **Niet:** wachten op GO bij voor-zichzelf-duidelijke voorkeuren. Maar bij voor-zichzelf-onduidelijk: liever wel pauzeren.
- **Niet:** drie opties verzinnen waar er maar twee zijn. Optie B/C alleen als ze echt onderscheid maken.

## Patroon-leerpunt v4.3.3

> **Bij D-beslissingen met owl:sameAs, disjointness of naming-conventies vooraf een "afgeleide consequenties"-sectie opnemen in instructies (SHACL-impact, disjointness-impact, meeliftregel-impact). Dan hoeven pauzes alleen voor werkelijke architecturale keuzes.**

Iteratie-feedback voor Master: instructies zelf verbeteren reduceert reactieve pauzes.

## Cross-references

- [[brain__workflow__masterchat-interactie]] — communicatie-protocol
- [[brain__workflow__opleveringsprotocol]] — documenteren van pauzes in patch-rapport

— Einde scope-discipline.
