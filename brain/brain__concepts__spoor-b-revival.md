---
type: concept
title: Spoor B-revival — B7-wiring + bron-split 1A + Q-M5 vendoring + B9 WCAG (grc-dashboard-v3-2)
status: living
date: 2026-05-29
related:
  - dashboard-productlijnen
  - H40_dashboard-ui-renderdekking
  - skos-export-filter
sources:
  - dashboard-tussenrapport-b7-wiring-2026-05-29
  - dashboard-rapport-qm5-vendoring-b9-wcag-2026-05-29
  - besluitnotitie-qm-dashboard-2026-05-29
chat-sources: []
confidence: high
---

# Spoor B-revival — grc-dashboard-v3-2 operationeel prototype (29 mei 2026)

## Wat het is

Op 29 mei 2026 is het Spoor B-prototype (`dashboard/grc-dashboard-v3-2.html`, de operationele werkmap — zie [[brain__concepts__dashboard-productlijnen]]) door de Dashboard-subagent gerevitaliseerd in drie opeenvolgende, **niet-architecturale** verbeteringen. Dit concept legt de werkstroom + de drie onderliggende Spoor B-bron-besluiten + twee bekende vervolgpunten vast. **Brein-registratie alleen** — de dashboard-code is dashboard-subagent-werkgebied en is door Brein niet aangeraakt.

> **Brein-oordeel over registratie-vorm:** dit is géén ontologie-sprint (geen TBox/ABox/SKOS-mutatie, baseline-metrics niet geraakt). Het past daarom niet als `brain__sprints__v*`-bestand maar als concept-entry, parallel aan hoe iteratie 15 `cross-category-mappings` als concept registreerde i.p.v. als sprint. De drie bron-besluiten zijn masterchat-besluiten; Brein legt ze vast, interpreteert ze niet.

## De drie revival-componenten

| Component | Inhoud | Bron-rapport |
|---|---|---|
| **B7 — ontologie-structuur-import + bron-split 1A** | Header-knop "⬇ Ontologie-import" → kolom-migratie (`migreerStructuurKolommen()`, idempotent, non-destructief: verwijderde IRI → `orphan=1`, nooit hard-delete) → import van 316 controls / 52 frameworks / 20 rollen. **Bron-split 1A** (zie hieronder): twee expliciete helpers `wStruct()` (structuurlaag → ontologie canoniek) en `wOper()` (operationele laag → hand-seed primair), expliciet per query aangebracht. K3-header toont "· ontologie-structuur v4.6.0 · SKOS-status t/m v4.6.3". Kernregressie-bevestiging: compliance-% blijft de hand-seed-waarde (35%), níét ~0% na import | `dashboard-tussenrapport-b7-wiring-2026-05-29.md` |
| **Q-M5 — lokaal vendoren** | Third-party assets lokaal gevendord naar `dashboard/vendor/` voor offline werking (Rijksoverheid-machine kan CDN blokkeren): Chart.js 4.4.1 + sql.js 1.12.0 (`.js` + `.wasm`) + IBM Plex fonts (36× woff2). SRI-integrity op de script-tags (matcht cdnjs exact). Offline-verificatie (Playwright, alle niet-localhost geblokkeerd): 0 geblokkeerde/mislukte requests, 0 console-errors | `dashboard-rapport-qm5-vendoring-b9-wcag-2026-05-29.md` |
| **B9 — WCAG 2.1 AA-audit + fixes** | axe-core-scan over 5 nav-tabs: **47 → 0** bevindingen (2 critical `select-name` + 45 serious, w.v. 44 `color-contrast` + 1 `scrollable-region-focusable`). Fixes: `aria-label` op 2 selects, `--text4`-token `#4d5358` → `#9097a0` (≥4.54:1), status-pill-kleuren, font-floor 9/10px → 12px / 11px, `tabindex=0`+`role=region` op scroll-containers. Alle fixes in één gemarkeerd override-blok (reviewbaar/reverteerbaar); layout intact, geen regressie | `dashboard-rapport-qm5-vendoring-b9-wcag-2026-05-29.md` |

Alle drie raken uitsluitend laad-bron (Q-M5), presentatie (B9) of wiring (B7) — geen organisatie-data, geen ontologie-mutatie. Disclosure-check op v3-2: geen organisatienaam (alleen generieke roltitels/kaders); framework-neutraal (D9, geen kader bevoorrecht); geen Cytoscape in Spoor B (Q-M3).

## De drie Spoor B-bron-besluiten (één samenhangend pakket — masterchat)

De B7-wiring is het sluitstuk van drie opeenvolgende masterchat-bron-laag-besluiten. Het B7-tussenrapport §6 markeert ze expliciet als "het 3e bron-laag-besluit … als één samenhangend pakket vastleggen in de Brein-cyclus":

| # | Besluit | Inhoud |
|---|---|---|
| **Optie A** | bron-import | Het dashboard importeert de ontologie-**structuur** (frameworks, controls, rollen) als canonieke structuurlaag — niet de operationele status |
| **Optie 1** | co-existentie | De geïmporteerde ontologie-structuurlaag en de bestaande hand-seed-operationele laag **co-existeren** naast elkaar; import is non-destructief voor de hand-seed-laag |
| **1A** | bron-split | De twee lagen worden **expliciet per query** gescheiden via `wStruct()` (structuur → ontologie canoniek) en `wOper()` (operationeel → hand-seed primair); nergens stilzwijgend. Bij divergerende aantallen (316 structuur vs 23 operationeel) labelt de UI per teller ("· structuur" / "· operationele SoA" / "X van Y operationeel beoordeeld") zodat de CSO het niet als inconsistentie leest |

Deze split is de Spoor B-tegenhanger van de Spoor A meet-laag-discipline (ontologie-laag vs export-laag, zie [[brain__concepts__skos-export-filter]]): twee bewust gescheiden datalagen met expliciete labeling i.p.v. één vermengde telling.

## Twee bekende vervolgpunten (geen H-items — bekend-vervolgpunt)

Twee aandachtspunten zijn in de rapporten gemeld als bekend vervolg. Conform Brein-discipline declareer ik hiervoor **geen nieuw H-item** zonder masterchat (de masterchat-benoemde dashboard-kandidaten zijn H42/H43/H44 — zie [[brain__architecture__H-register]]); ze staan hier als bekend-vervolgpunt + in de open-punten-lijst van het brein-rapport iteratie 16:

| # | Vervolgpunt | Detail + fix-richting |
|---|---|---|
| 1 | **`file://`-laadgedrag** | Bij dubbelklik (`file://`) faalt het WASM-laden → "DB fout". Werkt wél via `python3 -m http.server`. **Demo-risico:** een bestuurder die het bestand dubbelklikt ziet een fout. Fix-richting: base64-embedded WASM, of een duidelijke foutmelding-met-instructie ("serveer via http.server / open via de meegeleverde launcher") |
| 2 | **`herkomst`-kolom bij verse load** | Vóór de eerste ontologie-import bestaat de `herkomst`-kolom nog niet (wordt toegevoegd door `migreerStructuurKolommen()` binnen de import) → `wOper()` verwijst dan naar een niet-bestaande kolom → compliance toont "—" i.p.v. %. **Pre-existing B7-gedrag**, niet door Q-M5/B9 veroorzaakt. Fix-richting: kolom-migratie ook in `laadSeedData()` draaien |

## Verifieer-/demo-discipline

Beide rapporten benadrukken een **menselijke visuele pass vóór een CSO/CISO-demo** (de subagent kon de live browser-render in de eigen omgeving niet end-to-end draaien — Chrome/puppeteer-launch-incompatibiliteit, geen codeprobleem; B9 is wél via Playwright met eigen Chromium gedraaid). Serveren via `python3 -m http.server` (relatieve paden + SRI werken zo correct); offline-check via DevTools → Network → Offline.

## Hangt samen met

- [[brain__concepts__dashboard-productlijnen]] — Spoor A vs Spoor B; Q-M-besluiten + Q-M2-reversal
- [[brain__architecture__H40_dashboard-ui-renderdekking]] — Spoor A render-dekking (Q-M4 latent/parked); kandidaten H42/H43/H44 masterchat-benoemd
- [[brain__concepts__skos-export-filter]] — Spoor A meet-laag-analogie van de bron-split

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-29 | living | Concept geboren in Brein-cyclus iteratie 16. Legt de Spoor B-revival vast (B7-wiring + bron-split 1A + Q-M5 vendoring + B9 WCAG 47→0), de drie Spoor B-bron-besluiten (Optie A · Optie 1 · 1A) als één pakket, en twee bekende vervolgpunten (`file://`-laadgedrag + `herkomst`-kolom verse load). Brein-registratie alleen; dashboard-code niet aangeraakt. |

— Einde spoor-b-revival.
