# PATCH-RAPPORT — GRC KENNISMODEL v4.5.0 FASE 3

**Versie:** 1.0
**Datum:** 19 mei 2026
**Opsteller:** Technische chat
**Sprint:** v4.5.0 — Fase 3 (M21 NIST CSF 2.0)
**Basis:** v4.4.0-baseline (13 mei 2026)
**Doorlooptijd:** 13 — 19 mei 2026 (sprint-protocol B + scope-pauzes)

---

## §0. Executive samenvatting + kerncijfers

### Sprint-resultaat

**Scope-correct opgeleverd**: NIST CSF 2.0 als 11e namespace, 6 Functions + 22 Categories + 106 Subcategories + 363 Implementation Examples, plus 1.448 SKOS-mappings naar ISO 27001/27002, NIST SP 800-53 en COSO/COBIT.

**Schaal-multiplier**: sprint-omvang **~8,5× v4.4.0** (zoals masterchat-prognose voorzag). Drie significante stappen boven raming (Stap 4 IE-volume; Stap 5 sheet 8 dedup; Stap 6 OLIR-format-afwijking → CSF Reference Tool-fallback) afgevangen door cross-bron-overlap-compensatie in Stap 6.

**Cross-bron-overlap-kwaliteits-indicator**: Sheet 8 (ADR & NOREA) en CSF Reference Tool (NIST) leggen **105 keer dezelfde ISO 27001-mapping**. Twee onafhankelijke bronnen → bron-consistentie-bewijs. Dit is geen technisch dedup-feit maar een SKOS-kwaliteits-validatie.

### Baseline-vergelijking (uit canonical_metrics_v4.5.0.json, niet uit memorie)

| Metric | v4.4.0 baseline | **v4.5.0 eindstand** | Δ | Bron |
|---|---:|---:|---:|---|
| Pre-inferentie triples | 13.441 | **19.340** | **+5.899** (+43,9%) | `global_pre_inference.triples` |
| Post-inferentie triples (OWL RL) | 31.415 | **41.988** | +10.573 | `global_post_inference_owlrl.triples` |
| `owl:Class` | 189 | **193** | +4 | `global_pre.owl_Class` |
| `owl:NamedIndividual` | 679 | **1.179** | **+500** | idem |
| `owl:ObjectProperty` | 143 | **146** | +3 | idem |
| `owl:DatatypeProperty` | 93 | **94** | +1 | idem |
| `owl:sameAs` | 98 | **98** | 0 (ongewijzigd) | idem |
| ↳ D5 ctrl↔bio | 93 | **93** | 0 (ongewijzigd) | `D5_ctrl_bio_sameAs_count` |
| ↳ D11 asset-bridges | 5 | **5** | 0 (ongewijzigd) | `D11_asset_brug_count` |
| SKOS-mappings totaal | 346 | **1.794** | **+1.448** (+418%) | `skos_mappings_total` |
| `owl:Nothing` post-inferentie | 0 | **0** | 0 ✓ | `owl_Nothing_assertions_post_inference` |
| SHACL violations RUN 1 (`inference='none'`) | 0 | **0** | 0 ✓ | `shacl_results_v4.5.0.json` |
| SHACL violations RUN 2 (`inference='owlrl'`) | 290 | **290** | 0 ✓ | (104 asset + 93+93 ISO27002 NamingShape — bekende false-positives) |
| Namespaces (D3-revisie) | 10 | **11** | +1 (`csf:`) | `D3_namespaces_used` |
| Modules (.ttl) | 22 (20 data + grc-core + grc-bridges) | **23** (+m21-csf.ttl) | +1 | filesystem |
| Modules gewijzigd | — | **8** | — | grc-core, m01, m02, m08, m09, m11, m17, m21(NIEUW) |

### Verdeling SKOS-mappings na v4.5.0

| Type | Aantal | Bron |
|---|---:|---|
| `skos:closeMatch` totaal | 1.490 | sheet 8 + CSF Reference Tool |
| `skos:relatedMatch` totaal | 234 | inkl. 13 nieuwe csf→COSO/COBIT (Stap 7) |
| `skos:exactMatch` totaal | 46 | ongewijzigd v4.4.0 |
| `skos:broadMatch` totaal | 38 | ongewijzigd v4.4.0 |
| **Totaal** | **1.794** ✓ | |

### Bron-attributies in model na v4.5.0

| SourceAttribution-individual | Toegevoegd in | Licentie |
|---|---|---|
| `ext:Attr_CBW_NIS2_Framework_2025_CC_BY_4_0` | v4.4.0 | CC-BY 4.0 |
| `ext:Attr_NIST_CSF_2_0_Core_2024` | v4.5.0 Stap 2 | Public Domain |
| `ext:Attr_NIST_CSF_2_0_Reference_Tool_2026` (renamed van OLIR-versie) | v4.5.0 Stap 2 + 6 | Public Domain |

---

## §1. Stap 1 — Pre-sprint-inventarisatie (voltooid 13 mei)

Read-only inventarisatie volgens sprint-protocol B. Drie signalen vooraf gerapporteerd, allen architectuur-verwerkt in instructie:

| Signaal | Verwerking |
|---|---|
| ISO-notatie-corruptie (Griekse Α, 2× ontbrekende punt, 2× spaties) | Besluit 6 (tech-chat normaliseert in Stap 5) |
| Duale ISO-targets (hoofdtekst-clausules + Annex A) | Besluit 4 (beide target-typen via D5) |
| 0/93 BIO-Controls met directe SKOS naar ISO27001/NIST | Context: Fase 3 wordt eerste reguliere control-niveau SKOS-werk |

---

## §2. Stap 2 — TBox-uitbreidingen (+90 triples)

D3-revisie naar 11 namespaces. 4 klassen, 4 properties, 2 SourceAttribution-individuals, 1 framework-individual. D6 meeliftregel toegepast op `ctrl:CybersecurityConcept` (CSF v1.x → v2.0 incl. GOVERN).

| Module | Wijziging |
|---|---|
| `grc-core.ttl` | versie v4.5.0; `csf:`-prefix; `csf:Function`, `csf:Category`, `csf:Subcategory`, `csf:ImplementationExample` (allen ⊑ `ext:FrameworkComponent`); `csf:partOfFunction`, `csf:partOfCategory`, `csf:exemplifies`; `csf:csfIdentifier` |
| `m01-framework.ttl` | `fw:NIST_CSF_2_0`-individual |
| `m02-control.ttl` | D6 meeliftregel: `ctrl:CybersecurityConcept` comment 5 → 6 Functions |
| `m21-csf.ttl` (NIEUW) | 2 SourceAttribution-individuals (Core + Reference_Tool) |

---

## §3. Stap 3 — CSF Core (+1.094 triples)

6 Functions + 22 Categories + 106 Subcategories in `m21-csf.ttl`. Allen met bilingual labels (Function+Category), ID-form label (Subcategory), volledig NIST CSWP 29-statement als `rdfs:comment@en`, `csf:csfIdentifier`, `ext:isComponentOf fw:NIST_CSF_2_0`, `ext:sourceAttribution Attr_NIST_CSF_2_0_Core_2024`.

| CSF-level | Aantal | IRI-conventie |
|---|---:|---|
| Function | 6 | `csf:GOVERN`, `csf:IDENTIFY`, etc. (Optie C, volledige naam) |
| Category | 22 | `csf:GV_OrganizationalContext`, etc. (Oxford-`And` behouden, komma's gestript) |
| Subcategory | 106 | `csf:GV_OC_01`, etc. (pure underscore-substitutie) |

**Verifieerde scope-pauze in Stap 3**: `ext:belongsToFramework` bestond niet — bestaande `ext:isComponentOf` (m17-precedent voor `ext:FrameworkComponent → fw:GRCFramework`) gebruikt. Masterchat GO Optie A.

---

## §4. Stap 4 — Implementation Examples (+3.267 triples)

363 IE-individuals uit `CSF_2_0-Implementation_Examples.xlsx` (385 records-aanname → werkelijk 363 na uitfiltering van 22 Function/Category-header-rijen).

| Distributie | Waarde |
|---|---:|
| Min Examples per Subcategory | 1 |
| Max Examples per Subcategory | 10 (`GV.SC-05`) |
| Avg Examples per Subcategory | 3,42 |
| Subcategories met ≥1 IE | **106 / 106 = 100%** |

IRI-conventie: `csf:<FUNC>_<CAT>_<NN>_Ex<N>` (geen zfill op N; max `Ex10`).

---

## §5. Stap 5 — Sheet 8 mappings (+641 triples)

49 sheet 8-datarijen → **641 unieke `skos:closeMatch`-triples** in `m21-csf.ttl`.

| Target-type | Aantal | Route |
|---|---:|---|
| `bio:ISO27002_*` (Annex A) | 494 | D5 sameAs-brug naar ctrl: |
| `ext:ISO27001_*` (hoofdtekst-clausules) | 147 | direct |

**19 ISO-normalisaties uitgevoerd** vóór resolutie. **16 unresolved** (G1 niet gelegd):
- 12 csf-subject-missing (3 unique: `GV.OC-07`, `ID.RM-01`, `PR.AC-02` — CSF v1.x-naming in september-2025-bron)
- 4 target-missing (`5.28`-typo voor `A.5.28`)

Subcategory-dekking 86/106 = 81% via sheet 8 alleen.

---

## §6. Stap 6 — CSF Reference Tool IR-mappings (+794 triples graph-delta, 899 builder-unique)

**Scope-pauze**: csf2.xlsx bleek CSF Reference Tool-export, niet OLIR-snapshot (geen relationship-types, geen OLIR-IDs). Masterchat GO Optie B met 3 Aanpassingen:

1. SourceAttribution-rename: `Attr_NIST_CSF_2_0_OLIR_2026` → `Attr_NIST_CSF_2_0_Reference_Tool_2026`
2. Default-relationship `skos:closeMatch` voor alle drie target-typen
3. Filter op exact 3 source-prefixes (`SP 800-53 Rev 5.2.0`, `ISO/IEC 27001:2022: Annex A Controls`, `ISO/IEC 27001:2022: Mandatory Clause`)

| Module | Toegevoegde mappings |
|---|---:|
| `m11-nist-800-53.ttl` | 491 (CSF ↔ SP 800-53 Rev 5.2.0) |
| `m08-bio20.ttl` | 291 (CSF ↔ ISO Annex A via D5) |
| `m09-iso27001-ext.ttl` | 117 (CSF ↔ ISO Mandatory Clause) |
| Builder unique | 899 |
| **Graph-delta na merge** | **+794** (105 overlap met S5) |

**337 unresolved** met G1-discipline:
| Categorie | Aantal | Detail |
|---|---:|---|
| target-missing | 236 | 108 unieke SP 800-53 controls niet in m11 (modelbeperking) |
| iso_clause "None" | 66 | NIST bron-conventie voor "geen mapping" |
| sp_enhancement | 18 | 17 unieke enhancements, m11 geen enhancement-modellering |
| iso_annex "None"/empty | 13 | idem voor Annex A |
| sp_format_unknown (family-only) | 3 | `PT`, `CP`, `IR` |
| iso_clause komma-combinatie | 1 | `7.1, 7.2` |

Mapping-coverage gestegen naar **100% op alle 3 CSF-niveaus**: Function 6/6, Category 22/22, Subcategory 106/106.

---

## §7. Stap 7 — GOVERN-overlap COSO/COBIT (+13 triples)

13 `skos:relatedMatch`-triples in `m17-coso-cobit.ttl`. 5 GV-subjects → 12 unieke COSO/COBIT-targets (ControlEnvironment dubbel voor GV.OC + GV.RR).

| GV-Category | Mappings |
|---|---:|
| GV.OC Organizational Context | 2 |
| GV.RM Risk Management Strategy | **4** (incl. COSO_ERM_Performance toegevoegd door masterchat) |
| GV.RR Roles, Responsibilities, and Authorities | 2 |
| GV.PO Policy | 2 |
| GV.OV Oversight | 3 |
| GV.SC Cybersecurity Supply Chain Risk Management | **0 (SKIP — G1)** |

7 bewust niet-gemapte targets gedocumenteerd in TTL-comment + §8.

---

## §8. Aandachtspunten (19 punten — methodologisch + technisch + bron-specifiek)

### A. Methodologische leerpunten voor projectinstructie v1.8

1. **SHA256 in OLIR-/snapshot-SourceAttribution-attribution-text** als best practice voor snapshot-bronnen — los van `file_hashes_v[versie].txt` (laatste = build-state; SHA256 in attribuering = bron-state op moment van mapping-creatie)
2. **Sprint-protocol B-verfijning**: vóór instructie-opstelling met nieuwe property-namen, masterchat eerst grep door bestaande modules op vergelijkbare semantiek. Tweemaal in deze sprint toegepast (Stap 2 `ext:belongsToFramework` → `ext:isComponentOf`; Stap 6 OLIR-naam → Reference_Tool)
3. **Precedent-discipline 4-vragen-checklist** bij nieuw framework-cluster: (a) component→framework property, (b) parent-child binnen framework, (c) SourceAttribution-aanpak, (d) SKOS-mapping-conventies. Voorkomt mid-sprint-redesigns
4. **Bron-verificatie vóór raming-opstelling** als methodologie-element: Stap 4 (385→363) + Stap 5 (raming 220→werkelijk 641, 3×) + Stap 6 (raming 580→werkelijk 794) wijzen op structureel patroon: ramingen waren niet bottom-up afgeleid uit beschikbare pre-sprint-cijfers
5. **Bij concept-mapping-tabellen voor framework-overlap**: expliciet complement-paren binnen multi-pijler-frameworks (COSO ERM 5-pijler-structuur) evalueren. **v4.5.0 Stap 7-leerpunt**: GV.RM → StrategyObjectiveSetting was vooraf-vaststelling; Performance is continue-management. Beide relevant; één-match-per-cluster overslaat gerelateerd aspect
6. **Patch-rapport-§0-tabel direct uit canonical_metrics JSON** (consistent met leerpunt v4.3.3 §9.2). Dit rapport voldoet daaraan

### B. Bron-specifieke vondsten

7. **csf2.xlsx is CSF Reference Tool-export, geen OLIR-snapshot**: 23 source-prefixes (niet 11); geen OLIR-ID/relationship-type-kolommen. Bij Stap 6 leidde dat tot 3 Aanpassingen (rename SourceAttribution, uniform closeMatch, filter 3 prefixes)
8. **NIST Reference Tool-bron-conventie**: 75× letterlijke `"ISO/IEC 27001:2022: Mandatory Clause: None"`-lines waar geen mapping bestaat. G1 correct toegepast
9. **Sheet 8 mengt CSF v1.x en v2.0-naming**: 3 CSF-refs (`GV.OC-07`, `ID.RM-01`, `PR.AC-02`) bestaan niet in CSF 2.0 Core. ADR/NOREA-sheet september 2025 dateert van na CSF 2.0-launch (februari 2024) maar is niet volledig 2.0-conform
10. **ISO 27001 5.28-typo in sheet 8 UV 10.4**: hoofdtekst kent geen 5.28 (max clauses 4-10); vermoedelijk typo voor `A.5.28` (= `bio:ISO27002_5_28`, bestaat). Niet gelegd; kandidaat voor interpretatieve correctie in latere sprint
11. **ADR/NOREA bron-kwaliteits-patroon** cumulatief v4.4.0 + v4.5.0: 2 typo-categorieën in v4.4.0 + 19 normalisaties + 16 unresolved in v4.5.0. Bron is bruikbaar maar structureel licht inconsistent — relevant voor toekomstig ADR/NOREA-bron-gebruik
12. **CSF 2.0 Subcategory-numbering-gaps**: NIST heeft enkele Subcategory-nummers overgeslagen (`RC.CO-01` en `RC.CO-02` bestaan niet; RC.CO begint bij -03). Bron-eigen ontwerp, geen modelfout
13. **Bron-volume Implementation Examples**: 363 (niet 385); 100% Subcategory-dekking; gemiddeld 3,42 Examples/Subcat (max 10 voor `GV.SC-05`)

### C. Kwaliteits-indicatoren

14. **Cross-bron-overlap S5+S6 = 105 mappings** (sheet 8 ∩ CSF Reference Tool). Twee onafhankelijke bronnen leggen identieke ISO-mappings → **SKOS-kwaliteits-validatie**. Niet alleen technisch dedup; positief signaal voor mapping-correctheid
15. **IR-mapping-niveau-vondst**: 91% Subcategory / 8% Category / 1,5% Function. NIST publiceert IR-mappings op alle drie CSF-niveaus → directe Function-niveau-mappings voor dashboard zonder inferentie-aggregatie

### D. Architectuur-aandachtspunten + kandidaat-H-items

16. **`ctrl:CybersecurityConcept` ↔ `csf:Function`-overlap**: m02-update CSF v1.x → v2.0 legt overlap tussen beide klassen bloot. Beide modelleren Govern/Identify/Protect/Detect/Respond/Recover-concept. SKOS-mapping-kandidaat voor latere sprint
17. **m11 modelbeperking** (kandidaat-H-item): 124 van ~1000 SP 800-53 Rev 5-controls in model. 108 unique unresolved targets uit Stap 6. Bij toekomstig serieus SP 800-53-gebruik (Spoor B) zou m11 substantieel uitgebreid moeten worden. **Trigger-criterium**: Spoor B-organisatie heeft >50 niet-gemapte SP 800-53-individuals nodig
18. **GV.SC SKIP-rationale**: COSO/COBIT-clusters in m17 bevatten geen native cybersecurity-supply-chain-component. Mogelijke heroverweging bij Spoor B-data of bij introductie van een specifiek supply-chain-framework (TPRM, SOC 2 vendor-mgmt, etc.)
19. **6 bewust niet-gemapte COSO/COBIT-targets** (Stap 7): `COBIT_DSS05`, `COBIT_EDM02`, `COBIT_EDM04`, `COBIT_EDM05`, `COSO_ERM_InformationCommunicationReporting`, `COSO_ICF_InformationCommunication`. Documenteren als context voor toekomstige sprints

---

## §9. Geparkeerde-items-status-update (verplicht sinds projectinstructie v1.7)

| H-item | Status v4.4.0 | Status v4.5.0 |
|---|---|---|
| H15 — governance-graafdekking (Route P/Q/R) | geparkeerd | onveranderd geparkeerd |
| H21 — 421 implicit individuals consistentie-keuze | geparkeerd | onveranderd geparkeerd |
| H25 — D12 + compl:articleRef-domain-spanning | geen nieuwe articleRef-subjects | **onveranderd** (geen nieuwe verergering in v4.5.0 — alle Stap 5+6+7 mappings via skos:* zonder compl:articleRef-betrokkenheid) |
| H26 — OBL-laag gap NIS2 art. 18/19/22/24 | onveranderd | onveranderd; geen GRC-inhoudelijke analyse uitgevoerd |
| H27 — γ-migratie compl:articleRef → compl:articleIdentifier | geen trigger | onveranderd; geen trigger geactiveerd |
| H32 — OBL-laag modelleringsasymmetrie | geregistreerd post-v4.4.0 | onveranderd; geen Spoor B-data |
| H29 — Three Lines Model (toekomst-overweging) | onveranderd | onveranderd |
| H30 — GITC auditkader (toekomst-overweging) | onveranderd | onveranderd |
| H31 — Toetsingskader Algoritmes (toekomst-overweging) | onveranderd | onveranderd |

**Nieuwe geparkeerde items uit v4.5.0**:

| Nieuw H-item | Trigger-criterium |
|---|---|
| **H33** — m11 substantiële uitbreiding SP 800-53 | Spoor B-organisatie heeft >50 niet-gemapte SP 800-53-controls nodig (zie §8 punt 17) |
| **H34** — m11 enhancement-modellering | Bij seriuze SP 800-53-toepassing waar enhancements (`AC-2(1)`, `CM-07(02)`, etc.) auditief relevant zijn (17 unique enhancements in Stap 6) |
| **H35** — Cbb 5.28-typo-interpretatie | Bij Stap 5 unresolved: optionele heroverweging als `A.5.28` (=`bio:ISO27002_5_28`); 4 paren in sheet 8 UV 10.4 |

**Spoor B automatisch geparkeerd** (onveranderd): H11, H12, H13, H19, H20, H14.

**Overige** (onveranderd): HermiT-herrun in Protégé; Cbb-inwerkingtreding-monitoring; Route 1/1-light ISO-guidance-parafrasering geparkeerd naar v5.x.

**Beschikbaar voor Fase 4-overweging**:

- Volwassenheidsmodel: `biz:MaturityAssessment` bestaat al — eerst evalueren of hergebruik/uitbreiding van `biz:`-klasse zinvol is voordat nieuwe `isms:MaturityAssessment` wordt gedeclareerd (zie projectinstructie v1.7 Fase 4-aandachtspunt)
- ENISA TIG-PDF-integratie als kandidaat-Route (nog niet ingezet)

---

## §10. D-decision-conformiteit (uit canonical_metrics JSON)

| D | Status | Bron in JSON |
|---|---|---|
| D1 OWL 2 DL | conform (0 owl:Nothing post-inference) | `owl_Nothing_assertions_post_inference: 0` |
| D2 Turtle-serialisatie | conform (alle 22 .ttl files) | filesystem |
| **D3 Namespaces** | **uitgebreid naar 11 (csf: toegevoegd)** | `D3_namespaces_used` heeft 11 keys |
| D4 SKOS cross-framework mappings | conform (1.794 totaal) | `skos_mappings_total: 1794` |
| D5 owl:sameAs strikt ctrl↔bio | **conform (93/93)** | `D5_conform: true` |
| D6 Tweetalige annotaties | conform (3.399 labels; 1.568 comments) | `rdfs_label_total`, `rdfs_comment_total` |
| D7 BIO 2.0 twee klassen | conform (0 ctrl-BIO2-overblijfselen) | `D7_ctrl_BIO2_overblijfselen.count: 0` |
| D8 Canonieke SoA | conform (1 SoA + 93 SoAEntry) | `D8_SoAEntry_count: 93` |
| D9 Framework-neutraal | conform; CSF 2.0 als gemapt referentiekader toegevoegd | architectuurkeuze |
| D10 COSO ICF/ERM enterprise-laag | conform (incl. 13 nieuwe GV→COSO/COBIT-mappings) | m17 SKOS-uses verdriedubbeld (19→32) |
| **D11 owl:sameAs asset-convergentie** | **conform (5/5)** | `D11_conform: true` |
| D12 Drie-laags compliance | conform (geen wijzigingen aan compl-tak) | architectuur ongewijzigd in v4.5.0 |

---

## §11. Deliverables

| Bestand | Locatie |
|---|---|
| 22 .ttl-modules (8 gewijzigd in v4.5.0) | `/home/claude/v433/` |
| `canonical_metrics_v4_5_0.py` (script) | `/home/claude/v433/` |
| `canonical_metrics_v4.5.0.json` (output) | `/home/claude/` |
| `shacl_split_validate_v4_5_0.py` (script) | `/home/claude/v433/` |
| `shacl_results_v4.5.0.json` (output) | `/home/claude/` |
| `file_hashes_v4_5_0.txt` (SHA256-baseline) | `/home/claude/v433/` |
| `patch-rapport-v4_5_0.md` (dit rapport) | `/home/claude/v433/` |
| `inventarisatie-fase-3-precheck-v4_4_0.md` (Stap 1) | reeds opgeleverd 13 mei |

---

## §12. Sprint-prognose-evaluatie

| Fase | Masterchat-raming | Werkelijk | Δ |
|---|---:|---:|---:|
| Stap 2 TBox | +90-100 | +90 | exact in marge |
| Stap 3 CSF Core | +960-1.000 | +1.094 | iets boven raming (bilingual labels) |
| Stap 4 Implementation Examples | +1.500 (oud) → +2.300-2.500 (bijgesteld) | +3.267 | +30% boven hoogste raming |
| Stap 5 Sheet 8 | +170-220 | +641 | **3× boven raming** (sheet 8 multi-mapping rijker) |
| Stap 6 OLIR/Reference Tool | +500-680 (oud) → +1.100 (bijgesteld) | +794 (graph) / +899 (builder) | -28% onder bijgestelde raming (cross-bron-overlap-dedup) |
| Stap 7 GOVERN-overlap | +15-30 | +13 | onderaan marge |
| **Sprint-totaal** | +2.700-3.200 (oud) → +5.900-6.000 (bijgesteld) | **+5.899** | **exact onderaan band** |

**Patroon-bevinding**: 4 van 6 stappen boven raming. Mitigerend was Stap 6 cross-bron-overlap-dedup. Voor projectinstructie v1.8: bron-verificatie vóór raming-opstelling als verplicht protocol-element (leerpunt §8.4).

---

## §13. GO-criteria voor masterchat-eindreview

| Criterium | Status |
|---|---|
| Triple-Δ uit canonical_metrics JSON | ✓ +5.899 binnen prognose |
| `owl:Nothing` post-inferentie | ✓ 0 |
| SHACL RUN 1 (`inference='none'`) | ✓ 0 violations |
| SHACL RUN 2 (`inference='owlrl'`) | ✓ 290 (identiek aan v4.4.0-baseline, bekende false-positives) |
| D-decisions conformiteit | ✓ allen conform (D3 uitgebreid van 10 → 11) |
| D6 meeliftregel toegepast | ✓ m02 `ctrl:CybersecurityConcept` v1.x → v2.0 |
| `ext:isComponentOf` correct gebruikt | ✓ 516 uses (was 19; +497 op CSF) |
| G1 "bij twijfel niet leggen" | ✓ 353 unresolved gedocumenteerd, niet gelegd |
| Bron-attribuering (CC-BY + Public Domain) | ✓ 3 SourceAttribution-individuals |
| Versie-suffix op scripts | ✓ canonical_metrics + shacl + hashes allen `v4_5_0` |
| Cross-bron-overlap als kwaliteits-indicator | ✓ §8 punt 14 |
| §9 geparkeerde-items-status | ✓ inclusief 3 nieuwe H-items (H33/H34/H35) |
| Bewust-niet-gemapte targets gedocumenteerd | ✓ TTL-comment m17 + §8 punt 19 |

---

**Einde patch-rapport v4.5.0 Fase 3.**

*Workdir-status*: `/home/claude/v433/` bevat 22 .ttl + 6 scripts + 3 documentaties. 8 modules gewijzigd; 14 modules bytewise identiek aan v4.4.0-eindstand. Stand-by voor masterchat-eindreview.
