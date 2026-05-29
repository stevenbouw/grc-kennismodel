---
type: dashboard-rapport
title: Q-M5 lokaal vendoren + B9 WCAG 2.1 AA-audit & fixes (Spoor B, grc-dashboard-v3-2)
status: opgeleverd — wacht op inspectie + commit door projecteigenaar
date: 2026-05-29
subagent: Dashboard
spoor: B (operationele werkmap-prototype)
werkbestand: dashboard/grc-dashboard-v3-2.html
---

# Q-M5 + B9 — Oplevernotitie (Spoor B, dashboard v3-2)

> **Karakter:** twee opeenvolgende, niet-functionele verbeteringen aan het Spoor B-prototype.
> **STAP 1 (Q-M5)** = third-party assets lokaal vendoren voor offline werking.
> **STAP 2 (B9)** = WCAG 2.1 AA-audit (axe-core) + contrast/font/aria-fixes.
> Beide raken **uitsluitend** laad-bron resp. presentatie — de B7-wiring, bron-split
> (`wStruct`/`wOper`) en compliance-berekening zijn **niet** aangeraakt en blijven aantoonbaar intact.

## Uitgangspunt

- `git pull` op `main`: **already up to date**. B7-wiring-commit `4881a9a`
  (*feat(dashboard): B7 ontologie-import + bron-split 1A in Spoor B (v3-2)*) aanwezig, inclusief
  `grc-dashboard-v3-2.html`, `import-from-ontology.py`, `structure-import-v4_6_0.{sql,js}`. Basis vastgelegd.

---

## STAP 1 — Q-M5: lokaal vendoren

### Reden
Een Rijksoverheid-machine kan CDN's blokkeren; de CSO/CISO-demo **moet offline werken**.
v3-2 laadde voorheen drie externe bronnen.

### Gevendord → `dashboard/vendor/` (versies gepind, integriteit gecross-checkt tegen cdnjs)

| Resource | Library | Versie | SRI-integriteit |
|---|---|---|---|
| `chart.umd.min.js` | Chart.js | 4.4.1 | sha512 — **matcht cdnjs-gepubliceerde SRI exact** ✓ |
| `sql-wasm.js` | sql.js | 1.12.0 | sha512 — **matcht cdnjs-gepubliceerde SRI exact** ✓ |
| `sql-wasm.wasm` | sql.js | 1.12.0 | wasm magic-bytes valide; sha512 gepind (cdnjs publiceert geen SRI voor .wasm) |
| `fonts.css` + `fonts/` (36× woff2) | IBM Plex Mono/Sans/Serif | Google Fonts v20 | 0 externe URLs na herschrijving |

- SRI-`integrity` toegevoegd op de twee `<script>`-tags (Chart.js + sql.js).
- SHA256 van alle bestanden: `dashboard/vendor/file_hashes.txt`. Manifest: `dashboard/vendor/VENDOR.md`.
- **Google Fonts mee-gevendord** (buiten de letterlijke twee genoemde libs): zonder dit zou de
  `<link>` nog een externe request doen → doel "zonder externe requests" niet gehaald. Zelfde
  klasse-wijziging (alleen laad-bron), daarom meegenomen.

### Wijzigingen in `grc-dashboard-v3-2.html` (alleen laad-bron)
- `<link>` Google Fonts CDN → `vendor/fonts.css`
- `<script>` Chart.js CDN → `vendor/chart.umd.min.js` + `integrity`
- `<script>` sql.js CDN → `vendor/sql-wasm.js` + `integrity`
- `initSqlJs({locateFile: f=>`vendor/${f}`})` → laadt `vendor/sql-wasm.wasm` lokaal

### Offline-verificatie (Playwright bundled Chromium — **niet** system-Chrome)
Geserveerd via `python3 -m http.server`, **alle niet-localhost requests geblokkeerd** in de browser:
- Geblokkeerde externe requests: **0** · Mislukte requests: **0** · Console-errors: **0**
- Chart.js geladen ✓ · sql.js WASM actief (`DB actief · SQLite via sql.js`) ✓ · IBM Plex lokaal geladen ✓

---

## STAP 2 — B9: WCAG 2.1 AA-audit + fixes

### Toolchain
Playwright met **eigen meegeleverde Chromium** (`npx playwright install chromium`, headless-shell 148) +
`@axe-core/playwright`. Bewust niet de system-Chrome (die liep eerder vast). Scan over de 5 nav-tabs,
in de realistische post-import-staat, gededupliceerd op rule + target.

### Baseline (VOOR) — `output/reports/axe-qm5b9-voor-2026-05-29.json`
**47 unieke bevindingen — 2 critical, 45 serious:**

| Ernst | Rule | WCAG | n | Oorzaak |
|---|---|---|---|---|
| critical | `select-name` | 4.1.2 | 2 | `#bron-sel` + `#sf-rollen-stelsel` zonder toegankelijke naam |
| serious | `color-contrast` | 1.4.3 | 44 | 36× muted tekst `#4d5358` (2.17–2.31:1); 8× gekleurde status-pills (`.br`/`.bb`/`.bp`, 4.28–4.45:1) |
| serious | `scrollable-region-focusable` | 2.1.1 | 1 | `.tscroll` tabel-regio niet keyboard-focusbaar |

Betrokken te-kleine fonts: 33× 10px, 10× 12px, 1× 9px.

### Fixes (geprioriteerd: critical → serious; geconsolideerd in één gemarkeerd B9-blok)
Alle CSS-fixes staan in één override-blok onderaan de `<style>`; de originele regels zijn
onaangeroerd → diff is reviewbaar en reverteerbaar.

1. **`select-name` (critical):** `aria-label` toegevoegd op `#bron-sel` ("Weergavebron kiezen")
   en `#sf-rollen-stelsel` ("Filter op stelsel").
2. **Contrast muted tekst (1.4.3):** `--text4` `#4d5358` → `#9097a0` (≥4.54:1 op álle paneel-bg's,
   incl. lichtste `#24303f`). Dekt 36 bevindingen in één token.
3. **Contrast status-pills (1.4.3):** `.br` → `#ff8389` (6.0+), `.bb` → `#6ba5ff` (5.8+),
   `.bp` → `#bb8dff` (5.9+) op hun getinte achtergronden.
4. **Leesbaarheid (1.4.4):** font-floor — readability-tekst 9/10px → **12px**;
   dense micro-labels/badges → **11px**. Geen layout-herinrichting (zie verificatie).
5. **`scrollable-region-focusable` (2.1.1):** kleine B9-init zet `tabindex=0` + `role="region"`
   + `aria-label` op alle `.tscroll`-containers.

### Resultaat (NA) — `output/reports/axe-qm5b9-na-2026-05-29.json`
**0 bevindingen.** Alle 2 critical + 45 serious opgelost. WCAG 2.1 AA-clean op alle 5 tabs.

| | Critical | Serious | Totaal |
|---|---|---|---|
| Voor | 2 | 45 | 47 |
| **Na** | **0** | **0** | **0** |

### Scope-discipline
De fixes bleven binnen **contrast/font/aria-bijwerken** — geen structurele layout-herinrichting,
geen vormgevings-herziening. Visuele controle (screenshots overzicht + risk, 1440×900, full-page)
bevestigt: layout intact, beide Chart.js-grafieken renderen, badges leesbaar, geen overflow.
**Geen scope-pauze nodig.** De bredere visuele upgrade blijft een aparte, latere sessie.

---

## Regressie-check (B7-wiring / bron-split / compliance ongewijzigd)
Na alle fixes, offline, via de import-knop + `setBron()`:

| Bron-stand | Compliance | Controls | Duiding |
|---|---|---|---|
| auto | **35%** | 316 | hand-seed-compliance (8/23 Volledig); structuur=ontologie |
| ontologie | — | 316 | ontologie-rijen hebben geen operationele status (conform B7-ontwerp) |
| handmatig | **35%** | 23 | alleen hand-seed-laag |
| alle | 2% | 339 | alles samengevoegd |

- Compliance toont de **hand-seed-waarde 35%** (níét ~0%). ✓
- **Ontologie-import-knop** werkt (52 fw · 316 controls · 20 rollen). ✓
- **Bron-toggle** werkt en geeft per stand het verwachte, semantisch-correcte resultaat. ✓
- 0 console-errors. **Geen regressie** in data-/bron-/compliance-logica.

> **Observatie (buiten scope, niet gefixt):** op een *verse* load zonder gepersisteerde `.db`
> en vóór de eerste ontologie-import bestaat de `herkomst`-kolom nog niet (die wordt toegevoegd
> door `migreerStructuurKolommen()` binnen `importOntologieStructuur()`). De `wOper()`-query
> verwijst dan naar een niet-bestaande kolom → compliance toont "—" i.p.v. een %. Dit is
> **pre-existing B7-gedrag**, niet door deze sessie veroorzaakt, en valt buiten Q-M5/B9. Ter
> overweging voor een latere sessie (bv. kolom-migratie ook in `laadSeedData()` draaien).

---

## Disclosure-check (oplevereis)
- **Organisatienaam:** niet genoemd; "Rijksoverheidsorganisatie" / "de organisatie" gehanteerd. ✓
- **Framework-neutraal (D9):** geen framework architecturaal bevoorrecht; alle accenten zijn
  louter visuele status-kleuren. ✓
- **Geen Cytoscape/graaf in Spoor B:** niet geïntroduceerd. ✓
- **NEN-parafrase-discipline:** geen NEN-tekst toegevoegd; bestaande clausule-verwijzingen ongemoeid. ✓
- **Disclosure-hook:** actief tijdens alle Write/Edit-acties; geen blokkering/secret-melding. ✓
- **Geen autonome commit:** niets gecommit/gepusht — projecteigenaar inspecteert `git diff` en commit. ✓

---

## Deliverables (locaties)
| Artefact | Locatie |
|---|---|
| Gevendorde assets | `dashboard/vendor/` (chart.umd.min.js, sql-wasm.js, sql-wasm.wasm, fonts.css, fonts/*.woff2) |
| Vendor-manifest | `dashboard/vendor/VENDOR.md` |
| File-hashes (SHA256) | `dashboard/vendor/file_hashes.txt` |
| Bijgewerkt dashboard | `dashboard/grc-dashboard-v3-2.html` |
| axe-rapport VOOR | `output/reports/axe-qm5b9-voor-2026-05-29.json` (47 bevindingen) |
| axe-rapport NA | `output/reports/axe-qm5b9-na-2026-05-29.json` (0 bevindingen) |
| Deze oplevernotitie | `output/reports/dashboard-rapport-qm5-vendoring-b9-wcag-2026-05-29.md` |

> Toolchain (Playwright + axe-core + verificatiescripts) staat in `/tmp/grc-wcag-tooling/` —
> bewust buiten de repo (geen `node_modules`-vervuiling). Deliverable is het rapport, niet de tooling.

---

## Visuele-pass-instructie voor de projecteigenaar

**1. Lokaal serveren (relatieve paden + SRI werken zo correct):**
```
cd dashboard
python3 -m http.server 8099
```
Open: `http://127.0.0.1:8099/grc-dashboard-v3-2.html`

**2. Netwerk-uit-check (offline bewijs):**
- Open DevTools → tab **Network**.
- Zet throttling op **Offline** (of trek de wifi/ethernet eruit), **herlaad** de pagina.
- Verwacht: dashboard laadt volledig; **geen** requests naar `cdnjs.cloudflare.com`,
  `fonts.googleapis.com` of `fonts.gstatic.com`; alle assets komen van `127.0.0.1`.

**3. Functionele steekproef (regressie):**
- Klik **⬇ Ontologie-import** → bevestig → compliance-KPI toont **35%**, controls **316**.
- Wissel **Bron**-dropdown (auto → handmatig → alle) → cijfers veranderen zonder fout.

**4. Visuele controle WCAG:**
- Muted subtitels/labels (header, KPI-subteksten) zijn nu duidelijk leesbaar (lichter grijs).
- Status-badges (rood/blauw/paars) leesbaar; geen tekst kleiner dan ~11px.
