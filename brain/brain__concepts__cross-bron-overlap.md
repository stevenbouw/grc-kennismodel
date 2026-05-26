---
type: concept
title: Cross-bron-overlap als SKOS-kwaliteits-indicator
status: living
date: 2026-05-19
related:
  - v4_5_0_fase-3-nist-csf-2-0
  - provenance-en-attribuering
  - nist-csf-2-0
  - cbw-excel
sources:
  - patch-rapport-v4_5_0
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

— Einde cross-bron-overlap.
