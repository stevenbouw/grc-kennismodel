# SKOS-beoordelings-protocol v1.2 (DRAFT)

**Voor:** Tech-subagent in Claude Code — toepassing vanaf T2-sprint
**Auteur:** Masterchat
**Datum:** 27 mei 2026
**Status:** **DRAFT** — vaststelling pending bij T2-scoping-sessie
**Aanleiding:** T2-scope-vaststelling bidirectional (27-05-2026): audit-frame B (zwakker én sterker) + audit-uitbreiding A (18 resterende `exactMatch` geïntegreerd) + T1-28-coverage B (meenemen). v1.1-draft was downgrade-georiënteerd; v1.2 maakt protocol symmetrisch toepasbaar.
**Scope:** SKOS-predicate-keuze-criteria + predicate-doel-tabel + evidence-hiërarchie + twijfelgevallen-procedure + werkverdeling Tech↔Masterchat. Herbruikbaar voor T2 (~111 ctrl:↔compl: paren bidirectional) en T3+.
**Voorgangers:**
- `docs/skos-beoordelings-protocol-v1_1.md` (DRAFT, 27 mei 2026 — downgrade-georiënteerd; nooit operationeel gebruikt)
- `docs/skos-beoordelings-protocol-v1_0.md` (FINAL, 26 mei 2026 — gebruikt in T1)

---

## §0. Aanleiding voor v1.2 — wat verandert t.o.v. v1.1

T2-scoping-sessie (27 mei 2026) leverde drie scope-keuzes op:

1. **Audit-frame B** — bidirectioneel: mutaties zowel sterker (upgrade) als zwakker (downgrade) als richtings-correctie (broad↔narrow)
2. **Audit-uitbreiding A** — 18 resterende `skos:exactMatch`-paren geïntegreerd in T2-scope
3. **T1-28-coverage B** — de 28 T1-paren meenemen onder nieuwe protocol-versie

Hieruit volgt dat v1.1's downgrade-oriëntatie methodisch ontoereikend is voor T2. v1.2 maakt het protocol expliciet symmetrisch.

**Zes wijzigingen t.o.v. v1.1** (gedetailleerd in §13):

1. §1 Doel-formulering: expliciete bidirectional toetsing (vervangt anti-overclaim-framing)
2. §3 Predicate-doel-tabel vervangt failure-respons-tabel — input C1-C4 → doel-predicate; vergelijking met huidige predicate → mutatie-richting expliciet
3. §5 Output-formaat: nieuwe kolom "Mutatie-richting" (upgrade / downgrade / richtings-correctie / behoud / verwijderen / twijfel)
4. §6 Sample-keuze: spreiding over alle vier huidige predicate-types in T2-scope (exact + close + related + broad)
5. §10 Werkflow-leerpunten: "Upgrade-detectie-praktijk" als zevende categorie
6. §11 Sign-off-log: items 1 (T2-cluster-keuze) + 4 (NEN-werkverdeling) verwijderd (al beantwoord)

**Niet-gewijzigd t.o.v. v1.1:**

- §2 C1-C4-criteria + D4.1-vooraf-check (al symmetrisch / correct asymmetrisch)
- §4 Twijfelgevallen-procedure
- §7 Werkverdeling Tech↔Masterchat
- §8 Discipline voor licentie-bronnen
- §9 Diff-applier-discipline
- §12 Wat dit protocol NIET doet

---

## §1. Doel van het protocol

Voor elk SKOS-mapping-paar (subject in framework A, object in framework B) consistent en repliceerbaar **bidirectioneel** beoordelen of de gekozen SKOS-predicate (`exactMatch` / `closeMatch` / `relatedMatch` / `broadMatch` / `narrowMatch`) D4 + D4.1-conform is.

Het protocol toetst predicate-keuze in beide richtingen:

- **Downgrade**: huidige predicate is te sterk geclaimd (bv. `exactMatch` waar `broadMatch` past)
- **Upgrade**: huidige predicate is te zwak geclaimd (bv. `relatedMatch` waar `closeMatch` past)
- **Richtings-correctie**: subset-richting is omgekeerd geclaimd (bv. `broadMatch` waar `narrowMatch` past)
- **Behoud**: huidige predicate is conform doel
- **Verwijderen**: geen verdedigbare mapping (zeldzaam, evidence-niveau 4 + alle criteria falen)

T1-bewijs (26 mei 2026) heeft aangetoond dat onterechte `exactMatch`-claims systeemfouten veroorzaken (SKOS-transitiviteit-onhoudbaarheid). T2-scope verbreedt naar bidirectional: ook onderclaim (te zwak) kan in audit-context relevant zijn voor model-kwaliteit, ook al veroorzaakt onderclaim geen acute inconsistenties.

Voor `exactMatch`-claims geldt extra zware toets via vier-criteria-set + D4.1-vooraf-check (zie §2). Voor andere predicates: lichtere toets via inhoudelijke check tegen predicate-doel-tabel (§3).

---

## §2. D4 + D4.1-criteria — vooraf-check + vier-set

Identiek aan v1.1.

### §2.0 — D4.1-vooraf-check

**Vóór C1-C4 doorlopen voor een doel-predicate `skos:exactMatch`:** controleer of de autoritatieve bron achter de mapping een **non-equivalence-disclaimer** bevat.

**Praktische test:**

- Identificeer de bron-publicatie achter de mapping (ENISA TIG, NIST OLIR, ISO Annex F, CBW-Excel, BZK-publicatie, etc.)
- Lees het bron-document — zoek expliciete disclaimer-clauses (vaak in introductie, methode-sectie, of caveat-paragraaf)
- Bekende disclaimers (uitbreidbaar):
  - **ENISA TIG v1.0**, regel 285: "*The mapping should not be interpreted as a measure of equivalency among different standards or frameworks.*"
  - **NIST OLIR**: niet geverifieerd; te checken bij eerstvolgende NIST-mapping-sprint
  - **ISO Annex F**: niet geverifieerd; te checken bij eerstvolgende ISO-mapping-sprint

**Beslis-regel D4.1:**

- Disclaimer aanwezig → doel-predicate `skos:exactMatch` is **per definitie niet-conform**. Doel-predicate valt automatisch terug naar maximaal `closeMatch` (zwakker indien C1-C3 dat aangeven)
- Disclaimer afwezig of niet gedetecteerd → ga verder met C1-C4 vier-set

**Bidirectional-implicatie:** D4.1 werkt asymmetrisch en correct. Het blokkeert alleen *naar* `exactMatch`. Andere upgrades (bv. `relatedMatch` → `closeMatch` of `broadMatch` → `closeMatch`) zijn niet beperkt door D4.1 — wel door C1-C4-uitkomst.

### §2.1 — C1 Definitionele overlap

A en B hebben identieke scope volgens hun bron-definities.

**Praktische test:**

- Zou A de volledige reikwijdte van B invullen?
- Zou B de volledige reikwijdte van A invullen?
- Beide ja → C1 gehaald (bilateraal)
- Eén ja → C1 partieel (subset-relatie)
- Beide nee → C1 gefaald (geen overlap of alleen thematisch)

**Voor NEN-bronnen (ISO 27002, 27001, 27005, 31000, 22301, 22313):** Tech leest direct uit `/Users/stevenbouwmeester/grc-sources-licensed/` — geen masterchat-PK-toets nodig. Discipline-regels in §8.

### §2.2 — C2 Cardinaliteit (cluster-test)

**Formulering:** geen veel-op-één of één-op-veel binnen de **bredere mapping-cluster**.

**Praktische test:**

- Tel alle SKOS-mappings (alle predicate-types) waarvan subject in *zelfde framework-namespace* als ons subject én object in *zelfde framework-namespace* als ons object
- Voorbeeld bij ctrl:↔compl:: tel alle ctrl:↔compl:-mappings (exact + close + related + broad + narrow), niet alleen één predicate-subset
- Zijn er andere mappings met *zelfde subject* in de bredere cluster? Tel ze.
- Zijn er andere mappings met *zelfde object* in de bredere cluster? Tel ze.
- Beide tellingen ≤1 → C2 gehaald (1↔1 in cluster)
- Veel↔1 → C2 indiceert broadMatch-cluster
- 1↔veel → C2 indiceert narrowMatch-cluster

**T1-bewijs:** binnen-N-set-cardinaliteit kan 1↔1 lijken terwijl bredere-cluster-cardinaliteit veel↔1 toont. Cluster-niveau-telling is autoritatief.

### §2.3 — C3 Inclusie-richting (bilaterale containment)

A ⊆ B EN B ⊆ A volgens definitie-content.

**Praktische test:**

- Is alles wat A vereist ook B-vereiste? (A ⊆ B)
- Is alles wat B vereist ook A-vereiste? (B ⊆ A)
- Beide ja → C3 gehaald (bilateraal)
- A ⊂ B (alleen één richting) → C3 indiceert broadMatch
- B ⊂ A (alleen andere richting) → C3 indiceert narrowMatch
- Geen subset-relatie → C3 gefaald (partiële overlap zonder containment)

**Voor NEN-bronnen:** Tech leest direct uit lokale bron-toegang. Bij ambiguïteit waar lezing meerdere interpretaties toelaat: twijfelgevallen-lijst (zie §4).

### §2.4 — C4 Bron-bewijs

Een autoritatieve bron ondersteunt de gekozen SKOS-predicate.

**Evidence-hiërarchie (sterk → zwak):**

| Niveau | Bron-type |
|---|---|
| 1 | Expliciete mapping in autoritatief mapping-document |
| 2 | Norm-tekst identiek aan beide kanten |
| 3 | Definitie-overlap via rdfs:comment of bron-tekst |
| 4 | Onderwerp-titel-overlap (zwakste) |

**Evidence-niveau-1-pre-stap:**

Vóór C4-toekenning aan individuele paren: doe **standaard `sources/`-doorzoek** op cross-walk-Excels of mapping-documenten die in repo aanwezig zijn voor de betreffende framework-combinatie. Voorbeelden:

- `sources/adr-norea/Cbw_NIS2_Control_Framework.xlsx` (ISO 27002 ↔ NIS2 via UV)
- `sources/csf2/CSF_2_0Implementation_Examples.xlsx` (CSF 2.0)
- Toekomstige toegevoegde mapping-documenten

Doel: voorkomen dat per-paar opnieuw wordt gezocht naar bron. Tech-actie max ~10 min vooraf voor de hele sprint-scope.

---

## §3. Predicate-doel-tabel (HERZIEN v1.2)

**v1.2-fundamentele wijziging:** §3 is geen failure-respons-tabel meer, maar een **predicate-doel-tabel**. De tabel produceert per paar een doel-predicate op basis van C1-C4 + D4.1-uitkomsten, onafhankelijk van het huidige predicate. Daarna vergelijkt Tech doel met huidige predicate om de mutatie-richting te bepalen.

### §3.1 — Predicate-doel-tabel

| Configuratie | C1 | C2 | C3 | D4.1 | Evidence | Doel-predicate |
|---|---|---|---|---|---|---|
| **Volledig conform** | bilateraal | 1↔1 in cluster | bilateraal (A=B) | afwezig | 1-2 | `exactMatch` |
| **Conform onder disclaimer** | bilateraal | 1↔1 in cluster | bilateraal (A=B) | aanwezig | 1-2 | `closeMatch` |
| **Partiële overlap, geen subset** | partieel | 1↔1 in cluster | ✗ (geen containment) | n.v.t. | 1-3 | `closeMatch` |
| **A ⊂ B** | A partieel binnen B | A enger geclaimd OK | A ⊆ B (geen B ⊆ A) | n.v.t. | 1-3 | `broadMatch` (A → B) |
| **B ⊂ A** | B partieel binnen A | A breder geclaimd OK | B ⊆ A (geen A ⊆ B) | n.v.t. | 1-3 | `narrowMatch` (A → B) |
| **Veel A's → 1 B (cluster)** | A's afzonderlijk enger | veel↔1 in cluster | A_i ⊆ B per cluster-lid | n.v.t. | 1-3 | `broadMatch` (per A_i) |
| **1 A → veel B's (cluster)** | A breder dan B_i | 1↔veel in cluster | B_i ⊆ A per cluster-lid | n.v.t. | 1-3 | `narrowMatch` (per B_i) |
| **Thematische verwantschap** | zwakke overlap | n.v.t. | n.v.t. | n.v.t. | 1-3 | `relatedMatch` |
| **Onvoldoende bewijs** | onbekend | onbekend | onbekend | n.v.t. | 4 | twijfel → §4 |
| **Geen verdedigbare relatie** | ✗ | ✗ | ✗ | n.v.t. | 4 | verwijderen (zeldzaam) |

**Toelichting tabel:**

- C2 "1↔1 in cluster" is voorwaarde voor zowel `exactMatch` (rij 1) als `closeMatch` (rij 2-3). Bij veel↔1 of 1↔veel binnen het bredere cluster valt de claim hoe dan ook naar `broadMatch`/`narrowMatch`-cluster.
- "n.v.t." in C2/C3-kolom betekent: niet relevant voor predicate-keuze gegeven de andere criteria-uitkomsten.
- D4.1 wordt alleen geconsulteerd voor doel-predicate `exactMatch` (rij 1). Voor andere doel-predicates is D4.1 irrelevant; disclaimer-bron mag andere predicates wel ondersteunen.
- Evidence-niveau 4 (alleen titel-overlap) zonder andere C-criterium-bewijs → twijfel. Niet automatisch `relatedMatch`; lage evidence vereist masterchat-judgement.

### §3.2 — Predicate-sterkte-ordening (voor mutatie-richting-bepaling)

Voor het onderscheid upgrade vs downgrade hanteert dit protocol een interne sterkte-ordening van SKOS-predicates:

```
sterkste   exactMatch
           closeMatch
           broadMatch  ≈  narrowMatch    (parallel, niet onderling vergelijkbaar)
zwakste    relatedMatch
```

**Mutatie-richting-classificatie:**

| Huidige → Doel | Richting |
|---|---|
| `exactMatch` → `closeMatch` of zwakker | **downgrade** |
| `closeMatch` → `broadMatch`/`narrowMatch`/`relatedMatch` | **downgrade** |
| `broadMatch`/`narrowMatch` → `relatedMatch` | **downgrade** |
| Zwakker → sterker (omgekeerd) | **upgrade** |
| `broadMatch` ↔ `narrowMatch` | **richtings-correctie** |
| Doel = huidige | **behoud** |
| Doel = "verwijderen" | **verwijderen** |
| Doel = "twijfel" | **twijfel → §4** |

**`broadMatch` ↔ `narrowMatch`** zijn niet onderling vergelijkbaar in sterkte — beide drukken een specifieke asymmetrische subset-relatie uit. Wisseling tussen deze twee is een **richtings-correctie** van de geclaimde subset-richting, geen sterkte-mutatie.

### §3.3 — Cluster-discipline (verplicht)

Bij C2-failure (cardinaliteit veel↔1 of 1↔veel) is herclassificatie **systematisch binnen het cluster**. Alle paren in dezelfde cluster krijgen dezelfde doel-predicate-toewijzing tenzij voor een specifiek paar een individuele uitzondering aantoonbaar is.

**Bewijslast voor cluster-uitzondering:** Tech motiveert expliciet vanuit NEN-tekst of evidence-niveau-1-bron; bij twijfel naar twijfelgevallen.

Cluster-discipline geldt symmetrisch — ook bij upgrade-kandidaten. Als cluster-representant `relatedMatch` doel-predicate `closeMatch` krijgt, dan alle cluster-leden tenzij individuele uitzondering aantoonbaar.

---

## §4. Twijfelgevallen-procedure

Identiek aan v1.1.

**Tech-autonomie omhoog door lokale NEN-toegang.** Masterchat-escalatie alleen bij:

| Conditie | Reden voor escalatie |
|---|---|
| Cross-bron-interpretatie nodig | Meerdere bronnen tegenspreken elkaar |
| Bron-tekst is meerduidig | NEN-tekst zelf ambigu, geen eenduidige lezing |
| C1-C3-toets blijft sluitend ambigu | Zelfs na NEN-tekst-lezing geen helder oordeel |
| Cluster-uitzondering vereist masterchat-judgement | Bewijslast voor individuele uitzondering binnen cluster te zwak |

**Twee-zijdige analyse-format (verplicht voor escalatie):**

Bij masterchat-escalatie levert Tech **expliciet beide kanten** van de mogelijke beoordeling:

```
T2-XXX — masterchat-judgement-vraag:

Pro-[predicate A]-onderbouwing:
- [argument 1]
- [argument 2]
- [evidence-verwijzing]

Pro-[predicate B]-onderbouwing:
- [argument 1]
- [argument 2]
- [evidence-verwijzing]

Tech-positie: [voorkeur of "geen voorkeur"]
Vraag aan masterchat: [specifieke vraag, niet algemeen]
```

Voorkomt dat masterchat moet reverse-engineeren wat Tech al heeft overwogen.

---

## §5. Output-formaat per paar (HERZIEN v1.2)

Per paar levert Tech:

| Veld | Inhoud |
|---|---|
| Paar-ID | T2-001 t/m T2-NNN |
| Subject IRI | volledige IRI |
| Object IRI | volledige IRI |
| **Huidige predicate** | `exactMatch` / `closeMatch` / `broadMatch` / `narrowMatch` / `relatedMatch` |
| Cluster-context | bv. "ctrl:↔compl: NIS2_b (4↔1 in cluster)" |
| **D4.1-disclaimer-check** | aanwezig / afwezig / niet-onderzocht + bron-verwijzing |
| C1 (definitioneel) | bilateraal / partieel / gefaald + 1-2 zin reden |
| C2 (cardinaliteit cluster) | 1↔1 / veel↔1 / 1↔veel + cluster-grootte |
| C3 (inclusie) | bilateraal / A⊂B / B⊂A / geen + richting indien failure |
| C4 (bron-evidence) | niveau 1-4 + bron-verwijzing |
| **Doel-predicate** | uit §3.1 predicate-doel-tabel |
| **Mutatie-richting** | upgrade / downgrade / richtings-correctie / behoud / verwijderen / twijfel-escaleer |
| Confidence | hoog / middel / laag |
| Patch-vereist | ja / nee (nee bij "behoud") |

**Verschil t.o.v. v1.1:**

- Nieuwe kolom "Huidige predicate" expliciet (was impliciet)
- Nieuwe kolom "Doel-predicate" (resultaat §3.1-tabel)
- Nieuwe kolom "Mutatie-richting" vervangt v1.1's impliciete "herclass-[predicate]" formulering

---

## §6. Sample-keuze voor pilot (HERZIEN v1.2)

**Sample-grootte:** 5 paren standaard (T1-precedent). Voor T2 met ~111 paren over 4 predicate-types: **7-10 paren aanbevolen** voor adequate dekking.

**Spreiding-richtlijnen (v1.2 bidirectional):**

| Richtlijn | Reden |
|---|---|
| Verdeling over predicate-types | Pilot dekt alle vier huidige predicate-types in T2-scope (`exactMatch`, `closeMatch`, `broadMatch`, `relatedMatch`); narrowMatch ontbreekt in ctrl:↔compl: |
| Mix van upgrade- en downgrade-verwachting | Pilot is empirisch; geen pre-pilot-uitkomst-verwachting, wel spreiding over predicate-types waar zowel upgrade als downgrade waarschijnlijk is |
| Spreiding over cluster-typen | Cluster-representanten uit ≥3 verschillende clusters |
| Spreiding over evidence-niveau-1-bronnen | Niet alleen ENISA-TIG-gedreven paren; ook UV-gedreven en CBW-Excel-direct |
| Mix van module-combinaties | Alleen één module in T2-scope (m10-nis2-ext), maar bij latere sprints over modules heen |

**Stop-condities pilot (ongewijzigd t.o.v. v1.1):**

| # | Conditie | Wat te doen |
|---|---|---|
| 1 | Confidence "laag" op ≥3 van pilot-set | Pauze; protocol-criteria-bijstelling nodig |
| 2 | Evidence-niveau 4 op ≥3 van pilot-set | Pauze; bron-discipline-probleem |
| 3 | D4.1-disclaimer-status "niet-onderzocht" op ≥3 van pilot-set | Pauze; evidence-niveau-1-pre-stap onvoldoende uitgevoerd |
| 4 | Onverwacht-patroon — uitkomst sterk wijkt af van wat masterchat-scope-bepaling impliceerde | Pauze; masterchat-input nodig |

**Geen pre-pilot-uitkomst-verwachting** — empirische onafhankelijkheid van Tech-uitkomst is gewaarborgd. Pilot detecteert mismatch tussen scope-aanname en empirische uitkomst alleen via stop-conditie 4 (kwalitatief), niet via numerieke verwachting.

---

## §7. Werkverdeling Tech ↔ Masterchat

Identiek aan v1.1.

### §7.1 — Tech-autonomie

Tech voert volledig autonoom uit:

- Pre-sprint-inventarisatie + tabelopbouw
- D4.1-disclaimer-detectie via lokale bron-toegang
- ABox-extractie + cardinaliteit-tellingen + buiten-set-checks
- Evidence-niveau-1-pre-stap (`sources/`-doorzoek)
- C1-C3-toetsing via lokale NEN-bron-toegang in `/Users/stevenbouwmeester/grc-sources-licensed/`
- Cluster-representant-beoordeling + cluster-discipline-overerving
- Patch-voorbereiding (TTL-diffs, canonical metrics, SHACL, hashes, patch-rapport)
- Pre-push disclosure-check Protocol 14 (zie §8)

### §7.2 — Masterchat-judgement-rol

Masterchat acteert alleen op:

- Sprint-scope-bepaling vooraf
- Protocol-versie-vaststelling (bv. v1.1 → v1.2)
- Twijfelgevallen-escalatie conform §4
- Scope-pauze-rapport (Optie A/B/C)
- Strategische beslissingen die D-decisions of architectuur raken
- Eind-sign-off vóór commit + push

### §7.3 — Steven's rol

- Tussenmens Tech-Claude-Code ↔ masterchat-claude.ai
- Inspectie + handmatige commit + push (subagents committen niet zelfstandig)
- Acceptatie of bijsturing op scope-pauze-rapporten
- Finale autorisatie

---

## §8. Discipline voor licentie-bronnen

Identiek aan v1.1.

### §8.1 — NEN-bron-toegang voor Tech

Tech heeft toegang tot lokale NEN-bronnen in `/Users/stevenbouwmeester/grc-sources-licensed/`:

- ISO 27002:2022
- ISO 27001:2022
- ISO 27005:2024
- ISO 31000:2018
- ISO 22301:2019
- ISO 22313:2020

Toegang is binnen Steven's persoonlijke NEN-licentie en mag voor zijn eigen werk worden gebruikt.

### §8.2 — Parafrase-discipline (verplicht)

Tech mag NEN-tekst lezen voor toetsing, maar **mag onder geen beding NEN-tekst-fragmenten verbatim opnemen** in:

- Rapport-output (alle markdown-bestanden)
- Commit-messages
- Turtle-files (ontologie-modules, SHACL, demo-SPARQL)
- Canonical metrics-output of SHACL-resultaten
- Code-comments
- Eventuele andere geautomatiseerde output

**Wel toegestaan:**

- Parafrase + clausule-verwijzing ("ISO 27002:2022 §8.24 dekt beleid + procedures + sleutelbeheer + gebruik")
- Conceptuele samenvattingen in eigen woorden
- Verwijzingen naar bestandnaam + clausule-nummer

**Niet toegestaan:**

- Letterlijke citaten van controle-tekst
- Letterlijke citaten van guidance-tekst
- Letterlijke citaten van Annex-tekst
- Reproductie van figuren of tabellen

### §8.3 — Pre-push disclosure-check (Protocol 14-uitbreiding)

Protocol 14 omvat vijf check-categorieën:

1. Organisatie-naam
2. Persoonsnamen (m.u.v. Steven, conform)
3. Lokale paden buiten `/Users/stevenbouwmeester/grc-kennismodel/`
4. Credentials, TLD's, e-mail-domeinen
5. NEN-tekst-fragmenten (verbatim ISO-tekst >10 woorden)

Tech doet de check vóór hand-off aan Steven. Steven verifieert bij `git diff`-inspectie.

---

## §9. Diff-applier-discipline

Identiek aan v1.1.

T1-leerpunt 5: Tech leverde diff-bestanden als **specificatie** ("vervang X door Y voor deze 28 paren") in plaats van als werkbare applier. `patch -p0` faalde. Masterchat moest Python-applier schrijven.

**Verplichting:**

Bij sprints met ontologie-patches levert Tech standaard zowel:

1. **Specificatie** (TTL-diff-bestand of equivalente lijst van te wijzigen triples)
2. **Werkbare applier** — één van drie formaten:
   - Python-script (geprefereerd; volgt T1-`apply_patch_v4_6_1.py`-patroon met backup + count-verificatie + faal-veilig-exit)
   - Unified-diff-format (`patch -p0`-compatibel)
   - Sed-script met expliciete gerichte patterns

3. **Integratie-test** vóór levering — Tech runt de applier op een tijdelijke gepatchte kopie en verifieert dat:
   - Aantal mutaties matcht specificatie
   - Geen onbedoelde nevenwijzigingen
   - File-hash van resultaat matcht canonical metrics-script-verwachting

**Geen specificatie-only-deliverables**.

**Bidirectional-relevant detail:** de applier moet zowel upgrade-mutaties (`relatedMatch` → `closeMatch`, etc.) als downgrade-mutaties (`exactMatch` → `broadMatch`, etc.) als richtings-correcties (`broadMatch` → `narrowMatch`) ondersteunen. Eén applier voor alle drie types; geen aparte upgrade/downgrade-scripts.

---

## §10. Werkflow-leerpunten-markering tijdens sprint (UITGEBREID v1.2)

Tijdens uitvoering noteert Tech leerpunten voor de §10 van het eind-sprint-rapport. Categorieën om op te letten:

1. Tooling-gaten (welke automation ontbrak?)
2. Bron-toegankelijkheid (welke documenten waren niet vindbaar?)
3. Protocol-criteria-onduidelijkheden (welke C-criterium-formulering bleek ambigu?)
4. Werkverdeling-momenten waar Tech-autonomie of escalatie aan masterchat-discussie waard zijn
5. Cluster-discipline-toepassings-ervaringen
6. D4.1-pre-stap-praktijk (hoe lang duurt disclaimer-detectie per bron?)
7. **Upgrade-detectie-praktijk** (NIEUW v1.2) — hoe vaak bleek upgrade-doel-predicate aanwezig? Was de predicate-doel-tabel symmetrisch toepasbaar of bleek downgrade-bias toch in de praktijk? Welke evidence-bronnen ondersteunen upgrade-claims?

Markeren voortdurend, niet alleen achteraf. Voorkomt vergeten.

---

## §11. Sign-off-log

Vaststelling pending bij T2-scoping-sessie.

**Reeds beantwoord bij T2-scoping (27-05-2026):**

- T2-cluster-keuze → ctrl:↔compl: in `m10-nis2-ext.ttl`, bidirectional, ~111 paren (T1-28 + 18 resterende exactMatch + ~65 oude close/related/broad)
- NEN-werkverdeling-precieze-grenzen → Tech-autonomie via Protocol 17 herzien

**Pending bij T2-scoping:**

| # | Beslis-punt | Vastgesteld bij |
|---|---|---|
| 1 | Sample-grootte (7-10 i.p.v. T1's 5; voorkeur masterchat 8) | T2-scoping |
| 2 | D4.1-pre-stap-tijdsraming (ENISA TIG al bevestigd; overige bronnen optioneel) | T2-scoping |
| 3 | Sign-off Steven op v1.2 als operationeel protocol | T2-scoping |

---

## §12. Wat dit protocol NIET doet

- Beoordeelt geen individuele paren — dat is Tech-werk per sprint
- Bepaalt geen ontologie-patch — dat volgt uit beoordeling
- Wijzigt geen D-decisions — D4 + D4.1 zijn autoritatief; dit protocol opereert binnen D4 + D4.1
- Adresseert geen wijziging in andere SKOS-vocabulaire-keuzes (bv. SKOS-axioma-set-handling; H41-kandidaat)
- Vervangt v1.0 of v1.1 niet — beide blijven beschikbaar voor historische referentie (v1.0 voor T1-historie; v1.1 nooit operationeel gebruikt)

---

## §13. Wijzigingen — overzicht

### §13.1 — Wijzigingen v1.2 t.o.v. v1.1

| # | Wijziging | Bron |
|---|---|---|
| 1 | §1 Doel-formulering: expliciete bidirectional toetsing (vervangt anti-overclaim-framing) | T2-scope-vaststelling 27-05-2026 (frame B) |
| 2 | §3 Predicate-doel-tabel vervangt failure-respons-tabel | T2-scope-vaststelling 27-05-2026 + masterchat v1.1-review (drie operationele gaten) |
| 3 | §3.2 Predicate-sterkte-ordening + mutatie-richting-classificatie expliciet | T2-scope-vaststelling 27-05-2026 |
| 4 | §3.3 Cluster-discipline expliciet symmetrisch geformuleerd | T2-scope-vaststelling 27-05-2026 |
| 5 | §5 Output-formaat: nieuwe kolommen "Huidige predicate", "Doel-predicate", "Mutatie-richting" | T2-scope-vaststelling 27-05-2026 |
| 6 | §6 Sample-keuze: spreiding over predicate-types + mix upgrade/downgrade-kandidaten | T2-scope-vaststelling 27-05-2026 |
| 7 | §9 Bidirectional-applier-vereiste expliciet | T2-scope-vaststelling 27-05-2026 |
| 8 | §10 "Upgrade-detectie-praktijk" als zevende leerpunten-categorie | T2-scope-vaststelling 27-05-2026 |
| 9 | §11 Sign-off-log opgeschoond (items 1 + 4 verwijderd; al beantwoord) | T2-scoping 27-05-2026 |

### §13.2 — Cumulatieve wijzigingen v1.2 t.o.v. v1.0 (via v1.1)

| # | Wijziging | Bron |
|---|---|---|
| 1 | D4.1-vooraf-check als nieuwe stap vóór C1-C4 | D4.1 (27-05-2026) — uit v1.1 |
| 2 | C2-cardinaliteit binnen bredere mapping-cluster | T1 §8 leerpunt 3 — uit v1.1 |
| 3 | Evidence-niveau-1-pre-stap als standaard `sources/`-doorzoek | T1 §4.2 aanbeveling 3 — uit v1.1 |
| 4 | Pre-pilot-verwachting verwijderd uit §6 | T1 §8 leerpunt 2 (alt) — uit v1.1 |
| 5 | Tech-autonomie voor NEN-toetsing via lokale bron-toegang | T1 §8 leerpunt 4 + Steven-koers-correctie 27-05-2026 — uit v1.1 |
| 6 | §7 Werkverdeling Tech↔Masterchat als expliciete sectie | T1 §8 leerpunt 4 — uit v1.1 |
| 7 | §8 Discipline licentie-bronnen — parafrase-regels + Protocol 14-uitbreiding | T1 + Steven-koers-correctie 27-05-2026 — uit v1.1 |
| 8 | §9 Diff-applier-discipline — Tech levert werkbare applier | T1 §8 leerpunt 5 — uit v1.1 |
| 9 | Cluster-discipline expliciet verplicht | T1 §8 leerpunt 9 — uit v1.1 |
| 10 | Twee-zijdige edge-case-analyse-format als verplicht escalatie-format | T1 §8 leerpunt 8 — uit v1.1 |
| 11 | Bidirectional toetsing + predicate-doel-tabel + mutatie-richting | v1.2-delta (zie §13.1) |

---

*Einde protocol-draft v1.2. Bij vaststelling: protocol gaat naar Tech voor T2-uitvoering. Tot dan: v1.0 blijft autoritatief voor historische referentie; v1.1 was tussenstap die nooit operationeel gebruikt is.*
