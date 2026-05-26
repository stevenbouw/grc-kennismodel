---
type: sprint
id: v4.4.0
title: v4.4.0 — Fase 2: CBW + Cbb + UV-decompositie
status: active
date: 2026-05-13
related:
  - v4_3_3_d12-en-predicate-consolidatie
  - D09_framework-neutraliteit
  - D12_drie-laags-compliance
  - H32_obl-laag-asymmetrie
sources:
  - projectinstructie-v1.7
chat-sources: []
confidence: high
---

# v4.4.0 — Fase 2: CBW + Cbb + UV-decompositie

## Status

**Huidige actieve baseline** sinds 13 mei 2026. Opvolger van v4.3.3.

Bron: projectinstructie-v1.7, patch-rapport-v4_4_0.md.

## Scope: vier hoofditems + twee scope-addenda

| Item | Inhoud |
|---|---|
| 1 | CBW-laag — 26 controls als `ctrl:CBWControl` ⊑ `ctrl:Control` (control-tak, niet compliance-tak) |
| 2 | Cbb-laag — 14 zorgplichtartikelen (art. 6–19) als `compl:LegalObligation`; art. 18 als `compl:SupplierExclusionOrder` |
| 3 | UV-decompositie (Route 5) — ADR/NOREA's interpretatieve uitwerking van EU 2024/2690 op CBW-Control-niveau via `ext:hasUVInterpretation` |
| 4 | Sheet 9 mappings — 290 sheet-relaties → 183 unieke RDF-triples (37% dedup) op 81 BIO-Controls |
| Add. 1 | Drie wijzigingen na Stap 1-inventarisatie: sheet 9 op BIO-Control-niveau, geen AMvB-subklasse, BIO 5.33-acceptatie |
| Add. 2 | Route 5 herdefinitie (Scenario X), `ext:hasENISAGuidance` → `ext:hasUVInterpretation`, drie domain-versoepelingen |

## Wijzigingen per module

| Module | Wijziging |
|---|---|
| **grc-core.ttl** | TBox: 3 nieuwe klassen + 3 nieuwe properties + hardverwijdering `ext:hasENISAGuidance` |
| **M01 (framework)** | `fw:Cbb`-individual + `fw:uitgewerktIn` / `fw:werktUit` inverse-paar + `fw:CBW fw:uitgewerktIn fw:Cbb`-aanvulling |
| **M05 (compliance)** | `compl:SupplierExclusionOrder`-klasse + 14 Cbb-Art-individuals (compl:LegalObligation, art. 18 als SupplierExclusionOrder) |
| **M08 (BIO 2.0)** | Sheet 9 mappings op 81 BIO-Controls (CBW ↔ Cbb ↔ BIO) |
| **M10 (NIS2 ext)** | `ctrl:CBWControl`-klasse + 26 CBW-Control-individuals + 1 `ext:SourceAttribution` — eerste TBox-element in m10 |

## Triple-impact

| Metric | v4.3.3 | v4.4.0 | Δ |
|---|---:|---:|---:|
| Pre-inferentie triples | 12.739 | 13.441 | **+702** |
| Post OWL RL | 29.863 | 31.415 | +1.552 |
| Klassen | 186 | 189 | +3 |
| NamedIndividuals | 637 | 679 | +42 |
| ObjectProperties | 140 | 143 | +3 |
| DatatypeProperties | 84 | 93 | +9 |
| `owl:sameAs` | 98 | 98 | 0 |
| SKOS-mappings | 346 | 346 | 0 |
| SHACL RUN 1 | 0 | 0 | 0 |
| SHACL RUN 2 | 290 | 290 | 0 |

## Architectuur-betekenis

**Correctie op v1.6-aannames:**

1. **`compl:ComplianceArticle` bestond niet.** v1.6 plande Cbb-zorgplichtartikelen als `compl:ComplianceArticle`. Werkelijk: deze klasse bestond niet als TBox-declaratie in v4.3.3. Gecorrigeerd: Cbb-zorgplichtartikelen worden `compl:LegalObligation`, consistent met VIR/VIRBI/AVG/BVA-precedent.

2. **CBW-controls horen in control-tak, niet compliance-tak.** v1.6 was hier niet expliciet over. v4.4.0 plaatst 26 CBW-controls als `ctrl:CBWControl` ⊑ `ctrl:Control`. Rationale: het zijn beheersmaatregelen, geen wettelijke verplichtingen.

3. **Cbb-artikel-aantal: 14, niet 13.** v1.6 parafraseerde "art. 6–17, 19" wat 13 artikelen suggereerde. Correct: art. 6 t/m 19 inclusief (14 artikelen). Art. 18 (supplier-exclusion) wel meegeteld. Art. 5 is een verwijzings-artikel naar art. 6–19 en wordt niet als zelfstandige zorgplicht-individual gemodelleerd.

4. **Route 5 herdefinitie.** v1.6 zei "ENISA-guidance via CBW-Excel op 73 van 93 BIO-controls". Werkelijk: CBW-Excel bevat ADR/NOREA's UV-decompositie op CBW-Control-niveau (26 controls, ~25kB, sheet 3 kolom H). Geen ENISA-tekst in CBW-Excel. Geen UV-propagatie naar BIO-controls in de bron. ENISA TIG-PDF is een apart bestand, kandidaat voor v4.5.0+ als aparte route.

**D9-bevestiging op twee clusters.** v4.4.0 is de eerste sprint die framework-neutraliteit aantoonbaar test op twee framework-clusters: NIS2-EU (richtlijn → CBW via `fw:isTranspositieVan`) en CBW-NL (wet → Cbb via `fw:uitgewerktIn`). Het patroon werkt zonder dat één cluster architectureel-bevoorrecht is.

**D12-verfijning.** v4.3.3 introduceerde de drie-laags compliance-architectuur. v4.4.0 verfijnt: D12 is een **patroon**, geen starre symmetrie per cluster. NIS2 wordt toegepast als regulatory→legal→requirement-keten; CBW/Cbb als legal-only-keten zonder regulatory-laag (CBW en Cbb zijn beide `compl:LegalObligation`).

## Sprint-protocollen formeel geldend per v1.7

v4.4.0 was de eerste sprint waar nieuwe protocollen werden toegepast en bewezen:

| Protocol | Toepassing v4.4.0 |
|---|---|
| Protocol B — Pre-sprint-inventarisatie | 5 inventarisatie-vragen leverden 5 signalen; 4 architectuur-keuze-relevant; 1 fundamentele Route 5-correctie ontdekt |
| Protocol C — Schema-meta-rapport | Niet uitgevoerd in v4.4.0 (eenmalig artefact v4.3.3); herziening overwogen post-sprint |
| Bron-verificatie vóór TBox-declaratie | `ext:hasENISAGuidance`-naming-correctie kostte één addendum-ronde |
| Raming-discipline | Sheet 9-aggregatie: 290 → 183 unieke triples (37% dedup) — bij correcte raming was originele +290 naar +183-200 bijgesteld |
| Patch-rapport §9 verplicht | Geparkeerde-items-status-update geïntroduceerd in v4.4.0-patch-rapport |

## Scope-pauzes en addenda

**Addendum 1** — na Stap 1-inventarisatie:
- Sheet 9 op BIO-Control-niveau (was: op overheidsmaatregel-niveau)
- Geen AMvB-subklasse (Cbb-Art direct als compl:LegalObligation)
- BIO 5.33-acceptatie (specifieke uitzondering)

**Addendum 2** — Route 5 fundamentele herdefinitie:
- Werkelijke CBW-Excel-inhoud is UV-decompositie, niet ENISA-tekst
- Property hernoemd: `ext:hasENISAGuidance` → `ext:hasUVInterpretation`
- Drie domain-versoepelingen

## Nieuwe geparkeerde / aandachts-items

- **H32** — [[brain__architecture__H32_obl-laag-asymmetrie]] — OBL-laag modelleringsasymmetrie tussen 3 OBL_NIS2 (uitgebreide property-set) en 35 overige LegalObligations (minimale property-set). Trigger: na v4.5.0 of bij Spoor B-organisatorische invulling.

- **`ext:hasENISAGuidance` hardverwijdering** — geregistreerd voor eventuele retrofit bij echte ENISA TIG-integratie (Analyse-opdracht 2.0 of v4.5.0+).

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-13 | active | Oplevering v4.4.0 Fase 2 + 2 addenda + projectinstructie v1.7 |

## Bestand-wijzigingen

5 bestanden gewijzigd (grc-core, m01, m05, m08, m10); overige 17 ongewijzigd t.o.v. v4.3.3.

## Cross-references

- [[brain__sprints__v4_3_3_d12-en-predicate-consolidatie]] — voorganger met D12-introductie
- [[brain__decisions__D09_framework-neutraliteit]] — getest op twee clusters in deze sprint
- [[brain__decisions__D12_drie-laags-compliance]] — verfijnd in deze sprint
- [[brain__architecture__H32_obl-laag-asymmetrie]] — nieuw H-item, geregistreerd in deze sprint
- [[brain__sources__cbw-excel]] — Route 5-bron, herdefinieerd
- [[brain__workflow__sprint-protocollen]] — sprint-protocollen formeel sinds v1.7 (folder workflow)

— Einde v4.4.0.
