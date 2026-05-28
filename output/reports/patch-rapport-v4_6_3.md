---
type: report
subtype: patch-rapport
version: v4.6.3
baseline_from: v4.6.2
baseline_to: v4.6.3
sprint: T3
date: 2026-05-28
status: final-awaiting-masterchat-review
related:
  - skos-beoordelings-protocol-v1_3
  - H36_skos-exactmatch-ctrl-compl-audit
  - D04_skos-cross-framework
  - t3-pre-sprint-inventarisatie
  - t3-pilot-rapport
  - t3-stap3-eindrapport
  - patch-rapport-v4_6_2
scope: "Patch v4.6.3 — T3-sprint SKOS-bidirectional-audit m14. 2 SKOS-predicate-substituties in m14-avg-gdpr.ttl (T3-001 + T3-002, beide compl:AVG_Art5_1f broadMatch → relatedMatch op ctrl:ISO27002_5_01 respectievelijk ctrl:ISO27002_5_12). Cluster-discipline: Art5_1f-cluster (7 leden) wordt homogeen relatedMatch post-patch. Masterchat-besluit Optie C (cross-category-rationale: control ↔ legal-obligation = associatief, niet subsumptief). Geen TBox-wijziging. Geen andere modules dan m14-avg-gdpr.ttl."
---

> **Errata 2026-05-28 (post-masterchat-sign-off v4.6.3, Brein-cyclus iteratie 15):**
>
> §6.4 confidence-tabel: correctie cumulatief m14 van "26 hoog / 5 middel" naar **27 hoog / 4 middel / 0 laag**. T3-002 verschuift van middel naar **hoog** (analoog T3-001 — masterchat-besluit Optie C heeft de methode-vraag definitief opgelost; geen openstaande methode-twijfel meer per paar). De vier resterende middel-paren zijn: **T3-014, T3-026, T3-028, T3-030**.
>
> Surgische correctie conform Protocol v1.3 §10.4 (T-historie bewaard; alleen classificatie-kolommen aangepast). Patch-impact (m14-ttl-state + canonical metrics + SHACL) onveranderd. Per-paar-tabel in T3 Stap 3-eindrapport §6.1 blijft bron-van-waarheid.

# Patch-rapport v4.6.3

## §0. Versie + metrics-vergelijking

Cijfers in dit rapport komen uit `output/verification/canonical_metrics_v4_6_3.json` (gemeten op de gepatchte versie van de ontologie). **Niet uit memorie** (sprint-Protocol §18-discipline, v4.3.3-leerpunt; v4.6.2-precedent).

### §0.1 Vergelijking v4.6.2 → v4.6.3

| Metric | v4.6.2 | v4.6.3 | Δ |
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
| skos:closeMatch | 1.457 | 1.457 | 0 |
| skos:broadMatch | 131 | **129** | **−2** |
| skos:narrowMatch | 0 | 0 | 0 |
| skos:relatedMatch | 192 | **194** | **+2** |
| rdfs:label totaal | 3.827 | 3.827 | 0 |
| rdfs:comment totaal | 1.760 | 1.760 | 0 |
| owl:Nothing post-inferentie | 0 | 0 | 0 (consistent) |
| D5 ctrl↔bio sameAs | 93 | 93 | 0 (conform) |
| D11 asset-brug | 5 | 5 | 0 (conform) |
| D8 SoAEntry | 93 | 93 | 0 |
| ext:hasHandreikingBBN assertions | 241 | 241 | 0 |

**Kernobservatie:** triple-totaal en alle individuals/klassen/property-tellingen zijn ongewijzigd. Enige mutatie is predicate-name voor 2 specifieke triples in m14-avg-gdpr.ttl (broadMatch → relatedMatch). SKOS-mappings-totaal blijft 1.798 (predicate-substitutie binnen behouden totaal; geen toevoeging, geen verwijdering). broadMatch globaal van 131 naar 129 (−2); relatedMatch globaal van 192 naar 194 (+2) — exact zoals voorspeld in instructie.

### §0.2 compl→ctrl SKOS-paren-mutatie (m14-scope)

| Pair-type | v4.6.2 | v4.6.3 | Δ |
|---|---:|---:|---:|
| `compl->ctrl::exactMatch` | 0 | 0 | 0 |
| `compl->ctrl::closeMatch` | 2 | 2 | 0 |
| `compl->ctrl::broadMatch` | 2 | **0** | **−2** |
| `compl->ctrl::narrowMatch` | 0 | 0 | 0 |
| `compl->ctrl::relatedMatch` | 27 | **29** | **+2** |
| **Totaal compl→ctrl m14** | **31** | **31** | **0** |

Beide compl:AVG_Art5_1f → ctrl:ISO27002_*-broadMatch-paren convergeren post-patch naar `skos:relatedMatch`, conform masterchat-besluit Optie C (cross-category-rationale toegepast op Art5_1f-cluster). Zie §6 voor cluster-tabel en T3 Stap 3-eindrapport voor per-paar-onderbouwing.

### §0.3 File-hash-mutatie

| Bestand | v4.6.2 SHA256 | v4.6.3 SHA256 | Wijziging? |
|---|---|---|---|
| m14-avg-gdpr.ttl | `47daeb7e…51d353` | `874565ba…e1864` | **ja** |
| Andere 21 .ttl + grc-shacl.ttl | (zie file_hashes_v4_6_2.txt) | identiek | **nee** |

Volledige file-hash-lijst: `output/verification/file_hashes_v4_6_3.txt`. Vergelijking `diff file_hashes_v4_6_2.txt file_hashes_v4_6_3.txt` toont uitsluitend de m14-hash-mutatie; alle 22 andere bestanden hash-identiek.

---

## §1. Aanleiding

T3-sprint (SKOS-kwaliteitsanalyse Fase 3 — bidirectional audit compl:↔ctrl: in m14-avg-gdpr.ttl) is in drie stappen uitgevoerd:

1. **Stap 1** (pre-sprint-inventarisatie) — 31 compl→ctrl m14-paren bevestigd; ABox-baseline + cluster-cardinaliteit per AVG-artikel vastgelegd; ISO 27701:2025 Annex D-evidence-coverage gemeten (10 niveau-1 / 7 niveau-2 / 14 niveau-3 paren); Protocol v1.3 vastgesteld
2. **Stap 2** (pilot 6 paren) — Protocol v1.3 toegepast op cluster-representanten over alle 5 AVG-clusters; 0 patch-mutaties bevestigd in pilot (read-only); SKOS broadMatch-richtings-bevinding op Art5_1f-cluster (T3-002) als methode-vraag aan masterchat geëscaleerd (pilot §5.2: Opties A/B/C)
3. **Stap 3** (hoofd-uitvoering 25 resterende paren + cumulatief m14-overzicht + patch + verificatie + rapport — dit rapport) — masterchat-besluit Optie C op pilot-escalatie toegepast (broadMatch → relatedMatch op Art5_1f-cluster, n=2); 24 overige Stap-3-paren behoud; closeMatch-toets T3-026 verdedigbaar behouden analoog T3-014 pilot; 2 mutaties via `apply_patch_v4_6_3.py --apply`; canonical metrics + SHACL split-validatie + file-hashes

**Cross-category-rationale (T3-leerpunt voor v1.3.1-Brein-cyclus):** alle 31 m14-paren bevestigen empirisch dat control ↔ legal-obligation een cross-category-relatie is die inherent associatief (relatedMatch) is, niet subsumptief (broad/narrowMatch). Cluster-doel-default per Protocol §3.1 rij 7 (narrowMatch in 1↔veel-subject-cluster) is systematisch overstemd door C3-falen op cross-category-niveau. closeMatch (2 m14-paren: T3-014 Art32→5.01 + T3-026 Art33→5.24) is verdedigbaar op retrieval-interchangeability binnen specifieke domeinen (governance/policy respectievelijk incident-planning). Status: niet nu formaliseren in Protocol-tekst (Tech-subagent voert geen autonome Protocol-wijziging uit); kandidaat-precedent voor Brein-cyclus.

**Bron-erf:** evidence-coverage gemeten via ISO 27701:2025 Annex D + Annex F twee-staps-keten — 10 paren niveau-1, 7 paren niveau-2, 14 paren niveau-3 (zie pre-sprint-inventarisatie §5.1). 27701:2025 Annex D is non-exhaustive — keten-evidence levert bestaans-bewijs voor relatie, niet predicate-type-bewijs. Predicate-type-keuze verliep via C1+C3+cross-category-rationale.

**D4-rationale:** herclassificatie van T3-001 + T3-002 binnen Art5_1f-cluster is D4-conform:

- C2 1↔veel-cluster-cardinaliteit op Art5_1f-cluster (subject-cluster-grootte 7); cluster-doel per Protocol §3.1 rij 7 zou narrowMatch zijn, maar wordt op cross-category-basis overstemd
- D4.1-disclaimer afwezig (AVG = publiek EU-recht; geen non-equivalence-disclaimer in evidence-stack)
- Bilaterale containment afwezig op alle paren (ctrl:5.01 + 5.12 zijn implementatie-controls, Art. 5(1)(f) is brede juridische verplichting — geen conceptuele subsumptie)
- SKOS broadMatch-richtings-semantiek (`A skos:broadMatch B` ≡ B is broader than A) was omgekeerd geclaimd in oorspronkelijke m14-modellering; relatedMatch (symmetrisch) lost de richtings-kwestie definitief op

---

## §2. Scope

**Wat wijzigt:**

- 2 compl:AVG_Art5_1f → ctrl:ISO27002_5_01 + ctrl:ISO27002_5_12 skos:broadMatch-triples → skos:relatedMatch (downgrades per Protocol v1.3 §3.2)
- Totaal: **2 predicate-substituties** in `ontology/m14-avg-gdpr.ttl`
- Geen TBox-wijziging (geen klasse, property, restrictie, axiom toegevoegd of verwijderd)
- Geen wijziging in m02-control.ttl, m05-compliance.ttl, of enige andere module
- Geen wijziging in SHACL-shapes (grc-shacl.ttl onveranderd)

**Wat NIET wijzigt:**

- D5 (ctrl↔bio sameAs 93) — onveranderd
- D11 (asset-brug 5) — onveranderd
- 5 compl:AVG_Art*-individuals (Art5_1f, Art25, Art32, Art33, Art34) — onveranderd (geen wijziging in rdfs:label, compl:articleRef, compl:derivedFrom, of andere properties)
- SoA-structuur (D8, 93 SoAEntries) — onveranderd
- Bestaande 27 compl→ctrl skos:relatedMatch-triples (uit v4.6.2-baseline) — onveranderd
- 2 compl→ctrl skos:closeMatch-triples (T3-014 Art32→5.01 + T3-026 Art33→5.24) — behouden post-toets
- 21 niet-pilot-Stap-3-relatedMatch-paren — behouden
- Framework-niveau SKOS-triples in m14 (fw:AVG_GDPR → fw:ISO_IEC_27001_2022 / fw:BIO_2_0) — buiten T3-scope, onveranderd
- m10-broadMatch (ctrl→compl-richting) — niet retroactief geheraudit (formeel correct in andere richting; geen scope-uitbreiding)

**Eindstand m14 compl→ctrl SKOS-distributie post-patch:** exact 0 / close 2 / broad 0 / narrow 0 / related 29.

**Bron:** T3-sprint Stap 2 pilot-rapport + T3-sprint Stap 3 eindrapport (beide in `output/reports/`).

---

## §3. Wijzigingen in m14-avg-gdpr.ttl

### §3.1 Beschrijving

Twee regels in m14-avg-gdpr.ttl van de vorm:

```turtle
compl:AVG_Art5_1f
    skos:broadMatch ctrl:ISO27002_5_01 ;    # Beleidsregels IB
    skos:broadMatch ctrl:ISO27002_5_12 ;    # Classificeren informatie
    skos:relatedMatch ctrl:ISO27002_5_15 ;  # ... (rest van het blok ongewijzigd)
```

worden vervangen door:

```turtle
compl:AVG_Art5_1f
    skos:relatedMatch ctrl:ISO27002_5_01 ;    # Beleidsregels IB
    skos:relatedMatch ctrl:ISO27002_5_12 ;    # Classificeren informatie
    skos:relatedMatch ctrl:ISO27002_5_15 ;  # ... (rest van het blok ongewijzigd)
```

Geen andere wijziging aan het blok. Comments (`# Beleidsregels IB`, `# Classificeren informatie`), witregels en alle andere triples in het Art5_1f-cluster (5 relatedMatch-paren naar ctrl:5.15, 8.24, 8.10, 8.11, 8.12) blijven onveranderd. Andere AVG-clusters (Art25, Art32, Art33, Art34) blijven volledig onveranderd.

### §3.2 Mutatie-uitvoering — applier-output

Productie-run van `apply_patch_v4_6_3.py --apply` (script in `scripts/apply_patch_v4_6_3.py`, dry-run + productie-modus):

```
apply_patch_v4_6_3.py — modus: PRODUCTIE
Doel TTL: ontology/m14-avg-gdpr.ttl

Patch-vereiste mutaties totaal: 2

Per mutatie-richting:
  downgrade               :   2

Pre-patch m14 skos-predicate counts (m14-only):
  skos:exactMatch    :   0
  skos:closeMatch    :   2
  skos:broadMatch    :   2
  skos:narrowMatch   :   0
  skos:relatedMatch  :  29

Mutatie-toepassing-detail:
  OK  [T3-001] compl:AVG_Art5_1f    skos:broadMatch    -> skos:relatedMatch  ctrl:ISO27002_5_01
  OK  [T3-002] compl:AVG_Art5_1f    skos:broadMatch    -> skos:relatedMatch  ctrl:ISO27002_5_12

Toegepast: 2 / 2

Post-patch m14 skos-predicate counts (verwacht):
  skos:exactMatch    :   0  (Δ 0)
  skos:closeMatch    :   2  (Δ 0)
  skos:broadMatch    :   0  (Δ -2)
  skos:narrowMatch   :   0  (Δ 0)
  skos:relatedMatch  :  31  (Δ +2)

Backup gemaakt: ontology/m14-avg-gdpr.ttl.v4_6_2.bak
Patch v4.6.3 toegepast op ontology/m14-avg-gdpr.ttl
```

**Sanity-check (totaal SKOS-predicates in m14-bestand):** pre-patch 33 = post-patch 33 ✓ (alleen herclassificatie, geen toevoeging of verlies). Let op: m14-bestand telt 33 SKOS-mappings totaal (29 relatedMatch + 2 closeMatch + 2 broadMatch pre-patch; 31 relatedMatch + 2 closeMatch post-patch in raw bestand-tekst — inclusief de 2 framework-niveau fw:AVG_GDPR skos:relatedMatch fw:... triples uit Sectie 4 van het bestand. Het overzicht in §0.2 telt alleen compl→ctrl-paren (31 stuks, in scope T3). De 2 framework-niveau-triples vallen buiten T3-scope en blijven onveranderd.

### §3.3 Pre/post-hash m14-avg-gdpr.ttl

| Versie | SHA256 |
|---|---|
| v4.6.2 (pre-patch) | `47daeb7e6f37080b5f88b6d4d594a0401e5f1e32356d330d9cbc0b287251d353` |
| v4.6.3 (post-patch) | `874565bade04c1657841298d4b035fa9c7f06f46a8d76ce9efba8ecfb35e1864` |

Backup-file aanwezig: `ontology/m14-avg-gdpr.ttl.v4_6_2.bak`. Bevat exacte v4.6.2-staat voor rollback-mogelijkheid.

---

## §4. Triples-impact + per-metric Δ-tabel

### §4.1 Globale triples

| Aspect | v4.6.2 | v4.6.3 | Δ |
|---|---:|---:|---:|
| Pre-inference triples | 20.950 | 20.950 | **0** |
| Post-inference (OWL RL) triples | 44.907 | 44.907 | **0** |
| owl:Nothing post-inferentie | 0 | 0 | 0 |

**Verklaring Δ=0 op triple-niveau:** SKOS-predicate-substitutie binnen één blok wijzigt geen triple-aantal — de mutatie vervangt een triple `(s, skos:broadMatch, o)` door `(s, skos:relatedMatch, o)`. Beide tellen als één triple. Geen toevoeging, geen verwijdering. Post-OWL-RL-inferentie is eveneens stabiel omdat owlrl in deze configuratie geen SKOS-axiomas laadt (bekende beperking gedocumenteerd in v4.6.1-rapport §5.2 + v4.6.2-rapport §4.1). Predicate-naamverandering raakt geen RDFS/OWL-inferentie-pad.

### §4.2 SKOS-breakdown-Δ

| Predicate | v4.6.2 | v4.6.3 | Δ | Verklaring |
|---|---:|---:|---:|---|
| skos:exactMatch | 18 | 18 | 0 | Geen exactMatch-paren in T3-scope; m14 had reeds 0 exactMatch |
| skos:closeMatch | 1.457 | 1.457 | 0 | m14 closeMatch behouden (T3-014 + T3-026 post-toets behoud) |
| skos:broadMatch | 131 | 129 | **−2** | 2 m14-paren (T3-001 + T3-002) van broadMatch naar relatedMatch |
| skos:narrowMatch | 0 | 0 | 0 | Geen narrowMatch in model (cross-category-rationale blokkeert in m14) |
| skos:relatedMatch | 192 | 194 | **+2** | 2 ex-broadMatch uit m14 Art5_1f-cluster naar relatedMatch |
| **Totaal** | **1.798** | **1.798** | **0** | Predicate-substitutie binnen behouden totaal |

### §4.3 Stop-condities canonical metrics

| # | Conditie | Drempel | Stand | Status |
|---|---|---|---|---|
| 1 | Pre-inference triples-Δ | ±0 | 0 | **niet geraakt** |
| 2 | Post-inference triples-Δ | ±5 | 0 | **niet geraakt** |
| 3 | Klassen/Individuals/OP/DP-Δ | exact 0 | alle 0 | **niet geraakt** |
| 4 | owl:Nothing post-inf | 0 | 0 | **niet geraakt** |
| 5 | SKOS-mapping-totaal-Δ | ±0 | 0 | **niet geraakt** |

Geen stop-conditie geraakt. Mutaties conform raming (instructie-§ "Verwachte uitkomst": broadMatch −2 → 129, relatedMatch +2 → 194).

---

## §5. Klassen / Individuals / Properties-impact

| Aspect | v4.6.2 | v4.6.3 | Δ |
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

| Check | v4.6.2 | v4.6.3 |
|---|---:|---:|
| GRC-subjects zonder type | 0 | 0 |
| Object-properties zonder domain | 0 | 0 |
| Object-properties zonder range | 0 | 0 |
| Datatype-properties zonder domain | 0 | 0 |
| Datatype-properties zonder range | 0 | 0 |
| Dangling GRC references | 3 | 3 (identieke set; bekende baseline) |
| Duplicate owl:Class declarations | 0 | 0 |
| Namespace leakage | 22 | 22 (identieke set; bekende baseline) |

Geen integriteits-regressie. Identieke baseline aan v4.6.2.

---

## §6. SKOS-mappings paar-uitkomsten + per-cluster-tabel

### §6.1 Pre/post-distributie compl→ctrl:AVG_Art*-clusters (m14-scope)

| Cluster | Cluster-grootte | v4.6.2 close | v4.6.2 broad | v4.6.2 related | v4.6.3 close | v4.6.3 broad | v4.6.3 related | Heterogeniteit |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| AVG_Art5_1f | 7 | 0 | 2 | 5 | 0 | **0** | **7** | **van heterogeen naar homogeen** |
| AVG_Art25 | 6 | 0 | 0 | 6 | 0 | 0 | 6 | ongewijzigd homogeen |
| AVG_Art32 | 12 | 1 | 0 | 11 | 1 | 0 | 11 | ongewijzigd heterogeen |
| AVG_Art33 | 4 | 1 | 0 | 3 | 1 | 0 | 3 | ongewijzigd heterogeen |
| AVG_Art34 | 2 | 0 | 0 | 2 | 0 | 0 | 2 | ongewijzigd homogeen |
| **Totaal** | **31** | **2** | **2** | **27** | **2** | **0** | **29** | **broadMatch geëlimineerd** |

**Cluster-doel-predicate-uitkomst:** geen cluster convergeert naar Protocol §3.1 rij 7 cluster-default `narrowMatch` (cross-category-rationale blokkeert). Twee paren uit Art5_1f-cluster waar broadMatch was geclaimd, zijn naar relatedMatch verschoven (masterchat-besluit Optie C). Cluster Art5_1f wordt daarmee homogeen relatedMatch×7. closeMatch wordt behouden op 2 paren (Art32→5.01 governance/policy + Art33→5.24 incident-planning), beide verdedigd op retrieval-interchangeability binnen specifieke domeinen.

### §6.2 Mutatie-richting-verdeling

| Richting | Aantal | % van totaal m14-mutaties |
|---|---:|---:|
| Downgrade (broadMatch → relatedMatch) | **2** | 100,0% |
| Upgrade | 0 | 0% |
| Richtings-correctie (broad ↔ narrow) | 0 | 0% |
| Verwijdering | 0 | 0% |
| Behoud | 29 | n.v.t. (geen mutatie) |
| Twijfel/escalatie | 0 | 0% |

**Mutatie-context:** beide mutaties zijn directe instructie-uitvoering op masterchat-besluit (pilot-escalatie Optie C). Geen autonome Tech-bevindingen onder de 25 Stap-3-paren — alle 24 niet-besluit-paren krijgen behoud-classificatie via cross-category-rationale.

### §6.3 Per-paar-uitkomst-tabel cumulatief m14 (pilot 6 + Stap 3 25 = 31)

Volledige tabel: zie T3 Stap 3-eindrapport §6.1. Samenvattend per paar-type:

| Paar-categorie | Aantal | Paren | Uitkomst |
|---|---:|---|---|
| Mutatie (broadMatch → relatedMatch) | 2 | T3-001 + T3-002 | masterchat-besluit Optie C |
| Behoud relatedMatch (uit cross-category-rationale) | 27 | T3-003 t/m T3-013, T3-015 t/m T3-023, T3-024, T3-025, T3-027, T3-028, T3-029, T3-030, T3-031 | per-paar cross-category-rationale; cluster-conform |
| Behoud closeMatch (uit retrieval-interchangeability-uitzondering) | 2 | T3-014 (Art32→5.01) + T3-026 (Art33→5.24) | per-paar closeMatch-toets verdedigbaar |
| Behoud broadMatch | 0 | — | broadMatch geëlimineerd in m14 |

### §6.4 Confidence-verdeling cumulatief m14

| Confidence | Aantal | Paren |
|---|---:|---|
| Hoog | 27 | 4 pilot (T3-024, T3-008, T3-031, T3-002) + 23 Stap 3 (alle behalve T3-026 + T3-030) |
| Middel | 4 | T3-014 (pilot, closeMatch-toets), T3-028 (pilot, scope-asymmetrie), T3-026 (Stap 3, closeMatch-toets analoog T3-014), T3-030 (Stap 3, scope-asymmetrie analoog T3-028) |
| Laag | 0 | — |

**Bron-van-waarheid:** T3 Stap 3-eindrapport §6.1 per-paar-classificatie (Protocol v1.3 §10.4 — per-paar-classificatie autoritatief boven aggregatie-tabellen). Geen helper-script in T3 gebruikt (handmatige scope). T3-002 telt als hoog conform per-paar-classificatie: post-masterchat-besluit Optie C is de methode-vraag opgelost en T3-002-confidence analoog aan T3-001 (zie errata-aantekening bovenaan).

---

## §7. SHACL-validatie-uitkomsten

Script: `output/verification/shacl_split_validate_v4_6_3.py`
Output: `output/verification/shacl_results_v4_6_3.json`

### §7.1 Drie metingen (split-validatie conform sprint-protocol)

| Meting | Inference | Shapes | Verwacht | Werkelijk | Status |
|---|---|---|---:|---:|---|
| SECTIE A | none | ctrl/bio ISO27002NamingShape, HandreikingBBNValueShape, asset:NamespaceShape | 0 | **0** | ✓ |
| SECTIE B | owlrl | AppliesToAssetTypeRangeShape, BVASymmetryShape, OrphanClassShape | 0 | **0** | ✓ |
| COMBINED | owlrl | alle 7 shapes | 290 | **290** | ✓ (identiek v4.6.2) |

### §7.2 COMBINED-meting-detail

Per source-shape in COMBINED-meting:

| Shape | Violations | Type |
|---|---:|---|
| `https://grc.example.org/asset/NamespaceShape` | 104 | bekende false-positive (OWL-RL-typing-artefact) |
| `https://grc.example.org/bio/ISO27002NamingShape` | 93 | bekende false-positive (OWL-RL-typing-artefact) |
| `https://grc.example.org/control/ISO27002NamingShape` | 93 | bekende false-positive (OWL-RL-typing-artefact) |
| **Totaal** | **290** | identiek aan v4.6.2 |

**Δ vs v4.6.2 baseline: 0 violations.** Geen nieuwe violations geïntroduceerd; geen bestaande violations opgelost door SKOS-predicate-substitutie.

### §7.3 SHACL-blinde-vlek bevestiging

Geen shape in `ontology/grc-shacl.ttl` valideert direct op compl:↔ctrl:-mapping-distributie (T1 Vraag D-inventarisatie + T2 §3.2 stop-conditie-analyse + T3 pre-sprint-inventarisatie §8.4). De 2 SKOS-predicate-substituties raken daarom geen shape — SHACL-uitkomsten zijn structureel ongevoelig voor T3-mutaties. H39 (SHACL-blinde vlek) blijft active geparkeerd voor latere shape-uitbreiding indien gewenst. T3 bevestigt H39-trigger-relevantie opnieuw voor zowel ctrl→compl (m10) als compl→ctrl (m14)-richting.

### §7.4 Stop-condities SHACL

| Type | Drempel | Stand | Status |
|---|---|---|---|
| SECTIE A violations | >0 | 0 | **niet geraakt** |
| SECTIE B violations | >0 | 0 | **niet geraakt** |
| COMBINED Δ vs baseline | >0 of <0 | 0 | **niet geraakt** |

Geen stop-conditie geraakt. SHACL-uitkomsten regressie-vrij.

---

## §8. Sprint-multiplier + sprint-precedent-vergelijking

| Aspect | T3 (v4.6.3) | T2 (v4.6.2) | T1 (v4.6.1) | Verhouding T3:T2:T1 |
|---|---:|---:|---:|---:|
| Triple-Δ pre-inferentie | 0 | 0 | 0 | identiek |
| Triple-Δ post-OWL-RL | 0 | 0 | 0 | identiek |
| Aantal SKOS-mutaties | **2** | 65 | 28 | 0,03× / 0,07× |
| Mutatie-richtingen | downgrade-only (broad → related, cross-category) | upgrade + downgrade (bidirectional) | downgrade-only (exact → close) | smal mutatie-spectrum |
| Gewijzigde modules | 1 (m14) | 1 (m10) | 1 (m10) | identiek (m-niveau) |
| Scope | m14 compl→ctrl (31 paren) | m10 ctrl→compl (118 paren) | m10 ctrl→compl exactMatch (28 paren) | scope-reductie t.o.v. T2 |
| Protocol-versie | v1.3 | v1.2 | v1.0 | protocol-progressie |
| Pilot-omvang | 6 paren | 8 paren | 5 paren | binnen Protocol §6-richtlijn |
| Helper-tooling | n.v.t. (handmatige scope) | cluster-overerving-helper + heuristiek-screening | n.v.t. | T3 onder helper-drempel |
| NEN-werkverdeling | Tech-autonomie (Protocol 17 v1.3 + lokale ISO 27701:2025 + 27002:2022) | Tech-autonomie | masterchat-toets (Protocol 17 pre-herziening) | Tech-autonomie stabiel |
| Bron-stack | 27701:2025 Annex D + Annex F (twee-staps-keten) + 27002:2022 + AVG-publiek | CBW-Excel (Mapping UV/ENISA TIG) + 27002:2022 + NIS2-publiek | ENISA-TIG-disclaimer-detectie + 27002:2022 + NIS2-publiek | nieuw evidence-pad voor T3 |
| Cross-category-mappings | ja (control ↔ legal-obligation) | nee (control ↔ control-eis) | nee (control ↔ control-claim) | nieuwe categorie T3 |

**Sprint-multiplier:** T3 verwerkt 0,03× het aantal mutaties van T2 (2 vs 65). Het geringe mutatie-aantal komt door:

1. **Cross-category-rationale-stabilisatie**: alle 27 v4.6.2-relatedMatch-paren in m14 zijn cluster-conform onder de cross-category-basislijn. Geen upgrade-druk vanuit cluster-discipline-default omdat §3.1 rij 7 (narrowMatch) categorie-foutief zou zijn
2. **Pilot-effectiviteit**: pilot 6 paren detecteerde de SKOS-richtings-anomalie in Art5_1f-broadMatch-cluster vroegtijdig en escaleerde naar masterchat. Masterchat-besluit Optie C operationaliseerde de mutatie-richting voor zowel pilot-paar T3-002 als zuster-paar T3-001 (Stap 3) zonder dat Stap 3-Tech-werk autonoom hoefde te beslissen
3. **closeMatch-uitzondering-discipline**: 2 closeMatch-paren behouden onder verdedigbare retrieval-interchangeability-toets (T3-014 + T3-026); geen NEN-aantoonbare downgrade-grond op deze paren

**Methodologische uitkomst T3:** smal mutatie-spectrum maar **breed methodisch leerpunt** (cross-category-principe als kandidaat v1.3.1-precedent — zie §13).

---

## §9. Deliverables-tabel (Protocol 16 verplicht)

Expliciete relatieve lokaties vanaf repo-root van alle T3-deliverables.

### §9.1 Productie-scripts + outputs

| Deliverable | Pad | Type |
|---|---|---|
| Patch-applier (productie + dry-run) | `scripts/apply_patch_v4_6_3.py` | script |

Geen helper-script in T3 (handmatige scope; 25 paren onder helper-drempel).

### §9.2 Verificatie-scripts + outputs

| Deliverable | Pad | Type |
|---|---|---|
| Canonical metrics-script | `output/verification/canonical_metrics_v4_6_3.py` | script |
| Canonical metrics-output | `output/verification/canonical_metrics_v4_6_3.json` | output |
| SHACL split-validatie-script | `output/verification/shacl_split_validate_v4_6_3.py` | script |
| SHACL-validatie-output | `output/verification/shacl_results_v4_6_3.json` | output |
| File-hashes | `output/verification/file_hashes_v4_6_3.txt` | output |

### §9.3 Rapporten

| Deliverable | Pad | Type |
|---|---|---|
| Pre-sprint-inventarisatie (Stap 1) | `output/reports/t3-pre-sprint-inventarisatie.md` | rapport |
| Pilot-rapport (Stap 2) | `output/reports/t3-pilot-rapport.md` | rapport |
| Stap 3-eindrapport | `output/reports/t3-stap3-eindrapport.md` | rapport |
| Patch-rapport v4.6.3 (dit rapport) | `output/reports/patch-rapport-v4_6_3.md` | rapport |

### §9.4 Backup + sprint-instructies

| Deliverable | Pad | Type |
|---|---|---|
| Backup pre-patch | `ontology/m14-avg-gdpr.ttl.v4_6_2.bak` | backup |
| Sprint-instructies | `docs/instructies/instructie-t3-pre-sprint-inventarisatie.md` + `instructie-t3-pilot.md` + `instructie-t3-stap3.md` | instructies |
| Protocol-bestand | `docs/skos-beoordelings-protocol-v1_3.md` | protocol |

**Bevestiging:** alleen `ontology/m14-avg-gdpr.ttl` gewijzigd. Alle andere 21 .ttl-modules + `grc-shacl.ttl` byte-identiek aan v4.6.2 (zie `output/verification/file_hashes_v4_6_3.txt`).

---

## §10. Sprint-protocollen — geactiveerd / aangepast

### §10.1 Geactiveerde protocollen (uit `docs/sprint-protocols.md` v1.3)

| Protocol | Toepassing in T3 |
|---|---|
| Protocol 1 (Pre-sprint-inventarisatie) | Stap 1 — 31 m14-paren bevestigd; ABox-baseline + cluster-cardinaliteit per AVG-artikel + ISO 27701:2025 Annex D-evidence-coverage |
| Protocol 4 (Bron-verificatie vóór TBox) | n.v.t. — geen nieuwe property/klasse in T3 |
| Protocol 7 (Bron-bereikbaarheid) | Lokale NEN-bron-toegang `/Users/stevenbouwmeester/grc-sources-licensed/` getoetst (Protocol 17 v1.3); 27701:2025 + 27002:2022 + 29100:2011 leesbaar |
| Protocol 10 (Patch-rapport §9 geparkeerd-items) | §11 dit rapport |
| Protocol 12 (Instructie-consistentie code vs toelichting) | Geen inconsistentie tegengekomen in T3-instructie-tekst; instructie-§ "Verwachte uitkomst" sluit aan op canonical-metrics-uitkomst |
| Protocol 14 (Pre-push disclosure-check) | 5 categorieën gescand op alle T3-Stap-3-deliverables — geen vondsten |
| Protocol 15 (Tech levert werkbare applier) | `scripts/apply_patch_v4_6_3.py` geleverd (dry-run + productie); 2 mutaties via productie-run |
| Protocol 16 (Deliverables-tabel expliciet) | §9 dit rapport |
| Protocol 17 v1.3 (NEN-werkverdeling Tech-autonomie) | Lokale ISO 27002:2022 + 27701:2025-tekst-lezing voor C1+C3-toetsing op 31 paren; parafrase-discipline gehandhaafd |

### §10.2 Niet-geactiveerde protocollen

| Protocol | Reden |
|---|---|
| Protocol 5/6/9 (raming-discipline) | Sprint-doel was kwaliteitsanalyse, geen ABox-creatie; triple-Δ-raming = 0 (predicate-substitutie) |
| Protocol 8 (Precedent-discipline framework-cluster) | Geen nieuw cluster — m14-AVG-cluster bestond reeds in baseline |
| Protocol 11 (Brain-vault-update) | Brein-cyclus volgt na masterchat-GO op dit patch-rapport — buiten Tech-scope |
| Protocol 13 (Bron-typo-beleid) | Geen typo's tegengekomen in m14-mutaties (mutaties beperkt tot predicate-substitutie) |
| Protocol 16 (Sample-first) | Sample-first toegepast als pilot 6 paren (Stap 2); volledige scope (25 resterend) in Stap 3 binnen handmatige discipline; geen sample-first opnieuw nodig |
| GR (Property-semantiek) | Geen nieuwe property |

### §10.3 Protocol-progressie tijdens T3

Geen sprint-protocol-tekst is door Tech-subagent gewijzigd tijdens T3. SKOS-beoordelings-protocol v1.3 (operationeel autoritatief tijdens T3) bevat cross-category-mappings impliciet als geldig binnen §3.1 rij 8 (thematische verwantschap → relatedMatch); kandidaat-formalisering als expliciete §3.4 of §3.3-aanvulling is T3-leerpunt voor Brein-cyclus (zie §13).

---

## §11. Geparkeerde-items-status-update (Protocol 10)

| H-item | Vóór v4.6.3 | Na v4.6.3 | Mutatie |
|---|---|---|---|
| H36 (SKOS-exactMatch ctrl/compl-audit) | afgehandeld voor m10-scope (T1+T2); m14-component open subtask | **afgehandeld** voor m14-scope (T3); H36-volledige-scope closed | mutatie: T3-component closed; H36-totaal closed |
| H37 | active | active | ongewijzigd |
| H38 | active | active | ongewijzigd |
| H39 (SHACL-blinde vlek ctrl:↔compl:) | active — bevestigd in T1+T2 | active — opnieuw bevestigd in T3 (beide richtingen ctrl→compl én compl→ctrl ongevalideerd) | ongewijzigd; T3 bevestigt voor beide richtingen |
| H40 (UI-renderdekking Spoor A) | active | active | ongewijzigd |
| H25/H26/H27/H32/H33/H34/H35 | (per status H-register) | (per status H-register) | ongewijzigd |
| H41-kandidaat (SKOS-axioma-set-handling) | gedeclareerd-bewijs uit T2 §5.2 v4.6.1-rapport (Brein-overweging) | gedeclareerd-bewijs uitgebreid met T3 (compl:↔ctrl: skos:relatedMatch-impact op skos:related-axioma's, indien geladen) | Brein-overweging-uitbreiding |
| **H-kandidaat (cross-category-mappings)** | **niet gedeclareerd** | **T3-leerpunt voor Brein-cyclus** (zie §13.3) | **kandidaat-declaratie** |

Brein-cyclus-update vereist na masterchat-GO:
- H36-register-entry kan naar fully closed-segment (m10 + m14-scope volledig afgehandeld)
- H39 onveranderd active geparkeerd; T3-bevestiging voor beide richtingen documenteren
- Cross-category-mapping-leerpunt-overweging: H-kandidaat-declaratie (`H4X_cross-category-mappings`?) of concept-bestand-uitbreiding (`brain__concepts__skos-beoordelings-protocol.md` of nieuw `brain__concepts__cross-category-mappings.md`)

Geen H-register-update door Tech in dit rapport — Brein-cyclus uitvoert post-Stap-3.

---

## §12. D-decision-conformiteit-check (D1-D12)

| D | Conventie | v4.6.3-impact | Conform? |
|---|---|---|---|
| D1 | OWL 2 DL profiel | Geen TBox-wijziging, geen cycle/owl:Thing-domain | ✓ |
| D2 | Turtle-serialisatie | m14-avg-gdpr.ttl blijft Turtle | ✓ |
| D3 | 11 namespaces | Geen nieuwe namespace | ✓ |
| D4 | SKOS cross-framework — closeMatch default, exactMatch zeldzaam | Herclassificatie van 2 broadMatch naar relatedMatch is D4-conform onder cross-category-rationale (control ↔ legal-obligation) | ✓ verbetering |
| D4.1 | Disclaimer-handling autoritatieve mapping-bronnen | n.v.t. — geen exactMatch-overweging in T3; D4.1 inactief (bindende T3-steer 1) | ✓ (inactief, conform steer) |
| D5 | ctrl:↔bio: sameAs strikt — 93 pairs | Onveranderd 93 | ✓ |
| D6 | Bilinguale annotaties @nl/@en | Geen wijziging in labels/comments | ✓ |
| D7 | BIO 2.0 als twee klassen | Geen BIO2-wijziging | ✓ |
| D8 | Eén canonieke SoA — isms:SoA_2026 + 93 SoAEntry_* | Onveranderd 93 | ✓ |
| D9 | Framework-neutraal | Onveranderd | ✓ |
| D10 | COSO ICF/ERM enterprise-governance-laag | Onveranderd | ✓ |
| D11 | owl:sameAs asset-convergentie — ster-patroon | Onveranderd 5 | ✓ |
| D12 | Drie-laags compliance | Onveranderd; m14 compl:AVG_Art*-individuals zijn compl:LegalObligation (laag 2: legal obligation), conform D12-classificatie | ✓ |

**Alle 12 D-decisions conform.** D4-compliance bevestigd door symmetrische bidirectional toepassing van cross-category-rationale (Protocol v1.3-toepassing; cross-category-principe is kandidaat v1.3.1-precedent).

---

## §13. Aandachtspunten + open issues / vervolg

### §13.1 Cross-category-mapping-principe (T3-leerpunt voor v1.3.1-Brein-cyclus)

T3 leverde empirische bevestiging op productie-schaal (31 paren) van een principe dat T2 (m10, control ↔ control-eis) niet kon onthullen: **control ↔ legal-obligation is een cross-category-relatie die inherent associatief (relatedMatch) is, niet subsumptief (broad/narrowMatch).**

**Operationele werking in T3:**

- Cluster-doel-default per Protocol §3.1 rij 7 (narrowMatch in 1↔veel-subject-cluster) wordt op cross-category-niveau systematisch overstemd door C3-falen op conceptuele subsumptie
- closeMatch-uitzondering blijft mogelijk bij retrieval-interchangeability (T3-014 + T3-026 in m14)
- broadMatch is in m14 niet houdbaar in compl→ctrl-richting (SKOS-formal-semantics én cross-category-categorie-fout); masterchat-besluit Optie C verschoof beide broadMatch-paren naar relatedMatch

**Status:** kandidaat-formalisering voor v1.3.1-Brein-cyclus als nieuwe §3.4 of §3.3-aanvulling in SKOS-beoordelings-protocol. Tech-subagent voert geen autonome Protocol-tekst-wijziging uit (D4 + Protocol-vaststelling = masterchat-werk).

**Inscope-voorbeelden** (T3-precedent + projectie):

- control ↔ legal-obligation (T3 m14: ISO 27002 ↔ AVG; bewezen 31 paren)
- control ↔ standard-clause (open: ISO 27002 ↔ ISO 27001 Annex A; mogelijk nog niet T-sprint-scope)
- control ↔ wettelijke verplichting in andere modules (m16 VIRBI? m12 DORA? — toekomstige Brein-overweging)

**Buiten-scope-overweging:** lijst-uitbreiding via brain-vault concept-bestand (`brain__concepts__cross-category-mappings.md`?) als Brein-cyclus-output.

### §13.2 Brein-cyclus T3-afsluiting (Protocol 11)

Pending na masterchat-GO op dit patch-rapport. Brein-subagent in Claude Code voert uit:

**Verwachte updates in brain-vault:**

- Sprint-bestand `brain__sprints__T3-skos-bidirectional-audit-m14.md` (nieuw)
- Update `brain__sprints__sprint-register.md` (append T3-entry)
- Update `brain__decisions__D04_skos-cross-framework.md` (cross-category-rationale als toepassings-precedent; m14-scope toegevoegd aan D4-validatie-historiek)
- Update `brain__architecture__H36_skos-exactmatch-ctrl-compl-audit.md` (status fully closed; m10 + m14-scope volledig afgehandeld)
- Update `brain__concepts__skos-beoordelings-protocol.md` (v1.3-toepassings-bewijs op m14-scope)
- Update `brain__modules__M14_avg-gdpr.md` (post-patch SKOS-distributie 2 closeMatch + 29 relatedMatch + 0 broadMatch)
- Update `brain__log.md` + `brain__index.md` (T3-entry + v4.6.3-baseline)

**Verwachte nieuwe concept-bestanden:**

- `brain__concepts__cross-category-mappings.md` (T3-leerpunt-formalisering — cross-category-rationale als operationele principe binnen SKOS-beoordeling)
- Optioneel: `brain__architecture__H4X_cross-category-mappings-formalisering.md` (open H-item: moet Protocol v1.3.1 cross-category-mappings expliciet behandelen?)

### §13.3 Werkflow-leerpunten Stap 3 (Protocol v1.3 §10 categorieën)

Per Protocol v1.3 §10.1-categorieën:

**Categorie 1 (Tooling-gaten):**

- Canonical metrics-script v4.6.3 + SHACL-split-validator v4.6.3 efficient herbruikbaar uit T2-precedent (kleine versie-suffix-aanpassingen)
- Geen helper-script in T3 — handmatige scope (25 paren) volstond; helper-tooling-drempel zou bij ~50+ paren of grotere cluster-aantallen wel relevant zijn
- Bron-keten-traversal (ISO 27701:2025 Annex F + Annex D) was pre-sprint-inventarisatie-werk (Stap 1); geen tooling-gap in Stap 3
- Geen tooling-gap waargenomen

**Categorie 4 (Werkverdeling-momenten):**

- Tech-autonomie op Stap 3-uitvoering volstond — masterchat-besluit op pilot-§5.2-escalatie (Optie C) was vooraf-input (in instructie-tekst); geen runtime-escalatie nodig
- Protocol 17 v1.3 NEN-autonomie effectief: lokale ISO 27002:2022 + ISO 27701:2025-tekst-lezing voor 31 paren zonder masterchat-toets
- 0 stop-condities geraakt; 0 confidence-laag-paren; methodische sluiting binnen Tech-autonomie

**Categorie 7 (Upgrade-detectie-praktijk — Protocol v1.3 §10):**

- Cross-category-rationale blokkeert systematisch upgrade-claims richting broad/narrowMatch in m14
- Niet bidirectional in m14: alleen downgrade-mutaties (T3-001 + T3-002 broadMatch → relatedMatch) — geen upgrade-kandidaten ontdekt op de 25 Stap-3-paren
- closeMatch-uitzondering-detectie via retrieval-interchangeability-toets (T3-014 pilot + T3-026 Stap 3) is sterk evidence-pad — beide paren confidence middel, beide methode-conform behouden
- Conclusie: Protocol v1.3 + cross-category-rationale samen leveren methodisch-sluitende bidirectional audit voor m14-scope

### §13.4 Open issue: ISO 27701:2025 Annex D evidence-niveau-asymmetrie

T3 inventarisatie §5 detecteerde dat 27701:2025 Annex D non-exhaustief is op meerdere paren. Voorbeelden:

- Cryptografie (8.24): Annex D koppelt B.3.26 aan (32)(1)(a), niet aan (5)(1)(f) — terwijl semantiek beide ondersteunt (cryptografie is mechanisme voor vertrouwelijkheid ⇒ Art. 5(1)(f) én voor passende technische maatregelen ⇒ Art. 32)
- Access rights (5.18): Annex D-link voor (32) ontbreekt — terwijl 5.18 fundamenteel is voor toegangs-controle Art. 32 vereist

**Impact op T3-uitkomst:** evidence-niveau-2 (27701-equivalent bestaat, Annex D-link ontbreekt voor specifiek AVG-artikel) ondersteunt relatie zonder predicate-upgrade-grond. Geen mutatie-trigger.

**Brein-cyclus-overweging:** documenteren in `brain__concepts__skos-beoordelings-protocol.md` of nieuw concept-bestand dat **Annex D-non-exhaustiviteit niet als negatief evidence-signaal werkt** — alleen als positief evidence-signaal indien link aanwezig.

### §13.5 Toekomstige T-sprint-overwegingen

T3 sluit H36 volledig af voor m10 + m14-scope. Open SKOS-audit-gebieden voor toekomstige T-sprints (niet T4-scope vóór masterchat-besluit):

- m16 VIRBI-mappings (omvang onbekend, SKOS-distributie te checken)
- m12 DORA-mappings (omvang onbekend)
- m17 COSO-COBIT-mappings (eerder buiten focus; mogelijk relevant voor enterprise-governance-laag-completeness)
- Framework-niveau SKOS-mappings (fw:↔fw:; nu beperkt tot Sectie 4 m14 + m01/m07 — buiten T3-scope)

Geen pre-bepaling. Brein-cyclus + masterchat bepalen volgende SKOS-audit-scope.

---

## §14. Sprint-prognose-evaluatie

T3-sprint-prognose per Stap 3-instructie-§ "Verwachte uitkomst" + pilot-rapport §6.2-scenario-C:

| Aspect | Prognose | Werkelijk | Status |
|---|---:|---:|---|
| Mutaties in apply_patch_v4_6_3.py | 2 | **2** | ✓ exact |
| Pilot-paren in mutatie-set | 1 (T3-002) | **1** | ✓ exact |
| Patch-vereist Stap 3 resterend | 1 (T3-001) | **1** | ✓ exact |
| Backup-file aangemaakt | ja | ja | ✓ |
| Post-patch m14 broadMatch | 0 | **0** | ✓ exact |
| Post-patch m14 closeMatch | 2 | **2** | ✓ exact |
| Post-patch m14 relatedMatch | 29 | **29** | ✓ exact |
| Globale skos:broadMatch | 129 | **129** | ✓ exact |
| Globale skos:relatedMatch | 194 | **194** | ✓ exact |
| Canonical metrics-Δ triples | 0 (±5 OWL-RL) | 0 / 0 | ✓ binnen tolerantie |
| SHACL SECTIE A violations | 0 | 0 | ✓ |
| SHACL SECTIE B violations | 0 | 0 | ✓ |
| SHACL COMBINED violations | 290 (identiek baseline) | 290 (Δ 0) | ✓ |
| m14-hash gewijzigd | ja, ≠ `47daeb7e…` | ja, `874565ba…` | ✓ |
| 21 andere modules + grc-shacl hash-identiek | ja | ja | ✓ |
| Stop-condities geraakt | 0 | 0 | ✓ |
| Confidence-laag-paren | 0 | 0 | ✓ |
| Cluster-discipline-convergentie | Art5_1f homogeen post-patch | Art5_1f homogeen related×7 | ✓ |

**Sprint-prognose volledig geklopt op alle 17 metrics.** Geen afwijking, geen onverwachte uitkomst, geen scope-pauze-trigger geraakt tijdens Stap 3.

---

## §15. GO-criteria-checklist (instructie + Stap 3-discipline)

| # | Criterium | Drempel | Werkelijk | Status |
|---|---|---|---|---|
| 1 | Applier productie-run succesvol | 2/2 mutaties zonder fouten | 2/2 OK, 0 NOT FOUND, 0 ambigu | ✓ |
| 2 | Backup-file aanwezig | `m14-avg-gdpr.ttl.v4_6_2.bak` bestaat | aanwezig | ✓ |
| 3 | m14 SKOS-counts compl→ctrl post-patch | exact 0 / close 2 / broad 0 / narrow 0 / related 29 | 0 / 2 / 0 / 0 / 29 | ✓ |
| 4 | Canonical metrics totaal-triples | ±0 t.o.v. v4.6.2 (20.950) | 20.950 (Δ 0) | ✓ |
| 5 | Canonical metrics post-OWL-RL | ±5 t.o.v. v4.6.2 (44.907) | 44.907 (Δ 0) | ✓ |
| 6 | Klassen / Individuals / OP / DP | identiek (199 / 1.383 / 149 / 96) | 199 / 1.383 / 149 / 96 | ✓ |
| 7 | SHACL SECTIE A | 0 violations | 0 | ✓ |
| 8 | SHACL SECTIE B | 0 violations | 0 | ✓ |
| 9 | SHACL COMBINED | 290 (identiek v4.6.2) | 290 (Δ 0) | ✓ |
| 10 | File-hash m14 | nieuwe sha256 ≠ `47daeb7e…` | `874565bade04c1657841298d4b035fa9c7f06f46a8d76ce9efba8ecfb35e1864` | ✓ |
| 11 | File-hashes overige 21 modules + grc-shacl | identiek aan v4.6.2 | identiek (diff: alleen m14) | ✓ |
| 12 | Patch-rapport §0-§15 compleet | alle secties ingevuld | §0-§15 compleet | ✓ |
| 13 | Pre-push disclosure-check Protocol 14 | 5 categorieën pass | (1) geen organisatie-naam (2) geen persoonsnamen anders dan Steven (3) geen lokale paden buiten `/Users/stevenbouwmeester/grc-kennismodel/` + NEN-licentie-pad (4) geen credentials/TLD/e-mail (5) geen verbatim NEN-tekst >10 woorden | ✓ |
| 14 | T3-leerpunt cross-category-principe gedocumenteerd | ja, in §13.1 + Stap 3-eindrapport §5 | ja, niet-formaliserend (kandidaat-precedent voor v1.3.1-Brein-cyclus) | ✓ |
| 15 | Cumulatief m14-overzicht beschikbaar | ja, Stap 3-eindrapport §6 | aanwezig (31 paren tabelmatig) | ✓ |

**Alle 15 GO-criteria groen.** Tech-eindoordeel: T3-sprint-deliverables klaar voor masterchat-review en handmatige commit + push door Steven.

— Einde patch-rapport v4.6.3.
