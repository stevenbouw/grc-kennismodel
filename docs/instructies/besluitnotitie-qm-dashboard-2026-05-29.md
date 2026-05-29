# Besluitnotitie — architectuurvragen dashboard-landschap (Q-M)

**Van:** masterchat
**Datum:** 29 mei 2026
**Status:** vastgesteld — input voor eerstvolgende Brein-cyclus
**Bron:** `output/reports/dashboard-landschap-2026-05-28.md` (Analyse-deliverable, 13 open vragen)

---

## Vastgestelde Q-M-besluiten

| Vraag | Besluit | Grond |
|---|---|---|
| Q-M1 tech-stack hard/zacht | **Zacht, voortbouwend.** Voortbouwen op v3.x SQL.js + Chart.js; NLDS-tokens toevoegen; geen PWA/Electron-herbouw nu. | Projecteigenaar-bevestiging; v3.x werkt, niet weggooien |
| Q-M2 locatie v3-2 | **Repo akkoord.** v3-2 is org-data-vrij; mag in repo blijven. 27-mei "lokaal blijft"-besluit hiermee herzien. | Projecteigenaar-bevestiging |
| Q-M3 Cytoscape in Spoor B | **Nee.** Spoor B = operationele werkmap, geen graaf. Graaf blijft in explorer; koppeling via deep-link. | Masterchat-call; productlijnen-discipline |
| Q-M4 H40-trigger | **Latent, parked.** Demo-waarde uit dashboard, niet uit explorer-renderdekking. | Masterchat-call |
| Q-M5 lokaal-draaibaar prototype | **Soepel in dev (CDN mag), strict vóór demo (lokaal vendoren in `dashboard/vendor/`).** | Projecteigenaar-bevestiging; Rijksoverheid-machine kan CDN blokkeren |
| Q-M6 Spoor A-effort | **Minimaal.** Alleen goedkope geen-spijt-items die meeliften. | Volgt prioriteit dashboard boven explorer |

De zeven Q-D-vragen worden niet als aparte ronde gedraaid; ze zijn ingevouwen als STAP 0 van de Dashboard-instructie (v3-2-inspectie beantwoordt Q-D5/Q-D7; build-frictie + render-conventies komen uit het inspectierapport).

## Gerelateerde besluiten 29-05

- **Protocol 18** toegevoegd (concept in `protocol-18-concept.md`; Brein merget surgisch in `sprint-protocols.md`).
- **`/dashboard-build`-skill** verschoven naar sluitstuk van de dashboard-sprint (niet vooraf, niet via Tech) — codificeert pas een stabiele cyclus.
- **Tooling-04 overig** (`/pilot-rapport`, `/brein-cyclus`, 5e hook, cat-5 NEN-hook) blijft YAGNI-geparkeerd tot een T-sprint/Brein-cyclus het triggert.
- **D.7 GRC-domein-skill** gestart als parallelle Tech-track (`tech-d7-grc-domein-skill.md`).
- **Demo-export-skills** (frontend-design/pptx/pdf/docx/xlsx) preloaden in `dashboard.md`.

## Kandidaat-H-items uit het rapport (ter registratie, niet geactiveerd)

- H42 — SKOS-distributie-visualisatie in explorer (parked, koppelen aan H40).
- H43 — versie-templating-discipline explorer-HTML (Bouwsteen A).
- H44 — Spoor-A↔B-koppel-architectuur (P1+P3+K1..K4), formeel bij Spoor-B-operationeel.
