---
type: index
id: source-register
title: Source-register — Bronnen per licentie-categorie
status: living
date: 2026-05-21
---

# Source-register — Bronnen per licentie-categorie

Overzicht van alle bronnen die in het ontologie-model verwerkt zijn, gegroepeerd per licentie-categorie. Per v4.6.0 met cumulatieve bron-kwaliteits-patronen en 5 `ext:SourceAttribution`-individuals in model.

## Bronnen per licentie

### Onbeperkt — overheidspublicaties (geen attributie-eis)

| Bron | Versie | Toepassing | Detail |
|---|---|---|---|
| BIO 2.0 v1.2 | 24 sept 2025 | M08 BIO 2.0 (93 controls + 148 OM) | [[brain__sources__bio2-en-handreiking]] |
| Handreiking BIO2-opmaat | 2026 | M08 BBN-asserties (241× via `ext:hasHandreikingBBN`) | [[brain__sources__bio2-en-handreiking]] |

### Publiek domein — Amerikaanse overheidspublicaties (geen attributie-eis, wel formele SourceAttribution voor herkomst)

| Bron | Versie | Toepassing | Detail |
|---|---|---|---|
| NIST SP 800-53 R5 | 2020 | M11 (124/~1000 controls) | [[brain__sources__nist-800-53-39-30]] |
| NIST SP 800-39 | 2011 | Risico-management-referentie | [[brain__sources__nist-800-53-39-30]] |
| NIST SP 800-30 | 2012 | Risico-assessment-referentie | [[brain__sources__nist-800-53-39-30]] |
| NIST CSWP 29 (CSF 2.0) | feb 2024 | M21 Core (6 + 22 + 106) + **Tiers (v4.6.0 Appendix B)** | [[brain__sources__nist-csf-2-0]] |
| CSF 2.0 Implementation Examples | 2024 | M21 IE-individuals (363) | [[brain__sources__nist-csf-2-0]] |
| CSF Reference Tool | 2026 | Stap 6 v4.5.0 mappings naar SP 800-53 | [[brain__sources__nist-csf-2-0]] |

### Publiek EU-recht (vrij herbruikbaar)

| Bron | Datum | Toepassing |
|---|---|---|
| NIS2 (EU 2022/2555) | 2022 | M10 |
| DORA (EU 2022/2554) | 2022 | M12 (referentie) |
| Uitvoeringsverordening (EU) 2024/2690 | 2024 | Achterliggend bron Route 5 (via UV-decompositie in CBW-Excel) |
| AVG/GDPR | 2016 | M14 (IB-raakvlak) |

### Publiek NL-recht (vrij herbruikbaar)

| Bron | Datum | Toepassing |
|---|---|---|
| VIR 2007 | 2007 | M05 (5 artikelen) |
| VIRBI 2025 | 2025 | M16 |
| Besluit BVA-stelsel | — | M04 |
| Besluit CIO-stelsel 2026 | 2026 | M04 |
| CBW (Cyberbeveiligingswet) | in voorbereiding | M01 (fw:CBW) — markering "in voorbereiding" |
| Cbb (Cyberbeveiligingsbesluit) | concept t.b.v. TK | M05 (14 Cbb-Art) — markering "concept" |

### NEN-restrictief — geen tekst-reproductie in model

| Bron | Toepassing | Detail |
|---|---|---|
| ISO 27001:2022 | M09 (hoofdtekst-clausules, IRI-conventie alleen) | [[brain__sources__iso-normen-bundle]] |
| ISO 27002:2022 | M02 (93 controls, IRI-conventie alleen) | [[brain__sources__iso-normen-bundle]] |
| ISO 27005:2024 | Referentie | [[brain__sources__iso-normen-bundle]] |
| ISO 31000:2018 | M03 referentie | [[brain__sources__iso-normen-bundle]] |
| ISO 22301:2019 | M13 | [[brain__sources__iso-normen-bundle]] |
| ISO 22313:2020 | M13 | [[brain__sources__iso-normen-bundle]] |

### CC-BY 4.0 — attributie vereist

| Bron | Versie | Toepassing | SourceAttribution |
|---|---|---|---|
| CBW NIS2 Control Framework Excel — Sheet 3, 8, 9 (ADR & NOREA) | v1.0, 30 sept 2025 | M10 (sheet 3), M08 (sheet 9), M21 (sheet 8) | `ext:Attr_CBW_NIS2_Framework_2025_CC_BY_4_0` |
| **CBW NIS2 Control Framework Excel — Sheet 6 (NBA-LIO/NOREA)** | **v1.0, 30 sept 2025** | **M06 volwassenheidsmodel-cluster (v4.6.0)** | **`ext:Attr_NBA_LIO_NOREA_Volwassenheidsmodel_via_CBW_2026`** (SHA256) |

### Vrij gebruik met bronvermelding

| Bron | Versie | Toepassing | SourceAttribution |
|---|---|---|---|
| **NOREA Handreiking ENSIA 2024 versie 1.0** | **19 dec 2024** | **M01 (fw:ENSIA) + M15 (audit-domains)** | **`ext:Attr_ENSIA_Logius_2024`** (v4.6.0) |

## SourceAttribution-individuals na v4.6.0 (5 totaal)

| Individual | Toegevoegd in | Module | Licentie |
|---|---|---|---|
| `ext:Attr_CBW_NIS2_Framework_2025_CC_BY_4_0` | v4.4.0 | M10 | CC-BY 4.0 |
| `ext:Attr_NIST_CSF_2_0_Core_2024` | v4.5.0 | M21 | Public Domain |
| `ext:Attr_NIST_CSF_2_0_Reference_Tool_2026` | v4.5.0 | M21 | Public Domain |
| **`ext:Attr_NBA_LIO_NOREA_Volwassenheidsmodel_via_CBW_2026`** *(v4.6.0)* | **v4.6.0** | **M06** | **CC-BY 4.0 (via CBW-Excel)** |
| **`ext:Attr_ENSIA_Logius_2024`** *(v4.6.0)* | **v4.6.0** | **M01** | **Vrij gebruik met bronvermelding** |

## Cumulatieve bron-kwaliteits-patronen

### ADR/NOREA-patroon (cumulatief over drie sprints)

| Sprint | Sheet | Issue | Aantal |
|---|---|---|---:|
| v4.4.0 | sheet 9 | Typo-categorieën | 2 |
| v4.5.0 | sheet 8 | ISO-normalisaties | 19 |
| v4.5.0 | sheet 8 | Unresolved (CSF v1.x + 5.28-typo) | 16 |
| **v4.6.0** | **sheet 6** | **Typo's in capability-labels** | **4** |

**Conclusie:** ADR/NOREA-bron is bruikbaar maar structureel licht inconsistent. Cumulatief patroon zichtbaar over drie sheets in drie sprints. Sprint-protocol v1.9 "Bron-typo-beleid patroon-criterium" hanteert wel/niet-corrigeren-discipline (referentie-targets niet, individu-labels wel).

### NIST CSF-bron-patroon

| Aspect | Detail |
|---|---|
| Bron-eigen ontwerp | RC.CO begint bij -03 (geen -01/-02); GV.SC tot -05 met 10 IEs |
| OLIR-aanname onjuist (v4.5.0) | Reference Tool gebruikt eigen formaat, niet OLIR |
| **CSF Tiers @en-only descriptions (v4.6.0)** | **D6-symmetrische toepassing — lange normatieve EN-tekst zonder gezaghebbende NL-bron** |

### Cross-bron-overlap (v4.5.0)

105 ISO-mappings identiek tussen Sheet 8 (ADR/NOREA) en CSF Reference Tool (NIST). Bron-consistentie-bewijs van twee onafhankelijke bronnen. Zie [[brain__concepts__cross-bron-overlap]].

## Bronnen-overzicht per sprint

| Sprint | Nieuwe bronnen in model |
|---|---|
| Initieel | BIO 2.0 + ISO + NIST SP 800-53/39/30 + EU + NL-recht |
| v4.4.0 | CBW-Excel CC-BY 4.0 (Sheet 3 + 9) → `Attr_CBW_NIS2_Framework_2025_CC_BY_4_0` |
| v4.5.0 | NIST CSF 2.0 Public Domain → `Attr_NIST_CSF_2_0_Core_2024` + `Attr_NIST_CSF_2_0_Reference_Tool_2026` |
| **v4.6.0** | **NBA-LIO/NOREA volwassenheidsmodel via CBW-Excel Sheet 6 → `Attr_NBA_LIO_NOREA` (SHA256)** + **NOREA Handreiking ENSIA → `Attr_ENSIA_Logius_2024`** |

## Geparkeerde bronnen

| Bron | Status | Trigger |
|---|---|---|
| [[brain__sources__enisa-guidance]] (ENISA TIG-PDF) | Niet geïntegreerd | Analyse-opdracht 2.0 of v4.7.0+ |

## Cross-references

- [[brain__concepts__provenance-en-attribuering]] — discipline van bron-attribuering
- [[brain__concepts__cross-bron-overlap]] — kwaliteits-indicator
- [[brain__index]] — masterindex

— Einde source-register.
