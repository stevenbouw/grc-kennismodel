# Scope-pauze — B7 import-pijplijn: bron-versie-waarheid

- **Subagent:** Dashboard (Claude Code)
- **Datum:** 2026-05-29
- **Sprint:** Spoor B revival — bouwsteen B7 (`import-from-ontology-v4_6_3.py`), §4 stap 1
- **Status:** ⏸️ GEPAUZEERD bij de eerste structurele verrassing in B7 (conform projecteigenaar-instructie "bij eerste structurele verrassing: pauzeer en escaleer, niet doorbouwen").
- **Niet gebouwd, niet gecommit.** Alleen read-only bron-inventarisatie uitgevoerd.

---

## De verrassing (in één zin)

B7 is gespecificeerd als `import-from-ontology-**v4_6_3**.py`, maar er bestaat **geen v4.6.3-bron** om uit te importeren — de enige dashboard-export is `grc-data-**v4_6_0**.json` en de ontologie-TTL draagt zélf `owl:versionInfo "4.6.0"`. De bron-van-waarheid voor de import moet dus gekozen worden, en die keuze raakt drie eerder vastgelegde punten (Q-M6, K3, K4) — dat is een masterchat-besluit, geen Dashboard-keuze.

---

## Bevindingen (read-only geverifieerd)

| # | Bevinding | Bewijs |
|---|---|---|
| 1 | **Geen v4.6.3-export bestaat** | `dashboard/` bevat alleen `grc-data-v4.3.0/.1` + `grc-data-v4_6_0.json` (26 mei). Geen `v4_6_1/2/3`. |
| 2 | **Ontologie-TTL zegt zelf "4.6.0"** | `grc-core.ttl` → `owl:versionInfo "4.6.0"`. De repo-baseline-label v4.6.3 staat in CLAUDE.md/patch-rapporten, niet in de TTL-versionInfo. |
| 3 | **v4.6.3 ≡ v4.6.0 voor B7-structuur** | `patch-rapport-v4_6_3.md`: v4.6.3 = 2 SKOS-predicate-substituties in `m14-avg-gdpr.ttl` (broadMatch→relatedMatch), **geen TBox-wijziging, geen nieuwe frameworks/controls/rollen**, triples ongewijzigd (20.950). T1+T2 (v4.6.1/2) idem SKOS-only. → de structuur die B7 importeert (frameworks/controls/M04-rollen) is identiek tussen v4.6.0 en v4.6.3. |
| 4 | **De v4.6.0-export is structureel compleet + bruikbaar** | `grc-data-v4_6_0.json`: 1.788 nodes met `uri` (volle IRI → K1-geschikt), `label`+`label_en` (bilinguaal), `type`/`types`, `namespace`. Aanwezig: **60 frameworks** (ns `fw`), honderden controls (`bio`/`ctrl`/`ext`-NIST), **39 M04-rollen** (ns `roles`). Meta draagt `ontology_version: "4.6.0"` + source-hash. |

**Kort:** de data om B7 mee te bouwen is er en is goed — alleen draagt ze het label v4.6.0, niet v4.6.3.

---

## Waarom dit een escalatie is en geen zelf-besluit

De bron-keuze raakt drie vastgelegde punten die ik niet eigenstandig mag herinterpreteren:

- **K3 (versie-aanduiding in Spoor B)** — Spoor B moet de geïmporteerde ontologie-versie tonen. Als ik v4.6.0-data importeer via een script dat "v4_6_3" heet, ontstaat een versie-onwaarheid in de UI tenzij expliciet gelabeld.
- **Q-M6 (Spoor A-effort = minimaal)** — een v4.6.3-export produceren betekent de explorer-build (Spoor A) draaien = de geparkeerde 3-sprint-inhaalslag aanraken. Dat botst met "Spoor A minimaal".
- **K4 (geen twee parallelle export-paden)** — direct uit `ontology/*.ttl` parsen dupliceert de logica van `build_grc_explorer_v3.py`; de landschap-analyse waarschuwt expliciet tegen twee parallelle export-paden.

---

## Opties (A / B / C)

### Optie A — Importeer uit de bestaande `grc-data-v4_6_0.json` (aanbevolen) ✅
B7 consumeert de aanwezige export. Versie-eerlijkheid: het script + de Spoor B-metadata labelen de bron als **"v4.6.0-export (≡ v4.6.3 voor frameworks/controls/rollen; v4.6.1–3 zijn SKOS-only)"**. Script-naam: `import-from-ontology.py` (versie-geparametriseerd) of `import-from-ontology-v4_6_0.py` — i.p.v. een v4_6_3-naam die niet matcht met de bron.
- **Voor:** werkt nu; structuur bewezen identiek aan v4.6.3 (bevinding 3); respecteert Q-M6 (geen Spoor A-rebuild); vermijdt K4-dubbelpad; hergebruikt de al-gevalideerde build-pipeline-output.
- **Tegen:** de naam-mismatch met de instructie (`v4_6_3`) vraagt een bewuste her-labeling; K3 moet de v4.6.0/v4.6.3-nuance correct tonen.
- **Aanbeveling:** ✅ **Voorkeur** — eerlijk gelabeld is dit het snelste, invariant- en besluit-conforme pad.

### Optie B — Bouw eerst een v4.6.3-export, importeer daarna
Draai `build_grc_explorer_v3.py` (of een `--structure`-variant per K4) om `grc-data-v4_6_3.json` te genereren; B7 consumeert die.
- **Voor:** versie-label klopt exact; lift mee op de dashboard-inhaalslag (explorer v4.6.0→v4.6.3).
- **Tegen:** raakt **Spoor A** (Q-M6 "minimaal") en de geparkeerde 3-sprint-inhaalslag; scope-uitbreiding bovenop B7; vraagt ook de zes HTML-versie-strings-aanpassing (K1-Spoor-A). Groter dan B7.
- **Aanbeveling:** alleen als de masterchat de Spoor A-inhaalslag nú wil koppelen aan B7.

### Optie C — Parse `ontology/*.ttl` direct met rdflib
B7 leest de TTL-modules zelf (m01-framework, m02-control, m04-roles, m08-bio20, etc.).
- **Voor:** meest autoritatief/actueel; onafhankelijk van de export-cadans.
- **Tegen:** dupliceert build-pipeline-parsinglogica (**K4-conflict**); versionInfo zegt nog steeds "4.6.0" dus lost de label-vraag niet op; meer code + onderhoud; meer kans op divergentie met Spoor A-render.
- **Aanbeveling:** niet nu — tenzij de masterchat een bewuste TTL-first-architectuur voor Spoor B wil (dan is K4 te herzien).

---

## Mijn aanbeveling

**Optie A**, met eerlijke versie-labeling. Concreet, ná akkoord:
1. `import-from-ontology.py` (version-param) leest `grc-data-v4_6_0.json`, extraheert frameworks/controls/M04-rollen + IRI (`uri`) + bilinguale labels.
2. Levert een **idempotente, non-destructieve** SQL-INSERT-bundle (`INSERT OR IGNORE` / upsert; verwijderde IRIs → orphan-markeren, nooit hard-deleten).
3. K1: voegt `iri`-kolom toe aan de concept-tabellen (frameworks/controls/rollen).
4. K3: Spoor B-metadata toont "ontologie-structuur v4.6.0 (SKOS-status t/m v4.6.3)".

Ik wacht op je keuze (A/B/C) vóór ik B7 bouw.

## Niet-gedaan (bewust)
- ❌ Geen `import-from-ontology-*.py` geschreven.
- ❌ Geen schema-wijziging aan v3-2, geen SQL-bundle.
- ❌ Geen Spoor A-build gedraaid.
- ❌ Geen commit.
