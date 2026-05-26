---
type: module
id: M15
title: M15 — ENSIA (audit-domains, Laag 5)
status: active
date: 2026-05-21
related:
  - M01_framework
  - D09_framework-neutraliteit
  - v4_6_0_fase-4-ensia-en-volwassenheid
sources:
  - 19122024noreahandreikingensia2024versie10
chat-sources: []
confidence: high
---

# M15 — ENSIA

## Bestand
`m15-ensia.ttl`

## Namespaces
`fw:` (gedeeld met m01), `ext:` (audit-domains)

## Status

**Active sinds v4.6.0** — niet meer stub. Bevat ENSIA-domeinspecifieke aanvullingen naast de kerndeclaratie die in M01 staat (hybride locatie A3+B3+C2).

## Wat het bevat (post-v4.6.0)

| Inhoud | Aantal | Locatie |
|---|---:|---|
| `fw:ENSIA` kerndeclaratie | — | **Verplaatst naar M01** (v4.6.0) |
| NB-comment over gemeenten-context | 1 | M15 (behouden) |
| `ext:hasAuditDomain` (BAG, BGT, BIO, BRO, BRP, DigiD, Reisdocumenten, Suwinet) | 8 | M15 (behouden) |
| `skos:relatedMatch` (ISO-relaties) | 2 | M15 (behouden) |

## v4.6.0-uitbouw — promotie + hybride locatie

**Pre-v4.6.0 status:** M15 was stub met `fw:ENSIA rdf:type fw:Guideline`. Slechts beperkte declaratie.

**v4.6.0 wijzigingen:**

| Wat | Waarom |
|---|---|
| `fw:ENSIA` gepromoot `fw:Guideline` → `fw:GRCFramework` | ENSIA is auditkader, geen guideline-document |
| Kerndeclaratie verplaatst naar M01 | Hybride locatie A3+B3+C2 (masterchat-GO) |
| Oude `fw:Guideline`-blok in M15 verwijderd | Voorkomt dubbele type-assertion |
| Dubbele properties verwijderd | label, kern-comment, hasIdentifier, hasVersionLabel, isMandatoryForDutchGovernment, issuedBy, appliesInJurisdiction, hasDomain, fw:toetst, officialURL — staan nu allen in M01 |
| NB-comment behouden in M15 | ENSIA is alleen voor gemeenten van toepassing — gemeentespecifieke context past beter bij M15 |
| 8 `ext:hasAuditDomain` behouden in M15 | Audit-domain-detail is M15-specifiek, niet generiek |
| 2 `skos:relatedMatch` behouden in M15 | ISO-mappings zijn ENSIA-specifieke audit-context |

## Hybride locatie — A3+B3+C2

Masterchat-GO bij scope-pauze tijdens v4.6.0 Stap 5:

- **A3** Behoud bestaande 3 issuers (BZK/DutchCentral, NOREA, VNG); fw:Logius NIET als issuer toegevoegd (Logius beheert, geeft niet uit — property-semantiek-discipline)
- **B3** Hybride locatie: kerndeclaratie M01, domeinspecifiek M15
- **C2** Geen 2e `fw:toetst` naar ISO 27001 — ENSIA toetst formeel alleen BIO, ISO blijft `skos:relatedMatch`

## D9-bewijs — vierde verificatie-cluster

ENSIA-uitbouw bevestigt D9: audit-kaders krijgen geen apart privilege. Concrete keuzes:

- Geen aparte "audit:"-namespace — `fw:` is voldoende
- Geen aparte "audit kader"-class — `fw:GRCFramework` volstaat
- Hybride locatie respecteert domein-grenzen zonder hiërarchische subordering
- ISO-relatie via `skos:relatedMatch` (informatief), niet via 2e `fw:toetst`

Zie [[brain__decisions__D09_framework-neutraliteit]] voor het cumulatieve D9-bewijs op vier verschillende framework-soorten.

## ENSIA — wat het is

ENSIA = Eenduidige Normatiek Single Information Audit. Auditkader voor Nederlandse gemeenten over informatiebeveiliging van **DigiD-aansluiting + Suwinet** plus aanvullende basisregistraties (BAG, BGT, BRO, BRP, Reisdocumenten — sinds 2024 ook WOZ). Auditkader vraagt jaarlijkse collegeverklaring op basis van BIO 2.0-normenkader.

ENSIA-vragenlijst is per audit-domain ingericht. Bevat **geen control-set** in eigen recht — gebruikt BIO 2.0-controls als normenkader. Daarom geen ENSIA-eigen ctrl:-namespace.

## Bronlicentie

NOREA Handreiking ENSIA 2024 versie 1.0 (19 december 2024) — vrij gebruik met bronvermelding. Geattribueerd via `ext:Attr_ENSIA_Logius_2024` in M01.

## ENSIA-control-set — bron-zoeker-werk

NOREA-handreiking biedt geen control-set-bron. Analyse-opdracht 2.0-onderwerp: mogelijk ENSIA-vragenlijst online beschikbaar? Geen H-item — wacht op trigger.

## Cross-references

- [[brain__modules__M01_framework]] — fw:ENSIA kerndeclaratie + SourceAttribution
- [[brain__decisions__D09_framework-neutraliteit]] — vier verificatie-clusters
- [[brain__sprints__v4_6_0_fase-4-ensia-en-volwassenheid]] — sprint van uitbouw

— Einde M15.
