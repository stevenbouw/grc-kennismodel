# SKOS-kwaliteitsanalyse — GRC Kennismodel v4.6.0
**Eerste-versie rapport (Werkstroom C)**
**Datum:** 21 mei 2026
**Basis:** v4.6.0-snapshot (20.950 triples, 1.798 SKOS-mappings)

---

## Managementsamenvatting

Het SKOS-mapping-portfolio is in vijf sprints gegroeid van 346 (v4.3.1) naar 1.798 (v4.6.0) — een groei van 5,2×. Het CSF 2.0-cluster is verreweg de grootste toevoeging (1.448 nieuwe mappings). De algehele kwaliteit is solide: geen mapping-inconsistenties gevonden, de match-type-verdeling is logisch, en beide geïdentificeerde concentraties zijn architectureel verklaarbaar. Drie aandachtspunten verdienen opvolging in een latere sprint.

---

## C1 — Match-type verdeling

| Type | Aantal | Aandeel |
|---|---:|---:|
| `skos:closeMatch` | 1.489 | 82,8% |
| `skos:relatedMatch` | 225 | 12,5% |
| `skos:exactMatch` | 46 | 2,6% |
| `skos:broadMatch` | 38 | 2,1% |
| `skos:narrowMatch` | **0** | 0% |
| **Totaal** | **1.798** | 100% |

**Bevinding C1a — closeMatch-dominantie is verwacht en correct.** Cross-framework-mappings zijn per D4-conventie conservatief als `closeMatch` gedeclareerd tenzij de relatie sterker is. De 82,8% sluit aan op de bron-keuze-discipline uit v4.5.0 (Sheet 8 mapping-systematiek).

**Bevinding C1b — exactMatch: 46 triples verdienen audit.** D5 gebruikt `owl:sameAs` voor `ctrl:↔bio:`-bruggen (93 pairs), niet `skos:exactMatch`. De 46 exactMatch-triples zijn _geen_ D5-schendingen — ze bevinden zich in andere namespace-paren (zie C3b). Toch verdient een expliciete audit of alle 46 intentioneel zijn gedeclareerd als "conceptueel identiek", omdat exactMatch een sterke semantische claim is.

**Bevinding C1c — narrowMatch: 0.** Geen enkel framework-paar bevat een "specifieker dan"-relatie in het model. Dit is een inhoudelijke keuze, maar ook een potentiële expressiviteits-lacune: sommige BIO-controls zijn aantoonbaar specifieker dan de ISO 27002-controls waarop ze gebaseerd zijn. Aanbeveling: evalueren bij Spoor B-instroom of narrowMatch zinvol is voor BIO→ISO-richting.

---

## C2 — Namespace-paar matrix

| Bron | Doel | Mappings | Aandeel |
|---|---|---:|---:|
| `csf:` | `ext:` | 749 | 41,7% |
| `csf:` | `bio:` | 699 | 38,9% |
| `ctrl:` | `compl:` | 118 | 6,6% |
| `ext:` | `ctrl:` | 83 | 4,6% |
| `compl:` | `ctrl:` | 31 | 1,7% |
| `fw:` | `fw:` | 22 | 1,2% |
| `ctrl:` | `ctrl:` | 19 | 1,1% |
| Overige 12 paren | — | 77 | 4,3% |

**Bevinding C2a — CSF-dominantie (80,5% van alle mappings).** `csf:`-individuals genereren 1.448 van de 1.798 mappings. Dit is volledig structureel verklaard: 363 Implementation Examples × ~2 ext:-mappings + 106 Subcategories + 22 Categories + 6 Functions met BIO-targets. Geen kwaliteits-probleem — wel een beheer-implicatie: CSF-data-updates (bijv. CSF 2.1) zijn hoog-impact.

**Bevinding C2b — csf→ext (749): Implementation Examples naar ISO 27001-eisen.** De `ext:`-namespace bevat ISO 27001-vereisten (`ext:HSClause`) en andere extended-requirements. De 749 mappings zijn het directe resultaat van de Sheet 8-mapping-systematiek uit v4.5.0.

**Bevinding C2c — csf→bio (699) zonder csf→ctrl (0).** CSF mapt direct naar BIO-controls (`bio:`), niet naar ISO 27002-controls (`ctrl:`). Dit is een bewuste keuze (Sheet 8), maar creëert een indirecte relatie: voor het traject CSF → ISO 27002 moet men via D5 (ctrl:↔bio: sameAs-bruggen) redeneren. Post-inferentie is dit correct oplosbaar; pre-inferentie (explorer-view) is de relatie niet direct zichtbaar. **Aandachtspunt voor SPARQL-query-ontwerp.**

---

## C3 — Frameworks zonder uitgaande SKOS

Twee `fw:`-individuals hebben geen uitgaande SKOS-mappings:

| Individual | Verklaring |
|---|---|
| `fw:NIST_CSF_2_0` | Verwacht: mappings gaan van `csf:`-individuals, niet van het fw:-framework-individual. D9-conformant. |
| `fw:Cbb` | Verwacht: Cbb is "concept t.b.v. Tweede Kamer, nog niet vastgesteld". Geen SKOS-mappings voorzien tot inwerkingtreding + scope-besluit. |

**Geen actie vereist.** Beide gevallen zijn architectureel correct conform status-discipline (CBW/Cbb "in voorbereiding").

**C3b — exactMatch-audit (46 triples):**

| Namespace-paar | Aantal | Voorbeelden |
|---|---:|---|
| `ctrl:` → `compl:` | 28 | RiskAssessment → ISO_IEC_27005_2022 |
| `fw:` → `asset:` | 7 | (framework → asset-type) |
| `asset:` → `fw:` | 7 | (symmetrisch) |
| `risk:` → `fw:` | 2 | RiskManagementTier → NIST_SP_800_39 |
| `roles:` → `fw:` | 2 | (rol → framework) |

De ctrl→compl-exactMatches zijn semantisch plausibel (control is conceptueel identiek aan de verplichting die het afdekt). De fw→asset/asset→fw-symmetrie suggereert intentionele bidirectionele modellering. **Aanbeveling**: technische chat verifieert de 28 ctrl→compl-pairs in een latere sprint op semantische correctheid.

---

## C4 — Cross-bron overlap detectie

**Bevinding:** De 699 CSF→bio-mappings overlappen _niet_ direct met de 93 D5-bruggen (ctrl:↔bio:). De CSF mapt naar bio:-individuals (BIO-controls), de D5-bruggen verbinden ctrl:-individuals met diezelfde bio:-individuals. Post-inferentie zijn deze twee mapping-lagen complementair en consistent.

Dit is _geen_ inconsistentie — het is een bekende architecturele eigenschap. Maar het betekent wel dat voor een volledig CSF→ISO 27002-traject twee stappen nodig zijn: CSF→bio (SKOS) + bio:↔ctrl: (owl:sameAs). Dashboard en SPARQL-queries moeten dit meestap-patroon ondersteunen.

Eerder gedocumenteerde cross-bron-overlap (v4.5.0, 105 mappings Sheet 8 × Sheet 9-overlap): consistent — geen nieuw overlap-patroon gevonden in v4.6.0.

---

## C5 — Concentratie-detectie

Drie framework-paren met >100 mappings naar één target-namespace:

| Paar | Aantal | Beoordeling |
|---|---:|---|
| `csf:` → `ext:` | 749 | Structureel verklaard (zie C2b) |
| `csf:` → `bio:` | 699 | Structureel verklaard (zie C2c) |
| `ctrl:` → `compl:` | 118 | Verdient audit (zie C3b exactMatch) |

Geen onverwachte concentraties. Alle drie zijn verklaard door de architectuur of eerder gedocumenteerde mapping-besluiten.

---

## Drie aandachtspunten voor opvolging

| # | Aandachtspunt | Urgentie | Trigger |
|---|---|---|---|
| **A1** | exactMatch-audit: 28 ctrl→compl-pairs semantisch verifiëren | Laag | Volgende tech-sprint of Spoor B |
| **A2** | narrowMatch-overwegen voor BIO→ISO 27002 "specifieker dan"-relaties | Laag | Spoor B-instroom |
| **A3** | SPARQL-query-patroon documenteren voor CSF→ISO 27002 (vereist twee stappen: SKOS + owl:sameAs) | Middel | Vóór Dashboard-subagent productie-gebruik |

---

## Kanttekening bij 1.759 vs 1.798 SKOS-edges in export

De build-script-export toont 1.759 SKOS-edges (individual-niveau). De 39 overige mappings betreffen SKOS-mappings met minstens één `owl:Class`-endpoint — zelfde patroon als v4.3.x (gedocumenteerd in export-rapport v4.3.0). Geen nieuwe anomalie.

**Precisering 26 mei 2026** — root-cause-analyse `output/reports/skos-edge-discrepantie-v4_6_0.md` lokaliseert de 39 verlies-tripels exact: m03-risk (15), m18-assets (14), m07-business (10). Filter-attributie: 32 hebben een `owl:Class`-subject met Individual-object; 7 hebben een Concept-subject (TBB) met `owl:Class`-object. Geen tripel heeft beide endpoints als Class. Architectureel correct gevolg van `SCHEMA_TYPES`-filter in `build_grc_explorer_v3.py` (regel 77-86 + 482) — de explorer toont alleen ABox-individuen.

---

**Einde SKOS-kwaliteitsanalyse v4.6.0 — eerste versie.**
*Aanbeveling: herzien na Spoor B-instroom wanneer organisatie-specifieke data beschikbaar is.*
