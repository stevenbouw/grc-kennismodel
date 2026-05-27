---
type: concept
title: Mapping-bron-disclaimer-effect — non-equivalence-claims in autoritatieve cross-norm-mappings
status: living
date: 2026-05-27
related:
  - D04_skos-cross-framework
  - T1_skos-kwaliteitsanalyse-fase-1
  - T2-skos-bidirectional-audit-m10
  - skos-beoordelings-protocol
  - cluster-discipline-bewijslast
  - cross-bron-overlap
sources:
  - t1-eindrapport-v4_6_1
  - t1-pilot-rapport-stap3-v4_6_0
  - patch-rapport-v4_6_2
  - t2-stap3-eindrapport
chat-sources: []
confidence: medium
---

# Mapping-bron-disclaimer-effect

## Wat het is

Autoritatieve cross-norm-mapping-bronnen bevatten vaak een **expliciete disclaimer die *equivalence*-interpretatie uitsluit**, zelfs als de mapping-relatie zelf wel wordt onderkend. Het effect: een sluitende C1-C3-toets in [[brain__concepts__skos-beoordelings-protocol]] is niet voldoende om `skos:exactMatch` te rechtvaardigen wanneer de onderliggende mapping-bron expliciet stelt dat de mapping géén equivalence-claim is.

**Gevolg voor D4-conformiteit:** `skos:broadMatch` of `skos:closeMatch` is de juiste interpretatie, afhankelijk van scope-relatie.

## Eerste-bewijs-cluster — T1 (26 mei 2026)

In T1-sprint werd dit patroon voor het eerst expliciet vastgesteld als architectuur-relevante observatie. Bron-keten:

1. NIS2-richtlijn (EU) 2022/2555 art.21 → "de stand van de techniek en de desbetreffende Europese en internationale normen"
2. UV (EU) 2024/2690 considerans (3) → "based on European and international standards, such as ISO/IEC 27001, ISO/IEC 27002"
3. UV-Annex hoofdstukken 1-13 → expliciet gekoppeld aan NIS2 art.21-letters
4. ENISA TIG v1.0 juni 2025 → per-sectie mapping-tabellen
5. CBW-Excel reproduceert ENISA TIG-tabel

**Cruciale paradox — ENISA TIG regel 285:**

> *"The mapping should not be interpreted as a measure of equivalency among different standards or frameworks."*

De autoritatieve bron erkent dus expliciet dat de relatie bestaat én dat het géén equivalence-claim is. Dit ondergraaft `skos:exactMatch` als juiste SKOS-keuze op evidence-niveau 1.

T1-uitkomst: alle 28 ctrl:↔compl: paren herclassificeerd naar `broadMatch`, mede vanwege dit categorisch effect.

## Generaliseerbaarheid — vermoedelijk, niet geverifieerd

Het patroon (autoritatieve mapping-bron + non-equivalence-disclaimer) is waarschijnlijk standaard in cross-norm-mapping-documenten. Kandidaat-bronnen waar dit patroon vermoed wordt maar **nog niet geverifieerd** in dit project:

| Bron | Status | Onderzoek-aandacht |
|---|---|---|
| **ENISA TIG v1.0** (NIS2 ↔ ISO 27002:2022) | Bevestigd T1 | Regel 285 expliciet citeerbaar |
| NIST OLIR (Online Informative Reference) | Vermoed | Bij Tier 2-mapping-vraag tijdens T3 of later raadplegen |
| ISO Annex F (ISO 27001:2022 ↔ NIST CSF) | Vermoed | Bij T2-uitbreiding naar ctrl:↔compl: close+related+broad raadplegen |
| Andere mapping-publicaties | Vermoed | Per bron individueel toetsen |

Generaliseerbare regel-formulering (T1-empirie):

> Wanneer een autoritatieve mapping-bron expliciet *equivalence* uitsluit, is `skos:exactMatch` **niet** verdedigbaar zelfs bij volledig sluitende C1-C3-toets. Gebruik `skos:broadMatch` of `skos:closeMatch` afhankelijk van scope-relatie tussen subject en object.

## Effect op beoordelings-protocol

Het mapping-bron-disclaimer-effect raakt direct aan C4 (bron-bewijs) in [[brain__concepts__skos-beoordelings-protocol]]:

- Een evidence-niveau-1-bron met non-equivalence-disclaimer ondersteunt **niet** `exactMatch`
- C4-status bij disclaimer-aanwezigheid: gehaald voor lichtere SKOS-types (`broadMatch`/`closeMatch`/`relatedMatch`), faalt voor `exactMatch`
- Combinatie met C1-C3-failure leidt eenduidig tot herclassificatie

Voor protocol-v1.1-overweging bij T2-start: disclaimer-aanwezigheid expliciet als pre-stap binnen C4-evaluatie opnemen.

## D4-aanvulling — vastgesteld als D4.1 (27-05-2026)

Op 27 mei 2026 heeft masterchat (via mini-revisie) de D4-aanvulling formeel doorgevoerd als sub-regel **D4.1 — Disclaimer-handling bij autoritatieve mapping-bronnen**. D4 zelf is niet geherformuleerd; D4.1 vult D4 aan.

Vastgestelde keuzes:

| Aspect | Vastgesteld |
|---|---|
| Formaliteit | Sub-regel D4.1 onder D4 (geen D4-herformulering) |
| Reikwijdte | Disclaimer blokkeert alleen `skos:exactMatch`; `closeMatch`/`relatedMatch`/`broadMatch`/`narrowMatch` blijven valide |
| Retroactiviteit | Geen retroactieve audit; D4.1 geldt vanaf vaststelling. Audit van resterende 18 `skos:exactMatch`-mappings is T2-overweging |

Volledige tekst: [[brain__decisions__D04_skos-cross-framework]] §D4.1. Concept (dit bestand) blijft de generaliseerbare patroon-beschrijving; D4.1 is de formele beslissingsregel.

Status-verschuiving voor dit concept: van "open patroon-overweging" naar "formeel patroon onder D4.1". Verdere confidence-verhoging naar **high** vereist nog steeds tweede onafhankelijke bron-bevestiging (NIST OLIR of ISO Annex F-tekstverificatie) — D4.1-formalisatie is voldoende grond om het patroon vast te leggen, maar valideert generaliseerbaarheid nog niet empirisch.

## D4.1-toepassing op cluster-niveau — T2 (27-05-2026)

T2-sprint heeft D4.1-toepassing geoperationaliseerd op **cluster-niveau** voor 118 m10-paren over 10 NIS2-art.21-letter-clusters (per patch-rapport v4.6.2 §1 + Stap 3-eindrapport §6.6):

> Wanneer alle cluster-leden dezelfde bron-stack delen (homogene clusters), volstaat **één D4.1-bevestiging per cluster** — niet per-paar-werk. Voor heterogene clusters (mix van bronnen) blijft per-paar-toets vereist.

**T2-empirie:**
- Alle 10 m10-clusters deelden één D4.1-context: ENISA TIG R285 + CBW-Mapping-UV R3-erf (T1-bekend, pre-sprint-inventarisatie §5)
- Per-paar-D4.1-check op cluster-niveau = **één bevestiging per cluster, niet 11,8 keer per cluster** — efficiëntiewinst t.o.v. naïeve per-paar-aanpak
- 0 NEN-aantoonbare uitzonderingen op 10 heuristiek-flags (zie [[brain__concepts__cluster-discipline-bewijslast]])

**Bron-erf-relatie ENISA TIG R285 + CBW-Mapping-UV R3:** CBW-Excel "Mapping Uitvoeringsverordening" R3 verwijst expliciet naar ENISA TIG-disclaimer. T2 bevestigde dat één cluster-context-bewijs op deze keten volstaat voor alle cluster-leden binnen één m10-cluster. **Reikwijdte-beperking:** geldt alleen bij homogene cluster-bron-stack; heterogene clusters (toekomstig m14-sprint AVG-cross-walk, cross-bron-overlap-sprint) vereisen per-paar-D4.1-toets.

Operationele consequentie voor toekomstige T-sprints: vóór cluster-niveau-D4.1-toepassing eerst bron-stack-homogeniteit verifiëren als pre-cluster-stap.

## Confidence-status

**Medium**, niet hoog. Reden:

- T1 leverde **één** bewijs-cluster (ENISA TIG)
- NIST OLIR + ISO Annex F-tekstverificatie nog niet uitgevoerd in dit project
- Generaliseerbaarheid is **vermoeden** op basis van patroon-herkenning, niet aangetoond op 2+ onafhankelijke bronnen

File-back-criterium (CLAUDE.md §Operations) gesteld op "2+ keer in conversaties zonder centrale documentatie" — T1-eindrapport §6 + §8 leerpunt 2 markeert dit patroon als generaliseerbaar; concept-bestand voorkomt dat het inzicht verloren gaat bij latere sprints.

Verhoging naar **high confidence** vereist:
- Tweede onafhankelijke bron-bevestiging (bv. NIST OLIR-tekst geverifieerd met vergelijkbare disclaimer)
- Of: D4-aanvulling formeel doorgevoerd door masterchat met dit concept als onderbouwing

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-26 | living (confidence medium) | Concept ontstaan uit T1-sprint §6 + §8 leerpunt 2. Eerste bewijs-cluster: ENISA TIG regel 285. Generaliseerbaarheid vermoed maar niet 2+ keer bewezen |
| 2026-05-27 | living | D4.1 vastgesteld in D-register. Concept-status verschuift van "open patroon-overweging" naar "formeel patroon onder D4.1". Confidence blijft medium tot tweede onafhankelijke bron-bevestiging. |
| 2026-05-27 | living | D4.1-toepassings-precedent op cluster-niveau gedocumenteerd na T2-sprint. Bij homogene cluster-bron-stack volstaat één D4.1-bevestiging per cluster (T2: 10× toegepast, 0 uitzonderingen). Bron-erf ENISA TIG R285 + CBW-Mapping-UV R3 expliciet als één-context-keten erkend. Confidence blijft medium (toepassings-precedent vergroot niet de generaliseerbaarheids-empirie naar andere bronnen). |

## Cross-references

- [[brain__sprints__T1_skos-kwaliteitsanalyse-fase-1]] — sprint waarin patroon voor het eerst werd vastgesteld
- [[brain__sprints__T2-skos-bidirectional-audit-m10]] — sprint waarin D4.1-cluster-niveau-toepassings-precedent is gedocumenteerd
- [[brain__concepts__skos-beoordelings-protocol]] — methode-concept waarin D4.1-vooraf-check is opgenomen (Protocol v1.2/v1.3 §2.0)
- [[brain__concepts__cluster-discipline-bewijslast]] — bewijslast-asymmetrie bij cluster-uitzonderingen (raakt D4.1-toepassings-reikwijdte)
- [[brain__decisions__D04_skos-cross-framework]] — formele beslissing — zie §D4.1 voor de disclaimer-handling-regel (vastgesteld 27-05-2026) + cluster-niveau-toepassings-precedent
- [[brain__decisions__D-register]] — register-vermelding D4 incl. D4.1
- [[brain__concepts__cross-bron-overlap]] — gerelateerd kwaliteits-indicator-concept (S5 ∩ S6 = 105 mappings uit v4.5.0)
- [[brain__sources__cbw-excel]] — bron-bestand waarvia ENISA TIG-mapping in T1 toegankelijk werd

— Einde mapping-bron-disclaimer-effect.
