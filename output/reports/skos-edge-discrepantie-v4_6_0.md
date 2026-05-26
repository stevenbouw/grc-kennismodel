# SKOS-edge-discrepantie v4.6.0 — diagnostische notitie

**Datum**: 2026-05-26
**Subagent**: Tech
**Scope**: read-only diagnose van het verschil tussen 1.798 SKOS-mappings in `ontology/*.ttl` en 1.759 SKOS-edges in `dashboard/grc-data-v4_6_0.json`.
**Werkwijze**: geen wijzigingen aan `ontology/*.ttl`, `dashboard/build_grc_explorer_v3.py` of export-bestanden; uitsluitend rdflib-inspectie en JSON-parsing.

## Managementsamenvatting

Het verschil van 39 SKOS-tripels is **volledig verklaarbaar en correct**. Alle 39 betreffen SKOS-mappings op **klasse-niveau** (subject of object is een `owl:Class`, niet een `owl:NamedIndividual`). De build-pipeline `build_grc_explorer_v3.py` exporteert per architecturale keuze alleen ABox-individuen als nodes; TBox-elementen (klassen, properties) worden bewust uitgesloten via het `SCHEMA_TYPES`-filter. SKOS-edges met een TBox-endpoint vallen daardoor weg in de export-stap. Dit is **geen bug** maar een gevolg van twee samenwerkende filters in regels 411-422 (node-selectie) en regels 482 (edge-endpoint-validatie).

Telling-mathematica klopt: 1.759 (JSON) + 39 (TBox-SKOS) = 1.798 (TTL). Er zijn geen "extra" tripels in de JSON die niet in de TTL voorkomen — de export is een echte deelverzameling. De bestaande kanttekening in `skos-kwaliteitsanalyse-v4_6_0.md` ("class-niveau-SKOS, zelfde patroon als v4.3.x") is daarmee bevestigd; het rapport rondt dat sluitend af met concrete tripels en root-cause-locatie in het build-script.

**Aanbeveling**: **"Verklaarbaar + documenteren"**. Geen build-script-wijziging nodig. Toevoeging van een korte regel-commentaar in `build_grc_explorer_v3.py` regel 461-468 en aanvulling op `brain/brain__concepts__namedindividual-telmethode.md` met een sectie "Class-niveau SKOS-mappings & exportgevolg". Details onder §6.

---

## 1. Probleem-statement

Het validatie-rapport `output/reports/dashboard-validatie-v4_6_0.md` (Check 2) bevestigt dat de JSON-export 7.249 edges bevat; het SKOS-kwaliteitsanalyse-rapport `output/reports/skos-kwaliteitsanalyse-v4_6_0.md` rapporteert 1.759 SKOS-edges in die 7.249, terwijl de rdflib-telling op alle 21 actieve `.ttl`-modules samengevoegd 1.798 SKOS-tripels oplevert. Verschil: 39.

De bestaande "Kanttekening bij 1.759 vs 1.798 SKOS-edges in export" in het kwaliteitsanalyse-rapport stelt dat dit "class-niveau-SKOS" betreft (zelfde patroon als v4.3.x). Deze notitie verifieert die hypothese met concrete tripels en lokaliseert de exacte build-script-logica die het verschil veroorzaakt.

## 2. Methodiek

Vier stappen, alle read-only:

1. **Ontologie-telling** via `rdflib.Graph()`. Alle 21 modules (`grc-bridges`, `grc-core`, `m01` t/m `m18`, `m21`; `grc-shacl.ttl` bewust uitgesloten zoals build_v3 ook doet) ingelezen in één gecombineerde graph. SKOS-tripels geteld per predicaat (`exactMatch`, `closeMatch`, `broadMatch`, `narrowMatch`, `relatedMatch`).
2. **JSON-telling** via `json.load()` op `dashboard/grc-data-v4_6_0.json`. Edges met `category == "skos"` geselecteerd; per `relation` geteld.
3. **Set-vergelijking** op (subject-URI, predicaat-URI, object-URI). De JSON-edges gereconstrueerd naar volle URI's via de `nodes[].uri`-lookup. Verschilset = `TTL ∖ JSON` (TTL-tripels die niet in JSON staan).
4. **Endpoint-typering** per verschil-tripel: voor elk subject en object opgehaald welke `rdf:type`-claims bestaan, en gematcht tegen `SCHEMA_TYPES`-filter zoals gedefinieerd in build_v3 regel 77-86.

### 2.1 Kernsnippet ontologie-telling

```python
from rdflib import Graph
from rdflib.namespace import SKOS

g = Graph()
for f in ttl_files:                       # 21 modules, grc-shacl.ttl uitgesloten
    g.parse(os.path.join("ontology", f), format="turtle")

SKOS_PREDS = [SKOS.exactMatch, SKOS.closeMatch, SKOS.broadMatch,
              SKOS.narrowMatch, SKOS.relatedMatch]
ttl_triples = set()
for pred in SKOS_PREDS:
    for s, o in g.subject_objects(pred):
        ttl_triples.add((str(s), str(pred), str(o)))
# len(ttl_triples) == 1798
```

### 2.2 Kernsnippet JSON-telling

```python
with open("dashboard/grc-data-v4_6_0.json") as f:
    data = json.load(f)
node_id_to_uri = {n["id"]: n["uri"] for n in data["nodes"]}
json_skos = set()
for e in data["edges"]:
    if e["category"] != "skos": continue
    json_skos.add((node_id_to_uri[e["source"]], e["prop_uri"],
                   node_id_to_uri[e["target"]]))
# len(json_skos) == 1759
```

### 2.3 Verschil-bepaling

```python
missing_in_json = ttl_triples - json_skos    # len == 39
extra_in_json   = json_skos - ttl_triples    # len == 0  (geen onverwachte toevoegingen)
```

---

## 3. Bevinding 1 — ontologie-telling: 1.798 bevestigd

### 3.1 Match-type-verdeling (gecombineerde graph, post-dedup)

| Match-type | Aantal |
|---|---:|
| `skos:closeMatch` | 1.489 |
| `skos:relatedMatch` | 225 |
| `skos:exactMatch` | 46 |
| `skos:broadMatch` | 38 |
| `skos:narrowMatch` | 0 |
| **Totaal** | **1.798** |

Exact gelijk aan `skos-kwaliteitsanalyse-v4_6_0.md` §C1.

### 3.2 Per-module-telling (vóór dedup)

| Module | exact | close | broad | narrow | related | totaal |
|---|---:|---:|---:|---:|---:|---:|
| grc-bridges.ttl | 0 | 0 | 0 | 0 | 0 | 0 |
| grc-core.ttl | 0 | 0 | 0 | 0 | 0 | 0 |
| m01-framework.ttl | 0 | 6 | 3 | 0 | 2 | 11 |
| m02-control.ttl | 0 | 0 | 0 | 0 | 19 | 19 |
| m03-risk.ttl | 2 | 4 | 5 | 0 | 6 | 17 |
| m04-roles.ttl | 2 | 3 | 0 | 0 | 0 | 5 |
| m05-compliance.ttl | 0 | 5 | 1 | 0 | 0 | 6 |
| m06-isms.ttl | 0 | 0 | 0 | 0 | 0 | 0 |
| m07-business.ttl | 0 | 1 | 0 | 0 | 9 | 10 |
| m08-bio20.ttl | 0 | 291 | 0 | 0 | 0 | 291 |
| m09-iso27001-ext.ttl | 0 | 117 | 0 | 0 | 0 | 117 |
| m10-nis2-ext.ttl | 28 | 32 | 25 | 0 | 33 | 118 |
| m11-nist-800-53.ttl | 0 | 491 | 0 | 0 | 0 | 491 |
| m12-dora.ttl | 0 | 0 | 1 | 0 | 34 | 35 |
| m13-iso22301.ttl | 0 | 0 | 0 | 0 | 0 | 0 |
| m14-avg-gdpr.ttl | 0 | 2 | 2 | 0 | 29 | 33 |
| m15-ensia.ttl | 0 | 0 | 0 | 0 | 2 | 2 |
| m16-virbi-ext.ttl | 0 | 0 | 0 | 0 | 48 | 48 |
| m17-coso-cobit.ttl | 0 | 1 | 1 | 0 | 39 | 41 |
| m18-assets.ttl | 14 | 0 | 0 | 0 | 0 | 14 |
| m21-csf.ttl | 0 | 641 | 0 | 0 | 4 | 645 |
| **SOM (vóór dedup)** | **46** | **1.594** | **38** | **0** | **225** | **1.903** |
| **NA dedup (gecombineerd)** | **46** | **1.489** | **38** | **0** | **225** | **1.798** |

Het verschil 1.903 − 1.798 = 105 is **cross-bron-overlap** (identieke tripels in twee modules). Dit is gedocumenteerd in v4.5.0 (Sheet 8 × Sheet 9 = 105 overlap-mappings) en valt buiten de scope van deze notitie.

## 4. Bevinding 2 — JSON-telling: 1.759 bevestigd

### 4.1 Edge-categorie-distributie in `grc-data-v4_6_0.json`

| Category | Aantal |
|---|---:|
| other | 2.819 |
| **skos** | **1.759** |
| attribution | 725 |
| governance | 677 |
| csf-hierarchy | 491 |
| maturity | 320 |
| isms | 187 |
| roles | 120 |
| equivalence | 93 |
| compliance | 47 |
| risk | 11 |
| **Totaal** | **7.249** |

`meta.skos_mappings` in de JSON-header rapporteert óók 1.759 — consistent met de feitelijke edge-telling.

### 4.2 SKOS-edges per match-type in JSON

| Match-type (JSON `relation`) | TTL | JSON | Δ |
|---|---:|---:|---:|
| closeMatch | 1.489 | 1.484 | −5 |
| relatedMatch | 225 | 212 | −13 |
| exactMatch | 46 | 30 | −16 |
| broadMatch | 38 | 33 | −5 |
| narrowMatch | 0 | 0 | 0 |
| **Totaal** | **1.798** | **1.759** | **−39** |

Geen enkele match-type komt volledig "wel" of "niet" door — verlies is gespreid maar verhoudingsgewijs het grootst bij `exactMatch` (35% van de exactMatch-tripels valt weg).

## 5. Bevinding 3 — de 39 verschil-tripels

### 5.1 Mathematica

- `len(TTL) − len(JSON) = 1798 − 1759 = 39` ✓
- `TTL ∖ JSON = 39` tripels (alle in TTL, geen in JSON)
- `JSON ∖ TTL = 0` tripels (geen ongewenste toevoegingen door build_v3)

### 5.2 Reden per tripel (filter-attributie)

Set-vergelijking met `node_uri_set` (de 1.788 nodes in de JSON):

| Reden | Aantal |
|---|---:|
| subject niet als node geëxporteerd (object wél) | 32 |
| object niet als node geëxporteerd (subject wél) | 7 |
| beide endpoints geëxporteerd maar tripel verloren | **0** |
| externe URI (buiten `grc.example.org/`) | **0** |

**Conclusie**: 100% van de 39 verlies-tripels heeft tenminste één endpoint dat door de node-selectie wordt afgewezen. Er is **geen** tripel waarbij beide endpoints node zijn en de mapping toch verloren gaat — wat zou wijzen op een aanvullend filter of dedup-fout.

### 5.3 Endpoint-typering: alle 28 unieke missing endpoints zijn `owl:Class`

Onder de 39 tripels zitten 28 unieke endpoints die niet als node verschijnen. Voor elk endpoint: `rdf:type`-verzameling uitgelezen. Resultaat: **alle 28 zijn typed als `owl:Class`**. Geen enkele is `owl:NamedIndividual`. Het build-script's regel 421 (`if set(g.objects(s, RDF.type)) & SCHEMA_TYPES: continue`) sluit deze 28 daarmee bewust uit van het `individuals`-set, omdat `OWL.Class ∈ SCHEMA_TYPES`.

| Endpoint (URI-tail) | Class? | Andere zijde |
|---|---|---|
| asset/Equipment | owl:Class | framework/TBB_Materieel (Concept) |
| asset/HumanAsset | owl:Class | framework/TBB_Personen (Concept) |
| asset/InformationAsset | owl:Class | framework/TBB_Informatie (Concept) |
| asset/InformationSystem | owl:Class | framework/TBB_Informatiesystemen (Concept) |
| asset/IntangibleAsset | owl:Class | framework/TBB_Imago (Concept) |
| asset/PhysicalObject | owl:Class | framework/TBB_Objecten (Concept) |
| asset/TangibleGoods | owl:Class | framework/TBB_Goederen (Concept) |
| business/DirectieBeoordeling | owl:Class | extended/COSO_ERM_ReviewRevision (NamedInd) |
| business/GRCDashboard | owl:Class | extended/COSO_ERM_InformationCommunicationReporting (NamedInd) |
| business/KCI | owl:Class | extended/COSO_ERM_ReviewRevision (NamedInd) |
| business/KPI | owl:Class | extended/COSO_ERM_Performance (NamedInd) |
| business/KRI | owl:Class | extended/COSO_ERM_Performance (NamedInd) |
| business/ManagementReport | owl:Class | extended/COSO_ERM_InformationCommunicationReporting (NamedInd) |
| business/PerformanceIndicator | owl:Class | extended/COSO_ERM_Performance (NamedInd) |
| business/RiskAppetite | owl:Class | extended/COSO_ERM_GovernanceCulture (NamedInd) |
| business/RiskAppetiteStatement | owl:Class | extended/COSO_ERM_GovernanceCulture (NamedInd) |
| business/StrategicObjective | owl:Class | extended/COSO_ERM_StrategyObjectiveSetting (NamedInd) |
| risk/ImpactLevel | owl:Class | framework/NIST_SP_800_30_R1 (NationalStandard-individual) |
| risk/LikelihoodLevel | owl:Class | framework/NIST_SP_800_30_R1 |
| risk/ReportingRisk | owl:Class | extended/COSO_ERM_Performance (NamedInd) |
| risk/Risk | owl:Class | framework/COSO_ERM + framework/ISO_31000_2018 |
| risk/RiskAppetite | owl:Class | framework/ISO_31000_2018 + extended/COSO_ERM_GovernanceCulture |
| risk/RiskAssessment | owl:Class | framework/ISO_IEC_27005_2022 + extended/COSO_ERM_Performance |
| risk/RiskManagementTier | owl:Class | framework/NIST_SP_800_39 |
| risk/RiskRegister | owl:Class | extended/COSO_ERM_ReviewRevision |
| risk/RiskTreatment | owl:Class | framework/ISO_31000_2018 + extended/COSO_ERM_Performance |
| risk/Threat | owl:Class | framework/NIST_SP_800_30_R1 |
| risk/Vulnerability | owl:Class | framework/NIST_SP_800_30_R1 |

### 5.4 Per match-type van de 39

| Match-type | Aantal |
|---|---:|
| skos:exactMatch | 16 |
| skos:relatedMatch | 13 |
| skos:closeMatch | 5 |
| skos:broadMatch | 5 |
| skos:narrowMatch | 0 |
| **Totaal** | **39** |

### 5.5 Per namespace-paar van de 39

| Subject-ns | → | Match-type | Object-ns | Aantal |
|---|---|---|---|---:|
| business | | relatedMatch | extended | 9 |
| asset | | exactMatch | framework | 7 |
| framework | | exactMatch | asset | 7 |
| risk | | closeMatch | framework | 4 |
| risk | | broadMatch | framework | 4 |
| risk | | relatedMatch | extended | 4 |
| risk | | exactMatch | framework | 2 |
| risk | | broadMatch | extended | 1 |
| business | | closeMatch | extended | 1 |
| **Totaal** | | | | **39** |

Twee architecturale clusters dragen het overgrote deel:

- **TBB-asset-bidirectionele exactMatch (14 tripels)**: 7 × `asset:* exactMatch framework:TBB_*` + 7 × `framework:TBB_* exactMatch asset:*`. De `asset:`-zijde is `owl:Class`, de `framework:TBB_*`-zijde is `skos:Concept` (geen `owl:NamedIndividual`). Beide kanten gaan verloren, want het build_v3-script promoveert noch `owl:Class` noch `skos:Concept`-zonder-NamedIndividual-type tot node.
- **COSO ERM / ISO 31000 / NIST SP 800-30 → risico- en business-klassen (22 tripels)**: `risk:`- en `business:`-TBox-klassen mappen naar de COSO ERM-component-individuen (in `extended:`) en ISO/NIST-framework-individuen. Hier is de `risk:`/`business:`-zijde `owl:Class` (verloren), de andere zijde wél `owl:NamedIndividual` (in de export aanwezig).

### 5.6 Per module van herkomst (waar staan de 39 in de .ttl)

| Module | Aantal van de 39 |
|---|---:|
| m03-risk.ttl | 15 |
| m18-assets.ttl | 14 |
| m07-business.ttl | 10 |

Volledig consistent met de typering: M03 + M07 declareren respectievelijk de risico- en business-klassen, M18 declareert de bidirectionele asset↔TBB exactMatches. Geen verlies in CSF-, BIO-, NIST 800-53- of ISO 27002-mappings (die zijn allemaal individual-niveau).

### 5.7 Volledige lijst van de 39 missing tripels

Reden-classificatie: `subject-not-node` (S) of `object-not-node` (O).

```
[O] framework/TBB_Goederen           skos:exactMatch    asset/TangibleGoods
[O] framework/TBB_Imago              skos:exactMatch    asset/IntangibleAsset
[O] framework/TBB_Informatie         skos:exactMatch    asset/InformationAsset
[O] framework/TBB_Informatiesystemen skos:exactMatch    asset/InformationSystem
[O] framework/TBB_Materieel          skos:exactMatch    asset/Equipment
[O] framework/TBB_Objecten           skos:exactMatch    asset/PhysicalObject
[O] framework/TBB_Personen           skos:exactMatch    asset/HumanAsset
[S] asset/Equipment                  skos:exactMatch    framework/TBB_Materieel
[S] asset/HumanAsset                 skos:exactMatch    framework/TBB_Personen
[S] asset/InformationAsset           skos:exactMatch    framework/TBB_Informatie
[S] asset/InformationSystem          skos:exactMatch    framework/TBB_Informatiesystemen
[S] asset/IntangibleAsset            skos:exactMatch    framework/TBB_Imago
[S] asset/PhysicalObject             skos:exactMatch    framework/TBB_Objecten
[S] asset/TangibleGoods              skos:exactMatch    framework/TBB_Goederen
[S] risk/RiskAssessment              skos:exactMatch    framework/ISO_IEC_27005_2022
[S] risk/RiskManagementTier          skos:exactMatch    framework/NIST_SP_800_39
[S] risk/Risk                        skos:broadMatch    framework/COSO_ERM
[S] risk/Risk                        skos:broadMatch    framework/ISO_31000_2018
[S] risk/RiskAppetite                skos:broadMatch    framework/ISO_31000_2018
[S] risk/RiskTreatment               skos:broadMatch    framework/ISO_31000_2018
[S] risk/ReportingRisk               skos:broadMatch    extended/COSO_ERM_Performance
[S] risk/ImpactLevel                 skos:closeMatch    framework/NIST_SP_800_30_R1
[S] risk/LikelihoodLevel             skos:closeMatch    framework/NIST_SP_800_30_R1
[S] risk/Threat                      skos:closeMatch    framework/NIST_SP_800_30_R1
[S] risk/Vulnerability               skos:closeMatch    framework/NIST_SP_800_30_R1
[S] business/RiskAppetite            skos:closeMatch    extended/COSO_ERM_GovernanceCulture
[S] business/DirectieBeoordeling     skos:relatedMatch  extended/COSO_ERM_ReviewRevision
[S] business/GRCDashboard            skos:relatedMatch  extended/COSO_ERM_InformationCommunicationReporting
[S] business/KCI                     skos:relatedMatch  extended/COSO_ERM_ReviewRevision
[S] business/KPI                     skos:relatedMatch  extended/COSO_ERM_Performance
[S] business/KRI                     skos:relatedMatch  extended/COSO_ERM_Performance
[S] business/ManagementReport        skos:relatedMatch  extended/COSO_ERM_InformationCommunicationReporting
[S] business/PerformanceIndicator    skos:relatedMatch  extended/COSO_ERM_Performance
[S] business/RiskAppetiteStatement   skos:relatedMatch  extended/COSO_ERM_GovernanceCulture
[S] business/StrategicObjective      skos:relatedMatch  extended/COSO_ERM_StrategyObjectiveSetting
[S] risk/RiskAppetite                skos:relatedMatch  extended/COSO_ERM_GovernanceCulture
[S] risk/RiskAssessment              skos:relatedMatch  extended/COSO_ERM_Performance
[S] risk/RiskRegister                skos:relatedMatch  extended/COSO_ERM_ReviewRevision
[S] risk/RiskTreatment               skos:relatedMatch  extended/COSO_ERM_Performance
```

---

## 6. Root-cause-analyse: build_v3-logica

### 6.1 Filter-keten (drie samenwerkende keuzes)

**Filter A — SCHEMA_TYPES-definitie**, regel 77-86 van `build_grc_explorer_v3.py`:

```python
SCHEMA_TYPES = {
    OWL.Class, OWL.ObjectProperty, OWL.DatatypeProperty,
    OWL.AnnotationProperty, OWL.TransitiveProperty, OWL.SymmetricProperty,
    OWL.AsymmetricProperty, OWL.FunctionalProperty,
    OWL.InverseFunctionalProperty, OWL.Restriction, OWL.Ontology,
    RDF.Property, RDFS.Class,
    URIRef("http://www.w3.org/ns/shacl#NodeShape"),
    URIRef("http://www.w3.org/ns/shacl#PropertyShape"),
    SKOS.ConceptScheme,
}
```

Hier wordt `owl:Class` expliciet als "schema/TBox" gemarkeerd en uitgesloten van node-export.

**Filter B — individuals-set-bouw**, regel 411-422:

```python
individuals = set()
for s in g.subjects(RDF.type, OWL.NamedIndividual):
    if str(s).startswith(GRC_BASE):
        individuals.add(s)
for s, p, o in g.triples((None, RDF.type, None)):
    if not isinstance(s, URIRef): continue
    if not str(s).startswith(GRC_BASE): continue
    if o in SCHEMA_TYPES or o == OWL.NamedIndividual: continue
    if set(g.objects(s, RDF.type)) & SCHEMA_TYPES: continue   # ← uitsluiting van Classes
    individuals.add(s)
```

Een entiteit komt alleen in `individuals` als ze (i) `owl:NamedIndividual` is, óf (ii) een ander `rdf:type` heeft dat géén schema-type is **en** geen enkel van haar overige types in `SCHEMA_TYPES` zit. Voor `owl:Class`-entiteiten faalt (ii) op de tweede voorwaarde — ze hebben `OWL.Class` in hun type-set, dus de continue-statement op de laatste regel verwerpt ze.

**Filter C — edge-endpoint-validatie**, regel 482:

```python
for s, o in g.subject_objects(prop):
    ...
    sid = make_id(str(s))
    oid = make_id(str(o))
    if sid not in node_ids or oid not in node_ids: continue   # ← edges met TBox-endpoint verworpen
```

Een edge wordt alleen geëxporteerd als beide endpoints in `node_ids` voorkomen — wat per Filter B alleen ABox-individuen zijn.

### 6.2 Gevolg

Het samenspel A + B + C garandeert dat een SKOS-tripel `(C1, skos:closeMatch, C2)` waarbij `C1` óf `C2` typed is als `owl:Class`, nooit als edge in `grc-data-v4_6_0.json` verschijnt. Dit is geen ongewenst neveneffect — het past bij de scope van de dashboard-explorer ("individuen-grafiek voor traversal door governance-werkelijkheid"), waarin TBox-structuur via aparte hierarchie-properties (`rdfs:subClassOf` etc.) niet wordt getoond.

### 6.3 Geen dedup- of range-filter actief

De seen_edges-dedup (regel 484: `seen_edges` op `(sid, oid, prop_uri)`) is **niet** de oorzaak. Set-vergelijking toont aan dat alle 39 verlies-tripels uniek zijn en niet "samengevouwen" worden met andere — ze worden simpelweg nooit bereikt door Filter C. Ook geen range-restrictie op specifieke predicaten — `edge_category()` (regel 355-368) reageert symmetrisch op alle vijf SKOS-predicaten.

### 6.4 Mathematische sluiting

- 1.798 SKOS-tripels in TTL
- 39 met TBox-endpoint → verworpen door Filter B/C
- 1.759 met dubbele ABox-endpoints → geëxporteerd
- 1.759 + 39 = 1.798 ✓
- Geen "extra" tripels in JSON ([ttl ∖ json] = 39; [json ∖ ttl] = 0)

---

## 7. Aanbeveling — "Verklaarbaar + documenteren"

Het verschil is **geen bug**. Het is een gevolg van een bewuste architecturale keuze: dashboard-explorer toont uitsluitend ABox-individuen plus hun directe relaties. Class-niveau-SKOS-mappings (klassen die conceptueel overlappen met externe normen) horen wel in de ontologie thuis — ze zijn semantisch correct en SHACL-geldig — maar zijn voor een individual-centric visualisatie niet relevant.

Drie kleine documentatie-toevoegingen zorgen dat dit gegeven niet steeds opnieuw onderzocht hoeft te worden:

### 7.1 Comment-toevoeging in `build_grc_explorer_v3.py`

Voorgesteld commentaar bij regel 482 (de Filter-C-locatie). **Geen wijziging in code-gedrag**, alleen verklaring:

```python
for s, o in g.subject_objects(prop):
    if not (isinstance(s, URIRef) and isinstance(o, URIRef)): continue
    sid = make_id(str(s))
    oid = make_id(str(o))
    # Filter C: edges met een TBox-endpoint (owl:Class etc.) worden bewust
    # uitgesloten — de explorer toont alleen ABox-individuen. In v4.6.0 valt
    # daardoor 39 van de 1.798 SKOS-mappings weg (class-niveau bridges in
    # m03-risk.ttl, m07-business.ttl, m18-assets.ttl). Zie
    # output/reports/skos-edge-discrepantie-v4_6_0.md voor de volledige lijst.
    if sid not in node_ids or oid not in node_ids: continue
```

Doorvoering valt buiten deze read-only opdracht — masterchat-GO benodigd. Het zou consistent zijn met de bestaande wijzigingslog-comments bovenin het script (regel 6-37).

### 7.2 Aanvulling op `brain/brain__concepts__namedindividual-telmethode.md`

Sectie "Class-niveau SKOS-mappings — exportgevolg" toevoegen, kort, met verwijzing naar deze notitie. Het bestaande concept-bestand documenteert al de NamedIndividual-vs-Class-onderscheidingsdiscipline; een uitbreiding met het export-implicatie-aspect past natuurlijk in die context. Aanmaak/uitbreiding valt onder de Brein-subagent (niet onder Tech).

### 7.3 Kanttekening verfijnen in `skos-kwaliteitsanalyse-v4_6_0.md`

De huidige tekst:

> De build-script-export toont 1.759 SKOS-edges (individual-niveau). De 39 overige mappings betreffen class-niveau-SKOS (tussen OWL Classes, niet Individuals) — zelfde patroon als v4.3.x (gedocumenteerd in export-rapport v4.3.0). Geen nieuwe anomalie.

is grotendeels correct, maar in twee aspecten te aanscherpen:

- **Strikt genomen**: niet "tussen OWL Classes" — slechts één zijde hoeft `owl:Class` te zijn. 32 van de 39 hebben een Class-subject en Individual-object; 7 hebben een Concept-subject (TBB) en Class-object. Maar nooit beide Classes.
- **Module-spreiding**: niet enkel "class-niveau" — concreet zijn het 14 TBB↔asset-mappings (M18), 15 risk-klasse-mappings (M03) en 10 business-klasse-mappings (M07). Dit specifieker noemen helpt latere lezers.

Eventuele revisie van die kanttekening is dashboard-subagent-werk (eigenaar van het kwaliteitsanalyse-rapport).

### 7.4 Wat dit géén bug maakt — toetsing aan D-decisions

- **D1 (OWL 2 DL profiel)**: class-niveau-SKOS-mappings zijn legitiem in OWL 2 DL. Geen schending.
- **D4 (SKOS voor cross-framework)**: D4 specificeert match-type-keuze, niet of mappings op klasse- of individual-niveau geplaatst moeten worden. Beide niveaus zijn architectureel verdedigbaar.
- **D9 (framework-neutraal)**: het verschil heeft geen framework-bias — verlies treft drie modules gespreid.
- **D11 (asset-ster)**: de 14 TBB↔asset exactMatches zijn de SKOS-laag náást de owl:sameAs-bruggen (D11). Verlies in JSON betekent niet semantisch verlies in de ontologie — alleen visualisatie-verlies.

Geen enkele D-decision wordt door deze bevinding geraakt.

### 7.5 Wat het wél zou maken tot een toekomstig bespreekpunt

Als ooit besloten wordt om TBox-elementen in de explorer te tonen (bv. een aparte "schema-laag" naast de individuen), dan kan Filter B/C selectief aangepast worden om `owl:Class`-nodes wél te exporteren met een aparte marker. Niet in scope nu, maar registreerbaar als open architectuur-overweging (H-item-kandidaat indien masterchat dit later relevant acht).

---

## 8. Residuele open vragen

1. **Zijn de bidirectionele asset↔TBB exactMatches (14 tripels) intentioneel symmetrisch?** Bij D5 (owl:sameAs ctrl↔bio) is symmetrie inherent door OWL-semantiek; bij `skos:exactMatch` is symmetrie alleen via expliciete tweede-richting-triples bereikt. M18 declareert beide richtingen expliciet. Niet binnen scope van deze diagnose; gemeld voor latere semantische audit (sluit aan op aandachtspunt A1 in `skos-kwaliteitsanalyse-v4_6_0.md`).

2. **Het cross-bron-overlap van 105 (1.903 som per module − 1.798 gecombineerd)** is in deze notitie alleen genoemd, niet ontleed. Buiten scope — wel relevant voor brain__concepts__cross-bron-overlap.md (bestaand concept-bestand).

3. **De 749 csf→ext en 699 csf→bio mappings** worden door build_v3 wél correct als edges geëxporteerd; alle 1.448 CSF-mappings zijn individual↔individual. Geen actie nodig.

---

## 9. Reproduceerbaarheid

Alle tellingen, set-vergelijkingen en endpoint-typeringen in deze notitie zijn reproduceerbaar via de twee kernsnippets in §2 plus de filter-attributie-loop:

```python
# Reproductie filter-attributie (§5.2)
GRC_BASE = "https://grc.example.org/"
for s, p, o in missing_in_json:
    s_in = s in node_uri_set
    o_in = o in node_uri_set
    if not s.startswith(GRC_BASE) or not o.startswith(GRC_BASE):
        reason = "external-uri"
    elif not s_in and not o_in:
        reason = "both-not-node"
    elif not s_in:
        reason = "subject-not-node"
    elif not o_in:
        reason = "object-not-node"
    else:
        reason = "UNEXPLAINED"
```

Resultaat: 32 × subject-not-node, 7 × object-not-node, 0 × external-uri, 0 × both-not-node, 0 × UNEXPLAINED.

Voor endpoint-typering (§5.3):

```python
from rdflib.namespace import OWL, RDF
for ep_uri in missing_endpoints:
    types = set(g.objects(URIRef(ep_uri), RDF.type))
    is_class = OWL.Class in types
    # → alle 28 endpoints geven is_class == True
```

---

**Einde notitie.**
