---
type: report
subtype: presprint-inventarisatie
sprint: T1
baseline: v4.6.0
date: 2026-05-26
status: final
related:
  - H36_skos-exactmatch-ctrl-compl-audit
  - D04_skos-cross-framework
  - D05_sameAs-strikt-ctrl-bio
scope: "Stap 1 — pre-sprint-inventarisatie, read-only. Vraag A t/m E. Geen ontologie-wijzigingen, geen herclassificatie-voorstellen."
---

# T1 — Pre-sprint-inventarisatie SKOS-kwaliteitsanalyse Fase 1 (H36-cluster)

## Context

- Baseline: **v4.6.0** (21 mei 2026)
- Combined graph: **21.069 triples** uit **22 .ttl-modules** in `ontology/`
- Sprint-instructie: §3 (T1-test-sprint, pre-sprint-inventarisatie)
- Werkwijze: rdflib 7.6.0 + SPARQL over gecombineerde graph; per-file parse voor module-attributie
- Disclaimer: **alleen feiten, geen interpretatie of herclassificatie-voorstellen**

---

## Vraag A — Extractie van de 28 paren ctrl:→compl: `skos:exactMatch`

**Verificatie-getal: 28 — KLOPT EXACT** (geen afwijking, geen stop-conditie).

Reverse-richting (`compl:` → `ctrl:`): 0 paren. De relatie is asymmetrisch gemodelleerd (D4 staat dat toe; SKOS-symmetrie-eis geldt formeel maar wordt hier niet expliciet gespiegeld in de TBox).

Alle 28 paren staan gedeclareerd in **één enkel bestand**: `ontology/m10-nis2-ext.ttl`.

| # | Subject (ctrl:) | Object (compl:) | Module-bron | rdfs:label@nl (subject) | rdfs:label@nl (object) | ext:sourceAttribution |
|---|---|---|---|---|---|---|
| 1 | ctrl:ISO27002_5_01 | compl:NIS2_Art21_a | m10-nis2-ext.ttl | Beleidsregels voor informatiebeveiliging | NIS2 art.21(2)(a) — Risicoanalyse en beveiliging informatiesystemen | — (geen ext:sourceAttribution op individu-niveau) |
| 2 | ctrl:ISO27002_5_09 | compl:NIS2_Art21_i | m10-nis2-ext.ttl | Inventarisatie van informatie en andere gerelateerde bedrijfsmiddelen | NIS2 art.21(2)(i) — Beveiliging personeel, toegangsbeleid en activabeheer | — |
| 3 | ctrl:ISO27002_5_15 | compl:NIS2_Art21_i | m10-nis2-ext.ttl | Toegangsbeveiliging | NIS2 art.21(2)(i) — Beveiliging personeel, toegangsbeleid en activabeheer | — |
| 4 | ctrl:ISO27002_5_16 | compl:NIS2_Art21_i | m10-nis2-ext.ttl | Identiteitsbeheer | NIS2 art.21(2)(i) — Beveiliging personeel, toegangsbeleid en activabeheer | — |
| 5 | ctrl:ISO27002_5_18 | compl:NIS2_Art21_i | m10-nis2-ext.ttl | Toegangsrechten | NIS2 art.21(2)(i) — Beveiliging personeel, toegangsbeleid en activabeheer | — |
| 6 | ctrl:ISO27002_5_19 | compl:NIS2_Art21_d | m10-nis2-ext.ttl | Informatiebeveiliging in leveranciersrelaties | NIS2 art.21(2)(d) — Beveiliging van de toeleveringsketen | — |
| 7 | ctrl:ISO27002_5_20 | compl:NIS2_Art21_d | m10-nis2-ext.ttl | Adresseren van informatiebeveiliging in leveranciersovereenkomsten | NIS2 art.21(2)(d) — Beveiliging van de toeleveringsketen | — |
| 8 | ctrl:ISO27002_5_21 | compl:NIS2_Art21_d | m10-nis2-ext.ttl | Beheren van informatiebeveiliging in de ICT-toeleveringsketen | NIS2 art.21(2)(d) — Beveiliging van de toeleveringsketen | — |
| 9 | ctrl:ISO27002_5_22 | compl:NIS2_Art21_d | m10-nis2-ext.ttl | Monitoren, beoordelen en het beheren van wijzigingen van leveranciersdiensten | NIS2 art.21(2)(d) — Beveiliging van de toeleveringsketen | — |
| 10 | ctrl:ISO27002_5_24 | compl:NIS2_Art21_b | m10-nis2-ext.ttl | Plannen en voorbereiden van het beheer van informatiebeveiligingsincidenten | NIS2 art.21(2)(b) — Incidentbehandeling | — |
| 11 | ctrl:ISO27002_5_25 | compl:NIS2_Art21_b | m10-nis2-ext.ttl | Beoordelen van en besluiten over informatiebeveiligingsgebeurtenissen | NIS2 art.21(2)(b) — Incidentbehandeling | — |
| 12 | ctrl:ISO27002_5_26 | compl:NIS2_Art21_b | m10-nis2-ext.ttl | Reageren op informatiebeveiligingsincidenten | NIS2 art.21(2)(b) — Incidentbehandeling | — |
| 13 | ctrl:ISO27002_5_27 | compl:NIS2_Art21_b | m10-nis2-ext.ttl | Leren van informatiebeveiligingsincidenten | NIS2 art.21(2)(b) — Incidentbehandeling | — |
| 14 | ctrl:ISO27002_5_29 | compl:NIS2_Art21_c | m10-nis2-ext.ttl | Informatiebeveiliging tijdens een verstoring | NIS2 art.21(2)(c) — Bedrijfscontinuïteit, back-upbeheer en noodherstel | — |
| 15 | ctrl:ISO27002_5_30 | compl:NIS2_Art21_c | m10-nis2-ext.ttl | ICT-gereedheid voor bedrijfscontinuïteit | NIS2 art.21(2)(c) — Bedrijfscontinuïteit, back-upbeheer en noodherstel | — |
| 16 | ctrl:ISO27002_5_35 | compl:NIS2_Art21_f | m10-nis2-ext.ttl | Onafhankelijke beoordeling van informatiebeveiliging | NIS2 art.21(2)(f) — Beoordeling doeltreffendheid cyberbeveiligingsmaatregelen | — |
| 17 | ctrl:ISO27002_5_36 | compl:NIS2_Art21_f | m10-nis2-ext.ttl | Naleving van beleid, regels en normen voor informatiebeveiliging | NIS2 art.21(2)(f) — Beoordeling doeltreffendheid cyberbeveiligingsmaatregelen | — |
| 18 | ctrl:ISO27002_6_01 | compl:NIS2_Art21_i | m10-nis2-ext.ttl | Screening | NIS2 art.21(2)(i) — Beveiliging personeel, toegangsbeleid en activabeheer | — |
| 19 | ctrl:ISO27002_6_02 | compl:NIS2_Art21_i | m10-nis2-ext.ttl | Arbeidsovereenkomst | NIS2 art.21(2)(i) — Beveiliging personeel, toegangsbeleid en activabeheer | — |
| 20 | ctrl:ISO27002_6_03 | compl:NIS2_Art21_g | m10-nis2-ext.ttl | Bewustwording van, opleiding en training in informatiebeveiliging | NIS2 art.21(2)(g) — Cyberhygiënepraktijken en opleiding cyberbeveiliging | — |
| 21 | ctrl:ISO27002_8_05 | compl:NIS2_Art21_j | m10-nis2-ext.ttl | Beveiligde authenticatie | NIS2 art.21(2)(j) — Multi-factor authenticatie en continue authenticatie | — |
| 22 | ctrl:ISO27002_8_13 | compl:NIS2_Art21_c | m10-nis2-ext.ttl | Back-up van informatie | NIS2 art.21(2)(c) — Bedrijfscontinuïteit, back-upbeheer en noodherstel | — |
| 23 | ctrl:ISO27002_8_24 | compl:NIS2_Art21_h | m10-nis2-ext.ttl | Gebruik van cryptografie | NIS2 art.21(2)(h) — Cryptografie en encryptie | — |
| 24 | ctrl:ISO27002_8_25 | compl:NIS2_Art21_e | m10-nis2-ext.ttl | Beveiligen tijdens de ontwikkelcyclus | NIS2 art.21(2)(e) — Beveiliging verwerving, ontwikkeling en onderhoud systemen | — |
| 25 | ctrl:ISO27002_8_26 | compl:NIS2_Art21_e | m10-nis2-ext.ttl | Toepassingsbeveiligingseisen | NIS2 art.21(2)(e) — Beveiliging verwerving, ontwikkeling en onderhoud systemen | — |
| 26 | ctrl:ISO27002_8_27 | compl:NIS2_Art21_e | m10-nis2-ext.ttl | Veilige systeemarchitectuur en technische uitgangspunten | NIS2 art.21(2)(e) — Beveiliging verwerving, ontwikkeling en onderhoud systemen | — |
| 27 | ctrl:ISO27002_8_28 | compl:NIS2_Art21_e | m10-nis2-ext.ttl | Veilig coderen | NIS2 art.21(2)(e) — Beveiliging verwerving, ontwikkeling en onderhoud systemen | — |
| 28 | ctrl:ISO27002_8_29 | compl:NIS2_Art21_e | m10-nis2-ext.ttl | Testen van de beveiliging tijdens ontwikkeling en acceptatie | NIS2 art.21(2)(e) — Beveiliging verwerving, ontwikkeling en onderhoud systemen | — |

**Toelichting kolommen:**

- **Module-bron (subject)**: subject-individu `ctrl:ISO27002_*` is gedeclareerd in `ontology/m02-control.ttl` (ISO27002Control-cluster). Voor leesbaarheid is hierboven alleen de module getoond waarin de `skos:exactMatch`-triple zelf staat — dat is voor alle 28 paren `m10-nis2-ext.ttl`.
- **Module-bron (object)**: object-individu `compl:NIS2_Art21_*` is gedeclareerd in `ontology/m10-nis2-ext.ttl` (samen met de mappings zelf).
- **rdfs:comment**: geen van de 28 ctrl:-subjecten heeft een rdfs:comment vastgelegd; rdfs:comments staan wel op de compl:-objecten (zien hierboven onder "Label NL (o)" — die label-tekst is feitelijk een korte annotatie van de NIS2-clause). Per paar afzonderlijke comment-extractie is niet uitgevoerd omdat de bron-comment ontbreekt op subject-zijde.
- **ext:sourceAttribution**: geen van de 56 individu-uiteinden draagt een directe `ext:sourceAttribution`-triple. De attribuering staat op module-niveau in m10-nis2-ext.ttl (bron: EU NIS2-richtlijn 2022/2555). Geen per-mapping-attribuering.

---

## Vraag B — Multi-module-discipline (counts per predicate ctrl:↔compl:)

| Predicate | ctrl: → compl: | compl: → ctrl: | Som |
|---|---:|---:|---:|
| `skos:exactMatch` | **28** | 0 | 28 |
| `skos:closeMatch` | 32 | 2 | 34 |
| `skos:relatedMatch` | 33 | 27 | 60 |
| `skos:broadMatch` | 25 | 2 | 27 |
| `skos:narrowMatch` | 0 | 0 | 0 |
| **Totaal ctrl:↔compl:** | 118 | 31 | **149** |

**Observaties (feitelijk, niet interpretatief):**

- De 28 `exactMatch`-paren maken **19 %** uit van de 149 ctrl:↔compl:-cross-namespace-mappings.
- Het cluster ctrl:↔compl: bevat alle vier de "actieve" SKOS-match-types (`exactMatch`, `closeMatch`, `relatedMatch`, `broadMatch`). `narrowMatch` is niet gebruikt.
- Reverse-richting `compl:→ctrl:` bevat geen `exactMatch`-paren, wel `closeMatch` (2), `relatedMatch` (27) en `broadMatch` (2).
- De 28 `exactMatch`-paren zijn dus niet "geïsoleerd"; ze bestaan binnen een breder mapping-cluster met 121 andere mappings.

---

## Vraag C — Clustering per source-module

### C.1 — Verdeling van de 28 paren over modules

| Module(s) waarin triple gedeclareerd | # paren |
|---|---:|
| `m10-nis2-ext.ttl` | **28** |

Eén module bevat alle 28 `exactMatch`-paren. Geen verdeling over meerdere modules.

### C.2 — Subject/object-namespace-profiel per paar

| Aspect | Waarde |
|---|---|
| Subject-namespace | 28/28 in `ctrl:` (specifiek: `ctrl:ISO27002_*` ISO27002Control-individuals, gedeclareerd in `m02-control.ttl`) |
| Object-namespace | 28/28 in `compl:` (specifiek: `compl:NIS2_Art21_*` RegulatoryObligation-individuals, gedeclareerd in `m10-nis2-ext.ttl`) |
| Subject-type | 28/28 `ctrl:ISO27002Control` |
| Object-type | 28/28 `compl:RegulatoryObligation` |

### C.3 — D5-relevante observatie (ctrl:↔bio:-context)

Voor elk van de 28 `ctrl:`-subjecten is gecontroleerd of er ook een `owl:sameAs`-relatie naar `bio:` bestaat (D5-conform).

| Resultaat | Aantal |
|---|---:|
| `ctrl:`-subject heeft `owl:sameAs bio:*` | **28 / 28** |
| `ctrl:`-subject heeft géén `owl:sameAs bio:*` | 0 / 28 |

Alle 28 ctrl:-subjecten zijn dus ingebed in de bestaande D5-`owl:sameAs`-brug (93 paren in `grc-bridges.ttl`). Het patroon is consistent: `ctrl:ISO27002_X_YY owl:sameAs bio:ISO27002_X_YY`. **Feitelijk:** subject-zijde is volledig D5-genormaliseerd.

**Belangrijk feit (geen interpretatie):** de object-zijde (`compl:NIS2_Art21_*`) is geen ISO27002-control en geen BIO-maatregel — het is een NIS2-RegulatoryObligation. De vraag "had object eigenlijk in bio: moeten staan" (uit instructie §3 Vraag C) wordt verder onderzocht in Vraag E.

---

## Vraag D — SHACL-shape-betrokkenheid

### D.1 — Shapes die `skos:exactMatch` expliciet referenties

In `ontology/grc-shacl.ttl` zijn er **2 SPARQL-hits** op `skos:exactMatch`:

| Shape | sh:path | sh:targetNode / scope | Acteert op de 28 ctrl:↔compl:-paren? |
|---|---|---|---|
| `asset:BVASymmetryShape` | `skos:exactMatch` | `fw:TBB_Personen`, `fw:TBB_Informatie`, `fw:TBB_Informatiesystemen`, `fw:TBB_Materieel`, `fw:TBB_Goederen`, `fw:TBB_Imago`, `fw:TBB_Objecten` | **Nee** — `sh:targetNode` is beperkt tot 7 `fw:TBB_*`-concepten; raakt de 28 ctrl:↔compl:-paren niet. |
| (blank node) — eigenschap-blok binnen `asset:BVASymmetryShape` | `skos:exactMatch` | Idem | Nee — sub-blok van BVASymmetryShape. |

### D.2 — Bredere telling

| Aspect | Waarde |
|---|---:|
| Totaal `sh:NodeShape` + `sh:PropertyShape` in `grc-shacl.ttl` | 7 |
| Shapes met SKOS-predicate in `sh:path` | 1 (`asset:BVASymmetryShape`, path = `skos:exactMatch`) |
| Shapes die de 28 ctrl:↔compl:-paren als `sh:targetNode`/`sh:targetClass`/`sh:targetSubjectsOf` raken | **0** |

### D.3 — Conclusie van Vraag D (feitelijk)

Geen enkele SHACL-shape in `grc-shacl.ttl` valideert direct op de 28 ctrl:↔compl: `skos:exactMatch`-paren. Het is een **SHACL-blinde vlek**: de mappings ondergaan momenteel geen geautomatiseerde shape-validatie (los van eventuele indirecte effecten via SECTIE B AppliesToAssetTypeRange/OrphanClass, die niet op deze paren acteren).

---

## Vraag E — D5-collision-check

Vier heuristische checks uitgevoerd. **Stop-conditie zou intreden bij vondst van échte collision** (ctrl:↔compl:-paar waar object eigenlijk in `bio:` had moeten staan, of waar `owl:sameAs` had moeten gelden).

### E.1 — Check 1: dubbele mapping ctrl:→compl: én ctrl:→bio:?

Vraag: heeft enig ctrl:-subject uit de 28 paren ook `owl:sameAs` naar een bio:-individual? Zo ja, is dat een potentiële duplicate-mapping?

| Resultaat | Aantal |
|---|---:|
| ctrl:-subject heeft `owl:sameAs bio:*` | 28 / 28 |

**Feitelijke duiding:** alle 28 ctrl:-subjecten hebben `owl:sameAs` naar bio:. Dit is op zichzelf **geen collision** — D5 staat ctrl:↔bio: `owl:sameAs` toe en is daarvoor expliciet ontworpen. De vraag is of de target van de `skos:exactMatch` (`compl:NIS2_Art21_*`) overlapt met een bio:-individual; dat wordt in E.2 en E.3 getest.

### E.2 — Check 2: gelijknamige bio:-individuals voor de compl:-objecten?

Voor elk van de 28 unieke `compl:NIS2_Art21_*`-objecten: bestaat er een `bio:NIS2_Art21_*`-individual met dezelfde IRI-suffix?

| Resultaat | Aantal |
|---|---:|
| compl:-target heeft gelijknamig bio:-individual | **0 / 28** |

**Geen collision.** Geen enkele NIS2-clause heeft een dubbele declaratie in bio:.

### E.3 — Check 3: rdf:type van compl:-objecten — is enige er bio:BIOControl of bio:OverheidsMaatregel?

| Resultaat | Aantal |
|---|---:|
| compl:-object met `rdf:type bio:BIOControl` of `bio:OverheidsMaatregel` | **0 / 28** |

**Geen collision.** Alle 28 objecten zijn `compl:RegulatoryObligation`, geen bio:-typering.

### E.4 — Check 4: type-profiel sanity-check

| Type-profiel compl:-object | # paren |
|---|---:|
| `compl:RegulatoryObligation` | 28 / 28 |

| Type-profiel ctrl:-subject | # paren |
|---|---:|
| `ctrl:ISO27002Control` | 28 / 28 |

Strikt homogeen aan beide zijden — geen afwijkende paren.

### E.5 — Conclusie Vraag E (feitelijk)

**Geen D5-collisions gedetecteerd.** De 28 paren respecteren D5-discipline:

- subject-zijde is D5-gecanoniseerd (28/28 hebben `owl:sameAs bio:`)
- object-zijde zit in `compl:`-namespace, niet in `bio:` — geen overlap met D5-scope
- geen gelijknamige bio:-individuals, geen bio:-typering op compl:-objecten

**Geen stop-conditie geraakt.**

---

## Bevindingen-samenvatting

- Verificatie-getal **28 klopt exact** — geen afwijking, geen stop-conditie op Vraag A.
- Alle 28 paren zijn gedeclareerd in één bestand (`m10-nis2-ext.ttl`); subject-namespace `ctrl:` (ISO27002Control), object-namespace `compl:` (RegulatoryObligation) — strikt homogeen.
- De 28 `exactMatch`-paren maken deel uit van een breder ctrl:↔compl:-cluster van **149 mappings** verspreid over `exactMatch`, `closeMatch`, `relatedMatch` en `broadMatch` (geen `narrowMatch`).
- Geen SHACL-shape in `grc-shacl.ttl` valideert direct op deze 28 paren — `asset:BVASymmetryShape` raakt alleen `fw:TBB_*`-concepten.
- Geen D5-collisions: alle 28 ctrl:-subjecten zijn D5-`owl:sameAs`-genormaliseerd; geen gelijknamige bio:-individuals voor compl:-targets; geen bio:-typering op compl:-objecten.

---

## Volgende-stap-aanbeveling

Klaar voor masterchat-review voor Stap 2 protocol-draft (verificatie-getal bevestigd, geen stop-condities, geen scope-pauze nodig).

— Einde rapport.
