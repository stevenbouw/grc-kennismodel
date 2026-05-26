---
type: module
id: M01
title: M01 — Framework (fw:)
status: active
date: 2026-05-21
related:
  - D09_framework-neutraliteit
  - D10_coso-enterprise-governance
  - v4_4_0_fase-2-cbw-cbb
  - v4_5_0_fase-3-nist-csf-2-0
  - v4_6_0_fase-4-ensia-en-volwassenheid
sources:
  - projectinstructie-v1.9
chat-sources: []
confidence: high
---

# M01 — Framework

## Bestand
`m01-framework.ttl`

## Namespace
`fw: <https://grc.example.org/framework/>`

## Wat het bevat

Alle GRC-frameworks als individuals, organiserend kader voor het hele model. Bevat ook de Te Beschermen Belangen (TBB)-ConceptScheme uit BVA-stelsel.

| Inhoud | Voorbeelden |
|---|---|
| Framework-individuals | `fw:NIS2_Directive`, `fw:BIO_2_0`, `fw:ISO_IEC_27001_2022`, `fw:ISO_IEC_27002_2022`, `fw:CBW`, `fw:Cbb` *(v4.4.0)*, `fw:DORA`, `fw:AVG`, `fw:NIST_CSF_2_0` *(v4.5.0)*, `fw:VIR_2007`, `fw:VIRBI_2025`, `fw:BesluitBVAStelsel`, `fw:BesluitCIOStelsel_2026`, `fw:COSO_ICF`, `fw:COSO_ERM`, `fw:COBIT_2019`, **`fw:ENSIA`** *(v4.6.0, gepromoot uit m15)* |
| TBB ConceptScheme | `fw:BVATeBeschermenBelangen` met 7 te-beschermen-belangen (toegevoegd v4.2.0) |
| Klassen | `fw:Framework`, `fw:GRCFramework`, `fw:Guideline`, subklassen per laag |
| SourceAttributions | `ext:Attr_ENSIA_Logius_2024` *(v4.6.0)* |
| Relatie-properties | `fw:stelVerplicht`, `fw:geeftRichtlijnenVoor`, `fw:geeftITInvullingAan`, `fw:dektAf`, `fw:toetst`, `fw:isTranspositieVan`, `fw:transposedBy`, `fw:uitgewerktIn`, `fw:werktUit`, `ext:isComponentOf`, **`fw:status`** *(v4.6.0)*, **`fw:hasPublicationDate`** *(v4.6.0)* |

## v4.6.0-uitbreiding — fw:ENSIA als fw:GRCFramework

**Promotie uit m15** (was eerder `fw:Guideline`). Kerndeclaratie volledig verplaatst naar m01:

| Element | Wijziging |
|---|---|
| Type | `fw:Guideline` → `fw:GRCFramework` |
| Locatie | m15 (was) → **m01 kern + m15 domeinspecifiek** (hybride locatie A3+B3+C2) |
| Properties verplaatst | label, kern-comment, hasIdentifier, hasVersionLabel, isMandatoryForDutchGovernment, issuedBy, appliesInJurisdiction, hasDomain, fw:toetst BIO, officialURL |
| Nieuwe properties | `fw:status@nl/@en` (in productie sinds 2017), `fw:hasPublicationDate 2024-12-19` |
| Behouden in m15 | NB-comment over gemeenten-context, 8 `ext:hasAuditDomain`, 2 `skos:relatedMatch` |
| Bron-attribuering | Nieuwe `ext:Attr_ENSIA_Logius_2024` (vrij gebruik met bronvermelding) |

**Issuers ENSIA (bevestigd):** BZK/DutchCentral, NOREA, VNG. `fw:Logius` NIET als issuer (Logius beheert, geeft niet uit — property-semantiek-discipline §8.3 patch-rapport v4.6.0).

## v4.5.0-uitbreiding — fw:NIST_CSF_2_0 (in herinnering)

`fw:NIST_CSF_2_0`-individual als kader-individual voor M21. Alle 497 csf:-componenten verwijzen via `ext:isComponentOf fw:NIST_CSF_2_0`.

## v4.4.0-uitbreiding — CBW/Cbb cluster (in herinnering)

`fw:Cbb`-individual + `fw:uitgewerktIn` / `fw:werktUit` cluster-relatie.

## D9-bewijs — Vier verificatie-clusters

Vier aantoonbaar gelijkwaardige cluster-relaties zichtbaar in M01:

```
Cluster 1: fw:NIS2_Directive ←fw:isTranspositieVan— fw:CBW       (v4.4.0, EU-richtlijn ↔ NL-wet)
Cluster 2: fw:CBW —fw:uitgewerktIn→ fw:Cbb                       (v4.4.0, NL-wet → AMvB)
Cluster 3: fw:NIST_CSF_2_0 (geen hiërarchische relatie)          (v4.5.0, US-cybersecurity-framework)
Cluster 4: fw:ENSIA —fw:toetst→ fw:BIO_2_0                       (v4.6.0, NL-audit-kader → operationeel kader)
```

D9: alle vier de clusters tonen verschillende relatie-typen, geen hiërarchische subordering tussen frameworks. ENSIA-cluster bewijst dat audit-kaders géén apart privilege krijgen in het model.

## Hoort bij lagen

Laag 0 (COSO), Laag 1 (COBIT), Laag 2 (wet- en regelgeving incl. Cbb), Laag 4 (ISO/NIST-normen incl. NIST CSF 2.0), **Laag 5 (ENSIA als audit-kader)** hebben hier hun framework-individual.

## Cross-references

- [[brain__decisions__D09_framework-neutraliteit]] — vier verificatie-clusters geverifieerd
- [[brain__decisions__D10_coso-enterprise-governance]] — COSO ICF/ERM
- [[brain__sprints__v4_2_0_M18-asset-module]] — TBB-uitbreiding
- [[brain__sprints__v4_4_0_fase-2-cbw-cbb]] — fw:Cbb + fw:uitgewerktIn/werktUit
- [[brain__sprints__v4_5_0_fase-3-nist-csf-2-0]] — fw:NIST_CSF_2_0
- [[brain__sprints__v4_6_0_fase-4-ensia-en-volwassenheid]] — fw:ENSIA als GRCFramework + ext:Attr_ENSIA_Logius_2024
- [[brain__modules__M15_ensia]] — domeinspecifieke ENSIA-aanvullingen
- [[brain__modules__M21_nist-csf-2-0-planned]] — CSF-componenten via ext:isComponentOf

— Einde M01.
