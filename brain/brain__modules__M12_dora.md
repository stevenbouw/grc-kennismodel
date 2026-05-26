---
type: module
id: M12
title: M12 — DORA (compl: + ext:)
status: active
date: 2026-05-13
related:
  - D12_drie-laags-compliance
  - v4_3_3_d12-en-predicate-consolidatie
sources:
  - CELEX3A32022R25543AEN3ATXT
chat-sources: []
confidence: high
---

# M12 — DORA

## Bestand
`m12-dora.ttl`

## Namespace
Hergebruikt `compl:` + `ext:DORARequirement`-subklasse.

## Wat het bevat

Digital Operational Resilience Act (EU 2022/2554) — **referentiekader**: de organisatie valt **niet onder DORA** (financiële sector). Opgenomen voor cross-framework-zicht en thematische completeness.

| Inhoud | Aantal v4.3.3 |
|---|---:|
| `ext:DORARequirement`-subjects (art. 5-14, 16-19) | 14 (geen Art15 in bronmodel) |
| `compl:articleRef "art. N"`-asserties (na v4.3.3 α) | 14 |
| Module-grootte | 152 triples |

## D9-symmetrie

Predicate-consolidatie α (v4.3.3 Item 3): oorspronkelijk plande de instructie alleen 6 NIS2-subjects te migreren van `ext:articleNumber` naar `compl:articleRef`. Werkelijkheid: 20 uses (6 NIS2 + 14 DORA). Masterchat-GO Optie A op basis van [[brain__decisions__D09_framework-neutraliteit]]: DORA krijgt gelijke behandeling, volledige consolidatie naar 20 subjects.

## D12-context

DORA-subjects zitten op **Laag 3 (ComplianceRequirement)**. Geen aparte OBL-laag voor DORA in huidige model — overweegbaar bij latere uitbreiding indien D12-symmetrie dat vereist.

## Cross-references

- [[brain__sprints__v4_3_3_d12-en-predicate-consolidatie]] — predicate-consolidatie α-sprint
- [[brain__architecture__H25_compl-articleRef-domain-spanning]] — `articleRef`-domain raakt ook 14 DORA-subjects

## Bronlicentie

DORA = publiek EU-recht — vrij herbruikbaar.

— Einde M12.
