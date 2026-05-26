---
type: report
subtype: sprint-eindrapport
sprint: T1
baseline_from: v4.6.0
baseline_to: v4.6.1
date: 2026-05-26
status: final
related:
  - H36_skos-exactmatch-ctrl-compl-audit
  - D04_skos-cross-framework
  - skos-beoordelings-protocol-v1_0
  - t1-presprint-inventarisatie-v4_6_0
  - t1-pilot-rapport-stap3-v4_6_0
  - t1-stap4-rapport-v4_6_0
  - patch-rapport-v4_6_1
scope: "T1-sprint volledig — H36-cluster afgehandeld via 28 SKOS-herclassificaties exactMatch → broadMatch. Methode-protocol v1.0 vastgesteld als herbruikbare T2/T3-output. Werkflow-leerpunten voor productie-fase-discipline."
---

# T1-sprint Eindrapport — SKOS-kwaliteitsanalyse Fase 1 (H36-cluster)

## §0. Sprint-meta + uitkomst-samenvatting

**Sprint:** T1 — SKOS-kwaliteitsanalyse Fase 1 (H36-cluster: 28 ctrl:↔compl: exactMatch-paren)
**Periode:** 26 mei 2026 (één dag, vijf stappen)
**Baseline-mutatie:** v4.6.0 → v4.6.1 patch-release
**Sprint-type:** T1 test-sprint — eerste post-migratie werkflow-validatie

### Uitkomst in één blik

| Aspect | Resultaat |
|---|---|
| H36-cluster (28 paren) | **28 × herclassificatie exactMatch → broadMatch** |
| Confidence per paar | 28× hoog |
| Evidence-niveau per paar | 28× niveau 1 (CBW-Excel "Mapping Uitvoeringsverordening") |
| Twijfelgevallen | 2 edge-cases (T1-021 + T1-023) opgelost via masterchat-NEN-PK-toets |
| H36-status | **afgehandeld** — closed na patch v4.6.1 |
| Methode-protocol | **v1.0 vastgesteld** — herbruikbaar voor T2/T3 |
| D4-conformance | verbetering (exactMatch was te sterk geclaimd) |
| Andere D-decisions | onveranderd (D1-D3, D5-D12) |

### Werkflow-validatie (T1-test-doel)

| Werkflow-aspect | Bevinding |
|---|---|
| Pre-sprint-inventarisatie (Protocol B) | werkte als gepland; 0 stop-condities |
| Sample-first met cluster-spreiding | werkte; pilot leverde structureel inzicht |
| Cluster-discipline | werkte; geen half-half-cluster-behandeling |
| Edge-case-escalatie naar masterchat | werkte; twee-zijdige analyse-format effectief |
| NEN-PK-werkverdeling Tech↔Masterchat | werkte; nieuw werkflow-patroon vastgesteld |
| Vijf overhandigings-momenten | alle vijf bereikt; sprint binnen één dag voltooid |
| Protocol 14 pre-push disclosure-check | eerste productie-toepassing; ~3 min per rapport |

### Patch-uitkomst v4.6.1

| Metric | v4.6.0 | v4.6.1 | Δ |
|---|---:|---:|---:|
| Triples pre-inf | 20.950 | 20.950 | 0 |
| Triples post-inf | 44.907 | 44.907 | 0 |
| skos:exactMatch | 46 | 18 | −28 |
| skos:broadMatch | 38 | 66 | +28 |
| SKOS-totaal | 1.798 | 1.798 | 0 |
| owl:Nothing post-inf | 0 | 0 | 0 |
| D5 ctrl↔bio sameAs | 93 | 93 | 0 |
| D11 asset-brug | 5 | 5 | 0 |
| SHACL RUN 1 / RUN 2 | 0 / 290 | 0 / 290 | 0 / 0 |
| m10-nis2-ext.ttl hash | 78b8ee44... | cb2d567b... | gewijzigd |

Alle 21 andere modules + grc-shacl.ttl: hash onveranderd.

---

## §1. Context en aanleiding

T1 was de **eerste post-migratie productie-sprint** na voltooiing van de migratie van Tech/Brein/Dashboard naar Claude Code + GitHub. Doel was tweeledig:

1. **Inhoudelijk:** H36-cluster (28 ctrl:→compl: `skos:exactMatch`-paren) toetsen op D4-conformiteit
2. **Methodisch:** herbruikbaar SKOS-beoordelings-protocol vaststellen voor T2/T3 (overige 1.770 SKOS-mappings)

H36 stond geparkeerd in brain-vault sinds iteratie 12 (`brain__architecture__H36_skos-exactmatch-ctrl-compl-audit.md`). Trigger was "SKOS-kwaliteitsanalyse-sprint" — vervuld door de keuze van H36-cluster als pilot voor de bredere SKOS-kwaliteitsanalyse-werkstroom.

Belangrijke achtergrond uit pre-sprint-inventarisatie:
- 28 paren bevestigd, allemaal in `m10-nis2-ext.ttl`
- Subject-zijde: 28× `ctrl:ISO27002Control`
- Object-zijde: 28× `compl:RegulatoryObligation`
- Geen D5-collisions
- Geen SHACL-shape-validatie op deze paren (Vraag D — H39-relevant, T1-scope-vrij)

---

## §2. Sprint-uitvoering — vijf stappen

### Stap 1 — Pre-sprint-inventarisatie (Tech, ~15 min)

**Bron:** `output/reports/t1-presprint-inventarisatie-v4_6_0.md`

5 inventarisatie-vragen (A-E) door Tech read-only beantwoord. Verificatie-getal 28 bevestigd. Geen stop-conditie geraakt. Vraag B (multi-module-discipline) leverde belangrijk context-getal: 121 ctrl:↔compl:-mappings in totaal (28 exact + 32 close + 60 related + 27 broad), wat het 19%-aandeel van exactMatch in het bredere cluster aangaf.

### Stap 2 — Methode-protocol v1.0 (Masterchat + Steven sign-off, ~30 min)

**Bron:** `docs/skos-beoordelings-protocol-v1_0.md`

Vier-criteria-set (C1 definitioneel, C2 cardinaliteit, C3 inclusie-richting, C4 bron-evidence) + beslis-tabel + evidence-hiërarchie + twijfelgevallen-procedure + cluster-discipline-regel. Sign-off Steven 26 mei 2026 op vijf open beslis-punten:

1. Sample-keuze pilot-5 (T1-001, T1-020, T1-010, T1-002, T1-024)
2. Pilot-stop-conditie aangepast (inhoudelijk i.p.v. numeriek)
3. Cluster-discipline binnen C2-failure verplicht
4. SKOS-symmetrie-afwezigheid als T1-leerpunt, geen nieuw H-item
5. Evidence-niveau-onderzoek als pre-stap binnen Stap 3

### Stap 3 — Pilot van 5 (Tech, ~75 min) + Masterchat-escalatie

**Bron:** `output/reports/t1-pilot-rapport-stap3-v4_6_0.md`

**Inhoudelijke uitkomst:** alle 5 pilot-paren → broadMatch met hoog vertrouwen en evidence-niveau 1. Inclusief paren #1 (T1-001 cluster a) en #2 (T1-020 cluster g) — beide 1↔1 binnen 28-set, waar het protocol-§6-verwachting "behoud" was.

**Stop-conditie 1 (onverwachte uitkomst-richting) strikt gelezen geraakt.** Tech escaleerde correct naar masterchat (overhandigings-moment 3/5).

**Belangrijkste evidence-vondst:** CBW-Excel sheet "Mapping Uitvoeringsverordening" (`sources/adr-norea/`) blijkt **ENISA TIG v1.0 mapping-tabel te reproduceren** — autoritatieve bron NIS2 ↔ ISO 27002:2022 mapping op clausule-niveau. Bewijsketen:

1. NIS2-richtlijn (EU) 2022/2555 art.21 → "de stand van de techniek en de desbetreffende Europese en internationale normen"
2. UV (EU) 2024/2690 considerans (3) → "based on European and international standards, such as ISO/IEC 27001, ISO/IEC 27002"
3. UV-Annex hoofdstukken 1-13 → expliciet gekoppeld aan NIS2 art.21-letters
4. ENISA TIG v1.0 juni 2025 → per-sectie mapping-tabellen
5. CBW-Excel reproduceert ENISA TIG-tabel

**Cruciale paradox:** ENISA TIG regel 285 stelt expliciet "*The mapping should not be interpreted as a measure of equivalency among different standards or frameworks.*" Autoritatieve bron erkent relatie maar verbiedt equivalence-interpretatie. Dit ondergraaft `exactMatch` als juiste SKOS-keuze op evidence-niveau 1.

**Masterchat-besluit:** Optie A — voortgaan naar Stap 4 met geleerde nuance. C2-criterium moet binnen 121-set worden getoetst, niet alleen binnen 28-set. Inhoudelijk klopt protocol; pre-pilot-verwachting in §6 was te zwaar op C2-strikte-28-set.

### Stap 4 — Resterende 23 paren (Tech, ~2 uur)

**Bronnen:** `output/reports/t1-stap4-rapport-v4_6_0.md` + `output/reports/patch-rapport-v4_6_1.md`

**Aanpak:**
- Cluster-representant-beoordeling voor c (T1-014), d (T1-006), f (T1-016) — alle 3 → broadMatch
- Cluster-discipline-overerving voor 18 cluster-volgers (b, c, d, e, f, i) — alle 18 → broadMatch, geen uitzonderingen
- Edge-case twee-zijdige analyse voor T1-023 (h) en T1-021 (j) — verplichte masterchat-escalatie via NEN-PK-vragen

**Patch-voorbereiding:** twee TTL-diff-bestanden (`diff-26-broadMatch.ttl` voor zekere 26, `diff-2-edge-cases.ttl` voor 2 onder voorbehoud) + canonical metrics scenario C + SHACL + file-hashes.

### Stap 5 — Masterchat-NEN-PK-toets edge-cases (Masterchat + Steven, ~20 min)

Op basis van ISO 27002:2022 §8.05 en §8.24 tekst uit project knowledge:

**T1-023 (NIS2_h ↔ ISO27002 §8.24):** ISO27002 §8.24 dekt **meer** dan het label suggereert (was voorheen 10.1.1 + 10.1.2 in ISO 27002:2013) — beleid + procedures + sleutelbeheer + gebruik. Bilaterale containment marginaal-positief voor exactMatch op clause-niveau. Maar:

- C2 faalt op 121-set-niveau: NIS2_h heeft 7 ctrl:-mappings (1 exact + 1 close + 2 related + 3 broad)
- Consistency met pilot #1 en #2 (1↔1-binnen-28-set, veel→1-in-121-set)
- ENISA-disclaimer-categorisch-effect

→ **broadMatch** (niet vanwege C1/C3-failure, maar 121-set-cardinaliteit + consistency)

**T1-021 (NIS2_j ↔ ISO27002 §8.05):** ISO27002 §8.05 dekt MFA én continuous-style elementen ("vergezeld te gaan van aanvullende authenticatiefactoren ... zoals toegang vanaf een ongebruikelijke locatie, een ongebruikelijk apparaat of op een ongebruikelijk tijdstip"). Maar dekt **niet** secured voice/video/text communications + secured emergency communication systems uit NIS2_j.

- C1 faalt: NIS2_j omvat secured-communications, §8.05 niet
- C2 faalt: 9 ctrl:-mappings in 121-set
- C3 faalt: B ⊄ A — secured-communications zit niet in §8.05

→ **broadMatch** (duidelijke C1/C3-failure + 121-set-cardinaliteit)

**Scenario-keuze: C — alle 28 broadMatch.**

### Stap 6 — Patch-toepassing v4.6.1 (Steven, ~25 min)

**Tooling-incident:** Tech leverde diff-bestanden als **specificaties** (lijst van paren + handmatige/sed/python-instructie), niet als unified-diff-format. `patch -p0` faalde met "I can't seem to find a patch in there anywhere." Masterchat schreef werkbare Python-applier `apply_patch_v4_6_1.py` met backup + count-verificatie + faal-veilig-exit.

**Toepassing-uitkomst:**
- 28 mutaties succesvol
- Backup `ontology/m10-nis2-ext.ttl.v4_6_0.bak` aangemaakt
- Hash-verificatie: `cb2d567b184877e111800cc0a8af1e38d6d6f74ddca0477ee1a52df1d8afa2f1` ✓
- Canonical metrics: alle 28 mutaties + 0 nevenwijziging ✓
- SHACL gesplitste validatie: RUN 1 = 0, RUN 2 = 290 (identiek aan v4.6.0) ✓
- Commit + push voltooid

---

## §3. Uitkomst per paar (28 totaal)

### 3.1 Cluster-overzicht

| Cluster | NIS2-clause | Aantal | Pilot/representant | Uitkomst |
|---|---|---:|---|---|
| a | Risicoanalyse + beleidsregels | 1 | T1-001 (pilot) | 1× broadMatch |
| b | Incidentbehandeling | 4 | T1-010 (pilot) | 4× broadMatch |
| c | Continuïteit + back-up | 3 | T1-014 (representant) | 3× broadMatch |
| d | Toeleveringsketen | 4 | T1-006 (representant) | 4× broadMatch |
| e | Verwerving + ontwikkeling | 5 | T1-024 (pilot) | 5× broadMatch |
| f | Doeltreffendheid-beoordeling | 2 | T1-016 (representant) | 2× broadMatch |
| g | Cyberhygiëne + opleiding | 1 | T1-020 (pilot) | 1× broadMatch |
| h | Cryptografie | 1 | T1-023 (edge-case) | 1× broadMatch |
| i | Personeel + toegang + activa | 6 | T1-002 (pilot) | 6× broadMatch |
| j | Multi-factor auth | 1 | T1-021 (edge-case) | 1× broadMatch |
| **Totaal** | | **28** | | **28× broadMatch** |

### 3.2 Volledige paren-lijst

| Paar-ID | Subject | Object | Cluster | Pilot/Cluster/Edge | Confidence |
|---|---|---|---|---|---|
| T1-001 | ctrl:ISO27002_5_01 | compl:NIS2_Art21_a | a | pilot | hoog |
| T1-002 | ctrl:ISO27002_5_09 | compl:NIS2_Art21_i | i | pilot | hoog |
| T1-003 | ctrl:ISO27002_5_15 | compl:NIS2_Art21_i | i | cluster | hoog |
| T1-004 | ctrl:ISO27002_5_16 | compl:NIS2_Art21_i | i | cluster | hoog |
| T1-005 | ctrl:ISO27002_5_18 | compl:NIS2_Art21_i | i | cluster | hoog |
| T1-006 | ctrl:ISO27002_5_19 | compl:NIS2_Art21_d | d | representant | hoog |
| T1-007 | ctrl:ISO27002_5_20 | compl:NIS2_Art21_d | d | cluster | hoog |
| T1-008 | ctrl:ISO27002_5_21 | compl:NIS2_Art21_d | d | cluster | hoog |
| T1-009 | ctrl:ISO27002_5_22 | compl:NIS2_Art21_d | d | cluster | hoog |
| T1-010 | ctrl:ISO27002_5_24 | compl:NIS2_Art21_b | b | pilot | hoog |
| T1-011 | ctrl:ISO27002_5_25 | compl:NIS2_Art21_b | b | cluster | hoog |
| T1-012 | ctrl:ISO27002_5_26 | compl:NIS2_Art21_b | b | cluster | hoog |
| T1-013 | ctrl:ISO27002_5_27 | compl:NIS2_Art21_b | b | cluster | hoog |
| T1-014 | ctrl:ISO27002_5_29 | compl:NIS2_Art21_c | c | representant | hoog |
| T1-015 | ctrl:ISO27002_5_30 | compl:NIS2_Art21_c | c | cluster | hoog |
| T1-016 | ctrl:ISO27002_5_35 | compl:NIS2_Art21_f | f | representant | hoog |
| T1-017 | ctrl:ISO27002_5_36 | compl:NIS2_Art21_f | f | cluster | hoog |
| T1-018 | ctrl:ISO27002_6_01 | compl:NIS2_Art21_i | i | cluster | hoog |
| T1-019 | ctrl:ISO27002_6_02 | compl:NIS2_Art21_i | i | cluster | hoog |
| T1-020 | ctrl:ISO27002_6_03 | compl:NIS2_Art21_g | g | pilot | hoog |
| T1-021 | ctrl:ISO27002_8_05 | compl:NIS2_Art21_j | j | edge-case | hoog (na PK-toets) |
| T1-022 | ctrl:ISO27002_8_13 | compl:NIS2_Art21_c | c | cluster | hoog |
| T1-023 | ctrl:ISO27002_8_24 | compl:NIS2_Art21_h | h | edge-case | hoog (na PK-toets) |
| T1-024 | ctrl:ISO27002_8_25 | compl:NIS2_Art21_e | e | pilot | hoog |
| T1-025 | ctrl:ISO27002_8_26 | compl:NIS2_Art21_e | e | cluster | hoog |
| T1-026 | ctrl:ISO27002_8_27 | compl:NIS2_Art21_e | e | cluster | hoog |
| T1-027 | ctrl:ISO27002_8_28 | compl:NIS2_Art21_e | e | cluster | hoog |
| T1-028 | ctrl:ISO27002_8_29 | compl:NIS2_Art21_e | e | cluster | hoog |

Alle 28 → `skos:broadMatch`. Geen verwijderingen, geen behoud-exactMatch.

---

## §4. Methode-protocol v1.0 — herbruikbaar voor T2/T3

`docs/skos-beoordelings-protocol-v1_0.md` is na T1 **gevalideerd in productie** voor 28 paren met scope ctrl:↔compl:. Voor T2/T3-toepassing op andere mapping-clusters gelden onderstaande aandachtspunten en aanbevelingen voor protocol-evolutie.

### 4.1 Wat werkte ongewijzigd

| Onderdeel | Validatie |
|---|---|
| Vier-criteria-set (C1-C4) | leverde eenduidige beslissingen op alle 28 paren |
| C2-buiten-set-check (121-set) | doorslaggevend voor 4 van 4 1↔1-binnen-28-paren |
| Cluster-discipline (§3 slot) | voorkwam half-half cluster-behandelingen |
| Evidence-hiërarchie | niveau 1 haalbaar via CBW-Excel; niveau 2/3 vrijwel niet realistisch voor cross-norm |
| Twijfelgevallen-procedure | werkte voor 2 edge-cases (T1-021 + T1-023) |

### 4.2 Wat aanpassing behoeft voor T2/T3 (overweging voor protocol v1.1)

| Aandachtspunt | Aanbeveling |
|---|---|
| C2-strikte-N-set-interpretatie | Vervangen door **bredere-mapping-cluster-cardinaliteit** als primaire test |
| Pre-pilot-verwachting in protocol-§6 | Niet meer noemen — leidde tot stop-conditie-noise |
| Evidence-niveau 1-verifieer-stap | Standaard `sources/`-doorzoek op cross-walk-Excels als pre-Stap-3-actie |
| ENISA-disclaimer-soort-clauses | **D4-aanvulling-overweging** (zie §8 leerpunt 2) — algemene regel: autoritatieve mapping-bron met expliciete non-equivalence-disclaimer ondersteunt geen `exactMatch` |
| NEN-PK-werkverdeling Tech↔Masterchat | Standaard procedure-stap toevoegen aan protocol |
| Diff-applier | Tech levert standaard werkende Python-applier of unified-diff |

### 4.3 Protocol-versie-roadmap

- **v1.0** (huidig): vastgesteld 26 mei 2026 voor T1
- **v1.1** (overweging): bij T2-start, gebaseerd op T1-leerpunten — vooral §8.4-8.6 aanbevelingen
- **v2.0**: bij scope-uitbreiding naar non-SKOS-relaties (toekomst)

---

## §5. H-items-impact

| H | Status vóór T1 | Status na T1 | Mutatie |
|---|---|---|---|
| H36 | active — geparkeerd | **afgehandeld** | active → closed |
| H37 (open-ontologies MCP) | parked | parked | ongewijzigd |
| H38 (OWL RL vs HermiT) | parked | parked | ongewijzigd |
| H39 (SHACL RUN 2 false-positives) | parked | parked + **versterkt** — Vraag D bevestigde SHACL-blinde vlek op ctrl:↔compl: | trigger-relevantie verhoogd |
| H40 (Dashboard-UI-renderdekking) | parked | parked | ongewijzigd |
| H15, H21, H25-H35 | per H-register | per H-register | ongewijzigd |

**Brein-cyclus-actie (iteratie 13):** H36-bestand status → closed; H39-bestand bijwerken met T1-referentie als bewijs van blinde vlek.

### Kandidaat-nieuw H-item — vooralsnog niet registreren

**H41-kandidaat — SKOS-axioma-set (skos:S46 symmetrie):** owlrl-package laadt geen SKOS-axiomas, dus `skos:exactMatch is owl:SymmetricProperty` wordt niet geïnferreerd. Alle 28 ctrl:→compl: mappings waren asymmetrisch gemodelleerd (0 inverse). Geen impact op T1-patch (predicate-mutatie blijft asymmetrisch). Toekomstig overwegen bij overstap naar SKOS-axioma-incl-reasoning.

Status: T1-werkflow-leerpunt §8, **geen nieuw H-item nu**. Trigger voor herregistratie: overstap-besluit owlrl-incl-SKOS.

---

## §6. D-decisions-impact

| D | Conventie | T1-impact | Conform? |
|---|---|---|---|
| D1 | OWL 2 DL profiel | geen TBox-wijziging | ✓ |
| D2 | Turtle-serialisatie | enige m10-ttl-wijziging | ✓ |
| D3 | 11 namespaces | geen nieuwe namespace | ✓ |
| **D4** | **SKOS cross-framework — closeMatch default, exactMatch zeldzaam** | **Herclassificatie verbetert D4-conformance** — exactMatch was te sterk geclaimd voor 28 paren waar autoritatieve bron (ENISA TIG) equivalence expliciet ontkent | ✓ **verbetering** |
| D5 | ctrl:↔bio: sameAs strikt — 93 paren | onveranderd 93 | ✓ |
| D6 | bilinguale annotaties @nl/@en | geen wijziging in labels | ✓ |
| D7 | BIO 2.0 als twee klassen | geen BIO2-wijziging | ✓ |
| D8 | canonieke SoA — isms:SoA_2026 | onveranderd | ✓ |
| D9 | framework-neutraal | onveranderd | ✓ |
| D10 | COSO ICF/ERM enterprise-laag | onveranderd | ✓ |
| D11 | asset-convergentie — 5 bridges | onveranderd | ✓ |
| D12 | drie-laags compliance | onveranderd | ✓ |

**Alle 12 D-decisions conform. D4-conformance specifiek verbeterd.**

### D4-aanvulling-overweging (voor toekomstig D-register-update — geen T1-scope)

ENISA-disclaimer-categorisch-effect verdient een D4-aanvulling. Voorstel-tekst voor latere overweging:

> **D4-aanvulling (potentieel):** wanneer een autoritatieve mapping-bron expliciet *equivalence* uitsluit (zoals ENISA TIG regel 285), is `skos:exactMatch` **niet** verdedigbaar zelfs bij volledig sluitende C1-C3-toets. Gebruik `skos:broadMatch` of `skos:closeMatch` afhankelijk van scope-relatie.

Dit raakt aan D4 maar wijzigt het niet — D4 zegt momenteel niets over disclaimer-handling. Toevoeging is bewustzijn-verbetering. **Niet nu uitvoeren — masterchat-beslissing op moment van T2 of T3.**

---

## §7. Brain-vault-impact (input voor Brein-cyclus iteratie 13)

Voor `brain__sprints__T1_skos-kwaliteitsanalyse-fase-1.md` (nieuw):

- Sprint-info conform iteratie-12-template (sprint-register-rij + cross-references)
- Datum, scope, uitkomst, leerpunten
- Cross-reference naar protocol-bestand en H-bestanden

Voor `brain__concepts__skos-beoordelings-protocol.md` (nieuw):

- Protocol als concept (i.t.t. operationeel document in `docs/`)
- Cross-references naar D4, H36, T1-sprint
- Methode-criteria + evidence-hiërarchie + cluster-discipline samengevat
- T2/T3-relevantie-vermelding

Voor `brain__concepts__concept-register.md`:

- Nieuwe rij voor SKOS-beoordelings-protocol
- Cross-reference naar protocol-bestand en T1-sprint

Voor `brain__architecture__H36_skos-exactmatch-ctrl-compl-audit.md`:

- Status update: active → closed
- Uitkomst-sectie toevoegen (28 broadMatch, patch v4.6.1)
- Cross-reference naar T1-sprint-bestand

Voor `brain__architecture__H-register.md`:

- H36-rij naar closed-segment (of status-veld bijwerken indien register-format daarin voorziet)

Voor `brain__architecture__H39_*.md`:

- Aanvulling: T1-inventarisatie Vraag D bevestigt SHACL-blinde vlek op ctrl:↔compl: paren. Trigger-relevantie verhoogd.

Voor `brain__log.md`:

- Iteratie 13-entry conform stijl iteratie 12

Voor `brain__index.md`:

- Iteratie-teller 12 → 13
- Vault-staat-tabel-uitbreiding
- v4.6.1-baseline noteren onder "Status-overzicht ontologie"

**Optioneel — productlijn-scheiding van iteratie 12:** Brein-cyclus iteratie 13 kan ook de open productlijn-scheiding-vraag (lokatie `grc-dashboard-v3-2.html`) afronden indien Steven daar besluit op heeft genomen na T1.

---

## §8. Werkflow-leerpunten

Twee bronnen:

1. Tech's 8 leerpunten uit Stap 4-rapport (geverifieerd en hieronder samengebracht)
2. Masterchat-observaties uit sprint-coördinatie + Stap-5 + Stap-6

### Leerpunt 1 — Cluster-representant-aanpak operationeel zeer werkbaar

Cluster-pilot/representant + cluster-discipline-overerving leverde 18 paren in ~30 min (gemiddeld <2 min/paar), vergeleken met ~10 min/paar voor volledige beoordeling. Voor T2/T3 met grotere cluster-aantallen: aanbevolen patroon.

**Aanbeveling:** vasthouden als standaard-aanpak in protocol v1.1.

### Leerpunt 2 — ENISA-disclaimer-categorisch-effect

Centrale paradox van T1: de autoritatieve mapping-bron (ENISA TIG v1.0, gepubliceerd door EU-cybersecurity-agency, juni 2025) erkent **wel** dat ISO27002:2022-controls relevant zijn voor NIS2-clauses, maar **stelt expliciet** dat de mapping geen equivalence-claim is (regel 285: "*The mapping should not be interpreted as a measure of equivalency among different standards or frameworks.*").

Dit betekent dat zelfs perfect-niveau-1-evidence **geen `exactMatch` rechtvaardigt** in SKOS-zin. `broadMatch`/`closeMatch` is de juiste D4-conforme interpretatie.

**Vermoedelijke generaliseerbaarheid:** dit patroon (mapping-bron + non-equivalence-disclaimer) is waarschijnlijk standaard in cross-norm-mapping-documenten. NIST OLIR, ISO Annex F, en andere mapping-publicaties hanteren vergelijkbare disclaimers.

**Aanbeveling:** D4-aanvulling overwegen (zie §6) bij T2-voorbereiding. Niet T1-scope.

### Leerpunt 3 — C2-criterium binnen 121-set i.p.v. 28-set

Protocol v1.0 §2 C2 had "Belangrijke nuance" voor buiten-set-check, maar de pre-pilot-verwachting in §6 baseerde zich op strikte 28-set-cardinaliteit. Dit creëerde stop-conditie-noise op verwachte uitkomsten.

**Aanbeveling protocol v1.1:** primaire C2-toets binnen bredere-mapping-cluster (bv. alle ctrl:↔compl:-mappings, niet alleen exactMatch-subset). Strikte-N-set-interpretatie als secundaire context-vraag.

### Leerpunt 4 — NEN-werkverdeling Tech ↔ Masterchat (nieuw werkflow-patroon)

NEN-restrictieve bronnen (ISO 27002:2022) zijn niet lokaal beschikbaar in Tech-omgeving. Tech kan C1/C3 niet hard maken zonder ISO-tekst-toegang. Werkverdeling die in T1 werkte:

- **Tech (Claude Code):** ABox-extractie, label-vergelijking, 121-set-cardinaliteit, UV-decompositie-context
- **Masterchat (claude.ai):** NEN-tekst-toetsing vanuit project knowledge, bilaterale containment, edge-case-judgement

**Aanbeveling:** dit patroon formaliseren in protocol v1.1 als standaard-stap. Voor twijfelgevallen: Tech formuleert specifieke NEN-PK-vraag in tabel-format; masterchat verzorgt antwoord via PK.

### Leerpunt 5 — Tooling-gap: Tech leverde geen werkbare applier

Tech leverde diff-bestanden als **specificaties** (lijst van paren + sed/python-instructie als comments in bestand), niet als unified-diff-format. `patch -p0` faalde. Masterchat moest werkende Python-applier (`apply_patch_v4_6_1.py`) schrijven.

**Impact:** ~25 min overhead + Steven-frustratie ("denk ik")-moment.

**Aanbeveling:** sprint-protocol-checklist uitbreiden — Tech levert standaard:
- Specificatie (zoals nu in diff-bestanden)
- **PLUS** werkbare applier (Python-script of unified-diff)
- **PLUS** integratie-test (op tijdelijke kopie vóór levering)

Op te nemen in `docs/sprint-protocols.md` bij volgende Brein-cyclus-aanvulling.

### Leerpunt 6 — Pad-inconsistentie in verificatie-scripts

Masterchat-instructie noemde aanvankelijk `scripts/canonical_metrics_v4_6_1.py`, terwijl Tech de scripts in `output/verification/` had gezet. Twee aparte run-pogingen door Steven met file-not-found-fout voor verificatie van patch.

**Impact:** ~5 min verwarring.

**Aanbeveling:** sprint-protocol — Tech vermeldt expliciet de **lokatie van leverbare scripts** in patch-rapport §9 Deliverables-tabel. Masterchat-instructies altijd citeren uit die tabel, niet uit memory.

### Leerpunt 7 — Protocol 14 (pre-push disclosure-check) eerste productie-toepassing

Geïntroduceerd in Brein-cyclus iteratie 12 (na twee voorbarig-push-incidenten in eerdere sessies). T1 was eerste productie-toepassing. Tech rapporteerde:

- Vier checks per rapport (organisatie-naam, persoonsnamen, lokale paden, NEN-tekst-quotes)
- ~3 min per rapport van pilot/Stap-4-omvang
- Geen vondsten in alle T1-rapporten

**Aanbeveling:** automatisering-overweging — `scripts/protocol14_lint.py` met grep-patronen voor de vier check-categorieën. **Niet T1-scope; toekomstig overwegen** zodra ~5 producties tonen dat handmatige check te traag wordt.

### Leerpunt 8 — Twee-zijdige edge-case-analyse-format effectief

Tech-prompt §4 vroeg om twee-zijdige analyse (pro-broadMatch én pro-exactMatch-behoud) zonder Tech-voorstel. Tech leverde dit correct. Masterchat kon op basis van twee-zijdige analyse + NEN-PK-toets snel beslissen.

**Aanbeveling:** vasthouden als standaard voor edge-cases in protocol v1.1.

### Leerpunt 9 — SHACL-blinde vlek bevestigd op H36-cluster

Pre-sprint-inventarisatie Vraag D: geen SHACL-shape valideert op de 28 ctrl:↔compl:-paren. Predicate-mutatie raakte daarom geen shape (SHACL RUN 1/RUN 2 identiek aan baseline). Bevestigt H39-trigger-relevantie.

**Aanbeveling:** brain-vault `brain__architecture__H39_*.md` bijwerken met T1-bevestiging.

### Leerpunt 10 — Sprint-duur ~5 uur totaal (incl. tooling-incident)

| Stap | Geraamd | Werkelijk |
|---|---:|---:|
| Stap 1 inventarisatie | 15 min | 15 min |
| Stap 2 protocol-draft + sign-off | 30 min | ~30 min |
| Stap 3 pilot | 75 min | ~75 min |
| Stap 4 resterende 23 + patch-voorbereiding | 75-90 min | ~2 uur (incl. tooling-installatie) |
| Stap 5 NEN-PK-toets + scenario-keuze | n.v.t. | ~20 min |
| Stap 6 patch-toepassing | n.v.t. | ~25 min (incl. applier-incident) |
| **Totaal** | **~3-4 uur** | **~5 uur** |

**Aanbeveling T2/T3-planning:** **~5-6 uur** als realistische sprint-duur voor analoge scope (~30 paren). Verdeel over 1-2 dagen voor pauze-momenten.

---

## §9. Aanbevelingen voor T2 / T3

### 9.1 T2-scope-kandidaten

Drie kandidaten voor volgende SKOS-kwaliteitsanalyse-sprint:

| Cluster | Omvang | Karakteristiek | Aanbevolen volgorde |
|---|---:|---|---|
| **A — Overige ctrl:↔compl: mappings** (close + related + broad) | ~93 paren | Zelfde modules, andere predicate-types — T1-protocol direct toepasbaar | **T2 — eerste keuze** |
| B — Cross-bron-overlap-105-paren (uit v4.5.0) | ~105 paren | Andere bron-context, kwaliteits-indicator | T3 of later |
| C — m17-COSO/COBIT-mappings | onbekend | Andere namespaces, andere bron-context | Later |

Aanbevolen T2: optie A. Reden — protocol v1.0 is voor ctrl:↔compl:-context bewezen; T2 valideert protocol-toepassing op andere predicate-types.

### 9.2 Protocol v1.1-voorbereiding bij T2-start

- C2-toets binnen bredere mapping-cluster, niet alleen exactMatch-subset
- ENISA-disclaimer-soort-handling als expliciete D4-overweging
- NEN-PK-werkverdeling-procedure expliciet
- Tech levert werkende applier (niet alleen specificatie)
- Lokatie verificatie-scripts duidelijk in patch-rapport

### 9.3 Pre-T2-werkflow-aanvullingen

- Sprint-protocollen-uitbreiding (`docs/sprint-protocols.md`): "Tech levert werkbare applier voor patch-wijzigingen" + "Patch-rapport §9 deliverables-tabel inclusief script-lokaties"
- Brein-cyclus iteratie 13: zie §7

### 9.4 D4-aanvulling-overweging

Op moment van T2-start opnieuw bekijken — niet T1-scope. Mogelijk D4 verfijnen met disclaimer-handling-richtlijn (zie §6).

---

## §10. Conclusie

T1-sprint heeft drie doelen volledig bereikt:

1. **Inhoudelijk:** H36-cluster afgehandeld via 28 SKOS-herclassificaties exactMatch → broadMatch. Alle predicate-mutaties cluster-consistent met hoog vertrouwen en evidence-niveau 1. D4-conformance verbetering bevestigd.

2. **Methodisch:** SKOS-beoordelings-protocol v1.0 vastgesteld en in productie gevalideerd voor 28 paren. Concrete aanbevelingen voor v1.1-evolutie geïdentificeerd voor T2/T3.

3. **Werkflow-validatie:** vijf overhandigings-momenten Masterchat↔Tech (incl. Brein-cyclus afsluiting iteratie 12 als voorbereiding) volledig uitgevoerd. Eerste productie-toepassing Protocol 14 (pre-push disclosure-check) succesvol. NEN-PK-werkverdeling Tech↔Masterchat als nieuw werkflow-patroon vastgesteld.

**Productie-fase is hiermee daadwerkelijk gestart.** Migratie + polish + Brein-cyclus 12 + T1 zijn alle voltooid. Volgende fase: Brein-cyclus iteratie 13 (administratieve verwerking T1), gevolgd door T2-scoping in verse masterchat-sessie.

**Patch v4.6.1 is autoritatief** voor brain-vault-baseline-tabel-update.

---

## §11. Verwijzingen

| Document | Pad |
|---|---|
| Pre-sprint-inventarisatie | `output/reports/t1-presprint-inventarisatie-v4_6_0.md` |
| Methode-protocol v1.0 | `docs/skos-beoordelings-protocol-v1_0.md` |
| Pilot-rapport Stap 3 | `output/reports/t1-pilot-rapport-stap3-v4_6_0.md` |
| Stap 4-rapport | `output/reports/t1-stap4-rapport-v4_6_0.md` |
| Patch-rapport v4.6.1 | `output/reports/patch-rapport-v4_6_1.md` |
| TTL-diff zekere 26 | `output/patches/diff-26-broadMatch.ttl` |
| TTL-diff edge-cases 2 | `output/patches/diff-2-edge-cases.ttl` |
| Patch-applier | `apply_patch_v4_6_1.py` (repo-root) |
| Canonical metrics-script | `output/verification/canonical_metrics_v4_6_1.py` |
| Canonical metrics-output | `output/verification/canonical_metrics_v4_6_1.json` |
| SHACL-validatie-script | `output/verification/shacl_split_validate_v4_6_1.py` |
| SHACL-validatie-output | `output/verification/shacl_results_v4_6_1.json` |
| File-hashes | `output/verification/file_hashes_v4_6_1.txt` |
| Backup originele m10 | `ontology/m10-nis2-ext.ttl.v4_6_0.bak` |
| Dit eindrapport | `output/reports/t1-eindrapport-v4_6_1.md` |

— Einde T1-sprint Eindrapport.
