# grc-domein — kaders-reference (bijlage)

Reference-detail bij `SKILL.md`. Alle gegevens geverifieerd tegen `ontology/m01-framework.ttl`, `ontology/m17-coso-cobit.ttl`, `ontology/m15-ensia.ttl` en `ontology/grc-core.ttl` (baseline v4.6.3, 28 mei 2026). Geen verbatim NEN-tekst (Protocol 17). De vijf-lagen-ordening is functioneel, niet hiërarchisch (D9 — zie SKILL §1).

## 1. Per-kader-tabel

Namespace-codes (uit `grc-core.ttl`): `fw:` framework · `ctrl:` control · `bio:` BIO · `compl:` compliance/wettelijke verplichting · `isms:` ISMS · `csf:` NIST CSF · `ext:` extended. Elf namespaces totaal (D3).

| Laag | Kader | Type-klasse (m01) | Jurisdictie | Module |
|---|---|---|---|---|
| 0 | COSO ICF (`fw:COSO_ICF`) | enterprise-governance | INT | m17 |
| 0 | COSO ERM (`fw:COSO_ERM`) | enterprise-governance | INT | m17 |
| 1 | COBIT 2019 (`fw:COBIT_2019`) | `fw:Standard` | INT | m01 + m17 |
| 1 | Besluit BVA-stelsel Rijksdienst (`fw:BesluitBVAStelsel`) | `fw:NationalLaw` | NL | m01 |
| 1 | Besluit CIO-stelsel Rijksdienst (`fw:BesluitCIOStelsel`) | `fw:NationalLaw` | NL | m01 |
| 2 | NIS2-richtlijn (`fw:NIS2_Directive`) | `fw:EUDirective` | EU | m01 |
| 2 | VIR 2007 (`fw:VIR_2007`) | `fw:NationalLaw` | NL | m01 |
| 2 | VIRBI 2025 (`fw:VIRBI_2025`) | `fw:NationalLaw` | NL | m01 + m16 |
| 2 | AVG / GDPR (IB-raakvlakken) | `compl:`-verplichtingen | EU/NL | m14 |
| 2 | CBW — Cyberbeveiligingswet (`fw:CBW`) | `fw:NationalLaw` — **status "in voorbereiding"** | NL | m01 |
| 2 | Cbb — Cyberbeveiligingsbesluit (`fw:Cbb`) | `fw:NationalLaw` (AMvB) — **status "concept t.b.v. Tweede Kamer, nog niet vastgesteld"** | NL | m01 |
| 2 | DORA (`fw:DORA_Regulation`) | `fw:EURegulation` — **referentie; de organisatie valt er niet onder** | EU | m01 + m12 |
| 3 | BIO 2.0 (`fw:BIO_2_0`) | `fw:GovernmentBaseline` — operationeel; dashboard-view | NL | m08 |
| 4 | ISO/IEC 27001:2022 (`fw:ISO_IEC_27001_2022`) | `fw:InternationalStandard` | INT | m09 |
| 4 | ISO/IEC 27002:2022 (`fw:ISO_IEC_27002_2022`) | `fw:InternationalStandard` | INT | m02 |
| 4 | ISO/IEC 27005:2022 (`fw:ISO_IEC_27005_2022`) | `fw:InternationalStandard` | INT | m03 |
| 4 | ISO 31000:2018 (`fw:ISO_31000_2018`) | `fw:InternationalStandard` | INT | m03 |
| 4 | ISO 22301:2019 (`fw:ISO_22301_2019`) | `fw:InternationalStandard` | INT | m13 |
| 4 | ISO 22313:2020 (`fw:ISO_22313_2020`) | `fw:InternationalStandard` | INT | m13 |
| 4 | NIST SP 800-53 R5 (`fw:NIST_SP_800_53_R5`) | `fw:Standard` | US | m11 |
| 4 | NIST SP 800-39 (`fw:NIST_SP_800_39`) | `fw:Standard` | US | m11 |
| 4 | NIST SP 800-30 R1 (`fw:NIST_SP_800_30_R1`) | `fw:Standard` | US | m11 |
| 4 | NIST CSF 2.0 (`fw:NIST_CSF_2_0`) | gemapt referentiekader (Optie B, D9) | US | m21 |
| 4 | Annex SL | structuur-conventie (ISO-managementsysteem) | INT | (cross-norm) |
| 5 | ENSIA (`fw:ENSIA`) | auditkader (`fw:GRCFramework`) | NL | m15 |
| 5 | Volwassenheidsmodel | maturity-cluster (isms-cluster, parallel aan biz:MaturityAssessment — niet samenvoegen) | — | m06 |

> **Let op (geen samenvoeging):** het isms-volwassenheidsmodel-cluster en het `biz:MaturityAssessment`-cluster zijn bewust parallel. Zie `brain__concepts__parallelle-maturity-clusters.md`.

## 2. Geverifieerde relatie-triples (letterlijk in de modules aanwezig)

Deze triples bestaan feitelijk in de ontologie (regelnummers v4.6.3-baseline):

```turtle
# m01-framework.ttl
fw:ISO_IEC_27002_2022  fw:geeftRichtlijnenVoor  fw:ISO_IEC_27001_2022 .   # r.505
fw:NIS2_Directive      fw:transposedBy          fw:CBW .                  # r.651
fw:CBW                 fw:isTranspositieVan     fw:NIS2_Directive ;       # r.692
                       fw:uitgewerktIn          fw:Cbb .                  # r.693
fw:Cbb                 fw:werktUit              fw:CBW .                  # r.713
fw:BIO_2_0             fw:dektAf                fw:NIS2_Directive .       # r.731
fw:VIR_2007            fw:stelVerplicht         fw:BIO_2_0 .              # r.759
fw:ENSIA               fw:toetst                fw:BIO_2_0 .              # r.1039

# m17-coso-cobit.ttl
fw:COBIT_2019          fw:geeftITInvullingAan   fw:COSO_ICF , fw:COSO_ERM .  # r.329-330
# COSO-principes  ext:isComponentOf  fw:COSO_ICF / fw:COSO_ERM
# COBIT-objectives ext:isComponentOf fw:COBIT_2019
```

## 3. Relatie-property-definities (domain / range, parafrase comment)

Uit `m01-framework.ttl` SECTIE 2 + `m17-coso-cobit.ttl`:

| Property | Domain → Range | rdfs:label @nl / @en | Karakter |
|---|---|---|---|
| `fw:stelVerplicht` | GRCFramework → GRCFramework | stelt verplicht / mandates | directioneel, niet-symmetrisch |
| `fw:geeftRichtlijnenVoor` | GRCFramework → GRCFramework | geeft implementatierichtlijnen voor / provides implementation guidance for | directioneel |
| `fw:geeftITInvullingAan` | GRCFramework → GRCFramework | (IT-invulling van enterprise-kader) / provides IT-specific implementation of | directioneel |
| `fw:dektAf` | GRCFramework → GRCFramework | dekt eisen af van / covers requirements of | directioneel, niet-symmetrisch |
| `fw:toetst` | GRCFramework → GRCFramework | toetst / audits | directioneel |
| `fw:transposedBy` | EUDirective → NationalLaw | omgezet door / transposed by | inverse van `fw:isTranspositieVan` |
| `fw:isTranspositieVan` | NationalLaw → EUDirective | is omzetting van / is transposition of | inverse van `fw:transposedBy` |
| `fw:uitgewerktIn` | NationalLaw → NationalLaw | uitgewerkt in / elaborated in | inverse van `fw:werktUit` |
| `fw:werktUit` | NationalLaw → NationalLaw | werkt uit / elaborates | inverse van `fw:uitgewerktIn` |
| `ext:isComponentOf` | component → framework | (component-relatie) | vervangt het oude `compl:derivedFrom` voor component→framework |

Ondersteunend, generiek (geen inhoudelijke afhankelijkheid): `fw:relatedTo` (owl:SymmetricProperty), `fw:alignsWith`, `fw:supersedes` — alle GRCFramework → GRCFramework.

## 4. SKOS cross-category — basislijn-tabel

Samenvatting van `brain__concepts__cross-category-mappings.md` (kandidaat v1.3.1, **niet geformaliseerd — masterchat-werk**):

| Categorie-relatie | Basislijn-predicate | Toelichting |
|---|---|---|
| control ↔ control-eis (binnen categorie) | per cluster-discipline-default §3.1 | bv. ISO 27002 ↔ NIS2-art.21-letters (m10, T2 — 100% cluster-convergentie broadMatch) |
| **control ↔ legal-obligation (cross-category)** | **`skos:relatedMatch`** | bv. ISO 27002 ↔ AVG-artikel (m14, T3 — 27 paren relatedMatch; geen cluster-convergentie) |
| cross-category, retrieval-interchangeable | `skos:closeMatch` (uitzondering) | control = canonieke implementatie-equivalent van de verplichting (T3: 2 paren) |
| cross-category, conceptueel | `skos:exactMatch` | **structureel uitgesloten** |

`skos:exactMatch` is bovendien geblokkeerd door D4.1 wanneer de autoritatieve mapping-bron een non-equivalence-disclaimer bevat (onafhankelijk mechanisme).

— Einde kaders-reference.
