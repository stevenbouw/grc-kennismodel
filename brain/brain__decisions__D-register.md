---
type: index
id: D-register
title: D-register — Ontwerpbeslissingen GRC Kennismodel
status: living
date: 2026-05-21
---

# D-register — Ontwerpbeslissingen GRC Kennismodel

Twaalf vastgestelde ontwerpbeslissingen die de architectuur bepalen. Wijzigingen vereisen masterchat-goedkeuring.

## Overzicht

| ID | Beslissing | Status | Datum | Detail |
|---|---|---|---|---|
| D1 | OWL 2 DL profiel | active | Initieel | [[brain__decisions__D01_owl-2-dl-profiel]] |
| D2 | Turtle-serialisatie | active | Initieel | [[brain__decisions__D02_turtle-serialisatie]] |
| D3 | 11 namespaces (csf: toegevoegd v4.5.0) | active | v4.2.0 + v4.5.0 uitbreiding | [[brain__decisions__D03_10-namespaces]] |
| D4 | SKOS voor cross-framework mappings | active | Initieel | [[brain__decisions__D04_skos-cross-framework-mappings]] |
| D5 | owl:sameAs strikt ctrl:↔bio: (93 asserties) | active | Initieel | [[brain__decisions__D05_sameAs-strikt-ctrl-bio]] |
| **D6** | **Tweetalige annotaties — meeliftregel + symmetrische vertaling-scope v1.9** | **active** | **v4.1.0 + v1.7 + v1.9 symmetrische uitbreiding** | [[brain__decisions__D06_meeliftregel-tweetalig]] |
| D7 | BIO 2.0 als twee klassen (BIOControl + OverheidsMaatregel) | active | Initieel | [[brain__decisions__D07_bio2-twee-klassen]] |
| D8 | Eén canonieke SoA (isms:SoA_2026 + 93 SoAEntry_*) | active | v4.2.2 Route A | [[brain__decisions__D08_canonieke-soa]] |
| **D9** | **Framework-neutraal model — VIER verificatie-clusters per v4.6.0** | **active** | **17 mrt 2026 + v4.4.0 + v4.5.0 + v4.6.0 verificatie** | [[brain__decisions__D09_framework-neutraliteit]] |
| D10 | COSO ICF/ERM als enterprise-governance-laag | active | 17 mrt 2026 | [[brain__decisions__D10_coso-enterprise-governance]] |
| D11 | owl:sameAs asset-convergentie — ster-patroon (5 bridges) | active | 13 apr 2026 | [[brain__decisions__D11_sameAs-asset-convergentie]] |
| D12 | Drie-laags compliance-architectuur — patroon, geen starre symmetrie | active | 22 apr 2026 + v4.4.0 verfijning | [[brain__decisions__D12_drie-laags-compliance]] |

## Updates in iteratie 11 (v4.6.0 + v1.9-verwerking)

| D | Wijziging |
|---|---|
| D6 | **Symmetrische vertaling-scope-uitbreiding v1.9**: lange normatieve EN-tekst @en-only tenzij gezaghebbende NL-bron beschikbaar. Concrete toepassing: CSF Tier-descriptions (~4.900 chars EN, geen NL-bron). |
| D9 | **Vierde verificatie-cluster**: ENSIA als audit-kader gepromoot van fw:Guideline → fw:GRCFramework, zonder audit-kader-privilege. Bewijst dat D9 ook werkt voor verschillende framework-soorten (EU-richtlijn / NL-wet / US-cybersecurity-framework / NL-audit-kader). |

Alle overige D-decisions onveranderd. D5 (93 sameAs) en D11 (5 sameAs) hetzelfde aantal als v4.5.0.

## Nieuwe gedragsregel v1.9 (geen aparte D-decision)

**Property-semantiek-discipline**: rol-onderscheid bij framework-individual-properties — issuer ≠ beheerder; uitgever ≠ uitvoerder. Niet samenvoegen onder één property als rollen ontologisch verschillen.

Concrete v4.6.0-toepassing: `fw:Logius` NIET als `fw:issuedBy` ENSIA. Bestaande 3 issuers (BZK/DutchCentral, NOREA, VNG) behouden. `fw:isManagedBy` toegevoegd aan overwegingen-pool als toekomstige kandidaat-property.

Niet geformaliseerd als D-decision (te smal). Wel verwerkt in sprint v4.6.0-file en als gedragsregel in projectinstructie v1.9.

## Clusters per architectuur-domein

| Cluster | D-decisions | Hoofd-domein |
|---|---|---|
| Profiel & serialisatie | D1, D2 | OWL-keuze |
| Cross-framework | D3, D4 | Namespaces + mappings |
| sameAs-discipline | D5, D11 | Equivalentie-bruggen |
| Annotaties | D6 | Tweetaligheid + scope (3 versies — initieel, v1.7, v1.9) |
| BIO 2.0 + SoA | D7, D8 | Operationele kader |
| Framework-architectuur | D9, D10, D12 | Hoog-niveau structuur (D9 nu op 4 clusters bewezen) |

## Cross-references

- [[brain__concepts__concept-register]] — concepts die D-decisions toepassen
- [[brain__sprints__sprint-register]] — sprints waarin D-decisions zijn vastgelegd
- [[brain__architecture__H-register]] — open architectuur-vragen die D-decisions raken

— Einde D-register.
