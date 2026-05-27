# Sprint-protocollen — Werkwijze voor subagents in Claude Code

**Versie:** 1.3
**Datum:** 27 mei 2026
**Doelpubliek:** Tech-subagent, Brein-subagent, Dashboard-subagent
**Verhouding tot projectinstructie:** dit document is de **porteerbare uitvoerings-gerichte versie** van projectinstructie v1.9 §"Sprint-protocollen". De projectinstructie blijft autoritatief; dit document is praktisch werkmateriaal voor subagent-context. Bij conflict: projectinstructie prevaleert.

---

## Inleiding

Twaalf protocollen + één gedragsregel, ontstaan uit concrete sprint-leerpunten over meerdere releases (v4.4.0 t/m v4.6.0). Alle protocollen delen één onderliggend principe:

> **Discipline boven snelheid.** Pre-sprint-inventarisatie, bron-verificatie en raming-discipline kosten tijd vooraf, maar voorkomen scope-pauzes en verkeerde besluiten gedurende uitvoering.

Sprint-protocollen zijn **niet-onderhandelbaar** voor alle subagents (zie CLAUDE.md §"Werk-conventies"). Bij twijfel of een protocol van toepassing is: escaleer naar Steven via scope-pauze-route (zie §15).

---

## Overzicht — 17 protocollen + 1 gedragsregel

| # | Protocol | Primair-uitvoerend | Geformaliseerd in | Status |
|---|---|---|---|---|
| 1 | Protocol B — Pre-sprint-inventarisatie | Tech | v1.7 | Verplicht |
| 2 | Protocol B-multi-module-discipline | Tech | v1.9 | Verplicht |
| 3 | Protocol C — Schema-meta-rapport | Tech | v1.7 | Aanbevolen |
| 4 | Bron-verificatie vóór TBox-declaratie | Tech | v1.7 | Verplicht |
| 5 | Bron-verificatie vóór raming-opstelling | Tech | v1.8 | Verplicht |
| 6 | Ramings-baseline rdf:type-dubbele-telling | Tech | v1.9 | Verplicht |
| 7 | Bron-bereikbaarheid in uitvoerings-omgeving | Tech | v1.8 | Verplicht |
| 8 | Precedent-discipline bij nieuw framework-cluster | Tech | v1.8 | Verplicht |
| 9 | Raming-discipline bij aggregatie-mappings | Tech | v1.8 | Verplicht |
| 10 | Patch-rapport §9 verplicht | Tech | v1.7 | Verplicht |
| 11 | Brain-vault-update verplicht na minor-release | Brein | v1.8 | Verplicht |
| 12 | Instructie-consistentie code-block vs toelichting | (Masterchat-discipline) | v1.9 | Verplicht |
| 13 | Bron-typo-beleid patroon-criterium | Tech | v1.9 | Verplicht |
| 14 | Pre-push disclosure-check | Alle (subagent + Steven) | iteratie 12 | Verplicht |
| **15** | **Tech levert werkbare applier (niet alleen specificatie)** | **Tech** | **iteratie 13 (T1 §8 leerpunt 5)** | **Verplicht** |
| **16** | **Lokatie verificatie-scripts expliciet in patch-rapport** | **Tech** | **iteratie 13 (T1 §8 leerpunt 6)** | **Verplicht** |
| **17** | **NEN-werkverdeling met Tech-autonomie** | **Tech (autonoom); Masterchat alleen bij edge-cases** | **iteratie 13 (T1 §8 leerpunt 4); herzien 27 mei 2026** | **Verplicht** |
| **GR** | Property-semantiek-discipline | Alle (gedragsregel) | v1.9 | Verplicht |

---

## 1. Protocol B — Pre-sprint-inventarisatie

**Trigger:** Elke sprint die nieuwe klassen, properties of structurele wijzigingen introduceert.

**Subagent:** Tech.

**Procedure:**

1. Lees sprint-instructie van masterchat
2. Identificeer "Stap 1" of vergelijkbare inventarisatie-sectie
3. Voer **uitsluitend read-only** inventarisatie uit op model — geen wijzigingen
4. Beantwoord alle inventarisatie-vragen uit instructie
5. Schrijf inventarisatie-rapport in `output/inventarisatie-<sprintversie>-precheck.md`
6. Lever rapport via Steven aan masterchat
7. **Wacht op masterchat-besluit** vóór Stap 2 (architectuur of TBox-werk)

**Output:** Inventarisatie-rapport met signalen + scope-implicaties.

**Escalatie:** Bij onverwachte vondsten met scope-impact (bv. ontbrekende referentie-individual, naam-conflict, dubbele declaratie): scope-pauze met Optie A/B/C-rapport naar masterchat.

**Toepassings-bewijs:** v4.4.0 (Route 5 herdefinitie), v4.5.0 (csf2.xlsx Reference Tool), v4.6.0 (biz vs isms maturity-cluster).

---

## 2. Protocol B-multi-module-discipline (v1.9)

**Trigger:** Pre-sprint-inventarisatie waarbij gevraagd wordt of een entity bestaat in specifieke module.

**Subagent:** Tech.

**Procedure:**

1. Bij vraag "bestaat X in module Y": altijd uitbreiden naar "bestaat X model-breed?"
2. Voer `grep` uit over **alle 22 .ttl-modules**, niet alleen genoemde module
3. Rapporteer per locatie waar X gevonden wordt (module + context)
4. Documenteer expliciet als X niet model-breed gevonden wordt

**Output:** Multi-module-zoekresultaat in inventarisatie-rapport.

**Escalatie:** Bij entity gevonden in onverwachte module met architectuur-implicatie: scope-pauze.

**Achtergrond:** v4.6.0 pre-sprint vraag D claimde "fw:toetst 0 uses" terwijl werkelijk 1 use bestond in m15 (fw:ENSIA fw:toetst fw:BIO_2_0). Single-module-zoek leidde tot scope-pauze in Stap 5.

---

## 3. Protocol C — Schema-meta-rapport (aanbevolen)

**Trigger:** Bij elke minor-release: overwegen herziening van TBox-overzichtskaart.

**Subagent:** Tech.

**Procedure:**

1. Genereer TBox-overzichtskaart na release-afronding
2. Vergelijk met vorige versie indien beschikbaar
3. Indien substantiële wijziging: nieuwe versie van schema-meta-rapport (~697 regels voor v4.3.3 als referentie-grootte)
4. Niet verplicht — afhankelijk van wijziging-omvang

**Output:** Geactualiseerd schema-meta-rapport in `output/`.

**Escalatie:** Niet van toepassing.

---

## 4. Bron-verificatie vóór TBox-declaratie

**Trigger:** Voorstel om nieuwe property-naam of klasse-naam te declareren die naar externe bron verwijst (bv. `ext:hasENISAGuidance`, `csf:Function`).

**Subagent:** Tech.

**Procedure:**

1. Lees relevante bron-tekst (PDF, Excel, web-source) opnieuw vóór TBox-edit
2. Verifieer dat naam beschrijft wat het werkelijk is — niet alleen "domain/range klopt"
3. **Grep door alle bestaande modules** om parallelle properties voor identiek doel te voorkomen
4. Documenteer naam-keuze met bron-citaat in TBox-declaratie als `rdfs:comment`

**Output:** Geverifieerde naam + bron-citaat.

**Escalatie:** Bij twijfel over naam-semantiek: scope-pauze met voorstel A/B/C aan masterchat.

**Toepassings-bewijs:** v4.4.0 `ext:hasENISAGuidance` (bleek semantisch onjuist — vervangen door `ext:hasUVInterpretation`); v4.5.0 `ext:belongsToFramework` → `ext:isComponentOf` (precedent uit m17 gevonden via grep).

---

## 5. Bron-verificatie vóór raming-opstelling

**Trigger:** Sprint-instructie vraagt om triple-impact-raming voor nieuwe ABox-werk.

**Subagent:** Tech.

**Procedure:**

1. Tel **unieke (subject, predicate, object)-paren** als doelmetric — niet bron-rijen of grof-geschatte gemiddelden
2. Leid raming bottom-up af uit pre-sprint-cijfers
3. Voor aggregatie-mappings: zie Protocol 9 (dedup-effect)
4. Documenteer raming-methodiek in inventarisatie-rapport
5. Pauze-grens: **>30% boven raming** zonder verklaarbare oorzaak = scope-pauze

**Output:** Bottom-up raming met methodiek-toelichting.

**Escalatie:** Bij werkelijke triple-Δ >30% boven raming: scope-pauze + verklaring vereist.

**Toepassings-bewijs:** v4.5.0 cumulatief binnen prognose dankzij cross-bron-overlap-compensatie (S5∩S6 = 105 mappings vooraf herkend).

---

## 6. Ramings-baseline rdf:type-dubbele-telling (v1.9)

**Trigger:** Triple-impact-raming voor typed-individual-ABox-creatie.

**Subagent:** Tech.

**Procedure:**

Rdflib telt `rdf:type`-triples dubbel: class-membership + `owl:NamedIndividual`-membership. Voor toekomstige ramingen op typed-individual-ABox-creatie geldt:

| Element | Triples per individual |
|---|---:|
| Base (verplicht) | 5 |
| → `rdf:type X` (telt dubbel: X + owl:NamedIndividual) | 2 |
| → `rdfs:label`@nl + @en | 2 |
| → `ext:sourceAttribution` | 1 |
| **Extra properties** (per stuk) | +1 |

Voorbeeld v4.6.0: LevelDescription = 5 base + 3 extra (forCapability + atMaturityLevel + comment@nl) = **8 triples per individual**.

**Output:** Raming gebruikt 5/8-baseline expliciet.

**Escalatie:** Niet van toepassing — preventie tegen onder-raming.

**Toepassings-bewijs:** v4.6.0 Stap 4 was +44% boven instructie-raming (~900-1.000 → 1.088 werkelijk). Volledig verklaarbaar via dubbele-telling. Geen scope-pauze nodig.

---

## 7. Bron-bereikbaarheid in uitvoerings-omgeving

**Trigger:** Sprint-instructie verwijst naar externe bron (URL, web-locatie).

**Subagent:** Tech.

**Procedure:**

1. **Vóór Stap 1**: verifieer bereikbaarheid van bron in subagent-omgeving
2. Tech-subagent bash heeft beperkte allowed_domains (zie netwerkconfig)
3. Bij niet-bereikbaarheid: scope-pauze direct — wacht op alternatief van Steven (lokale upload via Steven, PK-fetch, etc.)
4. Niet aannemen dat URL werkt op basis van instructie-tekst

**Output:** Bereikbaarheids-bevestiging of scope-pauze.

**Escalatie:** Bij niet-bereikbaarheid: scope-pauze met verzoek tot Steven om bron-bestand lokaal beschikbaar te maken in `sources/`.

**Toepassings-bewijs:** v4.5.0 Stap 1-pauze door `csrc.nist.gov` 403-error; opgelost via masterchat-uploads naar PK door Steven.

---

## 8. Precedent-discipline bij nieuw framework-cluster

**Trigger:** Introductie van nieuw framework-cluster (bv. M21 NIST CSF 2.0, M22 hypothetisch).

**Subagent:** Tech.

**Procedure:**

Vóór TBox-werk voor nieuw cluster, voer **vier-vragen-checklist** uit door eerder framework-clusters te raadplegen:

1. Welke property voor **component → framework** relatie? (bv. `ext:isComponentOf`)
2. Welke property voor **parent-child binnen framework**? (bv. `csf:partOfFunction`, `csf:partOfCategory`)
3. Welke **SourceAttribution-aanpak**? (per-individu vs. blok-comment)
4. Welke **SKOS-mapping-conventies**? (`closeMatch` default, `relatedMatch` voor partial, etc.)

Documenteer keuzes in inventarisatie-rapport met verwijzing naar precedent.

**Output:** Precedent-document met vier antwoorden + bron-cluster.

**Escalatie:** Bij afwijking van precedent: scope-pauze met onderbouwing.

**Toepassings-bewijs:** v4.5.0 m21 gebruikte `ext:isComponentOf`-precedent uit m17 (COSO/COBIT); v4.6.0 `fw:NIST_CSF_2_0`-template voor `fw:ENSIA`.

---

## 9. Raming-discipline bij aggregatie-mappings

**Trigger:** Mapping-creatie waarbij subject-grain grover is dan source-grain (bv. Function-niveau mappings uit Subcategory-bron).

**Subagent:** Tech.

**Procedure:**

1. **Verwacht dedup-effect** — meerdere bron-rijen kunnen naar één target-triple compileren
2. Tel **unieke RDF-triples**, niet bron-rijen
3. Raming-input bottom-up:
   - Bron-rijen: N
   - Verwachte unique-ratio: bv. 0,60-0,80 (afhankelijk van overlap-patroon)
   - Verwacht aantal RDF-triples: N × ratio
4. Bij twijfel: doe **sample-eerst** (~10 bron-rijen) om dedup-ratio te schatten

**Output:** Raming met unique-ratio-expliciete toelichting.

**Escalatie:** Bij dedup-ratio buiten verwachting (>20% afwijking): scope-pauze met heroverweging.

**Toepassings-bewijs:** v4.4.0 sheet 9 (290 bron-rijen → 183 triples = 37% dedup-reductie); v4.5.0 Stap 6 cross-bron-overlap (105 mappings vooraf herkend uit S5∩S6).

---

## 10. Patch-rapport §9 verplicht — geparkeerde-items-status-update

**Trigger:** Elke release-afronding (minor + patch).

**Subagent:** Tech.

**Procedure:**

Patch-rapport bevat een §9 met status-update van **alle geparkeerde H-items + scope-besluiten**:

1. Lijst alle H-items in brain__architecture__H-register.md
2. Per H-item: status onveranderd / nieuw / status-gewijzigd
3. Lijst alle scope-besluiten uit eerdere sprints
4. Per scope-besluit: nog van toepassing / herzien / ingehaald

**Output:** §9 in patch-rapport, opgenomen vóór §10 (D-conformiteit).

**Escalatie:** Bij ontdekking dat H-item ingehaald is door sprint-werk: scope-pauze + masterchat-melding voor H-update.

---

## 11. Brain-vault-update verplicht na minor-release

**Trigger:** Elke minor-release-afronding (v4.X.0; niet bij patch-releases v4.X.Y tenzij masterchat anders aangeeft).

**Subagent:** Brein.

**Procedure:**

1. **Input verzamelen:**
   - Patch-rapport van afgesloten sprint
   - Nieuwe projectinstructie-versie (indien opgesteld)
   - Eventuele scope-besluiten + heads-up-momenten

2. **Autonoom bepalen** welke brain-bestanden geraakt worden:
   - Nieuwe sprint-file (verplicht)
   - Sprint-register (verplicht append)
   - Module-bestanden (per module-wijziging)
   - Concept-bestanden (bij nieuw concept)
   - D-bestanden (bij D-verfijning)
   - H-bestanden (bij nieuw of gewijzigd H-item)
   - Source-bestanden (bij nieuwe bron of bron-update)
   - Workflow-bestanden (bij nieuw protocol)
   - Index (verplicht update)
   - Log (verplicht append, nieuwste bovenaan)

3. **Werkwijze in 1-2 batches:**
   - Batch 1: kern (sprint-file + register-updates + log + index)
   - Batch 2 (optioneel): detail (modules + sources + concepts)

4. **Cross-referentie-coherentie bewaken**:
   - Wikilinks tussen geraakte bestanden moeten kloppen
   - Per-folder-registers consistent met individuele bestanden
   - Geen orphan-bestanden

5. **Output**: bijgewerkte brain-vault + Brein-eindrapport (welke bestanden bijgewerkt, eventuele leerpunten).

**Escalatie:**
- Bij conflict in patch-rapport vs. eerdere brain-content: scope-pauze
- Bij twijfel over brain-architectuur-wijziging: scope-pauze (geen architectuur-besluiten autonoom)

**Activeringsmoment:** Standaard na opstellen nieuwe projectinstructie-versie. Uitzonderingen mogelijk bij tussentijdse correcties.

**Toepassings-bewijs:** v4.5.0 → v1.8 cyclus (uitzondering, parallel); v4.6.0 → v1.9 cyclus = eerste reguliere cyclus (iteratie 11).

---

## 12. Instructie-consistentie code-block versus toelichting (v1.9)

**Trigger:** Sprint-instructie-uitvoering waarbij code-block en omringende toelichting tegenstrijdig lijken.

**Subagent:** Tech.

**Procedure:**

1. Bij conflict tussen code-block en toelichtende tekst: **toelichting prevaleert**
2. Documenteer waargenomen conflict in tussenrapport
3. Vraag masterchat-bevestiging via scope-pauze
4. Niet zelf de "juiste" interpretatie kiezen

**Output:** Conflict-melding aan masterchat met beide interpretaties.

**Escalatie:** Verplicht — masterchat moet expliciet bevestigen welke interpretatie geldt.

**Toepassings-bewijs:** v4.6.0 §6.3 toonde 2 `fw:toetst`-triples in code-block terwijl toelichting "ISO is referentieel" zei. Scope-pauze in Stap 5; masterchat-correctie: toelichting leidend (C2 — geen 2e fw:toetst).

**Implicatie voor masterchat-discipline:** sprint-instructies moeten code-block en toelichting consistent maken vóór uitlevering aan tech-subagent. Dit is **masterchat-verantwoordelijkheid**, tech-subagent meldt het conflict.

---

## 13. Bron-typo-beleid patroon-criterium (v1.9)

**Trigger:** Bron-tekst (Excel-sheet, PDF-extractie) bevat typo's die in model worden opgenomen.

**Subagent:** Tech.

**Procedure:**

Twee categorieën typo's, verschillende behandeling:

| Categorie | Voorbeeld | Behandeling |
|---|---|---|
| **Typo in referentie-targets** | ISO-clausule-naam met spelfout die als skos:mapping-target staat | **Niet corrigeren** — bron-getrouwheid; mapping niet leggen (G1: "bij twijfel niet leggen") |
| **Typo in nieuwe-individu rdfs:label** | "Bedrijfscontinuiteit" (mist trema) als capability-label | **Wel corrigeren** in `rdfs:label@nl` — alleen presentatie, geen referentie-integriteit |

Patroon: **bron-getrouwheid op semantisch-kritische velden** (target-IRIs, niveau-beschrijvingen-comments); **correctie alleen op presentatie-velden** (rdfs:label@nl) waar lezing in dashboard belangrijk is.

**Output:** Bij correctie: documentatie in patch-rapport §8 als bron-kwaliteits-observatie. Bron-attribuering blijft naar originele bron.

**Escalatie:** Bij twijfel over categorie-keuze: scope-pauze met voorstel.

**Toepassings-bewijs:** v4.5.0 sheet 8 ISO-typo's (categorie 1: niet gemapped, G1); v4.6.0 sheet 6 4 Cbw-typo's (categorie 2: gecorrigeerd in label, comment behouden).

---

## 14. Pre-push disclosure-check (iteratie 12)

**Trigger:** Vóór `git commit` + push van documenten met chat-historie, subagent-output, of inhoud die ooit door een claude.ai-chat is gegaan.

**Subagent:** Alle (Tech / Brein / Dashboard) — en Steven als finale lezer vóór push.

**Procedure:**

1. Vóór commit van een nieuw document: **scan op confidentieel-categorieën** —
   - Organisatie-naam (NOOIT in repo — altijd "de organisatie" of "Rijksoverheidsorganisatie")
   - Persoonsnamen anders dan Steven Bouwmeester (publieke projecteigenaar)
   - Lokale paden met identificerende inhoud (`/Users/<naam>/`, organisatie-interne shares)
   - IP-adressen, hostnames, internet-domeinen van de organisatie
   - Credentials, API-tokens, PAT's, wachtwoorden
   - E-mail-domeinen van de organisatie
   - TLD's die naar specifieke organisatie verwijzen
2. Scan-aanpak — twee niveaus, afhankelijk van bron:
   - **Subagent-output** (Tech/Brein/Dashboard zelf gegenereerd): grep-vóór-commit verplicht
   - **Documenten uit claude.ai-chats** (handover-rapporten, sprint-instructies met chat-context, sessie-rapporten): MCP-tool `grc-kennismodel:run_secret_scanning` aanroepen indien beschikbaar; anders handmatige grep
3. Bij twijfel: **niet committen** — eerst aan Steven voorleggen
4. Geldt voor alle output-locaties: `output/reports/`, `docs/handovers/`, `docs/instructies/`, `brain/**`, root-bestanden

**Output:** Stille pass = geen vondst, push toegestaan. Bij vondst: redactie of weglating vóór commit.

**Escalatie:** Bij vondst van identificeerbare organisatie-data in al-gepushte content: contact Steven voor `git filter-branch` of vergelijkbare history-rewrite. Niet zelf retroactief proberen op te lossen.

**Reikwijdte:**

- Geldt **vanaf nu** (iteratie 12 polish-mini-sprint, 26 mei 2026); geen retroactieve toepassing op reeds-gepushte handover-rapporten (die zijn geverifieerd schoon)
- Geldt **voor nieuwe** documenten en updates van bestaande documenten
- Niet uitgebreid naar geautomatiseerde pre-commit-hooks of CI-scans — die zijn toekomst-overweging, geen H-item nodig nu

**Toepassings-bewijs:** twee voorbarig-push-incidenten als aanleiding —
- PAT-blunder voorgaande sessie (token kortstondig in commit gezien)
- Handover-rapporten ongetoetst gepusht in Fase 0 (achteraf schoon, maar zonder pre-push-discipline)

Het protocol is preventief — niet alle disclosure-incidenten zijn even ernstig, maar de discipline om vóór elke push expliciet te scannen voorkomt herhaling.

---

## 15. Tech levert werkbare applier (iteratie 13)

**Trigger:** Sprints met ontologie-patches die mutaties in .ttl-modules voorschrijven.

**Subagent:** Tech.

**Procedure:**

Voor sprints met ontologie-patches: Tech-subagent levert standaard zowel een **specificatie** (welke triples wijzigen, welke voorwaarden) als een **werkbare applier** (Python-script, sed-script, of unified-diff-format dat `patch -p0` accepteert). De applier moet vóór levering getest zijn op een tijdelijke gepatchte kopie. Pure-specificatie-only-deliverables creëren overhead voor Steven en risico op verkeerde toepassing.

Concrete eisen:

1. Specificatie (zoals voorheen — lijst van paren + voorwaarden + verwachte counts)
2. **PLUS** werkbare applier:
   - Python-script (`apply_patch_v4_X_Y.py`) met backup + count-verificatie + faal-veilig-exit
   - OF unified-diff-format dat `patch -p0` accepteert
   - OF sed-script met expliciete pre/post-validatie
3. **PLUS** integratie-test: Tech voert applier op tijdelijke kopie van module(s) uit vóór levering, verifieert hash-mutatie en count-effect

**Output:** Werkende applier in patch-rapport-deliverables-tabel met expliciete lokatie (zie Protocol 16).

**Escalatie:** Bij twijfel over applier-vorm: scope-pauze met voorstel A/B/C aan masterchat.

**Toepassings-bewijs:** T1-sprint Stap 6 — Tech leverde alleen diff-bestanden als specificaties (lijst van paren + sed/python-instructie als comments). `patch -p0` faalde met "I can't seem to find a patch in there anywhere." Masterchat moest werkende Python-applier `apply_patch_v4_6_1.py` schrijven. Impact: ~25 min overhead + frustratie-moment. Vermijdbaar via Protocol 15.

---

## 16. Lokatie verificatie-scripts expliciet in patch-rapport (iteratie 13)

**Trigger:** Elke release-afronding (minor + patch) waarbij verificatie-scripts (canonical metrics, SHACL-validatie, file-hashes) deel zijn van deliverables.

**Subagent:** Tech (uitvoerend) + Masterchat (consument).

**Procedure:**

Patch-rapport §9 Deliverables-tabel vermeldt **expliciete lokatie** van alle leverbare scripts en outputs. Masterchat citeert in vervolg-instructies altijd uit deze tabel, niet uit memory. Voorkomt file-not-found-fouten bij verificatie-runs door Steven.

Concrete eisen:

1. Patch-rapport §9 Deliverables-tabel bevat per deliverable:
   - Type (script / output / config)
   - **Expliciete relatieve lokatie** vanaf repo-root (bv. `output/verification/canonical_metrics_v4_6_1.py`)
   - Korte beschrijving (één regel)
2. Masterchat-instructies citeren rechtstreeks uit Deliverables-tabel
3. Bij relocatie van scripts tijdens sprint: tabel bijwerken in patch-rapport vóór finale levering

**Output:** Consistente lokatie-vermelding tussen Tech-output en masterchat-instructies.

**Escalatie:** Bij conflict tussen instructie-lokatie en werkelijke deliverable-lokatie: scope-pauze + correctie van één van beide.

**Toepassings-bewijs:** T1-sprint — masterchat-instructie noemde aanvankelijk `scripts/canonical_metrics_v4_6_1.py`, terwijl Tech de scripts in `output/verification/` had gezet. Twee aparte run-pogingen door Steven met file-not-found-fout. Impact: ~5 min verwarring. Vermijdbaar via Protocol 16.

---

## 17. NEN-werkverdeling met Tech-autonomie (iteratie 13; herzien 27 mei 2026)

*Herzien 27 mei 2026 na koers-correctie lokale NEN-toegang voor Tech.*

Tech-subagent in Claude Code heeft toegang tot lokale NEN-bronnen in `/Users/stevenbouwmeester/grc-sources-licensed/`:

- ISO 27002:2022
- ISO 27001:2022
- ISO 27005:2024
- ISO 31000:2018
- ISO 22301:2019
- ISO 22313:2020

Bij sprints die NEN-restrictieve bronnen vereisen voor inhoudelijke toetsing: **Tech voert volledige beoordeling autonoom uit** via lokale bron-toegang, inclusief NEN-tekst-lezing voor C1 (definitionele overlap), C3 (inclusie-richting), en evidence-niveau-3-onderbouwing. Masterchat-judgement is alleen vereist voor:

- Cross-bron-interpretatie (meerdere bronnen tegenspreken elkaar)
- Bron-tekst die meerduidig is en geen eenduidige lezing toelaat
- C1-C3-toets die ook na NEN-tekst-lezing sluitend ambigu blijft
- Cluster-uitzondering waarvoor bewijslast te zwak is voor Tech-autonomie

**Parafrase-discipline (verplicht):** Tech mag NEN-tekst lezen voor toetsing, maar **mag onder geen beding NEN-tekst-fragmenten verbatim opnemen** in rapport-output, commit-messages, Turtle-files, code-comments, of geautomatiseerde output. Toegestaan: parafrase + clausule-verwijzing (bv. "ISO 27002:2022 §8.24 dekt beleid + procedures + sleutelbeheer + gebruik"). Niet toegestaan: letterlijke citaten >10 woorden.

**Twee-zijdige analyse-format voor masterchat-escalatie** (verplicht wanneer escalatie wel nodig is):

Tech levert beide kanten van de mogelijke beoordeling vóór masterchat-judgement:

```
[Paar-ID] — masterchat-judgement-vraag:

Pro-[predicate A]-onderbouwing:
- argument 1
- argument 2
- evidence-verwijzing

Pro-[predicate B]-onderbouwing:
- argument 1
- argument 2
- evidence-verwijzing

Tech-positie: [voorkeur of "geen voorkeur"]
Vraag aan masterchat: [specifieke vraag, niet algemeen]
```

Pre-push disclosure-check (Protocol 14) wordt v1.1 uitgebreid met NEN-tekst-fragment-detectie als vijfde categorie — zie protocol-bestand voor detail.

---

## GR — Property-semantiek-discipline (gedragsregel, v1.9)

**Trigger:** Modellering van rollen of relaties tussen frameworks/individuals.

**Subagent:** Alle (gedragsregel, geen sprint-protocol).

**Procedure:**

> **Rol-onderscheid bij framework-individual-properties: issuer ≠ beheerder; uitgever ≠ uitvoerder. Niet samenvoegen onder één property als rollen ontologisch verschillen.**

Concreet:

1. Vóór toevoeging van entity aan bestaande property: vraag "vervult deze entity exact dezelfde semantische rol als bestaande entities?"
2. Bij rol-verschil: aparte property overwegen (eventueel als toekomst-kandidaat documenteren)
3. Niet "ongeveer dezelfde rol"-redenering toepassen

**Output:** Property-keuze met semantiek-onderbouwing.

**Escalatie:** Bij voorstel om bestaande property uit te breiden naar nieuwe semantiek: scope-pauze.

**Toepassings-bewijs:** v4.6.0 `fw:Logius` NIET als `fw:issuedBy` ENSIA (Logius beheert; BZK/NOREA/VNG geven uit). Open kandidaat: `fw:isManagedBy`-property voor toekomstige beheerder-rol-modellering.

---

## 15. Scope-pauze-escalatie — Claude Code → Steven → claude.ai

Specifieke procedure voor scope-pauze in Claude Code-context.

### Wanneer scope-pauze (samenvattend)

Algemene triggers (specifiek per protocol hierboven):

- Onverwachte vondst in pre-sprint-inventarisatie met scope-impact
- Triple-Δ >30% boven raming zonder verklaarbare oorzaak
- Conflict tussen code-block en toelichting in instructie
- Twijfel over naam-semantiek voor nieuwe property/klasse
- Bron-niet-bereikbaarheid in subagent-omgeving
- D-conformance-risico (D1-D12 mogelijke schending)
- NEN-restrictieve bron-behoefte (subagent kan deze niet zelf raadplegen)

### Procedure

1. **STOP** met uitvoering bij scope-pauze-trigger
2. Schrijf **scope-pauze-rapport** in `output/scope-pauze-<sprintversie>-<onderwerp>.md` met:
   - Titel (kort, descriptief)
   - Type: pauze conform protocol-X
   - Status: uitvoering gestopt
   - Bevinding (wat is waargenomen)
   - Drie opties A/B/C met voor- en nadelen
   - Tech-aanbeveling (welke optie + reden)
   - Triple-impact-raming per optie
   - Verwacht effect op sprint-totaal
3. Commit + push naar GitHub met message `scope-pauze: <sprintversie> <onderwerp>`
4. Geen verdere uitvoering tot masterchat-besluit terugkomt

### Steven's rol als tussenmens

- Steven leest scope-pauze-rapport
- Steven raadpleegt Master-chat in claude.ai
- Masterchat bevestigt of wijzigt aanbeveling (Optie A/B/C/anders)
- Steven brengt besluit terug naar Claude Code (via volgende commit met instructie-update, of direct in subagent-sessie)

### Niet-doen bij scope-pauze

- **Niet** zelf interpreteren ("ik denk dat masterchat A bedoelt")
- **Niet** voortrollen naar volgende stap "alvast"
- **Niet** masterchat-discussie in Claude Code uitvoeren — Steven coördineert
- **Niet** scope-pauze stilzwijgend oplossen door instructie te herinterpreteren

---

## 16. Sample-first-discipline

**Trigger:** Grote ABox-werk (>50 individuals of >500 triples in één blok).

**Subagent:** Tech.

**Procedure:**

1. Vóór volledige batch: maak **eerste 3-5 individuals** als sample
2. Schrijf sample-TTL in tussenrapport
3. **Wacht op masterchat-bevestiging** (via Steven) dat patroon correct is
4. Daarna pas volledige batch uitvoeren
5. Bij batch-uitvoering: SHACL-validatie tussentijds (na elke ~50 individuals indien praktisch)

**Output:** Sample-tussenrapport + bevestiging vóór volledige batch.

**Escalatie:** Indien sample-feedback substantiële patroon-wijziging vereist: nieuwe sample-iteratie, niet voortrollen.

**Toepassings-bewijs:** v4.6.0 Stap 4 Sheet 6 (32 capabilities + 160 LevelDescriptions): eerste 3 Cbw-capabilities als sample, masterchat-bevestiging vóór volledige batch.

---

## 17. File-back-voorstel (verwijzing naar CLAUDE.md §Operations)

Tech/Brein/Dashboard kunnen een file-back-voorstel doen bij blijkend nieuw inzicht uit een query of sprint-werk.

**Niet autonoom uitvoeren** — altijd masterchat-besluit via Steven.

File-back-criterium: inzicht komt twee of meer keer terug zonder centrale documentatie.

Volledige procedure: zie CLAUDE.md §"Operations — File-back".

---

## 18. Output-conventies

### File-naming

| Type | Pattern | Voorbeeld |
|---|---|---|
| Sprint-instructie | `docs/instructies/instructie-v4.X.Y.md` | `instructie-v4.7.0.md` |
| Patch-rapport | `output/patch-rapport-v4_X_Y.md` | `patch-rapport-v4_6_0.md` |
| Canonical metrics | `output/canonical_metrics_v4_X_Y.json` | `canonical_metrics_v4_6_0.json` |
| SHACL results | `output/shacl_results_v4_X_Y.json` | `shacl_results_v4_6_0.json` |
| File hashes | `output/file_hashes_v4_X_Y.txt` | `file_hashes_v4_6_0.txt` |
| Inventarisatie | `output/inventarisatie-<sprintversie>-precheck.md` | `inventarisatie-v4_6_0-precheck.md` |
| Tussenrapport | `output/tussenrapport-<sprintversie>-stap-<N>.md` | `tussenrapport-v4_6_0-stap-3.md` |
| Scope-pauze | `output/scope-pauze-<sprintversie>-<onderwerp>.md` | `scope-pauze-v4_6_0-m15-harmonisatie.md` |
| Lint-rapport | `output/lint-<YYYY-MM-DD>.md` | `lint-2026-08-15.md` |

### Versie-suffix verplicht

Alle scripts, hash-files en patch-rapporten dragen **versie-suffix** sinds v4.3.3. Geen versie-suffix = niet-conforme output.

### Patch-rapport-structuur (Tech)

Verplichte secties (volgorde):
- §0 Tellingen-vergelijking vorige → nieuwe versie (uit canonical_metrics JSON, niet uit memorie)
- §1-7 Per Stap delta's + verificaties + samples
- §8 Aandachtspunten (Methodologisch / Bron-specifiek / Kwaliteits-indicatoren / Architectuur)
- §9 Geparkeerde-items-status-update (Protocol 10)
- §10 D-decision-conformiteit-check (D1-D12)
- §11 Deliverables
- §12 Sprint-prognose-evaluatie
- §13 GO-criteria-checklist

### Tussenrapport-structuur (Tech)

Per stap:
- Wijzigingen op modules
- Tellingen-delta stap N
- Verificaties uitgevoerd
- Sample TTL (kwaliteits-check)
- §8-aandachtspunten verzameld
- Sprint-totaal-stand na stap N
- Volgende: Stap N+1

---

## 19. Verwijzingen

| Bron | Locatie |
|---|---|
| Volledige projectinstructie | `projectinstructie-v1.9.md` (in claude.ai PK) |
| Sprint-protocollen brain-versie | `brain/brain__workflow__sprint-protocollen.md` |
| Workflow-register | `brain/brain__workflow__workflow-register.md` |
| Scope-discipline concept | `brain/brain__workflow__scope-discipline.md` |
| Opleveringsprotocol | `brain/brain__workflow__opleveringsprotocol.md` |
| Brein-werkwijze | `brain/brain__workflow__zes-chat-architectuur.md` (zeven chats, filename behouden) |
| Sprint-voorbeelden | `brain/brain__sprints__v4_4_0_*.md`, `v4_5_0_*.md`, `v4_6_0_*.md` |
| CLAUDE.md Operations-sectie | `CLAUDE.md` §"Operations" + §"Skills-ecosystem-positionering" |

---

## 20. Wijzigingsgeschiedenis

| Datum | Versie | Wijziging |
|---|---|---|
| 2026-05-22 | 1.0 | Initiële versie. Geporteerd uit projectinstructie v1.9 §"Sprint-protocollen" + brain__workflow__sprint-protocollen.md. Aangepast voor subagent-context met Trigger/Procedure/Output/Escalatie-structuur per protocol. Toevoeging §15 Scope-pauze-escalatie-route specifiek voor Claude Code, §16 Sample-first-discipline (afgeleid uit sprint-praktijk), §17 File-back-verwijzing, §18 Output-conventies. |
| 2026-05-26 | 1.1 | Toevoeging Protocol 14 — Pre-push disclosure-check (iteratie 12 polish-mini-sprint). Aanleiding: PAT-blunder voorgaande sessie + handovers ongetoetst gepusht. Reikwijdte: alle subagents + Steven, vóór elke push van documenten met chat-historie of subagent-output. Niet retroactief. |
| 2026-05-26 | 1.2 | Toevoeging drie protocollen 15-17 uit T1-leerpunten (iteratie 13 Brein-cyclus). Protocol 15: Tech levert werkbare applier (niet alleen specificatie) — bron T1 §8 leerpunt 5 (tooling-incident applier). Protocol 16: Lokatie verificatie-scripts expliciet in patch-rapport — bron T1 §8 leerpunt 6 (pad-inconsistentie). Protocol 17: NEN-werkverdeling Tech↔Masterchat — bron T1 §8 leerpunt 4 (eerste productie-toepassing). |
| 2026-05-27 | 1.3 | Protocol 17 herzien na koers-correctie lokale NEN-toegang. Tech-autonomie omhoog; masterchat-escalatie alleen bij edge-cases. Parafrase-discipline + twee-zijdige analyse-format toegevoegd. Overzichtstabel-rij voor Protocol 17 bijgewerkt (titel + uitvoerend + status-veld). |

---

**Einde sprint-protocollen v1.3.**

*Bij twijfel over toepasselijkheid van protocol: scope-pauze met vraag aan masterchat is altijd legitiem.*
