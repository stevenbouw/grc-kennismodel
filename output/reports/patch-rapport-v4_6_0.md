# PATCH-RAPPORT — GRC KENNISMODEL v4.6.0 FASE 4

**Versie:** 1.0
**Datum:** 21 mei 2026
**Opsteller:** Technische chat
**Sprint:** v4.6.0 — Fase 4 (M15-ENSIA-uitbouw + Volwassenheidsmodel)
**Basis:** v4.5.0-baseline (19 mei 2026)
**Doorlooptijd:** 20 — 21 mei 2026 (sprint-protocol B + 2 heads-up + 1 scope-pauze)

---

## §0. Executive samenvatting + kerncijfers

### Sprint-resultaat

**Scope-correct opgeleverd onder Optie A**: Volwassenheidsmodel-cluster (5 klassen + 3 OP + 2 DP) als nieuwe isms-cluster naast bestaande biz:MaturityAssessment-cluster (biz blijft ongewijzigd voor GRCDomain-dashboard). M15-ENSIA gepromoot van `fw:Guideline` naar `fw:GRCFramework` met volledige declaratie in m01. 32 Capabilities + 160 LevelDescriptions + 4 CSF Tier-individuals + 4 Tier↔Level-SKOS-mappings.

**Schaal-multiplier**: sprint-omvang **~2,7× v4.4.0** (oorspronkelijk geraamd 5-7× — onder ondergrens dankzij hergebruik bestaande m15-structuur in Stap 5).

**Cross-bron-overlap-kwaliteits-indicator**: bestaande m15 fw:ENSIA bevatte al `fw:toetst fw:BIO_2_0`, 3 issuers + 2 SKOS-mappings + 8 audit-domains. Pre-sprint-rapport miste dit (vraag D was te smal); werkelijke harmonisatie was minder ingrijpend dan instructie suggereerde (zie §8 leerpunt 1).

### Baseline-vergelijking (uit canonical_metrics_v4.6.0.json, niet uit memorie)

| Metric | v4.5.0 baseline | **v4.6.0 eindstand** | Δ | Bron |
|---|---:|---:|---:|---|
| Pre-inferentie triples | 19.340 | **20.950** | **+1.610** (+8,3%) | `global_pre_inference.triples` |
| Post-inferentie triples (OWL RL) | 41.988 | **44.907** | +2.919 | `global_post_inference_owlrl.triples` |
| `owl:Class` | 193 | **199** | +6 | 5 isms + 1 csf |
| `owl:NamedIndividual` | 1.179 | **1.383** | **+204** | 5 Level + 4 Tier + 32 Cap + 160 LevelDesc + 2 Attr + 1 fw:ENSIA |
| `owl:ObjectProperty` | 146 | **149** | +3 | 3 isms (hasLevelDescription, forCapability, atMaturityLevel) |
| `owl:DatatypeProperty` | 94 | **96** | +2 | 2 csf (riskGovernance/ManagementDescription) |
| `owl:sameAs` | 98 | **98** | 0 (ongewijzigd) | D5 + D11 |
| SKOS-mappings totaal | 1.794 | **1.798** | +4 | 4 Tier↔Level relatedMatch |
| `owl:Nothing` post-inferentie | 0 | **0** ✓ | consistent | |
| SHACL violations RUN 1 (`inference='none'`) | 0 | **0** ✓ | conform | |
| SHACL violations RUN 2 (`inference='owlrl'`) | 290 | **290** ✓ | identiek (bekende false-positives) | |
| Namespaces (D3) | 11 | **11** | 0 (ongewijzigd) | |
| Modules (.ttl) | 22 | **22** | 0 (geen nieuwe module) | |
| Modules gewijzigd | — | **5** | — | grc-core, m01, m06, m15, m21 |

### Bron-attributies in model na v4.6.0

| SourceAttribution-individual | Toegevoegd in | Licentie |
|---|---|---|
| `ext:Attr_CBW_NIS2_Framework_2025_CC_BY_4_0` | v4.4.0 | CC-BY 4.0 |
| `ext:Attr_NIST_CSF_2_0_Core_2024` | v4.5.0 | Public Domain |
| `ext:Attr_NIST_CSF_2_0_Reference_Tool_2026` | v4.5.0 | Public Domain |
| `ext:Attr_NBA_LIO_NOREA_Volwassenheidsmodel_via_CBW_2026` | **v4.6.0 Stap 2** (in m06, SHA256-bron) | CC-BY 4.0 (via CBW-Excel) |
| `ext:Attr_ENSIA_Logius_2024` | **v4.6.0 Stap 5** (in m01) | Vrij gebruik met bronvermelding |

---

## §1. Stap 2 — TBox-uitbreidingen (+80 triples)

| Element | Locatie |
|---|---|
| 5 nieuwe klassen (MaturityCapability + 2 subclasses CbwCapability/ISMSCapability + MaturityCapabilityLevel + CapabilityLevelDescription) | m06-isms.ttl |
| 1 nieuwe klasse (CSFTier ⊑ ext:FrameworkComponent, expliciete naam om collision met risk:RiskManagementTier te voorkomen) | m21-csf.ttl |
| 3 ObjectProperties (hasLevelDescription/forCapability inverseOf-paar + atMaturityLevel) | m06-isms.ttl |
| 2 DatatypeProperties (riskGovernanceDescription/riskManagementDescription) | m21-csf.ttl |
| 1 SourceAttribution Attr_NBA_LIO_NOREA met SHA256 CBW-Excel | m06-isms.ttl |
| grc-core versie-bump v4.5.0 → v4.6.0, modified 2026-05-21 | grc-core.ttl |

---

## §2. Stap 3 — Statische ABox (+71 triples)

| Individuals | Aantal | Locatie |
|---|---:|---|
| `isms:MaturityCapabilityLevel` (Level_1..5) — bilinguaal label + comment | 5 | m06-isms.ttl |
| `csf:CSFTier` (Tier_1_Partial..Tier_4_Adaptive) — Optie C | 4 | m21-csf.ttl |

**Optie C masterchat-GO**: bilinguale `rdfs:label`, `csf:csfIdentifier` zonder language-tag, `csf:riskGovernanceDescription` + `csf:riskManagementDescription` @en-only (lange normatieve tekst zonder gezaghebbende NL-bron; D6-symmetrische toepassing).

EN-tekst-lengten Tier-dimensies (uit CSWP 29 Appendix B Table 2): 178-1.085 chars. Totaal ~4.900 chars EN.

---

## §3. Stap 4 — Sheet 6 ABox (+1.440 triples)

32 Capabilities + 160 LevelDescriptions in m06-isms.ttl.

| Cluster | Aantal | IRI-conventie |
|---|---:|---|
| `isms:CbwCapability`-individuals | 23 | `isms:Cap_Cbw_01..23` |
| `isms:ISMSCapability`-individuals | 9 | `isms:Cap_ISMS_01..09` |
| `isms:CapabilityLevelDescription`-individuals | 160 | `isms:CapLevel_<CapID>_Level_<N>` |

**4 typo-correcties** in NL-labels (masterchat-GO): Cbw_05/11/12/14. Niveau-beschrijvingen (rdfs:comment) bron-getrouw uit CBW-Excel.

**EN-vertalingen**: 23 Cbw door masterchat geleverd; 9 ISMS via ISO 27001:2022-standaard-clausule-titels (autoritatieve EN-bron).

**Triple-impact-decompositie** (verklaart +44% boven instructie-raming 900-1.000):
- Per Capability: 5 triples (2 rdf:type, 2 label, 1 sourceAttribution) × 32 = 160
- Per LevelDescription: 8 triples (2 rdf:type, 2 label, 1 forCapability, 1 atMaturityLevel, 1 comment, 1 sourceAttribution) × 160 = 1.280
- **Verklaring**: rdflib telt rdf:type-dubbel (class-membership + NamedIndividual-membership). Pre-stap-raming nam 4+6 per element; werkelijk 5+8. Geen bron-afwijking.

---

## §4. Stap 5 — M15-ENSIA-uitbouw (netto +15 triples)

**Scope-pauze tijdens uitvoering**: pre-sprint vraag D bleek incompleet (alleen m01 ingekeken, niet model-breed). Werkelijke m15 bevatte al uitgebreide fw:ENSIA-declaratie incl. `fw:toetst fw:BIO_2_0` (pre-sprint claimde 0 uses). Masterchat-GO op **A3+B3+C2**.

### Wijzigingen

| Locatie | Wijziging |
|---|---|
| m01 nieuw | `ext:Attr_ENSIA_Logius_2024` SourceAttribution |
| m01 nieuw | `fw:ENSIA` als `fw:GRCFramework`-individual met 12 properties (incl. nieuwe `fw:status@nl/@en` + `fw:hasPublicationDate 2024-12-19` + verplaatste `fw:toetst fw:BIO_2_0` uit m15) |
| m15 verwijderd | Oude `fw:ENSIA rdf:type fw:Guideline`-blok + dubbele properties (label, kern-comment, hasIdentifier, hasVersionLabel, isMandatoryForDutchGovernment, issuedBy, appliesInJurisdiction, hasDomain, fw:toetst, officialURL) |
| m15 behouden | NB-comment over gemeenten-context, `ext:hasAuditDomain × 8`, `skos:relatedMatch × 2` |

### Architectuur-keuzes (masterchat A3+B3+C2)

- **A3** Behoud bestaande 3 issuers (DutchCentral, NOREA, VNG); fw:Logius NIET als issuer toegevoegd. Logius = beheerder, niet uitgever — semantiek-discipline (zie §8 leerpunt 3)
- **B3** Hybride locatie: kerndeclaratie in m01, domeinspecifieke aanvullingen in m15
- **C2** Geen 2e fw:toetst naar ISO 27001: ENSIA toetst formeel alleen BIO; ISO blijft `skos:relatedMatch`

---

## §5. Stap 6 — SKOS-mappings CSF Tier ↔ Level (+4 triples)

Locatie: m21-csf.ttl (target-module-precedent v4.5.0 Stap 5+6).

| Tier | ↔ | Level |
|---|---|---|
| `csf:Tier_1_Partial` | `skos:relatedMatch` | `isms:Level_1` (Ad-hoc) |
| `csf:Tier_2_RiskInformed` | `skos:relatedMatch` | `isms:Level_2` (Informeel) |
| `csf:Tier_3_Repeatable` | `skos:relatedMatch` | `isms:Level_4` (Geëvalueerd) |
| `csf:Tier_4_Adaptive` | `skos:relatedMatch` | `isms:Level_5` (Geïntegreerd) |

**`isms:Level_3` (Vastgesteld) krijgt geen Tier-equivalent** (G1-discipline): CSF heeft 4 Tiers, NBA-LIO/NOREA 5 Levels. Tussen-mapping zou geforceerd zijn.

---

## §6. Stap 7 — Verificatie

| Bestand | Status |
|---|---|
| `canonical_metrics_v4_6_0.py` + `.json` | ✓ gegenereerd; D5-conform 93/93; D11-conform 5/5 |
| `shacl_split_validate_v4_6_0.py` + `.json` | ✓ RUN 1=0, RUN 2=290 (identiek) |
| `file_hashes_v4_6_0.txt` | ✓ 22 .ttl-bestanden gehasht |

---

## §7. D-decision-conformiteit (uit canonical_metrics JSON)

| D | Status |
|---|---|
| D1 OWL 2 DL | conform (0 owl:Nothing) |
| D2 Turtle | conform |
| D3 11 namespaces | conform (geen wijziging in v4.6.0) |
| D4 SKOS cross-framework | conform (1.798 totaal) |
| D5 owl:sameAs ctrl↔bio | conform 93/93 |
| D6 Tweetalige annotaties | conform (D6-symmetrische toepassing op CSF Tier-descriptions; @nl-only op LevelDescription comment-veld) |
| D7 BIO 2.0 twee klassen | conform |
| D8 Canonieke SoA | conform |
| D9 Framework-neutraal | conform (fw:ENSIA als gelijkwaardig fw:GRCFramework-individual) |
| D10 COSO/COBIT | conform |
| D11 asset-convergentie | conform 5/5 |
| D12 Drie-laags compliance | conform (geen wijzigingen aan compl-tak) |

---

## §8. Aandachtspunten (8 punten — methodologisch + technisch)

### A. Methodologische leerpunten voor projectinstructie v1.9

**§8.1 — Pre-sprint-inventarisatie-multi-module-discipline (kritiek)**

Pre-sprint vraag D vroeg specifiek naar "fw:ENSIA volledige declaratie in m01". Tech-chat antwoordde correct dat het er niet was. Maar de werkelijke architecturele vraag was: *bestaat fw:ENSIA model-breed met welke staat?* Werkelijke m15-staat (3 issuers, fw:toetst fw:BIO_2_0, 8 audit-domains, 2 skos:relatedMatch, NB-comments) miste in rapport. Vraag B (zoekopdracht) deed wél multi-module-zoek; vraag D had dat patroon moeten volgen.

**v1.9-regel**: pre-sprint-vragen naar "X bestaat in module Y" altijd uitbreiden naar "bestaat X model-breed?" wanneer architectuur-keuze hieraan vasthangt.

**§8.2 — Instructie-inconsistentie code-block vs toelichting**

Instructie §6.3 toonde `fw:ENSIA fw:toetst fw:ISO_IEC_27001_2022` in code-block maar in toelichting *"ENSIA toetst momenteel alleen BIO conform officiële ENSIA-scope; ISO is referentieel"*. Spanning tussen sample en toelichting. Masterchat-correctie: toelichting leidend.

**v1.9-regel**: bij instructie-opstelling code-block en toelichting consistent maken; bij conflict toelichting leidend.

**§8.3 — Property-semantiek-discipline (issuedBy ≠ beheerder)**

`fw:issuedBy` = "heeft uitgegeven". Logius beheert ENSIA maar geeft niet uit (BZK/NOREA/VNG zijn uitgevers). Bij Logius toevoegen verwatert semantiek. Kandidaat-overweging voor latere sprint: aparte `fw:isManagedBy`-property. Niet H-item-niveau (geen blokkade).

**v1.9-overweging**: `fw:isManagedBy`-property voor beheerder-rol — toegevoegd aan overwegingen-pool.

**§8.4 — Ramings-discipline rdf:type-dubbele-telling**

rdflib telt rdf:type dubbel: class-membership + NamedIndividual-membership. Pre-stap-raming Stap 4 nam 4 triples/Capability + 6 triples/LevelDescription. Werkelijk 5 + 8. Daardoor +44% boven raming, volledig verklaarbaar. Geen bron-afwijking.

**v1.9-regel**: bij toekomstige ramingen op typed-individual-ABox-creatie: 5 triples/individual (2 type + 2 label + 1 attr) als base; meer properties tellen daarbij op.

### B. Bron-specifieke vondsten

**§8.5 — Bron-typo's CBW-Excel sheet 'Volwassenheid beheersmaatregel'**

4 typo's in NL-item-labels gecorrigeerd in Capability-rdfs:label (Cbw_05 "Bedrijfscontinuiteit" → "Bedrijfscontinuïteit", Cbw_11 + Cbw_12 "Cyberhygiene" → "Cyberhygiëne", Cbw_12 "specieke" → "specifieke", Cbw_14 "tav" → "t.a.v."). Bron-attribuering naar NBA-LIO/NOREA blijft. Correctie alleen presentatie (rdfs:label), niet bron-tekst (rdfs:comment niveau-beschrijvingen blijft bron-getrouw).

### C. Bewust-niet-mapped + open architectuur-vragen

**§8.6 — Wel/niet-corrigeren-beleid bron-typo's (patroon-criterium voor v1.9)**

- **Niet corrigeren**: typo's in referentie-targets (G1, v4.5.0-precedent sheet 8 ISO-typo's)
- **Wel corrigeren**: typo's in nieuwe-individu rdfs:label (alleen presentatie, geen referentie-integriteit; v4.6.0-precedent sheet 6 typo's)

**§8.7 — isms:Level_3 niet gemapped naar CSF Tier (G1-discipline)**

CSF heeft 4 Tiers, NBA-LIO/NOREA 5 Levels. isms:Level_3 (Vastgesteld) ligt conceptueel tussen Tier_2 en Tier_3. Tussen-mapping zou geforceerd zijn. Documenteren als bewuste G1-keuze.

**§8.8 — Sample-code vs toelichting fw:Logius (masterchat-attentiepunt)**

Instructie §6.2-sample toonde `fw:issuedBy fw:Logius`. Masterchat-correctie A3: bestaande 3 issuers behouden. Naam `Attr_ENSIA_Logius_2024` blijft (Logius = publicerende beheerder van www.ensia.nl, geen issuer-rol). Verschillende properties voor verschillende rollen.

---

## §9. Geparkeerde-items-status-update

| H-item | Status v4.5.0 | Status v4.6.0 |
|---|---|---|
| H15 — governance-graafdekking | geparkeerd | onveranderd |
| H21 — implicit individuals | geparkeerd | onveranderd |
| H25 — D12 + articleRef-domain-spanning | geen nieuwe verergering | onveranderd |
| H26 — OBL-laag gap NIS2 | onveranderd | onveranderd |
| H27 — γ-migratie articleRef → articleIdentifier | geen trigger | onveranderd |
| H29-H31 — Three Lines / GITC / Toetsingskader Algoritmes | toekomst-overweging | onveranderd |
| H32 — OBL-laag asymmetrie | geen Spoor B-data | onveranderd |
| H33 — m11 substantiële uitbreiding | wachten op trigger | onveranderd |
| H34 — m11 enhancement-modellering | wachten op trigger | onveranderd |
| H35 — Cbb 5.28-typo-interpretatie | wachten op trigger | onveranderd |

**Nieuwe overwegingen v4.6.0** (geen H-item-status, wachten op trigger):

| Overweging | Trigger-criterium |
|---|---|
| `fw:isManagedBy`-property voor beheerder-rol | Indien meerdere frameworks beheerder-rol-modellering vereisen (bv. NL Cybersecurity-strategie waar Logius/NCSC/BZK verschillende rollen hebben) |

**Spoor B automatisch geparkeerd** (onveranderd): H11-H14, H19, H20.

---

## §10. Deliverables

| Bestand | Locatie |
|---|---|
| 22 .ttl-modules (5 gewijzigd in v4.6.0: grc-core, m01, m06, m15, m21) | `/home/claude/v433/` |
| `canonical_metrics_v4_6_0.py` + `canonical_metrics_v4.6.0.json` | `/home/claude/v433/` + `/home/claude/` |
| `shacl_split_validate_v4_6_0.py` + `shacl_results_v4.6.0.json` | idem |
| `file_hashes_v4_6_0.txt` | `/home/claude/v433/` |
| `patch-rapport-v4_6_0.md` (dit rapport) | `/home/claude/v433/` |
| `inventarisatie-fase-4-precheck-v4_5_0.md` (pre-sprint, 20 mei) | reeds opgeleverd |
| `stap4_build_ttl_v4_6_0.py` + `stap3_tiers_build.py` (builders) | `/home/claude/v433/` |

---

## §11. Sprint-prognose-evaluatie

| Stap | Instructie-raming | Werkelijk | Δ |
|---|---:|---:|---:|
| Stap 2 TBox | +60-80 | +80 | bovengrens, conform |
| Stap 3 ABox (Levels + Tiers) | ~70 | +71 | exact |
| Stap 4 Sheet 6 ABox | +900-1.000 | +1.440 | +44% boven (verklaarbaar §8.4) |
| Stap 5 M15-ENSIA | ~25-30 (instructie) → 0-5 (na pauze-bijstelling) | +15 | binnen verklaarbaarheid |
| Stap 6 SKOS Tier↔Level | +4 | +4 | exact |
| **Sprint-totaal** | +1.080-1.210 (origineel) → +1.060-1.090 (na S5-bijstelling) | **+1.610** | **+33% boven origineel** |

**Patroon-bevinding**: hoofd-overshoot zit in Stap 4 (rdf:type-dubbele-telling); andere stappen binnen marge. **Sprint-schaalmultiplier 2,7× v4.4.0** — onder oorspronkelijke prognose van 5-7×.

---

## §12. GO-criteria voor masterchat-eindreview

| Criterium | Status |
|---|---|
| Triple-Δ uit canonical_metrics JSON | ✓ +1.610 |
| `owl:Nothing` post-inferentie | ✓ 0 |
| SHACL RUN 1 / RUN 2 | ✓ 0 / 290 (identiek baseline) |
| D-decisions conformiteit | ✓ allen conform |
| Versie-suffix op scripts | ✓ canonical_metrics + shacl + hashes allen `v4_6_0` |
| Bron-attribuering 2 nieuwe SourceAttributions | ✓ Attr_NBA_LIO_NOREA (m06, SHA256) + Attr_ENSIA_Logius_2024 (m01) |
| §9 geparkeerde-items-status | ✓ + 1 nieuwe overweging (fw:isManagedBy) |
| G1-discipline | ✓ Level_3 niet gemapped, 0 dangling references |
| Inverse-paar isms:hasLevelDescription ↔ forCapability | ✓ bidirectioneel |
| fw:ENSIA type-harmonisatie | ✓ alleen fw:GRCFramework (oude fw:Guideline weg) |
| 4 typo-correcties verifieerbaar | ✓ Cbw_05, Cbw_11, Cbw_12, Cbw_14 |
| Sample-first + heads-up moments respected | ✓ Stap 3.4.2 EN-tekst-sample + Stap 4 pre-stap mini-inventarisatie + Stap 5 scope-pauze |

---

**Einde patch-rapport v4.6.0 Fase 4.**

*Workdir-status: `/home/claude/v433/`. 5 modules gewijzigd; 17 modules bytewise identiek aan v4.5.0-eindstand. Stand-by voor masterchat-eindreview.*
