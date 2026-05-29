# vendor/ — lokaal gevendorde third-party assets (Q-M5)

**Doel:** `grc-dashboard-v3-2.html` (Spoor B) moet **volledig offline** draaien — een
Rijksoverheid-machine kan CDN's blokkeren, en de CSO/CISO-demo mag niet afhankelijk
zijn van externe requests. Alle voorheen-CDN-resources zijn hier lokaal gepind.

**Geen functionele wijziging** — alleen de laad-bron. Data-/bron-/compliance-logica
(B7-wiring, bron-split wStruct/wOper) ongewijzigd.

## Gepinde versies + integriteit

| Bestand | Library | Versie | Bron | SRI (sha512) | Status |
|---|---|---|---|---|---|
| `chart.umd.min.js` | Chart.js | 4.4.1 | cdnjs | `sha512-CQBWl4fJHWbryGE+…UyZAWw==` | ✓ matcht cdnjs-SRI |
| `sql-wasm.js` | sql.js | 1.12.0 | cdnjs | `sha512-tz0jOZaOg9RtWWB6…17Vw0w==` | ✓ matcht cdnjs-SRI |
| `sql-wasm.wasm` | sql.js | 1.12.0 | cdnjs | `sha512-danYXf4HJ8/l0CUS…WRLjIg==` | wasm (cdnjs publiceert geen SRI) |
| `fonts.css` + `fonts/*.woff2` | IBM Plex Mono/Sans/Serif | Google Fonts v20 | fonts.googleapis.com | n.v.t. (36 woff2 lokaal) | 0 externe URLs |

SHA256 (file-hash-verificatie) staat in `vendor/file_hashes.txt`.

## Wijzigingen in v3-2.html

- `<link>` Google Fonts → `vendor/fonts.css`
- `<script>` Chart.js CDN → `vendor/chart.umd.min.js` + `integrity` (SRI)
- `<script>` sql.js CDN → `vendor/sql-wasm.js` + `integrity` (SRI)
- `initSqlJs({locateFile: f=>`vendor/${f}`})` → laadt `vendor/sql-wasm.wasm` lokaal

## Verversen

Bij een library-upgrade: nieuwe versie van cdnjs halen, SRI cross-checken tegen
`https://api.cdnjs.com/libraries/<lib>/<versie>?fields=sri`, hashes hier + in
`file_hashes.txt` bijwerken, en de `integrity`-attributen in v3-2.html aanpassen.

## Serveren

Draai via een lokale statische server vanuit `dashboard/` (zodat relatieve paden +
SRI correct werken), bv. `python3 -m http.server`. Zie oplevernotitie voor de
netwerk-uit-check.
