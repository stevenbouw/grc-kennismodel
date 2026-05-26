---
type: module
id: M21
title: M21 — NIST CSF 2.0 (csf:)
status: active
date: 2026-05-21
related:
  - D03_10-namespaces
  - D06_meeliftregel-tweetalig
  - D09_framework-neutraliteit
  - cross-bron-overlap
  - parallelle-maturity-clusters
  - v4_5_0_fase-3-nist-csf-2-0
  - v4_6_0_fase-4-ensia-en-volwassenheid
sources:
  - NIST_CSWP_29
  - CSF_2_0Implementation_Examples
  - Cbw_NIS2_Control_Framework
chat-sources: []
confidence: high
---

# M21 — NIST CSF 2.0

> **Filename-noot:** filename behoudt `_planned`-suffix uit iteratie 5. Inhoud beschrijft `active`-staat (sinds v4.5.0) + Tiers-uitbreiding (v4.6.0).

## Bestand
`m21-csf.ttl`

## Namespace
`csf: <https://grc.example.org/csf/>` — 11e namespace, toegevoegd v4.5.0

## Status

**Active** sinds v4.5.0 (19 mei 2026), uitgebreid met **Tiers-cluster v4.6.0** (21 mei 2026).

## Wat het bevat (post-v4.6.0)

NIST Cybersecurity Framework 2.0 als gemapt referentiekader (D9 Optie B). Core + Implementation Examples (v4.5.0) + **Tiers (v4.6.0)**.

| Inhoud | Aantal v4.6.0 |
|---|---:|
| `csf:Function`-individuals (GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER) | 6 |
| `csf:Category`-individuals | 22 |
| `csf:Subcategory`-individuals | 106 |
| `csf:ImplementationExample`-individuals (100% Subcategory-dekking) | 363 |
| **`csf:CSFTier`-individuals** *(v4.6.0)* | **4** (Tier_1_Partial..Tier_4_Adaptive) |
| `ext:SourceAttribution`-individuals | 2 (Core + Reference Tool) |
| **Totaal NamedIndividuals in csf:** | **501 + 9 TBox-subjects = 510** |
| SKOS-mappings vanuit csf: | 1.448 (van v4.5.0) + 4 Tier↔Level (v4.6.0) = 1.452 |

## v4.6.0-uitbreiding — Tiers-cluster

### TBox (Stap 2 v4.6.0)

| Element | Type | Doel |
|---|---|---|
| `csf:CSFTier ⊑ ext:FrameworkComponent` | Klasse | 4 NIST CSF 2.0 Tiers — expliciete naam `CSFTier` om collision met `risk:RiskManagementTier` te voorkomen |
| `csf:riskGovernanceDescription` | DatatypeProperty | Lange normatieve EN-tekst per Tier (~250-1.085 chars) |
| `csf:riskManagementDescription` | DatatypeProperty | Lange normatieve EN-tekst per Tier (~178-1.085 chars) |

### Statische ABox (Stap 3 v4.6.0) — Optie C bilinguaal

Vier Tier-individuals met:
- `rdfs:label` bilingueel @nl/@en (kort)
- `csf:csfIdentifier` zonder language-tag
- `csf:riskGovernanceDescription` + `csf:riskManagementDescription` **@en-only** (D6-symmetrische toepassing v1.9 — lange normatieve EN-tekst, geen gezaghebbende NL-bron)

| Tier | NL-label | EN-label | Bron |
|---|---|---|---|
| `csf:Tier_1_Partial` | Gedeeltelijk | Partial | CSWP 29 Appendix B |
| `csf:Tier_2_RiskInformed` | Risico-bewust | Risk Informed | CSWP 29 Appendix B |
| `csf:Tier_3_Repeatable` | Reproduceerbaar | Repeatable | CSWP 29 Appendix B |
| `csf:Tier_4_Adaptive` | Adaptief | Adaptive | CSWP 29 Appendix B |

EN-tekst-lengten Tier-dimensies (uit CSWP 29 Appendix B Table 2): 178-1.085 chars per Tier. Totaal ~4.900 chars EN over alle Tiers.

### SKOS-mappings (Stap 6 v4.6.0) — Tier ↔ Level

4 nieuwe `skos:relatedMatch` van `csf:CSFTier` naar `isms:MaturityCapabilityLevel`:

| Tier | ↔ | Level |
|---|---|---|
| `csf:Tier_1_Partial` | skos:relatedMatch | `isms:Level_1` (Ad-hoc) |
| `csf:Tier_2_RiskInformed` | skos:relatedMatch | `isms:Level_2` (Informeel) |
| `csf:Tier_3_Repeatable` | skos:relatedMatch | `isms:Level_4` (Geëvalueerd) |
| `csf:Tier_4_Adaptive` | skos:relatedMatch | `isms:Level_5` (Geïntegreerd) |

**`isms:Level_3` (Vastgesteld) krijgt geen Tier-equivalent** — G1-discipline. CSF heeft 4 Tiers, NBA-LIO/NOREA 5 Levels. Tussen-mapping zou geforceerd zijn.

### Locatie van Tier↔Level mappings

In m21 (csf-zijde), conform target-module-precedent v4.5.0 Stap 5+6. NIET in m06 — m06 ontvangt mappings, m21 levert ze.

## v4.5.0-uitbreiding — Core + IE (in herinnering)

| Element | Aantal |
|---|---:|
| 4 csf-klassen (Function/Category/Subcategory/ImplementationExample) | 4 |
| 3 csf-properties (partOfFunction/partOfCategory/exemplifies) | 3 |
| csf:csfIdentifier DP | 1 |
| 6 Functions + 22 Categories + 106 Subcategories + 363 IE | 497 |

## D9-toepassing — Optie B

NIST CSF 2.0 blijft **gemapt referentiekader**, niet organiserend kader. Tiers-uitbreiding versterkt D9 niet aanvullend — gebruik via SKOS-mappings naar isms-cluster respecteert framework-grenzen.

## D6 — symmetrische toepassing v1.9

`csf:riskGovernanceDescription` en `csf:riskManagementDescription` zijn **@en-only**. Dit is de **eerste concrete toepassing van D6-symmetrische uitbreiding v1.9**:

> "Lange normatieve EN-tekst blijft @en-only tenzij gezaghebbende NL-bron beschikbaar (CSF Tier-descriptions-precedent)"

Bilingual `rdfs:label` voor Tier-individuals (kort), @en-only voor descriptions (lang normatief, geen gezaghebbende NL-vertaling).

## Naam-discipline — CSFTier vs RiskManagementTier

Twee Tier-concepten in het model:

| Klasse | Module | NIST-publicatie | Aantal levels |
|---|---|---|---|
| `risk:RiskManagementTier` | M03 | NIST SP 800-39 | 3 levels (organisational tiers) |
| `csf:CSFTier` | M21 (v4.6.0) | NIST CSF 2.0 | 4 levels (organizational profile tiers) |

Verschillende NIST-publicaties, verschillende concepten. Naam expliciet **"CSFTier"** gekozen om collision te voorkomen. Bij SPARQL-query's: namespace-onderscheid kritisch.

## Geparkeerde items uit M21

- [[brain__architecture__H33_m11-sp800-53-substantiele-uitbreiding]] — m11 modelbeperking (124/~1000)
- [[brain__architecture__H34_m11-enhancement-modellering]] — m11 enhancements (17 unique)
- [[brain__architecture__H35_cbb-528-typo-interpretatie]] — sheet 8 UV 10.4 typo

## Bronlicentie

| Bron | Licentie | SourceAttribution-individual |
|---|---|---|
| NIST CSWP 29 (CSF 2.0 Core) | Public Domain | `ext:Attr_NIST_CSF_2_0_Core_2024` |
| CSF 2.0 Implementation Examples Excel | Public Domain | `ext:Attr_NIST_CSF_2_0_Core_2024` |
| CSF Reference Tool (mappings) | Public Domain | `ext:Attr_NIST_CSF_2_0_Reference_Tool_2026` |
| Sheet 8 (CBW-Excel) — gebruikt in Stap 5 v4.5.0 | CC-BY 4.0 | `ext:Attr_CBW_NIS2_Framework_2025_CC_BY_4_0` (in m10) |

## Cross-references

- [[brain__decisions__D03_10-namespaces]] — csf: als 11e namespace
- [[brain__decisions__D06_meeliftregel-tweetalig]] — symmetrische toepassing v1.9 (CSF Tier-descriptions @en-only)
- [[brain__decisions__D09_framework-neutraliteit]] — Optie B in actie
- [[brain__concepts__cross-bron-overlap]] — S5∩S6 = 105 kwaliteits-validatie
- [[brain__concepts__parallelle-maturity-clusters]] — Tier↔Level mapping richting isms (niet biz)
- [[brain__sprints__v4_5_0_fase-3-nist-csf-2-0]] — sprint van Core + IE
- [[brain__sprints__v4_6_0_fase-4-ensia-en-volwassenheid]] — sprint van Tiers
- [[brain__sources__nist-csf-2-0]] — bron-detail
- [[brain__modules__M06_isms]] — target van Tier↔Level SKOS-mappings

— Einde M21.
