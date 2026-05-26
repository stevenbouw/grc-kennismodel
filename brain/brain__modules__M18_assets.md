---
type: module
id: M18
title: M18 — Assets (asset:)
status: active
date: 2026-05-13
related:
  - D11_sameAs-asset-convergentie
  - sameAs-discipline
  - v4_2_0_M18-asset-module
  - v4_3_0_gap-sprint-d11
sources:
  - Besluit_CIOstelsel_2026
chat-sources: []
confidence: high
---

# M18 — Assets

## Bestand
`m18-assets.ttl` (geconsolideerd in v4.2.1 uit 5 originele bestanden)

## Namespace
`asset: <https://grc.example.org/asset/>` — toegevoegd in v4.2.0 (namespace-count 9 → 10).

## Wat het bevat

Asset-taxonomie gebaseerd op CIO-stelsel 2026 art. 1o componenten. Het canonieke centrum voor asset-modellering — D11 ster-patroon.

| Inhoud | Aantal |
|---|---:|
| Hoofdklassen | 5 (Asset, InformationAsset, HumanAsset, PhysicalAsset, InformationSystem) |
| Sub-taxonomie | Procedure, Service, Software, Facility, etc. |
| Properties (asset-specifiek) | 6 (incl. `asset:appliesToAssetType`) |
| `asset:appliesToAssetType`-asserties | 428 expliciet, **973 inferred** onder OWL RL |
| ISO 27002 → asset-type mappings | 128 |
| BIO 2.0 OverheidsMaatregel → asset-type | 300 |
| SHACL-shapes | 4 (waarvan `asset:NamespaceShape` in SECTIE A na v4.3.0 D11-impact) |

## D11 ster-patroon (5 sameAs-bruggen)

`asset:` is canoniek **centrum** van asset-convergentie ([[brain__decisions__D11_sameAs-asset-convergentie]]):

```turtle
asset:Asset            owl:sameAs risk:Asset .
asset:InformationAsset owl:sameAs risk:InformationAsset .
asset:InformationAsset owl:sameAs isms:InformationAsset .
asset:HumanAsset       owl:sameAs risk:HumanAsset .
asset:PhysicalAsset    owl:sameAs risk:PhysicalAsset .
```

## Niet-gebrugd (bewuste keuzes)

- `asset:InformationSystem` ↔ `risk:SystemAsset` — risk: is breder (incl. ICT-dienst)
- `risk:ServiceAsset` — geen M18-equivalent
- `isms:PrimaryAsset` / `isms:SupportingAsset` — overlappen meerdere asset:-klassen

## Demo-SPARQL

`m18-demo-sparql.rq` als los bestand naast de module — demonstreert cross-namespace asset-queries onder OWL RL.

## Cross-references

- [[brain__decisions__D11_sameAs-asset-convergentie]] — vastlegging ster-patroon
- [[brain__concepts__sameAs-discipline]] — bredere context owl:sameAs-gebruik
- [[brain__sprints__v4_2_0_M18-asset-module]] — initiële opname
- [[brain__sprints__v4_3_0_gap-sprint-d11]] — formalisatie D11 + 5 bruggen

— Einde M18.
