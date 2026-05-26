---
type: report
subtype: stap4-rapport
sprint: T1
stap: 4
baseline: v4.6.0
date: 2026-05-26
status: final
related:
  - H36_skos-exactmatch-ctrl-compl-audit
  - D04_skos-cross-framework
  - skos-beoordelings-protocol-v1_0
  - t1-presprint-inventarisatie-v4_6_0
  - t1-pilot-rapport-stap3-v4_6_0
  - patch-rapport-v4_6_1
scope: "Stap 4 — resterende 23 paren + patch v4.6.1-voorbereiding. Cluster-representant-beoordeling (c, d, f), cluster-discipline-toepassing (b, c, d, e, f, i), edge-case-analyse (T1-023, T1-021) — twee-zijdig zonder Tech-voorstel. Read-only op TTL; voorbereiding alleen. Geen git-commits/pushes door Tech."
---

# T1 — Stap 4-rapport (23 resterende paren)

## §0. Samenvatting

- **26 paren herclassificeerbaar** als skos:broadMatch (5 pilot Stap 3 + 21 cluster-overerving/representant Stap 4) — confidence "hoog", patroon consistent met pilot, geen onverwachte uitkomsten.
- **3 cluster-representanten** uit clusters c/d/f bevestigen pilot-patroon (UV-Annex-decompositie + ENISA-disclaimer-categorisch + C1/C2/C3-failure).
- **2 edge-cases** (T1-023, T1-021) gaan naar masterchat-NEN-toets via twee twijfelgevallen — Tech doet **géén** voorstel, biedt twee-zijdige analyse per paar.
- Stop-condities Stap 4: **geen geraakt** voor §1-§2 (cluster-werk). Edge-cases h/j zijn verwachte masterchat-route, geen stop-conditie.
- **Patch v4.6.1 voorbereid**: `diff-26-broadMatch.ttl` (zeker), `diff-2-edge-cases.ttl` (onder masterchat). Verificatie-bundel (canonical metrics + SHACL + file-hashes) op gepatchte versie scenario C voltooid — alle metrics conform verwachting.

**Eindoordeel Tech**: GO voor masterchat-NEN-toets op T1-023 + T1-021. Stap-4-werk leverbaar, patch-rapport `patch-rapport-v4_6_1.md` separaat.

---

## §1. Cluster-representant-beoordelingen (clusters c, d, f)

Pilot Stap 3 bevatte representanten voor clusters a, b, e, g, i (paren #1, #3, #4, #5 + #2 voor 1↔1). Voor clusters c, d, f was geen pilot — Stap 4 vereist één representant per cluster met volledige vier-criteria-check inclusief C2-buiten-set-check in 121-set.

### §1.1 Representant cluster c — T1-014 (ctrl:ISO27002_5_29 ↔ compl:NIS2_Art21_c)

| Veld | Inhoud |
|---|---|
| Paar-ID | T1-014 |
| Subject IRI | `ctrl:ISO27002_5_29` ("Informatiebeveiliging tijdens een verstoring") |
| Object IRI | `compl:NIS2_Art21_c` ("Bedrijfscontinuïteit, back-upbeheer en noodherstel") |
| Cluster-context | NIS2-clause (c) — **3↔1 binnen 28-set** (5_29, 5_30, 8_13); buiten-set: NIS2_c heeft tevens 7_11 closeMatch + 8_14 closeMatch + 8_06 broadMatch + 5_24 relatedMatch + 8_31 relatedMatch. **9 mappings totaal richting NIS2_c**. |
| C1 Definitioneel | **✗** — Subject 5_29 dekt "informatiebeveiliging tijdens verstoring" — één fase binnen continuïteits-lifecycle. NIS2_c omvat business continuity (planning + uitvoering), back-upbeheer én disaster recovery. UV-Annex hoofdstuk 4 (Business continuity and crisis management, art.21(2)(c)) splitst dit in 4.1 BC/DR-plan + 4.2 backup management + 4.3 crisis management. Subject is één positie binnen drie-deling. |
| C2 Cardinaliteit | **✗** — 3↔1 binnen 28-set zichtbare C2-failure; 9↔1 in 121-set bevestigt structureel. UV-Annex-3-deling versterkt. |
| C3 Inclusie | **✗ partial: A ⊆ B, geen B ⊆ A** — informatiebeveiliging-tijdens-verstoring ⊆ continuïteit-NIS2_c; omgekeerd niet (NIS2_c omvat ook backup + DR-plan + crisis-mgmt). |
| C4 Bron | **Niveau 1** — CBW-Excel "Mapping Uitvoeringsverordening" toont UV 4.x → A.5.29/5.30 + A.8.13/8.14. ENISA TIG regel 285 disclaimer geldt: mapping ≠ equivalence. |
| Voorstel | **herclass-broadMatch** — subject enger dan object; B is breder; protocol §3 C1/C3-failure → A skos:broadMatch B. |
| Confidence | **hoog** — pilot-patroon-consistent; UV-3-deling structureel; evidence-niveau 1. |
| Patch-vereist | ja |
| Cluster-discipline | Cluster-c (3 paren: T1-014, T1-015, T1-022) krijgt **3× broadMatch** — geen reden voor uitzondering: T1-015 (5_30 ICT-gereedheid bedrijfscontinuïteit) sluit aan op UV 4.1; T1-022 (8_13 Back-up van informatie) op UV 4.2 — beide één-fase-controls in drie-deling. |

### §1.2 Representant cluster d — T1-006 (ctrl:ISO27002_5_19 ↔ compl:NIS2_Art21_d)

| Veld | Inhoud |
|---|---|
| Paar-ID | T1-006 |
| Subject IRI | `ctrl:ISO27002_5_19` ("Informatiebeveiliging in leveranciersrelaties") |
| Object IRI | `compl:NIS2_Art21_d` ("Beveiliging van de toeleveringsketen") |
| Cluster-context | NIS2-clause (d) — **4↔1 binnen 28-set** (5_19, 5_20, 5_21, 5_22); buiten-set: NIS2_d heeft tevens 5_23 closeMatch + 5_31 relatedMatch + 8_30 broadMatch. **7 mappings totaal richting NIS2_d**. |
| C1 Definitioneel | **✗** — Subject 5_19 dekt "leveranciersrelaties" — algemene relatie-eis. NIS2_d "toeleveringsketen-beveiliging" omvat de hele supply-chain-lifecycle: relaties + contracten + ICT-toeleveringsketen-beheer + monitoring/wijzigingen. UV-Annex hoofdstuk 5 (Supply chain security, art.21(2)(d)) verdeelt dit in meerdere sub-clauses die afzonderlijke ISO-controls aanroepen. Subject is één van vier 28-set-controls voor één thematische clause. |
| C2 Cardinaliteit | **✗** — 4↔1 binnen 28-set duidelijke C2-failure; 7↔1 in 121-set bevestigt. |
| C3 Inclusie | **✗ partial: A ⊆ B, geen B ⊆ A** — leveranciers-relatie-mgmt ⊆ supply-chain-security; omgekeerd faalt (NIS2_d omvat ook contracten 5_20, ICT-keten 5_21, wijzigingsmonitoring 5_22). |
| C4 Bron | **Niveau 1** — CBW-Excel UV 5.x → A.5.19/5.20/5.21/5.22. ENISA TIG regel 285 disclaimer geldt. |
| Voorstel | **herclass-broadMatch** — subject enger; protocol §3 C1/C3-failure. |
| Confidence | **hoog** — patroon identiek aan pilot cluster-i en cluster-e; UV-decompositie structureel. |
| Patch-vereist | ja |
| Cluster-discipline | Cluster-d (4 paren: T1-006, T1-007, T1-008, T1-009) krijgt **4× broadMatch** — geen reden voor uitzondering: T1-007 (5_20 leveranciersovereenkomsten), T1-008 (5_21 ICT-toeleveringsketen), T1-009 (5_22 monitoring/wijzigingsbeheer leveranciersdiensten) — alle drie aspect-specifieke controls binnen supply-chain-thema. |

### §1.3 Representant cluster f — T1-016 (ctrl:ISO27002_5_35 ↔ compl:NIS2_Art21_f)

| Veld | Inhoud |
|---|---|
| Paar-ID | T1-016 |
| Subject IRI | `ctrl:ISO27002_5_35` ("Onafhankelijke beoordeling van informatiebeveiliging") |
| Object IRI | `compl:NIS2_Art21_f` ("Beoordeling doeltreffendheid cyberbeveiligingsmaatregelen") |
| Cluster-context | NIS2-clause (f) — **2↔1 binnen 28-set** (5_35, 5_36); buiten-set: NIS2_f heeft tevens 8_08 broadMatch + 8_15 relatedMatch + 8_16 broadMatch + 8_34 closeMatch. **6 mappings totaal richting NIS2_f**. Subject 5_35 heeft daarnaast `skos:closeMatch compl:NIS2_Art21_a` op een ander object — **geen collision binnen 28-set** (andere object) maar relevant voor cluster-discipline-discussie. |
| C1 Definitioneel | **✗ marginaal-naar-duidelijk** — Subject 5_35 dekt "onafhankelijke beoordeling" (audit-vorm). NIS2_f vraagt "beleid en procedures om de doeltreffendheid van cyberbeveiligingsrisicobeheer-maatregelen te beoordelen" — breder dan alleen onafhankelijke audit (omvat ook self-assessment, monitoring, KPI's). UV-Annex hoofdstuk 7 (Policies and procedures to assess effectiveness, art.21(2)(f)) gaat verder dan ISO27002_5_35. Subject is één instrument binnen breder doeltreffendheids-thema. |
| C2 Cardinaliteit | **✗** — 2↔1 binnen 28-set; 6↔1 in 121-set. UV-hoofdstuk 7 als één hoofdstuk lijkt minder breed dan c/d/i, maar buiten-set-mappings tonen dat NIS2_f thematisch wel breder is dan één ISO-control. |
| C3 Inclusie | **✗ partial: A ⊆ B, geen B ⊆ A** — onafhankelijke audit ⊆ doeltreffendheidsbeoordeling; omgekeerd faalt (5_35 dekt niet self-assessment of compliance-monitoring zoals 5_36 of 8_34). |
| C4 Bron | **Niveau 1** — CBW-Excel UV 7.x → A.5.35/5.36. ENISA TIG regel 285 disclaimer geldt. |
| Voorstel | **herclass-broadMatch** — subject enger. |
| Confidence | **hoog** — patroon consistent met pilot; cluster-grootte 2 minder dramatisch dan i (6) of e (5) maar UV-decompositie structureel vergelijkbaar. |
| Patch-vereist | ja |
| Cluster-discipline | Cluster-f (2 paren: T1-016, T1-017) krijgt **2× broadMatch** — geen reden voor uitzondering: T1-017 (5_36 Naleving van beleid) is compliance-monitoring-aspect binnen zelfde doeltreffendheids-thema. |

### §1.4 Samenvatting §1

| Cluster | Representant | Uitkomst | Confidence | Bron-niveau |
|---|---|---|---|---|
| c | T1-014 | broadMatch | hoog | 1 |
| d | T1-006 | broadMatch | hoog | 1 |
| f | T1-016 | broadMatch | hoog | 1 |

**Geen stop-conditie geraakt.** Alle drie cluster-representanten reproduceren pilot-patroon (broadMatch op basis van UV-Annex-decompositie + ENISA-disclaimer-categorisch + C1/C2/C3-failure). Buiten-set-check in 121-set bevestigt dat geen van de drie objecten een unieke 1↔1 mapping heeft.

---

## §2. Cluster-discipline-toepassing (clusters b, c, d, e, f, i)

Per cluster: identieke herclassificatie op cluster-volgers als op pilot/representant, tenzij voor specifiek paar individuele uitzondering aantoonbaar is. Format conform sprint-instructie §3.

### §2.1 Cluster b — Incidentbehandeling (4↔1)

Pilot: **T1-010** (5_24, broadMatch, hoog, niveau 1) — Stap 3 §2.3.

| Paar-ID | Subject IRI | Object IRI | Cluster | Pilot/repr | Uitzondering aangetoond? | Voorstel | Confidence | Patch-vereist |
|---|---|---|---|---|---|---|---|---|
| T1-011 | ctrl:ISO27002_5_25 | compl:NIS2_Art21_b | b (4↔1) | T1-010 broad | nee — 5_25 "Beoordelen van en besluiten over informatiebeveiligingsgebeurtenissen" is detectie/classificatie-fase, sluit aan op UV 3.4 (event assessment) | overerving broadMatch | hoog (overerving) | ja |
| T1-012 | ctrl:ISO27002_5_26 | compl:NIS2_Art21_b | b (4↔1) | T1-010 broad | nee — 5_26 "Reageren op informatiebeveiligingsincidenten" is response-fase, sluit aan op UV 3.5 (incident response) | overerving broadMatch | hoog (overerving) | ja |
| T1-013 | ctrl:ISO27002_5_27 | compl:NIS2_Art21_b | b (4↔1) | T1-010 broad | nee — 5_27 "Leren van informatiebeveiligingsincidenten" is post-incident review, sluit aan op UV 3.6 (post-incident reviews) | overerving broadMatch | hoog (overerving) | ja |

### §2.2 Cluster c — Continuïteit (3↔1)

Representant: **T1-014** (5_29, broadMatch, hoog, niveau 1) — §1.1.

| Paar-ID | Subject IRI | Object IRI | Cluster | Pilot/repr | Uitzondering aangetoond? | Voorstel | Confidence | Patch-vereist |
|---|---|---|---|---|---|---|---|---|
| T1-015 | ctrl:ISO27002_5_30 | compl:NIS2_Art21_c | c (3↔1) | T1-014 broad | nee — 5_30 "ICT-gereedheid voor bedrijfscontinuïteit" sluit aan op UV 4.1 (BC/DR-plan) | overerving broadMatch | hoog (overerving) | ja |
| T1-022 | ctrl:ISO27002_8_13 | compl:NIS2_Art21_c | c (3↔1) | T1-014 broad | nee — 8_13 "Back-up van informatie" sluit aan op UV 4.2 (backup management) | overerving broadMatch | hoog (overerving) | ja |

### §2.3 Cluster d — Toeleveringsketen (4↔1)

Representant: **T1-006** (5_19, broadMatch, hoog, niveau 1) — §1.2.

| Paar-ID | Subject IRI | Object IRI | Cluster | Pilot/repr | Uitzondering aangetoond? | Voorstel | Confidence | Patch-vereist |
|---|---|---|---|---|---|---|---|---|
| T1-007 | ctrl:ISO27002_5_20 | compl:NIS2_Art21_d | d (4↔1) | T1-006 broad | nee — 5_20 "Adresseren van informatiebeveiliging in leveranciersovereenkomsten" is contractuele-aspect binnen supply chain | overerving broadMatch | hoog (overerving) | ja |
| T1-008 | ctrl:ISO27002_5_21 | compl:NIS2_Art21_d | d (4↔1) | T1-006 broad | nee — 5_21 "Beheren van informatiebeveiliging in de ICT-toeleveringsketen" is ICT-specifiek aspect binnen supply chain | overerving broadMatch | hoog (overerving) | ja |
| T1-009 | ctrl:ISO27002_5_22 | compl:NIS2_Art21_d | d (4↔1) | T1-006 broad | nee — 5_22 "Monitoren, beoordelen en beheren van wijzigingen van leveranciersdiensten" is monitor/wijzigings-aspect | overerving broadMatch | hoog (overerving) | ja |

### §2.4 Cluster e — Verwerving/ontwikkeling (5↔1)

Pilot: **T1-024** (8_25, broadMatch, hoog, niveau 1) — Stap 3 §2.5.

| Paar-ID | Subject IRI | Object IRI | Cluster | Pilot/repr | Uitzondering aangetoond? | Voorstel | Confidence | Patch-vereist |
|---|---|---|---|---|---|---|---|---|
| T1-025 | ctrl:ISO27002_8_26 | compl:NIS2_Art21_e | e (5↔1) | T1-024 broad | nee — 8_26 "Toepassingsbeveiligingseisen" is app-eisen-aspect binnen ontwikkelings-thema (UV 6.x sub-clauses) | overerving broadMatch | hoog (overerving) | ja |
| T1-026 | ctrl:ISO27002_8_27 | compl:NIS2_Art21_e | e (5↔1) | T1-024 broad | nee — 8_27 "Veilige systeemarchitectuur en technische uitgangspunten" is architectuur-aspect | overerving broadMatch | hoog (overerving) | ja |
| T1-027 | ctrl:ISO27002_8_28 | compl:NIS2_Art21_e | e (5↔1) | T1-024 broad | nee — 8_28 "Veilig coderen" is coderings-aspect | overerving broadMatch | hoog (overerving) | ja |
| T1-028 | ctrl:ISO27002_8_29 | compl:NIS2_Art21_e | e (5↔1) | T1-024 broad | nee — 8_29 "Testen van de beveiliging tijdens ontwikkeling en acceptatie" is test-aspect (UV 6.5) | overerving broadMatch | hoog (overerving) | ja |

### §2.5 Cluster f — Doeltreffendheid (2↔1)

Representant: **T1-016** (5_35, broadMatch, hoog, niveau 1) — §1.3.

| Paar-ID | Subject IRI | Object IRI | Cluster | Pilot/repr | Uitzondering aangetoond? | Voorstel | Confidence | Patch-vereist |
|---|---|---|---|---|---|---|---|---|
| T1-017 | ctrl:ISO27002_5_36 | compl:NIS2_Art21_f | f (2↔1) | T1-016 broad | nee — 5_36 "Naleving van beleid, regels en normen voor informatiebeveiliging" is compliance-monitoring-aspect binnen doeltreffendheids-thema | overerving broadMatch | hoog (overerving) | ja |

### §2.6 Cluster i — Personeel + toegang + activa (6↔1)

Pilot: **T1-002** (5_09, broadMatch, hoog, niveau 1) — Stap 3 §2.4.

| Paar-ID | Subject IRI | Object IRI | Cluster | Pilot/repr | Uitzondering aangetoond? | Voorstel | Confidence | Patch-vereist |
|---|---|---|---|---|---|---|---|---|
| T1-003 | ctrl:ISO27002_5_15 | compl:NIS2_Art21_i | i (6↔1) | T1-002 broad | nee — 5_15 "Toegangsbeveiliging" sluit aan op UV 11.x (Access control) | overerving broadMatch | hoog (overerving) | ja |
| T1-004 | ctrl:ISO27002_5_16 | compl:NIS2_Art21_i | i (6↔1) | T1-002 broad | nee — 5_16 "Identiteitsbeheer" sluit aan op UV 11.x | overerving broadMatch | hoog (overerving) | ja |
| T1-005 | ctrl:ISO27002_5_18 | compl:NIS2_Art21_i | i (6↔1) | T1-002 broad | nee — 5_18 "Toegangsrechten" sluit aan op UV 11.x | overerving broadMatch | hoog (overerving) | ja |
| T1-018 | ctrl:ISO27002_6_01 | compl:NIS2_Art21_i | i (6↔1) | T1-002 broad | nee — 6_01 "Screening" sluit aan op UV 10.x (HR security) | overerving broadMatch | hoog (overerving) | ja |
| T1-019 | ctrl:ISO27002_6_02 | compl:NIS2_Art21_i | i (6↔1) | T1-002 broad | nee — 6_02 "Arbeidsovereenkomst" sluit aan op UV 10.x (HR security) | overerving broadMatch | hoog (overerving) | ja |

### §2.7 Samenvatting §2 — cluster-overerving

| Cluster | # volgers | Allen broadMatch? | Uitzonderingen | Stop-conditie |
|---|---:|---|---|---|
| b | 3 | ja | 0 | nee |
| c | 2 | ja | 0 | nee |
| d | 3 | ja | 0 | nee |
| e | 4 | ja | 0 | nee |
| f | 1 | ja | 0 | nee |
| i | 5 | ja | 0 | nee |
| **Totaal** | **18** | **ja** | **0** | **nee** |

Stop-conditie 2 ("≥2 cluster-volgers met uitzondering binnen één cluster"): **niet geraakt**. Stop-conditie 3 ("buiten-set-collision"): geen vondst — geen bestaande broadMatch/closeMatch/relatedMatch op identiek subject-object-paar (predicate-mutatie alleen).

**Cluster-overerving totaal Stap 4: 18 paren** (3 b-volgers + 2 c-volgers + 3 d-volgers + 4 e-volgers + 1 f-volger + 5 i-volgers). Plus 3 representanten c/d/f uit §1 = 21 paren. Plus 5 pilot-paren Stap 3 = **26 paren zeker** (scenario A van patch).

---

## §3. Edge-case-analyse — T1-023 + T1-021

Beide paren zijn 1↔1 binnen 28-set met UV-Annex sub-clause die direct naar één ISO-control mapt. ENISA-disclaimer geldt categorisch, maar bilaterale containment kan in theorie uitkomst beïnvloeden. Tech levert **uitsluitend twee-zijdige analyse**; **géén voorstel**. Masterchat-NEN-toets vereist.

### §3.1 T1-023 — ctrl:ISO27002_8_24 ↔ compl:NIS2_Art21_h (Cryptografie)

**Subject IRI:** `ctrl:ISO27002_8_24` ("Gebruik van cryptografie")
**Object IRI:** `compl:NIS2_Art21_h` ("Cryptografie en encryptie")
**Cluster:** h (1↔1 in 28-set)

**Pro-broadMatch:**

- ENISA TIG regel 285-disclaimer geldt categorisch — autoritatieve mapping-bron erkent relatie maar verbiedt expliciet "equivalence"-interpretatie.
- 121-set NIS2_h heeft **6 andere ctrl:-mappings**: 5_14 closeMatch + 8_03 relatedMatch + 8_11 relatedMatch + 8_05 broadMatch + 8_20 broadMatch + 8_21 broadMatch. Object is dus geen unieke 1↔1.
- NIS2_h volledige tekst (NIS2 art.21(2)(h)): "**policies and procedures regarding the use of cryptography** and, where appropriate, encryption" — omvat use + policies/procedures.
- ISO27002:2022 §8.24 label (Nederlands): "**Gebruik van** cryptografie" — focust expliciet op gebruik, niet (primair) op policies/procedures.
- Mogelijke C1-failure: NIS2_h omvat policy/procedure-dimensie die ISO27002 §8.24 niet als primair bestek heeft → A enger dan B → broadMatch logisch.
- Consistentie met pilot-patroon: alle 5 pilot-paren leverden broadMatch ondanks variatie in cluster-cardinaliteit; 1↔1-binnen-28-set bleek geen behoud-trigger voor T1-001 en T1-020 wegens C1-failure en buiten-set-check.

**Pro-exactMatch-behoud:**

- UV-Annex hoofdstuk 9 (Cryptography, art.21(2)(h)) heeft **één sub-clause 9.1** — geen multi-clause-spread zoals bij c/d/f/i.
- 28-set-cardinaliteit 1↔1 op subject-zijde (8_24 mapt nergens anders heen binnen 28-set).
- CBW-Excel UV 9.1 mapt direct naar A.8.24 (= ISO27002 8.24).
- Geen structurele bewijslast tegen exactMatch buiten de ENISA-disclaimer.
- Indien ISO27002:2022 §8.24-tekst-toegang aantoont dat §8.24 ook policy + procedure adresseert (niet alleen "gebruik"-techniek), dan B ⊆ A geldt en C1+C3 zouden alsnog kunnen slagen.

**Tech-positie:** pro-broadMatch op basis van ENISA-disclaimer-categorisch + 121-set-buiten-set-data + NIS2_h-tekst-breedte. exactMatch-behoud denkbaar als bilaterale containment uit ISO27002:2022 §8.24-tekst hard te maken is.

### §3.2 T1-021 — ctrl:ISO27002_8_05 ↔ compl:NIS2_Art21_j (MFA + secured-comm)

**Subject IRI:** `ctrl:ISO27002_8_05` ("Beveiligde authenticatie")
**Object IRI:** `compl:NIS2_Art21_j` ("Multi-factor authenticatie en continue authenticatie")
**Cluster:** j (1↔1 in 28-set)

**Pro-broadMatch:**

- ENISA TIG regel 285-disclaimer geldt categorisch.
- 121-set NIS2_j heeft **7+ andere ctrl:-mappings**: 5_15 closeMatch + 5_16 closeMatch + 5_17 closeMatch + 8_03 relatedMatch + 8_22 relatedMatch + 5_32 relatedMatch + 6_07 broadMatch + 8_02 broadMatch. Object is dus géén unieke 1↔1.
- NIS2_j volledige tekst (NIS2 art.21(2)(j)): "the use of multi-factor authentication or continuous authentication solutions, **secured voice, video and text communications and secured emergency communication systems** within the entity, where appropriate" — MFA én secured-communications. Twee thema's in één clause.
- ISO27002:2022 §8.05 label (Nederlands): "Beveiligde authenticatie" — alleen authentication-aspect.
- Mogelijke C1-failure: NIS2_j omvat secured-communication-elementen (voice/video/text/emergency) die voorbij authentication gaan. ISO27002:2022 §8.05 adresseert deze waarschijnlijk niet — A enger dan B → broadMatch logisch.
- Subject 8_05 heeft tevens `skos:broadMatch compl:NIS2_Art21_h` (bestaand) — geen collision (ander object), maar toont dat subject-zijde reeds breder gemodelleerd is voor andere clause.

**Pro-exactMatch-behoud:**

- UV-Annex hoofdstuk 11 (Access control) deelt met (i) en (j); UV 11.7 ("Multi-factor authentication") mapt direct naar A.8.5 als enige sub-clause op NIS2_j-zijde — relatief schone 1↔1-mapping op UV-niveau.
- 28-set-cardinaliteit 1↔1.
- Geen UV-decompositie-multi-clause-spread voor MFA-element (1 sub-clause).
- Indien ISO27002:2022 §8.05-tekst-toegang aantoont dat §8.05 ook secured-communications adresseert (bv. via channel-protection-eisen), dan B ⊆ A geldt en exactMatch verdedigbaar.

**Tech-positie:** pro-broadMatch op basis van NIS2_j-tekst-breedte voorbij authentication (secured-communications-elementen ontbreken in ISO27002 §8.05-titel/scope). exactMatch-behoud denkbaar als ISO27002:2022 §8.05 ook secured-communications adresseert.

### §3.3 Twijfelgevallen-tabel — masterchat-NEN-PK-vragen

| Paar-ID | Subject | Object | C1 | C2 | C3 | C4-niveau | Tech-voorstel | Confidence | Vraag aan Masterchat |
|---|---|---|---|---|---|---|---|---|---|
| T1-023 | ctrl:ISO27002_8_24 | compl:NIS2_Art21_h | onbeslist | ✗ (buiten-set 6↔1) | onbeslist | 1 (mapping aanwezig) + ENISA-disclaimer | **geen** — twee-zijdig | n.v.t. | Is de scope van ISO27002:2022 §8.24 ("Gebruik van cryptografie") bilateraal identiek aan NIS2 art.21(2)(h) ("policies and procedures regarding the use of cryptography and, where appropriate, encryption"), of dekt NIS2_h aspecten (policies/procedures) die ISO27002 §8.24 niet adresseert? — Tech-positie pro-broadMatch op basis van ENISA-disclaimer + 121-set-buiten-set-data; exactMatch-behoud denkbaar bij bilaterale containment-bewijs uit ISO27002:2022-tekst. |
| T1-021 | ctrl:ISO27002_8_05 | compl:NIS2_Art21_j | onbeslist | ✗ (buiten-set 7↔1) | onbeslist | 1 (mapping aanwezig) + ENISA-disclaimer | **geen** — twee-zijdig | n.v.t. | Is de scope van ISO27002:2022 §8.05 ("Beveiligde authenticatie") bilateraal identiek aan NIS2 art.21(2)(j) ("multi-factor authentication or continuous authentication solutions, secured voice, video and text communications and secured emergency communication systems"), of is NIS2_j breder door secured-communication-aspecten buiten authentication? — Tech-positie pro-broadMatch op basis van NIS2_j-tekst-breedte voorbij authentication; exactMatch-behoud denkbaar als ISO27002:2022 §8.05 ook secured-communications adresseert. |

### §3.4 Edge-case-status

- T1-023 en T1-021 **niet** opgenomen in `diff-26-broadMatch.ttl`.
- Beide voorbereid in `diff-2-edge-cases.ttl` als broadMatch-variant, separaat toepasbaar (0, 1 of 2 keuzes mogelijk).
- Bij masterchat-besluit "behoud exactMatch": diff-2 niet toepassen voor dat paar.
- Bij masterchat-besluit "closeMatch in plaats van broadMatch": Stap 5 vereist aanpassing diff-2-paar.

---

## §4. Stop-conditie-check Stap 4

| # | Conditie | Telling | Hit? |
|---|---|---|---|
| 1 | Onverwachte cluster-uitkomst c/d/f (representant ≠ broadMatch ondanks C2-failure) | 0 representanten leverden andere uitkomst | nee |
| 2 | ≥2 cluster-volgers met uitzondering binnen één cluster | 0 uitzonderingen geclaimd over 18 volgers in 6 clusters | nee |
| 3 | Buiten-set-collision (bestaande broad/close/related voor zelfde subject-object) | 0 collisions — alle 26 predicate-mutaties op (subject, object)-paren die elders geen ctrl:↔compl:-relatie hebben buiten de te wijzigen exactMatch | nee |

**Geen stop-conditie geraakt voor §1-§2.** Edge-cases h/j zijn **verwachte masterchat-route** conform sprint-instructie §4.3 — geen stop-conditie.

**Eindoordeel:** GO voor patch-voorbereiding (26 zeker) + masterchat-NEN-toets op h/j.

### §4.1 Geen geconstateerde namespace-leakage of D-conformance-risico

- D4 (SKOS lichtere relatie verdedigbaar): conform — broadMatch is bekend D4-patroon (38 → 66 mappings in pre-inference).
- D5 (ctrl↔bio sameAs, 93): ongewijzigd — patch raakt geen owl:sameAs.
- D11 (asset-brug 5): ongewijzigd.
- D7 (BIO2-overblijfselen 0): ongewijzigd.

---

## §5. Patch-voorbereiding-status

### §5.1 Bestanden gereed

| Bestand | Pad | Doel |
|---|---|---|
| `diff-26-broadMatch.ttl` | `output/patches/diff-26-broadMatch.ttl` | Patch-instructie voor 26 zekere paren (5 pilot + 3 representanten + 18 cluster-volgers) |
| `diff-2-edge-cases.ttl` | `output/patches/diff-2-edge-cases.ttl` | Patch-instructie voor T1-023 + T1-021, separaat toepasbaar onder masterchat-besluit |
| `canonical_metrics_v4_6_1.py` | `output/verification/canonical_metrics_v4_6_1.py` | Metrics-script (versie-suffix-conventie sinds v4.3.3) |
| `canonical_metrics_v4_6_1.json` | `output/verification/canonical_metrics_v4_6_1.json` | Metrics op scenario C (alle 28 toegepast) — referentie voor patch-rapport |
| `shacl_split_validate_v4_6_1.py` | `output/verification/shacl_split_validate_v4_6_1.py` | SHACL gesplitste validatie |
| `shacl_results_v4_6_1.json` | `output/verification/shacl_results_v4_6_1.json` | SHACL-resultaten scenario C |
| `file_hashes_v4_6_1.txt` | `output/verification/file_hashes_v4_6_1.txt` | SHA256-hashes per .ttl-module, vergelijking met v4.6.0 |
| `patch-rapport-v4_6_1.md` | `output/reports/patch-rapport-v4_6_1.md` | Separaat patch-rapport voor v4.6.1-oplevering |

### §5.2 Verwachte metrics scenario C (gemeten op gepatchte versie)

| Metric | v4.6.0 | v4.6.1 (scenario C) | Δ | Verklaring |
|---|---:|---:|---:|---|
| Pre-inference triples | 20.950 | 20.950 | 0 | Predicate-mutatie houdt triple-totaal constant |
| Post-inference triples (OWL RL) | 44.907 | 44.907 | 0 | Predicate-mutatie idem |
| skos_mappings_total | 1.798 | 1.798 | 0 | Predicate-mutatie binnen totaal |
| skos:exactMatch | 46 | 18 | −28 | 28× ctrl→compl exactMatch verwijderd |
| skos:broadMatch | 38 | 66 | +28 | 28× ctrl→compl broadMatch toegevoegd |
| skos:closeMatch / relatedMatch / narrowMatch | 1.489 / 225 / 0 | 1.489 / 225 / 0 | 0 | Ongewijzigd |
| owl:Class / NamedIndividual / sameAs | 199 / 1.383 / 98 | 199 / 1.383 / 98 | 0 | Ongewijzigd |
| D5 ctrl↔bio sameAs | 93 | 93 | 0 | Conform |
| D11 asset-brug | 5 | 5 | 0 | Conform |
| owl:Nothing post-inferentie | 0 | 0 | 0 | Consistent |
| m10-nis2-ext.ttl SHA256 | 78b8ee… | cb2d56… | wijziging | Enige module met hash-wijziging |

### §5.3 SHACL gesplitste validatie scenario C

- RUN 1 (inference='none'): conforms = True, violations = 0 — identiek aan baseline.
- RUN 2 (inference='owlrl'): conforms = False, violations = 290, identiek aan baseline (104 asset:NamespaceShape + 93 control:ISO27002NamingShape + 93 bio:ISO27002NamingShape — bekende SECTIE A false-positives onder owlrl-inferentie).

**SHACL-blinde vlek bevestigd:** geen shape valideert direct op 28 ctrl:→compl:-paren (Vraag D inventarisatie). Predicate-mutatie raakt geen shape. Null-effect zoals verwacht.

### §5.4 Patch-rapport-verwijzing

Detail-rapport voor v4.6.1-oplevering: `output/reports/patch-rapport-v4_6_1.md`. Geschreven alsof scenario C (alle 28) wordt toegepast, met expliciete noot dat scenario A (26) of B (27) eveneens mogelijk is op basis van masterchat-besluit.

---

## §6. Werkflow-leerpunten

Genoteerd voor T1-eindrapport §8 (Stap 5 / 6 — masterchat-twijfelgevallen-sign-off):

1. **Cluster-representant-aanpak voor c/d/f werkbaar.** Drie representant-paren leverden gestructureerde vier-criteria-output identiek aan pilot. Operationele kosten ~10 min per representant (gegeven dat pilot-werkwijze al routine is). Inhoudelijke meerwaarde: bevestigt cluster-overerving als verdedigbare aanpak (anders alle 18 volgers individueel uitwerken zou ~3-4 uur extra hebben gekost). Aanbeveling voor T2/T3: behoud cluster-representant-aanpak voor clusters >2 paren.

2. **Twee-zijdige analyse-format voor edge-cases voldoende voor masterchat-input.** Pro/contra-structuur dwingt Tech tot expliciete onderbouwing van beide kanten zonder voortijdig besluit. Twijfelgevallen-tabel met NEN-PK-vraag is concrete actie voor masterchat (Steven brengt PK-bron). Aandachtspunt: tabel-NEN-vraag moet expliciet de tekst-passage benoemen die nodig is, niet vragen "wat zegt ISO over X". Voor T2/T3: format herbruikbaar; eventueel een NEN-PK-vraag-template ontwikkelen.

3. **Twee TTL-diff-bestanden-aanpak operationeel duidelijk.** Diff-26 (zeker) + diff-2 (onder masterchat) is helder gescheiden. Steven kan diff-26 toepassen na masterchat-GO; diff-2 (geheel of deels) na NEN-toets-besluit. Risico: drie scenario's (A=26, B=27, C=28) introduceren administratieve last in toekomstige versie-tracking. Voor v4.6.1-oplevering: scenario C als baseline-meting, scenario A/B/C-keuze in patch-rapport-§0 expliciet.

4. **Scenario-A/B/C-meet-aanpak werkbaar.** Tech levert metrics alleen voor scenario C; A en B zijn afleidbaar door masterchat omdat predicate-mutatie additief is. Geen extra Tech-runs nodig. Eventueel voor toekomstige edge-cases: kan een matrix met (scenario × metric) toegevoegd worden aan patch-rapport, maar dat is masterchat-keuze.

5. **Twee Protocol 14-toepassingen achter elkaar — automatiserings-overweging.** Stap 3-rapport eerste productie-toepassing van pre-push disclosure-check. Stap 4-rapport + patch-rapport-v4.6.1 = tweede en derde toepassing in korte tijd. Gemiddelde tijd ~3-5 min per rapport. **Concrete automatiserings-overweging**: een `scripts/protocol14_lint.py` die grep op (a) organisatie-trefwoorden, (b) absolute-pad-patroon `/Users/`, (c) NEN-quote-detectie via lange double-quoted strings boven 50 woorden in rdfs:comment/requirementText-blokken. Niet nu uitvoeren (scope-uitbreiding); wel als H-overweging meenemen naar Brein-cyclus. Voor T1-eindrapport: noteren als toekomstig H-item-kandidaat.

6. **Tijdsraming Stap 4 ~75-90 min — klopte ongeveer.** Werkelijke tijd Tech (exclusief lees-context): cluster-representant-werk (3×) ~25 min; cluster-overerving (18 paren tabel-werk) ~20 min; edge-case-analyse (2× twee-zijdig) ~25 min; patch-bestanden + verificatie-scripts ~30 min; rapporten + Protocol 14-check ~25 min. Totaal ~2 uur incl. tooling-installatie (owlrl/pyshacl). Lichte overschrijding van bovenkant raming maar binnen orde van grootte. T2/T3-raming: 90-120 min als richtlijn voor analoge scope.

7. **owlrl/pyshacl tooling niet pre-installed in Tech-subagent-omgeving.** `pip3 install owlrl pyshacl rdflib` voltooid tijdens sprint (~30 s). Niet kritisch maar wel observatie. Aanbeveling: in `scripts/`-folder een `requirements.txt` of `make setup` toevoegen voor future-proofing van Tech-subagent-bootstrap. Geen actie nu, voor Brein-cyclus.

8. **ENISA-disclaimer als categorisch argument robuust gebleken.** In §1 (c/d/f) en §3 (h/j) wordt deze als consistent ankerpunt gebruikt. Voor T2/T3 (andere cross-norm-mappings) kan een algemene "categorische-disclaimer-clause" in protocol-update verwerkt worden — buiten T1-scope.

---

## §7. Pre-push disclosure-check (Protocol 14)

Tweede productie-toepassing van Protocol 14 (na Stap-3-pilot-rapport).

Scope van check: dit rapport (`t1-stap4-rapport-v4_6_0.md`), `patch-rapport-v4_6_1.md`, `diff-26-broadMatch.ttl`, `diff-2-edge-cases.ttl`.

**Bevindingen per check:**

- **Organisatie-naam**: niet aangetroffen. Alle verwijzingen zijn "de organisatie" / "Rijksoverheidsorganisatie" of generiek "entiteit"/"essentiële entiteit" (uit NIS2-tekst). Het project genoemde naam komt nergens voor.
- **Persoonsnamen**: alleen "Steven" (projecteigenaar) in werkflow-context — toegestaan binnen project-context conform bestaande brain-vault-bestanden. Geen andere personen.
- **Lokale paden buiten repo-relative**: niet aangetroffen. Alle paden `ontology/`, `output/`, `docs/`, `sources/` zijn repo-relative. Geen `/Users/...`-absolutering in rapport-content (de `/tmp/grc-v461/`-paden zijn alleen in interne uitvoeringslog van Tech, niet in deze rapport-publicatie).
- **NEN-tekst-quotes**: niet aangetroffen. Alleen ISO-clausule-ID-verwijzingen (A.5.24, A.8.05, A.8.24) en label-vertaling uit het project zelf. Geen ISO-control-tekst geciteerd. NIS2-tekst-citaten zijn EU-richtlijn (publiek-domein).

**Ervaring tweede toepassing:** check duurde ~4 min over vier bestanden samen, ten opzichte van ~3 min voor Stap-3-pilot-rapport. Schaal lijkt lineair met aantal bestanden. Bevestiging van werkflow-leerpunt §6.5: automatiseringsoverweging gerechtvaardigd na 3+ productie-toepassingen, niet eerder.

**Geen vondsten — beide rapporten + diff-bestanden veilig voor publicatie.**

---

## §8. Bijlagen

### §8.1 Lijst van alle 28 paren met Stap-4-uitkomst

| # | Paar-ID | Subject | Object | Cluster | Uitkomst | Confidence | Patch-toewijzing |
|---|---|---|---|---|---|---|---|
| 1 | T1-001 | ctrl:ISO27002_5_01 | compl:NIS2_Art21_a | a (1↔1) | broadMatch | hoog | diff-26 |
| 2 | T1-002 | ctrl:ISO27002_5_09 | compl:NIS2_Art21_i | i (6↔1) | broadMatch | hoog | diff-26 |
| 3 | T1-003 | ctrl:ISO27002_5_15 | compl:NIS2_Art21_i | i (6↔1) | broadMatch | hoog (overerving) | diff-26 |
| 4 | T1-004 | ctrl:ISO27002_5_16 | compl:NIS2_Art21_i | i (6↔1) | broadMatch | hoog (overerving) | diff-26 |
| 5 | T1-005 | ctrl:ISO27002_5_18 | compl:NIS2_Art21_i | i (6↔1) | broadMatch | hoog (overerving) | diff-26 |
| 6 | T1-006 | ctrl:ISO27002_5_19 | compl:NIS2_Art21_d | d (4↔1) | broadMatch | hoog | diff-26 |
| 7 | T1-007 | ctrl:ISO27002_5_20 | compl:NIS2_Art21_d | d (4↔1) | broadMatch | hoog (overerving) | diff-26 |
| 8 | T1-008 | ctrl:ISO27002_5_21 | compl:NIS2_Art21_d | d (4↔1) | broadMatch | hoog (overerving) | diff-26 |
| 9 | T1-009 | ctrl:ISO27002_5_22 | compl:NIS2_Art21_d | d (4↔1) | broadMatch | hoog (overerving) | diff-26 |
| 10 | T1-010 | ctrl:ISO27002_5_24 | compl:NIS2_Art21_b | b (4↔1) | broadMatch | hoog | diff-26 |
| 11 | T1-011 | ctrl:ISO27002_5_25 | compl:NIS2_Art21_b | b (4↔1) | broadMatch | hoog (overerving) | diff-26 |
| 12 | T1-012 | ctrl:ISO27002_5_26 | compl:NIS2_Art21_b | b (4↔1) | broadMatch | hoog (overerving) | diff-26 |
| 13 | T1-013 | ctrl:ISO27002_5_27 | compl:NIS2_Art21_b | b (4↔1) | broadMatch | hoog (overerving) | diff-26 |
| 14 | T1-014 | ctrl:ISO27002_5_29 | compl:NIS2_Art21_c | c (3↔1) | broadMatch | hoog | diff-26 |
| 15 | T1-015 | ctrl:ISO27002_5_30 | compl:NIS2_Art21_c | c (3↔1) | broadMatch | hoog (overerving) | diff-26 |
| 16 | T1-016 | ctrl:ISO27002_5_35 | compl:NIS2_Art21_f | f (2↔1) | broadMatch | hoog | diff-26 |
| 17 | T1-017 | ctrl:ISO27002_5_36 | compl:NIS2_Art21_f | f (2↔1) | broadMatch | hoog (overerving) | diff-26 |
| 18 | T1-018 | ctrl:ISO27002_6_01 | compl:NIS2_Art21_i | i (6↔1) | broadMatch | hoog (overerving) | diff-26 |
| 19 | T1-019 | ctrl:ISO27002_6_02 | compl:NIS2_Art21_i | i (6↔1) | broadMatch | hoog (overerving) | diff-26 |
| 20 | T1-020 | ctrl:ISO27002_6_03 | compl:NIS2_Art21_g | g (1↔1) | broadMatch | hoog | diff-26 |
| 21 | T1-021 | ctrl:ISO27002_8_05 | compl:NIS2_Art21_j | j (1↔1) | **edge-case** | **n.v.t. — twee-zijdig** | **diff-2 (onder masterchat)** |
| 22 | T1-022 | ctrl:ISO27002_8_13 | compl:NIS2_Art21_c | c (3↔1) | broadMatch | hoog (overerving) | diff-26 |
| 23 | T1-023 | ctrl:ISO27002_8_24 | compl:NIS2_Art21_h | h (1↔1) | **edge-case** | **n.v.t. — twee-zijdig** | **diff-2 (onder masterchat)** |
| 24 | T1-024 | ctrl:ISO27002_8_25 | compl:NIS2_Art21_e | e (5↔1) | broadMatch | hoog | diff-26 |
| 25 | T1-025 | ctrl:ISO27002_8_26 | compl:NIS2_Art21_e | e (5↔1) | broadMatch | hoog (overerving) | diff-26 |
| 26 | T1-026 | ctrl:ISO27002_8_27 | compl:NIS2_Art21_e | e (5↔1) | broadMatch | hoog (overerving) | diff-26 |
| 27 | T1-027 | ctrl:ISO27002_8_28 | compl:NIS2_Art21_e | e (5↔1) | broadMatch | hoog (overerving) | diff-26 |
| 28 | T1-028 | ctrl:ISO27002_8_29 | compl:NIS2_Art21_e | e (5↔1) | broadMatch | hoog (overerving) | diff-26 |

**Totaal:** 26 broadMatch (diff-26) + 2 edge-cases (diff-2, masterchat-NEN-toets).

— Einde Stap-4-rapport.
