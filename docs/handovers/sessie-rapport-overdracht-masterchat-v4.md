# Sessie-rapport — Overdracht naar nieuwe masterchat (v4.0)

**Datum:** 28 mei 2026
**Versie:** v4.0 (opvolger van v3.0 d.d. 27 mei 2026)
**Status:** Definitief — klaar voor overdracht
**Doel:** Volledige zelfstandige context voor nieuwe masterchat in claude.ai. Met dit document + GitHub-MCP-toegang tot `stevenbouw/grc-kennismodel` is het project zonder gaps voort te zetten.
**Volgende voorgenomen activiteit:** T3 pre-sprint-inventarisatie draait **synchroon** (Tech-subagent in Claude Code); na oplevering volgt masterchat-review + protocol-beslissing (v1.3-vaststelling of v1.4-aanvulling) + pilot-instructie.

---

## §0. Quick-start voor nieuwe masterchat

Als nieuwe masterchat: lees eerst dit hele document. Bevestig daarna dat je GitHub-MCP-toegang werkt door één bestand uit `stevenbouw/grc-kennismodel` op te halen (suggestie: `brain/brain__index.md` voor vault-staat-overzicht). Wacht op Steven's volgende prompt.

**Vier meest-relevante punten om te onthouden:**

1. **Baseline is v4.6.2** (post-T2-patch, 27 mei 2026). Niet v4.6.0/v4.6.1 zoals oudere documenten suggereren.
2. **T3-sprint is actief** — de pre-sprint-inventarisatie (m14 AVG/GDPR SKOS-audit) draait synchroon bij Tech. Verwacht een inventarisatierapport ter review. Zie §12.1.
3. **SKOS-protocol staat op v1.2 (operationeel) + v1.3 (DRAFT)** — niet v1.1 zoals v3 vermeldde. Zie §5.
4. **Tech heeft uitgebreide lokale NEN-toegang** in `/Users/stevenbouwmeester/grc-sources-licensed/` — nu **14 ISO-normen** (was 6). Zie §6.

---

## §1. Project-essentie (één-paragraaf-versie)

Steven is GRC-adviseur bij een Nederlandse Rijksoverheidsorganisatie (gebruik altijd "de organisatie" of "Rijksoverheidsorganisatie", nooit de daadwerkelijke naam). Hij bouwt het **GRC Kennismodel** — een OWL 2 DL ontologie die alle toepasselijke wet- en regelgeving, normen en best practices integreert in één machine-leesbare kennisbron met dashboard-bediening. Het model is de informatie-laag van het ISMS. Steven is "redelijke leek" in ontologie-engineering met sterke GRC-domeinkennis. Hij communiceert in het Nederlands, verwacht eerlijke pushback, en geen diplomatieke omwegen. Formele Claude-toestemming verkregen maart 2026.

**Kernprincipe D9 — framework-neutraal:** alle normen/wetten/kaders zijn gelijkwaardig gemodelleerd; geen enkel framework heeft architecturaal privilege. BIO 2.0 is het operationele toepassings-perspectief voor dashboard + rapportage (verplichte Rijksoverheid-baseline), niet de architecturele kern. "Het model is het woordenboek (neutraal), het dashboard is het verhaal (perspectief)."

---

## §2. Project-architectuur — zeven chats

| Chat | Locatie | Rol | Doet wel | Doet niet |
|---|---|---|---|---|
| **Master** | claude.ai | Projectadviseur + GRC-architect | Strategie, sparring, architectuurbeslissingen, prioritering, scope-pauze-besluiten, eind-sign-off, sprint-instructies | Geen Turtle/SPARQL, geen documenten, geen dashboard-code, geen autonome bash-acties |
| **Technisch** | Claude Code | Ontologie-expert OWL/SPARQL/SHACL | Turtle, SPARQL, SHACL, reasoner-validatie, diagnostiek, patch-voorbereiding, applier-scripts, NEN-bron-lezing | Geen strategie, beleid, UI-code, geen autonome commits |
| **Documentatie** | claude.ai | Beleidsadviseur + schrijver | PID, managementcommunicatie, beleid (NL) | Geen ontologie-code, dashboard-code |
| **Dashboard** | Claude Code | Full-stack developer + visualisatie | HTML/JS dashboards, D3/Chart.js, SPARQL, export-scripts | Geen ontologie-wijzigingen, beleidsdocumenten |
| **Asset** | claude.ai | M18-specialist | M18 TBox, mappings, SHACL (afgerond; stand-by) | Geen wijzigingen andere modules |
| **Analyse** | claude.ai | Framework-analist | Externe frameworks analyseren, opties formuleren, landschap-onderzoek | Geen Turtle, geen architectuurbeslissingen, geen beleid |
| **Brein** | Claude Code | Brain-vault-onderhoud | Aanmaken/updaten brain__*-bestanden, cross-referentie-bewaking, autonoom bepalen welke bestanden bijwerken | Geen architectuurbeslissingen, geen ontologie-wijzigingen, geen beleid |

**Werkproces post-migratie (sinds 26 mei 2026):**

Masterchat in claude.ai schrijft instructie → Steven push naar GitHub → subagent in Claude Code voert uit → push deliverables → masterchat review → Brein-subagent doet brain-update na sprint.

**Steven is tussenmens** bij overhandigings-momenten Claude Code ↔ claude.ai. Subagents committen **nooit** zelfstandig — Steven inspecteert `git status` + `git diff` en commit handmatig.

---

## §3. Vastgestelde ontwerpbeslissingen — D1 t/m D12 + D4.1

Wijzigingen vereisen masterchat-goedkeuring. Geen D-wijzigingen sinds D4.1 (27 mei).

### §3.1 — D-decisions D1 t/m D12 (kort overzicht)

| ID | Beslissing | Status |
|---|---|---|
| D1 | OWL 2 DL profiel | Initieel |
| D2 | Turtle-serialisatie | Initieel |
| D3 | 11 namespaces (`fw:`, `ctrl:`, `bio:`, `risk:`, `roles:`, `compl:`, `isms:`, `biz:`, `ext:`, `asset:`, `csf:`) | Definitief sinds v4.5.0 |
| D4 | SKOS voor cross-framework mappings | Initieel; **D4.1 toegevoegd 27-05-2026** |
| D5 | `owl:sameAs` strikt voor ctrl:↔bio: brug (93 paren) | Initieel |
| D6 | Tweetalige annotaties @nl/@en — meeliftregel | v4.1.0 |
| D7 | BIO 2.0 als twee klassen (BIOControl + OverheidsMaatregel) | Initieel |
| D8 | Eén canonieke SoA (isms:SoA_2026 + 93 SoAEntry_*) | v4.2.2 |
| D9 | Framework-neutraal model — alle kaders gelijkwaardig | 17-03-2026; **bewijs verdiept v4.6.2** |
| D10 | COSO ICF/ERM als enterprise-governance-laag | 17-03-2026 |
| D11 | `owl:sameAs` asset-convergentie — ster-patroon asset:↔risk:↔isms: (5 bruggen) | 13-04-2026 |
| D12 | Drie-laags compliance-architectuur (regulatory / legal / requirement) | 22-04-2026 |

**D9-bewijs-verdieping (v4.6.2):** T2-sprint bevestigde framework-neutraliteit óók op de cross-framework SKOS-mapping-laag — op 118 ctrl→compl-paren over 10 NIS2-art.21-letter-clusters bleek geen framework sterker mapping-privilege te hebben; cluster-discipline-bewijslast is symmetrisch. Volledig in `brain/brain__decisions__D09_framework-neutraliteit.md`.

### §3.4 — D4.1 — Disclaimer-handling bij autoritatieve mapping-bronnen (vastgesteld 27-05-2026)

**Kern-regel** (volledige tekst in `brain/brain__decisions__D04_skos-cross-framework.md`):

Wanneer een autoritatieve mapping-bron tussen frameworks een expliciete non-equivalence-disclaimer bevat:

- **a)** `skos:exactMatch` is **niet verdedigbaar**, ongeacht of C1-C3 (zie §5) sluitend voldoen
- **b)** `closeMatch` / `relatedMatch` / `broadMatch` / `narrowMatch` blijven valide opties
- **c)** Geldt vanaf vaststelling; geen retroactieve audit

**Toepassings-precedent uitgebreid (T2):** D4.1 is bij T1 toegepast op paar-niveau (28 ENISA-TIG-erfde paren), en bij T2 bevestigd op **cluster-niveau** — bij een homogene bron-stack volstaat één D4.1-bevestiging per cluster; heterogene clusters vereisen per-paar-toets. Onderscheid homogeen/heterogeen vastgelegd in `brain/brain__decisions__D04`.

**Bekende disclaimers:**

| Bron | Locatie | Status |
|---|---|---|
| ENISA TIG v1.0 (juni 2025) | Regel 285 | **Bevestigd** — T1+T2 m10-cluster |
| NIST OLIR | Niet geverifieerd | Kandidaat — eerstvolgende NIST-sprint |
| ISO Annex F (27001:2022) | Niet geverifieerd | Kandidaat — eerstvolgende ISO-sprint |

---

## §4. Sprint-protocollen 1-17 (operationeel in `docs/sprint-protocols.md` v1.3)

Per 28 mei 2026 zijn er 17 sprint-protocollen actief, plus vier werkflow-disciplines uit Protocol v1.3 (zie §5).

| # | Protocol | Status |
|---|---|---|
| 1-13 | Pre-migratie-baseline (inventarisatie, multi-module-discipline, bron-verificatie, ramings-baseline, etc.) | Ongewijzigd; gedocumenteerd in projectinstructie v1.9/v1.10 |
| 14 | Pre-push disclosure-check (5 categorieën: organisatie-naam, persoonsnamen, lokale paden, credentials, NEN-tekst >10 woorden) | Actief |
| 15 | Tech levert werkbare applier (Python preferred), niet alleen specificatie | Actief — T2 leverde `apply_patch_v4_6_2.py` met dry-run + productie-modus |
| 16 | Lokatie verificatie-scripts expliciet in patch-rapport §9 Deliverables-tabel | Actief |
| 17 | NEN-werkverdeling met Tech-autonomie via lokale bron-toegang | Herzien 27-05-2026 |

**Protocol v1.3-werkflow-disciplines** (DRAFT, opgenomen als gedragsregel in projectinstructie v1.10, formele vaststelling pending bij T3/m14-scoping):

- §10.2 Bottom-up rapport-bouw verplicht (details vóór samenvatting; §1 vroeg-ingevuld = "INITIEEL, TE BEVESTIGEN")
- §10.3 Interne tabel-consistentie-discipline (Σ-check + bron-van-waarheid bij discrepantie)
- §10.4 Helper-script-classificatie autoritatief bij discrepantie met handmatige classificatie
- §10.5 Metrics-tabel-scope-annotatie verplicht (expliciete scope bij metrics-tabellen)

---

## §5. Methode-protocollen voor SKOS-beoordeling (CORRECTIE t.o.v. v3)

**Belangrijke correctie:** v3 vermeldde "Protocol v1.1-draft". Die draft is bij T2-scoping doorontwikkeld naar **v1.2** (operationeel voor T2-uitvoering) en daarna naar **v1.3** (draft, post-T2). De repo bevat `docs/skos-beoordelings-protocol-v1_2.md` en `docs/skos-beoordelings-protocol-v1_3.md`. Er is geen losse v1.1 meer in gebruik.

### §5.1 — `docs/skos-beoordelings-protocol-v1_0.md` (FINAL)

Vastgesteld 26-05-2026 voor T1. Vier-criteria-set (C1 definitioneel, C2 cardinaliteit, C3 inclusie-richting, C4 bron-evidence). Historische referentie + T1-vergelijking.

### §5.2 — `docs/skos-beoordelings-protocol-v1_2.md` (OPERATIONEEL)

Autoritatief voor T2-uitvoering en T2-historie. Bevat: D4.1-vooraf-check, C1-C4 met C2-cluster-cardinaliteit, evidence-niveau-1-pre-stap, Tech-autonomie NEN, cluster-discipline verplicht, bidirectional-audit-symmetrie.

### §5.3 — `docs/skos-beoordelings-protocol-v1_3.md` (DRAFT)

Opgesteld 27-05-2026 post-T2. Zeven verfijningen t.o.v. v1.2 (§2.1 C1-grens-verduidelijking, §2.2 C2 object-cluster-prevalentie, §3.3 cluster-discipline-bewijslast-asymmetrie, §5.1 cluster-representant-keuze, §5.2 confidence-drempels, §10.2-§10.5 werkflow-disciplines). **Status: DRAFT** — vaststelling pending bij T3/m14-scoping. v1.2 blijft autoritatief tot vaststelling.

**T3-relevante open vraag:** of v1.3 (of een nieuwe v1.4) een aanvulling nodig heeft voor (a) de compl→ctrl-richting van m14 (omgekeerd t.o.v. m10) en (b) heterogene-cluster-handling (m14 convergeert vermoedelijk níét naar één match-type). De T3 pre-sprint-inventarisatie (Vraag F) levert hierover een aanbeveling. Zie §12.1.

---

## §6. NEN-bron-toegang voor Tech (UITGEBREID 28-05-2026)

**Locatie op Steven's machine:** `/Users/stevenbouwmeester/grc-sources-licensed/`

**Beschikbare bronnen** (lokaal alleen, niet in repo wegens NEN-licentie-restrictie). Per 28 mei uitgebreid van 6 naar **14 normen**:

| Norm | Cluster | Sinds |
|---|---|---|
| ISO 27002:2022 | IB-controls | basis |
| ISO 27001:2022 | ISMS | basis |
| ISO 27005:2024 | Risk | basis |
| ISO 31000:2018 | Risk mgmt | basis |
| ISO 22301:2019 | BCM requirements | basis |
| ISO 22313:2020 | BCM guidance | basis |
| **ISO 27701:2025** | **Privacy (PIMS)** | **28-05 — T3 m14-bron** |
| **ISO 27701-conformiteitsbeoordeling** | **Privacy-aanvullend** | **28-05** |
| **ISO 29100:2011** | **Privacy framework** | **28-05** |
| **ISO 42001:2023** | **AI Management System** | **28-05 — M19-toekomst** |
| **ISO 23894:2023** | **AI risk management** | **28-05** |
| **ISO 22989** | **AI terminology** | **28-05** |
| **ISO 27035-1** | **Incident management** | **28-05 — AVG art. 33/34** |
| **ISO 27031** | **ICT readiness BC** | **28-05** |
| **ISO 19011** | **Auditing management systems** | **28-05** |

**Belangrijke versie-noot:** ISO 27701:**2025** (gepubliceerd 14-10-2025) vervangt de ingetrokken 2019-editie. 2025 is gebaseerd op 27001:2022 & 27002:2022 (huidige nummering) en is een standalone standaard. Steven heeft de 2025-editie — geen hercodering vanuit 2013-nummering nodig.

**Discipline-regels** (kritisch — geldt voor alle Tech-output naar repo):

- **Geen verbatim NEN-tekst-fragmenten** in rapport-output, commit-messages, Turtle-files, code-comments, of geautomatiseerde output
- Wel toegestaan: parafrase + clausule-verwijzing
- Niet toegestaan: letterlijke citaten >10 woorden
- Pre-push disclosure-check (Protocol 14) bevat NEN-tekst-fragment-detectie als vijfde categorie

**Niet in repo / niet in Project Knowledge als publieke bron** — deze 14 normen blijven uitsluitend lokaal bij Steven, Tech-leestoegang via Claude Code.

---

## §7. Actuele baseline — v4.6.2 (post-T2-patch)

**Patch-datum:** 27 mei 2026
**Aanleiding:** T2-sprint — 65 ctrl:↔compl: SKOS-herclassificaties in m10 (32 closeMatch→broadMatch + 33 relatedMatch→broadMatch)

### §7.1 — Kerncijfers

| Metric | v4.6.2 | Δ vs v4.6.1 |
|---|---:|---:|
| Triples pre-inferentie | 20.950 | 0 |
| Triples post OWL RL | 44.907 | 0 |
| Klassen | 199 | 0 |
| NamedIndividuals | 1.383 | 0 |
| ObjectProperties | 149 | 0 |
| DatatypeProperties | 96 | 0 |
| owl:sameAs | 98 (93 D5 + 5 D11) | 0 |
| SKOS-mappings totaal | 1.798 | 0 |
| — skos:exactMatch | 18 | 0 |
| — skos:closeMatch | 1.457 | −32 |
| — skos:broadMatch | 131 | +65 |
| — skos:narrowMatch | 0 | 0 |
| — skos:relatedMatch | 192 | −33 |
| owl:Nothing post-inf | 0 (consistent) | 0 |
| SHACL SECTIE A (inference=none) | 0 violations | 0 |
| SHACL SECTIE B (inference=owlrl) | 0 violations | 0 |
| SHACL COMBINED | 290 (identiek aan v4.6.0/v4.6.1-baseline) | 0 |

**T-sprint-patroon:** T-sprints zijn triple-neutraal (SKOS-predicate-substitutie, geen toevoeging/verwijdering). Δ pre-/post-OWL-RL = 0. Relevante meetwaarden voor T-sprints zijn SKOS-distributie-Δ + cluster-discipline-bewijs, niet triple-Δ. Zie H41 (§12.2).

### §7.2 — Module-impact

Alleen `m10-nis2-ext.ttl` gewijzigd in T1+T2. Hash-evolutie:

- v4.6.0: `78b8ee44...`
- v4.6.1 (T1): `cb2d567b...`
- v4.6.2 (T2): `a4bfdc12...`

Alle 21 andere modules + `grc-shacl.ttl`: hash ongewijzigd sinds v4.6.0.

### §7.3 — m10 ctrl→compl SKOS-eindstand (na T1+T2)

Cumulatief 93 m10-paren gepatcht (28 in T1 + 65 in T2). Alle 118 m10 ctrl→compl-paren convergeren naar `broadMatch`:

- exact 0 / close 0 / broad 118 / narrow 0 / related 0

H36 m10-component is daarmee **closed**. m14-component (31 paren) is open subtask → T3-scope.

---

## §8. Recente sessies-overzicht (chronologisch)

### §8.1 — 26 mei 2026 (migratie + T1)

Migratie naar Claude Code + GitHub; polish-mini-sprint; Brein-cyclus iteratie 12; **T1-sprint** (28 ctrl:↔compl: exactMatch→broadMatch, patch v4.6.1); methode-protocol v1.0 vastgesteld. Detail in v3-rapport §8.1 + `output/reports/t1-eindrapport-v4_6_1.md`.

### §8.2 — 27 mei 2026 ochtend (mini-revisies + Brein 13)

Vier mini-revisies: productlijn-scheiding (Optie D), D4.1-vaststelling, Protocol 17-herziening, SKOS-protocol-draft. Brein-cyclus iteratie 13. Detail in v3-rapport §8.2.

### §8.3 — 27 mei 2026 middag→avond (T2-sprint) — NIEUW

**T2-sprint volledig uitgevoerd** (SKOS-kwaliteitsanalyse Fase 2 — bidirectional audit ctrl:↔compl: in m10):

| Stap | Wat | Uitkomst |
|---|---|---|
| 1 | Pre-sprint-inventarisatie | 118 m10-paren bevestigd; cluster-structuur 10 clusters; evidence-coverage via CBW-Excel |
| 2 | Pilot (8 paren) | Pre-Stap-4 errata-correctie (pilot-rapport + Stap 3-rapport §1.1) |
| 3 | Hoofd-uitvoering | 118 paren beoordeeld onder Protocol v1.2; 10/10 clusters convergeren naar broadMatch |
| 4 | Patch v4.6.2 | 65 mutaties (32 downgrade close→broad + 33 upgrade related→broad); 13/13 GO-criteria groen |

**Masterchat-scope-besluit:** Optie C (m10-only T2; m14 uitgesteld naar T3). **Masterchat-instructie-fout** (zelf-erkend, patch-rapport §13.2): §1-verwachtings-tabel inconsistent met §8 GO-criterium door impliciete cumulatieve-scope-formulering. Tech paste Protocol 12 correct toe; §8 GO-criterium leidend. Leerpunt → Protocol v1.3 §10.5 (metrics-tabel-scope-annotatie verplicht).

### §8.4 — 27 mei avond → 28 mei (Optie C werkstroom + T3-scoping) — NIEUW, DEZE SESSIE-REEKS

**Optie C werkstroom (na T2-afsluiting):**

1. **Protocol v1.3-draft** opgesteld (`docs/skos-beoordelings-protocol-v1_3.md`, 618 regels) — commit `3b7a207`
2. **Projectinstructie v1.10** opgesteld (`docs/projectinstructie-v1_10.md`, 767 regels) — commit `212f853`. Vervangt v1.9; verwerkt T1+T2, migratie, protocollen 14-17, D4.1, H41, brain-vault-locatie-update, Tech-NEN-autonomie
3. **Brein-cyclus iteratie 14** — commit `fc0acfc`. Nieuwe brain-bestanden: `brain__sprints__T2-skos-bidirectional-audit-m10.md`, `brain__architecture__H41_skos-axioma-set-handling.md`, `brain__concepts__cluster-discipline-bewijslast.md`; updates op D04 (D4.1-cluster-precedent), H36 (m10 closed), H39, skos-beoordelings-protocol-concept, registers, index, log
4. **README v4.6.2** opgesteld (224 regels) — Optie C hybride: project-README + baseline + sprint-historie + key documents. Vervangt v4.5.0-eindoplevering-document. Gepushed.

**Skill-evaluatie Tier 1 + Tier 2** (masterchat-evaluatie, `/mnt/user-data/outputs/skill-eval-tier1-tier2-2026-05-27.md`, 335 regels — NB: dit bestand is in masterchat-outputs opgeleverd; Steven kan het naar `output/reports/` pushen indien gewenst):

| Skill | Recommendation | Kern |
|---|---|---|
| Sushegaad/Claude-Skills-GRC | 🟡 HOLD | Coverage-overlap; NEN-risico onbekend; geen NL-context |
| GRCEngClub/claude-grc-engineering | 🟢 NO-GO Spoor A / 🟡 HOLD Spoor B | Past bij Spoor B lab-test, niet huidige fase |
| fabio-rovai/open-ontologies (MCP) | 🟡 HOLD + evaluatie-sprint-kandidaat | Drie H-items (H37+H38+H41) gezamenlijke trigger; MIT; tableaux OWL2-DL |
| kfchou/wiki-skills | 🟡 HOLD installatie / 🟢 GO referentie | Karpathy-pattern doen we al via Brein-subagent |

**Extensie-landschap-analyse** (door aparte Analyse-chat, NIET deze masterchat): `output/reports/extensie-landschap-claude-2026-05-28-3.md` (~100 KB) — uitputtende landschap-analyse van skills/plugins/MCP-connectors/agent-setups voor het project. Naastgelegen onderzoek bij bovenstaande skill-evaluatie. **Nieuwe masterchat: raadpleeg dit document via GitHub-MCP indien skill/MCP-besluiten relevant worden.** Inhoud niet in dit overdracht-rapport samengevat (apart, groot, zelfstandig leesbaar).

**T3 m14-scoping (kern van deze sessie-reeks):**

- Sprint-keuze: **T3 = m14 AVG/GDPR SKOS-audit** (sluit H36 m14-component af)
- Bron-scan uitgevoerd (Optie C hybride): **geen autoritatieve EU-cross-walk** zoals ENISA TIG voor NIS2 — ENISA's GDPR-werk is risico-gebaseerde maatregelen-catalogus, geen ISO-control-mapping. Wel meerdere publieke cross-walks (ISMS.online 2022, SCF, NQA 2013, Legiscope)
- **ISO 27701:2025** geïdentificeerd als sterkste autoritatieve hulpbron (zie §6); door Steven opgenomen in lokale folder samen met 7 andere ISO-normen
- Evidence-discipline T3: gelaagde triangulatie (27701:2025 + conformiteitsbeoordeling + publieke 2022-cross-walks + ISO 27002:2022-lezing). Bijna-niveau-1, geen volledige convergentie-garantie zoals m10
- **T3 pre-sprint-inventarisatie-instructie** opgesteld (240 regels) — draait nu **synchroon** bij Tech. Zie §12.1

---

## §9. Brain-vault — primaire kennisbron

**Structuur:** flat bestanden in `brain/`-folder met `__`-separator voor folder-encoding (decisions, sprints, architecture, concepts, modules, sources, workflow, scope).

**Entry-points:**

- `brain/brain__index.md` — vault-staat-tabel, iteratie-teller, baseline-overzicht
- `brain/brain__log.md` — append-only iteratie-log (nieuwste bovenaan)
- Folder-registers: `brain__decisions__D-register.md`, `brain__sprints__sprint-register.md`, `brain__architecture__H-register.md`, `brain__concepts__concept-register.md`, `brain__modules__module-register.md`, `brain__sources__source-register.md`, `brain__workflow__workflow-register.md`, `brain__scope__scope-register.md`

**Iteratie-stand** per 28-05-2026: iteratie 14 afgesloten, brain-vault ~120 bestanden.

**Conventie:** bij vragen over projecthistorie, architectuur of conventies → raadpleeg brain-vault via GitHub-MCP vóór andere bronnen. De brain-vault is autoritatief. Bestanden gebruiken Obsidian-stijl `[[brain__*]]`-wikilinks.

---

## §10. Sprint-architectuur en huidige toestand

### §10.1 — Vijf doelen

G1 GRC Referentiemodel | G2 Rollen & RACI | G3 Business Alignment | G4 ISMS | G5 OWL Ontologie

### §10.2 — Drie sporen

| Spoor | Wat | Status |
|---|---|---|
| A | Technische ontologie-opbouw (zonder organisatiedata) | Voltooid t/m v4.6.2 voor Fase 1-4 scope + T1+T2; T3 actief (kwaliteitsanalyse) |
| B | Organisatiespecifieke invulling | Pending; lab-test bij Technologie & Innovatie gepland als eerste proeftuin |
| C | Gebruik en governance (triplestore, dashboard, beheerproces) | Pending; dashboard-inhaalslag staat open (5+ sprints achterstand, 5 pending decisions) |

### §10.3 — Sprint-historie sinds Fase 4

| Sprint | Datum | Scope | Status |
|---|---|---|---|
| v4.6.0 | 21-05-2026 | Fase 4 — ENSIA + volwassenheidsmodel + CSF Tiers | Afgerond |
| (Migratie) | 26-05-2026 | Tech/Brein/Dashboard naar Claude Code + GitHub | Afgerond |
| T1 | 26-05-2026 | SKOS Fase 1 — H36-cluster (28 paren) | Afgerond — patch v4.6.1 |
| Brein 13 + mini-revisies | 27-05-2026 | T1-afronding + D4.1 + Protocol 17 + protocol-draft | Afgerond |
| **T2** | **27-05-2026** | **SKOS Fase 2 — m10 bidirectional (118 paren, 65 mutaties)** | **Afgerond — patch v4.6.2** |
| Brein 14 + Optie C | 27/28-05-2026 | T2-afronding + Protocol v1.3-draft + projectinstructie v1.10 + README v4.6.2 | Afgerond |
| **T3** | **28-05-2026** | **SKOS Fase 3 — m14 AVG/GDPR (31 paren, compl→ctrl)** | **Pre-sprint draait synchroon** |

---

## §11. Werkflow-leerpunten — kritiek voor toekomstige sprints

Uit T1-eindrapport §8 + T2-ervaring + Optie C-sessie:

- **§11.1 Tooling-discipline (Protocol 15):** Tech levert werkbare applier, niet alleen specificatie. T2 deed dit goed (`apply_patch_v4_6_2.py` met dry-run + productie-modus)
- **§11.2 Pad-discipline (Protocol 16):** lokatie verificatie-scripts in patch-rapport §9 Deliverables-tabel
- **§11.3 Werkverdeling (Protocol 17):** Tech autonoom met lokale NEN-toegang; masterchat alleen bij cross-bron-interpretatie
- **§11.4 ENISA-disclaimer-categorisch-effect:** D4.1. **m14-relevantie:** geen ENISA-achtige disclaimer-bron voor AVG → D4.1-logica niet toepasbaar op T3; beoordeling op SKOS-semantiek-gronden
- **§11.5 Cluster-discipline-overerving:** efficiënt bij homogene clusters. **m14-waarschuwing:** m14-clusters zijn vermoedelijk heterogeen (AVG↔control-relatie verschilt per control) → per-paar-toetsing nodig, GEEN m10-convergentie-aanname
- **§11.6 Sample-first zonder pre-pilot-verwachting**
- **§11.7 Twee-zijdige edge-case-analyse-format** voor masterchat-escalatie
- **§11.8 Steven's "denk ik" als verifier-signaal** — bij onzekerheid altijd GitHub-MCP-check op repo-staat
- **§11.9 Sprint-multiplier T-sprints:** T2 = 2,32× T1 qua mutatie-volume; T-sprints triple-neutraal. T3-verwachting: laag mutatie-volume (0-4), bevestigings-sprint
- **§11.10 Helper-script-classificatie autoritatief (Protocol v1.3 §10.4):** bij discrepantie handmatig vs helper-script wint helper-script; corrigeer rapporten via errata (T-historie bewaren)
- **§11.11 Bottom-up rapport-bouw (Protocol v1.3 §10.2):** details vóór samenvatting; §1 vroeg-ingevuld = "INITIEEL, TE BEVESTIGEN"

---

## §12. Open punten en roadmap

### §12.1 — Direct openstaand (volgende activiteit) — T3 ACTIEF

**T3 pre-sprint-inventarisatie draait synchroon** bij Tech-subagent. Instructie: `docs/instructies/instructie-t3-pre-sprint-inventarisatie.md` (of nog te pushen — Steven liet 'm synchroon uitvoeren).

**Verwachte deliverable van Tech:** `output/reports/t3-pre-sprint-inventarisatie.md` met:
- Vraag A: scope-bevestiging (31 paren? 27 related + 2 close + 2 broad?)
- Vraag B: cluster-structuur per AVG-artikel (5(1f)/25/32/33/34)
- Vraag C (KERN): bron-structuur-verificatie 27701:2025 + conformiteitsbeoordeling — wáár staat de GDPR↔control-relatie?
- Vraag D: evidence-coverage per paar
- Vraag E: bron-toegankelijkheid
- Vraag F: symmetrie- + heterogeniteit-methode-check (informeert protocol-beslissing)
- §9: pilot-sample-aanbeveling (6 paren)

**Na inventarisatie-review beslist masterchat:**
1. Protocol-versie: v1.3-vaststelling of v1.4-aanvulling (voor compl→ctrl-richting + heterogene clusters)
2. Pilot-instructie (Stap 2)

**Kritieke scope-pauze-trigger T3:** als 27701:2025 géén bruikbare GDPR↔control-relatie blijkt te bevatten (direct/indirect/via conformiteitsbeoordeling) → niveau-1-basis valt weg → masterchat beslist over niveau-2-only-route.

**Methodische kern T3 (≠ m10):** geen D4.1-disclaimer-logica; geen convergentie-aanname; per-paar-toetsing verwacht; vermoedelijk laag mutatie-volume (bevestigings-sprint). De huidige 27 relatedMatch zijn waarschijnlijk grotendeels verdedigbaar.

### §12.2 — Bewust geparkeerd (geen urgentie)

| Item | Type | Trigger |
|---|---|---|
| H36 m14-component | Inhoudelijk | **Wordt door T3 afgesloten** |
| H37 — open-ontologies MCP-server | Architectuur | Gekoppeld aan skill-evaluatie; evaluatie-sprint-kandidaat na T3 (samen met H38+H41) |
| H38 — OWL RL vs HermiT-equivalentie | Architectuur | Idem — derde reasoner-vergelijking via open-ontologies-evaluatie |
| H41 — SKOS-axioma-set-handling (skos:S46/S47) | Architectuur | Volledig geregistreerd post-T2. Trigger: substantiële SKOS-mapping-uitbreiding waar transitiviteit/symmetrie auditief relevant wordt |
| H39 — 290 SHACL COMBINED false-positives uitsplitsen | Hygiëne | Rustige sprint of SHACL-shapes-wijziging |
| H40 — Dashboard-UI-renderdekking | UX | UI-moderniseringssprint na Fase 4 |
| H33 — m11 SP 800-53 substantiële uitbreiding | Inhoudelijk | Spoor B-organisatie >50 niet-gemapte controls nodig |
| H34 — m11 enhancement-modellering | Inhoudelijk | Serieuze SP 800-53-toepassing |
| H25/H26/H27/H32/H35 | Per H-register | Per-item triggers |
| H15 (governance-graafdekking) / H21 (implicit individuals) | Architectuur | Spoor B / consistentie-keuze |
| Dashboard-inhaalslag | Spoor C | 5+ sprints achterstand + 5 pending decisions (JS wrapper, SKOS template, hash padding, HTML shell, 39-edge discrepantie). 39-edge hermeten tegen v4.6.2 vereist |
| PK-opschoning brain-vault + publieke bronnen | Hygiëne | GitHub-MCP stabiel — Steven heeft dit reeds deels uitgevoerd (PK-opschoning bevestigd) |
| Skill-installaties (Sushegaad/GRCEngClub/open-ontologies/kfchou) | Tooling | Per skill-evaluatie-recommendaties; Claude Code-werk door Steven, niet masterchat |

### §12.3 — Toekomst-richting

| Sprint-kandidaat | Wanneer | Wat |
|---|---|---|
| T3 | Actief | m14 AVG/GDPR (loopt) |
| Protocol v1.3-vaststelling | Bij T3-scoping | Sign-off + eventuele v1.4-aanvulling |
| T4+ | Na T3 | Overige SKOS-clusters (m11, m09-iso27001) of structurele uitbreiding (H33/H34) |
| open-ontologies-evaluatie-sprint | Na T3 | H37+H38+H41 gezamenlijk; geen migratie-besluit, alleen empirisch onderzoek |
| Dashboard-inhaalslag | Parallel mogelijk | Build-script naar v4.6.2-snapshot |
| Spoor B-voorbereiding | Latere fase | T&I lab-test |

---

## §13. Wat de nieuwe masterchat NIET moet doen

- **Geen autonome bash/git/edit-acties** — masterchat opereert in claude.ai zonder die tools
- **Geen scope-uitbreidingen zonder Steven-akkoord** — bij ambiguïteit scope-pauze met Optie A/B/C-rapport
- **Geen m10-cluster-convergentie-discipline klakkeloos op m14 toepassen** — m14 is semantisch heterogeen
- **Geen wijziging aan D-decisions** (D1-D12 + D4.1) zonder expliciete masterchat-judgement-cyclus
- **Geen wijziging aan sprint-protocollen 1-17** zonder grondige aanleiding
- **Geen organisatie-naam noemen** — altijd "de organisatie" of "Rijksoverheidsorganisatie"
- **Geen NEN-verbatim-tekst** in welke output dan ook
- **Geen herinrichting brain-vault** — structuur stabiel sinds iteratie 11-14
- **Geen skill-installatie-beslissingen namens Steven** — masterchat evalueert; Steven installeert in Claude Code

---

## §14. Tooling-status (per 28-05-2026)

| Tooling | Status | Locatie/configuratie |
|---|---|---|
| GitHub-MCP voor claude.ai | Werkend | `stevenbouw/grc-kennismodel`, privé |
| Claude Code in VS Code | Geauthenticeerd, actief | Tech/Brein/Dashboard-subagents |
| `CLAUDE.md` | Active (v1.5, projectinstructie-ref bijgewerkt naar v1.10) | Repo-root. NB: Steven heeft zelf een CLAUDE.md-aanpassing gedaan (toestemming Claude Code) — buiten masterchat-scope tenzij werkwijze-impact |
| Subagent-configs | Actief | `.claude/agents/tech.md`, `brein.md`, `dashboard.md` |
| `docs/sprint-protocols.md` | Actief — 17 protocollen (v1.3) | Repo |
| OWL RL reasoning | `axiomatic_triples=False`, `datatype_axioms=False` | Standaard-script-instellingen |
| pySHACL | Gesplitste validatie (SECTIE A + B + COMBINED) | Standaard-script-instellingen |
| Protégé | Stand-by — geen HermiT-rerun sinds v4.0.0 | Mac, lokaal |
| Cytoscape.js | Dashboard-engine `grc-explorer-v4_6_0.html` (Spoor A) | Dashboard nog op v4.6.0-snapshot — inhaalslag open |
| Lokale NEN-bronnen | Toegankelijk voor Tech — **14 normen** | `/Users/stevenbouwmeester/grc-sources-licensed/` |

---

## §15. Wat Steven moet uploaden naar nieuwe masterchat

### §15.1 — Primair (verplicht)

**Dit document** (`sessie-rapport-overdracht-masterchat-v4.md`). Zelfstandige basis.

### §15.2 — Secundair (aanbevolen, niet kritisch)

| Bestand | Waarom |
|---|---|
| `output/reports/patch-rapport-v4_6_2.md` (uit repo) | Volledig T2-detail + §13.2 masterchat-instructie-fout-leerpunt |
| `docs/projectinstructie-v1_10.md` (uit repo) | Actuele projectinstructie — vervangt v1.9 |
| `docs/skos-beoordelings-protocol-v1_2.md` + `v1_3.md` (uit repo) | Operationeel + draft — relevant voor T3-protocol-beslissing |
| `output/reports/t3-pre-sprint-inventarisatie.md` (zodra Tech levert) | T3-inventarisatie-uitkomst — direct relevant voor pilot-besluit |

### §15.3 — Niet nodig

- Brain-vault-bestanden: GitHub-MCP-bereikbaar
- Eerdere sessie-rapporten (v1.0-v3.0): vervangen door dit document
- Tussen-rapporten T1/T2: detail; GitHub-MCP indien nodig
- Extensie-landschap-analyse (100 KB): in repo, GitHub-MCP-bereikbaar; alleen raadplegen bij skill/MCP-besluiten

### §15.4 — Initiële prompt voor nieuwe masterchat

```
Je bent de nieuwe masterchat voor het GRC Kennismodel-project. Lees eerst
`sessie-rapport-overdracht-masterchat-v4.md` volledig (in uploads).
Verifieer daarna kort dat GitHub-MCP werkt door `brain/brain__index.md`
uit `stevenbouw/grc-kennismodel` op te halen. Als de T3 pre-sprint-
inventarisatie inmiddels is opgeleverd (`output/reports/t3-pre-sprint-
inventarisatie.md`), haal die ook op. Bevestig dan kort dat je context
hebt en wacht op mijn volgende prompt. Geen acties tot voltooid.
```

---

## §16. Geheugen-overweging voor Steven

`userMemories` bevat mogelijk nog outdated info (baseline v4.6.0/v4.6.1, oude pending-decisions). Dit overdrachtsdocument + GitHub-MCP zijn autoritatief boven memory-context. Memory-update via `memory_user_edits` is een overweging voor een rustige tussensessie — geen prioriteit boven T3.

---

## §17. Conclusie — productie-fase actief, T3 lopend

T1 + T2 volledig afgerond (m10 ctrl→compl volledig naar broadMatch, H36 m10-component closed). Brein-vault iteratie 14 afgesloten. Baseline v4.6.2 in productie. Projectinstructie v1.10, Protocol v1.3-draft, README v4.6.2 opgeleverd. Skill-evaluatie + extensie-landschap-analyse beschikbaar. Lokale NEN-folder uitgebreid naar 14 normen incl. ISO 27701:2025.

**T3-sprint is actief** — pre-sprint-inventarisatie draait synchroon bij Tech. Eerste actie nieuwe masterchat: T3-inventarisatierapport reviewen + protocol-beslissing (v1.3-vaststelling/v1.4-aanvulling) + pilot-instructie. H36 m14-component wordt door T3 afgesloten.

**Productie-fase écht actief.** Geen blokkerend masterchat-werk; T3-voortzetting op Steven's tempo.

---

*Einde overdrachtsdocument v4.0. Nieuwe masterchat is klaar voor T3-inventarisatie-review + vervolg bij Steven's volgende prompt.*
