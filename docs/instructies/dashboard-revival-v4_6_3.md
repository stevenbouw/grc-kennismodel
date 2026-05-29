# Instructie Dashboard-subagent — Spoor B revival naar baseline v4.6.3

**Van:** masterchat
**Datum:** 29 mei 2026
**Doel-subagent:** Dashboard (Claude Code)
**Aanleiding:** dashboard-landschap-analyse `output/reports/dashboard-landschap-2026-05-28.md` + masterchat-besluiten 29-05 (zie `besluitnotitie-qm-dashboard-2026-05-29.md`)

---

## 0. Context en doel

Spoor B (`grc-dashboard`, operationele werkmap) staat sinds v3.x stil. Dit is nu prioriteit: het is de demonstratie-laag voor de opdrachtgever (CSO/CISO) — het laat zien wat het model kan, hoe het eruitziet en wat de toegevoegde waarde is. De explorer (Spoor A) is bewust secundair in deze sprint.

Lees vóór alles: `output/reports/dashboard-landschap-2026-05-28.md` (volledig), `CLAUDE.md`, `.claude/agents/dashboard.md`, `brain/brain__concepts__dashboard-productlijnen.md`. De bouwsteen-IDs (B1..B11, K1/K3) en O1..O6 hieronder verwijzen naar dat rapport.

## 1. Harde invarianten (niet onderhandelbaar)

- **Geen organisatienaam** — altijd "de organisatie" / "Rijksoverheidsorganisatie".
- **Framework-neutraal (D9)** — BIO 2.0 mag als dashboard-view-perspectief; geen framework als architecturale hub.
- **NEN-discipline** — geen verbatim ISO-tekst >10 woorden in dashboard-output; parafrase + clausule-verwijzing.
- **Geen autonome commit** — lever op, de projecteigenaar inspecteert `git status`/`git diff` en commit handmatig.
- **Twee-producten-discipline** — Spoor B blijft een apart product van de explorer; niet vermengen in één UI (productlijnen-concept).

## 2. Masterchat-besluiten (Q-M) die deze sprint kaderen

- **Q-M1 (tech-stack): ZACHT, voortbouwend.** Bouw voort op de bestaande v3.x SQL.js + Chart.js-basis — gooi werkend werk niet weg. Voeg NL Design System-tokens toe voor de Rijksoverheid-look. GEEN PWA/Electron-herbouw nu (productie-fase-vraag).
- **Q-M2 (locatie): repo is akkoord.** v3-2 is org-data-vrij; mag in de repo blijven. (27-mei "lokaal blijft"-besluit herzien.)
- **Q-M3 (Cytoscape in Spoor B): NEE.** Spoor B = operationele werkmap (status/CRUD/charts/RACI/kalender), geen graaf. De graaf blijft in de explorer; koppeling via deep-link.
- **Q-M4 (H40): latent, parked.** Demo-waarde komt uit het dashboard, niet uit explorer-renderdekking.
- **Q-M5 (lokaal-draaibaar): soepel in ontwikkeling, strict vóór demo.** CDN mag tijdens bouw; **vendor alle libs lokaal in `dashboard/vendor/` vóór elke opdrachtgever-demo** — een Rijksoverheid-machine kan CDN's blokkeren.
- **Q-M6 (Spoor A-effort): minimaal.** Alleen goedkope geen-spijt-items als ze meeliften.

## 3. STAP 0 — v3-2-inspectie (verplicht, vóór bouw)

Dit beantwoordt Q-D5. Inspecteer `dashboard/grc-dashboard-v3-2.html` (+ de aangrenzende `-2/-3/-v2/-v3/base`-varianten) en rapporteer:

- Wat werkt, wat is stub, wat is geparkeerd (CRUD / audit-trail / RACI / kalender / charts / data-laag).
- Welke ontologie-versie de huidige data representeert.
- Welke van de `grc-dashboard-*.html`-bestanden actief werkbestand is vs. historisch artefact (Q-D7).

**Scope-pauze-conditie:** als v3-2 substantieel méér of minder blijkt te bevatten dan de CLAUDE.md-spec, of als herstart voordeliger lijkt dan voortbouwen — STOP, lever een Optie A/B/C-rapport aan de masterchat (via de projecteigenaar), bouw niet door. De default is voortbouwen (Q-M1).

## 4. Bouwsteen-volgorde (na akkoord op STAP 0)

Kritiek pad eerst; zonder import-pijplijn is er geen werkende koppeling met de ontologie.

1. **B7 — import-pijplijn A→B** (kritiek pad). `import-from-ontology-v4_6_3.py` extraheert structuur (frameworks, controls, IRIs, labels, M04-RACI-rollen) uit de ontologie-export en levert een **idempotente, non-destructieve** SQL-INSERT-bundle. Verwijderde IRIs → orphan-markeren, nooit hard-deleten. Patroon C uit O2.
2. **B1 — SQL.js + schema** (voortbouwend op v3.x). Tabellen: `frameworks`, `controls`, `risicos`, `eigenaren`, `deadlines`, `voortgang`, `kalender_events`, `racis`, `audit_trail`, `schema_version`. **K1: elk concept-record draagt een `iri`-veld vanaf dag 1.**
3. **B2 — Chart.js** visualisaties (status-per-control, deadlines-per-maand, voortgang-trend).
4. **B3 — append-only audit-trail** (Rijksoverheid-essentie). INSERT-only-trigger; row-format met `hash_prev_row` (lichte hash-chain); CSV-export-knop voor handmatige back-up. Geen UPDATE/DELETE op audit-rijen.
5. **B4 — RACI-component** (uit M04 + lokale persoonsalias-tabel).
6. **B5 — kalender** (FullCalendar, MIT, lokaal te vendoren — of native `<table>`-grid bij stack-twijfel).
7. **B6 — form-validatie**, dunste optie: HTML5-native + ~50 regels JS; Just-Validate alleen bij complexere forms.
8. **B8 — NL Design System-tokens** (CSS-variabelen: kleur-palet, typografie, spacing) voor Rijksoverheid-look. Web Components optioneel; tokens minimaal.
9. **B9 — WCAG 2.1 AA** vanaf dag 1, niet later. axe-core (MIT) als linter; toetsenbord-navigatie + tabel-toegankelijkheid.
10. **B11 — export-discipline** (`.db`-dump + per-tabel CSV + JSON-snapshot, timestamped). Auditor-deliverable-template.
11. **K3 — versie-aanduiding** prominent zichtbaar (geïmporteerde ontologie-versie als metadata).
12. **Afsluitend: `/dashboard-build`-skill** bouwen op de dán-stabiele cyclus (skill-creator). §0.5-firewall in de skill-tekst opnemen (leerpunt §11.15). Dit is de laatste stap, niet de eerste.

## 5. Demo-deliverable-skills (preload in dashboard.md)

Voeg toe aan het `skills:`-veld van `.claude/agents/dashboard.md`: `frontend-design`, `pptx`, `pdf`, `docx`, `xlsx`. Deze leveren de opdrachtgever-deliverables (presentatie-deck, status-rapport, audit-export). Dragen alleen guidance, geen content — invariant-veilig.

## 6. Wat NIET

- Geen Cytoscape/graaf in Spoor B (Q-M3).
- Geen bidirectional sync naar de ontologie (P4 — organisatie-data-extern-risico).
- Geen iframe/micro-frontend-vermenging met de explorer (P5 — twee-producten-discipline).
- Geen server-laag / multi-user / auth (productie-fase, niet prototype).
- Geen explorer-modernisering (Q-M6: minimaal).
- Geen ontologie-wijzigingen (buiten Dashboard-rol).

## 7. Deliverables

- STAP 0-inspectierapport (`output/reports/`).
- Werkend dashboard op baseline v4.6.3 met kritiek pad B7+B1+B2+B3 + operationele uitbouw B4/B5/B6 + kwaliteit B8/B9 + B11.
- `/dashboard-build`-skill als sluitstuk.
- Patchnotitie-rapport conform dashboard-subagent-conventies; metrics-tabel met expliciete scope-annotatie.

Bij elke onverwachte structurele verrassing: scope-pauze + Optie A/B/C naar masterchat. Niet zelfstandig beslissen, niet zelfstandig committen.
