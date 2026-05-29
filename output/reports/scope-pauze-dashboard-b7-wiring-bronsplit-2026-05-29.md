# Scope-pauze — B7-wiring: structuur- vs. operationele-bron-split

- **Subagent:** Dashboard (Claude Code)
- **Datum:** 2026-05-29
- **Sprint:** Spoor B revival — B7-wiring (import-knop + dedup-renderlogica) na GO op Optie 1
- **Status:** ⏸️ GEPAUZEERD vóór de pervasieve render-edits (conform staande regel).
- **Niet gecommit.** Veilige `.js`-wrapper-uitbreiding is gedaan (geen v3-2-risico); v3-2 zelf onaangeraakt.

---

## De verrassing

Tijdens het uitlezen van de render-data-flow blijkt: **geïmporteerde controls dragen géén operationele status.** `implementatiestatus`, `eigenaar_rol`, `eigenaar_naam` zijn leeg — dat is **Patroon C by design** (operationele velden blijven in Spoor B, door de organisatie in te vullen; de ontologie levert alleen structuur).

De bestaande **hand-seed-controls hébben** die status (Volledig/Gedeeltelijk/In uitvoering) — dat is de demo-rijkdom die de CSO/CISO ziet.

**Gevolg:** als ik de dedup-nuance ("structuurweergaven default `herkomst='ontologie'`") blind op álle controls-queries toepas, dan rekenen "Compliance-score" en "implementatiestatus-totaal" over 316 status-loze ontologie-rijen → **~0%**, en oogt de demo leeg/kapot. Je eigen rollen-redenering ("hand-seed blijft de rijke primaire weergave") wijst exact dezelfde kant op voor operationele velden.

→ Dit is geen tegenslag maar een verfijning: "ontologie canoniek voor structuur" en "hand-seed rijk voor operationeel" zijn twee verschillende lagen, en ik moet weten **welke weergave welke bron** krijgt vóór ik ~15 verspreide queries aanpas. v3-2 heeft geen centraal query-choke-point, dus dit raakt veel plekken — daarom eerst je akkoord op de mapping.

## Bevestiging van de bron-realiteit (read-only)

| Laag | Ontologie-import | Hand-seed |
|---|---|---|
| Structuur (id, IRI, titel, framework, owl_klasse) | ✅ 316 controls, 52 fw, 20 rollen — autoritatief, traceerbaar | beperkt (23 controls demo-sample) |
| Operationeel (implementatiestatus, eigenaar, voortgang) | ❌ leeg (Patroon C) | ✅ rijk (de demo-status) |
| Rollen-detail (functienaam, grondslag, stelsel, RACI) | ❌ dun (rauwe ids) | ✅ rijk (CISO/BVA + grondslag) |

## Opties

### Optie 1A — Per-laag bron-split (aanbevolen ✅, blijft binnen Optie 1)
Ontologie canoniek voor **structuur/telling/traceerbaarheid**; hand-seed primair voor **operationele status + rollen**. Concrete mapping:

| Weergave | Default-bron | Reden |
|---|---|---|
| Controls-lijst, "controls per framework", totaal-controls, framework-paneel, IRI-kolom | **ontologie** (316, met IRI) | structuur autoritatief + traceerbaar |
| Compliance-score %, implementatiestatus-chart, SoA-status | **hand-seed** | operationele status; ontologie-rijen leeg |
| Rollen, RACI | **hand-seed** | ontologie-rollen dun |
| Risico's, findings, kalender, documenten | hand-seed (n.v.t. import) | niet uit ontologie |

Plus een filter-toggle ("bron: ontologie / handmatig / alle") om de andere laag zichtbaar te maken (jouw "filter houdt 'm zichtbaar"). Imported rows krijgen de IRI-kolom (K1) zichtbaar als traceerbaarheids-anker.
- **Voor:** demo blijft rijk én krijgt de ontologie-structuur + IRI-traceerbaarheid; non-destructief; trouw aan Optie 1 + je rollen-nuance.
- **Tegen:** raakt ~15 queries (mechanisch maar veel); de Controls-lijst (316, status-loos) en SoA (23, met status) tonen verschillende aantallen — moet duidelijk gelabeld ("structuur" vs "operationele SoA").

### Optie 1B — Hand-seed operationeel primair + ontologie als structuur-referentiepaneel
Operationele weergaven blijven volledig hand-seed (ongemoeid). De import voegt (a) IRI-verrijking waar concepten matchen en (b) één read-only paneel "Ontologie-structuur (316 controls, traceerbaar)" toe.
- **Voor:** nul risico op de werkende operationele demo; veel minder query-edits; toch volledige structuur + traceerbaarheid zichtbaar.
- **Tegen:** leunt richting de eerder afgewezen Optie 3 (apart paneel) — maar de status-leeg-bevinding is nieuwe informatie die dat mogelijk rechtvaardigt.

### Optie 1C — Organisatie vult operationele velden op imported rows
Import als enige structuurbron; operationele status wordt handmatig (of via migratie van hand-seed-status naar matchende IRI's) op de 316 rijen gezet.
- **Tegen:** groot, vraagt concept-matching hand-seed↔ontologie (de hand-seed-ids matchen niet 1-op-1 op IRI's); buiten B7-scope; niet nu.

## Mijn aanbeveling

**Optie 1A** — het blijft binnen jouw Optie-1-besluit en je dedup-nuance, en de per-laag-split lost het status-leeg-probleem op zonder de demo te verarmen. Als je het risico van ~15 query-edits op de werkende demo liever vermijdt vóór een CSO-moment, is **Optie 1B** de veiligere variant met bijna dezelfde demo-waarde.

Geef je de bron-mapping akkoord (1A of 1B)? Daarna bouw ik de migratie + import-knop + de gekozen renderlogica + K3-header af en smoke-test headless.

## Niet-gedaan (bewust)
- ❌ v3-2 nog niet gewijzigd (wacht op bron-split-keuze — geen stilzwijgende demo-impact).
- ✅ wel: `.js`-wrapper toegevoegd aan `import-from-ontology.py` (veilig, geen v3-2-risico).
- ❌ Geen commit.
