# Instructie Dashboard-subagent — Twee verse-load-fixes (demo-robuustheid)

**Van:** masterchat
**Datum:** 29 mei 2026
**Doel-subagent:** Dashboard (Claude Code)
**Bestand:** `dashboard/grc-dashboard-v3-2.html` (Spoor B operationele werkmap)
**Aard:** twee surgische robuustheids-fixes. Geen functionele/visuele herinrichting, geen wijziging aan B7-bron-split (wStruct/wOper) of compliance-logica.

---

## 0. Aanleiding

Masterchat-bron-inspectie (29 mei) bevestigde twee bekende vervolgpunten uit de dashboard-revival, beide demo-relevant: een bestuurder die het dashboard opent moet een gevulde, foutvrije staat zien — nu niet gegarandeerd.

## 1. Fix A — `file://`-laadgedrag (WASM faalt bij dubbelklik)

**Oorzaak (bron-geverifieerd):** `initApp()` roept `initSqlJs({locateFile:f=>`vendor/${f}`})` aan, dat `vendor/sql-wasm.wasm` via fetch laadt. Onder `file://` (dubbelklik op het HTML-bestand) blokkeert de browser die fetch → `initSqlJs` faalt → `catch` zet "DB fout" → `db` blijft undefined → elke latere actie (bv. import → `db.run`) faalt met "undefined is not an object". Werkt wel via `http.server`.

**Fix (geen base64-embed — bewust):** base64-WASM zou het bestand fors vergroten; de http-server-route werkt prima. Maak de fout **zelf-verklarend** in plaats van de laadmethode te herbouwen:

1. **Protocol-detectie vóór init:** als `location.protocol === 'file:'`, toon (in de loader of als prominente melding) een instructie i.p.v. de generieke "DB fout". Voorbeeld-tekst: "Dit dashboard moet via een lokale webserver geopend worden (de database-engine laadt niet vanaf een bestand). Open een terminal in de dashboard-map en draai: `python3 -m http.server 8099`, ga dan naar http://127.0.0.1:8099/grc-dashboard-v3-2.html". Houd de tekst feitelijk en kort.
2. **Behulpzamere generieke catch:** in de bestaande `catch(e)` van `initApp()`, als de fout WASM-/fetch-gerelateerd is, verwijs naar diezelfde http-server-instructie i.p.v. alleen `e.message`.

Geen wijziging aan de `locateFile`-logica zelf; de vendoring blijft zoals 'ie is. Dit is puur een betere foutafhandeling + vroege protocol-check.

## 2. Fix B — `herkomst`-kolom ontbreekt bij verse load

**Oorzaak (bron-geverifieerd):** `migreerStructuurKolommen()` (voegt o.a. `herkomst`, `iri`, `orphan` toe) wordt **alleen** aangeroepen in `importOntologieStructuur()`. In de init-flow (`initApp` → `maakTabellen` → `laadSeedData`) gebeurt dat niet. Vóór de eerste ontologie-import bestaat de `herkomst`-kolom dus niet, terwijl `wOper()`/`wStruct()` ernaar verwijzen → die queries falen stil (de `try/catch` in `sqlOne`/`sqlAll` geeft leeg terug) → KPI's tonen "—" en compliance "0 van 0" bij een verse load.

**Fix:** roep `migreerStructuurKolommen()` ook aan in de init-flow, **na `maakTabellen()`** (en vóór de eerste render/`renderAll`), zodat de structuur-kolommen altijd bestaan — ook zonder import. De functie is al PRAGMA-geguard (idempotent), dus dubbel aanroepen is veilig.

**Verwacht resultaat:** bij een verse load (geen opgeslagen DB, geen import) tonen de KPI's meteen de hand-seed-waarden — compliance ~35% (8 van 23 operationeel beoordeeld), controls = hand-seed-aantal — in plaats van "—". Na een import gedraagt alles zich zoals nu (de migratie draait dan opnieuw, idempotent).

## 3. Verificatie

- **Fix A:** open het bestand via `file://` (dubbelklik) → verwacht: duidelijke http-server-instructie, geen kale "DB fout". Open via `python3 -m http.server` → verwacht: normaal laden, "DB actief".
- **Fix B:** wis localStorage (of incognito) → open via http.server **zonder** te importeren → verwacht: KPI's tonen hand-seed-waarden (compliance ~35%, niet "—"; controls = hand-seed-aantal). Klik dan Ontologie-import → verwacht: 316 controls, compliance blijft 35% (regressie-check — wOper blijft hand-seed).
- **Regressie:** bevestig dat de B7-bron-split (wStruct/wOper), de bron-toggle, en de WCAG-fixes ongemoeid zijn. Deze twee fixes raken alleen init-volgorde + foutafhandeling.
- Draai axe-core niet opnieuw (geen DOM-/stijl-wijziging die WCAG raakt); als Fix A een zichtbare melding-element toevoegt, geef dat wel een correcte contrast + niet te kleine font (conform B9-tokens).

## 4. Discipline

- Geen organisatienaam. Geen wijziging aan bron-split-logica, compliance-berekening, of vendoring-paden.
- Surgical: Fix A = protocol-check + betere catch; Fix B = één extra functie-aanroep in de init-flow. Niets anders.
- Settings.json moet laden (disclosure-hook actief) vóór Write-acties.
- Pre-push disclosure-check (vijf categorieën).
- Geen autonome commit — lever op, de projecteigenaar inspecteert `git diff` en commit handmatig.

## 5. Scope-pauze

Als Fix B onverwacht de compliance-% naar ~0% of een ander getal dan ~35% duwt bij verse load (zou wijzen op een dieper bron-split-probleem), of als de migratie-aanroep in de init-flow een neveneffect heeft op bestaande opgeslagen DB's → stop en meld met Optie A/B/C. Niet zelf doorpatchen.

## 6. Deliverable

- Bijgewerkte `dashboard/grc-dashboard-v3-2.html` (twee surgische wijzigingen).
- Korte oplevernotitie met disclosure-check + de twee verificatie-uitkomsten (file:// + verse load).
