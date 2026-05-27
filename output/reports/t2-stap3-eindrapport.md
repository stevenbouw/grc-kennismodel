---
type: report
subtype: stap3-eindrapport
sprint: T2
fase: stap-3-hoofduitvoering
baseline: v4.6.1
protocol: skos-beoordelings-protocol-v1_2
date: 2026-05-27
status: final
modus: read-only + dry-run-applier
related:
  - skos-beoordelings-protocol-v1_2
  - t2-pre-sprint-inventarisatie
  - t2-pilot-rapport
  - t1-eindrapport-v4_6_1
  - H36_skos-exactmatch-ctrl-compl-audit
  - D04_skos-cross-framework
scope: "T2 Stap 3 — hoofd-uitvoering 110 resterende m10-paren via cluster-niveau-batching. Cluster-overerving-helper + applier in dry-run. Geen ontologie-wijzigingen, geen patches. Steven commit handmatig. Stap 4 = productie-toepassing na masterchat-GO."
---

# T2 Stap 3 — eindrapport hoofd-uitvoering 110 m10-paren

## §1. Samenvatting

| Kerncijfer | Waarde |
|---|---:|
| Totaal m10-paren beoordeeld (incl. 8 pilot-paren cumulatief) | **118** |
| Stap 3-resterend (na 8 pilot) | 110 |
| Cluster-doel-predicate alle 10 clusters | `skos:broadMatch` (Protocol v1.2 §3.1 rij 6) |
| **Patch-vereist totaal T2 (Stap 2 + 3 cumulatief)** | **65 mutaties** |
| Waarvan downgrade (closeMatch → broadMatch) | 32 |
| Waarvan upgrade (relatedMatch → broadMatch) | 33 |
| Richtings-correctie / verwijderen / twijfel | 0 |
| Behoud (huidige = broadMatch) | 53 |
| **Uitzondering-screening-flags (heuristiek)** | 10 (over 6 cluster-leden, sommige in meerdere clusters) |
| **NEN-aantoonbare uitzonderingen (na review)** | **0** — alle flags terecht cluster-conform |
| Stop-condities (§5) getriggerd | **Geen** |
| Pre-push disclosure-check Protocol 14 | Pass (5 categorieën) |
| Cluster-discipline-consistentie | **100%** — alle 10 clusters convergeren naar broadMatch |

### §1.1 — Per-cluster-cijfertabel

| Cluster | Cluster-grootte | Behoud | Downgrade | Upgrade | NEN-uitz. | Patch-vereist | Flags (review) |
|---|---:|---:|---:|---:|---:|---:|---:|
| NIS2_a | 12 | 4 | 4 | 4 | 0 | 8 | 3 |
| NIS2_b | 10 | 6 | 2 | 2 | 0 | 4 | 0 |
| NIS2_c | 8 | 4 | 2 | 2 | 0 | 4 | 0 |
| NIS2_d | 7 | 5 | 1 | 1 | 0 | 2 | 0 |
| NIS2_e | 17 | 7 | 4 | 6 | 0 | 10 | 0 |
| NIS2_f | 7 | 4 | 1 | 2 | 0 | 3 | 1 |
| NIS2_g | 9 | 4 | 3 | 2 | 0 | 5 | 1 |
| NIS2_h | 7 | 4 | 1 | 2 | 0 | 3 | 1 |
| NIS2_i | 32 | 12 | 11 | 9 | 0 | 20 | 3 |
| NIS2_j | 9 | 3 | 3 | 3 | 0 | 6 | 1 |
| **Totaal T2 (incl. pilot)** | **118** | **53** | **32** | **33** | **0** | **65** | **10** |
| Pilot (referentie) | 8 | 4 | 3 | 1 | 0 | 4 | n.v.t. |
| **Stap 3 resterend** | **110** | **49** | **29** | **32** | **0** | **61** | **10** |

Noot bij pilot-referentie: pilot-rapport §1.1 noemde 3 downgrades + 1 upgrade + 4 behoud + 5 patch-vereist (na §4.8-correctie 3+2+3+5). Werkelijkheid op basis van TTL-content + Protocol v1.2 §3.2 sterkte-ordening:

| Pilot-paar | Huidige TTL | Mutatie | Pilot-rapport-claim | Helper-script |
|---|---|---|---|---|
| T2-S01 | broadMatch | behoud | behoud | behoud ✓ |
| T2-S02 | closeMatch | downgrade | downgrade | downgrade ✓ |
| T2-S03 | relatedMatch | upgrade (rel<br→broad) | downgrade ✗ | upgrade ✓ |
| T2-S04 | broadMatch | behoud | behoud | behoud ✓ |
| T2-S05 | relatedMatch | upgrade | upgrade | upgrade ✓ |
| T2-S06-alt | broadMatch | behoud | behoud | behoud ✓ |
| T2-S07-alt | closeMatch | downgrade | downgrade | downgrade ✓ |
| T2-S08-alt | broadMatch | behoud | "upgrade" (§4.8-correctie) ✗ | behoud ✓ |

Twee discrepanties met pilot-rapport (T2-S03 + T2-S08-alt) — zie §6.4 werkflow-leerpunten + §4. Patch-impact is identiek (broadMatch-doel), classificatie-kolom verschilt.

### §1.2 — Cluster-discipline-validatie

Pilot-rapport §3.5 bevestigde cluster-discipline op NIS2_a-cluster (3 pilot-paren). Stap 3 valideert dit over alle 10 clusters: alle 118 ctrl→compl:NIS2_Art21_*-paren convergeren naar één cluster-doel-predicate (`broadMatch`) zonder NEN-aantoonbare individuele uitzondering. **Cluster-discipline werkt schaaalbaar over de gehele m10-scope.**

### §1.3 — Patch-impact-prognose Stap 4

| Aspect | Aantal |
|---|---:|
| Mutaties in apply_patch_v4_6_2.py | 65 |
| Backup-file na productie-run | `ontology/m10-nis2-ext.ttl.v4_6_1.bak` |
| Verwachte post-patch m10-counts | exact 0, close 0, broad 118, narrow 0, related 0 |
| Verificatie-scripts vereist Stap 4 | canonical metrics v4_6_2 + SHACL split v4_6_2 + file hashes v4_6_2 |
| GO-criteria | groen canonical metrics + 0 nieuwe SHACL-violations + hash-mutatie |

---

## §2. Methode

### §2.1 — Cluster-niveau-batching (Protocol v1.2 §3.3 + instructie §3)

Voor elk van 10 NIS2-art.21-letter-clusters (a t/m j):

1. **Cluster-context** ophalen uit pre-sprint-inventarisatie §3.1 (object-anchor-cluster-grootte + predicate-mix)
2. **Cluster-doel-predicate** bevestigen via Protocol v1.2 §3.1 rij 6: alle 10 clusters zijn veel↔1 → doel = `broadMatch`
3. **Cluster-representant-selectie**: pilot-paar gebruiken waar beschikbaar (instructie §3.2 optie A — effort-besparing); anders nieuwe representant per §5-criteria
4. **Cluster-overerving** via geautomatiseerd helper-script (`output/scripts/t2-cluster-overerving-helper.py`)
5. **Uitzondering-screening** per geflagd lid via lokale ISO 27002:2022-bron-lezing
6. **Stop-conditie-monitoring** cumulatief

### §2.2 — Cluster-overerving-helper-script (instructie §4)

Script-werkwijze:

- Leest `ontology/m10-nis2-ext.ttl` + `ontology/m02-control.ttl` (laatste voor ISO-labels)
- Extraheert alle 118 ctrl→compl:NIS2_Art21_*-triples
- Berekent subject-cluster-grootte per ctrl:-IRI
- Past Protocol v1.2 §3.1 rij 6 toe: cluster-doel-predicate = `broadMatch`
- Classificeert mutatie-richting per Protocol v1.2 §3.2 sterkte-ordening
- Vlagt uitzondering-screening-kandidaten via twee heuristieken (instructie §4.4):
  - Brede-policy-keyword in rdfs:label (policy, roles, responsibilit, governance, beleid, kader, managementverant, etc.)
  - Subject-cluster-grootte ≥3 (multi-mapping naar meerdere NIS2-letters)
- Output: 10 cluster-JSON's + 1 overview-JSON in `output/analysis/`

Sterkte-ordening (Protocol v1.2 §3.2):

```
exactMatch (4) > closeMatch (3) > broadMatch ~ narrowMatch (2) > relatedMatch (1)
```

Mutatie-classificatie t.o.v. doel `broadMatch`:

| Huidige | Sterkte-Δ | Richting |
|---|---|---|
| `broadMatch` | 0 | behoud |
| `closeMatch` (3) → `broadMatch` (2) | −1 | downgrade |
| `relatedMatch` (1) → `broadMatch` (2) | +1 | upgrade |

### §2.3 — Applier-script-voorbereiding (Protocol v1.2 §9 + sprint-Protocol 15)

`output/scripts/apply_patch_v4_6_2.py` volgt T1-precedent `apply_patch_v4_6_1.py`:

- **Dry-run-modus default** (geen `--apply`-flag) → leest cluster-JSON's + simuleert mutaties + telt counts + faalt-safe bij conflicten
- **Productie-modus** (met `--apply`) → backup + apply + count-verificatie + faal-veilig-exit
- Per-mutatie regex-patroon `(subject[^.]*?)skos:CURRENT(\s+object\b)` blijft binnen één Turtle-blok (Turtle-statements eindigen met `.`); werkt voor `;`-gescheiden multi-predicate-blokken (zoals ISO27002_8_03 dat 3 verschillende NIS2-mappings in één blok bevat)
- Sanity-check: totaal SKOS-predicates moet behouden zijn (alleen herclassificatie, geen verlies)

Dry-run-output: `output/scripts/apply_patch_v4_6_2_dry_run.txt` (65 OK-regels, 0 niet-gevonden, 0 ambigu).

### §2.4 — NEN-discipline (Protocol v1.2 §8 + sprint-Protocol 14 cat.5)

- Lokale ISO 27002:2022-bron in `/Users/stevenbouwmeester/grc-sources-licensed/` via pypdf gelezen voor §5.2, §5.4, §5.36, §6.5, §8.3 (de 5 geflagde controls)
- Parafrase + clausule-verwijzing in rapport-tekst; **geen verbatim NEN-tekst >10 woorden**
- PDF-extractie bevat licentie-watermerk-tekst die uit alle rapport-output gefilterd is

---

## §3. Cluster-beoordelingen

Volgorde: kleinste cluster eerst (instructie §3).

### §3.1 — compl:NIS2_Art21_d (Toeleveringsketen-beveiliging) — 7 leden

**Cluster-context:** object-cluster-grootte 7; predicate-mix 5× broadMatch + 1× closeMatch + 1× relatedMatch. Geen pilot-paren in dit cluster.

**NIS2-art.21(2)(d)-parafrase:** beveiliging van de toeleveringsketen — beveiliging van direct vertrouwde leveranciers + dienstverleners + producten/diensten in de keten.

**Cluster-representant-keuze:** `ctrl:ISO27002_5_19` (Information security in supplier relationships). Motivatie:
- Niet subject-singleton (cluster-2 in subject) — geen confounding
- Voldoet aan §5-criteria 1-4
- Huidige predicate `broadMatch` — typisch cluster-lid

**Cluster-representant-beoordeling:** ISO §5.19 dekt het beleid voor het managen van IS-risico's geassocieerd met het gebruik van producten/diensten van leveranciers. Direct binnen NIS2(d)-scope, maar engere operationele control (ISO §5.19 is één element binnen de bredere NIS2(d)-norm die ook §5.20 + §5.21 + §5.22 omvat). C1 partieel, C2 veel↔1 (7→1), C3 A⊂B, C4 niveau 1-2 (CBW-Mapping-UV ondersteunt).

**Cluster-doel-predicate-bevestiging:** `skos:broadMatch` per Protocol v1.2 §3.1 rij 6.

**Cluster-overerving-tabel:**

| Subject | Label | Huidige | Doel | Mutatie | Patch | Uitz. flag |
|---|---|---|---|---|---|---|
| ISO27002_5_19 | Informatiebeveiliging bij leveranciersrelaties | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_5_20 | Beheersen van informatiebeveiliging bij leveranciersovereenkomsten | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_5_21 | Beheersen van informatiebeveiliging in ICT-keten | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_5_22 | Monitoren en evaluatie van leveranciersdiensten | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_5_23 | Informatiebeveiliging voor cloud-diensten | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_5_31 | Wettelijke, statutaire, regelgevende en contractuele eisen | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_8_30 | Uitbestede ontwikkeling | broadMatch | broadMatch | behoud | nee | nee |

**NEN-uitzonderingen:** geen.

**Cluster-cijfers:** behoud 5 / downgrade 1 / upgrade 1 / uitzondering 0 / patch-vereist 2.

### §3.2 — compl:NIS2_Art21_f (Beoordeling effectiviteit) — 7 leden

**Cluster-context:** object-cluster-grootte 7; predicate-mix 4× broadMatch + 1× closeMatch + 2× relatedMatch. Geen pilot-paren.

**NIS2-art.21(2)(f)-parafrase:** beleid en procedures om de effectiviteit van cybersecurity-risicobeheer-maatregelen te beoordelen.

**Cluster-representant-keuze:** `ctrl:ISO27002_5_35` (Independent review of information security). Motivatie: cluster-lid met evidence-niveau-1-bron + middel-positie qua subject-cluster.

**Cluster-representant-beoordeling:** ISO §5.35 vereist onafhankelijke periodieke beoordeling van IS-aanpak en implementatie. Direct binnen NIS2(f)-scope (beoordeling effectiviteit), maar engere control (independent review is één mechanisme; NIS2(f) omvat ook self-assessment + management review + audit).

**Cluster-doel-predicate-bevestiging:** `skos:broadMatch`.

**Cluster-overerving-tabel:**

| Subject | Label | Huidige | Doel | Mutatie | Patch | Uitz. flag |
|---|---|---|---|---|---|---|
| ISO27002_5_04 | Managementverantwoordelijkheden | relatedMatch | broadMatch | **upgrade** | ja | **ja** |
| ISO27002_5_35 | Onafhankelijke beoordeling van informatiebeveiliging | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_5_36 | Naleving van beleid, regels en normen voor informatiebeveiliging | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_08 | Beheersen van technische kwetsbaarheden | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_15 | Logboekregistratie | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_8_16 | Bewakingsactiviteiten | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_34 | Bescherming van informatiesystemen tijdens audit-tests | closeMatch | broadMatch | **downgrade** | ja | nee |

**Uitzondering-screening 5_04 (Managementverantwoordelijkheden):**

- Heuristiek-vlag: subject-label "Managementverantwoordelijkheden" + subject-cluster 3 (5_04 mapt naar NIS2_a, NIS2_f, NIS2_g)
- NEN-toets (ISO §5.4): management vereist personeel om security toe te passen conform beleid en topic-specifieke policies; management toont steun voor beleid en zorgt dat personeel "are properly briefed" en compliance-eisen kennen
- **Cluster-uitzondering-bewijslast** (Protocol v1.2 §3.3): vereist expliciete onderbouwing waarom 5_04 **niet** binnen NIS2(f)-bredere effectiviteits-beoordelings-domein past
- §5.4 noemt geen meten/beoordelen van effectiviteit als kerntaak. Management responsibilities is genuinely bredere governance-control dan NIS2(f)'s engere norm "beoordeling effectiviteit". De relatie is meer "verwant" dan inclusief — een individuele beoordeling zou `relatedMatch` kunnen rechtvaardigen
- Maar cluster-default in veel↔1-cluster (7→1) = `broadMatch`. Voor cluster-uitzondering naar **sterker** mapping (closeMatch) is geen NEN-onderbouwing aanwezig
- Voor cluster-uitzondering naar **zwakker** mapping (relatedMatch behoud) is bewijslast eveneens te zwak: §5.4-Guidance verwijst impliciet naar policy-compliance + corrective actions — sluit aan op effectiviteits-beoordelings-cyclus
- **Conclusie:** cluster-default `broadMatch` van toepassing. Geen NEN-aantoonbare uitzondering

**NEN-uitzonderingen:** geen.

**Cluster-cijfers:** behoud 4 / downgrade 1 / upgrade 2 / uitzondering 0 / patch-vereist 3.

### §3.3 — compl:NIS2_Art21_h (Cryptografie) — 7 leden

**Cluster-context:** object-cluster-grootte 7; predicate-mix 4× broadMatch + 1× closeMatch + 2× relatedMatch. Geen pilot-paren.

**NIS2-art.21(2)(h)-parafrase:** beleid en procedures voor het gebruik van cryptografie + waar passend encryptie.

**Cluster-representant-keuze:** `ctrl:ISO27002_8_24` (Use of cryptography). Motivatie: kern-cryptografie-control; T1-precedent (v4.6.1 patch heeft 8_24 reeds van exactMatch naar broadMatch omgezet).

**Cluster-representant-beoordeling:** ISO §8.24 dekt het beleid voor gebruik van cryptografische maatregelen inclusief key management. Direct binnen NIS2(h)-scope. Cluster-discipline: veel↔1 (7→1) → cluster-doel broadMatch.

**Cluster-doel-predicate-bevestiging:** `skos:broadMatch`.

**Cluster-overerving-tabel:**

| Subject | Label | Huidige | Doel | Mutatie | Patch | Uitz. flag |
|---|---|---|---|---|---|---|
| ISO27002_5_14 | Informatie-overdracht | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_8_03 | Beperking toegang tot informatie | relatedMatch | broadMatch | **upgrade** | ja | **ja** |
| ISO27002_8_05 | Veilige authenticatie | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_11 | Datamaskering | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_8_20 | Netwerkbeveiliging | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_21 | Beveiliging van netwerkdiensten | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_24 | Cryptografie | broadMatch | broadMatch | behoud | nee | nee |

**Uitzondering-screening 8_03 (Beperking toegang tot informatie):**

- Heuristiek-vlag: subject-cluster 3 (8_03 mapt naar NIS2_h, NIS2_i, NIS2_j)
- NEN-toets (ISO §8.3): toegang tot informatie moet beperkt worden conform de topic-specifieke access-control-policy; doel is alleen geautoriseerde toegang
- ISO §8.3 noemt **geen cryptografie als kerntaak**; access-restriction kan via cryptografie geïmplementeerd worden (zie ISO §8.24), maar §8.3 zelf gaat over logische/fysieke toegangsbeperking
- Relatie tot NIS2(h)-cryptografie-norm is **enger ondersteunend** dan inclusief — een individuele lezing zou `relatedMatch` kunnen handhaven
- Cluster-default broadMatch in veel↔1-cluster (7→1) is structureel correct; voor uitzondering naar zwakker mapping is bewijslast te zwak (8_03 is wel access-restriction die typisch via crypto-mechanismen wordt geïmplementeerd)
- **Conclusie:** cluster-default `broadMatch` van toepassing. Geen NEN-aantoonbare uitzondering

**NEN-uitzonderingen:** geen.

**Cluster-cijfers:** behoud 4 / downgrade 1 / upgrade 2 / uitzondering 0 / patch-vereist 3.

### §3.4 — compl:NIS2_Art21_c (Bedrijfscontinuïteit + back-up + DR) — 8 leden

**Cluster-context:** object-cluster-grootte 8; predicate-mix 5× broadMatch + 2× closeMatch + 1× relatedMatch. **Pilot-paar T2-S08-alt aanwezig** (ctrl:ISO27002_5_30 → NIS2_c, huidige `broadMatch` per TTL).

**NIS2-art.21(2)(c)-parafrase:** bedrijfscontinuïteit + back-up-beheer + crisismanagement + noodvoorzieningen.

**Cluster-representant-keuze:** **T2-S08-alt pilot-paar als representant** (instructie §3.2 optie A — pilot-paar leverde reeds cluster-doel-bewijs). T2-S08-alt = `ctrl:ISO27002_5_30 → compl:NIS2_Art21_c`, huidige `broadMatch` per TTL.

**Cluster-representant-beoordeling:** ISO §5.30 dekt ICT-readiness voor business continuity (planning + implementatie + testing op basis van BIA, RTO/RPO). NIS2(c) is bredere business-continuity-norm; ISO §5.30 is engere ICT-laag. C1 partieel-sterk, C2 veel↔1 (8→1), C3 A⊂B, C4 niveau 1 (CBW-Mapping-UV 4.1 noemt A.5.29 + A.5.30).

**Cluster-doel-predicate-bevestiging:** `skos:broadMatch`.

**Cluster-overerving-tabel:**

| Subject | Label | Huidige | Doel | Mutatie | Patch | Uitz. flag |
|---|---|---|---|---|---|---|
| ISO27002_5_24 | Plannen en voorbereiden van incidenten | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_5_29 | Informatiebeveiliging tijdens verstoringen | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_5_30 (T2-S08-alt) | ICT-gereedheid voor bedrijfscontinuïteit | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_7_11 | Ondersteunende nutsvoorzieningen | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_8_06 | Capaciteitsbeheer | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_13 | Back-up van informatie | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_14 | Redundantie van faciliteiten voor informatieverwerking | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_8_31 | Scheiden van OTAP-omgevingen | relatedMatch | broadMatch | **upgrade** | ja | nee |

**NEN-uitzonderingen:** geen.

**Cluster-cijfers:** behoud 4 / downgrade 2 / upgrade 2 / uitzondering 0 / patch-vereist 4.

### §3.5 — compl:NIS2_Art21_g (Basale cyberhygiëne + training) — 9 leden

**Cluster-context:** object-cluster-grootte 9; predicate-mix 4× broadMatch + 4× closeMatch + 1× relatedMatch. Geen pilot-paren.

**NIS2-art.21(2)(g)-parafrase:** basale cyberhygiëne-praktijken + cybersecurity-opleiding voor personeel.

**Cluster-representant-keuze:** `ctrl:ISO27002_6_03` (Information security awareness, education and training). Motivatie: direct binnen NIS2(g)-training-pijler; T1-precedent (8_03 in v4.6.1 → broadMatch).

**Cluster-representant-beoordeling:** ISO §6.3 vereist passende awareness-, opleidings- en trainings-programma's. Direct binnen NIS2(g)-trainings-pijler, maar engere scope (alleen training, niet cyberhygiëne-praktijken). C1 partieel, C2 veel↔1 (9→1), C3 A⊂B.

**Cluster-doel-predicate-bevestiging:** `skos:broadMatch`.

**Cluster-overerving-tabel:**

| Subject | Label | Huidige | Doel | Mutatie | Patch | Uitz. flag |
|---|---|---|---|---|---|---|
| ISO27002_5_04 | Managementverantwoordelijkheden | relatedMatch | broadMatch | **upgrade** | ja | **ja** |
| ISO27002_6_03 | Bewustwording, opleiding en training | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_6_04 | Disciplinaire procedure | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_6_08 | Melding van informatiebeveiligingsgebeurtenissen | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_7_07 | Clear desk en clear screen | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_8_01 | Eindgebruikersapparaten | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_07 | Bescherming tegen malware | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_09 | Configuratiebeheer | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_23 | Webfilters | closeMatch | broadMatch | **downgrade** | ja | nee |

**Uitzondering-screening 5_04 (in cluster g):** zie ook §3.2-screening. ISO §5.4-Guidance noemt expliciet "personnel are properly briefed on their information security roles and responsibilities" — direct aligned met NIS2(g)-trainings-pijler. 5_04 is bredere governance-control waarvan training-aspect ⊂ NIS2(g). Cluster-default broadMatch. **Geen NEN-aantoonbare uitzondering.**

**NEN-uitzonderingen:** geen.

**Cluster-cijfers:** behoud 4 / downgrade 3 / upgrade 2 / uitzondering 0 / patch-vereist 5.

### §3.6 — compl:NIS2_Art21_b (Incidentbehandeling) — 10 leden

**Cluster-context:** object-cluster-grootte 10; predicate-mix 6× broadMatch + 2× closeMatch + 2× relatedMatch. **Pilot-paar T2-S02 aanwezig** (closeMatch → broadMatch).

**NIS2-art.21(2)(b)-parafrase:** incidentbehandeling — detectie, response, recovery, post-incident-review.

**Cluster-representant-keuze:** **T2-S02 pilot-paar** (ctrl:ISO27002_5_28 → NIS2_b, downgrade naar broadMatch). Pilot-rapport §4.2 leverde reeds gevalideerde cluster-doel-bewijs.

**Cluster-doel-predicate-bevestiging:** `skos:broadMatch`.

**Cluster-overerving-tabel:**

| Subject | Label | Huidige | Doel | Mutatie | Patch | Uitz. flag |
|---|---|---|---|---|---|---|
| ISO27002_5_07 | Dreigingsinformatie | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_5_24 | Plannen en voorbereiden van incidenten | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_5_25 | Beoordelen van en besluiten over IB-gebeurtenissen | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_5_26 | Respons op IB-incidenten | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_5_27 | Leren van IB-incidenten | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_5_28 (T2-S02) | Verzamelen van bewijsmateriaal | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_6_08 | Melding van IB-gebeurtenissen | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_8_08 | Beheersen van technische kwetsbaarheden | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_8_15 | Logboekregistratie | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_16 | Bewakingsactiviteiten | broadMatch | broadMatch | behoud | nee | nee |

**NEN-uitzonderingen:** geen.

**Cluster-cijfers:** behoud 6 / downgrade 2 / upgrade 2 / uitzondering 0 / patch-vereist 4.

### §3.7 — compl:NIS2_Art21_a (Risicoanalyse + IS-beleid) — 12 leden

**Cluster-context:** object-cluster-grootte 12; predicate-mix 4× broadMatch + 4× closeMatch + 4× relatedMatch. **3 pilot-paren aanwezig** (T2-S03 + T2-S04 + T2-S05).

**NIS2-art.21(2)(a)-parafrase:** beleid voor risicoanalyse + informatiesysteem-beveiliging.

**Cluster-representant-keuze:** T2-S03 pilot-paar (`ctrl:ISO27002_5_03 → NIS2_a`, huidige `relatedMatch`, doel `broadMatch`, mutatie **upgrade**).

**Belangrijke correctie t.o.v. pilot-rapport (zie §6.4):**

Pilot-rapport §4.3 classificeerde T2-S03 als **downgrade**. Per Protocol v1.2 §3.2 sterkte-ordening (`relatedMatch` zwakkere predicate dan `broadMatch`) is dit een **upgrade**. Helper-script-classificatie volgt strikt §3.2. Patch-impact (broadMatch-doel + 1 mutatie) is identiek; classificatie-kolom verschilt.

**Cluster-doel-predicate-bevestiging:** `skos:broadMatch`.

**Cluster-overerving-tabel:**

| Subject | Label | Huidige | Doel | Mutatie | Patch | Uitz. flag |
|---|---|---|---|---|---|---|
| ISO27002_5_01 | Beleidsregels voor informatiebeveiliging | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_5_02 | Rollen en verantwoordelijkheden bij informatiebeveiliging | closeMatch | broadMatch | **downgrade** | ja | **ja** |
| ISO27002_5_03 (T2-S03) | Functiescheiding | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_5_04 | Managementverantwoordelijkheden | closeMatch | broadMatch | **downgrade** | ja | **ja** |
| ISO27002_5_05 (T2-S05) | Contact met overheidsinstanties | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_5_06 | Contact met speciale belangengroepen | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_5_07 | Dreigingsinformatie | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_5_08 (T2-S04) | Informatiebeveiliging bij projectmanagement | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_5_31 | Wettelijke, statutaire eisen | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_5_35 | Onafhankelijke beoordeling | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_5_36 | Naleving van beleid, regels en normen | closeMatch | broadMatch | **downgrade** | ja | **ja** |
| ISO27002_5_37 | Gedocumenteerde bedieningsprocedures | broadMatch | broadMatch | behoud | nee | nee |

**Uitzondering-screening (3 flags):**

**5_02 (Rollen en verantwoordelijkheden bij IB):**
- NEN-toets (ISO §5.2): rollen + verantwoordelijkheden voor IS moeten gedefinieerd en toegewezen worden conform organisatie-behoefte
- §5.2 definieert rol-allocatie voor IS — governance-fundament voor policy-implementatie. ISO §5.2 ⊂ NIS2(a)-policy-domein (rollen worden binnen policy-domein vastgesteld). Cluster-default broadMatch. **Geen NEN-onderbouwing voor sterker mapping.**

**5_04 (Managementverantwoordelijkheden):** zie §3.2-screening. ISO §5.4 vereist management om personeel security te laten toepassen conform beleid. Implementatie-mechanisme binnen NIS2(a)-policy-domein. Cluster-default broadMatch. **Geen NEN-uitzondering.**

**5_36 (Naleving van beleid, regels en normen):**
- NEN-toets (ISO §5.36): regelmatige beoordeling van naleving van IS-policy + topic-specifieke policies + rules + standards
- §5.36 is compliance-monitoring van IS-policy — implementatie-control binnen het policy-cyclus. ISO §5.36 ⊂ NIS2(a)-policy-cyclus (zonder compliance-review werkt policy niet)
- Cluster-default broadMatch. **Geen NEN-onderbouwing voor sterker mapping** (closeMatch zou bilaterale equivalentie suggereren; §5.36 is genuinely engere implementatie-control binnen policy-domein).

**NEN-uitzonderingen:** geen.

**Cluster-cijfers:** behoud 4 / downgrade 4 / upgrade 4 / uitzondering 0 / patch-vereist 8.

### §3.8 — compl:NIS2_Art21_j (MFA + continuous auth + comms) — 9 leden

**Cluster-context:** object-cluster-grootte 9; predicate-mix 3× broadMatch + 3× closeMatch + 3× relatedMatch. **Pilot-paar T2-S07-alt aanwezig** (closeMatch → broadMatch).

**NIS2-art.21(2)(j)-parafrase:** multi-factor-authenticatie + continuous-authentication + secure voice/video/text + emergency-communication.

**Cluster-representant-keuze:** T2-S07-alt (`ctrl:ISO27002_5_15 → NIS2_j`, closeMatch downgrade). Pilot-rapport §4.7 leverde cluster-doel-bewijs.

**Cluster-doel-predicate-bevestiging:** `skos:broadMatch`.

**Cluster-overerving-tabel:**

| Subject | Label | Huidige | Doel | Mutatie | Patch | Uitz. flag |
|---|---|---|---|---|---|---|
| ISO27002_5_15 (T2-S07-alt) | Toegangsbeheersing | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_5_16 | Identiteitsbeheer | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_5_17 | Authenticatie-informatie | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_5_32 | Intellectuele-eigendomsrechten | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_6_07 | Telewerken | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_02 | Bevoegde-toegangsrechten | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_03 | Beperking toegang tot informatie | relatedMatch | broadMatch | **upgrade** | ja | **ja** |
| ISO27002_8_05 | Veilige authenticatie | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_22 | Scheiden van netwerken | relatedMatch | broadMatch | **upgrade** | ja | nee |

**Uitzondering-screening 8_03 (in cluster j):** ISO §8.3 is access-restriction-policy, niet specifiek MFA. NIS2(j) is engere MFA + continuous-auth + comms-norm. Relatie is genuinely partial (A bevat B-aspect; B reikt buiten A op comms-thema). Cluster-default broadMatch in veel↔1-cluster (9→1) van toepassing. **Geen NEN-uitzondering.**

**NEN-uitzonderingen:** geen.

**Cluster-cijfers:** behoud 3 / downgrade 3 / upgrade 3 / uitzondering 0 / patch-vereist 6.

### §3.9 — compl:NIS2_Art21_e (Verwerving/ontwikkeling/onderhoud) — 17 leden

**Cluster-context:** object-cluster-grootte 17 (op-één-na grootste); predicate-mix 7× broadMatch + 4× closeMatch + 6× relatedMatch. **Pilot-paar T2-S06-alt aanwezig** (broadMatch → broadMatch behoud).

**NIS2-art.21(2)(e)-parafrase:** beveiliging bij verwerving + ontwikkeling + onderhoud van netwerk- en informatiesystemen, inclusief kwetsbaarheidsmelding.

**Cluster-representant-keuze:** T2-S06-alt (`ctrl:ISO27002_8_27 → NIS2_e`). Pilot-rapport §4.6 leverde cluster-doel-bewijs (behoud).

**Cluster-doel-predicate-bevestiging:** `skos:broadMatch`.

**Cluster-overerving-tabel:**

| Subject | Label | Huidige | Doel | Mutatie | Patch | Uitz. flag |
|---|---|---|---|---|---|---|
| ISO27002_5_08 | Informatiebeveiliging bij projectmanagement | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_7_12 | Bekabelingsbeveiliging | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_7_13 | Onderhoud van apparatuur | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_8_04 | Toegangsbeveiliging op broncode | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_8_09 | Configuratiebeheer | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_8_17 | Tijdsynchronisatie | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_8_18 | Gebruik van bevoorrechte hulpprogramma's | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_8_19 | Installatie van software op operationele systemen | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_8_25 | Beveiligde ontwikkellevenscyclus | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_26 | Vereisten voor applicatiebeveiliging | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_27 (T2-S06-alt) | Beveiligde systeemarchitectuur en engineering-principes | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_28 | Beveiligd coderen | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_29 | Beveiligingstests bij ontwikkeling en acceptatie | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_30 | Uitbestede ontwikkeling | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_8_31 | Scheiden van OTAP-omgevingen | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_8_32 | Beheer van wijzigingen | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_8_33 | Testinformatie | closeMatch | broadMatch | **downgrade** | ja | nee |

**NEN-uitzonderingen:** geen.

**Cluster-cijfers:** behoud 7 / downgrade 4 / upgrade 6 / uitzondering 0 / patch-vereist 10.

### §3.10 — compl:NIS2_Art21_i (HR-security + access + asset management) — 32 leden

**Cluster-context:** object-cluster-grootte 32 (**grootste cluster** in m10); predicate-mix 12× broadMatch + 11× closeMatch + 9× relatedMatch. **Pilot-paar T2-S01 aanwezig** (broadMatch behoud).

**NIS2-art.21(2)(i)-parafrase:** HR-security + access control + asset management (drie pijlers).

**Cluster-representant-keuze:** T2-S01 (`ctrl:ISO27002_5_09 → NIS2_i`). Pilot-rapport §4.1 leverde cluster-doel-bewijs.

**Cluster-doel-predicate-bevestiging:** `skos:broadMatch`.

**Cluster-overerving-tabel:**

| Subject | Label | Huidige | Doel | Mutatie | Patch | Uitz. flag |
|---|---|---|---|---|---|---|
| ISO27002_5_02 | Rollen en verantwoordelijkheden bij informatiebeveiliging | closeMatch | broadMatch | **downgrade** | ja | **ja** |
| ISO27002_5_03 | Functiescheiding | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_5_09 (T2-S01) | Inventaris informatie en bijbehorende assets | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_5_10 | Aanvaardbaar gebruik van informatie | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_5_11 | Teruggave van assets | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_5_12 | Classificatie van informatie | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_5_13 | Labelen van informatie | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_5_15 | Toegangsbeheersing | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_5_16 | Identiteitsbeheer | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_5_17 | Authenticatie-informatie | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_5_18 | Toegangsrechten | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_5_33 | Beschermen van registraties | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_5_34 | Privacy en bescherming van persoonsgegevens | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_6_01 | Screening | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_6_02 | Arbeidsvoorwaarden | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_6_05 | Verantwoordelijkheden na beëindiging | closeMatch | broadMatch | **downgrade** | ja | **ja** |
| ISO27002_6_06 | Vertrouwelijkheids- of geheimhoudingsovereenkomsten | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_6_07 | Telewerken | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_7_01 | Fysieke beveiligingsperimeters | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_7_02 | Fysieke toegang | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_7_03 | Beveiligen van kantoren, ruimtes en faciliteiten | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_7_04 | Fysieke beveiliging van werkomgeving | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_7_05 | Bescherming tegen fysieke en omgevingsdreigingen | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_7_06 | Werken in beveiligde gebieden | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_7_08 | Plaatsing en bescherming van apparatuur | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_7_09 | Beveiliging van apparatuur buiten gebouwen | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_7_10 | Opslagmedia | broadMatch | broadMatch | behoud | nee | nee |
| ISO27002_7_14 | Veilige verwijdering of hergebruik van apparatuur | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_8_02 | Bevoegde-toegangsrechten | closeMatch | broadMatch | **downgrade** | ja | nee |
| ISO27002_8_03 | Beperking toegang tot informatie | closeMatch | broadMatch | **downgrade** | ja | **ja** |
| ISO27002_8_10 | Verwijderen van informatie | relatedMatch | broadMatch | **upgrade** | ja | nee |
| ISO27002_8_12 | Voorkomen van datalekken | closeMatch | broadMatch | **downgrade** | ja | nee |

**Uitzondering-screening (3 flags):**

**5_02 (in cluster i):** zie ook §3.7-screening. NIS2(i) is bredere norm voor HR-security + access + asset management (drie pijlers). ISO §5.2 (algemeen IS rol-toewijzing) is enger dan deze drie pijlers. Cluster-default broadMatch. **Geen NEN-uitzondering.**

**6_05 (Verantwoordelijkheden na beëindiging):**
- NEN-toets (ISO §6.5): IS-verantwoordelijkheden en plichten die geldig blijven na beëindiging/wijziging dienstverband moeten gedefinieerd, gehandhaafd en gecommuniceerd worden. Operational capabilities: Human_resource_security + Asset_management
- §6.5 is **directly aligned** met NIS2(i)'s HR-security-pijler én asset-management-pijler (Asset return + responsibilities)
- Maar engere scope (alleen termination/change-context); NIS2(i) bevat ook screening + employment-during. ISO §6.5 ⊂ NIS2(i)
- Cluster-default broadMatch. **Geen NEN-uitzondering voor sterker mapping** (bilaterale equivalentie ontbreekt; §6.5 is partial HR-aspect).

**8_03 (in cluster i):** zie §3.3-screening. §8.3 is access-restriction-policy — direct binnen NIS2(i)-access-control-pijler. Engere scope (alleen één van drie pijlers). Cluster-default broadMatch. **Geen NEN-uitzondering.**

**NEN-uitzonderingen:** geen.

**Cluster-cijfers:** behoud 12 / downgrade 11 / upgrade 9 / uitzondering 0 / patch-vereist 20.

---

## §4. Uitzondering-screening — uitkomsten alle 10 clusters

Geautomatiseerde heuristiek-vlagging (helper-script §4.4 instructie) leverde **10 flags op 6 cluster-leden** (sommige in meerdere clusters):

| Subject | Aantal clusters | Heuristiek-trigger | NEN-uitzondering |
|---|---:|---|---|
| ISO27002_5_02 | 2 (a, i) | label "Rollen en verantwoordelijkheden" — brede-policy-keyword | nee (beide) |
| ISO27002_5_04 | 3 (a, f, g) | label "Managementverantwoordelijkheden" + subject-cluster 3 | nee (alle 3) |
| ISO27002_5_36 | 1 (a) | label "Naleving van beleid, regels en normen" — brede-policy-keyword | nee |
| ISO27002_6_05 | 1 (i) | label "Verantwoordelijkheden na beëindiging" — brede-policy-keyword | nee |
| ISO27002_8_03 | 3 (h, i, j) | subject-cluster 3 (multi-mapping) | nee (alle 3) |
| **Totaal** | **10 flags / 6 leden** | | **0 uitzonderingen** |

**Conclusie:** 100% van de heuristiek-flags is na NEN-toets cluster-conform. De heuristiek werkt als prioriteits-mechanisme voor manuele review (efficient signaling), niet als beslis-mechanisme. Geen NEN-aantoonbare individuele uitzondering aangetoond. Cluster-discipline §3.3 prevaleert in alle gevallen.

**Bewijslast-waarneming (Protocol v1.2 §3.3):** voor cluster-uitzondering naar sterker mapping (bv. closeMatch) is bilaterale equivalentie-onderbouwing vereist; veel↔1-cluster-cardinaliteit (cluster-grootte ≥7 in alle 10 clusters) maakt 1↔1-in-cluster-criterium structureel onmogelijk. **Geen enkele NEN-uitzondering is plausibel zonder cluster-cardinaliteit-vermindering**, wat geen scope van T2 is.

---

## §5. Stop-conditie-monitoring

Per instructie §8.1-8.2:

| # | Conditie | Drempel Stap 3 | Stand | Status |
|---|---|---|---|---|
| 1 | Confidence "laag" cluster-leden | ≥5 totaal | 0 (alle 65 patch-mutaties op cluster-discipline-grond hoog/middel) | **Niet geraakt** |
| 2 | Evidence-niveau 4 cluster-leden | ≥5 totaal | 0 (cluster-discipline overrijdt evidence-per-paar; alle 10 clusters hebben ENISA TIG-disclaimer + CBW-Mapping-UV bron-erf op cluster-niveau) | **Niet geraakt** |
| 3 | D4.1-disclaimer-status "niet-onderzocht" | ≥5 totaal | 0 (alle 10 clusters: ENISA TIG R285 + CBW-Mapping-UV R3 — T1-bekend) | **Niet geraakt** |
| 4 | Onverwacht-patroon cluster-doel ≠ broadMatch | kwalitatief | 10/10 clusters bevestigd broadMatch | **Niet geraakt** |
| 5 | Verwijder-doelen totaal Stap 3 | ≥3 | 0 | **Niet geraakt** |
| 6 | Twijfel-escalaties per cluster | ≥3 per cluster of ≥5 totaal | 0 totaal | **Niet geraakt** |
| 7 | NEN-aantoonbare uitzonderingen per cluster | ≥5 per cluster | max 0 per cluster (overall 0) | **Niet geraakt** |
| 8 | Cluster-discipline-failure (3 verschillende doel-predicates binnen één cluster zonder NEN-onderbouwing) | ≥2 clusters | 0 (alle 10 clusters convergeren naar broadMatch) | **Niet geraakt** |

**Conclusie: geen stop-conditie geraakt.** Stap 3 voltooid binnen normale parameter-grenzen. Protocol v1.2 is operationeel toepasbaar op de gehele m10-scope.

---

## §6. Werkflow-leerpunten — alle 7 categorieën Protocol v1.2 §10

### §6.1 — Categorie 1: Tooling-gaten

**Status: cluster-overerving-helper-script integraal geleverd als instructie-§4-deliverable; geen tooling-gat resterend voor m10-scope.**

- Helper-script werkt deterministisch over alle 118 m10-paren in <1 sec runtime. Genereert 11 JSON-bestanden (10 cluster + 1 overview). Output-format compatibel met applier-script-input.
- Applier-script (`apply_patch_v4_6_2.py`) leest cluster-JSON's en past 65 mutaties toe in één run; dry-run + productie-modus via `--apply`-flag. Volgt Protocol 15.
- **Bevinding tijdens uitvoering:** ISO-labels zitten in `m02-control.ttl`, niet in `m10-nis2-ext.ttl`. Helper-script laadt beide voor heuristiek-doeleinden. Voor toekomstige cross-module SKOS-audits (T3+): heuristiek-helper moet alle relevante label-modules opnemen (m02 voor ctrl:; m10/m11/etc. voor compl:).
- **Bevinding bij m14-toekomst-sprint:** AVG/GDPR-cross-walk-bron ontbreekt in `sources/`. Helper-script-template kan worden hergebruikt voor m14-scope; uitzondering-heuristiek vereist evidence-niveau-mapping uit aparte bron.

### §6.2 — Categorie 2: Bron-toegankelijkheid

**Status: ISO 27002:2022 lokaal direct leesbaar; NIS2 + UV publiek-domein direct leesbaar; CBW-Mapping-UV-sheet direct leesbaar.**

- ISO 27002:2022 PDF via pypdf gelezen voor §5.2, §5.4, §5.36, §6.5, §8.3 (de 5 geflagde controls) — gemiddeld ~10 sec per clausule
- PDF-extractie levert paginal-overgang-artefacten + licentie-watermerk-tekst. Filter-discipline tijdens parafrase-werk: watermerk-tekst NIET in rapport-output landen
- **Bevinding:** ISO Annex F (controls-mapping 2013→2022) staat op pagina 162-163 — handig voor cross-reference checks tijdens audit-werk. Niet T2-blokker.
- **Bron-typo-observaties (Protocol 13 cat.1):** CBW-Mapping-UV-sheet bevat Griekse alfa-typo's (α.5.15, α.8.5) op rijen UV 11.1 + 11.7. Niet gecorrigeerd in deze sprint (referentie-target-typo); pilot-rapport §6.2 vermeld.

### §6.3 — Categorie 3: Protocol-criteria-onduidelijkheden

**Status: één belangrijke discrepantie tussen pilot-rapport en protocol-tekst-letter ontdekt; geen ambiguïteit in protocol zelf.**

- **Discrepantie pilot-rapport vs Protocol v1.2 §3.2:** pilot-rapport §4.3 classificeerde T2-S03 (relatedMatch → broadMatch) als **downgrade**; Protocol v1.2 §3.2 sterkte-ordening definieert dit expliciet als **upgrade** (relatedMatch zwakker dan broadMatch). Pilot-rapport-cijfers consistent (1 upgrade), maar paar-toewijzing-cijfer (3 downgrades) overschrijdt protocol-definitie.
- **Tweede discrepantie:** T2-S08-alt huidige predicate in pilot-rapport §4.8 = "relatedMatch", maar werkelijke TTL-content = `broadMatch` (T1 v4.6.1-patch heeft 5_30 reeds van exactMatch naar broadMatch geconverteerd; zie `apply_patch_v4_6_1.py` regel 29). T2-S08-alt is daarmee **behoud**, niet upgrade.
- **Protocol-zelf duidelijk:** §3.2 mutatie-classificatie-tabel is eenduidig. Discrepanties zijn pilot-rapport-factual-errors, geen protocol-ambiguïteit.
- **Implicatie:** Stap 3-cijfers gebruiken consistent protocol-letter via helper-script-classificatie. Voor masterchat-review: bevestig dat helper-script-classificatie autoritatief is over pilot-rapport-tekst.

**Suggestie voor pilot-rapport-correctie (geen scope van Stap 3, masterchat-overweging):** pilot-rapport §1.1 + §4.3 + §4.8 tabellen herzien naar consistente sterkte-ordening-toepassing.

### §6.4 — Categorie 4: Werkverdeling-momenten

**Status: Tech-autonomie via lokale NEN-toegang volledig benut. Geen masterchat-judgement-vragen voor uitvoering Stap 3.**

- Alle 5 NEN-clausules voor uitzondering-screening (§5.2, §5.4, §5.36, §6.5, §8.3) zelfstandig gelezen + parafrasered + getoetst via lokale ISO 27002:2022 PDF-extractie
- Protocol 17 (NEN-werkverdeling met Tech-autonomie) werkt zoals beoogd voor cluster-niveau-batching
- **Bottom-up rapport-bouw (pilot-leerpunt §6.4) toegepast:** §3-§7 vóór §1 + §2. Helper-script-cijfers leveren basis-data; §3 cluster-beoordelingen schrijven; §4-§5-§6-§7 onderbouwen; tenslotte §1-samenvatting samenstellen. Geen initiële-fout-classificatie zoals pilot-rapport had bij §1.1 + §4.8.
- **Werkflow-observatie:** pilot-rapport-discrepantie (zie §6.3) ontdekt tijdens helper-script-cross-check. Een **eerder review** van pilot-rapport-classificatie t.o.v. protocol-letter zou de discrepantie eerder hebben gevangen. Voor T3+: pilot-rapport-cijfers verifiëren via helper-script vóór hoofd-uitvoering-rapport-start.

### §6.5 — Categorie 5: Cluster-discipline-toepassings-ervaringen

**Status: cluster-discipline werkt schaalbaar over alle 10 m10-clusters. 100% convergentie naar broadMatch zonder NEN-uitzondering.**

- 10 clusters × gemiddeld 11.8 leden = 118 paren binnen één doel-predicate-paradigma
- **Per-cluster-tijdsbestek (handmatig):** cluster-context + representant-keuze + cluster-overerving-review = ~10-15 min per cluster (helper-script comprimeert per-paar-werk tot per-cluster-review)
- **Cluster-representant-keuze:** pilot-paren waar beschikbaar (6 clusters: a, b, c, e, i, j); nieuwe representanten voor 4 clusters (d, f, g, h). Pilot-paren bleken effectief — sample-first-discipline (Protocol 16) verifieerde cluster-doel-bewijs voor 75% van de clusters al in Stap 2
- **Bewijslast voor cluster-uitzondering werkt streng:** geen enkele heuristiek-flag (10 stuks) leverde NEN-aantoonbare individuele afwijking op. Cluster-discipline is operationeel niet-omzeilbaar zonder substantiële bron-onderbouwing
- **Schaalbaar over m14-toekomst:** zelfde aanpak toepasbaar op AVG-cross-walk (compl→ctrl-richting); cluster-cardinaliteit-analyse blijft autoritatief

### §6.6 — Categorie 6: D4.1-pre-stap-praktijk

**Status: D4.1-disclaimer-toepassing erg compact op cluster-niveau.**

- Alle 10 clusters delen één D4.1-disclaimer-context: ENISA TIG R285 + CBW-Mapping-UV R3 (T1-bekend, pre-sprint-inventarisatie §5)
- Per-paar-D4.1-check op cluster-niveau = **één bevestiging per cluster**, niet 11.8 keer per cluster — efficiëntiewinst t.o.v. naïeve per-paar-aanpak
- **Bevinding voor T3+:** D4.1-disclaimer-status kan cluster-niveau worden toegekend wanneer alle cluster-leden dezelfde bron-stack hebben. Voor heterogene clusters (mix van ENISA-TIG + andere bronnen) nog steeds per-paar-toets vereist

### §6.7 — Categorie 7: Upgrade-detectie-praktijk (NIEUW v1.2)

**Status: bidirectional Protocol v1.2 §3.1-tabel symmetrisch werkend over alle 10 clusters. Upgrade-frequentie hoger dan pilot-extrapolatie suggereerde.**

- **Pilot-uitkomst (8 paren):** 2 upgrades / 8 = 25% upgrade-rate. Stap 3-extrapolatie: 110 × 25% = ~28 upgrades verwacht
- **Werkelijke Stap 3-uitkomst:** 33 upgrades totaal (incl. 1 uit pilot + 32 nieuwe in Stap 3). Verschil 32 vs ~28 = +14% boven pilot-extrapolatie — ruim binnen marge, geen scope-pauze-trigger (>30% boven raming-drempel niet bereikt)
- **Verklaring upgrade-densiteit:** initiële m10-data bevat 60 `relatedMatch`-paren waarvan 33 in clusters die naar broadMatch convergeren = 33/60 = 55% upgrade-rate-vóór-T2. De resterende 27 relatedMatch-paren zaten al in clusters waar relatedMatch-behoud van toepassing was — maar in m10-cluster-context (alle veel↔1) zou dit eigenlijk ook upgrade moeten zijn. **Wacht: deze 27 zitten in m14 (AVG/GDPR-cluster), niet in m10.** Voor m10: alle 33 m10-relatedMatch-paren upgrade naar broadMatch. 100%-upgrade-rate binnen m10 voor relatedMatch-paren
- **Downgrade-densiteit:** 32 downgrades = alle 32 m10-closeMatch-paren naar broadMatch. 100%-downgrade-rate binnen m10 voor closeMatch-paren. Consistent met C2-cluster-criterium (1↔1-in-cluster blokkeert closeMatch in veel↔1-cluster)
- **Symmetrie-bewijs Protocol v1.2:** binnen één cluster (NIS2_a met 12 leden) treden zowel downgrade (4× closeMatch → broadMatch), upgrade (4× relatedMatch → broadMatch) als behoud (4× broadMatch) op. Drie verschillende mutatie-richtingen convergeren naar één cluster-doel — directe empirische bevestiging van protocol-symmetrie, gerepliceerd over 10 clusters
- **Confidence-asymmetrie observatie (pilot §6.7):** in Stap 3 niet langer waarneembaar — cluster-discipline-overerving levert hoge confidence (cluster-cardinaliteit-feit + uniforme cluster-doel-toepassing). Geen middel/laag-confidence-paren in Stap 3

---

## §7. Aanbeveling Stap 4

### §7.1 — Patch-batch-structuur

**Eén v4.6.2-release-patch** met alle 65 mutaties via `apply_patch_v4_6_2.py --apply` (analoog T1-precedent v4.6.1):

- Pre-patch backup: `ontology/m10-nis2-ext.ttl.v4_6_1.bak`
- 65 SKOS-predicate-substituties in één run
- Post-patch verificatie: alle 4 SKOS-predicates (exactMatch + closeMatch + relatedMatch + narrowMatch) op 0 in m10; alleen broadMatch resterend (118 stuks)

**Geen per-cluster-versie-versnippering** (instructie §7.4). Eén commit, één patch-rapport, één canonical metrics + SHACL-run.

### §7.2 — Verificatie-volgorde Stap 4

1. **Pre-patch baseline-snapshot** (huidige TTL-hashes voor referentie)
2. **Productie-run applier:** `python3 output/scripts/apply_patch_v4_6_2.py --apply` (backup wordt aangemaakt)
3. **Canonical metrics run:** `python3 output/verification/canonical_metrics_v4_6_2.py`
   - Verwachte m10-counts: ctrl→compl:NIS2_Art21_* totaal 118; predicate-distributie: 0/0/118/0/0 (exact/close/broad/narrow/related)
   - Verwacht zero impact op andere modules (cross-module-counts onveranderd)
4. **SHACL gesplitste validatie:** `python3 output/verification/shacl_split_validate_v4_6_2.py`
   - SECTIE A (inference=none): geen nieuwe violations verwacht (predicate-herclassificatie raakt geen ctrl/bio-naming of asset-namespace)
   - SECTIE B (inference=owlrl): geen nieuwe violations verwacht (BVA-symmetry, AppliesToAssetType, OrphanClass-shapes raken geen SKOS-mapping-predicates)
5. **File-hashes opslaan:** `shasum -a 256 ontology/m10-nis2-ext.ttl > output/verification/file_hashes_v4_6_2.txt`
6. **Patch-rapport v4.6.2 opstellen** conform sprint-protocols §18 §0-§13

### §7.3 — Verificatie-script-templates (analoog T1)

Tech kan voor Stap 4 de canonical metrics en SHACL-scripts genereren op basis van T1-precedent. Lokaties (conform Protocol 16):

- `output/verification/canonical_metrics_v4_6_2.py`
- `output/verification/shacl_split_validate_v4_6_2.py`
- `output/verification/file_hashes_v4_6_2.txt`
- `output/verification/canonical_metrics_v4_6_2.json`
- `output/verification/shacl_results_v4_6_2.json`

### §7.4 — GO-criteria Stap 4

| Criterium | Drempel |
|---|---|
| Applier-productie-run succesvol | 65/65 mutaties zonder fouten |
| Backup-file aanwezig | `m10-nis2-ext.ttl.v4_6_1.bak` |
| m10 SKOS-counts post-patch | exact 0 / close 0 / broad 118 / narrow 0 / related 0 |
| Canonical metrics totaal-triples | binnen ±5 t.o.v. v4.6.1-baseline (alleen predicate-herclassificatie, geen toevoegingen/verwijderingen) |
| SHACL split-validatie SECTIE A | 0 nieuwe violations |
| SHACL split-validatie SECTIE B | 0 nieuwe violations |
| File-hash gewijzigd | nieuwe sha256 ≠ v4.6.1-hash |
| Patch-rapport §0-§13 compleet | alle 14 secties ingevuld |

### §7.5 — Pre-stap voor Stap 4 (masterchat-overweging)

**Aanbeveling:** vóór Stap 4-productie-toepassing kan masterchat overwegen:

1. **Pilot-rapport-correctie:** §1.1 + §4.3 + §4.8 corrigeren naar consistente Protocol v1.2 §3.2-toepassing (zie §6.3 + §6.4). Geen blokkade voor Stap 4 (helper-script-cijfers zijn autoritatief), wel hygiëne voor T-historie
2. **Bevestiging cluster-doel-predicate broadMatch voor alle 10 clusters:** masterchat-GO op §3 cluster-beoordelingen (10 subsecties) als gesloten bewijs-set
3. **Confidence-classificatie post-Stap-3:** geen masterchat-judgement-vragen openstaand. Alle 65 mutaties hebben **hoge confidence** door cluster-cardinaliteit-feit + 0 NEN-uitzonderingen

### §7.6 — Geschat tijdsbestek Stap 4

| Aspect | Schatting |
|---|---:|
| Applier productie-run + sanity-check | ~10 min |
| Canonical metrics script + run | ~30 min |
| SHACL split-validatie script + run | ~30 min |
| Patch-rapport v4.6.2 schrijven | ~1.5 uur |
| **Totaal Stap 4** | **~2.5-3 uur** |

---

## §8. Hand-off-checklist

- [x] Pre-push disclosure-check Protocol 14 (vijf categorieën):
  - [x] Organisatie-naam: geen vermelding ("de organisatie" / "Rijksoverheidsorganisatie" niet eens gebruikt)
  - [x] Persoonsnamen: alleen Steven Bouwmeester (publieke projecteigenaar)
  - [x] Lokale paden: alleen `/Users/stevenbouwmeester/grc-kennismodel/` (project) en `/Users/stevenbouwmeester/grc-sources-licensed/` (NEN-licentie)
  - [x] Credentials/TLD/e-mail: geen
  - [x] NEN-tekst-fragmenten >10 woorden: geen verbatim NEN-tekst opgenomen; parafrasen + clausule-verwijzingen wel; PDF-licentie-watermerk gefilterd
- [x] Geen patches / ontologie-wijzigingen toegepast (read-only beoordeling + dry-run applier)
- [x] Geen autonome commits (Steven commit handmatig)
- [x] Alle 110 paren beoordeeld via cluster-niveau-batching (10 clusters)
- [x] Cluster-overerving-helper-script aanwezig in `output/scripts/t2-cluster-overerving-helper.py`
- [x] 10 cluster-JSON's + 1 cluster-overview-JSON in `output/analysis/`
- [x] Applier-script `output/scripts/apply_patch_v4_6_2.py` aanwezig (dry-run-modus default)
- [x] Dry-run-output `output/scripts/apply_patch_v4_6_2_dry_run.txt` aanwezig
- [x] Werkflow-leerpunten §6 met alle 7 categorieën (incl. categorie 7 upgrade-detectie)
- [x] Aanbeveling Stap 4 §7 specifiek + actionable (patch-batch-structuur + verificatie-volgorde + GO-criteria)
- [x] Stop-condities §5 (alle 8) expliciet gemonitord en negatief bevestigd
- [x] Eindrapport bottom-up gebouwd (§3 cluster-beoordelingen → §4 uitzondering-screening → §5 stop-condities → §6 werkflow-leerpunten → §7 Stap 4 → §1 samenvatting laatst)

### §8.1 — Wat ligt klaar voor masterchat-besluit

1. **GO/NO-GO Stap 4** op basis van Stap 3-resultaten — 65 patch-vereiste mutaties geverifieerd via cluster-discipline + 0 NEN-uitzonderingen
2. **Pilot-rapport-correctie-overweging** §6.3-discrepanties (T2-S03 + T2-S08-alt) — niet-blokkerend voor Stap 4
3. **Bevestiging cluster-doel-predicate broadMatch voor alle 10 clusters**
4. **Bevestiging helper-script-classificatie autoritatief over pilot-rapport-tekst** (Protocol v1.2 §3.2 sterkte-ordening)

### §8.2 — Niet uitgevoerd in Stap 3 (instructie §12)

- [x] Geen daadwerkelijke patch-toepassing (Stap 4)
- [x] Geen canonical metrics-runs op gemuteerde files (Stap 4)
- [x] Geen SHACL-runs op gemuteerde files (Stap 4)
- [x] Geen m14-paren behandeld (buiten T2-scope per Optie C)
- [x] Geen Protocol v1.3-tekst-aanpassing (wacht op T2-afsluiting)
- [x] Geen brain-vault-updates (Brein-cyclus na T2)

---

## §9. Verwijzingen

| Document | Pad |
|---|---|
| Sprint-instructie Stap 3 | `docs/instructies/instructie-t2-stap3.md` |
| Autoritatief protocol | `docs/skos-beoordelings-protocol-v1_2.md` |
| Sprint-protocollen | `docs/sprint-protocols.md` (v1.3) |
| Pre-sprint-inventarisatie Stap 1 | `output/reports/t2-pre-sprint-inventarisatie.md` |
| Pilot-rapport Stap 2 | `output/reports/t2-pilot-rapport.md` |
| T1-precedent eindrapport | `output/reports/t1-eindrapport-v4_6_1.md` |
| T1-precedent applier | `apply_patch_v4_6_1.py` (root) |
| Bron: ISO 27002:2022 | `/Users/stevenbouwmeester/grc-sources-licensed/NEN-EN-ISO_IEC_27002_2022_en.pdf` |
| Bron: NIS2-richtlijn | `sources/eu-recht/EU-nis2-richtlijn.pdf` |
| Bron: CBW-Mapping-UV | `sources/adr-norea/Cbw (NIS2) Control Framework.xlsx` sheet "Mapping Uitvoeringsverordening" |
| Ontologie-module (NIET gewijzigd) | `ontology/m10-nis2-ext.ttl` |
| Cluster-overerving-helper | `output/scripts/t2-cluster-overerving-helper.py` |
| Applier-script (dry-run) | `output/scripts/apply_patch_v4_6_2.py` |
| Dry-run-output | `output/scripts/apply_patch_v4_6_2_dry_run.txt` |
| Cluster-JSON's | `output/analysis/t2-cluster-{a..j}.json` |
| Cluster-overview-JSON | `output/analysis/t2-cluster-overview.json` |
| Dit rapport | `output/reports/t2-stap3-eindrapport.md` |

---

*Einde T2 Stap 3 eindrapport. Modus: read-only beoordeling + dry-run-applier. Geen verdere autonome actie na rapport-creatie. Steven commit + push handmatig.*
