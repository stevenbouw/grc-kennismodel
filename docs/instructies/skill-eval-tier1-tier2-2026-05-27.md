# Skill-evaluatie Tier 1 + Tier 2 — 27 mei 2026

**Type:** Quick-scan evaluatie (Optie A + B uit masterchat-sessie 27 mei)
**Scope:** Vier externe skills genoemd in `CLAUDE.md` §"Skills-ecosystem-positionering"
**Doel:** GO/HOLD/NO-GO-recommendatie per skill voor toekomstige Claude Code-installatie
**Status:** masterchat-deliverable; geen sprint-mutatie, geen ontologie-impact

---

## 0. Werkwijze + scope-disclaimer

Evaluatie via web-fetch + web-search van publieke GitHub-repository-content (README's en metadata). Geen daadwerkelijke installatie van skills in Claude Code uitgevoerd. Geen verbatim NEN-discipline-check op skill-content mogelijk vanuit masterchat — daarvoor moeten skills lokaal gedownload + gescand worden (Claude Code-werk, niet masterchat).

**Vier evaluatiecriteria per skill:**

1. **Inventarisatie** — Wat het is, scope, licentie, recency, install-mechanisme
2. **NEN-discipline-risico** — Kans op verbatim NEN-tekst > 10 woorden in skill-content
3. **Overlap met huidig project** — Brain-vault / ontologie / werkwijze
4. **GO / HOLD / NO-GO** — Aanbeveling + onderbouwing

**Beperking:** publieke GitHub-content is geen vervanger voor een installatie-test. Beoordeling per skill blijft "informed first impression".

---

## 1. Tier 1 — GRC-domein

### Skill 1: Sushegaad/Claude-Skills-Governance-Risk-and-Compliance

**Inventarisatie**

| Aspect | Waarde |
|---|---|
| Auteur | Hemant Naik (Sushegaad) |
| Stars / forks | 300 / 68 |
| Laatste commit | 4 dagen geleden (actief) |
| Licentie | Niet expliciet vermeld in README — moet vóór installatie geverifieerd |
| Install-mechanisme | Plugin marketplace via `/plugin marketplace add Sushegaad/Claude-Skills-Governance-Risk-and-Compliance` |
| Coverage | ISO 27001, SOC 2, FedRAMP, GDPR, HIPAA, NIST CSF, PCI DSS, EU AI Act, ISO 42001, ISO 27701, DORA, CSRD, India's DPDPA, CMMC 2.0, NIST AI Risk, SWIFT, Australia's ISM, EU NIS2, CCPA/CPRA |
| Skill-structuur | SKILL.md (always loaded) + references/ (on-demand) per framework |
| Claim | "Benchmark 96% (with skills) vs 81% (without skills)" — niet onafhankelijk geverifieerd |

**Relevant voor ons project:** ISO 27001 ✓, NIS2 ✓, GDPR (m14, T3-kandidaat) ✓, DORA ✓ (referentiekader), ISO 42001 (M19 toekomst) ✓, NIST CSF (M21 v4.5.0) ✓.

**Niet-relevant:** SOC 2, FedRAMP, HIPAA, PCI DSS, CMMC 2.0, SWIFT, Australia's ISM, India's DPDPA, CCPA/CPRA, CSRD (geen organisatie-relevantie).

**Ontbreekt voor ons:** BIO 2.0, VIR 2007, VIRBI 2025, CBW, Cbb, ENSIA, COSO ICF/ERM, COBIT 2019, BVA-stelsel, CIO-stelsel — alle Nederlands / Rijksoverheid-specifieke kaders.

**NEN-discipline-risico**

⚠ **Onbekend / potentieel hoog.** ISO 27001-skill bevat per definitie ISO-conceptmateriaal. Mogelijkheden:
- (a) Skill bevat *parafrases* van ISO 27001-controls (acceptabel, vergelijkbaar met onze brain-vault-praktijk)
- (b) Skill bevat *verbatim ISO-tekst > 10 woorden* (onaanvaardbaar onder NEN-restrictie)

Niet vast te stellen zonder skill-content-inspectie post-install. Pre-install-mitigatie: download repository lokaal en grep op verdachte ISO-fragmenten vóór installatie in werkomgeving.

**Voorbeeld uit SOC 2 README:** *"The skill is grounded in the AICPA 2017 Trust Services Criteria (TSC) with 2022 Revised Points of Focus."* — claim is parafrase + criteria-codes, geen verbatim normtekst. Voor SOC 2 (geen NEN-restrictie) is dit onproblematisch. Voor ISO 27001 (wel NEN) is dezelfde aanpak met "criteria-codes" pragmatisch acceptabel mits parafrase.

**Overlap met huidig project**

- ✓ Sushegaad biedt **kennis-injectie / expert-guidance** voor Claude-conversaties
- ✗ Onze brain-vault biedt **formele ontologie-modellering** (Turtle/OWL)
- ✗ Onze brain-vault is **project-specifiek** (Rijksoverheid + integraal model)
- → Verschillende functionele lagen. Sushegaad is **chat-augmenter**, geen ontologie-vervanger
- ✗ Sushegaad heeft geen Nederlandse Rijksoverheid-context (geen BIO/VIR/VIRBI/CBW/ENSIA)

**Conceptueel risico:** Sushegaad-skill voor "NIS2" kan in conflict komen met onze m10-modellering. Skill geeft mogelijk expert-guidance die afwijkt van onze cluster-discipline (Protocol v1.2/v1.3) of D4.1-disclaimer-handling. Bij gebruik tijdens sprint-werk: skill-output zou kunnen tegenspreken wat onze SKOS-mappings doen.

**GO/HOLD/NO-GO**

🟡 **HOLD met conditionele evaluatie-route**

**Aanbevolen aanpak indien je verder wilt:**
1. Test eerst op een framework waar wij **geen modellering** voor hebben (bv. ISO 42001 / M19 toekomst, ISO 27701, EU AI Act)
2. Vergelijk skill-output met onze brain-vault op één framework waar wij wel modelleren (bv. NIS2) — assess of skill ons werk versterkt of contradicteert
3. NEN-discipline-pre-install-check: download repo, grep op `^[^\#]{30,}` patronen in iso27001-skill om verbatim-tekst-risico in te schatten
4. Niet installeren in dezelfde Claude Code-omgeving waarin Tech-subagent draait — risico van skill-context-interferentie tijdens sprint-werk

**Waarom geen GO:**
- Overlap-risico met onze formele modellering tijdens sprint-werk
- Geen Nederlandse/Rijksoverheid-context — schaaft aan onze D9-framework-neutraal-discipline (alle skills van Sushegaad zijn EN-talig en US/EU-gericht)
- NEN-discipline-risico onbekend voor ISO-skills

**Waarom geen NO-GO:**
- Coverage van ISO 42001 (M19 toekomst), ISO 27701 (mogelijk toekomstige toevoeging), CSRD (mogelijk toekomstig relevant) kan operationele waarde leveren in latere fasen
- Plugin marketplace-installatie is reversibel — geen permanente repo-pollutie

---

### Skill 2: GRCEngClub/claude-grc-engineering

**Inventarisatie**

| Aspect | Waarde |
|---|---|
| Auteur | GRC Engineering Club (community) |
| Laatste commit | 2 weken geleden (actief) |
| Licentie | Open-source (niet expliciet in zoekresultaten — verifiëren) |
| Install-mechanisme | Claude Code plugin marketplace; Claude Desktop / Cowork via repo-context |
| Coverage frameworks | soc2, nist-800-53, iso27001, fedramp-rev5, fedramp-20x, pci-dss, cmmc, hitrust, cis-controls, gdpr, dora, us-hipaa-security |
| Onderscheidende tools | aws-inspector, github-inspector, gcp-inspector, azure-inspector, okta-inspector, slack-inspector, datadog-inspector (evidence collectors) |
| Diagram-tools | `/grc-diagrams:drawio`, `/grc-diagrams:system-boundary`, `/grc-diagrams:evidence-flow`, `/grc-diagrams:control-map` |
| OSCAL-ondersteuning | Ja — NIST Open Security Controls Assessment Language workflows |

**Belangrijkste afwijking:** GRCEngClub focust op **evidence collection** uit cloud/SaaS/security-tools → omzetten naar findings + gap-reports + remediation guidance. Niet kennis-injectie zoals Sushegaad.

**Coverage-gap:** **geen NIS2-vermelding** in framework-lijst. Wel DORA, GDPR. Voor onze NL-Rijksoverheid-context dus minder direct relevant dan Sushegaad.

**NEN-discipline-risico**

🟢 **Laag.** Focus is op evidence-output, niet op normtekst-reproductie. Inspectors-tools verzamelen evidence uit live cloud-omgevingen — geen risico op verbatim NEN-tekst > 10 woorden.

ISO 27001-coverage zou via parafrase en framework-naam-verwijzingen kunnen werken (analoog aan Sushegaad SOC 2). Te verifiëren bij eventuele installatie.

**Overlap met huidig project**

- ✓ Spoor A (huidige fase): **geen overlap** — wij doen formele ontologie, niet evidence-collection
- ✓ Spoor B (toekomst lab-test T&I): **substantiële overlap met value-add** — evidence-collection past precies bij wat Spoor B beoogt
- ✗ Cloud-inspectors vereisen toegang tot AWS/GCP/Azure/GitHub/Okta/Slack/Datadog — wij hebben dat niet in Spoor A
- ✗ OSCAL is NIST-standaard voor machine-leesbare controls — past niet bij onze Turtle/OWL-stack zonder bridge
- ⚠ Diagram-tools (`/grc-diagrams:*`) overlappen mogelijk met visualizer-tool die ik in deze chat heb — niet noodzakelijk maar mogelijk handig voor Steven's documentatie-flow

**GO/HOLD/NO-GO**

🟢 **NO-GO voor Spoor A — HOLD voor Spoor B**

**Onderbouwing voor Spoor A NO-GO:**
- Functionele scope past niet bij huidige fase (formele ontologie-opbouw)
- Cloud-inspectors irrelevant tot lab-test bij T&I
- Coverage-gap NIS2 maakt het minder waardevol dan Sushegaad voor NL-context

**Onderbouwing voor Spoor B HOLD (niet direct GO):**
- Bij Spoor B-overgang: heroverwegen + evalueren in detail
- Trigger-criterium: T&I lab-test met concrete evidence-collection-vraag
- Tussentijds: parkeer als bekende kandidaat in `brain__scope__*.md` of nieuw H-item

**Bevestigt CLAUDE.md-vermelding:** *"Past beter bij Spoor B / lab-test-fase"* — quick-scan bevestigt dit oordeel.

---

## 2. Tier 2 — Ontologie + brain-vault

### Skill 3: fabio-rovai/open-ontologies (MCP)

**Inventarisatie**

| Aspect | Waarde |
|---|---|
| Auteur | Fabio Rovai (academisch geverifieerd via arXiv-paper) |
| Laatste commit | April 2026 (actief, releases met platform-binaries) |
| Licentie | MIT |
| Install-mechanisme | MCP-server (single Rust binary, no JVM) + CLI-subcommands |
| Tools | 43 tools — core (validate/load/save/query/diff/lint/convert), data pipeline (map/ingest/shacl/reason/extend), lifecycle (plan/apply/lock/drift/enforce/monitor/lineage), advanced (align/crosswalk/enrich/embed) |
| Reasoner | Native OWL2-DL **tableaux reasoner** (volledige OWL 2 DL — sterker dan onze OWL RL) |
| Triple store | In-memory Oxigraph (SPARQL 1.1 query + update, persistent SQLite state) |
| SHACL | Volledige SHACL validation |
| Marketplace | 32 standaard-ontologieën, clinical crosswalks, semantic embeddings |
| Studio | Visual desktop environment met ontology tree, AI chat (/build, /sketch), Protégé-style property inspector |
| Academic validation | OAEI Anatomy F1 0.832 (vs unaided LLM 0.431) — onafhankelijk peer-reviewed |
| Co-author | "Claude Opus 4.6" in recente commits — actief LLM-ondersteund onderhoud |

**Vergelijking met onze huidige toolchain:**

| Aspect | Huidige (rdflib+owlrl+pySHACL) | Open Ontologies |
|---|---|---|
| Reasoner | OWL RL (subset OWL 2 DL) | Volledige OWL 2 DL via tableaux |
| Triple store | rdflib in-memory | Oxigraph (persistent + SPARQL Update) |
| Performance | Python — ~8-12s closure v4.6.2 | Rust — naar verwachting sneller |
| SKOS-axiomas | Niet geladen onder `axiomatic_triples=False` (zie H41) | Mogelijk geladen via tableaux (te verifiëren) |
| Stack-complexity | Standalone Python scripts | MCP-server + binary + state |
| Migratie-kost | n.v.t. (huidige) | Substantieel — canonical_metrics scripts herschrijven, dependency-injection, MCP-config |

**NEN-discipline-risico**

🟢 **Niet van toepassing.** Open-ontologies is een **toolchain**, geen content. Bevat geen normtekst. Risico nul.

**Overlap met huidig project**

- ✓ Direct gerelateerd aan H37 (al geregistreerd parked, geactiveerd door deze evaluatie)
- ✓ Direct gerelateerd aan **H41** (SKOS-axioma-set-handling) — als tableaux-reasoner wel SKOS-axiomas laadt, biedt dat de oplossing voor één van onze open architectuur-vragen
- ⚠ Direct gerelateerd aan H38 (OWL RL vs HermiT-equivalentie) — derde reasoner-vergelijking wordt mogelijk
- ✓ Triple-totaal-trigger: 44.907 post-RL ↔ H37-trigger 50.000 — drempel nadert (niet bereikt)
- ⚠ Migratie-overweging: 22 .ttl-modules + canonical_metrics scripts + SHACL split-validatie zouden herwerkt moeten worden

**Concrete H37 + H41 + H38 koppeling:**

Een gerichte open-ontologies-evaluatie kan **drie H-items tegelijk vooruithelpen**:

| H-item | Wat een evaluatie zou leveren |
|---|---|
| H37 | Empirisch antwoord op "biedt open-ontologies meerwaarde" |
| H38 | Tableaux-reasoner als derde vergelijkingspunt naast OWL RL + HermiT |
| H41 | Test of SKOS-axiomas wel/niet geladen worden onder tableaux → besluit over SKOS-axioma-handling |

**GO/HOLD/NO-GO**

🟡 **HOLD met sterke evaluatie-aanbeveling op middellange termijn**

**Aanbevolen aanpak indien je verder wilt:**
1. **Niet nu migreren** — onze toolchain werkt stabiel, v4.6.2 productie
2. **Wel evaluatie-sprint plannen** als "T-skills-evaluatie" of "H37-H38-H41-onderzoek" op middellange termijn (bv. na T3 m14-sprint)
3. **Concreet evaluatie-doel:**
   - Installeer open-ontologies-MCP in Claude Code (geen impact op huidige toolchain)
   - Load `grc-v4_6_2-merged.ttl` (gebruik `convert` of `load`-tool)
   - Run reasoning + SHACL — vergelijk uitkomst met canonical_metrics_v4_6_2.json
   - Focus-vragen: (a) is post-inferentie-triples-totaal anders? (b) worden SKOS-axiomas wel geladen? (c) performance-Δ?
4. **Output:** evaluatie-rapport + H37/H38/H41-status-updates in brain-vault

**Waarom geen GO (migratie):**
- Onze toolchain is bewezen op v4.0.0-v4.6.2 (14 sprints stabiel)
- Geen aangetoonde OWL RL-limitatie in productie
- Migratie-kosten substantieel
- "Krachtiger is beter" is geen valide argument zonder concrete trigger

**Waarom geen NO-GO:**
- Twee actieve H-items (H37 + H41) hebben deze tool als concrete trigger-kandidaat
- 50k-triple-drempel nadert
- MCP-architectuur past goed bij ons werkmodel (Claude Code + subagents)
- Academic validation (arXiv) verlaagt vendor-risico

---

### Skill 4: kfchou/wiki-skills

**Inventarisatie**

| Aspect | Waarde |
|---|---|
| Auteur | kfchou |
| Stars / forks | 127 / 21 |
| Laatste commit | 1 maand geleden |
| Licentie | Niet expliciet vermeld in zoekresultaten — verifiëren |
| Type | Claude Code wiki skills (.md per skill) |
| Patroon | Karpathy LLM Wiki gist (april 2026, 16M views, 5000+ stars) |
| Workflow | Ingest sources → compile into wiki/ → query met citations → lint |

**Karpathy LLM Wiki pattern (achtergrond):** Andrej Karpathy poste in april 2026 een workflow waarin LLM een persistent gestructureerd wiki onderhoudt, in plaats van one-shot RAG. Het idee ging viral; community ontwikkelde meerdere implementaties (kfchou, Astro-Han, toolboxmd, lewislulu, skyllwt, TrueHOOHA).

**NEN-discipline-risico**

🟢 **Niet van toepassing.** kfchou is **methode + tooling**, geen content. Bevat geen normtekst.

**Overlap met huidig project**

⚠ **Substantiële overlap — wij doen dit al.** CLAUDE.md zegt expliciet:

> *"Karpathy-pattern toepassing — De repo volgt het Karpathy LLM Wiki-patroon."*
> *"Operations — Karpathy's drie-operations-pattern (Ingest/Query/Lint), aangevuld met onze File-back-discipline."*

Onze invulling:

| Karpathy-laag | Onze implementatie |
|---|---|
| Raw sources (immutable) | `sources/` (publiek) + Steven's lokale NEN-licentie-folder |
| The wiki (LLM-maintained) | `brain/` + `ontology/` + `output/` |
| The schema (config) | `CLAUDE.md` + `docs/sprint-protocols.md` + `.claude/agents/*.md` |

Onze Brein-subagent (in `.claude/agents/brein.md`) doet al **wat kfchou-skills beogen**:
- Ingest: post-sprint brain-cyclus
- Query: brain-vault navigatie via index + registers
- Lint: gestructureerde health-check (per CLAUDE.md "Lint"-sectie)

**Mogelijke meerwaarde:**
- ✓ Referentie-set van conventies — vergelijking met onze sprint-protocollen
- ✓ Battle-tested lint-rules (kfchou heeft eigen wiki met 94+ artikelen)
- ✓ Mogelijk concrete lint-skill-template die we kunnen vergelijken met onze Brein-cyclus protocol

**Mogelijk geen meerwaarde:**
- ✗ Onze brain-vault is **al actief** met 115+ markdown-bestanden, 12+ D-decisions, 14+ sprints
- ✗ Onze Brein-subagent is **gespecialiseerd voor ons domein** (GRC + ontologie + multi-chat-architectuur)
- ✗ Installatie zou een tweede lint-pipeline introduceren — potentiële discipline-conflict met sprint-protocollen v1.3

**GO/HOLD/NO-GO**

🟡 **HOLD voor installatie — GO voor passieve referentie**

**Aanbevolen aanpak:**
- **Niet installeren** als skill — zou onze Brein-subagent-workflow doorkruisen
- **Wel lezen** kfchou's wiki-conventies (READMEs, AGENTS.md-spec, SKILL.md-templates) als referentie voor onze eigen Brein-cyclus
- **Mogelijk afgeleid werk:** vergelijking van kfchou's lint-rules met onze sprint-protocollen → identificatie van eventuele gaps in onze methode-discipline
- **File-back-discipline:** als kfchou-vergelijking concrete verbeterpunt voor onze Brein-cyclus oplevert → file-back als concept-update of nieuw protocol

**Waarom geen full GO:**
- Volledige adoptie zou conflict met Brein-subagent + sprint-protocollen v1.3 opleveren
- Onze workflow heeft project-specifieke disciplines (D-decisions, H-items, scope-pauzes) die generieke wiki-skills niet kennen
- 115+ brain-bestanden is voorbij het punt waar generieke skill-templates significant meerwaarde leveren

**Waarom geen NO-GO:**
- Karpathy-pattern als methodologische basis is goed — referentie blijft waardevol
- Kfchou's "wiki status — health report" (categories, page counts, depth-violation count, soft-ceiling indicator, quality rollup, last ingest, drift, recent ingester-reported issues, fork-asymmetry) is een interessante lint-output-structuur

---

## 3. Samenvatting + aanbeveling

| # | Skill | Tier | Recommendation | Korte reden |
|---|---|---|---|---|
| 1 | Sushegaad/Claude-Skills-GRC | T1 | 🟡 HOLD | Coverage-overlap; NEN-discipline-risico onbekend; geen NL-context |
| 2 | GRCEngClub/claude-grc-engineering | T1 | 🟢 NO-GO Spoor A / 🟡 HOLD Spoor B | Past niet bij huidige fase; relevant bij Spoor B lab-test |
| 3 | fabio-rovai/open-ontologies (MCP) | T2 | 🟡 HOLD + evaluatie-sprint plannen | Drie H-items (H37 + H38 + H41) hebben dit als trigger-kandidaat |
| 4 | kfchou/wiki-skills | T2 | 🟡 HOLD installatie + 🟢 GO passieve referentie | Wij doen Karpathy-pattern al; referentie-waarde wel aanwezig |

## 4. Concrete vervolgstappen

### Onmiddellijk (geen impact)

1. **Geen installatie** van skills in Claude Code-omgeving op dit moment
2. **Status van H37 update naar "active geparkeerd, evaluatie-kandidaat gekoppeld aan H41"** — overweging voor brein-cyclus iteratie 15
3. **GRCEngClub-kandidatuur expliciet bevestigd voor Spoor B** — overweging voor brain__scope__-bestand of nieuw H-item

### Middellange termijn (na T3 m14-sprint)

4. **T-evaluatie-sprint plannen:** open-ontologies-MCP-installatie + reasoning-test op `grc-v4_6_2-merged.ttl`
   - Doel: H37 + H38 + H41 gelijktijdig vooruithelpen
   - Output: evaluatie-rapport in `output/reports/skill-eval-open-ontologies-<datum>.md`
   - Geen migratie-besluit — alleen empirisch onderzoek

### Optioneel (geen prioriteit)

5. **kfchou-conventie-vergelijking:** download kfchou-repo README + SKILL.md-templates, vergelijk met onze Brein-cyclus + sprint-protocols → file-back-voorstel indien gaps gevonden
6. **Sushegaad-test** op één niet-gedekt framework (bv. ISO 42001 of CSRD) als M19 ooit in scope komt

---

## 5. Werkstroom-status na deze evaluatie

| Item | Status |
|---|---|
| Skill-evaluatie Tier 1 + Tier 2 | ✓ afgerond (dit rapport) |
| Skills daadwerkelijk geactiveerd | ✗ geen — dit is masterchat-evaluatie, geen Claude Code-installatie |
| Nieuwe H-items | Geen — H37 + H41 bestaan al; overweging voor status-verfijning |
| Brain-vault-update nodig? | Optioneel — als je dit rapport in brain-vault wilt opnemen: `brain__concepts__skill-ecosystem-evaluatie-2026-05-27.md` of vergelijkbaar |

---

*Einde quick-scan evaluatie. Geen sprint-protocollen actief; dit is exploratief masterchat-werk, geen ontologie-mutatie.*
