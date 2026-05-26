---
type: module
id: M07
title: M07 — Business-context + biz:MaturityAssessment (biz:)
status: active
date: 2026-05-21
related:
  - parallelle-maturity-clusters
  - v4_6_0_fase-4-ensia-en-volwassenheid
sources: []
chat-sources: []
confidence: high
---

# M07 — Business-context + biz:MaturityAssessment

## Bestand
`m07-business.ttl`

## Namespace
`biz: <https://grc.example.org/business/>`

## Wat het bevat

Business-context van de ontologie. Bevat o.a. het `biz:MaturityAssessment`-cluster dat sinds initieel operationeel is voor GRCDomain-dashboard-aggregatie.

| Inhoud | Detail |
|---|---|
| `biz:GRCDomain` (6 individuals DOM_01..DOM_06) | Domeinen voor GRC-aggregatie |
| `biz:MaturityAssessment` | Assessment-individual |
| `biz:MaturityLevel` (ML_0..ML_5) | 6-level CMMI-schaal |
| `biz:hasMaturityLevel` (domain: biz:GRCDomain) | Huidige volwassenheid per domein |
| `biz:targetMaturityLevel` | Doel-volwassenheid per domein |
| `biz:maturityScore` | Score-property |
| `biz:Dashboard_2026_Q1` | Dashboard-individual met `biz:aggregates` over GRCDomain-individuals |

## v4.6.0-status — ONGEWIJZIGD

**Geen wijzigingen in M07 in v4.6.0.** Sprint-protocol "respecteer bestaande operationele clusters" toegepast.

### Achtergrond V1-keuze v4.6.0

Bij Fase 4 (M15-ENSIA + Volwassenheidsmodel) werd geëvalueerd of het bestaande biz:MaturityAssessment-cluster hergebruikt of uitgebreid kon worden voor het NBA-LIO/NOREA-volwassenheidsmodel uit CBW-Excel Sheet 6.

**Uitkomst V1-evaluatie: Optie B — nieuwe isms-cluster naast biz**, biz blijft volledig ongewijzigd. Vier conflict-redenen:

| Conflict | Detail |
|---|---|
| **Niveau-schaal-mismatch** | biz: 6 levels (ML_0..ML_5 CMMI). isms: 5 levels (Level_1..5 NBA-LIO/NOREA) |
| **Semantiek-mismatch** | biz:hasMaturityLevel zegt iets over een GRCDomain (organisatie-niveau). isms:atMaturityLevel zegt iets over een Capability (control-niveau) |
| **Bron-mismatch** | biz is intern model-eigen ontwerp. isms is bron-getrouw NBA-LIO/NOREA via CBW-Excel met SHA256-attributie |
| **Dashboard-impact** | biz:Dashboard_2026_Q1 aggregaten zijn al gekoppeld aan biz:GRCDomain. Migratie zou Dashboard breken |

## Parallelle clusters — niet samenvoegen

Sinds v4.6.0 bestaat naast biz:MaturityAssessment het nieuwe `isms:MaturityCapability`-cluster in M06. **Niet samenvoegen.**

| Aspect | biz (M07, deze module) | isms (M06, v4.6.0) |
|---|---|---|
| Sinds | Initieel | v4.6.0 |
| Domein | GRCDomain-volwassenheid | Control/Capability-evaluatie |
| Schaal | 6 levels (CMMI) | 5 levels (NBA-LIO/NOREA) |
| ABox | 6 GRCDomain-individuals | 32 Capabilities + 160 LevelDescriptions |
| Bron | Intern | CBW-Excel Sheet 6 (CC-BY 4.0 via NBA-LIO/NOREA) |
| Gebruik | biz:Dashboard_2026_Q1 aggregatie | Sheet 6 evaluaties |

Zie [[brain__concepts__parallelle-maturity-clusters]] voor de volledige architectuur-betekenis en SPARQL-discipline (namespace-onderscheid bij maturity-queries).

## SPARQL-aandachtspunt

Bij queries die maturity-vragen stellen, **kies bewust welke cluster**:

```sparql
# Organisatie-niveau dashboard (biz):
SELECT ?domain ?currentLevel ?targetLevel WHERE {
  ?domain a biz:GRCDomain ;
          biz:hasMaturityLevel ?currentLevel ;
          biz:targetMaturityLevel ?targetLevel .
}

# Capability-niveau evaluatie (isms):
SELECT ?cap ?level ?description WHERE {
  ?cap a isms:MaturityCapability ;
       isms:hasLevelDescription ?desc .
  ?desc isms:atMaturityLevel ?level ;
        rdfs:comment ?description .
}
```

Gemengde queries (`biz:hasMaturityLevel` + `isms:atMaturityLevel` in één WHERE-block) zijn meestal een vergissing.

## Cross-references

- [[brain__concepts__parallelle-maturity-clusters]] — biz vs isms onderscheid
- [[brain__modules__M06_isms]] — isms:MaturityCapability-cluster (nieuw v4.6.0)
- [[brain__sprints__v4_6_0_fase-4-ensia-en-volwassenheid]] — V1-uitkomst Optie B

— Einde M07.
