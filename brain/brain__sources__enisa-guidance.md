---
type: source
title: ENISA Technical Implementation Guidance — apart bestand (CC-BY 4.0)
status: living
date: 2026-05-13
related:
  - v4_4_0_fase-2-cbw-cbb
  - cbw-excel
  - provenance-en-attribuering
sources: []
chat-sources: []
confidence: high
---

# ENISA Technical Implementation Guidance

## Status

**Kandidaat-bron voor Fase 3 of later** (v4.5.0+). Niet geïntegreerd in v4.4.0. Beschikbaar als apart PDF-bestand in Project Knowledge.

## Bron-identificatie

| Aspect | Detail |
|---|---|
| Officiële titel | ENISA Technical Implementation Guidance for the NIS2 Directive |
| Uitgever | European Union Agency for Cybersecurity (ENISA) |
| Bestand in PK | `ENISA_Technical_implementation_guidance_*.pdf` |
| Licentie | CC-BY 4.0 (typisch voor ENISA-publicaties — moet bij integratie geverifieerd worden) |

## Wat het is

ENISA's eigen technische implementatie-guidance voor NIS2. Geen wettelijke verplichtende tekst maar een **interpretatieve hulpbron** vanuit het EU-perspectief, naast (en mogelijk parallel met) ADR/NOREA's nationale UV-decompositie in [[brain__sources__cbw-excel]].

## Correctie t.o.v. eerdere aanname

### Wat v1.6 (oude analyse-chat Opdracht 1.0, 20 april 2026) suggereerde

> "ENISA-guidance via CBW-Excel op 73 van 93 BIO-controls (~25kB)."

### Werkelijke situatie (v4.4.0-verificatie)

ENISA-guidance bevindt zich **niet** in CBW-Excel. CBW-Excel sheet 3 kolom H bevat ADR/NOREA's eigen UV-decompositie — geen ENISA-tekst. De ~25kB die in v1.6 werd toegeschreven aan "ENISA-guidance" is in werkelijkheid de UV-interpretatie van ADR/NOREA.

ENISA TIG is een **apart PDF-document** dat los van CBW-Excel beschikbaar is.

## Kandidaat-integratie v4.5.0+

Bij eventuele toekomstige integratie:

| Aspect | Verwacht |
|---|---|
| Property | `ext:hasENISAGuidance` (naam komt vrij door v4.4.0-hardverwijdering — retrofit-mogelijk) |
| Subject | Hoogstwaarschijnlijk NIS2-Requirement-individuals of CBW-controls — afhankelijk van structuur ENISA-tekst |
| Granularity | Te bepalen — vermoedelijk per NIS2-artikel, niet per BIO-control |
| Module | M10 (`m10-nis2-ext.ttl`) of nieuwe submodule |
| Licentie | Te verifiëren bij upload (vermoedelijk CC-BY 4.0) — `ext:SourceAttribution`-individual nodig |
| Triple-impact | Te bepalen — afhankelijk van granularity-keuze |

## Triggers voor opname

| Trigger | Beoogd moment |
|---|---|
| **Analyse-opdracht 2.0** | Bron-inspectie + scope-bepaling vóór TBox-declaratie (per sprint-protocol "bron-verificatie") |
| **Spoor C activatie** | Bij toezicht-gerelateerde queries kan ENISA-guidance toegevoegde waarde leveren |
| **Fase 3 vrij ontwerpmoment** | Bij M21 NIST CSF 2.0-integratie kan ENISA mee-genomen worden indien EU↔US-mapping zinvol blijkt |

## Lesson learned (v4.4.0)

Pre-sprint-inventarisatie (Sprint-protocol B) ontdekte het verschil tussen verwachte ENISA-tekst en werkelijke UV-decompositie. Bron-verificatie vóór TBox-declaratie (Sprint-discipline v1.7) is hier expliciet uit voortgekomen — `ext:hasENISAGuidance`-naam was met v1.6-aanname als zekerheid behandeld, niet als hypothese.

Zie [[brain__workflow__sprint-protocollen]] voor de formalisering van bron-verificatie als sprint-discipline.

## Cross-references

- [[brain__sources__cbw-excel]] — bevat de werkelijke UV-decompositie (Route 5), géén ENISA-tekst
- [[brain__sprints__v4_4_0_fase-2-cbw-cbb]] — sprint waar deze correctie is geformaliseerd
- [[brain__modules__M10_nis2-ext]] — module waar `ext:hasUVInterpretation` is geland (vervanging van `ext:hasENISAGuidance`)
- [[brain__workflow__sprint-protocollen]] — bron-verificatie als geformaliseerd sprint-protocol

— Einde ENISA-guidance source.
