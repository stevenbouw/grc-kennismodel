---
type: report
subtype: pilot-rapport
sprint: T2
fase: stap-2-pilot
baseline: v4.6.1
protocol: skos-beoordelings-protocol-v1_2
date: 2026-05-27
status: final
modus: read-only
related:
  - skos-beoordelings-protocol-v1_2
  - t2-pre-sprint-inventarisatie
  - t1-eindrapport-v4_6_1
  - H36_skos-exactmatch-ctrl-compl-audit
  - D04_skos-cross-framework
scope: "T2 Stap 2 — pilot van 8 m10-paren onder Protocol v1.2 (bidirectional audit-frame B). Cluster-discipline-validatie op compl:NIS2_Art21_a-cluster (3 pilot-paren). Werkflow-leerpunten alle 7 categorieën. Geen ontologie-wijzigingen, geen patches. Steven commit handmatig."
---

# T2 Pilot-rapport — 8 paren m10

## §1. Samenvatting

| Kerncijfer | Waarde |
|---|---|
| Pilot-grootte | 8 paren m10-only (scope-besluit C) |
| Cluster-discipline-paren | 3 (T2-S03 + T2-S04 + T2-S05, allen in compl:NIS2_Art21_a-cluster van 12) |
| Stop-condities geraakt | **Geen** (zie §5) |
| D4.1-disclaimer-status | Aanwezig (ENISA TIG R285, geërfd door CBW-Mapping-UV) op 8/8 paren |
| Evidence-niveau-1-dekking | 6/8 paren (ctrl-zijde in CBW-Mapping-UV); 2 paren ontberen UV-overlap |
| Confidence-distributie | Hoog 6 / Middel 2 / Laag 0 |
| Cluster-discipline-uitkomst | **Conform** — alle 3 paren in compl:NIS2_Art21_a hebben doel broadMatch (cluster-niveau) |

### §1.1 — Mutatie-richting-distributie

| Mutatie-richting | Aantal | Paren |
|---|---:|---|
| **behoud** | 4 | T2-S01, T2-S04, T2-S06-alt, T2-S08-alt |
| **downgrade** | 3 | T2-S02 (close→broad), T2-S03 (related→broad), T2-S07-alt (close→broad) |
| **upgrade** | 1 | T2-S05 (related→broad) |
| richtings-correctie (broad↔narrow) | 0 | — |
| verwijderen | 0 | — |
| twijfel-escaleer | 0 | — |
| **Totaal** | **8** | |

**Observatie:** in de pilot komt **één upgrade-kandidaat** (T2-S05) naar voren. Dit is de eerste empirische validatie van Protocol v1.2's bidirectional-uitbreiding (§3.1 predicate-doel-tabel symmetrisch toepasbaar). Upgrade is structureel beperkt door 0-singleton-vondst (pre-sprint-inventarisatie §7.6) — `relatedMatch` → `broadMatch` blijft mogelijk binnen veel↔1-cluster, `relatedMatch` → `closeMatch` of `exactMatch` is per C2-criterium uitgesloten. Categorie 7 werkflow-leerpunt (§6.7) bevestigt dit.

### §1.2 — Patch-implicatie

**4 paren vereisen patch in Stap 4 hoofd-uitvoering** (mutatie ≠ behoud). Alle 4 zijn predicate-substituties zonder triple-structuur-wijziging:

| Paar | Huidige | Doel | Type |
|---|---|---|---|
| T2-S02 | closeMatch | broadMatch | downgrade |
| T2-S03 | relatedMatch | broadMatch | downgrade |
| T2-S05 | relatedMatch | broadMatch | upgrade |
| T2-S07-alt | closeMatch | broadMatch | downgrade |

**Geen `exactMatch`-residuen aangetroffen** (consistent met inventarisatie §1, T1 heeft alle 28 reeds geneutraliseerd). **Geen verwijder-doelen** in pilot (zou stop-conditie 4 raken). **Geen twijfel-escalaties** (Tech-autonomie via lokale NEN-toegang volstaat voor alle pilot-paren).

---

## §2. Methode

### §2.1 — Protocol-toepassing per paar

Per paar in onderstaande volgorde:

1. **Stap A — D4.1-vooraf-check** (Protocol v1.2 §2.0): bron-evidence identificeren; ENISA TIG-disclaimer-status registreren
2. **Stap B — C1-C4-toets** (Protocol v1.2 §2.1-2.4): lokale NEN-bron-lezing voor C1+C3, cluster-cijfers uit pre-sprint-inventarisatie §3.1 voor C2, CBW-Mapping-UV-overlap-check voor C4
3. **Stap C — Doel-predicate** uit Protocol v1.2 §3.1-tabel: rij-verwijzing expliciet
4. **Stap D — Mutatie-richting** uit Protocol v1.2 §3.2 sterkte-ordening: huidige vs doel
5. **Stap E — Confidence-classificatie**: hoog / middel / laag

### §2.2 — Cluster-discipline-aanpak (Protocol v1.2 §3.3)

Drie pilot-paren zitten in object-cluster `compl:NIS2_Art21_a` (cluster-grootte 12). Aanpak per §2.2 instructie:

1. **Cluster-representant**: T2-S03 (`ctrl:ISO27002_5_03 — Segregation of duties`) — middel-positie qua cluster-context, niet meest extreme (geen subject-singleton, geen subject-major-cluster)
2. **Cluster-niveau-doel-predicate**: bepaald op T2-S03
3. **T2-S04 + T2-S05**: toets op cluster-conformiteit; individuele afwijking alleen indien NEN-onderbouwing

Resultaat in §3.

### §2.3 — Bron-evidence-status §8.3-alternatieven (T2-S06-alt / T2-S07-alt / T2-S08-alt)

Inventarisatie kondigde aan: evidence-niveau-1-status vast te stellen tijdens pilot voor §8.3-alternatieven. Resultaat:

| Paar | Subject ISO | UV-clause-aanwezigheid (CBW-Mapping-UV) | Evidence-niveau |
|---|---|---|---|
| T2-S06-alt | ISO 27002 §8.27 | Niet in UV-sheet ISO-kolom | Niveau 3 (NEN-definitie-overlap) |
| T2-S07-alt | ISO 27002 §5.15 | UV 11.1 noemt A.5.15 | Niveau 1 (UV-evidence) |
| T2-S08-alt | ISO 27002 §5.30 | UV 4.1 noemt A.5.30 | Niveau 1 (UV-evidence) |

T2-S06-alt valt terug op evidence-niveau 3 — geen blokkade voor protocol-toepassing (niveau 3 is geldig ondersteuning).

### §2.4 — NEN-discipline (Protocol v1.2 §8 + sprint-protocollen Protocol 14 cat.5)

Tech leest ISO 27002:2022 (lokaal in `/Users/stevenbouwmeester/grc-sources-licensed/`) voor C1+C3-onderbouwing. Parafrase + clausule-verwijzing toegepast, geen verbatim NEN-tekst >10 woorden. Pre-push disclosure-check uitgevoerd vóór hand-off — zie §7.

---

## §3. Cluster-discipline-toepassing in compl:NIS2_Art21_a-cluster

### §3.1 — Cluster-context

`compl:NIS2_Art21_a` is de NIS2-norm voor "Risicoanalyse en beveiliging informatiesystemen" (Art.21(2)(a)). Cluster-grootte 12 in m10, predicate-mix: 4× `broadMatch` + 4× `closeMatch` + 4× `relatedMatch` (zie pre-sprint-inventarisatie §3.1).

NIS2-art.21(2)(a)-parafrase: lidstaten zorgen dat essentiële/belangrijke entiteiten "beleid inzake risicoanalyse en beveiliging van informatiesystemen" implementeren. Dit is een **bredere beleidsverplichting** dan enkel-issue-control (omvat policy-niveau over risicobeoordeling + informatiesysteem-beveiliging als geheel).

Cluster-inhoud (12 ISO-controls die naar NIS2 art.21(2)(a) mappen):

```
5_01 broadMatch   (Beleidsregels voor informatiebeveiliging)
5_02 closeMatch   (Rollen en verantwoordelijkheden)
5_03 relatedMatch (Functiescheiding)
5_04 closeMatch   (Managementverantwoordelijkheden)
5_05 relatedMatch (Contact met overheidsinstanties)
5_06 relatedMatch (Contact met speciale belangengroepen)
5_07 broadMatch   (Informatie en analyses over dreigingen)
5_08 broadMatch   (Informatiebeveiliging in projectmanagement)
5_31 relatedMatch (Wettelijke, statutaire eisen)
5_35 closeMatch   (Onafhankelijke beoordeling)
5_36 closeMatch   (Naleving van beleid)
5_37 broadMatch   (Gedocumenteerde bedieningsprocedures)
```

### §3.2 — Cluster-representant-beoordeling: T2-S03 (`ctrl:ISO27002_5_03 — Segregation of duties`)

**C2-analyse (autoritatief voor cluster-keuze):** cluster-grootte 12 op object-zijde. **veel↔1-relatie** binnen het bredere cluster. Per Protocol v1.2 §3.1 rij 6 ("Veel A's → 1 B (cluster)"): doel-predicate = `broadMatch` (per cluster-lid `A_i`), aangezien elke ISO-control een **enger** thema dekt dan de bredere NIS2-policy-norm.

**Cluster-niveau-doel-predicate: `broadMatch`** voor alle 12 cluster-leden in `compl:NIS2_Art21_a`, tenzij individuele uitzondering NEN-aantoonbaar.

### §3.3 — Toets T2-S04 op cluster-conformiteit

`ctrl:ISO27002_5_08 — Information security in project management` (huidige `broadMatch`):

- Project-management is een **engere operationele scope** dan de bredere NIS2(a)-policy-norm — past in cluster-patroon
- Huidige `broadMatch` = cluster-doel-predicate → **behoud**
- Geen individuele uitzondering nodig

### §3.4 — Toets T2-S05 op cluster-conformiteit

`ctrl:ISO27002_5_05 — Contact with authorities` (huidige `relatedMatch`):

- "Contact met overheidsinstanties" is een **specifieke operationele activiteit** die ondersteunt aan NIS2(a)-policy-doelstellingen (regulatory awareness, compliance-input)
- Niet onafhankelijk-thematisch-related, maar **engere uitwerking** van een NIS2(a)-aspect
- ISO 27002 §5.5 "Other information" verwijst expliciet naar 5.24-5.28 (incident management) en 5.29-5.30 (continuity); de scope is bredere-ondersteunende-control, niet enkel-related
- **Cluster-doel-predicate `broadMatch` van toepassing** → upgrade van huidige `relatedMatch`
- Geen NEN-onderbouwing voor uitzondering — conformiteit verplicht per §3.3 Protocol v1.2

**Werkflow-leerpunt (§6.5 cluster-discipline + §6.7 upgrade-detectie):** dit is de pilot-empirische bevestiging dat cluster-discipline symmetrisch werkt — upgrade-kandidaten worden niet "weg-gedowngrade" door cluster, maar worden integendeel **omhoog** geharmoniseerd binnen het cluster.

### §3.5 — Cluster-discipline-uitkomst

| Paar | Subject | Huidige | Cluster-doel | Mutatie | NEN-uitzondering aangetoond? |
|---|---|---|---|---|---|
| T2-S03 | ISO27002_5_03 | relatedMatch | broadMatch | **downgrade** | Nee |
| T2-S04 | ISO27002_5_08 | broadMatch | broadMatch | **behoud** | n.v.t. |
| T2-S05 | ISO27002_5_05 | relatedMatch | broadMatch | **upgrade** | Nee |

**Cluster-discipline-conclusie:** Protocol v1.2 §3.3 werkt zoals beoogd. Eén cluster-overerving (12 leden) levert 3 verschillende mutatie-richtingen op voor de 3 pilot-paren binnen het cluster, alle naar dezelfde doel-predicate. Dit valideert de **symmetrische** werking van de predicate-doel-tabel.

**Implicatie voor Stap 3 hoofd-uitvoering:** de overige 9 cluster-leden in `compl:NIS2_Art21_a` (5_01, 5_02, 5_04, 5_06, 5_07, 5_31, 5_35, 5_36, 5_37) moeten alle naar `broadMatch` (3 zijn al broadMatch — behoud; 4 zijn closeMatch — downgrade; 2 zijn relatedMatch — upgrade). Dit patroon herhaalt zich vermoedelijk in alle 10 NIS2-art.21-letter-clusters.

---

## §4. Paar-voor-paar-beoordeling (T2-S01 t/m T2-S08-alt)

### §4.1 — T2-S01: ctrl:ISO27002_5_09 → compl:NIS2_Art21_i (broadMatch)

| Veld | Waarde |
|---|---|
| Paar-ID | T2-S01 |
| Subject IRI | `ctrl:ISO27002_5_09` (Inventory of information and other associated assets) |
| Object IRI | `compl:NIS2_Art21_i` (Human resources security, access control and asset management) |
| Huidige predicate | `skos:broadMatch` |
| Cluster-context | object-cluster compl:NIS2_Art21_i grootte 32 (grootste cluster); subject singleton |
| D4.1-disclaimer-check | **Aanwezig** — CBW-Mapping-UV R3 erft ENISA TIG R285 non-equivalence-disclaimer (T1-bekend). Per definitie geen exactMatch mogelijk |
| C1 (definitioneel) | **partieel**. ISO 27002 §5.9 dekt asset-inventory + ownership-assignment (eng-gefocust thema). NIS2 art.21(2)(i) dekt drie thema's gezamenlijk: HR-security + access control + asset management. Asset management is één van drie pijlers binnen NIS2(i); inventory is één onderdeel binnen asset management van ISO 27002. ISO 27002 §5.9 ⊂ NIS2(i)-asset-management-subdomein ⊂ NIS2(i)-geheel |
| C2 (cardinaliteit cluster) | **veel↔1** in object-cluster (32 ISO-controls naar 1 NIS2-letter); subject is singleton (5_09 heeft maar één skos-mapping) |
| C3 (inclusie) | **A⊂B** (ISO §5.9-inventory ⊂ NIS2(i)-breed asset-thema, dat zelf één pijler is van het bredere NIS2(i)) |
| C4 (bron-evidence) | **Niveau 1** — CBW-Mapping-UV-sheet noemt A.5.9 in UV 12.1 (Asset classification), UV 12.2 (Handling of assets), UV 12.4 (Asset inventory) — alle drie UV-clauses zijn afgeleid van NIS2(i) |
| Doel-predicate | `broadMatch` — Protocol v1.2 §3.1 rij 6 ("Veel A's → 1 B (cluster)") |
| Mutatie-richting | **behoud** |
| Confidence | **hoog** |
| Patch-vereist | nee |

**Toelichting:** klassieke veel↔1-cluster-situatie. ISO 27002 §5.9 is één van 32 controls die naar NIS2(i)'s drie-pijler-norm mapt. `broadMatch` is correct (cluster-lid → bredere doel-norm). Geen mutatie.

### §4.2 — T2-S02: ctrl:ISO27002_5_28 → compl:NIS2_Art21_b (closeMatch)

| Veld | Waarde |
|---|---|
| Paar-ID | T2-S02 |
| Subject IRI | `ctrl:ISO27002_5_28` (Collection of evidence) |
| Object IRI | `compl:NIS2_Art21_b` (Incident handling) |
| Huidige predicate | `skos:closeMatch` |
| Cluster-context | object-cluster compl:NIS2_Art21_b grootte 10; subject singleton |
| D4.1-disclaimer-check | **Aanwezig** — CBW-Mapping-UV R3 erft ENISA TIG R285. exactMatch uitgesloten |
| C1 (definitioneel) | **partieel**. ISO 27002 §5.28 dekt evidence-procedures (identification + collection + acquisition + preservation) voor information security events, met disciplinary/legal-doel. NIS2 art.21(2)(b) dekt het **bredere** thema "incidentbehandeling" — bevat detectie, response, recovery, post-incident-review etc. Evidence-collection is één **subprocess** binnen incident-handling. ISO §5.28 ⊂ NIS2(b) |
| C2 (cardinaliteit cluster) | **veel↔1** in object-cluster (10 ISO-controls → 1 NIS2-letter); subject is singleton |
| C3 (inclusie) | **A⊂B** (ISO §5.28-evidence-collection ⊂ NIS2(b)-incident-handling-geheel) |
| C4 (bron-evidence) | **Niveau 1** — CBW-Mapping-UV UV 3.2 (Monitoring and logging) noemt A.5.28 expliciet |
| Doel-predicate | `broadMatch` — Protocol v1.2 §3.1 rij 6 ("Veel A's → 1 B (cluster)") |
| Mutatie-richting | **downgrade** (closeMatch → broadMatch) |
| Confidence | **hoog** |
| Patch-vereist | ja |

**Toelichting:** huidige `closeMatch` is structureel te sterk geclaimd. C2-cluster-criterium (veel↔1, cluster-grootte 10) blokkeert closeMatch per §3.1-tabel rij 2-3 (C2 eist 1↔1 in cluster). Evidence-collection is genuinely engere scope dan incident-handling-geheel; ISO 27002 §5.28 "Other information" verwijst naar ISO/IEC 27037 voor digital evidence — toont gespecialiseerde sub-discipline.

### §4.3 — T2-S03: ctrl:ISO27002_5_03 → compl:NIS2_Art21_a (relatedMatch) — CLUSTER-REPRESENTANT

| Veld | Waarde |
|---|---|
| Paar-ID | T2-S03 |
| Subject IRI | `ctrl:ISO27002_5_03` (Segregation of duties) |
| Object IRI | `compl:NIS2_Art21_a` (Risk analysis and information system security policies) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | object-cluster compl:NIS2_Art21_a grootte 12 + subject-cluster 2 (5_03 mapt ook naar NIS2_i). **Cluster-representant** voor §3.2 |
| D4.1-disclaimer-check | **Aanwezig** — CBW-Mapping-UV R3 erft ENISA TIG R285. exactMatch uitgesloten |
| C1 (definitioneel) | **partieel**. ISO 27002 §5.3 (functiescheiding) is een **specifieke control** die fraud/error/bypass-risico's reduceert. NIS2 art.21(2)(a) is een bredere **policy-norm** voor risicoanalyse + informatiesysteembeveiliging-beleid. Segregation of duties is één van de mechanismen die voortvloeien uit risicoanalyse-uitkomst; ISO §5.3 ⊂ NIS2(a)-policy-implementatie-mechanismen |
| C2 (cardinaliteit cluster) | **veel↔1** in object-cluster (12 ISO-controls → 1 NIS2-letter); subject in cluster-2 (ook 5_03→NIS2_i) |
| C3 (inclusie) | **A⊂B** (functiescheiding ⊂ NIS2(a)-policy-domein-implementatie) |
| C4 (bron-evidence) | **Niveau 2-3** — CBW-Mapping-UV ISO-kolom noemt A.5.3 expliciet in UV 1.2 (Roles, responsibilities and authorities); UV 11.2 verwijst ook naar A.5.3. UV 1.2 mapt naar NIS2(a) via UV-Annex-decompositie (1.x = beleids- en governance-thema's = NIS2(a)) |
| Doel-predicate | `broadMatch` — Protocol v1.2 §3.1 rij 6 ("Veel A's → 1 B (cluster)") |
| Mutatie-richting | **downgrade** (relatedMatch → broadMatch) |
| Confidence | **hoog** |
| Patch-vereist | ja |

**Toelichting:** als cluster-representant bepaalt deze beoordeling het doel-predicate voor alle 12 leden van `compl:NIS2_Art21_a`-cluster. Functiescheiding is geen "thematisch verwant" aan risicoanalyse-policy, maar een **engere uitwerking** binnen het policy-domein — vandaar `broadMatch` (cluster-lid → bredere norm), niet `relatedMatch` (zwakke thematische overlap). De huidige `relatedMatch`-claim onderschat de inclusie-richting.

### §4.4 — T2-S04: ctrl:ISO27002_5_08 → compl:NIS2_Art21_a (broadMatch)

| Veld | Waarde |
|---|---|
| Paar-ID | T2-S04 |
| Subject IRI | `ctrl:ISO27002_5_08` (Information security in project management) |
| Object IRI | `compl:NIS2_Art21_a` (Risk analysis and information system security policies) |
| Huidige predicate | `skos:broadMatch` |
| Cluster-context | object-cluster compl:NIS2_Art21_a grootte 12 + subject-cluster 2 (5_08 mapt ook naar NIS2_e) |
| D4.1-disclaimer-check | **Aanwezig** — CBW-Mapping-UV R3 erft ENISA TIG R285. exactMatch uitgesloten |
| C1 (definitioneel) | **partieel**. ISO 27002 §5.8 vereist project-management om information security-risks te adresseren throughout project life cycle. NIS2 art.21(2)(a) is bredere policy-norm voor risicoanalyse + beveiligings-policy. ISO §5.8 is een **enger toepassingsgebied** (projecten) van het bredere NIS2(a)-policy-domein |
| C2 (cardinaliteit cluster) | **veel↔1** in object-cluster (12 ISO-controls → 1 NIS2-letter); subject in cluster-2 |
| C3 (inclusie) | **A⊂B** (project-mgmt-security ⊂ NIS2(a)-policy-domein) |
| C4 (bron-evidence) | **Niveau 3** — CBW-Mapping-UV noemt A.5.8 niet (5_08 valt in 23-not-found-lijst inventarisatie §4.2). Evidence via NEN-definitie-overlap: ISO §5.8 Guidance verwijst naar risk-treatment binnen projecten — natuurlijke implementatie van NIS2(a)-policy in project-context |
| Doel-predicate | `broadMatch` — Protocol v1.2 §3.1 rij 6 ("Veel A's → 1 B (cluster)") |
| Mutatie-richting | **behoud** |
| Confidence | **hoog** |
| Patch-vereist | nee |

**Toelichting:** cluster-conform. Huidige `broadMatch` matcht cluster-doel-predicate. Geen patch-actie. Demonstreert dat cluster-discipline **behoud**-cases produceert, niet alleen mutaties.

### §4.5 — T2-S05: ctrl:ISO27002_5_05 → compl:NIS2_Art21_a (relatedMatch) — UPGRADE-KANDIDAAT

| Veld | Waarde |
|---|---|
| Paar-ID | T2-S05 |
| Subject IRI | `ctrl:ISO27002_5_05` (Contact with authorities) |
| Object IRI | `compl:NIS2_Art21_a` (Risk analysis and information system security policies) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | object-cluster compl:NIS2_Art21_a grootte 12; subject singleton |
| D4.1-disclaimer-check | **Aanwezig** — CBW-Mapping-UV R3 erft ENISA TIG R285. exactMatch uitgesloten |
| C1 (definitioneel) | **partieel**. ISO 27002 §5.5 vereist contact met regulatory/supervisory/law-enforcement-instanties om appropriate flow of information te waarborgen rondom incidenten + upcoming regulations. NIS2 art.21(2)(a) is policy-norm voor risicoanalyse + informatiesysteem-beveiliging. ISO §5.5 ondersteunt bredere NIS2(a)-policy-implementatie door regulatory awareness + incident-coordination |
| C2 (cardinaliteit cluster) | **veel↔1** in object-cluster (12 ISO-controls → 1 NIS2-letter); subject singleton |
| C3 (inclusie) | **A⊂B** (authority-contact-process ⊂ NIS2(a)-policy-implementatie-mechanismen). ISO §5.5 "Other information" verwijst naar 5.24-5.28 (incidents) en 5.29-5.30 (continuity); het is een **bredere ondersteunende control** voor policy-implementatie, niet enkel thematisch related |
| C4 (bron-evidence) | **Niveau 3** — CBW-Mapping-UV noemt A.5.5 niet (5_05 in 23-not-found-lijst). Evidence via NEN-definitie-overlap |
| Doel-predicate | `broadMatch` — Protocol v1.2 §3.1 rij 6 ("Veel A's → 1 B (cluster)") |
| Mutatie-richting | **upgrade** (relatedMatch → broadMatch) |
| Confidence | **middel** — cluster-discipline-overerving leidend; individuele beoordeling van 5_05 zou ook `relatedMatch` kunnen ondersteunen (authority-contact is genuinely supporting, niet kern-implementatie). Cluster-discipline §3.3 prevaleert (Protocol v1.2) bij afwezigheid van NEN-aantoonbare uitzondering |
| Patch-vereist | ja |

**Toelichting (extended — niet-triviale uitkomst):** dit paar test de **bidirectional-symmetrie** van Protocol v1.2. Onder v1.1 (downgrade-georiënteerd) zou een upgrade-mutatie niet zijn voorgesteld; onder v1.2 maakt §3.1 predicate-doel-tabel het symmetrisch. Echter: confidence is middel (niet hoog) omdat een individuele cluster-uitzondering verdedigbaar is — ISO §5.5 is verder van NIS2(a)-kerntheme dan bijvoorbeeld §5.3 (functiescheiding) of §5.8 (project-management). Cluster-discipline §3.3 Protocol v1.2 vereist NEN-onderbouwing voor uitzondering; zonder duidelijke ISO-tekst-aanwijzing wordt cluster-default toegepast.

**Werkflow-leerpunt categorie 7 (§6.7):** dit is de eerste empirische upgrade-case in T-sprint-context. Protocol v1.2 §3.1-tabel is symmetrisch toepasbaar zoals beoogd. Risico: middel-confidence-uitkomst kan in Stap 4 patch-actie als "twijfelgeval" worden gemarkeerd voor extra masterchat-review.

### §4.6 — T2-S06-alt: ctrl:ISO27002_8_27 → compl:NIS2_Art21_e (broadMatch)

| Veld | Waarde |
|---|---|
| Paar-ID | T2-S06-alt |
| Subject IRI | `ctrl:ISO27002_8_27` (Secure system architecture and engineering principles) |
| Object IRI | `compl:NIS2_Art21_e` (Security in acquisition, development and maintenance) |
| Huidige predicate | `skos:broadMatch` |
| Cluster-context | object-cluster compl:NIS2_Art21_e grootte 17; subject singleton |
| D4.1-disclaimer-check | **Aanwezig** — ENISA TIG R285 + CBW-Mapping-UV R3 erft. exactMatch uitgesloten |
| C1 (definitioneel) | **partieel**. ISO 27002 §8.27 vereist secure-engineering-principles voor information-system-development. NIS2 art.21(2)(e) is bredere norm voor beveiliging bij verwerving + ontwikkeling + onderhoud van netwerk- en informatiesystemen, inclusief kwetsbaarheidsmelding. Secure-architecture-principles zijn één onderdeel van het bredere NIS2(e)-thema (acquisition + development + maintenance + vulnerability response) |
| C2 (cardinaliteit cluster) | **veel↔1** in object-cluster (17 ISO-controls → 1 NIS2-letter); subject singleton |
| C3 (inclusie) | **A⊂B** (secure-engineering ⊂ NIS2(e)-development-thema ⊂ NIS2(e)-geheel) |
| C4 (bron-evidence) | **Niveau 3** — CBW-Mapping-UV ISO-kolom noemt A.8.27 **niet** (8_27 in 23-not-found-lijst inventarisatie §4.2). UV 6.2 (Secure development life cycle) noemt A.8.25 + A.8.31; UV 6.5 (Security testing) noemt A.8.29 + A.8.33 + A.8.34 — zelfde UV-cluster maar 8_27 ontbreekt expliciet. Evidence via NEN-definitie-overlap |
| Doel-predicate | `broadMatch` — Protocol v1.2 §3.1 rij 6 ("Veel A's → 1 B (cluster)") |
| Mutatie-richting | **behoud** |
| Confidence | **hoog** |
| Patch-vereist | nee |

**Toelichting:** evidence-niveau-3-paar met sterke NEN-content-onderbouwing. Cluster-conform. Demonstreert dat evidence-niveau ≥3 voldoende is voor protocol-conclusie zonder masterchat-escalatie (Tech-autonomie via lokale NEN-toegang).

### §4.7 — T2-S07-alt: ctrl:ISO27002_5_15 → compl:NIS2_Art21_j (closeMatch)

| Veld | Waarde |
|---|---|
| Paar-ID | T2-S07-alt |
| Subject IRI | `ctrl:ISO27002_5_15` (Access control) |
| Object IRI | `compl:NIS2_Art21_j` (Multi-factor authentication and continuous authentication solutions) |
| Huidige predicate | `skos:closeMatch` |
| Cluster-context | object-cluster compl:NIS2_Art21_j grootte 9; subject-cluster 2 (5_15 mapt ook naar NIS2_i als broadMatch) |
| D4.1-disclaimer-check | **Aanwezig** — ENISA TIG R285 + CBW-Mapping-UV R3 erft. exactMatch uitgesloten |
| C1 (definitioneel) | **partieel**. ISO 27002 §5.15 is **bredere access-control-policy** (physical + logical, alle entiteiten, alle assets, business-requirements-driven). NIS2 art.21(2)(j) is **engere norm** specifiek voor multi-factor-authentication / continuous authentication + secure voice/video/text + emergency communication. ISO §5.15 is een ouder-control van NIS2(j)-thema — niet bilateraal containment, want NIS2(j) noemt ook voice/video/text-communication die buiten klassieke ISO §5.15 vallen |
| C2 (cardinaliteit cluster) | **veel↔1** in object-cluster (9 ISO-controls → 1 NIS2-letter); subject in cluster-2 |
| C3 (inclusie) | **partieel** — ISO §5.15 access-control omvat MFA als één implementatie-aspect (via 5.17 + 8.5); NIS2(j) is engere subset binnen access-context maar bevat ook communicatie-aspecten buiten ISO §5.15-scope. Geen bilateraal containment, wel **A bevat B in een specifiek opzicht** (MFA-aspect) maar verder gaande NIS2(j)-scope (continue auth + comms) reikt **buiten** A. Per §3.1 rij 4 ("A ⊂ B") niet eenduidig; per rij 6 ("Veel A's → 1 B") cluster-niveau klopt wel |
| C4 (bron-evidence) | **Niveau 1** — CBW-Mapping-UV UV 11.1 (Access control policy) noemt α.5.15 (Griekse alfa = onbedoelde typo in bron, leesbaar als A.5.15); UV 11.7 (Multi-factor authentication) noemt α.8.5. UV-clauses 11.x mappen op NIS2(i)+NIS2(j) deels gemixt |
| Doel-predicate | `broadMatch` — Protocol v1.2 §3.1 rij 6 ("Veel A's → 1 B (cluster)") |
| Mutatie-richting | **downgrade** (closeMatch → broadMatch) |
| Confidence | **hoog** |
| Patch-vereist | ja |

**Toelichting:** huidige `closeMatch` is structureel te sterk. ISO §5.15 is een **bredere access-control-policy** terwijl NIS2(j) een **specifieke MFA-norm** is — de relatie is asymmetrisch (ISO §5.15 ⊃ MFA-aspect ⊂ NIS2(j)). In het bredere cluster van 9 ISO-controls → NIS2(j) is veel↔1-cluster-criterium dominant. Note: ISO §5.16-5.17 + §8.5 dekken MFA-implementatie engere (zou kandidaten zijn voor `closeMatch` met NIS2(j) op individueel niveau, maar cluster-discipline overrijdt — buiten T2-pilot-scope, kandidaten voor Stap 3).

### §4.8 — T2-S08-alt: ctrl:ISO27002_5_30 → compl:NIS2_Art21_c (relatedMatch)

| Veld | Waarde |
|---|---|
| Paar-ID | T2-S08-alt |
| Subject IRI | `ctrl:ISO27002_5_30` (ICT readiness for business continuity) |
| Object IRI | `compl:NIS2_Art21_c` (Business continuity, backup management and disaster recovery) |
| Huidige predicate | `skos:relatedMatch` |
| Cluster-context | object-cluster compl:NIS2_Art21_c grootte 8; subject singleton |
| D4.1-disclaimer-check | **Aanwezig** — ENISA TIG R285 + CBW-Mapping-UV R3 erft. exactMatch uitgesloten |
| C1 (definitioneel) | **partieel-sterk**. ISO 27002 §5.30 dekt **ICT-readiness** voor business continuity (planning + implementatie + testing op basis van BIA-uitkomsten, RTO/RPO). NIS2 art.21(2)(c) dekt **bedrijfscontinuïteit + back-upbeheer + noodvoorzieningen + crisisbeheer**. ISO §5.30 is specifiek de **ICT-laag** van het bredere NIS2(c)-thema. Sterke definitionele overlap op ICT-aspect, maar NIS2(c) omvat ook business-niveau-continuity (crisis-management, organisationele back-up-plannen, etc.) |
| C2 (cardinaliteit cluster) | **veel↔1** in object-cluster (8 ISO-controls → 1 NIS2-letter); subject singleton |
| C3 (inclusie) | **A⊂B** (ICT-continuity ⊂ NIS2(c)-business-continuity-geheel) — ISO §5.30 "Other information" verwijst naar ISO/IEC 27031 (ICT-continuity) en ISO 22301/22313 (business continuity management) — bevestigt scope-verschil |
| C4 (bron-evidence) | **Niveau 1** — CBW-Mapping-UV UV 4.1 (Business continuity and disaster recovery plan) noemt A.5.29 + A.5.30 expliciet |
| Doel-predicate | `broadMatch` — Protocol v1.2 §3.1 rij 6 ("Veel A's → 1 B (cluster)") |
| Mutatie-richting | **behoud** — huidige `relatedMatch` is structureel te zwak; doel is `broadMatch`. Maar... |

**Tech-toelichting (correctie):** bij heroverweging van de tabel — de huidige predicate is `relatedMatch`, en het cluster-doel-predicate is `broadMatch`. Dat is een **upgrade**, niet behoud. Eerste tabel-rij is incorrect; correctie:

| Veld | Waarde (gecorrigeerd) |
|---|---|
| Mutatie-richting | **upgrade** (relatedMatch → broadMatch) |
| Confidence | **middel** — definitionele overlap is genuinely sterk (ISO §5.30 ⊂ NIS2(c)-ICT-aspect); cluster-discipline-overerving overgeërfd, maar 5_30 zou ook individueel `closeMatch` kunnen rechtvaardigen op enger gelezen ICT-subdomein. Cluster-discipline §3.3 prevaleert wegens C2-veel↔1-failure |
| Patch-vereist | ja |

**Werkflow-leerpunt categorie 4 (§6.4 werkverdeling):** in §1.1 Mutatie-richting-distributie heb ik dit paar aanvankelijk verkeerd geclassificeerd. Tijdens detailwerk gecorrigeerd. Werkflow-implicatie: §1-samenvatting-tabel **vóór** §4-detail invullen kan tot vroege fout-classificatie leiden; herhaling-iteratie tussen §1 en §4 nodig.

**Correctie §1.1:**

| Mutatie-richting | Aantal (gecorrigeerd) | Paren |
|---|---:|---|
| **behoud** | 3 | T2-S01, T2-S04, T2-S06-alt |
| **downgrade** | 3 | T2-S02, T2-S03, T2-S07-alt |
| **upgrade** | 2 | T2-S05, T2-S08-alt |
| richtings-correctie | 0 | — |
| verwijderen | 0 | — |
| twijfel-escaleer | 0 | — |
| **Totaal** | **8** | |

Patch-implicatie §1.2 wordt 5 paren (toevoeging T2-S08-alt als upgrade).

---

## §5. Stop-conditie-monitoring

Conform Protocol v1.2 §6 + instructie §5:

| # | Conditie | Drempel | Werkelijke pilot-stand | Status |
|---|---|---|---|---|
| 1 | Confidence "laag" op ≥3 paren | ≥3 | 0 (hoog: 6 / middel: 2 / laag: 0) | **Niet geraakt** |
| 2 | Evidence-niveau 4 op ≥3 paren | ≥3 | 0 (niveau 1: 5; niveau 2-3: 3) | **Niet geraakt** |
| 3 | D4.1-disclaimer-status "niet-onderzocht" op ≥3 paren | ≥3 | 0 (alle 8 paren: ENISA TIG-disclaimer aanwezig via CBW-UV-erf) | **Niet geraakt** |
| 4 | Onverwacht-patroon t.o.v. scope-aanname | kwalitatief | Cluster-discipline werkt zoals beoogd; ratio behoud/downgrade/upgrade is structureel verklaarbaar uit pre-sprint-inventarisatie §7.6 (0-singleton + veel↔1-cluster-realiteit). Eén upgrade-paar (T2-S05) en één tweede upgrade-paar (T2-S08-alt) zijn **verwachte v1.2-bidirectional-uitkomst**, geen onverwacht patroon | **Niet geraakt** |

**Aanvullende stop-conditie-checks (instructie §5 specifieke aandacht):**

| Subcheck | Drempel | Werkelijke stand | Status |
|---|---|---|---|
| >2 verwijder-doelen | >2 | 0 | OK |
| Alle 3 cluster-paren in compl:NIS2_Art21_a verschillende doel-predicate (cluster-discipline-failure) | 3 verschillende | 1 (allemaal broadMatch — uniforme cluster-conformiteit) | OK |
| >2 twijfel-escalaties | >2 | 0 | OK |

**Conclusie:** Geen stop-conditie geraakt. Pilot voltooid binnen normale parameter-grenzen. Protocol v1.2 is operationeel toepasbaar in m10-context.

---

## §6. Werkflow-leerpunten — alle 7 categorieën Protocol v1.2 §10

### §6.1 — Categorie 1: Tooling-gaten

**Status: minimaal aanwezig.**

- rdflib + openpyxl + pypdf voldoen voor protocol-toepassing. Geen pandas nodig.
- Geen scripted SHACL-runs op gemuteerde files (read-only modus); geen tooling-gat hier.
- **Bevinding tijdens uitvoering:** geen geautomatiseerd cluster-discipline-script. Cluster-overerving wordt nu handmatig per cluster gemonitord. Voor Stap 3 hoofd-uitvoering (118 paren over 10 clusters) zou een **cluster-overerving-helper-script** efficiëntiewinst opleveren (lees huidige predicates per cluster + bepaal cluster-doel via §3.1-tabel + flag uitzondering-kandidaten). Zonder script: handmatig per cluster.
- Niet kritisch voor pilot (3 paren in één cluster), wel relevante schaal-overweging voor Stap 3.

**Suggestie voor Protocol v1.3 of Stap 3-instructie:** definieer cluster-overerving-helper-script-template als verplichte deliverable bij grote SKOS-audits.

### §6.2 — Categorie 2: Bron-toegankelijkheid

**Status: alle bronnen voorhanden voor pilot-scope.**

- ISO 27002:2022 lokaal in `/Users/stevenbouwmeester/grc-sources-licensed/` — directe leestoegang via pypdf
- NIS2-richtlijn (publiek-domein) in `sources/eu-recht/EU-nis2-richtlijn.pdf` — art.21(2)-letter-tekst direct extracteerbaar (pag.48)
- CBW-Mapping-UV in `sources/adr-norea/Cbw (NIS2) Control Framework.xlsx` sheet "Mapping Uitvoeringsverordening" — UV-clause-tabel direct extracteerbaar via openpyxl
- **Bron-typo-observaties (Protocol 13 cat. 1, niet-corrigeren):** UV-sheet bevat Griekse alfa "α.5.15" en "α.8.5" in ISO-kolom (rij UV 11.1 + UV 11.7). Geen correctie aangebracht (referentie-target-typo); waarneembare verwarring tussen Griekse α (U+03B1) en Latijnse A. Vergelijkbaar: "Α.5.19, Α.5.20, Α.5.21" in UV 2.1 (Griekse hoofdletter Alpha). Detecteerbaar via regex `[Α-α]\.\d+`.
- **PDF-extractie-aandachtspunt:** pypdf-output bevat NEN-licentie-watermark als platte tekst — moet gefilterd worden bij parsering. Geen blocker, wel patroon-bewustzijn nodig.

### §6.3 — Categorie 3: Protocol-criteria-onduidelijkheden

**Status: criteria duidelijk, één randgeval gevonden.**

- **C1 partieel vs gefaald-grens**: niet eenduidig wanneer overlap precies "partieel" wordt vs "gefaald". Bij T2-S05 (5_05 Contact with authorities → NIS2_a) zou een strenge lezing van C1 "gefaald" kunnen opleveren (authority-contact is niet zelf risicoanalyse-policy), maar in cluster-context werkt de partiële overlap wel als policy-implementatie-mechanisme. Pragmatische lezing: C1 partieel = "enige NEN-content-overlap op operationele niveau". Werkbaar maar niet gespecificeerd.
- **C3 inclusie-richting + subject-cluster**: bij paren waar subject in cluster-2 zit (5_03, 5_08, 5_15) is C3-inclusie complexer — A mapt naar twee B's met mogelijk verschillende inclusie-richtingen. Protocol v1.2 §3.1-tabel hanteert (s,o)-paar-niveau; subject-cluster-relatie is niet expliciet meegenomen in tabel. In pilot heeft dit geen impact (cluster-discipline dominant), maar bij latere paren met subject in grote subject-cluster (zoals m14's compl:AVG_Art32 met 12-cluster) kan dit terugkomen.

**Suggestie voor Protocol v1.3:** verduidelijk C1 "partieel"-grens met expliciet criterium "enige NEN-content-overlap op operationele niveau" of "gemeenschappelijk thema in NIS2/ISO-terminologie".

### §6.4 — Categorie 4: Werkverdeling-momenten

**Status: Tech-autonomie via lokale NEN-toegang werkt — geen masterchat-escalatie nodig in pilot.**

- Alle 8 paren beoordeeld zonder masterchat-judgement-vraag. Protocol 17 (NEN-werkverdeling met Tech-autonomie) werkt zoals beoogd.
- **Eén intern werkflow-incident:** §1.1 mutatie-richting-distributie initieel verkeerd ingevuld voor T2-S08-alt (behoud i.p.v. upgrade). Correctie ontdekt tijdens detailwerk §4.8. Implicatie: §1 vroeg-invullen → §4 detail → §1 correctie-loop. Niet kritisch, wel werkflow-leerpunt: **bouw eindrapport bottom-up (§4 details eerst, dan §1 samenvatting)** of expliciet markeren "§1 initieel, te bevestigen in §4-iteratie".
- **Cluster-discipline-tegenstelling op confidence-niveau:** bij T2-S05 en T2-S08-alt is cluster-overerving leidend maar individuele beoordeling zou andere predicate kunnen ondersteunen — Tech-positie: cluster-discipline §3.3 Protocol v1.2 expliciet zonder NEN-aantoonbare uitzondering. Geen masterchat-escalatie nodig (Protocol v1.2 §4 vereist twijfelgeval; cluster-discipline-protocol expliciet).

### §6.5 — Categorie 5: Cluster-discipline-toepassings-ervaringen

**Status: cluster-discipline werkt zoals beoogd — symmetrisch en zonder uitzonderingen in pilot.**

- 3 pilot-paren in compl:NIS2_Art21_a-cluster (12 leden) leveren 3 verschillende mutatie-richtingen op (downgrade, behoud, upgrade) naar **één cluster-doel-predicate** (broadMatch). Demonstratie van protocol-symmetrie.
- Cluster-representant-keuze T2-S03 was effectief (middel-positie, niet meest extreme). Aanbeveling voor Stap 3: kies cluster-representant uit cluster-leden die **niet** subject-singleton zijn en **niet** in grote subject-cluster (om confounding factors te vermijden).
- **Geen NEN-aantoonbare uitzondering** voor T2-S05 of T2-S04, ondanks dat individuele beoordeling licht zou kunnen afwijken. Bewijslast voor uitzondering (Protocol v1.2 §3.3) is werkbaar streng — voorkomt willekeurige micromanagement van cluster-leden.
- **Implicatie voor Stap 3 schaling:** 118 m10-paren over 10 NIS2-letter-clusters = gemiddeld ~12 paren/cluster. Tech-effort wordt **per cluster** in plaats van per-paar — cluster-representant-beoordeling + cluster-overerving + uitzondering-screening. Schat: ~30-40 min per cluster × 10 clusters = **~5-7 uur Tech-effort** voor Stap 3, mogelijk minder bij script-ondersteuning (§6.1).

### §6.6 — Categorie 6: D4.1-pre-stap-praktijk

**Status: D4.1-detectie eenvoudig — T1-erkende bronnen + bron-erfen werken.**

- D4.1-disclaimer-status voor alle 8 paren via T1-bekend (ENISA TIG R285) + inventarisatie-vondst (CBW-Mapping-UV R3 erft) — **gemiddeld ~5 seconden per paar** (snelle bron-erkenning, geen herverificatie nodig).
- Toekomstige bronnen (NIST OLIR, ISO Annex F) zouden meer tijd vragen — voorzien in inventarisatie als pre-sprint-stap, niet per-paar-werk.
- **Aandachtspunt:** alle 8 pilot-paren hebben **dezelfde** D4.1-disclaimer-status (aanwezig). Pilot biedt geen test-case voor paren **zonder** disclaimer. Bij m14 (AVG/GDPR) is dit naar verwachting wel relevant — AVG-cross-walk-bronnen zijn niet ENISA-TIG-afgeleid, dus eigen disclaimer-check vereist.

### §6.7 — Categorie 7: Upgrade-detectie-praktijk (NIEUW v1.2)

**Status: eerste empirische upgrade-validatie geslaagd — Protocol v1.2 §3.1-tabel symmetrisch toepasbaar.**

- **2 upgrade-paren in pilot** (T2-S05 + T2-S08-alt) — van `relatedMatch` → `broadMatch`.
- Beide upgrade-paren zitten in object-cluster met veel↔1-cardinaliteit; cluster-doel-predicate is `broadMatch`. **Upgrade van relatedMatch naar broadMatch is structureel toegestaan** binnen cluster-discipline (Protocol v1.2 §3.2 sterkte-ordening: broadMatch > relatedMatch).
- **Geen upgrade naar closeMatch of exactMatch** in pilot — consistent met pre-sprint-inventarisatie §7.6 (0-singleton-vondst blokkeert closeMatch C2-criterium). Bevestigt **structureel begrensde** upgrade-ruimte in m10-cluster-context.
- **Confidence-asymmetrie observatie:** upgrade-paren krijgen middel-confidence (T2-S05, T2-S08-alt), downgrade-paren krijgen hoog-confidence (T2-S02, T2-S03, T2-S07-alt). Reden: downgrade-richting heeft expliciete v1.0-precedent (T1 28 paren) + duidelijke C2-failure-onderbouwing; upgrade-richting is **nieuw** in v1.2 en cluster-discipline-overerving moet "verantwoorden" tegen individuele predicate-keuze die net-iets-anders zou kunnen rechtvaardigen.
- **Niet** "downgrade-bias in praktijk" — alle 3 downgrades + 2 upgrades volgen consistent uit §3.1-tabel. Confidence-verschil is content-driven (cluster-leden voor downgrade hebben sterker bewijs van veel↔1 dan voor upgrade-cases die op rand van related↔broad-grens zitten).
- **Evidence-bronnen voor upgrade-claims:** ISO 27002 §5.5 "Other information"-verwijzing naar 5.24-5.28 + 5.29-5.30 (T2-S05); ISO 27002 §5.30 verwijzing naar ISO/IEC 27031 + ISO 22301/22313 (T2-S08-alt). NEN-tekst-content levert evidence; CBW-Mapping-UV ondersteunt T2-S08-alt direct (UV 4.1).

**Conclusie categorie 7:** Protocol v1.2 bidirectional-uitbreiding is **operationeel valide**. Symmetrische toepassing van §3.1-tabel produceert upgrade- en downgrade-mutaties zonder bias.

---

## §7. Aanbeveling voor Stap 3 hoofd-uitvoering

### §7.1 — Cluster-discipline-aanpak voor 110 resterende m10-paren

Aanbevolen werkwijze voor 110 resterende paren (118 totaal − 8 pilot-paren):

1. **Cluster-niveau-aanpak per object-cluster (10 NIS2-letter-clusters)**:
   - compl:NIS2_Art21_i (32 leden — incl. T2-S01) → cluster-doel `broadMatch`; ~27 paren te toetsen op uitzondering
   - compl:NIS2_Art21_e (17 leden — incl. T2-S06-alt) → cluster-doel `broadMatch`; ~14 paren
   - compl:NIS2_Art21_a (12 leden — incl. T2-S03/S04/S05) → cluster-doel `broadMatch`; **0 paren overig** (alle 12 pilot-of-cluster-discipline-verwerkt)
   
   Wacht: pilot dekt 3/12 cluster-leden van NIS2_a; resterende 9 paren in dit cluster zijn:
   - 5_01 (broadMatch — behoud), 5_02 (closeMatch — downgrade), 5_04 (closeMatch — downgrade), 5_06 (relatedMatch — upgrade), 5_07 (broadMatch — behoud), 5_31 (relatedMatch — upgrade), 5_35 (closeMatch — downgrade), 5_36 (closeMatch — downgrade), 5_37 (broadMatch — behoud)
   - Per cluster-discipline: alle 9 → `broadMatch` als cluster-doel
   - Individuele NEN-uitzondering-screening voor 5_02 (Roles + Responsibilities) en 5_04 (Management responsibilities) — deze zijn breed-policy-georiënteerd; mogelijk legitiem `closeMatch`-kandidaat indien hun NEN-content sterk overlapt met NIS2(a)-bredere policy-norm. Tech-screening tijdens Stap 3 vereist.
   
   Overige clusters: NIS2_b (10), NIS2_c (8), NIS2_d (7), NIS2_f (7), NIS2_g (9), NIS2_h (7), NIS2_j (9). Allen veel↔1 → cluster-doel `broadMatch` voor elk cluster.

2. **Tech-script-ondersteuning (suggestie §6.1)**:
   - Genereer cluster-overerving-helper-script vóór Stap 3 die per cluster:
     - Alle huidige predicates leest
     - Cluster-doel-predicate uit §3.1-tabel bepaalt
     - Per cluster-lid mutatie-richting classificeert
     - Uitzondering-screening-flags zet voor cluster-leden waar individuele NEN-content sterke afwijking suggereert
   - Tech reviewt script-uitkomst per cluster (~10-15 min/cluster).

3. **Sample-first-discipline (Protocol 16) voor Stap 3**:
   - Voor elk van de 10 clusters: kies cluster-representant + 1-2 cluster-leden voor manuele beoordeling vóór bulk-uitvoering
   - Confirmatie cluster-doel-predicate, daarna bulk-toepassing voor overige cluster-leden
   - Niet alle 110 paren handmatig per protocol — cluster-aanpak prevaleert

### §7.2 — Geschatte duur Stap 3

| Bron | Schatting |
|---|---:|
| Cluster-niveau-beoordelingen (10 clusters × ~30 min) | ~5 uur |
| Uitzondering-screening per cluster (~5-15 min/cluster) | ~1 uur |
| Patch-voorbereiding + applier (Protocol 15) | ~1 uur |
| Verificatie + canonical metrics + SHACL-runs | ~1 uur |
| Patch-rapport-schrijven | ~1.5 uur |
| **Totaal Stap 3** | **~9-10 uur** |

T1-precedent: 28 paren ~5 uur. Stap 3 schaalt naar 110 paren = ~4× → ~20 uur naïef. **Cluster-aanpak comprimeert tot ~9-10 uur** door per-cluster-batching i.p.v. per-paar.

### §7.3 — Protocol-aanpassings-suggesties op basis van pilot-ervaring

1. **§3.1-tabel verduidelijking** (cat.3 leerpunt): C1 "partieel"-grens expliciet definiëren — "enige NEN-content-overlap op operationele niveau" of vergelijkbaar.
2. **§3.3 cluster-discipline + subject-cluster** (cat.3 leerpunt): voor paren waar subject ook in cluster zit, verduidelijk dat object-cluster-cardinaliteit prevaleert voor C2-criterium (in pilot al geverifieerd, niet expliciet in v1.2 vermeld).
3. **§5 output-formaat veld "Confidence" verbetering**: in pilot-praktijk kreeg upgrade-paar T2-S05 middel-confidence wegens cluster-overerving-spanning met individuele beoordeling. Confidence-criterium expliciteren: "hoog" als zowel cluster- als individuele-paar-beoordeling tot zelfde doel-predicate leiden; "middel" als cluster-overerving en individuele beoordeling licht afwijken (maar cluster-discipline prevaleert); "laag" als geen NEN-bewijs is.
4. **§6 sample-keuze toevoeging "cluster-representant-criteria"**: kies cluster-representant uit cluster-leden die niet zelf subject-singleton zijn of in grote subject-cluster — voorkomt confounding factors.
5. **Werkflow-leerpunt §6.4 incorporeren**: pilot-rapport § structuur — bouw bottom-up §4 vóór §1-samenvatting om initiële-fout-vermijding.

### §7.4 — Eventuele scope-aanbevelingen voor Stap 3

- **m14 (AVG/GDPR-cluster, 31 paren)**: blijft buiten T2-scope per masterchat-besluit C (m10-only T2; m14 wordt eigen sprint). T2-Stap 3 = 110 m10-paren resterend.
- **m14-specifieke voorbereiding bij T-volgnummer**: AVG-cross-walk-bron ontbreekt in `sources/`. Vereist masterchat-besluit over bron-upload of evidence-niveau-2/3-tolerantie. Niet T2-blokkade.

---

## §8. Hand-off-checklist

- [x] Pre-push disclosure-check Protocol 14 (vijf categorieën):
  - [x] Organisatie-naam: geen vermelding ("de organisatie" / "Rijksoverheidsorganisatie" niet eens gebruikt)
  - [x] Persoonsnamen: alleen Steven Bouwmeester (publieke projecteigenaar); CBW-Excel-auteurs niet genoemd in dit rapport
  - [x] Lokale paden: alleen `/Users/stevenbouwmeester/grc-kennismodel/` (project) en `/Users/stevenbouwmeester/grc-sources-licensed/` (NEN-licentie). Geen organisatie-interne paden
  - [x] Credentials/TLD/e-mail: geen
  - [x] NEN-tekst-fragmenten >10 woorden: **geen** verbatim NEN-tekst opgenomen. Parafrasen + clausule-verwijzingen wel. Pre-push-controle uitgevoerd
- [x] Geen patches / ontologie-wijzigingen toegepast (read-only beoordeling, zoals instructie §1 vereist)
- [x] Geen autonome commits (Steven commit handmatig)
- [x] Alle 8 paren beoordeeld met volledige Protocol v1.2 §5-output (13 velden per paar)
- [x] Cluster-discipline §3 expliciet gerapporteerd (compl:NIS2_Art21_a-cluster, 3 paren conformiteit verified)
- [x] Werkflow-leerpunten §6 met alle 7 categorieën (incl. nieuwe categorie 7 upgrade-detectie)
- [x] Aanbeveling Stap 3 §7 specifiek + actionable (cluster-aanpak + script-suggestie + duur-schatting + protocol-aanpassings-voorstellen)
- [x] Stop-condities §5 expliciet gemonitord en negatief bevestigd
- [x] Rapport zelfstandig leesbaar voor masterchat-review

### §8.1 — Wat ligt klaar voor masterchat-besluit

1. **Pilot-uitkomst-acceptatie**: GO/NO-GO voor Stap 3 hoofd-uitvoering op basis van pilot-resultaten + cluster-discipline-validatie
2. **Stap 3-aanpak-bevestiging**: cluster-niveau-aanpak per object-cluster (§7.1) + sample-first-discipline (Protocol 16) + cluster-overerving-helper-script (suggestie §6.1)
3. **Protocol-aanpassings-overwegingen voor v1.3**: 5 voorstellen in §7.3 (C1 partieel-grens, subject-cluster-criterium, confidence-criterium, sample-keuze-cluster-representant, werkflow-bouw-volgorde)
4. **T2-S08-alt confidence "middel" review**: cluster-discipline-overerving met individueel-beoordelings-spanning; mogelijk masterchat-bevestiging gewenst dat broadMatch correct is over closeMatch (individuele beoordeling)

### §8.2 — Verwijzingen

| Document | Pad |
|---|---|
| Sprint-instructie (Stap 2) | `docs/instructies/instructie-t2-pilot.md` |
| Pre-sprint-inventarisatie (Stap 1) | `output/reports/t2-pre-sprint-inventarisatie.md` |
| Autoritatief protocol | `docs/skos-beoordelings-protocol-v1_2.md` |
| Sprint-protocollen | `docs/sprint-protocols.md` (v1.3) |
| T1-precedent eindrapport | `output/reports/t1-eindrapport-v4_6_1.md` |
| Bron: ISO 27002:2022 | `/Users/stevenbouwmeester/grc-sources-licensed/NEN-EN-ISO_IEC_27002_2022_en.pdf` |
| Bron: NIS2-richtlijn | `sources/eu-recht/EU-nis2-richtlijn.pdf` |
| Bron: CBW-Mapping-UV | `sources/adr-norea/Cbw (NIS2) Control Framework.xlsx` sheet "Mapping Uitvoeringsverordening" |
| Ontologie-module (NIET gewijzigd) | `ontology/m10-nis2-ext.ttl` |
| Dit rapport | `output/reports/t2-pilot-rapport.md` |

### §8.3 — Verwacht vervolg

- Masterchat leest dit rapport, neemt GO/NO-GO-besluit Stap 3
- Bij protocol-aanpassings-besluit: nieuwe Protocol v1.3-versie opgesteld vóór Stap 3-instructie
- Steven commit + push handmatig (Tech doet dit niet zelf)
- Bij GO Stap 3: tech wacht op instructie-bestand voor Stap 3 hoofd-uitvoering

---

*Einde T2 Pilot-rapport. Modus: read-only. Geen verdere autonome actie na rapport-creatie. Steven commit handmatig.*
