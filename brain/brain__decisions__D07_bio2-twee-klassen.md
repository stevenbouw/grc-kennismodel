---
type: decision
id: D07
title: BIO 2.0 als twee klassen
status: active
date: 2026-03-16
related:
  - D05_sameAs-strikt-ctrl-bio
  - BBN-correctie
sources:
  - projectinstructie-v1.6
chat-sources:
  - https://claude.ai/chat/7b0a059c-d625-4942-9dbd-55e99c89e71c
confidence: high
---

# D07 — BIO 2.0 als twee klassen

## Beslissing

BIO 2.0 wordt gemodelleerd als **twee aparte klassen**, niet als één:

- `bio:BIOControl` — de 93 ISO 27002:2022-aligned controls (= ISO 27002 controls via `owl:sameAs`)
- `bio:OverheidsMaatregel` — de 148 aanvullende overheidsmaatregelen

## Aanleiding

ISO 27002:2022 controls en BIO 2.0 overheidsmaatregelen zijn fundamenteel verschillende type entiteiten:

- **ISO 27002-controls** zijn internationaal genormeerd, voor BIO overgenomen via 1:1-mapping → `bio:BIOControl` = `ctrl:ISO27002Control` (D5 sameAs-brug, 93 asserties)
- **Overheidsmaatregelen** zijn Nederland-specifieke *aanvullende* eisen, niet een verfijning van ISO-controls. Ze vullen aan, ze vervangen niet.

Eén klasse modelleren zou de juridische status verbloemen: een overheidsmaatregel is niet "een soort ISO-control"; het is een eigenstandige verplichting bovenop ISO.

## Implementatie

```turtle
bio:BIOControl rdfs:subClassOf ctrl:Control .
bio:OverheidsMaatregel rdfs:subClassOf ctrl:Control .  # direct subClass, niet via BIOControl

bio:OverheidsMaatregel_X biz:implementsControl bio:BIOControl_Y .  # relatie expliciet
```

## Wat het niet betekent

- D7 betekent niet dat overheidsmaatregelen los staan van ISO — ze worden via `biz:implementsControl` aan ISO-controls gekoppeld, expliciet
- D7 betekent niet dat één klasse "belangrijker" is — beide zijn verplicht voor de organisatie
- D7 betekent niet dat overheidsmaatregelen BBN-niveaus hebben — BBN is een Handreiking-eigenschap, niet een BIO 2.0-eigenschap. Zie [[brain__concepts__BBN-correctie]]

## Afgeleide consequenties

- Disjointness: `bio:BIOControl` en `bio:OverheidsMaatregel` zijn `owl:disjointWith` (logisch onmogelijk dat één entiteit beide is)
- Counts in metrics: 93 BIOControls + 148 OverheidsMaatregelen = 241 BIO 2.0-individuals
- SKOS-mappings tussen NIS2-eisen en BIO landen via beide klassen, afhankelijk van de eis-aard

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| ±2026-03-16 | active | Vaststelling (datum reconstructie via tech-chat 16/3/2026) |

— Einde D07.
