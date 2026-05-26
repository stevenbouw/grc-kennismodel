---
type: module
id: M04
title: M04 — Roles (roles:)
status: active
date: 2026-05-13
related:
  - D11_sameAs-asset-convergentie
  - H29_three-lines-model
sources:
  - BVAstelsel
  - Besluit_CIOstelsel_2026
  - VIR_2007
chat-sources: []
confidence: high
---

# M04 — Roles

## Bestand
`m04-roles.ttl`

## Namespace
`roles: <https://grc.example.org/roles/>`

## Wat het bevat

Rolverdeling uit BVA-stelsel (Besluit Beveiligingsambtenaren Rijksdienst 2021) en CIO-stelsel (Besluit CIO-stelsel 2026). RACI-skelet voor proces/control/risico-/asset-eigenaarschap.

| Inhoud | Voorbeelden |
|---|---|
| BVA-rollen | `roles:BVA`, `roles:Adj_BVA`, `roles:BVC` (Beveiligingscoördinator, formeel toegevoegd in v2.0 fix-release) |
| CIO-stelsel-rollen | `roles:CIO` (per Besluit CIO-stelsel 2026), specialist-rollen |
| Generieke rollen | `roles:ControlOwner`, `roles:RiskOwner`, `roles:ProcessOwner`, `roles:AssetOwner` |
| Auditor-rollen | `roles:Auditor`, gerelateerd aan Laag 5 |
| RACI-properties | `roles:hasResponsible`, `roles:hasAccountable`, `roles:hasConsulted`, `roles:hasInformed` |

## Spoor B (ABox-leeg)

Concrete persoon-instances zijn Spoor B. Zie geparkeerd H12.

## Cross-module

- `roles:Role rdfs:seeAlso asset:HumanAsset` (toegevoegd v4.2.0)
- D6-meelift in v4.2.0: 2 NL-only items tweetalig

## Toekomst-uitbreiding

[[brain__architecture__H29_three-lines-model]] — Three Lines Model (IIA 2020) als M04-uitbreiding via SKOS-mappings. ~6-12 nieuwe role-individuals plus 12-24 SKOS-mappings. Trigger: Fase 4 of mini-sprint na Fase 3.

— Einde M04.
