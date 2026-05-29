# Sessie-rapport — Overdracht naar nieuwe masterchat (v5.0)

**Datum:** 28 mei 2026 (avond)
**Versie:** v5.0 (opvolger van v4.0 d.d. 28 mei 2026 ochtend)
**Status:** Definitief — klaar voor overdracht
**Doel:** Volledige zelfstandige context voor nieuwe masterchat in claude.ai. Met dit document + GitHub-MCP-toegang tot `stevenbouw/grc-kennismodel` is het project zonder gaps voort te zetten.
**Volgende voorgenomen activiteit:** geen actieve sprint. Steven kiest tussen meerdere richtingen — zie §12.1 en §17.

---

## §0. Quick-start voor nieuwe masterchat

Lees eerst dit hele document. Bevestig daarna GitHub-MCP-toegang door één bestand uit `stevenbouw/grc-kennismodel` op te halen (suggestie: `brain/brain__index.md` voor vault-staat-overzicht). Wacht op Steven's volgende prompt — onderneem geen actie.

**Zes meest-relevante punten om te onthouden:**

1. **Baseline is v4.6.3** (post-T3-patch, 28 mei 2026). Niet v4.6.2 zoals v4-handover suggereert.
2. **Geen actieve sprint.** T1+T2+T3 alle voltooid; H36 (SKOS-exactMatch-audit ctrl↔compl) **FULLY CLOSED**. Steven kiest tussen meerdere kandidaten voor wat hierna komt. Zie §12.1.
3. **Tooling-track 01+02+03 voltooid** — `.claude/`-laag operationeel met hooks, permissions, en 8 skills. Bestaande discipline is nu deterministisch geborgd. Zie §14.
4. **SKOS-protocol v1.3 is FINAL** (vastgesteld door masterchat 28-05-2026 bij T3-scoping). Geen DRAFT meer.
5. **Masterchat mag voortaan committen + pushen** naar de repo (nieuwe werkflow-regel sinds 28-05). Subagent-invariant onveranderd hard. Zie §2a.
6. **Cross-category-principe** geboren uit T3: control ↔ legal-obligation = `relatedMatch` als basislijn, niet `broad`/`narrowMatch`. Empirisch gevalideerd, brain-precedent gelegd, **nog niet** formeel in protocol-tekst (kandidaat v1.3.1 bij volgende SKOS-scoping). Zie §11.12.

---

## §1. Project-essentie (één-paragraaf-versie)

Steven is GRC-adviseur bij een Nederlandse Rijksoverheidsorganisatie (gebruik altijd "de organisatie" of "Rijksoverheidsorganisatie", nooit de daadwerkelijke naam). Hij bouwt het **GRC Kennismodel** — een OWL 2 DL ontologie die alle toepasselijke wet- en regelgeving, normen en best practices integreert in één machine-leesbare kennisbron met dashboard-bediening. Het model is de informatie-laag van het ISMS. Steven is "redelijke leek" in ontologie-engineering met sterke GRC-domeinkennis. Hij communiceert in het Nederlands, verwacht eerlijke pushback, geen diplomatieke omwegen. Formele Claude-toestemming verkregen maart 2026.

**Kernprincipe D9 — framework-neutraal:** alle normen/wetten/kaders zijn gelijkwaardig gemodelleerd; geen enkel framework heeft architecturaal privilege. BIO 2.0 is het operationele toepassings-perspectief voor dashboard + rapportage (verplichte Rijksoverheid-baseline), niet de architecturele kern. "Het model is het woordenboek (neutraal), het dashboard is het verhaal (perspectief)."

---

## §2. Project-architectuur — zeven chats

| Chat | Locatie | Rol | Doet wel | Doet niet |
|---|---|---|---|---|
| **Master** | claude.ai | Projectadviseur + GRC-architect | Strategie, sparring, architectuurbeslissingen, prioritering, scope-pauze-besluiten, eind-sign-off, sprint-instructies, **eigen commits + pushes voor docs/instructies (sinds 28-05)** | Geen Turtle/SPARQL, geen documenten, geen dashboard-code, **geen pushes naar `ontology/`** |
| **Technisch** | Claude Code | Ontologie-expert OWL/SPARQL/SHACL | Turtle, SPARQL, SHACL, reasoner-validatie, diagnostiek, patch-voorbereiding, applier-scripts, NEN-bron-lezing | Geen strategie, beleid, UI-code, geen autonome commits |
| **Documentatie** | claude.ai | Beleidsadviseur + schrijver | PID, managementcommunicatie, beleid (NL) | Geen ontologie-code, dashboard-code |
| **Dashboard** | Claude Code | Full-stack developer + visualisatie | HTML/JS dashboards, Cytoscape.js/Chart.js, SPARQL, export-scripts | Geen ontologie-wijzigingen, beleidsdocumenten |
| **Asset** | claude.ai | M18-specialist | M18 TBox, mappings, SHACL (afgerond; stand-by) | Geen wijzigingen andere modules |
| **Analyse** | claude.ai | Framework-analist + landschap-onderzoek | Externe frameworks analyseren, opties formuleren, landschap-onderzoek | Geen Turtle, geen architectuurbeslissingen, geen beleid |
| **Brein** | Claude Code | Brain-vault-onderhoud | Aanmaken/updaten brain__*-bestanden, cross-referentie-bewaking, autonoom bepalen welke bestanden bijwerken | Geen architectuurbeslissingen, geen ontologie-wijzigingen, geen beleid |

## §2a. Werkflow-wijziging 28-05-2026 — masterchat-push-permissie

Vastgesteld door Steven op 28-05-2026: **masterchat mag voortaan zelf committen + pushen** naar `stevenbouw/grc-kennismodel`. Eerder uitsluitend Steven.

**Scope van de regel:**
- Geldt voor masterchat-eigen deliverables: `docs/instructies/`, `docs/skos-beoordelings-protocol-*.md` (status-bumps), `docs/handovers/` indien gepushed.
- Geldt NIET voor `ontology/`, `grc-shacl.ttl`, scripts, dashboard-code — die wegen alleen via Tech/Dashboard met Steven's handmatige commit.
- **De subagent-invariant blijft hard:** Tech/Brein/Dashboard committen NOOIT zelfstandig. Steven inspecteert `git status` + `git diff` en commit handmatig voor hun werk.

**Compensatie voor wegvallen menselijke diff-gate op masterchat-pushes:** masterchat kondigt vóór elke push expliciet aan WAT er gepushed wordt en WAAROM. Steven kan op elk moment onderbreken. Voor contested calls (overrulen van specialist-voorkeur, of wijzigingen aan autoritatieve docs): expliciete bevestiging vragen vóór push.

**Documentatie-staat van deze regel** (debt, zie §12.2):
- Vastgelegd in brain-vault via Brein-cyclus iteratie 15 (`brain__workflow__*`)
- NOG NIET verwerkt in `docs/projectinstructie-v1_10.md` (§ZEVEN CHATS + gedeelde gedragsregels) — die noemt nog "Steven pusht" voor alles
- NOG NIET in volgend overdrachtsrapport-format
- NOG NIET in `docs/skos-beoordelings-protocol-v1_3.md` §7.3 (Steven's rol-beschrijving)

Bij projectinstructie v1.11-cut en volgend overdrachtsrapport gelijktrekken.

**Conform regel uit deze sessie:** instructies voor Analyse- en Documentatie-chats (claude.ai-only, geen repo-toegang) lopen voortaan **inline via masterchat**, niet via GitHub. Steven kopieert ze handmatig naar de doel-chat. Subagent-instructies (Tech/Brein/Dashboard in Claude Code) blijven WEL via repo, want die hebben directe file-toegang.

**Werkproces-schema (geactualiseerd):**

```
Subagent-werk:
  Masterchat → push instructie naar docs/instructies/ → Tech/Brein/Dashboard leest
  → uitvoeren + leveren → Steven inspecteert + commit handmatig → masterchat review

Analyse-/Documentatie-werk:
  Masterchat → inline prompt in chat → Steven kopieert naar claude.ai-doel-chat
  → uitvoeren + leveren → eventueel handmatig in repo

Master-overdracht (van masterchat naar volgende masterchat):
  Masterchat → inline overdrachtsrapport in chat → Steven gebruikt het bij start
  van nieuwe sessie (upload of paste)
```

---

## §3. Vastgestelde ontwerpbeslissingen — D1 t/m D12 + D4.1

Wijzigingen vereisen masterchat-goedkeuring. Geen D-wijzigingen sinds D4.1 (27 mei).

### §3.1 — D-decisions D1 t/m D12 (kort overzicht — ongewijzigd t.o.v. v4)

| ID | Beslissing | Status |
|---|---|---|
| D1 | OWL 2 DL profiel | Initieel |
| D2 | Turtle-serialisatie | Initieel |
| D3 | 11 namespaces (`fw:`, `ctrl:`, `bio:`, `risk:`, `roles:`, `compl:`, `isms:`, `biz:`, `ext:`, `asset:`, `csf:`) | Definitief sinds v4.5.0 |
| D4 | SKOS voor cross-framework mappings | Initieel; D4.1 toegevoegd 27-05-2026 |
| D5 | `owl:sameAs` strikt voor ctrl:↔bio: brug (93 paren) | Initieel |
| D6 | Tweetalige annotaties @nl/@en — meeliftregel | v4.1.0 |
| D7 | BIO 2.0 als twee klassen (BIOControl + OverheidsMaatregel) | Initieel |
| D8 | Eén canonieke SoA (isms:SoA_2026 + 93 SoAEntry_*) | v4.2.2 |
| D9 | Framework-neutraal model — alle kaders gelijkwaardig | 17-03-2026; bewijs verdiept v4.6.2 (T2), opnieuw bevestigd v4.6.3 (T3) |
| D10 | COSO ICF/ERM als enterprise-governance-laag | 17-03-2026 |
| D11 | `owl:sameAs` asset-convergentie — ster-patroon (5 bruggen) | 13-04-2026 |
| D12 | Drie-laags compliance-architectuur | 22-04-2026 |

**D9-bewijs-verdere verdieping (v4.6.3 / T3):** waar T2 cluster-discipline-convergentie aantoonde op homogene cross-framework-mapping (m10 ctrl↔NIS2-letter), heeft T3 het complement aangetoond — bij **heterogene** cross-category-relaties (control ↔ AVG-artikel) is `relatedMatch` de framework-neutrale basislijn, geen broadMatch-convergentie. Beide uitkomsten bewijzen D9: het framework dicteert niet de mapping-sterkte; de ontologische categorie-relatie wel.

### §3.2 — D4.1 — Disclaimer-handling bij autoritatieve mapping-bronnen (ongewijzigd t.o.v. v4)

Kern-regel onveranderd. **T3-relevantie:** D4.1 was bij T3 **niet van toepassing** — er bestaat geen ENISA-achtige autoritatieve cross-walk-disclaimer voor AVG↔ISO 27002. T3-beoordeling rustte op SKOS-semantiek-gronden + ISO 27701:2025 als evidence-keten, niet op disclaimer-logica. D4.1 bleef intact als regel voor toekomstige sprints waar wel disclaimers aanwezig zijn.

---

## §4. Sprint-protocollen 1-17 (operationeel in `docs/sprint-protocols.md` v1.3)

17 actieve protocollen, ongewijzigd qua aantal/structuur t.o.v. v4. Wat WEL veranderde sinds v4: een aantal protocollen is nu **deterministisch geborgd** via Tooling-01 hooks i.p.v. enkel proza-discipline.

| # | Protocol | Borging per 28-05-2026 |
|---|---|---|
| 1 | Pre-sprint-inventarisatie | Proza + skill `/pre-sprint-inventarisatie` (Tooling-03) |
| 2-9 | Pre-migratie-baseline (multi-module-discipline, bron-verificatie, ramings-baseline, etc.) | Proza |
| 10 | Patch-rapport §9 verplicht (geparkeerde-items-status) | Proza + skill `/patch-rapport` (Tooling-02) |
| 11 | Brain-vault-update na minor-release | Proza (Brein-cyclus) |
| 12 | Instructie-consistentie code-block versus toelichting | Proza |
| 13 | Bron-typo-beleid patroon-criterium | Proza + skill `report-structure` (path-scoped op `output/reports/*`, Tooling-02) |
| **14** | **Pre-push disclosure-check (5 categorieën)** | **Proza + hooks `secret-scan.py` + `disclosure-check.py` (Tooling-01) — automatisch op PreToolUse Write/Edit** |
| **15** | **Tech levert werkbare applier** | **Proza + skill `/applier-template` (Tooling-03) — canoniek template met dry-run/--apply/idempotentie** |
| **16** | **Lokatie verificatie-scripts in patch-rapport §9** | **Proza + skill `/patch-rapport` (Tooling-02) — enforced** |
| 17 | NEN-werkverdeling Tech-autonomie | Proza (lokale NEN-toegang in `/Users/stevenbouwmeester/grc-sources-licensed/`) |

**Protocol v1.3-werkflow-disciplines (§10.2-§10.5)** — sinds 28-05 FINAL (waren DRAFT in v4):

- §10.2 Bottom-up rapport-bouw verplicht — geborgd via skill `report-structure` + `/patch-rapport`
- §10.3 Interne tabel-consistentie-discipline — geborgd via skill `report-structure`
- §10.4 Helper-script-classificatie autoritatief — geborgd via skill `report-structure`
- §10.5 Metrics-tabel-scope-annotatie verplicht — geborgd via skill `report-structure` + `/patch-rapport`

---

## §5. SKOS-beoordelings-protocol — v1.3 is FINAL (CORRECTIE t.o.v. v4)

**Belangrijke wijziging t.o.v. v4:** v4 vermeldde "v1.3 DRAFT, vaststelling pending". Per 28-05-2026 (T3-scoping-moment) is **v1.3 vastgesteld als FINAL** door masterchat. v1.2 blijft autoritatief voor T2-historie; voorgangers blijven beschikbaar voor referentie.

### §5.1 — `docs/skos-beoordelings-protocol-v1_3.md` (FINAL)

Vastgesteld 28-05-2026 (T3-scoping). Bevat alle v1.2-inhoud + zeven verfijningen + de vier §10-werkflow-disciplines (zie §4). **Toepassings-bewijs:** Protocol v1.3 is op T3 operationeel toegepast op 31 m14-paren met succesvolle pilot (6/6 behoud bij masterchat-steer) en hoofd-uitvoering (29 behoud + 2 mutaties).

### §5.2 — Open opvolging — kandidaat v1.3.1 (post-T3)

**Cross-category-principe** (geboren uit T3, zie §11.12) is empirisch gevalideerd over alle 31 m14-paren maar nog **NIET formeel** in v1.3-protocol-tekst opgenomen. Brein-cyclus iteratie 15 heeft het principe als toepassings-precedent vastgelegd in `brain/brain__concepts__cross-category-mappings.md` met markering "kandidaat v1.3.1-precedent". Formele protocol-tekst-wijziging is masterchat-werk bij **volgende SKOS-sprint-scoping** (T4 of vergelijkbaar).

Het kandidaat-principe luidt: *"control ↔ legal-obligation = associatief (relatedMatch) als semantische basislijn; broad/narrowMatch alleen bij aantoonbare conceptuele subsumptie op paar-niveau, niet als cluster-default; closeMatch-uitzondering bij retrieval-interchangeability."*

---

## §6. NEN-bron-toegang voor Tech — 14 normen (ongewijzigd t.o.v. v4)

Locatie, lijst, en discipline-regels identiek aan v4 §6. T3 maakte operationeel gebruik van **ISO 27701:2025** (Annex D voor AVG↔27002-mapping) + **ISO 27002:2022** + selectief 27001:2022 — bevestigd dat de 28-05-uitbreiding (van 6 naar 14 normen) de juiste reikwijdte heeft voor m14-werk. Toekomstige cross-walks (m11 NIST, m17 COSO/COBIT) zullen mogelijk uitbreiding nodig hebben naar SP 800-53-bronnen en COSO-frameworks, beide niet-NEN dus niet onder dezelfde restrictie.

---

## §7. Actuele baseline — v4.6.3 (post-T3-patch)

**Patch-datum:** 28 mei 2026
**Aanleiding:** T3-sprint — 2 ctrl:↔compl:-mutaties in m14 (T3-001 + T3-002, beide broadMatch → relatedMatch, masterchat-besluit Optie C)

### §7.1 — Kerncijfers v4.6.3

| Metric | v4.6.3 | Δ vs v4.6.2 |
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
| — skos:closeMatch | 1.457 | 0 |
| — skos:broadMatch | **129** | **−2** |
| — skos:narrowMatch | 0 | 0 |
| — skos:relatedMatch | **194** | **+2** |
| owl:Nothing post-inf | 0 (consistent) | 0 |
| SHACL SECTIE A | 0 violations | 0 |
| SHACL SECTIE B | 0 violations | 0 |
| SHACL COMBINED | 290 (identiek aan v4.6.0-baseline) | 0 |

**T-sprint-patroon bevestigd**: T3 is opnieuw triple-neutraal (predicate-substitutie). Vier opeenvolgende T-sprints (T1+T2+T3) hebben SKOS-distributie gewijzigd zonder triple-Δ. H41 (SKOS-axioma-set-handling als architectuur-overweging) blijft active geparkeerd.

### §7.2 — Module-impact T3

Alleen `m14-avg-gdpr.ttl` gewijzigd in T3. Eindstand m14 compl→ctrl SKOS-distributie:

| Predicate | Vóór T3 | Na T3 |
|---|---:|---:|
| exactMatch | 0 | 0 |
| closeMatch | 2 | 2 (T3-014 Art32→5.01, T3-026 Art33→5.24) |
| broadMatch | 2 | **0** |
| narrowMatch | 0 | 0 |
| relatedMatch | 27 | **29** |

m14 totaal compl→ctrl ongewijzigd (31 paren). 21 andere modules + `grc-shacl.ttl`: hash ongewijzigd sinds v4.6.0.

### §7.3 — H36 status: FULLY CLOSED

- m10 via T1+T2: 118 ctrl→compl-paren convergeren naar broadMatch (✓)
- m14 via T3: 31 compl→ctrl-paren in een 2 close / 0 broad / 29 related-eindstand met cross-category-rationale (✓)

H36 is daarmee in zijn geheel afgesloten. Geen open SKOS-exactMatch-audit-werk meer.

---

## §8. Recente sessies-overzicht (UITGEBREID t.o.v. v4)

### §8.1 — 26-27 mei 2026: migratie + T1 + Brein 13 + T2 + Brein 14 + Optie C

Volledig beschreven in v4 §8.1-§8.4. Niets veranderd aan die context.

### §8.2 — 28 mei 2026 ochtend: T3-pre-sprint-inventarisatie (door Tech)

Tech-subagent leverde `output/reports/t3-pre-sprint-inventarisatie.md` op (status: final-awaiting-masterchat-review):

- **Scope bevestigd**: 31 compl→ctrl-paren in m14 (2 close + 2 broad + 27 related).
- **0 scope-pauze-triggers**.
- **Evidence-strategie**: ISO 27701:2025 Annex D + Annex F als twee-staps-keten (10× niveau-1, 7× niveau-2, 14× niveau-3).
- **Protocol-aanbeveling**: v1.2/v1.3 toereikend; geen v1.4 nodig.
- **Pilot-sample voorgesteld**: 6 paren (T3-002, T3-014, T3-024, T3-008, T3-028, T3-031).

### §8.3 — 28 mei 2026 middag: T3 pilot + Optie C-besluit (KERN-SESSIE)

**Masterchat-review van T3-inventarisatie:**

1. **Protocol-beslissing**: v1.3 vastgesteld als FINAL (geen v1.4 — premature formalisering vermijden). Push van DRAFT→FINAL-status-bump in `docs/skos-beoordelings-protocol-v1_3.md`. Bindende T3-methode-steer meegegeven (kandidaat v1.3.1-precedentnotitie post-sprint): semantische basislijn voor m14 is `relatedMatch`; cluster-cardinaliteit is een signaal, geen mandaat; broad/narrow alleen bij aantoonbare subsumptie op paar-niveau.
2. **Pilot-instructie**: gepushed naar `docs/instructies/instructie-t3-pilot.md`. 6 paren, READ-ONLY analyse, geen patch. Specifieke focus op T3-014 (closeMatch-toets) en T3-024 (cluster-default-test).

**Tech-pilot-uitkomst**: 0 mutaties / 6 behoud op alle 6 paren — bevestiging dat de cross-category-steer hield. Tech rapporteerde een methodische escalatievraag op T3-001 + T3-002 (de twee broadMatch-paren in compl→ctrl-richting): formeel SKOS-omgekeerd ("control breder dan AVG-artikel"). Tech's voorkeur: Optie B (richtings-correctie naar narrowMatch). Optie C (downgrade naar relatedMatch) als alternatief.

**Masterchat-besluit op escalatie**: **Optie C, overrulend Tech's Optie B**. Onderbouwing:
- Tech's eigen cross-category-rationale (§3.3, §4.1 van pilot-rapport) classificeert narrowMatch tussen control en legal-obligation als "categorie-fout in de meeste gevallen". Optie B contradiceert die rationale.
- Geen principieel onderscheid tussen 5.01/5.12 (broadMatch) en 5 zuster-controls onder Art5_1f (relatedMatch). Vermoedelijk oorspronkelijke inconsistentie, geen bewuste keuze.
- Optie C herstelt cluster-consistentie binnen Art5_1f én lost de richtings-kwestie definitief op (`relatedMatch` is symmetrisch).
- Tech's tegenargument ("verliest sterkte-signaal") houdt niet: het echte sterkte-signaal zit in closeMatch (T3-014, T3-026), niet in mis-getypeerde broad/narrow.

m10 en andere modules niet heropend (m10-broadMatch is formeel correct; geen retroactieve audit).

### §8.4 — 28 mei 2026 middag: T3 Stap 3 + patch v4.6.3

**Masterchat-instructie Stap 3** gepusht (`docs/instructies/instructie-t3-stap3.md`): 25 resterende paren beoordelen onder cross-category-rationale; T3-001 muteren naar relatedMatch (T3-002 reeds via pilot-besluit); patch naar v4.6.3.

**Tech-eindrapport Stap 3**:
- 25 resterende paren beoordeeld; alle behoud (24× relatedMatch, 1× closeMatch T3-026)
- Patch v4.6.3 toegepast: 2 mutaties (T3-001 + T3-002 broadMatch → relatedMatch)
- Canonical metrics + SHACL: 17/17 prognose-criteria match exact
- 15/15 GO-criteria groen

**Sign-off bij masterchat-review**: GO op de patch, maar één **errata-vondst** in de confidence-tally:
- §6.1 per-paar-tabel (bron-van-waarheid per Protocol v1.3 §10.4) geeft 27 hoog / 4 middel / 0 laag
- §6.3 duplicaat-tabel gaf foutief 20/11
- §6.4 (door Tech als bron-van-waarheid gemarkeerd) gaf 26/5 — off-by-one omdat T3-002 nog als pilot-middel werd geteld, terwijl §6.1 hem post-besluit terecht op hoog had gezet
- Dezelfde fout was meegelift naar patch-rapport §6.4

Errata-correctie naar Brein-cyclus iteratie 15 gedelegeerd (zie §8.5).

### §8.5 — 28 mei 2026 avond: Brein-cyclus iteratie 15 (T3-close)

**Brein-instructie** gepusht (`docs/instructies/instructie-t3-brein-cyclus.md`) met vier delen:

- **Deel A — Errata-correctie**: surgische edits in Claude Code op eindrapport + patch-rapport. Correcte stand 27/4/0 met §6.1 als bron-van-waarheid. Errata-blok per rapport met verwijzing naar masterchat-sign-off. T-historie bewaard (geen herschrijven van §-detail).
- **Deel B — Brain-vault T3-close**: sprint-record `brain__sprints__T3-skos-bidirectional-audit-m14.md` (NIEUW), sprint-register update, D04-decision update (cross-category-precedent toegevoegd; D4.1 inactief in T3 als feit vastgelegd), H36 → fully-closed, H39 T3-bevestiging, M14-module update, log + index, baseline → v4.6.3.
- **Deel C — Cross-category-principe**: NIEUW concept-bestand `brain/brain__concepts__cross-category-mappings.md`, expliciet gemarkeerd als kandidaat v1.3.1-precedent. Niet formaliseren — dat is masterchat-werk.
- **Deel D — Workflow-record**: brain-vault-record van masterchat-push-permissie (28-05-2026). Onveranderd dat subagent-invariant hard blijft. Prozaregels in projectinstructie/overdrachtsrapport gemarkeerd als volgende-versie-cut, NIET Brein-taak.

Brein iteratie 15 afgesloten. Brain-vault per 28-05-2026 avond: ~125 bestanden.

### §8.6 — 28 mei 2026 avond: Tooling-track 01+02+03 (NIEUWE TRAJECT)

Op verzoek van Steven na inhoudelijke beoordeling van het **extensie-landschap-rapport** (zie §8.7) is een gefaseerde tooling-track uitgevoerd om de protocol-discipline van proza naar deterministisch te tillen. **§0.5-firewall hard ingebouwd**: géén autonomie-bouw, géén green-gates, géén commit-block-met-sunset, géén agent-teams. De track maakt bestaande discipline harder onder het huidige mens-commit-regime.

**Tooling-01 (commit `3fb1da0`):**

- **Permissions** in `.claude/settings.json`: hard `deny` op `Bash(git commit:*)` + `Bash(git push:*)` voor subagents (codificering van "subagents committen NOOIT zelfstandig"); `ask` op destructieve git-acties; `allow` op read-only + `python3`.
- **Vier defensieve hooks** in `.claude/hooks/`: `secret-scan.py` (PreToolUse, detecteert PAT/tokens/API-keys/PEM/JWT — directe les uit het PAT-incident), `disclosure-check.py` + `disclosure-config.json` (PreToolUse, Protocol 14 categorieën 1-4 deterministisch; categorie 5 NEN-tekst >10 woorden blijft handmatig), `versie-suffix-check.py` (PostToolUse, warn-only op output-naming), `sessionstart-context.sh` (SessionStart, injecteert log-tail + git status).
- **Twee verificatie-skills**: `.claude/skills/canonical-metrics/SKILL.md` (codificeert OWL-RL-instellingen + 6 invariantie-metrics + "§0 uit JSON"-leerpunt v4.3.3) en `.claude/skills/shacl-split/SKILL.md` (codificeert SECTIE A/B/COMBINED + 290 false-positives als OWA/CWA-fenomeen).
- 10/10 hook-tests groen. Ontologie ongewijzigd v4.6.3-baseline.

**Tooling-02 (commits `053e260` reeks):**

- **CLAUDE.md afgeslankt** van 293 → 168 regels (−43%). Always-on-invarianten **NETTO VERSTERKT**: drie eerder-impliciete (NEN-parafrase, status-discipline, BBN-correctie) zijn nu expliciet, plus "subagents committen NOOIT zelfstandig" als zevende invariant, plus expliciet aan `.claude/settings.json`-deny gekoppeld. Karpathy LLM-Wiki drie-lagen-pattern, repo-boom-detail, brain-organisatie-tabel, Operations-pattern-detail, skills-ecosystem-positionering, optional tooling: verplaatst naar `.claude/skills/repo-reference/SKILL.md` (description-triggered).
- **Pre-step Deel D — disclosure-config refactor**: Tech vond bij start een latente bug — `disclosure-config.json` was invalide JSON, bevatte de echte organisatienaam in een *versioned* bestand, én Steven stond niet in `allowed_persons` (zou hem zelf hebben geblokkeerd). Scope-pauze gehouden, Steven gaf go, gefixt. Alle org/persoon/allowed-velden naar lege arrays; werkelijke waarden naar gitignored `.local.json`. Organisatie-neutraliteit-invariant geborgd. 4/4 tests groen.
- **A.0 pre-check**: `.claude/rules/` met `paths`-frontmatter NIET ondersteund in actuele Claude Code (geverifieerd via officiële docs). Fallback toegepast per stop-conditie: skills met `paths`-frontmatter als officieel mechanisme.
- **Drie path-scoped + reference skills**: `repo-reference` (description-triggered, 187 regels), `ontology-conformance` (`paths: ontology/*.ttl`, 78 regels, D1-D12+D4.1-checklist), `report-structure` (`paths: output/reports/*`, 119 regels, Protocol 13 + Protocol v1.3 §10.2-§10.5).
- **Action-skill `/patch-rapport`**: 259 regels, canoniek §0-§15-skelet, afgedwongen §0-uit-JSON + §9 Protocol 16 + §12 D-conformance + scope-annotaties. Trigger-test tegen v4.6.3-baseline: 16/16 sectie-match + 8/8 cijfer-match + 3/3 SHACL-match.
- Hook live-validatie: disclosure-check blokkeerde Tech's eerste rapport-versie op verbatim organisatie-aanduidingen in een test-tabel. Geanonimiseerd. Productie-validatie van Tooling-01.

**Tooling-03 (commit `e1f0d4d` reeks):**

- **Skill `/pre-sprint-inventarisatie`** (Protocol 1): 225 regels, canoniek §0-§9-skelet. Afgedwongen: §2 uit `canonical_metrics_v(Y-1).json`, §3+§4 metrics-scope-annotatie, §6 geen pre-pilot-uitkomst-classificatie, §1 "INITIEEL — TE BEVESTIGEN" bij bottom-up. Mapping-tabel skill-§ ↔ T2/T3-precedent vraag-A-F-format (slimme bridging zonder scope-pauze). Trigger-test tegen T3-precedent: 5/5 groen.
- **Skill `/applier-template`** (Protocol 15, optioneel maar gebouwd): 191 regels, canoniek Python-skelet met dry-run + `--apply` + backup + MUTATIONS-list + integratie-test + idempotentie-check + faal-veilig-exit + per-mutatie-logging. **Toegevoegde waarde boven T3-precedent**: expliciete `ALREADY APPLIED`-detectie (Protocol-15 strict enforcement). Trigger-test 4/4 groen.
- Hook live-validatie #2: disclosure-check blokkeerde Tech's rapport op een `/Users/...`-pad-illustratie. Geanonimiseerd. Tweede productie-validatie.

**Masterchat-besluiten genomen tijdens de tooling-track:**

1. **Sectie-naam-strategie** (Tooling-03 §1.2 observatie): vanaf T4-instructies gebruikt masterchat de **skill-§-naamgeving** (§0-§9) als canonieke structuur; sprint-specifieke vraag-thema's mogen, maar als inner lens binnen §-secties, niet als vervangend top-level format.
2. **Tooling-04 `/pilot-rapport` + `/brein-cyclus`-skills**: kandidaat, niet gebouwd. YAGNI tot eerstvolgende T-sprint dit feitelijk triggert.

### §8.7 — 28 mei avond: dashboard-landschap-analyse opgesteld (nieuwe Analyse-opdracht)

Tijdens de tooling-afronding heeft Steven gevraagd of het **extensie-landschap-rapport** (`output/reports/extensie-landschap-claude-2026-05-28-3.md`, ~100 KB, geschreven door eerdere Analyse-chat) ook dashboard-toepassingen bevat. Eerlijke beoordeling: **nee, dashboard was structureel onder-belicht** in dat rapport. De D-skill-aanbevelingen waren ontologie-/verificatie-/protocol-gericht; dashboard kwam slechts indirect via Anthropic-native `frontend-design`. Tooling-track 01-03 heeft Tech-/protocol-discipline gedekt, niet dashboard-discipline.

**Verheldering bij Steven**: Dashboard-pijplijn-situatie is anders dan eerder projectgeheugen suggereerde:
- `grc-explorer` (Spoor A, in repo) staat op v4.6.0; Dashboard-chat heeft op v4.6.0 geleverd. T1/T2/T3 raakten alleen SKOS-distributie, geen render-relevante wijzigingen — **geen acute inhaalslag-druk**.
- `grc-dashboard` (Spoor B, lokaal/buiten repo) staat sinds v3 stil. Wordt feitelijk green-field-werk wanneer T&I-lab-test start.
- Steven wil **twee aparte producten** (geen samenvoeging), met latere koppeling.

**Dashboard-landschap-analyse-prompt opgesteld** (door masterchat, voor Analyse-chat) met drie sub-vragen:
1. **Spoor A** incrementele verbetering (probleem-eerst-inventarisatie, vragen-stellen-modus, oplossings-laag)
2. **Spoor B** green-field architectuur-overwegingen (CLAUDE.md-specs als richtinggevend kritisch beoordelen)
3. **Spoor A↔B-koppeling** denkwerk-laag (patronen + voor/nadelen + niet-aanbevolen patronen)

Met expliciete **probleem-eerst-discipline** + **vragen-mogen-terugleggen-modus** (Analyse-chat MAG via Steven vragen aan Dashboard-chat of masterchat voorleggen) + **vragen-bijlage** als verplicht rapport-onderdeel.

**Status van de prompt**: opgesteld, kort in repo geweest (`docs/instructies/analyse-prompt-dashboard-landschap.md`), op verzoek van Steven verwijderd uit repo en lokaal door Steven bewaard. **Voortaan werkflowregel**: analyse-/documentatie-instructies inline in masterchat, niet via repo (subagent-instructies blijven WEL via repo). Zie §2a.

De Analyse-chat is op moment van dit overdrachtsrapport **NOG NIET geopend** met deze prompt. Steven beslist wanneer.

### §8.8 — 28 mei 2026 avond: skill-evaluaties + extensie-landschap-rapport (referentie)

In repo aanwezig en autoritatief beschikbaar:

- `output/reports/skill-eval-tier1-tier2-2026-05-27.md` — vier kandidaat-skills met GO/HOLD/NO-GO (Sushegaad, GRCEngClub, open-ontologies, kfchou)
- `output/reports/extensie-landschap-claude-2026-05-28-3.md` — uitputtende landschap-analyse (~100 KB)

Beide blijven referentiemateriaal voor skill-/MCP-besluiten. Nieuwe masterchat: raadpleeg via GitHub-MCP indien relevant.

---

## §9. Brain-vault — primaire kennisbron

**Structuur:** flat bestanden in `brain/`-folder met `__`-separator voor folder-encoding (decisions, sprints, architecture, concepts, modules, sources, workflow, scope).

**Entry-points:** `brain/brain__index.md`, `brain/brain__log.md`, folder-registers.

**Iteratie-stand** per 28-05-2026 avond: **iteratie 15 afgesloten** (T3-close), brain-vault ~125 bestanden.

**Nieuwe brain-bestanden sinds v4** (incompleet, raadpleeg `brain__log.md` voor volledig overzicht):
- `brain__sprints__T3-skos-bidirectional-audit-m14.md`
- `brain__concepts__cross-category-mappings.md` (kandidaat v1.3.1-precedent)
- Workflow-record over masterchat-push-permissie 28-05

**Conventie ongewijzigd**: bij vragen over projecthistorie, architectuur of conventies → raadpleeg brain-vault via GitHub-MCP vóór andere bronnen.

---

## §10. Sprint-architectuur en huidige toestand

### §10.1 — Vijf doelen + drie sporen (ongewijzigd t.o.v. v4)

| Spoor | Status |
|---|---|
| A — Technische ontologie-opbouw | Voltooid t/m v4.6.3 voor Fase 1-4 + T1+T2+T3. **Kwaliteitsanalyse-fase voltooid voor m10 + m14**. H36 closed. |
| B — Organisatiespecifieke invulling | Pending; T&I-lab-test gepland. Dashboard-architectuur-overwegingen open (zie §12.1). |
| C — Gebruik en governance | Pending; explorer op v4.6.0 (Spoor A); dashboard sinds v3 stil (Spoor B). Geen acute druk omdat T-sprints triple-neutraal zijn. |

### §10.2 — Sprint-historie (UITGEBREID met T3 + Tooling-track)

| Sprint | Datum | Scope | Status |
|---|---|---|---|
| v4.6.0 | 21-05-2026 | Fase 4 — ENSIA + volwassenheidsmodel + CSF Tiers | Afgerond |
| Migratie | 26-05-2026 | Tech/Brein/Dashboard naar Claude Code + GitHub | Afgerond |
| T1 | 26-05-2026 | SKOS Fase 1 — H36 m10-cluster (28 paren) | Afgerond — patch v4.6.1 |
| Brein 13 + mini-revisies | 27-05-2026 | T1-afronding + D4.1 + Protocol 17 + protocol-draft | Afgerond |
| T2 | 27-05-2026 | SKOS Fase 2 — m10 bidirectional (118 paren, 65 mutaties) | Afgerond — patch v4.6.2 |
| Brein 14 + Optie C | 27/28-05 | T2-afronding + Protocol v1.3-draft + projectinstructie v1.10 + README v4.6.2 | Afgerond |
| **T3** | **28-05-2026** | **SKOS Fase 3 — m14 AVG/GDPR (31 paren, compl→ctrl, 2 mutaties)** | **Afgerond — patch v4.6.3** |
| **Brein 15** | **28-05-2026** | **T3-close + errata + cross-category-precedent + workflow-record** | **Afgerond** |
| **Tooling-01** | **28-05-2026** | **`.claude/`-hooks + permissions + verificatie-skills** | **Afgerond** |
| **Tooling-02** | **28-05-2026** | **CLAUDE.md afslanken + path-scoped skills + /patch-rapport** | **Afgerond** |
| **Tooling-03** | **28-05-2026** | **`/pre-sprint-inventarisatie` + `/applier-template`** | **Afgerond** |

**Geen actieve sprint per 28-05-2026 avond.**

### §10.3 — Tooling-laag overzicht (NIEUW, §14 voor detail)

| Laag | Inhoud |
|---|---|
| Hooks | `secret-scan`, `disclosure-check` (cat 1-4), `versie-suffix-check`, `sessionstart-context` |
| Permissions | Hard deny `git commit/push` voor subagents; `ask` destructieve git; `allow` read-only + python3 |
| Path-scoped skills | `ontology-conformance` (`ontology/*.ttl`), `report-structure` (`output/reports/*`) |
| Reference-skill | `repo-reference` (description-triggered, Karpathy + architectuur + optional tooling) |
| Action-skills | `/canonical-metrics`, `/shacl-split`, `/patch-rapport`, `/pre-sprint-inventarisatie`, `/applier-template` |
| Config | `.claude/settings.json`, `.claude/hooks/disclosure-config.json` (versioned, org-neutraal) + `.local.json` (gitignored) |

---

## §11. Werkflow-leerpunten — kritiek voor toekomstige sprints

Ongewijzigd t.o.v. v4: §11.1-§11.11. Aangevuld met:

### §11.12 — Cross-category-principe (T3-leerpunt, kandidaat v1.3.1)

Bij SKOS-mappings tussen ontologisch verschillende categorieën (control ↔ legal-obligation, control ↔ principe) is **`relatedMatch` de semantische basislijn**, niet broad/narrowMatch. Cluster-cardinaliteit is een signaal, géén mandaat voor cluster-default-subsumptie. broad/narrowMatch alleen bij aantoonbare conceptuele subsumptie op paar-niveau; closeMatch bij retrieval-interchangeability.

Empirisch gevalideerd op alle 31 m14-paren in T3. Vastgelegd als brain-vault-precedent (`brain__concepts__cross-category-mappings.md`). Formele protocol-tekst-wijziging (v1.3.1) is masterchat-werk bij volgende SKOS-sprint-scoping.

**m10-versus-m14-onderscheid voor toekomstige sprints**: m10 (control ↔ NIS2-art.21-letter) is binnen-categorie-cross-walk (beide zijn measure-categorieën); subsumptie via broadMatch is daar genuiene genus-species. m14 (control ↔ AVG-artikel) is cross-category (control vs legal duty); subsumptie is daar categorie-fout, associatief is correct.

### §11.13 — Masterchat-push-discipline (sinds 28-05-2026)

Met masterchat-push-permissie verdwijnt Steven's diff-gate op masterchat-eigen pushes. Compenserend gedrag:

- Vóór elke push expliciet aankondigen WAT en WAAROM
- Bij contested calls (overrulen van specialist-voorkeur, autoritatieve docs): expliciete bevestiging vragen
- Géén pushes naar `ontology/`, `grc-shacl.ttl`, scripts/dashboard-code — die blijven Tech/Dashboard + Steven's commit
- Bij grote bestanden (>200 regels): bij voorkeur surgische edit door Tech/Brein in Claude Code i.p.v. full-file-rewrite via MCP (corruptie-risico)

### §11.14 — Sign-off-discipline op rapporten (T3-leerpunt)

Bij eindrapporten een interne tabel-consistentie-check uitvoeren (Protocol v1.3 §10.3). T3-eindrapport had een confidence-tally die in §6.3, §6.4 en §6.1 onderling verschilde. Masterchat-sign-off ving het op; Brein-cyclus deed errata-correctie. Voortaan: bij elke sign-off expliciet de §-cross-consistentie checken, niet alleen de §0-cijfers.

### §11.15 — Tooling-track-leerpunt: §0.5-firewall in skill-tekst inbouwen

Tooling-03 toonde dat het opnemen van de §0.5-firewall expliciet in de skill-tekst zelf (in plaats van alleen in de instructie) één laag dieper veiligheid biedt — toekomstige aanroepingen van de skill exposen de firewall opnieuw. Patroon voor alle toekomstige zelf-gebouwde skills die proza-discipline mechaniseren.

---

## §12. Open punten en roadmap

### §12.1 — Volgende voorgenomen activiteit — Steven kiest

**Geen actieve sprint.** Masterchat-eerstvolgende-actie hangt af van Steven's prioriteits-keuze tussen meerdere richtingen:

| Kandidaat | Reden om nu te doen | Effort |
|---|---|---|
| **A. Dashboard-landschap-analyse via Analyse-chat** | Dashboard structureel onder-belicht in eerdere analyse; prompt klaar (zie §8.7); Steven bewaart 'm lokaal; vraagt vragen-terugleggen-modus aan Steven | Steven-initiatief (open Analyse-chat) + meerdere rondes vraag/antwoord met Dashboard-chat |
| **B. D.7 GRC-domein-skill bouwen** | Mijn voorkeur uit extensie-rapport — daadwerkelijk unieke lacune (NL-kaders: BIO/VIR/VIRBI/CBW/Cbb/ENSIA/COSO/COBIT/BVA/CIO-stelsel); nu pas goed bouwbaar dankzij Tooling-01-03 fundament | Substantieel — eigen Tech-sprint met NEN-discipline-discipline |
| **C. T4 ontology-sprint** | H33 (m11 NIST SP 800-53 substantiële uitbreiding), H34 (enhancement-modellering), m17 COSO/COBIT, m09 ISO 27001:2022, of m16 VIRBI | Per kandidaat verschillend — masterchat-scope-besluit nodig |
| **D. Open-ontologies-evaluatie** (H37+H38+H41) | Losse evaluatie-sprint, geen migratie-besluit; raakt drie geparkeerde H-items tegelijk; tableaux OWL2-DL als test | Beperkt — evaluatie, geen bouw |
| **E. Documentatie-debt afwerken** | Projectinstructie v1.11 (push-permissie + v4.6.3 + H36-closed + Tooling-laag), volgend overdrachtsrapport-template, README v4.6.3 | Bij masterchat in claude.ai (proza-werk), gefaseerd |
| **F. §0.5 autonomie-koers verankeren** | Parked door Steven; wanneer hij eraan toe is. Vereist formeel D-/scope-besluit | Substantieel; raakt visie-invariant |
| **G. Tooling-04 `/pilot-rapport` + `/brein-cyclus`** | YAGNI-positie; bouw bij eerstvolgende T-sprint die het triggert | Klein indien gewenst |

Mijn voorkeur bij gelijke prioriteiten: **A** (dashboard-analyse) eerst, want het opent het laatste structureel onder-belichte domein en is een Analyse-chat-deliverable (geen masterchat-bouwwerk). Daarna **B** (D.7) als grote bouw. Maar dit is Steven's keuze.

### §12.2 — Documentatie-debt (groeiend, niet urgent)

Lopende achterstand tussen praktijk en governance-documenten:

| Document | Wat moet bij | Trigger voor update |
|---|---|---|
| `docs/projectinstructie-v1_10.md` | Push-permissie, v4.6.3-baseline, H36-fully-closed, Tooling-01-03-realisaties, cross-category-principe, Protocol v1.3 FINAL | Cut naar v1.11 — masterchat-werk in claude.ai |
| `docs/handovers/sessie-rapport-overdracht-masterchat-v4.md` | Volledig vervangen door dit document (v5) | Bij volgend overdrachts-moment (niet retroactief v4 wijzigen) |
| `docs/skos-beoordelings-protocol-v1_3.md` §7.3 | Werkverdeling-tabel: Steven's rol + masterchat-push-permissie | Bij eerstvolgende protocol-update |
| `README.md` (v1.8/v4.5.0) | v4.6.3-baseline, Tooling-laag, H36-closed | Lage prioriteit; bij eerstvolgende `README`-touch |

Niet urgent. Geen actieve werkstroom geblokkeerd. Wel groeiend.

### §12.3 — Bewust geparkeerd (geen urgentie)

| Item | Type | Trigger |
|---|---|---|
| H36 (m10 + m14-component) | **CLOSED** (sinds T3) | — |
| H37 — open-ontologies MCP | Architectuur | Evaluatie-sprint (kandidaat D) |
| H38 — OWL RL vs HermiT-equivalentie | Architectuur | Idem |
| H41 — SKOS-axioma-set-handling | Architectuur | Idem |
| H39 — 290 SHACL false-positives uitsplitsen | Hygiëne | Rustige sprint of SHACL-shapes-wijziging |
| H40 — Dashboard-UI-renderdekking | UX | Dashboard-landschap-analyse (kandidaat A) zou hier richting moeten geven |
| H33 — m11 SP 800-53 uitbreiding | Inhoudelijk | T4-kandidaat |
| H34 — m11 enhancement-modellering | Inhoudelijk | Serieuze SP 800-53-toepassing |
| H25/H26/H27/H32/H35 | Per H-register | Per-item triggers |
| H15 (governance-graafdekking) / H21 (implicit individuals) | Architectuur | Spoor B / consistentie-keuze |
| Dashboard-inhaalslag | Spoor C | Dashboard-landschap-analyse-uitkomst stuurt dit |
| 39-edge SKOS-discrepantie (v4.6.0-migratie) | Hygiëne | Niet-blokkerend; bij dashboard-touch hermeten tegen v4.6.3 |
| Skill-installaties (Sushegaad/GRCEngClub/open-ontologies/kfchou) | Tooling | Per skill-evaluatie-recommendaties |
| Cross-category-principe v1.3.1-formalisering | Protocol | Volgende SKOS-sprint-scoping |

---

## §13. Wat de nieuwe masterchat NIET moet doen

- **Geen autonome bash/git/edit-acties** binnen claude.ai-context (geen tools); wel pushes via GitHub-MCP voor masterchat-eigen deliverables in `docs/instructies/` etc.
- **Geen pushes naar `ontology/`, `grc-shacl.ttl`, scripts of dashboard-code** — die hebben specialistische subagent-route + Steven's commit
- **Geen scope-uitbreidingen zonder Steven-akkoord** — bij ambiguïteit scope-pauze met Optie A/B/C-rapport
- **Geen wijziging aan D-decisions** (D1-D12 + D4.1) zonder expliciete judgement-cyclus
- **Geen wijziging aan sprint-protocollen 1-17** zonder grondige aanleiding
- **Geen formele v1.3.1-formalisering van cross-category-principe** zonder eerst de volgende SKOS-sprint-scoping af te wachten (precedent ligt al in brain; tekst-wijziging is bewust uitgesteld)
- **Geen autonomie-koers-formalisering** zonder dat Steven expliciet de §0.5-verankering vraagt
- **Geen organisatie-naam noemen** — altijd "de organisatie" of "Rijksoverheidsorganisatie"
- **Geen NEN-verbatim-tekst** in welke output dan ook
- **Geen Analyse-/Documentatie-instructies via repo** — die gaan inline (zie §2a)
- **Geen herinrichting brain-vault**
- **Geen skill-installatie-beslissingen namens Steven** — masterchat evalueert; Steven installeert in Claude Code

---

## §14. Tooling-status (UITGEBREID — `.claude`-laag operationeel)

### §14.1 — Repository en infrastructure (ongewijzigd t.o.v. v4)

| Tooling | Status | Locatie/configuratie |
|---|---|---|
| GitHub-MCP voor claude.ai | Werkend | `stevenbouw/grc-kennismodel`, privé |
| Claude Code in VS Code | Geauthenticeerd, actief | Tech/Brein/Dashboard-subagents |
| `CLAUDE.md` | v1.6 (Tooling-02-herstructurering) | Repo-root, 168 regels, 7 invarianten expliciet |
| Subagent-configs | Actief, ongewijzigd | `.claude/agents/tech.md`, `brein.md`, `dashboard.md` |
| `docs/sprint-protocols.md` | v1.3, 17 protocollen + v1.3-werkflow-disciplines | Repo |
| OWL RL reasoning | `axiomatic_triples=False`, `datatype_axioms=False` | Standaard-instellingen |
| pySHACL | Gesplitste validatie (SECTIE A + B + COMBINED) | Standaard-instellingen |
| Protégé | Stand-by — geen HermiT-rerun sinds v4.0.0 | Mac, lokaal |
| Cytoscape.js | `grc-explorer-v4_6_0.html` (Spoor A) | Op v4.6.0; geen acute druk |
| Lokale NEN-bronnen | 14 normen | `/Users/stevenbouwmeester/grc-sources-licensed/` |

### §14.2 — `.claude/`-laag (NIEUW, sinds Tooling-01-03)

| Categorie | Bestand | Functie |
|---|---|---|
| **Config** | `.claude/settings.json` | Permissions (deny git-commit/push voor subagents; ask destructief; allow read-only + python3) + hooks-config |
| **Config** | `.claude/hooks/disclosure-config.json` | Versioned, org-neutraal (lege placeholder-arrays + scan_scopes) |
| **Config** | `.claude/hooks/disclosure-config.local.json` | Gitignored — Steven's werkelijke org-/persoon-waarden (lokaal). Voorbeeld in `.local.json.example` (versioned, 7-velden-template) |
| **Hook** | `.claude/hooks/secret-scan.py` | PreToolUse Write/Edit — detecteert PAT/tokens/keys/PEM/JWT/AWS-id |
| **Hook** | `.claude/hooks/disclosure-check.py` | PreToolUse Write/Edit — Protocol 14 cat 1-4 deterministisch |
| **Hook** | `.claude/hooks/versie-suffix-check.py` | PostToolUse Write — warn-only op output-naming |
| **Hook** | `.claude/hooks/sessionstart-context.sh` | SessionStart — log-tail + git status + git log -5 |
| **Action-skill** | `.claude/skills/canonical-metrics/SKILL.md` | OWL-RL-meet-procedure + 6 invariantie-metrics |
| **Action-skill** | `.claude/skills/shacl-split/SKILL.md` | SECTIE A/B/COMBINED-validatie |
| **Action-skill** | `.claude/skills/patch-rapport/SKILL.md` | §0-§15-skelet voor patch-rapporten met afgedwongen disciplines |
| **Action-skill** | `.claude/skills/pre-sprint-inventarisatie/SKILL.md` | §0-§9-skelet voor pre-sprint-inventarisaties (Protocol 1) |
| **Action-skill** | `.claude/skills/applier-template/SKILL.md` | Python-applier-template met Protocol 15-discipline |
| **Reference-skill** | `.claude/skills/repo-reference/SKILL.md` | Description-triggered — Karpathy + repo-boom + architectuur + optional tooling |
| **Path-scoped skill** | `.claude/skills/ontology-conformance/SKILL.md` | `paths: ontology/*.ttl` — D1-D12 + D4.1-checklist |
| **Path-scoped skill** | `.claude/skills/report-structure/SKILL.md` | `paths: output/reports/*` — Protocol 13 + Protocol v1.3 §10.2-§10.5 |

**Operationele opmerkingen:**
- Hooks zijn live-gevalideerd: disclosure-check heeft tijdens Tooling-02 en Tooling-03 daadwerkelijk twee blokkades uitgevoerd op rapport-content (verbatim org-aanduidingen + `/Users/...`-pad-illustratie). Bewezen werking onder productie-condities.
- `.claude/rules/` met `paths`-frontmatter: NIET ondersteund in actuele Claude Code (geverifieerd). Path-scoped skills via skill-frontmatter zijn het officiële mechanisme.
- Steven moet `disclosure-config.local.json` zelf maken vanuit `.example` om cat1/2/4-detectie te activeren met productie-waarden. Cat3 (paden) werkt altijd via versioned `allowed_local_path_prefixes` (in lokale config, niet meer versioned na Tooling-02 Deel D).

### §14.3 — Wat Tooling-04 zou kunnen worden (kandidaat, niet gepland)

- `/pilot-rapport`-skill (T2+T3 valideren het patroon) — bouw bij eerstvolgende T-sprint
- `/brein-cyclus`-skill — bouw bij eerstvolgende minor-release waar Brein moet draaien
- Per-subagent path-context-aware hook (5e hook) — alleen bij incident dat het rechtvaardigt; YAGNI nu
- Categorie-5 (NEN-tekst >10 woorden) als semi-deterministische hook — alleen bij groei NEN-werk

---

## §15. Wat Steven moet uploaden naar nieuwe masterchat

### §15.1 — Primair (verplicht)

**Dit document** (`sessie-rapport-overdracht-masterchat-v5.md`). Zelfstandige basis.

### §15.2 — Secundair (aanbevolen, niet kritisch)

| Bestand | Waarom |
|---|---|
| `output/reports/patch-rapport-v4_6_3.md` (uit repo) | Volledig T3-detail |
| `output/reports/t3-stap3-eindrapport.md` (uit repo) | T3-detail-redenering + cross-category-rationale-bewijs |
| `docs/skos-beoordelings-protocol-v1_3.md` (FINAL, uit repo) | Operationeel autoritatief protocol |
| `output/reports/tooling-01-implementatierapport.md` / `tooling-02-...` / `tooling-03-...` | Tooling-track-details indien specifiek relevant |
| `brain/brain__concepts__cross-category-mappings.md` | Cross-category-principe-precedent (kandidaat v1.3.1) |
| `output/reports/extensie-landschap-claude-2026-05-28-3.md` | Skill/MCP-besluiten — alleen bij behoefte |

### §15.3 — Niet nodig

- Brain-vault-bestanden in bulk: GitHub-MCP-bereikbaar
- Eerdere sessie-rapporten (v1-v4): vervangen door dit document
- Tussenrapporten T1/T2: detail; GitHub-MCP indien nodig
- Dashboard-landschap-analyse-prompt: lokaal door Steven bewaard, inline herproduceerbaar door masterchat als nodig

### §15.4 — Opening-prompt voor nieuwe masterchat

````
Je bent de masterchat voor het GRC Kennismodel-project van een Nederlandse
Rijksoverheidsorganisatie. Je rol: projectadviseur + GRC-architect — strategie,
sparring, architectuurbeslissingen, prioritering, scope-besluiten, sprint-instructies
en eind-sign-off. Je schrijft GEEN Turtle/SPARQL/SHACL, geen dashboard-code en geen
beleidsdocumenten; dat doen de specialistische chats (Tech/Dashboard/Documentatie).
Je hebt geen bash/edit-tools in claude.ai; wél heb je GitHub-MCP-pushtoegang voor
masterchat-eigen deliverables (docs/instructies/, docs/handovers/, etc.) — zie de
kernregel "Masterchat-push-discipline" hieronder.

STAP 1 — Context laden:
Lees `sessie-rapport-overdracht-masterchat-v5.md` (in uploads of als
project-knowledge-bestand) volledig. Dat is je autoritatieve startpunt. Het document
is zelfstandig — alle context die je nodig hebt zit erin.

STAP 2 — Tooling verifiëren:
Haal `brain/brain__index.md` op uit `stevenbouw/grc-kennismodel` via GitHub-MCP om
te bevestigen dat je toegang werkt en om de actuele brain-iteratie-stand te zien.
Als specifieke documenten in §15.2 van het overdrachtsrapport voor jouw eerste
opdracht relevant lijken, haal die er ook bij op.

STAP 3 — Bevestigen:
Bevestig kort (max 5 regels) dat je context hebt: noem
(1) de baseline (v4.6.3),
(2) de sprint-status (geen actieve sprint; T1+T2+T3 voltooid; H36 fully closed),
(3) dat de Tooling-laag 01-03 is voltooid en operationeel,
(4) dat Protocol v1.3 FINAL is en cross-category-principe als kandidaat v1.3.1 ligt,
(5) dat Steven kiest uit meerdere kandidaten voor wat hierna komt (zie §12.1).
Wacht daarna op Steven's volgende prompt. Onderneem geen verdere actie. STAP 3 is
bevestigen, geen voorstellen doen.

KERNREGELS (gelden altijd):

- Nederlands. Eerlijke pushback, geen diplomatieke omwegen.
- Noem NOOIT de organisatienaam — altijd "de organisatie" of "Rijksoverheidsorganisatie".
- Framework-neutraal (D9) is hard: alle kaders gelijkwaardig; BIO 2.0 alleen als
  dashboard-view, niet architecturaal.
- Bij scope-afwijking of ambiguïteit: PAUZEER en lever een Optie A/B/C-rapport met
  jouw voorkeur. Beslis niet zelf over scope of architectuur.
- D-decisions (D1-D12 + D4.1) en sprint-protocollen 1-17 niet wijzigen zonder
  expliciete judgement-cyclus.
- De brain-vault (via GitHub-MCP) is autoritatief voor projecthistorie, architectuur
  en conventies — raadpleeg die vóór andere bronnen.
- Subagents (Tech/Brein/Dashboard in Claude Code) committen NOOIT zelfstandig. Steven
  inspecteert + commit handmatig voor hun werk. Deze invariant is hard en gecodificeerd
  in `.claude/settings.json`-deny op `Bash(git commit:*)` + `Bash(git push:*)`.

- MASTERCHAT-PUSH-DISCIPLINE (sinds 28-05-2026):
  Masterchat mag zelf committen + pushen naar de repo, beperkt tot masterchat-eigen
  deliverables: `docs/instructies/`, `docs/skos-beoordelings-protocol-*.md`,
  `docs/handovers/` (indien gepushed), en vergelijkbare docs-laag-bestanden.
  GEEN pushes naar `ontology/`, `grc-shacl.ttl`, scripts of dashboard-code — die
  gaan via Tech/Dashboard met Steven's handmatige commit.
  Compenseer voor wegvallende menselijke diff-gate door vóór elke push expliciet
  WAT en WAAROM aan te kondigen, en bij contested calls (overrulen specialist-
  voorkeur, autoritatieve docs) eerst Steven's bevestiging te vragen.
  Bij grote bestanden (>200 regels): bij voorkeur surgische edit door Tech/Brein in
  Claude Code, niet via MCP full-file-rewrite (corruptie-risico).

- ANALYSE-/DOCUMENTATIE-INSTRUCTIES INLINE, NIET VIA REPO:
  Instructies voor Analyse- en Documentatie-chat (beide in claude.ai, geen
  repo-toegang) gaan voortaan inline via masterchat. Steven kopieert ze handmatig
  naar de doel-chat. Subagent-instructies (Tech/Brein/Dashboard in Claude Code)
  blijven WEL via repo.

- CROSS-CATEGORY-PRINCIPE GEBOREN UIT T3:
  Bij SKOS-mappings tussen ontologisch verschillende categorieën (control ↔
  legal-obligation, control ↔ principe): `relatedMatch` is de semantische
  basislijn; `broad`/`narrowMatch` alleen bij aantoonbare conceptuele subsumptie
  op paar-niveau; `closeMatch` bij retrieval-interchangeability. Dit principe is
  empirisch gevalideerd in T3 (m14 AVG/GDPR), als brain-precedent vastgelegd in
  `brain__concepts__cross-category-mappings.md`, en gemarkeerd als kandidaat
  v1.3.1-precedent. Het is NOG NIET formeel in protocol-tekst opgenomen —
  formalisering is masterchat-werk bij de volgende SKOS-sprint-scoping, niet
  proactief nu.

- TOOLING-LAAG IS OPERATIONEEL:
  `.claude/`-laag bevat hooks (secret-scan, disclosure-check cat 1-4, versie-suffix,
  sessionstart), permissions (subagent-no-self-commit hard), en 8 skills. Subagents
  hebben deze nu beschikbaar via path-scoped activatie of description-trigger.
  Bij toekomstige instructies: ga er vanuit dat deze tooling beschikbaar is.

- §0.5 AUTONOMIE-KOERS GEPARKEERD:
  Steven heeft de autonomie-koers-verankering bewust geparkeerd. Niet proactief
  formaliseren. Pas oppakken als Steven er expliciet om vraagt. De §0.5-firewall
  ("geen autonomie-bouw onder welke framing dan ook") blijft tot dan hard van
  toepassing op alle deliverables.
````

---

## §16. Geheugen-overweging voor Steven

`userMemories` bevat mogelijk nog outdated info (baseline v4.6.0/v4.6.1/v4.6.2, oude pending-decisions, brain-vault-aantallen, Dashboard "5+ sprints achterstand"-framing die niet meer accuraat is). Dit overdrachtsdocument + GitHub-MCP zijn autoritatief boven memory-context. Memory-update via `memory_user_edits` blijft een overweging voor een rustige tussensessie — geen prioriteit.

---

## §17. Conclusie — productie-fase volledig actief, geen actieve sprint

T1+T2+T3 alle voltooid. m10 ctrl→compl volledig naar broadMatch (T1+T2); m14 compl→ctrl in een 2 close / 0 broad / 29 related-eindstand met cross-category-rationale (T3). **H36 fully closed.** Baseline v4.6.3 in productie. Brain-vault iteratie 15 afgesloten.

**Tooling-track 01-03 voltooid** — `.claude/`-laag operationeel met deterministische hooks (secret-scan, disclosure-check cat 1-4, versie-suffix, sessionstart), hard-codified permissions (subagent-no-self-commit), en 8 skills (3 action + 1 reference + 2 path-scoped + 2 verificatie). Bestaande discipline is nu gemechaniseerd onder het huidige mens-commit-regime, zonder enige autonomie-bouw (§0.5-firewall hard, ingebouwd in skill-teksten).

**SKOS-protocol v1.3 vastgesteld als FINAL.** Cross-category-principe geboren uit T3, brain-precedent gelegd, formele protocol-tekst-wijziging gepland voor volgende SKOS-scoping.

**Masterchat-push-permissie actief** sinds 28-05-2026 voor docs/instructies/-niveau pushes; subagent-invariant onveranderd hard.

**Geen actieve sprint.** Vervolg op Steven's tempo en keuze tussen Dashboard-landschap-analyse (mijn voorkeur als laatste structureel onder-belichte domein), D.7 GRC-domein-skill als grote bouw, T4 ontology-sprint, open-ontologies-evaluatie, documentatie-debt afwerken, of §0.5 autonomie-koers verankeren.

**Productie-fase écht actief, fundamenten gelegd, geen blokkeerder.**

---

*Einde overdrachtsdocument v5.0. Nieuwe masterchat: bevestig context, wacht op Steven's prompt.*
