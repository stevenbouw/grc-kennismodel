---
type: source
title: CBW NIS2 Control Framework Excel (CC-BY 4.0)
status: living
date: 2026-05-21
related:
  - v4_4_0_fase-2-cbw-cbb
  - v4_5_0_fase-3-nist-csf-2-0
  - v4_6_0_fase-4-ensia-en-volwassenheid
  - provenance-en-attribuering
  - cross-bron-overlap
sources:
  - Cbw_NIS2_Control_Framework
chat-sources: []
confidence: high
---

# CBW NIS2 Control Framework Excel

## Bron-identificatie

| Aspect | Detail |
|---|---|
| Officiële titel | CBW NIS2 Control Framework |
| Uitgevers | Auditdienst Rijk (ADR) + NOREA |
| Versie | 1.0 |
| Datum | 30 september 2025 |
| Licentie | **CC-BY 4.0** — attributie vereist |
| Attribuering in model | `ext:Attr_CBW_NIS2_Framework_2025_CC_BY_4_0` (in m10) |
| **+ Sheet 6 attribuering v4.6.0** | **`ext:Attr_NBA_LIO_NOREA_Volwassenheidsmodel_via_CBW_2026` (in m06, SHA256-bron-hash)** |

## Sheet-overzicht — wat is wanneer gebruikt

| Sheet | Inhoud | Gebruik |
|---|---|---|
| 1-2 | Inhoudsopgave + wijzigingen | Documentair |
| 3 | 26 CBW-controls + UV-decompositie (kolom H) | v4.4.0 Route 5 — `ext:hasControlStatement` + `ext:hasUVInterpretation` |
| 4-5, 7 | Risk-clusters + scope | Documentair |
| **6** | **NBA-LIO/NOREA-volwassenheidsmodel 3.0 (5-niveau-schaal) op 32 capabilities** | **v4.6.0 Stap 4 — 32 isms:MaturityCapability + 160 isms:CapabilityLevelDescription in m06** ✨ |
| 8 | CBW ↔ NIST CSF 2.0 mapping (49 CBW ↔ 90 CSF Subcategories) | v4.5.0 Stap 5 — 641 unieke `skos:closeMatch` |
| 9 | CBW ↔ Cbb ↔ BIO 2.0 mapping | v4.4.0 — 290 sheet-relaties → 183 unieke triples |

## v4.6.0-update — Sheet 6 gebruikt

In v4.6.0 Stap 4 werd Sheet 6 (Volwassenheid beheersmaatregel) verwerkt als bron voor het volwassenheidsmodel-cluster in m06:

| Aspect | Detail |
|---|---|
| Bron-records | 32 capability-rijen × 5 niveau-kolommen = 160 niveau-beschrijvingen |
| Resulterende triples | 1.440 (5 per Capability + 8 per LevelDescription) |
| Verdeling | 23 CbwCapability + 9 ISMSCapability (subclasses van isms:MaturityCapability) |
| Boven raming | **+44% boven raming** (volledig verklaarbaar via rdf:type-dubbele-telling, niet bron-afwijking) |
| Bron-attribuering | `ext:Attr_NBA_LIO_NOREA_Volwassenheidsmodel_via_CBW_2026` met SHA256-hash van CBW-Excel-bronbestand |
| 4 typo-correcties | Cbw_05/11/12/14 in rdfs:label@nl (presentatie alleen, bron-comment behouden) |

Zie [[brain__modules__M06_isms]] voor de cluster-detail en [[brain__concepts__parallelle-maturity-clusters]] voor het architectuur-onderscheid met biz:cluster.

## Route 5 (v4.4.0) — fundamentele bron-discipline

CBW-Excel bevat **ADR/NOREA's UV-decompositie** op CBW-Control-niveau, **niet** ENISA-tekst. Zie [[brain__sources__enisa-guidance]] voor de correctie t.o.v. v1.6-aanname.

## CC-BY 4.0 attribuering — cumulatief gebruik per v4.6.0

| Toepassing | Module | Triples | SourceAttribution |
|---|---|---:|---|
| 26 CBW-controls + UV-decompositie (Sheet 3) | M10 (v4.4.0) | ~52 + 26 | `Attr_CBW_NIS2_Framework_2025_CC_BY_4_0` |
| Sheet 9 mappings (BIO ↔ CBW ↔ Cbb) | M08 (v4.4.0) | 183 | idem |
| Sheet 8 mappings (CSF ↔ ISO) | M21 (v4.5.0) | 641 | idem |
| **Sheet 6 volwassenheidsmodel** | **M06 (v4.6.0)** | **1.440** | **`Attr_NBA_LIO_NOREA_Volwassenheidsmodel_via_CBW_2026`** |

**v4.6.0-detail:** Sheet 6 krijgt **eigen SourceAttribution** omdat de inhoud (NBA-LIO/NOREA-volwassenheidsmodel 3.0) een aparte bron-attribuering vereist binnen de CBW-Excel CC-BY 4.0-licentie. De CBW-controls (Sheet 3) zijn ADR/NOREA-werk, de volwassenheidsmodel-content is NBA-LIO/NOREA-werk dat via CBW-Excel is gedistribueerd.

## ADR/NOREA bron-kwaliteits-patroon — cumulatief

| v4.4.0 (Sheet 9) | v4.5.0 (Sheet 8) | v4.6.0 (Sheet 6) |
|---|---|---|
| 2 typo-categorieën | 19 ISO-normalisaties + 16 unresolved (incl. 5.28-typo) | 4 typo's in capability-labels |

**Bron-conclusie:** bruikbaar maar structureel licht inconsistent. Cumulatief patroon zichtbaar over drie sheets in drie sprints. Geen sprint-blokkade — sprint-protocol "Bron-typo-beleid patroon-criterium" v1.9 hanteert wel/niet-corrigeren-discipline.

## Cross-bron-overlap S5 ∩ S6 = 105 mappings (v4.5.0)

105 ISO-mappings zijn identiek tussen Sheet 8 (deze bron) en CSF Reference Tool (NIST). Onafhankelijk bewijs voor SKOS-kwaliteit. Zie [[brain__concepts__cross-bron-overlap]].

## v4.6.0 — alle sheets verwerkt

Alle relevante sheets uit CBW-Excel zijn nu verwerkt in het model:

| Sheet | Sprint | Status |
|---|---|---|
| 3 | v4.4.0 | ✓ |
| 9 | v4.4.0 | ✓ |
| 8 | v4.5.0 | ✓ |
| 6 | **v4.6.0** | **✓ ✨** |

Geen openstaande CBW-Excel-werk meer.

## Cross-references

- [[brain__sprints__v4_4_0_fase-2-cbw-cbb]] — Route 5 (sheet 3 + 9)
- [[brain__sprints__v4_5_0_fase-3-nist-csf-2-0]] — Stap 5 (sheet 8)
- [[brain__sprints__v4_6_0_fase-4-ensia-en-volwassenheid]] — Stap 4 (sheet 6)
- [[brain__modules__M06_isms]] — Sheet 6 landing (v4.6.0)
- [[brain__modules__M08_bio20]] — Sheet 9 landing (v4.4.0)
- [[brain__modules__M10_nis2-ext]] — Sheet 3 landing (26 CBW-controls)
- [[brain__modules__M21_nist-csf-2-0-planned]] — Sheet 8 landing (v4.5.0)
- [[brain__sources__enisa-guidance]] — apart bestand, geen ENISA-tekst in CBW-Excel
- [[brain__concepts__cross-bron-overlap]] — 105 mappings overlap met CSF Reference Tool
- [[brain__architecture__H35_cbb-528-typo-interpretatie]] — sheet 8 UV 10.4 5.28-typo
- [[brain__concepts__parallelle-maturity-clusters]] — Sheet 6 isms-cluster naast biz

— Einde CBW-Excel source.
