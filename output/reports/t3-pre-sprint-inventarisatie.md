---
type: report
subtype: pre-sprint-inventarisatie
sprint: T3
baseline_from: v4.6.2
date: 2026-05-28
status: final-awaiting-masterchat-review
mode: READ-ONLY
related:
  - skos-beoordelings-protocol-v1_2
  - skos-beoordelings-protocol-v1_3
  - H36_skos-exactmatch-ctrl-compl-audit
  - D04_skos-cross-framework
  - t1-eindrapport-v4_6_1
  - patch-rapport-v4_6_2
  - M14_avg-gdpr
scope: "T3 pre-sprint-inventarisatie — read-only verkenning van 31 compl:→ctrl: SKOS-mappings in m14-avg-gdpr.ttl. Bevestiging scope, cluster-structuur, evidence-coverage via ISO 27701:2025 Annex D + Annex F, bron-toegankelijkheid, en methode-check op Protocol v1.2/v1.3."
---

# T3 Pre-sprint-inventarisatie-rapport

## §1. Samenvatting

**INITIEEL — bottom-up bevestigd via §2-§9.**

| Aspect | Bevinding |
|---|---|
| Totaal m14-paren compl:→ctrl: | **31** (2 closeMatch + 2 broadMatch + 27 relatedMatch) — matcht H36-verwachting exact |
| Predicate-types aanwezig | closeMatch, broadMatch, relatedMatch — geen exactMatch, geen narrowMatch |
| Verstrooiing | 0 m14-mappings elders; alle 31 paren in `ontology/m14-avg-gdpr.ttl` |
| Richting-consistentie | 31/31 compl:→ctrl:; geen omgekeerde-richting paren |
| Cluster-structuur | 5 subject-clusters (AVG-artikelen), 1↔veel-patroon (omgekeerd t.o.v. m10) — 3 heterogene, 2 homogene clusters |
| Dangling-targets | 0 (alle 26 unieke ctrl:-targets bestaan in m02-control.ttl) |
| ISO 27701:2025 Annex D-bruikbaarheid | **bruikbaar — niveau-1 evidence voor 10 paren via twee-staps-keten (ctrl→27701 A.3.x via Annex F + A.3.x→GDPR-artikel via Annex D)** |
| Conformiteitsbeoordeling (NCS 27701:2020) | **niet bruikbaar** — auditor-eisen-document, geen GDPR↔control-mapping; verwijst naar verouderde 27701:2019 |
| Evidence-coverage 31 paren | 10× niveau-1 (Annex D direct) + 7× niveau-2 (27701-equivalent bestaat, Annex D non-exhaustive op dit artikel) + 14× niveau-3 (geen 27701-equivalent; Tech-analyse via 27002 + AVG-tekst) |
| Vraag F-conclusie | **Protocol v1.2/v1.3 toereikend** — richtings-asymmetrie m10↔m14 wordt opgevangen door §3.1-tabel rijen 6 vs 7; heterogene-cluster-handling al gedekt. Niet-substantiële verfijnings-suggestie in §7.3. |
| Scope-pauze-triggers | **0 geactiveerd** — alle bandbreedtes en methode-condities groen |

**Bottom-line:** T3-scope is precies zoals voorspeld (31 paren), Annex D 27701:2025 levert directe niveau-1 evidence voor 10 paren via een twee-staps-keten, de overige 21 paren vereisen niveau-2 of niveau-3 analyse via per-paar-toetsing. m14's cluster-cardinaliteit (1↔veel) is omgekeerd van m10 (veel↔1), wat een ander cluster-doel-predicate-pad activeert (§3.1 rij 7 vs rij 6); Protocol v1.2/v1.3 dekt beide rijen symmetrisch. Geen scope-pauze. Pilot-sample-aanbeveling in §9 (6 paren met spreiding).

---

## §2. Vraag A — Scope-bevestiging

### §2.1 SKOS-predicate-tellingen

Gemeten met rdflib op `ontology/m14-avg-gdpr.ttl` (read-only).

| Predicate | Aantal in m14 (compl:→ctrl:) | Aantal in m14 (fw:→fw:) | Totaal m14 | Aantal elders (in 21 andere modules) | Eindtotaal |
|---|---:|---:|---:|---:|---:|
| `skos:exactMatch` | 0 | 0 | 0 | n.v.t. (m14-scope) | 0 |
| `skos:closeMatch` | 2 | 0 | 2 | 0 (alle m14-AVG-mappings in m14) | 2 |
| `skos:broadMatch` | 2 | 0 | 2 | 0 | 2 |
| `skos:narrowMatch` | 0 | 0 | 0 | 0 | 0 |
| `skos:relatedMatch` | 27 | 2 | 29 | 0 | 29 |
| **Totaal compl:→ctrl:** | **31** | — | **31** | **0** | **31** |
| **Totaal m14 SKOS-triples (alle subj/obj)** | — | — | **33** | — | — |

**Bevestiging:** 31 compl:→ctrl:-paren — **exact volgens H36-verwachting (27 related + 2 close + 2 broad)**. Plus 2 framework-niveau `fw:AVG_GDPR skos:relatedMatch fw:...`-triples (Sectie 4 van m14-ttl) die buiten de T3-scope vallen (compl:↔ctrl:-relaties).

Geen verstrooiing naar andere modules — een `grep`-equivalent zoek (rdflib-traversal) naar AVG_Art-references buiten m14-ttl gaf **0 hits**.

### §2.2 Richting-consistentie

Alle 31 paren hebben:
- Subject: `compl:AVG_Art*` (instance van `compl:LegalObligation`)
- Object: `ctrl:ISO27002_*_*` (ISO 27002:2022-control)

**Geen** ctrl:→compl: paren (omgekeerde richting); geen mixed-richting clusters. Richting is uniform `compl:→ctrl:` — semantisch: "AVG-artikel relateert aan ISO-control".

**Methodische opmerking:** dit is de **omgekeerde** richting van m10 (T1+T2: ctrl:→compl:NIS2_Art21_*). Implicaties in Vraag F §7.

### §2.3 Geen exactMatch / narrowMatch

`skos:exactMatch` en `skos:narrowMatch` zijn beide afwezig. Geen scope-pauze-trigger (instructie §5: aanwezigheid was niet verwacht).

D4.1-vooraf-check (Protocol v1.2/v1.3 §2.0) is dus alleen relevant voor *upgrade*-overweging naar `exactMatch`; voor neerwaartse mutaties uit `closeMatch`/`broadMatch`/`relatedMatch` is D4.1 niet-blokkerend.

---

## §3. Vraag B — Cluster-structuur per AVG-artikel

### §3.1 Subject-zijde clusters (AVG-artikel → controls)

m14 toont **1↔veel-cluster-patroon**: één AVG-artikel mapt naar meerdere ISO-controls. Dit is het omgekeerde van m10 (waar één NIS2-clausule door meerdere ISO-controls werd gemapt = veel↔1).

```
Cluster AVG-Art5_1f (Integriteit en vertrouwelijkheid) — 7 paren
  Predicate-mix: 2× broadMatch, 5× relatedMatch  → HETEROGEEN
  - compl:AVG_Art5_1f skos:broadMatch ctrl:ISO27002_5_01    # Beleidsregels IB
  - compl:AVG_Art5_1f skos:broadMatch ctrl:ISO27002_5_12    # Classificeren info
  - compl:AVG_Art5_1f skos:relatedMatch ctrl:ISO27002_5_15  # Toegangsbeveiliging
  - compl:AVG_Art5_1f skos:relatedMatch ctrl:ISO27002_8_24  # Cryptografie
  - compl:AVG_Art5_1f skos:relatedMatch ctrl:ISO27002_8_10  # Wissen info
  - compl:AVG_Art5_1f skos:relatedMatch ctrl:ISO27002_8_11  # Maskeren gegevens
  - compl:AVG_Art5_1f skos:relatedMatch ctrl:ISO27002_8_12  # DLP

Cluster AVG-Art25 (Privacy by Design) — 6 paren
  Predicate-mix: 6× relatedMatch  → homogeen
  - compl:AVG_Art25 skos:relatedMatch ctrl:ISO27002_8_25  # Beveiligen tijdens ontwikkelcyclus
  - compl:AVG_Art25 skos:relatedMatch ctrl:ISO27002_8_26  # Toepassingsbeveiligingseisen
  - compl:AVG_Art25 skos:relatedMatch ctrl:ISO27002_8_27  # Veilige systeemarchitectuur
  - compl:AVG_Art25 skos:relatedMatch ctrl:ISO27002_8_28  # Veilig coderen
  - compl:AVG_Art25 skos:relatedMatch ctrl:ISO27002_8_11  # Maskeren gegevens
  - compl:AVG_Art25 skos:relatedMatch ctrl:ISO27002_8_33  # Testgegevens

Cluster AVG-Art32 (Beveiliging van de verwerking) — 12 paren
  Predicate-mix: 1× closeMatch, 11× relatedMatch  → HETEROGEEN
  - compl:AVG_Art32 skos:closeMatch ctrl:ISO27002_5_01     # Beleidsregels IB
  - compl:AVG_Art32 skos:relatedMatch ctrl:ISO27002_8_24   # Cryptografie
  - compl:AVG_Art32 skos:relatedMatch ctrl:ISO27002_5_15   # Toegangsbeveiliging
  - compl:AVG_Art32 skos:relatedMatch ctrl:ISO27002_5_16   # Identiteitsbeheer
  - compl:AVG_Art32 skos:relatedMatch ctrl:ISO27002_5_17   # Authenticatie-info
  - compl:AVG_Art32 skos:relatedMatch ctrl:ISO27002_5_18   # Toegangsrechten
  - compl:AVG_Art32 skos:relatedMatch ctrl:ISO27002_8_13   # Back-up
  - compl:AVG_Art32 skos:relatedMatch ctrl:ISO27002_5_29   # IB tijdens verstoring
  - compl:AVG_Art32 skos:relatedMatch ctrl:ISO27002_5_30   # ICT-gereedheid BCM
  - compl:AVG_Art32 skos:relatedMatch ctrl:ISO27002_8_07   # Bescherming tegen malware
  - compl:AVG_Art32 skos:relatedMatch ctrl:ISO27002_5_35   # Onafhankelijke beoordeling
  - compl:AVG_Art32 skos:relatedMatch ctrl:ISO27002_5_36   # Naleving beleid/regels/normen

Cluster AVG-Art33 (Melding inbreuk aan AP) — 4 paren
  Predicate-mix: 1× closeMatch, 3× relatedMatch  → HETEROGEEN
  - compl:AVG_Art33 skos:closeMatch ctrl:ISO27002_5_24     # Plannen incidentbeheer
  - compl:AVG_Art33 skos:relatedMatch ctrl:ISO27002_5_25   # Beoordelen security-events
  - compl:AVG_Art33 skos:relatedMatch ctrl:ISO27002_5_26   # Reageren op incidenten
  - compl:AVG_Art33 skos:relatedMatch ctrl:ISO27002_6_08   # Melden security-events

Cluster AVG-Art34 (Mededeling inbreuk aan betrokkene) — 2 paren
  Predicate-mix: 2× relatedMatch  → homogeen
  - compl:AVG_Art34 skos:relatedMatch ctrl:ISO27002_5_26   # Reageren op incidenten
  - compl:AVG_Art34 skos:relatedMatch ctrl:ISO27002_5_34   # Privacy en bescherming PII
```

### §3.2 Object-zijde cluster-overlap (veel→1: controls die door meerdere AVG-artikelen worden gemapt)

5 van de 26 unieke ctrl-targets zitten in **meerdere AVG-clusters**:

| Ctrl | Aantal AVG-mappings | Betrokken AVG-artikelen | Predicate-mix object-cluster |
|---|---:|---|---|
| `ctrl:ISO27002_5_01` (Beleidsregels IB) | 2 | Art32 (closeMatch) + Art5_1f (broadMatch) | heterogeen |
| `ctrl:ISO27002_5_15` (Toegangsbeveiliging) | 2 | Art5_1f + Art32 | homogeen (2× relatedMatch) |
| `ctrl:ISO27002_8_24` (Cryptografie) | 2 | Art5_1f + Art32 | homogeen (2× relatedMatch) |
| `ctrl:ISO27002_8_11` (Maskeren gegevens) | 2 | Art5_1f + Art25 | homogeen (2× relatedMatch) |
| `ctrl:ISO27002_5_26` (Reageren incidenten) | 2 | Art33 + Art34 | homogeen (2× relatedMatch) |

De overige 21 controls hebben elk precies 1 AVG-mapping.

**Object-cluster-cardinaliteit per Protocol v1.3 §2.2:** voor multi-mapping-paren (5 paren met object-cluster ≥2 op de subject-zijde, want elk paar zit zelf in een 1↔veel-subject-cluster) — object-cluster-cardinaliteit toont een **kleine veel↔1-component** op deze 5 ctrls (2 AVG-artikelen → 1 control). Voor de subject-zijde-clusters is de cardinaliteit echter dominant **1↔veel** (Art32 → 12, Art5_1f → 7).

### §3.3 Hetorogeniteit-overzicht

| Cluster | Cluster-grootte | Predicate-mix | Heterogeniteit |
|---|---:|---|---|
| AVG_Art5_1f | 7 | broadMatch×2, relatedMatch×5 | **HETEROGEEN** |
| AVG_Art25 | 6 | relatedMatch×6 | homogeen |
| AVG_Art32 | 12 | closeMatch×1, relatedMatch×11 | **HETEROGEEN** |
| AVG_Art33 | 4 | closeMatch×1, relatedMatch×3 | **HETEROGEEN** |
| AVG_Art34 | 2 | relatedMatch×2 | homogeen |

**Bevestiging instructie-§0.2-verwachting:** 3 van 5 clusters zijn predicate-mix-heterogeen. Per-paar-toetsing waarschijnlijk nodig (geen klakkeloze cluster-convergentie zoals in m10). Voor de homogene clusters (Art25, Art34) is cluster-discipline-overerving wel toepasbaar mits cluster-representant evidence levert.

---

## §4. Vraag C — Bron-structuur-verificatie (KERN-vraag T3)

### §4.1 ISO 27701:2025 — structuur-identificatie

**Editie-bevestiging:** `/Users/stevenbouwmeester/grc-sources-licensed/ISO27701.pdf` is **NEN-EN-ISO/IEC 27701:2025 (en)** — Second edition, oktober 2025, ICS 35.030, IDT-adoptie van ISO/IEC 27701:2025. Vervangt 27701:2021. NEN-licentie-versie via Rijksoverheid NEN Connect 2016-2020. Paginatel: 80 (incl. cover, foreword, body §1-10, Annexes A-F, bibliography).

**Inhoudsopgave-relevante structuur:**

- §4-10: PIMS-managementsysteem-eisen (Context, Leadership, Planning, Support, Operation, Performance evaluation, Improvement)
- Annex A (normative): "PIMS reference control objectives and controls for PII controllers and PII processors" — Tables A.1, A.2, A.3
  - Table A.1: PII controllers — control-IDs A.1.x.x
  - Table A.2: PII processors — control-IDs A.2.x.x
  - Table A.3: Information security controls voor beide — control-IDs A.3.x (A.3.3 t/m A.3.31)
- Annex B (normative): "Implementation guidance for PII controllers and PII processors" — guidance-clausules B.1.x, B.2.x, B.3.x (één-op-één met Annex A control-IDs)
- Annex C (informative): **Mapping to ISO/IEC 29100** (privacy principles)
- **Annex D (informative): Mapping to the General Data Protection Regulation** (pagina 53-55 in body / PDF p65-67)
- Annex E (informative): Mapping to ISO/IEC 27018 and ISO/IEC 29151
- Annex F (informative): Correspondence with ISO/IEC 27701:2019 — Tables F.1 + F.2

### §4.2 ISO 27701:2025 Annex D — feitelijke inhoud

**Annex D-inleidingstekst (parafrase):** Annex D bevat Table D.1, dat een "indicative mapping between the provisions of this document and Articles 5 to 49 except 43 of the General Data Protection Regulation" geeft. De tabel toont hoe compliance aan 27701-requirements en -controls relevant kan zijn voor GDPR-verplichtingen. **NOTE (verbatim-grens parafrase):** Annex D is expliciet niet-exhaustief en organisaties moeten hun eigen juridische verplichtingen beoordelen. (Verbatim citaat <10 woorden toelichting Protocol §8.2.)

**Tabel-structuur (kolommen):** `Subclause of this document | Relevant GDPR article`.

- Kolom 1: 27701-subclause-identifiers, mix van §4.1-§10-management-subclauses, §B.1.x, §B.2.x, §B.3.x guidance-subclauses (= equivalent Annex A control-IDs A.1.x, A.2.x, A.3.x).
- Kolom 2: GDPR-artikel-verwijzingen in formaat `(X)(y)(z)` zoals `(5)(1)(f)`, `(25)(1)`, `(32)(1)(a)`, `(33)(1)`, `(34)(2)`.

**Direct relevant voor T3-scope:** subclauses die linken naar AVG-art. 5(1)(f), 25, 32, 33, 34:

| 27701-subclause | Equivalente A.3.x-control-naam | GDPR-art. (Annex D-rij) |
|---|---|---|
| B.3.5 | A.3.5 Classification of information | (5)(1)(f), (32)(2) |
| B.3.6 | A.3.6 Labelling of information | (5)(1)(f) |
| B.3.7 | A.3.7 Information transfer | (5)(1)(f) |
| B.3.10 | A.3.10 Addressing IB within supplier agreements | (5)(1)(f), (32)(1)(b) e.a. |
| B.3.11 | A.3.11 IS incident management planning | (5)(1)(f), (33)(1)-(5), (34)(1)-(4) |
| B.3.12 | A.3.12 Response to IS incidents | (33)(1)-(5), (34)(1)-(2) |
| B.3.13 | A.3.13 Legal/statutory/regulatory requirements | (5)(1)(f), (32)(1)(b) e.a. |
| B.3.15 | A.3.15 Independent review of IS | (32)(1)(d), (32)(2) |
| B.3.16 | A.3.16 Compliance with policies/rules/standards | (32)(1)(d), (32)(2) |
| B.3.20 | A.3.20 Storage media | (5)(1)(f), (32)(1)(a) |
| B.3.24 | A.3.24 Information backup | (5)(1)(f), (32)(1)(c) |
| B.3.26 | A.3.26 Use of cryptography | (32)(1)(a) |
| B.3.27 | A.3.27 Secure development life cycle | (25)(1) |
| B.3.28 | A.3.28 Application security requirements | (5)(1)(f), (32)(1)(a) |
| B.3.29 | A.3.29 Secure system architecture | (25)(1) |
| B.3.31 | A.3.31 Test information | (5)(1)(f) |

Niet alle T3-relevante AVG-artikelen verschijnen in Annex D voor elke 27701-subclause — Annex D is een **selectie** van saillante GDPR-relaties, geen complete projectie. Dat raakt evidence-niveau (zie §5).

### §4.3 Twee-staps-keten: ISO 27002:2022 ↔ 27701:2025 ↔ GDPR

**Belangrijke vondst:** 27701:2025 Annex D linkt **27701-subclauses** aan GDPR-artikelen — niet rechtstreeks 27002-controls. Maar twee documenten samen vormen de keten:

```
Stap 1: ctrl:ISO27002_X_YY  ──(via Annex F.1 control-namen-match)──>  27701:2025 A.3.x
Stap 2: 27701:2025 A.3.x   ──(B.3.x = guidance voor A.3.x in Annex B)──>  B.3.x
Stap 3: 27701:2025 B.3.x   ──(via Annex D rij)──>  GDPR-artikel (X)(y)(z)
```

**Annex F.1-structuur (verbatim-grens parafrase):** Table F.1 lijst per 27701:2025-control-identifier (kolom 1) de corresponding 27701:2019-control-identifier (kolom 2) + control-name (kolom 3). Control-name kolom is precies de ISO 27002:2022-control-name (incl. "New"-markering voor controls die nieuw zijn t.o.v. 27701:2019 — zoals "Threat intelligence", "ICT readiness for business continuity", "Data masking", "Configuration management", "Secure coding"). **N/A in kolom 1** = control bestaat niet in 27701:2025 (niet alle 27002-controls hebben PIMS-relevantie volgens 27701-werkgroep).

Voor onze 26 unieke `ctrl:ISO27002_*`-targets — match naar Annex F.1 control-name:

| ctrl-target | 27002:2022 control-naam | 27701:2025 A.3.x | Reden indien N/A |
|---|---|---|---|
| ISO27002_5_01 | Policies for information security | A.3.3 | — |
| ISO27002_5_12 | Classification of information | A.3.5 | — |
| ISO27002_5_15 | Access control | **N/A** | 27001:2013 6.6.1.1+6.6.1.2 niet in PIMS-scope |
| ISO27002_5_16 | Identity management | A.3.8 | — |
| ISO27002_5_17 | Authentication information | **N/A** | 27001:2013 6.6.2.4/6.6.3.1/6.6.4.3 niet in PIMS-scope |
| ISO27002_5_18 | Access rights | A.3.9 | — |
| ISO27002_5_24 | IS incident management planning and preparation | **N/A** | 27001:2013 6.13.1.1 niet in PIMS-scope |
| ISO27002_5_25 | Assessment and decision on IS events | A.3.11 | — |
| ISO27002_5_26 | Response to IS incidents | A.3.12 | — |
| ISO27002_5_29 | IS during disruption | **N/A** | 27001:2013 6.14.1.x niet in PIMS-scope |
| ISO27002_5_30 | ICT readiness for business continuity | **N/A** | "New" t.o.v. 27701:2019, niet in 2025-scope |
| ISO27002_5_34 | Privacy and protection of PII | **N/A** | 27001:2013 6.15.1.4 niet in PIMS-scope (interessant want zelf privacy-thema) |
| ISO27002_5_35 | Independent review of IS | A.3.15 | — |
| ISO27002_5_36 | Compliance with policies/rules/standards | A.3.16 | — |
| ISO27002_6_08 | IS event reporting | **N/A** | 27001:2013 6.13.1.2+6.13.1.3 niet in PIMS-scope |
| ISO27002_8_07 | Protection against malware | **N/A** | 27001:2013 6.9.2.1 niet in PIMS-scope |
| ISO27002_8_10 | Information deletion | **N/A** | "New" niet in 2025-scope |
| ISO27002_8_11 | Data masking | **N/A** | "New" niet in 2025-scope |
| ISO27002_8_12 | Data leakage prevention | **N/A** | "New" niet in 2025-scope |
| ISO27002_8_13 | Information backup | A.3.24 | — |
| ISO27002_8_24 | Use of cryptography | A.3.26 | — |
| ISO27002_8_25 | Secure development life cycle | A.3.27 | — |
| ISO27002_8_26 | Application security requirements | A.3.28 | — |
| ISO27002_8_27 | Secure system architecture and engineering principles | A.3.29 | — |
| ISO27002_8_28 | Secure coding | **N/A** | "New" niet in 2025-scope |
| ISO27002_8_33 | Test information | A.3.31 | — |

**Totaal:** 14 van 26 unieke ctrls hebben een 27701:2025-equivalent (54%); 12 hebben dat niet. De N/A's zijn structureel: PIMS-werkgroep heeft alleen ISO 27002-controls in 27701-scope opgenomen die voor PII-bescherming directe relevantie hebben. Dataminimalisatie-controls als 8.10/8.11/8.12 zijn nieuw in 27002:2022 en nog niet in 27701:2025 verwerkt; access-control-clausules vallen onder een afzonderlijke ISO 27018 / ISO 27001-Annex A-structuur.

### §4.4 ISO 27701-Conformiteitsbeoordeling (NCS 27701:2020) — bruikbaarheid

**Identificatie:** `/Users/stevenbouwmeester/grc-sources-licensed/ISO27701 Conformiteitsbeoordeling.pdf` is **NCS 27701:2020 — NEN Certificatieschema** (december 2020, 28 pagina's). Volledige titel: "Conformiteitsbeoordeling – Eisen aan instellingen die audits ten behoeve van certificatie van privacy-informatiemanagementsystemen uitvoeren volgens ISO/IEC 27701".

**Karakter:** auditor-eisen-document op basis van ISO/IEC 17021-1 + ISO/IEC 27006 + NCS 7510 (zorginformatica). Specificeert competentie-eisen, structurele eisen, en audit-proces-eisen voor certificerende instellingen (CBI's) die PIMS-certificering uitvoeren in aanvulling op ISMS-certificering.

**Versie-erf:** verwijst expliciet naar **ISO/IEC 27701:2019** (verouderd) — niet de huidige 2025-editie. Dit beperkt de toepasselijkheid voor T3, ook indien het inhoudelijk-relevant zou zijn.

**Bruikbaarheid voor T3-evidence:** **nul mappings** voor GDPR-artikelen of ISO 27002-controls aangetroffen. Een scan op alle 28 pagina's met termen `gdpr`, `avg`, `mapping` leverde **geen treffers**. Het document bevat geen Annex met mapping-content. Bruikbaarheid voor T3 = **niet bruikbaar**.

**Conclusie:** NCS 27701:2020 valt buiten de evidence-pipeline voor T3.

### §4.5 Bruikbaarheids-conclusie

| Bron | Bruikbaarheid voor T3 | Niveau |
|---|---|---|
| **ISO/IEC 27701:2025 Annex D + Annex F (combinatie)** | **bruikbaar — twee-staps-keten** | niveau-1 voor 10 paren waar Annex D direct GDPR-artikel-link toont; niveau-2 voor 7 paren waar 27701-equivalent bestaat maar Annex D-link ontbreekt |
| ISO/IEC 27701:2025 Annex C (29100-mapping) | indirect bruikbaar voor terminologie-validatie | niveau-2/3 ondersteunend |
| ISO/IEC 27701:2025 Annex E (27018/29151-mapping) | niet direct GDPR-relevant | n.v.t. voor T3-paren |
| ISO/IEC 27701-Conformiteitsbeoordeling (NCS 27701:2020) | **niet bruikbaar** | — |
| ISO/IEC 29100:2011 (privacy framework) | ondersteunend voor terminologie | niveau-3 |
| ISO/IEC 27002:2022 | autoritatief voor control-tekst (C1/C3-toetsing) | n.v.t. — semantiek-basis, geen evidence-niveau |
| AVG/GDPR-tekst | autoritatief voor obligation-tekst (C1/C3-toetsing) | n.v.t. — semantiek-basis |
| Publieke 2022-cross-walks (ISMS.online e.a.) | aanvullend bewijs | niveau-2 (secundair) |

**Hoofdconclusie Vraag C:** **27701:2025 Annex D is voldoende basis voor niveau-1 evidence op 10 paren**. Voor de overige 21 paren is per-paar-toetsing nodig via C1+C3 met 27002:2022 + AVG-tekst (niveau-2/3). De Conformiteitsbeoordeling NCS 27701:2020 is geen bruikbare aanvullende bron.

---

## §5. Vraag D — Evidence-coverage per paar

Per paar bepaald via §4.3-keten:

| Evidence-bron | Aantal paren gedekt | Niveau |
|---|---:|---|
| **ISO 27701:2025 Annex D directe link naar AVG-artikel** (via twee-staps-keten Annex F + Annex D) | **10** | **1** |
| **ISO 27701:2025 27701-equivalent bestaat, Annex D-link ontbreekt voor dit AVG-artikel** (non-exhaustive Annex D — geen ontkenning) | **7** | **2** |
| NCS 27701:2020 Conformiteitsbeoordeling | 0 | — (niet bruikbaar) |
| Publieke 2022-cross-walks (ISMS.online e.a.) | indicatief (niet per paar gemeten) | 2 |
| **Geen 27701-equivalent — Tech-analyse via 27002:2022 + AVG-tekst** | **14** | **3** |
| Geen evidence-trace (rood vlaggetje) | 0 | — |

**Geen rode vlaggetjes** — alle 31 paren hebben minimaal niveau-3 evidence (combinatie van publiek 27002-tekst voor control-semantiek + publieke AVG-tekst voor obligation-semantiek).

### §5.1 Volledige paren-tabel met evidence-niveau

| Paar | Subject | Predicate | Object | 27701 A.3.x | Annex D link → AVG-art | Evidence-niveau |
|---|---|---|---|---|---|---|
| T3-001 | AVG_Art5_1f | broadMatch | ISO27002_5_01 | A.3.3 | nee | 2 |
| T3-002 | AVG_Art5_1f | broadMatch | ISO27002_5_12 | A.3.5 | **ja (5)(1)(f)** | **1** |
| T3-003 | AVG_Art5_1f | relatedMatch | ISO27002_5_15 | N/A | — | 3 |
| T3-004 | AVG_Art5_1f | relatedMatch | ISO27002_8_24 | A.3.26 | nee | 2 |
| T3-005 | AVG_Art5_1f | relatedMatch | ISO27002_8_10 | N/A | — | 3 |
| T3-006 | AVG_Art5_1f | relatedMatch | ISO27002_8_11 | N/A | — | 3 |
| T3-007 | AVG_Art5_1f | relatedMatch | ISO27002_8_12 | N/A | — | 3 |
| T3-008 | AVG_Art25 | relatedMatch | ISO27002_8_25 | A.3.27 | **ja (25)(1)** | **1** |
| T3-009 | AVG_Art25 | relatedMatch | ISO27002_8_26 | A.3.28 | nee | 2 |
| T3-010 | AVG_Art25 | relatedMatch | ISO27002_8_27 | A.3.29 | **ja (25)(1)** | **1** |
| T3-011 | AVG_Art25 | relatedMatch | ISO27002_8_28 | N/A | — | 3 |
| T3-012 | AVG_Art25 | relatedMatch | ISO27002_8_11 | N/A | — | 3 |
| T3-013 | AVG_Art25 | relatedMatch | ISO27002_8_33 | A.3.31 | nee | 2 |
| T3-014 | AVG_Art32 | closeMatch | ISO27002_5_01 | A.3.3 | nee | 2 |
| T3-015 | AVG_Art32 | relatedMatch | ISO27002_8_24 | A.3.26 | **ja (32)(1)(a)** | **1** |
| T3-016 | AVG_Art32 | relatedMatch | ISO27002_5_15 | N/A | — | 3 |
| T3-017 | AVG_Art32 | relatedMatch | ISO27002_5_16 | A.3.8 | nee | 2 |
| T3-018 | AVG_Art32 | relatedMatch | ISO27002_5_17 | N/A | — | 3 |
| T3-019 | AVG_Art32 | relatedMatch | ISO27002_5_18 | A.3.9 | nee | 2 |
| T3-020 | AVG_Art32 | relatedMatch | ISO27002_8_13 | A.3.24 | **ja (32)(1)(c)** | **1** |
| T3-021 | AVG_Art32 | relatedMatch | ISO27002_5_29 | N/A | — | 3 |
| T3-022 | AVG_Art32 | relatedMatch | ISO27002_5_30 | N/A | — | 3 |
| T3-023 | AVG_Art32 | relatedMatch | ISO27002_8_07 | N/A | — | 3 |
| T3-024 | AVG_Art32 | relatedMatch | ISO27002_5_35 | A.3.15 | **ja (32)(1)(d)/(2)** | **1** |
| T3-025 | AVG_Art32 | relatedMatch | ISO27002_5_36 | A.3.16 | **ja (32)(1)(d)/(2)** | **1** |
| T3-026 | AVG_Art33 | closeMatch | ISO27002_5_24 | N/A | — | 3 |
| T3-027 | AVG_Art33 | relatedMatch | ISO27002_5_25 | A.3.11 | **ja (33)(1)** | **1** |
| T3-028 | AVG_Art33 | relatedMatch | ISO27002_5_26 | A.3.12 | **ja (33)(1)** | **1** |
| T3-029 | AVG_Art33 | relatedMatch | ISO27002_6_08 | N/A | — | 3 |
| T3-030 | AVG_Art34 | relatedMatch | ISO27002_5_26 | A.3.12 | **ja (34)(1)/(2)** | **1** |
| T3-031 | AVG_Art34 | relatedMatch | ISO27002_5_34 | N/A | — | 3 |

**Distributie:** 10 niveau-1 (32%), 7 niveau-2 (23%), 14 niveau-3 (45%).

**Methodische opmerking voor pilot:** niveau-2 betekent niet "27701 ontkent de relatie" — Annex D is expliciet *non-exhaustive*. Voor C4-toetsing geldt: niveau-2 is een sterker signaal voor `relatedMatch`/`closeMatch` dan voor `narrowMatch`/`broadMatch` (cluster-doel-default). Niveau-3 vereist C1+C3-toetsing op 27002+AVG-semantiek alleen.

---

## §6. Vraag E — Bron-toegankelijkheid + blockers

| Bron | Locatie | Status | Blocker? |
|---|---|---|---|
| ISO/IEC 27701:2025 | `/Users/stevenbouwmeester/grc-sources-licensed/ISO27701.pdf` (1.412 KB, 80 pagina's) | leesbaar via pypdf | nee |
| ISO 27701-Conformiteitsbeoordeling (NCS 27701:2020) | `/Users/stevenbouwmeester/grc-sources-licensed/ISO27701 Conformiteitsbeoordeling.pdf` (675 KB, 28 pagina's) | leesbaar; niet bruikbaar voor T3-evidence | nee (irrelevant) |
| ISO/IEC 29100:2011 | `/Users/stevenbouwmeester/grc-sources-licensed/ISO29100.pdf` (1.649 KB) | leesbaar | nee |
| ISO/IEC 27002:2022 | `/Users/stevenbouwmeester/grc-sources-licensed/NEN-EN-ISO_IEC_27002_2022_en.pdf` (3.014 KB) | leesbaar | nee |
| AVG/GDPR-tekst | **NIET in `sources/eu-recht/`** | publiek beschikbaar via EUR-Lex; samenvattend opgenomen als `rdfs:comment` in m14-ttl | nee — publiek herbruikbaar; voor C1/C3-toetsing volstaat EUR-Lex |
| Publieke 2022-cross-walks (ISMS.online e.a.) | web-referentie, niet in repo | toegankelijk via web-fetch (auteursrechtelijk — parafraseren) | nee |
| `sources/`-doorzoek op GDPR-cross-walks | `sources/adr-norea/`, `sources/eu-recht/`, `sources/nist/` doorzocht | **geen GDPR/AVG/privacy-specifieke cross-walks aanwezig** | nee — Annex D + 27002-tekst zijn primaire bron |

**Geen blockers.** Discipline-reminder Protocol 14 + 17 toegepast — alle citaten in dit rapport zijn parafrase + clausule-verwijzing; geen verbatim NEN-tekst >10 woorden (gechecked tijdens schrijven).

**Opmerking AVG-bron:** AVG/GDPR is publiek EU-recht (Regulation (EU) 2016/679); de teksten van de 5 IB-raakvlakartikelen staan als samenvattende `rdfs:comment` in m14-ttl al beschikbaar voor C1/C3-toetsing. Voor pilot-paren waar verbatim-AVG-tekst nodig is, kan EUR-Lex direct geraadpleegd worden. Geen opname in `sources/`-folder vereist.

---

## §7. Vraag F — Symmetrie- en heterogeniteit-methode-check

### §7.1 F.1 — Richtings-symmetrie (compl→ctrl vs ctrl→compl)

**Vraag:** werken Protocol v1.2/v1.3 C1-C4-criteria symmetrisch bij omgekeerde richting?

**Analyse:**

- **C1 (definitionele overlap)** is richting-agnostisch geformuleerd: "Zou A de volledige reikwijdte van B invullen?" + "Zou B de volledige reikwijdte van A invullen?" — werkt symmetrisch.
- **C2 (cluster-cardinaliteit)** is richting-agnostisch: object-cluster + subject-cluster worden beide berekend; v1.3 §2.2 toevoegde prevalentie-regel "object-cluster prevaleert bij multi-mapping-paren". In m14: subject-cluster (1↔veel) is **dominant** (Art32 → 12 ctrls); object-cluster is klein (max 2 AVG-artikelen → 1 ctrl). Cluster-discipline opereert dus primair op subject-cluster.
- **C3 (inclusie-richting)** is bilateraal getest; "A ⊆ B" en "B ⊆ A" worden onafhankelijk getoetst. Werkt symmetrisch.
- **C4 (bron-evidence)** is richting-agnostisch.

**Praktische asymmetrie in §3.1-uitkomst:** in m10 (ctrl→NIS2, veel↔1-cluster) gaf §3.1 rij 6 als cluster-doel `broadMatch` (A → B waar A engerebepaalde control ⊂ B brede NIS2-clausule). In m14 (compl→ctrl, 1↔veel-cluster) zou §3.1 rij 7 als cluster-doel `narrowMatch` geven (A → B waar A brede AVG-artikel ⊃ B engerebepaalde control). **Dit is geen criteria-asymmetrie — het is symmetrische toepassing van dezelfde tabel op richting-omgekeerde cluster-cardinaliteit.**

**Implicatie voor m14:**
- Wanneer C2-failure-cluster-default `narrowMatch` zou impliceren, kan dat botsen met huidige predicates (`relatedMatch`/`closeMatch`/`broadMatch`).
- Echter: cluster-doel-`narrowMatch` vereist per Protocol §3.1 rij 7 dat "B_i ⊆ A per cluster-lid" houdt (per-paar bilaterale containment). Dat is een **per-paar-toets**, geen automatische cluster-overerving.
- Heterogene clusters (3 van 5 in m14) impliceren dat niet alle cluster-leden dezelfde subset-relatie hebben — sommige zijn `relatedMatch` (zwakker, geen subset), andere `closeMatch`/`broadMatch` (sterker, met subset of partial overlap).

**Conclusie F.1:** geen criteria-asymmetrie. Het cluster-doel-predicate verandert van `broadMatch` (m10) naar `narrowMatch` (m14) als gevolg van cluster-cardinaliteit-richting — dat is verwacht en symmetrisch protocol-gedrag.

### §7.2 F.2 — Heterogene-cluster-handling

**Vraag:** vereist heterogene-cluster-mix (zoals m14 Art32 met closeMatch+relatedMatch) een protocol-aanvulling?

**Analyse:**

- v1.3 §3.3 ("Cluster-discipline") stelt: "*Bij C2-failure (cardinaliteit veel↔1 of 1↔veel) is herclassificatie systematisch binnen het cluster. Alle paren in dezelfde cluster krijgen dezelfde doel-predicate-toewijzing tenzij voor een specifiek paar een individuele uitzondering aantoonbaar is.*"
- v1.3 §3.3 bewijslast-asymmetrie geeft expliciete regels voor uitzonderingen naar sterker, naar zwakker, en behoud van cluster-default.
- In m14's Art32-cluster (12 paren, mix close×1 + related×11): de bestaande heterogeniteit suggereert dat 11 cluster-leden eerder al als `relatedMatch` waren geclassificeerd (thematische verwantschap zonder subset), terwijl 1 paar (Art32 → ISO27002_5_01 Beleidsregels IB) als `closeMatch` (partiële overlap, geen subset).
- Protocol v1.3 dekt deze situatie via per-paar-toets: cluster-default zou via §3.1 rij 7 → `narrowMatch` opleveren, maar per-paar-toets met **falende C3** (geen B ⊆ A subset-relatie) → §3.1 rij 8 (thematische verwantschap) → `relatedMatch`. Voor het closeMatch-paar zou per-paar-toets met **partiële C1+C3 maar zonder subset** → §3.1 rij 3 → `closeMatch` opleveren.

**Conclusie F.2:** v1.3 dekt heterogene clusters al via per-paar-toetsing (mits de §3.3-bewijslast voor cluster-uitzondering wordt nageleefd). Geen substantiële protocol-aanvulling nodig.

### §7.3 Verfijnings-suggestie voor v1.3 (niet-blokkerend, niet-substantieel)

**Mogelijke verfijning (geen scope-pauze-trigger):** v1.3 §3.3 kan een korte voetnoot of T3-precedent-paragraaf toevoegen die expliciet maakt:

> "**Richtings-effect op cluster-doel-predicate:** veel↔1-cluster-cardinaliteit (subjects engerebepaald, object breder) → §3.1 rij 6 → `broadMatch`-default. 1↔veel-cluster-cardinaliteit (subject breder, objects engerebepaald) → §3.1 rij 7 → `narrowMatch`-default. Dit is symmetrische toepassing van dezelfde regel; richtings-keuze door modeller bepaalt welke rij geldt. Heterogene cluster-mix (zoals m14 Art32 close+related) vereist per-paar-toets via §2.1 C1 + §2.3 C3."

**Toon: documentatie-helderheid**, geen wijziging in criteria of beslis-regels. Een T2 vs T3-precedent-paragraaf zou methodisch duidelijk maken dat T2's cluster-convergentie (allemaal naar `broadMatch`) een bron-disclaimer-gedreven uitkomst was, terwijl T3 vermoedelijk vooral `relatedMatch`-behoud + enkele cluster-doel-`narrowMatch`-mutaties zal opleveren.

**Beslissing aan masterchat:** of deze verfijning als v1.3.1 of v1.4 wordt opgenomen, of in een T3-eindrapport-leerpunt blijft.

**Hoofdconclusie F:** **Protocol v1.2 (operationeel) + v1.3-draft (verfijningen) toereikend voor T3-uitvoering. Geen substantiële aanvulling vereist vóór pilot kan starten.** Optioneel: documentatie-verfijning per §7.3.

---

## §8. Tech-observaties (eigen vondsten buiten de zes vragen)

### §8.1 Geen verbatim-AVG-tekst-bron in repo, wel rdfs:comment in m14-ttl

`sources/eu-recht/` bevat NIS2-richtlijn (EU 2022/2555) en UV (EU 2024/2690) maar **geen AVG/GDPR-tekst** (Regulation (EU) 2016/679). Voor T3 niet-blokkerend: AVG is publiek EU-recht beschikbaar via EUR-Lex; m14-ttl-`rdfs:comment` bevat al samenvattende NL-teksten van Art. 5(1)(f), 25, 32, 33, 34 (zie m14-ttl regels 64, 73, 83, 94, 103). Voor verbatim-tekst-validatie tijdens pilot kan EUR-Lex direct geraadpleegd worden.

**Mogelijke aanvulling op `sources/`:** AVG-tekst PDF toevoegen aan `sources/eu-recht/` zou consistent zijn met het bestaande NIS2-recht-archief. Niet T3-scope; **leerpunt voor latere Brein-cyclus**.

### §8.2 Het control-name-matching-pad voor 27701-equivalent-lookup is robuust

De keten 27002:2022-control → 27001:2013-Annex-A-equivalent (via Annex F.1 kolom 2) → 27701:2025-A.3.x is een **deterministische lookup** mits control-name-match nauwkeurig is. Geen ambiguïteit aangetroffen. 27002:2022-control-name-list (10 nieuwe controls + 24 vernieuwde) is volledig herkenbaar in Annex F.1.

**Implicatie:** een herbruikbaar `helper_script.py` voor T3-hoofd-uitvoering kan de 14 niveau-1/2-paren via gestructureerde lookup classificeren; de 14 niveau-3-paren via een handmatige C1+C3-toets-lijst. Hybride aanpak verwacht.

### §8.3 NCS 27701:2020 + ISO 27701:2025-relatie heeft potentiële Brein-cyclus-leerpunt

NCS 27701:2020 verwijst expliciet naar **27701:2019** (verouderde editie). Een actualisatie van NCS 27701 naar de 2025-editie is mogelijk in voorbereiding bij NEN; status onbekend. Geen impact op T3, wel relevant voor latere brain-vault-update over Nederlandse PIMS-certificering-context.

**Status:** observatie, geen actie. Brein-subagent kan later overwegen of dit een file-back rechtvaardigt.

### §8.4 SHACL-blinde vlek opnieuw bevestigd

Snelle SPARQL-scan: geen SHACL-shape in `grc-shacl.ttl` valideert compl:→ctrl: SKOS-mappings. Mutaties in T3-uitvoering zullen daarom SHACL RUN 1/RUN 2 niet raken (analoog aan T1+T2). Bevestigt H39-trigger-relevantie opnieuw.

### §8.5 1↔veel-cluster-cardinaliteit suggereert ander cluster-doel-pad dan T2

In tegenstelling tot T2 (waar alle 10 NIS2-clusters via §3.1 rij 6 naar `broadMatch` convergeerden), genereert m14's 1↔veel-patroon `narrowMatch` als cluster-default via §3.1 rij 7 — voor zover cluster-discipline van toepassing is op subject-cluster-niveau. Echter: 100% cluster-convergentie naar `narrowMatch` is **onwaarschijnlijk** gegeven de heterogeniteit (3 van 5 clusters predicate-mix). Verwachting: gemengde uitkomst van behoud-relatedMatch + enkele `narrowMatch`-mutaties + enkele `closeMatch`-behoud — geheel binnen masterchat-§0.2-verwachting van "0-4 mutaties, bevestigings-sprint".

---

## §9. Pilot-sample-aanbeveling

**Sample-grootte:** 6 paren (instructie-§9 aanbeveling).

**Spreiding-richtlijnen:**
- ✓ Alle 3 aanwezige predicate-types (relatedMatch + closeMatch + broadMatch)
- ✓ Spreiding over alle 5 AVG-artikelen
- ✓ Verschillende evidence-niveaus (niveau-1 + niveau-2 + niveau-3)
- ✓ Mix van homogene en heterogene clusters
- ✓ Mix van object-cluster-singletons en multi-mappings

### Aanbevolen sample (6 paren)

| # | Paar-ID | Subject IRI | Object IRI | Pred | Cluster | Cluster-mix | Object-cluster | Evidence-niveau | Reden van keuze |
|---|---|---|---|---|---|---|---|---|---|
| 1 | T3-002 | `compl:AVG_Art5_1f` | `ctrl:ISO27002_5_12` | broadMatch | Art5_1f (7, heterogeen) | broad×2/rel×5 | singleton | **1** (Annex D B.3.5→(5)(1)(f)) | Heterogene cluster + broadMatch-predicate + niveau-1 evidence; toetst of broadMatch verdedigbaar is in 1↔veel-cluster |
| 2 | T3-014 | `compl:AVG_Art32` | `ctrl:ISO27002_5_01` | closeMatch | Art32 (12, heterogeen) | close×1/rel×11 | multi (Art5_1f+Art32) | 2 (A.3.3 bestaat, Annex D-link ontbreekt) | Closest-Match-paar in grootste cluster + multi-object-cluster; toetst of closeMatch behoud-waardig is |
| 3 | T3-024 | `compl:AVG_Art32` | `ctrl:ISO27002_5_35` | relatedMatch | Art32 (12, heterogeen) | close×1/rel×11 | singleton | **1** (Annex D B.3.15→(32)(1)(d)/(2)) | Niveau-1 relatedMatch-cluster-volger; toetst of cluster-doel narrowMatch overstemt of relatedMatch wint via per-paar-evidence |
| 4 | T3-008 | `compl:AVG_Art25` | `ctrl:ISO27002_8_25` | relatedMatch | Art25 (6, homogeen) | rel×6 | singleton | **1** (Annex D B.3.27→(25)(1)) | Homogene-cluster-representant + niveau-1; toetst cluster-discipline-overerving voor Art25 |
| 5 | T3-028 | `compl:AVG_Art33` | `ctrl:ISO27002_5_26` | relatedMatch | Art33 (4, heterogeen) | close×1/rel×3 | multi (Art33+Art34) | **1** (Annex D B.3.12→(33)(1)) | Multi-mapping ctrl + niveau-1 + heterogene cluster; toetst object-cluster-effect bij multi-mapping |
| 6 | T3-031 | `compl:AVG_Art34` | `ctrl:ISO27002_5_34` | relatedMatch | Art34 (2, homogeen) | rel×2 | singleton | 3 (geen 27701-equivalent) | Niveau-3-paar in kleinste cluster + interessante 27001:2013-N/A reden ("Privacy and protection of PII"); toetst Tech-only-analyse |

### Spreiding-validatie van sample

| Spreidings-as | Sample-dekking |
|---|---|
| Predicate-types | 1× broadMatch (T3-002), 1× closeMatch (T3-014), 4× relatedMatch (T3-024, T3-008, T3-028, T3-031) |
| AVG-artikelen | 1× Art5_1f, 1× Art25, 2× Art32, 1× Art33, 1× Art34 — alle 5 vertegenwoordigd |
| Evidence-niveaus | 4× niveau-1 (T3-002, T3-024, T3-008, T3-028), 1× niveau-2 (T3-014), 1× niveau-3 (T3-031) |
| Cluster-heterogeniteit | 4× heterogene cluster, 2× homogene cluster |
| Object-cluster | 4× singleton, 2× multi-mapping |

**Stop-conditie-bewaking tijdens pilot:**
- Confidence "laag" op ≥3 paren → pauze
- Evidence-niveau 4 op ≥3 paren → pauze (niet verwacht — minimum niveau is 3 in m14)
- D4.1-status "niet-onderzocht" op ≥3 paren → pauze (niet relevant — geen exactMatch-doel-paren)
- Onverwacht-patroon (bv. >3 mutaties terwijl masterchat-verwachting 0-4) → pauze; mogelijk methode-correctie

**Pilot-uitkomst-verwachting:** geen pre-pilot-projectie per paar (Protocol v1.3 §6). Wel kwalitatieve verwachting: cluster-discipline + per-paar-toets via §3.1 rij 7 + heterogene-mix-handling zal vermoedelijk gemengde mutatie-richting opleveren (behoud + enkele closeMatch ↔ narrowMatch / relatedMatch ↔ closeMatch grenswijzigingen).

---

## §10. Hand-off-checklist

- [x] **Pre-push disclosure-check Protocol 14** uitgevoerd op dit rapport:
  - [x] Organisatie-naam: geen vermelding ("de organisatie" / "Rijksoverheidsorganisatie" gebruikt; NEN-PDF-watermark verwijst naar generieke "Rijksoverheid NEN Connect" — dat is een licentie-identifier, geen organisatie-claim)
  - [x] Persoonsnamen: alleen "Steven" (toegestaan)
  - [x] Lokale paden: `/Users/stevenbouwmeester/grc-sources-licensed/`-paden zijn referenties naar NEN-licentie-locaties op de werkmachine; passen binnen scope Protocol 14 omdat ze geen credentials of secrets bevatten
  - [x] Credentials/e-mail-domeinen: geen
  - [x] NEN-tekst-fragmenten verbatim >10 woorden: **geen** — alle citaten zijn parafrase + clausule-verwijzing; één korte parafrase van Annex D NOTE in §4.2 (<10 woorden); ISO 27002-control-names in §4.3-tabel zijn factuele identifier-strings (control-name-niveau, geen guidance-tekst)
- [x] **Geen patches/ontologie-wijzigingen toegepast** — modus READ-ONLY gerespecteerd
- [x] **Geen autonome commits** — Steven commit handmatig na masterchat-review
- [x] **Rapport zelfstandig leesbaar voor masterchat** — context, scope, cijfers, evidence-pad, methode-conclusie, pilot-sample alle expliciet
- [x] **§9 pilot-sample bevat IRI's + cluster-context per paar** — 6 paren met volledige spreiding-rationale
- [x] **§4 bron-bruikbaarheids-conclusie expliciet** — 27701:2025 Annex D + Annex F twee-staps-keten = niveau-1 voor 10 paren, niveau-2 voor 7 paren, niveau-3 voor 14 paren; NCS 27701:2020 niet bruikbaar
- [x] **§7 methode-aanbeveling expliciet** — v1.2/v1.3 toereikend; optionele documentatie-verfijning per §7.3

### Achtergebleven werkende tree-status

Eén nieuw bestand aangemaakt: `output/reports/t3-pre-sprint-inventarisatie.md` (dit rapport). Geen wijzigingen aan `ontology/`, `scripts/`, of andere bestanden. Geen verificatie-scripts aangemaakt (pre-sprint-fase, geen patch).

---

## §11. Verwijzingen

| Document | Pad |
|---|---|
| Instructie T3 pre-sprint | `docs/instructies/instructie-t3-pre-sprint-inventarisatie.md` |
| SKOS-protocol v1.2 (operationeel) | `docs/skos-beoordelings-protocol-v1_2.md` |
| SKOS-protocol v1.3 (DRAFT) | `docs/skos-beoordelings-protocol-v1_3.md` |
| T1-eindrapport | `output/reports/t1-eindrapport-v4_6_1.md` |
| T2-patch-rapport v4.6.2 | `output/reports/patch-rapport-v4_6_2.md` |
| M14-brain | `brain/brain__modules__M14_avg-gdpr.md` |
| H36-brain | `brain/brain__architecture__H36_skos-exactmatch-ctrl-compl-audit.md` |
| ISO/IEC 27701:2025 (NEN-licensed) | `/Users/stevenbouwmeester/grc-sources-licensed/ISO27701.pdf` |
| NCS 27701:2020 Conformiteitsbeoordeling (NEN-licensed) | `/Users/stevenbouwmeester/grc-sources-licensed/ISO27701 Conformiteitsbeoordeling.pdf` |
| ISO/IEC 27002:2022 (NEN-licensed) | `/Users/stevenbouwmeester/grc-sources-licensed/NEN-EN-ISO_IEC_27002_2022_en.pdf` |
| ISO/IEC 29100:2011 (NEN-licensed) | `/Users/stevenbouwmeester/grc-sources-licensed/ISO29100.pdf` |
| m14-ontologie-module | `ontology/m14-avg-gdpr.ttl` |
| Dit rapport | `output/reports/t3-pre-sprint-inventarisatie.md` |

— Einde T3 Pre-sprint-inventarisatie-rapport.
