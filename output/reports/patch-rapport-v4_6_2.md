---
type: report
subtype: patch-rapport
version: v4.6.2
baseline_from: v4.6.1
baseline_to: v4.6.2
sprint: T2
date: 2026-05-27
status: final-awaiting-masterchat-review
related:
  - skos-beoordelings-protocol-v1_2
  - H36_skos-exactmatch-ctrl-compl-audit
  - D04_skos-cross-framework
  - t2-pre-sprint-inventarisatie
  - t2-pilot-rapport
  - t2-stap3-eindrapport
  - patch-rapport-v4_6_1
scope: "Patch v4.6.2 — T2-sprint SKOS-bidirectional-audit m10. 65 SKOS-predicate-substituties in m10-nis2-ext.ttl (32 closeMatch -> broadMatch downgrades + 33 relatedMatch -> broadMatch upgrades). Cluster-discipline over 10 NIS2-art.21-letter-clusters; alle clusters convergeren naar broadMatch. Geen TBox-wijziging. Geen andere modules dan m10-nis2-ext.ttl."
---

# Patch-rapport v4.6.2

## §0. Versie + metrics-vergelijking

Cijfers in dit rapport komen uit `output/verification/canonical_metrics_v4_6_2.json` (gemeten op de gepatchte versie van de ontologie). **Niet uit memorie** (sprint-Protocol §18-discipline, v4.3.3-leerpunt).

### §0.1 Vergelijking v4.6.1 → v4.6.2

| Metric | v4.6.1 | v4.6.2 | Δ |
|---|---:|---:|---:|
| Pre-inference triples | 20.950 | 20.950 | **0** |
| Post-inference triples (OWL RL) | 44.907 | 44.907 | **0** |
| owl:Class | 199 | 199 | 0 |
| owl:NamedIndividual | 1.383 | 1.383 | 0 |
| owl:ObjectProperty | 149 | 149 | 0 |
| owl:DatatypeProperty | 96 | 96 | 0 |
| owl:sameAs | 98 | 98 | 0 |
| skos_mappings_total | 1.798 | 1.798 | **0** |
| skos:exactMatch | 18 | 18 | 0 |
| skos:closeMatch | 1.489 | 1.457 | **−32** |
| skos:broadMatch | 66 | 131 | **+65** |
| skos:narrowMatch | 0 | 0 | 0 |
| skos:relatedMatch | 225 | 192 | **−33** |
| rdfs:label totaal | 3.827 | 3.827 | 0 |
| rdfs:comment totaal | 1.760 | 1.760 | 0 |
| owl:Nothing post-inferentie | 0 | 0 | 0 (consistent) |
| D5 ctrl↔bio sameAs | 93 | 93 | 0 (conform) |
| D11 asset-brug | 5 | 5 | 0 (conform) |
| D8 SoAEntry | 93 | 93 | 0 |
| ext:hasHandreikingBBN assertions | 241 | 241 | 0 |

**Kernobservatie:** triple-totaal en alle individuals/klassen/property-tellingen zijn ongewijzigd. Enige mutatie is predicate-name voor 65 specifieke triples in m10-nis2-ext.ttl (32 closeMatch + 33 relatedMatch herclassificeerd naar broadMatch). SKOS-mappings-totaal blijft 1.798 (predicate-substitutie binnen behouden totaal; geen toevoeging, geen verwijdering).

### §0.2 ctrl→compl SKOS-paren-mutatie (m10-scope)

| Pair-type | v4.6.1 | v4.6.2 | Δ |
|---|---:|---:|---:|
| `ctrl->compl::exactMatch` | 0 | 0 | 0 |
| `ctrl->compl::closeMatch` | 32 | **0** | −32 |
| `ctrl->compl::broadMatch` | 53 | **118** | +65 |
| `ctrl->compl::narrowMatch` | 0 | 0 | 0 |
| `ctrl->compl::relatedMatch` | 33 | **0** | −33 |
| **Totaal ctrl→compl m10** | **118** | **118** | **0** |

Alle 118 ctrl→compl:NIS2_Art21_*-paren convergeren post-patch naar `skos:broadMatch`, conform Protocol v1.2 §3.1 rij 6 cluster-doel-predicate voor veel↔1-cluster-cardinaliteit (zie §6 voor cluster-tabel).

### §0.3 File-hash-mutatie

| Bestand | v4.6.1 SHA256 | v4.6.2 SHA256 | Wijziging? |
|---|---|---|---|
| m10-nis2-ext.ttl | `cb2d567b…d8afa2f1` | `a4bfdc12…00a3dd44e` | **ja** |
| Andere 21 .ttl + grc-shacl.ttl | (zie file_hashes_v4_6_1.txt) | identiek | **nee** |

Volledige file-hash-lijst: `output/verification/file_hashes_v4_6_2.txt`. Vergelijking `diff file_hashes_v4_6_1.txt file_hashes_v4_6_2.txt` toont uitsluitend de m10-hash-mutatie; alle 22 andere bestanden hash-identiek.

---

## §1. Aanleiding

T2-sprint (SKOS-kwaliteitsanalyse Fase 2 — bidirectional audit ctrl:↔compl: in m10-nis2-ext.ttl) is in vier stappen uitgevoerd:

1. **Stap 1** (pre-sprint-inventarisatie) — 118 ctrl→compl m10-paren bevestigd (incl. 28 reeds in v4.6.1 omgezet); ABox-baseline + cluster-cardinaliteit per NIS2-art.21-letter vastgelegd
2. **Stap 2** (pilot 8 paren) — Protocol v1.2 toegepast op cluster-representanten over alle 10 clusters; 4 patch-mutaties bevestigd, cluster-discipline gevalideerd op pilot-niveau
3. **Stap 3** (hoofd-uitvoering 110 paren) — cluster-niveau-batching via cluster-overerving-helper-script; alle 10 clusters convergeren naar cluster-doel-predicate `skos:broadMatch`; 0 NEN-aantoonbare uitzonderingen
4. **Stap 4** (productie-patch + verificatie + rapport — dit rapport) — 65 mutaties via `apply_patch_v4_6_2.py --apply`; canonical metrics + SHACL split-validatie + file-hashes

**Cluster-discipline-bewijs (T2-leerpunt §3.3 Protocol v1.2):** alle 10 NIS2-art.21-letter-clusters convergeren naar één doel-predicate (`broadMatch`) zonder NEN-aantoonbare individuele uitzondering. 10 heuristiek-flags (op 6 cluster-leden) zijn na ISO 27002:2022-tekstlezing alle cluster-conform bevonden. Schaalbaarheid van cluster-discipline op m10-scope is daarmee empirisch bevestigd.

**Bron-erf:** evidence-niveau 1 voor alle 65 mutaties via CBW-Excel "Mapping Uitvoeringsverordening" (`sources/adr-norea/Cbw (NIS2) Control Framework.xlsx`) — reproductie van ENISA TIG v1.0. ENISA TIG regel 285-disclaimer (non-equivalence-clausule op cross-framework-mappings) blokkeert exactMatch-claims structureel (D4.1-toepassing). Verbatim citaat in `brain__concepts__mapping-bron-disclaimer-effect.md`.

**D4-rationale:** herclassificatie binnen cluster-discipline is D4 + D4.1-conform:

- C2 veel↔1-cluster-cardinaliteit op alle 10 clusters (object-cluster-grootte 7-32, alle ≥7) → cluster-doel `broadMatch` per Protocol v1.2 §3.1 rij 6
- D4.1-disclaimer-aanwezigheid (ENISA TIG R285) blokkeert exactMatch structureel
- Bilaterale containment afwezig op alle paren (subject ISO27002-control engerebepaalde implementatie-controle ⊂ object NIS2-norm bredere richtlijn-clausule)

---

## §2. Scope

**Wat wijzigt:**

- 32 ctrl→compl:NIS2_Art21_* skos:closeMatch-triples → skos:broadMatch (downgrades)
- 33 ctrl→compl:NIS2_Art21_* skos:relatedMatch-triples → skos:broadMatch (upgrades)
- Totaal: **65 predicate-substituties** in `ontology/m10-nis2-ext.ttl`
- Geen TBox-wijziging (geen klasse, property, restrictie, axiom toegevoegd of verwijderd)
- Geen wijziging in m02-control.ttl, m05-compliance.ttl, of enige andere module
- Geen wijziging in SHACL-shapes (grc-shacl.ttl onveranderd)

**Wat NIET wijzigt:**

- D5 (ctrl↔bio sameAs 93) — onveranderd
- D11 (asset-brug 5) — onveranderd
- 32 ctrl:ISO27002_*-individuals en 10 compl:NIS2_Art21_*-individuals zelf — onveranderd (geen wijziging in rdfs:label, compl:articleRef, of andere properties)
- SoA-structuur (D8, 93 SoAEntries) — onveranderd
- Bestaande 53 ctrl→compl:NIS2_Art21_* skos:broadMatch-triples (incl. de 28 uit v4.6.1-patch) — onveranderd
- m14-paren (31 compl→ctrl skos:closeMatch in m14-avg-gdpr.ttl) — buiten T2-scope per masterchat-besluit Optie C
- Pilot-paren met huidige broadMatch (T2-S01, T2-S04, T2-S06-alt, T2-S08-alt) — behoud, geen mutatie

**Eindstand m10 ctrl→compl SKOS-distributie post-patch:** exact 0 / close 0 / broad 118 / narrow 0 / related 0.

**Bron:** T2-sprint Stap 2 pilot-rapport + T2-sprint Stap 3 eindrapport (beide in `output/reports/`).

---

## §3. Wijzigingen in m10-nis2-ext.ttl

### §3.1 Beschrijving

Voor elk van de 65 regels in m10-nis2-ext.ttl van de vorm:

```turtle
ctrl:ISO27002_X_YY
    skos:[closeMatch|relatedMatch] compl:NIS2_Art21_Z [punt|;] ...
```

wordt het predicate vervangen door `skos:broadMatch`. Geen andere wijziging aan de regel of het omringende blok. Comments, witregels, andere triples (zoals reeds-bestaande broadMatch op andere objecten in hetzelfde subject-blok) blijven onveranderd.

### §3.2 Mutatie-uitvoering — applier-output

Productie-run van `apply_patch_v4_6_2.py --apply` (output volledig in dry-run-equivalent `output/scripts/apply_patch_v4_6_2_dry_run.txt`):

```
apply_patch_v4_6_2.py — modus: PRODUCTIE
Patch-vereiste mutaties totaal: 65
  Pilot-paren in mutatie-set:    4 (T2-S02, T2-S03, T2-S05, T2-S07-alt)
  Uitzondering-flag (review):    10

Per mutatie-richting:
  upgrade                 :  33
  downgrade               :  32

Pre-patch m10 skos-predicate counts:
  skos:exactMatch    :   0
  skos:closeMatch    :  32
  skos:broadMatch    :  53
  skos:narrowMatch   :   0
  skos:relatedMatch  :  33

Toegepast: 65 / 65

Post-patch m10 skos-predicate counts:
  skos:exactMatch    :   0  (Δ 0)
  skos:closeMatch    :   0  (Δ -32)
  skos:broadMatch    : 118  (Δ +65)
  skos:narrowMatch   :   0  (Δ 0)
  skos:relatedMatch  :   0  (Δ -33)

Backup gemaakt: ontology/m10-nis2-ext.ttl.v4_6_1.bak
```

Sanity-check (totaal SKOS-predicates in m10-bestand): 118 pre-patch = 118 post-patch ✓ (alleen herclassificatie, geen toevoeging of verlies).

### §3.3 Pre/post-hash m10-nis2-ext.ttl

| Versie | SHA256 |
|---|---|
| v4.6.1 (pre-patch) | `cb2d567b184877e111800cc0a8af1e38d6d6f74ddca0477ee1a52df1d8afa2f1` |
| v4.6.2 (post-patch) | `a4bfdc12cedb0c5018218a77480393e40fd301dddcd438abb31a84300a3dd44e` |

Backup-file aanwezig: `ontology/m10-nis2-ext.ttl.v4_6_1.bak` (80.429 bytes). Bevat exacte v4.6.1-staat voor rollback-mogelijkheid.

Diff-lijntelling `diff m10-nis2-ext.ttl.v4_6_1.bak m10-nis2-ext.ttl | wc -l` = **242 regels** (unified-diff-uitvoer voor 65 predicate-mutaties met bijbehorende context).

---

## §4. Triples-impact + per-metric Δ-tabel

### §4.1 Globale triples

| Aspect | v4.6.1 | v4.6.2 | Δ |
|---|---:|---:|---:|
| Pre-inference triples | 20.950 | 20.950 | **0** |
| Post-inference (OWL RL) triples | 44.907 | 44.907 | **0** |
| owl:Nothing post-inferentie | 0 | 0 | 0 |

**Verklaring Δ=0 op triple-niveau:** SKOS-predicate-substitutie binnen één blok wijzigt geen triple-aantal — de mutatie vervangt een triple `(s, skos:p1, o)` door `(s, skos:p2, o)`. Beide tellen als één triple. Geen toevoeging, geen verwijdering. Post-OWL-RL-inferentie is eveneens stabiel omdat owlrl in deze configuratie geen SKOS-axiomas laadt (skos:S46/S47 e.d. niet geactiveerd; bekende beperking gedocumenteerd in v4.6.1-rapport §5.2). Predicate-naamverandering raakt geen RDFS/OWL-inferentie-pad.

### §4.2 SKOS-breakdown-Δ

| Predicate | v4.6.1 | v4.6.2 | Δ | Verklaring |
|---|---:|---:|---:|---|
| skos:exactMatch | 18 | 18 | 0 | Alle 28 ctrl→compl exactMatch uit v4.6.0 reeds in v4.6.1 omgezet; resterende 18 zijn in andere paren (niet m10 ctrl→compl) |
| skos:closeMatch | 1.489 | 1.457 | −32 | 32 ctrl→compl m10-paren omgezet (downgrades) |
| skos:broadMatch | 66 | 131 | **+65** | 32 ex-close + 33 ex-related uit m10 ctrl→compl naar broadMatch |
| skos:narrowMatch | 0 | 0 | 0 | Geen narrowMatch in model |
| skos:relatedMatch | 225 | 192 | −33 | 33 ctrl→compl m10-paren omgezet (upgrades) |
| **Totaal** | **1.798** | **1.798** | **0** | Predicate-substitutie binnen behouden totaal |

### §4.3 Stop-condities canonical metrics

| # | Conditie | Drempel | Stand | Status |
|---|---|---|---|---|
| 1 | Pre-inference triples-Δ | ±0 | 0 | **niet geraakt** |
| 2 | Post-inference triples-Δ | ±5 | 0 | **niet geraakt** |
| 3 | Klassen/Individuals/OP/DP-Δ | exact 0 | alle 0 | **niet geraakt** |
| 4 | owl:Nothing post-inf | 0 | 0 | **niet geraakt** |
| 5 | SKOS-mapping-totaal-Δ | ±0 | 0 | **niet geraakt** |

Geen stop-conditie geraakt. Mutaties conform raming.

---

## §5. Klassen / Individuals / Properties-impact

| Aspect | v4.6.1 | v4.6.2 | Δ |
|---|---:|---:|---:|
| owl:Class | 199 | 199 | 0 |
| owl:NamedIndividual | 1.383 | 1.383 | 0 |
| owl:ObjectProperty | 149 | 149 | 0 |
| owl:DatatypeProperty | 96 | 96 | 0 |
| owl:sameAs | 98 | 98 | 0 |
| rdfs:label totaal | 3.827 | 3.827 | 0 |
| rdfs:comment totaal | 1.760 | 1.760 | 0 |

**Alle TBox/ABox-tellingen ongewijzigd.** Patch raakt geen klasse-, property-, restrictie- of axiom-declaratie. Patch is pure SKOS-predicate-substitutie binnen bestaande mapping-triples.

### §5.1 Integriteits-checks (canonical metrics §integrity_checks)

| Check | v4.6.1 | v4.6.2 |
|---|---:|---:|
| GRC-subjects zonder type | 0 | 0 |
| Object-properties zonder domain | 0 | 0 |
| Object-properties zonder range | 0 | 0 |
| Datatype-properties zonder domain | 0 | 0 |
| Datatype-properties zonder range | 0 | 0 |
| Dangling GRC references | 3 | 3 (identieke set; bekende baseline) |
| Duplicate owl:Class declarations | 0 | 0 |
| Namespace leakage | 22 | 22 (identieke set; bekende baseline) |

Geen integriteits-regressie. Identieke baseline aan v4.6.1.

---

## §6. SKOS-mappings pre/post distributie + per-cluster-tabel

### §6.1 Pre/post-distributie ctrl→compl:NIS2_Art21_* (m10-scope)

| Cluster | Cluster-grootte | v4.6.1 close | v4.6.1 broad | v4.6.1 related | v4.6.2 broad | Δ broad |
|---|---:|---:|---:|---:|---:|---:|
| NIS2_a | 12 | 4 | 4 | 4 | **12** | +8 |
| NIS2_b | 10 | 2 | 6 | 2 | **10** | +4 |
| NIS2_c | 8 | 2 | 4 | 2 | **8** | +4 |
| NIS2_d | 7 | 1 | 5 | 1 | **7** | +2 |
| NIS2_e | 17 | 4 | 7 | 6 | **17** | +10 |
| NIS2_f | 7 | 1 | 4 | 2 | **7** | +3 |
| NIS2_g | 9 | 4 | 4 | 1 | **9** | +5 |
| NIS2_h | 7 | 1 | 4 | 2 | **7** | +3 |
| NIS2_i | 32 | 11 | 12 | 9 | **32** | +20 |
| NIS2_j | 9 | 3 | 3 | 3 | **9** | +6 |
| **Totaal** | **118** | **32** | **53** | **33** | **118** | **+65** |

**Cluster-doel-predicate-convergentie:** alle 10 clusters → `skos:broadMatch` (cardinaliteit veel↔1, Protocol v1.2 §3.1 rij 6). 100% cluster-discipline-conform.

### §6.2 Mutatie-richting-verdeling

| Richting | Aantal | % van totaal |
|---|---:|---:|
| Downgrade (closeMatch → broadMatch) | 32 | 49,2% |
| Upgrade (relatedMatch → broadMatch) | 33 | 50,8% |
| Richtings-correctie (broad ↔ narrow) | 0 | 0% |
| Verwijdering | 0 | 0% |
| Behoud (al broadMatch) | 53 | n.v.t. (geen mutatie) |
| Twijfel/escalatie | 0 | 0% |

**Bidirectional bewijs:** mutaties zijn in beide richtingen aanwezig (upgrades én downgrades) met vrijwel identieke aantallen. Protocol v1.2's bidirectional toetsing is symmetrisch toepasbaar gebleken (geen downgrade-bias zoals v1.1-draft had aangenomen).

### §6.3 Uitzondering-screening-uitkomsten

Heuristiek-vlagging via `apply_patch_v4_6_2.py` (overgenomen uit cluster-overerving-helper):

| Subject | Aantal clusters | NEN-uitzondering? |
|---|---:|---|
| ISO27002_5_02 | 2 (a, i) | nee (beide) |
| ISO27002_5_04 | 3 (a, f, g) | nee (alle 3) |
| ISO27002_5_36 | 1 (a) | nee |
| ISO27002_6_05 | 1 (i) | nee |
| ISO27002_8_03 | 3 (h, i, j) | nee (alle 3) |
| **Totaal 10 flags / 6 leden** | | **0 uitzonderingen** |

Detail-onderbouwing per flag: zie Stap 3-eindrapport §3 (cluster-beoordelingen) en §4 (uitzondering-screening-uitkomsten). Alle flags zijn na ISO 27002:2022-tekstlezing cluster-conform bevonden — bilaterale containment (vereist voor `closeMatch`-uitzondering) ontbreekt op alle paren wegens engere ISO-control-scope ⊂ bredere NIS2-clausule-scope.

---

## §7. SHACL-validatie-uitkomsten

Script: `output/verification/shacl_split_validate_v4_6_2.py`
Output: `output/verification/shacl_results_v4_6_2.json`

### §7.1 Drie metingen (split-validatie conform sprint-protocol)

| Meting | Inference | Shapes | Verwacht | Werkelijk | Status |
|---|---|---|---:|---:|---|
| SECTIE A | none | ctrl/bio ISO27002NamingShape, HandreikingBBNValueShape, asset:NamespaceShape | 0 | **0** | ✓ |
| SECTIE B | owlrl | AppliesToAssetTypeRangeShape, BVASymmetryShape, OrphanClassShape | 0 | **0** | ✓ |
| COMBINED | owlrl | alle 7 shapes | 290 | **290** | ✓ (identiek v4.6.1) |

### §7.2 COMBINED-meting-detail

Per source-shape in COMBINED-meting:

| Shape | Violations | Type |
|---|---:|---|
| `https://grc.example.org/asset/NamespaceShape` | 104 | bekende false-positive (OWL-RL-typing-artefact) |
| `https://grc.example.org/bio/ISO27002NamingShape` | 93 | bekende false-positive (OWL-RL-typing-artefact) |
| `https://grc.example.org/control/ISO27002NamingShape` | 93 | bekende false-positive (OWL-RL-typing-artefact) |
| **Totaal** | **290** | identiek aan v4.6.1 |

**Δ vs v4.6.1 baseline: 0 violations.** Geen nieuwe violations geïntroduceerd; geen bestaande violations opgelost door SKOS-predicate-substitutie.

### §7.3 SHACL-blinde-vlek bevestiging

Geen shape in `ontology/grc-shacl.ttl` valideert direct op ctrl:↔compl:-mapping-distributie (T1 Vraag D-inventarisatie + T2 §3.2 stop-conditie-analyse). De 65 SKOS-predicate-substituties raken daarom geen shape — SHACL-uitkomsten zijn structureel ongevoelig voor T2-mutaties. H39 (SHACL-blinde vlek) blijft active geparkeerd voor latere shape-uitbreiding indien gewenst.

### §7.4 Stop-condities SHACL

| Type | Drempel | Stand | Status |
|---|---|---|---|
| SECTIE A violations | >0 | 0 | **niet geraakt** |
| SECTIE B violations | >0 | 0 | **niet geraakt** |
| COMBINED Δ vs baseline | >0 of <0 | 0 | **niet geraakt** |

Geen stop-conditie geraakt. SHACL-uitkomsten regressie-vrij.

---

## §8. Sprint-multiplier + sprint-precedent-vergelijking

| Aspect | T2 (v4.6.2) | T1 (v4.6.1) | Verhouding |
|---|---:|---:|---:|
| Triple-Δ pre-inferentie | 0 | 0 | identiek |
| Triple-Δ post-OWL-RL | 0 | 0 | identiek |
| Aantal SKOS-mutaties | 65 | 28 | 2,32× |
| Mutatie-richtingen | upgrade + downgrade (bidirectional) | downgrade-only | bidirectional-uitbreiding |
| Gewijzigde modules | 1 (m10) | 1 (m10) | identiek |
| Cluster-scope | 10 clusters | 10 clusters | identiek (m10-NIS2-art.21-scope) |
| Protocol-versie | v1.2 | v1.0 | protocol-progressie |
| Pilot-omvang | 8 paren | 5 paren | +60% (Protocol v1.2 §6 spreiding-richtlijn) |
| Helper-tooling | cluster-overerving-helper + heuristiek-screening | n.v.t. (geen helper) | nieuwe tooling-laag |
| NEN-werkverdeling | Tech-autonomie (Protocol 17 v1.3) | masterchat-toets (Protocol 17 pre-herziening) | Tech-autonomie-uitbreiding |

**Sprint-multiplier:** T2 verwerkt 2,32× meer mutaties dan T1 met vergelijkbare triple-impact (Δ=0 in beide gevallen, want pure predicate-substitutie). Het meervoud aan mutaties komt door:

1. Bidirectional-scope (Protocol v1.2 uitbreiding) — vangt zowel onderclaim (relatedMatch) als overclaim (closeMatch) op
2. Volledige m10-scope (T1 dekte alleen exactMatch-subset van 28 paren; T2 dekt ook close + related)
3. Cluster-doel-discipline (alle 10 clusters convergeren naar één predicate ipv. mengeling)

---

## §9. Deliverables-tabel (Protocol 16 verplicht)

Expliciete relatieve lokaties vanaf repo-root van alle T2-deliverables:

### §9.1 Productie-scripts + outputs

| Deliverable | Pad | Type |
|---|---|---|
| Patch-applier (productie + dry-run) | `output/scripts/apply_patch_v4_6_2.py` | script |
| Cluster-overerving-helper | `output/scripts/t2-cluster-overerving-helper.py` | script |
| Applier dry-run-log | `output/scripts/apply_patch_v4_6_2_dry_run.txt` | output |
| 10 cluster-JSON's | `output/analysis/t2-cluster-{a..j}.json` | output |
| Cluster-overview-JSON | `output/analysis/t2-cluster-overview.json` | output |

### §9.2 Verificatie-scripts + outputs

| Deliverable | Pad | Type |
|---|---|---|
| Canonical metrics-script | `output/verification/canonical_metrics_v4_6_2.py` | script |
| Canonical metrics-output | `output/verification/canonical_metrics_v4_6_2.json` | output |
| SHACL split-validatie-script | `output/verification/shacl_split_validate_v4_6_2.py` | script |
| SHACL-validatie-output | `output/verification/shacl_results_v4_6_2.json` | output |
| File-hashes | `output/verification/file_hashes_v4_6_2.txt` | output |

### §9.3 Rapporten

| Deliverable | Pad | Type |
|---|---|---|
| Pre-sprint-inventarisatie (Stap 1) | `output/reports/t2-pre-sprint-inventarisatie.md` | rapport |
| Pilot-rapport (Stap 2, met errata-blok) | `output/reports/t2-pilot-rapport.md` | rapport |
| Stap 3-eindrapport (met §1.1-correctie) | `output/reports/t2-stap3-eindrapport.md` | rapport |
| Patch-rapport v4.6.2 (dit rapport) | `output/reports/patch-rapport-v4_6_2.md` | rapport |

### §9.4 Backup + sprint-instructies

| Deliverable | Pad | Type |
|---|---|---|
| Backup pre-patch | `ontology/m10-nis2-ext.ttl.v4_6_1.bak` | backup |
| Sprint-instructies | `docs/instructies/instructie-t2-{pre-sprint-inventarisatie,pilot,stap3,pre-stap4-errata,stap4}.md` | instructies |
| Protocol-bestand | `docs/skos-beoordelings-protocol-v1_2.md` | protocol |

---

## §10. Sprint-protocollen — geactiveerd / aangepast

### §10.1 Geactiveerde protocollen (uit `docs/sprint-protocols.md` v1.3)

| Protocol | Toepassing in T2 |
|---|---|
| Protocol 1 (Pre-sprint-inventarisatie) | Stap 1 — 118 m10-paren bevestigd, ABox-baseline + cluster-cardinaliteit |
| Protocol 4 (Bron-verificatie vóór TBox) | n.v.t. — geen nieuwe property/klasse in T2 |
| Protocol 7 (Bron-bereikbaarheid) | Lokale NEN-bron-toegang `/Users/stevenbouwmeester/grc-sources-licensed/` getoetst (Protocol 17 v1.3) |
| Protocol 10 (Patch-rapport §9 geparkeerd-items) | §11 dit rapport |
| Protocol 12 (Instructie-consistentie code vs toelichting) | Genoteerd in §12.2 (m10-only scope §8 GO-criterium leidend; §1 verwachtings-tabel inclusief m14 niet geldend voor v4.6.2-meting) |
| Protocol 14 (Pre-push disclosure-check) | 5 categorieën gescand op alle Stap 4-deliverables — geen vondsten |
| Protocol 15 (Tech levert werkbare applier) | `apply_patch_v4_6_2.py` geleverd in Stap 3 (dry-run) + productie-run in Stap 4 |
| Protocol 16 (Deliverables-tabel expliciet) | §9 dit rapport |
| Protocol 17 v1.3 (NEN-werkverdeling Tech-autonomie) | Lokale ISO 27002:2022-tekst-lezing voor 10 uitzondering-screening-flags; parafrase-discipline gehandhaafd |

### §10.2 Niet-geactiveerde protocollen

| Protocol | Reden |
|---|---|
| Protocol 5/6/9 (raming-discipline) | Sprint-doel was kwaliteitsanalyse, geen ABox-creatie; triple-Δ-raming = 0 (predicate-substitutie) |
| Protocol 8 (Precedent-discipline framework-cluster) | Geen nieuw cluster — m10-NIS2 bestond reeds in baseline |
| Protocol 11 (Brain-vault-update) | Brein-cyclus volgt na masterchat-GO op dit patch-rapport — buiten Tech-scope |
| Protocol 13 (Bron-typo-beleid) | Geen typo's tegengekomen in m10-mutaties |
| GR (Property-semantiek) | Geen nieuwe property |

### §10.3 Protocol-progressie tijdens T2

Geen sprint-protocol-tekst is door Tech-subagent gewijzigd tijdens T2 (zie §12.3 voor protocol v1.3-overwegingen voor toekomstige Brein-cyclus).

---

## §11. Geparkeerde-items-status-update (Protocol 10)

| H-item | Vóór v4.6.2 | Na v4.6.2 | Mutatie |
|---|---|---|---|
| H36 (SKOS-exactMatch ctrl/compl-audit) | afgehandeld (T1) — open-uitbreiding voor close/related-audit (T2-scope) | **afgehandeld** voor m10-scope; m14-paren resterend voor toekomstige T-sprint | mutatie: T2-component closed |
| H37 | active | active | ongewijzigd |
| H38 | active | active | ongewijzigd |
| H39 (SHACL-blinde vlek ctrl:↔compl:) | active — bevestigd in T1+T2 | active | ongewijzigd; T2 bevestigt opnieuw |
| H40 (UI-renderdekking Spoor A) | active | active | ongewijzigd |
| H25/H26/H27/H32/H33/H34/H35 | (per status H-register) | (per status H-register) | ongewijzigd |
| H41-kandidaat (SKOS-axioma-set-handling) | niet gedeclareerd | gedeclareerd-bewijs uit T2 §5.2 v4.6.1-rapport | masterchat-overweging voor H-declaratie |

Brein-cyclus-update vereist na masterchat-GO:
- H36-register-entry kan naar closed-segment (m10-scope volledig afgehandeld); m14-component blijft als open subtask
- H39 onveranderd active geparkeerd
- Optionele H41-declaratie SKOS-axioma-set-handling (skos:S46 symmetrie, skos:S47 transitiviteit) als architectuur-vraag voor toekomstige OWL-RL-uitbreiding

Geen H-register-update door Tech in dit rapport — Brein-cyclus uitvoert post-Stap-4.

---

## §12. D-decision-conformiteit-check (D1-D12)

| D | Conventie | v4.6.2-impact | Conform? |
|---|---|---|---|
| D1 | OWL 2 DL profiel | Geen TBox-wijziging, geen cycle/owl:Thing-domain | ✓ |
| D2 | Turtle-serialisatie | m10-nis2-ext.ttl blijft Turtle | ✓ |
| D3 | 11 namespaces | Geen nieuwe namespace | ✓ |
| D4 | SKOS cross-framework — closeMatch default, exactMatch zeldzaam | Herclassificatie van 32 close + 33 related naar broadMatch is D4-conform onder cluster-veel↔1-cardinaliteit | ✓ verbetering |
| D4.1 | Disclaimer-handling autoritatieve mapping-bronnen | ENISA TIG R285-disclaimer-toepassing bevestigd op cluster-niveau voor alle 10 clusters | ✓ toepassing |
| D5 | ctrl:↔bio: sameAs strikt — 93 pairs | Onveranderd 93 | ✓ |
| D6 | Bilinguale annotaties @nl/@en | Geen wijziging in labels/comments | ✓ |
| D7 | BIO 2.0 als twee klassen | Geen BIO2-wijziging | ✓ |
| D8 | Eén canonieke SoA — isms:SoA_2026 + 93 SoAEntry_* | Onveranderd 93 | ✓ |
| D9 | Framework-neutraal | Onveranderd | ✓ |
| D10 | COSO ICF/ERM enterprise-governance-laag | Onveranderd | ✓ |
| D11 | owl:sameAs asset-convergentie — ster-patroon | Onveranderd 5 | ✓ |
| D12 | Drie-laags compliance | Onveranderd | ✓ |

**Alle 12 D-decisions conform. D4 + D4.1-compliance bevestigd door symmetrische bidirectional toepassing van cluster-discipline (Protocol v1.2 §3.3).**

---

## §13. Aandachtspunten + open issues / vervolg

### §13.1 — T-historie correctie-aantekeningen (pre-Stap-4 hygiëne)

Twee correctie-acties uitgevoerd 27 mei 2026 vóór Stap 4-uitvoering — beide geen impact op v4.6.2-mutaties, alleen consistentie-correctie van eerdere rapporten:

1. **Pilot-rapport (Stap 2):** errata-blok bovenaan toegevoegd m.b.t. T2-S03-classificatie (pilot-rapport noemde "downgrade"; Protocol v1.2 §3.2 sterkte-ordening classificeert relatedMatch → broadMatch als upgrade). Patch-impact identiek; classificatie-kolom gecorrigeerd.
2. **Stap 3-eindrapport §1.1:** pilot-referentie-rij gecorrigeerd naar helper-script-classificatie (2 downgrade / 2 upgrade ipv. 3 downgrade / 1 upgrade). Patch-totaal (4 pilot-paren patch-vereist) en T2-totaal (53/32/33) onveranderd.

T-historie is daarmee consistent met helper-script-output. Beide correcties zijn pre-Stap-4 hygiëne; geen v4.6.2-mutatie-impact.

### §13.2 — Instructie-consistentie-aandachtspunt (Protocol 12 categorie)

**Werkflow-leerpunt categorie 3 (Protocol-criteria-onduidelijkheden):**

Sprint-instructie-tekst bevat een interne inconsistentie in de verwachtings-tabel §1 vs §8 GO-criterium #3:

- **§1 verwachtings-tabel** voorspelt post-patch m10 ctrl→compl: "exact 0 / close 0 / broad 118 / narrow 0 / **related 27**" (suggereert m14-mappings meegerekend)
- **§8 GO-criterium #3** voorspelt: "exact 0 / close 0 / broad 118 / narrow 0 / **related 0**" (m10-only scope)

**Bron-van-waarheid toegepast:** werkelijke counts uit `canonical_metrics_v4_6_2.json` zijn autoritatief. m10 ctrl→compl-paren post-patch is **0 / 0 / 118 / 0 / 0** (m10-only scope conform §4.2 `expected_v4_6_2`-tabel en §8 GO-criterium #3). De 31 m14-paren (compl→ctrl-richting in m14-avg-gdpr.ttl) zijn niet in m10 — buiten T2-scope per masterchat-besluit Optie C. De §1-tabel-tekst-formulering "related 27" lijkt op m14-cumulatief te slaan; deze interpretatie is verworpen ten gunste van m10-only conform §8 GO-criterium.

Conform Protocol 12 markering — geen masterchat-escalatie vereist (toelichting in §1 + §4 + §8 alle wijzen op m10-only-scope; alleen één getal in §1-tabel was inconsistent).

### §13.3 — Protocol v1.3-overwegingen (5 voorstellen pilot/Stap-3-leerpunten)

Niet uitgevoerd in T2; aanbevolen voor Brein-cyclus post-T2 of toekomstige m14-sprint-voorbereiding. Bronnen: pilot-rapport §7.3 + Stap 3-rapport §6:

1. **C1 "partieel"-grens verduidelijking** — wanneer telt overlap als "bilateraal" vs. "partieel"? Operationele test verfijnen
2. **C2 + subject-cluster ↔ object-cluster-prevalence expliciet** — Protocol v1.2 §2.2 cluster-test verfijnt cardinaliteit aan object-zijde; subject-zijde-cluster-effect bleek in T2-praktijk relevant voor multi-mapping-leden (5_04, 8_03)
4. **§5 confidence-criterium expliciteren** — hoog/middel/laag drempels operationaliseren
5. **Cluster-representant-keuze-criteria** — formele criteria voor representant-selectie binnen cluster (T2-praktijk: pilot-paar waar beschikbaar, anders evidence-niveau-1 + middel-cluster-positie)
6. **Werkflow-leerpunten:**
   - Bottom-up rapport-bouw als verplichte werkwijze (Protocol-aanvulling)
   - Interne tabel-consistentie-discipline tussen instructie-secties (Protocol 12-aanvulling: instructie-schrijver-zijde)
   - Helper-script-classificatie als bron-van-waarheid bij discrepantie met handmatige rapport-classificatie

### §13.4 — Brein-cyclus T2-afsluiting (Protocol 11)

Pending na masterchat-GO op dit patch-rapport. Brein-subagent in Claude Code voert uit:

**Verwachte updates in brain-vault:**
- Sprint-bestand `brain__sprints__T2-skos-bidirectional-audit-m10.md` (nieuw)
- Update `brain__sprints__sprint-register.md` (append T2-entry)
- Update `brain__decisions__D04_skos-cross-framework.md` (D4.1-toepassings-precedent + cluster-discipline-validatie op m10-scope)
- Update `brain__architecture__H36_skos-exactmatch-ctrl-compl-audit.md` (status closed voor m10; subtask m14 open)
- Update `brain__concepts__skos-beoordelings-protocol.md` (v1.2-toepassings-bewijs)
- Update `brain__concepts__mapping-bron-disclaimer-effect.md` (D4.1-toepassing op cluster-niveau)
- Update `brain__log.md` + `brain__index.md` (T2-entry + v4.6.2-baseline)

**Verwachte nieuwe concept-bestanden:**
- `brain__concepts__cluster-discipline-bewijslast.md` (uit Stap 3-leerpunt §6.5 — bewijslast-asymmetrie voor cluster-uitzondering)
- Optioneel: `brain__concepts__bidirectional-audit-symmetrie.md` (Categorie 7-bewijs upgrade/downgrade-balans)

### §13.5 — Toekomstige T-sprint-voorbereiding (m14-paren)

Buiten T2-scope (Optie C masterchat-besluit), wachtend op aparte T-sprint:

- **31 compl→ctrl skos:closeMatch in m14-avg-gdpr.ttl** — m14-modelleringsconventie hanteert compl→ctrl-richting (omgekeerd t.o.v. m10's ctrl→compl)
- **AVG-cross-walk-bron ontbreekt in `sources/`** — bron-upload of evidence-niveau-2/3-tolerantie nodig
- **compl→ctrl-richting** vereist Protocol v1.2-symmetrie-validatie (mogelijk Protocol v1.3-aanvulling)
- **Helper-script-uitbreiding** voor cross-module label-bronnen + m14-specifieke heuristieken

### §13.6 — Werkflow-leerpunten Stap 4 (Protocol v1.2 §10 categorieën)

Per instructie §9.2-focus categorieën 1, 4, 7:

**Categorie 1 (Tooling-gaten):**
- Canonical metrics-script v4.6.2 + SHACL-split-validator v4.6.2 efficient herbruikbaar uit T1-precedent (kleine versie-suffix-aanpassingen)
- SHACL-split-validator uitgebreid met expliciete SECTIE B-subset-shapes-meting (was impliciet in v4.6.1 via combined-min-SECTIE-A); meerwaarde voor toekomstige H39-shape-uitbreiding-bewijs
- Geen tooling-gap waargenomen in Stap 4

**Categorie 4 (Werkverdeling-momenten):**
- Tech-autonomie op productie-uitvoering volstaat — geen masterchat-judgement-vragen voor Stap 4-mutaties (alle 65 hadden hoge confidence via cluster-discipline)
- Protocol 17 v1.3 NEN-autonomie effectief: lokale ISO-bron-toegang voorkwam masterchat-escalatie op 10 uitzondering-screening-flags
- Instructie-inconsistentie §1 vs §8 (zie §13.2) genoteerd als werkflow-leerpunt — bron-van-waarheid-discipline (`canonical_metrics_v4_6_2.json`) volstond zonder masterchat-escalatie

**Categorie 7 (Upgrade-detectie-praktijk — Protocol v1.2 §10 nieuw):**
- Mutatie-verdeling 32 downgrade + 33 upgrade bevestigt symmetrie van Protocol v1.2 bidirectional toetsing
- Geen downgrade-bias zoals v1.1-draft had verondersteld — predicate-doel-tabel §3.1 + sterkte-ordening §3.2 zijn methodisch symmetrisch toepasbaar gebleken
- Upgrade-detectie via cluster-discipline (relatedMatch onder veel↔1-cluster naar broadMatch) is sterkste evidence-basis voor systematische upgrade-claims; per-paar individuele upgrade-claims zouden zonder cluster-context veel zwakker zijn
- Conclusie: Protocol v1.2 + cluster-discipline samen leveren methodisch-sluitende bidirectional audit

---

## §14. Sprint-prognose-evaluatie

T2-sprint-prognose per Stap 3-rapport §1.3 + instructie §1 verwachtingstabel:

| Aspect | Prognose | Werkelijk | Status |
|---|---:|---:|---|
| Mutaties in apply_patch_v4_6_2.py | 65 | **65** | ✓ exact |
| Pilot-mutaties binnen 65 | 4 | **4** | ✓ exact |
| Patch-vereist Stap 3 resterend | 61 | **61** | ✓ exact |
| Backup-file aangemaakt | ja | ja | ✓ |
| Post-patch m10 broadMatch | 118 | **118** | ✓ exact |
| Post-patch m10 close/related/exact/narrow | 0 / 0 / 0 / 0 | **0 / 0 / 0 / 0** | ✓ exact |
| Canonical metrics-Δ triples | 0 (±5 OWL-RL) | 0 / 0 | ✓ binnen tolerantie |
| SHACL SECTIE A violations | 0 | 0 | ✓ |
| SHACL SECTIE B violations | 0 | 0 | ✓ |
| SHACL COMBINED violations | 290 (identiek baseline) | 290 (Δ 0) | ✓ |
| m10-hash gewijzigd | ja, ≠ cb2d567b | ja, `a4bfdc12…` | ✓ |
| 21 andere modules + grc-shacl hash-identiek | ja | ja | ✓ |
| Stop-condities geraakt | 0 | 0 | ✓ |
| NEN-aantoonbare uitzonderingen | 0 | 0 | ✓ |
| Cluster-discipline-consistentie | 100% | 100% | ✓ |

**Sprint-prognose volledig geklopt op alle 14 metrics.** Geen afwijking, geen onverwachte uitkomst, geen scope-pauze-trigger geraakt tijdens Stap 4.

Tijdsraming-evaluatie (per instructie §12):

| Stap | Raming | Werkelijk Tech | Δ |
|---|---:|---:|---:|
| A: pre-patch baseline | ~5 min | ~5 min | conform |
| B: applier productie-run | ~10 min | ~5 min | onder raming |
| C: canonical metrics | ~30 min | ~10 min (T1-precedent-hergebruik) | onder raming |
| D: SHACL split-validatie | ~30 min | ~15 min (incl. SECTIE B-subset-toevoeging) | onder raming |
| E: file-hashes | ~5 min | ~2 min | onder raming |
| F: patch-rapport bottom-up | ~1,5 uur | ~1 uur | onder raming |

T1-precedent-hergebruik (canonical metrics + SHACL-scripts) leverde substantiële tijdsbesparing op verificatie-fase.

---

## §15. GO-criteria-checklist (instructie §8)

| # | Criterium | Drempel | Werkelijk | Status |
|---|---|---|---|---|
| 1 | Applier productie-run succesvol | 65/65 mutaties zonder fouten | 65/65 OK, 0 NOT FOUND, 0 ambigu | ✓ |
| 2 | Backup-file aanwezig | `m10-nis2-ext.ttl.v4_6_1.bak` bestaat | aanwezig (80.429 bytes) | ✓ |
| 3 | m10 SKOS-counts post-patch | exact 0 / close 0 / broad 118 / narrow 0 / related 0 | 0 / 0 / 118 / 0 / 0 | ✓ |
| 4 | Canonical metrics totaal-triples | ±0 t.o.v. v4.6.1 (20.950) | 20.950 (Δ 0) | ✓ |
| 5 | Canonical metrics post-OWL-RL | ±5 t.o.v. v4.6.1 (44.907) | 44.907 (Δ 0) | ✓ |
| 6 | Klassen / Individuals / OP / DP | identiek (199 / 1.383 / 149 / 96) | 199 / 1.383 / 149 / 96 | ✓ |
| 7 | SHACL SECTIE A | 0 violations | 0 | ✓ |
| 8 | SHACL SECTIE B | 0 violations | 0 | ✓ |
| 9 | SHACL COMBINED | 290 (identiek v4.6.1) | 290 (Δ 0) | ✓ |
| 10 | File-hash m10 | nieuwe sha256 ≠ `cb2d567b…` | `a4bfdc12cedb0c5018218a77480393e40fd301dddcd438abb31a84300a3dd44e` | ✓ |
| 11 | File-hashes overige 21 modules + grc-shacl | identiek aan v4.6.1 | identiek (diff: alleen m10) | ✓ |
| 12 | Patch-rapport §0-§13 compleet | alle secties ingevuld | §0-§15 compleet | ✓ |
| 13 | Pre-push disclosure-check Protocol 14 | 5 categorieën pass | (1) geen organisatie-naam (2) geen persoonsnamen anders dan Steven (3) geen lokale paden buiten `/Users/stevenbouwmeester/grc-kennismodel/` + NEN-licentie-pad (4) geen credentials/TLD/e-mail (5) geen verbatim NEN-tekst >10 woorden | ✓ |

**Alle 13 GO-criteria groen.** Tech-eindoordeel: T2-sprint-deliverables klaar voor masterchat-review en handmatige commit + push door Steven.

— Einde patch-rapport v4.6.2.
