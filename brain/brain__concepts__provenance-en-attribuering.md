---
type: concept
title: Provenance en attribuering
status: living
date: 2026-05-13
related:
  - canonical-metrics
sources:
  - projectinstructie-v1.6
chat-sources: []
confidence: high
---

# Provenance en attribuering

## Wat het is

**Provenance** = elke factuele claim of beslissing in het model moet **terug-traceerbaar** zijn naar zijn bron. **Attribuering** = wanneer de bron onder licentie valt (vooral CC-BY), moet de attributie expliciet zijn.

Het GRC Kennismodel onderscheidt drie soorten provenance:

| Type | Wat | Hoe |
|---|---|---|
| **Bron-data** | Welk extern document leverde deze content? | `dcterms:source` op individuals + module-level header-comments |
| **Beslissing-context** | Welke D-decision of sprint leidde tot dit element? | Inline `rdfs:comment` met "D-N (v-X)" verwijzing |
| **Brain-provenance** | Waar in onze eigen documentatie staat dit? | `sources:` en `chat-sources:` frontmatter-velden in brain-files |

## Licentie-bewustzijn

Het model bevat bronmateriaal onder **verschillende licenties**. Dit is architectuur-relevant omdat het dashboard straks extern kan worden gepubliceerd en bron-attribuering juridisch vereist is.

| Licentie | Voorbeelden | Vereiste |
|---|---|---|
| **NEN-restrictief** | ISO 27001/27002/27005/31000/22301/22313 | Alleen via gelicentieerde kanalen. **Geen tekst-reproductie in het model.** |
| **CC-BY 4.0** | CBW-Excel (ADR & NOREA), ENISA-guidance | Attributie verplicht via `ext:sourceAttribution` (gepland Fase 2) |
| **Publiek domein** | NIST CSF 2.0, NIST SP 800-53/39/30, NIST CSWP 29 | Geen attributie-eis, wel goede praktijk |
| **Publiek EU-recht** | NIS2, DORA, EU 2024/2690, AVG | Vrij herbruikbaar |
| **Publiek NL-recht** | VIR 2007, VIRBI 2025, BVA-stelsel, CIO-stelsel, CBW-wet, Cbb-concept | Vrij herbruikbaar |
| **Onbeperkt** | BIO 2.0 | Overheidspublicatie zonder restrictie |

## Toepassings-bewijs v4.3.3

`ext:sourceAttribution` als formele property bestaat nog niet (gepland Fase 2), maar licentie-discipline is in praktijk consistent toegepast:

- **Geen NEN-tekst verbatim** in model
- Externe bronnen geattribueerd in patch-rapporten en module-headers
- `dcterms:source` consistent gebruikt waar van toepassing (bv. `ext:hasHandreikingBBN` heeft `dcterms:source "Handreiking BIO2-opmaat v2.5"`)

## Structurele attribuering vanaf Fase 2

Nieuwe property `ext:sourceAttribution` (gepland v4.4.0):

- Op Laag 2–4 individuals (frameworks, controls, mappings)
- Triple-niveau in plaats van alleen ontology-metadata
- Reden: meerdere CC-BY-bronnen bestaan straks naast elkaar; dashboard-export moet per-bron attributie kunnen tonen

**Eerste verplichte toepassing:** ENISA-guidance via Route 5 (Fase 2, CC-BY 4.0, ~25kB tekst voor 73 van 93 BIO-controls).

## Brain-provenance (deze vault)

Elke brain-file heeft verplicht in frontmatter:

```yaml
sources:               # project knowledge-files (bv. patch-rapport-v4_3_0)
  - patch-rapport-v4_3_0
chat-sources:          # directe URL's naar bron-chats
  - https://claude.ai/chat/<uri>
```

`chat-sources` mag **leeg zijn** (`[]`) maar dan is een `gaps:`-entry verplicht die uitlegt waarom (zie [[brain__CLAUDE]]).

Wikilinks `[[...]]` binnen body documenteren cross-references tussen brain-files.

## Praktische gevolgen

- Elke nieuwe factuele claim in een D-, sprint- of H-file krijgt een bron
- Patch-rapporten verwijzen naar canonical_metrics-JSON, niet naar memoire (zie [[brain__concepts__canonical-metrics]])
- Externe bron-documenten worden in Project Knowledge geüpload zodat brain-files ze kunnen referen
- Bij twijfel over bron-status: liever lege `chat-sources: []` met `gaps:` dan een verkeerde verwijzing

## Status-historie van de discipline

| Datum | Mijlpaal |
|---|---|
| ±2026-03 | Initiële discipline (D5 verwijst naar Handreiking) |
| 2026-04-10 | `ext:hasHandreikingBBN` met `dcterms:source` (v4.1.0 Actie A) |
| 2026-05-09 | Licentie-bewustzijn formeel in projectinstructie v1.6 |
| Gepland v4.4.0 | `ext:sourceAttribution`-property toegevoegd |

## Hangt samen met

- [[brain__concepts__canonical-metrics]] — meetmethode-discipline gebruikt provenance-principe
- [[brain__CLAUDE]] — frontmatter-schema vereist `sources` en `chat-sources`

— Einde provenance en attribuering.
