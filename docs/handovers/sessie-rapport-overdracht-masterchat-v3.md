# Sessie-rapport — Overdracht naar nieuwe masterchat (v3.0)

**Datum:** 27 mei 2026
**Versie:** v3.0 (opvolger van v2.0 d.d. 26 mei avond)
**Status:** Definitief — klaar voor overdracht
**Doel:** Volledige zelfstandige context voor nieuwe masterchat in claude.ai. Met dit document + GitHub-MCP-toegang tot `stevenbouw/grc-kennismodel` is het project zonder gaps voort te zetten.
**Volgende voorgenomen activiteit:** T2-sprint-scoping

---

## §0. Quick-start voor nieuwe masterchat

Als nieuwe masterchat: lees eerst dit hele document. Bevestig daarna dat je GitHub-MCP-toegang werkt door één bestand uit `stevenbouw/grc-kennismodel` op te halen (suggestie: `brain/brain__index.md` voor vault-staat-overzicht). Wacht op Steven's volgende prompt.

**Drie meest-relevante punten om te onthouden:**

1. **Baseline is v4.6.1** (post-T1-patch, 26 mei 2026). Niet v4.6.0 zoals oudere documenten suggereren.
2. **D4.1 is nieuw vastgesteld** (27 mei 2026) — disclaimer-handling bij autoritatieve mapping-bronnen, zie §3.4 dit document.
3. **Tech heeft lokale NEN-toegang** in `/Users/stevenbouwmeester/grc-sources-licensed/` — geen masterchat-PK-toets meer nodig voor ISO-bronnen. Zie §6.

---

## §1. Project-essentie (één-paragraaf-versie)

Steven is GRC-adviseur bij een Nederlandse Rijksoverheidsorganisatie (gebruik altijd "de organisatie" of "Rijksoverheidsorganisatie", nooit de daadwerkelijke naam). Hij bouwt het **GRC Kennismodel** — een OWL 2 DL ontologie die alle toepasselijke wet- en regelgeving, normen en best practices integreert in één machine-leesbare kennisbron met dashboard-bediening. Het model is de informatie-laag van het ISMS. Steven is "redelijke leek" in ontologie-engineering met sterke GRC-domeinkennis. Hij communiceert in het Nederlands, verwacht eerlijke pushback, en geen diplomatieke omwegen. Formele Claude-toestemming verkregen maart 2026.

---

## §2. Project-architectuur — zeven chats

| Chat | Locatie | Rol | Doet wel | Doet niet |
|---|---|---|---|---|
| **Master** | claude.ai | Projectadviseur + GRC-architect | Strategie, sparring, architectuurbeslissingen, prioritering, scope-pauze-besluiten, eind-sign-off | Geen Turtle/SPARQL, geen documenten, geen dashboard-code, geen autonome bash-acties |
| **Technisch** | Claude Code (post-migratie) | Ontologie-expert OWL/SPARQL/SHACL | Turtle, SPARQL, SHACL, reasoner-validatie, diagnostiek, patch-voorbereiding, applier-scripts | Geen strategie, beleid, UI-code, geen autonome commits |
| **Documentatie** | claude.ai | Beleidsadviseur + schrijver | PID, managementcommunicatie, beleid (NL) | Geen ontologie-code, dashboard-code |
| **Dashboard** | Claude Code (post-migratie) | Full-stack developer + visualisatie | HTML/JS dashboards, D3/Chart.js, SPARQL, export-scripts | Geen ontologie-wijzigingen, beleidsdocumenten |
| **Asset** | claude.ai | M18-specialist | M18 TBox, mappings, SHACL (afgerond; stand-by) | Geen wijzigingen andere modules |
| **Analyse** | claude.ai | Framework-analist | Externe frameworks analyseren, opties formuleren | Geen Turtle, geen architectuurbeslissingen, geen beleid |
| **Brein** | Claude Code (post-migratie) | Brain-vault-onderhoud | Aanmaken/updaten brain__*-bestanden, cross-referentie-bewaking, autonoom bepalen welke bestanden bijwerken | Geen architectuurbeslissingen, geen ontologie-wijzigingen, geen beleid |

**Werkproces post-migratie (sinds 26 mei 2026):**

Masterchat in claude.ai schrijft instructie → Steven push naar GitHub → subagent in Claude Code voert uit → push deliverables → masterchat review → Brein-subagent doet brain-update na sprint.

**Steven is tussenmens** bij overhandigings-momenten Claude Code ↔ claude.ai. Subagents committen **nooit** zelfstandig — Steven inspecteert `git status` + `git diff` en commit handmatig.

---

## §3. Vastgestelde ontwerpbeslissingen — D1 t/m D12 + D4.1

Wijzigingen vereisen masterchat-goedkeuring. Geen wijzigingen tijdens deze sessie behalve D4.1-toevoeging.

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
| D9 | Framework-neutraal model — alle kaders gelijkwaardig | 17-03-2026 |
| D10 | COSO ICF/ERM als enterprise-governance-laag | 17-03-2026 |
| D11 | `owl:sameAs` asset-convergentie — ster-patroon asset:↔risk:↔isms: (5 bruggen) | 13-04-2026 |
| D12 | Drie-laags compliance-architectuur (regulatory / legal / requirement) | 22-04-2026 |

### §3.4 — D4.1 — Disclaimer-handling bij autoritatieve mapping-bronnen (NIEUW 27-05-2026)

**Vastgesteld via mini-revisie 27 mei 2026** op basis van T1-leerpunt (ENISA TIG regel 285-effect).

**Kern-regel** (volledige tekst in `brain/brain__decisions__D04_skos-cross-framework.md`):

Wanneer een autoritatieve mapping-bron tussen frameworks een expliciete non-equivalence-disclaimer bevat:

- **a)** `skos:exactMatch` is **niet verdedigbaar**, ongeacht of C1-C3 (zie §5) sluitend voldoen
- **b)** `closeMatch` / `relatedMatch` / `broadMatch` / `narrowMatch` blijven valide opties — geen van deze claimt equivalence
- **c)** Geldt vanaf vaststelling; geen retroactieve audit (T2-overweging)

**Bekende disclaimers:**

| Bron | Locatie | Status |
|---|---|---|
| ENISA TIG v1.0 (juni 2025) | Regel 285 | **Bevestigd** — T1-sprint H36-cluster |
| NIST OLIR | Niet geverifieerd | Kandidaat — eerstvolgende NIST-sprint |
| ISO Annex F (27001:2022) | Niet geverifieerd | Kandidaat — eerstvolgende ISO-sprint |

---

## §4. Sprint-protocollen 1-17 (operationeel in `docs/sprint-protocols.md`)

Per 27 mei 2026 zijn er 17 sprint-protocollen actief. Recent toegevoegd of herzien:

| # | Protocol | Status |
|---|---|---|
| 14 | Pre-push disclosure-check (organisatie-naam, persoonsnamen, lokale paden, credentials, NEN-tekst-fragmenten >10 woorden) | Sinds iteratie 12; v1.1 uitgebreid met NEN-categorie |
| 15 | Tech levert werkbare applier (Python/sed/unified-diff), niet alleen specificatie | Sinds Brein iteratie 13 |
| 16 | Lokatie verificatie-scripts expliciet in patch-rapport §9 Deliverables-tabel | Sinds Brein iteratie 13 |
| 17 | NEN-werkverdeling met Tech-autonomie via lokale bron-toegang `/Users/stevenbouwmeester/grc-sources-licensed/`; parafrase-discipline; twee-zijdige analyse voor masterchat-escalatie | **Herzien 27-05-2026** |

Eerdere protocollen 1-13 zijn ongewijzigd en gedocumenteerd in projectinstructie v1.9. Voor detail: raadpleeg `docs/sprint-protocols.md`.

---

## §5. Methode-protocollen voor SKOS-beoordeling

Post-T1 zijn er twee SKOS-beoordelings-protocollen in `docs/`:

### §5.1 — `docs/skos-beoordelings-protocol-v1_0.md` (FINAL)

Vastgesteld 26-05-2026 voor T1. Vier-criteria-set (C1 definitioneel, C2 cardinaliteit, C3 inclusie-richting, C4 bron-evidence). Geldt nog steeds voor historische referentie en T1-vergelijking.

### §5.2 — `docs/skos-beoordelings-protocol-v1_1.md` (DRAFT)

Opgesteld 27-05-2026 op basis van T1-leerpunten + D4.1 + Steven-koers-correctie lokale NEN-toegang. **Status: DRAFT** — vaststelling pending bij T2-scoping-sessie.

**Negen wijzigingen t.o.v. v1.0** (gedetailleerd in protocol §13):

1. D4.1-vooraf-check als nieuwe stap vóór C1-C4
2. C2-cardinaliteit binnen bredere mapping-cluster (was N-set)
3. Evidence-niveau-1-pre-stap als standaard `sources/`-doorzoek
4. Pre-pilot-verwachting verwijderd uit §6
5. Tech-autonomie voor NEN-toetsing via lokale bron-toegang
6. §7 Werkverdeling Tech↔Masterchat als expliciete sectie
7. §8 Discipline licentie-bronnen (parafrase + Protocol 14-uitbreiding)
8. §9 Diff-applier-discipline (Tech levert werkbare applier)
9. Cluster-discipline expliciet verplicht (was aanbeveling)

Vaststellings-tabel `§11 Sign-off-log` is leeg in draft — wordt ingevuld bij T2-scoping-sessie.

---

## §6. NEN-bron-toegang voor Tech (NIEUW 27-05-2026)

**Locatie op Steven's machine:** `/Users/stevenbouwmeester/grc-sources-licensed/`

**Beschikbare bronnen** (lokaal alleen, niet in repo wegens NEN-licentie-restrictie):

- ISO 27002:2022
- ISO 27001:2022
- ISO 27005:2024
- ISO 31000:2018
- ISO 22301:2019
- ISO 22313:2020

**Tech-werkflow:** Tech kan deze bronnen direct lezen voor C1/C3-toetsing in SKOS-beoordelings-protocol. Masterchat-PK-toets is **niet meer nodig** als default-werkverdeling.

**Discipline-regels** (kritisch — geldt voor alle Tech-output naar repo):

- **Geen verbatim NEN-tekst-fragmenten** in rapport-output, commit-messages, Turtle-files, code-comments, of geautomatiseerde output
- Wel toegestaan: parafrase + clausule-verwijzing (bv. "ISO 27002:2022 §8.24 dekt beleid + procedures + sleutelbeheer + gebruik")
- Niet toegestaan: letterlijke citaten >10 woorden
- Pre-push disclosure-check (Protocol 14) is uitgebreid met NEN-tekst-fragment-detectie als vijfde categorie

---

## §7. Actuele baseline — v4.6.1 (post-T1-patch)

**Patch-datum:** 26 mei 2026
**Aanleiding:** T1-sprint H36-cluster afhandeling (28 ctrl:↔compl: SKOS-herclassificaties exactMatch → broadMatch)

### §7.1 — Kerncijfers

| Metric | v4.6.1 | Δ vs v4.6.0 |
|---|---:|---:|
| Triples pre-inferentie | 20.950 | 0 |
| Triples post OWL RL | 44.907 | 0 |
| Klassen | 199 | 0 |
| NamedIndividuals | 1.383 | 0 |
| ObjectProperties | 149 | 0 |
| DatatypeProperties | 96 | 0 |
| owl:sameAs | 98 (93 D5 + 5 D11) | 0 |
| SKOS-mappings totaal | 1.798 | 0 |
| **skos:exactMatch** | **18** | **−28** |
| **skos:broadMatch** | **66** | **+28** |
| owl:Nothing post-inf | 0 (consistent) | 0 |
| SHACL RUN 1 | 0 violations | 0 |
| SHACL RUN 2 | 290 (104+93+93, identiek aan v4.6.0-baseline) | 0 |

### §7.2 — Module-impact

Alleen `m10-nis2-ext.ttl` is gewijzigd. Hash mutatie:

- v4.6.0: `78b8ee44...`
- v4.6.1: `cb2d567b184877e111800cc0a8af1e38d6d6f74ddca0477ee1a52df1d8afa2f1`

Alle 21 andere modules + `grc-shacl.ttl`: hash ongewijzigd.

### §7.3 — Belangrijke afgeleiden

- **D4-conformance verbeterd** — exactMatch was te sterk geclaimd voor 28 paren waar ENISA TIG equivalence expliciet ontkent
- **D4.1 vastgesteld** op basis van deze bevinding
- **Geen ontology-inconsistenties** (owl:Nothing = 0)
- **Geen SHACL-impact** — Vraag D inventarisatie bevestigde dat geen shape valideert op de 28 paren (H39-relevant)

---

## §8. Recente sessies-overzicht (chronologisch)

### §8.1 — 26 mei 2026, ochtend tot avond

**Brein-cyclus iteratie 12 afgerond:** 13 bestanden gewijzigd (4 commits). Vijf werkpakketten:

- WP1: H-items H36-H40 registreren (5 nieuwe H-bestanden + register)
- WP2: Protocol 14 pre-push disclosure-check toegevoegd aan `docs/sprint-protocols.md`
- WP3: Productlijn-scheiding `brain__concepts__dashboard-productlijnen.md` + CLAUDE.md v1.4
- WP4: Log + index iteratie 12

**T1-sprint volledig uitgevoerd in vijf stappen:**

| Stap | Wat | Wie |
|---|---|---|
| 1 | Pre-sprint-inventarisatie (Vraag A-E) | Tech read-only |
| 2 | Methode-protocol v1.0 vastgesteld (5 open beslis-punten door Steven sign-off) | Masterchat + Steven |
| 3 | Pilot van 5 paren — alle 5 → broadMatch met hoog vertrouwen, evidence-niveau 1. Belangrijkste vondst: ENISA TIG regel 285-categorisch-effect | Tech + Masterchat-escalatie |
| 4 | Resterende 23 paren — 21 cluster-overerving + 2 edge-cases (T1-021, T1-023) verplicht masterchat-escalatie | Tech |
| 5 | NEN-PK-toets edge-cases via project knowledge → scenario C (alle 28 broadMatch) | Masterchat + Steven |

**Patch v4.6.1 toegepast** door Steven via `apply_patch_v4_6_1.py` (Python-applier door masterchat geschreven — Tech leverde alleen specificatie, geen werkbare applier; dit werd T1-leerpunt 5). Alle drie verificaties groen (hash + canonical metrics + SHACL).

**T1-eindrapport opgesteld** (`output/reports/t1-eindrapport-v4_6_1.md`) — 11 secties, met §8 als hoofdsectie: 10 werkflow-leerpunten.

### §8.2 — 27 mei 2026, ochtend (deze sessie)

**Optie B — vier mini-revisies afgerond:**

1. **Productlijn-scheiding locatie gesloten** (Optie D — Spoor B-prototype `grc-dashboard-v3-2.html` blijft lokaal, niet in repo). Vier trigger-condities voor heroverweging vastgelegd. Brein-mini-briefing uitgevoerd.

2. **D4.1 vastgesteld** als sub-regel onder D4 (zie §3.4). Drie keuzes vastgesteld: sub-regel-formaliteit (B), reikwijdte alleen exactMatch (C), geen retroactieve audit (A). Brein-mini-briefing uitgevoerd op `brain__decisions__D04` (bestond al, Geval A2 sectie-toevoeging), D-register en `brain__concepts__mapping-bron-disclaimer-effect`.

3. **Protocol 17 herzien** in `docs/sprint-protocols.md` — NEN-werkverdeling met Tech-autonomie i.p.v. masterchat-PK-toets. Aanleiding: Steven bevestigde dat NEN-bronnen lokaal beschikbaar zijn voor Tech in `/Users/stevenbouwmeester/grc-sources-licensed/`.

4. **Protocol v1.1-draft opgesteld** door masterchat, geplaatst in `docs/skos-beoordelings-protocol-v1_1.md` via Brein-mini-briefing. Status DRAFT — sign-off bij T2-scoping.

**Brein-cyclus iteratie 13 afgerond** (parallel aan mini-revisies):

| WP | Bestanden | Wat |
|---|---|---|
| WP1 | 1 nieuw + 1 update | T1-sprint geregistreerd + sprint-register |
| WP2 | 1 nieuw | skos-beoordelings-protocol als concept |
| WP3 | 3 updates | H36 closed, H39 versterkt, H-register |
| WP4 | 1 nieuw + 1 update | mapping-bron-disclaimer-effect concept (Optie A — patroon-herbruikbaar) |
| WP5 | 1 update | docs/sprint-protocols.md (Protocollen 15/16/17 — 17 nadien herzien) |
| WP6 | 2 updates | brain__log.md + brain__index.md v4.6.1-baseline |

**Brein keuze H42 retroactieve audit:** géén H-item; audit-haak vastgelegd in D4.1 §c als T2-overweging.

---

## §9. Brain-vault — primaire kennisbron

**Structuur:** flat bestanden in `brain/`-folder met `__`-separator voor folder-encoding (bv. `brain__sprints__T1_skos-kwaliteitsanalyse-fase-1.md`).

**Entry-points** (te raadplegen voor masterchat-vragen over project-historie):

- `brain/brain__index.md` — vault-staat-tabel, iteratie-teller, baseline-overzicht
- `brain/brain__log.md` — append-only iteratie-log
- Folder-registers: `brain__decisions__D-register.md`, `brain__sprints__sprint-register.md`, `brain__architecture__H-register.md`, `brain__concepts__concept-register.md`, etc.

**Iteratie-stand** per 27-05-2026: iteratie 13 afgesloten, brain-vault bevat ~115 bestanden.

**Conventie:** bij vragen over projecthistorie, architectuur of conventies → raadpleeg brain-vault via GitHub-MCP vóór andere bronnen. De brain-vault is autoritatief.

---

## §10. Sprint-architectuur en huidige toestand

### §10.1 — Vijf doelen

G1 GRC Referentiemodel | G2 Rollen & RACI | G3 Business Alignment | G4 ISMS | G5 OWL Ontologie

### §10.2 — Drie sporen

| Spoor | Wat | Status |
|---|---|---|
| A | Technische ontologie-opbouw (zonder organisatiedata) | Voltooid t/m v4.6.1 voor bedoelde Fase 1-4 scope + T1-sprint |
| B | Organisatiespecifieke invulling | Pending; lab-test bij Technologie & Innovatie gepland als eerste proeftuin |
| C | Gebruik en governance (triplestore, dashboard, beheerproces) | Pending |

### §10.3 — Sprint-historie sinds Fase 4

| Sprint | Datum | Scope | Status |
|---|---|---|---|
| v4.6.0 | 21-05-2026 | Fase 4 — ENSIA + volwassenheidsmodel + CSF Tiers | Afgerond |
| (Migratie) | 26-05-2026 | Tech/Brein/Dashboard naar Claude Code + GitHub | Afgerond |
| (Polish-mini-sprint) | 26-05-2026 | Pre-T1-correcties + GitHub-MCP-setup | Afgerond |
| Brein-cyclus 12 | 26-05-2026 | H36-H40 registreren + Protocol 14 + productlijn-scheiding | Afgerond |
| **T1** | **26-05-2026** | **SKOS-kwaliteitsanalyse Fase 1 — H36-cluster (28 paren)** | **Afgerond — patch v4.6.1** |
| Brein-cyclus 13 | 27-05-2026 | T1-administratieve afronding + Protocollen 15-17 | Afgerond |
| (Mini-revisies) | 27-05-2026 | Optie D + D4.1 + Protocol 17-herziening + Protocol v1.1-draft | Afgerond |

---

## §11. Werkflow-leerpunten — kritiek voor toekomstige sprints

Uit T1-eindrapport §8 + recente sessie-ervaring:

### §11.1 — Tooling-discipline (Protocol 15)

T1 toonde dat Tech een diff-bestand leverde als **specificatie** (lijst van te wijzigen triples) zonder werkbare applier. Steven probeerde `patch -p0` toe te passen — faalde. Masterchat moest `apply_patch_v4_6_1.py` schrijven. Sindsdien is Protocol 15 actief: Tech levert standaard zowel specificatie als werkbare applier + integratie-test.

### §11.2 — Pad-discipline (Protocol 16)

T1 toonde een werkflow-fout: masterchat-instructie noemde `scripts/canonical_metrics_v4_6_1.py` terwijl Tech de scripts in `output/verification/` had geplaatst. Sindsdien Protocol 16: lokatie scripts in patch-rapport §9 Deliverables-tabel, masterchat citeert daaruit.

### §11.3 — Werkverdeling Tech ↔ Masterchat (Protocol 17, herzien)

Pre-27-05-2026: Tech leverde structurele analyse; masterchat verzorgde NEN-tekst-toets via PK. Post-27-05-2026: Tech autonoom met lokale NEN-toegang, masterchat alleen bij cross-bron-interpretatie of ambigue lezing.

### §11.4 — ENISA-disclaimer-categorisch-effect

T1 toonde dat autoritatieve mapping-bronnen vaak een non-equivalence-disclaimer bevatten (ENISA TIG regel 285). Dit ondergraaft `skos:exactMatch` zelfs bij sluitende C1-C3-toets. Geformaliseerd als D4.1.

### §11.5 — Cluster-discipline-overerving

T1 toonde dat cluster-representant + cluster-discipline-overerving 18 paren in ~30 min levert (gemiddeld <2 min/paar) i.p.v. ~10 min/paar voor volledige beoordeling. Vasthouden als standaard.

### §11.6 — Sample-first zonder pre-pilot-verwachting

Protocol v1.0 had pre-pilot-verwachting in §6 wat stop-conditie-noise creëerde op verwachte uitkomsten. Protocol v1.1 verwijdert pre-pilot-verwachting expliciet.

### §11.7 — Twee-zijdige edge-case-analyse-format

Voor masterchat-escalatie levert Tech expliciet beide kanten (pro-X én pro-Y) van mogelijke beoordeling, plus Tech-positie + specifieke vraag. Voorkomt dat masterchat moet reverse-engineeren wat Tech al overwogen heeft.

### §11.8 — Steven's "denk ik" als verifier-signaal

In T1 zei Steven "denk ik" toen hij scripts had gerund. Dat bleek signaal om te verifiëren, niet aanname dat alles goed ging. Masterchat moet bij dergelijke onzekerheid altijd controle uitvoeren (in mijn geval: GitHub-MCP-check op repo-staat).

### §11.9 — Sprint-duur-raming

T1 geraamd op 3-4 uur, werkelijk ~5 uur door tooling-incident (applier). Voor T2-planning: rekenen op ~5-6 uur voor analoge ~30-paren-scope, verdeeld over 1-2 dagen.

### §11.10 — Memory-update-discipline (deze sessie)

Mijn `userMemories` (vorige sessie) vermeldt nog "Actuele baseline v4.6.0" en "Pending decisions handover naar nieuwe masterchat" (vijf items). Veel daarvan is inmiddels opgelost. Voor nieuwe masterchat: vertrouw op dit overdrachtsdocument boven `userMemories`-context. Memory-update via `memory_user_edits` is mogelijk overweging — wachtend op Steven-keuze.

---

## §12. Open punten en roadmap

### §12.1 — Direct openstaand (volgende activiteit)

**T2-scoping** — eerste activiteit voor nieuwe masterchat-sessie.

**T1-eindrapport §9.1 voorkeur:** T2 = overige ctrl:↔compl: mappings (~93 close + related + broad). Reden: protocol v1.0/v1.1 is voor ctrl:↔compl:-context bewezen; T2 valideert protocol-toepassing op andere predicate-types.

**Twee alternatieven** (afhankelijk van Steven-prioriteit):

- T2-alt-1: cross-bron-overlap-105-paren (uit v4.5.0)
- T2-alt-2: m17-COSO/COBIT-mappings audit

### §12.2 — Bewust geparkeerd (geen urgentie)

| Item | Type | Trigger voor heractivering |
|---|---|---|
| Projectinstructie v1.10 | Documentatie | Bij T2-vaststelling of bij Steven's keuze |
| Retroactieve audit 18 resterende `skos:exactMatch`-mappings | Inhoudelijk | Bij T2-uitvoering of als sub-sprint |
| NIST OLIR + ISO Annex F disclaimer-verificatie | Inhoudelijk | Eerstvolgende ISO/NIST-mapping-sprint |
| Wikilink-rot lint-cyclus in vault | Hygiëne | Geen actieve aanleiding |
| H37 — open-ontologies MCP-server | Architectuur | OWL RL-limitatie aantoonbaar of >50.000 triples |
| H38 — OWL RL vs HermiT-equivalentie | Architectuur | Significante ontology-groei of DL-conformance-twijfel |
| H39 — 290 SHACL RUN 2 false-positives uitsplitsen | Hygiëne | Rustige sprint of SHACL-shapes-wijziging |
| H40 — Dashboard-UI-renderdekking <10% | UX | UI-moderniseringssprint na Fase 4 |
| H41-kandidaat — SKOS-axioma-set (skos:S46) | Architectuur | Overstap-besluit owlrl-incl-SKOS |
| H25, H26, H27, H32, H33, H34, H35 | Per H-register | Per-item triggers (zie projectinstructie v1.9) |
| H15 (governance-graafdekking) | Architectuur | Spoor B-trigger |
| H21 (implicit individuals) | Architectuur | Consistentie-keuze-trigger |

### §12.3 — Toekomst-richting

| Sprint-kandidaat | Wanneer | Wat |
|---|---|---|
| T2 | Eerstvolgend | Volgende SKOS-cluster (zie §12.1) |
| T3 | Na T2 | Vermoedelijk nog een SKOS-cluster |
| Protocol v1.1-vaststelling | Bij T2-scoping | Sign-off log §11 invullen |
| Spoor B-voorbereiding | Latere fase | T&I lab-test als eerste proeftuin |
| Dashboard SKOS-kwaliteitsanalyse | Parallel mogelijk | Op 1.798 mappings na alle T-sprints |
| Dashboard-inhaalslag v4.6.1 | Parallel mogelijk | Build-script update naar v4.6.1-snapshot |

---

## §13. Wat de nieuwe masterchat NIET moet doen

- **Geen autonome bash/git/edit-acties** — masterchat opereert in claude.ai zonder die tools en moet dat zo houden
- **Geen scope-uitbreidingen zonder Steven-akkoord** — bij ambiguïteit altijd scope-pauze met Optie A/B/C-rapport
- **Geen retroactieve audit van 18 resterende `skos:exactMatch`-mappings** zonder T2-context — staat als T2-overweging vast
- **Geen wijziging aan D-decisions** (D1-D12 + D4.1) zonder expliciete masterchat-judgement-cyclus
- **Geen wijziging aan sprint-protocollen 1-17** zonder grondige aanleiding
- **Geen organisatie-naam noemen** — altijd "de organisatie" of "Rijksoverheidsorganisatie"
- **Geen tussentijdse projectinstructie-v1.10-opstelling** zonder Steven-trigger
- **Geen herinrichting brain-vault** — vault-structuur is stabiel sinds iteratie 11/12/13

---

## §14. Tooling-status (per 27-05-2026)

| Tooling | Status | Locatie/configuratie |
|---|---|---|
| GitHub-MCP voor claude.ai | Werkend via Anthropic's GitHub Integration | `stevenbouw/grc-kennismodel` repo, privé |
| Claude Code in VS Code | Geauthenticeerd, actief | Tech/Brein/Dashboard-subagents |
| `CLAUDE.md` v1.4 | Active | Repo-root |
| Subagent-configs | Actief | `.claude/agents/tech.md`, `brein.md`, `dashboard.md` |
| `docs/sprint-protocols.md` | Actief — 17 protocollen | Repo |
| OWL RL reasoning | `axiomatic_triples=False`, `datatype_axioms=False` | Standaard-script-instellingen |
| pySHACL | Gesplitste validatie (SECTIE A inference='none' + SECTIE B inference='owlrl') | Standaard-script-instellingen |
| Protégé | Stand-by — geen HermiT-rerun sinds v4.0.0 | Mac, lokaal |
| Cytoscape.js | Dashboard-engine voor `grc-explorer-v4_6_0.html` | Spoor A |
| Lokale NEN-bronnen | Toegankelijk voor Tech | `/Users/stevenbouwmeester/grc-sources-licensed/` |

---

## §15. Wat Steven moet uploaden naar nieuwe masterchat

### §15.1 — Primair (verplicht)

**Dit document** (`sessie-rapport-overdracht-masterchat-v3.md`). Bevat alles wat nieuwe masterchat nodig heeft als zelfstandige basis.

### §15.2 — Secundair (aanbevolen, niet kritisch)

| Bestand | Waarom |
|---|---|
| `output/reports/t1-eindrapport-v4_6_1.md` (uit repo) | Volledig detail T1-sprint + 10 werkflow-leerpunten — als nieuwe masterchat detail-verificatie wil |
| `docs/skos-beoordelings-protocol-v1_1.md` (uit repo) | Volledige tekst Protocol v1.1-draft — relevant voor T2-scoping-sessie |
| `projectinstructie-v1_9.pdf` (huidig in project knowledge) | Historische basis; bevat *niet* T1-uitkomst of D4.1 of v4.6.1-baseline. Met dit overdrachtsdocument als overlay nog steeds bruikbaar. v1.10-opstelling is geparkeerd |

### §15.3 — Niet nodig

- Andere brain-vault-bestanden: nieuwe masterchat heeft GitHub-MCP en kan zelf raadplegen
- Eerdere sessie-rapporten (v1.0, v2.0): vervangen door dit document
- T1-tussen-rapporten (pre-sprint, pilot, Stap 4): detail; raadplegen via GitHub-MCP indien nodig
- Patch v4.6.1-deliverables: in repo, GitHub-MCP-bereikbaar

### §15.4 — Initiële prompt voor nieuwe masterchat

Suggestie:

```
Je bent de nieuwe masterchat voor het GRC Kennismodel-project. Lees eerst
`sessie-rapport-overdracht-masterchat-v3.md` volledig (in uploads).
Verifieer daarna kort dat GitHub-MCP werkt door `brain/brain__index.md`
uit `stevenbouw/grc-kennismodel` op te halen en de eerste 10 regels te
tonen. Bevestig dan kort dat je context hebt en wacht op mijn volgende
prompt. Geen acties tot beide stappen voltooid.
```

---

## §16. Geheugen-overweging voor Steven

Mijn `userMemories` (uit huidige sessie) bevat outdated info: baseline v4.6.0 (nu v4.6.1), "pending decisions" met 5 items waarvan veel inmiddels gesloten. Voor nieuwe masterchat-sessie kun je overwegen om `memory_user_edits` te gebruiken om geheugen te updaten — maar dit overdrachtsdocument is autoritatief en overlay-geheugen-context werkt voor nieuwe sessie.

Mijn suggestie: laat geheugen-update voor later. Eerst T2-scoping doen; geheugen-update kan in een rustige tussensessie.

---

## §17. Conclusie — productie-fase actief

T1-sprint volledig afgerond. Vier mini-revisies gesloten. Brain-vault iteratie 13 afgesloten. Baseline v4.6.1 in productie. D4.1 vastgesteld. Protocol v1.1-draft beschikbaar. Tech-autonomie voor NEN uitgebreid.

**Productie-fase is écht actief.** Geen open masterchat-werk dat blokkeert. T2-scoping als logische voortzetting, op Steven's tempo.

---

*Einde overdrachtsdocument v3.0. Nieuwe masterchat is klaar voor T2-scoping bij Steven's volgende prompt.*
