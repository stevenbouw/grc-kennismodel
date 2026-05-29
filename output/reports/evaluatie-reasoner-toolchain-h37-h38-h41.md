# Evaluatie-rapport — reasoner-/toolchain-cluster (H38 + H41 + H37)

**Type:** evaluatie-rapport (geen bouw, geen ontologie-mutatie, geen config-omschakeling)
**Sprint-aard:** read-only + vergelijkende meet-runs
**Opsteller:** Tech-subagent (Claude Code)
**Datum:** 2026-05-29
**Instructie:** `docs/instructies/instructie-open-ontologies-evaluatie.md` (masterchat, 29 mei 2026)
**Baseline:** ontologie v4.6.3 (post-T3) — pre-inferentie 20.950 triples, post-OWL-RL 44.907 triples
**Toolversies:** rdflib 7.6.0, owlrl 7.1.4, pyshacl 0.31.0

> Bottom-up opgebouwd (Protocol v1.3 §10.2): eerst de subagent-uitvoerbare metingen + feiten, dan per H-item het oordeel, dan de cross-item-synthese. Elke meting met expliciete config + scope-annotatie (§10.5). De drie H-items blijven **parked** tot masterchat op basis van dit rapport beslist.

---

## §0. Samenvatting + oordeel per H-item

| H-item | Vraag | Oordeel | Kern |
|---|---|---|---|
| **H38** | Geeft OWL RL dezelfde inferenties als een volledige DL-reasoner (HermiT)? | **HOLD** | Analytisch: hele TBox bevat **één** OWL RL-onvolledige constructie (`asset:AssetOrComponent ≡ unionOf(Asset, AssetComponent)`), en die is **materialiseerbaarheids-compleet** onder OWL RL. Verwachte HermiT-delta = uitsluitend housekeeping. **Empirische bevestiging vergt de Protégé/HermiT-run** (projecteigenaar-actie) — runbook + diff-script geleverd. |
| **H41** | Moeten SKOS-axiomas (S46/S47) geactiveerd worden, en wat is de impact? | **HOLD** | Feit hard bevestigd: de post-inferentie SKOS-toename in de baseline (+956) is **100% toerekenbaar aan `owl:sameAs`-propagatie**, 0% aan SKOS-axiomas. Activering zou **+2.831 triples (+6,3%)** toevoegen, waaronder **12 cross-namespace exactMatch-claims** die spanning geven met D4. SHACL-impact: **0** (290→290). Geen actieve trigger. |
| **H37** | Biedt de open-ontologies-MCP (Rust+Oxigraph+tableaux) meerwaarde boven `rdflib`+`owlrl`+`pySHACL`? | **HOLD** | Geen van de vier trigger-criteria is geactiveerd: H38 toont geen aangetoonde OWL RL-limitatie; ontologie (44.907) nadert maar overschrijdt 50k niet; tool is pre-1.0 (v0.1.11, 125 ★). Legitieme toekomst-kandidaat, geen huidige trigger. |

**Geen scope-pauze getriggerd.** Toelichting in §4. Aanbevelingen aan masterchat in §6.

---

## §1. H38 — OWL RL vs HermiT (levert de DL-referentie)

### 1.1 Wat subagent-uitvoerbaar is vs projecteigenaar-actie

Protégé/HermiT is een lokale-Mac GUI-actie buiten Claude Code (per tooling-status stand-by). Conform instructie §43 is het werk gesplitst:

| Onderdeel | Status | Artefact |
|---|---|---|
| Canonieke OWL RL-closure + export inferred graph naar TTL | ✅ subagent-uitvoerbaar, **gedaan** | `output/verification/owlrl_inferred_v4_6_3.ttl` (44.907 triples) |
| DL-construct-census (voorspelt waar RL/DL kunnen afwijken) | ✅ subagent-uitvoerbaar, **gedaan** | `output/verification/owlrl_dl_census_v4_6_3.json` |
| HermiT-run in Protégé + export inferred axioms | ⏳ **projecteigenaar-actie** | runbook in §1.5 |
| Triple-set-diff owlrl-export ↔ HermiT-export | ✅ script klaar, draait zodra HermiT-export er is | `scripts/owlrl_hermit_diff.py` |

De owlrl-export reproduceert **exact 44.907** post-inferentie-triples — identiek aan `canonical_metrics_v4_6_3.json`. De export gebruikt letterlijk de canonieke config (`axiomatic_triples=False, datatype_axioms=False`); er is niets aan de productie-config gewijzigd.

### 1.2 DL-construct-census (de analytische kern)

Het census-script telt alle OWL 2-constructies in de TBox en markeert per constructie of OWL RL daar volledig is (`rl_complete=True`) of kan afwijken van een DL-reasoner (`rl_complete=False`). **Uitkomst over de hele ontologie:**

> **2 voorkomens** met `rl_complete=False` en count>0 — en dat zijn **dezelfde** constructie tweemaal geteld (vanuit `class_expressions.unionOf` én `class_axioms.equivalentClass_to_bnode_expression`).

Alle overige DL-relevante constructies in het model vallen binnen OWL RL-volledigheid: `inverseOf`, `propertyChainAxiom` (0), `SymmetricProperty`, `TransitiveProperty`, `FunctionalProperty`, `intersectionOf`, `allValuesFrom`, `disjointWith`, `AllDisjointClasses`, `maxCardinality`/`maxQualifiedCardinality`. Géén `complementOf`, `oneOf`, `hasKey`, `minCardinality>0`, `someValuesFrom`-in-superklasse-positie (0), `qualifiedCardinality`.

### 1.3 De enige divergentie-constructie, ontleed

```turtle
asset:AssetOrComponent  owl:equivalentClass  [ owl:unionOf ( asset:Asset asset:AssetComponent ) ] .
```

Wat doet OWL RL hier wél, empirisch gemeten op de merged graph:

| Richting | OWL RL | Bewijs |
|---|---|---|
| **lid → unie** (Asset ⊑ AssetOrComponent) | ✅ materialiseert | pre: 0 `AssetOrComponent`-instances → **post: 118** (waarvan 107 via `Asset`-membership + 11 via asset-bruggen) |
| **unie → lid** (AssetOrComponent → Asset ∨ AssetComponent) | ❌ niet | dit is een **disjunctieve** conclusie — niet-materialiseerbaar; **geen enkele** reasoner (ook HermiT niet) voegt een disjunctie als ABox-triple toe |

Conclusie: de enige OWL RL-onvolledige constructie produceert **geen materialiseerbare triple die OWL RL mist**. De volledige-DL-meerwaarde van HermiT zit hier in *consistentie-/entailment-checking* over de disjunctie — en de consistentie is al bevestigd: `owl:Nothing`-assertions post-inferentie = **0**.

### 1.4 Verwachte HermiT-delta (voorspelling, te bevestigen)

Op basis van 1.2–1.3: de HermiT-export zal naar verwachting **alleen housekeeping-triples** bevatten die OWL RL niet expliciet materialiseert (`rdf:type owl:Thing`, reflexieve `rdfs:subClassOf`/`owl:equivalentClass`/`owl:sameAs`, `owl:Class`/`owl:NamedIndividual`-typeringen). Dat is serialisatie-/redeneer-housekeeping, geen model-semantische delta. Het diff-script (§1.6) filtert deze categorie expliciet af, zodat de **model-semantische** delta apart zichtbaar wordt.

**Belangrijk:** dit is een **voorspelling uit de TBox-structuur**, geen empirische HermiT-meting. De definitieve H38-uitspraak vereist de runbook-uitvoering.

### 1.5 HermiT-runbook (projecteigenaar — lokale Mac)

1. Open **Protégé** (Desktop, Mac).
2. **File → Open** → laad de merged graph. Twee opties:
   - a) Open elk van de 21 `.ttl`-modules in `ontology/` (excl. `grc-shacl.ttl`) via *merge*, **of**
   - b) eenvoudiger: open `output/verification/owlrl_inferred_v4_6_3.ttl` **niet** (dat is al geïnfereerd); laad in plaats daarvan de **asserted** modules. Tip: maak desgewenst eerst één gemergd asserted-bestand met
     `python3 -c "from rdflib import Graph; from pathlib import Path; g=Graph(); [g.parse(p) for p in sorted(Path('ontology').glob('*.ttl')) if p.name!='grc-shacl.ttl']; g.serialize('output/verification/merged_asserted_v4_6_3.ttl','turtle')"`
     en open dat ene bestand in Protégé.
3. **Reasoner → HermiT** selecteren → **Reasoner → Start reasoner**.
4. Wacht tot classificatie klaar is. Controleer **geen** `owl:Nothing`/inconsistentie (verwacht: consistent).
5. **File → Export inferred axioms as ontology** (of via het *Ontology export*-menu) → kies inferred axioms (type-assertions, subclass, equivalences) → exporteer als **Turtle** naar bijv. `output/verification/hermit_inferred_v4_6_3.ttl`.
6. Draai de diff (§1.6).

> Als HermiT bij stap 4 een inconsistentie of een onverwachte hoeveelheid nieuwe axiomas meldt: **stop en meld** — dat is een scope-pauze-trigger (instructie §4), niet zelf de reasoner-config aanpassen.

### 1.6 Diff-script (klaar; self-test geslaagd)

```
python3 scripts/owlrl_hermit_diff.py \
    --owlrl  output/verification/owlrl_inferred_v4_6_3.ttl \
    --hermit output/verification/hermit_inferred_v4_6_3.ttl \
    --base   ALL \
    --out    output/reports/owlrl-hermit-vergelijking-v4_6_3.md
```

Het script vergelijkt grond-triples (excl. blank nodes, die niet stabiel matchen tussen serialisaties), scheidt **housekeeping** van **model-semantische** delta, en eindigt met exit-code 2 (en een waarschuwing) als HermiT model-semantische triples afleidt die OWL RL mist — exact de scope-pauze-conditie uit instructie §4. Self-test (owlrl tegen zichzelf) gaf 0 delta, exit 0.

### 1.7 Oordeel H38: **HOLD**

- **Waarom geen GO:** de equivalentie is nog niet *empirisch* bevestigd op deze baseline. De analyse is sterk maar voorspellend; de HermiT-run (projecteigenaar) is de ontbrekende schakel. GO zou "bevestigd equivalent" claimen zonder de meting.
- **Waarom geen NO-GO:** er is geen enkele aanwijzing voor een relevante OWL RL-limitatie. De TBox bevat één DL-only-constructie, en die is materialiseerbaarheids-compleet onder OWL RL; consistentie is al 0-`Nothing`. NO-GO ("HermiT nodig / OWL RL ontoereikend") wordt door de census tegengesproken.
- **Vervolg:** runbook uitvoeren (laagdrempelig, ~15 min). Verwachting: bevestigt HOLD→ feitelijk equivalent; H38 kan dan naar "geverifieerd, parked-met-health-check" i.p.v. "blind spot".

---

## §2. H41 — SKOS-axioma-set-handling (gemeten tegen de baseline)

Alle H41-metingen draaien in **aparte scripts/outputs**; de canonieke baseline (44.907) en de SHACL-baseline (290) worden gereproduceerd en blijven ongemoeid. De variant injecteert een **expliciete SKOS-axioma-graph** (W3C SKOS-Reference) i.p.v. de grove `axiomatic_triples=True` — surgisch en spec-getrouw.

Geactiveerde axiomas in de variant:
```turtle
skos:exactMatch   a owl:SymmetricProperty , owl:TransitiveProperty .   # S46 + S47
skos:closeMatch   a owl:SymmetricProperty .                            # S46-equivalent
skos:relatedMatch a owl:SymmetricProperty .
skos:broadMatch   owl:inverseOf skos:narrowMatch .
skos:exactMatch   rdfs:subPropertyOf skos:closeMatch .
```

### 2.1 Feit-bevestiging: huidige config laadt géén SKOS-axiomas

Control-run (identieke graph, `owl:sameAs`-triples verwijderd vóór OWL RL) isoleert de bron van de post-inferentie SKOS-toename in de baseline:

| Meting | Waarde |
|---|---:|
| SKOS-mappings pre-inferentie | 1.798 |
| SKOS-mappings post-OWL-RL (baseline) | 2.754 |
| Door inferentie toegevoegd | **+956** |
| Daarvan toerekenbaar aan `owl:sameAs`-propagatie (D5/D11) | **956 (100,0%)** |
| Toerekenbaar aan SKOS-axiomas | **0 (0,0%)** |

> Dit bevestigt H41's feitelijke basis **hard en empirisch**: de post-inferentie SKOS-groei is volledig `owl:sameAs`-propagatie (ctrl↔bio + asset-bruggen), niet SKOS-symmetrie/transitiviteit. De eerdere T1/T2/T3-observatie (Δ post-OWL-RL = 0 bij predicate-substituties) wordt hiermee mechanistisch verklaard.

### 2.2 Impact ALS de SKOS-axiomas geactiveerd zouden worden (vergelijkend)

| Metric | Baseline (canoniek) | Variant (SKOS-axiomas) | Δ |
|---|---:|---:|---:|
| Post-inferentie triples | 44.907 | 47.738 | **+2.831 (+6,3%)** |
| SKOS-mappings totaal (post) | 2.754 | 5.578 | +2.824 |
| — exactMatch | 24 | 61 | +37 |
| — closeMatch | 2.158 | 4.377 | +2.219 |
| — relatedMatch | 324 | 644 | +320 |
| — narrowMatch | 0 | 248 | +248 |
| — broadMatch | 248 | 248 | +0 |

Interpretatie van de toename:
- **narrowMatch +248** = inverse van de 248 post-inferentie `broadMatch` (S-inverse).
- **closeMatch +2.219** = symmetrie-inverses; geconcentreerd op de CSF-mappings — `ext→csf` 736, `bio→csf` 699, `ctrl→csf` 699. Dit zijn de *reverse*-richtingen van bestaande, bewust eenrichtings-geasserteerde CSF-mappings.
- **relatedMatch +320** = symmetrie-inverses.
- **exactMatch +37** = symmetrie + transitiviteit.

### 2.3 Cross-framework-implicaties (de auditief relevante kern)

`exactMatch` is de sterkste SKOS-relatie en onder D4 **zeldzaam/bewust**. Transitiviteit + symmetrie materialiseren **12 nieuwe cross-namespace exactMatch-triples**. Twee soorten:

**(a) Identiteits-consistent, maar mechanisme-vermenging** — bv.
`risk:InformationAsset ↔ asset:InformationAsset ↔ isms:InformationAsset` (exactMatch). Deze ontstaan door interactie met de asset-bruggen (`owl:sameAs`, D11). Effect: de **SKOS-identiteit (D4)** en de **`owl:sameAs`-identiteit (D5/D11)** raken vermengd — twee bewust gescheiden identiteits-mechanismen.

**(b) Genuine nieuwe cross-framework-claims** — bv.
`fw:ISO_IEC_27005_2022 exactMatch risk:RiskAssessment`,
`fw:NIST_SP_800_39 exactMatch risk:RiskManagementTier`,
`fw:BesluitCIOStelsel exactMatch roles:R_CIO`,
`fw:BesluitBVAStelsel exactMatch roles:R_BVA`.
Auto-gegenereerde exactMatch-identiteitsclaims tussen frameworks die **niet** handmatig zijn geauditeerd — directe spanning met D4 (exactMatch is geen automatisme).

**Bereikbaarheids-explosie (illustratief, géén nieuwe triples):** 3-hop cross-namespace closeMatch-*paden* gaan van 0 → 80.748 in de variant. Dit is een entanglement-indicator (het door H41 genoemde "CSF → ISO → BIO"-risico), niet een triple-toename — closeMatch is symmetrisch maar niet transitief, dus genereert geen nieuwe closeMatch-keten-triples. Het illustreert wél hoe sterk cross-framework-redenering vervlochten raakt zodra symmetrie aanstaat.

### 2.4 SHACL-impact

| Run | Violations |
|---|---:|
| COMBINED baseline (data + shapes, owlrl) | 290 (= bekende baseline, Δ 0) |
| COMBINED + SKOS-axiomas | 290 (Δ 0) |

Géén enkele actieve shape verschuift. Bevestigt dat de actieve shapes niet op SKOS-mapping-distributie valideren (de SHACL-blinde vlek op dit cluster, reeds bekend als H39-trigger). SKOS-axioma-activering raakt de SHACL-conformiteit dus niet.

### 2.5 Oordeel H41: **HOLD**

- **Waarom geen GO (= activeren):** geen actieve trigger. Geen aangekondigde externe SKOS-audit / DCAT-AP-publicatie; geen Spoor B-operationele keten-vraag. Activering kost **+6,3% triples** en — zwaarder — introduceert **ongeauditeerde cross-framework exactMatch-claims** die tegen D4-discipline indruisen en SKOS- met sameAs-identiteit vermengen. "Conformer aan W3C is beter" is onvoldoende grond (H41 expliciet).
- **Waarom geen NO-GO (= definitief afwijzen):** de impact is nu **gekwantificeerd en hanteerbaar** (+2.831 triples, SHACL 0-impact, helder afgebakende risico-set). Bij een toekomstige externe-SKOS-audit of DCAT-AP-publicatie is activering een reële, meetbaar-voorbereide optie — niet iets om uit te sluiten.
- **Status:** parked, ongewijzigd. Wel verrijkt: van "empirisch Δ=0 bij substituties" naar "volledige impact-kwantificatie inclusief D4-spanning". Eventuele toekomstige activering hoort een **nieuwe D-decision** over reasoner-/SKOS-axioma-configuratie te zijn (masterchat) — in dit rapport alleen als *overweging* genoemd, niet als besluit.

---

## §3. H37 — open-ontologies-MCP als alternatieve toolchain (desk-evaluatie)

Gebaseerd op de **publieke** projectpagina (`github.com/fabio-rovai/open-ontologies`), desk-evaluatie — niet geïnstalleerd, niet geïntegreerd.

### 3.1 Karakterisering (publieke bron)

| As | Bevinding |
|---|---|
| Reasoner | Native **OWL2-DL tableaux** (SHOIQ) **+ OWL-RL + RDFS** |
| Triplestore | **Oxigraph 0.4** (in-memory, pure-Rust, SPARQL 1.1) |
| Interface | **MCP-server, 70+ `onto_`-tools** (o.a. validate, query, reason, align, shacl, plan, apply, monitor, lineage) |
| Taal/runtime | **Rust** (edition 2024), single binary, geen JVM |
| Volwassenheid | **v0.1.11** (25 mrt 2026), 4 releases, **125 ★ / 19 forks**, **geen 1.0** |
| Licentie | **MIT** |
| SKOS-reasoning | **Niet specifiek** geclaimd (SKOS alleen als vocab-vermelding) |
| SHACL | Ja (`shacl`, `shacl_check`, + co-evolution-primitieven) |
| Performance | Benchmark-claims o.a. LUBM-reasoning **15 ms vs HermiT 24.490 ms @ 50k axiomas (≈1.633×)**; marketplace OWL-RL-inferentie 2–117 ms |

### 3.2 Weging tegen de huidige toolchain (H37-assen)

| As | Huidig (`rdflib`+`owlrl`+`pySHACL`) | open-ontologies-MCP | Weging voor dít project |
|---|---|---|---|
| Reasoner-dekking | OWL RL (subset DL) | Volledig OWL 2 DL tableaux | Alleen waardevol bij **aangetoonde** OWL RL-limitatie — H38 toont die **niet** |
| Performance | ~8–30 s closure op 44.907 triples | Rust, ms-bereik geclaimd | Relevant pas richting 50k+ / Spoor B; nu geen knelpunt |
| Protégé-integratie | Indirect (TTL-export → rdflib) | MCP naar Claude Code, geen Protégé-brug | Protégé blijft nodig voor HermiT-validatie (H38); MCP vervangt dat niet |
| Black-box-risico | Laag — Python, code bekend, settings canoniek | Hoger — Rust-binary, andere reasoner-implementatie | Canonical-metrics-discipline (reproduceerbaarheid) zwaarder dan snelheid |
| Migratie-kosten | n.v.t. | `canonical_metrics_*`/`shacl_split_*`-scripts herschrijven + her-baselinen | Substantieel; raakt de hele verificatie-pijplijn |
| SKOS-axioma-handling | Expliciet/transparant (zie H41) | Niet specifiek beschreven | H41 vraagt juist **fijnmazige** SKOS-controle — onbekend gedrag is een risico |
| Licentie | — | MIT (gunstig) | Geen blokkade |

### 3.3 Trigger-herijking met H38 + H41 als input

De vier H37-triggers (uit `brain__architecture__H37`), nu getoetst:

| Trigger | Status na deze evaluatie |
|---|---|
| Concrete OWL RL-limitatie aangetoond | **Niet** — H38-census: enige DL-constructie is materialiseerbaarheids-compleet; 0 `owl:Nothing` |
| Ontology > ~50.000 triples | **Niet** (nadert) — 44.907 post-OWL-RL; pre-inferentie 20.950. Drempel in zicht, niet bereikt |
| H38 toont substantiële delta | **Niet** — voorspelde delta = housekeeping (te bevestigen via runbook) |
| MCP-ecosystem-volwassenheid (stabiele 1.0) | **Niet** — v0.1.11, geen 1.0, beperkte adoptie (125 ★) |

H41 voegt toe: áls SKOS-axioma-handling materieel zou zijn, stijgt de relevantie van een sterkere/andere reasoner. H41 toont dat de SKOS-impact **bestaat maar hanteerbaar is en SHACL-neutraal** — dus geen H37-versterkende trigger.

### 3.4 Oordeel H37: **HOLD**

- **Waarom geen GO:** geen van de vier triggers actief. Pre-1.0-volwassenheid, niet-getest op deze ontologie, niet-beschreven SKOS-axioma-gedrag (juist H41-gevoelig), en substantiële migratie-/black-box-kosten tegenover een huidige toolchain die bewezen voldoet. GO zou speculatief "krachtiger = beter" zijn — expliciet verworpen in het H37-bestand.
- **Waarom geen NO-GO:** de tool is technisch serieus (volledig DL-tableaux + Oxigraph + MCP-native + MIT + sterke benchmark-claims) en het 50k-triggerpunt nadert (44.907). Definitief afwijzen zou een legitieme toekomst-optie wegstrepen. Bij Spoor B-overgang of bij overschrijding van 50k triples is herwaardering gerechtvaardigd.
- **Belangrijk:** dit oordeel is bereikt **zonder installatie** (desk-evaluatie op publieke bron). De scope-pauze-conditie uit instructie §73 (installatie nodig om te oordelen) deed zich **niet** voor.

---

## §4. Cross-item-synthese + scope-pauze-status

De drie H-items grijpen consistent in elkaar:

1. **H38 is de spil en wijst "geen sterkere reasoner nodig" aan:** de enige DL-only-constructie is materialiseerbaarheids-compleet onder OWL RL. Dit ontneemt zowel H41 (geen DL-gedreven SKOS-axioma-noodzaak) als H37 (geen aangetoonde OWL RL-limitatie) hun belangrijkste activerende trigger.
2. **H41 verklaart een lang-geobserveerd feit mechanistisch** (post-inferentie SKOS-groei = 100% `owl:sameAs`) en kwantificeert de hypothetische activerings-impact als hanteerbaar maar D4-gevoelig.
3. **H37 erft beide uitkomsten:** geen reasoner-limitatie (H38) + hanteerbare, SHACL-neutrale SKOS-impact (H41) = geen versterkende trigger voor een toolchain-wissel.

**Scope-pauze-condities (instructie §4) — geen getriggerd:**

| Conditie | Status |
|---|---|
| H38: substantiële, model-semantisch kritische HermiT-delta | Niet van toepassing — HermiT-run nog uit te voeren; analytische voorspelling = housekeeping. (Het diff-script triggert exit-2 + waarschuwing zodra een echte delta verschijnt.) |
| H41: meet-variant raakt canonieke baseline of 290-SHACL-baseline | **Niet** — baseline 44.907 en SHACL 290 exact gereproduceerd en ongemoeid; variant-deltas staan in aparte, niet-canonieke outputs (= het beoogde meet-resultaat, geen drift) |
| H37: evaluatie vereist installatie om te oordelen | **Niet** — desk-evaluatie op publieke bron volstond |
| Structurele verrassing buiten evaluatie-scope | Geen |

---

## §5. D-conformiteit van de evaluatie zelf

| D | Relevantie | Status |
|---|---|---|
| D1 (OWL 2 DL) | H38 betreft reasoner-*keuze* binnen D1, niet D1 zelf | Ongewijzigd; geen voorstel tot D1-wijziging |
| D3 (11 namespaces) | Metingen lezen alle 11 | Geen mutatie |
| D4 (SKOS) | H41 raakt SKOS-semantiek | Geen mutatie; D4-spanning bij hypothetische activering *gerapporteerd*, niet doorgevoerd |
| D5/D11 (`owl:sameAs`) | H41 toont sameAs als bron van SKOS-propagatie | Bevestigd 93 + 5; geen mutatie |
| Canonical-metrics-discipline | Alle varianten met expliciete config + scope-annotatie, in aparte outputs | Conform §10.5 |

Geen ontologie-mutatie, geen reasoner-config-omschakeling, geen patch/versie-bump, geen autonome commit, geen D-wijziging voorgesteld-als-besluit.

---

## §6. Deliverables + aanbevelingen aan masterchat

### 6.1 Geleverde artefacten

| Artefact | Pad | Aard |
|---|---|---|
| Dit evaluatie-rapport | `output/reports/evaluatie-reasoner-toolchain-h37-h38-h41.md` | rapport |
| H38 owlrl-export + DL-census-script | `scripts/owlrl_export_inferred_v4_6_3.py` | meet-script (read-only config) |
| H38 inferred-TTL-export | `output/verification/owlrl_inferred_v4_6_3.ttl` | diff-input (44.907 triples) |
| H38 DL-construct-census | `output/verification/owlrl_dl_census_v4_6_3.json` | meet-output |
| H38 diff-script (owlrl↔HermiT) | `scripts/owlrl_hermit_diff.py` | klaar; draait na HermiT-export |
| H41 SKOS-axioma-variant-script | `scripts/skos_axioma_variant_v4_6_3.py` | vergelijkend meet-script |
| H41 variant-meting | `output/verification/skos_axioma_variant_v4_6_3.json` | meet-output (niet-canoniek) |
| H41 SHACL-impact-script | `scripts/skos_axioma_shacl_impact_v4_6_3.py` | vergelijkend meet-script |
| H41 SHACL-impact-meting | `output/verification/skos_axioma_shacl_impact_v4_6_3.json` | meet-output (niet-canoniek) |

Alle meet-outputs zijn **niet-canoniek** benoemd (geen `canonical_metrics_*`/`shacl_results_*`-overschrijving). De canonieke baseline-bestanden zijn niet aangeraakt.

### 6.2 Aanbevelingen (besluit aan masterchat)

1. **H38 → HOLD, met één concrete vervolgactie:** voer het HermiT-runbook (§1.5) uit (~15 min, projecteigenaar) en draai het diff-script. Verwachting: bevestigt materialiseerbaarheids-equivalentie → H38 promoveren van "blind spot" naar "geverifieerd, parked met 2-jaarlijkse health-check". Alleen bij een model-semantische delta (exit-2): scope-pauze.
2. **H41 → HOLD, parked ongewijzigd, impact nu gekwantificeerd.** Niet activeren zonder concrete trigger (externe SKOS-audit / DCAT-AP / Spoor B-keten-vraag). Mocht activering ooit aan de orde komen, behandel het als **nieuwe D-decision** (reasoner-/SKOS-axioma-configuratie) en let op D4-spanning (auto-exactMatch) + SKOS↔sameAs-identiteits-vermenging.
3. **H37 → HOLD, parked ongewijzigd.** Herwaarderen bij (a) overschrijding ~50.000 triples (nu 44.907 — in zicht), (b) Spoor B-overgang, of (c) een 1.0-release met bredere adoptie. Geen installatie zonder apart masterchat-besluit.

---

## §7. Oplevernotitie + disclosure-check

**Aard:** evaluatie-sprint, read-only + vergelijkende meet-runs. Geen TTL-mutatie, geen config-omschakeling, geen MCP-installatie, geen patch/versie-bump, geen autonome commit. De drie H-items blijven parked.

**Disclosure-check (vijf categorieën, Protocol 14):**

| # | Categorie | Resultaat |
|---|---|---|
| 1 | Organisatienaam | Geen — uitsluitend "de organisatie"/"Rijksoverheidsorganisatie" waar relevant; geen organisatienaam in rapport of scripts |
| 2 | Persoonsnamen ≠ Steven | Geen |
| 3 | Lokale paden buiten repo | Geen — alle paden repo-relatief; geen verwijzing naar `grc-sources-licensed/` of andere externe paden |
| 4 | E-mail/organisatie-TLD's | Geen |
| 5 | NEN-tekst-fragment >10 woorden (handmatige toets) | Geen — geen NEN/ISO-bron geraadpleegd of geciteerd; evaluatie raakt reasoner-toolchain, niet normtekst |

**Bron-attribuering H37:** karakterisering gebaseerd op de publieke projectpagina `github.com/fabio-rovai/open-ontologies` (MIT-licentie, publiek domein) — geen restrictieve bron.

**Git:** subagent commit niet zelfstandig. Steven inspecteert `git status`/`git diff` en commit handmatig.

— Einde evaluatie-rapport H37 + H38 + H41.
