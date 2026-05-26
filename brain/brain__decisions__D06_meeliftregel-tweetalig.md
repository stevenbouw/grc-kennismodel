---
type: decision
id: D6
title: D6 — Tweetalige annotaties + meeliftregel + vertaling-scope
status: active
date: 2026-05-21
related:
  - v4_1_0-alpha_werkpakket-opschoning
  - v4_6_0_fase-4-ensia-en-volwassenheid
  - meeliftregel-edit-scope
sources:
  - projectinstructie-v1.9
chat-sources: []
confidence: high
---

# D6 — Tweetalige annotaties + meeliftregel

## Beslissing

Alle annotaties (`rdfs:label`, `rdfs:comment`, `skos:prefLabel`, etc.) zijn **tweetalig @nl/@en** waar mogelijk. Bij elke module-edit geldt de **meeliftregel**: Dutch-only annotaties in het edit-scope moeten bilingueel gemaakt worden in dezelfde commit. Het edit-scope is gebonden — niet het hele bestand.

## Wat het inhoudt

- **Standaard:** elke nieuwe annotatie komt in @nl én @en
- **Meeliftregel:** wijzig je iets in een bestand, dan de aanpalende Dutch-only annotaties in dat edit-scope meenemen (niet het hele bestand)
- **Vertaling-scope:** beperkt tot wat redelijk binnen masterchat/tech-chat-capabiliteit valt — gezaghebbende bronnen prevaleren

## Vertaling-scope (v1.7 + v1.9 uitbreidingen)

### Originele regel (v4.1.0-alpha)
Vertaling van Dutch-only annotaties naar @en is wenselijk maar niet altijd haalbaar.

### v1.7 uitbreiding (mei 2026)
> Korte titel-fraseringen mogen door masterchat/tech-chat zelf vertaald worden; lange normatieve tekst blijft @nl-only tenzij gezaghebbende EN-bron beschikbaar.

Concrete consequentie: bv. ISO 27002-control-titels (kort) → vertaal zelf naar @en; ISO 27001-clausule-doelstellingen (langer, normatief) → blijven @nl-only.

### v1.9 symmetrische toepassing (21 mei 2026)
> Lange normatieve EN-tekst blijft @en-only tenzij gezaghebbende NL-bron beschikbaar (CSF Tier-descriptions-precedent).

Concrete consequentie: bv. CSF Tier-descriptions uit NIST CSWP 29 (lange normatieve EN-tekst, geen gezaghebbende NL-bron) blijven @en-only. Symmetrisch aan v1.7-regel: beide richtingen gelijkwaardig.

**Vier mogelijke situaties:**

| Tekst-lengte | Origineel-taal | Gezaghebbende vertaling beschikbaar | Resultaat |
|---|---|---|---|
| Kort (titel) | NL | — | Bilingueel @nl/@en |
| Kort (titel) | EN | — | Bilingueel @en/@nl |
| Lang (normatief) | NL | Geen gezaghebbende @en-bron | @nl-only |
| Lang (normatief) | NL | Wel gezaghebbende @en-bron | Bilingueel @nl/@en |
| Lang (normatief) | EN | Geen gezaghebbende @nl-bron | @en-only ← **v1.9** |
| Lang (normatief) | EN | Wel gezaghebbende @nl-bron | Bilingueel @en/@nl |

## Concrete toepassingen tot heden

### v4.5.0 — M02 ctrl:CybersecurityConcept
ConceptScheme-comment v1.x (5 Functions) → v2.0 (6 Functions incl. GOVERN). Comment bilingueel bijgewerkt. Edit-scope: alleen die ConceptScheme — overige M02-content ongemoeid.

### v4.6.0 — CSF Tier-descriptions (symmetrische toepassing)
`csf:riskGovernanceDescription` + `csf:riskManagementDescription`:
- `rdfs:label` bilingueel (kort, eigen vertaling)
- `csf:csfIdentifier` zonder language-tag
- `riskGovernanceDescription` / `riskManagementDescription` **@en-only** (178-1.085 chars per Tier, totaal ~4.900 chars EN; geen gezaghebbende NL-bron)

### v4.6.0 — LevelDescription comment-veld
160 `isms:CapabilityLevelDescription`:
- `rdfs:label` bilingueel
- `rdfs:comment` met niveau-beschrijving uit CBW-Excel **@nl-only** (bron-getrouw, geen gezaghebbende EN-bron)

### v4.6.0 — ISMS Capability-labels
9 `isms:ISMSCapability`-individuals: EN-vertalingen via **ISO 27001:2022-standaard-clausule-titels** (gezaghebbende EN-bron beschikbaar). Bilingueel.

23 `isms:CbwCapability`-individuals: 23 Cbw EN-vertalingen door masterchat geleverd. Bilingueel.

## Conventies

- **Bilingual = @nl/@en op één regel** (Turtle multi-line per language)
- **Edit-scope ≠ bestand-scope** — bij grote files alleen wat je raakt
- **Status-discipline** — bij CBW: markeren als "in voorbereiding"; bij Cbb: "concept t.b.v. Tweede Kamer"

## Wat de meeliftregel NIET vereist

- ❌ Geen verplichting om hele module bilingueel te maken bij kleine edits
- ❌ Geen reden om externe tekst (NEN-ISO-controls) verbatim te kopiëren — NEN-restrictief
- ❌ Geen verplichting om tijdelijk @nl-only individuals (bv. tijdens prototyping) onmiddellijk bilingueel te maken

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| v4.1.0-alpha | active | Initieel: bilingual @nl/@en + meeliftregel edit-scope |
| 2026-05-13 (v1.7) | active | Vertaling-scope uitbreiding: korte titel-fraseringen zelf vertalen, lange normatieve @nl-only tenzij EN-bron |
| 2026-05-21 (v1.9) | active | Symmetrische toepassing: lange normatieve EN-tekst @en-only tenzij gezaghebbende NL-bron (CSF Tier-descriptions-precedent) |

## Hangt samen met

- [[brain__concepts__meeliftregel-edit-scope]] — uitgewerkt edit-scope-discipline
- [[brain__sprints__v4_1_0-alpha_werkpakket-opschoning]] — initiële vastlegging
- [[brain__sprints__v4_6_0_fase-4-ensia-en-volwassenheid]] — symmetrische toepassing
- [[brain__modules__M21_nist-csf-2-0-planned]] — concrete @en-only toepassing (Tier-descriptions)
- [[brain__modules__M06_isms]] — concrete @nl-only toepassing (LevelDescription-comment)

— Einde D6.
