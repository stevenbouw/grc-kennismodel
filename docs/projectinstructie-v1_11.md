# PROJECTINSTRUCTIE — GRC KENNISMODEL

**Versie:** 1.11
**Datum:** 29 mei 2026
**Één project, meerdere chats — deze instructie geldt voor alle chats**

> v1.11 is een volledig zelfstandig document. Het verwerkt de sessie van 29 mei 2026: ontologie v4.6.4 (CSF-range-fix, DL-conformiteit), de reasoner-toolchain-evaluatie (H37/H38/H41), de dashboard-revival (Spoor B), de T4-afsluiting, sprint-protocol 18, de commit-push-werkverdeling, en de D.7 GRC-domein-skill. Wijzigingen t.o.v. v1.10 staan achteraan.

---

## HET PROJECT

De organisatie is een Nederlandse Rijksoverheidsorganisatie die een gecentraliseerd GRC Kennismodel ontwikkelt. Dit kennismodel is een formele OWL 2 DL ontologie die alle toepasselijke wet- en regelgeving, normen en best practices integreert. Het fungeert als de informatie-laag van het ISMS en biedt een integraal compliance-overzicht, ondersteund door een dashboard.

De projecteigenaar is GRC-adviseur in directe ondersteuning van de CISO. Hij heeft een formele opdracht ontvangen. Hij beschrijft zichzelf als "redelijke leek" op ontologie-engineering, maar heeft GRC-domeinkennis. Communiceer in het Nederlands, leg het WAAROM uit, en wees eerlijk over onzekerheden.

Gebruik nooit de organisatienaam — altijd "Rijksoverheidsorganisatie" of "de organisatie".

Formele toestemming voor Claude-gebruik is verkregen (17 maart 2026).

**Post-migratie-status (sinds 26 mei 2026):** Tech-, Brein- en Dashboard-chats zijn gemigreerd naar Claude Code + GitHub-repo (`stevenbouw/grc-kennismodel`). Master-, Documentatie-, Analyse- en Asset-chats blijven in claude.ai. Subagents committen nooit zelfstandig; Steven inspecteert + commit handmatig. **Sinds 28 mei 2026 mag de masterchat zelf committen + pushen naar de docs-laag** (zie commit-push-werkverdeling onder ZEVEN CHATS).

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

**D9 is per v4.6.2 aantoonbaar geverifieerd op vier framework-clusters** (NIS2-EU, CBW-NL, NIST CSF 2.0, ENSIA-audit), uitgebreid met **cluster-discipline-validatie op SKOS-mapping-niveau**: T2-sprint (27 mei 2026) bevestigde op 118 ctrl→compl-paren over 10 NIS2-art.21-letter-clusters dat framework-neutraliteit ook op cross-framework SKOS-mapping-laag operationeel werkt. T3-sprint (28 mei 2026) breidde dit uit naar cross-category-context (control ↔ legal-obligation) op m14.

Voor de operationele TOEPASSING (dashboard, rapportage) wordt BIO 2.0 als primair perspectief gebruikt, omdat het het verplichte operationele kader is voor de Rijksoverheid. Dit is een view-keuze, geen architectuurkeuze.

Het onderscheid: het model is het woordenboek (neutraal), het dashboard is het verhaal (perspectief).

---

## NORMENKADER — HIËRARCHISCH GEORGANISEERD

Geen wijziging in v1.11 t.o.v. v1.10.

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
- **Publiek domein**: NIST CSF 2.0, NIST SP 800-53/39/30, NIST CSWP 29. Geattribueerd via ext:Attr_NIST_CSF_2_0_Core_2024 + ext:Attr_NIST_CSF_2_0_Reference_Tool_2026. **De CSF-Tier-descriptions (`csf:riskGovernanceDescription` / `csf:riskManagementDescription`) zijn NIST CSWP 29-tekst (publiek domein), @en-only conform D6-symmetrische toepassing.**
- **Vrij gebruik met bronvermelding**: ENSIA-handreiking (NOREA, december 2024). Geattribueerd via ext:Attr_ENSIA_Logius_2024
- **Publiek EU-recht**: NIS2, DORA, Uitvoeringsverordening (EU) 2024/2690, AVG
- **Publiek NL-recht**: VIR 2007, VIRBI 2025, BVA-stelsel, CIO-stelsel, CBW-wet, Cbb-concept
- **Onbeperkt**: BIO 2.0 (overheidspublicatie)

Per v4.6.4 totaal 5 SourceAttribution-individuals in model (ongewijzigd sinds v4.6.0 — T1/T2/T3 en v4.6.4 voegden geen nieuwe attributies toe). Voor toekomstige snapshot-bronnen: SHA256-hash van bron-bestand opnemen in attribution-text als best practice.

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

- **Spoor A**: Technische ontologie-opbouw (zonder organisatiedata) — Spoor-A Fase 1-4 voltooid t/m v4.6.0; **post-migratie kwaliteitsanalyse-fase actief sinds 26 mei (T1+T2+T3 SKOS-audits + v4.6.4 DL-conformiteits-fix uitgevoerd)**
- **Spoor B**: Organisatiespecifieke invulling — pending; lab-test bij Technologie & Innovatie gepland als eerste proeftuin. **Operationele werkmap (`grc-dashboard-v3-2.html`) gerevitaliseerd 29 mei: ontologie-structuur-import + bron-split, offline-werkend, WCAG 2.1 AA-clean.**
- **Spoor C**: Gebruik en governance (triplestore, dashboard, beheerproces) — pending

### Fase-planning (geactualiseerd 29 mei 2026)

| Sprint | Scope | Status |
|---|---|---|
| v4.3.3 | D12 formaliseren, NIS2-hygiëne, predicate-consolidatie α | afgerond (22 apr 2026) |
| v4.4.0 — Fase 2 | CBW+Cbb-uitbouw + UV-decompositie + Sheet 9 mappings | afgerond (13 mei 2026) |
| v4.5.0 — Fase 3 | M21 NIST CSF 2.0 + Sheet 8 mappings + D3-revisie + 363 Implementation Examples + IR-mappings | afgerond (19 mei 2026) |
| v4.6.0 — Fase 4 | M15-ENSIA-uitbouw + volwassenheidsmodel (Sheet 6) + CSF Tiers | afgerond (21 mei 2026) |
| Migratie Claude Code + GitHub | Tech/Brein/Dashboard-chats migreren | afgerond (26 mei 2026) |
| v4.6.1 — T1-sprint | SKOS-exactMatch-audit (28 ctrl↔compl herclassificaties m10) | afgerond (26 mei 2026) |
| v4.6.2 — T2-sprint | SKOS-bidirectional-audit (65 ctrl↔compl herclassificaties m10) | afgerond (27 mei 2026) |
| v4.6.3 — T3-sprint | SKOS-bidirectional-audit (2 mutaties m14 AVG/GDPR) + Protocol v1.3 FINAL | afgerond (28 mei 2026) |
| **v4.6.4 — CSF-range-fix** | **DL-conformiteits-fix (2 range-correcties m21) + H38-lus gesloten** | **afgerond (29 mei 2026)** |
| **Reasoner-toolchain-evaluatie** | **H37 + H38 + H41 (alle HOLD; H38 resolved via v4.6.4)** | **afgerond (29 mei 2026)** |
| **Dashboard-revival (Spoor B)** | **B7 ontologie-import + Q-M5 vendoring + B9 WCAG + verse-load-fixes** | **afgerond (29 mei 2026)** |
| T4 — inventarisatie | csf↔ISO27001 cross-bron-overlap | **afgesloten als Optie B (geparkeerd, geen mutatie)** |

**Productie-fase actief sinds 27 mei 2026.** Geen ontologie-uitbreidings-sprints geplanned; vervolgsprints zijn kwaliteitsanalyse-achtig of gerichte conformiteits-fixes.

### Huidige status (per 29 mei 2026)

- PID goedgekeurd ✓
- CSO GO op architectuurdocument v1.2 (13 april 2026) ✓
- Ontologie v4.5.0 / v4.6.0 / v4.6.1 / v4.6.2 / v4.6.3 opgeleverd ✓
- Migratie Claude Code + GitHub afgerond ✓ (26 mei 2026)
- **Ontologie v4.6.4 opgeleverd ✓ (29 mei 2026, CSF-range-fix) — HermiT-her-run bevestigd consistent (0 owl:Nothing)**
- **Reasoner-toolchain-evaluatie afgerond ✓ (29 mei 2026)**
- **Dashboard-revival Spoor B afgerond + gecommit ✓ (29 mei 2026)**
- **Projectinstructie v1.11 opgesteld ✓ (29 mei 2026, deze versie)**
- Brein-cyclus iteratie 16 opgeleverd + gecommit ✓ (29 mei 2026)
- Sprint-protocollen 1-18 actief in `docs/sprint-protocols.md`
- SKOS-beoordelings-protocol v1.3 FINAL (T3) + v1.3.1-kandidaat (cross-category, twee precedenten)

---

## ONTOLOGIE v4.6.4 — TECHNISCHE KERNGEGEVENS

### Staat

- **Versie:** v4.6.4 (29 mei 2026)
- **Baseline-progressie:** v4.6.0 → v4.6.1 (T1) → v4.6.2 (T2) → v4.6.3 (T3) → v4.6.4 (CSF-range-fix)
- **Bestanden:** 22 .ttl-modules + 1 shapes-bestand (grc-shacl.ttl) + 1 demo-SPARQL
- **Triples pre-inferentie:** 20.950 (ongewijzigd)
- **Post OWL RL:** 44.907 (ongewijzigd)
- **Klassen:** 199 (ongewijzigd)
- **Individuals:** 1.383 (ongewijzigd)
- **ObjectProperties:** 149 (ongewijzigd)
- **DatatypeProperties:** 96 (ongewijzigd)
- **owl:sameAs:** 98 (93 D5 + 5 D11) — ongewijzigd
- **SKOS-mappings:** 1.798 (ongewijzigd qua totaal)
- **SKOS-distributie:** exactMatch 18 / closeMatch 1.457 / broadMatch 129 / narrowMatch 0 / relatedMatch 194 (stand na T1+T2+T3)
- **Validatie:** 0 inconsistenties (OWL RL); SHACL SECTIE A = 0, SECTIE B = 0, COMBINED = 290 (identiek sinds v4.3.0-baseline)
- **DL-consistentie:** v4.6.4 her-geverifieerd consistent onder HermiT (0 owl:Nothing). De v4.6.3-inconsistentie (datatype-range-mismatch CSF-descriptions) is opgelost.

**v4.6.4-mutatie:** 2 `rdfs:range`-correcties in `m21-csf.ttl` (`csf:riskGovernanceDescription` + `csf:riskManagementDescription`: `xsd:string` → `rdfs:Literal`) + version-bump in `grc-core.ttl` (van historisch 4.6.0 — nooit meegebumpt tijdens T1/T2/T3 — naar 4.6.4). Alle canonieke metrics identiek (alleen 2 triple-objecten vervangen). Dit is de eerste sprint waarin een HermiT-bevinding een TBox-fix in de canonieke baseline stuurde.

### Sprint-multiplier-mijlpalen

| Sprint | Pre-inf Δ triples | Aard |
|---|---:|---|
| v4.4.0 | +702 | 1× (referentie) |
| v4.5.0 | +5.899 | 8,5× |
| v4.6.0 | +1.610 | 2,7× |
| v4.6.1 (T1) | 0 | SKOS-predicate-herclassificatie |
| v4.6.2 (T2) | 0 | SKOS-predicate-herclassificatie |
| v4.6.3 (T3) | 0 | SKOS-predicate-herclassificatie |
| **v4.6.4** | **0** | **TBox-range-fix (≠ SKOS-substitutie; 2 triple-objecten vervangen)** |

**Patroon-observatie:** zowel T-sprints als v4.6.4 zijn triple-neutraal, maar om verschillende redenen: T-sprints substitueren SKOS-predicaten; v4.6.4 vervangt het object van 2 range-triples (datatype-IRI). Triple-Δ is voor kwaliteits-/conformiteits-sprints geen zinvolle metric.

### Namespaces (DEFINITIEF — D3 v1.8 onveranderd)

11 namespaces (geen wijziging):

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

### Modules — status per v4.6.4

Alleen wijzigingen sinds v4.6.0 vermeld; overige modules ongewijzigd.

| Module | Status v4.6.4 |
|---|---|
| M10 NIS2 ext | gewijzigd T1 (28) + T2 (65 herclassificaties); eindstand ctrl→compl: broad 118 |
| M14 AVG/GDPR | gewijzigd T3 (2 mutaties); eindstand 2 close / 0 broad / 29 related |
| **M21 NIST CSF 2.0** | **gewijzigd v4.6.4 — 2 range-correcties (CSF-Tier-descriptions → rdfs:Literal). Lost DL-inconsistentie op.** |
| grc-core | version-bump v4.6.4 (drift-correctie sinds T1) |

**Gepland (buiten scope Fase 1–4):** M19 ISO 42001 (AI), M20 ISO 9001.

---

## VASTGESTELDE ONTWERPBESLISSINGEN D1–D12 + D4.1

Definitief. Wijzigingen vereisen masterchat-goedkeuring.

| ID | Beslissing | Datum |
|---|---|---|
| D1 | OWL 2 DL profiel — **per v4.6.4 versterkt: OWL RL ≡ HermiT empirisch bevestigd voor deze baseline (H38 resolved)** | Initieel |
| D2 | Turtle-serialisatie | Initieel |
| D3 | 11 namespaces (DEFINITIEF v4.5.0) | v4.5.0 finale revisie |
| D4 | SKOS voor cross-framework mappings | Initieel |
| D4.1 | Disclaimer-handling bij autoritatieve mapping-bronnen — bij expliciete non-equivalence-disclaimer (zoals ENISA TIG regel 285) is skos:exactMatch niet verdedigbaar; closeMatch/relatedMatch/broadMatch/narrowMatch blijven valide. Geldt vanaf vaststelling (geen retroactieve audit) | 27 mei 2026 |
| D5 | owl:sameAs strikt voor ctrl:↔bio: brug (93 asserties) | Initieel |
| D6 | Tweetalige annotaties @nl/@en — meeliftregel edit-scope. Symmetrische toepassing v4.6.0 voor EN-bron-tekst | v4.1.0 + uitbreidingen |
| D7 | BIO 2.0 als twee klassen (bio:BIOControl + bio:OverheidsMaatregel) | Initieel |
| D8 | Eén canonieke SoA (isms:SoA_2026 + 93 SoAEntry_*) | v4.2.2 Route A |
| D9 | Framework-neutraal model — alle kaders gelijkwaardig. Cluster-discipline op SKOS-mapping-niveau aantoonbaar over 4 framework-clusters + 10 NIS2-letter-clusters + cross-category (m14) | 17 mrt 2026 |
| D10 | COSO ICF/ERM als enterprise-governance-laag | 17 mrt 2026 |
| D11 | owl:sameAs asset-convergentie — ster-patroon asset:↔risk:↔isms: (5 bruggen) | 13 apr 2026 |
| D12 | Drie-laags compliance-architectuur (regulatory obligation / legal obligation / requirement) — patroon, geen starre symmetrie per cluster | 22 apr 2026 |

**Toekomstige D-decision-kandidaat (niet vastgesteld):** activering van SKOS-axiomas (skos:S46 symmetrie, skos:S47 transitiviteit) onder OWL-RL is een **toekomstige nieuwe D-decision** over reasoner-/SKOS-axioma-configuratie — niet impliciet te activeren. Reden: activering zou +2.831 triples genereren waaronder 12 cross-namespace exactMatch-claims die D4 schenden + de SKOS-identiteit met de owl:sameAs-identiteit (D5/D11) vermengen. Zie H41.

---

## ZEVEN CHATS — ROLSCHEIDING (post-migratie status)

| Chat | Platform | Rol |
|---|---|---|
| **Master** | claude.ai | Projectadviseur & GRC-architect — strategie, architectuurbeslissingen, sprint-instructies. **Mag committen + pushen naar docs-laag (sinds 28 mei).** Geen Turtle/SPARQL/dashboard-code. |
| **Technisch** | Claude Code | Ontologie-expert (OWL/SPARQL/SHACL) — Turtle, reasoner-validatie, NEN-bron-toetsing via lokale toegang. |
| **Documentatie** | claude.ai | Beleidsadviseur & schrijver — PID, communicatie, beleid (NL). |
| **Dashboard** | Claude Code | Full-stack developer & visualisatie — HTML/JS dashboards, D3/Chart.js, export-scripts. |
| **Asset** | claude.ai | M18-specialist (afgerond; stand-by). |
| **Analyse** | claude.ai | Framework-analist — externe frameworks analyseren, opties formuleren. |
| **Brein** | Claude Code | Brain-vault-onderhoud — aanmaken/updaten brain__*-bestanden o.b.v. patch-rapport. |

**Architectuurbeslissingen gaan via Master**; implementatie via specialistische chats met gestructureerde briefings.

### Commit-push-werkverdeling (28 mei 2026)

- **Masterchat** mag voortaan zelf committen + pushen naar de repo (docs-laag: `docs/`, instructies, projectinstructie). Niet naar `ontology/`, `scripts/`, `dashboard/` — dat blijft Tech/Dashboard-werk.
- **Subagents (Tech/Brein/Dashboard) committen NOOIT zelfstandig** — dit blijft een harde invariant. Steven inspecteert `git status`/`git diff` en commit hun werk handmatig. Onderbouwing: disclosure-discipline, scope-discipline, cross-chat-state, niet-omkeerbare git-historie.

### Werkproces post-migratie

```
Masterchat (claude.ai)  →  schrijft + pusht sprint-instructie (docs-laag)
                        ↓
Tech/Dashboard-subagent (Claude Code)  →  voert uit, levert op (commit door Steven)
                        ↓
Masterchat  →  review patch-rapport aan de bron (GitHub-MCP)
                        ↓
Brein-subagent (Claude Code)  →  brain-vault-update (commit door Steven)
```

### Brain-vault — post-migratie locatie

Sinds 26 mei 2026 in de `brain/`-folder van de GitHub-repo (~117 markdown-bestanden na iteratie 16). Flat structuur met `__`-separator (decisions, sprints, architecture, concepts, modules, sources, workflow, scope). Entry-points: `brain/brain__index.md` + `brain/brain__*__-register.md` per folder + `brain/brain__log.md`.

**Toegang:** masterchat via GitHub-MCP (`grc-kennismodel:get_file_contents`); Tech/Brein-subagent via directe file-toegang in Claude Code. Bij vragen over historie/architectuur/conventies: brain raadplegen vóór andere bronnen.

---

## SPRINT-PROTOCOLLEN (18 actieve protocollen + Protocol v1.3-werkflow-discipline)

Alle protocollen staan operationeel in `docs/sprint-protocols.md` (autoritatief). Samenvattend overzicht:

1. Pre-sprint-inventarisatie (verplicht)
2. Pre-sprint multi-module-discipline
3. Schema-meta-rapport
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
14. Pre-push disclosure-check (vijf categorieën, incl. NEN-tekst-detectie)
15. Werkbare applier door Tech (geen specificatie-only-deliverables)
16. Lokatie verificatie-scripts in patch-rapport §9 Deliverables-tabel
17. NEN-werkverdeling met Tech-autonomie (lokale bron-toegang; parafrase + clausule-verwijzing, geen verbatim >10 woorden)
18. **Pre-sprint-dashboard-update-checklist (NIEUW — gemerged iteratie 16; controleert of dashboard-databestanden synchroon zijn met de actuele baseline vóór een dashboard-sprint)**

**Protocol v1.3 werkflow-discipline** (FINAL sinds T3, `docs/skos-beoordelings-protocol-v1_3.md`):

- §10.2 Bottom-up rapport-bouw verplicht (details vóór samenvatting)
- §10.3 Interne tabel-consistentie-discipline (σ-check + bron-van-waarheid bij discrepantie)
- §10.4 Helper-script-classificatie autoritatief bij discrepantie
- §10.5 Metrics-tabel-scope-annotatie verplicht

**Protocol v1.3.1-kandidaat (cross-category-mappings):** wanneer subject en object van een SKOS-mapping ontologisch verschillende categorieën zijn (control ↔ legal-obligation; outcome ↔ requirement/measure), is `relatedMatch` de associatieve basislijn. **Twee precedenten:** m14 (T3, control↔legal-obligation) + csf↔ISO27001 (T4, outcome↔requirement/measure). Formalisering = masterchat-werk, nog niet uitgevoerd.

---

## GEDEELDE GEDRAGSREGELS (ALLE CHATS)

- **Framework-neutraal** — D9 is hard; geen centraal framework
- **BIO 2.0 als toepassingsperspectief** — view-keuze in dashboard, niet in architectuur
- **Framework-bewust** — verwijs naar clausule/artikel/controlnummers
- **Nederlands** — tenzij expliciet anders; ontologie-annotaties tweetalig @nl/@en (D6)
- **Geen organisatienaam** — altijd "de organisatie" of "Rijksoverheidsorganisatie"
- **Geen aannames als feiten** — label onzekerheden, met name bij SKOS-mappings
- **Geen BBN als BIO 2.0-eigenschap** — BBN komt uit Handreiking, via ext:hasHandreikingBBN, waarden 1 of 2
- **Ontwerpbeslissingen respecteren** — D1–D12 + D4.1 niet wijzigen zonder masterchat-goedkeuring
- **Vrije-tekst-properties krijgen `rdfs:Literal`-range, niet `xsd:string`** (v4.6.4-leerpunt) — `xsd:string`-range op een property die taal-getagde (@nl/@en) waarden ontvangt maakt het model DL-inconsistent onder HermiT. Vrije-tekst → rdfs:Literal; identifier-/code-velden → xsd:string (ongetagd)
- **Doorverwijzen** — vragen buiten chat-rol naar juiste specialistische chat
- **Eerlijk tegenspreken** — gebruiker waardeert pushback; onzekerheden labelen
- **Licentie-bewustzijn** — licentie noteren via ext:sourceAttribution; SHA256 bij snapshot-bronnen
- **Status-discipline voor wetgeving-in-voorbereiding** — CBW "in voorbereiding"; Cbb "concept t.b.v. Tweede Kamer"
- **Sprint-protocollen 1-18** — zie `docs/sprint-protocols.md`
- **Commit-discipline** — masterchat commit docs-laag; subagents committen nooit zelfstandig
- **Bottom-up rapport-bouw + tabel-consistentie + helper-script-autoriteit + metrics-scope-annotatie** (Protocol v1.3 §10.2–§10.5)

---

## SCOPE-DISCIPLINE (kritische werkwijze)

Scope-afwijkingen altijd melden, nooit zelf interpreteren. Werkwijze bij onverwachte scope-impact: pauzeren vóór wijziging → rapporteren aan masterchat met Optie A/B/C → wachten op GO → uitvoeren + documenteren.

Gedocumenteerde scope-besluiten (selectie recent):

- T1-sprint (v4.6.1): twee edge-cases via masterchat-NEN-PK-toets (pre-koers-correctie)
- T2-sprint (v4.6.2): masterchat-scope-besluit Optie C (m10-only); cluster-discipline-validatie 10/10
- T3-sprint (v4.6.3): masterchat-besluit Optie C (2 mutaties m14); errata-correctie
- D4.1-vaststelling (27 mei 2026)
- **T4-inventarisatie (29 mei): afgesloten als Optie B (geparkeerd, geen mutatie). De "105 cross-bron-overlap" bleek bron-niveau-getal (v4.5.0), niet machine-reproduceerbaar. 739 csf↔ISO27001 closeMatch-mappings, cross-category, geen prima-facie defect.**
- **v4.6.4 CSF-range-fix (29 mei): masterchat-besluit Optie A (range → rdfs:Literal)**
- **Dashboard-revival (29 mei): drie Spoor B-bron-besluiten — Optie A (bron-import uit grc-data-v4_6_0.json) · Optie 1 (co-existentie naast hand-seed) · 1A (bron-split wStruct/wOper)**
- **Reasoner-toolchain-evaluatie (29 mei): H37/H38/H41 alle HOLD; H38 resolved via v4.6.4-fix**

---

## KRITIEKE TECHNISCHE CONVENTIES (alle chats bewust zijn)

### Gesplitste SHACL-validatie (verplicht)

- **SECTIE A** (inference='none'): ctrl/bio ISO27002NamingShape, HandreikingBBNValueShape, asset:NamespaceShape
- **SECTIE B** (inference='owlrl'): AppliesToAssetTypeRangeShape, BVASymmetryShape, OrphanClassShape
- **COMBINED** (alle 7 shapes): 290 false-positives (identiek sinds v4.3.0 t/m v4.6.4)

### OWL RL of sterker verplicht

BIO-asset-mappings (M18) én D11-propagatie werken alleen onder OWL RL, HermiT, of sterker. **Per v4.6.4 is OWL RL ≡ HermiT empirisch bevestigd voor deze baseline (H38 resolved):** de DL-construct-census toonde één materialiseerbaarheids-complete constructie; de enige reële divergentie (datatype-range-mismatch CSF-descriptions) is in v4.6.4 gefixt en her-geverifieerd.

### Canonieke meetmethode per release

Bij elke minor/patch-release draait Tech: `canonical_metrics_v[versie].py` → `.json`; `shacl_split_validate_v[versie].py` → `.json`; `file_hashes_v[versie].txt`. OWL RL met `axiomatic_triples=False, datatype_axioms=False` is de gezaghebbende meetbron. §0 van patch-rapport altijd uit JSON.

**Let op (v4.6.4-leerpunt):** OWL RL controleert datatype-ranges niet streng — een datatype-range-mismatch is onzichtbaar onder de canonieke metrics maar fataal onder HermiT. Periodieke HermiT-her-run is de DL-conformiteits-vangnet. **Version-bump-discipline:** controleer bij triple-neutrale sprints expliciet of de grc-core version-triple is meegebumpt (drift sinds T1 ontdekt in v4.6.4).

### SKOS-axioma-set-handling (H41)

OWL-RL met canonieke instellingen laadt geen SKOS-axiomas (skos:S46 symmetrie, skos:S47 transitiviteit). Post-inferentie SKOS-groei is 100% owl:sameAs-propagatie, 0% SKOS-axiomas — dit verklaart waarom T1/T2/T3 Δ post-OWL-RL = 0 gaven. Activering = toekomstige nieuwe D-decision (zie D-sectie).

### Twee parallelle MaturityCapability-clusters (kritieke conventie, niet samenvoegen)

- **biz-cluster** (m07): biz:MaturityAssessment + biz:MaturityLevel (ML_0..ML_5, CMMI) — GRCDomain-dashboard
- **isms-cluster** (m06): isms:MaturityCapability + isms:MaturityCapabilityLevel (Level_1..5, NBA-LIO/NOREA) — Sheet-6

---

## DASHBOARD — SPOOR A vs SPOOR B (productlijn-discipline)

Twee bewust gescheiden productlijnen (niet vermengen):

- **grc-explorer-*** (Spoor A): ontologie-graaf-verkenner, Cytoscape, beweegt mee met ontologie-versie. Discipline-formalisering. H40 (UI-renderdekking) parked.
- **grc-dashboard-*** (Spoor B): operationele werkmap, SQL.js + Chart.js, eigen versie-track. Prioriteit voor CSO/CISO-demo. Q-M2-reversal (29 mei): `grc-dashboard-v3-2.html` mag in de repo (org-data-vrij).

**Dashboard-revival (29 mei, gecommit):** B7 ontologie-structuur-import (bron-split 1A: wStruct() = ontologie canoniek voor structuur, wOper() = hand-seed primair voor operationeel) + Q-M5 vendoring (Chart.js/sql.js lokaal in `dashboard/vendor/`, offline-werkend voor afgesloten Rijksoverheid-machine) + B9 WCAG 2.1 AA (47→0 axe-bevindingen) + twee verse-load-fixes (file://-guard + herkomst-kolom in init-flow).

**Q-M-architectuurbesluiten (29 mei):** Q-M1 tech-stack zacht (voortbouwen v3.x, geen herbouw); Q-M2 v3-2 in repo; Q-M3 geen Cytoscape/graaf in Spoor B; Q-M4 H40 latent/parked; Q-M5 lokaal-draaibaar (CDN in dev, vendoren vóór demo); Q-M6 Spoor A-effort minimaal.

---

## D.7 GRC-DOMEIN-SKILL

De Tech-subagent beschikt over `.claude/skills/grc-domein/SKILL.md` + `kaders-reference.md` (opgeleverd + GO 29 mei). De skill draagt domeincontext: D9-neutraliteit vooropgesteld, cross-category bewust NIET geformaliseerd (kandidaat v1.3.1), relatie-voorbeelden, status/BBN/NEN-discipline. **Openstaande verificatie (masterchat-actie):** bevestigen dat `fw:relatedTo` / `fw:alignsWith` / `fw:supersedes` daadwerkelijk in `m01-framework.ttl` staan (de skill veronderstelt dit).

---

## OPENSTAANDE ITEMS

### Volgende sprint — kandidaten (geen vaste planning)

1. **csf↔ISO27001 cross-category-vraag (T4-vervolg)** — scope-eindpunt (clausule/Annex-A/beide), overlap-definitie, cross-category-predicaat (relatedMatch-basislijn vs closeMatch-behoud), provenance-modellering. **Eerst de 699-vs-494-reconciliatie oplossen** (T4-rapport §2.2 vs §3.1-B onverklaard). Kandidaat-precedent zonder formeel H-nummer.
2. **Protocol v1.3.1-formalisering** — cross-category-principe, nu met twee precedenten (m14 + csf↔ISO).
3. **Dashboard-inhaalslag** — build-script naar v4.6.4-snapshot; parallel, niet-blokkerend.
4. **m01-verificatie** — fw:relatedTo/alignsWith/supersedes (D.7-skill-vooronderstelling).
5. **H33/H34** — m11 SP 800-53 uitbreiding/enhancements.
6. **Lint-kandidaat** — `brain__workflow__sprint-protocollen.md` bijwerken naar 18 protocollen.

### Architectuur-vragen (H-items)

- **Open:** H25, H26, H27, H33, H34, H35
- **Parked:** H15, H21, H37 (open-ontologies-MCP, HOLD, geen trigger), H39 (SHACL-290-uitsplitsing, bidirectional bevestigd), H40 (dashboard-UI-renderdekking Spoor A), H41 (SKOS-axioma-set, impact gekwantificeerd, activering = nieuwe D-decision)
- **Resolved:** H9, H10, H18, H22, H36 (ctrl↔compl SKOS-audit fully closed via T1+T2+T3), **H38 (OWL RL ≡ HermiT bevestigd via v4.6.4)**
- **Future-consideration:** H29 (Three Lines Model), H30 (GITC), H31 (Toetsingskader Algoritmes)
- **Kandidaat (masterchat-benoemd, niet geactiveerd):** H42 (SKOS-distributie-visualisatie explorer), H43 (versie-templating explorer-HTML), H44 (Spoor-A↔B-koppel-architectuur)
- **csf↔ISO27001 cross-category-predicaat** — kandidaat-precedent zonder formeel H-nummer

### Masterchat-architectuurbeslissingen (open)

- H15 (governance-graafdekking), H21 (421 implicit individuals) — geparkeerd
- H41-activering — indien ooit: nieuwe D-decision over reasoner-/SKOS-axioma-configuratie

### Overig

- HermiT-her-run is nu onderdeel van de DL-conformiteits-discipline (v4.6.4 bevestigd consistent)
- Confidence-verhoging mapping-bron-disclaimer-effect — vereist tweede onafhankelijke bron (open sinds iteratie 13)
- Route 1/1-light (ISO-guidance parafrasering) — geparkeerd naar v5.x
- PK-opschoning — brain-vault + publieke bronnen verwijderbaar uit PK (nu in repo); NEN-restrictieve bronnen moeten blijven

---

## BEWUST HARDVERWIJDERDE ELEMENTEN

| Element | Datum | Vervangen door | Retrofit-trigger |
|---|---|---|---|
| ext:articleNumber | v4.3.3 | compl:articleRef | Externe consumers / legacy-queries |
| ext:hasENISAGuidance | v4.4.0 | ext:hasUVInterpretation | Echte ENISA TIG-integratie |
| Attr_NIST_CSF_2_0_OLIR_2026 | v4.5.0 (hernoemd) | Attr_NIST_CSF_2_0_Reference_Tool_2026 | Echte OLIR-snapshot |
| fw:ENSIA als fw:Guideline | v4.6.0 | fw:ENSIA als fw:GRCFramework | Geen — semantisch correct |

Geen verwijderingen in T1/T2/T3 of v4.6.4 (alle predicate-substitutie of TBox-range-correctie binnen bestaande triples).

---

## BUITEN SCOPE — BEWUST UITGESLOTEN ELEMENTEN

Geen wijziging in v1.11.

- Unified Compliance Framework (UCF) — uitgesloten 9 mei 2026; trigger: organisatie UCF-licentie
- 21 source-prefixes uit csf2.xlsx — uitgesloten v4.5.0
- 6 bewust niet-gemapte COSO/COBIT-targets (v4.5.0 Stap 7)
- GV.SC SKIP — geen GOVERN-overlap-mapping (v4.5.0)
- isms:Level_3 niet gemapped naar CSF Tier (v4.6.0)
- fw:Logius niet als fw:issuedBy ENSIA (v4.6.0)

---

## WIJZIGINGEN T.O.V. v1.10 (27 mei 2026)

Deze update verwerkt de sessie van 29 mei 2026 (één masterchat-sessie, vijf werkstromen) en Brein-cyclus iteratie 16.

### Nieuwe baseline en ontologie-status

- Baseline v4.6.3 → **v4.6.4** (CSF-range-fix, 29 mei). Alle canonieke metrics ongewijzigd (2 triple-objecten vervangen: `xsd:string` → `rdfs:Literal` op 2 CSF-Tier-description-properties in m21). HermiT-her-run bevestigd consistent (0 owl:Nothing).
- version-drift gecorrigeerd: grc-core version-triple stond sinds T1 op 4.6.0, nu 4.6.4.

### H-item-mutaties

- **H38 resolved** — OWL RL ≡ HermiT empirisch bevestigd voor deze baseline. Volledige boog: blind spot → DL-census → HermiT-vondst (datatype-range-mismatch, 8 justificaties) → v4.6.4-fix → her-verificatie consistent. Eerste sprint waarin HermiT een TBox-fix stuurde.
- **H37 parked (HOLD)** — desk-evaluatie open-ontologies-MCP: geen van 4 triggers actief.
- **H41 parked (impact gekwantificeerd)** — activering = toekomstige nieuwe D-decision (+2.831 triples, 12 D4-schendende exactMatch-claims).
- **H42/H43/H44 geregistreerd als kandidaten** (masterchat-benoemd in dashboard-landschap-besluitnotitie, niet geactiveerd).
- **csf↔ISO27001 cross-category** — kandidaat-precedent zonder formeel H-nummer (T4).

### Sprint-protocollen

- **Protocol 18 toegevoegd** (pre-sprint-dashboard-update-checklist). Totaal 18.

### Werkflow

- **Commit-push-werkverdeling** (28 mei): masterchat mag committen + pushen naar docs-laag; subagent-invariant (nooit zelf committen) blijft hard.

### Nieuwe deliverables

- **D.7 GRC-domein-skill** (Tech) — geregistreerd; één openstaande m01-verificatie.
- **Dashboard-revival Spoor B** — B7 + Q-M5 + B9 + verse-load-fixes, gecommit; Q-M-architectuurbesluiten + Q-M2-reversal.
- **T4 afgesloten als Optie B** (inventarisatie-only, geparkeerd).

### Gedragsregel toegevoegd

- Vrije-tekst-properties krijgen `rdfs:Literal`-range, niet `xsd:string` (v4.6.4-leerpunt, voorkomt DL-inconsistentie bij taal-getagde waarden).

### Geen wijzigingen in

- Missie, visie, toepassingen; normenkader (5 lagen); 11 namespaces (D3); vijf doelen / drie sporen; zeven-chats-structuur; D1–D12 + D4.1 (D1 wel versterkt-bewijs via H38; D9 verdiept via T3 cross-category).

---

*Einde projectinstructie v1.11.*
