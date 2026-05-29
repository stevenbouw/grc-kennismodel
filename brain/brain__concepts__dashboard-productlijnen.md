---
type: concept
title: Dashboard-productlijnen — Spoor A explorer vs Spoor B dashboard
status: living
date: 2026-05-29
related:
  - namedindividual-telmethode
  - skos-export-filter
  - H40_dashboard-ui-renderdekking
  - spoor-b-revival
sources:
  - sessie-rapport-v2_0
  - handover-dashboard-chat-v1
  - besluitnotitie-qm-dashboard-2026-05-29
chat-sources: []
confidence: high
---

# Dashboard-productlijnen — Spoor A explorer vs Spoor B dashboard

## Wat het is

Sinds v4.6.0 bestaan er **twee parallelle dashboard-productlijnen** in het project met **fundamenteel verschillende doelen, datamodel en engine**. Beide zijn legitiem; ze hebben elk hun eigen rol. Verwarring is begrijpelijk omdat beide "dashboard" heten in informele communicatie — vandaar deze expliciete documentatie.

## Twee productlijnen, één tabel

| Aspect | **`grc-explorer-*`** | **`grc-dashboard-*` (bv. v3-2)** |
|---|---|---|
| **Spoor** | A — read-only ontologie-graaf-verkenner | B — operationele werkmap (prototype) |
| **Naam-actueel** | `grc-explorer-v4_6_0.html` | `grc-dashboard-v3-2.html` (**mag in de repo** sinds Q-M2-reversal 29 mei 2026 — org-data-vrij) |
| **Doel** | Inspectie + navigatie van ontologie-graaf | CRUD, audit-trail, kalender, RACI |
| **Data-bron** | `grc-data-v4_6_0.js` (export uit ontologie) | Lokale SQL.js `.db`-bestand |
| **Engine** | Cytoscape.js | Chart.js + SQL.js |
| **Datamodel-bron** | Ontologie-individuals (gefilterde ABox) | Organisatie-specifieke tabellen (`risicos`, `controls`, `rollen`, `documenten`, `audit_bevindingen`, `kalender`, `audit_trail`) |
| **Velden** | `rdfs:label`, `rdf:type`, `owl:sameAs`, SKOS-mappings, etc. | `eigenaar_naam`, `bezet_door_email`, `deadline`, `voortgang`, etc. |
| **Versie-tracking** | Beweegt mee met ontologie-versie (`v4_6_0`-suffix) | Eigen versie-track (`v3-2`-suffix, los van ontologie) |
| **Status (29 mei 2026)** | Productief in repo (`dashboard/`-folder) | Prototype, **in repo** (Q-M2-reversal); B7-wiring + Q-M5 vendoring + B9 WCAG opgeleverd. Zie [[brain__concepts__spoor-b-revival]] |

## Discipline — niet vermengen

| Regel | Reden |
|---|---|
| **Niet vermengen in één UI** | Spoor A toont generieke ontologie-graaf; Spoor B toont organisatie-specifieke werkstaat. Eén UI zou conceptueel verwarrend zijn |
| **Spoor A wijzigt mee met ontologie-versie** | Build-pipeline genereert `grc-data-v[X_Y_Z].js` per release; explorer-HTML krijgt corresponderende versie-suffix |
| **Spoor B heeft eigen versie-track** | Organisatie-specifieke velden (eigenaar_naam, deadline, voortgang) komen niet uit de ontologie; SQL.js-data is autoriteit, ontologie geeft hooguit referentie-IRIs |
| **Spoor B-data is organisatie-eigendom** | Indien Spoor B ooit met echte organisatie-data wordt gevuld: GitHub.com (publiek) is dan niet meer geschikt — heroverwegen naar GitLab-on-prem (zie CLAUDE.md §"Spoor B-overweging") |

## Wat ze gemeen hebben (beperkt)

Beide producten kunnen ontologie-IRIs als referentie gebruiken voor cross-link:

- Een `risicos`-rij in Spoor B kan een `risk:R_*`-IRI als referentie-veld dragen, wijzend naar de ontologie-individual
- Een SKOS-mapping in Spoor A kan in principe naar een Spoor B-record verwijzen via een externe `ext:`-property

In de praktijk gebeurt dit cross-link-werk niet automatisch — het is een toekomstige integratie-vraag (geen actief H-item nu, want geen concrete trigger).

## Verwante meet-laag-discrepanties

Het onderscheid productlijn-A vs productlijn-B sluit aan bij twee andere meet-laag-onderscheidingen die in de brain-vault zijn gedocumenteerd:

| Onderscheid | Concept | Aard |
|---|---|---|
| Ontologie-laag (1.798 SKOS) vs dashboard-export-laag (1.759 SKOS) | [[brain__concepts__skos-export-filter]] | Filter-keten in `build_grc_explorer_v3.py` |
| Class-niveau-telling vs Individual-niveau-telling | [[brain__concepts__namedindividual-telmethode]] | Canonieke meet-conventie binnen ontologie |
| **Spoor A render-laag (<10% JSON-velden) vs Spoor B operationeel-datamodel** | [[brain__architecture__H40_dashboard-ui-renderdekking]] + dit concept | Productlijn-keuze + UI-scope |

Beide andere onderscheidingen blijven binnen de Spoor A-pijplijn (ontologie → export → render). Het Spoor A vs Spoor B-onderscheid is een **dimensie hoger** — het zijn twee **verschillende producten**, niet twee fasen in één pipeline.

## Locatie-besluit — Spoor B-prototype blijft lokaal

Op 27 mei 2026 is besloten dat `grc-dashboard-v3-2.html` **lokaal bij Steven blijft staan**, buiten de repo. De drie eerder besproken kandidaat-locaties (eigen GitHub-repo, `sources/spoor-b/`, `dashboard/spoor-b/`) zijn alle drie afgewezen ten gunste van status quo.

### Motivering

De verwarring die productlijn-scheiding moest oplossen kwam uit informeel naamgebruik ("dashboard" voor twee producten), niet uit fysieke locatie. Naam-discipline (`grc-explorer-*` vs `grc-dashboard-*`) plus dit concept-bestand plus de CLAUDE.md-sectie pakken die verwarring direct aan. Locatie-wijziging zou geen extra waarde toevoegen en wel overhead creëren.

| Argument | Waarom dit doorslag gaf |
|---|---|
| Werkt nu zonder problemen | Geen actieve klacht; geen team-collaboration-behoefte |
| Prototype, geen productie | Versie-tracking via lokale filesystem of lokale git-repo is voldoende voor één-persoon-werk |
| Risico op data-lekkage | Zelfs met `.gitignore` voor `.db`-bestanden kunnen testdata-screenshots, config-paths of accidentele commits in publieke GitHub-history terechtkomen |
| Toekomstige migratie sowieso nodig | Bij echte organisatie-data is GitHub-publiek hoe dan ook ongeschikt — dan migratie naar GitLab-on-prem of vergelijkbaar; nu in publiek GitHub zetten zou twee-keer-werk betekenen |
| Conceptuele zuiverheid | Verschillende locaties (lokaal vs repo) versterkt productlijn-scheiding sterker dan zusterfolders zou doen |

### Trigger-condities voor heroverweging

De keuze "lokaal blijven" is niet permanent. Bij één of meer van onderstaande condities moet de locatie opnieuw worden geëvalueerd:

| # | Trigger-conditie | Vermoedelijke richting |
|---|---|---|
| 1 | **Echte organisatie-data in v3-2** (niet meer dummy/test) | Migratie naar GitLab-on-prem of vergelijkbare interne hosting |
| 2 | **Team-collaboration ontstaat** (meerdere ontwikkelaars/auditors actief in Spoor B) | Repository-toegang nodig; opnieuw evalueren tussen eigen repo en interne hosting |
| 3 | **Productie-transitie** (Spoor B wordt operationeel-productie i.p.v. prototype) | Andere infrastructuur, versie-discipline, deployment-pipelines vereist; mogelijk eigen repo |
| 4 | **Geautomatiseerde cross-link** met Spoor A (Spoor B-records actief gekoppeld aan ontologie-IRIs via sync) | Mogelijk eigen repo met submodule of vergelijkbare nabijheid |

Geen van de vier triggers is op moment van schrijven (mei 2026) actief.

### Status

Locatie-vraag **gesloten** (27 mei). **Herzien 29 mei 2026 — zie Q-M2-reversal hieronder.**

## Q-M2-reversal — Spoor B-prototype mag in de repo (29 mei 2026)

Het 27-mei-besluit ("`grc-dashboard-v3-2.html` blijft lokaal, buiten de repo") is op 29 mei 2026 **herzien** via Q-M2 in de dashboard-landschap-besluitnotitie (`docs/instructies/besluitnotitie-qm-dashboard-2026-05-29.md`):

> **Q-M2 — locatie v3-2: Repo akkoord.** v3-2 is org-data-vrij; mag in repo blijven. Het 27-mei "lokaal blijft"-besluit is hiermee herzien. Grond: projecteigenaar-bevestiging.

Hiermee is de openstaande **"locatie Spoor B-prototype"-vraag** — open sinds iteratie 12, genoemd in iteraties 13/14/15 — **opgelost**. Het prototype draagt geen organisatie-data (alleen generieke roltitels/kaders + dummy hand-seed); de disclosure-scan op v3-2 bevestigde geen organisatienaam. De vier trigger-condities hierboven blijven relevant voor het moment dat er wél echte organisatie-data in zou komen — dán verschuift de hosting-vraag opnieuw (GitHub-publiek wordt ongeschikt, zie CLAUDE.md §"Spoor B-overweging"). De repo-aanwezigheid nu is dus org-data-conditioneel akkoord.

## Q-M-dashboard-architectuurbesluiten (29 mei 2026 — masterchat, vastgesteld)

De zes Q-M-vragen uit de dashboard-landschap-analyse zijn door masterchat vastgesteld (besluitnotitie 29 mei). Brein legt ze vast; interpreteert ze niet:

| Vraag | Besluit | Grond |
|---|---|---|
| **Q-M1** tech-stack hard/zacht | **Zacht, voortbouwend** — voortbouwen op v3.x SQL.js + Chart.js; NLDS-tokens toevoegen; geen PWA/Electron-herbouw nu | v3.x werkt, niet weggooien |
| **Q-M2** locatie v3-2 | **Repo akkoord** — org-data-vrij; 27-mei "lokaal"-besluit herzien | projecteigenaar |
| **Q-M3** Cytoscape in Spoor B | **Nee** — Spoor B = operationele werkmap, geen graaf; graaf blijft in explorer, koppeling via deep-link | productlijnen-discipline |
| **Q-M4** H40-trigger | **Latent, parked** — demo-waarde uit dashboard, niet uit explorer-renderdekking | masterchat-call |
| **Q-M5** lokaal-draaibaar prototype | **Soepel in dev (CDN mag), strict vóór demo (lokaal vendoren in `dashboard/vendor/`)** | Rijksoverheid-machine kan CDN blokkeren |
| **Q-M6** Spoor A-effort | **Minimaal** — alleen goedkope geen-spijt-items die meeliften | prioriteit dashboard boven explorer |

Q-M3 bevestigt de bestaande productlijnen-discipline ("niet vermengen in één UI") expliciet: geen Cytoscape/graaf in Spoor B. Q-M4 houdt [[brain__architecture__H40_dashboard-ui-renderdekking]] latent/parked. De zeven Q-D-vragen zijn niet als aparte ronde gedraaid; ze zijn ingevouwen als STAP 0 van de Dashboard-instructie.

## Hangt samen met

- [[brain__architecture__H40_dashboard-ui-renderdekking]] — H40 scope-afbakening: H40 betreft **alleen** Spoor A explorer-UI, niet Spoor B
- [[brain__concepts__skos-export-filter]] — verwante meet-laag-discrepantie binnen Spoor A
- [[brain__concepts__namedindividual-telmethode]] — verwante telmethode-discipline binnen ontologie
- `CLAUDE.md` §"Spoor B-overweging" — toekomstige hosting-vraag (GitHub vs GitLab-on-prem)
- `docs/handovers/handover-dashboard-chat-v1.md` — handover-rapport waarin productlijn-onderscheid is bevestigd

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-26 | living | Concept geboren uit iteratie 12 polish-mini-sprint. Aanleiding: sessie-rapport v2.0 §2.1 + §9.2 expliciet onderscheid productlijn-A vs productlijn-B. Locatie-vraag Spoor B-prototype expliciet open gelaten voor masterchat-beslissing. |
| 2026-05-27 | living | Locatie-vraag gesloten: Optie D — Spoor B-prototype blijft lokaal. Vier trigger-condities voor heroverweging vastgelegd. Drie eerder besproken kandidaat-locaties (A/B/C) afgewezen ten gunste van status quo. |
| 2026-05-29 | living | **Q-M2-reversal**: locatie-besluit herzien — v3-2 mag in de repo (org-data-vrij). Openstaande "locatie Spoor B-prototype"-vraag (sinds iteratie 12) opgelost. Zes Q-M-architectuurbesluiten vastgelegd (Q-M1..Q-M6). Naam-actueel- + status-rij bijgewerkt. Verwijzing naar nieuw concept [[brain__concepts__spoor-b-revival]] (B7 + Q-M5 + B9). |

— Einde dashboard-productlijnen.
