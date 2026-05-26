---
type: module
id: M17
title: M17 — COSO ICF/ERM + COBIT 2019 (fw:)
status: active
date: 2026-05-19
related:
  - D10_coso-enterprise-governance
  - v4_5_0_fase-3-nist-csf-2-0
sources:
  - COBIT2019FrameworkIntroductionandMethodology_res_eng_1118
chat-sources: []
confidence: high
---

# M17 — COSO ICF/ERM + COBIT 2019

## Bestand
`m17-coso-cobit.ttl`

## Namespace
`fw: <https://grc.example.org/framework/>` (gedeeld met M01)

## Wat het bevat

Enterprise governance (Laag 0) + IT-governance (Laag 1):

| Inhoud | Aantal |
|---|---:|
| COSO ICF-componenten | 5 (Control Environment, Risk Assessment, Control Activities, Information and Communication, Monitoring Activities) |
| COSO ERM-componenten | 5 (Strategic, Operational, Reporting, Compliance, Performance) |
| COBIT 2019 governance- en management-objectives | 40 (in 5 domeinen: EDM, APO, BAI, DSS, MEA) |

## v4.5.0-uitbreiding — GOVERN-overlap met csf:

In v4.5.0 Stap 7 zijn **13 nieuwe `skos:relatedMatch`-triples** toegevoegd: van `csf:GV_*` Categories (GOVERN-Function in CSF 2.0) naar COSO/COBIT-componenten.

| Aspect | Detail |
|---|---|
| SKOS-uses in m17 | Verdriedubbeld: 19 → 32 |
| Mapping-richting | `csf:GV_*` → `fw:COSO_*` of `fw:COBIT_*` (relatedMatch, niet exact/close) |
| Rationale | GOVERN is in CSF 2.0 nieuw toegevoegde Function die overlap heeft met enterprise governance (COSO) en IT-governance (COBIT) |

### 6 bewust niet-gemapte targets

Gedocumenteerd in patch-rapport-v4_5_0 §8 punt 19:
- `fw:COBIT_DSS05` (Manage Security Services)
- `fw:COBIT_EDM02`, `fw:COBIT_EDM04`, `fw:COBIT_EDM05`
- `fw:COSO_ERM_InformationCommunicationReporting`
- `fw:COSO_ICF_InformationCommunication`

**GV.SC SKIP-rationale**: COSO/COBIT-clusters in m17 bevatten geen native cybersecurity-supply-chain-component. CSF GV.SC (Cybersecurity Supply Chain Risk Management) heeft daarom geen natuurlijk equivalent in COSO/COBIT.

Mogelijke heroverweging bij Spoor B-data of bij introductie van een specifiek supply-chain-framework (TPRM, SOC 2 vendor-mgmt, etc.).

## D10-toepassing

[[brain__decisions__D10_coso-enterprise-governance]] vastgelegd 17 mrt 2026. M17 is de implementatie voor COSO ICF/ERM als Laag 0 + COBIT 2019 als Laag 1.

## Bronlicentie

COBIT 2019 = ISACA, restrictief. M17 bevat IRI-conventies + structuur-componenten, geen COBIT-tekst verbatim.

COSO ICF/ERM = restrictief. M17 bevat de 5-componenten-structuur per kader, geen normatieve tekst.

## Cross-references

- [[brain__decisions__D10_coso-enterprise-governance]] — formele beslissing
- [[brain__sprints__v4_5_0_fase-3-nist-csf-2-0]] — GV→COSO/COBIT 13 nieuwe mappings
- [[brain__modules__M21_nist-csf-2-0-planned]] — herkomst csf:GV_*-mappings
- [[brain__concepts__framework-neutraliteit]] — D9-context

— Einde M17.
