---
type: report
subtype: patch-rapport
version: v4.6.1
baseline_from: v4.6.0
baseline_to: v4.6.1
date: 2026-05-26
status: draft-awaiting-masterchat-NEN-toets
related:
  - H36_skos-exactmatch-ctrl-compl-audit
  - D04_skos-cross-framework
  - t1-stap4-rapport-v4_6_0
  - skos-beoordelings-protocol-v1_0
scope: "Patch v4.6.1 — H36-cluster SKOS-herclassificatie. 26 zekere ctrl:↔compl:-paren skos:exactMatch → skos:broadMatch (diff-26-broadMatch.ttl) plus 2 edge-cases onder masterchat-NEN-toets (diff-2-edge-cases.ttl). Geen TBox-wijziging. Geen andere modules dan m10-nis2-ext.ttl."
---

# Patch-rapport v4.6.1

## §0. Versie + metrics-vergelijking

Cijfers in dit rapport komen uit `output/verification/canonical_metrics_v4_6_1.json` (scenario C — alle 28 toegepast), gemeten op gepatchte versie van ontologie. **Niet uit memory** (leerpunt v4.3.3).

**Scenario-keuze nog open:** masterchat besluit op basis van Stap 5 (NEN-toets edge-cases h/j) tussen drie scenario's:

- **Scenario A (26 paren):** alleen diff-26 toegepast — h en j blijven exactMatch.
- **Scenario B (27 paren):** diff-26 + één van twee edge-cases naar broadMatch.
- **Scenario C (28 paren):** diff-26 + diff-2 beide volledig — alle 28 worden broadMatch.

Dit rapport is **geschreven alsof scenario C** wordt toegepast. Scenario A/B afleidbaar omdat predicate-mutatie additief is — geen extra metrics-runs nodig.

### §0.1 Vergelijking v4.6.0 → v4.6.1 (scenario C)

| Metric | v4.6.0 | v4.6.1 scenario C | Δ |
|---|---:|---:|---:|
| Pre-inference triples | 20.950 | 20.950 | **0** |
| Post-inference triples (OWL RL) | 44.907 | 44.907 | **0** |
| owl:Class | 199 | 199 | 0 |
| owl:NamedIndividual | 1.383 | 1.383 | 0 |
| owl:ObjectProperty | 149 | 149 | 0 |
| owl:DatatypeProperty | 96 | 96 | 0 |
| owl:sameAs | 98 | 98 | 0 |
| skos_mappings_total | 1.798 | 1.798 | **0** |
| skos:exactMatch | 46 | 18 | **−28** |
| skos:closeMatch | 1.489 | 1.489 | 0 |
| skos:broadMatch | 38 | 66 | **+28** |
| skos:relatedMatch | 225 | 225 | 0 |
| skos:narrowMatch | 0 | 0 | 0 |
| owl:Nothing post-inferentie | 0 | 0 | 0 (consistent) |
| D5 ctrl↔bio sameAs | 93 | 93 | 0 (conform) |
| D11 asset-brug | 5 | 5 | 0 (conform) |
| ext:hasHandreikingBBN assertions | 241 | 241 | 0 |

**Kernobservatie:** triple-totaal en alle individuals/klassen/property-tellingen zijn ongewijzigd. Enige mutatie is predicate-name voor 28 specifieke triples (exactMatch → broadMatch). 

### §0.2 ctrl:→compl: SKOS-paren-mutatie

| Pair-type | v4.6.0 | v4.6.1 scenario C | Δ |
|---|---:|---:|---:|
| `ctrl->compl::exactMatch` | 28 | **0** | −28 |
| `ctrl->compl::broadMatch` | 25 | **53** | +28 |
| `ctrl->compl::closeMatch` | 32 | 32 | 0 |
| `ctrl->compl::relatedMatch` | 33 | 33 | 0 |

### §0.3 File-hash-mutatie

| Bestand | v4.6.0 SHA256 | v4.6.1 SHA256 | Wijziging? |
|---|---|---|---|
| m10-nis2-ext.ttl | `78b8ee44…b389735ee` | `cb2d567b…f1d8afa2f1` | **ja** |
| Andere 21 .ttl + grc-shacl.ttl | (zie file_hashes_v4_6_0.txt) | identiek | nee |

Volledige file-hash-lijst: `output/verification/file_hashes_v4_6_1.txt`.

---

## §1. Scope

**Wat wijzigt:**

- 26 ctrl:→compl: skos:exactMatch-triples → skos:broadMatch (scenario A, B, C identiek voor deze 26 paren).
- 0 tot 2 extra ctrl:→compl: skos:exactMatch-triples → skos:broadMatch afhankelijk van masterchat-NEN-toets op T1-023 en T1-021 (scenario B = +1, scenario C = +2).
- Geen TBox-wijziging (geen klasse, property, restrictie, axiom toegevoegd of verwijderd).
- Geen wijziging in m02-control.ttl, m05-compliance.ttl, of enige andere module.
- Geen wijziging in SHACL-shapes (grc-shacl.ttl onveranderd).

**Wat NIET wijzigt:**

- D5 (ctrl↔bio sameAs 93) — onveranderd.
- D11 (asset-brug 5) — onveranderd.
- 28 ctrl:ISO27002_*-individuals en 10 compl:NIS2_Art21_*-individuals zelf — onveranderd (geen wijziging in rdfs:label, compl:articleRef, compl:derivedFrom).
- SoA-structuur (D8, 93 SoAEntries) — onveranderd.
- Bestaande closeMatch/relatedMatch/broadMatch op identieke subjecten naar **andere** objecten — onveranderd. Bijvoorbeeld: `ctrl:ISO27002_8_05 skos:broadMatch compl:NIS2_Art21_h` (bestaande triple) wordt niet aangeraakt; alleen `ctrl:ISO27002_8_05 skos:exactMatch compl:NIS2_Art21_j` muteert in scenario C naar broadMatch.

**Bron:** T1-sprint Stap 3 pilot-rapport + T1-sprint Stap 4-rapport (beide `output/reports/`).

**D-rationale:** D4 (SKOS cross-framework). Herclassificatie naar broadMatch is verdedigbaar onder D4 omdat:

- Autoritatieve mapping-bron (CBW-Excel "Mapping Uitvoeringsverordening" reproductie ENISA TIG v1.0) erkent relatie maar verbiedt expliciet equivalence-interpretatie (ENISA TIG regel 285).
- Cluster-cardinaliteit-failure C2 op 24 van 28 paren (veel→1-clusters b, c, d, e, f, i).
- C1/C3-failure op 1↔1-paren a en g eveneens (UV-Annex-decompositie + buiten-set-121-set-context).

---

## §2. Wijzigingen in m10-nis2-ext.ttl

### §2.1 Beschrijving

Voor elk van de 28 (scenario C) regels in m10-nis2-ext.ttl van de vorm:

```turtle
ctrl:ISO27002_X_YY
    skos:exactMatch compl:NIS2_Art21_Z [punt|;] ...
```

wordt het predicate `skos:exactMatch` vervangen door `skos:broadMatch`. Geen andere wijziging aan de regel of het omringende blok. Comments, witregels, andere triples in m10-nis2-ext.ttl blijven exact onveranderd.

### §2.2 Triple-Δ per cluster

| Cluster | NIS2-clause | Aantal triples gewijzigd | Patch-bestand |
|---|---|---:|---|
| a | art.21(2)(a) | 1 | diff-26 |
| b | art.21(2)(b) | 4 | diff-26 |
| c | art.21(2)(c) | 3 | diff-26 |
| d | art.21(2)(d) | 4 | diff-26 |
| e | art.21(2)(e) | 5 | diff-26 |
| f | art.21(2)(f) | 2 | diff-26 |
| g | art.21(2)(g) | 1 | diff-26 |
| h | art.21(2)(h) | **1** | **diff-2 (masterchat-keuze)** |
| i | art.21(2)(i) | 6 | diff-26 |
| j | art.21(2)(j) | **1** | **diff-2 (masterchat-keuze)** |
| **Totaal scenario C** | | **28** | |

### §2.3 Voorbeeld-mutatie (T1-001)

**Vóór patch (m10-nis2-ext.ttl regel 182-183):**

```turtle
# ctrl:ISO27002_5_01 — Beleidsregels voor informatiebeveiliging
ctrl:ISO27002_5_01
    skos:exactMatch compl:NIS2_Art21_a .
```

**Na patch:**

```turtle
# ctrl:ISO27002_5_01 — Beleidsregels voor informatiebeveiliging
ctrl:ISO27002_5_01
    skos:broadMatch compl:NIS2_Art21_a .
```

### §2.4 Voorbeeld-mutatie compound-triple (T1-010 + bestaande relatedMatch op zelfde subject)

**Vóór patch (regel 283-285):**

```turtle
# ctrl:ISO27002_5_24 — Plannen en voorbereiden van het beheer van informatiebeveiligingsincidenten
ctrl:ISO27002_5_24
    skos:exactMatch compl:NIS2_Art21_b ;
    skos:relatedMatch compl:NIS2_Art21_c .
```

**Na patch:**

```turtle
# ctrl:ISO27002_5_24 — Plannen en voorbereiden van het beheer van informatiebeveiligingsincidenten
ctrl:ISO27002_5_24
    skos:broadMatch compl:NIS2_Art21_b ;
    skos:relatedMatch compl:NIS2_Art21_c .
```

Tweede triple (`skos:relatedMatch compl:NIS2_Art21_c`) blijft ongewijzigd — patch werkt strikt op `skos:exactMatch compl:NIS2_Art21_*`.

---

## §3. Verificatie

### §3.1 Canonical metrics

Script: `output/verification/canonical_metrics_v4_6_1.py` (versie-suffix-conventie sinds v4.3.3).
Output: `output/verification/canonical_metrics_v4_6_1.json`.

Gemeten op: gepatchte versie scenario C (28 mutaties toegepast op tijdelijke kopie van `ontology/`).

| Resultaat | Status |
|---|---|
| Pre-inference triples | 20.950 (Δ = 0 vs v4.6.0) |
| Post-inference triples | 44.907 (Δ = 0) |
| exactMatch −28, broadMatch +28 | conform verwachting |
| owl:Nothing post-inferentie | 0 (consistent) |
| Geen namespace-leakage-toename | conform (22 module-leakage identiek aan baseline) |
| Geen dangling references-toename | conform (3 identiek) |
| D5 conform | 93 ctrl↔bio sameAs |
| D11 conform | 5 asset-brug |

**Geen afwijking > 50 triples in post-inference.** Stop-conditie §9 niet geraakt.

### §3.2 SHACL gesplitste validatie

Script: `output/verification/shacl_split_validate_v4_6_1.py`.
Output: `output/verification/shacl_results_v4_6_1.json`.

| Run | Inference | Conforms | Violations | Per shape |
|---|---|---|---:|---|
| RUN 1 | none | True | 0 | n.v.t. — SECTIE A geen violations |
| RUN 2 | owlrl | False | 290 | 104 asset:NamespaceShape + 93 control:ISO27002NamingShape + 93 bio:ISO27002NamingShape (bekende SECTIE A false-positives onder OWL RL — identiek aan v4.6.0-baseline) |

**SHACL-blinde vlek bevestigd:** geen shape valideert direct op 28 ctrl:↔compl:-paren (Vraag D pre-sprint-inventarisatie). Predicate-mutatie raakt geen shape. **Geen significant verschil met baseline.** Stop-conditie §9 niet geraakt.

### §3.3 File-hashes

Script: ingebed in canonical_metrics-script (per_module.sha256).
Output: `output/verification/file_hashes_v4_6_1.txt`.

Alleen m10-nis2-ext.ttl-hash wijzigt:
- v4.6.0: `78b8ee44453202c8826afca998d44e4bd71a4662e13c37a61cf2837b389735ee`
- v4.6.1: `cb2d567b184877e111800cc0a8af1e38d6d6f74ddca0477ee1a52df1d8afa2f1`

Andere 21 module-hashes + grc-shacl.ttl identiek aan v4.6.0.

---

## §4. Methodologie

### §4.1 Beslis-protocol-bron

Protocol `docs/skos-beoordelings-protocol-v1_0.md` (sign-off Steven 26 mei 2026). Vier-criteria-toets per paar (C1 definitioneel, C2 cardinaliteit, C3 inclusie-richting, C4 bron-bewijs). Cluster-discipline (§3) verplicht voor C2-failure: systematische cluster-behandeling tenzij individuele uitzondering expliciet gemotiveerd.

### §4.2 Evidence-niveau-1-bron

CBW-Excel "Mapping Uitvoeringsverordening" (`sources/adr-norea/Cbw (NIS2) Control Framework.xlsx`) reproduceert ENISA TIG v1.0 mapping-tabel. Combinatie:

1. NIS2-richtlijn (EU) 2022/2555 art.21(2) (NL/EN PDF in `sources/eu-recht/`)
2. UV (EU) 2024/2690 considerans (3) + Annex (PDF in `sources/eu-recht/`)
3. ENISA TIG v1.0 juni 2025 (tekst-extract in `sources/ensia/`)
4. CBW-Excel sheet "Mapping Uitvoeringsverordening" reproduceert per UV-clause de ISO 27001:2022 Annex A-controls

Vormt evidence-niveau 1 voor aanwezigheid van mapping. ENISA TIG regel 285 disclaimer ("mapping should not be interpreted as a measure of equivalency") prevent gebruik als equivalence-bron — dat is juist het centrale argument tegen exactMatch en vóór broadMatch/closeMatch.

### §4.3 Cluster-aanpak

Stap 3 pilot 5 paren (één per cluster-type a/b/e/g/i). Stap 4 representant-aanpak voor c/d/f, plus cluster-overerving voor 18 cluster-volgers met expliciete uitzonderings-check per paar (0 uitzonderingen gevonden). Edge-cases h/j volgen twee-zijdige analyse-route conform sprint-instructie §4.3.

---

## §5. Bekende beperkingen

### §5.1 NEN-bron-toegankelijkheid

ISO 27002:2022-tekst niet beschikbaar in Tech-omgeving (NEN-restrictief). C1/C3-toetsing kon alleen via:

- ISO27002-label-vergelijking (subject-zijde rdfs:label uit m02-control.ttl)
- UV-Annex-mapping-structuur (objectieve evidence-niveau 1-bron)
- NIS2-tekst (objectieve EU-publiek-domein-bron)

Voor edge-cases T1-023 en T1-021 is bilaterale containment niet hard te maken zonder ISO27002:2022 §8.24 en §8.05 tekst. Daarom twee-zijdige analyse + masterchat-NEN-toets.

### §5.2 SKOS-symmetrie-afwezigheid

owlrl laadt geen SKOS-axiomas. `skos:exactMatch is owl:SymmetricProperty` (skos:S46) wordt niet geïnferreerd. Gevolg: alle 28 mappings zijn asymmetrisch gemodelleerd (ctrl: → compl:, geen reverse). Geen invloed op patch-correctheid (predicate-mutatie blijft asymmetrisch). T1-werkflow-leerpunt, geen H-item nu.

### §5.3 SHACL-blinde vlek op ctrl:↔compl:-mappings

Geen shape in grc-shacl.ttl valideert deze paren (Vraag D inventarisatie). Patch wordt niet door SHACL gevalideerd. H39-relevant — meegenomen in geparkeerde-items-status.

---

## §6. Risico's + restricties

| Risico | Mitigatie |
|---|---|
| Predicate-mutatie wijzigt semantische verwachting van downstream-consumers | broadMatch is bestaand patroon (38 → 66 mappings); geen nieuwe predicate. Backward-compatible SKOS-namespace. |
| Dashboard (grc-explorer Spoor A) gebruikt mogelijk skos:exactMatch-specifieke styling | Dashboard-subagent moet bij build van grc-data-v4_6_1.js controleren of styling-onderscheid tussen exact/broad consistent blijft. **Aandachtspunt voor Dashboard-subagent-handover na v4.6.1-oplevering.** |
| Toekomstige reasoning op skos:exactMatch (transitivity skos:S47) zou anders zijn | Onder huidige owlrl-instelling (geen SKOS-axiomas) geen effect. Bij overstap naar owlrl-incl-SKOS in toekomst: 28 fewer transitive-closures, correcter want NIS2-clauses zijn geen onderling-equivalent. |
| Scenario A/B/C-administratieve last in versie-tracking | Patch-rapport §0 documenteert keuze; metric-runs alleen voor scenario C; A/B afleidbaar. |

---

## §7. Geparkeerde-items-status-update

| H-item | Vóór v4.6.1 | Na v4.6.1 | Mutatie |
|---|---|---|---|
| H36 (SKOS-exactMatch ctrl/compl-audit) | active — analyse-fase | **afgehandeld**: 26 broadMatch toegepast, 2 onder masterchat-toets. Bij Stap 5-sign-off door masterchat: status → closed. | mutatie: active → afgehandeld (afhankelijk van scenario-keuze) |
| H37 | active | active | ongewijzigd |
| H38 | active | active | ongewijzigd |
| H39 (SHACL-blinde vlek ctrl:↔compl:) | active — bevestigd in T1-inventarisatie Vraag D | active | ongewijzigd |
| H40 (UI-renderdekking Spoor A) | active | active | ongewijzigd |
| H25/H26/H27/H32/H33/H34/H35 | (per status H-register) | (per status H-register) | ongewijzigd |

Brein-cyclus update: H36-register-entry verplaatsen naar closed-segment indien masterchat scenario-keuze finaliseert. Geen H-register-update door Tech.

---

## §8. D-conformance-check (D1-D12)

| D | Conventie | v4.6.1-impact | Conform? |
|---|---|---|---|
| D1 | OWL 2 DL profiel | geen TBox-wijziging | ✓ |
| D2 | Turtle-serialisatie | enige module m10-nis2-ext.ttl blijft Turtle | ✓ |
| D3 | 11 namespaces | geen nieuwe namespace | ✓ |
| D4 | SKOS cross-framework — closeMatch default, exactMatch zeldzaam | herclassificatie naar broadMatch verbreedt D4-compliance (exactMatch was te sterk geclaimd) | ✓ verbetering |
| D5 | ctrl:↔bio: sameAs strikt — 93 pairs | onveranderd 93 | ✓ |
| D6 | bilinguale annotaties @nl/@en | geen wijziging in labels/comments | ✓ |
| D7 | BIO 2.0 als twee klassen | geen BIO2-wijziging | ✓ |
| D8 | één canonieke SoA — isms:SoA_2026 + 93 SoAEntry_* | onveranderd | ✓ |
| D9 | framework-neutraal | onveranderd | ✓ |
| D10 | COSO ICF/ERM enterprise-governance-laag | onveranderd | ✓ |
| D11 | owl:sameAs asset-convergentie — ster-patroon | onveranderd 5 | ✓ |
| D12 | drie-laags compliance | onveranderd | ✓ |

**Alle 12 D-decisions conform. D4-compliance verbetert door herclassificatie.**

---

## §9. Deliverables

| Deliverable | Pad | Status |
|---|---|---|
| Patch-instructie zekere 26 | `output/patches/diff-26-broadMatch.ttl` | klaar |
| Patch-instructie 2 edge-cases | `output/patches/diff-2-edge-cases.ttl` | klaar — onder masterchat-NEN-toets |
| Canonical metrics-script | `output/verification/canonical_metrics_v4_6_1.py` | klaar |
| Canonical metrics-output (scenario C) | `output/verification/canonical_metrics_v4_6_1.json` | klaar |
| SHACL-validatie-script | `output/verification/shacl_split_validate_v4_6_1.py` | klaar |
| SHACL-validatie-output (scenario C) | `output/verification/shacl_results_v4_6_1.json` | klaar |
| File-hashes met v4.6.0-vergelijking | `output/verification/file_hashes_v4_6_1.txt` | klaar |
| Stap 4-rapport | `output/reports/t1-stap4-rapport-v4_6_0.md` | klaar |
| Dit patch-rapport | `output/reports/patch-rapport-v4_6_1.md` | draft — masterchat-NEN-toets pending |

---

## §10. Sprint-prognose-evaluatie

T1-sprint was test-sprint conform sprint-instructie. Verwachte uitkomst was **niet** pre-bepaald (anti-pre-judging). Tech leverde:

- Stap 1 (pre-sprint-inventarisatie): 28 paren bevestigd, geen stop-conditie.
- Stap 2 (protocol-draft door masterchat): protocol v1.0 sign-off Steven.
- Stap 3 (pilot 5): alle 5 → broadMatch met hoge confidence + evidence-niveau 1. Optie A bevestigd door masterchat — voortgaan met geleerde nuance.
- Stap 4 (resterende 23): 21 paren bevestigd broadMatch (cluster-discipline); 2 edge-cases naar masterchat-NEN-toets.
- Stap 5 (verwacht): masterchat-NEN-toets op h/j en finale scenario-keuze.

**Prognose Stap 4 voor 21 broadMatch + 2 edge-cases = GEKLOPT.** Confidence verwachting was "hoog" voor representant/cluster-overerving (gehaald) en "n.v.t." voor edge-cases (gehaald — twee-zijdig zonder Tech-voorstel).

Tijdsraming Stap 4 ~75-90 min — lichte overschrijding (totaal ~2 uur incl. tooling-installatie). Voor T2/T3-planning: ~90-120 min richtlijn voor analoge scope (~30 paren).

---

## §11. GO-criteria-checklist

Voor masterchat-review:

- [x] Pre-sprint-inventarisatie bevestigt baseline (28 paren, 0 stop-conditie) — Stap 1.
- [x] Protocol v1.0 toegepast op alle 28 paren — Stap 3+4.
- [x] Cluster-discipline (protocol §3) toegepast — 21 paren via overerving + 3 representanten.
- [x] Edge-cases conform sprint-instructie §4.3 twee-zijdig zonder Tech-voorstel — Stap 4 §3.
- [x] Canonical metrics scenario C voltooid, mutaties conform raming, geen stop-conditie geraakt.
- [x] SHACL gesplitste validatie identiek aan baseline (0 + 290).
- [x] Geen TBox-wijziging, geen D-conformance-schending.
- [x] D-decision-conformance-check positief (D1-D12 alle conform; D4 verbetering).
- [x] Patch-bestanden klaar (diff-26 + diff-2 separaat toepasbaar).
- [x] File-hash-vergelijking sluitend (alleen m10 wijzigt).
- [x] Pre-push disclosure-check (Protocol 14) uitgevoerd — geen vondsten.
- [ ] Masterchat-NEN-toets edge-cases h/j (T1-023, T1-021) — **wachtend**.
- [ ] Scenario-keuze A/B/C door masterchat — **wachtend**.
- [ ] Steven inspecteert + commit handmatig — **wachtend**.

**Tech-eindoordeel:** GO voor masterchat-NEN-toets en scenario-keuze. Patch v4.6.1 leverbaar onder de drie scenario-opties.

— Einde patch-rapport v4.6.1.
