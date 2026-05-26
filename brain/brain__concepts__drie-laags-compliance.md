---
type: concept
title: Drie-laags compliance-architectuur
status: living
date: 2026-05-13
related:
  - D12_drie-laags-compliance
  - framework-neutraliteit
  - H25_compl-articleRef-domain-spanning
  - H26_OBL-laag-gap-NIS2
  - H32_obl-laag-asymmetrie
sources:
  - projectinstructie-v1.7
chat-sources: []
confidence: high
---

# Drie-laags compliance-architectuur

## Wat het is

De **drie-laags compliance-architectuur** ([[brain__decisions__D12_drie-laags-compliance]]) modelleert wettelijke en regulatoire verplichtingen in drie hiërarchische lagen:

| Laag | Klasse | Wat het is | Voorbeelden |
|---|---|---|---|
| 1 | `compl:RegulatoryObligation` | Wettelijke verplichting op kader-niveau (richtlijn-artikel) | NIS2 art. 21 onderdelen a–j |
| 2 | `compl:LegalObligation` | Juridische verplichting op artikel-niveau (transpositie-, wet- of besluit-artikel) | OBL_NIS2_Art20/21/23; 14 Cbb-Art; VIR-artikelen; VIRBI; AVG IB-raakvlak |
| 3 | `compl:ComplianceRequirement` (+ subklasse) | Concrete, toepasbare eis | `ext:NIS2Requirement`, `ext:DORARequirement` |

## Waarom drie lagen

Compliance-werkelijkheid heeft drie natuurlijke aggregatie-niveaus:

1. **Wetgeving** spreekt op kader-niveau (richtlijn, wet) — wat zijn de algemene verplichtingen?
2. **Artikel-niveau** specificeert per artikel concreet wat de verplichting is
3. **Eis-niveau** detailleert wat een organisatie precies moet doen om aan dat artikel te voldoen

Drie lagen geven flexibiliteit om op het juiste niveau te queryen: "welke wetten zijn van toepassing?" (Laag 1) versus "welke artikel-verplichtingen heb ik?" (Laag 2) versus "wat moet ik concreet implementeren?" (Laag 3).

## Patroon, geen starre symmetrie

**Verfijning v4.4.0:** D12 is een **patroon**, geen verplichting tot symmetrie per cluster. Niet elk framework-cluster doorloopt alle drie de lagen.

### Toepassings-patronen v4.4.0

| Cluster | Lagen | Modellering |
|---|---|---|
| **NIS2** | 1 + 2 + 3 (volledig) | 10 RegulatoryObligations (art. 21 a-j) + 3 LegalObligations (OBL_NIS2_Art20/21/23) + 15 Requirements |
| **CBW/Cbb** *(v4.4.0)* | **Alleen 2** (legal-only-keten) | 14 Cbb-Art als LegalObligation. Géén regulatory-laag — CBW/Cbb zijn nationale wetgeving (geen EU-richtlijn). Géén requirement-laag in v4.4.0 (Spoor B-afhankelijk) |
| VIR 2007 | Alleen 2 | 5 artikelen als LegalObligation |
| VIRBI 2025 | Alleen 2 | LegalObligation-individuals |
| BVA-stelsel | Alleen 2 | LegalObligation-individuals (BVA, Adj-BVA, BVC) |
| AVG (IB-raakvlak) | Alleen 2 | 5 LegalObligation-individuals (art. 5(1f), 25, 32, 33, 34) |
| DORA | Alleen 3 | DORARequirements (organisatie valt niet onder DORA — geen Legal-laag-instantiatie nodig) |

### Wat dit patroon-onderscheid mogelijk maakt

| Implicatie | Wat het inhoudt |
|---|---|
| **Niet geforceerd** | Cluster zonder regulatory-laag (zoals CBW) hoeft niet kunstmatig een RegulatoryObligation te krijgen |
| **Expliciete keuze** | Per cluster moet wel expliciet zijn welke laag(en) bevat zijn |
| **Cluster-coherentie** | Binnen één cluster moet patroon consistent zijn (niet de helft van Cbb-Art als LegalObligation en helft als RegulatoryObligation) |

## CBW/Cbb als legal-only-cluster (v4.4.0 voorbeeld)

CBW is een **nationale wet** (geen EU-richtlijn). Cbb is een AMvB onder CBW. Beide zijn juridische verplichtingen op artikel-niveau. Geen van beide is op kader-niveau zoals NIS2:

```turtle
fw:CBW rdf:type compl:LegalObligation .                # Laag 2
fw:Cbb rdf:type compl:LegalObligation .                # Laag 2
fw:CBW fw:uitgewerktIn fw:Cbb .                        # cluster-relatie (v4.4.0)

compl:Cbb_Art_06 rdf:type compl:LegalObligation .      # Laag 2
compl:Cbb_Art_07 rdf:type compl:LegalObligation .
...
compl:Cbb_Art_18 rdf:type compl:SupplierExclusionOrder . # subklasse van LegalObligation
...
compl:Cbb_Art_19 rdf:type compl:LegalObligation .
```

**14 Cbb-Art-individuals** allemaal op Laag 2. Geen Laag 1, geen Laag 3 — dat is het cluster-patroon.

## D9-relatie: compatibel

Drie-laags-architectuur is **niet strijdig** met framework-neutraliteit ([[brain__concepts__framework-neutraliteit]]):

- NIS2 krijgt drie lagen, maar dat is omdat de NIS2-werkelijkheid drie niveaus heeft (richtlijn → artikel → requirement)
- CBW krijgt één laag, omdat de CBW-werkelijkheid op één niveau opereert
- Geen van beide is "centraler" dan de ander — beide zijn cluster-eigen

D12-patroon = "elk cluster modelleert zoals de werkelijkheid in dat cluster is", niet "elk cluster doorloopt voorgeschreven structuur".

## Open architectuur-vragen rondom D12

| H-item | Onderwerp | Status v4.4.0 |
|---|---|---|
| [[brain__architecture__H25_compl-articleRef-domain-spanning]] | `compl:articleRef`-domain-spanning over D12-lagen | Onveranderd (14 Cbb-Art zijn domain-conform) |
| [[brain__architecture__H26_OBL-laag-gap-NIS2]] | OBL-laag gap voor NIS2 art. 18, 19, 22, 24 | Onveranderd |
| [[brain__architecture__H27_gamma-migratie-articleIdentifier]] | Voorwaardelijke γ-migratie | Geen trigger geactiveerd |
| [[brain__architecture__H32_obl-laag-asymmetrie]] | Modelleringsasymmetrie tussen OBL_NIS2 (uitgebreid) en overige LegalObligations (minimaal) — *nieuw v4.4.0* | Open, post-v4.5.0-trigger |

## Geschiedenis

| Datum | Gebeurtenis |
|---|---|
| 22 april 2026 | D12 formeel vastgelegd (v4.3.3) — drie-laags-architectuur met starre symmetrie-verwachting |
| 13 mei 2026 | **Verfijning v4.4.0** — patroon-interpretatie expliciet gemaakt na CBW/Cbb-toepassing (legal-only) |

## Cross-references

- [[brain__decisions__D12_drie-laags-compliance]] — formele beslissing
- [[brain__concepts__framework-neutraliteit]] — D9 → patroon-keuze is consistent met framework-neutraliteit
- [[brain__modules__M05_compliance]] — implementatie-module (inclusief 14 Cbb-Art)
- [[brain__modules__M10_nis2-ext]] — NIS2-specifieke uitwerking + CBW-controls
- [[brain__sprints__v4_3_3_d12-en-predicate-consolidatie]] — initiële formalisering
- [[brain__sprints__v4_4_0_fase-2-cbw-cbb]] — verfijning + eerste legal-only-toepassing

— Einde drie-laags-compliance.
