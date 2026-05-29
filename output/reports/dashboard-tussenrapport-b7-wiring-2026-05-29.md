# Tussenrapport — B7-wiring afgerond (Optie 1A bron-split)

- **Subagent:** Dashboard (Claude Code)
- **Datum:** 2026-05-29
- **Sprint:** Spoor B revival, B7-sluitstuk — na masterchat-GO op Optie 1A
- **Status:** ✅ wiring gebouwd + geverifieerd (syntax + SQL-semantiek) · ⚠️ live browser-render niet uitvoerbaar in deze omgeving (zie §5)
- **Niet gecommit** — projecteigenaar inspecteert `git diff` en commit handmatig.

## 1. Wat is gebouwd (in `grc-dashboard-v3-2.html` + script)

| Onderdeel | Implementatie |
|---|---|
| **Kolom-migratie** (K1) | `migreerStructuurKolommen()` — PRAGMA-geguard: voegt `iri`/`herkomst`/`bron_versie`/`orphan`/`owl_klasse` toe waar ze ontbreken (o.a. `owl_klasse` op `controls`). Idempotent. |
| **Import-knop** | Header-knop "⬇ Ontologie-import" → `importOntologieStructuur()`: migratie → `db.run(window.STRUCTURE_IMPORT.sql)` → autoSave → render. `confirm()`-bevestiging; non-destructief. |
| **Bron-split (1A)** | Twee expliciete helpers: `wStruct()` (structuurlaag → ontologie canoniek) en `wOper()` (operationele laag → hand-seed primair). **Expliciet per query** aangebracht (voorwaarde 1), nergens stilzwijgend. |
| **Bron-toggle** | Header-`<select>` "Bron: auto / ontologie / handmatig / alle" → `setBron()`. Houdt de andere laag zichtbaar (voorwaarde: filter). |
| **K3-header** | `updateK3()` toont `· ontologie-structuur v4.6.0 · SKOS-status t/m v4.6.3` in de header-sub (uit `ontologie_import_meta`). |
| **IRI-anker** | Controls-lijst toont 🔗 met de IRI als tooltip op geïmporteerde rijen (traceerbaarheid). |
| **`.js`-wrapper** | `import-from-ontology.py` genereert nu ook `structure-import-v4_6_0.js` (`window.STRUCTURE_IMPORT`), via `<script src>` geladen — werkt onder `file://` (waar `fetch()` faalt). |

### Bron-mapping (voorwaarde 1 — expliciet per query)
- **Structuurlaag → `wStruct()` (ontologie canoniek):** totaal-controls-KPI, ISO/BIO/NIST-tellingen, "controls per framework"-chart, controls-lijst (+IRI).
- **Operationele laag → `wOper()` (hand-seed primair):** compliance-%, implementatiestatus-charts, SoA-lijst + SoA-count, compliance-tab-%, rollen + rollen-bezet-% + RACI-context.
- **Roltabel bewust omgekeerd:** hand-seed primair; geïmporteerde ontologie-rollen als telbare referentie ("+20 ontologie-ref").

### Labeling bij divergerende aantallen (voorwaarde 2)
- Controls-lijst-teller: `… · structuur`. SoA-teller: `… · operationele SoA`. Compliance-KPI-sub: "X van Y **operationeel beoordeeld**" (noemer = operationele telling, niet de structuur-316). Zo leest de CSO 316 (structuur) vs 23 (operationeel) niet als inconsistentie.

## 2. Verificatie — SQL-bron-semantiek (de regressie-check, voorwaarde 3)

Gesimuleerd via `sqlite3` met de echte v3-2-schema + 5 hand-seed-controls (2 Volledig) + de import-bundle:

| | controls-lijst (structuur) | compliance-% | rollen |
|---|---|---|---|
| **vóór import** | 5 (hand-seed) | **40%** (over 5) | 3 |
| **ná import** | **316** (ontologie) | **40%** (over 5 hand-seed — **niet ~0%** ✅) | 3 (+20 ontologie-ref) |

Toggle ná import: `ontologie`→316 · `handmatig`→5 · `alle`→321. **De kernregressie die je markeerde (compliance blijft hand-seed, niet ~0%) is bevestigd.**

## 3. Verificatie — overig
- ✅ **JS-syntax** van het volledige inline-script (72k tekens) na álle ~20 edits: `node --check` OK.
- ✅ **Idempotent + non-destructief** (uit B7-pijplijn-self-test): re-run identiek; verwijderde IRI → `orphan=1`, nooit hard-delete; handmatige rijen ongemoeid.
- ✅ **Gates:** settings.json `$schema` + disclosure-hook actief; disclosure-scan op v3-2 = geen organisatienaam (alleen generieke roltitels/kaders).
- ✅ `http.server` serveert `grc-dashboard-v3-2.html` + `structure-import-v4_6_0.js` (HTTP 200).

## 4. Deliverables (working tree, untracked/gewijzigd)
- `dashboard/grc-dashboard-v3-2.html` (M) — wiring.
- `dashboard/import-from-ontology.py` (??) — pijplijn (+ `.js`-emit).
- `dashboard/structure-import-v4_6_0.sql` + `.js` (??) — bundle + wrapper.

## 5. Niet geverifieerd — live browser-render
Headless render (Chrome via puppeteer-core) **kon niet draaien**: Chrome-launch hangt in deze omgeving (ook met `--no-sandbox`, eigen `user-data-dir` en sandbox uit) — een Chrome/puppeteer-launch-incompatibiliteit, geen codeprobleem. Daardoor niet live geverifieerd: Chart.js-tekening, volledige init-flow en de import-knop-klik end-to-end visueel.

**Aanbevolen visuele pass (jij, conform je eigen voorwaarde "menselijke blik vóór CSO"):**
```
cd dashboard && python3 -m http.server 8765
# open http://localhost:8765/grc-dashboard-v3-2.html
# 1) check: KPI's + compliance-% tonen hand-seed-waarden (niet leeg/0%)
# 2) klik "⬇ Ontologie-import" → bevestig
# 3) check: "Totaal controls" → 316; Controls-lijst → 316 met 🔗-IRI; compliance-% ongewijzigd;
#    header toont "· ontologie-structuur v4.6.0 · SKOS-status t/m v4.6.3"; toggle "Bron" werkt
```
Als je wilt dat ik headless + axe-core (WCAG) alsnog draai, kan ik puppeteer/playwright met een gedownloade Chromium proberen i.p.v. system-Chrome — maar dat vergt een grotere install.

## 6. Open / vervolg
- **B9 (WCAG):** nog niet uitgevoerd (axe-core hangt aan de render-omgeving). Dark-theme-contrast + 10px-fonts blijven aandachtspunt.
- **Q-M5 (vendoren):** v3-2 laadt Chart.js/sql.js nog van CDN — vóór een CSO-demo lokaal vendoren in `dashboard/vendor/`.
- **Brein-pakket:** dit is het 3e bron-laag-besluit (Optie A · Optie 1 · 1A) — als één samenhangend pakket vastleggen in de Brein-cyclus (genoteerd).

## 7. Niet-gedaan (bewust)
- ❌ Geen commit.
- ❌ Geen CDN-vendoring (Q-M5, aparte stap).
- ❌ Geen B9/axe-core-run (render-omgeving).
