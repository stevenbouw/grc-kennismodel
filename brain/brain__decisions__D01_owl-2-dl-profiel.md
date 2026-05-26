---
type: decision
id: D01
title: OWL 2 DL profiel
status: active
date: 2026-03-01
related:
  - D02_turtle-serialisatie
  - D04_skos-cross-framework
sources:
  - projectinstructie-v1.6
chat-sources:
  - https://claude.ai/chat/76420a5b-11ac-4f22-af7a-5e2404201bdd
confidence: medium
gaps:
  - "Exacte datum vaststelling onbekend (geen specifieke beslissing-chat gevonden); datum 2026-03-01 is conservatieve schatting op basis van vroege project-fase"
---

# D01 — OWL 2 DL profiel

## Beslissing

Het GRC Kennismodel wordt gebouwd binnen het **OWL 2 DL profiel** — geen OWL Full, geen onbeslisbare constructies.

## Aanleiding

OWL 2 DL biedt het beste evenwicht tussen expressiviteit en beslisbaarheid. Reasoners als HermiT en Pellet kunnen DL-modellen volledig valideren op consistentie en onverwachte inferenties detecteren. OWL Full zou meer flexibiliteit bieden (bijv. metaclasses), maar geen reasoner kan dat volledig afhandelen — een onaanvaardbaar risico voor een audit-relevant model.

## Implementatie

- Elke nieuwe constructie wordt getoetst op DL-compliance vóór commit
- HermiT (Protégé) en `owlrl.OWLRL_Semantics` (rdflib/pySHACL) zijn de canonieke validators
- Bekend OWL Full-risico (punning) wordt actief vermeden

## Afgeleide consequenties

- [[brain__decisions__D02_turtle-serialisatie]] — Turtle als format dat DL-compatible werkt
- Reasoning-vereiste OWL RL of sterker in alle technische conventies
- Klassen en properties moeten disjoint blijven van metalogica-constructies

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| ±2026-03 | active | Vaststelling (datum reconstructie) |

— Einde D01.
