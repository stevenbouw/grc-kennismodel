---
type: decision
id: D12
title: D12 — Drie-laags compliance-architectuur
status: active
date: 2026-05-13
related:
  - drie-laags-compliance
  - D09_framework-neutraliteit
  - H25_compl-articleRef-domain-spanning
  - H26_OBL-laag-gap-NIS2
  - H32_obl-laag-asymmetrie
  - v4_3_3_d12-en-predicate-consolidatie
  - v4_4_0_fase-2-cbw-cbb
sources:
  - projectinstructie-v1.7
chat-sources: []
confidence: high
---

# D12 — Drie-laags compliance-architectuur

## Beslissing

Compliance-eisen worden gemodelleerd in **drie lagen**:

| Laag | Klasse | Wat het is |
|---|---|---|
| 1 | `compl:RegulatoryObligation` | Wettelijke verplichting op kader-niveau (richtlijn-artikel-niveau) |
| 2 | `compl:LegalObligation` | Juridische verplichting op artikel-niveau (transpositie-, wet- of besluit-artikel) |
| 3 | `compl:ComplianceRequirement` (+ subklasse zoals `ext:NIS2Requirement`) | Concrete, toepasbare eis |

**D12 is een patroon, geen starre symmetrie per cluster.** Niet elk framework-cluster doorloopt alle drie de lagen — sommige clusters bevatten alleen Laag 2 + 3, anderen alle drie.

## Datum

- **Initieel:** v4.3.3 (22 april 2026) — geformaliseerd als ontwerpbeslissing
- **Verfijnd:** v4.4.0 (13 mei 2026) — patroon-onderscheid expliciet gemaakt na CBW/Cbb-toepassing

## Toepassings-patronen

### NIS2 — volledige drie-laags-keten

| Laag | Voorbeeld |
|---|---|
| Regulatory | `compl:NIS2_Art21_a` t/m `_j` (10 individuals, kader-niveau) |
| Legal | `compl:OBL_NIS2_Art20`, `_Art21`, `_Art23` (transpositie-artikel-niveau) |
| Requirement | `compl:REQ_NIS2_Art20_1`, `_Art21_a..j`, `_Art23_*` (concrete eisen) |

### CBW/Cbb — legal-only-keten (geen regulatory-laag)

| Laag | Voorbeeld |
|---|---|
| Regulatory | *(geen — CBW en Cbb zijn beide nationale wetgeving, niet EU-richtlijn)* |
| Legal | `fw:CBW` (wet) en 14 `compl:Cbb_Art_*` (zorgplichtartikelen Cbb) — beide `compl:LegalObligation` |
| Requirement | Nog niet gemodelleerd voor CBW/Cbb in v4.4.0 — Spoor B-afhankelijk |

Verfijning v4.4.0: CBW en Cbb krijgen géén `compl:RegulatoryObligation`-laag. CBW is een nationale wet (geen EU-richtlijn); Cbb is een AMvB onder CBW. Beide functioneren op Laag 2 en zijn via `fw:uitgewerktIn` / `fw:werktUit` verbonden.

### Andere clusters

- **VIR 2007, VIRBI 2025, BVA-stelsel, CIO-stelsel, AVG (IB-raakvlak)** — Laag 2 (`compl:LegalObligation`), geen Laag 1
- **DORA** — Laag 3 (`compl:ComplianceRequirement` via `ext:DORARequirement`); de organisatie valt niet onder DORA, dus geen LegalObligation-instantiatie nodig

## Architectuur-implicatie

D12 als **patroon** (niet als symmetrie-vereiste) betekent:

1. **Geen verplichting** om elk framework-cluster compleet door alle drie lagen te modelleren
2. **Wel verplichting** om expliciet te zijn over welke laag(en) een cluster bevat
3. **Wel verplichting** dat de gekozen lagen consistent zijn binnen het cluster

## Properties bij D12

- `compl:articleRef` — artikel-referentie als string ("art. N"), domain `compl:Obligation` (zie H25 voor domain-spanning-discussie)
- `compl:requirementText` — eis-tekst (NL/EN)
- `compl:derivedFrom` — relatie REQ → OBL → RO
- `fw:uitgewerktIn` / `fw:werktUit` *(v4.4.0)* — verbindt wet met AMvB, geen D12-laag-relatie maar wel cluster-relatie

## Hangt samen met open H-items

- [[brain__architecture__H25_compl-articleRef-domain-spanning]] — domain-spanning van `articleRef` over D12-lagen
- [[brain__architecture__H26_OBL-laag-gap-NIS2]] — gap in Laag 2 voor NIS2 art. 18, 19, 22, 24
- [[brain__architecture__H32_obl-laag-asymmetrie]] — modelleringsasymmetrie tussen verschillende `compl:LegalObligation`-groepen

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-04-22 | active | Geformaliseerd in v4.3.3 (drie-laags-architectuur met starre symmetrie-verwachting) |
| 2026-05-13 | active | Verfijnd in v4.4.0 — patroon-interpretatie: niet elk cluster doorloopt alle lagen; CBW/Cbb als legal-only-keten voorbeeld |

## Hangt samen met

- [[brain__concepts__drie-laags-compliance]] — uitleg van het concept
- [[brain__decisions__D09_framework-neutraliteit]] — D9 vereist geen architectuur-bias; D12 als patroon (niet starre symmetrie) past hierin
- [[brain__sprints__v4_3_3_d12-en-predicate-consolidatie]] — sprint van initiële formalisering
- [[brain__sprints__v4_4_0_fase-2-cbw-cbb]] — sprint van verfijning

— Einde D12.
