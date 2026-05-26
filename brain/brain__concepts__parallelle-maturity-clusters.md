---
type: concept
title: Parallelle Maturity-Clusters (biz vs isms)
status: living
date: 2026-05-21
related:
  - v4_6_0_fase-4-ensia-en-volwassenheid
  - M06_isms
  - M07_business
  - framework-neutraliteit
sources:
  - patch-rapport-v4_6_0
chat-sources: []
confidence: high
---

# Parallelle Maturity-Clusters (biz vs isms)

## Wat het is

Sinds v4.6.0 bestaan **twee parallelle volwassenheidsmodel-clusters** in het model met **verschillende semantieken, schaal-grootten en domains**. Beide blijven actief — niet samenvoegen.

| Aspect | **biz-cluster** (m07) | **isms-cluster** (m06, NIEUW v4.6.0) |
|---|---|---|
| Sinds | Initieel (pre-v4.6.0) | v4.6.0 |
| Domein | GRCDomain-volwassenheid | Control/Capability-evaluatie |
| Niveau-schaal | **6 levels** (ML_0..ML_5, CMMI) | **5 levels** (Level_1..Level_5, NBA-LIO/NOREA) |
| Hoofdklasse | `biz:MaturityAssessment` | `isms:MaturityCapability` |
| Level-klasse | `biz:MaturityLevel` | `isms:MaturityCapabilityLevel` |
| Beschrijving-klasse | (geen aparte) | `isms:CapabilityLevelDescription` |
| Properties | `biz:hasMaturityLevel`, `biz:targetMaturityLevel`, `biz:maturityScore` | `isms:hasLevelDescription`, `isms:forCapability`, `isms:atMaturityLevel` |
| ABox-domain | 6 `biz:GRCDomain`-individuals (DOM_01..DOM_06) | 32 `isms:MaturityCapability` (23 CbwCapability + 9 ISMSCapability) |
| Gebruik | Dashboard-aggregatie (biz:Dashboard_2026_Q1) | Sheet 6 evaluaties uit CBW-Excel |
| Bron-attributie | (interne, sinds initieel) | `ext:Attr_NBA_LIO_NOREA_Volwassenheidsmodel_via_CBW_2026` |

## Waarom twee clusters — niet samenvoegen

De V1-evaluatie in v4.6.0 Stap 2 toonde dat samenvoegen vier conflicten zou veroorzaken:

| Conflict | Detail |
|---|---|
| **Niveau-schaal-mismatch** | 6 vs 5 levels. Eén schaal kiezen verliest betekenis aan de andere kant |
| **Semantiek-mismatch** | biz:hasMaturityLevel zegt iets over een GRCDomain (organisatie-niveau). isms:atMaturityLevel zegt iets over een Capability (control-niveau). Niet uitwisselbaar |
| **Bron-mismatch** | biz is intern model-eigen ontwerp. isms is bron-getrouw NBA-LIO/NOREA via CBW-Excel. Samenvoegen vertroebelt bron-attribuering |
| **Dashboard-impact** | biz:Dashboard_2026_Q1 aggregaten zijn al gekoppeld aan biz:GRCDomain. Migratie zou Dashboard breken |

V1-uitkomst: **Optie B — nieuwe isms-cluster naast biz-cluster**. biz blijft volledig ongewijzigd.

## Hoe ze samenwerken

```
GRCDomain-niveau (organisatie-aggregatie)        Capability-niveau (control-evaluatie)
────────────────────────────────────────         ──────────────────────────────────────
biz:DOM_01 biz:hasMaturityLevel biz:ML_3         isms:Cap_Cbw_01 isms:hasLevelDescription
  ↑                                                    isms:CapLevel_Cap_Cbw_01_Level_3 .
biz:Dashboard_2026_Q1 biz:aggregates DOM_01      
                                                  isms:CapLevel_Cap_Cbw_01_Level_3
                                                    isms:forCapability isms:Cap_Cbw_01 ;
                                                    isms:atMaturityLevel isms:Level_3 ;
                                                    rdfs:comment "..." .
```

Géén verbinding tussen de twee. Verschillende vragen, verschillende antwoorden.

## Mapping naar CSF Tiers — alleen vanuit isms-cluster

In v4.6.0 Stap 6 zijn 4 SKOS-mappings gelegd: `csf:CSFTier` ↔ `isms:MaturityCapabilityLevel`. **Niet** naar `biz:MaturityLevel`. Reden: CSF Tiers werken op control-capability-niveau (zoals isms), niet op organisatie-niveau (zoals biz).

| Tier | ↔ | Level |
|---|---|---|
| Tier_1_Partial | skos:relatedMatch | Level_1 (Ad-hoc) |
| Tier_2_RiskInformed | skos:relatedMatch | Level_2 (Informeel) |
| Tier_3_Repeatable | skos:relatedMatch | Level_4 (Geëvalueerd) |
| Tier_4_Adaptive | skos:relatedMatch | Level_5 (Geïntegreerd) |

`isms:Level_3` ontbreekt (G1-discipline — 4 vs 5 schaal-verschil).

## SPARQL-discipline — namespace-onderscheid

Bij queries die maturity-vragen stellen, **kies bewust welke cluster**:

```sparql
# Organisatie-niveau dashboard:
SELECT ?domain ?currentLevel ?targetLevel WHERE {
  ?domain a biz:GRCDomain ;
          biz:hasMaturityLevel ?currentLevel ;
          biz:targetMaturityLevel ?targetLevel .
}

# Capability-niveau evaluatie:
SELECT ?cap ?level ?description WHERE {
  ?cap a isms:MaturityCapability ;
       isms:hasLevelDescription ?desc .
  ?desc isms:atMaturityLevel ?level ;
        rdfs:comment ?description .
}
```

Gemengde queries (`biz:hasMaturityLevel` + `isms:atMaturityLevel` in één WHERE-block) zijn meestal een vergissing — bedoel je dashboard-aggregatie of capability-evaluatie?

## Toekomst-overweging

Indien Spoor B-organisatie ooit beide clusters gevuld wil hebben (zowel dashboard-aggregatie als capability-evaluaties), kan een **brug-mapping** worden overwogen — bijvoorbeeld:

```
biz:DOM_01 biz:relatesToCapabilityCluster (isms:Cap_Cbw_01, isms:Cap_Cbw_02, ...)
```

Dit is **geen samenvoeging** maar een expliciete brug die de semantiek-verschillen respecteert. Niet als H-item geregistreerd — wacht op werkelijke Spoor B-vraag.

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-21 | living | Concept ontstaan uit v4.6.0 V1-evaluatie (Optie B) |

## Cross-references

- [[brain__sprints__v4_6_0_fase-4-ensia-en-volwassenheid]] — sprint waarin keuze is gemaakt
- [[brain__modules__M06_isms]] — isms-cluster
- [[brain__modules__M07_business]] — biz-cluster (ongewijzigd)
- [[brain__modules__M21_nist-csf-2-0-planned]] — CSF Tiers mapping naar isms
- [[brain__concepts__framework-neutraliteit]] — D9-context

— Einde parallelle-maturity-clusters.
