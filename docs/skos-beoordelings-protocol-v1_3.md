# SKOS-beoordelings-protocol v1.3

**Voor:** Tech-subagent in Claude Code — toepassing vanaf T3-sprint of m14-sprint (afhankelijk van masterchat-scope-besluit)
**Auteur:** Masterchat
**Datum:** 27 mei 2026
**Status:** **FINAL** — vastgesteld door masterchat 28 mei 2026 (T3-scoping)
**Aanleiding:** T2-sprint-leerpunten (pilot-rapport §7.3 + Stap 3-rapport §6 + patch-rapport v4.6.2 §13.3/§13.6) + masterchat-werkflow-leerpunt (patch-rapport §13.2). v1.2 was operationeel autoritatief tijdens T2; v1.3 incorporeert empirische verfijningen.
**Scope:** SKOS-predicate-keuze-criteria + predicate-doel-tabel + evidence-hiërarchie + twijfelgevallen-procedure + werkverdeling Tech↔Masterchat + werkflow-discipline. Herbruikbaar voor T3+, m14-sprint, en latere SKOS-audit-sprints.
**Voorgangers:**
- `docs/skos-beoordelings-protocol-v1_2.md` (27 mei 2026 — T2-sprint operationeel, succesvol gevalideerd op 118 m10-paren over 10 clusters)
- `docs/skos-beoordelings-protocol-v1_1.md` (27 mei 2026 — downgrade-georiënteerd, nooit operationeel)
- `docs/skos-beoordelings-protocol-v1_0.md` (26 mei 2026 — T1-sprint operationeel)

---

## §0. Aanleiding voor v1.3 — wat verandert t.o.v. v1.2

T2-sprint heeft Protocol v1.2 empirisch gevalideerd op 118 m10-paren over 10 NIS2-letter-clusters met 100% cluster-discipline-convergentie en 0 NEN-aantoonbare uitzonderingen. Pilot-rapport + Stap 3-rapport + patch-rapport v4.6.2 leverden samen 7 concrete verfijnings-voorstellen die in v1.3 verwerkt worden.

**Zeven verfijningen t.o.v. v1.2** (gedetailleerd in §13):

1. **§2.1 C1 "partieel"-grens** — operationele test verfijnd met expliciet criterium "enige NEN-content-overlap op operationele niveau" + T2-precedenten
2. **§2.2 C2 + subject-cluster** — object-cluster-cardinaliteit prevaleert bij multi-mapping-paren; subject-cluster-effect bleek niet-bepalend in T2-praktijk
3. **§3.3 Cluster-discipline-bewijslast** — bewijslast-asymmetrie expliciet (uitzondering naar sterker mapping vereist bilaterale containment; T2 leverde 0 succesvolle uitzonderingen op 10 flags)
4. **§5 Confidence-criterium** — hoog/middel/laag-drempels expliciet gedefinieerd
5. **§5.1 Cluster-representant-keuze-criteria** — formeel als sub-sectie (was impliciet in v1.2 §3.3 + §6)
6. **§10 Werkflow-discipline voor rapport-bouw** — nieuwe sub-secties §10.2-§10.5: bottom-up bouw, tabel-consistentie, helper-script-autoritatief, metrics-tabel-scope-annotatie
7. **§11 Sign-off-log** — protocol-versie-historie opgenomen i.p.v. open beslis-punten-lijst

**Niet-gewijzigd t.o.v. v1.2:**

- §2.0 D4.1-vooraf-check (al correct asymmetrisch)
- §2.3 C3 inclusie-richting (al symmetrisch)
- §2.4 C4 bron-bewijs + evidence-niveau-1-pre-stap
- §3.1 predicate-doel-tabel (operationeel sluitend, T2-bewijs 10/10 clusters)
- §3.2 predicate-sterkte-ordening
- §4 Twijfelgevallen-procedure + twee-zijdige analyse-format
- §6 Sample-keuze (al gevalideerd in T2-pilot)
- §7 Werkverdeling Tech↔Masterchat
- §8 Discipline voor licentie-bronnen
- §9 Diff-applier-discipline (Protocol 15)
- §12 Wat dit protocol NIET doet

---

## §1. Doel van het protocol

Voor elk SKOS-mapping-paar (subject in framework A, object in framework B) consistent en repliceerbaar **bidirectioneel** beoordelen of de gekozen SKOS-predicate (`exactMatch` / `closeMatch` / `relatedMatch` / `broadMatch` / `narrowMatch`) D4 + D4.1-conform is.

Het protocol toetst predicate-keuze in beide richtingen:

- **Downgrade**: huidige predicate is te sterk geclaimd
- **Upgrade**: huidige predicate is te zwak geclaimd
- **Richtings-correctie**: subset-richting is omgekeerd geclaimd (broadMatch ↔ narrowMatch)
- **Behoud**: huidige predicate is conform doel
- **Verwijderen**: geen verdedigbare mapping (zeldzaam)

T1-bewijs (26 mei 2026) heeft onterechte `exactMatch`-claims als systeemfout aangetoond. T2-bewijs (27 mei 2026) heeft bidirectional cluster-discipline op productie-schaal gevalideerd: 65 mutaties (32 downgrade + 33 upgrade) zonder NEN-aantoonbare uitzondering op 10 cluster-discipline-flags.

Voor `exactMatch`-claims geldt extra zware toets via vier-criteria-set + D4.1-vooraf-check (zie §2). Voor andere predicates: lichtere toets via inhoudelijke check tegen predicate-doel-tabel (§3).

---

## §2. D4 + D4.1-criteria — vooraf-check + vier-set

### §2.0 — D4.1-vooraf-check (ongewijzigd t.o.v. v1.2)

**Vóór C1-C4 doorlopen voor een doel-predicate `skos:exactMatch`:** controleer of de autoritatieve bron achter de mapping een **non-equivalence-disclaimer** bevat.

**Praktische test:**

- Identificeer de bron-publicatie achter de mapping (ENISA TIG, NIST OLIR, ISO Annex F, CBW-Excel, BZK-publicatie, etc.)
- Lees het bron-document — zoek expliciete disclaimer-clauses (vaak in introductie, methode-sectie, of caveat-paragraaf)
- Bekende disclaimers (uitbreidbaar):
  - **ENISA TIG v1.0**, regel 285: "*The mapping should not be interpreted as a measure of equivalency among different standards or frameworks.*"
  - **CBW-Excel "Mapping Uitvoeringsverordening"**, rij R3: bron-verklaring erft ENISA TIG-disclaimer expliciet
  - **NIST OLIR**: niet geverifieerd; te checken bij eerstvolgende NIST-mapping-sprint
  - **ISO Annex F**: niet geverifieerd; te checken bij eerstvolgende ISO-mapping-sprint

**Beslis-regel D4.1:**

- Disclaimer aanwezig → doel-predicate `skos:exactMatch` is **per definitie niet-conform**. Doel-predicate valt automatisch terug naar maximaal `closeMatch` (zwakker indien C1-C3 dat aangeven)
- Disclaimer afwezig of niet gedetecteerd → ga verder met C1-C4 vier-set

**Bidirectional-implicatie:** D4.1 werkt asymmetrisch en correct. Het blokkeert alleen *naar* `exactMatch`. Andere upgrades (bv. `relatedMatch` → `closeMatch` of `broadMatch` → `closeMatch`) zijn niet beperkt door D4.1 — wel door C1-C4-uitkomst.

**T2-praktijkbevinding:** D4.1-disclaimer-status kan **cluster-niveau** worden toegekend wanneer alle cluster-leden dezelfde bron-stack hebben. T2 m10-cluster had één D4.1-context (ENISA TIG R285 + CBW-Mapping-UV R3-erf) — één bevestiging per cluster volstond, niet per-paar-werk. Heterogene clusters (mix van bronnen) vereisen per-paar-toets.

### §2.1 — C1 Definitionele overlap (HERZIEN v1.3)

A en B hebben identieke scope volgens hun bron-definities.

**Praktische test:**

- Zou A de volledige reikwijdte van B invullen?
- Zou B de volledige reikwijdte van A invullen?

**Drie-uitkomst-classificatie** (verfijnd v1.3):

| Uitkomst | Definitie | Operationele test |
|---|---|---|
| **C1 bilateraal** | Beide ja — A en B dekken elkaars volledige scope | Beide bron-definities bevatten alle elementen van de andere; geen scope-elementen "buiten" de andere |
| **C1 partieel** | Eén ja, of: enige NEN-content-overlap op operationele niveau zonder bilateraliteit | Subject-scope ⊂ object-scope (of omgekeerd), OF gedeelde thematische scope met operationele NEN-tekst-aanknopingspunten in beide richtingen |
| **C1 gefaald** | Beide nee — geen scope-overlap of alleen onderwerp-titel-gelijkenis | Geen NEN-tekst-aanknopingspunten op operationele niveau; thema-titels alleen oppervlakkig gelijkend |

**Verduidelijking "partieel"-grens** (T2-leerpunt §6.3): partiële overlap vereist tenminste één van:

1. **Subset-relatie** (A ⊂ B of B ⊂ A) — engere control past binnen bredere norm
2. **Operationeel NEN-content-overlap** — beide bronnen verwijzen naar overlappend implementatie-domein, ook zonder strikte subset
3. **Cross-bron-verwijzing** — A's "Other information"-clausule of B's guidance verwijst expliciet naar de andere

Voorbeelden uit T2:

- ISO §5.5 (Contact with authorities) ↔ NIS2(a) policy-norm: partieel — authority-contact is operationele ondersteuning binnen policy-implementatie; ISO §5.5 "Other information" verwijst naar incident- en continuity-clausules
- ISO §5.30 (ICT-readiness business continuity) ↔ NIS2(c) BC+backup+DR: partieel-sterk — ICT-readiness is engere ICT-laag binnen bredere BC-norm; "Other information" verwijst naar ISO 27031 + ISO 22301/22313
- ISO §8.3 (Access restriction) ↔ NIS2(h) cryptografie: partieel — access-restriction kan via crypto worden geïmplementeerd; zelf-thema is operationeel verschillend

**Voor NEN-bronnen** (ISO 27002, 27001, 27005, 31000, 22301, 22313): Tech leest direct uit `/Users/stevenbouwmeester/grc-sources-licensed/` — geen masterchat-PK-toets nodig. Discipline-regels in §8.

### §2.2 — C2 Cardinaliteit cluster-test (HERZIEN v1.3)

**Formulering ongewijzigd:** geen veel-op-één of één-op-veel binnen de **bredere mapping-cluster**.

**Praktische test:**

- Tel alle SKOS-mappings (alle predicate-types) waarvan subject in *zelfde framework-namespace* als ons subject én object in *zelfde framework-namespace* als ons object
- Bredere-cluster-cardinaliteit:
  - Object-zijde-cluster: aantal subjects dat naar het object mapt
  - Subject-zijde-cluster: aantal objects waarnaar het subject mapt
- Beide tellingen ≤1 → C2 gehaald (1↔1 in cluster)
- Veel↔1 → C2 indiceert broadMatch-cluster
- 1↔veel → C2 indiceert narrowMatch-cluster

**Subject-cluster vs. object-cluster — prevalence-regel** (NIEUW v1.3, T2-leerpunt §6.3):

Wanneer een paar in *beide* een object-cluster en een subject-cluster zit (multi-mapping), prevaleert **object-cluster-cardinaliteit** voor C2-toets en cluster-doel-predicate-bepaling.

**Onderbouwing:** Protocol toetst (s,o)-paar-niveau predicate-keuze. De cluster-discipline (§3.3) opereert op de mapping-eindpunt-relatie: het object is wat door meerdere subjects gemapt wordt; subject-cluster betekent dat het subject naar meerdere objects mapt (een andere relatie). Object-cluster is de operationele scope voor cluster-doel-predicate-bepaling.

**T2-praktijkvoorbeelden** (multi-mapping-leden):

- `ctrl:ISO27002_5_04` mapt naar NIS2_a + NIS2_f + NIS2_g (subject-cluster 3) — in alle drie clusters cluster-doel `broadMatch` per object-cluster-cardinaliteit (12/7/9-1)
- `ctrl:ISO27002_8_03` mapt naar NIS2_h + NIS2_i + NIS2_j (subject-cluster 3) — in alle drie clusters cluster-doel `broadMatch` per object-cluster-cardinaliteit (7/32/9-1)

In beide gevallen 0 NEN-uitzondering ondanks subject-cluster ≥3. Subject-cluster-effect is informatief (uitzondering-screening-flag) maar niet beslissend.

### §2.3 — C3 Inclusie-richting (ongewijzigd t.o.v. v1.2)

A ⊆ B EN B ⊆ A volgens definitie-content.

**Praktische test:**

- Is alles wat A vereist ook B-vereiste? (A ⊆ B)
- Is alles wat B vereist ook A-vereiste? (B ⊆ A)
- Beide ja → C3 gehaald (bilateraal)
- A ⊂ B (alleen één richting) → C3 indiceert broadMatch
- B ⊂ A (alleen andere richting) → C3 indiceert narrowMatch
- Geen subset-relatie → C3 gefaald (partiële overlap zonder containment)

**Voor NEN-bronnen:** Tech leest direct uit lokale bron-toegang. Bij ambiguïteit waar lezing meerdere interpretaties toelaat: twijfelgevallen-lijst (zie §4).

### §2.4 — C4 Bron-bewijs (ongewijzigd t.o.v. v1.2)

Een autoritatieve bron ondersteunt de gekozen SKOS-predicate.

**Evidence-hiërarchie (sterk → zwak):**

| Niveau | Bron-type |
|---|---|
| 1 | Expliciete mapping in autoritatief mapping-document |
| 2 | Norm-tekst identiek aan beide kanten |
| 3 | Definitie-overlap via rdfs:comment of bron-tekst |
| 4 | Onderwerp-titel-overlap (zwakste) |

**Evidence-niveau-1-pre-stap** (standaard `sources/`-doorzoek):

Vóór C4-toekenning aan individuele paren: doe standaard doorzoek op cross-walk-Excels of mapping-documenten in repo aanwezig voor de betreffende framework-combinatie. Voorbeelden:

- `sources/adr-norea/Cbw (NIS2) Control Framework.xlsx` (ISO 27002 ↔ NIS2 via UV)
- `sources/csf2/CSF_2_0Implementation_Examples.xlsx` (CSF 2.0)
- Toekomstige toegevoegde mapping-documenten

Doel: voorkomen dat per-paar opnieuw wordt gezocht naar bron. Tech-actie max ~10 min vooraf voor de hele sprint-scope.

---

## §3. Predicate-doel-tabel (ongewijzigd t.o.v. v1.2)

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

### §3.2 — Predicate-sterkte-ordening (ongewijzigd t.o.v. v1.2)

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

### §3.3 — Cluster-discipline (HERZIEN v1.3 — bewijslast-verfijning)

Bij C2-failure (cardinaliteit veel↔1 of 1↔veel) is herclassificatie **systematisch binnen het cluster**. Alle paren in dezelfde cluster krijgen dezelfde doel-predicate-toewijzing tenzij voor een specifiek paar een individuele uitzondering aantoonbaar is.

**Bewijslast-asymmetrie voor cluster-uitzondering** (NIEUW v1.3, T2-leerpunt):

| Uitzondering-richting | Bewijslast |
|---|---|
| **Uitzondering naar sterker mapping** (bv. closeMatch in veel↔1-cluster waar cluster-default broadMatch is) | **Streng** — vereist bilaterale containment-aantoonbaarheid via NEN-tekst (C1 bilateraal + C3 bilateraal). In veel↔1-cluster structureel zeer moeilijk omdat object-cluster-cardinaliteit ≥2 betekent dat object niet bilateraal A=B kan zijn met meerdere A's. |
| **Uitzondering naar zwakker mapping** (bv. relatedMatch in veel↔1-cluster waar cluster-default broadMatch is) | **Streng** — vereist NEN-bewijs dat C3 (subset-relatie A⊂B) faalt; alleen thematische verwantschap. Operationeel zeldzaam want cluster-lidmaatschap impliceert reeds enige subset-relatie. |
| **Behoud cluster-default** | Geen aanvullende bewijslast nodig; cluster-discipline §3.3 prevaleert |

**T2-empirisch bewijs voor strenge bewijslast:** alle 10 heuristiek-screening-flags (op 6 cluster-leden, sommige in meerdere clusters) zijn na ISO 27002:2022-tekstlezing cluster-conform bevonden. Geen enkele bilaterale containment-claim houdbaar in veel↔1-cluster. **Cluster-discipline is operationeel niet-omzeilbaar zonder substantiële NEN-onderbouwing.**

**Cluster-discipline geldt symmetrisch** — ook bij upgrade-kandidaten. Als cluster-representant `relatedMatch` doel-predicate `broadMatch` krijgt, dan alle cluster-leden tenzij individuele uitzondering aantoonbaar.

---

## §4. Twijfelgevallen-procedure (ongewijzigd t.o.v. v1.2)

**Tech-autonomie omhoog door lokale NEN-toegang.** Masterchat-escalatie alleen bij:

| Conditie | Reden voor escalatie |
|---|---|
| Cross-bron-interpretatie nodig | Meerdere bronnen tegenspreken elkaar |
| Bron-tekst is meerduidig | NEN-tekst zelf ambigu, geen eenduidige lezing |
| C1-C3-toets blijft sluitend ambigu | Zelfs na NEN-tekst-lezing geen helder oordeel |
| Cluster-uitzondering vereist masterchat-judgement | Bewijslast voor individuele uitzondering binnen cluster te zwak |

**Twee-zijdige analyse-format (verplicht voor escalatie):**

```
T*-XXX — masterchat-judgement-vraag:

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

## §5. Output-formaat per paar (HERZIEN v1.3 — confidence-criteria + cluster-representant-criteria)

Per paar levert Tech alle 13 velden ingevuld:

| Veld | Inhoud |
|---|---|
| Paar-ID | T*-001 t/m T*-NNN |
| Subject IRI | volledige IRI |
| Object IRI | volledige IRI |
| Huidige predicate | `exactMatch` / `closeMatch` / `broadMatch` / `narrowMatch` / `relatedMatch` |
| Cluster-context | bv. "ctrl:↔compl: NIS2_b (4↔1 in cluster)" |
| D4.1-disclaimer-check | aanwezig / afwezig / niet-onderzocht + bron-verwijzing |
| C1 (definitioneel) | bilateraal / partieel / gefaald + 1-2 zin reden |
| C2 (cardinaliteit cluster) | 1↔1 / veel↔1 / 1↔veel + cluster-grootte (object-cluster + subject-cluster) |
| C3 (inclusie) | bilateraal / A⊂B / B⊂A / geen + richting indien failure |
| C4 (bron-evidence) | niveau 1-4 + bron-verwijzing |
| Doel-predicate | uit §3.1 predicate-doel-tabel + rij-verwijzing |
| Mutatie-richting | upgrade / downgrade / richtings-correctie / behoud / verwijderen / twijfel-escaleer |
| Confidence | hoog / middel / laag (zie §5.2 criteria) |
| Patch-vereist | ja / nee (nee bij "behoud") |

### §5.1 — Cluster-representant-keuze-criteria (NIEUW v1.3 — formeel)

Was impliciet in v1.2 §3.3 + §6.2; v1.3 formaliseert als sub-sectie.

**Bij selectie van cluster-representant voor diepe Protocol-beoordeling, geef voorkeur aan cluster-leden die:**

1. **Niet subject-singleton** zijn met enkel deze cluster-mapping (geeft cluster-context, geen geïsoleerde paar)
2. **Niet in groot subject-cluster** (>3 cluster-mappings) zitten (voorkomt confounding factors)
3. **Hoogste evidence-niveau** hebben (niveau 1 via cross-walk-Excel is sterkste basis)
4. **Middelmatig in cluster-mix** zijn (niet de enige uitzonderlijke predicate in cluster)
5. **Pilot-paar waar beschikbaar** (efficiëntie — pilot leverde reeds cluster-doel-bewijs; instructie-§3.2 optie A)

**Bij conflict tussen criteria:** prevaleren in volgorde 1 → 5. Documenteer cluster-representant-keuze per cluster met motivatie.

**T2-praktijkvoorbeeld:** pilot koos T2-S03 (`ctrl:ISO27002_5_03`) als representant voor compl:NIS2_Art21_a-cluster. Subject in subject-cluster 3 (criterium 2 licht geschonden — acceptabel want middel-cluster, niet groot). Evidence-niveau 2-3 (criterium 3 acceptabel). relatedMatch in cluster met mixed predicates (criterium 4 middelmatig). Geldige keuze gegeven afwezigheid van perfect-conforme kandidaten.

### §5.2 — Confidence-criterium (NIEUW v1.3 — expliciete drempels)

Was kwalitatief in v1.2; v1.3 expliciteert drempels op basis van T1/T2-praktijk.

| Niveau | Drempel |
|---|---|
| **Hoog** | Cluster-doel-predicate én individuele beoordeling convergeren naar zelfde doel; evidence-niveau 1-2; D4.1-status helder; geen NEN-onderbouwing voor uitzondering |
| **Middel** | Cluster-doel-predicate prevaleert; individuele beoordeling zou licht kunnen afwijken naar naabbergelegen predicate (bv. relatedMatch ipv. broadMatch); evidence-niveau 1-3; cluster-discipline §3.3 leidend |
| **Laag** | Evidence-niveau 4 OF meerdere C-criteria ambigu OF D4.1-status niet vast te stellen; mogelijk masterchat-escalatie nodig |

**Mapping naar werkflow-actie:**

- Hoog/middel → patch-voorstel autoritatief; geen masterchat-judgement nodig
- Laag → twijfel-escalatie conform §4 of cluster-discipline-default-toepassing met expliciete confidence-vermelding

**T2-praktijkbevinding:** in Stap 3 leverde cluster-discipline-overerving uitsluitend hoge confidence (cluster-cardinaliteit-feit + uniforme cluster-doel-toepassing). Middel-confidence trad alleen op in pilot (T2-S05, T2-S08-alt) waar cluster-discipline-overerving spanning had met individuele beoordeling — beide zonder NEN-aantoonbare uitzondering.

---

## §6. Sample-keuze voor pilot (ongewijzigd t.o.v. v1.2)

**Sample-grootte:** 5 paren standaard (T1-precedent). Voor sprints met >50 paren over meerdere predicate-types: **7-10 paren aanbevolen** voor adequate dekking (T2-precedent: 8).

**Spreiding-richtlijnen:**

| Richtlijn | Reden |
|---|---|
| Verdeling over predicate-types | Pilot dekt alle aanwezige huidige predicate-types in sprint-scope |
| Mix van upgrade- en downgrade-verwachting | Pilot is empirisch; geen pre-pilot-uitkomst-verwachting, wel spreiding waar zowel upgrade als downgrade waarschijnlijk is |
| Spreiding over cluster-typen | Cluster-representanten uit ≥3 verschillende clusters |
| Spreiding over evidence-niveau-1-bronnen | Niet alleen één bron-context; ook bron-ontbrekend-cases |
| Mix van module-combinaties | Bij multi-module-scope: cross-module-paren in pilot |

**Stop-condities pilot:**

| # | Conditie | Wat te doen |
|---|---|---|
| 1 | Confidence "laag" op ≥3 van pilot-set | Pauze; protocol-criteria-bijstelling nodig |
| 2 | Evidence-niveau 4 op ≥3 van pilot-set | Pauze; bron-discipline-probleem |
| 3 | D4.1-disclaimer-status "niet-onderzocht" op ≥3 van pilot-set | Pauze; evidence-niveau-1-pre-stap onvoldoende uitgevoerd |
| 4 | Onverwacht-patroon — uitkomst sterk wijkt af van wat masterchat-scope-bepaling impliceerde | Pauze; masterchat-input nodig |

**Geen pre-pilot-uitkomst-verwachting** — empirische onafhankelijkheid van Tech-uitkomst is gewaarborgd.

---

## §7. Werkverdeling Tech ↔ Masterchat (ongewijzigd t.o.v. v1.2)

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
- Protocol-versie-vaststelling
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

## §8. Discipline voor licentie-bronnen (ongewijzigd t.o.v. v1.2)

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

- Letterlijke citaten van controle-tekst, guidance-tekst, of Annex-tekst
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

## §9. Diff-applier-discipline (ongewijzigd t.o.v. v1.2)

T1-leerpunt 5: Tech leverde diff-bestanden als specificatie zonder werkbare applier. `patch -p0` faalde. Masterchat moest Python-applier schrijven.

**Verplichting:**

Bij sprints met ontologie-patches levert Tech standaard zowel:

1. **Specificatie** (TTL-diff-bestand of equivalente lijst van te wijzigen triples)
2. **Werkbare applier** — Python-script (geprefereerd; T1-precedent), unified-diff (`patch -p0`-compatibel), of sed-script met gerichte patterns
3. **Integratie-test** vóór levering — Tech runt de applier op een tijdelijke gepatchte kopie en verifieert:
   - Aantal mutaties matcht specificatie
   - Geen onbedoelde nevenwijzigingen
   - File-hash van resultaat matcht canonical metrics-script-verwachting

**Geen specificatie-only-deliverables.**

**Bidirectional-relevant detail:** de applier moet zowel upgrade-, downgrade-, als richtings-correctie-mutaties ondersteunen. Eén applier voor alle drie types; geen aparte upgrade/downgrade-scripts.

**T2-precedent:** `apply_patch_v4_6_2.py` met dry-run + productie-modus via `--apply`-flag werkt voor alle 65 mutaties (32 downgrade + 33 upgrade) in één run.

---

## §10. Werkflow-discipline (HERZIEN v1.3 — uitgebreid met §10.2-§10.5)

### §10.1 — Werkflow-leerpunten-markering tijdens sprint (ongewijzigd t.o.v. v1.2)

Tijdens uitvoering noteert Tech leerpunten voor de § van het eind-sprint-rapport. Zeven categorieën:

1. **Tooling-gaten** — welke automation/scripts ontbraken?
2. **Bron-toegankelijkheid** — welke documenten waren niet vindbaar?
3. **Protocol-criteria-onduidelijkheden** — welke C-criterium-formulering bleek ambigu?
4. **Werkverdeling-momenten** — waar Tech-autonomie of escalatie aan masterchat-discussie waard?
5. **Cluster-discipline-toepassings-ervaringen** — werkte cluster-overerving in praktijk?
6. **D4.1-pre-stap-praktijk** — hoeveel tijd kostte disclaimer-detectie? Cluster-niveau of per-paar?
7. **Upgrade-detectie-praktijk** — kwamen er upgrade-kandidaten boven? Was §3.1-tabel symmetrisch toepasbaar?

Markeren voortdurend, niet alleen achteraf.

### §10.2 — Bottom-up rapport-bouw (NIEUW v1.3 — verplicht)

T2-pilot-leerpunt §6.4 + T2-Stap-3-toepassing bevestigden: **rapport-secties opbouwen in deze volgorde:**

| Sectie-volgorde | Reden |
|---|---|
| §3 detail-werk eerst (cluster-beoordelingen, paar-tabellen) | Feitelijke basis-data |
| §4-§7 onderbouwing + analyse | Volgt uit §3 |
| §8-§9 hand-off + verwijzingen | Volgt uit §3-§7 |
| **§1 samenvatting + §2 methode laatst** | Afgeleid uit alle voorgaande secties |

**Indien §1 vroeg-invullen onvermijdelijk** (bv. bij raming-werk): expliciet markeren "INITIEEL, TE BEVESTIGEN IN §3-§7-ITERATIE" en in finale versie corrigeren via iteratie-loop.

**Anti-patroon:** §1.1 distributie-tabel invullen vóór §4 detail-werk leidde in T2-pilot tot classificatie-fout (T2-S08-alt initieel "behoud" → §4.8-correctie "upgrade" — uiteindelijk weer "behoud" na helper-script-validatie). Bottom-up volgorde voorkomt herhaling.

### §10.3 — Interne tabel-consistentie-discipline (NIEUW v1.3)

Bij rapporten + instructies met meerdere metrics-tabellen die naar elkaar verwijzen of overlappen: **expliciete consistentie-check voorafgaand aan hand-off.**

**Praktische test:** voor elke twee tabellen die dezelfde metric in andere context tonen (bv. "T2-totaal" + "Stap 3 resterend" + "Pilot referentie"):

- Optellingen moeten kloppen: Σ(deelverzamelingen) = totaal
- Definitie-grenzen moeten compatibel zijn (zelfde scope-aanname)
- Bij discrepantie: bron-van-waarheid expliciet aanwijzen (helper-script / canonical metrics JSON)

**T2-instructie-leerpunt (patch-rapport §13.2):** masterchat-instructie §1 verwachtings-tabel ("m10 related 27") was niet consistent met §8 GO-criterium ("m10 related 0") door impliciete cumulatieve-scope-formulering. Protocol 12 (instructie-consistentie) is in v1.3 expliciet uitgebreid met deze tabel-consistentie-discipline voor zowel masterchat-instructies als Tech-rapporten.

### §10.4 — Helper-script-classificatie als bron-van-waarheid (NIEUW v1.3)

Bij discrepantie tussen handmatige rapport-classificatie en helper-script-output is **helper-script autoritatief** omdat het strikt protocol-letter toepast (§3.1 predicate-doel-tabel + §3.2 sterkte-ordening).

**Werkwijze bij discrepantie-vondst:**

1. Helper-script-output documenteren in patch-rapport
2. Handmatige rapport-classificatie vergelijken
3. Discrepantie expliciet noemen (welke paren, welke afwijking)
4. Helper-script-classificatie als finale toepassen
5. Bron-rapporten corrigeren via errata-aantekening (T-historie bewaren; geen herschrijven van §-detail-tekst)

**T2-precedent:** T2-S03 + T2-S08-alt-discrepanties in pilot-rapport → errata-blok bovenaan pilot-rapport + correctie in Stap 3-rapport §1.1 pilot-referentie-rij. Patch-impact identiek (helper-script werkt op TTL-state, niet rapport-state); classificatie-kolom gecorrigeerd voor methodische hygiëne.

### §10.5 — Metrics-tabel-scope-annotatie (NIEUW v1.3)

Bij metrics-tabellen in rapporten + instructies: **expliciete scope-annotatie verplicht** (bv. "m10-only" / "m10+m14 cumulatief" / "T-sprint-totaal" / "module-X-scope").

**Onderbouwing:** patch-rapport v4.6.2 §13.2-leerpunt toonde dat impliciete scope-aanname in metrics-tabel-cellen (bv. "related 27" zonder annotatie) leidt tot interpretatie-discrepantie tussen instructie-secties en tussen instructie en werkelijke uitkomst.

**Praktisch:**

- Tabel-titel of -caption noemt scope expliciet
- Bij multi-scope-tabellen: rijen of kolommen apart annoteren
- Bij Δ-tabellen (vergelijking v_a vs v_b): scope-grenzen voor beide versies expliciet

---

## §11. Sign-off-log (HERZIEN v1.3 — protocol-versie-historie)

In v1.2 bevatte deze sectie pending-beslis-punten voor T2-scoping. Voor v1.3 wordt §11 protocol-versie-historie + sign-off-status per versie.

| Versie | Datum | Status | Sign-off door | Operationeel toegepast op |
|---|---|---|---|---|
| v1.0 | 26 mei 2026 | final | Steven (T1-scoping) | T1-sprint (28 paren) |
| v1.1 | 27 mei 2026 | DRAFT — nooit operationeel | n.v.t. | n.v.t. (vervangen door v1.2 in T2-scoping) |
| v1.2 | 27 mei 2026 | final | Steven (T2-scoping) | T2-sprint (118 paren over 10 clusters) |
| v1.3 | 27 mei 2026 | **final** — vastgesteld 28 mei 2026 | Masterchat (T3-scoping) | T3-sprint (m14, 31 paren) |

**Vastgesteld bij T3-scoping** (28 mei 2026, masterchat-besluit; push door masterchat conform werkflow-wijziging 28 mei 2026). v1.2 blijft autoritatief voor T2-historie.

---

## §12. Wat dit protocol NIET doet (ongewijzigd t.o.v. v1.2)

- Beoordeelt geen individuele paren — dat is Tech-werk per sprint
- Bepaalt geen ontologie-patch — dat volgt uit beoordeling
- Wijzigt geen D-decisions — D4 + D4.1 zijn autoritatief; dit protocol opereert binnen D4 + D4.1
- Adresseert geen wijziging in andere SKOS-vocabulaire-keuzes (bv. SKOS-axioma-set-handling; H41-kandidaat-status)
- Vervangt v1.0/v1.1/v1.2 niet — voorgangers blijven beschikbaar voor historische referentie

---

## §13. Wijzigingen — overzicht

### §13.1 — Wijzigingen v1.3 t.o.v. v1.2

| # | Wijziging | Bron |
|---|---|---|
| 1 | §2.1 C1 "partieel"-grens verduidelijking + drie-uitkomst-classificatie + T2-precedenten | Pilot-rapport §7.3 voorstel 1 + Stap 3-rapport §6.3 |
| 2 | §2.2 C2 subject-cluster vs object-cluster prevalence-regel expliciet | Pilot-rapport §7.3 voorstel 2 + Stap 3-rapport §6.3 |
| 3 | §3.3 Cluster-discipline-bewijslast-asymmetrie + T2-empirisch bewijs | Stap 3-rapport §6.5 + patch-rapport §6.3 |
| 4 | §5.1 Cluster-representant-keuze-criteria als formele sub-sectie | Pilot-rapport §7.3 voorstel 4 |
| 5 | §5.2 Confidence-criterium expliciete drempels (hoog/middel/laag) | Pilot-rapport §7.3 voorstel 3 + Stap 3-rapport §6.7 |
| 6 | §10.2 Bottom-up rapport-bouw verplicht | Pilot-rapport §6.4 + Stap 3-rapport §6.4 |
| 7 | §10.3 Interne tabel-consistentie-discipline | Patch-rapport v4.6.2 §13.2 (masterchat-instructie-fout) |
| 8 | §10.4 Helper-script-classificatie als bron-van-waarheid | Stap 3-rapport §6.4 + patch-rapport §13.1 (errata-precedent) |
| 9 | §10.5 Metrics-tabel-scope-annotatie verplicht | Patch-rapport v4.6.2 §13.2 |
| 10 | §11 Protocol-versie-historie + sign-off-status | Administratieve herziening |

### §13.2 — Cumulatieve wijzigingen v1.3 t.o.v. v1.0 (via v1.1 + v1.2)

| # | Wijziging | Eerste introductie |
|---|---|---|
| 1 | D4.1-vooraf-check als nieuwe stap vóór C1-C4 | v1.1 (D4.1 vastgesteld 27 mei 2026) |
| 2 | C2-cardinaliteit binnen bredere mapping-cluster | v1.1 (T1 §8 leerpunt 3) |
| 3 | Evidence-niveau-1-pre-stap als standaard `sources/`-doorzoek | v1.1 (T1 §4.2 aanbeveling 3) |
| 4 | Pre-pilot-verwachting verwijderd uit §6 | v1.1 (T1 §8 leerpunt 2 alt) |
| 5 | Tech-autonomie voor NEN-toetsing via lokale bron-toegang | v1.1 (Steven-koers-correctie 27 mei 2026) |
| 6 | §7 Werkverdeling Tech↔Masterchat als expliciete sectie | v1.1 (T1 §8 leerpunt 4) |
| 7 | §8 Discipline licentie-bronnen — parafrase-regels + Protocol 14-uitbreiding | v1.1 (T1 + Steven-koers-correctie) |
| 8 | §9 Diff-applier-discipline — Tech levert werkbare applier | v1.1 (T1 §8 leerpunt 5) |
| 9 | Cluster-discipline expliciet verplicht | v1.1 (T1 §8 leerpunt 9) |
| 10 | Twee-zijdige edge-case-analyse-format als verplicht escalatie-format | v1.1 (T1 §8 leerpunt 8) |
| 11 | Bidirectional toetsing + predicate-doel-tabel + mutatie-richting | v1.2 (T2-scope-vaststelling) |
| 12 | §3.1 Predicate-doel-tabel vervangt failure-respons-tabel | v1.2 (T2-scope B bidirectional) |
| 13 | §3.2 Predicate-sterkte-ordening + mutatie-richting-classificatie expliciet | v1.2 |
| 14 | §3.3 Cluster-discipline expliciet symmetrisch geformuleerd | v1.2 |
| 15 | §5 Output-formaat: nieuwe kolommen "Huidige predicate", "Doel-predicate", "Mutatie-richting" | v1.2 |
| 16 | §6 Sample-keuze: spreiding over predicate-types + mix upgrade/downgrade-kandidaten | v1.2 |
| 17 | §9 Bidirectional-applier-vereiste expliciet | v1.2 |
| 18 | §10 "Upgrade-detectie-praktijk" als zevende leerpunten-categorie | v1.2 |
| 19 | C1 "partieel"-grens verduidelijking + drie-uitkomst-classificatie | v1.3 (T2-leerpunt) |
| 20 | C2 subject-cluster vs object-cluster prevalence-regel | v1.3 (T2-leerpunt) |
| 21 | Cluster-discipline-bewijslast-asymmetrie expliciet | v1.3 (T2-leerpunt) |
| 22 | Cluster-representant-keuze-criteria formele sub-sectie | v1.3 (T2-leerpunt) |
| 23 | Confidence-criterium expliciete drempels | v1.3 (T2-leerpunt) |
| 24 | Bottom-up rapport-bouw verplicht | v1.3 (T2-leerpunt) |
| 25 | Interne tabel-consistentie-discipline | v1.3 (masterchat-werkflow-leerpunt) |
| 26 | Helper-script-classificatie autoritatief | v1.3 (T2-leerpunt) |
| 27 | Metrics-tabel-scope-annotatie verplicht | v1.3 (masterchat-werkflow-leerpunt) |
| 28 | §11 Protocol-versie-historie | v1.3 (administratief) |

---

*Einde protocol v1.3 (FINAL). Protocol gaat naar Tech voor T3-sprint-uitvoering (m14). v1.2 blijft autoritatief voor T2-historie; voorgangers blijven beschikbaar voor historische referentie.*
