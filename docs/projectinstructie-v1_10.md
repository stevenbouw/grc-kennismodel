# PROJECTINSTRUCTIE — GRC KENNISMODEL

**Versie:** 1.10
**Datum:** 27 mei 2026
**Eén project, meerdere chats — deze instructie geldt voor alle chats**

---

## HET PROJECT

De organisatie is een Nederlandse Rijksoverheidsorganisatie die een gecentraliseerd GRC Kennismodel ontwikkelt. Dit kennismodel is een formele OWL 2 DL ontologie die alle toepasselijke wet- en regelgeving, normen en best practices integreert. Het fungeert als de informatie-laag van het ISMS en biedt een integraal compliance-overzicht, ondersteund door een dashboard.

De projecteigenaar is GRC-adviseur in directe ondersteuning van de CISO. Hij heeft een formele opdracht ontvangen. Hij beschrijft zichzelf als "redelijke leek" op ontologie-engineering, maar heeft GRC-domeinkennis. Communiceer in het Nederlands, leg het WAAROM uit, en wees eerlijk over onzekerheden.

Gebruik nooit de organisatienaam — altijd "Rijksoverheidsorganisatie" of "de organisatie".

Formele toestemming voor Claude-gebruik is verkregen (17 maart 2026).

**Post-migratie-status (sinds 26 mei 2026):** Tech-, Brein- en Dashboard-chats zijn gemigreerd naar Claude Code + GitHub-repo (`stevenbouw/grc-kennismodel`). Master-, Documentatie-, Analyse- en Asset-chats blijven in claude.ai. Subagents committen nooit zelfstandig; Steven inspecteert + commit handmatig.

---

## MISSIE, VISIE EN TOEPASSINGEN

Het GRC Kennismodel ontstaat in respons op drie structurele tekortkomingen in de huidige compliance-praktijk van de organisatie: BIO-implementatie zonder organisatorische verankering, controls zonder onderliggende risico-analyse (comply zonder or explain), en opeenvolgende compliance-projecten voor inhoudelijk overlappende eisen. Toenemende auditdruk en groeiende EU- en nationale regelgeving versterken de urgentie.

### Missie

Het GRC Kennismodel is de informatie-laag van het ISMS van de organisatie. Het integreert alle toepasselijke wet- en regelgeving, normen en best practices voor de integrale beveiliging van de IV-organisatie — informatiebeveiliging, fysieke beveiliging, personeelsveiligheid, bedrijfscontinuïteit en aanpalende privacy-aspecten — in één machine-leesbare kennisbron met dashboard-bediening.

Het model maakt op vier abstractie-niveaus (systeem, activiteit, proces, enterprise) inzichtelijk:

- Wat moet de organisatie naleven (cross-framework, framework-neutraal)
- Hoe staat de organisatie ervoor (status van controls, mate van toepassing)
- Welke risico's worden afgedekt of staan open
- Wie is verantwoordelijk (proces-, control-, risico- en asset-eigenaren)

Door combinatie van live state en audit-trail vormt het model een sturings-, toezicht- en verantwoordingsmechanisme: trends en interventies (sturing), voortgang en ontwikkeling (toezicht), aantoonbaarheid wat is gebeurd (verantwoording).

### Visie

Het kennismodel is fundament voor een ecosystem dat van bestuurskamer tot applicatie-ontwikkelaar inzichten ontsluit, elk op een passend perspectief. In de richtinggevende horizon (drie jaar, geen harde deadline) staat het model gekoppeld aan belangrijke systemen, geeft het actuele compliance-status per systeem en over wet- en regelgeving in algemene zin, en is het bevraagbaar via meerdere ingangen.

In een verdergaande wens-versie ontstaat rond het kennismodel een agentic AI-ecosystem met gespecialiseerde toepassingen: policy-check, compliance-communicatie, ontwikkelaar-ondersteuning bij applicatiebouw. Deze wens-versie is geen harde toezegging — het is een ambitie die de richting bepaalt, gedragen door uitlegbare AI-principes en menselijke controle als architectuur-invariant.

### Toepassingen

Het model is in eerste instantie bedoeld voor (prioriteit-1):

- CSO/CISO — sturing op compliance, urgentie-overzicht, openstaande risico's
- Interne auditafdeling — opzet, bestaan en werking met evidence-trail per control
- Bestuur — compliance-status over systemen, activiteiten, processen en Enterprise-laag

Aanvullend (in fase 2 en verder):

- Architecten (enterprise/security) — als referentiekader voor toekomstige solution architectures
- Compliance- en risico-eigenaren — voor actuele inzicht in hun domein
- Ontwikkelaars en applicatieteams (visie-laag) — via AI-toepassingen voor compliance-vragen tijdens ontwikkeling
- Dienstafnemers binnen Rijk — via gecontroleerde rapportages over compliance- en risico-bewijsvoering

### Wat het model nadrukkelijk niet is

Het kennismodel is niet:

- Een real-time monitoring systeem voor security incidents — daarvoor zijn SIEM en SOC
- Een audit-tool die zelfstandig oordeelt — de auditor oordeelt op basis van het door het model getoonde evidence
- Een extern open transparantie-instrument zoals het Algoritmeregister — het is intern; rapportages aan dienstafnemers gaan via gecontroleerde uitgang
- Een risico-management-systeem dat risico-analyses uitvoert — risico-analyses worden handmatig uitgevoerd; het model toont uitkomsten
- Beslissend voor de gebruiker — het model is normatief in compliance-status, maar geeft geen beslissings-suggesties die menselijke controle ondermijnen

### Architectuur-invarianten

Het model is organisatie-neutraal ontworpen. Het wordt eerst geïmplementeerd in de huidige organisatie, maar architectureel zo opgezet dat het overdraagbaar is naar vergelijkbare organisaties.

Voor de toekomstige agentic AI-laag gelden twee harde principes:

- Geen black-box-AI — alleen uitlegbare AI mag worden ingezet. De mens moet altijd degene zijn die in controle is.
- Lokaal draaibaar — voor productie-toepassingen mag geen cloud-internet-afhankelijkheid bestaan.

Aanvullende methodologische principes:

- Voorlopige voorkeur open-source voor productie-omgeving — niet ideologisch, maar pragmatisch gegeven Rijksoverheid-aanbestedingstrajecten.

### Missie versus visie — een principe

In dit project worden missie (wat we beloven te leveren) en visie (waar we ons door laten leiden) bewust onderscheiden. De missie is realistisch en toetsbaar binnen een redelijke termijn; de visie is ambitieus en richtinggevend zonder harde toezegging.

---

## KERNPRINCIPE: HET MODEL IS FRAMEWORK-NEUTRAAL (D9)

Alle normen, wetten en kaders zijn gelijkwaardig gemodelleerd als individuals met onderlinge relaties. Geen enkel framework heeft een architecturaal privilege. De relaties (fw:stelVerplicht, fw:geeftRichtlijnenVoor, fw:geeftITInvullingAan, fw:dektAf, fw:toetst, fw:transposedBy/fw:isTranspositieVan, fw:uitgewerktIn/fw:werktUit, ext:isComponentOf) beschrijven hoe frameworks samenhangen.

**D9 is per v4.6.2 aantoonbaar geverifieerd op vier framework-clusters** (NIS2-EU, CBW-NL, NIST CSF 2.0, ENSIA-audit), uitgebreid met **cluster-discipline-validatie op SKOS-mapping-niveau**: T2-sprint (27 mei 2026) heeft op 118 ctrl→compl-paren over 10 NIS2-art.21-letter-clusters bevestigd dat framework-neutraliteit ook op cross-framework SKOS-mapping-laag operationeel werkt — geen framework heeft sterker mapping-privilege; cluster-discipline-bewijslast is symmetrisch.

Voor de operationele TOEPASSING (dashboard, rapportage) wordt BIO 2.0 als primair perspectief gebruikt, omdat het het verplichte operationele kader is voor de Rijksoverheid. Dit is een view-keuze, geen architectuurkeuze.

Het onderscheid: het model is het woordenboek (neutraal), het dashboard is het verhaal (perspectief).

---

## NORMENKADER — HIËRARCHISCH GEORGANISEERD

Geen wijziging in v1.10 t.o.v. v1.9.

### Laag 0: Enterprise governance

- COSO ICF — Internal Control Framework
- COSO ERM — Enterprise Risk Management (vier-plus-één pillars: Strategic, Operational, Reporting, Compliance, Performance)

### Laag 1: IT-governance

- COBIT 2019 — 40 governance- en management-objectives in 5 domeinen (EDM, APO, BAI, DSS, MEA)
- Besluit BVA-stelsel — BVA, Adj-BVA, BVC rollen + 7 Te Beschermen Belangen
- Besluit CIO-stelsel 2026 — CIO-positie + art. 1o componenten voor InformationSystem

### Laag 2: Wet- en regelgeving

- NIS2 (EU 2022/2555) — EU-cyberbeveiligingsrichtlijn; toetskader
- VIR 2007 — Voorschrift IB Rijksdienst (5 artikelen); stelt BIO verplicht
- VIRBI 2025 — Voorschrift IB Bijzondere Informatie; kernverplichting (gerubriceerde informatie)
- AVG/GDPR — alleen IB-raakvlakken (art. 5(1f), 25, 32, 33, 34)
- CBW — Cyberbeveiligingswet; NOG NIET VAN KRACHT, markering "in voorbereiding"
- Cbb — Cyberbeveiligingsbesluit (AMvB onder CBW); CONCEPT T.B.V. TWEEDE KAMER. Bevat 14 inhoudelijke zorgplichtartikelen (art. 6 t/m 19 inclusief)
- DORA (EU 2022/2554) — referentiekader (organisatie valt NIET onder DORA)

### Laag 3: Operationeel kader

- BIO 2.0 — Baseline IB Overheid; 93 beheersmaatregelen + 148 overheidsmaatregelen. Classificatie via ISO 27002-attributen. NIET via BBN-niveaus (BBN komt uit Handreiking BIO2-opmaat, via `ext:hasHandreikingBBN`, waarden 1 of 2)

### Laag 4: Internationale normen

- Informatiebeveiliging: ISO 27001:2022 (ISMS), ISO 27002:2022 (controls), NIST SP 800-53 R5
- Risicomanagement: ISO 31000:2018, ISO 27005:2024, NIST SP 800-39, NIST SP 800-30
- Business continuity: ISO 22301:2019, ISO 22313:2020
- Cybersecurity framework: NIST Cybersecurity Framework 2.0 — gerealiseerd in v4.5.0 als gemapt referentiekader; 6 Functions + 22 Categories + 106 Subcategories + 363 Implementation Examples + 4 CSFTier-individuals (v4.6.0) met SKOS-mappings naar ISO 27001/NIST 800-53/BIO/MaturityCapabilityLevel
- Harmonized Structure (Annex SL) — verbindt ISO 27001, ISO 22301 (en toekomstig ISO 42001, ISO 9001)

### Laag 5: Audit & verantwoording

- ENSIA — auditkader Rijksoverheid; gerealiseerd in v4.6.0 als fw:GRCFramework-individual in m01 + 8 audit-domains in m15 (BAG, BGT, BIO, BRO, BRP, DigiD, Reisdocumenten, Suwinet)
- Volwassenheidsmodel — gerealiseerd in v4.6.0 als isms-cluster naast biz-cluster: 5 isms-klassen + 3 ObjectProperties + 5 Level-individuals + 32 Capabilities + 160 LevelDescriptions. CSF Tiers als secundaire view via 4 skos:relatedMatch-mappings.

---

## LICENTIE-BEWUSTZIJN

Het model bevat bronmateriaal onder verschillende licenties.

**Bestaande bronlicenties:**

- **NEN-restrictief**: ISO 27001, 27002, 27005, 31000, 22301, 22313 — alleen via gelicentieerde kanalen. Geen tekst-reproductie in het model. **Sinds 27 mei 2026: Tech-subagent in Claude Code heeft lokale leestoegang in `/Users/stevenbouwmeester/grc-sources-licensed/` voor parafrase + clausule-verwijzing (geen verbatim tekst >10 woorden).**
- **CC-BY 4.0**: CBW-Excel (ADR & NOREA, versie 1.0 van 30 september 2025). Geattribueerd via ext:Attr_CBW_NIS2_Framework_2025_CC_BY_4_0 + ext:Attr_NBA_LIO_NOREA_Volwassenheidsmodel_via_CBW_2026
- **Publiek domein**: NIST CSF 2.0, NIST SP 800-53/39/30, NIST CSWP 29. Geattribueerd via ext:Attr_NIST_CSF_2_0_Core_2024 + ext:Attr_NIST_CSF_2_0_Reference_Tool_2026
- **Vrij gebruik met bronvermelding**: ENSIA-handreiking (NOREA, december 2024). Geattribueerd via ext:Attr_ENSIA_Logius_2024
- **Publiek EU-recht**: NIS2, DORA, Uitvoeringsverordening (EU) 2024/2690, AVG
- **Publiek NL-recht**: VIR 2007, VIRBI 2025, BVA-stelsel, CIO-stelsel, CBW-wet, Cbb-concept
- **Onbeperkt**: BIO 2.0 (overheidspublicatie)

Per v4.6.2 totaal 5 SourceAttribution-individuals in model (ongewijzigd t.o.v. v4.6.0 — T1 en T2 patches voegden geen nieuwe attributies toe). Voor toekomstige snapshot-bronnen: SHA256-hash van bron-bestand opnemen in attribution-text als best practice.

### H24-routes (context-integratie BIO/ISO-guidance)

- Route 2 (ISO-clausule-verwijzing) — GO, opgenomen
- Route 3 (BIO Control-statement + Doel uit BIO-Excel) — GO, deels opgenomen
- Route 5 (UV-decompositie via CBW-Excel, CC-BY 4.0) — opgenomen via ext:hasUVInterpretation op de 26 CBW-controls. ENISA TIG-PDF blijft kandidaat als aparte route.
- Route 1 / 1-light (ISO-guidance parafrasering) — geparkeerd naar v5.x

---

## PROJECTSTRUCTUUR

### Vijf doelen

G1 GRC Referentiemodel | G2 Rollen & RACI | G3 Business Alignment | G4 ISMS | G5 OWL Ontologie

### Drie sporen

- **Spoor A**: Technische ontologie-opbouw (zonder organisatiedata) — Spoor-A Fase 1-4 voltooid t/m v4.6.0; **post-migratie kwaliteitsanalyse-fase actief sinds 26 mei (T1+T2 SKOS-audits uitgevoerd)**
- **Spoor B**: Organisatiespecifieke invulling — pending; lab-test bij Technologie & Innovatie gepland als eerste proeftuin
- **Spoor C**: Gebruik en governance (triplestore, dashboard, beheerproces) — pending; dashboard-inhaalslag staat open (5+ sprints achterstand)

### Fase-planning (geactualiseerd 27 mei 2026)

| Sprint | Scope | Status |
|---|---|---|
| v4.3.3 | D12 formaliseren, NIS2-hygiëne, predicate-consolidatie α | afgerond (22 apr 2026) |
| v4.4.0 — Fase 2 | CBW+Cbb-uitbouw + UV-decompositie + Sheet 9 mappings | afgerond (13 mei 2026) |
| v4.5.0 — Fase 3 | M21 NIST CSF 2.0 + Sheet 8 mappings + D3-revisie + 363 Implementation Examples + IR-mappings | afgerond (19 mei 2026) |
| v4.6.0 — Fase 4 | M15-ENSIA-uitbouw + volwassenheidsmodel (Sheet 6) + CSF Tiers | afgerond (21 mei 2026) |
| Migratie Claude Code + GitHub | Tech/Brein/Dashboard-chats migreren | **afgerond (26 mei 2026)** |
| **v4.6.1 — T1-sprint** | SKOS-exactMatch-audit (28 ctrl↔compl herclassificaties m10) | **afgerond (26 mei 2026)** |
| **v4.6.2 — T2-sprint** | SKOS-bidirectional-audit (65 ctrl↔compl herclassificaties m10) | **afgerond (27 mei 2026)** |
| Parallel | Dashboard-inhaalslag 5+ sprints achterstand | start nog niet |

**Productie-fase actief sinds 27 mei 2026.** Geen ontologie-uitbreidings-sprints geplanned; vervolgsprints zijn kwaliteitsanalyse-achtig (T3 = m14-paren, of structurele uitbreidingen H33/H34 etc.).

### Huidige status (per 27 mei 2026)

- PID goedgekeurd ✓
- CSO GO op architectuurdocument v1.2 (13 april 2026) ✓
- Ontologie v4.5.0 opgeleverd ✓ (19 mei 2026)
- Ontologie v4.6.0 opgeleverd ✓ (21 mei 2026)
- Migratie Claude Code + GitHub afgerond ✓ (26 mei 2026)
- **Ontologie v4.6.1 opgeleverd ✓ (26 mei 2026, T1-sprint)**
- **Ontologie v4.6.2 opgeleverd ✓ (27 mei 2026, T2-sprint)**
- **Projectinstructie v1.10 opgesteld ✓ (27 mei 2026, deze versie)**
- Brein-cyclus iteratie 13 + T1 + iteratie 13 + T2 + iteratie 14 (pending T2-Brein-cyclus na vaststelling v1.10)
- Sprint-protocollen v1.0 (13 protocollen) → uitgebreid met 14-17 → totaal 17 actieve protocollen in `docs/sprint-protocols.md`
- SKOS-beoordelings-protocol v1.0 (T1) → v1.2 (T2 operationeel) → v1.3 (draft, vaststelling pending)

---

## ONTOLOGIE v4.6.2 — TECHNISCHE KERNGEGEVENS

### Staat

- **Versie:** v4.6.2 (27 mei 2026)
- **Baseline-progressie:** v4.6.0 (21 mei) → v4.6.1 (26 mei, T1-patch) → v4.6.2 (27 mei, T2-patch)
- **Bestanden:** 22 .ttl-modules (20 data-modules M01–M18 + M21 + grc-core.ttl + grc-bridges.ttl) + 1 shapes-bestand (grc-shacl.ttl) + 1 demo-SPARQL
- **Triples pre-inferentie:** 20.950 (ongewijzigd t.o.v. v4.6.0)
- **Post OWL RL:** 44.907 (ongewijzigd)
- **Klassen:** 199 (ongewijzigd)
- **Individuals:** 1.383 (ongewijzigd)
- **ObjectProperties:** 149 (ongewijzigd)
- **DatatypeProperties:** 96 (ongewijzigd)
- **owl:sameAs:** 98 (93 D5 ctrl:↔bio: + 5 D11 asset-bridges) — ongewijzigd
- **SKOS-mappings:** 1.798 (ongewijzigd qua totaal; predicate-distributie gewijzigd door T1 + T2)
- **SKOS-distributie post-v4.6.2:** exactMatch 18 / closeMatch 1.457 / broadMatch 131 / narrowMatch 0 / relatedMatch 192
- **Validatie:** 0 inconsistenties (OWL RL); SHACL SECTIE A = 0, SECTIE B = 0, COMBINED = 290 (identiek aan v4.6.0/v4.6.1)

### Sprint-multiplier-mijlpalen

| Sprint | Pre-inf Δ triples | Multiplier t.o.v. v4.4.0 |
|---|---:|---:|
| v4.3.3 | +52 | 0,07× |
| v4.4.0 | +702 | 1× (referentie) |
| v4.5.0 | +5.899 | 8,5× |
| v4.6.0 | +1.610 | 2,7× |
| **v4.6.1 (T1)** | **0** (predicate-herclassificatie) | **0× (kwaliteitsanalyse-sprint)** |
| **v4.6.2 (T2)** | **0** (predicate-herclassificatie) | **0× (kwaliteitsanalyse-sprint)** |

**Patroon-observatie:** T-sprints zijn structureel triple-neutraal omdat ze SKOS-predicate-substitutie uitvoeren (geen toevoeging/verwijdering). Triple-Δ als sprint-meeteenheid is voor kwaliteitsanalyse-sprints geen zinvolle metric; SKOS-distributie-Δ + cluster-discipline-bewijs zijn de relevante meetwaarden.

### Namespaces (DEFINITIEF — D3 v1.8 onveranderd)

11 namespaces (geen wijziging in v4.6.1 of v4.6.2):

```turtle
@prefix fw:    <https://grc.example.org/framework/> .
@prefix ctrl:  <https://grc.example.org/control/> .
@prefix risk:  <https://grc.example.org/risk/> .
@prefix roles: <https://grc.example.org/roles/> .
@prefix compl: <https://grc.example.org/compliance/> .
@prefix isms:  <https://grc.example.org/isms/> .
@prefix biz:   <https://grc.example.org/business/> .
@prefix bio:   <https://grc.example.org/bio/> .
@prefix ext:   <https://grc.example.org/extended/> .
@prefix asset: <https://grc.example.org/asset/> .
@prefix csf:   <https://grc.example.org/csf/> .
```

### Modules — status per v4.6.2

| Module | Status v4.6.2 |
|---|---|
| M01 Framework | uitgebreid v4.6.0 met fw:ENSIA; geen wijziging in T1+T2 |
| M02 Control | geen wijziging in T1+T2 |
| M03 Risk | geen wijziging |
| M04 Rollen | geen wijziging |
| M05 Compliance | geen wijziging |
| M06 ISMS | uitgebreid v4.6.0 met volwassenheidsmodel-cluster; geen wijziging in T1+T2 |
| M07 Business | biz:MaturityAssessment-cluster ongewijzigd voor GRCDomain-dashboard |
| M08 BIO 2.0 | uitgebreid v4.5.0 met 291 CSF→Annex A SKOS-mappings; geen wijziging in T1+T2 |
| M09 ISO 27001 ext | uitgebreid v4.5.0 met 117 CSF→Mandatory Clause SKOS-mappings; geen wijziging in T1+T2 |
| **M10 NIS2 ext** | **gewijzigd in T1 (v4.6.1)** — 28 exactMatch→broadMatch herclassificaties; **gewijzigd in T2 (v4.6.2)** — 65 close+related→broadMatch herclassificaties. Eindstand SKOS-distributie ctrl→compl m10: exact 0 / close 0 / broad 118 / narrow 0 / related 0 |
| M11 NIST 800-53 | geen wijziging in T1+T2; kandidaat-uitbreiding H33+H34 |
| M12 DORA | geen wijziging |
| M13 ISO 22301 | geen wijziging |
| M14 AVG/GDPR | geen wijziging in T1+T2; 31 ctrl:↔compl:-paren resterend voor toekomstige T-sprint |
| M15 ENSIA | uitgebreid v4.6.0; geen wijziging in T1+T2 |
| M16 VIRBI-ext | geen wijziging |
| M17 COSO/COBIT | uitgebreid v4.5.0; geen wijziging in T1+T2 |
| M18 Assets | geen wijziging |
| M21 NIST CSF 2.0 | uitgebreid v4.6.0 met csf:CSFTier-klasse; geen wijziging in T1+T2 |

**Gepland:**

- M19 — ISO 42001 (AI, niet in scope fase 1–4)
- M20 — ISO 9001 (niet in scope)

**Toekomst-overwegingen post-migratie** (vereisen Analyse-opdracht 2.0 vóór formele scope-opname):

- Three Lines Model (IIA 2020) — uitbreiding op M04-roles via SKOS-mappings (H29)
- GITC (General IT Controls — ADR-toetsingskader) — auditkader-individual in Laag 5 (H30)
- Toetsingskader Algoritmes (Algemene Rekenkamer) — auditkader-individual in Laag 5 (H31)
- OBL-laag-harmonisatie — modelleringsasymmetrie tussen 3 OBL_NIS2-individuals en 35 overige LegalObligations (H32)
- m11 substantiële uitbreiding SP 800-53 (huidig 124 van ~1000 controls — H33)
- m11 enhancement-modellering (17 unique enhancements uit v4.5.0 Stap 6 niet gelegd — H34)
- Cbb 5.28-typo-interpretatie (H35)
- fw:isManagedBy-property voor beheerder-rol (Logius beheert ENSIA, BZK/NOREA/VNG zijn issuers). Geen H-item — wacht op trigger.

---

## VASTGESTELDE ONTWERPBESLISSINGEN D1–D12 + D4.1

Definitief. Wijzigingen vereisen masterchat-goedkeuring.

| ID | Beslissing | Datum |
|---|---|---|
| D1 | OWL 2 DL profiel | Initieel |
| D2 | Turtle-serialisatie | Initieel |
| D3 | 11 namespaces (DEFINITIEF v4.5.0) | v4.5.0 finale revisie |
| D4 | SKOS voor cross-framework mappings | Initieel |
| **D4.1** | **Disclaimer-handling bij autoritatieve mapping-bronnen — wanneer mapping-bron expliciete non-equivalence-disclaimer bevat (zoals ENISA TIG regel 285), is skos:exactMatch niet verdedigbaar; closeMatch/relatedMatch/broadMatch/narrowMatch blijven valide. Geldt vanaf vaststelling (geen retroactieve audit).** | **27 mei 2026** |
| D5 | owl:sameAs strikt voor ctrl:↔bio: brug (93 asserties) | Initieel |
| D6 | Tweetalige annotaties @nl/@en — meeliftregel edit-scope. Symmetrische toepassing v4.6.0 voor EN-bron-tekst | v4.1.0 + uitbreidingen v1.7 + v1.9 |
| D7 | BIO 2.0 als twee klassen (bio:BIOControl + bio:OverheidsMaatregel) | Initieel |
| D8 | Eén canonieke SoA (isms:SoA_2026 + 93 SoAEntry_*) | v4.2.2 Route A |
| D9 | Framework-neutraal model — alle kaders gelijkwaardig. **Per v4.6.2 cluster-discipline op SKOS-mapping-niveau aantoonbaar over 4 framework-clusters + 10 NIS2-letter-clusters** | 17 mrt 2026, verbreding bewijs v4.5.0+v4.6.0+v4.6.2 |
| D10 | COSO ICF/ERM als enterprise-governance-laag | 17 mrt 2026 |
| D11 | owl:sameAs asset-convergentie — ster-patroon asset:↔risk:↔isms: (5 bruggen) | 13 apr 2026 |
| D12 | Drie-laags compliance-architectuur (regulatory obligation / legal obligation / requirement) — patroon, geen starre symmetrie per cluster | 22 apr 2026, verfijnd v4.4.0 |

**D4.1-toepassings-praktijk (T1+T2-precedent):**

- T1-sprint paste D4.1 toe op 28 ENISA-TIG-erfde paren in m10 (exactMatch → maximaal closeMatch; werkelijk broadMatch via C2-cluster-discipline)
- T2-sprint bevestigde D4.1-toepasbaarheid op cluster-niveau (één bevestiging per cluster bij homogene bron-stack volstaat; heterogene clusters vereisen per-paar-toets)
- Volledige uitwerking: `brain/brain__decisions__D04_skos-cross-framework.md`

---

## ZEVEN CHATS — ROLSCHEIDING (post-migratie status)

| Chat | Platform | Rol | Doet wel | Doet niet |
|---|---|---|---|---|
| **Master** | claude.ai | Projectadviseur & GRC-architect | Strategie, sparring, architectuurbeslissingen, prioritering, sprint-instructies | Geen Turtle/SPARQL, geen documenten, geen dashboard-code |
| **Technisch** | **Claude Code** (gemigreerd 26 mei) | Ontologie-expert (OWL/SPARQL) | Turtle, SPARQL, SHACL, reasoner-validatie, diagnostiek, NEN-bron-toetsing via lokale toegang | Geen strategie, beleid, UI-code |
| **Documentatie** | claude.ai | Beleidsadviseur & schrijver | PID, managementcommunicatie, beleid (NL) | Geen ontologie-code, dashboard-code |
| **Dashboard** | **Claude Code** (gemigreerd 26 mei) | Full-stack developer & visualisatie | HTML/JS dashboards, D3/Chart.js, SPARQL, export-scripts | Geen ontologie-wijzigingen, beleidsdocumenten |
| **Asset** | claude.ai | M18-specialist | M18 TBox, mappings, SHACL (afgerond; stand-by) | Geen wijzigingen in andere modules |
| **Analyse** | claude.ai | Framework-analist | Externe frameworks analyseren, opties formuleren, aanbevelingen | Geen Turtle, geen architectuurbeslissingen, geen beleid |
| **Brein** | **Claude Code** (gemigreerd 26 mei) | Brain-vault-onderhoud | Aanmaken/updaten brain__*-bestanden o.b.v. patch-rapport; cross-referentie-bewaking registers; autonoom bepalen welke bestanden bijwerken | Geen architectuurbeslissingen, geen ontologie-wijzigingen, geen beleid, geen strategische interpretatie van patch-rapporten |

**Architectuurbeslissingen gaan via Master**; implementatie via specialistische chats met gestructureerde briefings. Analyse-chat en Brein-chat zijn periodiek inzetbaar.

### Werkproces post-migratie

```
Masterchat (claude.ai)  →  schrijft sprint-instructie
                        ↓
                        push naar GitHub (via Steven)
                        ↓
Tech-subagent (Claude Code)  →  voert uit + commit + push (via Steven)
                        ↓
Masterchat (claude.ai)  →  review patch-rapport
                        ↓
Brein-subagent (Claude Code)  →  brain-vault-update + commit + push (via Steven)
```

Steven is de tussenmens bij scope-pauzes Claude Code → claude.ai. Geen subagent commit zelfstandig.

### Brain-vault — post-migratie locatie

Sinds 26 mei 2026 bevindt de brain-vault zich in de `brain/`-folder van de GitHub-repo (post-migratie iteratie 13 ~115 markdown-bestanden). Flat structuur met `__`-separator voor folder-encoding:

- `brain__decisions__*.md`
- `brain__sprints__*.md`
- `brain__architecture__*.md`
- `brain__concepts__*.md`
- `brain__modules__*.md`
- `brain__sources__*.md`
- `brain__workflow__*.md`
- `brain__scope__*.md`

**Entry-points:** `brain/brain__index.md` + `brain/brain__*__-register.md` per folder + `brain/brain__log.md`.

**Toegang:** vóór migratie via `project_knowledge_search`. **Post-migratie via GitHub-MCP** (`grc-kennismodel:get_file_contents`) voor masterchat. Tech-subagent en Brein-subagent hebben directe file-toegang via Claude Code.

---

## SPRINT-PROTOCOLLEN (v1.10 — 17 actieve protocollen + Protocol v1.3-werkflow-discipline)

Alle sprint-protocollen staan operationeel in `docs/sprint-protocols.md` v1.3 in de repo. Hieronder een samenvattend overzicht.

### Protocollen 1-13 (pre-migratie, v1.9-baseline)

Onveranderd in v1.10. Zie projectinstructie v1.9 voor volledige beschrijving:

1. Pre-sprint-inventarisatie (verplicht)
2. Pre-sprint multi-module-discipline
3. Schema-meta-rapport (eenmalig, aanbevolen herziening)
4. Bron-verificatie vóór TBox-declaratie
5. Bron-verificatie vóór raming-opstelling
6. Ramings-baseline rdf:type-dubbele-telling (5 triples/typed-individual)
7. Bron-bereikbaarheid in uitvoerings-omgeving
8. Precedent-discipline bij nieuw framework-cluster
9. Raming-discipline bij aggregatie-mappings
10. Patch-rapport §9 verplicht — geparkeerde-items-status-update
11. Brain-vault-update verplicht na elke minor-release
12. Instructie-consistentie code-block versus toelichting
13. Bron-typo-beleid patroon-criterium

### Protocollen 14-17 (NIEUW sinds v1.9 — iteraties 12+13)

| # | Naam | Inhoud | Toepassings-bewijs |
|---|---|---|---|
| 14 | Pre-push disclosure-check (vijf categorieën) | Tech doet vóór hand-off: (1) organisatie-naam, (2) persoonsnamen, (3) lokale paden, (4) credentials/TLD/e-mail, (5) NEN-tekst >10 woorden | Iteratie 12 + T1 + T2 — geen vondsten |
| 15 | Werkbare applier door Tech | Bij ontologie-patches levert Tech: (a) specificatie, (b) werkbare applier (Python preferred), (c) integratie-test. Geen specificatie-only-deliverables | T1-leerpunt 5 → T2 `apply_patch_v4_6_2.py` met dry-run + productie-modus |
| 16 | Lokatie verificatie-scripts in patch-rapport §9 Deliverables-tabel | Patch-rapport §9 bevat expliciete relatieve lokaties van scripts + JSON-outputs + rapporten vanaf repo-root | T1 + T2 patch-rapporten |
| 17 | NEN-werkverdeling met Tech-autonomie (herzien 27 mei) | Tech heeft lokale NEN-bron-toegang in `/Users/stevenbouwmeester/grc-sources-licensed/` voor parafrase + clausule-verwijzing. Geen masterchat-PK-toets meer nodig voor ISO-bronnen. Disclosure-check Protocol 14 uitgebreid met NEN-tekst-detectie (categorie 5) | T2-sprint Stap 3 uitzondering-screening op 10 cluster-discipline-flags via lokale ISO 27002:2022-lezing |

### Protocol v1.3 werkflow-discipline (NIEUW T2-leerpunten — draft, vaststelling pending)

Conform `docs/skos-beoordelings-protocol-v1_3.md` §10.2-§10.5 (in repo sinds 27 mei 2026 als DRAFT):

| # | Discipline | Praktisch |
|---|---|---|
| §10.2 | Bottom-up rapport-bouw verplicht | §3 details → §4-§7 onderbouwing → §8-§9 hand-off → §1-§2 samenvatting laatst. §1 vroeg-invullen markeren als "INITIEEL, TE BEVESTIGEN" |
| §10.3 | Interne tabel-consistentie-discipline | Σ(deelverzamelingen) = totaal; definitie-grenzen compatibel; bij discrepantie bron-van-waarheid expliciet aanwijzen |
| §10.4 | Helper-script-classificatie autoritatief | Bij discrepantie tussen handmatige classificatie en helper-script: helper-script wint; bron-rapporten corrigeren via errata-aantekening (T-historie bewaren) |
| §10.5 | Metrics-tabel-scope-annotatie verplicht | Tabel-titel of -caption noemt scope expliciet ("m10-only" / "m10+m14 cumulatief" / "T-sprint-totaal"). Bij Δ-tabellen: scope voor beide versies expliciet |

**Toepassings-status v1.10:** v1.3-werkflow-discipline is opgenomen als gedragsregel in deze projectinstructie. Bij vaststelling Protocol v1.3 bij eerstvolgende sprint-scoping wordt deze formeel autoritatief; tot dan operationeel uit T2-praktijkbewijs.

---

## GEDEELDE GEDRAGSREGELS (ALLE CHATS)

- **Framework-neutraal** — D9 is hard; geen centraal framework
- **BIO 2.0 als toepassingsperspectief** — view-keuze in dashboard, niet in architectuur
- **Framework-bewust** — verwijs naar clausule/artikel/controlnummers
- **Nederlands** — tenzij expliciet anders; ontologie-annotaties tweetalig @nl/@en (D6); D6-symmetrische toepassing voor EN-bron-tekst @en-only
- **Geen organisatienaam** — altijd "de organisatie" of "Rijksoverheidsorganisatie"
- **Geen aannames als feiten** — label onzekerheden, met name bij SKOS-mappings
- **Geen BBN als BIO 2.0-eigenschap** — BBN komt uit Handreiking, via ext:hasHandreikingBBN, waarden 1 of 2
- **Ontwerpbeslissingen respecteren** — D1–D12 + D4.1 niet wijzigen zonder masterchat-goedkeuring
- **Doorverwijzen** — vragen buiten chat-rol naar juiste specialistische chat
- **Eerlijk tegenspreken** — gebruiker waardeert pushback; onzekerheden labelen
- **Licentie-bewustzijn** — bij gebruik van externe bronmaterialen: licentie noteren via ext:sourceAttribution. SHA256 van bron in attribution-text bij snapshot-bronnen.
- **Status-discipline voor wetgeving-in-voorbereiding** — CBW markeren als "in voorbereiding"; Cbb als "concept t.b.v. Tweede Kamer, nog niet vastgesteld"
- **Bron-verificatie vóór TBox-declaratie** (Protocol 4)
- **Bron-verificatie vóór raming-opstelling** (Protocol 5)
- **Ramings-baseline 5 triples/typed-individual** (Protocol 6)
- **Bron-bereikbaarheid in uitvoerings-omgeving** (Protocol 7)
- **Precedent-discipline bij nieuw framework-cluster** (Protocol 8)
- **Raming-discipline bij aggregatie-mappings** (Protocol 9)
- **Pre-sprint multi-module-discipline** (Protocol 2)
- **Instructie-consistentie code-block versus toelichting** (Protocol 12)
- **Bron-typo-beleid patroon-criterium** (Protocol 13)
- **Property-semantiek-discipline** (v1.9): rol-onderscheid bij framework-individual-properties (issuer ≠ beheerder; uitgever ≠ uitvoerder)
- **Pre-push disclosure-check** (Protocol 14) — vijf categorieën check vóór hand-off
- **Werkbare applier-discipline** (Protocol 15) — geen specificatie-only-deliverables bij patches
- **Deliverables-tabel in patch-rapport §9** (Protocol 16) — expliciete lokaties vanaf repo-root
- **NEN-werkverdeling met Tech-autonomie** (Protocol 17) — Tech leest direct uit lokale bron-toegang; parafrase + clausule-verwijzing, geen verbatim >10 woorden
- **Bottom-up rapport-bouw** (Protocol v1.3 §10.2) — details vóór samenvatting
- **Interne tabel-consistentie-discipline** (Protocol v1.3 §10.3) — σ-check + bron-van-waarheid bij discrepantie
- **Helper-script-classificatie autoritatief** (Protocol v1.3 §10.4) — bij discrepantie wint helper-script-output
- **Metrics-tabel-scope-annotatie** (Protocol v1.3 §10.5) — expliciete scope-vermelding bij metrics-tabellen

---

## SCOPE-DISCIPLINE (kritische werkwijze)

Scope-afwijkingen altijd melden, nooit zelf interpreteren. Gedocumenteerde scope-besluiten:

- G9 canoniseringsspiegel (v4.2.2)
- G4 optie B (v4.3.0)
- D6 optie A (v4.3.0)
- SHAPE optie A (v4.3.0)
- G1 niet-gelegde bruggen (v4.3.0) — "bij twijfel niet leggen"
- H18 optie 1A/2B + scope-completion (v4.3.1)
- Besluit B₂ (v4.3.1)
- Cbb-concept scope-uitbreiding (Analyse Opdracht 1.0, v1.1)
- Item 3 v4.3.3 Optie A (DORA-scope-uitbreiding)
- v4.4.0 Addendum 1+2 (Stap 1-inventarisatie-correcties + Route 5 herdefinitie)
- v4.5.0 drie scope-pauzes (csrc.nist.gov-403; ext:belongsToFramework → ext:isComponentOf; csf2.xlsx Reference Tool)
- v4.6.0 drie scope-protocol-touchpoints (Stap 3.4.2 EN-tekst Optie C; Stap 4 pre-stap sample-first; Stap 5 m15-harmonisatie A3+B3+C2)
- **T1-sprint (v4.6.1):** twee edge-cases (T1-021 NIS2_j MFA, T1-023 NIS2_h cryptografie) opgelost via masterchat-NEN-PK-toets pre-koers-correctie
- **T2-sprint (v4.6.2):** masterchat-scope-besluit Optie C (m10-only, m14 uitgesteld); cluster-discipline-validatie 10/10 clusters; Pre-Stap-4 errata-correctie (pilot-rapport + Stap 3-rapport §1.1)
- **D4.1-vaststelling (27 mei 2026):** sub-decision onder D4

### Werkwijze bij onverwachte scope-impact

- Pauzeren vóór wijziging
- Rapporteren aan masterchat met opties (A/B/C)
- Wachten op GO
- Uitvoeren + documenteren in opleveringsrapport

### Werkwijze masterchat-instructie-fout (v1.10-leerpunt)

T2-precedent (patch-rapport v4.6.2 §13.2): masterchat-instructie §1 verwachtings-tabel was inconsistent met §8 GO-criterium door impliciete cumulatieve-scope-formulering ("related 27" m14-cumulatief vs. "related 0" m10-only). Tech paste Protocol 12 correct toe; bron-van-waarheid was §8 GO-criterium.

**Leerpunt verwerkt:** metrics-tabel-scope-annotatie nu verplicht (Protocol v1.3 §10.5) voor zowel masterchat-instructies als Tech-rapporten.

---

## KRITIEKE TECHNISCHE CONVENTIES (alle chats bewust zijn)

### Gesplitste SHACL-validatie (verplicht)

- **SECTIE A** (inference='none'): ctrl/bio ISO27002NamingShape, HandreikingBBNValueShape, asset:NamespaceShape
- **SECTIE B** (inference='owlrl'): AppliesToAssetTypeRangeShape, BVASymmetryShape, OrphanClassShape
- **COMBINED** (inference='owlrl', alle 7 shapes): 290 false-positives (identiek sinds v4.3.0-baseline en t/m v4.6.2)

### OWL RL of sterker verplicht

BIO-asset-mappings (M18) én D11-propagatie werken alleen onder OWL RL, HermiT, of sterker. Pure RDFS-inferentie is onvoldoende.

### Canonieke meetmethode per release

Bij elke minor- of patch-release draait technische chat:

- `canonical_metrics_v[versie].py` → `canonical_metrics_v[versie].json`
- `shacl_split_validate_v[versie].py` → `shacl_results_v[versie].json`
- `file_hashes_v[versie].txt` (versie-suffix verplicht sinds v4.3.3)

Doel: meetmethode-consistentie. §0 van patch-rapport altijd uit JSON (leerpunt v4.3.3).

### NamedIndividual-telmethode (geformaliseerd v4.3.3)

```python
len(set(g.subjects(RDF.type, OWL.NamedIndividual)))
```

Per-module-geparste graph, pre-inference, zonder impliciete rdflib-assertions.

### Semantische invariantie-check

Zes metrics voorspelbaar bij refactoring/consolidatie: classes, NamedIndividuals, ObjectProperties, DatatypeProperties, owl:sameAs, asset:appliesToAssetType. Ontology-metadata-triples mogen verschillen.

Canonieke referentie `asset:appliesToAssetType` onder `owlrl.DeductiveClosure(OWLRL_Semantics, axiomatic_triples=False, datatype_axioms=False)`: 428 expliciet, 973 inferred.

### Twee parallelle MaturityCapability-clusters (v4.6.0 — kritieke conventie)

Sinds v4.6.0 bestaan twee maturity-clusters parallel in het model (ongewijzigd in v4.6.1+v4.6.2):

- **biz-cluster** (m07): biz:MaturityAssessment + biz:MaturityLevel (ML_0..ML_5, CMMI-schaal) — voor GRCDomain-dashboard-aggregatie
- **isms-cluster** (m06): isms:MaturityCapability + isms:MaturityCapabilityLevel (Level_1..5, NBA-LIO/NOREA-schaal) — voor Sheet-6-evaluaties

**Niet samenvoegen.** Verschillende semantieken; verschillende niveau-schalen.

### CSFTier versus RiskManagementTier (v4.6.0 — naam-discipline)

- **risk:RiskManagementTier** (m03, NIST SP 800-39): organisational tiers (3 levels)
- **csf:CSFTier** (m21, NIST CSF 2.0): organizational profile tiers (4 levels Partial-Adaptive)

### SKOS-axioma-set-handling (v4.6.1 leerpunt — H41-kandidaat)

OWL-RL met huidige instellingen (`axiomatic_triples=False, datatype_axioms=False`) laadt geen SKOS-axiomas (skos:S46 symmetrie, skos:S47 transitiviteit). SKOS-predicate-substitutie binnen één blok raakt geen RDFS/OWL-inferentie-pad — daarom is Δ post-OWL-RL triples = 0 bij T-sprints (T1 + T2 beide bewijs).

**Architectuur-overweging (H41-kandidaat):** of skos-axiomas geactiveerd moeten worden in OWL-RL is een open vraag. Trigger voor heractivering: substantiële SKOS-mapping-uitbreiding waar transitiviteit/symmetrie auditief relevant wordt.

---

## OPENSTAANDE ITEMS

### Volgende sprint — kandidaten (post-T2)

Geen vaste planning. Kandidaten in volgorde van architectuur-prioriteit:

1. **T3-sprint** — m14 ctrl:↔compl: paren (31 stuks AVG/GDPR)
   - Compl→ctrl-richting (omgekeerd t.o.v. m10's ctrl→compl)
   - AVG-cross-walk-bron ontbreekt in `sources/` — bron-upload nodig of evidence-niveau-2/3-tolerantie
   - Helper-script-uitbreiding voor cross-module label-bronnen + m14-specifieke heuristieken
   - Protocol v1.2/v1.3-symmetrie-validatie nodig
2. **Protocol v1.3 vaststelling** — bij T3 of m14-sprint-scoping; sign-off door Steven
3. **Dashboard-inhaalslag** — v3 build scripts en v4.6.2 databestanden; 5+ sprints achterstand. Parallel met sprint-werk, niet-blokkerend.
4. **README.md-update** — nog op v1.8/v4.5.0-niveau; bijwerken naar v1.10/v4.6.2
5. **SP 800-53 → ISO 27001:2013 docx integratie** — hercodering naar 2022 via ISO 27002:2022 Annex F vereist
6. **BZK/kern-IBO NIS2 mapping** — digitaleoverheid.nl PDF 10 november 2023
7. **ENISA TIG-PDF integratie** — kandidaat-Route via Analyse-opdracht 2.0
8. **Spoor B-voorbereiding** — T&I lab-test
9. **H33** m11 substantiële uitbreiding SP 800-53 (huidig 124 van ~1000)
10. **H34** m11 enhancement-modellering (17 unique enhancements niet gelegd in v4.5.0)

### Parallel (geen blokker)

- **Dashboard SKOS-kwaliteitsanalyse** op 1.798 mappings — eerste deel (m10) afgerond via T1+T2; resterende mappings nog niet onderzocht
- **Dashboard-inhaalslag** — build-script update naar v4.6.2-snapshot; 5+ sprints aan ontologie-wijzigingen verwerken

### Masterchat-architectuurbeslissingen (open)

- **H15** — governance-graafdekking (Route P/Q/R) — geparkeerd
- **H21** — 421 implicit individuals (consistentie-keuze) — geparkeerd
- **H41 (NIEUW)** — SKOS-axioma-set-handling (skos:S46 symmetrie, skos:S47 transitiviteit) in OWL-RL — geparkeerd. Trigger: substantiële SKOS-mapping-uitbreiding waar transitiviteit auditief relevant wordt.

### Post-v4.3.3 architectuur-aandachtspunten

- **H25** — D12 + compl:articleRef-domain-spanning. Per v4.6.2 onveranderd
- **H26** — OBL-laag gap NIS2 art. 18, 19, 22, 24. Onveranderd
- **H27** — Voorwaardelijke γ-migratie compl:articleRef → compl:articleIdentifier. Onveranderd
- **H32** — OBL-laag modelleringsasymmetrie. Onveranderd; trigger bij Spoor B
- **H33** — m11 substantiële uitbreiding SP 800-53. Trigger: Spoor B-organisatie heeft >50 niet-gemapte SP 800-53-individuals nodig
- **H34** — m11 enhancement-modellering. Trigger: serieuze SP 800-53-toepassing waar enhancements auditief relevant zijn
- **H35** — Cbb 5.28-typo-interpretatie. Trigger: optionele interpretatieve correctie bij latere sprint
- **H36** — SKOS-exactMatch-audit ctrl:↔compl:. **m10-component closed via T1+T2.** m14-component open subtask.
- **H37** — open-ontologies MCP integratie. Post-migratie evaluatie pending.
- **H38** — actief (zie H-register).
- **H39** — SHACL-blinde vlek ctrl:↔compl:-mapping-distributie. Active geparkeerd (T1 + T2 bevestigen). Trigger: shape-uitbreiding op SKOS-distributie indien gewenst.
- **H40** — UI-renderdekking Spoor A. Active geparkeerd.

### Niet-formeel-geregistreerde kandidaten (wachten op natuurlijk trigger)

- SP 800-53 → ISO 27001:2013 docx integratie (project knowledge bevat bestand; 2013-versie vereist hercodering naar 2022 via ISO 27002:2022 Annex F)
- BZK/kern-IBO NIS2 ↔ ISO 27002:2022 mapping (digitaleoverheid.nl PDF, 10 november 2023; 2022-conform, Rijksoverheid-relevant)
- fw:isManagedBy-property voor beheerder-rol (Logius beheert ENSIA, BZK/NOREA/VNG zijn issuers). Trigger: meerdere frameworks vereisen beheerder-rol-modellering

### Spoor B automatisch geparkeerd

- H11, H12, H13, H19, H20 — ABox-lege schalen in risk/roles/isms/asset namespaces
- H14 — 3 sample-controls zonder compl:satisfiedBy

### Overig

- HermiT-herrun in Protégé (niet uitgevoerd sinds v4.0.0)
- Community Profile NL Rijksoverheid (NIST CSF 2.0) — overwegen na T-sprints
- Cbb-inwerkingtreding-monitoring — Spoor C
- Route 1/1-light (ISO-guidance parafrasering) — geparkeerd naar v5.x
- ctrl:CybersecurityConcept ↔ csf:Function-overlap als SKOS-mapping-kandidaat (vondst v4.5.0)
- ENSIA-control-set: NOREA-handreiking biedt geen control-set-bron. Bron-zoeker-werk nodig (mogelijk ENSIA-vragenlijst online?). Analyse-opdracht 2.0-onderwerp.
- **PK-opschoning** post-GitHub-MCP-setup: brain-vault en publieke bronnen verwijderbaar uit PK (nu in repo); NEN-restrictieve bronnen moeten blijven

---

## BEWUST HARDVERWIJDERDE ELEMENTEN

Geregistreerde verwijderingen die later geretrofit kunnen worden bij specifieke trigger-condities.

| Element | Datum | Vervangen door | Retrofit-trigger |
|---|---|---|---|
| ext:articleNumber | v4.3.3 (22 apr 2026) | compl:articleRef | Indien externe consumers / legacy-queries zich melden |
| ext:hasENISAGuidance | v4.4.0 (13 mei 2026) | ext:hasUVInterpretation | Bij echte ENISA TIG-integratie |
| Attr_NIST_CSF_2_0_OLIR_2026 | v4.5.0 (19 mei 2026, hernoemd) | Attr_NIST_CSF_2_0_Reference_Tool_2026 | Geen — OLIR-naam blijft beschikbaar voor echte OLIR-snapshot |
| fw:ENSIA als fw:Guideline (gepromoot v4.6.0) | 21 mei 2026 | fw:ENSIA als fw:GRCFramework | Geen — semantisch correct |

Geen verwijderingen in T1 (v4.6.1) of T2 (v4.6.2) — beide sprints zijn predicate-substitutie binnen bestaande triples.

---

## BUITEN SCOPE — BEWUST UITGESLOTEN ELEMENTEN

Geen wijziging in v1.10 t.o.v. v1.9.

- **Unified Compliance Framework (UCF)** — uitgesloten 9 mei 2026; trigger: organisatie UCF-licentie
- **21 source-prefixes uit csf2.xlsx** — uitgesloten v4.5.0 sub-keuze C1
- **6 bewust niet-gemapte COSO/COBIT-targets** (Stap 7 v4.5.0): COBIT_DSS05, COBIT_EDM02, COBIT_EDM04, COBIT_EDM05, COSO_ERM_InformationCommunicationReporting, COSO_ICF_InformationCommunication
- **GV.SC SKIP** — geen GOVERN-overlap-mapping (v4.5.0)
- **isms:Level_3 niet gemapped naar CSF Tier** (v4.6.0)
- **fw:Logius niet als fw:issuedBy ENSIA** (v4.6.0)

---

## CORRECTIEGESCHIEDENIS (informatief)

[Pre-v4.5.0-correcties: zie projectinstructie v1.7]
[v4.5.0-correcties: zie projectinstructie v1.8]
[v4.6.0-correcties: zie projectinstructie v1.9]

### v4.6.1-correcties (T1-sprint, 26 mei 2026)

- T1-precedent-werk vond 28 onterechte ctrl:↔compl: exactMatch-claims in m10 die alle herclassificeerd zijn naar broadMatch via C2-cluster-discipline + D4.1-disclaimer-toepassing (ENISA TIG R285)
- Twee edge-cases (T1-021 NIS2_j MFA, T1-023 NIS2_h cryptografie) initieel via masterchat-NEN-PK-toets opgelost (pre-Tech-NEN-autonomie-koers-correctie)
- Steven-koers-correctie 27 mei 2026: Tech-subagent krijgt lokale NEN-bron-toegang — geen masterchat-PK-toets meer nodig voor ISO-bronnen

### v4.6.2-correcties (T2-sprint, 27 mei 2026)

- T2-sprint vond 65 onterechte ctrl:↔compl: closeMatch + relatedMatch-claims in m10; alle herclassificeerd naar broadMatch via cluster-discipline (10 clusters convergeren naar broadMatch)
- Pre-Stap-4 errata-correctie: pilot-rapport (errata-blok bovenaan) + Stap 3-rapport §1.1 (pilot-referentie-rij + Stap 3 resterend-rij gecorrigeerd naar helper-script-classificatie)
- Helper-script-classificatie autoritatief over handmatige rapport-classificatie bij discrepantie (T2-leerpunt; verwerkt in Protocol v1.3 §10.4)
- Masterchat-instructie-fout: §1 verwachtings-tabel ("m10 related 27" — m14-cumulatief) inconsistent met §8 GO-criterium ("m10 related 0" — m10-only). Tech paste Protocol 12 correct toe; §8 GO-criterium leidend. Leerpunt verwerkt in Protocol v1.3 §10.5 (metrics-tabel-scope-annotatie verplicht)

---

## WIJZIGINGEN T.O.V. v1.9 (21 mei 2026)

Deze update verwerkt twee sprint-cycli (T1 v4.6.1 + T2 v4.6.2), de migratie naar Claude Code + GitHub, sprint-protocollen 14-17, D4.1-vaststelling, en SKOS-beoordelings-protocol v1.0 → v1.2 → v1.3-draft.

### Nieuwe baseline en ontologie-status

- Baseline v4.6.0 → **v4.6.1 (26 mei) → v4.6.2 (27 mei)**
- Triple-totalen ongewijzigd (20.950 pre-/44.907 post-OWL-RL); klassen/individuals/properties/sameAs ongewijzigd
- SKOS-mappings-totaal 1.798 ongewijzigd; predicate-distributie gewijzigd via T1 (28 substituties) + T2 (65 substituties)
- m10 ctrl→compl SKOS-distributie eindstand v4.6.2: exact 0 / close 0 / broad 118 / narrow 0 / related 0
- SHACL-uitkomsten ongewijzigd (A=0, B=0, COMBINED=290)
- Alleen `m10-nis2-ext.ttl` gewijzigd in T1 + T2; alle 21 andere modules + grc-shacl.ttl ongewijzigd

### Nieuwe D-decision

- **D4.1 (27 mei 2026):** Disclaimer-handling bij autoritatieve mapping-bronnen. Sub-rule onder D4. Volledig in `brain/brain__decisions__D04_skos-cross-framework.md`.

### Migratie Claude Code + GitHub afgerond (26 mei 2026)

- Repo: `stevenbouw/grc-kennismodel` (privé)
- Tech-, Brein-, Dashboard-chats gemigreerd naar Claude Code
- Master-, Documentatie-, Analyse-, Asset-chats blijven in claude.ai
- CLAUDE.md v1.3 actief; subagent configs (tech.md, brein.md, dashboard.md)
- Sprint-protocols.md v1.3 in repo (13 protocollen → uitgebreid met 14-17)
- Karpathy-principes (Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution) verwerkt in Tech en Dashboard configs
- Subagents committen nooit zelfstandig — Steven inspecteert + commit handmatig
- GitHub-MCP geconfigureerd in masterchat (toegankelijk via `grc-kennismodel:*` tools)

### Nieuwe sprint-protocollen (14-17)

- **Protocol 14**: Pre-push disclosure-check (vijf categorieën, incl. NEN-tekst-detectie)
- **Protocol 15**: Werkbare applier door Tech (geen specificatie-only-deliverables)
- **Protocol 16**: Lokatie verificatie-scripts in patch-rapport §9 Deliverables-tabel
- **Protocol 17**: NEN-werkverdeling met Tech-autonomie (herzien 27 mei na Steven-koers-correctie)

### Protocol v1.3 werkflow-discipline (draft, vaststelling pending)

Vier nieuwe werkflow-disciplines in Protocol v1.3 (`docs/skos-beoordelings-protocol-v1_3.md`):

- §10.2 Bottom-up rapport-bouw verplicht
- §10.3 Interne tabel-consistentie-discipline
- §10.4 Helper-script-classificatie autoritatief bij discrepantie
- §10.5 Metrics-tabel-scope-annotatie verplicht

Opgenomen als gedragsregel in v1.10 in afwachting van formele vaststelling Protocol v1.3 bij T3 of m14-sprint-scoping.

### Nieuwe H-items

- **H41 (NIEUW geparkeerd):** SKOS-axioma-set-handling (skos:S46 symmetrie, skos:S47 transitiviteit) in OWL-RL — architectuur-vraag voor toekomstige OWL-RL-uitbreiding

### H-status mutaties

- **H36 (closed voor m10):** SKOS-exactMatch-audit ctrl:↔compl: m10-component afgesloten via T1+T2. m14-component open subtask voor toekomstige T-sprint.

### Brain-vault locatie-update

- Brain-vault verhuisd van Project Knowledge naar `brain/`-folder in GitHub-repo (post-migratie iteratie 13)
- Toegang vóór migratie: `project_knowledge_search`
- Toegang post-migratie: GitHub-MCP voor masterchat; directe file-toegang voor Tech-subagent en Brein-subagent in Claude Code
- ~115 markdown-bestanden in brain/-folder (iteratie 13); iteratie 14 pending na vaststelling v1.10

### Tech-NEN-autonomie

- Lokale NEN-bron-toegang in `/Users/stevenbouwmeester/grc-sources-licensed/` voor ISO 27002:2022, 27001:2022, 27005, 31000, 22301, 22313
- Parafrase-discipline verplicht (geen verbatim NEN-tekst >10 woorden)
- Geen masterchat-PK-toets meer nodig voor ISO-bronnen
- Disclosure-check Protocol 14 uitgebreid met NEN-tekst-detectie (categorie 5)

### Fase-planning verschuiving

- v4.6.0 = laatste geplande Spoor-A-uitbreidings-sprint
- Post-migratie kwaliteitsanalyse-fase actief: T1 + T2 uitgevoerd
- v4.7.0 als sprint-nummer niet gebruikt (T-naamgeving in plaats)
- Volgende kandidaten: T3 (m14-paren), Protocol v1.3-vaststelling, dashboard-inhaalslag, structurele uitbreidingen H33/H34

### Geen wijzigingen in

- Missie, visie, toepassingen
- Normenkader (5 lagen, ongewijzigd qua structuur)
- 11 namespaces (D3 definitief sinds v4.5.0)
- Vijf doelen / drie sporen
- Zeven chats structuur (alleen platform-locatie van Tech/Brein/Dashboard gewijzigd door migratie)
- D1, D2, D3, D5, D6, D7, D8, D9, D10, D11, D12 (D9 wel verdiept-bewijs door T2)

---

## WIJZIGINGEN T.O.V. v1.8 / v1.7 / v1.6 / v1.5 / v1.4 / v1.3 / v1.2

[Inhoud uit v1.9 + voorgangers onverkort van toepassing.]

---

*Einde projectinstructie v1.10.*
