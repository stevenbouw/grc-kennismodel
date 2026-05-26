---
type: sprint
id: v4.5.0
title: v4.5.0 — Fase 3: NIST CSF 2.0 (M21)
status: active
date: 2026-05-19
related:
  - v4_4_0_fase-2-cbw-cbb
  - D03_10-namespaces
  - D09_framework-neutraliteit
  - cross-bron-overlap
  - H33_m11-sp800-53-substantiele-uitbreiding
  - H34_m11-enhancement-modellering
  - H35_cbb-528-typo-interpretatie
sources:
  - patch-rapport-v4_5_0
  - canonical_metrics_v4_5_0
chat-sources: []
confidence: high
---

# v4.5.0 — Fase 3: NIST CSF 2.0 (M21)

## Status

**Huidige actieve baseline** sinds 19 mei 2026. Opvolger van v4.4.0.

Doorlooptijd: 13 — 19 mei 2026 (zes dagen, sprint-protocol B + meerdere scope-pauzes).

Bron: `patch-rapport-v4_5_0.md`, `canonical_metrics_v4_5_0.json`.

## Scope: zeven stappen + drie nieuwe geparkeerde items

| Stap | Inhoud | Triple-impact |
|---|---|---:|
| 1 | Pre-sprint-inventarisatie (Sprint-protocol B) — 3 signalen vooraf gerapporteerd | read-only |
| 2 | TBox-uitbreidingen + D3-revisie naar 11 namespaces (`csf:` toegevoegd) | +90 |
| 3 | CSF Core — 6 Functions + 22 Categories + 106 Subcategories als individuals | +1.094 |
| 4 | Implementation Examples — 363 IE-individuals (100% Subcategory-dekking) | +3.267 |
| 5 | Sheet 8 mappings (CBW-Excel) — 641 unieke `skos:closeMatch`-triples | +641 |
| 6 | NIST CSF Reference Tool mappings — OLIR-formaat-afwijking ontdekt → fallback | +794 / +899 (graph/builder) |
| 7 | GOVERN-overlap met COSO/COBIT (m17) — 13 `skos:relatedMatch`-triples | +13 |
| **Sprint-totaal** | — | **+5.899** |

## Triple-impact

| Metric | v4.4.0 | v4.5.0 | Δ |
|---|---:|---:|---:|
| Pre-inferentie triples | 13.441 | 19.340 | **+5.899** (+43,9%) |
| Post OWL RL | 31.415 | 41.988 | +10.573 |
| Klassen | 189 | 193 | +4 (4× csf:) |
| NamedIndividuals | 679 | 1.179 | **+500** |
| ObjectProperties | 143 | 146 | +3 (csf:partOfFunction, csf:partOfCategory, csf:exemplifies) |
| DatatypeProperties | 93 | 94 | +1 (csf:csfIdentifier) |
| `owl:sameAs` | 98 | 98 | 0 (D5 + D11 onveranderd) |
| **SKOS-mappings** | 346 | **1.794** | **+1.448** (+418%) |
| Namespaces (D3) | 10 | 11 | +1 (csf:) |
| Modules | 22 | 23 | +m21-csf.ttl |
| SHACL RUN 1 | 0 | 0 | 0 ✓ |
| SHACL RUN 2 | 290 | 290 | 0 ✓ (identieke false-positives) |

## Wijzigingen per module — 8 gewijzigd

| Module | Wijziging | csf-subjects |
|---|---|---:|
| **grc-core.ttl** | csf:-prefix; 4 csf-klassen (Function/Category/Subcategory/ImplementationExample ⊑ `ext:FrameworkComponent`); 3 csf-properties; csf:csfIdentifier DP | 8 (TBox) |
| **m01-framework.ttl** | `fw:NIST_CSF_2_0`-individual | — |
| **m02-control.ttl** | D6 meeliftregel: `ctrl:CybersecurityConcept` comment 5 → 6 Functions (CSF v1.x → v2.0 incl. GOVERN) | — |
| **m08-bio20.ttl** | csf-mappings landing (494 mappings naar `bio:ISO27002_*`) | 121 |
| **m09-iso27001-ext.ttl** | csf-mappings landing (hoofdtekst-clausules) | 65 |
| **m11-nist-800-53.ttl** | csf-mappings landing (SP 800-53 Rev 5) | 98 |
| **m17-coso-cobit.ttl** | GV→COSO/COBIT 13 nieuwe `skos:relatedMatch` (SKOS-uses verdriedubbeld 19→32) | — |
| **m21-csf.ttl (NIEUW)** | 6 Functions + 22 Categories + 106 Subcategories + 363 IE + 2 SourceAttributions | 497 |

## Architectuur-betekenis

### D3 — eerste expansie sinds vastlegging

v4.5.0 voert de **eerste D3-namespace-uitbreiding** uit sinds D3 in v4.2.0 werd vastgelegd (10 namespaces). Toevoeging: `csf:` (https://grc.example.org/csf/) voor NIST CSF 2.0. Geen wijziging aan bestaande 10 namespaces.

Zie [[brain__decisions__D03_10-namespaces]] voor de uitgebreide D3-staat.

### D9 — Optie B in actie

NIST CSF 2.0 is opgenomen als **gemapt referentiekader** (Optie B), niet als organiserend kader (Optie A). Concrete invulling van D9 framework-neutraliteit:

| Implementatie-keuze | D9-compatibel |
|---|---|
| CSF als 11e namespace náást ISO/NIST 800-53/BIO | ✓ — gelijkwaardig, niet centraal |
| Geen CSF-eigen control-klassen | ✓ — CSF Subcategories blijven outcomes, niet beheersmaatregelen |
| 1.448 SKOS-mappings naar bestaande kaders | ✓ — CSF positioneert zich relatief tot bestaande model, niet als root |
| `ext:isComponentOf fw:NIST_CSF_2_0` | ✓ — generiek framework-componenten-pattern (m17-precedent) |

### D6 meeliftregel — concrete edit-scope-toepassing

In M02 werd `ctrl:CybersecurityConcept`-comment bijgewerkt van CSF v1.x (5 Functions) naar CSF v2.0 (6 Functions, incl. GOVERN). Edit-scope: alleen die comment tweetalig — overige M02-content ongemoeid. Zie [[brain__decisions__D06_meeliftregel-tweetalig]].

## Sprint-protocollen — toepassings-bewijs

| Protocol | v4.5.0-toepassing |
|---|---|
| **Protocol B — Pre-sprint-inventarisatie** | 3 signalen vooraf in instructie verwerkt (Besluit 4 + 6 + Fase-3-context) |
| **Bron-verificatie vóór TBox-declaratie** | Stap 6 OLIR-formaat-aanname ontkracht door bron-inspectie → CSF Reference Tool-fallback |
| **Raming-discipline** | Sprint-totaal exact onderaan bijgestelde band (+5.899 vs +5.900-6.000 bijgesteld); Stap 5 sheet 8 wel 3× boven raming |
| **Patch-rapport §9 verplicht** | Uitgevoerd; 3 nieuwe H-items (H33/H34/H35) toegevoegd; alle 9 voorgaande H-items status-bevestigd |
| Protocol C — Schema-meta-rapport | Niet uitgevoerd; herziening overwogen post-Fase 3 wegens D3-uitbreiding (mogelijk vóór v4.6.0) |

**Patroon-bevinding (§12.4):** 4 van 6 stappen boven raming → leerpunt voor projectinstructie v1.8 — **bron-verificatie vóór raming-opstelling** als toe te voegen sprint-protocol-element.

## Methodologische bevindingen

### Cross-bron-overlap als SKOS-kwaliteits-indicator (NIEUW concept)

Stap 5 (Sheet 8 ADR & NOREA) en Stap 6 (CSF Reference Tool NIST) leggen **105 keer dezelfde ISO 27001-mapping**. Twee onafhankelijke bronnen → **bron-consistentie-bewijs**. Dit is geen technisch dedup-feit maar een SKOS-kwaliteits-validatie.

Zie [[brain__concepts__cross-bron-overlap]] voor de architectuur-betekenis.

### G1 "bij twijfel niet leggen" — discipline-toepassing

353 unresolved totaal:
- 16 sheet 8-unresolved (12 csf-subject-missing + 4 target-missing — bv. 5.28-typo)
- 108 unique unresolved SP 800-53-targets uit Stap 6 (modelbeperking m11)
- 75× letterlijke `"Mandatory Clause: None"` (CSF Reference Tool-conventie)
- Overige edge-cases

Allen gedocumenteerd, niet gelegd. Zie ook H33/H34.

### CSF Subcategory-numbering-gaps

NIST heeft `RC.CO-01` en `RC.CO-02` overgeslagen; RC.CO begint bij `-03`. Bron-eigen ontwerp, geen modelfout — landed in m21 conform NIST-publicatie.

## Nieuwe geparkeerde items

| H-item | Onderwerp | Trigger |
|---|---|---|
| [[brain__architecture__H33_m11-sp800-53-substantiele-uitbreiding]] | m11 substantiële uitbreiding SP 800-53 (124/~1000 nu in model) | Spoor B-organisatie heeft >50 niet-gemapte controls nodig |
| [[brain__architecture__H34_m11-enhancement-modellering]] | Enhancement-modellering (AC-2(1), CM-07(02), 17 unique enhancements in Stap 6) | Serieus SP 800-53-gebruik met enhancement-audit-behoefte |
| [[brain__architecture__H35_cbb-528-typo-interpretatie]] | Cbb 5.28-typo (sheet 8 UV 10.4 — vermoedelijk `A.5.28` = `bio:ISO27002_5_28`) | Stap 5-unresolved als interpretatieve correctie in latere sprint |

## ADR/NOREA bron-kwaliteits-patroon (cumulatief)

| Bron-issue | v4.4.0 | v4.5.0 |
|---|---|---|
| Typo-categorieën | 2 (in CBW-Excel sheet 9) | + 19 ISO-normalisaties + 16 unresolved + 5.28-typo |

Bron-conclusie: ADR/NOREA-content is bruikbaar maar structureel licht inconsistent — relevant voor toekomstig ADR/NOREA-bron-gebruik. Niet als ophouding gemarkeerd; G1-discipline volstaat.

## SourceAttribution-individuals na v4.5.0

| Individual | Toegevoegd | Licentie |
|---|---|---|
| `ext:Attr_CBW_NIS2_Framework_2025_CC_BY_4_0` | v4.4.0 | CC-BY 4.0 |
| `ext:Attr_NIST_CSF_2_0_Core_2024` | v4.5.0 Stap 2 | Public Domain |
| `ext:Attr_NIST_CSF_2_0_Reference_Tool_2026` | v4.5.0 Stap 2 + 6 | Public Domain |

## Bestand-wijzigingen

8 bestanden gewijzigd in v4.5.0; 14 modules bytewise identiek aan v4.4.0-eindstand. Plus `m21-csf.ttl` als 23e module.

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-19 | active | Oplevering v4.5.0 Fase 3 — M21 NIST CSF 2.0 + D3-revisie + 1.448 SKOS-mappings + 3 nieuwe H-items |

## Cross-references

- [[brain__sprints__v4_4_0_fase-2-cbw-cbb]] — voorganger
- [[brain__decisions__D03_10-namespaces]] — D3 uitgebreid in deze sprint
- [[brain__decisions__D09_framework-neutraliteit]] — Optie B-toepassing in deze sprint
- [[brain__concepts__cross-bron-overlap]] — nieuw concept geboren uit S5∩S6
- [[brain__modules__M21_nist-csf-2-0-planned]] — van planned naar active
- [[brain__sources__nist-csf-2-0]] — Core + Reference Tool + IE bron-detail
- [[brain__architecture__H-register]] — H33/H34/H35 nieuw geregistreerd

— Einde v4.5.0.
