# Handover Dashboard-chat → Dashboard-subagent
**Datum:** 21 mei 2026
**Voor:** Dashboard-subagent (Claude Code) — eerste sessie-start
**Van:** Dashboard-chat (claude.ai), na inhaalslag v4.3.1 → v4.6.0

**Vooraf, eerlijk:** mijn werk in deze chat-instantie betrof primair de **data-export-kant** (build_grc_explorer v1 → v3) en het SKOS-analyse-rapport. Ik heb de gegenereerde JSON niet in een echte browser opengeleund. Wat ik over Cytoscape weet komt uit het lezen van `grc-explorer-v2.html`, niet uit eigen rendering-experimenten. Ik label hieronder duidelijk wat eigen observatie is en wat afgeleid uit code.

---

## §1 Build-script-evolutie v1 → v2 → v3

**v1 → v2 (aanleiding):** v1 was gebouwd op een v4.2.1-snapshot en bleek bij contextdiepte-diagnostiek 43% van de model-triples onzichtbaar te exporteren. De drie diepere oorzaken — niet alleen de oppervlakkige bugs:

1. **De fundamentele aanname was fout**: v1 ging ervan uit dat `rdfs:label` _de_ label-property is. In de praktijk staat 93× de control-titel uitsluitend in `ctrl:hasControlTitle`. v2's fallback-keten (`rdfs:label@nl → @en → ctrl:hasControlTitle@nl → @en → rdfs:label nolang → skos:prefLabel → IRI-fragment`) is een **patroon, geen lijst** — bij elke nieuwe namespace moet je je afvragen "heeft deze nog een eigen titel-property?". Voor csf: bleek dat niet het geval (`rdfs:label@nl` dekt alles), dus de keten bleef ongewijzigd.

2. **Literal-export was niet vergeten — het was niet voorzien**: v1's mental model was puur graaf (nodes + edges). v2 voegde literals toe omdat zonder die velden de explorer nodes alleen kan tonen met IRI en type — wat onbruikbaar is voor een GRC-gebruiker. Belangrijke ontwerpkeuze: literals komen _in_ het node-object, niet als aparte lookup-tabel. Dat lijkt redundant (meer JSON-grootte) maar betekent dat Cytoscape direct `data(description)` kan binden zonder JS-side joins.

3. **`GOVERNANCE_PROPS` als dict, niet set**: v1 had dubbele declaratie waarvan de eerste een set was. v2 koos bewust voor `Dict[uri_string, prefix_label]` zodat één lookup zowel "is dit een governance-property?" als "wat is de leesbare naam?" beantwoordt. Behouden in v3.

**v2 → v3 (aanleiding):** vijf sprints achterstand, drie soorten wijzigingen:

| Type wijziging | Aanpak in v3 |
|---|---|
| **Nieuwe namespace** (csf:) | `NS_PREFIX` uitbreiden + `bepaal_laag()` clause. Triviaal omdat v2's namespace-detectie al string-prefix-gebaseerd was. |
| **Predicate-rename** (ext:articleNumber → compl:articleRef) | Tijdens eerste run van v2 op v4.6.0-data zag ik `law_article: 0 nodes`. Diagnose: predicate-consolidatie α. Fix: één regel. **Pitfall**: je ziet dit alleen als je literal-coverage in de verificatie meet — anders blijft het onopgemerkt. |
| **Property-naming-aanname** (`csf:subcategoryID` bestond niet, het was `csf:csfIdentifier`) | Verificatie-output toonde `csf_id: 0` ondanks 501 CSF-individuals. Diagnose via grep door m21-csf.ttl op `^csf:.*Identifier\|ID\b`. |

**Welke namespace-binding-volgorde matters in rdflib**: in de praktijk geen, omdat rdflib het hele graph als één Triples-set behandelt zodra `Graph.parse()` klaar is. De *parse-volgorde* maakt alleen uit voor foutmeldingen (welk bestand de fout veroorzaakt). Belangrijker: zorg dat `grc-shacl.ttl` **niet** geladen wordt — anders muteert het de class-tellingen en raken canonical metrics overeind.

**Export-volgorde nodes-dan-edges is bewust**: edges verwijzen naar `node_ids`, en de edge-builder filtert orphan-targets uit. Andersom (eerst edges) zou betekenen dat je achteraf nog moet opruimen. Daarnaast: de `meta`-block staat in v3 als eerste in het JSON-output zodat een dashboard die eerst kan lezen voor versie-check vóór het de zwaardere `nodes`+`edges` parseert.

---

## §2 Cytoscape.js-keuzes en alternatieven

**Eerlijke disclaimer**: ik heb in deze chat geen Cytoscape-experimenten gedraaid. Wat hieronder staat is geëxtraheerd uit `grc-explorer-v2.html` (Cytoscape 3.28.1 via CDN) — niet uit eigen test.

**Wat in v2 van de HTML staat:**

```js
// Layout-keuze is conditioneel op subgraaf-grootte:
layout: subgraph_small
  ? { name:'concentric', concentric: nd => degrees[nd.id()]||0,
      levelWidth:()=>2, padding:50, animate:false }
  : { name:'cose', animate:false, randomize:true,
      nodeRepulsion:()=>8000, idealEdgeLength:()=>80, numIter:300 }
```

Deze keuze is verstandig: `cose` op een volledige graaf van 1.788 nodes + 7.249 edges loopt al snel >10 seconden in browser-CPU (afgeleid uit v3-uitvoer-grootte; niet getest). `concentric` is goedkoop genoeg voor focus-subgrafen.

**Wat de HTML _niet_ gebruikt (belangrijke gap):** v2 en v3 produceren node-velden `description`, `attributes`, `bbn`, `control_id`, `requirement_text`, `iso_clause`, `law_article`, `control_family_code`, `csf_id` — de huidige HTML rendert hiervan **niets**. Alleen `n.label`, `n.namespace`, `n.type` en `n.laag` worden aangeroepen. Dit is _de_ tacit-knowledge-bullet: **de UI rendert <10% van wat de data biedt**. UI-modernisering staat na Fase 4 in de roadmap; tot dan is bouwen-zonder-rendering-zien een terugkerende situatie.

**Wat ik niet weet maar je waarschijnlijk wel moet testen:** 1.788 nodes is groter dan v4.3.1's 1.043 — performance-grens van `cose` ligt mogelijk dichterbij dan in v2 acceptabel was. Test op een verouderde laptop, niet alleen op snelle dev-hardware.

**Onbeproefde alternatieven die overweging verdienen:** `fcose` (Cytoscape Extensions, snelle force-directed voor middelgroot, vereist extra script-import), `dagre` (hiërarchische lagen — past bij het lagenmodel 0-9), `elk` (zware maar mooie hiërarchie). `cose-bilkent` is verouderd; `fcose` is de moderne opvolger.

---

## §3 Smoke-test-routine

**Eerlijk:** ik heb alleen data-side smoke-tests gedraaid, geen browser-smoke-tests. De Python-side smoke-tests die ik standaard draai zitten al ingebouwd in v3 (laatste 50 regels): verificatie van 8 canary-nodes, literal-coverage-tabel, H4-label-check.

**Wat ik wel data-side controleer als routine:**

| Check | Acceptabel | Niet acceptabel |
|---|---|---|
| Triple-count vs canonical_metrics | ±0 (exact) | enige afwijking |
| Individuals in export vs canonical NamedIndividuals | export ≥ canonical (door H21 implicit) | export < canonical |
| owl:sameAs in export vs canonical | 93 (= 98 − 5 D11 class-bridges) | iets anders |
| SKOS in export vs canonical | export = canonical − ~39 (class-niveau) | grote afwijking |
| IRI-fragment-fallbacks op ctrl: en csf: | 0 | >0 (= label-keten gebroken) |
| Literal-coverage per veld | conform vorige snapshot ± nieuwe nodes | onverklaarde drop tot 0 |

**Canary-nodes die ik in v3 controleer (en waarom juist deze 8):**
`BIO_2_0`, `NIS2_Directive`, `ISO_IEC_27001_2022`, `VIR_2007` zijn stabiel sinds v1 — als deze foutgaan is het de _basis_-laden, niet de wijziging. `ENSIA` test laag-5-promotie v4.6.0. `GOVERN`, `Level_1`, `Tier_1_Partial` testen de drie nieuwe clusters (CSF, Maturity, CSFTier).

**Wat ik wel zou _willen_ testen in browser maar niet kan**: of `tooltip`-rendering op nodes uit nieuwe namespaces (csf:, isms:Maturity*) niet onbedoeld breekt door ontbrekende velden — er staat in de HTML `tooltip` met `pointer-events:none`; bij undefined-data zou JS waarschijnlijk falen-stil.

**Edges die symptomatisch zijn voor fout-in-mapping:** als `csf-hierarchy`-edge-count != 491 (363 exemplifies + 106 partOfCategory + 22 partOfFunction) na een herrun, dan is de CSF-module-parse partial. Als `attribution`-edge-count != 725, dan zijn niet alle nieuwe individuals geattribueerd (= SourceAttribution-gap).

**Console-warnings die ik nooit heb gezien maar zou flagen:** elke `rdflib`-warning over "ignoring triple with blank node subject" duidt op een SHACL-bestand dat per ongeluk wel geladen is. Cytoscape's `cy.add() — duplicate ID` betekent dat de v3 dedup-key (`(sid, oid, prop_uri)`) niet greep — vermoedelijk een dubbel-geparste TTL.

---

## §4 SKOS-analyse-pitfalls

Wat niet in `skos-kwaliteitsanalyse-v4_6_0.md` staat:

**Objectief vs subjectief in match-type-classificatie:** `closeMatch` is in de praktijk de default-keuze van menselijke mappers wanneer ze _aarzelen_ tussen exactMatch en relatedMatch. Het is daarmee veiliger dan de andere twee. Conclusie: een hoge closeMatch-fractie (82,8%) is **geen kwaliteits-signaal in zichzelf** — het kan zowel "mappers zijn zorgvuldig conservatief" als "mappers wisten het niet beter" betekenen. Niet aggregeren als kwaliteits-metric zonder steekproef-audit.

**Misleidende aggregaties op deze data:**

- **"Mappings per framework" telt scheef.** CSF heeft 497 individuals × ~3 mappings = ~1.450 mappings. ISO 27002 heeft 93 individuals × ~2 = ~186. Dat verhoudingsgetal zegt niets over framework-belangrijkheid; het zegt iets over framework-granulariteit. Altijd normaliseren op `mappings per source-individual` als je frameworks wilt vergelijken.
- **Namespace-paar-matrix toont _niet_ de transitive closure.** Als `csf:→bio:` en `bio:↔ctrl:` (D5 sameAs) beide bestaan, is er een impliciete `csf:→ctrl:`-relatie. De matrix telt die niet. Dashboard-gebruiker die "welke ISO 27002-controls dekken CSF GV.OC?" vraagt, krijgt zonder traversal het antwoord 0 — terwijl het correcte antwoord ~5-10 is.

**Cross-bron-overlap-patronen die extra interpretatie vragen:** twee onafhankelijke mappers die _hetzelfde paar_ leggen is een sterk kwaliteits-signaal; twee die _verschillende_ paren voor dezelfde source leggen is een conflict-signaal. De huidige analyse meet alleen het eerste (105 overlap-mappings v4.5.0). Het tweede vereist source-attribution-vergelijking per individual — niet uitgevoerd, kandidaat voor volgende sprint.

**Patroon-herkenning problematische mappings:** verdacht zijn (a) mappings tussen entiteiten van zeer verschillende abstractie-niveaus (Function → Control suggereert te ruim closeMatch), (b) één-op-veel mappings waar bron-individual >5 closeMatch-targets heeft naar één target-namespace (concept-vervaging), (c) symmetrische exactMatch-paren in beide richtingen (vraagt af waarom geen owl:sameAs).

---

## §5 Open punt A3 — SPARQL-query-patroon CSF → ISO 27002

**Mijn huidige denken**, niet uitgewerkt:

CSF maps direct naar `bio:`, niet naar `ctrl:` (zie SKOS-rapport C2c). Voor de query "welke ISO 27002-controls dekken CSF Subcategorie X" moet de query twee stappen lopen:

```sparql
SELECT DISTINCT ?iso_ctrl WHERE {
  csf:GV.OC-01 skos:closeMatch ?bio_ctrl .
  ?bio_ctrl ^owl:sameAs ?iso_ctrl .          # D5-brug omgekeerd
  ?iso_ctrl a ctrl:ISO27002Control .
}
```

Aandachtspunten voor de subagent:

- `owl:sameAs` is symmetrisch — `?a owl:sameAs ?b` betekent ook `?b owl:sameAs ?a`. Maar in TTL is meestal maar één richting geschreven. Dus òf `^owl:sameAs` gebruiken (zoals boven), òf inferentie aanzetten in de triplestore.
- Wel of niet pre-inferentie laten draaien bij dashboard-query's is een afweging. OWL RL maakt SPARQL eenvoudiger maar verveelvoudigt de triplestore-grootte (12K → 31K bij v4.3.0). Voor dashboard-snelheid loont pre-inferentie meestal.
- De omgekeerde query "welke CSF Subcategorieën dekken ISO 27002 5.01" loopt symmetrisch: start in ctrl:, hop via sameAs naar bio:, dan ^skos:closeMatch terug naar csf:.

**Niet onderschat**: gebruikers verwachten dat dit één-stap is. Het is een UX-probleem zolang er geen pre-berekend "csf-to-iso27002-coverage"-veld op csf:-nodes bestaat. Suggestie voor masterchat: overweeg een materialisatie-query die deze indirectie pre-berekent en als `ext:transitivelyCoversISO27002` per CSF-node opslaat. Vermijdt query-complexiteit aan dashboard-zijde.

---

## §6 Tips voor opvolger

1. Hernoem `grc-data-v4_6_0.js` naar `grc-data.js` vóór browser-test — de HTML hardcodet die naam zonder versie-suffix.
2. Voor elke build: run de ingebouwde verificatie aan het einde van `build_grc_explorer_v3.py` voordat je iets in browser opent. Als data-side iets stuk is, ga je in browser tijd verspillen aan symptomen.
3. Bij iedere nieuwe namespace: voeg ook een **canary-node** toe aan de `VERIFY`-lijst, anders ontdek je naam-typo's pas in productie.
4. `grc-shacl.ttl` **nooit** laden in build-script — de class-counts verschuiven, canonical-comparison breekt.
5. Cytoscape 3.28+: `cy.add()` met duplicate ID gooit géén error meer maar logt warning. Check console expliciet.
6. Bij property-aanname twijfels: één `python3 -c "from rdflib import Graph; g=Graph(); g.parse('m21-csf.ttl'); print(sorted({p for s,p,o in g}))"` redt je 30 minuten gokken.
7. SKOS-aggregaties: normaliseer altijd op source-individual-count vóór je framework-vergelijking toont.
8. Voor performance-test van layouts: simuleer op `_.sampleSize(nodes, 500)` voor je `cose` op volle dataset draait — als 500 al traag is, is 1.788 hopeloos.
9. OWL RL aanzetten in dashboard-triplestore: doe het _één keer_ vooraf, niet per query. Het verviervoudigt query-snelheid maar verviervoudigt ook geheugengebruik.
10. Bij elke patch-notitie: noteer welke `meta.source_files_hash` bij die snapshot hoort — als de hash ooit reproduceert maar de export niet, dan is het script-bug, niet data-bug.

---

**Einde handover.**
*Bij twijfel: de patchnotities v4.3.0/v4.3.1/v4.6.0 en het SKOS-rapport hebben de feiten; dit document heeft de intuïties.*
