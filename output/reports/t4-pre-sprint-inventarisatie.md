---
type: report
subtype: pre-sprint-inventarisatie
sprint: T4
baseline_from: v4.6.3
date: 2026-05-29
status: final-awaiting-masterchat-review
mode: READ-ONLY
related:
  - skos-beoordelings-protocol-v1_3
  - cross-bron-overlap
  - cross-category-mappings
  - D04_skos-cross-framework
  - M21_nist-csf-2-0-planned
  - M09_iso27001-ext
scope: "T4 pre-sprint-inventarisatie — cross-bron-overlap CSF ↔ ISO 27001 (SKOS-kwaliteits-validatie). READ-ONLY, geen mutatie."
---

# T4 Pre-sprint-inventarisatie-rapport — cross-bron-overlap CSF ↔ ISO 27001

> **Meet-laag (Protocol v1.3 §10.5):** alle tellingen in dit rapport zijn op de **ONTOLOGIE-LAAG** gemeten — rdflib-parse van `ontology/*.ttl`, `inference='none'` (géén OWL-RL), via read-only helper-script `scripts/t4_inventory_query.py`. Niet op de dashboard-export-laag. Baseline-tellingen geciteerd uit `output/verification/canonical_metrics_v4_6_3.json` (gemeten 2026-05-28T10:33Z).
>
> **§0.5-firewall.** Dit is een read-only inventarisatie. Geen TTL-mutatie, geen applier, geen patch, geen herklassificatie — ook niet "alvast". Geen autonome commit; Steven inspecteert + commit handmatig. Geen architectuurbeslissing; categorie-classificatie en pilot-scope = masterchat-werk. Vaststellen, niet beslissen.

---

## §1. Scope-bevestiging — **INITIEEL, TE BEVESTIGEN door masterchat**

> Drie van de zes inventarisatie-vragen leveren een bevinding op die de aanname "±105 machine-detecteerbare overlap-paren, enkelvoudige categorie" **niet bevestigt**. Zie §5. De scope kán daardoor niet zonder masterchat-besluit worden vastgelegd.

| Aspect | Initiële bevinding | Bron |
|---|---|---|
| Sprint-scope | cross-bron-overlap CSF ↔ ISO 27001 (SKOS-kwaliteit) | instructie §0 |
| Audit-richting | csf → ISO 27001 (uitgaand vanuit csf:Subcategory) | §2.3 |
| Baseline | v4.6.3 | `canonical_metrics_v4_6_3.json` |
| Predicate-types in scope | **100% `skos:closeMatch`** (geen exact/broad/related/narrow op deze paren) | §2.2 |
| **Overlap-set ±105** | **niet machine-reproduceerbaar uit het model** — zie §5-A | §3 + §5-A |
| **Categorie** | **gesplitst** (eis-categorie clausules + measure-categorie Annex A) — niet enkelvoudig | §3.4 + §5-C |
| **Divergentie-set** | per-bron afleidbaar via module-herkomst (m21 vs m09), maar dat is gemodelleerde herkomst, niet bron-attributie | §3.2 + §5-B |

---

## §2. ABox-baseline (uit `canonical_metrics_v4_6_3.json` — niet uit memorie)

### §2.1 Globale telling — baseline v4.6.3 (scope: global)

| Metric | v4.6.3 | Scope |
|---|---:|---|
| triples (pre-inference) | 20.950 | global |
| owl:Class | 199 | global |
| owl:NamedIndividual | 1.383 | global |
| owl:ObjectProperty | 149 | global |
| owl:DatatypeProperty | 96 | global |
| owl:sameAs | 98 (93 D5 + 5 D11) | D5/D11-conformance |
| skos:closeMatch (totaal) | 1.457 | global |
| skos:relatedMatch (totaal) | 194 | global |
| skos:broadMatch (totaal) | 129 | global |
| skos:exactMatch (totaal) | 18 | global |
| SHACL SECTIE A / B / COMBINED | 0 / 0 / 290 | drift-referentie (schone baseline) |

SHACL-baseline (`shacl_results_v4_6_3.json`): SECTIE A = 0, SECTIE B = 0, COMBINED (run2_owlrl) = 290 false-positives (93 bio:ISO27002NamingShape + 104 asset:NamespaceShape + 93 ctrl:ISO27002NamingShape). **T4 start op een schone baseline** (geen drift; A=0, B=0 conform verwachting).

### §2.2 SKOS-predicate-tellingen — scope: csf-uitgaande mappings naar ISO 27001

Uit `skos_mapping_pairs` (canonical json) + helper-script. csf-uitgaande SKOS-mappings per doel-namespace (ontologie-laag, unie over alle modules):

| csf → doel-namespace | predicate | aantal | ISO 27001-relevantie |
|---|---|---:|---|
| csf → ext (`ext:ISO27001_*`) | closeMatch | 245 | **ISO 27001 mandatory clauses 4-10** (`ext:ISMSRequirement`) |
| csf → ext (overig) | relatedMatch | 13 | n.v.t. (niet-ISO27001-eindpunten) |
| csf → bio (`bio:ISO27002_*`) | closeMatch | 699 | **ISO 27001 Annex A-controls** (D5 sameAs-brug bio:↔ctrl:) |
| csf → isms | relatedMatch | 4 | n.v.t. |

> **Scope-annotatie:** "ISO 27001" als mapping-eindpunt heeft in het model **twee representaties** (zie §3.4). Beide zijn ISO-27001-mappings; ze leven in verschillende namespaces door de import-target-resolutie van v4.5.0.

### §2.3 Richting-consistentie

Alle scope-mappings zijn **uitgaand vanuit `csf:Subcategory`** (csf → ISO). Geen tegen-richting (ISO → csf) op deze paren aangetroffen. 100% richtings-consistent.

---

## §3. Cluster-cardinaliteit + bron-/module-structuur (scope: csf ↔ ISO 27001)

### §3.1 Tellingen per bron-module (instructie-vraag 1 + 2)

De twee bronnen zijn in v4.5.0 in **verschillende modules** geïmporteerd (regel-comment m21 r.32: "IR-mappings naar SP 800-53 + ISO 27001 zitten in m11 + m09 (Stap 6)"; Sheet 8 → m21 Stap 5):

**A — mandatory-clause-mappings (csf → `ext:ISO27001_*`, ISMSRequirement):**

| Herkomst-module | Bron | aantal closeMatch-paren |
|---|---|---:|
| m21-csf | Sheet 8 (ADR & NOREA, `ext:Attr_CBW_NIS2_Framework_2025_CC_BY_4_0`) | 147 |
| m09-iso27001-ext | CSF Reference Tool (NIST, `ext:Attr_NIST_CSF_2_0_Reference_Tool_2026`) | 117 |
| **Intersectie** (identieke triple in beide modules) | beide bronnen leggen dezelfde mapping | **19** |
| **Unie** (distinct triples) | — | **245** |
| alleen m21 / alleen m09 | divergentie-set per bron | 128 / 98 |
| distinct ISO27001-clausule-eindpunten | — | 23 |

**B — Annex A-control-mappings (csf → `bio:ISO27002_*`, via D5-brug):**

| Herkomst-module | Bron | aantal closeMatch-paren |
|---|---|---:|
| m21-csf | Sheet 8 (ADR & NOREA) | 494 |
| m09-iso27001-ext | CSF Reference Tool | **0** |
| **Intersectie / Unie** | — | **0 / 494** |

> **Interne tabel-consistentie (§10.3):** A-unie 245 = 128 (alleen m21) + 98 (alleen m09) + 19 (intersectie). ✓ Σ(m21 147 + m09 117) − intersectie 19 = 245. ✓

### §3.2 Divergentie vs overlap (instructie-vraag 1)

- **Machine-zichtbare overlap op clausule-niveau (A): 19 paren** — triples die zowel in m21 (Sheet 8) als m09 (Reference Tool) identiek voorkomen.
- **Machine-zichtbare overlap op Annex A-niveau (B): 0 paren** — de Reference Tool-Annex A-controls (volgens attributie-tekst 301 refs) zijn in m09 **niet** als csf→bio/ctrl-mappings gemodelleerd (m09 draagt uitsluitend 117 csf→clausule-mappings). Sheet 8's 494 Annex A-mappings staan alleen in m21.
- **Divergentie-set** is dus per module afleidbaar (128 m21-only + 98 m09-only op clausules; 494 m21-only op Annex A), maar dit is **gemodelleerde herkomst**, niet bron-onafhankelijke bevestiging in de zin van het cross-bron-overlap-concept.

### §3.3 Heterogeniteit

Bron-stack is **heterogeen** (twee onafhankelijke bronnen, twee modules, twee attributie-individuals) — relevant voor een eventuele latere per-paar-D4.1-toets (heterogene stack → per-paar, niet cluster-niveau; vgl. T2 homogeen).

### §3.4 Categorie-classificatie ISO-eindpunt (instructie-vraag 4) — **GESPLITST**

De open classificatie-vraag uit instructie §2 ("Annex A-control = measure-categorie of management-clausule = eis-categorie?") heeft in het model **twee gelijktijdige antwoorden**:

| ISO-eindpunt | Model-representatie | rdf:type | Categorie | csf↔X karakter |
|---|---|---|---|---|
| Mandatory clauses 4-10 | `ext:ISO27001_*` (23 distinct) | `ext:ISMSRequirement` | **eis-categorie** | outcome ↔ requirement → **cross-category** (relatedMatch-basislijn-kandidaat, vgl. T3) |
| Annex A-controls | `bio:ISO27002_*` (D5-brug → ctrl:) | bio/ctrl control | **measure-categorie** | outcome ↔ control → **cross-category** (outcome ≠ measure) |

Geverifieerd: alle 23 clausule-eindpunten zijn `ext:ISMSRequirement` (100%); `ext:ISO27001_9_1 ext:implementedBy ctrl:ISO27002_5_35` bevestigt de clausule→control-brug. **Beide csf-eindpunt-typen zijn prima facie cross-category** t.o.v. `csf:Subcategory` (een outcome/uitkomst-statement). Dit is een vaststelling; de predicate-implicatie (relatedMatch-basislijn vs closeMatch-behoud) is masterchat-werk (v1.3.1-kandidaat, niet formaliseren — instructie §6).

---

## §4. Evidence-coverage + provenance + NEN (scope: csf ↔ ISO 27001)

### §4.1 Huidige predicate-status (instructie-vraag 5)

- **100% `skos:closeMatch`** op alle 245 clausule- + 494 Annex A-paren. Geen `exactMatch` (dus **geen prima-facie cross-category-exactMatch-schending**), geen broad/related/narrow.
- De closeMatch is een **conversie-default, geen evidence-gebaseerd per-paar-oordeel.** Reference Tool-attributie-tekst (m21 r.58-59, parafrase): de export bevat géén OLIR-relationship-types (equivalent/subset/intersects); álle mappings zijn als `skos:closeMatch` geconverteerd. Idem Sheet 8 (m21 r.4582, "Match-type: skos:closeMatch (besluit 5)").
- Prima-facie aandachtspunt (vaststelling, geen oordeel): closeMatch op cross-category outcome↔requirement/measure-paren staat in spanning met de relatedMatch-basislijn uit het cross-category-precedent (T3). Of dat een pilot rechtvaardigt is masterchat-besluit.

### §4.2 Provenance — dubbele attributie (instructie-vraag 3) — **niet machine-detecteerbaar**

De detection-query uit `brain__concepts__cross-bron-overlap.md` (`COUNT(DISTINCT ?attribution) ... HAVING (?bron_count >= 2)`) levert op het model **0 paren** op, niet 105:

- Attributie is bewust op **blok-comment-niveau** vastgelegd, **niet als per-triple `ext:sourceAttribution`-link**. Letterlijk in m21 r.4584-4586 (parafrase): "Bron-attribuering via blok-comment … geen per-triple ext:sourceAttribution-link — consistent met v4.4.0 Stap 5-precedent en masterchat-voorkeur Stap 5-GO v4.5.0."
- De `ext:sourceAttribution`-triples die wél bestaan (504 in m21) staan op de **csf-knopen** (CSF Core-herkomst, `Attr_NIST_CSF_2_0_Core_2024`), niet op de mapping-triples. Daardoor draagt elk csf↔ISO-paar machinaal één attribution (de csf-knoop), nooit twee.
- Gevolg: de "105-overlap" uit v4.5.0 is een **bron-niveau-getal** (Sheet 8 XLSX ∩ CSF Reference Tool XLSX), berekend tijdens de v4.5.0-analyse — **niet reconstrueerbaar uit de model-triples** via het concept-detection-patroon.

### §4.3 Bron-toegankelijkheid (instructie-vraag 6 + Protocol 17)

| Bron | Lokale toegang | Locatie | NEN-status |
|---|---|---|---|
| Sheet 8 (CBW/NIS2 Control Framework, ADR & NOREA v1.0) | ✅ | `sources/adr-norea/Cbw (NIS2) Control Framework.xlsx` | CC-BY 4.0 (publiek) |
| CSF Reference Tool export (csf2.xlsx) | ✅ | `sources/nist/NIST-CSF-2/` (XLSX-structuur aanwezig) | Publiek domein |
| ISO/IEC 27001:2022 (normtekst) | ❌ niet nodig | NEN-restrictief | parafrase volstaat (zie hieronder) |

**Beide bron-bestanden zijn in de repo aanwezig** — een eventuele her-afleiding van de 105-overlap uit de twee XLSX-bronnen is technisch mogelijk (maar is pilot-/analyse-werk, geen inventarisatie; masterchat beslist).

**NEN-aanraking (vraag 6):** de betrokken ISO 27001-eindpunten zijn mandatory clauses 4-10 (m09 draagt al NL-parafrase via `compl:requirementText`, geen verbatim) en Annex A-controls (= ISO 27002, via bio:/ctrl:). **Parafrase + clausule-/Annex-A-verwijzing volstaat; geen verbatim NEN-tekst nodig** voor een eventuele vervolg-sprint. Bevestigd: geen ISO-normtekst in dit rapport.

---

## §5. Risico-inventarisatie + scope-pauze-bevindingen (Protocol v1.3 §6 + instructie §5)

> Drie van de drie expliciete §5-scope-pauze-condities uit de instructie zijn getriggerd. Conform instructie: **gemeld, niet zelf beslist.**

### §5-A — Overlap-set wijkt substantieel af van ±105 (instructie §5, conditie 1)

De ±105 is niet machine-reproduceerbaar uit het model. Machine-meetbaar: unie 245 (clausule) + 494 (Annex A); clausule-intersectie tussen de twee bron-modules = 19; Annex A-intersectie = 0. De twee bronnen gebruikten **verschillende ISO-target-resoluties** (Sheet 8: Annex A → `bio:`, clausule → `ext:`; Reference Tool in m09: alleen clausule → `ext:`), waardoor bron-overeenstemming op Annex A-niveau **structureel niet als identieke triple** verschijnt. De 105 is een bron-niveau-getal uit v4.5.0.

### §5-B — Provenance-administratie zonder dubbele triple-attributie (instructie §5, conditie 2)

Overlap-paren dragen geen dubbele `ext:sourceAttribution` (block-comment-design, masterchat v4.5.0 Stap 5-GO). De concept-detection-query is op dit model **niet toepasbaar** zoals beschreven. Dit is geen administratie-fout maar een bewuste modelleer-keuze; het maakt de overlap-set echter niet model-intern detecteerbaar.

### §5-C — Categorie-classificatie is gesplitst, niet enkelvoudig (instructie §5, conditie 3 + §2-classificatie-vraag)

Het ISO-eindpunt is zowel eis-categorie (mandatory clauses, ISMSRequirement) als measure-categorie (Annex A, control). Beide zijn cross-category t.o.v. csf-outcomes. De instructie-§2-vraag "binnen-categorie of cross-category?" heeft dus geen enkelvoudig antwoord; de methode van een eventuele pilot hangt af van welk eindpunt-type masterchat in scope wil.

### §5.1 Methodische risico's (informatief)

- **SHACL-blinde vlek (H39):** csf↔ISO-mappings vallen niet onder SECTIE A/B-shapes; SHACL bewaakt deze predicate-keuzes niet (consistent met H39 bidirectional-bevinding).
- **closeMatch-conversie-default:** uniforme closeMatch is import-conventie, niet per-paar-evidence — een latere kwaliteits-toets zou per-paar moeten beoordelen, niet de aanname overnemen.
- **Heterogene bron-stack:** per-paar-D4.1-toets vereist (niet cluster-niveau), mocht een pilot volgen.

### §5.2 Stop-condities-voorstel (voor een eventuele latere pilot — masterchat beslist of)

- Stop-conditie A: helper-script-telling wijkt >5% af van masterchat-verwachting → her-inventariseer.
- Stop-conditie B: als pilot 105-overlap uit XLSX wil her-afleiden → dat is eigen analyse-stap, niet pilot-Stap-2-scope; expliciet beslissen.
- Stop-conditie C: D4/D4.1- of cross-category-conformance-twijfel → escalatie.
- Stop-conditie D: SHACL-drift A>0 of B>0 → stop (nu A=0/B=0, schoon).

---

## §6. Sample-keuze-voorstel (Protocol v1.3 §6 — indicatief, GEEN pre-pilot-uitkomst)

Indien masterchat een pilot autoriseert, voorstel voor een gespreide sample van 8 paren over de variatie-assen. **Geen predicate-mutatie-voorstel per paar** (Protocol v1.3 §6 stop-conditie-4); alleen evidence-niveau-raming.

| # | Subject (csf) | Predicate (current) | Object (ISO) | Eindpunt-type | Herkomst | Evidence-niveau (pre-pilot raming) |
|---|---|---|---|---|---|---|
| 1 | csf:GV_OV_01 | closeMatch | ext:ISO27001_9_1 (clausule 9.1) | eis | beide (intersectie-19) | 1 (twee bronnen) |
| 2 | csf:DE_CM_03 | closeMatch | ext:ISO27001_9_1 | eis | m21 + m09 | 1 |
| 3 | (csf-paar alleen m21) | closeMatch | ext:ISO27001_* | eis | Sheet 8-only (divergentie) | 3 (één bron) |
| 4 | (csf-paar alleen m09) | closeMatch | ext:ISO27001_* | eis | Reference Tool-only (divergentie) | 3 |
| 5 | csf:DE_AE_02 | closeMatch | bio:ISO27002_5_26 (Annex A) | measure | Sheet 8 | 3 |
| 6 | csf:DE_AE_04 | closeMatch | bio:ISO27002_5_25 | measure | Sheet 8 | 3 |
| 7 | (clausule met veel csf-subjecten) | closeMatch | ext:ISO27001_* (cluster veel→1) | eis | beide | cardinaliteit-anker |
| 8 | (csf-subject met meerdere ISO-targets) | closeMatch | meerdere | eis+measure | Sheet 8 | 1→veel-anker |

> Concrete subject-IRI's voor #3, #4, #7, #8 zijn met het helper-script per masterchat-scope-keuze te genereren; hier bewust open gelaten tot de scope (clausule-only / Annex-A-only / beide) is vastgesteld.

### §6.3 Spreidings-verantwoording

Sample dekt: beide eindpunt-categorieën (eis + measure), overlap- én divergentie-set, beide herkomst-modules, en beide cardinaliteit-richtingen (veel→1 + 1→veel). Geen pre-classificatie van uitkomst.

---

## §7. Verwachte uitkomst (indicatief — aggregate, geen per-paar-mandaat)

Op basis van §3-§5: de scope-vraag is in deze sprint **primair een classificatie-/scope-vraag, niet een herklassificatie-volume**. Anders dan T1-T3 (waar het mutatie-volume vooraf grofweg bekend was) is het hier eerst nodig dat masterchat (a) kiest welk eindpunt-type in scope is, en (b) bepaalt of de 105-overlap uit de XLSX-bronnen her-afgeleid moet worden. Pas daarna is een mutatie-prognose mogelijk. **Aggregate verwachting:** als cross-category-relatedMatch-basislijn (T3-precedent) wordt aangehouden, is het *potentiële* mutatie-bereik groot (tot 245 + 494 closeMatch → relatedMatch); maar dat is een masterchat-besluit dat afhangt van de retrieval-interchangeability-uitzondering per paar — niet hier vast te stellen.

---

## §8. GO/NO-GO-criteria (pre-pilot — masterchat-eindbesluit)

| # | Criterium | Status (pre-pilot) |
|---|---|---|
| 1 | Scope (N paren) bevestigd in §1 | ⚠️ — overlap-set niet model-reproduceerbaar (§5-A); scope vergt masterchat-besluit |
| 2 | ABox-baseline-cijfers consistent (§2) | ✅ uit canonical_metrics_v4_6_3.json |
| 3 | Cluster-/bron-cardinaliteit gemeten (§3) | ✅ helper-script (147/117/19/245 + 494/0) |
| 4 | Evidence- + provenance-pre-check (§4) | ✅ — bevinding: 100% closeMatch-default; provenance block-level |
| 5 | Risico-/stop-condities expliciet (§5) | ✅ — drie scope-pauze-condities gemeld |
| 6 | Sample-keuze onderbouwd (§6) | ✅ (indicatief, scope-afhankelijk) |
| 7 | Geen onbevestigde scope-aannamen | ⚠️ — categorie gesplitst (§5-C); ±105-aanname niet bevestigd |
| 8 | Bron-toegankelijkheid voldoende (§4.3) | ✅ — beide XLSX-bronnen in repo; geen NEN-verbatim nodig |

**Drie ⚠️ → expliciete masterchat-beslispunten** (zie §9.1). Niet zelf opgelost.

---

## §9. Hand-off + Deliverables (Protocol 16)

### §9.1 Beslispunten voor masterchat (niet door Tech te beslissen)

1. **Scope-eindpunt:** clausule-mappings (eis, 245), Annex A-mappings (measure, 494), of beide?
2. **Overlap-definitie:** accepteren dat de model-overlap = 19 (clausule-intersectie tussen modules), óf de 105 her-afleiden uit de twee XLSX-bronnen (aparte analyse-stap)?
3. **Cross-category-predicate-vraag:** geldt de relatedMatch-basislijn (T3-precedent) hier, of blijft closeMatch verdedigbaar via retrieval-interchangeability? (v1.3.1-formalisering blijft masterchat-werk.)
4. **Provenance-modellering:** is block-level attributie acceptabel, of wenst masterchat per-triple-attributie zodat cross-bron-overlap voortaan machine-detecteerbaar wordt? (architectuur-vraag.)

### §9.2 Deliverables

| Type | Locatie | Beschrijving |
|---|---|---|
| Inventarisatie | `output/reports/t4-pre-sprint-inventarisatie.md` | Dit document |
| Read-only helper-script | `scripts/t4_inventory_query.py` | Reproduceerbare tellingen (ontologie-laag) |
| ABox-baseline | `output/verification/canonical_metrics_v4_6_3.json` | Bron §2 (geen her-meting nodig) |
| SHACL-baseline | `output/verification/shacl_results_v4_6_3.json` | Drift-referentie (A=0/B=0/COMBINED=290) |

### §9.3 Verwijzingen

- Sprint-instructie: `docs/instructies/instructie-t4-pre-sprint-inventarisatie.md`
- Concept: `brain/brain__concepts__cross-bron-overlap.md` + `brain__concepts__cross-category-mappings.md`
- Protocol v1.3 FINAL: `docs/skos-beoordelings-protocol-v1_3.md`
- Modules: `ontology/m21-csf.ttl` (Sheet 8, Stap 5) + `ontology/m09-iso27001-ext.ttl` (Reference Tool, Stap 6)
- D-register: `brain/brain__decisions__D-register.md` (D4 + D4.1 + D9)

— Einde pre-sprint-inventarisatie T4. **READ-ONLY. Wacht op masterchat-review + scope-besluit.**
