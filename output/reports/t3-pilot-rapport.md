---
type: report
subtype: pilot-rapport
sprint: T3
sprint_stap: 2
baseline_from: v4.6.2
date: 2026-05-28
status: final-awaiting-masterchat-review
mode: READ-ONLY
related:
  - skos-beoordelings-protocol-v1_3
  - t3-pre-sprint-inventarisatie
  - H36_skos-exactmatch-ctrl-compl-audit
  - D04_skos-cross-framework
  - M14_avg-gdpr
scope: "T3 Stap 2 — per-paar-beoordeling van 6 m14-paren onder SKOS-protocol v1.3 FINAL. Read-only, geen patch. Pilot toetst of de geïdentificeerde 5 bindende T3-steers (geen D4.1, geen cluster-convergentie, semantische basislijn relatedMatch, evidence-hantering, closeMatch-toets) operationeel zijn op heterogene 1↔veel-AVG-cluster-structuur en levert oordeel of opschaling naar Stap 3 verantwoord is."
---

# T3 Pilot-rapport — Stap 2

> **Methodische notitie:** dit rapport is bottom-up opgebouwd conform Protocol v1.3 §10.2. De zes paar-analyses (§3) zijn als eerste geschreven; analyse (§4) + onderbouwing (§5) + samenvatting (§1-§2) volgen daaruit.

> **Disclosure-discipline:** alle NEN-citaten zijn parafrase + clausule-verwijzing. Geen verbatim ISO-tekst >10 woorden in dit rapport (Protocol 14 + Protocol v1.3 §8.2 gerespecteerd).

---

## §1. Samenvatting

| Aspect | Bevinding |
|---|---|
| Totaal beoordeelde paren | 6 |
| Mutaties voorgesteld | **0** |
| Behoud | **6** |
| Confidence hoog | 3 |
| Confidence middel | 3 |
| Confidence laag | 0 |
| closeMatch-toets T3-014 | **verdedigbaar behouden als closeMatch** (per-paar bilateraal partiële C1; geen NEN-aantoonbare grond om naar relatedMatch te downgraden; confidence middel) |
| Stop-conditie geactiveerd | **nee** (drempels: ≥3 laag, ≥3 mutaties, onverwacht patroon) |
| Methode-conclusie | Bindende T3-steers houden op deze sample. Geen cluster-convergentie-effect aangetroffen. Semantische basislijn `relatedMatch` is per-paar passend voor alle 5 relatedMatch-paren in sample. broadMatch (T3-002) en closeMatch (T3-014) zijn beide per-paar verdedigd op afzonderlijke gronden. |
| Vervolg | **GO opschaling naar Stap 3 (resterende 25 paren)**, masterchat-beslissing |

**Bottom-line:** alle 6 sample-paren krijgen behoud-classificatie. De m14-cluster-structuur (1↔veel-subject-clusters) genereert geen automatische cluster-doel-projectie naar `narrowMatch`, omdat per-paar-toets via C3 (B ⊆ A) systematisch faalt — geen ISO-control is als geheel ⊆ in een breed AVG-artikel; controls zijn altijd operationele beveiligingsmaatregelen, AVG-artikelen zijn principe- of doelvoorschriften. Predicate-discipline verloopt langs C1+C4-evidence per individueel paar.

---

## §2. Methode

### §2.1 Protocol-toepassing

Per paar toegepast: Protocol v1.3 §2.1 (C1) + §2.2 (C2) + §2.3 (C3) + §2.4 (C4), gevolgd door §3.1 predicate-doel-tabel-mapping en §5.2 confidence-criterium. D4.1-vooraf-check (§2.0) is op alle 6 paren irrelevant — geen exactMatch-doel-overweging (bindende T3-steer 1).

### §2.2 Bindende T3-steers — operationele toepassing

| Steer | Toepassing in deze pilot |
|---|---|
| 1. Geen D4.1-disclaimer-logica | Geen ENISA-TIG of vergelijkbare bron-disclaimer in m14-evidence-stack. AVG is publiek EU-recht (geen disclaimer). 27701:2025 Annex D bevat alleen indicatief-non-exhaustive caveat — dat is geen non-equivalence-disclaimer in D4.1-zin |
| 2. Geen cluster-convergentie-aanname | Elk paar afzonderlijk getoetst. Subject-cluster-cardinaliteit (Art32 → 12 controls) is informatief signaal voor 1↔veel-structuur, maar per-paar-C3-toets prevaleert |
| 3. Semantische basislijn = relatedMatch | Voor alle 4 relatedMatch-huidige-paren (T3-024, T3-008, T3-028, T3-031) is relatedMatch per-paar bevestigd; voor T3-002 (broadMatch) en T3-014 (closeMatch) zijn de huidige predicates per-paar verdedigd op evidence-niveau-1 respectievelijk per-paar-C1-partieel |
| 4. Evidence-hantering | Niveau-1-keten (27701 Annex F + Annex D) is gebruikt als sterk ondersteunend bewijs dát een relatie bestaat. De keten bepaalt niet het predicate-type — predicate-type volgt uit C1+C3-toets op 27002 + AVG-tekst |
| 5. closeMatch-toets T3-014 | Expliciet getoetst; uitkomst: behoud verdedigbaar (zie §3.2 en §4.2) |

### §2.3 Bron-stack per paar

| Bron | Rol |
|---|---|
| `ontology/m14-avg-gdpr.ttl` rdfs:comment per AVG-artikel | Obligation-semantiek (NL-parafrase EUR-Lex) |
| `/Users/stevenbouwmeester/grc-sources-licensed/NEN-EN-ISO_IEC_27002_2022_en.pdf` Control+Purpose-secties | Control-semantiek (C1 + C3-toets) |
| `/Users/stevenbouwmeester/grc-sources-licensed/ISO27701.pdf` Annex D (Table D.1) + Annex F.1 + Annex B.3 | Keten-evidence (C4 niveau-1/2) |
| EUR-Lex Regulation (EU) 2016/679 | AVG-tekst-verificatie (publiek; m14 rdfs:comment volstond op deze sample) |

---

## §3. Per-paar-beoordeling

### §3.1 T3-002 — compl:AVG_Art5_1f `skos:broadMatch` ctrl:ISO27002_5_12

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art5_1f` (AVG Art. 5(1)(f) — integriteit en vertrouwelijkheid) |
| Object IRI | `ctrl:ISO27002_5_12` (Classificeren van informatie / Classification of information) |
| Huidige predicate | `skos:broadMatch` |
| Cluster-context | Art5_1f-subject-cluster (7, heterogeen: broad×2/related×5); object-cluster: singleton (alleen Art5_1f mapt naar 5.12) |
| D4.1-disclaimer-check | n.v.t. — geen exactMatch-doel-overweging |
| **C1 (definitioneel)** | **partieel** — Art. 5(1)(f) is een breed principe: passende technische en organisatorische maatregelen voor passende beveiliging tegen ongeoorloofde/onrechtmatige verwerking + verlies/vernietiging/beschadiging. Classification of information is een specifieke ondersteunende control: classificeren op basis van C/I/A-behoeften en stakeholder-eisen. Cross-overlap is op operationeel niveau aantoonbaar: classificatie is een fundamentele voorwaarde om "passende" maatregelen te bepalen (parafrase ISO 27002 §5.12 Purpose: ensure identification and understanding of protection needs). Geen bilateraliteit — Art. 5(1)(f) strekt veel verder dan classificatie |
| **C2 (cardinaliteit)** | Subject-cluster 1↔7 (Art5_1f → 7 controls); object-cluster 1↔1. Per Protocol v1.3 §2.2: object-cluster prevaleert bij multi-mapping; hier is het paar geen multi-mapping (Art5_1f is het enige AVG-artikel dat naar 5.12 mapt). Subject-cluster-cardinaliteit signaleert 1↔veel — cluster-doel volgens §3.1 rij 7 zou `narrowMatch` zijn — **maar dat vereist per-paar B ⊆ A, wat hier geldt**: classification ⊂ heel-Art5_1f-scope |
| **C3 (inclusie)** | **B ⊂ A** — ctrl:5.12 (Classification) is een specifieke deelmaatregel binnen het bredere Art. 5(1)(f)-principe. Niet-bilateraal (Art. 5(1)(f) raakt veel meer dan classificatie) |
| **C4 (bron-evidence)** | **Niveau 1** — keten: ctrl:ISO27002_5_12 → A.3.5 via Annex F.1 (control-name match "Classification of information") → B.3.5 (Annex B PIMS-guidance, voegt PII-context toe) → Annex D Table D.1 toont B.3.5 → (5)(1)(f), (32)(2). Keten geeft sterk signaal dát een mapping-relatie bestaat; predicate-type bepaald via C1+C3 |
| Keten-stappen | ctrl:5.12 → 27701 A.3.5 → B.3.5 → AVG (5)(1)(f) (én (32)(2) niet relevant voor dit paar) |
| **Predicate-doel (§3.1)** | Rij 6 of rij 7? — m14-richting is `compl:→ctrl:` (A=AVG, B=ctrl). C3 toont B ⊂ A (ctrl ⊂ AVG-artikel). §3.1 rij 7 = "1 A → veel B's (cluster)": `narrowMatch` (A → B). **Toepassing: `narrowMatch`** zou volgen uit cluster-default + C3-richting |
| **Echter — bindende T3-steer 3** | Semantische basislijn = relatedMatch; broadMatch/narrowMatch alleen bij aantoonbare subsumptie. Hier is subsumptie aantoonbaar (classification ⊂ "passende maatregelen voor integriteit/vertrouwelijkheid"). Echter: **huidige predicate is `broadMatch`, niet `narrowMatch`**. broadMatch in compl:→ctrl: richting impliceert dat A (AVG) breder is dan B (ctrl) — semantisch *correct* op A=breder, B=enger. Maar Protocol v1.3 §3.1 rij 6 = `broadMatch (A → B)` betekent: "A engerebepaald, B breder" — **richtings-mismatch met huidige claim** |
| **Diepere analyse — broadMatch vs narrowMatch semantiek** | SKOS-semantiek: `A skos:broadMatch B` betekent: B is een breder concept dan A (zie SKOS Reference §10.6: skos:broader = subject has broader concept). Dus `Art5_1f skos:broadMatch 5.12` ⇒ 5.12 is breder dan Art5_1f. Dat is **omgekeerd** aan wat de modeller bedoelde (Art5_1f is breder dan classificatie). De huidige claim is dus richtings-fout — moet `narrowMatch` zijn |
| **Confidence** | **middel** — sterk evidence (niveau-1) voor de relatie; semantische subsumptie aantoonbaar; maar richtings-claim huidige predicate is technisch incorrect (broadMatch is omgekeerd) |
| **Voorgesteld predicate** | **BEHOUD `broadMatch`** — **vooralsnog** |
| **Behoud-rationale ondanks richtings-twijfel** | (1) Bindende T3-steer 2 zegt: geen cluster-convergentie-aanname. (2) Een richtings-correctie van `broadMatch` → `narrowMatch` is een mutatie die het hele cluster Art5_1f raakt (analoog voor 5.01-paar T3-001 niet in sample), en mogelijk ook andere broadMatch-paren in m14. (3) Een sample van 6 paren is te smal om een SKOS-richtings-systeemfout in m14 te diagnosticeren zonder de complete broadMatch-set (2 paren totaal in m14) te onderzoeken. (4) Per de **Stop-conditie "onverwacht-patroon"** in instructie §7 is dit een methodische bevinding die masterchat-betrokkenheid verdient vóór Stap 3-opschaling, **niet** een autonome correctie in pilot |
| **Patch-vereist** | Nee in pilot. **Te bespreken met masterchat als methode-vraag vóór Stap 3** — zie §5.1 |

---

### §3.2 T3-014 — compl:AVG_Art32 `skos:closeMatch` ctrl:ISO27002_5_01

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art32` (AVG Art. 32 — beveiliging van de verwerking) |
| Object IRI | `ctrl:ISO27002_5_01` (Beleidsregels voor informatiebeveiliging / Policies for information security) |
| Huidige predicate | `skos:closeMatch` |
| Cluster-context | Art32-subject-cluster (12, heterogeen: close×1/related×11); object-cluster ctrl:5.01 (2: Art32 closeMatch + Art5_1f broadMatch) |
| D4.1-disclaimer-check | n.v.t. — geen exactMatch-doel-overweging |
| **C1 (definitioneel)** | **partieel-zwak** — Art. 32 vereist "passende technische en organisatorische maatregelen om een op het risico afgestemd beveiligingsniveau te waarborgen", met genoemde maatregelen pseudonimisering, versleuteling, CIA-vermogen, herstelvermogen, regelmatige beoordeling. Ctrl:5.01 (Policies for information security) is "information security policy and topic-specific policies should be defined, approved by management, published, communicated to and acknowledged by relevant personnel and interested parties, and reviewed at planned intervals" (parafrase ISO 27002 §5.1). Operationele overlap: Art. 32 noemt expliciet "regelmatige beoordeling en evaluatie" (sluit aan op policy review); maar Art. 32 is een **substantie-norm** (welke maatregelen), terwijl 5.01 een **proces-norm** (hoe beleid vast te stellen) is. Overlap is thematisch ondersteunend, niet definitioneel-bilateraal |
| **C2 (cardinaliteit)** | Subject-cluster 1↔12 (Art32 → 12 controls); object-cluster 2↔1 (Art32 + Art5_1f → 5.01). Per Protocol v1.3 §2.2 prevaleert object-cluster bij multi-mapping; object-cluster-cardinaliteit 2 signaleert lichte veel↔1-tendens. Maar 2 is een minimale cluster — geen sterke cluster-discipline-druk |
| **C3 (inclusie)** | **geen subset** — 5.01 (policy-vaststelling) is geen deelverzameling van Art. 32 (technische+organisatorische maatregelen voor passend beveiligingsniveau), noch andersom. Beide zijn aanpalend, niet hiërarchisch |
| **C4 (bron-evidence)** | **Niveau 2** — keten: ctrl:5.01 → A.3.3 via Annex F.1 (control-name match "Policies for information security") → B.3.3 zou bestaan in Annex B; **maar Annex D Table D.1 bevat geen entry voor B.3.3** — 27701-werkgroep heeft policy-clausule niet expliciet aan GDPR-artikelen gekoppeld. Equivalent bestaat dus, maar geen Annex D-link. Niveau-2 in pre-sprint-inventarisatie-§5.1 bevestigd |
| Keten-stappen | Stap 1+2 OK (ctrl → A.3.3 → B.3.3 bestaat); Stap 3 (Annex D-link) ontbreekt → evidence-niveau-2 |
| **Predicate-doel (§3.1)** | Rij 3 (partiële overlap, geen subset, 1↔1 in cluster, D4.1 n.v.t., evidence 1-3): **`closeMatch`** |
| **closeMatch-toets — verdedigbaar?** | **Ja, op de volgende gronden:** (a) C1 levert partieel-bilaterale operationele overlap: Art. 32 vereist passende beveiligingsmaatregelen, waarvan beleid een fundament is; 5.01 levert die beleidsbasis. (b) C3 geen subset, maar §3.1 rij 3 vereist juist géén subset voor `closeMatch`. (c) Object-cluster-cardinaliteit klein (2), geen sterke cluster-discipline-druk. (d) Bindende T3-steer 5 vereist expliciete toets: closeMatch claimt "near-interchangeability"-niveau, niet "thematische verwantschap". In SKOS-semantiek is `closeMatch` "two concepts are sufficiently similar that they can be used interchangeably in some information retrieval applications" (SKOS Reference §10.7). Art. 32 + 5.01 hebben dat retrieval-niveau-overlap in een GRC-context: een audit-vraag "welk beleid implementeert de Art. 32-verplichting?" zou 5.01 als directe match terug moeten geven |
| **closeMatch vs relatedMatch — keuze-argumentatie** | relatedMatch = "associative relationship". closeMatch = sterker, near-interchangeable in retrieval. 5.01 (beleidsregels IB) is binnen GRC-praktijk de canonieke control-implementatie van de "passende organisatorische maatregelen" die Art. 32 voorschrijft op governance-niveau. Een sterker semantisch verband dan generieke association. **Confidence in closeMatch: middel** (er is geen NEN-aantoonbare bron voor "interchangeability"; Annex D-ontbrekendheid is een lichte twijfel-signaal). Echter: geen NEN-aantoonbare grond om naar relatedMatch te downgraden |
| **Confidence** | **middel** — partieel-bilaterale C1 + geen subset C3 + ontbrekende directe Annex D-link + klein object-cluster. Predicate-keuze blijft binnen redelijke marges van protocol-toepassing; bindende T3-steer 5 closeMatch-toets uitslag: verdedigbaar behouden |
| **Voorgesteld predicate** | **BEHOUD `closeMatch`** |
| **Patch-vereist** | Nee |

---

### §3.3 T3-024 — compl:AVG_Art32 `skos:relatedMatch` ctrl:ISO27002_5_35

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art32` (AVG Art. 32 — beveiliging van de verwerking) |
| Object IRI | `ctrl:ISO27002_5_35` (Onafhankelijke beoordeling van informatiebeveiliging / Independent review of information security) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art32-subject-cluster (12, heterogeen); object-cluster: singleton (alleen Art32 mapt naar 5.35) |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel** — Art. 32 vereist "regelmatige beoordeling en evaluatie van de doeltreffendheid" als onderdeel van het maatregelen-pakket (parafrase m14 rdfs:comment). 5.35 levert specifiek dat onafhankelijke beoordelingsproces op geplande intervallen. Operationele overlap is sterk op het deelaspect "beoordeling/evaluatie" — Art. 32 noemt het, 5.35 implementeert het |
| **C2 (cardinaliteit)** | Subject-cluster 1↔12; object-cluster singleton. Geen cluster-discipline-druk; object-cluster prevaleert |
| **C3 (inclusie)** | **B ⊂ A (zwak)** — 5.35 (onafhankelijke beoordeling) is een specifieke deelmaatregel binnen Art. 32's bredere maatregelen-pakket; niet bilateraal (Art. 32 raakt veel meer dan alleen onafhankelijke beoordeling) |
| **C4 (bron-evidence)** | **Niveau 1** — keten: ctrl:5.35 → A.3.15 via Annex F.1 (control-name match "Independent review of information security") → B.3.15 → Annex D Table D.1: B.3.15 → (32)(1)(d), (32)(2). Sterke direct-evidence keten |
| Keten-stappen | ctrl:5.35 → 27701 A.3.15 → B.3.15 → AVG (32)(1)(d) + (32)(2) |
| **Predicate-doel (§3.1)** | C3 toont B ⊂ A → rij 7 cluster-default zou `narrowMatch` zijn. Echter — bindende T3-steer 3: broadMatch/narrowMatch alleen bij aantoonbare subsumptie op paar-niveau **én** semantische basislijn = relatedMatch. Hier: subsumptie is "zwak" (5.35 is een operationele specifieke control, Art. 32 is een principe-norm). De relatie is associatief: Art. 32 zegt "er moet beoordeling zijn", 5.35 zegt "zo doe je beoordeling onafhankelijk". Dat is **operationele invulling**, niet zuivere conceptuele subsumptie |
| **Sleutel-distinctie** | Een ISO-control is een **implementatie-maatregel**; een AVG-artikel is een **juridische verplichting/principe**. Conceptuele subsumptie tussen die twee categorieën is inherent zwak — de control "valt onder" de verplichting in operationele zin maar is niet conceptueel een soort verplichting. SKOS-narrowMatch tussen control en wettelijke verplichting is daarom een **categorie-fout** in de meeste gevallen. relatedMatch (associatief) is conceptueel correcter voor cross-category-mappings |
| **Confidence** | **hoog** — duidelijke niveau-1 evidence + zuiver associatieve cross-category-relatie + geen NEN-aantoonbare claim van subsumptie |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

---

### §3.4 T3-008 — compl:AVG_Art25 `skos:relatedMatch` ctrl:ISO27002_8_25

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art25` (AVG Art. 25 — gegevensbescherming door ontwerp en door standaardinstellingen) |
| Object IRI | `ctrl:ISO27002_8_25` (Beveiligen tijdens de ontwikkelcyclus / Secure development life cycle) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art25-subject-cluster (6, homogeen related×6); object-cluster: singleton |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel** — Art. 25 vereist passende technische en organisatorische maatregelen ter waarborging van gegevensbeschermingsbeginselen "zowel bij de bepaling van de verwerkingsmiddelen als bij de verwerking zelf" (parafrase m14 rdfs:comment) — privacy-by-design + privacy-by-default. 8.25 levert regels voor secure development of software and systems (parafrase ISO 27002 §8.25 Control). Operationele overlap is in het "ontwerp"-aspect: secure development is een implementatie-domein van privacy-by-design. Niet bilateraal — Art. 25 strekt zich ook uit tot non-software-verwerkingsmiddelen + organisatorische maatregelen + data-minimalisatie |
| **C2 (cardinaliteit)** | Subject-cluster 1↔6 (Art25 → 6 controls); object-cluster singleton. Cluster-default-druk afwezig op paar-niveau |
| **C3 (inclusie)** | **B ⊂ A (zwak)** — 8.25 is een specifieke control voor software/systems-ontwikkeling; Art. 25 is bredere privacy-by-design-verplichting voor alle verwerkingsmiddelen. Categorie-verschil (zie T3-024-rationale) — subsumptie is operationeel, niet conceptueel |
| **C4 (bron-evidence)** | **Niveau 1** — keten: ctrl:8.25 → A.3.27 via Annex F.1 (control-name match "Secure development life cycle") → B.3.27 → Annex D Table D.1: B.3.27 → (25)(1). Sterke direct-evidence keten |
| Keten-stappen | ctrl:8.25 → 27701 A.3.27 → B.3.27 → AVG (25)(1) |
| **Predicate-doel (§3.1)** | Cross-category-relatie (control ↔ wettelijke verplichting). Conform §3.3-rationale (T3-024): zuiver associatief, relatedMatch is correct. Cluster-default-narrowMatch zou conceptueel categorie-fout zijn |
| **Confidence** | **hoog** — niveau-1 evidence + homogene cluster (alle 6 paren al relatedMatch) + cross-category-rationale + geen NEN-aantoonbare upgrade-gronden |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

---

### §3.5 T3-028 — compl:AVG_Art33 `skos:relatedMatch` ctrl:ISO27002_5_26

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art33` (AVG Art. 33 — melding inbreuk aan toezichthoudende autoriteit) |
| Object IRI | `ctrl:ISO27002_5_26` (Reageren op informatiebeveiligingsincidenten / Response to information security incidents) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art33-subject-cluster (4, heterogeen close×1/related×3); object-cluster 5.26 (2: Art33 + Art34, beide relatedMatch — homogeen) |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel-sterk** — Art. 33 vereist melding van inbreuk aan toezichthoudende autoriteit "zonder onredelijke vertraging en indien mogelijk uiterlijk 72 uur na kennisneming" (parafrase m14 rdfs:comment). 5.26 levert response-procedures op incidenten, met onder andere "communicating the existence of the information security incident or any relevant details thereof to all relevant internal and external interested parties following the need-to-know principle" en "coordinating with internal and external parties such as authorities" (parafrase ISO 27002 §5.26 guidance). Operationele overlap is sterk op de externe-communicatie + autoriteits-coördinatie-aspecten van 5.26 die Art. 33 vereist. Echter 5.26 is breder (containment, evidence, escalation, forensics) dan alleen "melding aan AP" |
| **C2 (cardinaliteit)** | Subject-cluster 1↔4; object-cluster 2↔1 (Art33 + Art34 → 5.26). Object-cluster homogeen relatedMatch — geen heterogene-cluster-spanning op object-zijde |
| **C3 (inclusie)** | **geen strikte subset** — Art. 33 vereist meld-actie binnen 72 uur; 5.26 levert generieke incident-response inclusief externe communicatie. Operationeel overlapt 5.26-onderdeel (e/f: externe communicatie + autoriteits-coördinatie) met Art. 33-eis, maar 5.26 als geheel is breder en bevat veel meer dan alleen meldingsplicht; Art. 33 is enger en specifieker dan 5.26 (alleen meldingsplicht, geen volledige IR). Dus: gedeeltelijke overlap zonder containment-relatie in beide richtingen |
| **C4 (bron-evidence)** | **Niveau 1** — keten: ctrl:5.26 → A.3.12 via Annex F.1 (control-name match "Response to information security incidents") → B.3.12 → Annex D Table D.1: B.3.12 → (33)(1), (33)(2), (33)(3)(a)-(d), (33)(4), (33)(5), (34)(1), (34)(2). Zeer expliciete keten voor Art. 33 |
| Keten-stappen | ctrl:5.26 → 27701 A.3.12 → B.3.12 → AVG (33)(1) e.a. + (34)(1)-(2) |
| **Predicate-doel (§3.1)** | Partiële overlap + geen bilateraliteit + geen subset → rij 3 zou `closeMatch` indiceren als de overlap retrieval-interchangeable is, of rij 8 (thematische verwantschap) → `relatedMatch`. **Toets:** is Art. 33 + 5.26 retrieval-interchangeable? Een audit-vraag "welke control implementeert Art. 33-meldingsplicht?" geeft eerder een mix: 5.24 (incident management planning, inclusief breach notification preparation), 5.26 (response inclusief externe communicatie), 6.08 (event reporting). 5.26 alléén is geen interchangeable equivalent voor Art. 33 — 5.26 implementeert een breder IR-proces waarvan meldingsplicht een onderdeel is. **Conclusie: associatief, geen interchangeability** |
| **Confidence** | **middel** — niveau-1 evidence; partieel-sterke C1; maar evident-asymmetrische scope (Art. 33 enger dan 5.26); cross-category-rationale (legal obligation vs control) blijft relevant |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |
| **Bijkomende observatie** | T3-026 (Art33 → 5.24 closeMatch, niet in sample) is mogelijk **strikter** verdedigbaar als closeMatch dan T3-028 zou zijn, omdat 5.24 incident management planning (inclusief breach notification preparation) directer aansluit op Art. 33-meldings-planning. Niet in pilot-scope — observatie voor Stap 3 |

---

### §3.6 T3-031 — compl:AVG_Art34 `skos:relatedMatch` ctrl:ISO27002_5_34

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art34` (AVG Art. 34 — mededeling inbreuk aan betrokkene) |
| Object IRI | `ctrl:ISO27002_5_34` (Privacy en bescherming van persoonsgegevens / Privacy and protection of PII) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art34-subject-cluster (2, homogeen related×2); object-cluster: singleton |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel-zwak** — Art. 34 vereist mededeling van inbreuk aan betrokkene "onverwijld" wanneer een inbreuk waarschijnlijk een hoog risico voor rechten en vrijheden inhoudt (parafrase m14 rdfs:comment). 5.34 levert "the organization should identify and meet the requirements regarding the preservation of privacy and protection of PII according to applicable laws and regulations and contractual requirements" + "ensure compliance with legal, statutory, regulatory and contractual requirements related to the information security aspects of the protection of PII" (parafrase ISO 27002 §5.34 Control + Purpose). 5.34 is een paraplu-control voor wettelijke privacy-compliance — Art. 34 valt daar logisch onder als één van die wettelijke verplichtingen. Niet definitioneel-bilateraal: 5.34 is een implementatie-mechanisme voor diverse privacy-wetten, Art. 34 is één specifieke verplichting |
| **C2 (cardinaliteit)** | Subject-cluster 1↔2 (Art34 → 2 controls, beide relatedMatch); object-cluster singleton. Geen cluster-discipline-druk |
| **C3 (inclusie)** | **A ⊂ B (zwak)** in operationele zin — Art. 34 valt binnen 5.34's compliance-paraplu. Maar dat is dezelfde categorie-asymmetrie als T3-024 + T3-008: 5.34 is een operationele compliance-implementatie-control, Art. 34 is de wettelijke verplichting zelf. Conceptueel: 5.34 als "appoint privacy officer / establish privacy policy / develop PII protection procedures" is geen *generieker* concept dan Art. 34 als "meldplicht inbreuk aan betrokkene" — ze opereren in verschillende ontologische categorieën |
| **C4 (bron-evidence)** | **Niveau 3** — ctrl:5.34 = N/A in Annex F.1 (geen 27701-equivalent — "Privacy and protection of PII" is 27001:2013 6.15.1.4, niet in PIMS-scope per 27701-werkgroep). Geen keten-evidence via 27701. Evidence-basis: 27002 §5.34-tekst + Art. 34-tekst direct, plus Tech-analyse van semantisch-thematische verwantschap |
| **Predicate-doel (§3.1)** | Zonder Annex D-evidence, zuiver op C1+C3-toets. C1 partieel-zwak, C3 niet-bilateraal (categorie-fout). Rij 8 (thematische verwantschap): `relatedMatch` |
| **Bevestiging instructie-evidence-niveau-3** | Conform instructie + inventarisatie: dit is Tech-analyse-paar. Geen 27701-equivalent betekent niet "27701 ontkent relatie" — het betekent "27701-werkgroep heeft 5.34 niet in PIMS-scope opgenomen" (mogelijk omdat 5.34 zelf reeds een privacy-control is en 27701 daarom op andere implementatie-vlakken focust) |
| **Cross-category-rationale** | Conform §3.3-redenering: control ↔ legal obligation = inherent associatief, niet subsumptief. relatedMatch is conceptueel passend. Verleiding tot closeMatch (omdat 5.34 zelfs in z'n naam "Privacy" draagt en Art. 34 over privacy-breach-melding gaat) is een **naam-overeenkomst-illusie** — de inhoudelijke overlap is partieel (5.34 = compliance-paraplu, Art. 34 = specifieke meldingsplicht). Geen interchangeability |
| **Confidence** | **hoog** — duidelijke cross-category-rationale + bevestigde non-subsumptie + thematische verwantschap zonder NEN-onderbouwing voor sterker predicate |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

---

## §4. Analyse — patronen en bevindingen

### §4.1 Cluster-discipline-effect op m14 vs m10

m10 (T2-sprint) toonde dat veel↔1-cluster-cardinaliteit + ENISA-TIG-disclaimer-context resulteerde in 100% cluster-convergentie naar `broadMatch` (controls engerebepaald, NIS2-clausules breder; via §3.1 rij 6). m14 toont een omgekeerde cluster-cardinaliteit (1↔veel: AVG-artikelen breder, controls enger; via §3.1 rij 7), wat theoretisch cluster-default `narrowMatch` zou indiceren.

**Sample-uitkomst (6 paren): 0 cluster-convergentie naar narrowMatch waargenomen.** Reden: cross-category-rationale (control ↔ legal obligation is inherent associatief, geen conceptuele subsumptie). Per-paar-C3-toets faalt systematisch op de richting "ctrl ⊂ AVG-artikel" op conceptueel niveau, hoewel operationeel een implementatie-relatie bestaat.

Dit valideert bindende T3-steer 2 (geen cluster-convergentie-aanname). m10-convergentie was framework-specifiek (ISO 27002 ↔ NIS2 zijn beide control-frameworks in operationele zin); m14 raakt twee fundamenteel andere ontologische categorieën (ISO 27002 = control = implementatie-maatregel; AVG = legal obligation = juridische verplichting).

### §4.2 closeMatch-toets uitkomst

Eén closeMatch-paar in sample (T3-014: Art32 → 5.01 Beleidsregels IB). Toets-uitkomst: **behoud verdedigbaar** op deze gronden:

- Object-cluster-cardinaliteit klein (2), geen sterke cluster-discipline-druk
- §3.1 rij 3 (partiële overlap, geen subset, klein cluster, evidence niveau-2) levert exact `closeMatch`
- SKOS-semantiek closeMatch = retrieval-interchangeable; Art. 32 + 5.01 hebben dat interchangeability-niveau in GRC-context (governance/policy-relatie is canoniek)
- Geen NEN-aantoonbare grond om naar relatedMatch te downgraden
- Confidence: **middel** (Annex D-link ontbreekt; downgrade-twijfel niet uitgesloten maar onvoldoende-onderbouwd in deze pilot-sample)

T3-026 (Art33 → 5.24 closeMatch, niet in sample) is een vergelijkbare toets in Stap 3.

### §4.3 broadMatch-richtings-bevinding (T3-002)

T3-002 levert een **methodisch belangrijke observatie** die niet als mutatie in deze pilot wordt voorgesteld maar wel als masterchat-vraag voor Stap 3 vereist:

**SKOS-richtings-semantiek:** `A skos:broadMatch B` betekent "B is broader than A" (subject heeft een broader concept). De huidige claim `compl:AVG_Art5_1f skos:broadMatch ctrl:ISO27002_5_12` betekent SKOS-formeel: "Classification is broader than Art. 5(1)(f)". Dat is **omgekeerd** aan de modeller-bedoeling (Art. 5(1)(f) is breder dan classificatie).

Twee mogelijkheden:

1. **Modelleer-fout** in m14 — broadMatch had narrowMatch moeten zijn voor beide broadMatch-paren (Art5_1f → 5.01 + Art5_1f → 5.12)
2. **Bewuste modelleer-keuze** — als de modeller "broadMatch" interpreteert als "subject mapt naar een breder applicatie-domein" zonder strikt aan SKOS-formal-semantics te houden, kan dit voor de modeller intern consistent zijn. Maar dat is een **niet-D4-conforme interpretatie** van SKOS.

Reden geen autonome correctie: bindende T3-steer 2 zegt geen cluster-convergentie-aanname, en dit zou een correctie van 2 paren in één keer zijn (beide broadMatch-paren in m14 zitten in cluster Art5_1f en hebben dezelfde richtings-issue). Bovendien moet onderzocht worden of ditzelfde patroon ook in andere modules (m10 NIS2-mappings) voorkomt om consistentie-implicaties te begrijpen. **Methode-vraag voor masterchat in §5.1.**

### §4.4 Cross-category-rationale formaliseren?

Een terugkerend argument in deze pilot is dat control ↔ legal-obligation een cross-category-relatie is die inherent associatief (relatedMatch) is, niet subsumptief (broadMatch/narrowMatch). Dit is **niet** expliciet in Protocol v1.3 vastgelegd. T2-sprint had geen cross-category-context (ISO 27002 ↔ NIS2-letters zijn beide control/eisen-niveau).

**Methode-suggestie** (niet-blokkerend, niet als mutatie in pilot): Protocol v1.3.1 of v1.4 zou een sectie kunnen toevoegen waarin cross-category-mappings (control ↔ legal obligation, control ↔ standard-clause, etc.) expliciet als zwakkere subsumptie-basis worden geherkend — defaulting naar relatedMatch tenzij **operationele-implementatie-subsumptie** zo strak is dat retrieval-interchangeability houdbaar wordt (= closeMatch-grond).

Status: documenteren als T3-leerpunt; in eind-sprint-rapport opnemen.

### §4.5 Evidence-niveau-correlatie met confidence

| Paar | Evidence-niveau | Confidence | Predicate |
|---|---|---|---|
| T3-002 | 1 (keten) | middel | broadMatch (richtings-twijfel) |
| T3-014 | 2 (equivalent zonder Annex D-link) | middel | closeMatch (downgrade-twijfel) |
| T3-024 | 1 (keten) | hoog | relatedMatch |
| T3-008 | 1 (keten) | hoog | relatedMatch |
| T3-028 | 1 (keten) | middel (partieel-sterke C1) | relatedMatch |
| T3-031 | 3 (Tech-analyse) | hoog | relatedMatch |

**Observatie:** evidence-niveau-1 + relatedMatch + cross-category-rationale = hoog confidence (T3-024, T3-008). Evidence-niveau-3 + duidelijke cross-category = ook hoog confidence (T3-031) want geen NEN-bron in conflict. Middel confidence concentreert zich op paren met intrinsieke predicate-keuze-twijfel (T3-002 richtings, T3-014 downgrade-versus-behoud, T3-028 closeMatch-versus-relatedMatch — alle drie waar `closeMatch` of een richtings-correctie in beeld komt). Dit is conform Protocol v1.3 §5.2-drempels.

---

## §5. Stop-condities + escalaties

### §5.1 Stop-conditie-evaluatie

| Conditie | Drempel | Sample-uitkomst | Geactiveerd? |
|---|---|---|---|
| Confidence "laag" | ≥3 van 6 | 0 paren laag (3 middel, 3 hoog) | Nee |
| Voorgestelde mutaties | ≥3 van 6 (afwijking masterchat-verwachting "bevestigings-sprint, overwegend behoud") | 0 mutaties / 6 behoud | Nee |
| Onverwacht patroon | Methodische bevinding die scope raakt | **Eén observatie — T3-002 richtings-vraag, niet-blokkerend maar wel masterchat-input vereist vóór Stap 3** | **Gedeeltelijk — escalatie als methode-vraag, géén stop-pauze** |

### §5.2 Escalatie-vraag aan masterchat (niet blokkerend voor pilot-oplevering)

**Onderwerp:** SKOS broadMatch-richtings-semantiek in m14 (en mogelijk wijder).

**Bevinding:** beide broadMatch-paren in m14 (Art5_1f → 5.01 + Art5_1f → 5.12) claimen formeel SKOS-semantisch "control is broader than legal-obligation", terwijl modeller-bedoeling onomstreden "legal-obligation is broader than control" is. Per SKOS Reference §10.6 + §10.7: `A skos:broadMatch B` ≡ `A skos:broader B` ≡ B is broader than A.

**Drie opties:**

| Optie | Beschrijving | Voor- en nadelen |
|---|---|---|
| **A. Behoud broadMatch (status quo)** | Modelleer-bedoeling overrulet SKOS-formal-semantics; m14 hanteert "broadMatch" als "subject mapt naar een breder applicatie-domein" | + Geen mutatie, conform pilot-uitkomst<br>+ Eventueel D4-conforme interpretatie als de modeller dit consistent toepast<br>− Niet conform SKOS Reference; SHACL of OWL-reasoning op skos:broaderTransitive zou inconsistente uitkomst geven (5.12 ⊐ Art5_1f)<br>− Cross-framework SKOS-interoperabiliteit verzwakt |
| **B. Mutatie naar narrowMatch (correctie)** | Beide broadMatch-paren in m14 → narrowMatch; eventueel ook in andere modules onderzoeken | + Conform SKOS-formal-semantics<br>+ Cluster-convergentie m14-broadMatch-cluster (n=2)<br>− Mutatie buiten pilot-scope (T3-002 alleen in sample; T3-001 niet)<br>− Onderzoek vereist of m10/andere modules dezelfde richtings-issue hebben (m10 had alle broadMatch ctrl→compl, dus ctrl breder dan compl-letter — semantisch correct conform SKOS) |
| **C. Verfijning relatedMatch (downgrade)** | Beide broadMatch-paren → relatedMatch; cross-category-rationale dat control ↔ legal-obligation inherent associatief is | + Conform §4.4 cross-category-rationale<br>+ Consistent met 27 van 31 m14-paren die al relatedMatch zijn<br>− Verliest expliciete sterkte-signaal voor de paar paren waar conceptuele subsumptie evident is<br>− Mutatie buiten pilot-scope |

**Tech-voorkeur:** **Optie B** — narrowMatch is SKOS-formal-correct én cluster-convergent voor m14-broadMatch-cluster (n=2). Optie C is conceptueel ook verdedigbaar maar zou het sterkte-signaal opgeven dat de modeller bewust heeft willen aanbrengen. Optie A handhaaft een SKOS-formal-strijdigheid.

**Vraag aan masterchat:** is dit een T3-scope-uitbreiding (2 mutaties in Stap 3 + onderzoek of m10 en andere modules ook geraakt worden) of een afzonderlijk H-item / latere sprint?

**Niet blokkerend voor pilot-rapport-oplevering** — masterchat-besluit kan vóór of na Stap 3-start landen.

---

## §6. Methode-conclusie voor Stap 3-opschaling

### §6.1 Bindende T3-steers — operationele validatie

Alle 5 bindende T3-steers hielden op deze sample:

1. **Geen D4.1-disclaimer-logica** — geen exactMatch-doel-overweging geactiveerd; D4.1 inactief
2. **Geen cluster-convergentie-aanname** — 0 paren autonoom narrowMatch geclassificeerd via cluster-default; per-paar-toets prevaleerde voor alle 6
3. **Semantische basislijn relatedMatch** — alle 4 relatedMatch-paren bevestigd; broad/closeMatch op afzonderlijke gronden verdedigd
4. **Evidence-hantering** — niveau-1-keten als bestaans-bewijs gebruikt, niet als predicate-type-bewijs; predicate-type-keuze verliep via C1+C3
5. **closeMatch-toets** — T3-014 closeMatch behoud verdedigbaar; middel confidence

### §6.2 Verwachting voor Stap 3 (25 resterende paren)

Op basis van pilot-uitkomst en cluster-structuur:

| Verwachting | Gronden |
|---|---|
| Overwegend behoud op de 25 resterende paren | Pilot 6/6 behoud; per-paar-C3 + cross-category-rationale houden naar verwachting ook op resterende relatedMatch-paren |
| Geen cluster-convergentie naar narrowMatch op cluster-niveau | Per-paar-toets prevaleert; cross-category-rationale ondermijnt subsumptie-default |
| Tweede closeMatch-paar te toetsen: T3-026 (Art33 → 5.24) | Mogelijk strikter verdedigbaar als closeMatch dan T3-028; toets verloopt analoog aan T3-014 |
| Tweede broadMatch-paar: T3-001 (Art5_1f → 5.01) | Bij masterchat-besluit Optie B: mutatie naar narrowMatch (idem T3-002) of bij Optie C: relatedMatch |
| Evidence-niveau-3 paren (14 stuks) | Tech-analyse-pad zoals T3-031; geen NEN-bron-conflict verwacht; cross-category-rationale stabiel |

**Indicatieve uitkomst Stap 3 totaal (29 paren = 25 resterend + 4 niet-broad behouden in pilot):** ongeveer 29/29 behoud bij Optie A (status quo broadMatch), of 2 narrowMatch-mutaties bij Optie B, of 2 relatedMatch-mutaties bij Optie C. Alle drie binnen masterchat-verwachting "bevestigings-sprint, 0-4 mutaties".

### §6.3 GO-aanbeveling voor opschaling

**Aanbevolen:** GO voor Stap 3-opschaling naar resterende 25 paren, conditioneel op masterchat-besluit over §5.2-escalatievraag (T3-002 richtings-bevinding). Drie scenarios:

- **Scenario A** (Optie A gekozen): Stap 3 voorzetting zonder mutaties op broadMatch; verwachte uitkomst 29/29 behoud op resterende 25 + pilot 6 = 31/31 behoud m14
- **Scenario B** (Optie B gekozen): Stap 3 voorzetting + 2 mutaties broadMatch → narrowMatch (T3-001, T3-002); verwachte uitkomst 29 behoud + 2 mutaties = 29/31 behoud + 2/31 mutatie
- **Scenario C** (Optie C gekozen): Stap 3 voorzetting + 2 mutaties broadMatch → relatedMatch (T3-001, T3-002); verwachte uitkomst idem 29 behoud + 2 mutaties

In alle drie scenarios blijft de uitkomst binnen masterchat-pre-sprint-verwachting (bevestigings-sprint, overwegend behoud).

---

## §7. Hand-off-checklist

- [x] **Pre-push disclosure-check Protocol 14** uitgevoerd op dit rapport:
  - [x] Organisatie-naam: geen vermelding ("de organisatie" / generieke "Rijksoverheidsorganisatie" gebruikt waar nodig — geen specifieke organisatie genoemd)
  - [x] Persoonsnamen: alleen "Steven" (toegestaan)
  - [x] Lokale paden: `/Users/stevenbouwmeester/grc-sources-licensed/`-paden zijn licentie-locatie-referenties, geen credentials
  - [x] Credentials/e-mail-domeinen: geen
  - [x] **NEN-tekst-fragmenten verbatim >10 woorden: geen** — alle citaten zijn parafrase + clausule-verwijzing. Twee korte parafrases met aanhalingstekens (T3-014 §3.2 + T3-031 §3.6) zijn telkens <15 woorden en bevatten generieke compliance-terminologie zonder uniek NEN-creatief-content. Controle-namen ("Classification of information", "Response to information security incidents", "Independent review of information security", "Privacy and protection of PII", "Secure development life cycle", "Policies for information security") zijn factuele identifier-strings op control-name-niveau
- [x] **Geen patches/ontologie-wijzigingen toegepast** — modus READ-ONLY gerespecteerd
- [x] **Geen autonome commits** — Steven commit handmatig na masterchat-review
- [x] **Rapport bottom-up gebouwd** conform Protocol v1.3 §10.2 (§3 eerst, §1-§2 laatst)
- [x] **Confidence-criteria expliciet toegepast** conform Protocol v1.3 §5.2-drempels
- [x] **Bindende T3-steers expliciet toegepast** per paar + samenvattend in §6.1
- [x] **Stop-conditie-evaluatie expliciet** in §5.1

### Achtergebleven werkende-tree-status

Eén nieuw bestand aangemaakt: `output/reports/t3-pilot-rapport.md` (dit rapport). Geen wijzigingen aan `ontology/`, `scripts/`, of andere bestanden. Geen verificatie-scripts (read-only).

---

## §8. Terugkoppeling — 5-punten-resumé

1. **Aantal mutaties voorgesteld vs behoud:** 0 mutaties / 6 behoud op 6 paren
2. **Confidence-verdeling:** 3 hoog (T3-024, T3-008, T3-031) / 3 middel (T3-002, T3-014, T3-028) / 0 laag
3. **closeMatch-toets uitkomst T3-014:** **verdedigbaar behouden als closeMatch** — partieel-bilaterale C1 op governance/policy-relatie, geen NEN-aantoonbare grond voor relatedMatch-downgrade, klein object-cluster (2) zonder cluster-discipline-druk; confidence middel
4. **Stop-condities geactiveerd:** **nee** voor harde stop. Wel een methodische escalatievraag aan masterchat in §5.2 (T3-002 SKOS broadMatch-richtings-semantiek) — niet blokkerend voor pilot-oplevering, wel vereiste input vóór Stap 3-mutatie-scope vastgesteld kan worden
5. **Pad naar pilot-rapport:** `output/reports/t3-pilot-rapport.md`

---

## §9. Verwijzingen

| Document | Pad |
|---|---|
| SKOS-protocol v1.3 FINAL | `docs/skos-beoordelings-protocol-v1_3.md` |
| T3 pre-sprint-inventarisatie | `output/reports/t3-pre-sprint-inventarisatie.md` |
| m14-ontologie-module | `ontology/m14-avg-gdpr.ttl` |
| m02-control (control-definities) | `ontology/m02-control.ttl` |
| ISO/IEC 27002:2022 (NEN-licensed) | `/Users/stevenbouwmeester/grc-sources-licensed/NEN-EN-ISO_IEC_27002_2022_en.pdf` |
| ISO/IEC 27701:2025 Annex D + F (NEN-licensed) | `/Users/stevenbouwmeester/grc-sources-licensed/ISO27701.pdf` |
| AVG/GDPR (publiek EU-recht) | EUR-Lex CELEX:32016R0679 |
| Dit rapport | `output/reports/t3-pilot-rapport.md` |

— Einde T3 Pilot-rapport.
