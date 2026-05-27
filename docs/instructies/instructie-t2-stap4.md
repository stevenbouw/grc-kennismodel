# T2 Stap 4 — productie-patch + verificatie + patch-rapport v4.6.2

**Sprint:** T2 (SKOS-kwaliteitsanalyse Fase 2 — bidirectional audit ctrl:↔compl:)
**Fase:** Stap 4 — productie-toepassing
**Auteur:** Masterchat
**Datum:** 27 mei 2026
**Modus:** **PRODUCTIE** — ontologie-mutatie + canonical metrics + SHACL-runs + patch-rapport
**Autoritatief protocol:** `docs/skos-beoordelings-protocol-v1_2.md`
**Voorgangers:**
- `output/reports/t2-pre-sprint-inventarisatie.md` (Stap 1)
- `output/reports/t2-pilot-rapport.md` (Stap 2, inclusief errata-blok)
- `output/reports/t2-stap3-eindrapport.md` (Stap 3, met §1.1 gecorrigeerd)

---

## §0. Context — Stap 3-uitkomst + masterchat-besluit

**Stap 3 voltooid:** alle 110 m10-paren beoordeeld via cluster-niveau-batching over 10 NIS2-letter-clusters. Alle 10 clusters convergeren naar cluster-doel-predicate `skos:broadMatch`. 0 NEN-uitzonderingen na review van 10 heuristiek-flags. 0 stop-condities geraakt.

**Pre-Stap-4 errata uitgevoerd:** pilot-rapport heeft errata-blok bovenaan; Stap 3-rapport §1.1 pilot-referentie-rij + Stap 3 resterend-rij gecorrigeerd naar helper-script-classificatie. T-historie is consistent.

**Masterchat-besluit:**

1. **GO voor Stap 4** met aanpak Tech §7.1-7.4 Stap 3-rapport
2. **65 mutaties in één v4.6.2-release-patch** (5 pilot + 60 Stap 3) via `apply_patch_v4_6_2.py --apply`
3. **Verificatie-volgorde Tech §7.2 bevestigd:** productie-run → canonical metrics → SHACL split-validatie → file-hashes → patch-rapport
4. **Cluster-doel-predicate broadMatch bevestigd voor alle 10 clusters** als gesloten bewijs-set onder Protocol v1.2

---

## §1. Doel Stap 4

Stap 4 is de **enige productie-stap** binnen T2-sprint. Output:

1. Daadwerkelijke TTL-mutatie van `m10-nis2-ext.ttl` met 65 SKOS-predicate-substituties
2. Canonical metrics-script + run + JSON-output (v4.6.2-baseline-bewijs)
3. SHACL split-validatie-script + run + JSON-output (regressie-vrij bewijs)
4. File-hashes opslag (cryptografisch bewijs file-mutatie-scope)
5. Patch-rapport v4.6.2 met §0-§13-structuur (T1-precedent + Protocol 16 + Protocol 14)

**Eindstand T2 na Stap 4:**

| Metric | v4.6.1 (huidig) | v4.6.2 (verwacht) |
|---|---:|---:|
| Pre-inference triples | 20.950 | 20.950 (ongewijzigd) |
| Post OWL RL triples | 44.907 | 44.907 (ongewijzigd) |
| Klassen | 199 | 199 (ongewijzigd) |
| Individuals | 1.383 | 1.383 (ongewijzigd) |
| ObjectProperties | 149 | 149 (ongewijzigd) |
| DatatypeProperties | 96 | 96 (ongewijzigd) |
| `owl:sameAs` | 98 | 98 (ongewijzigd) |
| **SKOS-mappings totaal** | 1.798 | **1.798 (predicate-herclassificatie, geen toevoegingen)** |
| m10 ctrl→compl SKOS-distributie | exact 0 / close 34 / broad 53 (waarvan 32 m10) / narrow 0 / related 60 | **exact 0 / close 0 / broad 118 / narrow 0 / related 27** (alleen m10-paren gemuteerd; m14's 31 paren behouden) |
| SHACL RUN 1 (split SECTIE A) | 0 violations | 0 violations (verwacht) |
| SHACL RUN 2 (gecombineerd) | 290 false-positives | 290 false-positives (identiek; geen regressie) |
| Gewijzigde modules | — | **alleen `m10-nis2-ext.ttl`** (1/22) |

**Mutatie-cijfers herinnering (Stap 3-rapport §1):**

- 32 downgrades: `closeMatch` → `broadMatch`
- 33 upgrades: `relatedMatch` → `broadMatch`
- Totaal: 65 predicate-substituties
- Behoud: 53 paren (al `broadMatch`)
- Verwijderen / richtings-correctie / twijfel: 0

---

## §2. Stap A — Pre-patch baseline-snapshot

Vóór elke wijziging: leg actuele staat vast voor latere referentie + rollback-mogelijkheid.

### §2.1 — Hash-snapshot huidige TTL

```bash
shasum -a 256 ontology/m10-nis2-ext.ttl
```

Vermeld in patch-rapport §3 als pre-patch-hash (verwacht: `cb2d567b184877e111800cc0a8af1e38d6d6f74ddca0477ee1a52df1d8afa2f1` per v4.6.1-baseline).

### §2.2 — Sanity-check m10-counts pre-patch

Quick SPARQL of `grep`-count voor verificatie:

- Aantal `skos:closeMatch` in m10 ctrl→compl: verwacht 32
- Aantal `skos:broadMatch` in m10 ctrl→compl: verwacht 53
- Aantal `skos:relatedMatch` in m10 ctrl→compl: verwacht 33
- Aantal `skos:exactMatch` in m10: verwacht 0
- Aantal `skos:narrowMatch` in m10: verwacht 0
- Totaal m10 ctrl→compl SKOS: verwacht 118

Documenteer in patch-rapport §3.

---

## §3. Stap B — Productie-run applier

### §3.1 — Uitvoering

```bash
python3 output/scripts/apply_patch_v4_6_2.py --apply
```

Script-gedrag (per Stap 3-rapport §2.3):

- Backup: `ontology/m10-nis2-ext.ttl.v4_6_1.bak` aangemaakt vóór mutatie
- 65 mutaties via per-mutatie regex-patroon (Turtle-blok-aware)
- Sanity-check: totaal SKOS-predicates in m10 moet exact behouden zijn (alleen herclassificatie, geen toevoeging/verwijdering)
- Faal-safe exit bij conflicten

### §3.2 — Verwachte output

```
Backup: ontology/m10-nis2-ext.ttl.v4_6_1.bak
Toegepast: 65 mutaties (32 downgrades + 33 upgrades)
Sanity-check: pre-totaal 118 = post-totaal 118 ✓
File-mutatie: ontology/m10-nis2-ext.ttl (nieuw hash)
```

### §3.3 — Post-patch sanity-check (immediaat)

```bash
shasum -a 256 ontology/m10-nis2-ext.ttl  # moet ≠ pre-patch-hash
diff ontology/m10-nis2-ext.ttl.v4_6_1.bak ontology/m10-nis2-ext.ttl | wc -l  # moet >0 (mutaties zichtbaar)
```

### §3.4 — Stop-conditie bij Stap B-failure

Als applier faalt of sanity-check mismatch:

1. **Stop direct.** Geen verdere Stap-C/D/E-uitvoering.
2. **Rollback:** `cp ontology/m10-nis2-ext.ttl.v4_6_1.bak ontology/m10-nis2-ext.ttl`
3. **Scope-pauze-rapport** schrijven met error-output + diagnose
4. Wacht op masterchat-besluit

---

## §4. Stap C — Canonical metrics script + run

### §4.1 — Script-creatie

Tech genereert `output/verification/canonical_metrics_v4_6_2.py` op basis van T1-precedent (`output/verification/canonical_metrics_v4_6_1.py` of equivalent in repo).

**Vaste OWL RL-instellingen** (per sprint-protocol):

```python
import owlrl
owlrl.DeductiveClosure(
    owlrl.OWLRL_Semantics,
    axiomatic_triples=False,
    datatype_axioms=False
).expand(graph)
```

### §4.2 — Per-metric expected-values voor v4.6.2

Tech bouwt verwachtingstabel in script:

```python
expected_v4_6_2 = {
    "pre_inference_triples": 20950,
    "post_owlrl_triples": 44907,
    "classes": 199,
    "named_individuals": 1383,
    "object_properties": 149,
    "datatype_properties": 96,
    "owl_sameAs": 98,
    "skos_mappings_total": 1798,
    "m10_skos_exactMatch": 0,
    "m10_skos_closeMatch": 0,
    "m10_skos_broadMatch": 118,
    "m10_skos_narrowMatch": 0,
    "m10_skos_relatedMatch": 0,
}
```

Per metric: verwacht vs werkelijk. Δ-toets binnen tolerantie ±0 (alleen predicate-herclassificatie binnen m10; geen invloed op andere metrics).

### §4.3 — Output

`output/verification/canonical_metrics_v4_6_2.json` met volledig metric-overzicht + per-module-breakdown + Δ-tabel t.o.v. v4.6.1.

### §4.4 — Stop-conditie bij Stap C-failure

Als canonical metrics afwijkt van verwachting buiten tolerantie:

1. **Stop direct.** Geen verdere SHACL-run.
2. Rollback overwegen (masterchat-besluit)
3. Scope-pauze-rapport met afwijkings-analyse
4. Wacht op masterchat-besluit

Tolerantie: 0 voor alle metrics behalve `post_owlrl_triples` (mogelijk ±5 wegens inference-randgevallen; meer dan ±5 = stop).

---

## §5. Stap D — SHACL split-validatie script + run

### §5.1 — Script-creatie

Tech genereert `output/verification/shacl_split_validate_v4_6_2.py` op basis van T1-precedent.

**Twee secties verplicht** (per kritieke conventie):

```python
# SECTIE A — inference='none'
# Shapes: ctrl/bio ISO27002NamingShape, HandreikingBBNValueShape, asset:NamespaceShape
validate(graph, shapes_graph=section_a, inference='none')

# SECTIE B — inference='owlrl'
# Shapes: AppliesToAssetTypeRangeShape, BVASymmetryShape, OrphanClassShape
validate(graph, shapes_graph=section_b, inference='owlrl')

# Gecombineerd (referentie-meting)
validate(graph, shapes_graph=full_shapes, inference='owlrl')
```

### §5.2 — Per-sectie expected-values voor v4.6.2

```python
expected_shacl_v4_6_2 = {
    "section_a_violations": 0,           # inference='none'
    "section_b_violations": 0,           # inference='owlrl'
    "combined_violations": 290,          # bekende false-positives, identiek aan v4.6.1
}
```

### §5.3 — Output

`output/verification/shacl_results_v4_6_2.json` met:

- Per sectie: violation-count + violation-details (indien aanwezig)
- Gecombineerde uitvoering: violation-count + diff t.o.v. v4.6.1-baseline (verwacht: identiek 290)

### §5.4 — Stop-conditie bij Stap D-failure

Als SHACL nieuwe violations toont:

| Type | Drempel | Actie |
|---|---|---|
| SECTIE A violations | >0 | Stop + rollback overwegen + masterchat-escalatie |
| SECTIE B violations | >0 | Stop + rollback overwegen + masterchat-escalatie |
| Combined violations | >290 of <290 | Diagnose-vereist; masterchat-input nodig |

SKOS-predicate-substitutie binnen m10 zou geen SHACL-impact moeten hebben (geen shape valideert op skos:closeMatch/broadMatch/relatedMatch-distributie). Onverwachte violations = onverwachte side-effect = stop.

---

## §6. Stap E — File-hashes

### §6.1 — Uitvoering

```bash
shasum -a 256 ontology/*.ttl > output/verification/file_hashes_v4_6_2.txt
```

### §6.2 — Verwachte hash-impact

| Bestand | Verwachting |
|---|---|
| `m10-nis2-ext.ttl` | **Nieuwe hash** (≠ v4.6.1-baseline `cb2d567b...`) |
| 21 andere modules + `grc-shacl.ttl` | **Identiek aan v4.6.1-baseline** |

### §6.3 — Stop-conditie bij Stap E-failure

Indien meer dan één module-hash veranderd is: stop, rollback, masterchat-escalatie. Mogelijke oorzaak: applier-script heeft per ongeluk buiten m10 gemuteerd.

---

## §7. Stap F — Patch-rapport v4.6.2 schrijven

### §7.1 — Bestandsnaam

`output/reports/patch-rapport-v4_6_2.md`

### §7.2 — Structuur (§0-§13 conform sprint-Protocol §18 / T1-precedent)

Tech genereert volledige §0-§13 conform `output/reports/t1-eindrapport-v4_6_1.md`-precedent of `output/reports/patch-rapport-v4_6_1.md` (indien aparte file). Indeling:

| § | Inhoud | Bron |
|---|---|---|
| §0 | Samenvatting (uit canonical_metrics_v4_6_2.json) | `output/verification/canonical_metrics_v4_6_2.json` |
| §1 | Aanleiding (T2-sprint kernuitkomst + cluster-discipline-validatie) | Stap 3-rapport §1 |
| §2 | Scope (m10-only, 65 mutaties, alleen predicate-substitutie) | Stap 3-rapport §1.3 |
| §3 | Wijzigingen per module (alleen m10-nis2-ext.ttl; hash-mutatie) | Stap E-output |
| §4 | Triples-impact + per-metric Δ-tabel | Stap C-output |
| §5 | Klassen / Individuals / Properties-impact (alle 0) | Stap C-output |
| §6 | SKOS-mappings pre/post distributie + per-cluster-tabel | Stap 3-rapport §1.1 |
| §7 | SHACL-validatie-uitkomsten (SECTIE A + B + combined) | Stap D-output |
| §8 | Sprint-multiplier (Δ triples / sprint-precedent) | Berekening |
| §9 | **Deliverables-tabel** (lokaties scripts + JSON's + rapporten conform Protocol 16) | — |
| §10 | Sprint-protocollen geactiveerd / aangepast (Protocol 14/15/16/17) | — |
| §11 | Verwijzingen | — |
| §12 | Open issues / vervolg (Protocol v1.3-overweging, Brein-cyclus) | — |
| §13 | Wijzigingsoverzicht / changelog t.o.v. v4.6.1 | — |

### §7.3 — §9 Deliverables-tabel (verplicht conform Protocol 16)

Expliciete lokaties van alle Stap 4-deliverables:

| Deliverable | Pad |
|---|---|
| Patch-applier (productie) | `output/scripts/apply_patch_v4_6_2.py` |
| Cluster-overerving-helper | `output/scripts/t2-cluster-overerving-helper.py` |
| 10 cluster-JSON's + overview | `output/analysis/t2-cluster-{a..j}.json` + `output/analysis/t2-cluster-overview.json` |
| Canonical metrics script | `output/verification/canonical_metrics_v4_6_2.py` |
| Canonical metrics resultaat | `output/verification/canonical_metrics_v4_6_2.json` |
| SHACL split-validatie script | `output/verification/shacl_split_validate_v4_6_2.py` |
| SHACL resultaat | `output/verification/shacl_results_v4_6_2.json` |
| File-hashes | `output/verification/file_hashes_v4_6_2.txt` |
| Pre-sprint-inventarisatie | `output/reports/t2-pre-sprint-inventarisatie.md` |
| Pilot-rapport (met errata-blok) | `output/reports/t2-pilot-rapport.md` |
| Stap 3-eindrapport (met §1.1 gecorrigeerd) | `output/reports/t2-stap3-eindrapport.md` |
| Patch-rapport v4.6.2 (dit rapport) | `output/reports/patch-rapport-v4_6_2.md` |
| Backup-file (pre-patch) | `ontology/m10-nis2-ext.ttl.v4_6_1.bak` |
| Sprint-instructies | `docs/instructies/instructie-t2-{pre-sprint-inventarisatie,pilot,stap3,pre-stap4-errata,stap4}.md` |

### §7.4 — §12 Open issues / vervolg

Verplichte sub-secties:

**§12.1 — T-historie correctie-aantekeningen** (referentie naar errata-acties):
- Pilot-rapport heeft errata-blok bovenaan (T-historie-correctie 27-05-2026)
- Stap 3-rapport §1.1 pilot-referentie + Stap 3 resterend gecorrigeerd (27-05-2026)
- Beide correcties zijn pre-Stap-4 hygiëne; geen impact op v4.6.2-mutaties

**§12.2 — Protocol v1.3-overwegingen** (5 voorstellen pilot-rapport §7.3 + Stap 3-leerpunten):
- C1 "partieel"-grens verduidelijking
- C2 + subject-cluster object-cluster-prevalence expliciet
- §5 confidence-criterium expliciteren
- Cluster-representant-keuze-criteria
- Bottom-up rapport-bouw werkflow + interne tabel-consistentie-discipline
- Status: niet uitgevoerd in T2; aanbevolen voor Brein-cyclus post-T2 of m14-sprint-voorbereiding

**§12.3 — Brein-cyclus T2-afsluiting**:
- Pending na Stap 4-afsluiting; Brein-subagent doet brain-vault-update
- Verwachte updates:
  - Sprint-bestand `brain__sprints__T2-skos-bidirectional-audit-m10.md`
  - Update `brain__sprints__sprint-register.md`
  - Update `brain__decisions__D04_skos-cross-framework.md` (D4.1-toepassing-precedent met cluster-discipline-validatie)
  - Update `brain__architecture__H36_skos-exactmatch-ctrl-compl-audit.md` (parent voor T1+T2)
  - Update `brain__concepts__skos-beoordelings-protocol.md` (v1.2-toepassings-bewijs)
  - Update `brain__concepts__mapping-bron-disclaimer-effect.md` (D4.1-toepassing op cluster-niveau)
  - Update `brain__log.md` + `brain__index.md` (iteratie-teller + v4.6.2-baseline)
- Verwachte nieuwe concept-bestanden:
  - `brain__concepts__cluster-discipline-bewijslast.md` (uit Stap 3-leerpunt §6.5)
  - Optioneel: `brain__concepts__bidirectional-audit-symmetrie.md` (Categorie 7-bewijs)

**§12.4 — m14-sprint-voorbereiding** (toekomstig T-volgnummer):
- 31 m14 ctrl:↔compl: paren wachten op aparte sprint (besluit C masterchat-review §2)
- AVG-cross-walk-bron ontbreekt in `sources/` → bron-upload of evidence-niveau-2/3-tolerantie nodig
- compl→ctrl-richting (m14-modelleringsconventie) vereist protocol-symmetrie-validatie
- Helper-script-uitbreiding voor cross-module label-bronnen + m14-specifieke heuristieken

---

## §8. GO-criteria Stap 4

Per Stap 3-rapport §7.4, met aanvullingen:

| # | Criterium | Drempel | Bron |
|---|---|---|---|
| 1 | Applier productie-run succesvol | 65/65 mutaties zonder fouten | Stap B-output |
| 2 | Backup-file aanwezig | `m10-nis2-ext.ttl.v4_6_1.bak` bestaat | Filesystem-check |
| 3 | m10 SKOS-counts post-patch | exact 0 / close 0 / broad 118 / narrow 0 / related 0 | Stap C SPARQL |
| 4 | Canonical metrics totaal-triples | ±0 t.o.v. v4.6.1 (pre-inference 20.950) | `canonical_metrics_v4_6_2.json` |
| 5 | Canonical metrics post-OWL-RL | ±5 t.o.v. v4.6.1 (44.907) | `canonical_metrics_v4_6_2.json` |
| 6 | Klassen / Individuals / OP / DP | identiek aan v4.6.1 (199/1383/149/96) | `canonical_metrics_v4_6_2.json` |
| 7 | SHACL SECTIE A | 0 nieuwe violations | `shacl_results_v4_6_2.json` |
| 8 | SHACL SECTIE B | 0 nieuwe violations | `shacl_results_v4_6_2.json` |
| 9 | SHACL combined | 290 (identiek aan v4.6.1) | `shacl_results_v4_6_2.json` |
| 10 | File-hash m10 | nieuwe sha256 ≠ `cb2d567b...` | `file_hashes_v4_6_2.txt` |
| 11 | File-hashes overige 21 modules + grc-shacl | identiek aan v4.6.1 | `file_hashes_v4_6_2.txt` |
| 12 | Patch-rapport §0-§13 compleet | alle 14 secties ingevuld | `patch-rapport-v4_6_2.md` |
| 13 | Pre-push disclosure-check Protocol 14 | 5 categorieën pass | Tech-check vóór hand-off |

Alle 13 criteria moeten **groen** zijn vóór hand-off naar Steven. Bij één rood criterium: stop + scope-pauze-rapport + wacht op masterchat-besluit.

---

## §9. Werkflow-discipline tijdens Stap 4

### §9.1 — Bottom-up rapport-bouw (pilot/Stap-3-leerpunt §6.4)

Patch-rapport v4.6.2 bouwen in volgorde:

1. Eerst Stap A t/m E uitvoeren + outputs vastleggen
2. Dan §3-§9 patch-rapport (feitelijke verificatie-resultaten)
3. Dan §10-§13 (context + verwijzingen)
4. **Laatst** §0 samenvatting + §1 aanleiding + §2 scope (afgeleid uit §3-§9)

### §9.2 — Werkflow-leerpunten markeren tijdens uitvoering (Protocol v1.2 §10)

Markeer voortdurend. Zeven categorieën, maar in Stap 4 ligt focus op:

- **Categorie 1: Tooling-gaten** — werkten canonical_metrics + SHACL-scripts efficient?
- **Categorie 2: Bron-toegankelijkheid** — niet relevant in Stap 4 (geen NEN-toets)
- **Categorie 4: Werkverdeling-momenten** — Tech-autonomie op productie-uitvoering volstaat?
- **Categorie 7: Upgrade-detectie-praktijk** — wel meenemen voor patch-rapport §6 patch-distributie-tabel

---

## §10. Hand-off-checklist

- [ ] Pre-push disclosure-check Protocol 14 (vijf categorieën)
  - [ ] Organisatie-naam: geen vermelding
  - [ ] Persoonsnamen: alleen Steven Bouwmeester
  - [ ] Lokale paden: alleen `/Users/stevenbouwmeester/grc-kennismodel/` + NEN-licentie-pad
  - [ ] Credentials/TLD/e-mail: geen
  - [ ] NEN-tekst-fragmenten >10 woorden: geen verbatim
- [ ] Alle 13 GO-criteria §8 groen
- [ ] m10-nis2-ext.ttl gemuteerd, backup-file aanwezig
- [ ] Canonical metrics + SHACL-scripts + outputs in `output/verification/`
- [ ] Patch-rapport v4.6.2 §0-§13 compleet
- [ ] Deliverables-tabel §9 patch-rapport bevat alle lokaties
- [ ] §12 Open issues bevat T-historie-correctie-aantekeningen + Protocol v1.3-overwegingen + Brein-cyclus-richtlijnen + m14-sprint-voorbereiding
- [ ] Geen autonome commits (Steven commit handmatig)
- [ ] Bottom-up rapport-bouw toegepast (§3-§9 vóór §0-§2)

---

## §11. Wat NIET in Stap 4

- Geen Protocol v1.3-tekst-aanpassing (wachten op Brein-cyclus na T2-afsluiting)
- Geen `docs/sprint-protocols.md`-aanpassing (Brein-cyclus)
- Geen brain-vault-bestanden (Brein-cyclus)
- Geen m14-paren behandeld (buiten T2-scope per Optie C)
- Geen dashboard-build (separate Dashboard-werkstroom + dashboard-inhaalslag staat open)
- Geen masterchat-judgement-vragen verwacht (alle 65 mutaties hebben hoge confidence via cluster-discipline)

---

## §12. Geschatte duur Stap 4

Per Tech §7.6 Stap 3-rapport + masterchat-aanvulling:

| Aspect | Schatting |
|---|---:|
| Stap A: pre-patch baseline-snapshot | ~5 min |
| Stap B: applier productie-run + sanity-check | ~10 min |
| Stap C: canonical metrics script-creatie + run | ~30 min |
| Stap D: SHACL split-validatie script-creatie + run | ~30 min |
| Stap E: file-hashes opslaan | ~5 min |
| Stap F: patch-rapport v4.6.2 schrijven (bottom-up) | ~1.5 uur |
| **Totaal Stap 4** | **~2.5-3 uur** |

Geen harde deadline. Kwaliteit + verificatie-discipline boven snelheid.

---

## §13. Bij voltooiing

Tech pushed alle deliverables. Steven commit + push handmatig. Masterchat reviewt:

- Alle 13 GO-criteria groen?
- Patch-rapport-volledigheid §0-§13?
- Eventuele werkflow-leerpunten reden voor protocol-aanpassing?
- T2-sprint-afsluiting akkoord?

**Bij masterchat-GO: T2-sprint formeel afgesloten.** Daarna:

1. **Brein-cyclus** voor brain-vault-update (Brein-subagent in Claude Code)
2. **Protocol v1.3-overweging** door masterchat (5 voorstellen + Stap 3-leerpunten)
3. **T-volgnummer-scoping** voor m14 of andere SKOS-audit-uitbreiding (apart sessie)
4. **Optioneel: dashboard-inhaalslag** vanaf v4.6.0 → v4.6.2 in dashboard-pipeline (Dashboard-subagent, separaat werk)

T2-sprint-architectuur is dan compleet:

```
Stap 1: pre-sprint-inventarisatie    [voltooid]
Stap 2: pilot van 8 paren            [voltooid, errata 27-05]
Stap 3: hoofd-uitvoering 110 paren   [voltooid, §1.1 gecorrigeerd 27-05]
Pre-Stap-4 errata-correctie          [voltooid 27-05]
Stap 4: productie-patch + verificatie + rapport [Tech-actie]
Brein-cyclus T2-afsluiting           [post-Stap-4]
```

---

*Einde T2 Stap 4 instructie. Modus: PRODUCTIE — ontologie-mutatie + verificatie + patch-rapport. Geen verdere autonome actie na deliverables-push.*
