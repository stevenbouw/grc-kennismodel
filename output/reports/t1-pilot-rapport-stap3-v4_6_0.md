---
type: report
subtype: pilot-rapport
sprint: T1
stap: 3
baseline: v4.6.0
date: 2026-05-26
status: final
related:
  - H36_skos-exactmatch-ctrl-compl-audit
  - D04_skos-cross-framework
  - skos-beoordelings-protocol-v1_0
scope: "Stap 3 — pre-Stap-3 evidence-onderzoek + pilot-5-beoordeling. Read-only. Geen TTL-wijzigingen. Geen git-commits/pushes."
---

# T1 — Pilot-rapport Stap 3 (5 paren)

## §1. Pre-Stap-3 evidence-onderzoek

### §1.1 Bron-toegankelijkheid in subagent-omgeving

| # | Bron | Lokaal beschikbaar? | Pad |
|---|---|---|---|
| 1 | ISO 27002:2022 | **Nee** | NEN-restrictief — uitsluitend in claude.ai PK |
| 2 | ISO 27001:2022 | **Nee** | NEN-restrictief — uitsluitend in claude.ai PK |
| 3 | NIS2-richtlijn (EU) 2022/2555 | Ja | `sources/eu-recht/EU-nis2-richtlijn.pdf` (73 p.) |
| 4 | Uitvoeringsverordening (EU) 2024/2690 | Ja | `sources/eu-recht/EU_2024_2690.pdf` (34 p.) |
| 5 | ENISA Technical Implementation Guidance v1.0 (juni 2025) | Ja (tekst-extract) | `sources/ensia/ENISA_Technical_implementation_guidance_on_cybersecurity_risk_management_measures_version_1_0.pdf` (6.297 regels platte tekst — bestand is geen geldige PDF maar wel doorzoekbare tekst) |
| 6 | BZK / NCSC-NL NIS2 ↔ ISO27002:2022-mapping | **Niet aangetroffen** | Geen lokaal bestand in `sources/overheid/`, `sources/nl-recht/` of `sources/adr-norea/`. (`sources/overheid/` bevat BIO 2.0 en ENISA-handreiking; geen mapping-document.) |
| 7 | CBW (NIS2) Control Framework — Excel | Ja | `sources/adr-norea/Cbw (NIS2) Control Framework.xlsx` (11 sheets, 215 rijen in hoofdsheet) |

### §1.2 Belangrijkste bevinding — autoritatieve mapping-keten gevonden

**De CBW-Excel sheet "Mapping Uitvoeringsverordening" reproduceert de officiële ENISA TIG mapping-tabel.** Deze tabel mapt per UV-clause (1.1 t/m 13.3) zowel naar ISO 27001:2022 (incl. Annex A controls op clausule-niveau) als naar NIST CSF v2.0 subcategories.

Bewijsketen:

1. **NIS2-richtlijn (EU) 2022/2555 art.21 lid 2** (PDF p. 47, NL/EN beide) noemt 10 thematische clauses (a t/m j). Art.21 zélf verwijst naar **"de stand van de techniek en de desbetreffende Europese en internationale normen"** zonder ISO 27002 expliciet te noemen.

2. **UV (EU) 2024/2690 considerans (3)** stelt expliciet (PDF p.0):

   > "the technical and methodological requirements of the cybersecurity risk-management measures set out in the Annex to this Regulation **are based on European and international standards, such as ISO/IEC 27001, ISO/IEC 27002** and ETSI EN 319 401, and technical specifications, such as CEN/TS 18026:2024"

3. **UV-Annex** (PDF p. 13-32) structureert de technische eisen in 13 hoofdstukken, **elk expliciet gekoppeld aan een NIS2-art.21-letter** via headers van het type *"3. Incident handling (Article 21(2), point (b), of Directive (EU) 2022/2555)"*. Volledige cross-walk:

   | UV-hoofdstuk | UV-titel | NIS2 art.21(2)(letter) |
   |---:|---|---|
   | 1 | Policy on the security of network and information systems | (a) |
   | 2 | Risk management policy | (a) |
   | 3 | Incident handling | (b) |
   | 4 | Business continuity and crisis management | (c) |
   | 5 | Supply chain security | (d) |
   | 6 | Security in network and information systems acquisition, development and maintenance | (e) |
   | 7 | Policies and procedures to assess the effectiveness of cybersecurity risk-management measures | (f) |
   | 8 | Basic cyber hygiene practices and security training | (g) |
   | 9 | Cryptography | (h) |
   | 10 | Human resources security | (i) |
   | 11 | Access control | (i) en (j) |
   | 12 | Asset management | (i) |
   | 13 | Physical and environmental security | — (geen art.21-letter; afgeleid uit algemene art.21 lid 1) |

4. **ENISA TIG v1.0** (regels 273-313) verwijst naar ISO 27002:2022 als bron-norm en vermeldt expliciet dat de mapping-tabel **als Excel-bestand op ENISA-website beschikbaar is**. Per-sectie-mapping-tabellen worden ook in de TIG-PDF aangeroepen (regels 1648, 2794, 2922, etc.) — die tabellen vormen de autoritatieve bron.

5. **De CBW-Excel sheet "Mapping Uitvoeringsverordening"** is een reproductie van deze ENISA TIG-tabel, met per UV-clause de ISO 27001:2022-referenties (Annex A controls op clausule-niveau, bv. "A.5.24" voor UV 3.1 Incident handling policy).

**Conclusie evidence-keten**: voor de relatie *NIS2 art.21 → ISO 27002:2022* bestaat een **expliciete autoritatieve mapping-keten via UV 2024/2690 + ENISA TIG**, gepubliceerd door de Europese Commissie (Implementing Regulation) en ENISA (de EU-cybersecurity-agency). Dit is **evidence-niveau 1** in protocol §2 C4-zin.

### §1.3 Reikwijdte van evidence-niveau-1 voor de 28 paren

UV 2024/2690 dekt **DNS-providers, TLD-registries, cloud, datacenters, CDN's, MSP's, MSSP's, marktplaatsen, search engines, social platforms en trust service providers** (UV considerans 1, art.1) — dus alleen sectorspecifieke "relevant entities". Voor andere NIS2-essentiële/belangrijke entiteiten (incl. overheidsorganisatie) is UV niet direct van toepassing maar wel **doctrinair gezaghebbend** als invulling van art.21 lid 1's "stand van de techniek". De Nederlandse Cbw-wet refereert hier ook aan via art.19 Cbw.

Voor protocol C4-toekenning betekent dit:

- Voor UV-clauses die direct corresponderen met een NIS2-art.21-letter (bv. UV 3 ↔ art.21(2)(b)), is evidence-niveau 1 haalbaar
- Voor de specifieke ISO27002-controls die per UV-clause genoemd worden in de Mapping Uitvoeringsverordening, is **evidence-niveau 1** beschikbaar voor *aanwezigheid van mapping*, maar de mapping zelf geeft **geen kwalificatie naar SKOS-niveau** (exactMatch vs broadMatch vs closeMatch). De ENISA-disclaimer (TIG regel 285) zegt expliciet: *"The mapping should not be interpreted as a measure of equivalency among different standards or frameworks."*

Dat is een belangrijke nuance: **de autoritatieve bron erkent de relatie maar verbiedt expliciet de gelijkstellings-interpretatie.** Dit ondergraaft `exactMatch` als juiste SKOS-keuze juist op evidence-niveau 1.

### §1.4 Evidence-niveau realistisch haalbaar per paar

| Niveau | Haalbaarheid | Toepassing |
|---|---|---|
| 1 (autoritatieve mapping aanwezig) | Ja, voor paren waar UV/TIG de control noemt — én met expliciete waarschuwing dat mapping géén equivalence betekent | Per pilot-paar te checken |
| 2 (norm-tekst identiek) | Nee, niet uitvoerbaar zonder ISO 27002-tekst-toegang | n.v.t. |
| 3 (definitie-overlap via rdfs:comment / norm-tekst) | Deels — NIS2 art.21-clauses zijn in eigen ontologie + NIS2-PDF; ISO27002-bron-tekst niet beschikbaar in subagent | Slechts unilaterale richting |
| 4 (label-overlap) | Altijd | Fallback |

**Operationele conclusie:** voor de pilot wordt C4-toekenning **niveau 1** gegeven wanneer paar voorkomt in CBW-Excel "Mapping Uitvoeringsverordening" met de specifieke ISO-control vermeld, **met disclaimer** dat ENISA expliciet equivalence ontkent. Anders niveau 3 (op basis van NIS2-tekst + label-overlap subject-zijde) of 4.

---

## §2. Pilot-paren beoordeling

Per paar: 4 criteria conform protocol §2 + voorstel + confidence. Beslis-tabel-toepassing conform protocol §3. Cluster-discipline (§3 slot) verplicht — als C2 faalt en voorstel is `broadMatch`, geldt dezelfde behandeling voor alle paren in het cluster tenzij expliciet anders gemotiveerd.

### §2.1 — Paar #1: T1-001 (ctrl:ISO27002_5_01 ↔ compl:NIS2_Art21_a)

| Veld | Inhoud |
|---|---|
| Paar-ID | T1-001 |
| Subject IRI | `ctrl:ISO27002_5_01` ("Beleidsregels voor informatiebeveiliging") |
| Object IRI | `compl:NIS2_Art21_a` ("Risicoanalyse en beveiliging informatiesystemen") |
| Cluster-context | NIS2-clause (a) — 1→1 binnen 28-set; **12-naar-1 binnen 121-set** (1 exact + 4 close + 4 related + 3 broad andere ctrl:-controls mappen ook naar NIS2_a) |
| C1 Definitioneel | **✗** — Subject is één control voor het opstellen van een ISMS-beleidsdocument; NIS2_a verplicht "beleid inzake risicoanalyse én beveiliging van informatiesystemen" (NIS2-PDF p.47 art.21(2)(a)). UV-Annex hoofdstuk 1 (Policy on security NIS) én hoofdstuk 2 (Risk management policy) zijn beide gekoppeld aan art.21(2)(a). NIS2_a is dus structureel breder: het omvat zowel beleids-eis als risico-eis. ISO27002_5_01 is enger. |
| C2 Cardinaliteit | **✗** — Binnen 28-set 1→1; binnen 121-set (Vraag B) heeft NIS2_a **11 andere ctrl:-mappings** (closeMatch: 5_02, 5_04, 5_35, 5_36; relatedMatch: 5_03, 5_05, 5_06, 5_31; broadMatch: 5_07, 5_08, 5_37). Subject zelf heeft alleen deze ene mapping (geen buiten-set-uitbreiding). De NIS2-clause (a) heeft dus géén unieke 1→1-relatie met enige ISO-control — exactMatch impliceert echter wel uniciteit. |
| C3 Inclusie | **✗ partial: A ⊆ B, geen B ⊆ A** — Beleidsregels-control past binnen NIS2_a (A ⊆ B geldt), maar NIS2_a omvat ook risico-analyse-eisen die niet door 5_01 alleen worden afgedekt (B ⊆ A faalt). UV-Annex bewijst dit door art.21(2)(a) zowel UV-hoofdstuk 1 *als* hoofdstuk 2 toe te wijzen. |
| C4 Bron | **Niveau 1** — CBW-Excel "Mapping Uitvoeringsverordening" rij 6: UV 1.1 "Policy on the security of network and information systems" → ISO 27001:2022 "5.2, A.5.1, A.5.36, A.5.4, 9.3" (ISO27002 5.01 = ISO27001 Annex A.5.1, dus formeel meegenomen). **Disclaimer**: ENISA TIG regel 285 stelt expliciet dat "*The mapping should not be interpreted as a measure of equivalency*". Niveau 1 voor aanwezigheid van mapping, nadrukkelijk geen niveau 1 voor *exact* equivalence. |
| Voorstel | **herclass-broadMatch** — Subject is enger dan object; protocol §3 zegt: "C1: A dekt deel van B (A enger) → A skos:broadMatch B (B is breder dan A)". |
| Confidence | **hoog** — alle vier criteria duidelijk wel of niet voldaan; autoritatieve bron geeft mapping én ontkent equivalence. |
| Patch-vereist | ja |

### §2.2 — Paar #2: T1-020 (ctrl:ISO27002_6_03 ↔ compl:NIS2_Art21_g)

| Veld | Inhoud |
|---|---|
| Paar-ID | T1-020 |
| Subject IRI | `ctrl:ISO27002_6_03` ("Bewustwording van, opleiding en training in informatiebeveiliging") |
| Object IRI | `compl:NIS2_Art21_g` ("Cyberhygiënepraktijken en opleiding cyberbeveiliging") |
| Cluster-context | NIS2-clause (g) — 1→1 binnen 28-set; **9-naar-1 binnen 121-set** (1 exact + 3 close + 2 related + 3 broad). UV-Annex hoofdstuk 8 splitst dit thema in 8.1 "Awareness raising and basic cyber hygiene practices" + 8.2 "Security training" — twee deel-onderwerpen. |
| C1 Definitioneel | **✗ marginaal** — Subject 6_03 dekt awareness + opleiding + training. NIS2_g vraagt "cyberhygiënepraktijken én opleiding cyberbeveiliging". Cyberhygiëne (UV 8.1) is breder dan ISO27002_6_03 (opleidings-focus); UV koppelt 8.1 → ISO Annex "7.3, A.6.3, A.8.7" en 8.2 → "7.2, A.6.3" — A.6.3 (= ISO27002_6_03) komt in beide voor. Maar UV 8.1 voegt A.8.7 (Bescherming tegen malware) en 7.3 (Awareness — clause uit ISO27001 main body) toe; UV 8.2 voegt 7.2 (Competence) toe. NIS2_g overlapt dus met ISO27002_6_03 maar omvat ook andere controls. A is enger dan B. |
| C2 Cardinaliteit | **✗** — Binnen 28-set 1→1; binnen 121-set heeft NIS2_g **8 andere ctrl:-mappings** (closeMatch: 6_08, 7_07, 8_23; relatedMatch: 5_04, 6_04; broadMatch: 8_01, 8_07, 8_09). Subject heeft alleen deze ene mapping. |
| C3 Inclusie | **✗ partial: A ⊆ B, geen B ⊆ A** — Awareness/training-control valt binnen cyberhygiëne+opleiding, maar NIS2_g dekt méér (malware-bescherming, clear desk, web-filtering volgens cluster — die zijn in 28-set niet als exactMatch maar close/related/broad gemapped). |
| C4 Bron | **Niveau 1** — CBW-Excel rijen 33-34 (UV 8.1 en 8.2) tonen ISO 27001 A.6.3 expliciet. Disclaimer ENISA TIG van toepassing: mapping ≠ equivalence. |
| Voorstel | **herclass-broadMatch** — Subject enger dan object. |
| Confidence | **hoog** — patroon identiek aan paar #1; cluster-grootte beperkt; UV-bewijs eenduidig. |
| Patch-vereist | ja |

### §2.3 — Paar #3: T1-010 (ctrl:ISO27002_5_24 ↔ compl:NIS2_Art21_b)

| Veld | Inhoud |
|---|---|
| Paar-ID | T1-010 |
| Subject IRI | `ctrl:ISO27002_5_24` ("Plannen en voorbereiden van het beheer van informatiebeveiligingsincidenten") |
| Object IRI | `compl:NIS2_Art21_b` ("Incidentbehandeling") |
| Cluster-context | NIS2-clause (b) — **4→1 binnen 28-set** (cluster: 5_24, 5_25, 5_26, 5_27 — alle exactMatch met NIS2_b); **10 totaal binnen 121-set** (4 exact + 2 close + 2 related + 2 broad). UV-Annex hoofdstuk 3 splitst dit in 6 sub-clauses (3.1 incident handling policy, 3.2 monitoring/logging, 3.3 event reporting, 3.4 event assessment/classification, 3.5 incident response, 3.6 post-incident reviews) → corresponderen 1-op-1 met 5_24-5_27 + 5_28 + 6_08 + 8_15/8_16. |
| C1 Definitioneel | **✗** — Subject 5_24 dekt specifiek "plannen en voorbereiden" (de "policy"-fase, UV 3.1). NIS2_b "Incidentbehandeling" omvat de hele lifecycle: detectie, classificatie, respons, herstel, evaluatie. Subject is één fase van een meerstaps-proces. |
| C2 Cardinaliteit | **✗** — 4→1 binnen 28-set is overduidelijke C2-failure (cluster van 4 ISO-controls map allemaal naar dezelfde NIS2-clause via exactMatch). UV-Annex hoofdstuk 3 splitst NIS2_b expliciet in 6 sub-clauses — wat de cluster-aard bevestigt. |
| C3 Inclusie | **✗ partial: A ⊆ B, geen B ⊆ A** — Plannings-control valt binnen incidentbehandeling, maar omgekeerd niet (NIS2_b vereist veel meer dan alleen plannen). |
| C4 Bron | **Niveau 1** — CBW-Excel rij 11 (UV 3.1 "Incident handling policy") → ISO 27001 Annex A.5.24. Direct hit. |
| Voorstel | **herclass-broadMatch** — Subject is één fase, object is hele lifecycle. |
| Confidence | **hoog** — C2-failure expliciet zichtbaar (4 ctrl:'s naar één compl:), C1/C3 conform UV-decompositie. |
| Patch-vereist | ja |
| Cluster-discipline | Cluster-b (4 paren: T1-010, T1-011, T1-012, T1-013) krijgt dezelfde behandeling — alle vier herclass-broadMatch — tenzij voor specifiek paar afwijking aantoonbaar is. Geen reden voor afwijking gevonden: alle 4 zijn fase-controls binnen incidentbehandelings-lifecycle (5_24=plannen, 5_25=beoordelen, 5_26=reageren, 5_27=leren) en alle 4 mappen volgens UV-Annex naar verschillende UV 3.x-sub-clauses van hoofdstuk 3. **Logische projectie cluster-b: 4× broadMatch.** |

### §2.4 — Paar #4: T1-002 (ctrl:ISO27002_5_09 ↔ compl:NIS2_Art21_i)

| Veld | Inhoud |
|---|---|
| Paar-ID | T1-002 |
| Subject IRI | `ctrl:ISO27002_5_09` ("Inventarisatie van informatie en andere gerelateerde bedrijfsmiddelen") |
| Object IRI | `compl:NIS2_Art21_i` ("Beveiliging personeel, toegangsbeleid en activabeheer") |
| Cluster-context | NIS2-clause (i) — **6→1 binnen 28-set** (cluster: 5_09, 5_15, 5_16, 5_18, 6_01, 6_02); **32-naar-1 binnen 121-set** — verreweg de grootste cluster (6 exact + 11 close + 9 related + 6 broad). NIS2_i omvat drie expliciete thema's: HR-security, access control, asset management. UV-Annex splitst dit in 3 hoofdstukken: 10 (HR), 11 (Access control — gedeeld met (j)), 12 (Asset management). |
| C1 Definitioneel | **✗ duidelijk** — Subject 5_09 is asset-inventarisatie (één activiteit binnen asset management). NIS2_i is brede thematische clause met drie sub-domeinen (HR + access + assets). UV-Annex bewijst de drie-deling structureel via hoofdstukken 10, 11, 12. Subject is een micro-deel van macro-clause. |
| C2 Cardinaliteit | **✗ massaal** — 6→1 binnen 28-set; 32→1 in 121-set. Sterkst gefaalde C2 van alle pilot-paren. UV-decompositie in 3 hoofdstukken bevestigt structurele veel→1-aard. |
| C3 Inclusie | **✗ partial: A ⊆ B, geen B ⊆ A** — Asset-inventarisatie ⊆ NIS2_i; omgekeerd valt grootste deel van NIS2_i (HR, access control, andere asset-controls) niet binnen 5_09. |
| C4 Bron | **Niveau 1** — CBW-Excel rij 50 (UV 12.4 "Asset inventory") → ISO 27001 A.5.9. Direct hit. |
| Voorstel | **herclass-broadMatch** |
| Confidence | **hoog** — sterkste C2-failure in pilot; UV-3-hoofdstuks-decompositie is structureel ondubbelzinnig. |
| Patch-vereist | ja |
| Cluster-discipline | Cluster-i (6 paren: T1-002, T1-003, T1-004, T1-005, T1-018, T1-019) krijgt dezelfde behandeling — alle zes herclass-broadMatch. Geen reden voor uitzondering: alle 6 vertegenwoordigen specifieke controls binnen één van de drie NIS2_i-sub-domeinen (5_09=asset inventory, 5_15=toegangsbeveiliging, 5_16=identiteitsbeheer, 5_18=toegangsrechten, 6_01=screening, 6_02=arbeidsovereenkomst), die in UV-Annex verspreid zijn over hoofdstukken 10, 11, 12. **Logische projectie cluster-i: 6× broadMatch.** |

### §2.5 — Paar #5: T1-024 (ctrl:ISO27002_8_25 ↔ compl:NIS2_Art21_e)

| Veld | Inhoud |
|---|---|
| Paar-ID | T1-024 |
| Subject IRI | `ctrl:ISO27002_8_25` ("Beveiligen tijdens de ontwikkelcyclus") |
| Object IRI | `compl:NIS2_Art21_e` ("Beveiliging verwerving, ontwikkeling en onderhoud systemen") |
| Cluster-context | NIS2-clause (e) — **5→1 binnen 28-set** (cluster: 8_25, 8_26, 8_27, 8_28, 8_29); **17-naar-1 binnen 121-set** (5 exact + 4 close + 6 related + 2 broad). NIS2_e omvat verwerving + ontwikkeling + onderhoud — drie fasen. UV-Annex hoofdstuk 6 splitst dit in 7 sub-clauses (6.1 acquisition, 6.2 secure development life cycle, 6.3 configuration mgmt, 6.4 change mgmt/repair/maintenance, 6.5 security testing, 6.6 patch mgmt, 6.7 network security). |
| C1 Definitioneel | **✗** — Subject 8_25 is "Secure development life cycle" — exact UV 6.2. NIS2_e omvat dit én verwerving (UV 6.1) én onderhoud/wijzigingsbeheer (UV 6.4) én testen (UV 6.5) én patching (UV 6.6) én netwerk-beveiliging (UV 6.7). Subject is één van zeven UV-sub-clauses. |
| C2 Cardinaliteit | **✗** — 5→1 binnen 28-set; 17→1 in 121-set. UV-Annex-decompositie in 7 sub-clauses bevestigt veel→1. |
| C3 Inclusie | **✗ partial: A ⊆ B, geen B ⊆ A** — SDLC-control ⊆ NIS2_e; omgekeerd dekt NIS2_e veel méér dan alleen SDLC. |
| C4 Bron | **Niveau 1** — CBW-Excel rij 23 (UV 6.2 "Secure development life cycle") → ISO 27001 A.8.25, A.8.31. Direct hit. |
| Voorstel | **herclass-broadMatch** |
| Confidence | **hoog** — UV-7-sub-clauses-decompositie is structureel ondubbelzinnig. |
| Patch-vereist | ja |
| Cluster-discipline | Cluster-e (5 paren: T1-024, T1-025, T1-026, T1-027, T1-028) krijgt dezelfde behandeling — alle vijf herclass-broadMatch. Geen reden voor uitzondering: alle 5 zijn specifieke development-fase-controls (8_25=SDLC, 8_26=app-eisen, 8_27=architectuur, 8_28=veilig coderen, 8_29=testen) die in UV-Annex verspreid zijn over sub-clauses 6.2, 6.5, 6.6 etc. **Logische projectie cluster-e: 5× broadMatch.** |

---

## §3. Stop-conditie-check

| # | Stop-conditie | Telling | Hit? |
|---|---|---|---|
| 1 | Onverwachte uitkomst-richting (behoud op #3/#4/#5 of herclass op #1/#2) | Verwachting protocol §6: paren #1+#2 → behoud; paren #3+#4+#5 → broadMatch. Pilot-uitkomst: **#1+#2 → herclass-broadMatch** (afwijking van verwachting); #3+#4+#5 → broadMatch (conform verwachting). | **JA — partial hit** — paren #1 en #2 (1→1-binnen-28-set) krijgen tóch herclass-voorstel |
| 2 | Confidence "laag" op ≥3 van 5 | 0 paren met confidence "laag" (alle 5 op "hoog") | NEE |
| 3 | Evidence-niveau 4 op ≥3 van 5 | 0 paren op niveau 4 (alle 5 op niveau 1) | NEE |

### §3.1 Analyse stop-conditie 1 (partial hit)

De verwachting in protocol §6 dat de 1→1-paren (#1+#2) `exactMatch`-behoud zouden krijgen, is **niet gerealiseerd**. Beide paren krijgen herclass-broadMatch-voorstel. **Reden**: het cardinaliteit-criterium C2 is in de pre-sprint-inventarisatie gedefinieerd binnen de 28 exactMatch-paren, maar protocol §2 C2 "Belangrijke nuance" verplicht óók buiten-set-check binnen de bredere 121 ctrl:↔compl:-mappings. Voor #1 en #2 toont die buiten-set-check dat het object respectievelijk 11 en 8 *andere* ctrl:-mappings heeft via close/related/broadMatch. Een 1→1-cardinaliteit binnen de exactMatch-set bestaat wel, maar binnen de hele mapping-set is er géén 1→1.

Daarbovenop faalt C1/C3 voor #1 en #2 zelfstandig: de NIS2-clauses (a) en (g) zijn thematisch breder dan de individuele ISO-controls volgens UV-Annex-decompositie. Voor (a): UV-hoofdstukken 1 én 2 zijn beide aan art.21(2)(a) gekoppeld. Voor (g): UV-hoofdstuk 8 splitst in 8.1 + 8.2.

**Het is dus geen uitkomst die het protocol op een onverwachte plek raakt: het is een uitkomst die de C1/C3-criteria correct toetsen, terwijl C2 in de strikte 28-set-interpretatie de verwachting kleurde**. Het protocol werkt — alleen de pre-pilot-verwachting in §6 was te zwaar gewogen op C2-strikte-28-set.

### §3.2 Eindoordeel stop-conditie

**Strikt lezen protocol §6**: stop-conditie 1 ("onverwachte uitkomst") triggert.
**Inhoudelijk lezen**: het protocol werkt zoals bedoeld; de pre-pilot-verwachting was te beperkt geformuleerd, niet het protocol zelf.

Tech-aanbeveling: **PAUZE — escalatie Masterchat** voor expliciete go/no-go-beslissing. De pilot levert een **inhoudelijk eenduidige en cluster-consistente uitkomst** (alle 5 paren → broadMatch met hoge confidence en evidence-niveau 1), maar wijkt af van de pre-pilot-verwachting in protocol §6 voor twee paren. Masterchat moet bevestigen of:

- **Optie A**: voortgaan naar Stap 4 met geleerde nuance (verwachting was protocol-context, niet criterium-norm; pilot bevestigt cluster-broadMatch als systemisch patroon ook voor 1→1-binnen-28-set-clusters)
- **Optie B**: protocol §6-verwachting bijstellen en daarna voortgaan (sub-versie protocol v1.1)
- **Optie C**: aanvullend onderzoek op #1+#2 (bv. ISO 27002:2022-tekst-toegang via Steven uit PK om C1 op definitionele-tekst-niveau te verifiëren) voordat doorgaan

**Tech-aanbeveling: Optie A** — de pilot is materieel succesvol (cluster-consistente broadMatch-voorstellen met hoge confidence en evidence-niveau 1 op alle 5). De afwijking van §6-verwachting is een protocol-leerpunt, niet een data-failure. Stap 4 kan parallel doorlopen met expliciete vermelding dat ook 1→1-binnen-28-set-clusters cluster-broadMatch krijgen als bredere C2-context dat onderbouwt.

---

## §4. Cluster-impact-projectie (bij GO van Masterchat)

Indien Masterchat Optie A/B goedkeurt en Stap 4 doorgaat, dan is dit de projectie op de resterende 23 paren op basis van pilot-cluster-leerpunten:

| NIS2-cluster | Paren in cluster | Pilot-paar | Verwachte uitkomst overige paren | Logische motivering |
|---|---|---|---|---|
| (a) — Risicoanalyse + beleid | 1 paar: T1-001 | T1-001 | n.v.t. — pilot is enige paar | — |
| (b) — Incidentbehandeling (4→1) | 4 paren: T1-010 t/m T1-013 | T1-010 → broad | T1-011, T1-012, T1-013 → broadMatch | UV-3-decompositie in 6 sub-clauses; alle 4 zijn fase-controls in incident-lifecycle |
| (c) — Continuïteit + back-up (3→1) | 3 paren: T1-014, T1-015, T1-022 | geen pilot | Te verifiëren in Stap 4 | UV-Annex hoofdstuk 4 splitst in 4.1 BC/DR-plan + 4.2 backup mgmt + 4.3 crisis mgmt; cluster-broadMatch verwacht maar niet gevalideerd in pilot |
| (d) — Toeleveringsketen (4→1) | 4 paren: T1-006 t/m T1-009 | geen pilot | Te verifiëren in Stap 4 | UV-Annex hoofdstuk 5; cluster-broadMatch verwacht maar niet gevalideerd in pilot |
| (e) — Verwerving/ontwikkeling (5→1) | 5 paren: T1-024 t/m T1-028 | T1-024 → broad | T1-025, T1-026, T1-027, T1-028 → broadMatch | UV-6-decompositie in 7 sub-clauses; alle 5 zijn development-fase-controls |
| (f) — Doeltreffendheid (2→1) | 2 paren: T1-016, T1-017 | geen pilot | Te verifiëren in Stap 4 | UV-Annex hoofdstuk 7; cluster-broadMatch verwacht maar niet gevalideerd in pilot |
| (g) — Cyberhygiëne + opleiding | 1 paar: T1-020 | T1-020 → broad | n.v.t. — pilot is enige paar in cluster | UV-8-decompositie in 8.1+8.2 onderbouwt broadMatch |
| (h) — Cryptografie | 1 paar: T1-023 | geen pilot | Te verifiëren in Stap 4 | UV-Annex hoofdstuk 9; 1→1 binnen 28-set maar buiten-set-check Stap 4 vereist (in 121-set: 5_14 closeMatch + 8_03/8_11 relatedMatch + 8_05/8_20/8_21 broadMatch naar NIS2_h) — verwachting broadMatch op basis van pilot-patroon |
| (i) — Personeel + toegang + activa (6→1) | 6 paren: T1-002, T1-003, T1-004, T1-005, T1-018, T1-019 | T1-002 → broad | T1-003, T1-004, T1-005, T1-018, T1-019 → broadMatch | UV-decompositie in 3 hoofdstukken (10, 11, 12); structureel veel→1 |
| (j) — Multi-factor authenticatie | 1 paar: T1-021 | geen pilot | Te verifiëren in Stap 4 | UV-Annex hoofdstuk 11 deelt met (i); UV 11.7 "Multi-factor authentication" → A.8.5 (= 8_05). 1→1 binnen 28-set, buiten-set: 8_03 relatedMatch + 8_22 relatedMatch + 5_32 relatedMatch + 5_15/5_16/5_17 closeMatch + 6_07/8_02 broadMatch. Verwachting **mogelijk behoud-exactMatch** voor (j) — UV 11.7 mapt 1-op-1 naar één ISO-control; dit is uniek in pilot-context. Tech-aanbeveling: Stap 4 expliciet onderzoeken. |

**Projectie totaal** voor de 23 niet-piloted paren:

- Hoge-confidence verwachting broadMatch op basis van pilot-cluster: **20 paren** (clusters b, e, i — 4+5+6 = 15 paren — plus c, d, f vanwege identieke UV-decompositie-patroon — 3+4+2 = 9, maar c/d/f zonder pilot-bevestiging = **9 paren als "verwacht-broadMatch-pending-Stap4-validatie"**)
- Mogelijk behoud-exactMatch (UV-1-op-1-mapping): **1 paar** (T1-021 NIS2_j ↔ 8_05 — UV 11.7 als enige sub-clause)
- Mogelijk behoud-exactMatch op basis van NIS2-clause-smal-genoeg (klein cluster): **1 paar** (T1-023 NIS2_h ↔ 8_24 — UV-hoofdstuk 9 heeft één sub-clause 9.1)

**Verfijnde verwachting**: 21 van 23 resterende paren → broadMatch; 2 paren (h, j) zijn **kandidaten voor behoud-exactMatch** mits bilaterale containment in Stap 4 hard te maken is (B ⊆ A test).

---

## §5. Werkflow-leerpunten

Inhoudelijke en operationele leerpunten voor T1-eindrapport §8:

1. **Evidence-niveau-1-bron bestaat onverwacht in eigen sources** — De CBW-Excel "Mapping Uitvoeringsverordening"-sheet bleek de ENISA TIG-mapping-tabel te reproduceren. Pre-sprint-inventarisatie van Stap 1 (Vraag A) heeft deze sheet niet als evidence-bron geïdentificeerd; het hoort dáár expliciet vermeld te worden in toekomstige T-sprints. Aanbeveling: T-sprints starten standaard met een `sources/`-doorzoek op cross-walk-Excels.

2. **ENISA-disclaimer ondergraaft exactMatch op evidence-niveau 1** — Centrale paradox: de autoritatieve mapping-bron (ENISA TIG) erkent de relatie maar verbiedt expliciet de "equivalence"-interpretatie. Dit betekent dat zelfs perfect-niveau-1-evidence **geen `exactMatch` rechtvaardigt** als SKOS-keuze — `broadMatch`/`closeMatch` is de juiste D4-conforme interpretatie. Dit is een **structurele les voor T2/T3** en mogelijk een D4-aanvulling/-verheldering waard.

3. **C2 in protocol §2 — strikte vs brede interpretatie** — Het protocol legt C2 binnen-28-set + verplichte buiten-set-check; pilot heeft dit uitgevoerd en aangetoond dat de buiten-set-check beslissend is voor #1+#2. De pre-pilot-verwachting in §6 was gebaseerd op strikte 28-set-interpretatie. T-sprint-2 (resterende 23 paren) moet dit consequent toepassen om consistentie te borgen.

4. **NEN-bron-toegankelijkheid blijft beperking** — ISO 27002:2022-tekst niet beschikbaar in Tech-omgeving (NEN-restrictief, alleen claude.ai PK). C1/C3-toetsing kon nu alleen via label + structurele UV-mapping-interpretatie. Voor edge-cases (bv. T1-023 (h) of T1-021 (j)) waar bilaterale containment moet worden vastgesteld, kan Steven gericht passages uit ISO 27002 ophalen via PK indien noodzakelijk in Stap 4.

5. **SKOS-symmetrie-afwezigheid (uit protocol §7)** — Tijdens C2-buiten-set-check zichtbaar dat alle 28 exactMatch-paren asymmetrisch zijn (ctrl:→compl: zonder reverse). owlrl laadt geen SKOS-axiomas (skos:S46). Niet als nieuw H-item nu — bevestigd T1-werkflow-leerpunt voor §8.

6. **Tooling-observatie: ENISA TIG-PDF is geen geldig PDF** — `sources/ensia/ENISA_Technical_implementation_guidance_*.pdf` start met "EUROPEAN UNION..." (platte tekst), niet met `%PDF`-header. Pypdf faalt op dit bestand. Workaround via grep/sed werkt. Aanbeveling: in `brain__sources__-register.md` markeren als "tekst-extract, geen werkende PDF" en bij vervangings-trigger oorspronkelijke PDF van ENISA opnieuw downloaden.

7. **Per-sectie mapping-tabellen in TIG-PDF zelf verloren** — TIG-PDF-tekst verwijst expliciet naar "mapping table at the end of this section" (regels 1648, 2794, 2922, 3049, 3178, 3348, 3573, 3746, 4083 — 9 tabellen totaal), maar tabel-content is bij tekst-extractie verloren. De CBW-Excel-reproductie compenseert dit volledig.

8. **Protocol 14 (pre-push disclosure-check) — eerste productie-toepassing** — Rapport gescand vóór finalisering op:
   - Organisatie-naam: **niet aangetroffen** (altijd "de organisatie" / "Rijksoverheidsorganisatie")
   - Persoonsnamen: **alleen Steven (projecteigenaar)** — toegestaan binnen project-context, zoals in bestaande brain-vault-bestanden
   - Lokale paden buiten repo-relative: **niet aangetroffen** (alle paden `sources/...`, `ontology/...`, `output/...`, `docs/...` repo-relative; geen absolute paden naar `/Users/...`)
   - NEN-tekst-quotes: **niet aangetroffen** (alleen verwijzingen naar ISO-clausule-IDs zoals A.5.24, niet de inhoudelijke tekst van ISO-controls)
   
   Ervaring: protocol 14-check duurt ~3 minuten voor een rapport van deze omvang; goed uitvoerbaar zonder geautomatiseerde tooling. Aanbeveling: voor terugkerende rapport-typen kan een eenvoudig `grep`-script in `scripts/` worden toegevoegd dat zoekt op organisatie-trefwoorden + absolute-pad-patroon — niet nu uitvoeren (scope-uitbreiding), wel als toekomstig H-item-overweging.

9. **Cluster-discipline operationeel goed werkbaar** — Pilot-paren #3, #4, #5 zaten in clusters van 4, 6, 5 paren; per cluster één paar in pilot, conclusies expliciet doorgetrokken naar overige cluster-leden. Operationeel praktisch (bespaart 9 detail-beoordelingen die conceptueel identiek zijn), inhoudelijk verdedigbaar (cluster-leden delen UV-Annex-decompositie-positie). Aanbevolen patroon voor Stap 4.

---

## §6. Rapport-conclusie

- Evidence-niveau 1 is **wel** haalbaar — via UV 2024/2690 + ENISA TIG + CBW-Excel "Mapping Uitvoeringsverordening"
- Alle 5 pilot-paren leveren herclass-broadMatch-voorstel met confidence "hoog"
- Stop-conditie 1 (onverwachte uitkomst-richting) **strikt gelezen geraakt** voor paren #1 en #2 — maar inhoudelijk klopt het protocol; alleen pre-pilot-verwachting in §6 was te beperkt
- **Tech-aanbeveling: PAUZE — escalatie Masterchat** met Optie A/B/C-keuze (voorkeur: Optie A — voortgaan met geleerde nuance)
- Bij GO: 21 van 23 resterende paren projecteerbaar als broadMatch op basis van cluster-discipline + UV-decompositie; 2 paren (T1-023, T1-021) zijn behoud-exactMatch-kandidaten waarvoor Stap 4 bilaterale containment moet vaststellen

— Einde rapport.
