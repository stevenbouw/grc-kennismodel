---
type: concept
title: Cross-bron-overlap als SKOS-kwaliteits-indicator
status: living
date: 2026-05-29
related:
  - v4_5_0_fase-3-nist-csf-2-0
  - provenance-en-attribuering
  - nist-csf-2-0
  - cbw-excel
  - cross-category-mappings
sources:
  - patch-rapport-v4_5_0
  - t4-pre-sprint-inventarisatie
chat-sources: []
confidence: high
---

# Cross-bron-overlap als SKOS-kwaliteits-indicator

## Wat het is

**Cross-bron-overlap** is het fenomeen dat twee of meer **onafhankelijke bronnen** dezelfde SKOS-mapping leggen tussen dezelfde subject en object. In v4.5.0 voor het eerst geconstateerd en gedocumenteerd als methodologisch leerpunt.

**Concrete observatie v4.5.0:**

- **Bron 1 — Sheet 8 (ADR & NOREA)** levert ISO 27001-mappings vanuit CSF Subcategories
- **Bron 2 — CSF Reference Tool (NIST)** levert ISO 27001-mappings vanuit CSF Subcategories
- **Overlap**: 105 identieke `csf:Subcategory ↔ ISO27001`-mappings tussen de twee bronnen

## Wat het NIET is

| Geen | Reden |
|---|---|
| **Technisch dedup-feit** | De 105 mappings worden niet dubbel in het model opgenomen, maar zelfs vóór dedup zijn ze al een interessant signaal |
| **Bewijs van correctheid** | Bron-onafhankelijkheid is een nodige, geen voldoende voorwaarde voor correctheid |
| **Validatie tegen werkelijkheid** | Het is bron-onderlinge consistentie, geen empirische verificatie |

## Wat het WEL is

**SKOS-kwaliteits-validatie via bron-onafhankelijkheid.** Het feit dat twee onafhankelijk samengestelde bronnen dezelfde mapping leggen, vergroot de waarschijnlijkheid dat die mapping correct is.

| Aspect | Implicatie |
|---|---|
| Twee onafhankelijke teams (ADR/NOREA + NIST) | Komen tot dezelfde mapping-conclusie |
| Twee verschillende methodieken | Komen op zelfde plek uit |
| Twee verschillende publicatie-data | Geen wederzijdse beïnvloeding |

Bij **divergentie** tussen bronnen: kandidaat voor nadere inspectie, mogelijk fout in een van beide bronnen.

## Architectuur-implicatie

Cross-bron-overlap is een **emergente kwaliteits-indicator** — het ontstaat vanzelf bij gebruik van meerdere bronnen voor hetzelfde domein, mits provenance correct wordt geadministreerd via `ext:SourceAttribution`.

### Voorwaarden voor detectie

| Voorwaarde | Beschikbaar in model |
|---|---|
| Multiple bronnen voor zelfde mapping-domein | ✓ (v4.5.0: CBW-Excel + CSF Reference Tool) |
| `ext:sourceAttribution` per mapping | ✓ (provenance-discipline) |
| Detecteerbaarheid via SPARQL | ✓ (queries op `?map ?p ?map` patroon mogelijk) |

### Detection-query (illustratief)

```sparql
SELECT ?subject ?object (COUNT(DISTINCT ?attribution) AS ?bron_count)
WHERE {
  ?subject skos:closeMatch ?object ;
           ext:sourceAttribution ?attribution .
}
GROUP BY ?subject ?object
HAVING (?bron_count >= 2)
```

Bij `bron_count >= 2`: cross-bron-overlap gevonden — kwaliteits-positief signaal.

## Toepassings-bewijs v4.5.0

| Bron-paar | Overlap |
|---|---:|
| Sheet 8 (ADR/NOREA) ∩ CSF Reference Tool (NIST) | **105 mappings** |

105 keer twee onafhankelijke bronnen die hetzelfde zeggen — substantieel kwaliteits-bewijs. Niet bewijs van correctheid, wel signaal voor mapping-betrouwbaarheid.

## Toekomstige uitbreidingen

| Mogelijk bron-paar | Domein |
|---|---|
| OLIR (Online Informative References) — bij latere integratie | CSF ↔ andere kaders |
| ENISA TIG ∩ CBW UV-decompositie | NIS2 ↔ technische uitwerking |
| Multiple consultants/audit-firma's | Bedrijfs-specifieke mappings (Spoor B) |

## T4-bevinding (29 mei 2026) — de 105 is een bron-niveau-getal, niet machine-reproduceerbaar

De T4-pre-sprint-inventarisatie (`output/reports/t4-pre-sprint-inventarisatie.md`, READ-ONLY, geen mutatie) toetste de detection-query hierboven op het feitelijke model en legde een belangrijke nuance bloot: **de 105-overlap is niet uit het model afleidbaar via de illustratieve detection-query.** Drie bevindingen:

1. **De ±105 is een bron-niveau-getal uit v4.5.0** (Sheet 8 XLSX ∩ CSF Reference Tool XLSX), berekend tijdens de v4.5.0-analyse — niet reconstrueerbaar uit de model-triples. Machine-meetbaar in het model: csf↔ISO27001 mandatory clauses (eis, `ext:ISMSRequirement`) = **245 unie** (m21 Sheet 8: 147 / m09 Reference Tool: 117 / intersectie **19**); csf↔Annex A (measure, `bio:ISO27002` via D5-brug) = **494**, uitsluitend in m21 (m09 = 0). De twee bronnen gebruikten **verschillende ISO-target-resoluties** (Sheet 8: Annex A → `bio:`, clausule → `ext:`; Reference Tool in m09: alleen clausule → `ext:`), waardoor bron-overeenstemming op Annex A-niveau structureel **niet als identieke triple** verschijnt.
2. **Provenance is niet per-triple, maar block-comment-niveau** (bewuste modelleer-keuze, masterchat v4.5.0 Stap 5-GO). De `ext:sourceAttribution`-triples staan op de csf-knopen (CSF Core-herkomst), niet op de mapping-triples. Daardoor draagt elk csf↔ISO-paar machinaal één attribution, nooit twee — de `HAVING (?bron_count >= 2)`-query levert **0**, niet 105.
3. **De detection-query is daarom op dit model niet toepasbaar zoals beschreven.** Dit is geen administratie-fout maar een gevolg van de block-level-provenance-keuze; het maakt de overlap-set echter niet model-intern detecteerbaar.

**Gevolg voor dit concept:** cross-bron-overlap blijft een geldige *emergente kwaliteits-indicator*, maar de detection-query hierboven is **alleen toepasbaar als provenance per-triple wordt geadministreerd**. Of dat wenselijk is (per-triple `ext:sourceAttribution` zodat overlap voortaan machine-detecteerbaar wordt) is een **architectuur-vraag voor masterchat** (T4-beslispunt 4) — niet door Brein te beslissen. T4 zelf is afgesloten als **inventarisatie-only, geparkeerd (Optie B)**; geen mutatie, baseline ongewijzigd. Zie ook [[brain__concepts__cross-category-mappings]] voor de csf↔ISO27001 cross-category-predicaat-vraag.

## Relatie tot G1 "bij twijfel niet leggen"

Cross-bron-overlap is een **complement** van G1, niet een vervanging:

- **G1**: niet leggen als niet bewezen → conservatief
- **Cross-bron-overlap**: extra zekerheid bij wél leggen → kwaliteitsverhogend

Beide werken samen: G1 voorkomt valse mappings, cross-bron-overlap bevestigt echte mappings.

## Cross-references

- [[brain__sprints__v4_5_0_fase-3-nist-csf-2-0]] — sprint waarin het patroon werd ontdekt
- [[brain__concepts__provenance-en-attribuering]] — voorwaarde-discipline (SourceAttribution)
- [[brain__sources__nist-csf-2-0]] — een van de twee bronnen
- [[brain__sources__cbw-excel]] — andere van de twee bronnen
- [[brain__sources__source-register]] — cumulatieve bron-patronen

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-19 | living | Concept geboren uit v4.5.0 Stap 5 ∩ Stap 6-observatie (105 mappings) |
| 2026-05-29 | living | T4-bevinding toegevoegd: de 105 is een bron-niveau-getal (v4.5.0), niet machine-reproduceerbaar uit het model (block-level provenance → detection-query levert 0). Model-meetbaar: 245 clausule-unie (intersectie 19) + 494 Annex A (m21-only). Per-triple-provenance is een open architectuur-vraag voor masterchat (T4-beslispunt 4). T4 afgesloten als inventarisatie-only, geparkeerd (Optie B) |

— Einde cross-bron-overlap.
