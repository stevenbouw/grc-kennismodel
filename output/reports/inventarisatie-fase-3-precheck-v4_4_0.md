# INVENTARISATIE FASE 3 PRECHECK — v4.4.0

**Versie:** 1.0
**Datum:** 13 mei 2026
**Opsteller:** Technische chat
**Type:** Read-only pre-sprint-inventarisatie conform sprint-protocol B
**Basis:** v4.4.0 (opgeleverd 13 mei 2026)
**Status:** ter masterchat-beoordeling

---

## 0. Executive summary

Zes vragen beantwoord. Drie vondsten als **Signaal voor masterchat** gemarkeerd (§7). Geen ontologie-wijzigingen verricht.

| Vraag | Onderwerp | Verrassing? |
|---|---|---|
| A | NIST CSWP 29 inventarisatie | Nee — 6/22/106 exact bevestigd. Implementation Examples + Informative References staan online bij NIST, niet in PDF |
| B | CBW-Excel sheet 8 structuur | **Ja** — ISO-refs hebben inconsistente notatie (Griekse Α i.p.v. Latin A; spaties; ontbrekende puntjes). Niet 90, maar 89 unieke CSF-Subcategories. Signaal 1 |
| C | Bestaande CSF-verwijzingen | Nee — `csf:`-namespace niet gedefinieerd; 3 prose-mentions in rdfs:comment; geen stubs |
| D | SKOS-target-IRI-patronen | **Ja** — ISO 27001-mappings hebben twee target-typen (Annex A via D5 sameAs-brug; hoofdtekst-clausule direct). Signaal 2 |
| E | SKOS-346 verdeling + anomalieën | **Ja** — 9 bidirectionele exactMatch-paren; **0/93 BIO-Controls** hebben directe SKOS-mapping naar ISO 27001 of NIST 800-53. Signaal 3 |
| F | COSO/COBIT in m17 | Nee — 5/5/9 exact bevestigd; IRI-format consistent; 19 bestaande SKOS-relations als framework-niveau-mappings (niet control-niveau) |

---

## 1. Vraag A — NIST CSWP 29 structurele inventarisatie

**Bron**: `NIST_CSWP_29.pdf` (feitelijk zip-archive, uitgepakt). 32 pagina's, geëxtraheerde tekst ~1.015 regels.

| Vraag | Antwoord |
|---|---|
| A.1 Functions | **6** ✓ — GOVERN (GV), IDENTIFY (ID), PROTECT (PR), DETECT (DE), RESPOND (RS), RECOVER (RC) |
| A.2 Categories totaal | **22** ✓ |
| A.3 Subcategories totaal | **106** ✓ |
| A.4 Format | `XX.YY-NN` met **dash** tussen Category en Subcategory-nummer (bv. `GV.OC-01`, `PR.AA-02`) |
| A.5 Implementation Examples | **Concept vermeld in PDF** (twee mentions, pagina ~2 en pagina ~3); concrete inhoud niet in PDF — wordt online gepubliceerd door NIST en regelmatig bijgewerkt |
| A.6 Informative References | **Concept vermeld in PDF** (twee mentions); concrete mappings niet in PDF — wordt online gepubliceerd door NIST |

**Verdeling per Function:**

| Function | Categories | Subcategories |
|---|---:|---:|
| GV (GOVERN) | 6 (OC, OV, PO, RM, RR, SC) | 31 |
| ID (IDENTIFY) | 3 (AM, IM, RA) | 21 |
| PR (PROTECT) | 5 (AA, AT, DS, IR, PS) | 22 |
| DE (DETECT) | 2 (AE, CM) | 11 |
| RS (RESPOND) | 4 (AN, CO, MA, MI) | 13 |
| RC (RECOVER) | 2 (CO, RP) | 8 |
| **Totaal** | **22** | **106** |

---

## 2. Vraag B — CBW-Excel sheet 8 structuur

**Bron**: `Cbw_NIS2_Control_Framework.xlsx`, tabblad `Mapping Uitvoeringsverordening` (sheet-index 8). 55 totale rijen, 11 kolommen.

| Vraag | Antwoord |
|---|---|
| B.1 Datarijen | **49** (rij 7 t/m 55; rij 2-6 zijn meta-header) |
| B.2 Kolomstructuur | K2 = UV-onderwerp-ID (rij 6 header: *"Uitvoeringsverordening (EU) 2024/2690"*) · K3 = Engelse titel · K4 = *"ISO 27001:2022"* · K5 = *"NIST Cybersecurity Framework v2.0"* |
| B.3 CSF-format | `XX.YY-NN` (2-digit) — **identiek aan CSWP 29-format**; 50/50 sample-matches |
| B.4 ISO-format | **Inconsistent** — zie Signaal 1 |
| B.5 Unique UV-IDs | **49** (formaat: `1.1`, `1.2`, `2.1`, …) |
| B.5 Unique CSF-Subcategories | **89** (van de 106 → 17 ontbreken) |
| B.5 Unique ISO-refs | **93** (na notatie-normalisatie mogelijk minder) |
| B.5 CSF-occurrences (multi) | 284 |
| B.5 ISO-occurrences (multi) | 118 |
| B.6 Combinatie-refs | **0** — geen `/`-, `en`- of dubbele-spatie-combinaties zoals in sheet 9. Wel andere typo-categorie (Griekse Α) — zie Signaal 1 |

**Meta-headerinhoud (rij 3-5):**
> "De ENISA heeft voor de uitvoeringsverordening … een technical implementation guide opgesteld."
> "Link naar de ENISA technical implementation guide: www.enisa.europa.eu/publications/nis2-technical…"

Sheet 8 verwijst expliciet naar ENISA TIG als bron van het mapping-werk; de sheet zelf bevat alleen de gestructureerde mapping-tabel, geen tekst-toelichting.

**Sample-datarij (UV 1.1):**
- K2 = `1.1`
- K3 = `Policy on the security of network and information systems`
- K4 = `5.2, A.5.1, A.5.36, A.5.4, 9.3`
- K5 = `PR.AT-02, GV.PO-01, GV.PO-02, GV.OC-03, GV.RM-03, GV.OC-02, ID.IM-01, ID.IM-02, ID.IM-03, ID.IM-04`

---

## 3. Vraag C — Bestaande CSF-verwijzingen in v4.4.0

| Vraag | Antwoord |
|---|---|
| C.1 `csf:`-namespace | **Niet gedefinieerd** in enig v4.4.0-bestand |
| C.2 CSF-string-literals | 3 bestanden noemen CSF in `rdfs:comment`-tekst — geen IRIs, geen properties |
| C.3 Stub-klassen of -individuals met CSF-naam | **Geen** |

**C.2 detail — drie locaties:**

- `grc-core.ttl` regel 358-359: comment bij `ext:hasControlStatement` vermeldt *"future NIST CSF, NIST 800-53, ISO 27002-controls"*. Vooruit-verwijzing.
- `m02-control.ttl` regel 98-99: comment vermeldt *"NIST CSF-aligned concept: Identify, Protect, Detect, Respond, Recover"*. **NB: dit verwijst naar CSF v1.x's 5 Functions; CSF v2.0 heeft 6 (incl. GOVERN).**
- `m17-coso-cobit.ttl` regel 56-57: comment bij een algemene framework-klasse vermeldt *"…NIST CSF function"*. Indirecte referentie.

Geen IRI-conflicten, geen overschrijvings-risico.

---

## 4. Vraag D — SKOS-mapping-target-IRI-patronen

| D | Bron-bestand | Aantal | IRI-format | Klasse-type |
|---|---|---:|---|---|
| D.1 ISO 27001 | `m09-iso27001-ext.ttl` | **48** | `HSClause_X_<Name>` (7×) + `ISO27001_X[_Y]` (~41×) | `HSClause` / `ISMSRequirement` |
| D.2 NIST 800-53 | `m11-nist-800-53.ttl` | **124** | `NIST_<XX>_<NN>` (bv. `NIST_AC_1`, `NIST_AT_2`) | `NISTControl` |
| D.3 BIO 2.0 | `m08-bio20.ttl` | **93** `BIOControl` + **148** `OverheidsMaatregel` | `bio:ISO27002_X_YY` (zfill-conventie) | `bio:BIOControl` + `bio:OverheidsMaatregel` |

**Detail D.1 — ISO 27001 dual scheme:**
- `HSClause_*` voor Harmonized Structure-clausules (4 Context, 5 Leadership, 6 Planning, …, 10 Improvement)
- `ISO27001_X` of `ISO27001_X_Y` voor ISMS-vereisten (bv. `ISO27001_10`, `ISO27001_10_1`)
- **ISO 27001 Annex A-controls hebben GEEN eigen individuals in m09** — refs zoals `A.5.1` uit sheet 8 verwijzen naar wat in dit model `bio:ISO27002_5_01` is (via D5 sameAs is dat ook `ctrl:ISO27002_5_01`)

**Detail D.3 — BIO 2.0 IRI-format:**
- IRI: `bio:ISO27002_X_YY` (geen `BIOControl_*`-prefix; rename via Actie A v4.1.0-alpha)
- `bio:bioControlNummer`-literal: format inconsistent door Excel-conversie — `"5.01"` voor sectie 5.1, maar `"5.1"` voor sectie 5.10 (zelfde issue opgelost in Stap 5 v4.4.0 via zfill-conversie)

---

## 5. Vraag E — SKOS-346 verdeling + anomalieën

### E.1 Verdeling per match-type

| Match-type | Aantal | % |
|---|---:|---:|
| `skos:exactMatch` | 46 | 13,3% |
| `skos:closeMatch` | 54 | 15,6% |
| `skos:broadMatch` | 38 | 11,0% |
| `skos:narrowMatch` | 0 | 0,0% |
| `skos:relatedMatch` | 208 | 60,1% |
| **Totaal** | **346** | 100,0% |

### E.2 Verdeling per module (top 6)

| Module | Aantal | Verdeling |
|---|---:|---|
| `m10-nis2-ext.ttl` | 118 | exactMatch=28, closeMatch=32, broadMatch=25, relatedMatch=33 |
| `m16-virbi-ext.ttl` | 48 | relatedMatch=48 (alleen) |
| `m12-dora.ttl` | 35 | broadMatch=1, relatedMatch=34 |
| `m14-avg-gdpr.ttl` | 33 | closeMatch=2, broadMatch=2, relatedMatch=29 |
| `m17-coso-cobit.ttl` | 28 | closeMatch=1, broadMatch=1, relatedMatch=26 |
| `m02-control.ttl` | 19 | relatedMatch=19 (alleen) |
| 7 andere modules | 65 | gemengd |

`narrowMatch` wordt nergens gebruikt (impliciet via `broadMatch`-inverse).

### E.3 Anomalieën

| Anomalie | Aantal | Risico |
|---|---:|---|
| Bidirectionele assertions (zelfde paar beide kanten) | **9** | Redundant; functioneel correct voor `skos:exactMatch` (symmetrisch); zie Signaal 3 |
| Inconsistente match-types (zelfde paar, ≠ types) | 0 | Geen |
| Dangling SKOS-targets (subject/object niet als triple-subject elders) | 0 | Geen |

**Bidirectionele sample**: `asset:HumanAsset ↔ ext:TBB_Personen` (`skos:exactMatch` in beide richtingen). Vergelijkbaar voor 8 andere `asset:↔ext:TBB_*`-paren in `m18-assets.ttl`.

### E.4 BIO-Control SKOS-mapping-dekking

| Metric | Aantal |
|---|---:|
| BIO-Controls totaal | 93 |
| BIO-Controls met **directe** SKOS-mapping naar ISO 27001 of `HSClause` | **0 / 93** |
| BIO-Controls met **directe** SKOS-mapping naar NIST 800-53 | **0 / 93** |

Zie Signaal 3 hieronder voor toelichting (D5 sameAs-brug compenseert mogelijk).

---

## 6. Vraag F — COSO/COBIT-individuals voor GOVERN-overlap

| Vraag | Aantal | IRI-format |
|---|---:|---|
| F.1 COSO ICF-components | **5** ✓ | `ext:COSO_ICF_<Name>` (ControlActivities, ControlEnvironment, InformationCommunication, MonitoringActivities, RiskAssessment) |
| F.2 COSO ERM-pillars | **5** ✓ | `ext:COSO_ERM_<Name>` (GovernanceCulture, InformationCommunicationReporting, Performance, ReviewRevision, StrategyObjectiveSetting) |
| F.3 COBIT 2019-objectives | **9** ✓ | `ext:COBIT_<Code>` (APO12, APO13, DSS05, EDM01-05, MEA02) |

**Totaal m17 NamedIndividuals: 19** (= 5+5+9).

### F.5 Bestaande SKOS-mappings vanuit deze individuals

| Aantal | Patroon |
|---|---|
| **19 mappings** vanuit COSO/COBIT-individuals | Targets zijn **framework-niveau-individuals** (`ISO_IEC_27001_2022`, `NIST_SP_800_39`, `ISO_31000_2018`, `BIO_2_0`), niet individuele controls |

**Sample:**
- `ext:COBIT_APO12 skos:relatedMatch ext:ISO_IEC_27005_2024`
- `ext:COBIT_APO13 skos:closeMatch ext:ISO_IEC_27001_2022`
- `ext:COBIT_APO12 skos:relatedMatch ext:COSO_ERM_Performance`

Geen bestaande SKOS-mapping van individuele COSO/COBIT-individuals naar individuele controls. Voor CSF GOVERN-overlap-`skos:relatedMatch`-strategie zou dit het 1e gebruik van dat patroon op deze targets zijn.

---

## 7. Signalen voor masterchat

### Signaal 1 — ISO 27001-referentienotatie in sheet 8 is inconsistent (Vraag B.4)

Sheet 8 K4 (ISO 27001:2022-mappings) bevat **drie soorten typo's** die exact-IRI-matching zullen belemmeren bij Fase 3-mappings:

- **Griekse Alpha (Α) i.p.v. Latin A**: bv. `Α.5.19`, `Α.5.20`, `Α.5.21`, `Α.8.2` (2×), `Α.8.3`, `Α.8.21`, `Α.5.18`, `Α.5.16`, `Α.5.17`, `Α.5.15`, `Α.8.5` — totaal **12 hits** in eerste 100 refs gescand
- **Ontbrekende punt na A**: `A5.7`, `A5.29` — totaal **2 hits**
- **Onverwachte interne spaties**: `A.5 .24`, `A. 5.30` — totaal **2 hits**

Plus sub-sub-clausules zoals `6.1.2`, `6.1.3` (geldig formaat, maar wel apart te onderscheiden van top-level clausules `6.1`).

Feitelijke impact: bij letterlijke overname (Signaal 4-precedent uit v4.4.0) komen typo-strings als ondoorzoekbare literals in het model; bij normalisatie moet de aanpak expliciet besloten worden. Geen tech-chat-oplossing — feitelijk gerapporteerd.

### Signaal 2 — ISO 27001-mappings vereisen twee verschillende target-typen (Vraag D.1)

Sheet 8 ISO-refs combineren twee soorten verwijzingen:

- **Hoofdtekst-clausules** (`5.2`, `5.3`, `9.3`, `6.1.2`): targetbaar als `m09:ISO27001_X[_Y]` (bestaat in v4.4.0, 41 ISMS-Requirement-individuals)
- **Annex A controls** (`A.5.1`, `A.5.4`, `A.5.36`): bestaan **niet** als eigen `ISO27001_AnnexA_*`-individuals in m09. Conventie in dit model: ISO 27001 Annex A = ISO 27002:2022 = `bio:ISO27002_X_YY` (via D5 sameAs `ctrl:↔bio:`).

Voorbeeld: `A.5.1` (Policies for information security) uit sheet 8 → IRI-target = `bio:ISO27002_5_01` na zfill, of `ctrl:ISO27002_5_01` (D5-equivalent).

Eén SKOS-mapping-target-strategie moet beide soorten dekken. Geen tech-chat-aanbeveling.

### Signaal 3 — Geen directe SKOS-mappings van BIO-Controls naar ISO 27001 of NIST 800-53 (Vraag E.4)

**0/93 BIO-Controls** hebben directe `skos:*Match`-mapping naar `m09:ISO27001_*`, `m09:HSClause_*` of `m11:NIST_*` individuals.

Indirecte koppeling bestaat wel:
- BIO ↔ ISO 27002 via D5 sameAs (`bio:ISO27002_X_YY = ctrl:ISO27002_X_YY`)
- ISO 27001 Annex A ≈ ISO 27002 (conceptueel; in dit model alleen via de bio:-prefix gerepresenteerd)
- ISO 27002 ↔ NIST 800-53: project bevat `sp800-53r5-to-iso-27001-mapping.docx` als bron, maar deze inhoud is **niet** als SKOS-mapping in v4.4.0 opgenomen

Feitelijk: huidige SKOS-mappings zijn vooral wet-naar-wet (NIS2, DORA, AVG, VIRBI, COSO/COBIT-frameworkniveau) en niet control-naar-control. Voor CSF 2.0 Fase 3-mappings naar ISO 27001 (via sheet 8) en BIO (via brug naar ISO 27002) zal dit het eerste reguliere control-niveau SKOS-mapping-werk zijn. Geen tech-chat-aanbeveling.

### Sub-signaal — Bidirectionele exactMatch-paren (Vraag E.3)

9 paren met `skos:exactMatch` in beide richtingen geassert (allen in `m18-assets.ttl`, patroon `asset:* ↔ ext:TBB_*`). Niet kritiek (exactMatch is symmetrisch), maar redundant — één richting volstaat. Geen tech-chat-aanbeveling; relevant als parallel-spoor "SKOS-kwaliteitsanalyse" zich bezighoudt met dedup.

### Verfijning Vraag A — Implementation Examples + Informative References online

CSWP 29 vermeldt beide concepten maar bevat de inhoud niet. *"NIST now provides Implementation Examples and Informative References, which are available online and updated regularly."* — bron: pagina ~2 PDF.

Feitelijk: voor opname in M21 zou een aparte bronvalidatie nodig zijn (NIST CSF 2.0 online resources op nvd.nist.gov of csrc.nist.gov). Niet binnen scope huidige inventarisatie.

---

## 8. Stand-by

Tech-chat blijft stand-by voor:

- Masterchat-architectuurbeslissingen Fase 3 (v4.5.0-instructie)
- Of: vervolg-opdracht (parallel-spoor SKOS-kwaliteitsanalyse, andere inventarisatie)

Geen ontologie-wijzigingen verricht. Workdir `/home/claude/v433` bevat 22 ontologie-bestanden bytewise identiek aan v4.4.0-oplevering.

---

**Einde inventarisatie Fase 3 precheck v4.4.0.**
