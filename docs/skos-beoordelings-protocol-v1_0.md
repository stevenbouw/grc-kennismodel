# SKOS-beoordelings-protocol v1.0

**Voor:** Tech-subagent in Claude Code — Stap 3 (pilot-sample) en Stap 4 (resterende paren)
**Auteur:** Masterchat
**Datum:** 26 mei 2026
**Status:** FINAL — sign-off Steven 26 mei 2026
**Aanleiding:** T1-sprint Stap 2, op basis van inventarisatie-rapport `t1-presprint-inventarisatie-v4_6_0.md`
**Scope:** SKOS-exactMatch-beoordelings-criteria + beslis-tabel + evidence-hiërarchie + twijfelgevallen-procedure. Herbruikbaar voor T2/T3 met aanpassingen.

---

## §0. Inventarisatie-bevindingen die het protocol direct vormgeven

De pre-sprint-inventarisatie heeft twee structurele patronen blootgelegd:

1. **Veel-naar-één-clustering:** 24 van 28 paren zitten in mappings waar meerdere `ctrl:`-controls dezelfde `compl:`-target hebben. Verdeling per NIS2-clause:

   | NIS2-clause | # ISO27002-controls | Cardinaliteit |
   |---|---:|---|
   | a (risicoanalyse + beleidsregels) | 1 | 1→1 |
   | b (incidentbehandeling) | 4 | 4→1 |
   | c (continuïteit + back-up) | 3 | 3→1 |
   | d (toeleveringsketen) | 4 | 4→1 |
   | e (verwerving + ontwikkeling) | 5 | 5→1 |
   | f (doeltreffendheid-beoordeling) | 2 | 2→1 |
   | g (cyberhygiëne + opleiding) | 1 | 1→1 |
   | h (cryptografie) | 1 | 1→1 |
   | i (personeel + toegang + activa) | **6** | 6→1 |
   | j (multi-factor auth) | 1 | 1→1 |

   **Implicatie:** SKOS-transitiviteit (skos:S47) impliceert dat alle 6 ISO-controls onder NIS2-clause i óók onderling `exactMatch` zouden moeten zijn — semantisch onhoudbaar (Screening ≠ Toegangsbeveiliging). Het cardinaliteit-criterium krijgt prominente positie in dit protocol.

2. **Bredere mapping-strategie reeds aanwezig:** het ctrl:↔compl:-cluster bevat al 32 closeMatch, 33+27 relatedMatch, 25+2 broadMatch. **Herclassificatie naar deze types is consistent met bestaand model-patroon**, geen breukwijziging.

**Verwachte uitkomst-range** (voorzichtig geformuleerd, niet pre-judging):

- 4 paren in 1→1-clusters (a, g, h, j) — mogelijk behoud `exactMatch` als overige criteria gelden
- 24 paren in veel→1-clusters — mogelijk `broadMatch` (NIS2-clause is breder dan individuele ISO-control)

**Belangrijk:** dit is verwachting, geen pre-decisie. Stap 3 en 4 moeten elk paar individueel toetsen volgens onderstaande criteria.

---

## §1. Doel van het protocol

Voor elk SKOS-`exactMatch`-paar consistent en repliceerbaar beoordelen of:

- **Behoud** als `exactMatch` (D4-conformiteit aangetoond)
- **Herclassificeer** naar `closeMatch`, `relatedMatch`, `broadMatch` of `narrowMatch` (D4-conformiteit niet aantoonbaar; lichtere relatie wel verdedigbaar)
- **Verwijder** (geen verdedigbare semantische relatie — zeldzaam verwacht)

Daarnaast: vastleggen welke twijfelgevallen naar Masterchat escaleren.

---

## §2. D4-`exactMatch`-criteria — vier-set

Een `skos:exactMatch`-relatie tussen A en B is verdedigbaar wanneer **alle vier** criteria gelden. Bij failure op één of meer criteria → herclassificatie volgens beslis-tabel §3.

### Criterium 1 — Definitionele overlap

A en B hebben identieke scope volgens hun bron-definities.

**Praktische test:**

- Zou A de volledige reikwijdte van B invullen? (A dekt alle aspecten van B)
- Zou B de volledige reikwijdte van A invullen? (B dekt alle aspecten van A)
- Beide ja → C1 gehaald

**Faalmodus voor ISO27002↔NIS2:** ISO-control adresseert één specifieke maatregel; NIS2-clause omvat meestal een **bredere thematische verplichting**. Bijvoorbeeld:

- ISO27002_5_24 ("Plannen en voorbereiden van incidentbeheer") dekt slechts één aspect van NIS2_Art21_b ("Incidentbehandeling" — inclusief detectie, respons, herstel, evaluatie)
- → C1 faalt: A is enger dan B

### Criterium 2 — Cardinaliteit (cluster-test)

Geen veel-op-één of één-op-veel relaties binnen de mapping-set.

**Praktische test:**

- Zijn er andere `ctrl:`-paren in de 28-set met dezelfde `compl:`-target? Tel ze.
- Zijn er andere `compl:`-paren in de 28-set met dezelfde `ctrl:`-source? Tel ze.
- Beide tellingen ≤1 → C2 gehaald

**Voor de huidige 28 paren:** cardinaliteit-data staat in §0 hierboven. Pre-bepalende vraag bij beoordeling:

- "Is dit paar onderdeel van een 1→1-cluster (a/g/h/j) of een veel→1-cluster (b/c/d/e/f/i)?"

Bij veel→1-cluster → C2 faalt automatisch.

**Belangrijke nuance:** een 1→1-cardinaliteit binnen deze 28 paren betekent **niet** automatisch dat C2 gehaald wordt. Check ook of er buiten de 28 exactMatch-paren (in de 121 andere ctrl:↔compl:-mappings van Vraag B) mappings bestaan met dezelfde subject of object. Als ctrl:5_01 ook `closeMatch` heeft met compl:NIS2_Art21_a via een ander pad, dan is het 1→1-patroon brozer dan op het eerste oog lijkt. Tech: voer deze brede-cluster-check uit per paar.

### Criterium 3 — Inclusie-richting (bilaterale containment)

A ⊆ B EN B ⊆ A volgens definitie-content.

**Praktische test (volgt logisch uit C1 mits scherp uitgewerkt):**

- Is alles wat ISO-control vereist ook NIS2-clause-vereiste? (A ⊆ B)
- Is alles wat NIS2-clause vereist ook ISO-control-vereiste? (B ⊆ A)
- Beide ja → C3 gehaald

**Faalmodus:** zelfde als C1. Vaakst: A ⊆ B geldt wel (ISO-control is subset van NIS2-clause), maar B ⊆ A geldt niet (NIS2-clause vereist méér dan deze ene ISO-control). → herclassificatie naar `broadMatch` (B is breder).

**C1 vs C3 — verschil:** C1 toetst definitionele scope; C3 toetst formele subset-relatie. In de praktijk leveren ze meestal dezelfde uitkomst, maar C3 dwingt expliciete richting (broadMatch vs narrowMatch).

### Criterium 4 — Bron-bewijs

Een autoritatieve bron ondersteunt "exact" expliciet.

**Evidence-hiërarchie (sterk → zwak):**

| Niveau | Bron-type | Voorbeeld |
|---|---|---|
| 1 | Expliciete mapping in autoritatief mapping-document | ISO 27001:2022 Annex F (ISO-NIST-mapping); officiële BZK NIS2↔ISO-mapping; CBW-Excel |
| 2 | Norm-tekst identiek aan beide kanten | Zelden voor cross-norm; geldt vaker binnen één framework |
| 3 | Definitie-overlap via rdfs:comment of bron-tekst | rdfs:comment-vergelijking in module; norm-tekst-vergelijking in ISO27002:2022-PDF en NIS2-richtlijn |
| 4 | Onderwerp-titel-overlap (zwakste, vaak misleidend) | rdfs:label@nl-vergelijking |

**Voor de huidige 28 paren:** de inventarisatie meldt dat geen subject `rdfs:comment` heeft; de attribuering op module-niveau in `m10-nis2-ext.ttl` verwijst naar NIS2-richtlijn 2022/2555 maar niet naar specifieke per-mapping-bronnen. Verwachte evidence-niveaus dus voornamelijk **3 of 4**, mogelijk **1** als ISO 27002:2022 Annex A.7 of vergelijkbaar expliciete mapping-documenten beschikbaar zijn.

**Tech-actie bij Stap 3 pilot:** verifieer of ISO 27002:2022 een Annex bevat met NIS2-mapping (Annex A of B — momenteel onbekend uit inventarisatie); of er BZK-publicaties over NIS2↔ISO27002:2022 zijn. Dit bepaalt of evidence-niveau 1 haalbaar is voor enige paren. Resultaat van dit onderzoek **vóór** per-paar-beoordeling rapporteren (max ~15 min Tech-werk).

**C4 gehaald** wanneer evidence-niveau ≤ 2. Bij niveau 3 of 4 → twijfelgevallen-lijst.

---

## §3. Beslis-tabel bij criterium-failure

Onderstaande tabel geeft per failure-modus de voorgestelde herclassificatie. Bij meervoudige failure: het strengste failure-criterium leidt.

| Failure | Aard | Herclassificatie |
|---|---|---|
| C1: A dekt deel van B (A enger) | Definitionele subset zonder bilaterale gelijkheid | `A skos:broadMatch B` (B is breder dan A) |
| C1: A en B overlappen partieel maar geen subset-relatie | Geen heldere richting; thematische verwantschap | `A skos:closeMatch B` |
| C1: zwakke definitionele overlap, alleen thematische verwantschap | Onderwerp-domein hetzelfde, scope-overlap minimaal | `A skos:relatedMatch B` |
| C2: meerdere A's mappen naar één B | Eén-richting veel→1 | Per A: `A skos:broadMatch B` |
| C2: één A mapt naar meerdere B's | Eén-richting 1→veel | Per B: `A skos:narrowMatch B` |
| C3: A is enger dan B (geen bilaterale containment) | Subset-relatie expliciet | `A skos:broadMatch B` (B is breder) |
| C3: A is breder dan B | Subset-relatie expliciet | `A skos:narrowMatch B` |
| C4: evidence-niveau 3 of 4 ÉN C1-C3 niet sluitend | Onvoldoende bron-bewijs voor sterke claim | Naar twijfelgevallen-lijst |
| Alle criteria falen ÉN geen thematische verwantschap | Geen verdedigbare relatie | Verwijderen (zeldzaam) |

**Cluster-discipline (verplicht):** bij C2-failure (cardinaliteit) is herclassificatie **systematisch binnen het cluster**. Alle paren in dezelfde veel→1-cluster krijgen dezelfde behandeling tenzij voor een specifiek paar een individuele uitzondering aantoonbaar is. Voorbeeld: alle 6 paren onder NIS2-clause i krijgen `broadMatch` of allen `exactMatch`-behoud, niet half-half. Voorkomt inconsistente cluster-behandeling.

**Bewijslast voor uitzondering binnen cluster:** Tech moet voor een uitzondering expliciet motiveren waarom dat individuele paar afwijkt van het cluster-patroon (bv. specifieke autoritatieve mapping-bron evidence-niveau 1 die exact ondersteunt). Bij twijfel → twijfelgevallen-lijst.

---

## §4. Twijfelgevallen-procedure

Een paar gaat naar twijfelgevallen-lijst (escalatie naar Masterchat) wanneer:

- Evidence-niveau 3 of 4 (geen autoritatieve mapping-bron) **én** C1/C3-toets niet sluitend
- Cardinaliteit-twijfel: paar lijkt 1→1 binnen 28-set maar heeft buiten-set-mappings die patroon ondergraven
- Cross-norm-interpretatie nodig: NIS2-clause-tekst is op meerdere manieren te lezen (a-clauses zijn vaak meerlagig)
- Tech-confidence "laag" op één of meer criteria
- Individuele uitzondering claim binnen cluster (zie §3 cluster-discipline)

**Format voor twijfelgevallen-tabel:**

| Paar-ID | Subject | Object | C1 | C2 | C3 | C4-niveau | Tech-voorstel | Confidence | Vraag aan Masterchat |
|---|---|---|---|---|---|---|---|---|---|

**Procedure:**

1. Tech verzamelt twijfelgevallen tijdens Stap 4
2. Aparte tabel in eindrapport
3. Masterchat-sessie met Steven doorloopt lijst, beslist per paar
4. Beslissing terug naar Tech voor eventuele patch-opname

---

## §5. Output-formaat per paar (verplicht)

Conform sprint-instructie §4 Stap 3 + 4, met aanvullingen op basis van inventarisatie:

| Veld | Inhoud |
|---|---|
| Paar-ID | T1-001 t/m T1-028 |
| Subject IRI | `ctrl:ISO27002_X_YY` |
| Object IRI | `compl:NIS2_Art21_X` |
| Cluster-context | NIS2-clause + cluster-grootte (bv. "i (6→1)") |
| Criterium 1 (definitioneel) | ✓ / ✗ + 1-2 zin reden |
| Criterium 2 (cardinaliteit) | ✓ / ✗ + cluster-grootte + buiten-set-check |
| Criterium 3 (inclusie) | ✓ / ✗ + richting indien failure (A⊆B / B⊆A / partial) |
| Criterium 4 (bron) | niveau 1-4 + verwijzing naar bron-document of -sectie |
| Voorstel | behoud-exactMatch / herclass-broadMatch / herclass-closeMatch / herclass-relatedMatch / herclass-narrowMatch / verwijder / twijfel-escaleer |
| Confidence | hoog / middel / laag |
| Patch-vereist | ja / nee (= behoud → nee) |

**Cluster-discipline-regel (§3) is verplicht** bij voorstel-bepaling: een individueel paar dat afwijkt van zijn cluster-behandeling moet expliciet gemotiveerd worden of naar twijfelgevallen.

---

## §6. Sample-keuze voor Stap 3 (pilot van 5)

Aangezien er één bestand-bron + één module-combinatie is, ligt spreiding niet over modules maar over **cluster-patronen**. Vastgelegde 5 paren:

| Pilot-# | Paar-ID | Subject | Object | Cluster | Reden van keuze |
|---|---|---|---|---|---|
| 1 | T1-001 | ctrl:ISO27002_5_01 | compl:NIS2_Art21_a | a (1→1) | Test 1→1 — beleidsregels |
| 2 | T1-020 | ctrl:ISO27002_6_03 | compl:NIS2_Art21_g | g (1→1) | Test 1→1 — opleiding (smal NIS2-clause-onderwerp) |
| 3 | T1-010 | ctrl:ISO27002_5_24 | compl:NIS2_Art21_b | b (4→1) | Test 4→1 — incidentbehandeling, eerste van cluster |
| 4 | T1-002 | ctrl:ISO27002_5_09 | compl:NIS2_Art21_i | i (6→1) | Test 6→1 — grootste cluster, breedste NIS2-clause |
| 5 | T1-024 | ctrl:ISO27002_8_25 | compl:NIS2_Art21_e | e (5→1) | Test 5→1 — verwerving/ontwikkeling, hoofdstuk 8 ISO27002 |

**Spreidings-eigenschappen:**

- Twee 1→1-paren (verwacht behoud)
- Drie veel→1-paren uit drie verschillende clusters (b, e, i)
- ISO27002-hoofdstukken 5, 6 én 8 vertegenwoordigd
- NIS2-clause-typen "smal/eenduidig" (g, a) én "breed/multilagig" (i, e, b) beide vertegenwoordigd

**Verwachting (voor sanity-check, geen pre-judging):** als protocol werkt, leveren pilot-paren #1 en #2 behoud-voorstellen, paren #3, #4, #5 broadMatch-voorstellen.

**Stop-condities pilot (overschrijft sprint-instructie §4 Stap 3):**

De generieke "≥3 van 5 herclassificatie-voorstellen → stop"-regel uit de sprint-instructie houdt geen rekening met de cluster-cardinaliteit-bevinding. Aangezien de inventarisatie al voorspelt dat 3 van 5 pilot-paren herclassificatie krijgen, zou die regel de pilot onterecht stoppen op de **verwachte** uitkomst.

**Vervangen door deze drie stop-condities:**

1. **Onverwachte uitkomst-richting:** behoud-voorstel op #3, #4 of #5 (de veel→1-paren) — of — herclassificatie-voorstel op #1 of #2 (de 1→1-paren). Eén van deze patronen betekent dat het protocol niet beschrijft wat in de data zit; pauze met analyse-rapport naar Masterchat.
2. **Confidence "laag" op ≥3 van 5:** protocol-criteria zijn niet eenduidig toepasbaar; bijstelling nodig vóór doorgaan naar Stap 4.
3. **Evidence-niveau 4 op ≥3 van 5:** bron-discipline-probleem — autoritatieve bronnen ontbreken zelfs voor pilot-cases; mogelijk evidence-pre-onderzoek (§2 C4) eerst structureler aanpakken.

**Reden voor vervanging:** zonder aanpassing zou pilot zichzelf stoppen op verwachte cardinaliteit-uitkomst. Inhoudelijke stop-conditie (onverwacht patroon) is informatiever dan numerieke drempel.

---

## §7. Werkflow-leerpunten markeren (voor T1 §8)

Bij toepassen van dit protocol: noteer in T1-eindrapport §8 onder andere:

- **SKOS-symmetrie-afwezigheid** (Vraag B liet 0 inverse zien): owlrl-package laadt geen SKOS-axiomas, dus `skos:exactMatch is owl:SymmetricProperty` (skos:S46) wordt niet geïnferreerd. **Status:** T1-leerpunt, niet als nieuw H-item nu — focus blijft H36. Toekomstige overweging.
- **SHACL-blinde vlek** op deze 28 paren (Vraag D): geen shape valideert. Reeds H39-relevant.
- Tooling-gaten uit Tech-inventarisatie-rapport (5 punten) overnemen.
- Evidence-niveau-onderzoeks-uitkomst (§2 C4 Tech-actie): wat is beschikbaar, wat ontbreekt, welke autoritatieve bronnen had het project willen hebben.

---

## §8. Sign-off-log

Vastgestelde keuzes door Steven op 26 mei 2026 vóór doorzetten naar Tech Stap 3:

| # | Beslis-punt | Vastgesteld |
|---|---|---|
| 1 | Sample-keuze pilot-5 (§6) | T1-001, T1-020, T1-010, T1-002, T1-024 |
| 2 | Pilot-stop-conditie aanpassen (§6) | Vervang generieke ≥3/5 door drie inhoudelijke stop-condities |
| 3 | Cluster-discipline binnen C2-failure (§3, §5) | Verplicht — systematische cluster-behandeling, individuele uitzondering vereist expliciete motivering of escalatie naar twijfelgevallen |
| 4 | SKOS-symmetrie-afwezigheid (§7) | Markeren als T1-werkflow-leerpunt in eindrapport §8 — geen nieuw H-item nu |
| 5 | Evidence-niveau-onderzoek (§2 C4) | Tech voert ~15 min onderzoek uit als pre-stap binnen Stap 3 vóór per-paar-beoordeling |

---

## §9. Wat dit protocol NIET doet

- Beoordeelt geen individuele paren — dat is Tech-werk in Stap 3/4
- Bepaalt geen ontologie-patch — dat volgt uit beoordeling
- Wijzigt geen D-decisions — D4 blijft autoritatief; dit protocol opereert binnen D4
- Adresseert geen andere SKOS-predicate-evaluaties (closeMatch, relatedMatch) — alleen exactMatch — restant valt onder T2/T3 of aparte sprint
- Adresseert geen SKOS-axioma-set-vraag (skos:S46 symmetrie) — alleen markering voor T1-leerpunten

---

*Einde protocol v1.0. Klaar voor Tech Stap 3 (pilot van 5).*
