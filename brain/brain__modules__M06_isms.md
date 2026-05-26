---
type: module
id: M06
title: M06 — ISMS + canonieke SoA + Volwassenheidsmodel-cluster (isms:)
status: active
date: 2026-05-21
related:
  - D08_canonieke-soa
  - parallelle-maturity-clusters
  - v4_6_0_fase-4-ensia-en-volwassenheid
sources:
  - Cbw_NIS2_Control_Framework
chat-sources: []
confidence: high
---

# M06 — ISMS + Volwassenheidsmodel-cluster

## Bestand
`m06-isms.ttl`

## Namespace
`isms: <https://grc.example.org/isms/>`

## Wat het bevat

ISMS-laag inclusief canonieke SoA (D8) en — **per v4.6.0** — het volwassenheidsmodel-cluster naast biz:MaturityAssessment in M07.

| Inhoud | Aantal v4.6.0 |
|---|---:|
| ISMS-klassen + canonieke SoA-structuur | (sinds initieel) |
| `isms:SoA_2026` + 93 `isms:SoAEntry_*` (D8) | 94 |
| **isms:MaturityCapability** + 2 subclasses (CbwCapability, ISMSCapability) | 3 nieuwe klassen v4.6.0 |
| **isms:MaturityCapabilityLevel** (Level_1..5, NBA-LIO/NOREA) | 1 nieuwe klasse v4.6.0 |
| **isms:CapabilityLevelDescription** | 1 nieuwe klasse v4.6.0 |
| **5 isms:MaturityCapabilityLevel-individuals** | 5 v4.6.0 |
| **32 isms:MaturityCapability-individuals** (23 CbwCapability + 9 ISMSCapability) | 32 v4.6.0 |
| **160 isms:CapabilityLevelDescription-individuals** (32 × 5) | 160 v4.6.0 |
| **3 ObjectProperties** (hasLevelDescription/forCapability inverseOf-paar + atMaturityLevel) | 3 v4.6.0 |
| **SourceAttribution** | 1 v4.6.0 (`ext:Attr_NBA_LIO_NOREA_Volwassenheidsmodel_via_CBW_2026`, SHA256) |

## v4.6.0-uitbreiding — Volwassenheidsmodel-cluster

**V1-uitkomst Optie B** (gekozen ondanks bestaande biz:cluster). 5 nieuwe klassen + 3 OP + 197 nieuwe individuals + 1 SourceAttribution.

### TBox (Stap 2)

```turtle
isms:MaturityCapability a owl:Class .
isms:CbwCapability rdfs:subClassOf isms:MaturityCapability .
isms:ISMSCapability rdfs:subClassOf isms:MaturityCapability .
isms:MaturityCapabilityLevel a owl:Class .
isms:CapabilityLevelDescription a owl:Class .

isms:hasLevelDescription owl:inverseOf isms:forCapability .
isms:atMaturityLevel a owl:ObjectProperty .
```

### Statische ABox (Stap 3) — 5 Levels, NBA-LIO/NOREA-schaal

| Level | Naam (NL) | Naam (EN) |
|---|---|---|
| `isms:Level_1` | Ad-hoc | Ad-hoc |
| `isms:Level_2` | Informeel | Informal |
| `isms:Level_3` | Vastgesteld | Established |
| `isms:Level_4` | Geëvalueerd | Evaluated |
| `isms:Level_5` | Geïntegreerd | Integrated |

### Sheet 6 ABox (Stap 4) — 32 Capabilities + 160 LevelDescriptions

IRI-conventies:
- `isms:Cap_Cbw_01..23` (23 CbwCapability)
- `isms:Cap_ISMS_01..09` (9 ISMSCapability)
- `isms:CapLevel_<CapID>_Level_<N>` (160 LevelDescriptions, 32 × 5)

**4 typo-correcties** in NL-labels (presentatie alleen, niet bron-tekst): Cbw_05/11/12/14. Niveau-beschrijvingen (rdfs:comment) bron-getrouw uit CBW-Excel.

**EN-vertalingen:**
- 23 Cbw door masterchat geleverd (kort, conform D6 vertaling-scope v1.7)
- 9 ISMS via ISO 27001:2022-standaard-clausule-titels (autoritatieve EN-bron, D6 vertaling-scope)

**D6 toepassing:**
- `rdfs:label` bilingueel
- `rdfs:comment` met niveau-beschrijving uit CBW-Excel @nl-only (bron-getrouw, geen gezaghebbende EN-bron)

### Triple-impact-decompositie (verklaart +44% boven raming)

| Element | Per element | Aantal | Totaal |
|---|---:|---:|---:|
| Per Capability | 5 triples (2 rdf:type + 2 label + 1 sourceAttribution) | 32 | 160 |
| Per LevelDescription | 8 triples (2 rdf:type + 2 label + 1 forCapability + 1 atMaturityLevel + 1 comment + 1 sourceAttribution) | 160 | 1.280 |

**Verklaring:** rdflib telt `rdf:type` dubbel (class-membership + NamedIndividual-membership). Pre-stap-raming nam 4+6 per element; werkelijk 5+8. Sprint-protocol "Ramings-baseline rdf:type-dubbele-telling" geformaliseerd in projectinstructie v1.9.

## Parallel naast biz:MaturityAssessment-cluster

**Niet samenvoegen** met biz:cluster in M07 — verschillende semantieken, schaal-grootten en domains. Zie [[brain__concepts__parallelle-maturity-clusters]] voor de architectuur-betekenis.

| Aspect | biz (M07) | isms (M06, v4.6.0) |
|---|---|---|
| Semantiek | GRCDomain-volwassenheid (organisatie-niveau) | Capability-evaluatie (control-niveau) |
| Schaal | 6 levels (ML_0..ML_5, CMMI) | 5 levels (Level_1..Level_5, NBA-LIO/NOREA) |
| Domain | 6 `biz:GRCDomain` | 32 `isms:MaturityCapability` |

## CSF Tier-mapping (in m21)

In Stap 6 zijn 4 `skos:relatedMatch` gelegd in m21 vanuit `csf:CSFTier` naar `isms:MaturityCapabilityLevel`:

| Tier | ↔ | Level |
|---|---|---|
| `csf:Tier_1_Partial` | skos:relatedMatch | `isms:Level_1` (Ad-hoc) |
| `csf:Tier_2_RiskInformed` | skos:relatedMatch | `isms:Level_2` (Informeel) |
| `csf:Tier_3_Repeatable` | skos:relatedMatch | `isms:Level_4` (Geëvalueerd) |
| `csf:Tier_4_Adaptive` | skos:relatedMatch | `isms:Level_5` (Geïntegreerd) |

`isms:Level_3` (Vastgesteld) heeft géén Tier-equivalent (G1-discipline — 4 vs 5 schaal-verschil).

## SourceAttribution

`ext:Attr_NBA_LIO_NOREA_Volwassenheidsmodel_via_CBW_2026` met SHA256-hash van CBW-Excel-bronbestand. CC-BY 4.0 via CBW-Excel — attribuering naar NBA-LIO/NOREA.

## D-relaties

- [[brain__decisions__D08_canonieke-soa]] — SoA structuur (sinds v4.2.2)

## Cross-references

- [[brain__concepts__parallelle-maturity-clusters]] — biz vs isms-onderscheid
- [[brain__modules__M07_business]] — biz:MaturityAssessment-cluster (ongewijzigd)
- [[brain__modules__M21_nist-csf-2-0-planned]] — CSF Tier↔Level mappings
- [[brain__sources__cbw-excel]] — Sheet 6 bron
- [[brain__sprints__v4_6_0_fase-4-ensia-en-volwassenheid]] — sprint van uitbreiding

— Einde M06.
