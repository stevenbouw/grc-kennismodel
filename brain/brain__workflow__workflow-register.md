---
type: index
id: workflow-register
title: Workflow-register — Werkwijze GRC Kennismodel-project
status: living
date: 2026-05-29
---

# Workflow-register — Werkwijze GRC Kennismodel-project

Overzicht van werkdisciplines en proces-conventies die het project beheersbaar houden. Zeven workflow-files in totaal (incl. sprint-protocollen + commit-push-werkverdeling iteratie 15). Canonieke sprint-protocollen-set staat in `docs/sprint-protocols.md` (**18 protocollen + 1 gedragsregel** sinds iteratie 16 — Protocol 18 toegevoegd).

## Snelle navigatie

| Workflow | Wat het regelt | Status |
|---|---|---|
| [[brain__workflow__zes-chat-architectuur]] | Master/Tech/Doc/Dashboard/Asset/Analyse — rolverdeling + doorverwijs-discipline | living |
| [[brain__workflow__scope-discipline]] | Werkwijze bij scope-afwijkingen (Optie A/B/C-rapport, pauze-protocol) | living |
| [[brain__workflow__opleveringsprotocol]] | Opzet/bestaan/werking-formaat per release + canonieke artefacten | living |
| [[brain__workflow__masterchat-interactie]] | Wat aan Master / wat zelf — grens-discipline | living |
| [[brain__workflow__opzet-bestaan-werking]] | Drie-niveau-audit-conventie (opzet → bestaan → werking) | living |
| [[brain__workflow__sprint-protocollen]] *(v1.7)* | Vijf nieuwe sprint-protocollen formeel: pre-sprint-inventarisatie + schema-meta-rapport + bron-verificatie + raming-discipline + patch-rapport §9 | living |
| [[brain__workflow__commit-push-werkverdeling]] *(iteratie 15)* | Wie commit + pusht naar de repo: masterchat sinds 28-05-2026 autonoom; subagents NOOIT zelfstandig (invariant) | living |

## Clusters per fase van het werk

### Pre-sprint (vóór het werk begint)

- [[brain__workflow__sprint-protocollen]] — Protocol B (inventarisatie) + bron-verificatie
- [[brain__workflow__masterchat-interactie]] — GO/NO-GO

### Tijdens-sprint (tijdens het werk)

- [[brain__workflow__zes-chat-architectuur]] — wie doet wat
- [[brain__workflow__scope-discipline]] — wat te doen bij afwijking
- [[brain__workflow__sprint-protocollen]] — raming-discipline tijdens aggregatie

### Post-sprint (na het werk)

- [[brain__workflow__opleveringsprotocol]] — release-artefacten
- [[brain__workflow__opzet-bestaan-werking]] — kwaliteits-niveau-bewijs
- [[brain__workflow__sprint-protocollen]] — Protocol C (schema-meta-rapport-herziening) + patch-rapport §9
- [[brain__workflow__commit-push-werkverdeling]] — wie commit + pusht (iteratie 15)

## v1.7-uitbreiding: vijf nieuwe protocollen

Per projectinstructie v1.7 zijn vijf werkdisciplines formeel geldend gemaakt. Zie [[brain__workflow__sprint-protocollen]] voor uitwerking.

| Protocol | Aard | Eerste toepassings-bewijs |
|---|---|---|
| Pre-sprint-inventarisatie (Protocol B) | Verplicht bij structurele wijziging | v4.4.0: 5/5 signalen → Route 5-correctie |
| Schema-meta-rapport (Protocol C) | Eenmalig + herziening per minor-release | v4.3.3-eerste; niet geüpdatet v4.4.0 |
| Bron-verificatie vóór TBox-declaratie | Verplicht bij externe-naam-verwijzing | v4.4.0: `ext:hasENISAGuidance`-correctie gemarkeerd |
| Raming-discipline bij aggregatie | Verplicht bij grain-mismatch | v4.4.0: 290→183 (37% dedup) Sheet 9 mapping |
| Patch-rapport §9 verplicht | Per release | v4.4.0: eerste exemplaar |

## Iteratie 16-additions (29 mei 2026) — Protocol 18 + skill + twee leerpunten

Brein-cyclus iteratie 16 verwerkte naast de v4.6.4-sprint vier proces-/tooling-items:

### Protocol 18 — Pre-sprint-dashboard-update-discipline
Surgisch toegevoegd aan `docs/sprint-protocols.md` (kop 17 → 18; canonieke 1-17 ongewijzigd). Dashboard-tegenhanger van Protocol 1: vier-tot-zeven-vragen-checklist die de Dashboard-subagent vóór elke build-script-aanraking bij een nieuwe baseline doorloopt; uitkomst (ja/nee + impact) in het dashboard-patchnotitie-rapport. Bron: masterchat-concept `docs/instructies/protocol-18-concept.md`, GO 29 mei. Zie [[brain__workflow__sprint-protocollen]].

### D.7 — GRC-domein-skill (Claude Code)
Nieuwe **description-triggered skill** opgeleverd + GO: `.claude/skills/grc-domein/SKILL.md` (116 regels) + `kaders-reference.md` (93 regels). Bevat NL-kaders-domeinkennis (COSO/COBIT/BVA-CIO/NIS2/VIR-VIRBI/AVG/CBW-Cbb/DORA/BIO 2.0/ISO/NIST/CSF 2.0/ENSIA/volwassenheidsmodel), vijf-lagen-ordening, relatie-semantiek (9 properties + 2 ketens), SKOS cross-category-basislijn, status-discipline, BBN-discipline, NEN-discipline, §0.5-firewall. Elk feit bron-geverifieerd (Protocol 4-geest). **Brein heeft de skill-bestanden NIET aangeraakt** (buiten brain-scope — `.claude/skills/`). 
> **Openstaande verificatie (masterchat-actie, NIET Brein):** bevestigen dat `fw:relatedTo` / `fw:alignsWith` / `fw:supersedes` daadwerkelijk in `m01-framework.ttl` staan zoals de skill veronderstelt. De skill verifieerde 9 relatie-properties aan de bron (m01 r.196-291 + m17 r.81-97); deze drie zijn als aandachtspunt genoteerd.

### Leerpunt — settings.json-schemafix (workflow-leerpunt)
De `.claude/settings.json` faalde te parsen door een foute `$schema`-URL (`claude.com/...` i.p.v. `json.schemastore.org/claude-code-settings.json`); opgelost. **Brein heeft settings.json niet aangeraakt** (`.claude/settings.json` buiten brain-scope). Leerpunt: een verkeerde `$schema`-URL breekt stil de settings-parse — bij hook-/permission-vreemdheden eerst de `$schema`-regel checken.

### Leerpunt — version-drift grc-core version-triple
De `grc-core` version-triple stond sinds T1 op **4.6.0** — nooit meegebumpt bij T1/T2/T3 (SKOS-substituties, triple-neutraal). v4.6.4 corrigeerde naar 4.6.4. Leerpunt: de version-bump-stap wordt bij **triple-neutrale** T-sprints makkelijk overgeslagen omdat de canonieke metrics niet veranderen → geen meet-signaal. Aandachtspunt voor toekomstige kwaliteitsanalyse-/T-sprints. **Mogelijk relevant voor een Protocol-aanvulling (kandidaat, NIET nu formaliseren — masterchat-werk).** Zie [[brain__sprints__v4_6_4_csf-range-fix-dl-conformiteit]].

## Cross-references

- [[brain__concepts__scope-discipline]] — concept-niveau-uitleg (waarom)
- [[brain__concepts__meeliftregel-edit-scope]] — D6-conventie (vertaling-scope-uitbreiding v1.7)
- [[brain__concepts__provenance-en-attribuering]] — bron-discipline (CC-BY-attributie)
- [[brain__sprints__sprint-register]] — geschiedenis-overzicht waarin disciplines zijn ontstaan
- [[brain__decisions__D-register]] — D-decisions die werkwijze ondersteunen
- [[brain__index]] — masterindex

## Wat NIET in workflow zit

| Onderwerp | Waar dan wel |
|---|---|
| Ontologie-conventies (naming, namespaces) | [[brain__decisions__D-register]] (D2, D3, D5 etc.) |
| Bron-licentie-discipline | [[brain__sources__source-register]] + [[brain__concepts__provenance-en-attribuering]] |
| Module-conventies | [[brain__modules__module-register]] |
| Karakter-beleid (organisatie-naam etc.) | Projectinstructie v1.7 (`gedeelde gedragsregels`) |

— Einde workflow-register.
