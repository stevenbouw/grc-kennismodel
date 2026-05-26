---
type: architecture
id: H40
title: H40 — Dashboard-UI rendert <10% van data-velden uit JSON-export
status: parked
date: 2026-05-26
related:
  - skos-export-filter
  - namedindividual-telmethode
sources:
  - handover-dashboard-chat-v1
chat-sources: []
confidence: high
---

# H40 — Dashboard-UI rendert <10% van data-velden uit JSON-export

## Status

**Parked** — geregistreerd post-v4.6.0 in polish-mini-sprint (iteratie 12). Trigger: UI-moderniseringssprint na Fase 4 (al genoemd in migratie-roadmap).

## Scope-afbakening (belangrijk)

H40 betreft uitsluitend de **`grc-explorer-*.html`-UI** (Spoor A, ontologie-graaf-verkenner). H40 raakt **niet** aan de parallelle `grc-dashboard-v3-2`-productlijn (Spoor B, lokaal prototype) — die heeft een eigen datamodel uit SQL.js en een ander UI-doel (CRUD, audit-trail, kalender, RACI). Zie [[brain__concepts__dashboard-productlijnen]] voor het onderscheid.

## Wat het is

De `grc-data-v4_6_0.js`-export bevat per node meer velden dan de huidige `grc-explorer-v4_6_0.html`-UI toont. Schatting: **<10% renderdekking**. De UI is read-only ontologie-graaf-verkenner met focus op IRI/type/label + edge-navigatie via Cytoscape. Aanvullende node-context die wel in de JSON staat maar in de UI niet zichtbaar is, omvat onder meer:

| Veldcategorie | In JSON aanwezig | In UI getoond |
|---|---|---|
| `rdfs:label`@nl / @en | ✓ | ✓ (één taal als label) |
| `rdfs:comment`@nl / @en | ✓ | ✗ of beperkt (tooltip-niveau) |
| `rdf:type` (alle types) | ✓ | gedeeltelijk (primair type) |
| `owl:sameAs`-targets | ✓ | edge-only |
| SKOS-mapping-types (exact/close/related) | ✓ | edge-only, type-onderscheid niet visueel onderscheidend |
| `ext:sourceAttribution`-referentie | ✓ | ✗ |
| Bron-citaten via SourceAttribution-individu | ✓ | ✗ |
| Classificatie-attributen (BBN-niveau, Tier, CapabilityLevel) | ✓ | ✗ |
| Cross-framework-context | ✓ | impliciet via edges |

Het exacte percentage is niet gemeten — "<10%" is conservatieve schatting van het Fase 0 Dashboard-handover-rapport.

## Waarom dit een open vraag is

Het is **geen bug** — het is een bewuste scope-keuze: de explorer is bedoeld als graaf-navigator, niet als detail-viewer. Maar de gap heeft drie gevolgen:

| Gevolg | Impact |
|---|---|
| Demonstratie-waarde beperkt | Externe stakeholders zien graaf maar niet de rijkdom van de onderliggende ontologie |
| Audit-spoor onzichtbaar | SourceAttribution en bron-citaten zijn juist het verschil tussen "willekeurige RDF" en "verifieerbare GRC-kennisbasis" |
| Cross-framework-uitleg ontbreekt | D9-framework-neutraliteit en D11-asset-convergentie zijn de architecturale kern, maar zichtbaar alleen via edge-tracing |

## Trigger-criterium

| Trigger | Wanneer renderdekking aanpakken |
|---|---|
| UI-moderniseringssprint post-Fase 4 | Al voorzien in migratie-roadmap; H40 is dan inhoudelijke scope-input |
| Externe demo-vraag met audit-aspect | Bv. presentatie aan auditor / NOREA — dan rdfs:comment + SourceAttribution minimaal vereist |
| Tweede dashboard-iteratie (na v3-2-prototype) | Als Spoor B-prototype lessen oplevert die ook explorer-relevant zijn |

## Aanpak bij activering (toekomst, niet nu)

Niet uitgewerkt — natuurlijke vorm is een UI-moderniseringssprint met dashboard-subagent-instructie, scope-gebaseerd op:

1. Inventarisatie welke velden uit JSON momenteel niet renderen (per node-type)
2. Per veldcategorie: prioriteit voor zichtbaarheid (label > comment > attributie > overig)
3. UI-component-keuze (side-panel, tooltip, modal, in-node)
4. Performance-impact op Cytoscape-render (groot aantal nodes met rijke data kan layout vertragen)

## Hangt samen met

- [[brain__concepts__dashboard-productlijnen]] — scope-afbakening Spoor A explorer vs Spoor B dashboard
- [[brain__concepts__skos-export-filter]] — verwante meet-laag-discrepantie (1.798 ontologie vs 1.759 export); H40 is een latere stap in dezelfde pipeline (export → render)
- [[brain__concepts__namedindividual-telmethode]] — render gebruikt individual-set; class-niveau-content (SKOS-class-edges) wordt al niet geëxporteerd én niet gerenderd
- `dashboard/build_grc_explorer_v3.py` — export-pipeline-zijde van dezelfde pijplijn
- `dashboard/grc-explorer-v4_6_0.html` — render-zijde waar de gap zit
- `docs/handovers/handover-dashboard-chat-v1.md` — handover-rapport waarin het <10%-cijfer is genoemd

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-26 | parked | Geregistreerd in iteratie 12 polish-mini-sprint, oorspronkelijk uit Fase 0 Dashboard-handover-rapport |

— Einde H40.
