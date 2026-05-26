---
type: architecture
id: H36
title: H36 — 28 ctrl→compl exactMatch-pairs audit
status: parked
date: 2026-05-26
related:
  - v4_6_0_fase-4-ensia-en-volwassenheid
  - skos-export-filter
  - sameAs-discipline
sources:
  - sessie-rapport-v2_0
  - patch-rapport-v4_6_0
chat-sources: []
confidence: high
---

# H36 — 28 ctrl→compl exactMatch-pairs audit

## Status

**Parked** — geregistreerd post-v4.6.0 in polish-mini-sprint (iteratie 12). Trigger: SKOS-kwaliteitsanalyse-sprint (T1-kandidaat) of externe audit-vraag.

## Wat het is

In de SKOS-laag van v4.6.0 bestaan **28 expliciete `skos:exactMatch`-relaties tussen `ctrl:`- en `compl:`-namespaces**. De vraag is of alle 28 paren semantisch verdedigbaar zijn als "exact" (D4-conformiteit) of dat enkele eigenlijk `skos:closeMatch` of `skos:relatedMatch` zouden moeten zijn.

Het cijfer 28 is afgeleid uit de bredere SKOS-kwaliteitsanalyse v4.6.0 — ctrl→compl is één van meerdere cross-namespace-clusters in de 1.798-mappings totaal-set.

## Waarom dit een open vraag is

D4 staat alle vier de SKOS-match-types toe (`exactMatch`, `closeMatch`, `relatedMatch`, `narrowMatch`/`broadMatch`), maar geeft geen mechanische procedure om per individueel paar de juiste graad te bepalen. Bij ctrl→compl-paren spelen specifiek:

| Aspect | Risico |
|---|---|
| Control-statement vs. compliance-vereiste hebben verschillende ontologische rol | "Exact" kan misleidend zijn als de tekst-overeenkomst niet matcht met semantische gelijkheid |
| Cumulatief effect over 1.798 mappings | Bij 5% mis-classificatie zou ~90 paren herbeoordeling vragen, niet alleen deze 28 |
| Audit-implicatie | Externe SKOS-audit (DCAT-AP, externe linked-data review) zou exactMatch strenger lezen dan de huidige praktijk |

## Trigger-criterium

| Trigger | Wanneer aandacht oppakken |
|---|---|
| SKOS-kwaliteitsanalyse formeel als sprint geagendeerd | Audit van alle 28 ctrl→compl-paren als onderdeel van bredere 1.798-review |
| Externe audit-vraag over SKOS-mapping-rigour | Per-paar verdediging vereist; nu zou dat improvisatie zijn |
| Spoor B-organisatie eist DCAT-AP-conforme publicatie | exactMatch heeft strengere semantische plicht in linked-data-publicatie-context |

## Aanpak bij activering (toekomst, niet nu)

Niet uitgewerkt — bij activering is een evaluatie-matrix per paar de natuurlijke vorm: per paar de bron-vergelijking + voorgestelde match-type + onderbouwing. Resultaat kan zijn: 0-3 paren herclassificeren, of bevestiging dat alle 28 exact zijn.

## Hangt samen met

- [[brain__decisions__D04_skos-cross-framework]] — D-decision die match-type-keuze definieert
- [[brain__concepts__skos-export-filter]] — meet-laag-onderscheid (1.798 ontologie vs 1.759 export); relevant omdat ctrl/compl-paren beide individual-niveau zijn en wel in JSON-export verschijnen
- [[brain__concepts__sameAs-discipline]] — owl:sameAs is strikt; SKOS is losser maar verdient zelfde rigour-aandacht
- [[brain__sprints__v4_6_0_fase-4-ensia-en-volwassenheid]] — sprint waarin 1.798-baseline is bevestigd

## Bredere context — 1.798 SKOS-totaal

H36 is potentieel het eerste sub-cluster van een grotere kwaliteits-review. Andere clusters kunnen later geregistreerd worden indien specifieke audit-aandacht ontstaat (bv. csf→ctrl, csf→nist-controls, BIO→ISO-Annex-A). Voor nu: alleen het 28-paar-cluster geregistreerd als concrete grootte met expliciete trigger.

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-26 | parked | Geregistreerd in iteratie 12 polish-mini-sprint, eerder aangemerkt als "te registreren v1.10" in sessie-rapport v2.0 |

— Einde H36.
