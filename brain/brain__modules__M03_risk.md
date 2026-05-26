---
type: module
id: M03
title: M03 — Risk (risk:)
status: active
date: 2026-05-13
related:
  - D11_sameAs-asset-convergentie
  - v4_3_0_gap-sprint-d11
sources:
  - NENENISO_IEC_27005_2024_en
  - NENISO_31000__C11_2019_nl
  - nistspecialpublication80039
chat-sources: []
confidence: high
---

# M03 — Risk

## Bestand
`m03-risk.ttl`

## Namespace
`risk: <https://grc.example.org/risk/>`

## Wat het bevat

Risk management TBox-grondlaag uit ISO 31000:2018, ISO 27005:2024 en NIST SP 800-39/30.

| Inhoud | Voorbeelden |
|---|---|
| Hoofd-risico-klassen | `risk:Risk`, `risk:ResidualRisk`, `risk:OperationalRisk`, `risk:ComplianceRisk`, `risk:StrategicRisk`, **`risk:ReportingRisk`** (toegevoegd v4.3.0 G4) |
| Risk-componenten | `risk:Threat`, `risk:ThreatSource`, `risk:Vulnerability`, `risk:Asset` |
| Asset-subklassen | `risk:InformationAsset`, `risk:HumanAsset`, `risk:PhysicalAsset`, `risk:SystemAsset`, `risk:ServiceAsset` |
| Assessment-scales | `risk:Likelihood`, `risk:Impact` (5-puntsschaal) |
| Properties | `risk:mitigatedBy`, `risk:hasLikelihood`, `risk:hasImpact` |
| SKOS-altLabel | `risk:Impact skos:altLabel "Consequence"@en` (G5 v4.3.0, ISO 27005:2024 conformiteit) |

## Spoor B (ABox-leeg)

Het bestand bevat TBox + lege ABox. Risico-instances worden pas toegevoegd bij Spoor B (organisatie-specifiek). Zie geparkeerd H11.

## D-relaties

- [[brain__decisions__D11_sameAs-asset-convergentie]] — 4 sameAs-bruggen met asset: (Asset, InformationAsset, HumanAsset, PhysicalAsset). `risk:ServiceAsset` blijft ongekoppeld; `risk:SystemAsset` bewust niet gebrugd (breder dan `asset:InformationSystem`)
- [[brain__sprints__v4_3_0_gap-sprint-d11]] — sprint waarin G2/G4/G5 zijn uitgevoerd

## Cross-module

`isms:forRisk` ObjectProperty (M06, toegevoegd v4.3.0 G2) brugt SoAEntry → Risk.

— Einde M03.
