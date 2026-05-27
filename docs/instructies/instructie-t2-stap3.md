# T2 Stap 3 — hoofd-uitvoering instructie voor Tech-subagent

**Sprint:** T2 (SKOS-kwaliteitsanalyse Fase 2 — bidirectional audit ctrl:↔compl:)
**Fase:** Stap 3 — hoofd-uitvoering (110 m10-paren resterend)
**Auteur:** Masterchat
**Datum:** 27 mei 2026
**Modus:** **READ-ONLY beoordeling** + applier-script-voorbereiding (dry-run). Geen TTL-mutaties.
**Autoritatief protocol:** `docs/skos-beoordelings-protocol-v1_2.md`
**Voorgangers:** `output/reports/t2-pre-sprint-inventarisatie.md` (Stap 1) + `output/reports/t2-pilot-rapport.md` (Stap 2)

---

## §0. Context — Stap 2 pilot-uitkomsten + masterchat-besluit Stap 3

**Pilot-uitkomst (8 paren):** 3 behoud + 3 downgrade + 2 upgrade + 0 richtings-correctie + 0 verwijderen + 0 twijfel = 5 patch-vereiste mutaties. Alle mutaties convergeren naar `broadMatch` (cluster-doel-predicate).

**Cluster-discipline §3.3 valide gewerkt:** compl:NIS2_Art21_a-cluster (3 pilot-paren) toont drie verschillende mutatie-richtingen die convergeren naar één cluster-doel-predicate. Eerste empirische bevestiging dat Protocol v1.2 symmetrisch werkt — bidirectional uitbreiding is operationeel toepasbaar.

**Categorie 7 upgrade-detectie:** 2 upgrades gevonden (T2-S05, T2-S08-alt: `relatedMatch` → `broadMatch`). Geen upgrades naar `closeMatch`/`exactMatch` — consistent met 0-singleton-feit.

**Masterchat-besluit:**

1. **GO voor Stap 3** met Tech's voorgestelde cluster-niveau-aanpak (§7.1 pilot-rapport)
2. **Protocol v1.2 blijft autoritatief** — vijf v1.3-voorstellen §7.3 pilot-rapport zijn niet-blokkerend voor Stap 3 en worden na T2-afsluiting verwerkt
3. **Cluster-overerving-helper-script** wordt integraal Stap 3-deliverable (geen verborgen pre-stap)
4. **T2-S08-alt confidence "middel" bevestigd** als correct gelabeld — cluster-doel `broadMatch` over individueel-`closeMatch`-alternatief

---

## §1. Doel Stap 3

Beoordelen van de **110 resterende m10-paren** (118 totaal − 8 pilot) onder Protocol v1.2 met cluster-niveau-batching. Output:

1. Per cluster: cluster-doel-predicate + cluster-discipline-conformiteits-check per cluster-lid
2. Uitzondering-screening per cluster (NEN-aantoonbare individuele afwijking van cluster-doel)
3. Werkbare cluster-overerving-helper-script (deliverable + dry-run-output)
4. Werkbare applier-script in dry-run-modus (Protocol v1.2 §9; productie-uitvoering pas in Stap 4)
5. Werkflow-leerpunten alle 7 categorieën Protocol v1.2 §10
6. Aanbevelingen voor Stap 4 patch-toepassing (patch-batch-structuur, verificatie-volgorde)

**Doel is niet:**

- Daadwerkelijke patch-toepassing — Stap 4 na masterchat-review
- Canonical metrics / SHACL-runs op gemuteerde files — Stap 4
- v4.6.2-release-voorbereiding — Stap 4

**Modus:** read-only beoordeling. Geen wijzigingen aan `m10-nis2-ext.ttl`, geen test-applies in productie. Dry-run-applier-uitvoer wel toegestaan en gewenst (toont verwachte mutatie-impact zonder file-mutatie).

---

## §2. Scope

### §2.1 — Resterende paren per cluster

Cluster-overzicht (uit pre-sprint-inventarisatie §3.1, exclusief 8 pilot-paren):

| Cluster (object-anchor) | Cluster-grootte totaal | Pilot-paren | Resterend Stap 3 |
|---|---:|---:|---:|
| compl:NIS2_Art21_a (Risicoanalyse + IB-beleid) | 12 | 3 (T2-S03/S04/S05) | 9 |
| compl:NIS2_Art21_b (Incidentbehandeling) | 10 | 1 (T2-S02) | 9 |
| compl:NIS2_Art21_c (Bedrijfscontinuïteit + back-up + DR) | 8 | 1 (T2-S08-alt) | 7 |
| compl:NIS2_Art21_d (Toeleveringsketen-beveiliging) | 7 | 0 | 7 |
| compl:NIS2_Art21_e (Verwerving/ontwikkeling/onderhoud) | 17 | 1 (T2-S06-alt) | 16 |
| compl:NIS2_Art21_f (Beoordeling effectiviteit) | 7 | 0 | 7 |
| compl:NIS2_Art21_g (Basale cyberhygiëne + training) | 9 | 0 | 9 |
| compl:NIS2_Art21_h (Cryptografie) | 7 | 0 | 7 |
| compl:NIS2_Art21_i (HR-security + access + asset mgmt) | 32 | 1 (T2-S01) | 31 |
| compl:NIS2_Art21_j (MFA + continuous auth + comms) | 9 | 1 (T2-S07-alt) | 8 |
| **Totaal m10** | **118** | **8** | **110** |

### §2.2 — Cluster-doel-predicate per cluster

Alle 10 clusters zijn veel↔1 (object-cluster met meerdere ISO-controls naar één NIS2-letter). Per Protocol v1.2 §3.1 rij 6: cluster-doel-predicate = `broadMatch` voor alle 10 clusters.

**Dit is geen pre-uitkomst-voorspelling van Stap 3** (Protocol v1.2 §6 verbiedt expliciet). Het is een **structureel feit** uit C2-cardinaliteit-analyse (Protocol v1.2 §2.2): cluster-doel volgt deterministisch uit cluster-grootte > 1 + veel↔1-relatie.

Individuele cluster-leden kunnen NEN-aantoonbare uitzondering rechtvaardigen — zie §6.

---

## §3. Aanpak per cluster (cluster-niveau-batching)

Voor elk van de 10 clusters, in volgorde van toenemende cluster-grootte (kleinste eerst om vroege werkflow-validatie te krijgen):

| # | Cluster | Resterend |
|---|---|---:|
| 1 | NIS2_Art21_d | 7 |
| 2 | NIS2_Art21_f | 7 |
| 3 | NIS2_Art21_h | 7 |
| 4 | NIS2_Art21_c | 7 |
| 5 | NIS2_Art21_g | 9 |
| 6 | NIS2_Art21_b | 9 |
| 7 | NIS2_Art21_a | 9 |
| 8 | NIS2_Art21_j | 8 |
| 9 | NIS2_Art21_e | 16 |
| 10 | NIS2_Art21_i | 31 |

### §3.1 — Stappen per cluster

Voor elk cluster:

1. **Cluster-representant-selectie** (§5-criteria): kies één cluster-lid als representant
2. **Cluster-representant-beoordeling** via Protocol v1.2 §2-3 (alle 13 velden Protocol v1.2 §5 ingevuld)
3. **Cluster-doel-predicate-bepaling**: bevestig dat doel = `broadMatch` (verwacht conform §2.2) of motiveer afwijking
4. **Cluster-overerving voor overige cluster-leden**: helper-script-output reviewen + per-lid bevestigen
5. **Uitzondering-screening** per cluster-lid (§6): flag kandidaten + NEN-onderbouwing-toets
6. **Stop-conditie-monitoring** per cluster + cumulatief over Stap 3

### §3.2 — Cluster-representant zonder volledige nieuwe beoordeling

Voor clusters die pilot-paren bevatten (NIS2_Art21_a, b, c, e, i, j): pilot-paren leveren reeds cluster-doel-bewijs. Tech kan kiezen uit:

- (A) Pilot-paar als cluster-representant gebruiken (effort-besparing); of
- (B) Nieuwe cluster-representant kiezen ter cross-validatie

Tech-keuze documenteren per cluster.

### §3.3 — Cluster-overerving-discipline

Cluster-doel-predicate is `broadMatch` voor alle 10 clusters (verwacht). Per cluster-lid:

- Huidige predicate = `broadMatch` → behoud (geen patch)
- Huidige predicate ≠ `broadMatch` → patch-vereist, mutatie-richting via Protocol v1.2 §3.2:
  - `closeMatch` → `broadMatch`: **downgrade**
  - `relatedMatch` → `broadMatch`: **upgrade**
  - `narrowMatch` → `broadMatch`: niet aangetroffen in cluster-mix (m10 heeft 0 narrowMatch)

Uitzondering: indien NEN-aantoonbare individuele afwijking → cluster-uitzondering (§6).

---

## §4. Cluster-overerving-helper-script (verplichte deliverable)

### §4.1 — Doel

Geautomatiseerd genereren van cluster-beoordelings-tabel per cluster met:

- Alle cluster-leden (ctrl-IRI's per object-anchor)
- Huidige predicate per cluster-lid
- Cluster-doel-predicate (vast op `broadMatch` voor veel↔1-clusters)
- Mutatie-richting per cluster-lid (behoud / downgrade / upgrade)
- Uitzondering-screening-flag (heuristisch — Tech reviewt) op basis van bv. subject-cluster-grootte, evidence-niveau-bron-aanwezigheid

### §4.2 — Script-locatie + naam

`output/scripts/t2-cluster-overerving-helper.py`

### §4.3 — Output-format

Per cluster JSON-bestand: `output/analysis/t2-cluster-{letter}.json`

```json
{
  "cluster_id": "compl:NIS2_Art21_a",
  "cluster_size": 12,
  "cluster_target_predicate": "skos:broadMatch",
  "rationale": "veel↔1 object-cluster, Protocol v1.2 §3.1 rij 6",
  "members": [
    {
      "subject": "ctrl:ISO27002_5_01",
      "current_predicate": "skos:broadMatch",
      "mutation_direction": "behoud",
      "patch_required": false,
      "exception_screening_flag": false,
      "exception_screening_rationale": null,
      "is_pilot_pair": false,
      "subject_cluster_size": 1
    },
    {
      "subject": "ctrl:ISO27002_5_02",
      "current_predicate": "skos:closeMatch",
      "mutation_direction": "downgrade",
      "patch_required": true,
      "exception_screening_flag": true,
      "exception_screening_rationale": "5.2 Roles + Responsibilities is breed-policy-control; mogelijk legitiem closeMatch-kandidaat indien NEN-content sterk overlap met NIS2(a)",
      "is_pilot_pair": false,
      "subject_cluster_size": 2
    }
    // ... overige cluster-leden
  ]
}
```

### §4.4 — Heuristieken voor `exception_screening_flag`

Auto-flag-cluster-lid voor handmatige uitzondering-review als één of meer geldt:

- Subject-rdfs:label bevat termen als "policy", "framework", "management responsibilities", "governance", "roles" — suggereert breed-policy-control die mogelijk legitiem closeMatch-kandidaat is
- Subject in subject-cluster ≥3 (multi-mapping naar meerdere NIS2-letters) — suggereert brede toepasbaarheid
- Evidence-niveau 4 of ontbrekend — vereist extra NEN-toets
- Subject-IRI verwijst naar ISO 27002 §X-clausules die in NEN-tekst expliciet bidirectionele scope-claim maken (handmatig te detecteren)

Flag is heuristiek + niet-bindend. Tech reviewt alle flags individueel; sommige worden cluster-conform bevestigd, andere uitzondering.

### §4.5 — Dry-run-output

Bij script-uitvoering: alleen lezen + JSON-genereren. **Geen TTL-mutatie**. Script faalt safe als TTL-mutatie-flag wordt geprobeerd zonder expliciete activatie.

Resultaten:
- 10 JSON-bestanden in `output/analysis/`
- Cumulatieve tabel in `output/analysis/t2-cluster-overview.json` met totalen + uitzondering-flag-counts

---

## §5. Cluster-representant-criteria (uit v1.3-voorstel 4)

**Bij selectie van cluster-representant voor diepe Protocol v1.2-beoordeling:**

Geef voorkeur aan cluster-leden die:

1. **Niet subject-singleton** zijn met enkel deze cluster-mapping (geeft cluster-context, geen geïsoleerde paar)
2. **Niet in grote subject-cluster** (>3) zitten (voorkomt confounding factors van multiple-mapping-effecten)
3. **Hoogste evidence-niveau** hebben (niveau 1 via CBW-Mapping-UV is sterkste basis)
4. **Middelmatig in cluster-mix** zijn (niet extremen — bv. niet de enige `closeMatch` in cluster of de enige `relatedMatch`)

Bij conflict tussen criteria: prevaleren in volgorde 1 → 4. Documenteer cluster-representant-keuze per cluster met motivatie.

### §5.1 — Voorbeeld-criteria-toepassing op compl:NIS2_Art21_a

Pilot koos T2-S03 (`ctrl:ISO27002_5_03`) als representant:

- Subject in subject-cluster 3 (criterium 2 licht geschonden — acceptabel want middel-cluster, niet groot)
- Evidence-niveau 2-3 (criterium 3 acceptabel)
- relatedMatch in cluster met mixed predicates (criterium 4 middelmatig)

Geldige keuze, demonstreert dat pragmatische cluster-representant-keuze werkbaar is bij minor-conflict tussen criteria.

---

## §6. Uitzondering-screening per cluster

Per Protocol v1.2 §3.3: cluster-discipline prevaleert tenzij **NEN-aantoonbare** individuele uitzondering.

### §6.1 — Werkwijze

Per cluster-lid dat door helper-script als uitzondering-kandidaat is geflagd (§4.4):

1. **NEN-tekst-onderbouwing zoeken**: lees ISO 27002:2022 §X-clausule (NEN-content + clausule-structuur + "Other information"-verwijzingen) via `/Users/stevenbouwmeester/grc-sources-licensed/`
2. **Argument-onderbouwing**: cluster-uitzondering vereist expliciete onderbouwing waarom dit cluster-lid **niet** binnen de bredere cluster-doel-categorie past
3. **Twee-zijdige analyse** (Protocol v1.2 §4): pro-cluster-default vs pro-uitzondering
4. **Beslissing**: indien onderbouwing zwak → cluster-default toepassen; indien sterk → uitzondering vastleggen
5. **Twijfel-escalatie**: indien geen sluitend oordeel → masterchat-judgement-vraag conform Protocol v1.2 §4 format

### §6.2 — Precedent: compl:NIS2_Art21_a (uit pilot §3 + §7.1)

In NIS2_a-cluster zijn pilot-aangewezen uitzondering-screening-kandidaten:

- **ISO27002_5_02 (Roles + Responsibilities)**: breed-policy-control. Mogelijk legitiem closeMatch-kandidaat als NEN-content sterk overlapt met NIS2(a)-policy-norm op bredere scope. NEN-toets vereist.
- **ISO27002_5_04 (Management responsibilities)**: breed-policy-control. Vergelijkbaar kandidaat.

Pilot heeft beide niet beoordeeld (waren niet in pilot-sample). Stap 3 moet uitsluitsel geven.

### §6.3 — Verwachte uitzondering-frequentie

Bij realistische schatting: per cluster 0-2 NEN-aantoonbare uitzonderingen. Over 10 clusters: 0-20 uitzonderingen verwacht.

Stop-conditie indien >5 uitzonderingen per cluster → cluster-discipline-failure-signal, masterchat-escalatie.

### §6.4 — NEN-discipline (Protocol v1.2 §8)

Uitzondering-onderbouwing in eindrapport: parafrase + clausule-verwijzing. **Geen verbatim NEN-tekst >10 woorden.** Pre-push disclosure-check Protocol 14 cat.5 verplicht vóór hand-off.

---

## §7. Applier-script-voorbereiding (Protocol v1.2 §9)

### §7.1 — Doel

Werkbaar applier-script dat in Stap 4 de gehele T2-mutatie-set in één commit toepast:

- **Pilot-mutaties (5)**: T2-S02, T2-S03, T2-S05, T2-S07-alt, T2-S08-alt
- **Stap 3-mutaties (geschat 60-75)**: uit cluster-doel-toepassing + uitzonderingen

Totaal verwacht: ~65-80 SKOS-predicate-mutaties in één v4.6.2-release-patch.

### §7.2 — Script-format

`output/scripts/apply_patch_v4_6_2.py` analoog T1-precedent `apply_patch_v4_6_1.py`:

- Backup van `m10-nis2-ext.ttl` vóór mutatie
- Count-verificatie (pre + post mutatie-aantallen)
- Faal-veilig-exit bij hash-mismatch of count-mismatch
- Dry-run-modus (default in Stap 3) + productie-modus (Stap 4)

### §7.3 — Dry-run-uitvoering in Stap 3

Tech voert applier in dry-run-modus uit:

- Toont verwachte mutaties zonder file-mutatie
- Output naar `output/scripts/apply_patch_v4_6_2_dry_run.txt`
- Verifieert dat alle ~65-80 mutaties correct ge-identificeerd worden in TTL-graph

Dry-run is integraal onderdeel van Stap 3-deliverables; Stap 4 voert script in productie-modus uit na masterchat-review.

### §7.4 — Patch-batch-structuur

Eén v4.6.2-release-patch met alle mutaties (zoals T1-precedent v4.6.1). Geen per-cluster-versie-versnippering.

---

## §8. Stop-condities (Protocol v1.2 §6 — schaal-aangepast voor Stap 3)

### §8.1 — Drempels

Schaal-aangepast van pilot (≥3/8) naar Stap 3 (~110 paren):

| # | Conditie | Drempel Stap 3 |
|---|---|---|
| 1 | Confidence "laag" op cluster-leden | ≥5 paren totaal over Stap 3 |
| 2 | Evidence-niveau 4 op cluster-leden | ≥5 paren totaal |
| 3 | D4.1-disclaimer-status "niet-onderzocht" | ≥5 paren totaal |
| 4 | Onverwacht-patroon t.o.v. cluster-doel-verwachting (kwalitatief) | bv. cluster-doel ≠ broadMatch voor één cluster zonder duidelijke NEN-onderbouwing |

### §8.2 — Cluster-specifieke stop-condities

| # | Sub-conditie | Drempel |
|---|---|---|
| 5 | Verwijder-doelen totaal Stap 3 | ≥3 |
| 6 | Twijfel-escalaties per cluster | ≥3 per cluster, of ≥5 totaal |
| 7 | NEN-aantoonbare uitzonderingen per cluster | ≥5 per cluster |
| 8 | Cluster-discipline-failure (drie verschillende doel-predicates binnen één cluster zonder NEN-onderbouwing) | ≥2 clusters |

### §8.3 — Bij stop-conditie-trigger

Stop direct, schrijf scope-pauze-rapport conform Protocol v1.2 §4 twee-zijdige analyse-format. Geen aparte scope-pauze-md vereist — incorporeer in lopende Stap 3-eindrapport-draft als §X "Scope-pauze-uitkomst". Wacht op masterchat-besluit voor verdere actie.

---

## §9. Werkflow-discipline tijdens Stap 3

### §9.1 — Bottom-up rapport-bouw (uit pilot-leerpunt §6.4)

Eindrapport-secties bouwen in volgorde:

1. Eerst §3 cluster-beoordelingen (10 secties, één per cluster — paar-niveau-detail)
2. Dan §4 uitzondering-screening-resultaten
3. Dan §5 stop-conditie-monitoring
4. Dan §6 werkflow-leerpunten alle 7 categorieën
5. Dan §7 aanbeveling Stap 4
6. **Laatst** §1 samenvatting (kerncijfers + uitkomst-distributie) — afgeleid uit §3-§7

Indien §1 vroeg-invullen: expliciet markeren "INITIEEL, TE BEVESTIGEN IN §3-§7-ITERATIE" en in finale versie corrigeren.

### §9.2 — Werkflow-leerpunten markeren tijdens uitvoering (Protocol v1.2 §10)

Markeer voortdurend, niet alleen achteraf. Zeven categorieën:

1. Tooling-gaten — werkte cluster-overerving-helper-script efficient? Applier-script?
2. Bron-toegankelijkheid — welke NEN-clausules of CBW-Mapping-UV-rijen waren niet vindbaar?
3. Protocol-criteria-onduidelijkheden — welke C-criterium-formulering bleek ambigu op cluster-niveau?
4. Werkverdeling-momenten — waar Tech-autonomie volstond / waar masterchat-escalatie nodig was
5. Cluster-discipline-toepassings-ervaringen — werkte cluster-overerving consistent over alle 10 clusters?
6. D4.1-pre-stap-praktijk — was T1-bekend-status voldoende voor alle 110 paren?
7. **Upgrade-detectie-praktijk** — schaalde Protocol v1.2 §3.1-tabel symmetrisch over alle clusters? Frequentie upgrade vs downgrade ratio?

---

## §10. Output-formaat eindrapport

**Bestandsnaam:** `output/reports/t2-stap3-eindrapport.md`

**Structuur:**

```
# T2 Stap 3 — eindrapport hoofd-uitvoering 110 m10-paren

## §1. Samenvatting (LAATST INVULLEN — bottom-up)
## §2. Methode (cluster-niveau-batching + helper-script + applier-dry-run)
## §3. Cluster-beoordelingen (10 subsecties, één per cluster)
  ### §3.1 — compl:NIS2_Art21_d (volgorde: kleinste cluster eerst)
  ### §3.2 — compl:NIS2_Art21_f
  ### §3.3 — compl:NIS2_Art21_h
  ### §3.4 — compl:NIS2_Art21_c
  ### §3.5 — compl:NIS2_Art21_g
  ### §3.6 — compl:NIS2_Art21_b
  ### §3.7 — compl:NIS2_Art21_a
  ### §3.8 — compl:NIS2_Art21_j
  ### §3.9 — compl:NIS2_Art21_e
  ### §3.10 — compl:NIS2_Art21_i
## §4. Uitzondering-screening — uitkomsten alle 10 clusters
## §5. Stop-conditie-monitoring (acht condities §8)
## §6. Werkflow-leerpunten (7 categorieën)
## §7. Aanbeveling Stap 4 (patch-batch-structuur + verificatie-volgorde)
## §8. Hand-off-checklist
## §9. Verwijzingen
```

### §10.1 — Per cluster (§3.X) bevat

1. Cluster-context (object-anchor + cluster-grootte + huidige predicate-mix)
2. Cluster-representant-keuze + motivatie (§5-criteria)
3. Cluster-representant-beoordeling (volledige Protocol v1.2 §5-tabel)
4. Cluster-doel-predicate-bevestiging
5. Cluster-overerving-tabel: alle resterende cluster-leden met huidige + doel + mutatie-richting + uitzondering-screening-resultaat
6. NEN-uitzonderingen (indien aanwezig): per-lid onderbouwing
7. Cluster-niveau-cijfers: aantal behoud / downgrade / upgrade / uitzondering

### §10.2 — Per-cluster-cijfertabel (§1 samenvatting cumulatief)

| Cluster | Resterend | Behoud | Downgrade | Upgrade | NEN-uitzondering | Patch-vereist |
|---|---:|---:|---:|---:|---:|---:|
| NIS2_a | 9 | ? | ? | ? | ? | ? |
| ... | ... | ... | ... | ... | ... | ... |
| **Totaal Stap 3** | **110** | **?** | **?** | **?** | **?** | **?** |
| Pilot (referentie) | 8 | 3 | 3 | 2 | 0 | 5 |
| **T2-totaal** | **118** | **?** | **?** | **?** | **?** | **?** |

---

## §11. Hand-off-checklist

- [ ] Pre-push disclosure-check Protocol 14 (vijf categorieën inclusief NEN-tekst >10 woorden)
- [ ] Geen patches / ontologie-wijzigingen toegepast (read-only beoordeling + dry-run)
- [ ] Geen autonome commits (Steven commit handmatig)
- [ ] Alle 110 paren beoordeeld via cluster-niveau-batching
- [ ] Cluster-overerving-helper-script aanwezig in `output/scripts/`
- [ ] 10 cluster-JSON's + cluster-overview-JSON in `output/analysis/`
- [ ] Applier-script `apply_patch_v4_6_2.py` aanwezig (dry-run-modus default)
- [ ] Dry-run-output `apply_patch_v4_6_2_dry_run.txt` aanwezig
- [ ] Werkflow-leerpunten §6 met alle 7 categorieën
- [ ] Aanbeveling Stap 4 §7 specifiek + actionable
- [ ] Stop-condities §5 expliciet gemonitord en gerapporteerd
- [ ] Eindrapport bottom-up gebouwd (§3-§7 vóór §1)

---

## §12. Wat NIET in Stap 3

- Geen daadwerkelijke patch-toepassing — Stap 4 na masterchat-review
- Geen canonical metrics-runs op gemuteerde files — Stap 4
- Geen SHACL-runs (gesplitste sectie A + B) op gemuteerde files — Stap 4
- Geen m14-paren — buiten T2-scope per Optie C
- Geen Protocol v1.3-tekst-aanpassing — wachten op T2-afsluiting
- Geen brain-vault-updates — wachten op Brein-cyclus na T2

---

## §13. Geschatte duur

Pilot-rapport §7.2:

| Aspect | Schatting |
|---|---:|
| Helper-script + dry-run bouwen + valideren | ~1 uur |
| Cluster-niveau-beoordelingen (10 × ~30 min) | ~5 uur |
| Uitzondering-screening + NEN-toets per cluster | ~1 uur |
| Applier-script + dry-run | ~1 uur |
| Eindrapport-schrijven (bottom-up) | ~1.5 uur |
| **Totaal Stap 3** | **~9-10 uur** |

Geen harde deadline. Kwaliteit + correcte protocol-toepassing boven snelheid.

---

## §14. Bij voltooiing

Tech pushed eindrapport + scripts + analysis-JSON's. Steven commit handmatig. Masterchat reviewt:

- Cluster-doel-predicate-bevestiging voor alle 10 clusters
- NEN-uitzonderingen valide onderbouwd?
- Stop-condities geraakt?
- Applier-script dry-run-output consistent met cluster-beoordelings-cijfers?
- Werkflow-leerpunten reden voor Protocol v1.3-revisie of v1.4-aanvulling?
- Aanbeveling Stap 4 patch-batch-structuur acceptabel?

Bij masterchat-GO: **Stap 4** wordt geïnstrueerd voor patch-toepassing in productie-modus + canonical metrics + SHACL + patch-rapport v4.6.2.

---

*Einde T2 Stap 3 instructie. Modus: read-only beoordeling + dry-run-applier. Geen verdere autonome actie na rapport-push.*
