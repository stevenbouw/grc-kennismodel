# Tussenrapport — B7 import-pijplijn A→B (Spoor B revival)

- **Subagent:** Dashboard (Claude Code)
- **Datum:** 2026-05-29
- **Sprint:** Spoor B revival, §4 stap 1 (B7) — na masterchat-GO op Optie A
- **Status:** ✅ pijplijn-kern gebouwd + geverifieerd · ⏸️ UI-wiring wacht op één productbeslissing
- **Niet gecommit** — projecteigenaar inspecteert `git diff` en commit handmatig.

---

## 1. Wat is gebouwd

| Deliverable | Pad | Wat |
|---|---|---|
| Import-pijplijn | `dashboard/import-from-ontology.py` | Python, dry-run-default + `--apply` + `--self-test`. Volgt de canonical applier-discipline (dry-run, idempotentie, provenance-hash, per-tabel-logging). |
| SQL-bundle | `dashboard/structure-import-v4_6_0.sql` | 477 regels, idempotent + non-destructief. Artefact dat de v3-2-importfunctie uitvoert. |

Conform de drie masterchat-labeling-eisen (Optie A):
1. **Scriptnaam volgt de bron** — `import-from-ontology.py` (versie-geparametriseerd); bundle heet `structure-import-v4_6_0.sql` naar de bron, niet `v4_6_3`.
2. **K3-metadata toont de nuance letterlijk** — `ontologie-structuur v4.6.0 · SKOS-status t/m v4.6.3` (opgeslagen in tabel `ontologie_import_meta`).
3. **Provenance-anker** — `meta.source_files_hash` (`3b8d07fc…`) wordt meegeschreven.

## 2. Wat de import extraheert (uit `grc-data-v4_6_0.json`)

| Type | Aantal | Bron-filter | In Spoor B |
|---|---|---|---|
| Frameworks | **52** | ns `fw`, exclusief 8 `FrameworkDomain`-helpernodes | tabel `frameworks` |
| Controls | **316** | OWL-types BIOControl (93) · ISO27002Control (93) · NISTControl (104) · CBWControl (26) | tabel `controls` |
| Rollen | **20** | ns `roles`, alleen echte rol-types (excl. 19 `GRCActivity`/`RACIType`) | tabel `rollen` |

Elk record draagt: `id` (prefixed), **`iri`** (volle URI → K1), label→`naam`/`titel`/`functienaam`, `owl_klasse` (OWL-type), `beschrijving` (controls, NL), plus `herkomst='ontologie'` / `bron_versie='4.6.0'` / `orphan`.

Control→framework-koppeling is **deterministisch op OWL-type** (geen brosse IRI-regex — vermijdt knelpunt K1-Spoor-A): BIOControl→`BIO-2.0`, ISO27002Control→`ISO-27002-2022`, NISTControl→`NIST-800-53-R5`, CBWControl→`CBW` — dezelfde framework-ids als de bestaande v3-2-seed, zodat "controls per framework" blijft kloppen. (De 93 BIO-controls matchen exact de "93 controls" die v3-2 al toonde.)

## 3. Idempotentie + non-destructiviteit — geverifieerd

`--self-test` en een end-to-end-run tegen het **échte v3-2-schema** bewijzen:

- **Idempotent:** bundle 2× uitvoeren → identieke eindstaat (53 fw / 316 controls / 20 rollen). Patroon: `INSERT … ON CONFLICT(id) DO UPDATE`.
- **Non-destructief:** een uit de bron verdwenen IRI wordt `orphan=1` gemarkeerd, **nooit hard-gedeletet** (getest met een gesimuleerde verwijderde control).
- **Handmatige data ongemoeid:** rijen met `herkomst='handmatig'` (de bestaande demo-seed) worden niet aangeraakt; alleen `herkomst='ontologie'`-rijen worden gesynct.
- **Schema-migratie PRAGMA-geguard:** `iri`/`herkomst`/`bron_versie`/`orphan`/`owl_klasse` worden alleen toegevoegd waar ze ontbreken (de echte `controls`-tabel mist `owl_klasse` — de self-test ving dat).

## 4. Bevinding: rollen in de ontologie zijn dun

De ontologie-rollen dragen **rauwe IRI-labels** (`roles:R_ITBeheerder`, label = local-id, geen NL-naam, geen `grondslag`/`stelsel`/`rapporteert_aan`). De bestaande v3-2-hand-seed (CISO/BVA/CISO met wettelijke grondslag, RACI-koppeling) is voor rollen **juist rijker**. Voor frameworks en controls is de ontologie-import daarentegen autoritatief en rijker.

→ Implicatie: voor rollen ligt **co-existentie** (hand-seed behouden, ontologie als referentie) meer voor de hand dan vervanging.

## 5. Eén beslissing vóór de UI-wiring (B7 sluitstuk)

De pijplijn is af en getest; resteert het inbouwen van een **"Importeer ontologie-structuur"-knop** in `grc-dashboard-v3-2.html` die de bundle uitvoert. Daarvoor één productkeuze die ik niet stilzwijgend maak — het bepaalt wat de opdrachtgever (CSO/CISO) ná import ziet:

**Hoe verhoudt de geïmporteerde structuur zich tot de bestaande demo-seed?**

- **Optie 1 — Co-existentie + tagging (aanbevolen ✅).** Import voegt `herkomst='ontologie'`-rijen toe naast de hand-seed; de UI-structuurweergaven (frameworks/controls/SoA) defaulten naar `herkomst='ontologie'` (autoritatief), met een filter om hand-seed/orphan te tonen. Non-destructief, reversibel, en voor rollen behoudt het de rijkere hand-seed. *Tegen:* tijdelijk dubbele concepten in de DB (wel gescheiden via `herkomst`).
- **Optie 2 — Import vervangt de structuur-seed.** De `laadSeedData()`-structuurrijen (frameworks/controls) vervallen ten gunste van de import. *Tegen:* raakt werkende seed-code (surgical-changes-discipline → masterchat-akkoord nodig); rollen-seed is rijker dus die zou je toch moeten behouden → inconsistent.
- **Optie 3 — Aparte "ontologie-referentie"-weergave.** Import laadt in read-only referentietabellen los van de operationele tabellen. *Tegen:* meer schema + UI-werk; minder integratie-waarde.

**Mijn aanbeveling: Optie 1** — sluit aan op Patroon C (ontologie = structuur-autoriteit, Spoor B = operationeel), is non-destructief en demo-veilig, en respecteert de rijkere hand-seed voor rollen.

## 6. Daarna (binnen B7-afronding)
- v3-2: PRAGMA-geguarde kolom-migratie + import-knop + `renderXxx`-refresh + K3-versielabel in de header (toont nu "v3.0 Database" — moet ook de geïmporteerde ontologie-structuur-versie tonen).
- Smoke-test in browser (raakt Q-D6 — mag ik zelf renderen?).

## 7. Niet-gedaan (bewust)
- ❌ v3-2 nog niet gewijzigd (wacht op §5-keuze — geen stilzwijgende product-/seed-beslissing).
- ❌ Geen browser-smoke-test (Q-D6 open).
- ❌ Geen commit.
