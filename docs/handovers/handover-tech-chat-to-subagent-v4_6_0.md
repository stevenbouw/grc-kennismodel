# HANDOVER TECH-CHAT → TECH-SUBAGENT (CLAUDE CODE)

**Datum:** 21 mei 2026 | **Auteur:** Tech-chat v4.6 | **Voor:** Tech-subagent Claude Code, eerste sessie
**Scope:** Tacit knowledge — observaties die niet in brain-vault, patch-rapporten of projectinstructie staan

---

## §1 Tacit knowledge over ontologie-werk

**Per module — wat je moet weten dat niet expliciet ergens staat:**

- **m02-control.ttl** — fragiel bij D6 meeliftregel-triggers. `ctrl:CybersecurityConcept` is meeg-evolueerd v1.x→v2.0 (incl. GOVERN); SPARQL-queries die de oude 5-functie-list verwachten breken stilletjes
- **m05-compliance.ttl** — D12 drie-laags-architectuur is conceptueel complex. `compl:LegalObligation` ≠ `compl:ComplianceArticle` (laatste bestaat NIET in v4.6.0 baseline — alleen `compl:LegalObligation` voor Cbb compliance-artikelen)
- **m07-business.ttl** — heeft operationele dashboard-toepassing via `biz:DOM_01..06` + `biz:ML_*`. Cross-cluster-bridge naar `Dashboard_2026_Q1 aggregates DOM_*` zit in `grc-bridges.ttl`, niet in m07 zelf. Verborgen dependency
- **m08-bio20.ttl** — grootste module (~150KB, 2.876 triples). Bevat sinds v4.5.0 ook `csf:`-source SKOS-triples; vereist `@prefix csf:` in m08. Fragiel: D5 sameAs-bruggen (93 paren) breken collectief bij verkeerde refactoring
- **m11-nist-800-53.ttl** — dekt 124 van ~1000 SP 800-53 Rev 5-controls. Bij mappings: hoge "target-missing"-rate (108 unique in v4.5.0 Stap 6). Modelbeperking, geen bug
- **m15-ensia.ttl** — pas geharmoniseerd in v4.6.0; oude `fw:ENSIA a fw:Guideline`-typing is verwijderd. SPARQL-queries die oude typing verwachten breken
- **m17-coso-cobit.ttl** — COSO/COBIT-individuals hebben gedetailleerde rdfs:comment die als interpretatie-bron dienen voor SKOS-mapping-rationale. Niet aanpassen zonder semantische impact-analyse
- **m18-assets.ttl** — D11 asset-star (5 sameAs-bruggen) is fragile; refactoring vereist herrun van bridge-validatie
- **m21-csf.ttl** — IRI-conventies niet uniform: Functions/Categories/Subcategories volgen één patroon (`csf:GV_OC_01`), Tiers volgen Optie C (`csf:Tier_1_Partial`). Implementation Examples gebruiken `csf:GV_OC_01_Ex1` (geen zfill op N)

**Parsing edge-cases die triviaal lijken:**

- **CBW-Excel** (`Cbw_NIS2_Control_Framework.xlsx`): `ws.max_row` is misleidend door trailing empty rows (sheet 'Volwassenheid beheersmaatregel' rapporteert 706, werkelijke data eindigt R30). Tel non-empty rijen via expliciete scan
- **csf2.xlsx** — bevat 23 source-prefixes, niet 11; sheet-naam letterlijk hanteren ('CSF 2.0'), niet index 6
- **NIST_CSWP_29.pdf** en **ensia-handreiking.pdf** — beide zijn **ZIP-archives** met per-pagina `.jpeg + .txt` extracts, geen native PDF. Eerst `file <pad>` checken
- **CSF Reference Tool "None"-conventie**: bron schrijft letterlijk `"ISO/IEC 27001:2022: Mandatory Clause: None"` waar geen mapping bestaat — geen parsing-bug

**Verborgen cross-module dependencies (niet via owl:imports):**

- `ext:isComponentOf` wordt gebruikt door m17 én m21 én (per v4.6.0) m06 — multi-module property zonder centrale schema-locatie
- `ext:sourceAttribution`-individuals leven verspreid: m17 (CBW), m21 (NIST CSF Core + Reference Tool), m06 (NBA-LIO/NOREA), m01 (ENSIA-Logius)
- m08/m09/m11 hebben sinds v4.5.0 `csf:`-source-triples (Stap 6), wat impliciet `@prefix csf:`-declaratie vereist in target-modules

---

## §2 Pitfalls per sprint-fase

### Pre-sprint

- Vraag "bestaat X in module M" is NIET vraag "bestaat X model-breed". Bij architectuur-relevante entities: doe altijd multi-module-zoek (cf. v4.6.0 §8.1)
- Property-existence ≠ property-uses: `fw:toetst` was gedeclareerd in m01 zonder uses in m01, maar wèl 1 use in m15. Pre-sprint moet beide checken
- `openpyxl.load_workbook(data_only=True)` verplicht voor formule-bevattende Excel — anders krijg je formula-strings ipv values
- Memory entries kunnen incompleet zijn (entry #17 noemde 5 maturity-elementen, werkelijkheid was 5 declaraties + 6 individuals + 12 cross-cluster-uses + dashboard-bridge)

### Uitvoering

- **rdflib telt rdf:type dubbel**: een typed individual met `rdf:type FooClass, owl:NamedIndividual` levert 2 type-triples. Base voor ramingen: 5 triples/individual (2 type + 2 label + 1 attr), niet 4
- **Merge dedupliceert (s,p,o) automatisch**: builder zegt "899 unique" maar merged-graph-delta is +794 (cross-bron-overlap 105 keer dezelfde triple)
- **bash brace-expansion** `{a,b,c}` werkt niet in elke shell (`/bin/sh -c` faalde in mijn omgeving). Gebruik expliciete mkdir per directory
- **str_replace** is gevoelig voor exacte whitespace/newlines. Voor multi-line TTL-blokken: heredoc-append (`cat >> file << 'EOF'`) of Python-script is robuuster
- **TTL-comments met `<`-karakters**: Turtle-parser is meestal tolerant, maar bij dubieuze multi-line comments controleer parse-check direct
- **@prefix-declaratie nodig voor cross-namespace triples**: m08 schrijft `csf:GV_OC_01 skos:closeMatch bio:...` vereist beide prefixes
- **Per-module wijzigingen vereisen merged-parse-check**: een module parses individueel correct kan in merged-graph alsnog conflicts produceren

### Verificatie

- **`canonical_metrics_v<N>.py` heeft hardcoded NAMESPACES-dict**. Bij toevoegen 11e/12e namespace ook script updaten — anders fall-out via "_other"-bucket in skos_mapping_pairs
- **SHACL combined-run (zonder split) levert 290 false-positives**. Dat lijken violations maar zijn baseline. Gebruik ALTIJD split-validation: SECTIE A `inference='none'` + SECTIE B `inference='owlrl'`
- **D-conformance-checks** staan in JSON onder `d_decision_conformance`, niet `d_decisions`
- **`globals_pre`/`globals_post` bestaat niet**; sleutels zijn `global_pre_inference`/`global_post_inference_owlrl`
- **HermiT in Protégé** is niet meer gerund sinds v4.0.0 — alleen OWL RL via owlrl-package. Bij echte DL-validatie eerst Protégé-run plannen

### Patch-rapport

- **§0-tabel uit JSON, niet uit memorie** (leerpunt v4.3.3). Snel te vergeten bij grote sprints — leid waardes mechanisch af uit `canonical_metrics_v<N>.0.json`
- **§9 geparkeerde-items**: inclusief Spoor B-items (H11-H14, H19, H20) en niet-formeel-geregistreerde kandidaten
- **§8 aandachtspunten** zwellen tot 15-20 bij grote sprints — categoriseer in subsecties (A methodologisch / B bron-specifiek / C kwaliteits-indicatoren / D architectuur)
- **Bij Sprint-prognose-evaluatie**: noem altijd raming + werkelijk + verklaring voor afwijking. Werkelijk-zonder-verklaring is incompleet rapport

---

## §3 Tips voor opvolger (max 10)

1. Lees patch-rapporten in volgorde v4.0→v4.6 voor patroon-herkenning, niet alleen de laatste
2. Sprint-start: `sha256sum -c file_hashes_v<vorige>.txt` vóór elke wijziging — voorkomt werk op corrupte baseline
3. `cat >> file.ttl << 'EOF'` is sneller dan str_replace voor append; gebruik Python-builders voor parametrische blokken
4. Excel: print(sheetnames) als eerste actie — 0-indexed vs 1-indexed verwarring komt structureel voor
5. PDF in /mnt/project: `file <pad>` checken voordat je pdftotext gebruikt — kan ZIP-archive zijn
6. Pre-sprint: multi-module-zoek altijd, ook als vraag specifiek over één module gaat
7. Bij triple-impact-raming: 5/typed-individual als base; tel additional properties bovenop; verklaar afwijkingen bottom-up
8. Bij nieuwe namespace: update NAMESPACES-dict in canonical_metrics-script in dezelfde commit
9. Heads-up moments respecteren: masterchat-bevestiging vóór ABox-creatie scheelt scope-pauzes later
10. Vertrouw nooit een memory-entry zonder cross-check tegen actuele TTL (memory entries kunnen achterlopen)

---

## §4 Open vragen / blind spots (max 5)

1. `m02:ctrl:CybersecurityConcept` v2.0-update met GOVERN: zijn er SPARQL-queries in dashboard die nog v1.x-naming verwachten? Niet getest, mogelijk silent-failure
2. OWL RL via owlrl-package vs HermiT in Protégé: produceren ze identieke post-inference closure op v4.6.0 merged graph? Niet geverifieerd sinds v4.0.0
3. `isms:hasLevelDescription ↔ forCapability` als owl:inverseOf-paar: gedeclareerd, maar niet getest via SPARQL of OWL RL daadwerkelijk bidirectionele inferentie uitvoert
4. 290 SHACL RUN 2 false-positives: zijn ALLE 290 echt false-positives, of zit er een echte violation tussen die toevallig op zelfde totaal-getal uitkomt? Niet uitgesplitst per individuele violation
5. `csf:CSFTier ⊑ ext:FrameworkComponent` — Tiers zijn semantisch geen "component" van fw:NIST_CSF_2_0 op dezelfde manier als Functions/Categories/Subcategories. Subclass-relatie mogelijk geforceerd; geen impact-analyse

---

## §5 Toolchain-ervaring

**Versies stabiel op v4.6.0-baseline:**
- `rdflib 7.x` — geen segfaults, parse + serialize stabiel
- `owlrl 7.x` — `DeductiveClosure(OWLRL_Semantics, axiomatic_triples=False, datatype_axioms=False)` is sprint-standaard; defaults geven meer triples (axiomatic noise)
- `pyshacl ~0.25` — stabiel bij split-validation

**Runtime-observaties op v4.6.0 (20.950 pre / 44.907 post triples):**
- Parse per module: <1s elk
- Merged parse (22 modules): ~2-3s
- OWL RL closure (merged): ~8-12s
- pySHACL split-validation (beide runs): ~10-15s totaal
- pySHACL combined run: ~10s (geeft 290 false-positives, gebruik split)
- canonical_metrics_v<N>.py volledige run: ~10-15s
- SPARQL op pre-inference graph: <2s; op post-OWL-RL-graph: ~5-8s (~3-4× trager)
- file_hashes generatie: <1s

**Snel-versus-traag in praktijk:**
- Snel (<5s): per-module parse, namespace-counts, individual-existence-checks, SHACL met `inference='none'`
- Medium (5-15s): merged parse + reasoning + split-SHACL combined
- Traag (>15s): SPARQL met meerdere OPTIONAL-clauses op post-inference graph; HermiT in Protégé (niet gerund sinds v4.0.0)

**Geheugen:**
- Geen OOM events tijdens v4.0.0-v4.6.0 sprints
- Merged graph + OWL RL closure ruim binnen container-limits
- Geen specifieke metingen gedaan; aanname is dat huidige model-omvang (max ~50K triples post-inferentie) ook bij verdubbeling geen issue is

**Subtiel:**
- `openpyxl.load_workbook(data_only=True)` essentieel bij formule-bevattende Excel — anders krijg je formule-strings ipv values
- `Graph().parse(format='turtle')` is strikter dan Protégé over IRI-validiteit (spaties in IRI, ongeldige escapes) — bij parse-error eerst regel-nummer in Turtle inspecteren, niet Protégé
- `g.predicate_objects(subject)` itereert in willekeurige volgorde; voor reproduceerbare output altijd `sorted()`
- `rdflib.Literal` met language-tag vs xsd:string: language-tag overrules datatype; bij explicit `xsd:string`-cast met language-tag krijg je language-tag-versie

---

**Einde handover. Succes met v4.7.0 en verder.**
