# Instructie Tech-subagent — T4 pre-sprint-inventarisatie

**Van:** masterchat
**Datum:** 29 mei 2026
**Doel-subagent:** Technisch (Claude Code)
**Sprint:** T4 — cross-bron-overlap CSF ↔ ISO 27001 (SKOS-kwaliteits-validatie)
**Fase:** pre-sprint-inventarisatie (Protocol 1). **Geen mutaties in deze fase.**

---

## 0. Context, doel en framing (lees dit eerst goed)

T4 zet de SKOS-kwaliteits-lijn van T1/T2/T3 door, maar op een ander domein én met een ander karakter. Bron: `brain/brain__concepts__cross-bron-overlap.md` (raadpleeg volledig).

**Wat het is:** in v4.5.0 is geconstateerd dat twee onafhankelijke bronnen — Sheet 8 (ADR/NOREA) én de CSF Reference Tool (NIST) — dezelfde 105 `csf:Subcategory ↔ ISO 27001`-mappings leggen. Bron-onafhankelijke overeenstemming is een **kwaliteits-positief signaal**, geen foutenlijst.

**Cruciale framing — niet de overlap, maar de divergentie is het werk.** Anders dan T1–T3 (waar verkeerde exact/closeMatch herklassificeren de taak was) is de 105-overlap-set vermoedelijk al correct. Het inspectie-relevante deel is het **complement / de divergentie**: paren waar Sheet 8 en de CSF Reference Tool van elkaar afwijken of waar de één zwijgt. Het concept zegt expliciet: bij divergentie = kandidaat voor nadere inspectie, mogelijk fout in een van beide bronnen.

**Doel van deze fase:** de echte scope vaststellen. Niet muteren. Lever een inventarisatie-rapport en stop voor masterchat-review — zoals T1/T2/T3 begonnen.

## 1. Harde invarianten

- **Geen organisatienaam.**
- **Framework-neutraal (D9)** — CSF noch ISO 27001 als hub; mappings beschrijven samenhang, geen privilege.
- **NEN-discipline** — ISO 27001:2022 is NEN-restrictief. In het rapport: alleen parafrase + clausule-/Annex-A-verwijzing, **geen verbatim NEN-tekst >10 woorden.** CSF 2.0 = publiek domein; Sheet 8 = ADR/NOREA-attributie (CC-BY-context, zie source-register).
- **Geen autonome commit** — lever op, de projecteigenaar inspecteert + commit handmatig.
- **Geen mutatie** — deze fase is read-only analyse. Geen TTL-aanraking, geen applier, geen patch.

## 2. Methode-kader

- **Protocol 1** (pre-sprint-inventarisatie) — gebruik de `/pre-sprint-inventarisatie`-skill als skelet (§0–§9).
- **Canonical baseline = v4.6.3** (`canonical_metrics`-skill). Verifieer aan de bron; ga niet uit van geheugen. Referentie-distributie post-v4.6.3: SKOS-totaal 1.798 (exact 18 / close 1.457 / broad 129 / related 194). Let op: de TTL draagt `owl:versionInfo "4.6.0"`; v4.6.1–3 zijn SKOS-only — structuur identiek. Noem de meet-laag expliciet (Protocol v1.3 §10.5: ontologie-laag vs. dashboard-export-laag).
- **Gesplitste SHACL** (SECTIE A + B + COMBINED) — baseline-check dat T4 op een schone baseline start (verwacht A=0, B=0, COMBINED=290).
- **Protocol v1.3 FINAL** — inclusief het cross-category-principe (control ↔ legal-obligation = relatedMatch-basislijn). **Open classificatie-vraag voor deze inventarisatie:** is `csf:Subcategory ↔ ISO 27001` binnen-categorie (→ cluster-discipline, zoals m10) of cross-category (→ relatedMatch-basislijn)? Dit hángt af van of het ISO-eindpunt een Annex A-control is (measure-categorie) of een management-clausule (eis-categorie). Stel dit vast, beslis het niet — het bepaalt de methode van een eventuele latere pilot.

## 3. Inventarisatie-vragen (vast te stellen, niet te beslissen)

1. **Tellingen.** Hoeveel `csf:Subcategory ↔ ISO 27001`-mappings totaal? Hoeveel daarvan dragen attributie van béíde bronnen (de overlap-set — verwacht ±105)? Hoeveel van één bron (de divergentie-set)? Symmetrisch verschil per bron.
2. **Modules.** Welke modules dragen deze mappings (verwacht m21 csf + m09 iso27001-ext)? Per module de predicate-distributie op deze paren.
3. **Provenance.** Dragen de overlap-paren daadwerkelijk dubbele `ext:sourceAttribution` (Sheet 8 + CSF Reference Tool)? Gebruik het detection-query-patroon uit het concept (`bron_count >= 2`). Rapporteer afwijkingen.
4. **Categorie-classificatie.** Is het ISO-eindpunt Annex A-control of management-clausule? → binnen-categorie of cross-category? Onderbouw per bron-verificatie.
5. **Huidige predicate-status.** Welke SKOS-predicates liggen er nu op de overlap- en divergentie-set (close/related/broad/exact)? Zijn er prima facie verdachte classificaties (bv. exactMatch op cross-category)?
6. **NEN-aanraking.** Welke ISO 27001-clausules/Annex-A-controls zijn betrokken? Bevestig dat parafrase volstaat en geen verbatim nodig is.

## 4. Deliverable + stop-conditie

- Rapport: `output/reports/t4-pre-sprint-inventarisatie.md` (bottom-up bouw per Protocol v1.3 §10.2; §1-samenvatting markeren als "INITIEEL — TE BEVESTIGEN"). Metrics-tabellen met scope-annotatie (§10.5). Interne tabel-consistentie (§10.3): Σ(deelverzamelingen) = totaal.
- **Daarna STOPPEN.** Geen pilot, geen stap3, geen mutatie. Masterchat reviewt de inventarisatie en bepaalt of/welke pilot+stap3 volgen — met name op basis van de divergentie-set en de categorie-classificatie.

## 5. Scope-pauze-condities

- Als de overlap-set substantieel afwijkt van 105, of als de provenance-administratie niet blijkt te kloppen (overlap-paren zonder dubbele attributie), of als de categorie-classificatie ambigu is → meld het in het rapport, beslis niet zelf.
- Bij elke structurele verrassing buiten de inventarisatie-scope: Optie A/B/C naar masterchat.

## 6. Wat NIET

- Geen TTL-mutatie, geen applier-script, geen patch-release.
- Geen predicate-herklassificatie — ook niet "alvast" op evidente gevallen.
- Geen formalisering van het cross-category-principe (v1.3.1 = masterchat-werk).
- Geen Spoor A-/dashboard-/explorer-aanraking (dat loopt parallel in de Dashboard-subagent).
- Geen autonome commit; geen architectuurbeslissing.

## 7. Afsluiting

Lever het rapport + een korte oplevernotitie met disclosure-check (vijf categorieën, incl. NEN-tekst-detectie). Bij read-only-analyse is de NEN-tekst-categorie het belangrijkste aandachtspunt.
