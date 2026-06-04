# Patch-rapport v4.6.4 — CSF-description range-fix (DL-conformiteit, H38-lus)

**Type:** patch-rapport (TBox-bugfix)
**Opsteller:** Tech-subagent (Claude Code)
**Datum:** 2026-05-29
**Instructie:** `docs/instructies/instructie-csf-range-fix-v4_6_4.md` (masterchat, 29 mei 2026)
**Baseline:** v4.6.3 → **v4.6.4** (patch-bump)
**Aard:** surgische TBox-correctie — 2 `rdfs:range`-declaraties in `m21-csf.ttl` + version-bump in `grc-core.ttl`. Geen ABox-, SKOS- of shape-wijziging.

> Bottom-up opgebouwd (Protocol v1.3 §10.2): eerst de mutatie + gemeten verificatie, dan administratie, dan GO-criteria. §0-metrics uit `canonical_metrics_v4_6_4.json` (niet uit memorie — leerpunt v4.3.3). Metrics met scope-annotatie (§10.5).

---

## §0. Tellingen-vergelijking v4.6.3 → v4.6.4

**Scope-annotatie:** alle waarden uit `output/verification/canonical_metrics_v4_6_4.json` (config: OWL RL, `axiomatic_triples=False`, `datatype_axioms=False`; rdflib 7.6.0 / owlrl 7.1.4 / pyshacl 0.31.0). Pre-inferentie = gemergde data-graph excl. `grc-shacl.ttl`. Post = na canonieke OWL RL-closure.

| Metric | v4.6.3 (baseline) | v4.6.4 | Δ |
|---|---:|---:|---:|
| Triples pre-inferentie | 20.950 | 20.950 | **0** |
| Triples post-OWL-RL | 44.907 | 44.907 | **0** |
| owl:Class | 199 | 199 | 0 |
| owl:NamedIndividual | 1.383 | 1.383 | 0 |
| owl:ObjectProperty | 149 | 149 | 0 |
| owl:DatatypeProperty | 96 | 96 | 0 |
| owl:sameAs (D5 93 + D11 5) | 98 | 98 | 0 |
| SKOS-mappings totaal | 1.798 | 1.798 | 0 |
| — exactMatch / closeMatch / broadMatch / relatedMatch / narrowMatch | 18 / 1.457 / 129 / 194 / 0 | 18 / 1.457 / 129 / 194 / 0 | 0 |
| owl:Nothing post-inferentie | 0 | 0 | 0 |

**Alle tellingen identiek** — exact zoals voorspeld: de fix vervangt uitsluitend het *object* van 2 triples (`xsd:string` → `rdfs:Literal`), zonder triple toe te voegen of te verwijderen. Geen afwijking → geen scope-pauze-trigger (instructie §6).

---

## §1. De mutatie

### 1.1 m21-csf.ttl — twee range-correcties

Aanleiding: HermiT (Protégé, projecteigenaar, 29 mei 2026) meldde de merged graph v4.6.3 **inconsistent** (`owl:Thing SubClassOf owl:Nothing`, 8 justificaties = 4 CSF-Tiers × 2 properties). Diagnose (masterchat, bron-geverifieerd): de twee CSF-Tier-vrije-tekst-properties hebben `rdfs:range xsd:string`, maar dragen `@en`-getagde waarden (`rdf:langString`). Een volledige DL-reasoner ziet dat als datatype-botsing; OWL RL controleert datatype-ranges niet streng (vandaar 0 `owl:Nothing` + 44.907 schone triples onder de canonieke owlrl-config). Dit is de concrete H38-vondst: een reële OWL-RL/DL-divergentie.

| Property (regel) | Voor | Na |
|---|---|---|
| `csf:riskGovernanceDescription` (5436) | `rdfs:range xsd:string ;` | `rdfs:range rdfs:Literal ;` |
| `csf:riskManagementDescription` (5444) | `rdfs:range xsd:string ;` | `rdfs:range rdfs:Literal ;` |

`rdfs:Literal` omvat zowel `xsd:string` als `rdf:langString` → de botsing verdwijnt. Conform de bestaande projectconventie (Optie A masterchat): vrije-tekst-velden gebruiken `rdfs:Literal` (`ext:hasControlStatement`, `ext:hasUVInterpretation`, `ext:hasAttributionText`); `xsd:string` blijft gereserveerd voor identifier-/code-velden zonder taal-tags. De `@en`-waarden en alle overige regels blijven ongemoeid (git-diff: exact 2 regels in m21).

### 1.2 grc-core.ttl — version-bump

`owl:versionInfo` + `owl:versionIRI` bijgewerkt naar 4.6.4.

**Observatie (geen scope-afwijking, ter info):** de version-triples stonden op **"4.6.0"**, niet 4.6.3 — tijdens T1/T2/T3 (v4.6.1/2/3, SKOS-predicate-substituties in m10/m14) zijn de `grc-core`-version-triples kennelijk nooit meegebumpt. v4.6.4 zet ze nu correct op 4.6.4 conform instructie §3. De historische drift (4.6.0 → 4.6.4) is hiermee opgelost; geen verdere actie nodig.

| Regel | Voor | Na |
|---|---|---|
| `owl:versionInfo` | `"4.6.0"` | `"4.6.4"` |
| `owl:versionIRI` | `<…/v4.6.0/>` | `<…/v4.6.4/>` |

### 1.3 Bereedte-bevestiging (m21-only, 2 properties)

Na de fix: **0** resterende `xsd:string`-voorkomens in `m21-csf.ttl` (de twee waren de enige). Dit bevestigt de masterchat-breedte-conclusie: geen andere `xsd:string`-range in m21 die op tagged-waarden kon botsen. De scope-pauze-conditie "meer dan twee botsende range-regels" (instructie §6) deed zich **niet** voor.

---

## §2. Verificatie

### 2.1 Canonieke meet-cyclus (subagent-uitgevoerd) — ✅ conform verwachting

| Run | Resultaat | Verwacht | Status |
|---|---|---|---|
| `canonical_metrics_v4_6_4.py` → `.json` | pre 20.950 / post 44.907 / owl:Nothing 0 | identiek aan v4.6.3 | ✅ |
| `shacl_split_validate_v4_6_4.py` → `.json` | SECTIE A=0, SECTIE B=0, COMBINED=290 | 0 / 0 / 290 | ✅ |
| `file_hashes_v4_6_4.txt` | alleen `m21-csf.ttl` + `grc-core.ttl` gewijzigd; 20 overige + `grc-shacl.ttl` identiek aan v4.6.3 | 2 gewijzigd | ✅ |

`owl:Nothing` = 0 onder de canonieke OWL RL-closure bevestigt de **owlrl-zijde**-consistentie (zoals altijd — OWL RL zag de datatype-botsing niet). De DL-zijde-bevestiging vergt de HermiT-her-run (§2.2).

### 2.2 HermiT-her-run-runbook (projecteigenaar — sluit de H38-lus)

De DL-inconsistentie hoort na de fix weg te zijn. De HermiT-run is een lokale-Mac GUI-actie buiten Claude Code; de merge-input is **al gegenereerd** zodat het één stap is:

1. Input staat klaar: `output/verification/merged_asserted_v4_6_4.ttl` (20.950 triples, alle 21 modules excl. `grc-shacl.ttl`).
   *(reproduceren mag ook: `python3 -c "from rdflib import Graph; from pathlib import Path; g=Graph(); [g.parse(p) for p in sorted(Path('ontology').glob('*.ttl')) if p.name!='grc-shacl.ttl']; g.serialize('output/verification/merged_asserted_v4_6_4.ttl','turtle')"`)*
2. Open `merged_asserted_v4_6_4.ttl` in **Protégé** (Mac).
3. **Reasoner → HermiT** → **Start reasoner**.
4. **Verwacht: CONSISTENT, 0 `owl:Nothing`, geen justificaties.** De 8 v4.6.3-justificaties (4 Tiers × 2 properties) horen verdwenen te zijn.
5. Resultaat terugmelden aan masterchat → H38-lus gesloten ("één reële DL-conformiteits-bevinding gevonden en gefixt, daarna her-geverifieerd").

> Meldt HermiT ná de fix **nog steeds** een inconsistentie (andere bron): **stop, niet zelf doorpatchen** — scope-pauze met de nieuwe justificaties (instructie §6).

---

## §3. Geparkeerde-items-status (Protocol 10)

| H-item | Status | Wijziging door v4.6.4 |
|---|---|---|
| **H38** (OWL RL vs HermiT) | parked → **gefixt + her-te-verifiëren** | Van "waarschijnlijk equivalent, HOLD" naar "één reële DL-divergentie gevonden (datatype-range) en gecorrigeerd". HermiT-her-run (§2.2) levert het sluitende bewijs. Masterchat verwerkt de definitieve H38-status. |
| **H41** (SKOS-axioma-handling) | parked, ongewijzigd | Niet geraakt — geen SKOS-/reasoner-config-wijziging in deze patch. |
| **H37** (open-ontologies-MCP) | parked, ongewijzigd | Niet geraakt. De H38-vondst is een *modelleer*-fout (range), geen aangetoonde OWL RL-*reasoner*-limitatie → versterkt de H37-trigger niet. |

---

## §4. D-decision-conformiteit (D1–D12)

| D | Relevantie | Status |
|---|---|---|
| **D1** (OWL 2 DL) | Kern van deze patch — `rdfs:Literal`-range is OWL 2 DL-conform; de fix herstelt juist de DL-conformiteit (HermiT-consistentie) | ✅ versterkt |
| D2 (Turtle) | edits in Turtle | ✅ |
| D3 (11 namespaces) | geen nieuwe namespace | ✅ |
| D4 (SKOS) | geen SKOS-wijziging | ✅ n.v.t. |
| D5/D11 (sameAs) | 93 + 5 ongewijzigd (gemeten) | ✅ |
| **D6** (bilinguaal + meeliftregel) | edit-scope = 2 property-declaraties (m21) + version-triples (grc-core); binnen die scope alle annotaties al tweetalig | ✅ geen meelift-schuld |
| D7/D8/D9/D10/D12 | niet geraakt | ✅ n.v.t. |

Geen D-schending. Geen D-wijziging voorgesteld.

---

## §5. Aandachtspunten

- **Methodologisch:** dit is het eerste geval waarin een HermiT-bevinding (DL-zijde) een concrete TBox-fix in de canonieke baseline stuurde — bewijst de waarde van de H38-her-run-discipline. OWL RL bleef de fout missen; de canonieke metrics zijn dus *invariant* onder deze fix (een gewenste eigenschap: de fix is puur DL-correctheid, geen telmetingswijziging).
- **Bron-specifiek:** de 8 CSF-Tier-descriptions blijven `@en`-only (NIST CSWP 29-tekst, geen gezaghebbende NL-bron) — bewust, conform D6-symmetrische toepassing. Een `@nl`-vertaling is een aparte inhoudelijke keuze, expliciet **buiten** deze patch (instructie §5).
- **Administratief:** de `grc-core`-version-triple stond historisch op 4.6.0 (drift sinds T1); nu gecorrigeerd naar 4.6.4 (§1.2).

---

## §6. Deliverables (Protocol 16 — met lokaties)

| Deliverable | Lokatie | Aard |
|---|---|---|
| Range-fix (2 properties) | `ontology/m21-csf.ttl` | **gewijzigd bestand 1** |
| Version-bump 4.6.4 | `ontology/grc-core.ttl` | **gewijzigd bestand 2** |
| Canonical-metrics-script | `output/verification/canonical_metrics_v4_6_4.py` | nieuw |
| Canonical-metrics-output | `output/verification/canonical_metrics_v4_6_4.json` | nieuw |
| SHACL-split-script | `output/verification/shacl_split_validate_v4_6_4.py` | nieuw |
| SHACL-split-output | `output/verification/shacl_results_v4_6_4.json` | nieuw |
| File-hashes | `output/verification/file_hashes_v4_6_4.txt` | nieuw |
| HermiT-her-run-input | `output/verification/merged_asserted_v4_6_4.ttl` | nieuw (runbook §2.2) |
| Dit patch-rapport | `output/reports/patch-rapport-v4_6_4.md` | nieuw |

**Twee gewijzigde ontology-bestanden** (m21 + grc-core), conform instructie §4. Overige deliverables zijn meet-/rapport-artefacten.

---

## §7. Disclosure-check (vijf categorieën, Protocol 14)

| # | Categorie | Resultaat |
|---|---|---|
| 1 | Organisatienaam | Geen — "de organisatie"/"Rijksoverheidsorganisatie" waar relevant |
| 2 | Persoonsnamen ≠ Steven | Geen |
| 3 | Lokale paden buiten repo | Geen — alle paden repo-relatief |
| 4 | E-mail/organisatie-TLD's | Geen |
| 5 | NEN-tekst-fragment >10 woorden (handmatige toets) | Geen — geen NEN/ISO-normtekst geraakt; de CSF-descriptions zijn NIST CSWP 29 (publiek domein), niet gewijzigd |

---

## §8. GO-criteria-checklist

- [x] Mutatie surgisch: exact 2 regels in m21 (range), 2 regels in grc-core (version)
- [x] Parse-check beide gewijzigde modules OK
- [x] `xsd:string`-voorkomens in m21 na fix = 0 (breedte bevestigd)
- [x] Canonical metrics identiek aan v4.6.3 (20.950 / 44.907 / owl:Nothing 0)
- [x] SHACL A=0 / B=0 / COMBINED=290 (identiek)
- [x] file_hashes: alleen m21 + grc-core gewijzigd
- [x] Version-bump 4.6.4 doorgevoerd (versionInfo + versionIRI)
- [x] Deliverables-tabel met lokaties (§6)
- [x] D-conformiteit gecheckt (§4); geen schending
- [x] Disclosure-check vijf categorieën schoon (§7)
- [x] **HermiT-her-run consistent (projecteigenaar-actie, §2.2)** — sluit H38-lus *(zie §9)*
- [x] Commit door projecteigenaar (geen autonome commit)

**Tech-conclusie: GO** voor de subagent-uitvoerbare scope. De enige openstaande verificatie is de HermiT-her-run (§2.2, projecteigenaar) — de verwachte bevestiging dat de DL-inconsistentie is opgelost.

— Einde patch-rapport v4.6.4.

---

## §9. Post-oplevering — H38-lus gesloten (masterchat-addendum)

**Vastgelegd:** 4 juni 2026 (masterchat, op verzoek van de projecteigenaar).

De in §2.2 / §8 aan de projecteigenaar gedelegeerde HermiT-her-run op `merged_asserted_v4_6_4.ttl` is **uitgevoerd**, met het verwachte resultaat: **CONSISTENT, 0 `owl:Nothing`, geen justificaties.** De v4.6.3-inconsistentie (8 justificaties = 4 CSF-Tiers × 2 properties) is daarmee opgelost en her-geverifieerd onder een volledige DL-reasoner.

**H38 is hiermee RESOLVED** — OWL RL ≡ HermiT empirisch bevestigd voor deze baseline. Eerste sprint waarin een HermiT-bevinding een TBox-fix in de canonieke baseline stuurde. De beide projecteigenaar-vakjes in §8 zijn op deze bevestiging afgevinkt. De resolved-status is reeds verwerkt in `docs/projectinstructie-v1_11.md`, overdrachtsrapport v6 en brain-iteratie 16; dit addendum sluit de checklist van het patch-rapport zelf gelijk.
