---
type: architecture
id: H33
title: H33 — m11 substantiële uitbreiding SP 800-53 (modelbeperking)
status: open
date: 2026-05-19
related:
  - H34_m11-enhancement-modellering
  - v4_5_0_fase-3-nist-csf-2-0
  - M11_nist-800-53
sources:
  - patch-rapport-v4_5_0
chat-sources: []
confidence: high
---

# H33 — m11 substantiële uitbreiding SP 800-53

## Status

**Open** — geregistreerd post-v4.5.0 (19 mei 2026). Trigger: Spoor B-organisatie heeft >50 niet-gemapte SP 800-53-controls nodig.

## Wat het is

Modelbeperking in M11: slechts **124 van ~1000 SP 800-53 Rev 5-controls** zijn opgenomen. Dit was acceptabel voor Fase 1-3 (referentie-gebruik), maar wordt knellend bij serieus operationeel gebruik.

In Stap 6 van v4.5.0 (CSF Reference Tool / OLIR-mappings) bleken **108 unique unresolved SP 800-53-targets** te bestaan — controls die de NIST Reference Tool noemt als CSF-gerelateerd maar niet in M11 staan.

## Waarom dit een open vraag is

Bij Spoor B-activatie (organisatie-specifieke invulling) is de keuze:

| Optie | Voor | Tegen |
|---|---|---|
| **A — Volledige SP 800-53 R5 opnemen** | Geen unresolved meer; volledige mapping-dekking | ~1000 - 124 = ~876 nieuwe individuals; significante M11-uitbreiding; mogelijk performance-impact |
| **B — Status quo behouden** | Geen werk | Unresolved blijft groeien bij nieuwe SKOS-mapping-sprints |
| **C — Incrementeel uitbreiden op vraag** | Pragmatisch | Geen voorspelbare modelstaat; per-sprint instabiliteit |

**Voorkeur (informeel):** geen actie tot Spoor B-trigger zich voordoet. Optie A is correct maar te duur zonder operationele noodzaak.

## Trigger-criterium

Spoor B-organisatie heeft **>50 niet-gemapte SP 800-53-controls nodig** voor operationele compliance-vraag (bv. bij FedRAMP-equivalente eis of leveranciers-assurance).

## Verschil met H34

H33 gaat over **breedte** (meer controls). H34 gaat over **diepte** (enhancements per control — bv. `AC-2(1)`, `CM-07(02)`).

Beide raken M11. Bij gelijktijdige trigger zou een M11-uitbreidings-sprint H33 en H34 samen oppakken.

## Hangt samen met

- [[brain__architecture__H34_m11-enhancement-modellering]] — gerelateerde M11-modelbeperking
- [[brain__modules__M11_nist-800-53]] — module
- [[brain__sprints__v4_5_0_fase-3-nist-csf-2-0]] — sprint waar de unresolved zijn gedocumenteerd

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-19 | open | Geregistreerd post-v4.5.0 op basis van 108 unique unresolved SP 800-53-targets in Stap 6 |

— Einde H33.
