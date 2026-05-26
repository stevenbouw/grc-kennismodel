---
type: decision
id: D02
title: Turtle-serialisatie
status: active
date: 2026-03-01
related:
  - D01_owl-2-dl-profiel
sources:
  - projectinstructie-v1.6
chat-sources:
  - https://claude.ai/chat/76420a5b-11ac-4f22-af7a-5e2404201bdd
confidence: medium
gaps:
  - "Exacte datum vaststelling onbekend; datum 2026-03-01 is conservatieve schatting"
---

# D02 — Turtle-serialisatie

## Beslissing

**Turtle** (`.ttl`) is het primaire werkformaat voor alle ontologie-bestanden. Niet RDF/XML, niet JSON-LD.

## Aanleiding

Turtle is mens-leesbaar, compact, en de-facto standaard voor handmatig OWL-werk. RDF/XML is verbose en moeilijk te diffen in git. JSON-LD is browser-vriendelijk maar minder handig voor reasoning-werk in Protégé.

## Implementatie

- Alle 20 modules zijn `.ttl`-bestanden (M01–M18 plus grc-core.ttl en grc-bridges.ttl)
- Shapes-bestand `grc-shacl.ttl` ook in Turtle
- Demo-SPARQL `m18-demo-sparql.rq` als aparte query-file
- Bij dashboard-export wordt Turtle eventueel naar JSON-LD geconverteerd; bronformaat blijft Turtle

## Afgeleide consequenties

- Git-diffs blijven leesbaar en reviewbaar
- Alle technische conventies (canonical metrics, gesplitste SHACL) opereren op Turtle-bestanden via rdflib
- Module-splitsing via `owl:imports` is Turtle-conform

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| ±2026-03 | active | Vaststelling (datum reconstructie) |

— Einde D02.
