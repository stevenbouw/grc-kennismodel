---
type: index
id: scope-register
title: Scope-register — Bewust uitgesloten elementen
status: living
date: 2026-05-13
---

# Scope-register — Bewust uitgesloten elementen

Overzicht van alle elementen die **bewust niet in het GRC Kennismodel** zijn opgenomen of zijn geparkeerd. Het verschil tussen "niet opgenomen omdat we het vergeten zijn" en "niet opgenomen omdat we het hebben overwogen en afgewezen" is cruciaal — dit register documenteert de tweede categorie.

## Snelle navigatie

| Item | Status | Reden | Detail |
|---|---|---|---|
| **UCF** (Unified Compliance Framework) | excluded | Conceptuele overlap + IP/licentie + commerciële afhankelijkheid + geen NL-meerwaarde | [[brain__scope__UCF-uitgesloten]] |
| **M19 ISO 42001** (AI Management) | deferred | Geen IB-raakvlak in Fase 1-3; mogelijk Fase 4+ | [[brain__scope__M19-iso-42001-buiten-fase]] |
| **M20 ISO 9001** (Quality) | excluded | Buiten IB-scope; niet voorzien | [[brain__scope__M20-iso-9001-niet-in-scope]] |
| **Route 1 / 1-light** (ISO-guidance parafrasering) | parked v5.x | NEN-licentie-restrictie op parafrasering | [[brain__scope__route-1-iso-guidance-parafrasering-geparkeerd]] |

## Status-categorieën

| Status | Betekenis | Heropname-trigger |
|---|---|---|
| **excluded** | Bewust niet opgenomen, geen automatische heropname | Fundamentele scope-uitbreiding of nieuw project |
| **deferred** | Mogelijk later, mits specifieke trigger | Concrete IB-raakvlak of stakeholder-vraag |
| **parked** | Niet actief, status-trigger gespecificeerd | Licentie-clearance of alternatieve bron |

## Niet in dit register (andere folders)

Sommige scope-relateerde onderwerpen passen elders:

| Onderwerp | Waar | Reden |
|---|---|---|
| AVG buiten IB-scope | [[brain__modules__M14_avg-gdpr]] | Module-detail, niet uitsluiting |
| ABox-leegheid (Spoor B) | `architecture/` (H11, H12, H13, H19, H20) | Geparkeerd, geen scope-uitsluiting |
| Toekomst-overwegingen (H29/H30/H31) | `architecture/` | Future-consideration, niet excluded |
| Sprint-specifieke parkeer-items | `sprints/` per sprint | Punctueel, niet structureel |

## Heropname-protocol

Bij voorstel tot heropname van een uitgesloten item:

1. **Trigger documenteren** — waarom nu wel?
2. **Master-beslissing** vereist (geen tech-chat-discretie)
3. **Analyse-opdracht** waarschijnlijk nodig (Opdracht 2.0, 3.0, ...)
4. **Update dit register** — status veranderen of file verplaatsen
5. **Eventuele D-decisions** aanpassen indien architectuur-impact

## Scope-bewustzijn in toekomst-vragen

Bij elke nieuwe sprint of uitbreiding: scope-register checken om te zien of de uitbreiding raakvlak heeft met bewust-uitgeslotene. Bv:

- Nieuwe AI-management-vraag → check M19 status
- Nieuwe kwaliteitsmanagement-vraag → check M20 (waarschijnlijk niet-onderhandelbaar)
- Nieuwe meta-framework-vraag → check UCF
- Implementatie-detail-vraag voor ISO-control → check Route 1 (gebruik Route 2/3/5 als alternatief)

## Cross-references

- [[brain__concepts__framework-neutraliteit]] — D9 is reden voor UCF-uitsluiting (één van vier)
- [[brain__sources__iso-normen-bundle]] — NEN-licentie achter Route 1-parkering
- [[brain__decisions__D-register]] — geen D-decision specifiek voor scope-uitsluitingen (bewuste keuze: scope is in projectinstructie)
- [[brain__modules__module-register]] — modules-perspectief op uitsluitingen (M19, M20)

— Einde scope-register.
