---
type: report
subtype: pre-sprint-inventarisatie
sprint: T2
baseline: v4.6.1
protocol: skos-beoordelings-protocol-v1_2
date: 2026-05-27
status: final
modus: read-only
related:
  - skos-beoordelings-protocol-v1_2
  - t1-eindrapport-v4_6_1
  - H36_skos-exactmatch-ctrl-compl-audit
  - D04_skos-cross-framework
scope: "T2-sprint Stap 1 — pre-sprint-inventarisatie. Vragen A-E + Tech-observaties + pilot-sample-aanbeveling + hand-off-checklist. Geen ontologie-wijzigingen, geen herclassificatie-voorstellen. SIGNAAL: scope-trigger geraakt (149 > 130, instructie §5)."
---

# T2 Pre-sprint-inventarisatie-rapport

## §1. Samenvatting

| Kerncijfer | Waarde |
|---|---:|
| **Totaal ctrl: ↔ compl: SKOS-paren** | **149** |
| Verwacht uit instructie | ~111 |
| **Afwijking** | **+34% boven raming → scope-pauze-trigger §5 geraakt (>130)** |
| `skos:exactMatch` | **0** (instructie verwacht ~18 — niet aangetroffen) |
| `skos:closeMatch` | 34 |
| `skos:broadMatch` | 55 |
| `skos:narrowMatch` | 0 |
| `skos:relatedMatch` | 60 |
| Module-verdeling | 118 in `m10-nis2-ext.ttl` + 31 in `m14-avg-gdpr.ttl` |
| Cluster-membership | 149 / 149 = **100% cluster-member** (0 singletons) |
| Evidence-niveau-1-dekking ctrl-zijde (m10) | 93/118 = 79% (via CBW-Mapping-UV) |
| D4.1-disclaimer CBW-Excel "Mapping Uitvoeringsverordening" | ENISA TIG-disclaimer indirect van toepassing (R3 verwijst expliciet naar ENISA TIG) — T1-bekend |
| D4.1-disclaimer CBW-Excel "Mapping BIO2" | **Eigen non-equivalence-disclaimer R4 + R3 expliciet één-op-één-uitsluiting** |
| ABox-anomalieën | 0 dubbele triples, 0 expliciete symmetrie, 0 (s,o)-paren met meerdere predicates |
| Bron-toegankelijkheid | Alle bronnen aanwezig (ENISA-TIG, EU-UV, EU-NIS2, CBW-Excel, ISO 27001/27002 lokaal) |

**Hoofdconclusie:** Scope-aanname uit instructie wijkt structureel af van werkelijkheid:

1. Verwachte ~18 `skos:exactMatch` bestaan **niet meer** in het model. De v4.6.1-patch (T1) heeft alle 28 oorspronkelijke exactMatch al weggehaald. Een nazoek op model-breed (alle 22 modules) levert **0 `exactMatch` op ctrl: ↔ compl:**. De "18 resterende exactMatch" uit T2-scoping-aanname is dus reeds geneutraliseerd door T1.
2. Het cluster bevat ook **31 paren in `m14-avg-gdpr.ttl`** (compl:AVG ↔ ctrl:ISO27002). Deze waren niet in T2-scoping benoemd; T1-precedent richtte zich enkel op m10/NIS2.
3. Het totaal (149) ligt 34% boven raming. Dit raakt scope-pauze-trigger §5 ("Totaal-aantal mappings >130"). **Tech voltooit volledige inventarisatie (read-only is safe) en levert dit rapport als signaal. Masterchat beslist over scope-aanpassing voor T2 vervolgsstap.**

**Geen aparte scope-pauze-md geschreven** — dit inventarisatie-rapport ís het scope-signaal-mechanisme; aparte pauze-md zou doublure zijn (zie §7 Tech-observatie 1).

---

## §2. Vraag A — Scope-bevestiging

### §2.1 — Tabel: ctrl: ↔ compl: SKOS-mappings per predicate-type, per module

| Predicate | `m10-nis2-ext.ttl` | `m14-avg-gdpr.ttl` | Elders | **Totaal** |
|---|---:|---:|---:|---:|
| `skos:exactMatch` | 0 | 0 | 0 | **0** |
| `skos:closeMatch` | 32 | 2 | 0 | **34** |
| `skos:broadMatch` | 53 | 2 | 0 | **55** |
| `skos:narrowMatch` | 0 | 0 | 0 | **0** |
| `skos:relatedMatch` | 33 | 27 | 0 | **60** |
| **Totaal** | **118** | **31** | **0** | **149** |

**Multi-module-discipline (Protocol 2):** alle 22 .ttl-modules doorzocht. Buiten m10 en m14 zijn er **geen** ctrl: ↔ compl: SKOS-mappings. Geen verborgen entries in `m02-control.ttl`, `m05-compliance.ttl`, `m09-iso27001-ext.ttl`, `m17-coso-cobit.ttl`, of andere modules.

### §2.2 — Richting-verdeling

| Richting | exactMatch | closeMatch | broadMatch | narrowMatch | relatedMatch | Totaal |
|---|---:|---:|---:|---:|---:|---:|
| ctrl: → compl: | 0 | 32 | 53 | 0 | 33 | 118 |
| compl: → ctrl: | 0 | 2 | 2 | 0 | 27 | 31 |
| **Totaal** | 0 | 34 | 55 | 0 | 60 | 149 |

**Observatie:** Reverse-richting (compl: → ctrl:) komt enkel voor:
- In m14-avg-gdpr.ttl voor 31 paren (alle 31 paren in m14 zijn compl: → ctrl:)
- In m10 niet aanwezig — m10 hanteert strikt ctrl: → compl:

Dit suggereert dat m14 een andere modelleringsconventie volgt dan m10 (subject-zijde = compliance-clause, niet control). Geen ABox-anomalie, wel ontwerpheterogeniteit binnen het ctrl: ↔ compl:-cluster.

### §2.3 — Afwijking-analyse t.o.v. instructie

| Aspect | Instructie-aanname | Werkelijkheid | Δ |
|---|---:|---:|---|
| Totaal | ~111 | 149 | **+34%** |
| `exactMatch` | ~18 (T1-residueel) | 0 | −18, niet aanwezig |
| `broadMatch` | ≥28 (T1-output + bestaand) | 55 | +27 |
| `closeMatch` + `relatedMatch` + `broadMatch` "oude" | ~65 | 149 | +84 (m14 toegevoegd) |
| `narrowMatch` aanwezig? | vermoedelijk 0 | 0 | conform |

**Verklaring 34%-afwijking:**

1. **−18 exactMatch:** v4.6.1 (T1-patch) heeft alle 28 oorspronkelijke `exactMatch` omgezet naar `broadMatch`. Er zijn dus 0 residuele exactMatch om "uit te breiden" naar audit-scope. De "18 resterende exactMatch"-aanname uit T2-scoping is achterhaald.
2. **+31 m14-paren:** AVG/GDPR-ctrl:compl-mappings zijn niet expliciet in T2-scope benoemd. Het is mogelijk dat deze impliciet bedoeld waren (cluster = "ctrl: ↔ compl: cross-namespace" als algemeen geval) of expliciet uitgesloten (cluster = "ctrl: ↔ NIS2-compl: in m10"). **Masterchat-beslissing nodig: T2-scope = m10-only of m10+m14?**

**Beide scope-keuzes zijn legitiem:**
- Optie A (m10-only, 118 paren): consistent met T1-scope (m10-cluster), Mapping-UV-evidence direct toepasbaar
- Optie B (m10 + m14, 149 paren): consistent met bredere "ctrl: ↔ compl: audit"-framing; vereist aparte AVG-bron-doorzoek
- Optie C (m10 + m14, gefaseerd): T2 = m10, T3 = m14

Zie §7 Tech-observatie 2 voor onderbouwing aanbeveling.

---

## §3. Vraag B — Cluster-structuur (per predicate-type, met bredere-cluster-cardinaliteit)

Cluster-definitie conform Protocol v1.2 §2.2 (C2 cardinaliteit binnen bredere mapping-cluster): een **cluster** is een subject- of object-anchor met cardinaliteit > 1 over alle predicate-types samen.

### §3.1 — Object-anchor-clusters (compl: → meerdere ctrl:)

**15 object-anchors met cluster-grootte > 1.** Sorteerd op cluster-grootte:

| # | Object-anchor | Cluster-grootte | Predicate-mix | Module-bron |
|---|---|---:|---|---|
| 1 | `compl:NIS2_Art21_i` | **32** | 12× broadMatch + 11× closeMatch + 9× relatedMatch | m10 |
| 2 | `compl:NIS2_Art21_e` | **17** | 7× broadMatch + 4× closeMatch + 6× relatedMatch | m10 |
| 3 | `compl:NIS2_Art21_a` | **12** | 4× broadMatch + 4× closeMatch + 4× relatedMatch | m10 |
| 4 | `compl:NIS2_Art21_b` | **10** | 6× broadMatch + 2× closeMatch + 2× relatedMatch | m10 |
| 5 | `compl:NIS2_Art21_g` | 9 | 4× broadMatch + 3× closeMatch + 2× relatedMatch | m10 |
| 6 | `compl:NIS2_Art21_j` | 9 | 3× broadMatch + 3× closeMatch + 3× relatedMatch | m10 |
| 7 | `compl:NIS2_Art21_c` | 8 | 4× broadMatch + 2× closeMatch + 2× relatedMatch | m10 |
| 8 | `compl:NIS2_Art21_d` | 7 | 5× broadMatch + 1× closeMatch + 1× relatedMatch | m10 |
| 9 | `compl:NIS2_Art21_f` | 7 | 4× broadMatch + 1× closeMatch + 2× relatedMatch | m10 |
| 10 | `compl:NIS2_Art21_h` | 7 | 4× broadMatch + 1× closeMatch + 2× relatedMatch | m10 |
| 11 | `ctrl:ISO27002_5_01` | 2 | 1× broadMatch + 1× closeMatch | m14+m14 |
| 12 | `ctrl:ISO27002_5_15` | 2 | 2× relatedMatch | m14+m14 |
| 13 | `ctrl:ISO27002_5_26` | 2 | 2× relatedMatch | m14+m14 |
| 14 | `ctrl:ISO27002_8_11` | 2 | 2× relatedMatch | m14+m14 |
| 15 | `ctrl:ISO27002_8_24` | 2 | 2× relatedMatch | m14+m14 |

**Observaties:**

- Alle 10 NIS2-art.21-letters hebben cluster-grootte ≥ 7 (object-anchor van veel↔1-relatie).
- 5 ISO27002-controls fungeren in m14 als object-anchor met grootte 2 (omdat m14 compl→ctrl-richting hanteert, niet ctrl→compl).
- **Cluster-membership-implicatie**: voor 118 m10-paren zit het object-anchor altijd in een cluster ≥ 7. C2-toets "1↔1 in cluster" wordt voor m10 nooit gehaald op object-zijde.

### §3.2 — Subject-anchor-clusters (subject met >1 mappings)

**28 subject-anchors met cluster-grootte > 1.** Top selectie:

| # | Subject-anchor | Cluster-grootte | Predicate-mix | Module-bron |
|---|---|---:|---|---|
| 1 | `compl:AVG_Art32` | **12** | 1× closeMatch + 11× relatedMatch | m14 |
| 2 | `compl:AVG_Art5_1f` | 7 | 2× broadMatch + 5× relatedMatch | m14 |
| 3 | `compl:AVG_Art25` | 6 | 6× relatedMatch | m14 |
| 4 | `compl:AVG_Art33` | 4 | 1× closeMatch + 3× relatedMatch | m14 |
| 5 | `ctrl:ISO27002_5_04` | 3 | 1× closeMatch + 2× relatedMatch | m10 |
| 6 | `ctrl:ISO27002_8_03` | 3 | 1× closeMatch + 2× relatedMatch | m10 |
| 7 | `compl:AVG_Art34` | 2 | 2× relatedMatch | m14 |
| 8-28 | (22× ctrl:ISO27002_*) | 2 | gemengd (broad/close/related) | m10 |

**Observatie:** In m14 zijn de subject-anchors AVG-clauses (compl→ctrl); in m10 zijn de subject-anchors ISO-controls (ctrl→compl). M14's `compl:AVG_Art32` is uniek het grootste subject-anchor in het hele model (12).

### §3.3 — Singletons (1↔1 binnen volledig cluster)

**0 singletons.** Alle 149 paren hebben òf subject-zijde òf object-zijde in een cluster > 1.

**Implicatie voor C2-toets:** Protocol v1.2 §3.1 stelt dat `exactMatch` "1↔1 in cluster"-voorwaarde vereist. Met 0 singletons zou geen enkel paar in T2-scope `exactMatch` ondersteunen. Dit is consistent met T1-uitkomst (alle 28 exactMatch → broadMatch).

### §3.4 — Cluster-membership per predicate-type

| Predicate | Totaal | In cluster (>1 op subject of object) | Singleton |
|---|---:|---:|---:|
| `closeMatch` | 34 | 34 | 0 |
| `broadMatch` | 55 | 55 | 0 |
| `relatedMatch` | 60 | 60 | 0 |
| **Totaal** | **149** | **149 (100%)** | **0** |

---

## §4. Vraag C — Evidence-niveau-1-coverage

### §4.1 — CBW-Excel sheets-overzicht

| Sheet | Aantal rijen | Relevant voor T2? |
|---|---:|---|
| `Toelichting` | 45 | Context (geen mapping) |
| `Keuzes` | 44 | Niet relevant |
| `Cbw (NIS2) Control Framework` | 215 | Indirect — bevat Cbw-art-verwijzingen per Cbw-control |
| `ISMS evaluatie` | 936 | Niet direct relevant voor SKOS-mappings |
| `Resultaten` | 78 | Niet relevant |
| `Volwassenheid beheersmaatregel` | 706 | Niet relevant |
| `Template` | 27 | Niet relevant |
| **`Mapping Uitvoeringsverordening`** | **55** (49 mapping-rijen) | **PRIMAIRE bron — reproduceert ENISA TIG** |
| `Mapping BIO2` | 168 | Andere doelgroep (BIO2 ↔ Cbw), niet ctrl: ↔ compl: |
| `Mapping DORA` | 47 | Andere doelgroep (DORA ↔ Cbw) |
| `Mapping NEN7510` | 1412 | Andere doelgroep (NEN 7510 ↔ Cbw); zorg-specifiek |

### §4.2 — Bron-overlap CBW-Mapping-UV ↔ m10-paren

**Methodische opmerking:** de CBW-Mapping-UV-sheet mapt **UV-clauses** (1.1, 1.2, 2.1, ..., 13.x) naar **ISO 27001:2022 clauses**, **niet** direct NIS2 art.21-letters. De UV-clauses zijn afgeleid van NIS2 art.21 via UV-Annex-decompositie. Voor evidence-overlap op (ctrl, compl)-paar-niveau zou complete UV-Annex → NIS2-art.21-mapping nodig zijn.

Als **proxy voor evidence-niveau-1-dekking** is geteld: van de unieke ctrl: ISO27002-IDs in de m10-paren, hoeveel komen voor in de ISO-kolom van CBW-Mapping-UV?

| Bron-bestand | Sheet | Mapping-rijen in bron | Unieke ISO-IDs in bron | Overlap met m10-ctrl-IDs | m10-ctrl-IDs zonder bron-overlap |
|---|---|---:|---:|---:|---:|
| `Cbw (NIS2) Control Framework.xlsx` | `Mapping Uitvoeringsverordening` | 49 | 74 | **70** | **23** |

**Per-paar-dekking m10 (ctrl-zijde-proxy):**

| Categorie | Aantal | % |
|---|---:|---:|
| m10-paren met ctrl-zijde gedekt in CBW-Mapping-UV | 93 | 79% |
| m10-paren met ctrl-zijde **niet** gedekt | 25 | 21% |
| **Totaal m10-paren** | **118** | 100% |

**ISO-IDs in m10 maar niet in CBW-Mapping-UV (23 stuks):**
`5.5, 5.6, 5.8, 5.33, 5.34, 5.37, 6.6, 6.7, 7.6, 7.8, 7.9, 7.12, 7.14, 8.4, 8.6, 8.10, 8.11, 8.12, 8.19, 8.23, 8.26, 8.27, 8.28`

**ISO-IDs in CBW-Mapping-UV maar niet in m10 (4 stuks):**
`9.1, 9.2, 9.3, 10.1` (management-clauses uit ISO 27001-body, geen Annex A-controls; m10 mapt enkel Annex A-controls = ISO 27002)

**Implicatie:** 25 m10-paren (21%) hebben **geen direct ctrl-zijde-overlap** met CBW-Mapping-UV. Deze paren steunen op andere evidence (model-eigen interpretatie, NIS2-letter ↔ ISO-control-zonder-UV-link, of ontstaan uit pre-T1-historie). Voor T2-pilot moet hier expliciet aandacht naar uitgaan (zie §8 Type 4 + 5).

### §4.3 — Evidence-coverage m14 (AVG/GDPR)

Voor m14-paren bestaat **geen autoritatieve cross-walk-bron** in `sources/`. AVG-art.32 / art.5(1f) ↔ ISO 27002-mappings circuleren in praktijkliteratuur (bv. ENISA Handbook on Security of Personal Data Processing 2018), maar geen specifieke mapping-publicatie is in repo aanwezig. Voor evidence-niveau 1 zou een externe bron geüpload moeten worden of zou een masterchat-judgement op basis van algemene AVG-tekst nodig zijn.

**Implicatie:** indien T2-scope m14 omvat, is evidence-niveau-1-coverage voor die 31 paren niet voorhanden. Dit is een aanvullende reden om m14 separaat te behandelen (T3) of expliciet als evidence-niveau-2/3-cluster mee te nemen.

---

## §5. Vraag D — D4.1-disclaimer-overzicht

### §5.1 — Disclaimer-tabel

| # | Bron | Bestand / locatie | Disclaimer-locatie | Disclaimer-parafrase | D4.1-implicatie |
|---|---|---|---|---|---|
| 1 | ENISA TIG v1.0 | `sources/ensia/ENISA_Technical_implementation_guidance...v1_0.pdf` | regel 285 (T1-bekend) | Bron ontkent categorisch dat de mapping als equivalence-claim mag worden gelezen | `exactMatch` voor paren met ENISA-evidence is **per definitie niet-conform** (Protocol v1.2 §2.0) |
| 2 | CBW-Excel `Mapping Uitvoeringsverordening` | `sources/adr-norea/Cbw (NIS2) Control Framework.xlsx`, sheet "Mapping Uitvoeringsverordening" | R3 (bron-verklaring), geen eigen disclaimer-clausule | Bron verklaart expliciet dat de mapping is overgenomen uit ENISA TIG ("De ENISA heeft voor de uitvoeringsverordening (EU) 2024/2690 een technical implementation guidance uitgebracht. In deze guidance heeft de ENISA voor de maatregelen uit de CIR 2024/2690 een mapping gemaakt naar de ISO 27001:2022 en de NIST CF 2.0.") | **ENISA-TIG-disclaimer indirect van toepassing** — CBW-Excel-UV-sheet voegt geen eigen equivalence-claim toe; erft de non-equivalence-status van de bron |
| 3 | CBW-Excel `Mapping BIO2` | Idem, sheet "Mapping BIO2" | **R3 + R4** | R3: "Daarmee wordt dus geen één-op-één-relatie tussen de BIO2-maatregelen en de vereisten uit de wet weergegeven. Een één-op-één-relatie zou niet mogelijk zijn omdat de BIO2 en de wet verschillen in scope en detailniveau." R4: "Disclaimer: de scope van de Cbw/Cbb en de ISO/BIO2 verschillen van elkaar." | **Eigen non-equivalence-disclaimer aanwezig.** Voor toekomstige BIO2-mappings (niet T2-scope) is `exactMatch` per definitie niet-conform |
| 4 | EU NIS2-richtlijn 2022/2555 | `sources/eu-recht/EU-nis2-richtlijn.pdf` | Niet onderzocht (geen mapping-bron, primaire wettekst) | n.v.t. — primaire bron, geen mapping-claim | n.v.t. |
| 5 | EU UV 2024/2690 | `sources/eu-recht/EU_2024_2690.pdf` | Niet onderzocht (geen mapping-bron, primaire wettekst) | n.v.t. — primaire bron, geen mapping-claim | n.v.t. |

### §5.2 — Bevestiging en signaal

**Bevestigd:**
- ENISA TIG-disclaimer (T1-bekend) blijft van toepassing op alle m10-paren met ENISA-evidence
- CBW-Mapping-UV-sheet voegt geen eigen disclaimer toe maar erft via expliciete bron-verklaring

**Nieuw signaal (instructie §5 scope-pauze-trigger):**
- **CBW-Mapping-BIO2-sheet bevat eigen non-equivalence-disclaimer.** Niet relevant voor T2 (scope = ctrl: ↔ compl:, niet BIO2 ↔ Cbw), maar wel signaal voor toekomstige BIO2-audit-sprints. Documenteer in brain-vault zodra T2 afgerond.

**Niet-onderzocht-status (uit instructie):** geen bronnen in scope (alleen CBW-Excel + ENISA-TIG; NEN bronnen onderzochteens m.b.t. C1-C3 in vervolg-stap, niet in deze inventarisatie).

---

## §6. Vraag E — Bron-toegankelijkheid + blockers

### §6.1 — Bron-toegankelijkheids-matrix

| # | Bron-type | Lokatie | Status | Blocker? |
|---|---|---|---|---|
| 1 | ISO 27002:2022 | `/Users/stevenbouwmeester/grc-sources-licensed/NEN-EN-ISO_IEC_27002_2022_en.pdf` | Aanwezig (3.0 MB) | Nee |
| 2 | ISO 27001:2022 | `/Users/stevenbouwmeester/grc-sources-licensed/ISO27001.pdf` | Aanwezig (0.68 MB) | Nee |
| 3 | ISO 27005:2024 | `/Users/stevenbouwmeester/grc-sources-licensed/ISO27005.pdf` | Aanwezig (2.4 MB) | Nee |
| 4 | ISO 31000:2018 | `/Users/stevenbouwmeester/grc-sources-licensed/ISO31000.pdf` | Aanwezig | Nee |
| 5 | ISO 22301:2019 | `/Users/stevenbouwmeester/grc-sources-licensed/ISO22301.pdf` | Aanwezig | Nee |
| 6 | ISO 22313:2020 | `/Users/stevenbouwmeester/grc-sources-licensed/ISO22313.pdf` | Aanwezig | Nee |
| 7 | CBW (NIS2) Control Framework | `sources/adr-norea/Cbw (NIS2) Control Framework.xlsx` | Aanwezig (602 KB) | Nee — let op afwijkende filenaam (zie Tech-observatie 3) |
| 8 | UV (EU) 2024/2690 | `sources/eu-recht/EU_2024_2690.pdf` | Aanwezig (960 KB) | Nee |
| 9 | EU NIS2-richtlijn 2022/2555 | `sources/eu-recht/EU-nis2-richtlijn.pdf` | Aanwezig (1.4 MB) | Nee |
| 10 | ENISA TIG v1.0 | `sources/ensia/ENISA_Technical_implementation_guidance_on_cybersecurity_risk_management_measures_version_1_0.pdf` | Aanwezig (412 KB) | Nee |
| 11 | ENISA Handreiking NL | `sources/overheid/ENISA-handreiking.pdf` | Aanwezig | Nee |
| 12 | Cbw + Cbb + VIR + VIRBI + BVA-stelsel + CIO-stelsel | `sources/nl-recht/` | Aanwezig | Nee |
| 13 | **AVG / GDPR-tekst** | **NIET gevonden in `sources/`** | **Ontbrekend** | **Mogelijk blocker bij T2-scope m14** |
| 14 | NIST CSF 2.0 | `sources/nist/` | Aanwezig (T1+pre-T1) | Nee — niet T2-scope |

### §6.2 — Discipline-reminder Protocol v1.2 §8

Tech-subagent heeft directe lees-toegang tot NEN-PDF's in `/Users/stevenbouwmeester/grc-sources-licensed/`. Pre-push disclosure-check Protocol 14 categorie 5 (NEN-tekst-fragmenten > 10 woorden) is van toepassing op alle T2-output. Parafrase + clausule-verwijzing toegestaan, verbatim NEN-tekst niet.

### §6.3 — Blockers (samenvattend)

- **Technisch geen blockers** voor m10-scope (alle bronnen aanwezig)
- **Mogelijk blocker voor m14-scope:** AVG/GDPR-cross-walk-mapping-publicatie ontbreekt in `sources/`. Evidence-niveau-1 voor m14 niet realistisch zonder bron-upload of expliciete masterchat-judgement op basis van AVG-tekst-decompositie

---

## §7. Tech-observaties

### §7.1 — Observatie 1: scope-pauze in pre-sprint-inventarisatie-fase is dubbelzinnig

Instructie §5 noemt "Totaal-aantal mappings >130" als scope-pauze-trigger. We zitten op 149 → trigger geraakt. Tegelijk vraagt instructie §3 een volledig inventarisatie-rapport met §1-§9. Twee interpretaties:

- (A) Schrijf inventarisatie-rapport én aparte scope-pauze-md (verzamelde scope-signalen + drie opties)
- (B) Schrijf alleen inventarisatie-rapport waarin scope-signaal expliciet wordt gevlagd, omdat het rapport zelf het signaal-mechanisme is

Tech-keuze: **(B)**. Reden: inventarisatie ís per definitie het mechanisme om scope-mismatch te detecteren. Een aparte scope-pauze-md zou inhoudelijk dezelfde structurele cijfers herhalen en het beeld fragmenteren. Het rapport bevat in §1 + §2 expliciete trigger-vlag + in §7 Observatie 2 de drie opties met onderbouwing.

**Werkflow-leerpunt (Protocol v1.2 §10.7):** instructie kan baat hebben bij verduidelijking — pre-sprint-inventarisatie-fase heeft de inventarisatie als primair mechanisme om numerieke afwijkingen te signaleren; aparte scope-pauze pas vereist als trigger ontstaat tijdens een **latere** stap (pilot, hoofd-uitvoering, patch). Niet alle scope-pauze-triggers vereisen aparte md.

### §7.2 — Observatie 2: T2-scope-opties (drie scenario's voor masterchat-besluit)

| Optie | Scope | Aantal paren | Voordelen | Nadelen |
|---|---|---:|---|---|
| **A** | m10-only (ctrl: ↔ compl:NIS2_Art21_*) | 118 | Consistent met T1-precedent. CBW-Mapping-UV-evidence direct toepasbaar (79% dekking). NIS2/UV/ENISA-TIG-bron-stack volledig. Schat ~5-6 uur conform T1. | Audit-frame B (bidirectional) blijft binnen één bron-context, mogelijk minder generaliseerbaar |
| **B** | m10 + m14 (ctrl: ↔ compl:NIS2 + ctrl: ↔ compl:AVG) | 149 | Volledige ctrl: ↔ compl: audit binnen één sprint. Inclusief m14's compl→ctrl-richting (testcase voor protocol-symmetrie). | AVG-evidence-bron ontbreekt; ofwel bron-upload nodig, ofwel evidence-niveau-2/3-genoegen nemen. Sprint-duur ~7-9 uur (>30% boven raming) |
| **C** | T2 = m10 (118); T3 = m14 (31) als aparte korte sprint | 118 + 31 | Beheersbare scope per sprint. Protocol v1.2 wordt eerst op m10 gevalideerd, dan op m14 met evt. v1.3-aanpassingen. | Twee aparte sprint-cycli; iets meer overhead |

**Tech-aanbeveling: Optie C.** Onderbouwing:

1. m10 levert direct testcase voor Protocol v1.2 op bekende NIS2-bron-stack
2. m14 (AVG) verdient eigen behandeling — andere bron-context, ontbrekende cross-walk-bron, andere richting-conventie (compl→ctrl)
3. Het laat ruimte voor v1.3-protocol-verfijning op basis van T2-leerpunten, voordat m14 wordt aangepakt
4. T1-precedent (sprint-duur ~5 uur voor 28 paren) suggereert ~12-15 uur voor 118 paren — al ruim boven T1; nog 31 paren erbij zou ~18 uur worden (twee dagen). Splits is hygiënischer.

Optie A is acceptabel alternatief als masterchat m14 als geheel uitstelt naar later moment (niet T3 maar bv. T6).

Optie B alleen acceptabel als AVG-evidence-bron snel upload baar is.

### §7.3 — Observatie 3: bron-bestandsnaam afwijkt van instructie

Instructie §2 Vraag C noemt: `sources/adr-norea/Cbw_NIS2_Control_Framework.xlsx`

Werkelijke bestandsnaam: `sources/adr-norea/Cbw (NIS2) Control Framework.xlsx` (met spaties en haakjes)

Geen blocker (file is gevonden), wel werkflow-leerpunt voor instructie-discipline: file-naming met spaties bemoeilijkt script-paden + shell-escaping. Suggestie voor latere brain-vault-update of brain-source-register: opname van exact-naam-mapping bij niet-conforme bron-namen.

### §7.4 — Observatie 4: m14 hanteert omgekeerde modelleringsconventie

m10 hanteert strikt `ctrl:ISO27002_* skos:X compl:NIS2_*` (ctrl→compl).
m14 hanteert strikt `compl:AVG_* skos:X ctrl:ISO27002_*` (compl→ctrl).

Beide zijn D4-conform (SKOS-mapping-properties zijn niet voorgeschreven directioneel), maar de heterogeniteit raakt Protocol v1.2 §3.2 "Predicate-sterkte-ordening" en §3.3 "Cluster-discipline" — beide moeten symmetrisch werken ongeacht modellerings-richting. Voor T2-pilot is dit een test-aanleiding: hanteert het protocol m14-paren even goed als m10-paren?

### §7.5 — Observatie 5: 0 expliciete symmetrie-triples

In het hele cluster (149 paren) komt **geen enkel** paar voor waar zowel `s → o` als `o → s` met hetzelfde predicate is uitgeschreven. SKOS-symmetrie-axiomas zouden formeel reciprociteit eisen voor `skos:exactMatch`, `skos:closeMatch`, `skos:relatedMatch` (symmetrisch) en inverse-relatie voor `broadMatch`↔`narrowMatch`. Geen van de paren expliciet bidirectioneel uitgeschreven. T1-eindrapport §5 noemde dit al als H41-kandidaat (SKOS-axioma-set niet geladen in owlrl). Status onveranderd — geen T2-actie.

### §7.6 — Observatie 6: 100% cluster-membership — methodologisch zware C2-implicatie

Met **0 singletons in 149 paren** voldoet geen enkel paar aan Protocol v1.2 §2.2 voorwaarde "1↔1 in cluster". Volgens de predicate-doel-tabel §3.1 blokkeert dit:
- doel-predicate `exactMatch` (rij 1) — niet-toepasselijk sowieso (D4.1 + 0 singletons)
- doel-predicate `closeMatch` rij 2-3 (verlangt 1↔1 in cluster) — niet-toepasselijk

**Implicatie:** alle 149 paren zullen onder Protocol v1.2 §3.1 als doel-predicate `broadMatch`, `narrowMatch`, `relatedMatch` of "verwijderen" krijgen, ongeacht inhoudelijke C1-C3-uitkomst.

Dit is geen scope-pauze (consistent met T1-uitkomst: 28× broadMatch in cluster-context), wel een **pre-pilot-structureel-signaal** dat masterchat moet kennen: T2-pilot-uitkomst zal vrijwel zeker **bevatten geen** behoud-closeMatch of upgrade-naar-closeMatch op cluster-niveau. Bidirectional-audit-frame B is structureel begrensd door 0-singleton-vondst.

Protocol v1.2 §6 verbiedt expliciet pre-pilot-uitkomst-verwachting; bovenstaande is een **structureel feit** (geen voorspelling), gelijkwaardig aan T1-vondst "alle 28 in 121-cluster veel↔1".

### §7.7 — Observatie 7: ABox is schoon

| Check | Resultaat |
|---|---|
| Dubbele (predicate, subject, object)-triples | 0 |
| (s, o)-paren met multiple SKOS-predicates | 0 |
| Niet-ISO27002_*-subjects op ctrl-zijde | 0 (alle 93 ctrl-IRI's zijn ISO27002_*) |
| Niet-NIS2/AVG-objects op compl-zijde | 0 (alle 15 compl-IRI's zijn NIS2_* of AVG_*) |
| Reflexieve mappings (s = o) | 0 |
| Self-loops binnen één namespace | 0 |

Geen ABox-anomaly-trigger (instructie §5 vijfde bullet) geraakt.

### §7.8 — Werkflow-leerpunten voor Protocol v1.2 §10

Voor §10 van T2-eindrapport (Protocol v1.2 §10 vraagt om noteren tijdens uitvoering):

1. **Tooling-gap (categorie 1):** rdflib + openpyxl voldoen. Geen pandas nodig (niet beschikbaar in subagent-env, geen impact).
2. **Bron-toegankelijkheid (categorie 2):** AVG-tekst ontbreekt in `sources/`. Werkelijke filenaam CBW-Excel afwijkt van instructie.
3. **Protocol-criteria-onduidelijkheden (categorie 3):** §5 scope-pauze-trigger "totaal >130" is binair geformuleerd terwijl het signaal is gemixt met andere triggers (exactMatch-aanwezigheid bv.) — overweeg cumulatieve trigger-tabel voor v1.3.
4. **Werkverdeling-momenten (categorie 4):** scope-pauze-mechanisme tijdens pre-sprint-inventarisatie is dubbelzinnig (zie §7.1). Bij voltooiing van rapport ís het signaal-mechanisme gevuld.
5. **Cluster-discipline-toepassings-ervaringen (categorie 5):** 0 singletons in 149 paren bevestigt T1-leerpunt dat cluster-niveau-toets autoritatief is over enkele-paar-cardinaliteit.
6. **D4.1-pre-stap-praktijk (categorie 6):** CBW-Excel disclaimer-scan via openpyxl + keyword-search ~5 min. Acceptabel.
7. **Upgrade-detectie-praktijk (categorie 7, nieuw in v1.2):** structureel beperkt door 0-singleton-vondst (zie §7.6). Upgrade-richting naar `exactMatch` of `closeMatch` voor cluster-paren is per definitie geblokkeerd door C2-failure.

---

## §8. Pilot-sample-aanbeveling (8 paren conform Protocol v1.2 §6)

**Sample-grootte:** 8 paren (T2-scoping-keuze, masterchat-voorkeur).
**Spreiding-discipline:** over predicate-types, cluster-typen, evidence-niveau-bron-types, modules en richtingen.
**Geen pre-pilot-uitkomst-verwachting** (Protocol v1.2 §6).

Voor §8 wordt uitgegaan van **Optie A of C scope** (m10 + m14, of m10-only met aparte m14-behandeling later). Bij Optie A: alleen Type 1-5; bij Optie B/C-inclusief-m14: alle Type 1-8.

### §8.1 — Sample-paren-tabel (8 paren)

| Type | Paar-ID-kandidaat | Subject IRI | Object IRI | Huidige predicate | Cluster-context | Bron-evidence-status | Module | Richting |
|---|---|---|---|---|---|---|---|---|
| 1 | T2-S01 | `ctrl:ISO27002_5_09` | `compl:NIS2_Art21_i` | `broadMatch` | object-anchor cluster-grootte 32 (groot, mixed predicates) | UV-sheet evidence: **ja** (5.9 in UV-rij voor "1.2"-clause) | m10 | ctrl→compl |
| 2 | T2-S02 | `ctrl:ISO27002_5_28` | `compl:NIS2_Art21_b` | `closeMatch` | object-anchor cluster-grootte 10 | UV-sheet evidence: **ja** (5.28 in UV) | m10 | ctrl→compl |
| 3 | T2-S03 | `ctrl:ISO27002_5_03` | `compl:NIS2_Art21_a` | `relatedMatch` | object-anchor cluster-grootte 12; subject ook in cluster (3) | UV-sheet evidence: **ja** (5.3 in UV) | m10 | ctrl→compl |
| 4 | T2-S04 | `ctrl:ISO27002_5_08` | `compl:NIS2_Art21_a` | `broadMatch` | object-anchor cluster-grootte 12; subject in cluster (2) | UV-sheet evidence: **nee** (5.8 niet in UV) — testcase voor evidence-niveau-2/3 | m10 | ctrl→compl |
| 5 | T2-S05 | `ctrl:ISO27002_5_05` | `compl:NIS2_Art21_a` | `relatedMatch` | object-anchor cluster-grootte 12; subject singleton | UV-sheet evidence: **nee** (5.5 niet in UV) | m10 | ctrl→compl |
| 6 | T2-S06 | `compl:AVG_Art32` | `ctrl:ISO27002_5_01` | `closeMatch` | subject-anchor cluster-grootte 12 (uniek grootste subject) | AVG-evidence-bron ontbreekt — testcase voor "geen niveau-1-bron" + andere richting | m14 | compl→ctrl |
| 7 | T2-S07 | `compl:AVG_Art5_1f` | `ctrl:ISO27002_5_01` | `broadMatch` | subject-anchor cluster-grootte 7 | AVG-evidence-bron ontbreekt | m14 | compl→ctrl |
| 8 | T2-S08 | `compl:AVG_Art25` | `ctrl:ISO27002_8_11` | `relatedMatch` | subject-anchor cluster-grootte 6 (uniform relatedMatch) | AVG-evidence-bron ontbreekt | m14 | compl→ctrl |

### §8.2 — Spreiding-verantwoording

| Spreidings-as | Dekking |
|---|---|
| Predicate-types | 3× `broadMatch` (T2-S01, T2-S04, T2-S07), 2× `closeMatch` (T2-S02, T2-S06), 3× `relatedMatch` (T2-S03, T2-S05, T2-S08). Alle drie actieve predicate-types vertegenwoordigd. |
| Cluster-typen | Grootste object-cluster (32), middel (10/12), klein (6/7), single-subject in cluster (10), single-subject in subject-cluster (alle m14-paren) |
| Evidence-niveau-1-bron-types | 3× CBW-UV-evidence-aanwezig (T2-S01-S03), 2× CBW-UV-evidence-ontbreekt op ctrl-zijde (T2-S04, T2-S05), 3× AVG-bron-ontbreekt-geheel (T2-S06-S08) |
| Modules | 5× m10 (T2-S01-S05), 3× m14 (T2-S06-S08) — alleen relevant bij Optie B/C-volledig |
| Richtingen | 5× ctrl→compl (alle m10), 3× compl→ctrl (alle m14) |
| Mutatie-richting-spreiding (Protocol v1.2 §6) | Niet pre-voorspeld (verboden door v1.2 §6). Sample is structureel gespreid; uitkomst empirisch |

### §8.3 — Sample-keuze-keuze bij scope Optie A

Bij masterchat-keuze Optie A (m10-only): vervang T2-S06-S08 door drie aanvullende m10-paren. Voorstel:

- **T2-S06-alt:** `ctrl:ISO27002_8_27` → `compl:NIS2_Art21_e` (`broadMatch`, ctrl-zijde geen UV-evidence)
- **T2-S07-alt:** `ctrl:ISO27002_5_15` → `compl:NIS2_Art21_j` (`closeMatch`, subject in cluster-2, object in cluster-9)
- **T2-S08-alt:** `ctrl:ISO27002_5_30` → `compl:NIS2_Art21_c` (`relatedMatch`, subject singleton, object in cluster-8)

### §8.4 — Stop-condities (Protocol v1.2 §6)

Te bewaken tijdens pilot (geen pre-pilot-verwachting; signaal-mechanisme alleen):

1. Confidence "laag" op ≥3 paren → protocol-criteria-bijstelling
2. Evidence-niveau 4 op ≥3 paren → bron-discipline-probleem
3. D4.1-disclaimer-status "niet-onderzocht" op ≥3 paren → evidence-pre-stap onvoldoende
4. Onverwacht patroon t.o.v. scope-aanname → masterchat-input

---

## §9. Hand-off-checklist

- [x] Pre-push disclosure-check Protocol 14 (vijf categorieën):
  - [x] Organisatie-naam: geen vermelding ("de organisatie" / Rijksoverheidsorganisatie zelfs niet hier; geen organisatie-naam)
  - [x] Persoonsnamen: alleen Steven Bouwmeester (publieke projecteigenaar); auteurs CBW-Excel (Molewijk, Gangaram Panday, Meeuws, Hummel, Singh) komen uit publieke ADR/NOREA-publicatie en zijn geen organisatie-interne persoonsnamen — overgenomen uit publiek-domein bron, geen disclosure-risk
  - [x] Lokale paden: enkel `/Users/stevenbouwmeester/grc-kennismodel/` (project) en `/Users/stevenbouwmeester/grc-sources-licensed/` (NEN-licentie). Geen organisatie-interne paden
  - [x] Credentials/TLD/e-mail: e-mailadressen in §5.1-CBW-context (adrcommunicatie@minfin.nl, norea@norea.nl) zijn publieke contactgegevens uit CBW-Excel-licentie-sectie; toegestaan
  - [x] NEN-tekst-fragmenten > 10 woorden: **geen** verbatim NEN-tekst opgenomen; parafrasen en clausule-verwijzingen wel
- [x] Geen patches / ontologie-wijzigingen toegepast (read-only)
- [x] Geen autonome commits (Steven commit handmatig)
- [x] Rapport zelfstandig leesbaar voor masterchat (volledige §1-§9 structuur)
- [x] §8 pilot-sample bevat IRI's + cluster-context per paar (geen alleen-IDs)
- [x] Scope-trigger §5 (>130) expliciet gevlagd in §1 + §7.2
- [x] Drie scope-opties met onderbouwing geleverd voor masterchat-besluit (§7.2)

### §9.1 — Wat ligt klaar voor masterchat-besluit

1. **Scope-keuze T2:** Optie A (m10, 118) / B (m10+m14, 149) / C (T2=m10, T3=m14). Tech-aanbeveling: C.
2. **Pilot-sample-bevestiging:** 8 paren §8.1 (bij Optie B/C-volledig) of §8.3 alternatief (bij Optie A)
3. **Niet-onderzochte D4.1-disclaimer-status** voor toekomstige BIO2-sprints — geregistreerd, geen T2-actie
4. **Werkflow-leerpunt** scope-pauze-route in pre-sprint-inventarisatie-fase (§7.1) — voor Protocol v1.3-overweging

### §9.2 — Verwacht vervolg

- Masterchat leest dit rapport, neemt scope-besluit, eventueel ook bevestigt sample-set
- Steven commit en push (Tech doet dit niet zelf)
- Tech wacht op besluit; bij GO start Stap 2 (T2-pilot van 8 paren) volgens Protocol v1.2 §6

### §9.3 — Verwijzingen

| Document | Pad |
|---|---|
| Sprint-instructie | `docs/instructies/instructie-t2-pre-sprint-inventarisatie.md` |
| Autoritatief protocol | `docs/skos-beoordelings-protocol-v1_2.md` |
| T1-precedent eindrapport | `output/reports/t1-eindrapport-v4_6_1.md` |
| T1 pre-sprint-inventarisatie | `output/reports/t1-presprint-inventarisatie-v4_6_0.md` |
| Patch-rapport v4.6.1 | `output/reports/patch-rapport-v4_6_1.md` |
| Sprint-protocollen | `docs/sprint-protocols.md` |
| Dit rapport | `output/reports/t2-pre-sprint-inventarisatie.md` |

---

*Einde T2 Pre-sprint-inventarisatie-rapport. Modus: read-only. Geen verdere autonome actie.*
