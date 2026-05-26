# Dashboard-export rapport — v4.3.0
**Werkpakket:** H1–H8 build-script export-fix
**Script:** `build_grc_explorer_v2.py`
**Opgesteld door:** Dashboard-chat
**Datum:** 14 april 2026
**Basis:** v4.3.0-snapshot (20 TTL-bestanden, 12.354 triples)

---

## Samenvatting

Alle acht bevindingen (H1–H8) zijn opgelost. Het herziene script `build_grc_explorer_v2.py` exporteert nu de volledige contextrijkdom van het v4.3.0-model. De meest impactvolle wijziging is de literal-export (H5): 43% van de model-triples (5.319 literals) was voorheen volledig onzichtbaar in de explorer — dat is nu opgelost. ISO 27002-controls hebben nu echte titels in plaats van IRI-fragmenten (H4). De governance-graaf is correct en volledig (H1–H3). De output bevat een traceeerbare versie-header (H8).

---

## Before/after kerngetallen

| Metric | v1 (oud) | v2 (nieuw) | Verschil |
|---|---:|---:|---:|
| TTL-bestanden geladen | 18 (schatting) | **20** | +2 |
| Triples | ~12.151 | **12.354** | +203 |
| Nodes (individuals) | ~615 | **1.036** | +421 |
| Edges totaal | onbekend | **3.671** | n.v.t. |
| Governance-edges | 0 (non-existente props) | **147** | +147 |
| SKOS-edges | 307 | **307** | 0* |
| Equivalence (owl:sameAs) | ~93 | **93** | 0† |
| Nodes met `label` uit hasControlTitle | 0 | **93** | +93 |
| Nodes met IRI-fragment als fallback-label | ~93 | **0** | −93 |
| Nodes met `description` | 0 | **320** | +320 |
| Nodes met `control_id` | 0 | **217** | +217 |
| Nodes met `attributes` (6 ISO 27002-attr.) | 0 | **93** | +93 |
| Nodes met `bbn` | 0 | **241** | +241 |
| Nodes met `requirement_text` | 0 | **93** | +93 |
| Nodes met `iso_clause` | 0 | **58** | +58 |
| Nodes met `law_article` | 0 | **20** | +20 |
| Nodes met `control_family_code` | 0 | **20** | +20 |
| Outputbestand voorzien van versie-header | nee | **ja** | ✓ |
| Outputbestandsgrootte (JS) | ~klein | **1.052 KB** | n.v.t. |

\* Zie toelichting H5/SKOS hieronder.
† Zie toelichting D11 hieronder.

---

## Impact per bevinding H1–H8

### H1 — `fw:implementeert` + `fw:baseertOp` verwijderd ✅

**Probleem:** twee non-existente properties in `GOVERNANCE_PROPS` (0 triples, 0 declaraties in model).
**Oplossing:** volledig verwijderd.
**Impact:** geen valse governance-edges meer; geen verborgen fouten in edge-categorisatie.

---

### H2 — 8 ontbrekende governance-properties toegevoegd ✅

**Probleem:** `GOVERNANCE_PROPS` bevatte slechts 3 properties; 8 echte governance-properties ontbraken.
**Oplossing:** correcte set van 10 properties:

| Property | Triples in model | Categorie |
|---|---:|---|
| `fw:stelVerplicht` | 1 | governance |
| `fw:geeftRichtlijnenVoor` | 1 | governance |
| `fw:geeftITInvullingAan` | 2 | governance |
| `fw:dektAf` | 1 | governance |
| `fw:toetst` | 1 | governance |
| `fw:transposedBy` | 1 | governance |
| `fw:supersedes` | 3 | governance |
| `fw:alignsWith` | 5 | governance |
| `ext:isComponentOf` | 19 | governance |
| `ctrl:belongsToFramework` | 113 | governance (H6 toevoeging) |

**Impact:** governance-graaf stijgt van 0 naar **147 edges**.

---

### H3 — Dubbele GOVERNANCE_PROPS-declaratie verwijderd ✅

**Probleem:** regels 41-58 declareerden `GOVERNANCE_PROPS` twee maal; de eerste (set-syntax, onjuist) werd overschreven door de tweede (dict), maar de dubbele declaratie veroorzaakte verwarring en de set-versie beperkte `fw:implementeert` en `fw:baseertOp` als nep-filter.
**Oplossing:** één correcte dict-declaratie.

---

### H4 — `ctrl:hasControlTitle` als label-fallback ✅

**Probleem:** alle 93 ISO 27002-controls hadden hun titel uitsluitend in `ctrl:hasControlTitle@nl`; het script kende deze property niet en viel terug op de IRI-lokale naam (bijv. `ISO27002_5_01`).
**Oplossing:** label-opzoek-keten uitgebreid:
1. `rdfs:label@nl`
2. `rdfs:label@en`
3. `ctrl:hasControlTitle@nl` ← nieuw
4. `ctrl:hasControlTitle@en` ← nieuw
5. `rdfs:label` (geen taal)
6. `skos:prefLabel`
7. IRI-lokale naam (laatste fallback)

**Resultaat:** 0 IRI-fragment-fallbacks op ctrl:-nodes (was: ~93).

**Voorbeeld na fix:**
```json
{
  "id": "ctrl:ISO27002_7_06",
  "label": "Werken in beveiligde zones",
  "control_id": "7.06",
  ...
}
```

---

### H5 — Literal-export toegevoegd ✅

**Probleem:** 5.319 van 12.354 triples (43,1%) zijn literals — volledig onzichtbaar in de oude export.
**Oplossing:** per node worden de volgende velden geëxporteerd waar van toepassing:

| Veld | Bron | Nodes |
|---|---|---:|
| `description` | `rdfs:comment@nl/en` | 320 |
| `control_id` | `ctrl:hasControlID` | 217 |
| `control_title` | `ctrl:hasControlTitle@nl/en` | 93 |
| `attributes` | 6 ISO 27002-attributen (`ctrl:has*`) | 93 |
| `bbn` | `ext:hasHandreikingBBN` (xsd:integer, waarden 1 of 2) | 241 |
| `requirement_text` | `compl:requirementText@nl/en` | 93 |
| `iso_clause` | `ext:clauseNumber` | 58 |
| `law_article` | `ext:articleNumber` | 20 |
| `control_family_code` | `ext:controlFamilyCode` | 20 |

**Voorbeeld ISO 27002-control (volledig):**
```json
{
  "id": "ctrl:ISO27002_7_06",
  "label": "Werken in beveiligde zones",
  "label_en": null,
  "type": "ISO27002Control",
  "namespace": "ctrl",
  "laag": 4,
  "laag_naam": "Normen (ISO/NIST)",
  "control_id": "7.06",
  "control_title": { "nl": "Werken in beveiligde zones" },
  "attributes": {
    "control_type": ["Preventief"],
    "security_properties": ["Beschikbaarheid", "Integriteit", "Vertrouwelijkheid"],
    "cybersecurity_concept": ["Beschermen"],
    "operational_capability": ["OC_FysiekeBeveiliging"],
    "security_domain": ["SD_Bescherming"],
    "theme": ["Fysiek"]
  }
}
```

**Voorbeeld ISMSRequirement-node (met requirement_text + iso_clause):**
```json
{
  "id": "ext:ISO27001_7_5_3",
  "label": "Beheersing van gedocumenteerde informatie",
  "label_en": "Control of documented information",
  "type": "ISMSRequirement",
  "requirement_text": {
    "nl": "Gedocumenteerde informatie vereist door het ISMS en door deze norm wordt beheerd...",
    "en": null
  },
  "iso_clause": "7.5.3"
}
```

---

### H6 — TBox-relaties uitgesloten; `ctrl:belongsToFramework` toegevoegd ✅

**Probleem (H6 deels):** `rdfs:domain`, `rdfs:range`, `rdfs:subClassOf` waren potentieel zichtbaar als edges. `ctrl:belongsToFramework` (113 triples) ontbrak als categorie.
**Oplossing:** `TBOX_PREDICATES`-set met 15 predicaten die altijd worden overgeslagen. `ctrl:belongsToFramework` toegevoegd aan `GOVERNANCE_PROPS` als categorie `governance`.

**Opmerking H6 architecturaal (model-driven laag-toewijzing):** de heuristische `bepaal_laag()` blijft staan conform de instructie — dit is een open punt voor masterchat (eventuele toevoeging van `fw:laag`-property in v4.3.1).

---

### H7 — v4.3.0-snapshot ✅

**Probleem:** script draaide op ~18-bestandssnapshot (v4.2.1-basis), miste `grc-core.ttl` en `grc-bridges.ttl`.
**Oplossing:** draait nu op alle 20 TTL-bestanden, 12.354 triples.
**Inhoud die nu correct aanwezig is:**
- 5 D11 `owl:sameAs`-bruggen (asset:↔risk:↔isms: klassenniveau — zie toelichting)
- Nieuwe klasse `risk:ReportingRisk` (G4)
- Nieuwe property `isms:forRisk` (G2)
- Nieuwe altLabel `"Consequence"@en` op `risk:Impact` (G5)

---

### H8 — Versie-header in output ✅

**Probleem:** geen traceerbaarheid over welke model-versie achter een gegeven snapshot zit.
**Oplossing:** `meta`-object in outputbestand:

```json
"meta": {
  "generated": "2026-04-14T...",
  "ontology_version": "4.3.0",
  "ontology_version_iri": "https://grc.example.org/ontology/v4.3.0/",
  "source_files": ["grc-bridges.ttl", "grc-core.ttl", ...],
  "source_files_count": 20,
  "source_files_hash": "9e39fe6eca791a17...",
  "script_version": "build_grc_explorer v2.0",
  "triples_loaded": 12354,
  "individuals": 1036,
  "edges": 3671,
  "skos_mappings": 307,
  "governance_edges": 147
}
```

`owl:versionInfo` wordt uitgelezen uit `grc-core.ttl`; `source_files_hash` is SHA256 van alle input-TTL's.

---

## Twee technische bevindingen voor masterchat

### Bevinding I — D11-bruggen niet zichtbaar als edges (architectureel correct)

De 5 D11 `owl:sameAs`-bruggen (asset:↔risk:↔isms:) zijn **class-level** bruggen — ze verbinden OWL Classes, niet NamedIndividuals. Het script filtert classes terecht als schema-elementen. Zij zijn dus niet exporteerbaar als nodes of edges in de individual-gerichte explorer-export.

Dit is **architectureel correct gedrag**: D11 werkt op TBox-niveau en materialiseert via OWL RL-inferentie op instance-niveau. De effecten van D11 zijn wél zichtbaar in de post-inferentie-analyse (contextdiepte-diagnostiek A.1.3: asset_pre→asset_post verdubbeling).

**Geen actie vereist** op het model of het script. Documenteer dit als bekende beperking van de pre-inferentie explorer-export.

---

### Bevinding II — SKOS: 307 van 346 in export (correct, rest is schema-niveau)

De export toont 307 SKOS-mappings; canonical telt 346. Het verschil van 39 is volledig verklaard: die 39 mappings betreffen SKOS-relaties waarbij minstens één kant een OWL Class is (bijv. `risk:RiskAssessment`, `risk:RiskManagementTier`, `asset:HumanAsset`, `asset:InformationAsset`). Classes worden terecht uitgesloten. De 307 geëxporteerde mappings zijn alle individual-niveau-relaties.

**Geen actie vereist.** Cijfers zijn consistent. In communicatie: rapporteer 307 als "SKOS-edges in explorer" en 346 als "SKOS-mappings in model (inclusief class-niveau)".

---

## Oplevering

| Bestand | Omschrijving | Grootte |
|---|---|---|
| `build_grc_explorer_v2.py` | Herzien build-script | — |
| `grc-data-v4.3.0.js` | Nieuwe snapshot (browser-standalone) | 1.052 KB |
| `grc-data-v4.3.0.json` | Nieuwe snapshot (machine-leesbaar) | 1.314 KB |
| `dashboard-export-rapport-v4.3.0.md` | Dit rapport | — |

---

## Volgende stap (buiten scope dit werkpakket)

De UI-aanpassing van `grc-explorer.html` — zodat de nieuwe velden (`description`, `attributes`, `bbn`, etc.) ook zichtbaar worden in het scherm — is een apart werkpakket. De data is er nu; de viewer moet worden uitgebreid om er gebruik van te maken. Afstemmen met masterchat over prioriteit.

---

**Einde rapport.**
