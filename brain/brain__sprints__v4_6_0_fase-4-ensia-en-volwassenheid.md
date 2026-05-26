---
type: sprint
id: v4.6.0
title: v4.6.0 — Fase 4: M15-ENSIA-uitbouw + Volwassenheidsmodel
status: active
date: 2026-05-21
related:
  - v4_5_0_fase-3-nist-csf-2-0
  - D06_meeliftregel-tweetalig
  - D09_framework-neutraliteit
  - parallelle-maturity-clusters
  - cross-bron-overlap
sources:
  - patch-rapport-v4_6_0
  - canonical_metrics_v4_6_0
  - projectinstructie-v1.9
chat-sources: []
confidence: high
---

# v4.6.0 — Fase 4: M15-ENSIA-uitbouw + Volwassenheidsmodel

## Status

**Huidige actieve baseline** sinds 21 mei 2026. Opvolger van v4.5.0. Laatste sprint vóór migratie naar Claude Code + GitHub.

Doorlooptijd: 20 — 21 mei 2026 (sprint-protocol B + 2 heads-up + 1 scope-pauze).

Bron: `patch-rapport-v4_6_0.md`, `canonical_metrics_v4_6_0.json`, `projectinstructie-v1.9.md`.

## Scope: vijf stappen + V1-uitkomst Optie B

| Stap | Inhoud | Triple-impact |
|---|---|---:|
| 1 | Pre-sprint-inventarisatie (Protocol B) — 4 vragen, scope-impact ontdekt | read-only |
| 2 | TBox-uitbreidingen: 5 isms-klassen + 1 csf-klasse + 3 OP + 2 DP + 2 SourceAttributions | +80 |
| 3 | Statische ABox: 5 isms:MaturityCapabilityLevel + 4 csf:CSFTier (Optie C bilinguaal) | +71 |
| 4 | Sheet 6 ABox: 32 Capabilities + 160 LevelDescriptions in m06 | +1.440 |
| 5 | M15-ENSIA-uitbouw met scope-pauze (A3+B3+C2) — promotie naar fw:GRCFramework | netto +15 |
| 6 | SKOS-mappings: 4 Tier↔Level skos:relatedMatch | +4 |
| **Sprint-totaal** | — | **+1.610** |

## Triple-impact

| Metric | v4.5.0 | v4.6.0 | Δ |
|---|---:|---:|---:|
| Pre-inferentie triples | 19.340 | 20.950 | **+1.610** (+8,3%) |
| Post OWL RL | 41.988 | 44.907 | +2.919 |
| Klassen | 193 | 199 | +6 (5 isms + 1 csf) |
| NamedIndividuals | 1.179 | 1.383 | **+204** |
| ObjectProperties | 146 | 149 | +3 (isms:hasLevelDescription, forCapability, atMaturityLevel) |
| DatatypeProperties | 94 | 96 | +2 (csf:riskGovernance/Management-Description) |
| `owl:sameAs` | 98 | 98 | 0 (D5 + D11 ongewijzigd) |
| SKOS-mappings | 1.794 | 1.798 | +4 (Tier↔Level) |
| Namespaces (D3) | 11 | 11 | 0 (ongewijzigd) |
| Modules | 22 | 22 | 0 (geen nieuwe, 5 gewijzigd) |
| SHACL RUN 1 | 0 | 0 | 0 ✓ |
| SHACL RUN 2 | 290 | 290 | 0 ✓ (identieke false-positives) |

## Wijzigingen per module — 5 gewijzigd

| Module | Wijziging |
|---|---|
| **grc-core.ttl** | Versie-bump v4.5.0 → v4.6.0, modified 2026-05-21 |
| **m01-framework.ttl** | + `ext:Attr_ENSIA_Logius_2024` SourceAttribution + `fw:ENSIA` als `fw:GRCFramework` met 12 properties (incl. nieuwe `fw:status@nl/@en` + `fw:hasPublicationDate 2024-12-19` + verplaatste `fw:toetst fw:BIO_2_0` uit m15) |
| **m06-isms.ttl** | + 5 isms-klassen (MaturityCapability + 2 subclasses + MaturityCapabilityLevel + CapabilityLevelDescription) + 3 OP + 5 Level-individuals + 32 Capabilities + 160 LevelDescriptions + `ext:Attr_NBA_LIO_NOREA` SourceAttribution (SHA256) |
| **m15-ensia.ttl** | Oude `fw:ENSIA rdf:type fw:Guideline`-blok + dubbele properties verwijderd; NB-comment + 8 ext:hasAuditDomain + 2 skos:relatedMatch behouden |
| **m21-csf.ttl** | + `csf:CSFTier`-klasse + 2 DP + 4 Tier-individuals (Tier_1..4 Optie C) + 4 skos:relatedMatch naar `isms:MaturityCapabilityLevel` |

## V1-uitkomst — Optie B gekozen ondanks bestaande biz:cluster

**Fase 4 V1-evaluatie (21 mei 2026 Stap 2):** `biz:MaturityAssessment` + `biz:MaturityLevel` (ML_0..5 CMMI) + 6 `biz:GRCDomain`-individuals waren al OPERATIONEEL in m07 voor GRCDomain-dashboard-aggregatie.

V1-keuze: **nieuwe isms-cluster naast biz** ipv hergebruik:

| Cluster | Semantiek | Niveau-schaal | Domain | Behoud |
|---|---|---|---|---|
| **biz** (m07, sinds initieel) | GRCDomain-volwassenheid | 6 levels (ML_0..ML_5, CMMI) | `biz:GRCDomain` | ONGEWIJZIGD — biz:Dashboard_2026_Q1 aggregaten blijven werken |
| **isms** (m06, NIEUW v4.6.0) | Control/Capability-evaluatie | 5 levels (Level_1..Level_5, NBA-LIO/NOREA) | 32 `isms:MaturityCapability` (Cbw + ISMS) | Sheet 6 evaluaties uit CBW-Excel |

**Niet samenvoegen** — verschillende semantieken, verschillende schaal-grootten, verschillende domains. Zie [[brain__concepts__parallelle-maturity-clusters]] voor de architectuur-betekenis.

## D9 — vierde verificatie-cluster

v4.6.0 voegt **ENSIA als gelijkwaardig fw:GRCFramework-individual** toe (geen audit-kader-privilege).

Cumulatief D9-bewijs:
1. NIS2-EU + CBW-NL (v4.4.0, horizontale transpositie)
2. CBW + Cbb (v4.4.0, wet → AMvB)
3. NIST CSF 2.0 (v4.5.0, gemapt referentiekader Optie B)
4. **ENSIA-audit (v4.6.0, gelijkwaardig framework zonder audit-kader-privilege)**

Concrete keuzes voor ENSIA conform D9:
- Geen aparte audit-namespace — fw: is voldoende
- Geen "audit kader"-class — fw:GRCFramework volstaat
- Hybride locatie (A3+B3+C2): kern in m01, domein-specifiek (audit-domains) in m15
- Mappings via SKOS, niet via hiërarchische subordering

## Architectuur-keuzes Stap 5 (masterchat A3+B3+C2)

Scope-pauze tijdens uitvoering — pre-sprint vraag D bleek incompleet (alleen m01 ingekeken, niet model-breed). Werkelijke m15 bevatte al `fw:toetst fw:BIO_2_0`.

| Sub-keuze | Inhoud |
|---|---|
| **A3** | Behoud bestaande 3 issuers (DutchCentral, NOREA, VNG); fw:Logius NIET als issuer toegevoegd |
| **B3** | Hybride locatie: kerndeclaratie in m01, domeinspecifieke aanvullingen in m15 |
| **C2** | Geen 2e fw:toetst naar ISO 27001 — ENSIA toetst formeel alleen BIO, ISO blijft skos:relatedMatch |

## CSF Tiers — Optie C masterchat-GO

| Aspect | Keuze |
|---|---|
| Tier-individuals | Tier_1_Partial, Tier_2_RiskInformed, Tier_3_Repeatable, Tier_4_Adaptive |
| `rdfs:label` | Bilingual @nl/@en |
| `csf:csfIdentifier` | Zonder language-tag |
| `csf:riskGovernanceDescription` + `csf:riskManagementDescription` | @en-only — lange normatieve tekst zonder gezaghebbende NL-bron |
| Naam-keuze | Expliciet "CSFTier" (niet "Tier") om collision met `risk:RiskManagementTier` te voorkomen |

EN-tekst-lengten Tier-dimensies (uit CSWP 29 Appendix B Table 2): 178-1.085 chars, totaal ~4.900 chars.

## D6 — symmetrische toepassing v4.6.0

[[brain__decisions__D06_meeliftregel-tweetalig]] vertaling-scope uitgebreid in projectinstructie v1.9:

> "Symmetrische toepassing v4.6.0: lange normatieve EN-tekst blijft @en-only tenzij gezaghebbende NL-bron beschikbaar (CSF Tier-descriptions-precedent)"

Concreet: CSF Tier-descriptions (lange normatieve NIST-tekst) blijven @en. Eerder: lange normatieve NL-tekst blijft @nl tenzij gezaghebbende EN-bron. Beide richtingen nu gelijkwaardig.

## Sprint-protocollen — vier nieuwe geformaliseerd in projectinstructie v1.9

Concrete leerpunten uit v4.6.0 zijn formeel sprint-protocollen geworden. Zie [[brain__workflow__sprint-protocollen]] voor de volledige discipline.

| Protocol | Bron-leerpunt | Concrete v4.6.0-toepassing |
|---|---|---|
| **Pre-sprint-multi-module-discipline** | §8.1 — vraag D was te smal | Stap 5 scope-pauze: m15 had al fw:toetst dat in pre-sprint miste |
| **Ramings-baseline rdf:type-dubbele-telling** | §8.4 — rdflib telt type dubbel | Stap 4 +44% boven raming, volledig verklaarbaar (5+8 ipv 4+6 triples) |
| **Instructie-consistentie code-block vs toelichting** | §8.2 — sample toonde 2e fw:toetst | Stap 5 C2: toelichting leidend ipv code-block |
| **Bron-typo-beleid patroon-criterium** | §8.6 — wel/niet corrigeren | Stap 4: 4 typo's in Capability-rdfs:label gecorrigeerd (presentatie); rdfs:comment niveau-beschrijvingen bron-getrouw behouden |

## Property-semantiek-discipline — nieuwe gedragsregel

Uit §8.3 leerpunt — geformaliseerd als gedragsregel in projectinstructie v1.9:

> Rol-onderscheid bij framework-individual-properties: issuer ≠ beheerder; uitgever ≠ uitvoerder. Niet samenvoegen onder één property als rollen ontologisch verschillen.

Concrete v4.6.0-toepassing: `fw:Logius` NIET als `fw:issuedBy` ENSIA toegevoegd (Logius beheert, geeft niet uit). Bestaande 3 issuers (BZK/DutchCentral, NOREA, VNG) behouden.

## Nieuwe kandidaat-overweging — geen H-item

| Overweging | Trigger-criterium |
|---|---|
| `fw:isManagedBy`-property voor beheerder-rol | Indien meerdere frameworks beheerder-rol-modellering vereisen (bv. NL Cybersecurity-strategie waar Logius/NCSC/BZK verschillende rollen hebben) |

Niet als H-item geregistreerd — wacht op natuurlijk trigger.

## Sample-first + heads-up protocol-touchpoints

| Touchpoint | Inhoud |
|---|---|
| **Stap 3.4.2 EN-tekst Optie C** | Sample-first: 1 Tier complete output → masterchat-validatie → 3 overige |
| **Stap 4 pre-stap mini-inventarisatie** | Sample-first (1 Capability + 5 LevelDescriptions) + 3 beslis-punten (typo-correcties, EN-vertalingen, comment-tekst-strategie) |
| **Stap 5 m15-harmonisatie A3+B3+C2** | Scope-pauze + masterchat-correctie op vier sub-keuzes |

## Bron-typo-correcties Stap 4

| Capability | Origineel | Correctie | Veld |
|---|---|---|---|
| Cbw_05 | "Bedrijfscontinuiteit" | "Bedrijfscontinuïteit" | rdfs:label@nl |
| Cbw_11 | "Cyberhygiene" | "Cyberhygiëne" | rdfs:label@nl |
| Cbw_12 | "Cyberhygiene" / "specieke" | "Cyberhygiëne" / "specifieke" | rdfs:label@nl |
| Cbw_14 | "tav" | "t.a.v." | rdfs:label@nl |

Bron-attribuering naar NBA-LIO/NOREA blijft. Correctie alleen op presentatie (rdfs:label), bron-tekst (rdfs:comment niveau-beschrijvingen) bron-getrouw behouden.

## isms:Level_3 niet gemapped naar CSF Tier (G1-discipline)

CSF heeft 4 Tiers, NBA-LIO/NOREA 5 Levels. `isms:Level_3` (Vastgesteld) ligt conceptueel tussen Tier_2 en Tier_3. Tussen-mapping zou geforceerd zijn.

Mapping-tabel daadwerkelijk gelegd:

| Tier | ↔ | Level |
|---|---|---|
| `csf:Tier_1_Partial` | `skos:relatedMatch` | `isms:Level_1` (Ad-hoc) |
| `csf:Tier_2_RiskInformed` | `skos:relatedMatch` | `isms:Level_2` (Informeel) |
| `csf:Tier_3_Repeatable` | `skos:relatedMatch` | `isms:Level_4` (Geëvalueerd) |
| `csf:Tier_4_Adaptive` | `skos:relatedMatch` | `isms:Level_5` (Geïntegreerd) |

`isms:Level_3` ontbreekt bewust. Documentatie in scope-register.

## Geparkeerde items — onveranderd

Alle H-items (H15, H21, H25, H26, H27, H29-31, H32, H33, H34, H35) onveranderd. Geen nieuwe H-items in v4.6.0.

## Sprint-multiplier-mijlpaal

| Sprint | Pre-inf Δ triples | Multiplier t.o.v. v4.4.0 |
|---|---:|---:|
| v4.3.3 | +52 | 0,07× |
| v4.4.0 | +702 | 1× (referentie) |
| v4.5.0 | +5.899 | 8,5× |
| **v4.6.0** | +1.610 | **2,7×** |

v4.6.0 onder oorspronkelijke prognose (5-7×) dankzij hergebruik bestaande m15-structuur en pre-sprint-discipline.

## Bestand-wijzigingen

5 modules gewijzigd; 17 modules bytewise identiek aan v4.5.0-eindstand.

## Volgende fase — MIGRATIE naar Claude Code + GitHub

v4.6.0 is de **laatste geplande Spoor A-sprint** voor de bedoelde Fase 1-4 scope. Volgende activiteit: migratie van Tech/Brein/Dashboard chats naar Claude Code + GitHub repo. Zie `migratie-roadmap.md` en `handover-master-v4.5.0.md` (in PK) voor uitvoeringsdetail.

v4.7.0 = eerste post-migratie-sprint, scope nog te bepalen. Kandidaten:
- SKOS-kwaliteitsanalyse formeel als sprint (1.798 mappings)
- ENISA TIG-PDF-integratie via Analyse-opdracht 2.0
- Spoor B-voorbereiding (T&I lab-test)

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-21 | active | Oplevering v4.6.0 Fase 4 — M15-ENSIA + Volwassenheidsmodel + CSF Tiers; 5 modules gewijzigd; +1.610 triples |

## Cross-references

- [[brain__sprints__v4_5_0_fase-3-nist-csf-2-0]] — voorganger
- [[brain__decisions__D06_meeliftregel-tweetalig]] — symmetrische toepassing v4.6.0
- [[brain__decisions__D09_framework-neutraliteit]] — vierde verificatie-cluster
- [[brain__concepts__parallelle-maturity-clusters]] — NIEUW concept biz vs isms
- [[brain__concepts__cross-bron-overlap]] — relevant voor toekomstige SKOS-kwaliteitsanalyse
- [[brain__modules__M01_framework]] — fw:ENSIA gepromoot
- [[brain__modules__M06_isms]] — volwassenheidsmodel-cluster nieuw
- [[brain__modules__M07_business]] — biz blijft ongewijzigd
- [[brain__modules__M15_ensia]] — uitgebreid naar productie
- [[brain__modules__M21_nist-csf-2-0-planned]] — CSF Tiers toegevoegd
- [[brain__workflow__sprint-protocollen]] — 4 nieuwe protocollen formeel
- [[brain__architecture__H-register]] — alle items onveranderd

— Einde v4.6.0.
