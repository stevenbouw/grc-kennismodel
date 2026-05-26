---
type: concept
title: SKOS-export-filter — ontologie-laag vs dashboard-laag meet-conventie
status: living
date: 2026-05-26
related:
  - namedindividual-telmethode
  - canonical-metrics
  - v4_6_0_fase-4-ensia-en-volwassenheid
sources:
  - skos-edge-discrepantie-v4_6_0
  - skos-kwaliteitsanalyse-v4_6_0
  - patch-rapport-v4_3_3
chat-sources: []
confidence: high
---

# SKOS-export-filter — ontologie-laag vs dashboard-laag meet-conventie

## Wat het is

De **SKOS-export-filter** is het mechanisme in `dashboard/build_grc_explorer_v3.py` (regel 482) dat SKOS-mappings met minstens één TBox-endpoint (`owl:Class` etc.) bewust uitsluit van de JSON-export. Het is geen bug — het is een gevolg van een bewuste architecturale keuze dat de dashboard-explorer uitsluitend **ABox-individuen** toont als nodes en daardoor alleen edges met dubbele ABox-endpoints kan exporteren.

**Concrete observatie v4.6.0:**

| Laag | SKOS-telling | Meet-conventie |
|---|---:|---|
| **Ontologie-laag** (`ontology/*.ttl`, rdflib) | **1.798** | Alle SKOS-tripels in TTL, ongeacht endpoint-type |
| **Dashboard-laag** (`grc-data-v4_6_0.json`) | **1.759** | Alleen tripels met dubbele ABox-endpoints |
| **Verschil** | **39** | Tripels met ≥1 `owl:Class`-endpoint |

Mathematisch sluitend: `1.759 + 39 = 1.798`. Geen "extra" tripels in JSON die niet in TTL voorkomen — de export is een echte deelverzameling.

## Kernprincipe

> **Ontologie-laag en export-laag meten verschillende dingen. Beide kloppen.**
> Het is een measurement-conventie-verschil, geen inconsistentie.

| Laag | Vraag die de meting beantwoordt |
|---|---|
| Ontologie | "Hoeveel SKOS-mappings staan er in de formele kennisbasis?" |
| Dashboard | "Hoeveel SKOS-edges zijn er tussen individuen in de visualisatie?" |

De cijfers 1.798 en 1.759 hebben elk hun eigen autoritatieve toepassing. Wie de canonical_metrics-JSON consulteert voor TBox+ABox-omvang krijgt 1.798. Wie het dashboard-JSON consulteert voor visualisatie-edge-count krijgt 1.759.

## Root-cause: drie samenwerkende filters in `build_v3`

De export-filter is een keten van drie keuzes in `dashboard/build_grc_explorer_v3.py`:

**Filter A — SCHEMA_TYPES-definitie** (regel 77-86): markeert `owl:Class`, alle property-types, `owl:Restriction`, `owl:Ontology`, SHACL-shapes en `skos:ConceptScheme` als "schema/TBox".

**Filter B — individuals-set-bouw** (regel 411-422): een entiteit komt alleen in `individuals` als ze (i) `owl:NamedIndividual` is, óf (ii) een ander `rdf:type` heeft dat géén schema-type is. Voor `owl:Class`-entiteiten faalt voorwaarde (ii).

**Filter C — edge-endpoint-validatie** (regel 482): een edge wordt alleen geëxporteerd als beide endpoints in `node_ids` staan — wat per Filter B alleen ABox-individuen zijn. SKOS-tripel `(C1, skos:closeMatch, C2)` waarbij C1 óf C2 `owl:Class` is, verschijnt daardoor nooit in `grc-data-v4_6_0.json`.

## De 39 verschil-tripels in v4.6.0 — twee semantische clusters

### Cluster 1 — TBB ↔ asset bidirectionele exactMatches (14 tripels)

`m18-assets.ttl` declareert 7 paren van bidirectionele `skos:exactMatch` tussen `asset:`-klassen en `framework:TBB_*`-Concepts:

| asset:-klasse (owl:Class) | framework:TBB_* (skos:Concept) |
|---|---|
| `asset:Equipment` | `framework:TBB_Materieel` |
| `asset:HumanAsset` | `framework:TBB_Personen` |
| `asset:InformationAsset` | `framework:TBB_Informatie` |
| `asset:InformationSystem` | `framework:TBB_Informatiesystemen` |
| `asset:IntangibleAsset` | `framework:TBB_Imago` |
| `asset:PhysicalObject` | `framework:TBB_Objecten` |
| `asset:TangibleGoods` | `framework:TBB_Goederen` |

Beide kanten gaan verloren in de export: `asset:`-zijde is `owl:Class` (afgewezen door Filter B), `framework:TBB_*`-zijde is `skos:Concept` zonder `owl:NamedIndividual`-type (ook afgewezen). Verlies in JSON betekent **niet** semantisch verlies in de ontologie — de owl:sameAs-bruggen uit D11 zijn de primaire convergentie-laag; SKOS-exactMatch is de aanvullende cross-framework-laag.

### Cluster 2 — risk/business-klassen → COSO ERM / ISO 31000 / NIST SP 800-30 (25 tripels)

15 tripels in `m03-risk.ttl` en 10 in `m07-business.ttl` mappen risico- en business-domein-klassen naar externe framework-individuen:

| Module | Klasse-subjecten | Framework-objecten |
|---|---|---|
| m03-risk | `Risk`, `RiskAppetite`, `RiskTreatment`, `RiskAssessment`, `RiskManagementTier`, `RiskRegister`, `ReportingRisk`, `ImpactLevel`, `LikelihoodLevel`, `Threat`, `Vulnerability` | COSO ERM-componenten (extended:), ISO 31000:2018, NIST SP 800-30 Rev 1, NIST SP 800-39, ISO/IEC 27005:2022 |
| m07-business | `DirectieBeoordeling`, `GRCDashboard`, `KCI`, `KPI`, `KRI`, `ManagementReport`, `PerformanceIndicator`, `RiskAppetite`, `RiskAppetiteStatement`, `StrategicObjective` | COSO ERM-componenten (Performance, GovernanceCulture, ReviewRevision, InformationCommunicationReporting, StrategyObjectiveSetting) |

In deze cluster is de domein-zijde een `owl:Class` (afgewezen door Filter B), de framework-zijde is wél `owl:NamedIndividual` (in de export aanwezig) — maar omdat één endpoint TBox is, faalt Filter C.

### Concentratie

| Module van herkomst | Tripels van de 39 |
|---|---:|
| m03-risk.ttl | 15 |
| m18-assets.ttl | 14 |
| m07-business.ttl | 10 |
| **Totaal** | **39** |

Geen verlies in CSF-, BIO-, NIST 800-53-, ISO 27001/27002- of NIS2-mappings — die zijn allemaal individual↔individual en passeren Filter C zonder probleem.

## Historische lijn — leerpunt v4.3.3 → v4.6.0

De canonieke-metrics-discipline ([[brain__concepts__canonical-metrics]]) en NamedIndividual-telmethode ([[brain__concepts__namedindividual-telmethode]]) zijn ontstaan uit een tellingsdiscrepantie in v4.3.3: patch-rapport (607 → 622) versus canonical_metrics-JSON (637). Conclusie destijds:

> **Canonical_metrics-JSON is enige autoritatieve bron** voor kerntellingen.

Dat principe geldt nog steeds, maar v4.6.0 voegt een verfijning toe: er is niet één meet-laag, er zijn er **twee**. Elk met een eigen geldige conventie.

| Versie | Inzicht |
|---|---|
| **v4.3.3** | Canonieke meet-discipline binnen één laag (ontologie). Eén autoritatieve bron per metric. |
| **v4.6.0** | Twee meet-lagen (ontologie + dashboard) elk met eigen meet-conventie. Beide autoritatief binnen hun laag; cross-laag-vergelijking vraagt expliciete verklaring. |

Het is **geen** terugtrekking van het v4.3.3-principe — het is een uitbreiding: binnen de ontologie-laag blijft canonical_metrics-JSON autoritatief; binnen de dashboard-laag is `grc-data-v*.json` autoritatief; cross-laag-deltas moeten expliciet geadresseerd worden in plaats van als "ruis" afgedaan.

## Toetsing aan D-decisions — geen schending

| D-decision | Toetsing |
|---|---|
| **D1 (OWL 2 DL profiel)** | Class-niveau-SKOS-mappings zijn legitiem in OWL 2 DL. Geen schending. |
| **D4 (SKOS voor cross-framework)** | D4 specificeert match-type-keuze, niet of mappings op klasse- of individual-niveau geplaatst moeten worden. Beide niveaus zijn architectureel verdedigbaar. |
| **D9 (framework-neutraliteit)** | Het verschil heeft geen framework-bias — verlies treft drie modules gespreid (M03, M07, M18). |
| **D11 (asset-ster sameAs-convergentie)** | De 14 TBB↔asset exactMatches zijn de SKOS-laag náást de owl:sameAs-bruggen (D11). Verlies in JSON betekent **niet** semantisch verlies in de ontologie — alleen visualisatie-verlies. |

## Implicaties voor toekomstige sprints

### Patch-rapporten

Bij rapportage van SKOS-tellingen voortaan expliciet de laag noemen:
- "1.798 SKOS-mappings in ontologie" (rdflib-telling op TTL)
- "1.759 SKOS-edges in dashboard-export" (build_v3-JSON-output)

Niet generiek "1.798 SKOS" of "1.759 SKOS" zonder laag-aanduiding — dat veroorzaakte de oorspronkelijke verwarring in v4.6.0.

### Build-pipeline-architectuur

Als ooit besloten wordt om TBox-elementen in de explorer te tonen (bv. een aparte "schema-laag" naast de individuen), kan Filter B/C selectief aangepast worden om `owl:Class`-nodes wél te exporteren met een aparte marker. Niet in scope nu — wel registreerbaar als open architectuur-overweging indien masterchat dit later relevant acht.

### Andere edge-categorieën — generaliseerbaarheid

Het patroon "ontologie-laag bevat meer dan dashboard-laag exporteert" geldt potentieel ook voor andere edge-categorieën met TBox-endpoints (bv. `rdfs:subClassOf`, `owl:equivalentClass`). Build_v3 exporteert deze in de regel niet als edges; ze zijn impliciet via de class-hierarchy, niet via de individual-grafiek. Voor SKOS is het zichtbaar omdat SKOS-edges een aparte categorie zijn in de JSON; voor pure schema-relaties is het minder zichtbaar omdat ze nooit als edge bedoeld waren.

## Cross-references

- [[brain__concepts__canonical-metrics]] — zusterconcept: meet-methode-discipline binnen ontologie-laag
- [[brain__concepts__namedindividual-telmethode]] — formalisering van Class-vs-Individual-onderscheiding (v4.3.3)
- [[brain__sprints__v4_6_0_fase-4-ensia-en-volwassenheid]] — sprint waarin de discrepantie expliciet geanalyseerd is
- `output/reports/skos-edge-discrepantie-v4_6_0.md` — volledige tech-inspectie met de 39 tripels, root-cause-analyse en filter-keten
- `output/reports/skos-kwaliteitsanalyse-v4_6_0.md` — kanttekening-precisering (sectie "Kanttekening bij 1.759 vs 1.798 SKOS-edges in export")
- `dashboard/build_grc_explorer_v3.py` regel 482 — code-implementatie van de filter (Filter C, met inline commentaar)

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-26 | living | Concept geboren uit v4.6.0 tech-inspectie SKOS-edge-discrepantie. Mathematica + root-cause + twee semantische clusters + verfijning van v4.3.3 canonical_metrics-principe. |

— Einde SKOS-export-filter.
