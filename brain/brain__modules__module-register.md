---
type: index
id: module-register
title: Module-register — Ontologie-modules GRC Kennismodel v4.6.0
status: living
date: 2026-05-21
---

# Module-register — Ontologie-modules v4.6.0

Overzicht van alle 19 actieve data-modules + infrastructuur. **M15-ENSIA per v4.6.0 uitgebreid van stub naar productie**; volwassenheidsmodel-cluster nieuw in m06.

## Actieve modules — staat per v4.6.0

| ID | Bestand | Domein | Namespace | v4.6.0 wijziging | Detail |
|---|---|---|---|---|---|
| M01 | `m01-framework.ttl` | Frameworks + TBB ConceptScheme | `fw:` | **+ `fw:ENSIA` als `fw:GRCFramework` (gepromoot uit m15) + `ext:Attr_ENSIA_Logius_2024` SourceAttribution** | [[brain__modules__M01_framework]] |
| M02 | `m02-control.ttl` | 93 ISO 27002 controls | `ctrl:` | — | [[brain__modules__M02_iso27002-control]] |
| M03 | `m03-risk.ttl` | Risicomodel TBox | `risk:` | — | [[brain__modules__M03_risk]] |
| M04 | `m04-roles.ttl` | BVA/CIO-rollen + RACI | `roles:` | — | [[brain__modules__M04_roles]] |
| M05 | `m05-compliance.ttl` | D12 drie-laags compliance | `compl:` | — | [[brain__modules__M05_compliance]] |
| **M06** | `m06-isms.ttl` | ISMS + canonieke SoA + **volwassenheidsmodel-cluster** | `isms:` | **+ 5 isms-klassen + 3 OP + 5 Levels + 32 Capabilities + 160 LevelDescriptions + Attr_NBA_LIO_NOREA SourceAttribution (SHA256)** | [[brain__modules__M06_isms]] |
| M07 | `m07-business.ttl` | Business-context **(biz:MaturityAssessment-cluster, ongewijzigd)** | `biz:` | — (parallel naast isms-cluster, **niet samenvoegen**) | [[brain__modules__M07_business]] |
| M08 | `m08-bio20.ttl` | BIO 2.0 — 93 controls + 148 OM | `bio:` | — | [[brain__modules__M08_bio20]] |
| M09 | `m09-iso27001-ext.ttl` | ISO 27001:2022 + HSClause | `ext:` | — | [[brain__modules__M09_iso27001-ext]] |
| M10 | `m10-nis2-ext.ttl` | NIS2 EU/NL + CBW-controls | `compl:`, `ext:`, `ctrl:` | — | [[brain__modules__M10_nis2-ext]] |
| M11 | `m11-nist-800-53.ttl` | NIST SP 800-53 R5 | `ctrl:` | — | [[brain__modules__M11_nist-800-53]] |
| M12 | `m12-dora.ttl` | DORA (referentie) | `compl:`, `ext:` | — | [[brain__modules__M12_dora]] |
| M13 | `m13-iso22301.ttl` | ISO 22301 BCM | `ext:` | — | [[brain__modules__M13_iso22301]] |
| M14 | `m14-avg-gdpr.ttl` | AVG IB-raakvlak | `compl:` | — | [[brain__modules__M14_avg-gdpr]] |
| **M15** | `m15-ensia.ttl` | ENSIA (Laag 5 audit) | `fw:` (verplaatst naar m01), `ext:` | **Oude fw:Guideline-blok verwijderd; behoudt NB-comment + 8 ext:hasAuditDomain + 2 skos:relatedMatch** | [[brain__modules__M15_ensia]] |
| M16 | `m16-virbi-ext.ttl` | VIRBI 2025 | `fw:`, `compl:` | — | [[brain__modules__M16_virbi-ext]] |
| M17 | `m17-coso-cobit.ttl` | COSO ICF/ERM + COBIT 2019 | `fw:` | — | [[brain__modules__M17_coso-cobit]] |
| M18 | `m18-assets.ttl` | Asset-taxonomie + D11 ster | `asset:` | — | [[brain__modules__M18_assets]] |
| **M21** | `m21-csf.ttl` | NIST CSF 2.0 — Core + IE **+ Tiers** | `csf:` | **+ csf:CSFTier-klasse + 2 DP (riskGovernance/Management-Description) + 4 Tier-individuals + 4 skos:relatedMatch naar isms:MaturityCapabilityLevel** | [[brain__modules__M21_nist-csf-2-0-planned]] |

**5 modules gewijzigd in v4.6.0:** grc-core (versie-bump), M01, M06, M15, M21. De overige 14 modules zijn bytewise identiek aan v4.5.0-eindstand.

## Infrastructuur-bestanden

| Bestand | v4.6.0 wijziging |
|---|---|
| `grc-core.ttl` | Versie-bump v4.5.0 → v4.6.0, modified 2026-05-21 |
| `grc-bridges.ttl` | — |
| `grc-shacl.ttl` | — |
| `m18-demo-sparql.rq` | — |

## Nieuwe klassen v4.6.0 (6)

| Klasse | Module | Doel |
|---|---|---|
| `isms:MaturityCapability` | m06 | Generieke parent voor maturity-capabilities |
| `isms:CbwCapability ⊑ isms:MaturityCapability` | m06 | 23 CBW-specifieke capabilities |
| `isms:ISMSCapability ⊑ isms:MaturityCapability` | m06 | 9 ISMS-clausule-capabilities |
| `isms:MaturityCapabilityLevel` | m06 | 5 niveaus Level_1..Level_5 (NBA-LIO/NOREA-schaal) |
| `isms:CapabilityLevelDescription` | m06 | 160 (32 capabilities × 5 levels) niveau-beschrijvingen |
| `csf:CSFTier ⊑ ext:FrameworkComponent` | m21 | 4 NIST CSF 2.0 Tiers (Optie C) |

## Nieuwe properties v4.6.0 (5)

| Property | Type | Module | Doel |
|---|---|---|---|
| `isms:hasLevelDescription` | ObjectProperty (inverse van forCapability) | m06 | Capability → LevelDescription |
| `isms:forCapability` | ObjectProperty (inverse van hasLevelDescription) | m06 | LevelDescription → Capability |
| `isms:atMaturityLevel` | ObjectProperty | m06 | LevelDescription → MaturityCapabilityLevel |
| `csf:riskGovernanceDescription` | DatatypeProperty | m21 | Lange normatieve EN-tekst per Tier (~250-1.085 chars) |
| `csf:riskManagementDescription` | DatatypeProperty | m21 | Lange normatieve EN-tekst per Tier (~178-1.085 chars) |

## SourceAttribution-individuals na v4.6.0 (5)

| Individual | Module | Licentie | Toegevoegd |
|---|---|---|---|
| `ext:Attr_CBW_NIS2_Framework_2025_CC_BY_4_0` | M10 | CC-BY 4.0 | v4.4.0 |
| `ext:Attr_NIST_CSF_2_0_Core_2024` | M21 | Public Domain | v4.5.0 |
| `ext:Attr_NIST_CSF_2_0_Reference_Tool_2026` | M21 | Public Domain | v4.5.0 |
| `ext:Attr_NBA_LIO_NOREA_Volwassenheidsmodel_via_CBW_2026` | **M06** | **CC-BY 4.0** (via CBW-Excel) | **v4.6.0** ✨ |
| `ext:Attr_ENSIA_Logius_2024` | **M01** | **Vrij gebruik met bronvermelding** | **v4.6.0** ✨ |

## SKOS-mappings na v4.6.0

| Type | Aantal v4.6.0 | Δ |
|---|---:|---:|
| `skos:closeMatch` | 1.490 | 0 |
| `skos:relatedMatch` | 238 | +4 (Tier↔Level) |
| `skos:exactMatch` | 46 | 0 |
| `skos:broadMatch` | 38 | 0 |
| **Totaal** | **1.798** | **+4** |

## Status-tellingen v4.6.0

| Status | Aantal |
|---|---:|
| Active modules | 19 (M01-M14, M15 uitgebreid, M16-M18, M21) |
| Stub modules | 0 (M15 niet meer stub na v4.6.0) |
| Infrastructure files | 4 |
| Out of scope | 2 (M19, M20) |
| **Totaal data-modules in v4.6.0** | **19 + 4 infrastructure = 23 .ttl + 1 .rq** |

## Modules per laag

| Laag | Modules |
|---|---|
| Laag 0 — Enterprise governance | M17 (COSO ICF/ERM) |
| Laag 1 — IT-governance | M17 (COBIT 2019), M04 (CIO-stelsel) |
| Laag 2 — Wet- en regelgeving | M10 (NIS2 + CBW + Cbb), M14 (AVG IB-raakvlak), M16 (VIRBI 2025) |
| Laag 3 — Operationeel kader | M08 (BIO 2.0) |
| Laag 4 — Normen | M02 (ISO 27002), M09 (ISO 27001), M11 (NIST 800-53), M13 (ISO 22301), M21 (NIST CSF 2.0 + Tiers) |
| **Laag 5 — Audit & verantwoording** | **M15 (ENSIA, uitgebreid v4.6.0)** ✨ |
| Transversaal | M01 (frameworks incl. fw:ENSIA), M03 (risk), M04 (roles), M05 (compliance + Cbb), **M06 (ISMS + volwassenheidsmodel)** ✨, M07 (business — biz:MaturityAssessment ongewijzigd), M12 (DORA referentie), M18 (assets) |

## Twee parallelle MaturityCapability-clusters

Sinds v4.6.0 bestaan twee maturity-clusters **parallel** in het model — **niet samenvoegen** (zie [[brain__concepts__parallelle-maturity-clusters]]):

| Cluster | Locatie | Semantiek | Schaal |
|---|---|---|---|
| **biz** (ongewijzigd) | M07 | GRCDomein-volwassenheid | 6 levels (ML_0..ML_5, CMMI) |
| **isms** (v4.6.0) | M06 | Control/Capability-evaluatie | 5 levels (Level_1..5, NBA-LIO/NOREA) |

## Cross-references

- [[brain__sprints__sprint-register]] — sprints waarin modules zijn ontstaan / uitgebreid
- [[brain__decisions__D-register]] — D-decisions per module
- [[brain__concepts__concept-register]] — overkoepelende concepten (incl. parallelle-maturity-clusters)
- [[brain__sprints__v4_6_0_fase-4-ensia-en-volwassenheid]] — actuele baseline-sprint

— Einde module-register.
