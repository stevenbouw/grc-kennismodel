---
type: sprint
id: T2
title: T2 — SKOS-bidirectional-audit m10 (118 paren over 10 NIS2-clusters)
status: active
date: 2026-05-27
baseline_from: v4.6.1
baseline_to: v4.6.2
related:
  - T1_skos-kwaliteitsanalyse-fase-1
  - D04_skos-cross-framework
  - H36_skos-exactmatch-ctrl-compl-audit
  - H39_shacl-run2-290-false-positives-uitsplitsing
  - H41_skos-axioma-set-handling
  - skos-beoordelings-protocol
  - mapping-bron-disclaimer-effect
  - cluster-discipline-bewijslast
sources:
  - patch-rapport-v4_6_2
  - t2-pre-sprint-inventarisatie
  - t2-pilot-rapport
  - t2-stap3-eindrapport
  - skos-beoordelings-protocol-v1_2
  - skos-beoordelings-protocol-v1_3
chat-sources: []
confidence: high
---

# T2 — SKOS-bidirectional-audit m10 (118 paren over 10 NIS2-clusters)

## Status

**Tweede post-migratie productie-sprint** — opgeleverd 27 mei 2026. Patch-release v4.6.1 → v4.6.2. T2-sprint behandelt SKOS-kwaliteitsanalyse Fase 2 (bidirectional audit op ctrl:↔compl: in `m10-nis2-ext.ttl`) onder Protocol v1.2. Alle 118 m10-paren convergeren naar `skos:broadMatch` via 65 predicate-substituties (32 downgrade + 33 upgrade). Sprint-multiplier 2,32× t.o.v. T1.

Methode-protocol v1.2 (vastgesteld vooraf door masterchat) bevestigd in productie op cluster-niveau: 10/10 clusters converge naar cluster-doel-predicate, 0 NEN-aantoonbare uitzonderingen op 10 heuristiek-flags. Zeven Protocol v1.3-verfijning-voorstellen geleverd; v1.3-tekst staat als **DRAFT** in `docs/skos-beoordelings-protocol-v1_3.md` (vaststelling pending bij eerstvolgende sprint-scoping).

## Scope — m10 ctrl:↔compl: bidirectional, m14 deferred

T2-scope per masterchat-besluit **Optie C** (m10-only T2; m14 wordt aparte T-sprint):

| Aspect | T2-scope | Buiten T2 |
|---|---|---|
| Module | `m10-nis2-ext.ttl` (NIS2-art.21 ↔ ISO 27002) | `m14-avg-gdpr.ttl` (31 compl→ctrl-paren, omgekeerde modelleringsconventie) |
| Richting | ctrl: → compl: (118 paren in m10) | compl: → ctrl: (31 m14-paren) |
| Predicate-types | closeMatch + broadMatch + relatedMatch | exactMatch (al door T1 omgezet — 0 residueel) |
| Cluster-omvang | 10 NIS2-art.21-letter-clusters | n.v.t. |

Pre-sprint-inventarisatie bevestigde 149 ctrl:↔compl:-paren totaal (118 m10 + 31 m14), 34% boven instructie-raming (~111). Scope-pauze-trigger §5 (totaal >130) geraakt, masterchat-beslissing Optie C: T2 = m10-only, m14 = aparte sprint. Zie `output/reports/t2-pre-sprint-inventarisatie.md` §7 Tech-observatie 2.

## Sprint-uitvoering — vier stappen + pre-Stap-4 errata

| Stap | Inhoud | Output |
|---|---|---|
| 1 | Pre-sprint-inventarisatie — 118 m10-paren + 31 m14-deferral; ABox-baseline + 10-cluster-cardinaliteit per NIS2-letter | `output/reports/t2-pre-sprint-inventarisatie.md` |
| 2 | Pilot 8 paren over 10 clusters — Protocol v1.2 in productie; 4 patch-mutaties, cluster-discipline op NIS2_a-cluster gevalideerd | `output/reports/t2-pilot-rapport.md` |
| pre-4 | Errata-correctie pilot-rapport + Stap 3-rapport §1.1 — helper-script-classificatie autoritatief over handmatige pilot-rapport-tekst | errata-blok in pilot-rapport, §1.1-correctie in Stap 3-rapport |
| 3 | Hoofd-uitvoering 110 paren via cluster-overerving-helper-script; alle 10 clusters → broadMatch; 0 NEN-uitzonderingen op 10 heuristiek-flags | `output/reports/t2-stap3-eindrapport.md` |
| 4 | Productie-patch v4.6.2 — 65 mutaties via `apply_patch_v4_6_2.py --apply`; canonical metrics + SHACL split-validatie + file-hashes; 13/13 GO-criteria groen | `output/reports/patch-rapport-v4_6_2.md` |

**Sample-first-discipline (Protocol 16) toegepast:** pilot-paren in 6/10 clusters gebruikt als cluster-representant in Stap 3 (effort-besparing per Stap 3-instructie §3.2 optie A). Resterende 4 clusters (d, f, g, h) kregen nieuwe representanten.

## Uitkomst — 65 mutaties, alle clusters convergeren naar broadMatch

### Per-cluster (per patch-rapport v4.6.2 §6.1)

| Cluster | NIS2-clause | Cluster-grootte | Behoud | Downgrade | Upgrade | Patch | Flags | NEN-uitz. |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| a | Risicoanalyse + IS-beleid | 12 | 4 | 4 | 4 | 8 | 3 | 0 |
| b | Incidentbehandeling | 10 | 6 | 2 | 2 | 4 | 0 | 0 |
| c | Bedrijfscontinuïteit + back-up + DR | 8 | 4 | 2 | 2 | 4 | 0 | 0 |
| d | Toeleveringsketen | 7 | 5 | 1 | 1 | 2 | 0 | 0 |
| e | Verwerving + ontwikkeling | 17 | 7 | 4 | 6 | 10 | 0 | 0 |
| f | Beoordeling effectiviteit | 7 | 4 | 1 | 2 | 3 | 1 | 0 |
| g | Cyberhygiëne + training | 9 | 4 | 3 | 2 | 5 | 1 | 0 |
| h | Cryptografie | 7 | 4 | 1 | 2 | 3 | 1 | 0 |
| i | HR + access + asset | 32 | 12 | 11 | 9 | 20 | 3 | 0 |
| j | MFA + continuous auth + comms | 9 | 3 | 3 | 3 | 6 | 1 | 0 |
| **Totaal** | | **118** | **53** | **32** | **33** | **65** | **10** | **0** |

**Cluster-discipline-bewijs:** 10/10 clusters convergeren naar `skos:broadMatch` (cardinaliteit veel↔1, alle cluster-grootte ≥7). 100% cluster-discipline-conform op productie-schaal.

### Bidirectional mutatie-verdeling

| Richting | Aantal | % |
|---|---:|---:|
| Downgrade (closeMatch → broadMatch) | 32 | 49,2 |
| Upgrade (relatedMatch → broadMatch) | 33 | 50,8 |
| Richtings-correctie / verwijdering / twijfel | 0 | 0 |
| **Totaal patch-mutaties** | **65** | 100 |
| Behoud (al broadMatch) | 53 | n.v.t. |

**Symmetrisch bewijs Protocol v1.2:** mutaties zijn in beide richtingen aanwezig met vrijwel identieke aantallen. Protocol v1.2's bidirectional toetsing is symmetrisch toepasbaar gebleken (geen downgrade-bias zoals v1.1-draft veronderstelde). Drie verschillende mutatie-richtingen (downgrade + upgrade + behoud) komen binnen één cluster voor (bv. NIS2_a met 4+4+4) — directe empirische bevestiging van protocol-symmetrie, gerepliceerd over 10 clusters. Zie patch-rapport v4.6.2 §6.2 en Stap 3-rapport §6.7.

### Heuristiek-flag-screening

| Subject | Aantal clusters | Heuristiek-trigger | NEN-uitz. |
|---|---:|---|---|
| ISO27002_5_02 | 2 (a, i) | brede-policy-keyword in label | 0 |
| ISO27002_5_04 | 3 (a, f, g) | brede-policy-keyword + subject-cluster 3 | 0 |
| ISO27002_5_36 | 1 (a) | brede-policy-keyword | 0 |
| ISO27002_6_05 | 1 (i) | brede-policy-keyword | 0 |
| ISO27002_8_03 | 3 (h, i, j) | subject-cluster 3 (multi-mapping) | 0 |
| **Totaal** | **10 flags / 6 leden** | | **0** |

100% van de heuristiek-flags na ISO 27002:2022-tekstlezing cluster-conform bevonden. Heuristiek werkt als prioriteits-mechanisme voor manuele review, niet als beslis-mechanisme. Geen NEN-aantoonbare individuele uitzondering aangetoond. Zie patch-rapport v4.6.2 §6.3 en Stap 3-rapport §4.

## Triple-impact v4.6.1 → v4.6.2

Per patch-rapport v4.6.2 §0.1 + §0.2:

| Metric | v4.6.1 | v4.6.2 | Δ |
|---|---:|---:|---:|
| Pre-inferentie triples | 20.950 | 20.950 | 0 |
| Post-inferentie triples (OWL RL) | 44.907 | 44.907 | 0 |
| Klassen / NamedIndividuals / OP / DP | 199 / 1.383 / 149 / 96 | identiek | 0 |
| owl:sameAs (D5 + D11) | 98 | 98 | 0 |
| SKOS-mappings totaal | 1.798 | 1.798 | 0 |
| `skos:exactMatch` | 18 | 18 | 0 |
| `skos:closeMatch` | 1.489 | 1.457 | −32 |
| `skos:broadMatch` | 66 | 131 | **+65** |
| `skos:relatedMatch` | 225 | 192 | −33 |
| `skos:narrowMatch` | 0 | 0 | 0 |
| SHACL SECTIE A / SECTIE B / COMBINED | 0 / 0 / 290 | 0 / 0 / 290 | 0 / 0 / 0 |

**Predicate-substitutie zonder triple-totaal-impact** — 65 triples van predicate veranderd, geen triple toegevoegd of verwijderd. Eén module geraakt: `m10-nis2-ext.ttl` (hash `cb2d567b…` → `a4bfdc12…`). 21 andere modules + `grc-shacl.ttl` bytewise identiek aan v4.6.1.

**Post-OWL-RL-stabiliteit:** Δ = 0. Verklaring (per patch-rapport v4.6.2 §4.1): `owlrl`-package laadt in canonieke configuratie (`axiomatic_triples=False`, `datatype_axioms=False`) geen SKOS-axiomas (S46-symmetrie, S47-transitiviteit). Predicate-naamverandering raakt daarom geen RDFS/OWL-inferentie-pad. Bekende beperking gedocumenteerd in [[brain__architecture__H41_skos-axioma-set-handling]].

## Belangrijkste bevindingen

### 1. Cluster-discipline schaalbaar op productie-niveau (per patch-rapport v4.6.2 §1)

Pilot-rapport (T1) valideerde cluster-discipline op één cluster (3 paren in NIS2_a). T2 valideert dit over **10 clusters × 118 paren**: alle clusters convergeren naar één doel-predicate zonder NEN-aantoonbare individuele uitzondering. Cluster-overerving-helper-script (`output/scripts/t2-cluster-overerving-helper.py`) comprimeert per-paar-werk tot per-cluster-review (~10-15 min per cluster).

**D4.1-toepassing op cluster-niveau** (per patch-rapport v4.6.2 §1): één D4.1-bevestiging per cluster volstaat wanneer alle cluster-leden dezelfde bron-stack hebben (ENISA TIG R285 + CBW-Mapping-UV R3-erf). Voor heterogene clusters (mix van bronnen) blijft per-paar-toets vereist. Zie [[brain__decisions__D04_skos-cross-framework]] §D4.1 voor formele D4.1-precedent-uitbreiding.

### 2. Bidirectional symmetrie methodisch sluitend (per Stap 3-rapport §6.7)

Mutatie-verdeling 32 downgrade + 33 upgrade bevestigt symmetrie van Protocol v1.2 bidirectional toetsing. Geen downgrade-bias zoals v1.1-draft veronderstelde — predicate-doel-tabel §3.1 + sterkte-ordening §3.2 zijn methodisch symmetrisch toepasbaar gebleken. Binnen één cluster (NIS2_a met 12 leden) treden zowel downgrade (4× closeMatch → broadMatch), upgrade (4× relatedMatch → broadMatch) als behoud (4× broadMatch) op — drie mutatie-richtingen convergeren naar één cluster-doel-predicate.

Concept-niveau verankering: [[brain__concepts__skos-beoordelings-protocol]] §"Bidirectional-audit-symmetrie" *(nieuw iteratie 14)*.

### 3. Bewijslast-asymmetrie voor cluster-uitzondering (per Stap 3-rapport §6.5 + patch-rapport v4.6.2 §6.3)

10 heuristiek-screening-flags op 6 cluster-leden (sommige in meerdere clusters) leverden 0 NEN-aantoonbare uitzonderingen op. Empirisch bewijs voor bewijslast-asymmetrie:

- **Uitzondering naar sterker mapping** (bv. closeMatch in veel↔1-cluster): vereist bilaterale containment-aantoonbaarheid via NEN-tekst. In veel↔1-cluster structureel zeer moeilijk omdat object-cluster-cardinaliteit ≥2 betekent dat object niet bilateraal A=B kan zijn met meerdere A's.
- **Uitzondering naar zwakker mapping** (bv. relatedMatch in veel↔1-cluster): vereist NEN-bewijs dat C3 (subset-relatie) faalt; operationeel zeldzaam want cluster-lidmaatschap impliceert reeds enige subset-relatie.
- **Behoud cluster-default**: geen aanvullende bewijslast.

Concept-niveau verankering: [[brain__concepts__cluster-discipline-bewijslast]] *(nieuw iteratie 14)*.

### 4. SHACL-blinde-vlek bevestigd op 118-paren-schaal (per patch-rapport v4.6.2 §7.3)

Geen shape in `ontology/grc-shacl.ttl` valideert direct op ctrl:↔compl:-mapping-distributie. De 65 SKOS-predicate-substituties raken daarom geen shape — SHACL-uitkomsten zijn structureel ongevoelig voor T2-mutaties. T1 toonde dit op 28-paren-schaal; T2 bevestigt op 118-paren-schaal. [[brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing]] blijft active geparkeerd; trigger-relevantie verder verhoogd.

### 5. SKOS-axioma-set-handling als architectuur-vraag (per patch-rapport v4.6.2 §11)

T1 markeerde dit reeds als werkflow-leerpunt (zonder H-registratie). T2 levert op productie-schaal empirisch bewijs: post-OWL-RL Δ-triples = 0 ondanks 65 SKOS-predicate-mutaties (waarvan 32 closeMatch ↔ symmetrie-relevant + 0 transitiviteits-relevant). [[brain__architecture__H41_skos-axioma-set-handling]] *(nieuw iteratie 14)* geregistreerd als geparkeerde architectuur-vraag.

### 6. Helper-script-classificatie autoritatief (per Stap 3-rapport §6.4 + patch-rapport v4.6.2 §13.1)

Pre-Stap-4 errata-correctie: pilot-rapport §4.3 (T2-S03) en §4.8 (T2-S08-alt) classificeerden mutatie-richtingen handmatig in afwijking van Protocol v1.2 §3.2 sterkte-ordening. Helper-script (`t2-cluster-overerving-helper.py`) past §3.2 strikt toe en classificeert autoritatief. Errata-blok in pilot-rapport + §1.1-correctie in Stap 3-rapport documenteren discrepantie zonder T-historie te herschrijven. Patch-impact identiek (alle paren convergeren naar broadMatch); classificatie-kolom gecorrigeerd voor methodische hygiëne.

### 7. Masterchat-instructie-tabel-inconsistentie (per patch-rapport v4.6.2 §13.2)

Sprint-instructie-tekst bevatte interne inconsistentie tussen §1 verwachtings-tabel ("m10 related 27") en §8 GO-criterium #3 ("m10 related 0"). §1-tabel suggereerde m14-cumulatief; §8 was m10-only. Bron-van-waarheid: `canonical_metrics_v4_6_2.json` (m10-only conform Optie C). Tech-zelfcorrectie via Protocol 12-discipline zonder masterchat-escalatie. Werkflow-leerpunt vertaald naar Protocol v1.3 §10.3 (interne tabel-consistentie-discipline) en §10.5 (metrics-tabel-scope-annotatie verplicht).

## H-impact

| H | Status vóór T2 | Status na T2 | Mutatie |
|---|---|---|---|
| [[brain__architecture__H36_skos-exactmatch-ctrl-compl-audit]] | closed (T1) — open-uitbreiding voor close/related-audit (T2-scope) | **active, m10-component closed** — m14-component blijft open subtask | T2 voltooit m10-scope volledig (T1+T2 = 28+65 = 93 m10-paren); m14 (31 paren) blijft open |
| [[brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing]] | parked (versterkt T1) | parked (versterkt T2) | T2 bevestigt SHACL-blinde-vlek op 118-paren-schaal; trigger-relevantie verder verhoogd |
| [[brain__architecture__H41_skos-axioma-set-handling]] | n.v.t. — T1-werkflow-leerpunt zonder H-registratie | **parked (nieuw geregistreerd)** | T2-empirisch bewijs (Δ post-OWL-RL = 0 op 65 SKOS-mutaties) + masterchat-besluit tot H-registratie |
| H15, H21, H25-H35, H37, H38, H40 | per H-register | ongewijzigd | — |

## D-impact — D4.1-precedent-uitbreiding naar cluster-niveau

Alle 12 D-decisions blijven conform. **D4 + D4.1 specifiek versterkt:**

| D | Conformance | Detail |
|---|---|---|
| D1 OWL 2 DL | ✓ ongewijzigd | Geen TBox-wijziging |
| D2 Turtle-serialisatie | ✓ ongewijzigd | Enige m10-wijziging |
| D3 11 namespaces | ✓ ongewijzigd | Geen nieuwe namespace |
| **D4 SKOS cross-framework** | ✓ **bidirectional bewijs op productie-schaal** | 65 mutaties (32 downgrade + 33 upgrade) zonder D4-conflict |
| **D4.1 Disclaimer-handling** | ✓ **cluster-niveau-toepassing bewezen** | ENISA TIG R285 + CBW-Mapping-UV R3-erf blokkeert exactMatch op cluster-niveau voor alle 10 clusters; één bevestiging per cluster volstond |
| D5–D12 | ✓ ongewijzigd | Geen impact |

D4.1 is na T1 (28 paren) en T2 (65 mutaties op 118 paren, 10 clusters) operationeel bewezen op cluster-discipline-schaal. Zie [[brain__decisions__D04_skos-cross-framework]] §D4.1 voor toepassings-precedent-uitbreiding.

## Methode-protocol — v1.2 toegepast, v1.3-draft als T2-output

| Versie | Status | Toepassing |
|---|---|---|
| v1.0 | superseded | T1 (28 paren) |
| v1.1 | DRAFT (nooit operationeel) | n.v.t. |
| v1.2 | autoritatief tijdens T2 | T2 (118 paren over 10 clusters) — operationeel succesvol |
| **v1.3** | **DRAFT** | Vaststelling pending bij eerstvolgende sprint-scoping (T3 of m14) |

Zeven Protocol v1.3-verfijning-voorstellen geleverd in T2 (per `docs/skos-beoordelings-protocol-v1_3.md` §13.1):

1. §2.1 C1 "partieel"-grens — operationele test met drie-uitkomst-classificatie + T2-precedenten
2. §2.2 C2 subject-cluster vs object-cluster prevalence-regel expliciet (object-cluster prevaleert)
3. §3.3 Cluster-discipline-bewijslast-asymmetrie expliciet + T2-empirisch bewijs
4. §5.1 Cluster-representant-keuze-criteria als formele sub-sectie
5. §5.2 Confidence-criterium expliciete drempels (hoog/middel/laag)
6. §10.2 Bottom-up rapport-bouw verplicht (T2-pilot werkflow-leerpunt)
7. §10.3-§10.5 Werkflow-discipline-uitbreiding: interne tabel-consistentie + helper-script-autoritatief + metrics-tabel-scope-annotatie

v1.3-tekst is masterchat-geschreven post-T2 en wacht op sprint-scoping-vaststelling. Operationeel document `docs/skos-beoordelings-protocol-v1_3.md`.

## Sprint-multiplier + sprint-precedent-vergelijking

Per patch-rapport v4.6.2 §8:

| Aspect | T2 (v4.6.2) | T1 (v4.6.1) | Verhouding |
|---|---:|---:|---:|
| Triple-Δ pre-inferentie | 0 | 0 | identiek |
| Triple-Δ post-OWL-RL | 0 | 0 | identiek |
| Aantal SKOS-mutaties | 65 | 28 | **2,32×** |
| Mutatie-richtingen | upgrade + downgrade (bidirectional) | downgrade-only | bidirectional-uitbreiding |
| Cluster-scope | 10 clusters | 10 clusters | identiek |
| Protocol-versie | v1.2 | v1.0 | protocol-progressie |
| Pilot-omvang | 8 paren | 5 paren | +60% (Protocol v1.2 §6 spreiding-richtlijn) |
| Helper-tooling | cluster-overerving-helper + heuristiek-screening | n.v.t. | nieuwe tooling-laag |
| NEN-werkverdeling | Tech-autonomie (Protocol 17 v1.3) | masterchat-NEN-PK-toets | Tech-autonomie-uitbreiding |

**Sprint-multiplier:** T2 verwerkt 2,32× meer mutaties dan T1 met vergelijkbare triple-impact (Δ = 0 in beide gevallen; predicate-substitutie). Multiplier verklaard door bidirectional-scope (Protocol v1.2) + volledige m10-scope (T1 dekte alleen exactMatch-subset) + cluster-doel-discipline.

## Geactiveerde sprint-protocollen (per patch-rapport v4.6.2 §10)

Protocol 1 (Pre-sprint-inventarisatie), Protocol 7 (Bron-bereikbaarheid lokaal NEN), Protocol 10 (Patch-rapport §9 geparkeerd-items), Protocol 12 (Instructie-consistentie code vs toelichting), Protocol 14 (Pre-push disclosure-check 5 categorieën), Protocol 15 (Tech levert werkbare applier), Protocol 16 (Deliverables-tabel expliciet), Protocol 17 v1.3 (NEN-werkverdeling Tech-autonomie via lokale ISO 27002:2022-toegang).

Niet geactiveerd: Protocol 4 (Bron-verificatie vóór TBox — geen TBox-wijziging); Protocol 5/6/9 (raming-discipline — kwaliteits-sprint geen ABox-creatie); Protocol 8 (precedent-discipline — m10-NIS2 bestond reeds); Protocol 13 (bron-typo-beleid — geen typo's in m10-mutaties).

## Sprint-duur-evaluatie

Per patch-rapport v4.6.2 §14:

| Stap | Raming | Werkelijk |
|---|---:|---:|
| A: pre-patch baseline | ~5 min | ~5 min |
| B: applier productie-run | ~10 min | ~5 min |
| C: canonical metrics | ~30 min | ~10 min (T1-precedent-hergebruik) |
| D: SHACL split-validatie | ~30 min | ~15 min (incl. SECTIE B-subset) |
| E: file-hashes | ~5 min | ~2 min |
| F: patch-rapport bottom-up | ~1,5 uur | ~1 uur |

T1-precedent-hergebruik (canonical metrics + SHACL-scripts met versie-suffix-aanpassing) leverde substantiële tijdsbesparing op verificatie-fase. Bottom-up rapport-bouw (Protocol v1.3 §10.2) voorkwam classificatie-iteratie-loops.

## GO-criteria-resultaat — 13/13 groen

Alle 13 GO-criteria uit instructie §8 behaald (per patch-rapport v4.6.2 §15): applier 65/65 mutaties, backup-file aanwezig, m10-counts 0/0/118/0/0 conform, canonical metrics Δ = 0, klassen/individuals/OP/DP identiek, SHACL SECTIE A/B/COMBINED 0/0/290 (Δ 0), m10-hash gewijzigd, 21 andere modules + grc-shacl hash-identiek, patch-rapport §0-§15 compleet, Protocol 14 disclosure-check pass op 5 categorieën.

## Cross-references

- [[brain__sprints__T1_skos-kwaliteitsanalyse-fase-1]] — voorganger (v4.6.1-baseline waarop T2 patcht)
- [[brain__sprints__v4_6_0_fase-4-ensia-en-volwassenheid]] — voor-voorganger (Fase 4)
- [[brain__decisions__D04_skos-cross-framework]] — D4 + D4.1-precedent-uitbreiding naar cluster-niveau
- [[brain__architecture__H36_skos-exactmatch-ctrl-compl-audit]] — m10-component closed via T1+T2; m14 open subtask
- [[brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing]] — versterkt door T2 op 118-paren-schaal
- [[brain__architecture__H41_skos-axioma-set-handling]] — nieuw geregistreerd (T2-empirisch bewijs)
- [[brain__concepts__skos-beoordelings-protocol]] — methode-concept met v1.2-toepassings-bewijs + v1.3-draft-status
- [[brain__concepts__mapping-bron-disclaimer-effect]] — D4.1-cluster-niveau-toepassing
- [[brain__concepts__cluster-discipline-bewijslast]] — nieuw concept (bewijslast-asymmetrie)
- [[brain__workflow__sprint-protocollen]] — Protocol 14 + 16 + 17 toegepast in T2
- [[brain__modules__M10_nis2-ext]] — module waarop patch v4.6.2 is toegepast

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-27 | active | Oplevering T2-sprint — 65 SKOS-mutaties (32 downgrade + 33 upgrade) in m10-nis2-ext.ttl; alle 10 clusters convergeren naar broadMatch; methode-protocol v1.2 in productie bevestigd; v1.3-draft opgeleverd; H41 nieuw geregistreerd; m10-component van H36 closed; tweede post-migratie productie-sprint |

— Einde T2.
