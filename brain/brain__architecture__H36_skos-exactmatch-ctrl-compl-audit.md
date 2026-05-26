---
type: architecture
id: H36
title: H36 — 28 ctrl→compl exactMatch-pairs audit
status: closed
date: 2026-05-26
related:
  - v4_6_0_fase-4-ensia-en-volwassenheid
  - T1_skos-kwaliteitsanalyse-fase-1
  - skos-beoordelings-protocol
  - mapping-bron-disclaimer-effect
  - skos-export-filter
  - sameAs-discipline
sources:
  - sessie-rapport-v2_0
  - patch-rapport-v4_6_0
  - t1-eindrapport-v4_6_1
  - patch-rapport-v4_6_1
chat-sources: []
confidence: high
---

# H36 — 28 ctrl→compl exactMatch-pairs audit

## Status

**Closed** — afgehandeld via T1-sprint (26 mei 2026). Alle 28 paren herclassificeerd `exactMatch` → `broadMatch` via patch v4.6.1. Methode-protocol v1.0 vastgesteld als bijproduct. Zie [[brain__sprints__T1_skos-kwaliteitsanalyse-fase-1]].

Eerder geregistreerd post-v4.6.0 in polish-mini-sprint (iteratie 12) als parked, met trigger "SKOS-kwaliteitsanalyse-sprint". Trigger vervuld door T1.

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

## Uitkomst T1-sprint (26 mei 2026)

T1-sprint heeft alle 28 paren beoordeeld volgens [[brain__concepts__skos-beoordelings-protocol]] v1.0:

| Aspect | Resultaat |
|---|---|
| Beoordeelde paren | 28 (volledig — geen openstaande paren) |
| Uitkomst | **28× herclassificatie `exactMatch` → `broadMatch`** |
| Confidence per paar | 28× hoog |
| Evidence-niveau per paar | 28× niveau 1 (CBW-Excel reproduceert ENISA TIG v1.0 mapping-tabel) |
| Twijfelgevallen | 2 edge-cases (T1-021 + T1-023) opgelost via masterchat-NEN-PK-toets — beide → broadMatch |
| Patch | v4.6.1 toegepast op `m10-nis2-ext.ttl` (hash `78b8ee44...` → `cb2d567b...`) |
| Cluster-consistentie | 10 clusters, alle behandeld zonder half-half-cluster-uitkomsten |
| D4-conformance | Verbetering — `exactMatch` was te sterk geclaimd; ENISA TIG regel 285 stelt expliciet dat mapping géén equivalence-claim is |

**Belangrijkste bevinding voorbij H36:** ENISA-disclaimer-categorisch-effect — autoritatieve mapping-bron verbiedt equivalence-interpretatie via expliciete disclaimer. Vermoedelijk generaliseerbaar patroon. Zie [[brain__concepts__mapping-bron-disclaimer-effect]].

## Kandidaat-overweging (NIET geregistreerd als H41)

T1 toonde dat owlrl-package geen SKOS-axiomas laadt; `skos:exactMatch is owl:SymmetricProperty` (skos:S46) wordt niet geïnferreerd. Alle 28 mappings asymmetrisch gemodelleerd (0 inverse). Geen impact op T1-patch.

**Status:** T1-werkflow-leerpunt, **geen nieuw H-item nu**. Trigger voor herregistratie: overstap-besluit owlrl-incl-SKOS-axioma-reasoning.

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-26 | parked | Geregistreerd in iteratie 12 polish-mini-sprint, eerder aangemerkt als "te registreren v1.10" in sessie-rapport v2.0 |
| 2026-05-26 | **closed** | **Afgehandeld via T1-sprint — 28× exactMatch → broadMatch via patch v4.6.1; methode-protocol v1.0 als bijproduct vastgesteld** |

— Einde H36.
