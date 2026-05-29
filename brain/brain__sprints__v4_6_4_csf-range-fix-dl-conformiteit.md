---
type: sprint
id: v4.6.4
title: v4.6.4 — CSF-description range-fix (DL-conformiteit, H38-lus gesloten)
status: active
date: 2026-05-29
baseline_from: v4.6.3
baseline_to: v4.6.4
related:
  - T3-skos-bidirectional-audit-m14
  - D01_owl-2-dl-profiel
  - H38_owlrl-vs-hermit-equivalentie
  - H37_open-ontologies-mcp
  - H41_skos-axioma-set-handling
  - M21_nist-csf-2-0-planned
  - owl-rl-reasoning
sources:
  - patch-rapport-v4_6_4
  - evaluatie-reasoner-toolchain-h37-h38-h41
chat-sources: []
confidence: high
---

# v4.6.4 — CSF-description range-fix (DL-conformiteit, H38-lus gesloten)

## Status

**TBox-bugfix-patch** — opgeleverd 29 mei 2026. Patch-release v4.6.3 → v4.6.4. Geen T-sprint, geen kwaliteits-sprint: een surgische **TBox-correctie** die de DL-conformiteit van twee CSF-Tier-vrije-tekst-properties herstelt. Twee `rdfs:range`-declaraties in `m21-csf.ttl` (`xsd:string` → `rdfs:Literal`) + version-bump in `grc-core.ttl`. Geen ABox-, SKOS- of shape-wijziging.

**Methodologisch precedent:** dit is de **eerste sprint waarin een HermiT-bevinding (DL-zijde) een concrete TBox-fix in de canonieke baseline stuurde**. OWL RL zag de datatype-botsing niet (controleert datatype-ranges niet streng); een volledige DL-reasoner (HermiT/Protégé) wél. De fix is puur DL-correctheid — de canonieke metrics blijven daardoor *invariant* (gewenste eigenschap). Zie patch-rapport v4.6.4 §5.

## De mutatie

Aanleiding: HermiT (Protégé, projecteigenaar, 29 mei 2026) meldde de merged graph v4.6.3 **inconsistent** (`owl:Thing SubClassOf owl:Nothing`, 8 justificaties = 4 CSF-Tiers × 2 properties). Diagnose (masterchat, bron-geverifieerd): de twee CSF-Tier-vrije-tekst-properties hebben `rdfs:range xsd:string`, maar dragen `@en`-getagde waarden (`rdf:langString`). Een volledige DL-reasoner ziet dat als datatype-botsing; OWL RL controleert datatype-ranges niet streng (vandaar 0 `owl:Nothing` + 44.907 schone triples onder de canonieke owlrl-config).

| Property (regel m21) | Voor | Na |
|---|---|---|
| `csf:riskGovernanceDescription` (5436) | `rdfs:range xsd:string ;` | `rdfs:range rdfs:Literal ;` |
| `csf:riskManagementDescription` (5444) | `rdfs:range xsd:string ;` | `rdfs:range rdfs:Literal ;` |

`rdfs:Literal` omvat zowel `xsd:string` als `rdf:langString` → de botsing verdwijnt. Conform de bestaande projectconventie (**Optie A** masterchat): vrije-tekst-velden gebruiken `rdfs:Literal` (`ext:hasControlStatement`, `ext:hasUVInterpretation`, `ext:hasAttributionText`); `xsd:string` blijft gereserveerd voor identifier-/code-velden zonder taal-tags. Na de fix: **0** resterende `xsd:string`-voorkomens in `m21-csf.ttl` (breedte bevestigd; de scope-pauze-conditie "meer dan twee botsende range-regels" deed zich niet voor).

`grc-core.ttl`: `owl:versionInfo` + `owl:versionIRI` bijgewerkt naar 4.6.4 (zie version-drift-leerpunt hieronder).

## Baseline-metrics — ONGEWIJZIGD (TBox-bugfix, geen telmetingswijziging)

Alle canonieke tellingen identiek aan v4.6.3 — exact zoals voorspeld: de fix vervangt uitsluitend het *object* van 2 triples (`xsd:string` → `rdfs:Literal`), zonder triple toe te voegen of te verwijderen.

| Metric | v4.6.3 | v4.6.4 | Δ |
|---|---:|---:|---:|
| Pre-inferentie triples | 20.950 | 20.950 | **0** |
| Post-OWL-RL triples | 44.907 | 44.907 | **0** |
| Klassen | 199 | 199 | 0 |
| NamedIndividuals | 1.383 | 1.383 | 0 |
| ObjectProperties | 149 | 149 | 0 |
| DatatypeProperties | 96 | 96 | 0 |
| owl:sameAs (93 D5 + 5 D11) | 98 | 98 | 0 |
| SKOS-mappings totaal | 1.798 | 1.798 | 0 |
| — exact / close / broad / related / narrow | 18 / 1.457 / 129 / 194 / 0 | idem | 0 |
| owl:Nothing post-inferentie | 0 | 0 | 0 |
| SHACL SECTIE A / B / COMBINED | 0 / 0 / 290 | 0 / 0 / 290 | 0 |

**Onderscheid met T1/T2/T3 (belangrijk):** de T-sprints waren triple-neutraal door **SKOS-predicate-substitutie** (predicate van mapping-triples gewijzigd binnen behouden SKOS-totaal). v4.6.4 is óók triple-neutraal, maar door een **TBox-datatype-range-fix** (object van 2 property-declaratie-triples gewijzigd) — een fundamenteel ander mutatie-type. Geen SKOS-context, geen mapping-herklassificatie.

File-hashes: alleen `m21-csf.ttl` + `grc-core.ttl` gewijzigd; 20 overige modules + `grc-shacl.ttl` byte-identiek aan v4.6.3.

## H38-lus gesloten (de volledige boog)

v4.6.4 sluit het empirische bewijs voor [[brain__architecture__H38_owlrl-vs-hermit-equivalentie]] (parked → **resolved**):

1. **Blind spot** (iteratie 12): sinds v4.0.0 geen HermiT-herrun; OWL RL ≡ HermiT plausibel maar niet aangetoond.
2. **Evaluatie** (29 mei): DL-construct-census voorspelde één DL-only-constructie (`asset:AssetOrComponent ≡ unionOf`, materialiseerbaarheids-compleet onder OWL RL → verwachte HermiT-delta = housekeeping).
3. **Bevinding**: de HermiT-run op v4.6.3 vónd echter een **reële DL-divergentie** — datatype-range-mismatch op de 2 CSF-description-properties (8 justificaties, 4 Tiers × 2 properties).
4. **Fix**: v4.6.4 corrigeert de range (`xsd:string` → `rdfs:Literal`).
5. **Her-verificatie**: HermiT-her-run op `output/verification/merged_asserted_v4_6_4.ttl` (20.950 triples) bevestigt **consistent, 0 `owl:Nothing`, geen justificaties**.

Dit is het **eerste empirische bewijs dat OWL RL ≡ HermiT** voor deze baseline (na de range-fix). H38 promoveert van "blind spot" naar "geverifieerd". Zie [[brain__sprints__T3-skos-bidirectional-audit-m14]] (vorige baseline) en de reasoner-toolchain-evaluatie (H37/H41 blijven parked).

## D-decision-conformiteit

| D | Relevantie | Status |
|---|---|---|
| **D1** (OWL 2 DL) | Kern — `rdfs:Literal`-range is OWL 2 DL-conform; de fix herstelt juist de DL-conformiteit (HermiT-consistentie) | ✅ versterkt |
| D4 (SKOS) | Geen SKOS-wijziging | ✅ n.v.t. |
| D5/D11 (sameAs) | 93 + 5 ongewijzigd (gemeten) | ✅ |
| D6 (bilinguaal + meeliftregel) | Edit-scope = 2 property-declaraties (m21) + version-triples (grc-core); binnen die scope alle annotaties al tweetalig. De 8 CSF-Tier-descriptions blijven `@en`-only (NIST CSWP 29, geen gezaghebbende NL-bron) — bewust, conform D6-symmetrische toepassing; `@nl`-vertaling expliciet buiten deze patch | ✅ geen meelift-schuld |

Geen D-schending, geen D-wijziging voorgesteld.

## Cross-referenties

- [[brain__decisions__D01_owl-2-dl-profiel]] — D1 versterkt; de fix herstelt DL-conformiteit
- [[brain__architecture__H38_owlrl-vs-hermit-equivalentie]] — resolved via deze patch
- [[brain__architecture__H37_open-ontologies-mcp]] — parked; H38-vondst is *modelleer*-fout (range), geen OWL RL-*reasoner*-limitatie → versterkt H37-trigger niet
- [[brain__architecture__H41_skos-axioma-set-handling]] — parked; niet geraakt
- [[brain__modules__M21_nist-csf-2-0-planned]] — gewijzigde module (m21-csf)
- [[brain__concepts__owl-rl-reasoning]] — OWL RL ziet datatype-botsing niet; DL wel
- [[brain__sprints__T3-skos-bidirectional-audit-m14]] — vorige baseline (v4.6.3)

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-29 | active | v4.6.4 patch opgeleverd; 2 range-fixes m21 + version-bump grc-core; baseline-metrics ongewijzigd; HermiT-her-run consistent → H38 resolved; eerste sprint waarin HermiT een TBox-fix stuurde |

— Einde v4.6.4.
