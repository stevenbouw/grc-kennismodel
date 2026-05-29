---
type: dashboard-rapport
title: Twee verse-load-fixes (file://-guard + herkomst-kolom bij init) — Spoor B v3-2
status: opgeleverd — wacht op inspectie + commit door projecteigenaar
date: 2026-05-29
subagent: Dashboard
spoor: B (operationele werkmap-prototype)
werkbestand: dashboard/grc-dashboard-v3-2.html
instructie: docs/instructies/instructie-dashboard-verse-load-fixes.md (masterchat 2026-05-29)
---

# Dashboard verse-load-fixes — Oplevernotitie

> **Aard:** twee surgische robuustheids-fixes voor demo-betrouwbaarheid. Geen functionele/visuele
> herinrichting, geen wijziging aan B7-bron-split (`wStruct`/`wOper`), compliance-berekening of
> vendoring-paden. Diff: **28 inserts / 4 deletes** in één bestand.

## Uitgangspunt
`git pull` op `main`: already up to date. Instructie-commit `10acde9` aanwezig. Q-M5/B9-commit
`ec138a5` (vorige sessie) zit in de history. Brain/-wijzigingen in de working tree zijn van een
parallelle Brein-cyclus — **niet aangeraakt**.

---

## Fix A — `file://`-laadgedrag (WASM faalt bij dubbelklik)

**Oorzaak:** onder `file://` blokkeert de browser de `vendor/sql-wasm.wasm`-fetch → `initSqlJs` faalt
→ oude `catch` toonde kale "DB fout" → `db` bleef undefined → latere acties faalden cryptisch.

**Fix (geen base64-embed, geen wijziging aan `locateFile`/vendoring — alleen betere foutafhandeling):**
1. **Vroege protocol-check** bovenin `initApp()`: bij `location.protocol === 'file:'` meteen
   `toonServerInstructie()` + `return` (vóór de init-poging).
2. **Behulpzamere catch:** bij een WASM-/fetch-gerelateerde fout (regex op `e.message`) verwijst de
   catch nu naar dezelfde http-server-instructie i.p.v. `e.message`; niet-WASM-fouten houden de
   bestaande "DB fout"-afhandeling.
3. **Nieuw melding-element** `toonServerInstructie()` — toont in de loader een feitelijke instructie:
   *"Dit dashboard moet via een lokale webserver geopend worden … `python3 -m http.server 8099` …
   http://127.0.0.1:8099/grc-dashboard-v3-2.html"*, met de spinner verborgen.
   **B9-conform:** kop 16px (`--text`), body 14px (`--text2`), code-block 13px mono (`--green-br`
   op `--bg2`), URL mono (`--cyan-lt`) — alle ≥13px, hoog contrast op donkere achtergrond.

## Fix B — `herkomst`-kolom ontbreekt bij verse load

**Oorzaak:** `migreerStructuurKolommen()` (voegt o.a. `herkomst` toe) werd alléén in
`importOntologieStructuur()` aangeroepen. Vóór de eerste import bestond de kolom niet, terwijl
`wOper()`/`wStruct()` ernaar verwijzen → queries faalden stil → KPI's toonden "—".

**Fix:** één extra aanroep `migreerStructuurKolommen()` in de verse-init-flow, **ná `maakTabellen()`
en vóór `laadSeedData()`/render**. Functie is PRAGMA-geguard (idempotent). Aanroep staat in het
verse-pad (`!herstel`), zodat **bestaande opgeslagen DB's niet geraakt worden** (conform de
scope-pauze-waarschuwing in de instructie).

---

## Verificatie (Playwright + bundled Chromium / http.server)

| # | Scenario | Verwacht | Resultaat |
|---|---|---|---|
| A | `file://` (dubbelklik) | duidelijke http-server-instructie, geen kale "DB fout" | `db-status`="Lokale webserver vereist", instructie + code getoond, spinner verborgen — **PASS ✓** |
| A' | via `http.server` | normaal laden | `DB actief · SQLite via sql.js` — **PASS ✓** |
| B | verse load, **geen** import (lege localStorage) | compliance ~35%, controls = hand-seed, niet "—" | compliance **35%** · "8 van 23 operationeel beoordeeld" · controls **23** · 0 console-errors — **PASS ✓** |
| B' | dáárna Ontologie-import | 316 controls, compliance blijft 35% | controls **316** · compliance **35%** — **PASS ✓** |

**Regressie — bron-split / bron-toggle ongemoeid:**

| Bron | Compliance | Controls |
|---|---|---|
| auto | 35% | 316 |
| ontologie | — | 316 |
| handmatig | 35% | 23 |
| alle | 2% | 339 |

Identiek aan de waarden vóór deze fixes → `wStruct`/`wOper`, bron-toggle en compliance-logica
ongewijzigd. **WCAG-fixes (B9-override-blok) niet aangeraakt** — geen DOM-/stijl-wijziging die
bestaande WCAG-conformiteit raakt; het nieuwe melding-element is zelf B9-conform gestyled.
Scope-pauze-conditie (compliance ≠ ~35% of neveneffect op opgeslagen DB's) **niet getriggerd**.

---

## Disclosure-check (vijf categorieën)
- **Organisatienaam:** niet genoemd. ✓
- **Framework-neutraal (D9):** geen framework bevoorrecht; fixes raken alleen init-volgorde + foutafhandeling. ✓
- **Geen Cytoscape/graaf in Spoor B:** niet geïntroduceerd. ✓
- **NEN-parafrase-discipline:** geen NEN-tekst toegevoegd. ✓
- **Disclosure-hook:** actief tijdens alle Write/Edit-acties; geen blokkering/secret-melding. ✓
- **Geen autonome commit:** niets gecommit/gepusht. ✓

---

## Deliverable
- Bijgewerkte `dashboard/grc-dashboard-v3-2.html` (twee surgische wijzigingen).
- Deze oplevernotitie: `output/reports/dashboard-rapport-verse-load-fixes-2026-05-29.md`.

> Verificatie-toolchain in `/tmp/grc-wcag-tooling/` (buiten de repo). Screenshot van de
> file://-instructie ter controle gemaakt (niet in repo opgenomen).
