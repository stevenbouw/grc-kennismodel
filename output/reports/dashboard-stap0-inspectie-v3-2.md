# STAP 0 — Inspectierapport `grc-dashboard-v3-2.html` (Spoor B revival)

- **Subagent:** Dashboard (Claude Code)
- **Datum:** 2026-05-29
- **Opdracht:** `docs/instructies/dashboard-revival-v4_6_3.md` §3 (beantwoordt Q-D5 + Q-D7)
- **Methode:** code-inspectie (geen browser-render — zie §0). Read-only; geen mutatie.
- **Status:** ⏸️ STAP 0 afgerond — **wacht op masterchat-akkoord vóór bouwsteen-volgorde §4** (instructie §3 + §4).
- **Niet gecommit** — projecteigenaar inspecteert `git diff` en commit handmatig.

---

## 0. Methode-disclaimer

Dit oordeel berust op statische code-inspectie van `dashboard/grc-dashboard-v3-2.html` (1.735 regels, 127 kB) plus signaal-extractie over de vijf aangrenzende varianten. Ik heb het dashboard **niet in een browser gerenderd**: SQL.js-init, Chart.js-tekening, modal-flows en WCAG-gedrag ken ik uit de code, niet uit observatie. "Werkt" hieronder betekent "code is volledig en plausibel functioneel", niet "live geverifieerd". Een render-smoke-test is een logische eerste stap ná akkoord (raakt Q-D6 — kan de subagent zelf renderen).

---

## 1. Bestand-inventarisatie + actief vs. artefact (Q-D7)

Alle zes `grc-dashboard*.html` dateren identiek (21 mei 2026 17:04) en kwamen samen binnen via de **initial commit** (`d33e1e4`). Het zijn dus geen parallelle werkbestanden maar een **bewaarde iteratie-reeks**.

| Bestand | Regels | kB | Titel | Engine | Oordeel |
|---|---|---|---|---|---|
| `grc-dashboard.html` | 1.086 | 43 | "GRC Dashboard — Nederlandse Overheidsorganisatie" | Chart.js | 🗄️ artefact (vroegste iteratie) |
| `grc-dashboard-2.html` | 675 | 49 | idem | Chart.js | 🗄️ artefact |
| `grc-dashboard-3.html` | 675 | 49 | idem | Chart.js | 🗄️ artefact |
| `grc-dashboard-v2.html` | 1.115 | 87 | "GRC Dashboard v2.0 — Rijksoverheidsorganisatie" | Chart.js | 🗄️ artefact |
| `grc-dashboard-v3.html` | 1.188 | 90 | "GRC Dashboard v2.0 — Rijksoverheidsorganisatie" | Chart.js | 🗄️ artefact |
| **`grc-dashboard-v3-2.html`** | **1.735** | **127** | **"GRC Dashboard v3.0 — Rijksoverheidsorganisatie"** | **SQL.js + Chart.js** | ✅ **actief werkbestand** |

**Conclusie Q-D7:** `grc-dashboard-v3-2.html` is het enige bestand met een **SQL.js-data-laag** en is unaniem het meest complete en recentste. De andere vijf zijn historische Chart.js-only-iteraties (statische demo-dashboards zonder persistente data-laag). Aanbeveling: behoud als artefact (reproduceerbaarheid), maar markeer `v3-2` als de canonieke basis. Een latere opruim-/archiveer-beslissing (bv. `dashboard/archief/`) is een aparte masterchat-vraag, geen STAP 0-actie.

---

## 2. v3-2 feature-staat — werkt / stub / geparkeerd

v3-2 is een **single-file SQL.js-applicatie**: SQLite-in-WASM, met `localStorage`-persistentie van de geëxporteerde `.db`. Structuur: 5 hoofdtabs (`overzicht`, `governance`, `risk`, `compliance`, `isms`) met geneste sub-tabs.

### 2.1 Data-laag — ✅ werkt, ⚠️ hand-geseed

- **9 tabellen** (`maakTabellen`, regel 824): `frameworks`, `controls`, `risicos`, `risico_controls` (N:M-junction), `rollen`, `documenten`, `audit_bevindingen`, `kalender`, `audit_trail`. Schema is rijk en doordacht (timestamps `aangemaakt_op`/`gewijzigd_op`, cross-framework-ref-velden op controls: `nis2_ref`/`dora_ref`/`bio_ref`/`nist_ref`).
- **Seed-data** (`laadSeedData`, regel 839): handmatig ingebouwde demo-set — 15 frameworks, **23 controls** (een SoA-*sample*, geen volledige 93), 4 risico's + 7 risico-control-koppelingen, 10 rollen, 8 documenten, 2 audit-bevindingen, 10 kalender-events.
- **Geen ontologie-import.** De data is met de hand getypt, niet uit `grc-data-v4_X_Y.json` of de TTL-modules geëxtraheerd. → **Bouwsteen B7 (import-pijplijn A→B) ontbreekt volledig** — dit is de grootste functionele lacune en het kritieke pad uit §4.

### 2.2 CRUD — ✅ werkt

- Volledige modal-CRUD per entiteit: `modalRisico`, `modalControl`, `modalRol`, `modalDocument`, `modalBevinding`, `modalKalender`, plus `modalDelete`. Generieke `buildForm`/`getFormData`/`saveModal`-laag met veld-definities (incl. `required` + placeholders).
- INSERT/UPDATE/DELETE via `sqlRun`; UI ververst via de `renderXxx`-functies.

### 2.3 Charts — ✅ werkt (6 stuks)

`mkChart`-wrapper (regel 1415, de enige `new Chart`) + `renderCharts` voeden 6 canvassen: controls-per-framework, compliance-status-overzicht, risicobereidheid-radar, behandelingsverdeling, implementatiestatus-totaal, KRI. → **Bouwsteen B2 grotendeels af.**

### 2.4 Audit-trail — 🟡 werkt basaal, niet Rijksoverheid-hard

- Tabel `audit_trail` + `auditTrail()`-render + INSERT-logging bij schrijfacties (regel 999).
- **Maar:** géén DB-trigger die UPDATE/DELETE op audit-rijen blokkeert (append-only is app-conventie, niet afgedwongen), en **géén hash-chain** (`hash_prev_row` ontbreekt). → **Bouwsteen B3 is half af**: structuur aanwezig, integriteits-hardening (B3-kern voor Rijksoverheid) ontbreekt.

### 2.5 RACI — ✅ werkt

Echte RACI-matrix (`renderRaci`/`raciCell`/`RACI_DATA`, regel 1134+) met 8 rol-kolommen (SG/DG, CIO, CISO, BVA, BVC, FG, ISSO, Audit). Gekoppeld aan een "Ontologie-lens M4 Roles"-paneel dat de RACI-properties toont (`isResponsibleFor` · `isAccountableFor` · `isConsultedFor` · `isInformedAbout`). → **Bouwsteen B4 af** (op import na — rollen zijn hand-geseed).

### 2.6 Kalender — ✅ werkt, native

`renderKalender` + `modalKalender` + `kalender`-tabel + **iCal-export** (`expIcal`). Native implementatie — **geen FullCalendar**. → **Bouwsteen B5 af** in native vorm (consistent met de "dunste optie" uit §4 stap 6).

### 2.7 Compliance / SoA / heatmap / governance — ✅ werkt (méér dan spec)

Naast de spec: Statement of Applicability (`renderSoA` + `exportSOACSV`), risk-heatmap (`renderHeatmap`/`hmClick`), non-conformiteit-tracking (`renderNC`/`renderFindings`), governance-model-view (`renderGovModel`), KPI-dashboard (`updateKPIs`).

### 2.8 Export / import — ✅ rijk (Bouwsteen B11 grotendeels af)

- Export: `.db`-dump (`exportDB`, regel 978), CSV (`exportCSV`), SoA-CSV (`exportSOACSV`), **TTL ABox-export van het risico-register** (`exportTTLRegister`, regel 1682 → `risicos-abox-*.ttl`), iCal (`expIcal`).
- Import: `.db`-import (`importDB`). → **Géén** ontologie-import (= B7, zie 2.1).
- Persistentie: `autoSave` + `loadFromStorage` (localStorage).

### 2.9 Ontologie-lens — ✅ werkt, read-only conceptueel

Meerdere panelen tonen **SPARQL-queries** (bv. de BIO-control-query in de framework-metadata) en OWL-klasse-verwijzingen. Dit is een *illustratieve* koppeling (getoonde query-strings), geen live SPARQL-engine. Conceptueel waardevol; geen functionele afhankelijkheid.

---

## 3. Welke ontologie-versie representeert de data?

**Geen expliciete versie-binding.** De data draagt nergens een `v4.x.y`-marker; de header toont "v3.0 Database" (= de Spoor B-eigen versie-track, niet de ontologie-versie). De seed is een **curated snapshot die conceptueel aansluit** op de ontologie-baseline:

- Frameworks + modules matchen de ontologie-structuur: BIO 2.0 v1.3 (M08), NIS2 (M10), DORA (M12), NIST 800-53 R5 (M11), ISO-serie (M02/M03/M09/M13), VIR/VIRBI (M01), BVA/CIO-stelsel (M04), CBW (M05).
- Rollen matchen M04 (`roles:CISO`, `roles:BVA`, …); het BIO-paneel toont "93 controls + 148 maatregelen" als **weergegeven metric** (niet als geseede rij-telling).

→ **Bevinding K3:** de geïmporteerde-ontologie-versie is **niet zichtbaar** in Spoor B. Dat moet via B7-import als metadata komen (instructie §4 stap 11). Voor nu: de data benadert een baseline rond de v4.6.x-structuur, maar is een handmatige demo-set, niet een geverifieerde export van v4.6.3.

---

## 4. Mapping op de bouwsteen-volgorde §4 (kern voor masterchat)

De inspectie verschuift §4 fundamenteel: het kritieke pad is **niet** "B1→B6 bouwen" maar "B7 toevoegen + B3 harden + B8/B9/K1/K3 aanvullen op een al-werkend fundament".

| §4-stap | Bouwsteen | Staat in v3-2 | Resterend werk |
|---|---|---|---|
| 1 | **B7** import-pijplijn A→B | ❌ afwezig | **Volledig bouwen** — kritieke pad. `import-from-ontology-v4_6_3.py` → idempotente, non-destructieve SQL-bundle. Vervangt hand-seed. |
| 2 | **B1** SQL.js + schema | ✅ af | K1: `iri`-veld toevoegen aan concept-tabellen (nu alleen `owl_klasse`-prefix op frameworks/rollen). |
| 3 | **B2** Chart.js | ✅ af (6 charts) | Evt. uitbreiden bij nieuwe import-data. |
| 4 | **B3** append-only audit-trail | 🟡 half | INSERT-only-**trigger** + **hash-chain** (`hash_prev_row`) + CSV-back-up-knop toevoegen. |
| 5 | **B4** RACI | ✅ af | Rollen uit B7-import i.p.v. hand-seed. |
| 6 | **B5** kalender | ✅ af (native + iCal) | — |
| 7 | **B6** form-validatie | 🟡 basaal (`required`) | HTML5-native + ~50 regels JS verstevigen. |
| 8 | **B8** NLDS-tokens | ❌ afwezig (eigen dark-theme) | CSS-variabelen (kleur/typografie/spacing) toevoegen voor Rijksoverheid-look. |
| 9 | **B9** WCAG 2.1 AA | ⚠️ risico | axe-core-audit; dark-theme-contrast + 10px-mono-fonts zijn waarschijnlijke AA-knelpunten. Vanaf dag 1. |
| 10 | **B11** export-discipline | ✅ rijk (DB/CSV/TTL/iCal) | Timestamped-folder-conventie + auditor-deliverable-template formaliseren. |
| 11 | **K3** versie-aanduiding | ❌ (toont "v3.0", niet ontologie-versie) | Geïmporteerde ontologie-versie als zichtbare metadata (komt uit B7). |
| 12 | `/dashboard-build`-skill | ❌ | Sluitstuk, ná stabiele cyclus. |

**Samengevat:** ~6 van de 11 bouwstenen zijn al substantieel aanwezig. Het echte werk concentreert zich op **B7 (import), B3-hardening, B8 (NLDS), B9 (WCAG), K1 + K3 (IRI + versie)** — plus het vendoren van libs (Q-M5) vóór een demo.

---

## 5. Invariant-check

| Invariant | Bevinding |
|---|---|
| **Geen organisatienaam** | ✅ Overal "Rijksoverheidsorganisatie" / "Nederlandse Overheidsorganisatie". Geen echte naam. |
| **Geen persoonsdata** | ✅ `rollen`-schema heeft `bezet_door_naam`/`bezet_door_email`, maar de seed laat die **leeg** (`''`). Geen namen/e-mails in de repo. Aandachtspunt: B7/CRUD mag deze velden nooit met echte personen committen (lokaal-only). |
| **Framework-neutraal (D9)** | ✅ 15 frameworks gelijkwaardig geseed; BIO 2.0 als view-perspectief (`selFW`), geen architecturale hub. Consistent met Q-M3 (geen graaf). |
| **NEN-discipline** | ✅ Control-titels zijn korte parafrases ("Beleidsregels voor IB", "Dreigingsanalyse"), geen verbatim ISO-tekst. Bij B7-import op dit punt blijven letten. |
| **Geen graaf in Spoor B (Q-M3)** | ✅ Geen Cytoscape; ontologie-koppeling is read-only SPARQL-lens + (potentieel) deep-link. |

---

## 6. Scope-pauze — §3-conditie + Optie A/B/C

**§3-trigger formeel geraakt:** v3-2 bevat **substantieel méér** dan de CLAUDE.md-spec (SoA, heatmap, KRI, governance-view, 6 charts, TTL/CSV/iCal-export, localStorage-persistentie — bovenop CRUD/audit/RACI/kalender). Daarom leg ik conform §3 expliciet Optie A/B/C voor. De §4-default is voortbouwen (Q-M1, zacht).

### Optie A — Voortbouwen op v3-2 (aanbevolen) ✅
Behoud v3-2 als basis. Voer §4 uit met de herijkte focus uit §4-tabel: **B7 eerst** (import vervangt hand-seed), dan B3-hardening, B8, B9, K1, K3, en als sluitstuk `/dashboard-build`.
- **Voor:** respecteert Q-M1 ("gooi werkend werk niet weg"); ~6 bouwstenen al af; snelste pad naar demo-waarde.
- **Tegen:** v3-2 is één bestand van 1.735 regels; B7/B8/B9 inpassen vraagt zorgvuldige chirurgische edits in bestaande code.
- **Dashboard-aanbeveling:** ✅ **Voorkeur.** De prototype is rijk en invariant-veilig; herstart zou aantoonbaar werk weggooien.

### Optie B — Voortbouwen mét lichte herstructurering
Als Optie A, maar splits het 1.735-regel-bestand eerst in `index.html` + `app.js` + `schema.sql` + `vendor/` vóór de bouwstenen, voor onderhoudbaarheid.
- **Voor:** maakt B7/B8/B9-werk en de `/dashboard-build`-skill schoner; vendoren (Q-M5) wordt natuurlijk.
- **Tegen:** herstructurering is werk zonder directe demo-waarde; raakt de "surgical changes"-discipline; één-bestand heeft ook voordelen (lokaal openen zonder server).
- **Dashboard-aanbeveling:** overweegbaar als tussenstap vóór B7, mits masterchat de extra effort accordeert. Niet mijn eerste voorkeur — eerst waarde (B7), splitsen kan later.

### Optie C — Green-field herstart
v3-2 als referentie, nieuw bouwen vanaf B1.
- **Voor:** schoon vertrekpunt met B8/B9/K1 vanaf dag 1 ingebakken.
- **Tegen:** gooit een rijk, invariant-veilig, grotendeels werkend prototype weg; strijdig met Q-M1; trager naar demo.
- **Dashboard-aanbeveling:** ❌ **Niet doen** — de "substantieel méér"-bevinding pleit júist tegen herstart.

**Mijn aanbeveling: Optie A.** Het "substantieel méér" is een meevaller, geen probleem — het bevestigt voortbouwen i.p.v. herstart. Als de masterchat onderhoudbaarheid zwaar weegt, is Optie B een verdedigbare variant, met B7 nog steeds als eerste inhoudelijke stap.

---

## 7. Openstaande punten voor akkoord

1. **Optie A / B / C** — akkoord op voortbouwen (en zo ja, A of B)?
2. **Q-D6** — mag ik zelf renderen (headless/`python -m http.server`) voor smoke-tests, of loopt verificatie via de projecteigenaar? Bepaalt of ik B9/WCAG zelf kan valideren.
3. **Archiveren artefacten** — de vijf oudere `grc-dashboard*.html` naar `dashboard/archief/` verplaatsen, of in `dashboard/` laten? (Aparte beslissing, geen STAP 0-actie.)

## 8. Niet-gedaan (bewust)

- ❌ Geen bouwsteen-volgorde §4 gestart (wacht op akkoord).
- ❌ Geen browser-render / smoke-test (Q-D6 open).
- ❌ Geen bestand verplaatst/verwijderd/gewijzigd.
- ❌ Geen commit.
