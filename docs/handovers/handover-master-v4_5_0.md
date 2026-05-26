# MASTER-HANDOVER-DOCUMENT — GRC KENNISMODEL

**Versie:** 1.0
**Datum:** 20 mei 2026
**Opsteller:** Masterchat v4.0
**Type:** Strategisch + operationeel handover-document
**Status:** levend document, bijwerken bij belangrijke koers-veranderingen
**Locatie post-migratie:** `docs/handovers/handover-master-v4.5.0.md`

---

## 0. Document-doel en lezers

Dit document is **niet** de projectinstructie en **niet** de brain-vault. Het complementeert beide voor drie soorten lezers:

| Lezer | Wat hier te vinden is |
|---|---|
| **Vervangende Claude-instance** (chat-restart, migratie, andere reden) | Operationele context — werkwijze, conventies, lopende afwegingen die niet in projectinstructie staan |
| **Andere mens dan de huidige projecteigenaar** (vakantie-vervanger, project-overdracht, audit) | Strategische context — stakeholders, beslissings-historie achter beslissingen, visie-onderbouwing |
| **Toekomstige projecteigenaar** (zelf, terugkomst na onderbreking) | Geheugen-anker — waar waren we, wat speelde, wat nu |

**Wat hier niet hoort**: technische ontologie-details (zit in brain-vault + projectinstructie), sprint-protocollen (projectinstructie), patch-rapport-historie (output/-folder).

Bij conflict met projectinstructie: projectinstructie prevaleert (= autoritatieve werkwijze).

---

## 1. Project-essentie in 3 alinea's

Een Nederlandse Rijksoverheidsorganisatie ontwikkelt een **gecentraliseerd GRC Kennismodel** — een formele OWL 2 DL ontologie die alle toepasselijke wet- en regelgeving, normen en best practices integreert. Het fungeert als informatie-laag van het ISMS van de organisatie. Drie tekortkomingen in de huidige compliance-praktijk vormen de aanleiding: BIO-implementatie zonder organisatorische verankering, controls zonder onderliggende risico-analyse, en opeenvolgende compliance-projecten voor inhoudelijk overlappende eisen.

Het model is **framework-neutraal** (D9): alle normen, wetten en kaders zijn gelijkwaardig gemodelleerd als individuals met onderlinge relaties. Geen enkel framework heeft een architecturaal privilege. Voor de operationele toepassing (dashboard, rapportage) wordt BIO 2.0 als primair perspectief gebruikt, omdat het het verplichte operationele kader is voor de Rijksoverheid. Dit is een view-keuze, geen architectuurkeuze.

Per mei 2026 staat het model op v4.5.0 (19.340 pre-inferentie triples, 41.988 post OWL RL, 193 klassen, 1.179 individuals, 1.794 SKOS-mappings, 11 namespaces). Drie framework-clusters geverifieerd: NIS2-EU, CBW-NL, NIST CSF 2.0. Implementatie loopt volgens drie sporen: technische ontologie-opbouw zonder organisatiedata (Spoor A, voltooid t/m v4.5.0), organisatiespecifieke invulling (Spoor B, lab-test T&I pending), gebruik en governance (Spoor C, pending).

---

## 2. Stakeholder-landschap

### Primaire stakeholders

| Stakeholder | Rol in project | Relatie |
|---|---|---|
| **CSO** | Formele projectsponsor | GO op architectuurdocument v1.2 (13 april 2026) gegeven. Strategische escalatie-route. |
| **CISO** | Directe werkrelatie projecteigenaar | Projecteigenaar werkt in directe ondersteuning van CISO. Operationele beslissingen lopen hier doorheen. |
| **Bestuur** | Rapportage-target | Dashboard wordt straks bestuurs-bruikbare interface. Status: nog niet betrokken in detail; visie-laag. |
| **Interne auditafdeling** | Prioriteit-1 gebruiker | Opzet/bestaan/werking met evidence-trail per control. Belangrijke validator van model-bruikbaarheid. |
| **Architecten (enterprise/security)** | Doorbraak-stakeholder | Als referentiekader voor toekomstige solution architectures. Nog niet actief betrokken; pending Spoor B. |

### Secundaire stakeholders

- Compliance- en risico-eigenaren (toekomstig gebruik, Spoor B)
- Ontwikkelaars en applicatieteams (visie-laag, agentic AI-ecosystem)
- Dienstafnemers binnen Rijk (gecontroleerde rapportages, Spoor C)
- Technologie & Innovatie (lab-test als eerste Spoor B-proeftuin)

### Niet-stakeholders (bewust)

- **Geen externe rapportage** naar burgers/markt (intern model)
- **Geen audit-vervanger** (auditor oordeelt op basis van model-evidence, niet model zelf)
- **Geen real-time security monitoring** (SIEM/SOC blijft separaat)
- **Geen DORA-doelgroep** (organisatie valt niet onder DORA; DORA als referentiekader)

### Projecteigenaar — werkprofiel

- **Rol**: GRC-adviseur in directe ondersteuning CISO
- **Domein-expertise**: hoog op GRC-inhoud (wet- en regelgeving, controls, audit-discipline)
- **Technische expertise op ontologie-engineering**: zelf beschreven als "redelijke leek". OWL/SPARQL/SHACL geen primaire vaardigheid; concepten zoals D-decisions/H-items zelf opgebouwd.
- **Communicatiestijl**: voorkeur voor Nederlandse taal, eerlijke pushback, korte antwoorden, structurele opties (A/B/C) bij dilemma's. Werkt vlot, accepteert directe terugkoppeling, vraagt zelf om verheldering bij twijfel.
- **Tijdsbeschikbaarheid**: pragmatisch — wisselt tussen vlot doorpakken en doordachte pauzes. Geen externe deadlines gemeld.

**Niet uitspreken**: de naam van de organisatie blijft buiten alle outputs. Altijd "de organisatie" of "Rijksoverheidsorganisatie". Dit is harde discipline.

---

## 3. Drie-sporen-status

### Spoor A — Technische ontologie-opbouw

**Status**: voltooid t/m v4.5.0 (19 mei 2026). Lopend Fase 4+.

Belangrijkste mijlpalen:
- v3.0 (monolithisch) → v4.0.0 (modulaire split) — april 2026
- v4.2.x (SoA-canonisering, M18 Asset-module) — april 2026
- v4.3.x (gap-sprints, D11 asset-convergentie, D12 drie-laags compliance) — april 2026
- v4.4.0 Fase 2 (CBW + Cbb + UV-decompositie) — 13 mei 2026
- v4.5.0 Fase 3 (NIST CSF 2.0) — 19 mei 2026
- v4.6.0 Fase 4 (M15-ENSIA + volwassenheidsmodel) — pending

### Spoor B — Organisatiespecifieke invulling

**Status**: pending. Lab-test bij Technologie & Innovatie gepland als eerste proeftuin.

Spoor B raakt iets fundamenteels: het model is nu organisatie-neutraal. Bij Spoor B stroomt organisatie-data in. Drie architecturale invarianten worden dan kritiek:

- Geen black-box-AI — alleen uitlegbare AI mag worden ingezet
- Lokaal draaibaar — geen cloud-internet-afhankelijkheid voor productie-toepassingen
- Open-source voorkeur — pragmatisch gegeven Rijksoverheid-aanbestedingstrajecten

Migratie naar Claude Code + GitHub (gepland na v4.6.0) raakt invariant 2 al: GitHub.com is cloud. Acceptabel voor Spoor A; herzien bij eerste Spoor B-stap.

### Spoor C — Gebruik en governance

**Status**: pending. Triplestore + dashboard + beheerproces. Geen actieve werkstroom nu.

Dashboard-chat bestaat sinds v4.0.0, maar is sinds v4.3.1 (20 april 2026) niet meer bijgewerkt. **Vier sprints achterstand**: v4.3.2, v4.3.3, v4.4.0, v4.5.0. Dashboard kent geen csf:-namespace, geen CBW-controls, geen Cbb-individuals, geen 363 Implementation Examples, geen 1.448 nieuwe SKOS-mappings.

Dashboard-inhaalslag staat gepland parallel aan v4.6.0 als niet-blokkerend werk.

---

## 4. Lopende strategische afwegingen (open)

### 4.1 V1 biz: vs isms: voor volwassenheidsmodel (Fase 4)

**Status**: open. Beslissingsmoment: v4.6.0 Stap 2 (drievoudige aanpak).

Originele analyse-rapport Opdracht 1.0 (20 april 2026) koos **V1 Optie B**: nieuwe `isms:MaturityAssessment`-klasse. Maar in m07-business.ttl bestaan al `biz:MaturityAssessment`, `biz:MaturityLevel`, `biz:hasMaturityLevel`, `biz:targetMaturityLevel`, `biz:maturityScore`. Voorkeursbesluit V1 moet hierop opnieuw worden gewogen vóór nieuwe isms:-klasse wordt gedeclareerd.

**Mijn neiging**: biz:-cluster uitbreiden i.p.v. nieuwe isms:-klasse declareren. Reden: hergebruik > duplicatie; biz:-cluster heeft al de juiste domain-modellering. Maar dit is GRC-domeinkennis-vraag (wat is ISMS-volwassenheid semantisch versus business-volwassenheid?) — projecteigenaar beslist.

### 4.2 M19 (ISO 42001 AI) en M20 (ISO 9001)

**Status**: niet in scope fase 1-4. Harmonized Structure (Annex SL) maakt latere toevoeging eenvoudig.

Trigger voor heroverweging: organisatie krijgt concrete AI-systeem-verplichting (ISO 42001) of kwaliteitssysteem-ambitie (ISO 9001). Geen automatische trigger.

### 4.3 ENISA TIG-PDF integratie

**Status**: kandidaat voor v4.5.0+. Property `ext:hasENISAGuidance` is in v4.4.0 hardverwijderd en kan opnieuw gedeclareerd worden bij integratie.

Trigger: Analyse-opdracht 2.0 of expliciete sprint-overweging in v4.6.0+. Tot nu niet geprioriteerd omdat UV-decompositie via CBW-Excel al deels deze rol vervult.

### 4.4 Drie geparkeerde architectuur-aandachtspunten (vereisen Analyse-opdracht 2.0)

- **H29** — Three Lines Model (IIA 2020) als M04-roles-uitbreiding via SKOS
- **H30** — GITC (General IT Controls — ADR-toetsingskader) als auditkader-individual in Laag 5
- **H31** — Toetsingskader Algoritmes (Algemene Rekenkamer) als auditkader-individual in Laag 5

Alle drie wachten op natuurlijke trigger of Spoor B-data.

### 4.5 Niet-formeel-geregistreerde kandidaten

- SP 800-53 → ISO 27001:2013 docx integratie (project knowledge bevat bestand; 2013-versie vereist hercodering naar 2022 via ISO 27002:2022 Annex F)
- BZK/kern-IBO NIS2 ↔ ISO 27002:2022 mapping (digitaleoverheid.nl PDF, november 2023; 2022-conform, Rijksoverheid-relevant)

Beide gevonden in cross-framework-crosswalks-onderzoek (mei 2026). Status "wachten op natuurlijk trigger". Krijgen H36/H37 bij trigger.

### 4.6 Migratie naar Claude Code + GitHub

**Status**: voorbereiding. Volledig gedocumenteerd in `migratie-roadmap.md`.

Korte versie: drie chats migreren na v4.6.0 (Tech/Brein/Dashboard); vier blijven (Master/Documentatie/Analyse/Asset). Vier pre-condities. Bron-architectuur Optie D (publiek-domein in repo; NEN-ISO blijft in claude.ai PK). PAT + export-fallback voor Anthropic bug #33875.

### 4.7 SKOS-kwaliteitsanalyse op 1.794 mappings

**Status**: verhoogde urgentie sinds v4.5.0. Was eerder gepland op 346 baseline; nu 1.794 (5,2× zo veel). Parallel-spoor in Dashboard-chat.

---

## 5. Roadmap-niveau visie voorbij v4.6.0

### Horizon 1 jaar (mei 2027)

- Spoor A volledig (model + alle modules + alle SKOS-kwaliteit)
- Spoor B-eerste-stap: lab-test bij Technologie & Innovatie. Eerste organisatie-data in pilot-modus
- Spoor C beheerproces operationeel: triplestore, beheer-werkstroom

### Horizon 3 jaar (mei 2029)

Conform projectinstructie missie-visie:
- Model gekoppeld aan belangrijke systemen
- Actuele compliance-status per systeem en wet/regelgeving in algemene zin
- Bevraagbaar via meerdere ingangen (dashboard, SPARQL, AI-toepassingen)

### Wens-versie (geen harde toezegging)

- Agentic AI-ecosystem rond het kennismodel met gespecialiseerde toepassingen:
  - Policy-check
  - Compliance-communicatie
  - Ontwikkelaar-ondersteuning bij applicatiebouw
- Twee harde principes blijven:
  - Geen black-box-AI (alleen uitlegbare AI)
  - Lokaal draaibaar (geen cloud-internet-afhankelijkheid voor productie)
- Voorlopige voorkeur open-source voor productie

### Wat dit niet wordt

- Geen real-time SIEM-vervanger
- Geen audit-tool die zelfstandig oordeelt
- Geen extern transparantie-instrument (intern; rapportages aan dienstafnemers via gecontroleerde uitgang)
- Geen risico-management-systeem dat risico-analyses uitvoert (toont uitkomsten + zichtbaar-maken gebreken)
- Geen menselijke-controle-ondermijnende beslissings-suggesties

---

## 6. Masterchat-werkwijze-conventies

Dit zijn werkpatronen die in conversaties zijn gegroeid maar **niet** expliciet in projectinstructie staan. Verwachte continuïteit door opvolger-instances.

### 6.1 Drievoudige aanpak voor grote sprints

Bij sprints die nieuwe klassen/properties/structuren introduceren of significante architectuurkeuzes vereisen:

1. **Stap 1** — Pre-sprint-inventarisatie tech-chat (read-only, gerichte vragen)
2. **Stap 2** — Architectuur-keuzes-overleg masterchat ↔ projecteigenaar (op basis van inventarisatie + bron-feiten)
3. **Stap 3** — Gestructureerde sprint-instructie aan tech-chat (met expliciete besluiten)

Toegepast in v4.4.0 (Fase 2) en v4.5.0 (Fase 3). Heeft scope-pauzes voorkomen.

### 6.2 Routine-controle-tabel aan begin van elke tussenrapport-review

Eerste paragraaf van masterchat-reactie op tussenrapport is een tabel met checks:

```
| Check | Resultaat |
|---|---|
| Triple-Δ +X vs raming +Y | binnen marge ✓ |
| SHACL identiek | ✓ |
| Bilinguale labels | ✓ |
| ... | ... |
```

Doel: snelle objectieve toets vóór inhoudelijke beoordeling. Bij rode vlaggen direct in tabel zichtbaar.

### 6.3 Eerlijke pushback-discipline (intern)

Masterchat erkent eigen fouten expliciet wanneer ze blijken. Voorbeelden in v4.5.0-sprint:
- "Dit is mijn instructie-fout, niet een upload-fout van jou" (csf2.xlsx-format)
- "Dit had ik in pre-sprint-stap moeten anticiperen" (csrc.nist.gov-403)
- "Dit is mijn instructie-fout. Klassieke fout van het type dat sprint-protocol B juist beoogt te voorkomen" (ext:belongsToFramework)

Cultuur: fouten benoemen, niet wegmoffelen. Leerpunten naar projectinstructie. Niet over-apologetisch — concreet wat ging mis en wat erfgenaam moet weten.

### 6.4 Triple-A/B/C-opties-presentatie

Bij scope-pauzes en architectuurkeuzes structureel format:

| Optie | Aanpak | Triple-impact / consequentie |
|---|---|---|
| A | ... | ... |
| B (voorkeur) | ... | ... |
| C | ... | ... |

Voorkeur expliciet met rationale. Projecteigenaar beslist. Geen verborgen aanbevelingen.

### 6.5 Heads-up vs scope-pauze onderscheid

Niet alles vereist masterchat-overleg. Tech-chat-rapportage-patroon:

- **Heads-up**: vermelden in tussenrapport, doorrollen zonder masterchat-GO af te wachten. Voor afwijkingen binnen redelijke marge met voor de hand liggende verklaring.
- **Scope-pauze**: stoppen, rapporteren met opties, wachten op masterchat-GO. Voor architectuurkeuzes, fundamentele afwijkingen, beslissingen die masterchat-domein zijn.

Tech-chat heeft dit onderscheid goed in vingers. Bij twijfel: pauzeren is veiliger dan doorrollen.

### 6.6 Sample-first benadering bij parsing

Bij grote parsing-taken (bv. 145 sheet-rijen, 363 Implementation Examples, 1.238 IR-mappings): eerst sample (eerste 3-5 records of representatieve subset), masterchat-bevestiging op patroon, dan volledige batch. Voorkomt grote re-do-rondes.

### 6.7 "Kwaliteit boven kwantiteit" bij interpretatieve mappings

Bij subjectieve mapping-keuzes (zoals GOVERN-overlap COSO/COBIT in v4.5.0): liever 12 sterke mappings dan 15 zwakke. SKIP-keuze is legitiem. G1-discipline ("bij twijfel niet leggen") geldt ook voor interpretatieve mappings.

### 6.8 Mini-inventarisaties binnen sprints

Bij grote sprints met meerdere bron-bestanden: ingebouwde mini-inventarisaties vóór ABox-werk per nieuwe bron. Voorkomt v4.4.0 Route 5-type instructie-fouten. Toegepast in v4.5.0 Stap 4 + Stap 6.

### 6.9 Verheldering-vragen vóór grote outputs

Bij groot document (handover, projectinstructie, masterchat-instructie): expliciet kort verheldering vragen vóór schrijven. Voorkomt redo-rondes door verkeerde scope-aanname. Gebruikt in handover-document-aanloop (scenario 1+2+3-vraag).

---

## 7. Specifieke afwegingen die niet in D/H zijn geland

Dingen die in conversatie zijn besloten maar nooit als formele D-decision of H-item geregistreerd, omdat ze meer werkwijze-conventies zijn dan ontologie-architectuur.

### 7.1 Triple-stappen-aanpak voor scope-pauzes

Tech-chat-format bij scope-pauze: Diagnose / Drie opties / Feitelijke punten / Tech-chat-voorkeur (presentabel, niet beslissend). Dit format heeft zich uitgekristalliseerd; werkt goed. Niet formeel geregistreerd.

### 7.2 Bron-attribuering via blok-comment i.p.v. per-triple

Bij grote SKOS-mapping-batches: één bron-attribuering-statement per ontologie-module-blok via rdfs:comment, niet per individuele triple. ABox-licht. Toegepast in v4.4.0 Stap 5 + v4.5.0 Stap 5+6. Niet formeel als pattern geregistreerd.

### 7.3 SHA256 in SourceAttribution-attribution-text

Best practice geïntroduceerd in v4.5.0 Stap 2.4 (csf2.xlsx). Voor snapshot-bronnen: SHA256-hash van bron in attribution-text voor reproduceerbaarheid los van canonical_metrics file_hashes. Vermeld in v1.8 maar niet als verplichte regel.

### 7.4 "Wel-aanwezig-buiten-scope"-rapportage

Bij filtering van bron op subset (zoals v4.5.0 sub-keuze C1 met 23 source-prefixes → 3 opgenomen): rest **wel** documenteren in patch-rapport §8 als "wel in bron aanwezig, buiten scope" met counts. Voorkomt vergeten kandidaten bij latere overweging.

### 7.5 Sprint-multiplier-mijlpalen tracking

In v1.8 toegevoegd: tabel van Δ-triples per sprint als multiplier t.o.v. v4.4.0-baseline. Voor toekomstige sprint-planning relevant. Maakt sprint-omvang vergelijkbaar.

### 7.6 Patch-rapport §9-formaat (geparkeerde-items)

Tech-chat heeft dit in v4.4.0 als bonus toegevoegd. v1.7 maakte het verplicht. v1.8 bevestigt + uitbreidt met §9-status-update bij elke release. Geboren uit goede praktijk, geformaliseerd post-hoc.

---

## 8. Pushback-cultuur (verwachting van Master-rol)

Drie expliciete verwachtingen die projecteigenaar herhaaldelijk heeft uitgesproken:

### 8.1 Eerlijk tegenspreken

Onzekerheden labelen. Bij verkeerde scope-keuze van projecteigenaar: direct aankaarten met argumenten, niet alleen volgzaam uitvoeren. Voorbeelden in v4.5.0:

- Sub-keuze C1 versus C2 (Implementation Examples + IR-mappings): masterchat heeft expliciet pushback gegeven op C2 met concrete 7-frameworks-zonder-modellering-consequentie. Projecteigenaar koos uiteindelijk C1.
- COSO_ERM_Performance heroverweging in Stap 7 GOVERN-overlap: masterchat heeft tech-chat-SKIP omgezet naar GO met motivering. Projecteigenaar accepteerde.

### 8.2 Onzekerheden expliciet markeren

Bij raming/inschatting met onzekere basis: "±25% marge", "borderline-mapping", "raming-fout van mij", "had ik moeten zien". Geen pseudo-zekerheid.

### 8.3 Pushback op grote scope-uitbreidingen

Bij voorstel tot grote scope-uitbreiding (zoals C2 in v4.5.0): expliciete schaal-vergelijking met huidige sprint-omvang. 5× v4.4.0 versus 13× v4.4.0 is een wezenlijk verschil dat zichtbaar moet zijn.

---

## 9. Tools + omgevings-context

### 9.1 Huidige claude.ai-omgeving

- **Brain-vault**: ~99 brain__*.md in PK (zie projectinstructie §brain-vault)
- **Bronnen**: ~30+ documenten in PK (PDFs, Excels)
- **Tools**: project_knowledge_search (primair), web_search, web_fetch, bash, view/create_file/str_replace, present_files
- **Memory-system**: userMemories voor cross-chat-staat-behoud. Per 20 mei 2026 bevat ~18 entries.

### 9.2 Beperkingen tegen aan gelopen

- `csrc.nist.gov` niet in tech-chat's allowed_domains → workaround: PK-upload
- `nist.gov` direct ook beperkt → idem
- web_fetch werkt soms wel waar bash niet werkt (verschillende permissions)
- PDF's die "scanned" zijn (zoals NIST CSWP 29) hebben geen extractbare tekst — workaround: project knowledge_search-via-PDF-rendering
- File-uploads via gebruiker verschijnen direct in PK maar zijn niet altijd direct in masterchat-omgeving zichtbaar (sessie-cache-issue) — tech-chat-zijde kan wel direct toegang hebben

### 9.3 Post-migratie-omgeving (na v4.6.0)

Zie `migratie-roadmap.md` voor details. Korte versie:
- Claude Code voor Tech/Brein/Dashboard (lokaal)
- claude.ai voor Master/Documentatie/Analyse/Asset
- GitHub repo als single-source-of-truth voor brain + ontologie + sources
- Steven (= projecteigenaar) als tussenmens bij scope-pauzes Claude Code → claude.ai

---

## 10. Kritieke historische beslissingen (pivots)

Beslissingen die het project op koers hebben gezet of bijgesteld. Belangrijk voor begrip van waar we staan.

### 10.1 Framework-neutraliteit (D9) — 17 maart 2026

Eerder: NIS2 was "primaire driver"; daarna BIO 2.0 als "operationeel uitgangspunt". Beide leverden architectureel scheve modellering op. Per 17 maart: framework-neutraal model met BIO 2.0 alleen als operationeel-toepassings-perspectief.

**Waarom belangrijk**: D9 is harde architectuur-invariant. Bij elke nieuwe framework-toevoeging: respecteer D9. Geen "centraal framework" mag insluipen.

Per v4.4.0 aantoonbaar op 2 clusters (NIS2 + CBW/Cbb). Per v4.5.0 op 3 clusters (NIS2 + CBW/Cbb + NIST CSF). Patroon werkt.

### 10.2 BBN-correctie — 17 maart 2026

Eerder aangenomen: BIO 2.0 kent BBN-niveaus toe aan maatregelen. Werkelijk: BBN komt uit **Handreiking BIO2-opmaat** (transitiedocument) en BIO 1.04, niet uit BIO 2.0 zelf. Handreiking gebruikt alleen BBN 1 en 2 (geen 3).

**Waarom belangrijk**: BIO 2.0 classificeert via ISO 27002-attributen (control-soort, type, CIA, etc.), niet via BBN. Gebruik `ext:hasHandreikingBBN` met waarden 1 of 2.

### 10.3 D11 asset-convergentie — 13 april 2026

Risk-koppeling-nulmeting toonde dat asset: en risk: en isms: drie parallelle werelden waren met 0 bruggen. D11 introduceert owl:sameAs asset:↔risk:↔isms: in ster-patroon (5 bruggen). D5-patroon strikt ctrl:↔bio: behouden.

**Waarom belangrijk**: D5+D11 sameAs-discipline is gevoelig. Niet uitbreiden zonder masterchat-overleg.

### 10.4 D12 drie-laags compliance — 22 april 2026

Drie-laags-architectuur: regulatory obligation / legal obligation / requirement. Patroon, geen starre symmetrie per cluster.

**Toepassings-asymmetrie tussen NIS2 en CBW/Cbb (v4.4.0)**: NIS2 = regulatory→legal→requirement-keten; CBW+Cbb = legal-only-keten (beide LegalObligation, geen regulatory-laag). D12 staat dit expliciet toe — geen modelfout.

### 10.5 Route 5-herdefinitie — 13 mei 2026

Originele aanname: ENISA TIG-tekst in CBW-Excel propagatie naar 73/93 BIO-Controls. Werkelijk: CBW-Excel sheet 3 kolom H is ADR/NOREA's interpretatieve UV-decompositie op CBW-Control-niveau (26 controls). Geen ENISA-tekst in CBW-Excel. Geen propagatie naar BIO-controls in bron.

**Waarom belangrijk**: leerpunt voor "bron-verificatie vóór TBox-declaratie" sprint-protocol. ENISA TIG-PDF blijft als aparte route-kandidaat voor latere sprint.

### 10.6 csf2.xlsx-correctie — 19 mei 2026

Aangenomen: OLIR-snapshot met expliciete relationship-types. Werkelijk: CSF Reference Tool-export met grouped-by-CSF-component-structuur. Drie aanpassingen: rename SourceAttribution, uniform skos:closeMatch, filter op 3 source-prefixes binnen sub-keuze C1.

**Waarom belangrijk**: leerpunt voor "bron-bereikbaarheid in uitvoerings-omgeving" + bron-format-specificatie. Niet alleen URL maar exacte export-variant noemen.

---

## 11. Wat ik op dit moment wel/niet zou doen

Strategisch advies voor opvolger-instance of toekomstige projecteigenaar.

### Wel doen

- **Fase 4 (v4.6.0) afronden vóór migratie**. Migratie tijdens conceptuele sprint = leercurve-risico hoog, baten laag. Wachten op patch-sprint of parallel-spoor als test-periode.
- **Master-handover-document onderhouden** bij belangrijke koers-veranderingen. Niet bij elke iteratie.
- **Drievoudige aanpak gebruiken** bij sprints groter dan ~500 triples. Bij kleinere sprints overkill.
- **Pushback geven** bij verkeerde scope-keuzes — projecteigenaar waardeert dit en verwacht het.
- **Bij twijfel: sprint-protocollen volgen**. Pre-sprint-inventarisatie heeft v4.4.0 + v4.5.0 schoongehouden.

### Niet doen

- **Geen organisatienaam noemen** in outputs. Discipline-fout met grote impact.
- **Geen D-decisions wijzigen** zonder masterchat-overleg. D1-D12 zijn immutable.
- **Geen owl:sameAs uitbreiden** buiten D5 (93 ctrl-bio) en D11 (5 asset-bridges). Strikt gescoped.
- **Geen NEN-ISO-tekst** opnemen in model (licentie-restrictie). Alleen via clausule-referenties.
- **Geen Subagent-configs** schrijven vóór projecteigenaar concrete migratie-GO heeft gegeven.
- **Geen aannames als feiten** rapporteren. Onzekerheden labelen. Bij raming: "±X% marge".

### Bij verwarring eerst

1. Lees brain-vault via `project_knowledge_search` ("brain__index" als start)
2. Lees projectinstructie v1.8 voor werkwijze
3. Lees migratie-roadmap.md voor post-v4.6.0-context
4. Lees dit document voor strategische context
5. Lees recente patch-rapporten in output/-folder voor sprint-realiteit
6. Bij nog steeds verwarring: vraag projecteigenaar om verheldering. Beter een vraag stellen dan verkeerd doorduwen.

---

## 12. Eerste-hulp bij specifieke verwarring

### "Welke sprint is huidige?"

Per 20 mei 2026: v4.5.0 opgeleverd, v4.6.0 in voorbereiding (Fase 4 — M15-ENSIA + volwassenheidsmodel).

### "Wat is de baseline?"

v4.5.0: 19.340 pre-inf / 41.988 post OWL RL / 193 klassen / 1.179 individuals / 146 OP / 94 DP / 98 sameAs / 1.794 SKOS / 11 namespaces. Details in patch-rapport-v4_5_0.md (uploads-folder) + projectinstructie v1.8.

### "Hoe werkt brain-vault?"

~99 brain__*.md bestanden in PK. Pattern: `brain__folder__slug.md` (folders via __-separator: decisions, sprints, architecture, concepts, modules, sources, workflow, scope). Entry-points: brain__index.md + brain__*_register.md per folder + brain__log.md. Bij vragen over project-historie: `project_knowledge_search` met brein-zoekwoorden eerst.

### "Welke chat doet wat?"

| Chat | Rol |
|---|---|
| Master | Strategie, sparring, architectuurbeslissingen |
| Technisch | OWL/SPARQL, scripts, parsing |
| Documentatie | PID, beleid, communicatie |
| Dashboard | Visualisaties, build-pipeline |
| Asset | M18 (afgerond, stand-by) |
| Analyse | Framework-analist, incidenteel |
| Brein | Brain-vault-onderhoud (NIEUW v1.8) |

Architectuurbeslissingen via Master; implementatie via specialistische chats.

### "Wat is de status van X?"

Voor open afwegingen: zie §4 hierboven. Voor module-status: projectinstructie v1.8 §Modules. Voor geparkeerde H-items: projectinstructie v1.8 §Openstaande items.

### "Hoe wordt de organisatie genoemd?"

"De organisatie" of "Rijksoverheidsorganisatie". Nooit de echte naam. Harde discipline.

---

## 13. Verwachting bij chat-restart of vervangende instance

Als deze masterchat-context ooit verloren gaat (claude.ai-chat-restart, migratie, andere reden):

1. **Eerste actie**: lees dit document + projectinstructie v1.8 + migratie-roadmap.md
2. **Tweede actie**: `project_knowledge_search` brain__index.md om brain-vault te verkennen
3. **Derde actie**: bevestig aan projecteigenaar dat handover-context is geladen, vraag of er recent niets-in-deze-documenten gebeurd is
4. **Vierde actie**: hervat normale masterchat-rol

**Niet doen bij restart**:
- Niet doen alsof alle context aanwezig is. Eerlijk: "Ik ben een vervangende instance. Heb [document X] gelezen. Vraag of er recent dingen gespeeld zijn die hier niet in staan."
- Niet hervatten van een specifieke sprint zonder eerst stand-check
- Geen aannames maken over chats die parallel draaien (Tech-chat-stand check bij projecteigenaar)

**Wel doen bij restart**:
- Erken de discontinuïteit eerlijk
- Vraag concrete bevestiging op huidige sprint-staat
- Bij twijfel: vraag eerst, doe later

---

## 14. Wijzigingsgeschiedenis

| Datum | Versie | Wijziging |
|---|---|---|
| 20 mei 2026 | 1.0 | Initiële versie. Opgesteld na v4.5.0-oplevering als verzekeringsbeleid los van migratie-timing. Dekt scenario 1+2+3 (vervangende AI + mens-overdracht + toekomstige projecteigenaar). |

Updates verwacht bij:
- Belangrijke strategische koers-veranderingen (bv. Spoor B-start, V1-besluit)
- Nieuwe stakeholders die actief worden
- Migratie-voltooiing
- Significante visie-aanpassingen

Niet bij elke sprint-oplevering — patch-rapporten + brain-vault dekken dat.

---

**Einde master-handover-document v1.0.**
