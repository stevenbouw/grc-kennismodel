# SKOS-beoordelings-protocol v1.1 (DRAFT)

**Voor:** Tech-subagent in Claude Code — toepassing vanaf T2-sprint
**Auteur:** Masterchat
**Datum:** 27 mei 2026
**Status:** **DRAFT** — vaststelling pending bij T2-scoping-sessie
**Aanleiding:** T1-eindrapport §4.2 (6 aanbevelingen) + §8 leerpunten 2, 4, 5, 8, 9 + D4.1-vastlegging (27-05-2026 mini-revisie)
**Scope:** SKOS-predicate-keuze-criteria + beslis-tabel + evidence-hiërarchie + twijfelgevallen-procedure + werkverdeling Tech↔Masterchat. Herbruikbaar voor T2 (overige 1.770 SKOS-mappings) en T3+.
**Voorganger:** `docs/skos-beoordelings-protocol-v1_0.md` (vastgesteld 26 mei 2026 voor T1, blijft beschikbaar voor historische referentie)

---

## §0. Aanleiding voor v1.1 — wat verandert t.o.v. v1.0

T1 (26 mei 2026) leverde 28 ctrl:↔compl:-paren-uitkomst en negen werkflow-leerpunten. Daarop volgde D4.1-vastlegging (27 mei 2026). Beide rechtvaardigen protocol-evolutie.

**Negen aanpassingen t.o.v. v1.0** (uitgebreid in §13):

1. C2-cardinaliteit-toets binnen bredere mapping-cluster (niet alleen N-set)
2. Pre-pilot-verwachting verwijderd uit §6 (leverde stop-conditie-noise in T1)
3. Evidence-niveau-1-pre-stap als standaard (`sources/`-doorzoek)
4. **D4.1-vooraf-check** als nieuwe stap vóór C1-C4 (disclaimer-detectie)
5. **Tech autonomie voor NEN-toetsing** via lokale bron-toegang — vervangt T1-masterchat-PK-werkverdeling
6. Diff-applier-discipline expliciet (Tech levert werkbare applier, niet alleen specificatie)
7. Pre-push disclosure-check Protocol 14 breder: NEN-tekst-fragment-detectie expliciet
8. Tweezijdige edge-case-analyse-format als standaard voor twijfelgevallen
9. Cluster-discipline-overerving als verplicht werkpatroon voor cluster-volgers

---

## §1. Doel van het protocol

Voor elk SKOS-mapping-paar (subject in framework A, object in framework B) consistent en repliceerbaar beoordelen of de gekozen SKOS-predicate (`exactMatch` / `closeMatch` / `relatedMatch` / `broadMatch` / `narrowMatch`) D4 + D4.1-conform is.

Voor `exactMatch`-paren: extra zware toets via vier-criteria-set (zie §2). Voor andere predicates: lichtere toets via inhoudelijke check.

T1-bewijs heeft aangetoond dat onterechte `exactMatch`-claims systeemfouten veroorzaken (SKOS-transitiviteit-onhoudbaarheid). Protocol v1.1 is gericht op vermijden van die fouten.

---

## §2. D4 + D4.1-criteria — vooraf-check + vier-set

### §2.0 — D4.1-vooraf-check (NIEUW v1.1)

**Vóór C1-C4 doorlopen voor een `skos:exactMatch`-claim:** controleer of de autoritatieve bron achter de mapping een **non-equivalence-disclaimer** bevat.

**Praktische test:**

- Identificeer de bron-publicatie achter de mapping (ENISA TIG, NIST OLIR, ISO Annex F, CBW-Excel, BZK-publicatie, etc.)
- Lees het bron-document — zoek expliciete disclaimer-clauses (vaak in introductie, methode-sectie, of caveat-paragraaf)
- Bekende disclaimers (uitbreidbaar):
  - **ENISA TIG v1.0**, regel 285: "*The mapping should not be interpreted as a measure of equivalency among different standards or frameworks.*"
  - **NIST OLIR**: niet geverifieerd; te checken bij eerstvolgende NIST-mapping-sprint
  - **ISO Annex F**: niet geverifieerd; te checken bij eerstvolgende ISO-mapping-sprint

**Beslis-regel D4.1:**

- Disclaimer aanwezig → `skos:exactMatch` is **per definitie niet-conform**. Ga direct naar `broadMatch`/`closeMatch`/`relatedMatch`-keuze via C1-C3 (zonder C4-evidence-niveau-1-noodzaak voor de `exactMatch`-claim — alleen voor de uiteindelijke predicate-keuze)
- Disclaimer afwezig of niet gedetecteerd → ga verder met C1-C4 vier-set

### §2.1 — C1 Definitionele overlap

A en B hebben identieke scope volgens hun bron-definities.

**Praktische test:**

- Zou A de volledige reikwijdte van B invullen?
- Zou B de volledige reikwijdte van A invullen?
- Beide ja → C1 gehaald

**Voor NEN-bronnen (ISO 27002, 27001, 27005, 31000, 22301, 22313):** Tech leest direct uit `/Users/stevenbouwmeester/grc-sources-licensed/` — geen masterchat-PK-toets nodig. Discipline-regels in §8.

### §2.2 — C2 Cardinaliteit (cluster-test, gewijzigd v1.1)

**v1.0-formulering:** "geen veel-op-één of één-op-veel binnen de mapping-set"

**v1.1-formulering:** "geen veel-op-één of één-op-veel binnen de **bredere mapping-cluster**"

**Praktische test:**

- Tel alle SKOS-mappings (alle predicate-types) waarvan subject in *zelfde framework-namespace* als ons subject én object in *zelfde framework-namespace* als ons object
- Voorbeeld bij ctrl:↔compl:: tel alle 121 ctrl:↔compl:-mappings (exact + close + related + broad + narrow), niet alleen de exactMatch-subset
- Zijn er andere mappings met *zelfde subject* in de bredere cluster? Tel ze.
- Zijn er andere mappings met *zelfde object* in de bredere cluster? Tel ze.
- Beide tellingen ≤1 → C2 gehaald

**T1-bewijs voor wijziging:** binnen-N-set-cardinaliteit kan 1↔1 lijken (zoals pilot-paren #1 en #2) terwijl bredere-cluster-cardinaliteit veel↔1 toont. Strikte binnen-N-set-interpretatie leidde in T1 tot ad-hoc oplossing — v1.1-formulering voorkomt herhaling.

### §2.3 — C3 Inclusie-richting (bilaterale containment)

A ⊆ B EN B ⊆ A volgens definitie-content.

**Praktische test:**

- Is alles wat A vereist ook B-vereiste? (A ⊆ B)
- Is alles wat B vereist ook A-vereiste? (B ⊆ A)
- Beide ja → C3 gehaald

**Voor NEN-bronnen:** Tech leest direct uit lokale bron-toegang. Bij ambiguïteit waar lezing meerdere interpretaties toelaat: twijfelgevallen-lijst (zie §4).

### §2.4 — C4 Bron-bewijs

Een autoritatieve bron ondersteunt de gekozen SKOS-predicate.

**Evidence-hiërarchie (sterk → zwak), v1.1 ongewijzigd t.o.v. v1.0:**

| Niveau | Bron-type |
|---|---|
| 1 | Expliciete mapping in autoritatief mapping-document |
| 2 | Norm-tekst identiek aan beide kanten |
| 3 | Definitie-overlap via rdfs:comment of bron-tekst |
| 4 | Onderwerp-titel-overlap (zwakste) |

**Evidence-niveau-1-pre-stap (NIEUW v1.1):**

Vóór C4-toekenning aan individuele paren: doe **standaard `sources/`-doorzoek** op cross-walk-Excels of mapping-documenten die in repo aanwezig zijn voor de betreffende framework-combinatie. Voorbeelden:

- `sources/adr-norea/Cbw_NIS2_Control_Framework.xlsx` (ISO 27002 ↔ NIS2 via UV)
- `sources/csf2/CSF_2_0Implementation_Examples.xlsx` (CSF 2.0)
- Toekomstige toegevoegde mapping-documenten

Doel: voorkomen dat per-paar opnieuw wordt gezocht naar bron. Tech-actie max ~10 min vooraf voor de hele sprint-scope.

---

## §3. Beslis-tabel bij criterium-failure (D4.1-bewust)

Onderstaande tabel geeft per failure-modus de voorgestelde herclassificatie.

**v1.1-wijziging:** D4.1-detectie heeft prioriteit. Indien §2.0 disclaimer-aanwezigheid bevestigt: rij 1 (`exactMatch`-behoud) is uitgesloten ongeacht C1-C4-uitkomst.

| Failure | Aard | Herclassificatie |
|---|---|---|
| **D4.1: disclaimer aanwezig** | Bron ontkent equivalence categorisch | `skos:exactMatch` niet verdedigbaar; ga naar broadMatch/closeMatch/relatedMatch via C1-C3 |
| Geen failure + geen disclaimer | Alle vier criteria + D4.1 voldoen | Behoud `skos:exactMatch` |
| C1: A enger dan B | Definitionele subset zonder bilateraliteit | `A skos:broadMatch B` |
| C1: partiële overlap zonder subset-relatie | Thematische verwantschap | `A skos:closeMatch B` |
| C1: zwakke overlap, alleen thematisch | Onderwerp-domein hetzelfde | `A skos:relatedMatch B` |
| C2: veel A's mappen naar één B | Veel↔1 in bredere cluster | Per A: `A skos:broadMatch B` |
| C2: één A mapt naar veel B's | 1↔veel in bredere cluster | Per B: `A skos:narrowMatch B` |
| C3: A enger dan B | Subset-relatie expliciet | `A skos:broadMatch B` |
| C3: A breder dan B | Subset-relatie expliciet | `A skos:narrowMatch B` |
| C4: evidence-niveau 3-4 + C1-C3 niet sluitend | Onvoldoende bron-bewijs | Naar twijfelgevallen-lijst |
| Alle criteria falen + geen thematische verwantschap | Geen verdedigbare relatie | Verwijderen (zeldzaam) |

**Cluster-discipline (verplicht v1.1, was v1.0 §3-slot):** bij C2-failure (cardinaliteit) is herclassificatie **systematisch binnen het cluster**. Alle paren in dezelfde veel↔1-cluster krijgen dezelfde behandeling tenzij voor een specifiek paar een individuele uitzondering aantoonbaar is. Bewijslast voor uitzondering: Tech motiveert expliciet vanuit NEN-tekst of evidence-niveau-1-bron; bij twijfel naar twijfelgevallen.

---

## §4. Twijfelgevallen-procedure (gewijzigd v1.1)

**v1.0:** alle twijfelgevallen → masterchat-escalatie.

**v1.1:** Tech-autonomie omhoog door lokale NEN-toegang. Masterchat-escalatie alleen bij:

| Conditie | Reden voor escalatie |
|---|---|
| Cross-bron-interpretatie nodig | Meerdere bronnen tegenspreken elkaar |
| Bron-tekst is meerduidig | NEN-tekst zelf ambigu, geen eenduidige lezing |
| C1-C3-toets blijft sluitend ambigu | Zelfs na NEN-tekst-lezing geen helder oordeel |
| Cluster-uitzondering vereist masterchat-judgement | Bewijslast voor individuele uitzondering binnen cluster te zwak |

**Twee-zijdige analyse-format (verplicht voor escalatie, v1.1):**

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

## §5. Output-formaat per paar (v1.1 minor aangepast)

Per paar levert Tech:

| Veld | Inhoud |
|---|---|
| Paar-ID | T2-001 t/m T2-NNN |
| Subject IRI | volledige IRI |
| Object IRI | volledige IRI |
| Cluster-context | bv. "ctrl:↔compl: NIS2_b (4↔1 in 121-set)" |
| **D4.1-disclaimer-check** | aanwezig / afwezig / niet-onderzocht + bron-verwijzing |
| C1 (definitioneel) | ✓ / ✗ + 1-2 zin reden |
| C2 (cardinaliteit in bredere cluster) | ✓ / ✗ + cluster-grootte |
| C3 (inclusie) | ✓ / ✗ + richting indien failure |
| C4 (bron-evidence) | niveau 1-4 + bron-verwijzing |
| Voorstel | behoud / herclass-[predicate] / verwijder / twijfel-escaleer |
| Confidence | hoog / middel / laag |
| Patch-vereist | ja / nee |

**Verschil t.o.v. v1.0:** D4.1-disclaimer-check is nieuwe verplichte kolom. C2-formulering verwijst nu naar bredere cluster.

---

## §6. Sample-keuze voor pilot (v1.1 — pre-pilot-verwachting verwijderd)

**v1.0 had pre-pilot-verwachting in §6**: "als protocol werkt, leveren pilot-paren #1 en #2 behoud-voorstellen, paren #3, #4, #5 broadMatch-voorstellen."

**v1.1 verwijdert deze verwachting volledig.** T1 toonde dat pre-pilot-verwachting:

- Inadequate was (pilot-paren #1 en #2 werden ook broadMatch)
- Stop-conditie-noise creëerde (numerieke ≥3/5 stop-regel werd door verwachte uitkomst geraakt)
- Empirische onafhankelijkheid van Tech ondergroef

**v1.1-richtlijnen voor sample-keuze:**

- Sample-grootte: 5 paren (T1-precedent; aanpasbaar bij groter cluster naar 7-10)
- Spreiding: over cluster-typen, predicate-types, evidence-niveau-bronnen
- Verspreid over verschillende module-combinaties indien meer dan één
- Geen pre-pilot-uitkomst-verwachting

**Stop-condities pilot (v1.1):**

| # | Conditie | Wat te doen |
|---|---|---|
| 1 | Confidence "laag" op ≥3 van 5 | Pauze; protocol-criteria-bijstelling nodig |
| 2 | Evidence-niveau 4 op ≥3 van 5 | Pauze; bron-discipline-probleem |
| 3 | D4.1-disclaimer-status "niet-onderzocht" op ≥3 van 5 | Pauze; pre-stap evidence-niveau-1-pre-stap onvoldoende uitgevoerd |
| 4 | Onverwacht-patroon — uitkomst sterk wijkt af van predicate-mix die masterchat-scope-bepaling impliceerde | Pauze; masterchat-input nodig |

Verschil: geen ≥3/5-numerieke verwachting; alleen kwalitatieve stop-condities die op een werkelijk werkflow-probleem wijzen.

---

## §7. Werkverdeling Tech ↔ Masterchat (NIEUW v1.1)

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

### §7.2 — Masterchat-judgement-rol (smaller dan v1.0)

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

## §8. Discipline voor licentie-bronnen (NIEUW v1.1)

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

Protocol 14 omvat per v1.1 vijf check-categorieën (was vier):

1. Organisatie-naam
2. Persoonsnamen (m.u.v. Steven, conform)
3. Lokale paden buiten `/Users/stevenbouwmeester/grc-kennismodel/`
4. Credentials, TLD's, e-mail-domeinen
5. **NEN-tekst-fragmenten** (verbatim ISO-tekst >10 woorden) — **NIEUW v1.1**

Tech doet de check vóór hand-off aan Steven. Steven verifieert bij `git diff`-inspectie.

---

## §9. Diff-applier-discipline (NIEUW v1.1)

T1-leerpunt 5: Tech leverde diff-bestanden als **specificatie** ("vervang X door Y voor deze 28 paren") in plaats van als werkbare applier. `patch -p0` faalde. Masterchat moest Python-applier schrijven.

**v1.1-verplichting:**

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

---

## §10. Werkflow-leerpunten-markering tijdens sprint

Tijdens uitvoering noteert Tech leerpunten voor de §10 van het eind-sprint-rapport. Categorieën om op te letten:

- Tooling-gaten (welke automation ontbrak?)
- Bron-toegankelijkheid (welke documenten waren niet vindbaar?)
- Protocol-criteria-onduidelijkheden (welke C-criterium-formulering bleek ambigu?)
- Werkverdeling-momenten waar Tech-autonomie of escalatie aan masterchat-discussie waard zijn
- Cluster-discipline-toepassings-ervaringen
- D4.1-pre-stap-praktijk (hoe lang duurt disclaimer-detectie per bron?)

Markeren voortdurend, niet alleen achteraf. Voorkomt vergeten.

---

## §11. Sign-off-log

Vaststelling pending bij T2-scoping-sessie. Lege tabel voor toekomstig invullen.

| # | Beslis-punt | Vastgesteld bij |
|---|---|---|
| 1 | T2-cluster-keuze (bv. overige 121 ctrl:↔compl: of andere) | T2-scoping |
| 2 | Sample-grootte (5 of groter bij groter cluster) | T2-scoping |
| 3 | D4.1-pre-stap-tijdsraming | T2-scoping |
| 4 | NEN-werkverdeling-precieze-grenzen | T2-scoping |
| 5 | Sign-off Steven op v1.1 als operationeel protocol | T2-scoping |

---

## §12. Wat dit protocol NIET doet

- Beoordeelt geen individuele paren — dat is Tech-werk per sprint
- Bepaalt geen ontologie-patch — dat volgt uit beoordeling
- Wijzigt geen D-decisions — D4 + D4.1 zijn autoritatief; dit protocol opereert binnen D4 + D4.1
- Adresseert geen wijziging in andere SKOS-vocabulaire-keuzes (bv. SKOS-axioma-set-handling; H41-kandidaat T1)
- Adresseert geen retroactieve audit van 18 resterende `exactMatch`-mappings — T2-overweging
- Vervangt v1.0 niet — v1.0 blijft beschikbaar voor historische referentie en T1-vergelijking

---

## §13. Wijzigingen t.o.v. v1.0 — overzicht

| # | Wijziging | Bron-T1-leerpunt of D-decision |
|---|---|---|
| 1 | D4.1-vooraf-check als nieuwe stap vóór C1-C4 | D4.1 (27-05-2026) |
| 2 | C2-cardinaliteit binnen bredere mapping-cluster (was: binnen N-set) | T1 §8 leerpunt 3 |
| 3 | Evidence-niveau-1-pre-stap als standaard `sources/`-doorzoek | T1 §4.2 aanbeveling 3 |
| 4 | Pre-pilot-verwachting verwijderd uit §6 | T1 §8 leerpunt 2 (alt) |
| 5 | Tech-autonomie voor NEN-toetsing via lokale bron-toegang | T1 §8 leerpunt 4 + Steven-koers-correctie 27-05-2026 |
| 6 | §7 Werkverdeling Tech↔Masterchat als expliciete sectie | T1 §8 leerpunt 4 |
| 7 | §8 Discipline licentie-bronnen — parafrase-regels + Protocol 14-uitbreiding | T1 + Steven-koers-correctie 27-05-2026 |
| 8 | §9 Diff-applier-discipline — Tech levert werkbare applier | T1 §8 leerpunt 5 |
| 9 | Cluster-discipline expliciet verplicht (was: aanbeveling) | T1 §8 leerpunt 9 |
| 10 | Twee-zijdige edge-case-analyse-format als verplicht escalatie-format | T1 §8 leerpunt 8 |

---

*Einde protocol-draft v1.1. Bij vaststelling: protocol gaat naar Tech voor T2-uitvoering. Tot dan: v1.0 blijft autoritatief voor historische referentie.*
