# Protocol 18 — concept (pre-sprint-dashboard-update-checklist)

**Van:** masterchat
**Datum:** 29 mei 2026
**Status:** CONCEPT — vereist surgische merge in `docs/sprint-protocols.md` door Brein/Tech (geen full-file-rewrite via MCP).
**Aanleiding:** dashboard-landschap-analyse Bouwsteen E; masterchat-GO 29-05 voor toevoeging aan de canonieke protocollen.

---

## Protocol 18 — Pre-sprint-dashboard-update-discipline

Analoog aan Protocol 1 (pre-sprint-inventarisatie voor Tech), maar voor de Dashboard-subagent. Vóór elke build-script-aanraking bij een nieuwe ontologie-baseline doorloopt de Dashboard-subagent deze checklist en levert de uitkomst (ja/nee + impact) in het patchnotitie-rapport:

1. Welke modules zijn gewijzigd in deze release? (uit patch-rapport "Gewijzigde modules")
2. Zijn er nieuwe namespaces? (raakt namespace-binding + class-mapping)
3. Zijn er nieuwe properties met SKOS-impact? (raakt edge-export)
4. Is er een nieuwe Laag? (raakt LAAG-config)
5. Is er een nieuw framework-individual? (raakt framework-config)
6. Build-script-versie-bump nodig of niet?
7. SKOS-tellingen: noem expliciet de meet-laag (ontologie 1.798 vs. dashboard-export 1.759) zodat de 39-edge-discrepantie niet elke release opnieuw als "bug" opduikt (zie `brain__concepts__skos-export-filter`).

**Discipline:** vier-tot-zeven vragen volstaan — niet bureaucratiseren. Output is een impact-tabel met expliciete scope-annotatie (Protocol v1.3 §10.5).

---

**Merge-aanwijzing voor Brein:** voeg dit toe als Protocol 18 in `docs/sprint-protocols.md`, werk het protocol-totaal bij (17 → 18) in de relevante koppen, en registreer in de brain-vault (sprints/workflow). De canonieke 1-17 blijven ongewijzigd.
