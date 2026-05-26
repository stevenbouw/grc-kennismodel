---
type: concept
title: Meeliftregel — edit-scope versus bestand-scope
status: living
date: 2026-05-13
related:
  - D06_meeliftregel-tweetalig
sources: []
chat-sources: []
confidence: high
---

# Meeliftregel — edit-scope versus bestand-scope

## Wat het is

De **D6 meeliftregel** is de discipline die zegt: elke wijziging aan een ontologie-bestand moet voor de **gewijzigde annotaties** tweetalig zijn (@nl + @en). De cruciale nuance: dit geldt voor de **edit-scope**, niet voor het **gehele bestand-scope**.

Het verschil:

| Interpretatie | Wat het betekent | Gevolg |
|---|---|---|
| **Bestand-scope** (verworpen) | Bij elke edit moet het hele bestand 100% tweetalig zijn | Bij elke kleine wijziging in m08 (~2000 regels) moet alle @nl-only content bijgewerkt worden — onpraktisch, scope-creep |
| **Edit-scope** (gekozen, D6) | Alleen de annotaties die je *zelf wijzigt* worden tweetalig opgeleverd | Pragmatisch — wijzigingen blijven beheersbaar, achterstand wordt geleidelijk ingelopen |

## Waarom edit-scope

Drie redenen:

1. **Praktische haalbaarheid.** Bestand-scope zou betekenen dat elke kleine fix een uitgebreide tweetalige refactor wordt. Dat schaalt niet bij 22 ontologie-bestanden en honderden annotaties.

2. **Geen schijn-perfectie.** Bestand-scope dwingt tot oppervlakkige vertalingen onder druk. Edit-scope laat ruimte voor **kwalitatieve tweetaligheid** waar het er toe doet.

3. **Achterstand wordt automatisch ingelopen.** Wie aan een bestand werkt, raakt automatisch de meest-gewijzigde delen. Die worden over de tijd dus zeker tweetalig. Stille delen blijven NL-only — dat is acceptabel als ze niet actief onderhouden worden.

## Wat het in praktijk betekent

**Voorbeeld 1 — kleine fix:**
- Tech-chat fixt een typo in `bio:ISO27002_5_03`-comment
- Edit-scope: alleen deze comment moet tweetalig (NL + EN)
- Niet vereist: 92 andere bio-control-comments ook bijwerken

**Voorbeeld 2 — module-uitbreiding:**
- Tech-chat voegt 6 nieuwe `compl:REQ_NIS2_*` toe aan m05
- Edit-scope: alle 6 nieuwe REQ-subjects krijgen NL + EN labels
- Niet vereist: bestaande oudere REQ-subjects ook bijwerken (tenzij ze in scope zitten via andere wijziging)

**Voorbeeld 3 — refactor:**
- Tech-chat hernoemt een property over 20 subjects
- Edit-scope: alle 20 gewijzigde subjects krijgen tweetalige labels
- Wel relevant: de TBox-declaratie van de hernoemde property zelf

## Edge-cases

**Edge-case A — bestaande NL-only annotatie wordt gewijzigd:**
- Pre-wijziging: alleen NL bestond
- Post-wijziging: NL gewijzigd
- Regel: **maak nu ook EN aan** (de annotatie is in edit-scope geraakt)

**Edge-case B — nieuwe annotatie op bestaand subject:**
- Subject bestond, nieuwe rdfs:comment wordt toegevoegd
- Regel: **deze comment moet tweetalig** (nieuwe content = automatisch in scope)
- Bestaande andere comments op zelfde subject: niet verplicht bij te werken

**Edge-case C — typo-fix in EN-only labels:**
- Bestaand EN-label heeft typo
- Fix: typo corrigeren
- Regel: alleen EN bijwerken. Geen verplichting om NL ook te checken (tenzij die ook fout is).

## Waarom dit een belangrijk concept is

De meeliftregel staat op het snijvlak van **kwaliteits-discipline** en **scope-discipline**:

- Te losse interpretatie ("alles is edit-scope") → achterstand groeit, model wordt structureel NL-only
- Te strikte interpretatie ("alles in bestand bijwerken") → kleine edits worden grote sprints

Het edit-scope-onderscheid is een **bewust pragmatisch compromis** — vastgelegd op 10 april 2026 (v4.1.0-alpha Actie G) na ervaring dat bestand-scope onhoudbaar bleek.

## Toepassings-bewijs

Sinds v4.1.0-alpha consistent toegepast in alle sprints:

- v4.2.0: D6 meelift bij M18-introductie — 5 categorie-comments tweetalig (M18-specifiek, niet hele M06)
- v4.3.1: D6 meelift bij H18 scope-completion — alleen nieuwe HSClause-individuals + ext:alignsWithHSClause TBox tweetalig
- v4.3.3: D6 meelift bij REQ-subjects — 15 + 6 + 15 nieuwe annotaties tweetalig, bestaande oudere REQ-content ongemoeid

## Wat NIET D6-meelift is

- **Bulk-vertaling van bestaande content** — apart project, geen automatische scope
- **Annotaties in patch-rapporten of brain-files** — D6 geldt voor de **ontologie** (Turtle-bestanden), niet voor procesdocumentatie
- **SPARQL-queries of SHACL-shapes** — die zijn meestal taal-onafhankelijk (URIs)

## Cross-references

- [[brain__decisions__D06_meeliftregel-tweetalig]] — formele beslissing
- [[brain__concepts__scope-discipline]] — meeliftregel is voorbeeld van scope-begrenzing
- [[brain__sprints__v4_1_0-alpha_werkpakket-opschoning]] — vastlegging (Actie G)

— Einde meeliftregel-edit-scope (concept).
