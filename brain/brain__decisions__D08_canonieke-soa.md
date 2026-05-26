---
type: decision
id: D08
title: Eén canonieke SoA (v4.2.2 Route A)
status: active
date: 2026-04-13
related:
  - D05_sameAs-strikt-ctrl-bio
  - D09_framework-neutraliteit
sources:
  - projectinstructie-v1.6
chat-sources:
  - https://claude.ai/chat/95d2b45f-4d7a-48f2-a4c2-e47d6e4d4a0f
  - https://claude.ai/chat/f527e7ab-bc17-44f4-a878-598e8ca7a632
confidence: high
---

# D08 — Eén canonieke SoA (v4.2.2 Route A)

## Beslissing

Het GRC Kennismodel kent **één canonieke Statement of Applicability**:

- `isms:SoA_2026` als de SoA-container (één instance)
- 93 `isms:SoAEntry_*`-individuals, één per ISO 27002-control
- Default-status per entry: "Nog niet beoordeeld"

Niet meerdere parallelle SoA-versies of duplicaat-shells.

## Evolutie

Deze beslissing kent twee fasen:

**Initieel:** "SoA met 93 shells" — één entry per ISO 27002-control, default "Nog niet beoordeeld". Geformuleerd in early-project ontwerpbesluiten.

**v4.2.2 Route A (13 april 2026):** SoA-canonisering uitgevoerd. In v4.2.1 was per ongeluk een tweede SoA-container ontstaan (`SOA_v1`) plus 15 duplicate SoAEntry-individuals (Scenario 2 unintended duplication). Route A: verwijder de duplicaten en de oude container, voeg één canonisering-mirror-triple toe na expliciete masterchat-GO. Resultaat: schone `isms:SoA_2026` + 93 unieke `SoAEntry_*`.

## Aanleiding

Een Statement of Applicability is per definitie één document per organisatie per beoordelingsmoment. Meerdere parallelle SoA-instances zou:
- Audit-trail verwarrend maken (welke is "de" SoA?)
- SPARQL-queries dwingen tot disambigueren
- Aansluiting met externe assessor-tools belemmeren

## Implementatie

```turtle
isms:SoA_2026 a isms:StatementOfApplicability ;
  dcterms:date "2026"^^xsd:gYear ;
  rdfs:label "Statement of Applicability 2026"@nl, "Statement of Applicability 2026"@en .

isms:SoAEntry_5_01 a isms:SoAEntry ;
  isms:forControl ctrl:ISO27002_5_01 ;  # via D5 sameAs ook bio:ISO27002_5_01
  isms:applicabilityStatus isms:Status_NogNietBeoordeeld .
# × 93
```

## Afgeleide consequenties

- SoA-update is een wijziging per `SoAEntry_*`, niet creatie van een nieuwe SoA-container
- Bij jaarwisseling: `SoA_2026` blijft, status-evolutie via audit-trail; ten tijde van schrijven geen besluit over `SoA_2027` (Spoor C-vraag)
- Afkappingsbug `SoAEntry_5_02` opgelost in v4.3.1 B₂

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| ±2026-03 | active | Initiële vaststelling "SoA met 93 shells" |
| 2026-04-13 | active | Route A canonisering (v4.2.2) — duplicate-cleanup |
| 2026-04-20 | active | Afkappingsbug `SoAEntry_5_02` opgelost (v4.3.1 B₂) |

— Einde D08.
