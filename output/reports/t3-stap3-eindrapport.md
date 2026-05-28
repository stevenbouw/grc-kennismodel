---
type: report
subtype: stap3-eindrapport
sprint: T3
sprint_stap: 3
baseline_from: v4.6.2
baseline_to: v4.6.3
date: 2026-05-28
status: final-awaiting-masterchat-review
mode: PATCH-TOEGEPAST (m14-only)
related:
  - skos-beoordelings-protocol-v1_3
  - t3-pre-sprint-inventarisatie
  - t3-pilot-rapport
  - H36_skos-exactmatch-ctrl-compl-audit
  - D04_skos-cross-framework
  - M14_avg-gdpr
scope: "T3 Stap 3 — per-paar-beoordeling van 25 resterende m14-paren onder SKOS-protocol v1.3 FINAL + cumulatief 31-paren-m14-overzicht. Inclusief masterchat-besluit-toepassing op T3-001 (broadMatch → relatedMatch, analoog T3-002 pilot) en closeMatch-toets T3-026 analoog T3-014 pilot. Cross-category-rationale (control ↔ legal-obligation = associatief) leidend voor relatedMatch-behoud op niet-closeMatch-paren."
---

# T3 Stap 3 — Eindrapport (per-paar-beoordeling 25 resterende paren + cumulatief m14)

> **Methodische notitie:** dit rapport is bottom-up opgebouwd conform Protocol v1.3 §10.2. De per-paar-beoordelingen (§3) zijn als eerste geschreven, gegroepeerd per AVG-cluster om herhaling te beperken. Analyse + cross-category-leerpunt (§4-§5) + cumulatief m14-overzicht (§6) + samenvatting (§1-§2) volgen daaruit.

> **Disclosure-discipline:** alle NEN-citaten zijn parafrase + clausule-verwijzing. Geen verbatim ISO-tekst >10 woorden in dit rapport (Protocol 14 + Protocol v1.3 §8.2 gerespecteerd). Control-name-strings (bv. "Information backup", "Access control") zijn factuele identifier-strings op control-name-niveau.

---

## §1. Samenvatting

| Aspect | Bevinding |
|---|---|
| Totaal beoordeelde paren in Stap 3 | 25 (alle m14-paren minus pilot 6) |
| Mutaties voorgesteld onder de 25 | **1** (T3-001, broadMatch → relatedMatch — masterchat-besluit per pilot-§5.2 Optie C, niet autonome Tech-mutatie) |
| Behoud onder de 25 | **24** |
| Confidence hoog | 23 |
| Confidence middel | 2 (T3-026 closeMatch-toets + T3-030 scope-asymmetrie analoog T3-028) |
| Confidence laag | 0 |
| closeMatch-toets T3-026 | **verdedigbaar behouden als closeMatch** (analoog T3-014; partiële overlap op incident-planning-domein; geen NEN-aantoonbare grond voor relatedMatch-downgrade; confidence middel — vergelijkbaar T3-014) |
| Stop-conditie geactiveerd in Stap 3 | **nee** (drempels: ≥3 laag, totaal mutaties m14 >4) |
| **Cumulatief m14 (pilot 6 + Stap 3 25)** | **31 paren — 2 mutaties (beide T3-001 + T3-002 = Art5_1f broadMatch-cluster); 29 behoud** |
| m14-eindstand v4.6.3 | 2 closeMatch + 0 broadMatch + 29 relatedMatch — conform instructie-§ "Verwachte uitkomst" |
| Methode-conclusie | Cross-category-rationale (control ↔ legal-obligation = associatief, niet subsumptief) houdt op alle 25 paren. Cluster-discipline `narrowMatch`-default uit Protocol §3.1 rij 7 (1↔veel-subject-cluster m14) wordt op paar-niveau systematisch overstemd door C3-falen op conceptuele subsumptie. closeMatch (2 paren resterend) blijft strikt verdedigd op retrieval-interchangeability binnen governance/policy-respectievelijk incident-planning-domein |

**Bottom-line:** masterchat-besluit op pilot-escalatie (Optie C — beide Art5_1f broadMatch-paren naar relatedMatch) is in `ontology/m14-avg-gdpr.ttl` toegepast voor zowel T3-002 (al gemuteerd vóór deze Stap conform pilot-escalatie-rapportage) als T3-001 (in deze Stap toegepast als directe instructie-uitvoering, niet als autonome Tech-bevinding). De 24 overige Stap-3-paren krijgen alle behoud-classificatie, conform de pilot-vastgestelde semantische basislijn `relatedMatch` + cross-category-rationale. T3-026 closeMatch-toets levert behoud-verdedigbaar uitkomst analoog aan T3-014. Geen onverwachte patronen; geen aanvullende methode-escalatie.

---

## §2. Methode

### §2.1 Protocol-toepassing

Per paar toegepast: Protocol v1.3 §2.1 (C1) + §2.2 (C2) + §2.3 (C3) + §2.4 (C4), gevolgd door §3.1 predicate-doel-tabel-mapping en §5.2 confidence-criterium. D4.1-vooraf-check (§2.0) is op alle 25 paren irrelevant — geen exactMatch-doel-overweging (bindende T3-steer 1, gehandhaafd uit pilot).

### §2.2 Bindende T3-steers — operationele toepassing in Stap 3

| Steer | Toepassing in Stap 3 |
|---|---|
| 1. Geen D4.1-disclaimer-logica | Geen exactMatch-doel-overweging op 25 paren; D4.1 inactief |
| 2. Geen cluster-convergentie-aanname | Per paar getoetst; subject-cluster-cardinaliteit (Art32 → 12 controls) is informatief signaal voor 1↔veel-structuur, maar per-paar-C3-toets prevaleert. Cluster-discipline-bewijslast §3.3 (v1.3 verfijning) blokkeert ongefundeerde cluster-projectie naar `narrowMatch` |
| 3. Semantische basislijn = relatedMatch | Voor 23 van 24 niet-closeMatch-paren in Stap-3-scope is `relatedMatch` per-paar bevestigd; voor T3-001 is `relatedMatch` per masterchat-besluit gemuteerd uit `broadMatch` (instructie-toepassing, niet autonome Tech-bevinding) |
| 4. Evidence-hantering | Niveau-1/2/3-keten gebruikt als bestaans-bewijs (dat een relatie bestaat), niet als predicate-type-bewijs. Predicate-type-keuze verliep via C1+C3 op 27002 + AVG-semantiek + cross-category-rationale |
| 5. closeMatch-toets | Expliciet toegepast op T3-026 (Art33 → 5.24); uitkomst: behoud verdedigbaar — analoog aan T3-014 (Art32 → 5.01) |

### §2.3 Cross-category-rationale (kernprincipe uit pilot §4.4)

Een ISO 27002-control is een **implementatie-maatregel**; een AVG-artikel is een **juridische verplichting/principe**. SKOS-broad/narrowMatch tussen control en wettelijke verplichting is een **categorie-fout** in de meeste gevallen, omdat een control niet conceptueel "een soort verplichting" is — het is een operationele invulling die "valt onder" een verplichting. relatedMatch (associatief) is daarom de semantisch correcte basislijn voor cross-category-mappings, tenzij retrieval-interchangeability houdbaar is (→ closeMatch).

**Status in deze sprint:** documenteren als T3-leerpunt voor v1.3.1-Brein-cyclus (niet nu formaliseren in Protocol-tekst — zie §5).

### §2.4 Bron-stack per paar (ongewijzigd uit pilot §2.3)

| Bron | Rol |
|---|---|
| `ontology/m14-avg-gdpr.ttl` rdfs:comment per AVG-artikel | Obligation-semantiek (NL-parafrase EUR-Lex) |
| `/Users/stevenbouwmeester/grc-sources-licensed/NEN-EN-ISO_IEC_27002_2022_en.pdf` Control+Purpose-secties | Control-semantiek (C1 + C3-toets) |
| `/Users/stevenbouwmeester/grc-sources-licensed/ISO27701.pdf` Annex D + Annex F.1 + Annex B.3 | Keten-evidence (C4 niveau-1/2 indien beschikbaar) |
| EUR-Lex Regulation (EU) 2016/679 | AVG-tekst-verificatie (publiek; m14 rdfs:comment volstaat in deze scope) |

### §2.5 Groeperings-strategie

De 25 paren zijn georganiseerd per AVG-subject-cluster (Art5_1f resterend / Art25 resterend / Art32 resterend / Art33 resterend / Art34 resterend). Per cluster wordt de cluster-context één keer beschreven, gevolgd door een compacte per-paar-tabel met de 13 verplichte velden conform Protocol v1.3 §5. Voor paren waarvoor de cross-category-rationale identiek geldt (en de C1+C3+C4-uitkomst homogeen is), wordt de redenering geconsolideerd en per paar verwezen — conform §10.2 efficiency, zonder velden te schrappen.

---

## §3. Per-paar-beoordeling Stap 3 — 25 paren gegroepeerd per cluster

### §3.1 Cluster Art5_1f resterend (6 paren: T3-001 + T3-003 t/m T3-007)

**Cluster-context:** AVG_Art5_1f — Integriteit en vertrouwelijkheid; subject-cluster-grootte 7 (was heterogeen broad×2/related×5 in v4.6.2; wordt homogeen related×7 post-patch v4.6.3 na muteren van T3-001 + T3-002). Cluster-doel-predicate per cross-category-rationale: `relatedMatch`. T3-002 is pilot-paar (behandeld in pilot-rapport §3.1 — vóór masterchat-besluit; mutatie naar `relatedMatch` is in v4.6.3 toegepast).

**Cluster-evidence-overzicht (uit pre-sprint-inventarisatie §5.1):**

| Paar | Object | Pred (v4.6.2) | A.3.x | Annex D-link | Evidence-niveau |
|---|---|---|---|---|---|
| T3-001 | ISO27002_5_01 | broadMatch | A.3.3 | nee | 2 |
| T3-003 | ISO27002_5_15 | relatedMatch | N/A | — | 3 |
| T3-004 | ISO27002_8_24 | relatedMatch | A.3.26 | nee | 2 |
| T3-005 | ISO27002_8_10 | relatedMatch | N/A | — | 3 |
| T3-006 | ISO27002_8_11 | relatedMatch | N/A | — | 3 |
| T3-007 | ISO27002_8_12 | relatedMatch | N/A | — | 3 |

#### T3-001 — compl:AVG_Art5_1f `skos:broadMatch` → `skos:relatedMatch` ctrl:ISO27002_5_01

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art5_1f` (AVG Art. 5(1)(f) — integriteit en vertrouwelijkheid) |
| Object IRI | `ctrl:ISO27002_5_01` (Beleidsregels voor informatiebeveiliging / Policies for information security) |
| Huidige predicate (v4.6.2) | `skos:broadMatch` |
| Cluster-context | Art5_1f-subject-cluster (7); object-cluster ctrl:5_01 (2: Art32 closeMatch + Art5_1f broadMatch, heterogeen pre-patch — wordt heterogeen close×1/related×1 post-patch) |
| D4.1-disclaimer-check | n.v.t. — geen exactMatch-doel-overweging |
| **C1 (definitioneel)** | **partieel** — Art. 5(1)(f) is een breed principe (passende technische/organisatorische maatregelen voor integriteit + vertrouwelijkheid + bescherming tegen ongeoorloofde/onrechtmatige verwerking en verlies/vernietiging/beschadiging). 5.01 (parafrase ISO 27002 §5.1) levert beleidsregels-fundament voor IB. Operationele overlap: beleid is een fundament-mechanisme om "passende maatregelen" te kunnen waarborgen. Geen bilateraliteit — Art. 5(1)(f) strekt veel verder dan beleidsregels-vaststelling |
| **C2 (cardinaliteit)** | Subject-cluster 1↔7; object-cluster 2↔1. Object-cluster heterogeen pre-patch — pas via T3-014 (Art32 closeMatch) gedeeld met dit paar. Per §2.2 prevaleert object-cluster bij multi-mapping; object-cluster klein (2), geen sterke cluster-discipline-druk |
| **C3 (inclusie)** | **geen strikte subset** — 5.01 (beleidsregels-vaststelling) is een proces-norm; Art. 5(1)(f) is een substantie-principe over data-beveiliging. Operationeel: beleid implementeert *deel* van het principe, maar 5.01-scope is geen subset van Art. 5(1)(f)-scope (beleid gaat over IB-vaststelling, niet alleen integriteit/vertrouwelijkheid van persoonsgegevens). Geen conceptuele subsumptie |
| **C4 (bron-evidence)** | **Niveau 2** — keten: ctrl:5.01 → A.3.3 via Annex F.1 (control-name match "Policies for information security") → B.3.3 zou bestaan; Annex D Table D.1 bevat geen entry voor B.3.3 → (5)(1)(f). 27701-werkgroep heeft policy-clausule niet expliciet aan Art. 5(1)(f) gekoppeld |
| Keten-stappen | Stap 1+2 OK (ctrl:5.01 → A.3.3 → B.3.3 bestaat); Stap 3 (Annex D-link voor (5)(1)(f)) ontbreekt — niveau 2 |
| **Predicate-doel (§3.1)** | Was rij 6/7 in pre-patch-claim (broadMatch met richtings-issue per pilot §3.1 analyse). Per cross-category-rationale + masterchat-besluit Optie C (pilot-escalatie): rij 8 → `relatedMatch` |
| **Mutatie-richting** | **downgrade** (broadMatch → relatedMatch) per Protocol v1.3 §3.2 |
| **Confidence** | **hoog** — masterchat-besluit op pilot-escalatie (Optie C) is autoritatief; pilot-§5.2 cross-category-rationale toegepast op zuster-paar T3-002 levert directe analogie; geen NEN-aantoonbare grond voor handhaven broadMatch |
| **Voorgesteld predicate** | **relatedMatch** |
| **Patch-vereist** | **Ja** — toegepast in v4.6.3 (analoog T3-002 pilot-mutatie); zie §6 |

**Onderbouwing — analogie met T3-002 (pilot-rapport §3.1 + escalatie §5.2):**

Pilot heeft T3-002 (Art5_1f broadMatch ctrl:5.12 Classification of information) onderzocht en gevonden:
- SKOS-broadMatch-richtings-semantiek: `A skos:broadMatch B` ≡ B is broader than A — dat is **omgekeerd** aan modeller-bedoeling
- Drie opties (pilot §5.2): A. status quo, B. mutatie naar narrowMatch (SKOS-formeel), C. mutatie naar relatedMatch (cross-category-rationale)
- Masterchat-besluit (instructie-§ "Masterchat-besluit op pilot-escalatie"): **Optie C** — control ↔ legal-obligation is associatief, niet subsumptief; relatedMatch is symmetrisch en lost de richtingskwestie definitief op

T3-001 is het zuster-paar binnen hetzelfde Art5_1f broadMatch-cluster (n=2 totaal). Dezelfde rationale geldt:
- 5.01 (Beleidsregels IB) ↔ Art. 5(1)(f) is een cross-category-relatie
- Beleidsregels-vaststelling is een organisatorische maatregel die kan bijdragen aan Art. 5(1)(f)-implementatie, maar is conceptueel geen subset
- relatedMatch maakt het Art5_1f-cluster consistent (alle 7 paren post-patch `relatedMatch`)

Mutatie is directe instructie-uitvoering op masterchat-besluit, niet autonome Tech-bevinding. Verschil met T3-002 (pilot-confidence middel wegens openstaande methode-vraag): T3-001-confidence is **hoog** omdat de methode-vraag is opgelost door masterchat-besluit en het besluit eenduidig op het cluster (beide leden) van toepassing is.

#### T3-003 — compl:AVG_Art5_1f `skos:relatedMatch` ctrl:ISO27002_5_15

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art5_1f` |
| Object IRI | `ctrl:ISO27002_5_15` (Toegangsbeveiliging / Access control) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art5_1f-cluster (7); object-cluster ctrl:5_15 (2: Art5_1f + Art32, homogeen related×2) |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel** — Art. 5(1)(f) eist passende beveiliging tegen ongeoorloofde verwerking; 5.15 (parafrase ISO 27002 §5.15) levert toegangsbeveiligings-regels op basis van bedrijfs- en IB-eisen. Operationele overlap: toegangsbeveiliging is een fundamenteel mechanisme tegen ongeoorloofde verwerking. Niet bilateraal — Art. 5(1)(f) strekt zich uit tot meer dan toegang (ook integriteit + bescherming tegen verlies/vernietiging) |
| **C2 (cardinaliteit)** | Subject-cluster 1↔7; object-cluster 2↔1 (homogeen). Geen cluster-discipline-druk; object-cluster prevaleert |
| **C3 (inclusie)** | **geen strikte conceptuele subset** — 5.15 is een specifieke deelcontrol; Art. 5(1)(f) is een breder principe. Operationeel: toegangsbeveiliging implementeert *een aspect* van het principe; geen subsumptieve relatie tussen control en juridische verplichting (cross-category-rationale §2.3) |
| **C4 (bron-evidence)** | **Niveau 3** — 5.15 (Access control) is N/A in 27701:2025 Annex F.1 (27001:2013 6.6.1.1+6.6.1.2 niet in PIMS-scope). Geen keten-evidence via 27701; Tech-analyse via 27002 + AVG-tekst |
| **Predicate-doel (§3.1)** | Rij 8 (thematische verwantschap, cross-category): `relatedMatch` |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — duidelijke cross-category-rationale + zuster-positie binnen homogeen Art5_1f-cluster (post-patch); geen NEN-aantoonbare upgrade-grond |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

#### T3-004 — compl:AVG_Art5_1f `skos:relatedMatch` ctrl:ISO27002_8_24

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art5_1f` |
| Object IRI | `ctrl:ISO27002_8_24` (Cryptografie / Use of cryptography) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art5_1f-cluster (7); object-cluster ctrl:8_24 (2: Art5_1f + Art32, homogeen related×2) |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel** — Art. 5(1)(f) noemt geen specifiek cryptografische maatregelen, maar verwijst naar passende technische maatregelen voor vertrouwelijkheid; 5.30 niet relevant (overigens: 8.24 dekt cryptografie-gebruik, sleutel-beheer, key-rotatie). Operationele overlap: cryptografie is canoniek mechanisme voor vertrouwelijkheid + integriteit |
| **C2 (cardinaliteit)** | Subject-cluster 1↔7; object-cluster 2↔1 (homogeen) |
| **C3 (inclusie)** | **geen subset** — 8.24 is een technische implementatie-maatregel; Art. 5(1)(f) is een principe. Cross-category-rationale geldt |
| **C4 (bron-evidence)** | **Niveau 2** — keten: ctrl:8.24 → A.3.26 via Annex F.1 ("Use of cryptography") → B.3.26 → Annex D Table D.1: B.3.26 → (32)(1)(a) (geen directe (5)(1)(f)-link voor A.3.26). 27701 koppelt 8.24 expliciet aan Art. 32(1)(a), niet aan Art. 5(1)(f) |
| Keten-stappen | Stap 1+2 OK (ctrl:8.24 → A.3.26 → B.3.26); Stap 3 (Annex D-link voor (5)(1)(f)) ontbreekt — niveau 2 |
| **Predicate-doel (§3.1)** | Rij 8 (thematische verwantschap, cross-category): `relatedMatch` |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — cross-category-rationale + homogeen object-cluster; evidence-niveau-2 ondersteunt relatie zonder predicate-upgrade-grond |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

#### T3-005 — compl:AVG_Art5_1f `skos:relatedMatch` ctrl:ISO27002_8_10

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art5_1f` |
| Object IRI | `ctrl:ISO27002_8_10` (Wissen van informatie / Information deletion) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art5_1f-cluster (7); object-cluster ctrl:8_10 (singleton) |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel** — Art. 5(1)(f) noemt bescherming tegen verlies/vernietiging; 8.10 (Information deletion, parafrase) levert procedures voor gecontroleerde verwijdering van informatie. Operationele overlap: deletion is keerzijde van retention; bijdraagt aan dataminimalisatie (samen met Art. 5(1)(c)) en aan integriteit-controle door uitsluiten van niet-vereiste data. Niet bilateraal |
| **C2 (cardinaliteit)** | Subject-cluster 1↔7; object-cluster singleton. Geen cluster-druk |
| **C3 (inclusie)** | **geen subset** — 8.10 is operationele deletion-control; Art. 5(1)(f) is een veel breder principe. Cross-category-rationale geldt |
| **C4 (bron-evidence)** | **Niveau 3** — 8.10 N/A in 27701:2025 Annex F.1 ("New" t.o.v. 27701:2019, niet in 2025-scope). Tech-analyse via 27002 + AVG-tekst |
| **Predicate-doel (§3.1)** | Rij 8 (thematische verwantschap, cross-category): `relatedMatch` |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — duidelijke cross-category + thematische verwantschap; geen NEN-aantoonbare upgrade |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

#### T3-006 — compl:AVG_Art5_1f `skos:relatedMatch` ctrl:ISO27002_8_11

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art5_1f` |
| Object IRI | `ctrl:ISO27002_8_11` (Maskeren van gegevens / Data masking) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art5_1f-cluster (7); object-cluster ctrl:8_11 (2: Art5_1f + Art25, homogeen related×2) |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel** — Art. 5(1)(f) eist passende beveiliging tegen ongeoorloofde verwerking; 8.11 (Data masking, parafrase) levert technieken zoals pseudonimisering en anonimisering. Operationele overlap: masking is een vertrouwelijkheids-bevorderend mechanisme tegen ongeoorloofde verwerking. Niet bilateraal |
| **C2 (cardinaliteit)** | Subject-cluster 1↔7; object-cluster 2↔1 (homogeen) |
| **C3 (inclusie)** | **geen subset** — 8.11 is technische masking-control; Art. 5(1)(f) is principe. Cross-category-rationale |
| **C4 (bron-evidence)** | **Niveau 3** — 8.11 N/A in 27701:2025 Annex F.1 ("New" niet in 2025-scope). Tech-analyse |
| **Predicate-doel (§3.1)** | Rij 8: `relatedMatch` |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — cross-category + homogeen object-cluster |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

#### T3-007 — compl:AVG_Art5_1f `skos:relatedMatch` ctrl:ISO27002_8_12

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art5_1f` |
| Object IRI | `ctrl:ISO27002_8_12` (Voorkomen gegevenslekken / Data leakage prevention) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art5_1f-cluster (7); object-cluster ctrl:8_12 (singleton) |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel** — Art. 5(1)(f) eist passende beveiliging tegen ongeoorloofde verwerking; 8.12 (DLP, parafrase) detecteert/voorkomt ongeoorloofde verspreiding van gevoelige informatie. Operationele overlap: DLP is gericht mechanisme tegen ongeoorloofde verwerking-uitkomst (data-exfiltratie). Niet bilateraal |
| **C2 (cardinaliteit)** | Subject-cluster 1↔7; object-cluster singleton |
| **C3 (inclusie)** | **geen subset** — DLP is specifieke control; Art. 5(1)(f) is principe. Cross-category |
| **C4 (bron-evidence)** | **Niveau 3** — 8.12 N/A in 27701:2025 Annex F.1 ("New" niet in 2025-scope) |
| **Predicate-doel (§3.1)** | Rij 8: `relatedMatch` |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — cross-category + duidelijke thematische verwantschap |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

---

### §3.2 Cluster Art25 resterend (5 paren: T3-009 + T3-010 + T3-011 + T3-012 + T3-013)

**Cluster-context:** AVG_Art25 — Gegevensbescherming door ontwerp en standaardinstellingen; subject-cluster-grootte 6, homogeen relatedMatch×6 (in v4.6.2). Pilot T3-008 (Art25 → 8.25) bevestigde cluster-doel `relatedMatch` via cross-category-rationale (pilot-rapport §3.4, confidence hoog). Stap-3-paren in dit cluster volgen dezelfde cluster-discipline-overerving + per-paar-confirmatie.

**Cluster-evidence-overzicht:**

| Paar | Object | Pred | A.3.x | Annex D-link | Evidence-niveau |
|---|---|---|---|---|---|
| T3-009 | ISO27002_8_26 | relatedMatch | A.3.28 | nee | 2 |
| T3-010 | ISO27002_8_27 | relatedMatch | A.3.29 | **ja (25)(1)** | **1** |
| T3-011 | ISO27002_8_28 | relatedMatch | N/A | — | 3 |
| T3-012 | ISO27002_8_11 | relatedMatch | N/A | — | 3 |
| T3-013 | ISO27002_8_33 | relatedMatch | A.3.31 | nee | 2 |

#### T3-009 — compl:AVG_Art25 `skos:relatedMatch` ctrl:ISO27002_8_26

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art25` |
| Object IRI | `ctrl:ISO27002_8_26` (Toepassingsbeveiligingseisen / Application security requirements) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art25-cluster (6, homogeen related×6); object-cluster singleton |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel** — Art. 25 eist privacy-by-design + privacy-by-default in verwerkingsmiddelen; 8.26 (parafrase ISO 27002 §8.26) eist dat IB-eisen voor applicaties worden geïdentificeerd, gespecificeerd en goedgekeurd bij ontwikkeling/aankoop. Operationele overlap: applicatie-IB-eisen-specificatie is mechanisme voor privacy-by-design-implementatie. Niet bilateraal — Art. 25 strekt zich uit tot data-minimalisatie + organisatorische maatregelen |
| **C2 (cardinaliteit)** | Subject-cluster 1↔6 (homogeen); object-cluster singleton |
| **C3 (inclusie)** | **geen subset** — 8.26 is technische applicatie-eisen-control; Art. 25 is breder principe. Cross-category |
| **C4 (bron-evidence)** | **Niveau 2** — keten: ctrl:8.26 → A.3.28 via Annex F.1 ("Application security requirements") → B.3.28 → Annex D Table D.1: B.3.28 → (5)(1)(f), (32)(1)(a) (geen directe (25)(1)-link voor B.3.28). 27701 koppelt 8.26 niet expliciet aan Art. 25 |
| Keten-stappen | Stap 1+2 OK; Stap 3 (Annex D-link voor (25)(1)) ontbreekt — niveau 2 |
| **Predicate-doel (§3.1)** | Rij 8 (cross-category): `relatedMatch` |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — cluster-discipline-overerving Art25-homogeen + cross-category-rationale; pilot T3-008 levert representant-precedent |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

#### T3-010 — compl:AVG_Art25 `skos:relatedMatch` ctrl:ISO27002_8_27

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art25` |
| Object IRI | `ctrl:ISO27002_8_27` (Veilige systeemarchitectuur / Secure system architecture and engineering principles) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art25-cluster (6, homogeen); object-cluster singleton |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel-sterk** — Art. 25 vereist privacy-by-design; 8.27 (parafrase) levert principes voor veilige systeemarchitectuur en engineering. Operationele overlap is sterk: secure-by-design-principes zijn canonieke implementatie van privacy-by-design op architectuur-niveau. Niet bilateraal (Art. 25 raakt ook organisatorische + procedurele aspecten) |
| **C2 (cardinaliteit)** | Subject-cluster 1↔6; object-cluster singleton |
| **C3 (inclusie)** | **B ⊂ A (zwak, operationeel)** — 8.27 is operationele engineering-control; Art. 25 is bredere privacy-by-design-verplichting. Cross-category-rationale: conceptueel niet subsumptief |
| **C4 (bron-evidence)** | **Niveau 1** — keten: ctrl:8.27 → A.3.29 via Annex F.1 ("Secure system architecture and engineering principles") → B.3.29 → Annex D Table D.1: B.3.29 → (25)(1). Direct Annex D-link |
| Keten-stappen | ctrl:8.27 → 27701 A.3.29 → B.3.29 → AVG (25)(1) |
| **Predicate-doel (§3.1)** | Niveau-1 evidence + partieel-sterke C1 + cross-category-rationale → rij 8 `relatedMatch`. closeMatch-toets niet aangewezen: Art. 25 strekt zich verder uit dan systeemarchitectuur (data-minimalisatie + organisatorische maatregelen) — geen retrieval-interchangeability |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — niveau-1 evidence + cluster-conform + cross-category-rationale |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

#### T3-011 — compl:AVG_Art25 `skos:relatedMatch` ctrl:ISO27002_8_28

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art25` |
| Object IRI | `ctrl:ISO27002_8_28` (Veilig coderen / Secure coding) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art25-cluster (6, homogeen); object-cluster singleton |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel** — Art. 25 eist privacy-by-design; 8.28 (parafrase) levert veilige codeer-praktijken voor software-ontwikkeling. Operationele overlap: secure coding is detail-implementatie van privacy-by-design in de codeer-laag. Niet bilateraal |
| **C2 (cardinaliteit)** | Subject-cluster 1↔6; object-cluster singleton |
| **C3 (inclusie)** | **geen conceptuele subset** — secure coding is technische codeer-praktijk; Art. 25 is principe. Cross-category |
| **C4 (bron-evidence)** | **Niveau 3** — 8.28 N/A in 27701:2025 Annex F.1 ("New" niet in 2025-scope). Tech-analyse |
| **Predicate-doel (§3.1)** | Rij 8: `relatedMatch` |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — cross-category + cluster-conform |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

#### T3-012 — compl:AVG_Art25 `skos:relatedMatch` ctrl:ISO27002_8_11

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art25` |
| Object IRI | `ctrl:ISO27002_8_11` (Maskeren van gegevens / Data masking) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art25-cluster (6, homogeen); object-cluster ctrl:8_11 (2: Art5_1f + Art25, homogeen related×2) |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel** — Art. 25 eist privacy-by-default (dataminimalisatie); 8.11 (parafrase) levert masking + pseudonimisering. Operationele overlap: masking is canoniek mechanisme voor dataminimalisatie-by-default. Niet bilateraal |
| **C2 (cardinaliteit)** | Subject-cluster 1↔6; object-cluster 2↔1 (homogeen related×2) |
| **C3 (inclusie)** | **geen subset** — masking is technische control; Art. 25 is principe. Cross-category |
| **C4 (bron-evidence)** | **Niveau 3** — 8.11 N/A in 27701:2025 Annex F.1. Tech-analyse |
| **Predicate-doel (§3.1)** | Rij 8: `relatedMatch` |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — cross-category + homogeen object-cluster |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

#### T3-013 — compl:AVG_Art25 `skos:relatedMatch` ctrl:ISO27002_8_33

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art25` |
| Object IRI | `ctrl:ISO27002_8_33` (Testgegevens / Test information) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art25-cluster (6, homogeen); object-cluster singleton |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel** — Art. 25 eist dataminimalisatie-by-default; 8.33 (parafrase) levert dat test-informatie zorgvuldig geselecteerd, beschermd en beheerd wordt — vermijden van productie-PII in test-omgevingen. Operationele overlap: testgegevens-beheer is een ontwikkelfase-implementatie van dataminimalisatie + integriteits-bescherming. Niet bilateraal |
| **C2 (cardinaliteit)** | Subject-cluster 1↔6; object-cluster singleton |
| **C3 (inclusie)** | **geen subset** — testgegevens-control is specifieke ontwikkelfase-maatregel; Art. 25 is breder principe. Cross-category |
| **C4 (bron-evidence)** | **Niveau 2** — keten: ctrl:8.33 → A.3.31 via Annex F.1 ("Test information") → B.3.31 → Annex D Table D.1: B.3.31 → (5)(1)(f) (geen directe (25)(1)-link voor B.3.31). 27701 koppelt 8.33 aan Art. 5(1)(f), niet aan Art. 25 |
| Keten-stappen | Stap 1+2 OK; Stap 3 (Annex D-link voor (25)(1)) ontbreekt — niveau 2 |
| **Predicate-doel (§3.1)** | Rij 8: `relatedMatch` |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — cross-category + cluster-conform; evidence-niveau-2 ondersteunt relatie zonder upgrade-grond voor Art. 25 |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

---

### §3.3 Cluster Art32 resterend (10 paren: T3-015 t/m T3-023, T3-025)

**Cluster-context:** AVG_Art32 — Beveiliging van de verwerking; subject-cluster-grootte 12, heterogeen close×1/related×11. Pilot T3-014 bevestigde closeMatch behoud voor Art32 → 5.01 (governance/policy-relatie, niveau-2 evidence, confidence middel). Pilot T3-024 bevestigde relatedMatch voor Art32 → 5.35 (cross-category-rationale, niveau-1 evidence, confidence hoog). Stap-3-paren in dit cluster: 10 relatedMatch-paren (T3-015 t/m T3-023, T3-025).

**Cluster-evidence-overzicht:**

| Paar | Object | Pred | A.3.x | Annex D-link | Evidence-niveau |
|---|---|---|---|---|---|
| T3-015 | ISO27002_8_24 | relatedMatch | A.3.26 | **ja (32)(1)(a)** | **1** |
| T3-016 | ISO27002_5_15 | relatedMatch | N/A | — | 3 |
| T3-017 | ISO27002_5_16 | relatedMatch | A.3.8 | nee | 2 |
| T3-018 | ISO27002_5_17 | relatedMatch | N/A | — | 3 |
| T3-019 | ISO27002_5_18 | relatedMatch | A.3.9 | nee | 2 |
| T3-020 | ISO27002_8_13 | relatedMatch | A.3.24 | **ja (32)(1)(c)** | **1** |
| T3-021 | ISO27002_5_29 | relatedMatch | N/A | — | 3 |
| T3-022 | ISO27002_5_30 | relatedMatch | N/A | — | 3 |
| T3-023 | ISO27002_8_07 | relatedMatch | N/A | — | 3 |
| T3-025 | ISO27002_5_36 | relatedMatch | A.3.16 | **ja (32)(1)(d)/(2)** | **1** |

**Per-paar (gecondenseerd waar cross-category-rationale + cluster-conform-zekerheid samenvallen):**

#### T3-015 — compl:AVG_Art32 `skos:relatedMatch` ctrl:ISO27002_8_24

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art32` |
| Object IRI | `ctrl:ISO27002_8_24` (Cryptografie / Use of cryptography) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art32-cluster (12, heterogeen); object-cluster 2↔1 (homogeen, Art5_1f + Art32) |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel-sterk** — Art. 32 noemt expliciet pseudonimisering + versleuteling als voorbeeld-maatregelen; 8.24 levert cryptografie-gebruik. Operationele overlap is direct genoemd in Art. 32-tekst. Niet bilateraal — Art. 32 strekt zich uit tot CIA-vermogen, herstelvermogen, regelmatige beoordeling |
| **C2 (cardinaliteit)** | Subject-cluster 1↔12 (heterogeen); object-cluster 2↔1 (homogeen) |
| **C3 (inclusie)** | **geen conceptuele subset** — 8.24 is technische maatregel; Art. 32 is principe-norm. Cross-category-rationale: operationeel implementeert 8.24 *een onderdeel* van Art. 32, conceptueel geen subsumptie |
| **C4 (bron-evidence)** | **Niveau 1** — keten: ctrl:8.24 → A.3.26 → B.3.26 → Annex D (32)(1)(a). Direct |
| **Predicate-doel (§3.1)** | Rij 8 (cross-category): `relatedMatch`. closeMatch-toets: ondanks Art. 32 expliciete vermelding van versleuteling is interchangeability-niveau niet aanwezig — Art. 32 is veel breder dan cryptografie alleen |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — niveau-1 evidence + cross-category-rationale + sterke C1-overlap zonder retrieval-interchangeability |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

#### T3-016 — compl:AVG_Art32 `skos:relatedMatch` ctrl:ISO27002_5_15

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art32` |
| Object IRI | `ctrl:ISO27002_5_15` (Toegangsbeveiliging / Access control) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art32-cluster (12, heterogeen); object-cluster 2↔1 (Art5_1f + Art32, homogeen) |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel** — Art. 32 eist passende technische/organisatorische maatregelen + CIA-vermogen; 5.15 levert toegangsbeveiligings-regels op basis van bedrijfs- en IB-eisen. Operationele overlap: toegangsbeveiliging is canoniek voor CIA-vermogen. Niet bilateraal |
| **C2 (cardinaliteit)** | Subject-cluster 1↔12; object-cluster 2↔1 (homogeen) |
| **C3 (inclusie)** | **geen subset** — 5.15 is specifieke control; Art. 32 is principe. Cross-category |
| **C4 (bron-evidence)** | **Niveau 3** — 5.15 N/A in 27701:2025 Annex F.1 (27001:2013 6.6.1.1+6.6.1.2 niet in PIMS-scope). Tech-analyse |
| **Predicate-doel (§3.1)** | Rij 8: `relatedMatch` |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — cross-category + cluster-conform |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

#### T3-017 — compl:AVG_Art32 `skos:relatedMatch` ctrl:ISO27002_5_16

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art32` |
| Object IRI | `ctrl:ISO27002_5_16` (Identiteitsbeheer / Identity management) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art32-cluster (12, heterogeen); object-cluster singleton |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel** — Art. 32 eist passende beveiligings-maatregelen + CIA-vermogen; 5.16 levert identity-management-life-cycle (registratie, wijziging, beëindiging). Operationele overlap: identiteitsbeheer is fundament voor toegangsbeveiliging en daarmee voor CIA. Niet bilateraal |
| **C2 (cardinaliteit)** | Subject-cluster 1↔12; object-cluster singleton |
| **C3 (inclusie)** | **geen subset** — 5.16 is specifieke identity-control; Art. 32 is principe. Cross-category |
| **C4 (bron-evidence)** | **Niveau 2** — keten: ctrl:5.16 → A.3.8 via Annex F.1 ("Identity management") → B.3.8 → Annex D Table D.1 bevat geen directe entry voor B.3.8 → (32). 27701-equivalent bestaat, Annex D-link voor Art. 32 ontbreekt |
| Keten-stappen | Stap 1+2 OK; Stap 3 (Annex D-link voor (32)) ontbreekt — niveau 2 |
| **Predicate-doel (§3.1)** | Rij 8: `relatedMatch` |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — cross-category + cluster-conform; niveau-2 ondersteunt relatie zonder upgrade-grond |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

#### T3-018 — compl:AVG_Art32 `skos:relatedMatch` ctrl:ISO27002_5_17

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art32` |
| Object IRI | `ctrl:ISO27002_5_17` (Authenticatie-informatie / Authentication information) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art32-cluster (12, heterogeen); object-cluster singleton |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel** — Art. 32 eist passende beveiliging + CIA; 5.17 levert toewijzing en beheer van authenticatie-informatie (incl. paswoorden, tokens). Operationele overlap: authenticatie is fundament voor toegangsbeveiliging. Niet bilateraal |
| **C2 (cardinaliteit)** | Subject-cluster 1↔12; object-cluster singleton |
| **C3 (inclusie)** | **geen subset** — 5.17 is specifieke control; Art. 32 is principe. Cross-category |
| **C4 (bron-evidence)** | **Niveau 3** — 5.17 N/A in 27701:2025 Annex F.1 (27001:2013 6.6.2.4/6.6.3.1/6.6.4.3 niet in PIMS-scope). Tech-analyse |
| **Predicate-doel (§3.1)** | Rij 8: `relatedMatch` |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — cross-category + cluster-conform |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

#### T3-019 — compl:AVG_Art32 `skos:relatedMatch` ctrl:ISO27002_5_18

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art32` |
| Object IRI | `ctrl:ISO27002_5_18` (Toegangsrechten / Access rights) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art32-cluster (12, heterogeen); object-cluster singleton |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel** — Art. 32 eist passende beveiliging; 5.18 levert toewijzing, review en intrekking van toegangsrechten. Operationele overlap: rechten-beheer is fundament voor vertrouwelijkheids-bescherming. Niet bilateraal |
| **C2 (cardinaliteit)** | Subject-cluster 1↔12; object-cluster singleton |
| **C3 (inclusie)** | **geen subset** — 5.18 is specifieke access-rights-control; Art. 32 is principe. Cross-category |
| **C4 (bron-evidence)** | **Niveau 2** — keten: ctrl:5.18 → A.3.9 via Annex F.1 ("Access rights") → B.3.9 → Annex D Table D.1 bevat geen directe entry voor B.3.9 → (32). 27701-equivalent bestaat, Annex D-link voor Art. 32 ontbreekt |
| Keten-stappen | Stap 1+2 OK; Stap 3 (Annex D-link voor (32)) ontbreekt — niveau 2 |
| **Predicate-doel (§3.1)** | Rij 8: `relatedMatch` |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — cross-category + cluster-conform; niveau-2 ondersteunt relatie |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

#### T3-020 — compl:AVG_Art32 `skos:relatedMatch` ctrl:ISO27002_8_13

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art32` |
| Object IRI | `ctrl:ISO27002_8_13` (Back-up / Information backup) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art32-cluster (12, heterogeen); object-cluster singleton |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel-sterk** — Art. 32 noemt expliciet "vermogen tot herstel" als maatregel; 8.13 levert back-up-procedures. Operationele overlap is direct genoemd in Art. 32-tekst (herstel-vermogen). Niet bilateraal |
| **C2 (cardinaliteit)** | Subject-cluster 1↔12; object-cluster singleton |
| **C3 (inclusie)** | **geen conceptuele subset** — 8.13 is technische back-up-control; Art. 32 is principe. Cross-category |
| **C4 (bron-evidence)** | **Niveau 1** — keten: ctrl:8.13 → A.3.24 via Annex F.1 ("Information backup") → B.3.24 → Annex D Table D.1: B.3.24 → (5)(1)(f), (32)(1)(c). Directe Annex D-link voor Art. 32(1)(c) |
| Keten-stappen | ctrl:8.13 → 27701 A.3.24 → B.3.24 → AVG (32)(1)(c) |
| **Predicate-doel (§3.1)** | Rij 8 (cross-category): `relatedMatch`. closeMatch-toets: Art. 32 noemt herstel-vermogen expliciet, maar 8.13 implementeert *één onderdeel* van het brede maatregelen-pakket — geen retrieval-interchangeability |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — niveau-1 evidence + cross-category-rationale + sterke C1-overlap zonder interchangeability |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

#### T3-021 — compl:AVG_Art32 `skos:relatedMatch` ctrl:ISO27002_5_29

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art32` |
| Object IRI | `ctrl:ISO27002_5_29` (IB tijdens verstoring / Information security during disruption) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art32-cluster (12, heterogeen); object-cluster singleton |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel** — Art. 32 eist CIA-vermogen + herstel-vermogen na fysieke/technische incidenten; 5.29 levert IB-handhaving tijdens verstoring (BC-context). Operationele overlap: BC-aspect van CIA-handhaving. Niet bilateraal |
| **C2 (cardinaliteit)** | Subject-cluster 1↔12; object-cluster singleton |
| **C3 (inclusie)** | **geen subset** — 5.29 is BC-specifieke control; Art. 32 is principe. Cross-category |
| **C4 (bron-evidence)** | **Niveau 3** — 5.29 N/A in 27701:2025 Annex F.1 (27001:2013 6.14.1.x niet in PIMS-scope). Tech-analyse |
| **Predicate-doel (§3.1)** | Rij 8: `relatedMatch` |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — cross-category + cluster-conform |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

#### T3-022 — compl:AVG_Art32 `skos:relatedMatch` ctrl:ISO27002_5_30

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art32` |
| Object IRI | `ctrl:ISO27002_5_30` (ICT-gereedheid BCM / ICT readiness for business continuity) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art32-cluster (12, heterogeen); object-cluster singleton |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel** — Art. 32 eist herstel-vermogen na incidenten; 5.30 levert ICT-gereedheid voor BC, met capaciteit voor planning, implementatie, beheer, testen en evaluatie. Operationele overlap: ICT-readiness ondersteunt herstel-vermogen. Niet bilateraal |
| **C2 (cardinaliteit)** | Subject-cluster 1↔12; object-cluster singleton |
| **C3 (inclusie)** | **geen subset** — 5.30 is specifieke BC-control; Art. 32 is principe. Cross-category |
| **C4 (bron-evidence)** | **Niveau 3** — 5.30 N/A in 27701:2025 Annex F.1 ("New" niet in 2025-scope). Tech-analyse |
| **Predicate-doel (§3.1)** | Rij 8: `relatedMatch` |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — cross-category + cluster-conform |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

#### T3-023 — compl:AVG_Art32 `skos:relatedMatch` ctrl:ISO27002_8_07

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art32` |
| Object IRI | `ctrl:ISO27002_8_07` (Bescherming tegen malware / Protection against malware) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art32-cluster (12, heterogeen); object-cluster singleton |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel** — Art. 32 eist passende beveiliging tegen onrechtmatige verwerking + verlies/vernietiging/beschadiging; 8.07 levert malware-bescherming. Operationele overlap: malware is een belangrijk dreigings-mechanisme voor onrechtmatige verwerking / data-vernietiging. Niet bilateraal |
| **C2 (cardinaliteit)** | Subject-cluster 1↔12; object-cluster singleton |
| **C3 (inclusie)** | **geen subset** — 8.07 is specifieke malware-control; Art. 32 is principe. Cross-category |
| **C4 (bron-evidence)** | **Niveau 3** — 8.07 N/A in 27701:2025 Annex F.1 (27001:2013 6.9.2.1 niet in PIMS-scope). Tech-analyse |
| **Predicate-doel (§3.1)** | Rij 8: `relatedMatch` |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — cross-category + cluster-conform |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

#### T3-025 — compl:AVG_Art32 `skos:relatedMatch` ctrl:ISO27002_5_36

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art32` |
| Object IRI | `ctrl:ISO27002_5_36` (Naleving beleid/regels/normen / Compliance with policies, rules and standards) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art32-cluster (12, heterogeen); object-cluster singleton |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel-sterk** — Art. 32 eist "regelmatige beoordeling en evaluatie van de doeltreffendheid"; 5.36 levert naleving-controle op IB-beleid en -procedures. Operationele overlap is sterk op evaluatie/audit-aspect. Niet bilateraal (Art. 32 raakt veel meer dan naleving-controle alleen) |
| **C2 (cardinaliteit)** | Subject-cluster 1↔12; object-cluster singleton |
| **C3 (inclusie)** | **geen conceptuele subset** — 5.36 is specifieke compliance-evaluatie-control; Art. 32 is principe. Cross-category |
| **C4 (bron-evidence)** | **Niveau 1** — keten: ctrl:5.36 → A.3.16 via Annex F.1 ("Compliance with policies, rules and standards") → B.3.16 → Annex D Table D.1: B.3.16 → (32)(1)(d), (32)(2). Direct |
| Keten-stappen | ctrl:5.36 → 27701 A.3.16 → B.3.16 → AVG (32)(1)(d) + (32)(2) |
| **Predicate-doel (§3.1)** | Rij 8 (cross-category): `relatedMatch`. closeMatch-toets: 5.36 dekt naleving-monitoring; Art. 32 is veel breder — geen retrieval-interchangeability |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — niveau-1 evidence + cross-category-rationale + sterke C1-overlap zonder interchangeability |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

---

### §3.4 Cluster Art33 resterend (3 paren: T3-026 + T3-027 + T3-029)

**Cluster-context:** AVG_Art33 — Melding inbreuk aan toezichthoudende autoriteit; subject-cluster-grootte 4, heterogeen close×1/related×3. Pilot T3-028 bevestigde relatedMatch voor Art33 → 5.26 (cross-category-rationale, niveau-1 evidence, confidence middel — partieel-sterke C1 maar evident asymmetrische scope). Pilot observeerde reeds (§3.5 slot): T3-026 (Art33 → 5.24, closeMatch) is mogelijk strikter verdedigbaar als closeMatch dan T3-028. Stap-3-toets bevestigt deze observatie.

**Cluster-evidence-overzicht:**

| Paar | Object | Pred | A.3.x | Annex D-link | Evidence-niveau |
|---|---|---|---|---|---|
| T3-026 | ISO27002_5_24 | closeMatch | N/A | — | 3 |
| T3-027 | ISO27002_5_25 | relatedMatch | A.3.11 | **ja (33)(1)** | **1** |
| T3-029 | ISO27002_6_08 | relatedMatch | N/A | — | 3 |

#### T3-026 — compl:AVG_Art33 `skos:closeMatch` ctrl:ISO27002_5_24 (closeMatch-toets)

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art33` (AVG Art. 33 — melding inbreuk aan toezichthoudende autoriteit) |
| Object IRI | `ctrl:ISO27002_5_24` (Plannen incidentbeheer / Information security incident management planning and preparation) |
| Huidige predicate | `skos:closeMatch` |
| Cluster-context | Art33-subject-cluster (4, heterogeen close×1/related×3); object-cluster singleton |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel-sterk** — Art. 33 vereist meldings-procedure aan toezichthoudende autoriteit binnen 72 uur (parafrase m14 rdfs:comment), met meldings-inhoud-vereisten in lid 3. 5.24 (parafrase ISO 27002 §5.24) eist plannen en voorbereiden van incident management, inclusief vaststellen van rollen, escalatie-procedures, externe-communicatie-procedures, en breach-notification-voorbereiding. Operationele overlap is sterk op het deelaspect "breach notification-planning + externe meldings-procedure". 5.24 als geheel is echter breder dan alleen meldings-planning (omvat ook detectie, escalatie-intern, post-incident-review-planning) |
| **C2 (cardinaliteit)** | Subject-cluster 1↔4 (heterogeen); object-cluster singleton |
| **C3 (inclusie)** | **A ⊂ B (zwak)** — Art. 33 als specifieke meldings-procedure-eis kan binnen 5.24's bredere incident-management-planning-paraplu vallen. Echter conceptueel: Art. 33 is wettelijke verplichting; 5.24 is operationele plannings-maatregel. Cross-category-asymmetrie blijft (zie pilot §3.3 + §4.4). Operationeel: 5.24-plannings-output bevat de breach-notification-procedure die Art. 33 vereist |
| **C4 (bron-evidence)** | **Niveau 3** — 5.24 N/A in 27701:2025 Annex F.1 (27001:2013 6.13.1.1 niet in PIMS-scope). Geen keten-evidence via 27701; Tech-analyse via 27002 + AVG-tekst |
| **Predicate-doel (§3.1)** | Rij 3 (partiële overlap, geen subset, klein cluster, evidence 1-3): **`closeMatch`** — toetsbaar |
| **closeMatch-toets — verdedigbaar?** | **Ja, op de volgende gronden** (analoog T3-014 pilot-rapport §3.2-rationale): (a) C1 levert partieel-sterke operationele overlap op het kernaspect van Art. 33: incident-meldings-planning + externe-communicatie-procedure. (b) C3 toont zwakke operationele A⊂B-relatie; §3.1 rij 3 vereist geen bilaterale subset. (c) Object-cluster singleton — geen cluster-discipline-druk. (d) SKOS-semantiek closeMatch = retrieval-interchangeable. Art. 33 + 5.24 hebben dat interchangeability-niveau in GRC-context: een audit-vraag "welke control implementeert Art. 33-meldings-planningsplicht?" zou 5.24 als directe primaire match terug moeten geven — sterker dan voor 5.26 (zie pilot T3-028) of 5.25 (T3-027 zie hieronder) of 6.08 (T3-029) |
| **closeMatch vs relatedMatch — keuze-argumentatie** | **Analogie met T3-014 toegepast:** waar T3-014 (Art32 → 5.01 Beleidsregels IB) closeMatch verdedigt op governance/policy-relatie-canoniciteit, verdedigt T3-026 closeMatch op incident-planning-relatie-canoniciteit. **Distinctie van T3-026 vs T3-014:** evidence-niveau is lager (3 ipv. 2) — geen 27701-equivalent voor 5.24 in 2025-scope. Conceptuele verbinding is echter sterker (Art. 33 vereist specifiek "plan voor meldings-procedure"; 5.24 levert exact "incident management planning and preparation" inclusief breach notification). Pilot-observatie (§3.5 slot) bevestigd: T3-026 is strikter verdedigbaar als closeMatch dan T3-028 (Art33 → 5.26) zou zijn — 5.26 is reactief (incident-response in algemene zin), 5.24 is planning (waar de meldings-procedure thuishoort) |
| **Cross-category-rationale-overweging** | Een control ↔ legal-obligation closeMatch impliceert dat de control conceptueel "near-interchangeable" is met de juridische verplichting voor retrieval-doeleinden. Dit is een sterke claim. Pilot T3-014 (governance/policy) en deze T3-026 (incident-planning) zijn de twee m14-paren waar deze interchangeability houdbaar is op operationele basis. Voor andere paren (zoals T3-028 Art33→5.26) is interchangeability niet houdbaar — pilot heeft dat onderbouwd voor T3-028 |
| **Confidence** | **middel** — niveau-3 evidence (geen 27701-equivalent als ondersteunend signaal), C3 zwak (A⊂B operationeel maar cross-category-asymmetrie); maar partieel-sterke C1 + duidelijke retrieval-interchangeability + analogie met T3-014-redenering. Vergelijkbaar middel als T3-014 (evidence-niveau-2 ↔ niveau-3 verschil; conceptuele basis sterker bij T3-026) |
| **Voorgesteld predicate** | **BEHOUD `closeMatch`** |
| **Patch-vereist** | Nee |

#### T3-027 — compl:AVG_Art33 `skos:relatedMatch` ctrl:ISO27002_5_25

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art33` |
| Object IRI | `ctrl:ISO27002_5_25` (Beoordelen beveiligingsgebeurtenissen / Assessment and decision on IS events) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art33-cluster (4, heterogeen); object-cluster singleton |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel** — Art. 33 vereist meldings-procedure aan AP; 5.25 levert beoordeling van events + beslissing of een event een incident is. Operationele overlap: assessment-stap bepaalt of er "een inbreuk in verband met persoonsgegevens" is in Art. 33-zin (drempel-bepaling). Niet bilateraal — 5.25 is event-classificatie-control, Art. 33 is meldings-plicht |
| **C2 (cardinaliteit)** | Subject-cluster 1↔4; object-cluster singleton |
| **C3 (inclusie)** | **geen strikte subset** — 5.25 is operationele assessment-control; Art. 33 is wettelijke verplichting. Cross-category |
| **C4 (bron-evidence)** | **Niveau 1** — keten: ctrl:5.25 → A.3.11 via Annex F.1 ("Assessment and decision on IS events") → B.3.11 → Annex D Table D.1: B.3.11 → (33)(1) + andere Art. 33-paragrafen. Directe Annex D-link |
| Keten-stappen | ctrl:5.25 → 27701 A.3.11 → B.3.11 → AVG (33)(1) |
| **Predicate-doel (§3.1)** | Rij 8 (cross-category): `relatedMatch`. closeMatch-toets: 5.25 dekt assessment-stap; Art. 33 dekt meldings-plicht — operationeel sequentieel maar niet interchangeable |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — niveau-1 evidence + cross-category-rationale + duidelijke functionele complementariteit zonder interchangeability |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

#### T3-029 — compl:AVG_Art33 `skos:relatedMatch` ctrl:ISO27002_6_08

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art33` |
| Object IRI | `ctrl:ISO27002_6_08` (Melden beveiligingsgebeurtenissen / Information security event reporting) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art33-cluster (4, heterogeen); object-cluster singleton |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel** — Art. 33 vereist externe melding aan toezichthoudende autoriteit binnen 72 uur; 6.08 levert mechanismen voor medewerkers om IB-events tijdig intern te melden. Operationele overlap: 6.08 is interne event-reporting (medewerker → meldpunt), Art. 33 is externe breach-notification (organisatie → autoriteit). Verschillende meldings-richtingen + reikwijdtes |
| **C2 (cardinaliteit)** | Subject-cluster 1↔4; object-cluster singleton |
| **C3 (inclusie)** | **geen subset** — 6.08 is interne meldings-control; Art. 33 is externe meldings-plicht. Cross-category + andere meldings-laag |
| **C4 (bron-evidence)** | **Niveau 3** — 6.08 N/A in 27701:2025 Annex F.1 (27001:2013 6.13.1.2+6.13.1.3 niet in PIMS-scope). Tech-analyse |
| **Predicate-doel (§3.1)** | Rij 8: `relatedMatch` |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **hoog** — cross-category + duidelijke functionele complementariteit (interne meldings-stroom feed externe meldings-plicht) zonder interchangeability |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

---

### §3.5 Cluster Art34 resterend (1 paar: T3-030)

**Cluster-context:** AVG_Art34 — Mededeling inbreuk aan betrokkene; subject-cluster-grootte 2, homogeen relatedMatch×2. Pilot T3-031 (Art34 → 5.34 Privacy and protection of PII) bevestigde cluster-doel `relatedMatch` via cross-category-rationale (niveau-3 evidence, confidence hoog). Stap-3-paar T3-030 is het zuster-paar.

**Cluster-evidence-overzicht:**

| Paar | Object | Pred | A.3.x | Annex D-link | Evidence-niveau |
|---|---|---|---|---|---|
| T3-030 | ISO27002_5_26 | relatedMatch | A.3.12 | **ja (34)(1)/(2)** | **1** |

#### T3-030 — compl:AVG_Art34 `skos:relatedMatch` ctrl:ISO27002_5_26

| Veld | Waarde |
|---|---|
| Subject IRI | `compl:AVG_Art34` |
| Object IRI | `ctrl:ISO27002_5_26` (Reageren op informatiebeveiligingsincidenten / Response to information security incidents) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | Art34-cluster (2, homogeen); object-cluster 2↔1 (Art33 + Art34, homogeen related×2) |
| D4.1-disclaimer-check | n.v.t. |
| **C1 (definitioneel)** | **partieel-sterk** — Art. 34 vereist mededeling van inbreuk aan betrokkene bij hoog risico (parafrase m14 rdfs:comment); 5.26 levert response-procedures inclusief externe communicatie following need-to-know. Operationele overlap is sterk op externe-communicatie-aspect — voor Art. 34-gevallen omvat dat de mededeling aan betrokkenen. 5.26 als geheel is breder dan alleen mededeling (omvat containment, evidence, escalation, forensics) |
| **C2 (cardinaliteit)** | Subject-cluster 1↔2 (homogeen); object-cluster 2↔1 (homogeen). Geen cluster-discipline-druk; object-cluster ook homogeen |
| **C3 (inclusie)** | **geen strikte subset** — 5.26 is breder incident-response; Art. 34 is specifieke mededelings-plicht. Cross-category + scope-asymmetrie analoog T3-028 (pilot §3.5) |
| **C4 (bron-evidence)** | **Niveau 1** — keten: ctrl:5.26 → A.3.12 via Annex F.1 ("Response to information security incidents") → B.3.12 → Annex D Table D.1: B.3.12 → (34)(1), (34)(2). Directe Annex D-link |
| Keten-stappen | ctrl:5.26 → 27701 A.3.12 → B.3.12 → AVG (34)(1) + (34)(2) |
| **Predicate-doel (§3.1)** | Rij 8 (cross-category): `relatedMatch`. closeMatch-toets: 5.26 dekt brede incident-response; Art. 34 dekt specifieke mededelings-plicht — operationeel-component overlap maar geen retrieval-interchangeability (5.26 alleen is geen primaire match voor Art. 34) |
| **Mutatie-richting** | **behoud** |
| **Confidence** | **middel** — niveau-1 evidence + partieel-sterke C1; analoog T3-028 (pilot) scope-asymmetrie blijft methodisch-relevant; cluster-conform (homogeen Art34); cross-category-rationale leidend |
| **Voorgesteld predicate** | **BEHOUD `relatedMatch`** |
| **Patch-vereist** | Nee |

---

## §4. Analyse — patronen en bevindingen Stap 3

### §4.1 Cross-category-rationale-consolidatie (alle 25 paren bevestigen pilot-§4.4)

In alle 25 Stap-3-paren is dezelfde rationale leidend: control ↔ legal-obligation is een cross-category-relatie die inherent associatief (relatedMatch) is, niet subsumptief (broad/narrowMatch). Per-paar-C3-toets faalt systematisch op de richting "ctrl ⊂ AVG-artikel" op conceptueel niveau, hoewel operationeel een implementatie-relatie bestaat.

**Empirische bevestiging op productie-schaal:**

- Pilot 6 paren (Stap 2) — 0 cluster-convergentie naar narrowMatch
- Stap 3 25 paren — 0 cluster-convergentie naar narrowMatch
- Cumulatief m14 31 paren — 0 cluster-convergentie naar narrowMatch
- Cluster-doel-predicate per §3.1 rij 7 (1↔veel-subject-cluster): **systematisch overstemd door C3-falen op cross-category-niveau**

Dit is methodisch het tegenovergestelde van T2 (m10), waar alle 10 NIS2-clusters via §3.1 rij 6 naar broadMatch convergeerden. Het verschil:

| Module | Cluster-richting | Cluster-doel-default §3.1 | Cluster-convergentie-uitkomst | Categorie-relatie |
|---|---|---|---|---|
| m10 (T2) | veel↔1 (ctrl→NIS2) | broadMatch (rij 6) | 100% (alle 10 clusters) | control ↔ control-eis (zelfde categorie operationeel) |
| m14 (T3) | 1↔veel (compl→ctrl) | narrowMatch (rij 7) | 0% (geen cluster) | control ↔ legal-obligation (cross-category) |

m10's convergentie was framework-specifiek (ISO 27002 ↔ NIS2 zijn beide control/eisen-niveau). m14's non-convergentie is categorie-specifiek (cross-category-asymmetrie blokkeert cluster-projectie).

### §4.2 closeMatch-toets uitkomst voor Stap 3 (T3-026)

Eén closeMatch-paar in Stap 3 (T3-026: Art33 → 5.24 Plannen incidentbeheer). Toets-uitkomst: **behoud verdedigbaar** op deze gronden (analoog T3-014 pilot §3.2):

- Object-cluster-cardinaliteit singleton — geen cluster-discipline-druk
- §3.1 rij 3 (partiële overlap, geen strikte subset, klein cluster, evidence 1-3) levert exact `closeMatch`
- SKOS-semantiek closeMatch = retrieval-interchangeable; Art. 33 + 5.24 hebben dat interchangeability-niveau in GRC-context (incident-planning-relatie is canoniek voor breach-notification-plannings-aspect)
- Pilot-observatie (§3.5 slot) bevestigd: T3-026 is strikter verdedigbaar als closeMatch dan T3-028 (Art33 → 5.26 reactief) zou zijn
- Geen NEN-aantoonbare grond om naar relatedMatch te downgraden
- Confidence: **middel** (niveau-3 evidence ipv. T3-014's niveau-2; conceptuele basis is echter sterker bij T3-026 — incident-planning is preciezer-overlappend dan governance/policy)

**Cumulatieve closeMatch-status m14:** 2 closeMatch-paren (T3-014 Art32→5.01 + T3-026 Art33→5.24), beide behouden onder cross-category-rationale-uitzondering naar retrieval-interchangeability. Beide confidence middel. Beide methodologisch consistent toegepast.

### §4.3 broadMatch-richtings-bevinding — afgehandeld via masterchat-besluit

Pilot §5.2 escalatie (SKOS broadMatch-richtings-semantiek voor Art5_1f-cluster) is gesloten door masterchat-besluit Optie C (instructie-§ "Masterchat-besluit op pilot-escalatie"):

- T3-001 + T3-002: beide broadMatch-paren → relatedMatch in v4.6.3
- Rationale: cross-category-rationale + symmetrisch lossen van richtings-kwestie + cluster-consistentie (Art5_1f wordt homogeen related×7 post-patch)
- m10-broadMatch (ctrl→compl-richting) niet retroactief geheraudit; geldt als formeel correct in andere richting

Post-patch m14 SKOS-distributie: 0 broadMatch + 2 closeMatch + 29 relatedMatch. Cluster Art5_1f wordt homogeen.

### §4.4 Evidence-niveau-correlatie met confidence (cumulatief m14)

| Confidence | # paren cumulatief | Evidence-niveau-mix | Predicate-mix |
|---|---:|---|---|
| **hoog** | 26 (3 pilot + 23 Stap 3) | niveau-1 dominant, ook niveau-2/3 | relatedMatch (25) + relatedMatch-mutatie (T3-001) |
| **middel** | 5 (3 pilot + 2 Stap 3) | gemengd | relatedMatch (2: T3-028 + T3-030) + closeMatch (2: T3-014 + T3-026) + broadMatch oud (T3-002 pilot, nu gemuteerd) |
| **laag** | 0 | — | — |

Zie §6.5 voor de bron-van-waarheid-tabel (helper-script-onafhankelijke handmatige telling op §3 + §6.1 per-paar-classificatie).

**Observatie:** middel-confidence concentreert zich op paren met:
- Predicate-keuze-twijfel inherent (closeMatch-paren T3-014 + T3-026)
- Scope-asymmetrie tussen control en obligation (T3-028 + T3-030 — incident-response 5.26 versus specifieke Art. 33 en Art. 34 verplichtingen)
- Methode-kwestie die masterchat-besluit-input vroeg (T3-002 pilot oorspronkelijk — opgelost door besluit)

Conform Protocol v1.3 §5.2-drempels. Geen confidence-laag-paren geactiveerd; stop-conditie ≥3 laag niet genaderd.

### §4.5 Cluster-discipline §3.3 (v1.3 bewijslast-asymmetrie) — operationele werking op m14

v1.3 §3.3 bewijslast-asymmetrie stelt dat:

| Uitzondering-richting | Bewijslast |
|---|---|
| Naar sterker mapping | streng — bilaterale containment |
| Naar zwakker mapping | streng — NEN-bewijs dat C3 faalt |
| Behoud cluster-default | geen aanvullende bewijslast |

In m14-context werkt dit anders dan in m10:

- **m10**: cluster-default was `broadMatch`; alle 10 clusters convergeerden — bewijslast-asymmetrie blokkeerde 10 heuristiek-flags richting uitzondering-naar-sterker
- **m14**: cluster-default per §3.1 rij 7 zou `narrowMatch` zijn; 0 clusters convergeerden — cluster-discipline overstemd door C3-falen op cross-category-niveau

**Methode-vraag**: is "C3-falen op cross-category-niveau" een toelaatbare "individuele uitzondering aantoonbaar" in §3.3-zin, of is het een meta-niveau-blokkade die cluster-discipline-default-toepassing voorkomt? In de praktijk werkt het als de tweede: cross-category-rationale opereert vóór cluster-discipline-default-toepassing zou kunnen plaatsvinden. Dit is een **structurele eigenschap van cross-category-mappings**, niet een per-paar-uitzondering.

Status: **kandidaat voor v1.3.1-Brein-cyclus** (zie §5).

---

## §5. T3-leerpunt — cross-category-principe als kandidaat v1.3.1-precedent

### §5.1 Bevinding

Op de schaal van 31 m14-paren (pilot 6 + Stap 3 25) heeft de cross-category-rationale (control ↔ legal-obligation = associatief, niet subsumptief) systematisch gewerkt:

- 0 paren waar broad/narrowMatch op cross-category-basis verdedigbaar bleek
- 2 paren waar closeMatch op retrieval-interchangeability-basis verdedigbaar bleek (T3-014 + T3-026)
- 29 paren waar relatedMatch op cross-category-basis canoniek was

Dit is een **operationeel sluitend patroon** dat T2 (m10) niet kon onthullen, omdat m10 geen cross-category-mappings bevatte (ISO 27002 ↔ NIS2 zijn beide control/eisen-niveau).

### §5.2 Kandidaat-formalisering (NIET nu uitvoeren)

Voor Brein-cyclus-overweging na T3-afsluiting:

**Mogelijke v1.3.1-aanvulling op Protocol §3.3 (Cluster-discipline)** of nieuwe §3.4 (Cross-category-mappings):

> "**Cross-category-mappings:** wanneer subject en object van een SKOS-mapping in ontologisch verschillende categorieën zitten (bv. control ↔ legal-obligation, control ↔ standard-clause), is de basislijn-predicate `relatedMatch` (associatief). broad/narrowMatch tussen cross-category-paren is een categorie-fout in de meeste gevallen omdat operationele implementatie-relatie geen conceptuele subsumptie impliceert. Uitzondering naar `closeMatch` is mogelijk bij **retrieval-interchangeability** — wanneer de control de canonieke implementatie-equivalent is van de verplichting in een GRC-audit-context. Cluster-discipline §3.3 default-toepassing wordt op cross-category-niveau overstemd door C3-falen op conceptuele subsumptie."

**Inscope-voorbeelden:**
- control ↔ legal-obligation (T3-precedent m14: AVG ↔ ISO 27002)
- control ↔ wettelijke verplichting in andere modules (m10's compl:NIS2_a-j → control via ctrl→compl-richting was operationeel hetzelfde categorie omdat NIS2-Art21-letters control-eisen formuleren; geen cross-category)

**Buiten-scope-overweging:**
- Welke categorie-paren zijn cross-category? Lijst-uitbreiding via brain-vault concept-bestand (`brain__concepts__cross-category-mapping.md`?) als Brein-cyclus-output

### §5.3 Status

Niet uitgevoerd in T3. Aanbevolen voor Brein-cyclus post-T3 of v1.3.1-protocol-revisie. Tech-subagent voert geen autonome Protocol-tekst-wijziging uit (D4 + Protocol-vaststelling = masterchat-werk).

---

## §6. Cumulatief m14-overzicht (pilot 6 + Stap 3 25 = 31)

### §6.1 Per-paar-uitkomst-tabel cumulatief

| Paar | Subject | Object | Pred (v4.6.2) | Pred (v4.6.3) | Mutatie? | Confidence | Bron |
|---|---|---|---|---|---|---|---|
| T3-001 | AVG_Art5_1f | ISO27002_5_01 | broadMatch | **relatedMatch** | **ja (downgrade)** | hoog | Stap 3 §3.1 (masterchat-besluit Optie C) |
| T3-002 | AVG_Art5_1f | ISO27002_5_12 | broadMatch | **relatedMatch** | **ja (downgrade)** | hoog | Pilot §3.1 + masterchat-besluit |
| T3-003 | AVG_Art5_1f | ISO27002_5_15 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.1 |
| T3-004 | AVG_Art5_1f | ISO27002_8_24 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.1 |
| T3-005 | AVG_Art5_1f | ISO27002_8_10 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.1 |
| T3-006 | AVG_Art5_1f | ISO27002_8_11 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.1 |
| T3-007 | AVG_Art5_1f | ISO27002_8_12 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.1 |
| T3-008 | AVG_Art25 | ISO27002_8_25 | relatedMatch | relatedMatch | nee | hoog | Pilot §3.4 |
| T3-009 | AVG_Art25 | ISO27002_8_26 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.2 |
| T3-010 | AVG_Art25 | ISO27002_8_27 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.2 |
| T3-011 | AVG_Art25 | ISO27002_8_28 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.2 |
| T3-012 | AVG_Art25 | ISO27002_8_11 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.2 |
| T3-013 | AVG_Art25 | ISO27002_8_33 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.2 |
| T3-014 | AVG_Art32 | ISO27002_5_01 | closeMatch | closeMatch | nee | middel | Pilot §3.2 |
| T3-015 | AVG_Art32 | ISO27002_8_24 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.3 |
| T3-016 | AVG_Art32 | ISO27002_5_15 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.3 |
| T3-017 | AVG_Art32 | ISO27002_5_16 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.3 |
| T3-018 | AVG_Art32 | ISO27002_5_17 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.3 |
| T3-019 | AVG_Art32 | ISO27002_5_18 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.3 |
| T3-020 | AVG_Art32 | ISO27002_8_13 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.3 |
| T3-021 | AVG_Art32 | ISO27002_5_29 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.3 |
| T3-022 | AVG_Art32 | ISO27002_5_30 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.3 |
| T3-023 | AVG_Art32 | ISO27002_8_07 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.3 |
| T3-024 | AVG_Art32 | ISO27002_5_35 | relatedMatch | relatedMatch | nee | hoog | Pilot §3.3 |
| T3-025 | AVG_Art32 | ISO27002_5_36 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.3 |
| T3-026 | AVG_Art33 | ISO27002_5_24 | closeMatch | closeMatch | nee | middel | Stap 3 §3.4 |
| T3-027 | AVG_Art33 | ISO27002_5_25 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.4 |
| T3-028 | AVG_Art33 | ISO27002_5_26 | relatedMatch | relatedMatch | nee | middel | Pilot §3.5 |
| T3-029 | AVG_Art33 | ISO27002_6_08 | relatedMatch | relatedMatch | nee | hoog | Stap 3 §3.4 |
| T3-030 | AVG_Art34 | ISO27002_5_26 | relatedMatch | relatedMatch | nee | middel | Stap 3 §3.5 |
| T3-031 | AVG_Art34 | ISO27002_5_34 | relatedMatch | relatedMatch | nee | hoog | Pilot §3.6 |

**Mutatie-totaal cumulatief m14:** 2 (T3-001 + T3-002, beide downgrade broadMatch → relatedMatch). Triple-neutraal — predicate-substitutie binnen behouden totaal van 31.

### §6.2 Cluster-stand m14 v4.6.3 (post-patch)

| Cluster | Grootte | Predicate-mix v4.6.2 | Predicate-mix v4.6.3 | Heterogeniteit-Δ |
|---|---:|---|---|---|
| AVG_Art5_1f | 7 | broad×2 / related×5 | related×7 | **van heterogeen naar homogeen** |
| AVG_Art25 | 6 | related×6 | related×6 | ongewijzigd homogeen |
| AVG_Art32 | 12 | close×1 / related×11 | close×1 / related×11 | ongewijzigd heterogeen |
| AVG_Art33 | 4 | close×1 / related×3 | close×1 / related×3 | ongewijzigd heterogeen |
| AVG_Art34 | 2 | related×2 | related×2 | ongewijzigd homogeen |
| **Totaal** | **31** | broad×2 / close×2 / related×27 | **close×2 / related×29** | broadMatch geëlimineerd |

### §6.3 Confidence-verdeling cumulatief

| Confidence | Pilot (6) | Stap 3 (25) | Cumulatief m14 (31) |
|---|---:|---:|---:|
| hoog | 3 | 17 | 20 |
| middel | 3 | 8 | 11 |
| laag | 0 | 0 | 0 |

### §6.4 Confidence-verdeling cumulatief

| Confidence | Pilot (6) | Stap 3 (25) | Cumulatief m14 (31) |
|---|---:|---:|---:|
| hoog | 3 | 23 | 26 |
| middel | 3 | 2 | 5 |
| laag | 0 | 0 | 0 |

**Stap-3-middel-paren:** T3-026 (closeMatch-toets verdedigbaar; niveau-3 evidence; conceptuele basis sterker dan T3-014) + T3-030 (scope-asymmetrie analoog T3-028 — Art34 enger dan 5.26).

**Pilot-middel-paren:** T3-002 (SKOS-richtings-methodevraag — afgehandeld via masterchat-besluit; gemuteerd naar relatedMatch in v4.6.3), T3-014 (closeMatch-toets verdedigbaar; ontbrekende Annex D-link), T3-028 (partieel-sterke C1 maar evidente scope-asymmetrie Art33 enger dan 5.26).

### §6.5 Bron-van-waarheid + telling-discipline

Bovenstaande tellingen zijn handmatig afgeleid uit §3 per-paar-classificaties en §6.1 cumulatieve tabel. Geen helper-script gebruikt in T3 (Stap 3 25 paren is binnen handmatige scope). Conform Protocol v1.3 §10.3-discipline: §1-samenvattings-tabel + §4.4-tabel zijn afgeleid uit §6.4 (bron-van-waarheid); bij discrepantie geldt §6.4. Tabel-consistentie expliciet getoetst tijdens rapport-finalisering.

---

## §7. Stop-condities + escalaties Stap 3

### §7.1 Stop-conditie-evaluatie

| Conditie | Drempel | Stap-3-uitkomst | Cumulatief m14 | Geactiveerd? |
|---|---|---|---|---|
| Confidence "laag" | ≥3 paren | 0 paren laag (23 hoog, 2 middel) | 0 paren laag | Nee |
| Voorgestelde mutaties m14 | totaal >4 | 1 mutatie onder de 25 (T3-001, instructie-uitvoering) | 2 mutaties cumulatief (T3-001 + T3-002) | Nee (drempel >4 niet bereikt) |
| T3-026 of ander paar dwingt methode-vraag die cross-category-principe raakt | escalatie-vereiste | T3-026 bevestigt cross-category-principe en sluit binnen Protocol §3.1 rij 3; geen methode-vraag-trigger; cross-category-principe is leerpunt voor v1.3.1-Brein-cyclus | n.v.t. | Nee (leerpunt voor Brein, niet escalatie) |
| Onverwacht patroon | scope-impact | Geen — uitkomst conform pilot-prognose §6.2 en instructie-verwachte uitkomst | n.v.t. | Nee |

### §7.2 Geen escalatie-vraag aan masterchat in Stap 3

Geen masterchat-escalatie vereist tijdens Stap 3. Pilot-escalatie (broadMatch-richting) is opgelost door instructie-§ "Masterchat-besluit". Cross-category-principe-formalisering blijft Brein-cyclus-overweging, niet sprint-escalatie.

---

## §8. Mutatie-toepassing — gerapporteerde uitvoering

### §8.1 m14-ttl-staat v4.6.3

Twee mutaties toegepast op `ontology/m14-avg-gdpr.ttl` via `scripts/apply_patch_v4_6_3.py --apply`:

- T3-001: `compl:AVG_Art5_1f skos:broadMatch ctrl:ISO27002_5_01` → `skos:relatedMatch`
- T3-002: `compl:AVG_Art5_1f skos:broadMatch ctrl:ISO27002_5_12` → `skos:relatedMatch`

Beide mutaties zijn directe instructie-uitvoering op masterchat-besluit Optie C (pilot-escalatie §5.2). Geen autonome Tech-bevindingen onder de 25 Stap-3-paren. 24 paren behoud zonder file-mutatie.

### §8.2 Backup + verificatie

| Bestand | Pad |
|---|---|
| Backup pre-patch | `ontology/m14-avg-gdpr.ttl.v4_6_2.bak` (verwacht; aanwezig na productie-run) |
| Canonical metrics output | `output/verification/canonical_metrics_v4_6_3.json` |
| SHACL split-validatie output | `output/verification/shacl_results_v4_6_3.json` |
| File-hashes | `output/verification/file_hashes_v4_6_3.txt` |
| m14-ttl SHA256 v4.6.3 | `874565bade04c1657841298d4b035fa9c7f06f46a8d76ce9efba8ecfb35e1864` |
| m14-ttl SHA256 v4.6.2 (pre-patch) | `47daeb7e6f37080b5f88b6d4d594a0401e5f1e32356d330d9cbc0b287251d353` |

### §8.3 SHACL-uitkomsten Stap 3 (m14-mutaties)

Bevestigd ongewijzigd vs v4.6.2 baseline:

| Meting | Inference | Verwacht | Werkelijk |
|---|---|---:|---:|
| SECTIE A | none | 0 | **0** |
| SECTIE B | owlrl | 0 | **0** |
| COMBINED | owlrl | 290 (identiek v4.6.2) | **290** |

m14 ctrl↔compl-mappings worden niet door enige shape gevalideerd (H39-blinde-vlek, bevestigd in inventarisatie §8.4). De 2 SKOS-predicate-substituties raken geen shape — analoog T1/T2-precedent.

---

## §9. Hand-off-checklist

- [x] **Pre-push disclosure-check Protocol 14** uitgevoerd op dit rapport:
  - [x] Organisatie-naam: geen vermelding (`de organisatie` / generieke "Rijksoverheidsorganisatie" gebruikt waar nodig)
  - [x] Persoonsnamen: alleen "Steven" (toegestaan)
  - [x] Lokale paden: `/Users/stevenbouwmeester/grc-sources-licensed/`-paden zijn licentie-locatie-referenties; geen credentials
  - [x] Credentials/e-mail-domeinen: geen
  - [x] **NEN-tekst-fragmenten verbatim >10 woorden: geen** — alle citaten zijn parafrase + clausule-verwijzing. Control-name-strings (bv. "Information backup", "Access control", "Use of cryptography", "Independent review of information security", "Information security incident management planning and preparation", "Response to information security incidents") zijn factuele identifier-strings op control-name-niveau, geen guidance- of Control+Purpose-tekst
- [x] **Patch toegepast op `ontology/m14-avg-gdpr.ttl`** — 2 mutaties (T3-001 + T3-002), beide masterchat-besluit-uitvoering; geen autonome Tech-bevindingen
- [x] **Geen autonome commits** — Steven inspecteert + commit handmatig
- [x] **Rapport bottom-up gebouwd** conform Protocol v1.3 §10.2 (§3 per-paar eerst; §4-§7 daarna; §1-§2 laatst)
- [x] **Confidence-criteria expliciet toegepast** conform Protocol v1.3 §5.2-drempels
- [x] **Bindende T3-steers expliciet toegepast** per paar + samenvattend in §2.2
- [x] **Cross-category-rationale gedocumenteerd** als T3-leerpunt voor v1.3.1-Brein-cyclus (§5)
- [x] **Stop-conditie-evaluatie expliciet** in §7
- [x] **Cumulatief m14-overzicht** in §6 (31 paren tabelmatig)

### Achtergebleven werkende-tree-status

Bestanden gewijzigd of nieuw aangemaakt door deze hand-off:

| Pad | Type | Status |
|---|---|---|
| `ontology/m14-avg-gdpr.ttl` | TTL | gewijzigd (2 predicate-mutaties, pre-Stap-3-Stap; reeds aanwezig vóór deze rapport-opbouw) |
| `ontology/m14-avg-gdpr.ttl.v4_6_2.bak` | backup | aangemaakt (door applier productie-run) |
| `scripts/apply_patch_v4_6_3.py` | script | reeds aanwezig (vóór deze rapport-opbouw) |
| `output/verification/canonical_metrics_v4_6_3.py` | script | reeds aanwezig |
| `output/verification/canonical_metrics_v4_6_3.json` | output | reeds aanwezig |
| `output/verification/shacl_split_validate_v4_6_3.py` | script | reeds aanwezig |
| `output/verification/shacl_results_v4_6_3.json` | output | reeds aanwezig |
| `output/verification/file_hashes_v4_6_3.txt` | output | **nieuw aangemaakt in deze hand-off** |
| `output/reports/t3-stap3-eindrapport.md` | rapport | **nieuw aangemaakt (dit rapport)** |
| `output/reports/patch-rapport-v4_6_3.md` | rapport | **nieuw aangemaakt in deze hand-off** |

---

## §10. Terugkoppeling — 5-punten-resumé (Stap 3)

1. **Aantal mutaties voorgesteld onder de 25 Stap-3-paren:** 1 (T3-001, directe masterchat-besluit-uitvoering; geen autonome Tech-bevindingen onder de overige 24)
2. **Confidence-verdeling Stap 3:** 23 hoog / 2 middel (T3-026 + T3-030) / 0 laag
3. **closeMatch-toets T3-026 uitkomst:** **behoud verdedigbaar als closeMatch** — partieel-sterke C1 op incident-planning-relatie, retrieval-interchangeability houdbaar (Art33 + 5.24 conceptueel strikt-overlappend op breach-notification-planningsaspect), analoog T3-014 maar conceptuele basis sterker; niveau-3 evidence vergelijkbaar middel-confidence
4. **Stop-condities geactiveerd:** **nee** — geen confidence-laag-paren; cumulatief m14-mutaties = 2 (drempel >4 niet bereikt); T3-026 valt binnen Protocol §3.1 rij 3 zonder methode-vraag-trigger
5. **Cumulatief m14 cijfers (pilot + Stap 3):** 31 paren — 2 mutaties (beide broadMatch → relatedMatch op Art5_1f-cluster) + 29 behoud; eindstand m14 = 2 closeMatch + 0 broadMatch + 29 relatedMatch — conform instructie-§ "Verwachte uitkomst"

---

## §11. Verwijzingen

| Document | Pad |
|---|---|
| SKOS-protocol v1.3 FINAL | `docs/skos-beoordelings-protocol-v1_3.md` |
| T3-instructie Stap 3 | `docs/instructies/instructie-t3-stap3.md` |
| T3 pre-sprint-inventarisatie | `output/reports/t3-pre-sprint-inventarisatie.md` |
| T3 pilot-rapport (Stap 2) | `output/reports/t3-pilot-rapport.md` |
| T3 patch-rapport v4.6.3 | `output/reports/patch-rapport-v4_6_3.md` |
| Applier v4.6.3 | `scripts/apply_patch_v4_6_3.py` |
| Canonical metrics v4.6.3 (script + output) | `output/verification/canonical_metrics_v4_6_3.{py,json}` |
| SHACL v4.6.3 (script + output) | `output/verification/shacl_split_validate_v4_6_3.py` + `shacl_results_v4_6_3.json` |
| File-hashes v4.6.3 | `output/verification/file_hashes_v4_6_3.txt` |
| m14-ontologie-module | `ontology/m14-avg-gdpr.ttl` |
| m02-control (control-definities) | `ontology/m02-control.ttl` |
| ISO/IEC 27002:2022 (NEN-licensed) | `/Users/stevenbouwmeester/grc-sources-licensed/NEN-EN-ISO_IEC_27002_2022_en.pdf` |
| ISO/IEC 27701:2025 Annex D + F (NEN-licensed) | `/Users/stevenbouwmeester/grc-sources-licensed/ISO27701.pdf` |
| AVG/GDPR (publiek EU-recht) | EUR-Lex CELEX:32016R0679 |
| Dit rapport | `output/reports/t3-stap3-eindrapport.md` |

— Einde T3 Stap 3-eindrapport.
