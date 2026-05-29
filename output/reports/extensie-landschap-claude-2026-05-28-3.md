
# Extensie-oppervlakte Claude × Claude Code voor het GRC Kennismodel — 28 mei 2026

**Type:** Uitputtende extensie-oppervlakte-analyse Claude × Claude Code
**Scope:** Domeinen A–I (zie onderzoeks-prompt). **Dit bestand is COMPLEET: installment 1 (A + D + I, herzien op de autonomie-koers van 28-05-2026), installment 2 (E + H), installment 3 (B + C), installment 4 (F + G) + eind-samenvatting A–I + vervolgstappen + werkstroomstatus.**
**Doel:** GO/HOLD/NO-GO per mogelijkheid, gewogen tegen toegevoegde waarde
**Status:** Analyse-chat-deliverable; geen sprint-mutatie, geen ontologie-impact, geen architectuurbesluit. Aanbevelingen gaan naar masterchat.

> **Lever-fasering (Optie A, voltooid 28 mei 2026):**
> - **Installment 1 (✓, herzien 28-05-2026):** A + D + I — herwogen op de operating-model-koers-correctie (zie §0.5)
> - **Installment 2 (✓):** E (MCP-servers) + H (ontologie-/taxonomie-tooling)
> - **Installment 3 (✓):** B (claude.ai-features) + C (Anthropic-native skills)
> - **Installment 4 (✓):** F (Obsidian + plugins) + G (GRC-community-tooling) + eind-samenvatting + vervolgstappen + werkstroomstatus
>
> Per installment staat een deel-samenvatting; de geconsolideerde eind-samenvatting (A–I) staat onderaan.

---

## 0. Werkwijze + scope-disclaimer + evaluatiecriteria

### 0.1 Onderzoeksmethode

STAP 0 ("bouw voort, herontdek niet") uitgevoerd vóór nieuw onderzoek:

- **Repo-grounding via GitHub-MCP** (`stevenbouw/grc-kennismodel`, ref `afefe8e…`, gelezen 28 mei 2026): `CLAUDE.md` (incl. §Skills-ecosystem-positionering, §Optional tooling, niet-aanbevolen-lijst), `.claude/agents/tech.md`, repo-root + `output/reports/`-listing.
- **Projectinstructie v1.10** (27 mei 2026) in context: missie/visie/invarianten, D1–D12 + D4.1, 17 sprint-protocollen + Protocol v1.3-draft, scope-discipline.
- **Bestaand eval-rapport** `skill-eval-tier1-tier2-2026-05-27.md` aangeleverd door Steven en gelezen — de vier eerdere verdicten (Sushegaad 🟡, GRCEngClub 🟢 NO-GO A/🟡 HOLD B, open-ontologies-MCP 🟡, kfchou 🟡/🟢-referentie) worden in installments 2 en 4 her-gevalideerd, niet her-ontdekt.
- **Feature-landschap geverifieerd tegen officiële bron** (`code.claude.com/docs`, geraadpleegd 28 mei 2026) plus gedateerde community-bronnen. Mijn kennisgrens is januari 2026; alle Claude-Code-features zijn behandeld als mogelijk-verouderd-tenzij-geverifieerd.

### 0.2 Scope-disclaimer

Publieke documentatie + community-content is **geen vervanger voor een installatie-test**. Elk oordeel is "informed assessment", niet "geverifieerd in de werkomgeving". Waar de officiële docs en community-bronnen verschillen (bv. exact aantal hook-events: bronnen noemen 10/12/17/21/24), is de officiële `code.claude.com`-referentie leidend en label ik het verschil expliciet. Onzekerheid wordt gelabeld; niet als feit gepresenteerd.

### 0.3 Beslis-rubriek (consistent toegepast)

Per kandidaat vijf criteria, score **1 (laag) – 5 (hoog)**:

1. **Waarde** — concreet probleem/chat/spoor dat het oplost
2. **Effort** — installatie + onderhoud + migratiekost (hoog = veel effort = láge score)
3. **Invarianten** — lokaal-draaibaar (productie) · mens-in-controle als toezicht/uitlegbaarheid/override (géén black-box) · NEN-discipline · security/secret-hygiëne · D9-framework-neutraliteit (hoog = past goed bij invarianten). **Let op (zie §0.5):** "geen autonome commits / mens-per-stap" is hercodeerd van *terminale invariant* naar *transitionele begin-fase-controle met geplande sunset*; het telt niet langer mee als reden om autonomie af te wijzen.
4. **Overlap/conflict** — botsing met brain-vault, sprint-protocollen, formele modellering (hoog = lage botsing)
5. **Reversibiliteit** — makkelijk terug te draaien? (hoog = goed reversibel)

GO/HOLD/NO-GO volgt uit de score, gesplitst Spoor A / Spoor B waar relevant. Emoji-conventie: 🟢 GO · 🟡 HOLD · 🔴 NO-GO.

### 0.4 Recency-cutoff

Onderzoek uitgevoerd 28 mei 2026. Claude Code-CLI-referentiepunt: v2.1.150 (community-cheat-sheet, 24 mei 2026). Het ecosysteem beweegt wekelijks; features gemarkeerd "experimenteel" of "research preview" kunnen vóór activering wijzigen — her-verifiëren bij daadwerkelijke inzet.

### 0.5 Operating-model-trajectorie (koers-correctie 28 mei 2026)

De projecteigenaar (Steven) heeft verduidelijkt dat het **einddoel een autonoom systeem is waarin géén mens-per-stap vereist is**. De huidige "geen autonome commit"-regel + de mens-als-verplichte-tussenmens waren **bewust transitioneel**: bedoeld om in de beginfase te leren hoe Claude Code en claude.ai samenwerken en om de controle in die fase te behouden. Het is geen terminale invariant.

Dit herweegt het hele rapport. Concreet:

- **Hercodering criterium 3:** "geen autonome commits / mens-per-stap" is geen reden meer om een mechanisme af te wijzen. Autonome commits en autonome acties zijn op termijn het doel, niet de uitzondering.
- **Behouden invariant — en dit is geen detail.** De projectinstructie v1.10 (§Architectuur-invarianten / visie) stelt expliciet: *"Geen black-box-AI — alleen uitlegbare AI mag worden ingezet. De mens moet altijd degene zijn die in controle is."* Steven heeft gevraagd de **per-stap-poort** te verwijderen — niet uitlegbaarheid of menselijk toezicht. De productieve lezing die dit rapport hanteert: **per-stap-approval weg, maar autonomie-met-toezicht blijft** — uitlegbaar, auditeerbaar, override-baar, en deterministisch geverifieerd. Pure black-box-autonomie zou de invariant schenden; autonomie-onder-deterministische-guardrails niet.
- **De brug tussen beide (kernsynthese van dit rapport).** De academische literatuur over LLM-ondersteunde ontologie-engineering (zie domein H: Salovsky 2026, ARIA-gatekeeper-architectuur, OWL+SHACL-combinatie) convergeert op één principe: *"maak niet de LLM deterministisch, maak de verificatie deterministisch."* Dat is precies wat een mens-per-stap nu doet (de mens is de verificatie-poort) — en wat in een autonoom systeem wordt overgenomen door **deterministische guardrails (hooks), deterministische verificatie (SHACL-split + canonical-metrics) en een audit-trail**. Dit project bouwt een GRC-model dat zélf audit-trails produceert; een autonome build-pijplijn die haar eigen acties hook-logt is daarmee zelf auditeerbaar — methode en missie vallen samen. Daarom verschuift het zwaartepunt van mechanismen die autonomie blokkeren naar mechanismen die autonomie *veilig en aantoonbaar* maken.

> **Eerlijke flag (Analyse-rol-grens):** het formeel wijzigen van het operating-model — van "geen autonome commit + mens-per-stap" naar "autonomie-met-toezicht" — raakt gedocumenteerde projectbesluiten (o.a. CLAUDE.md "subagents committen nooit zelfstandig", de scope-pauze-route in `tech.md`, sprint-protocol-werkproces) **en de visie-invariant**. Dat is een **masterchat-architectuurbesluit**, niet iets dat de Analyse-chat vaststelt. Aanbeveling: formaliseer de nieuwe koers als nieuw D-besluit of scope-besluit, met een **expliciete definitie van wat "mens-in-controle" betekent in de autonome eindfase** (toezicht/override/audit op doel- en uitkomstniveau i.p.v. per-stap-approval). Tot die formalisering hanteert dit rapport de koers als richting, niet als vastgesteld feit.

---

## DOMEIN A — Claude Code kern-extensiemechanismen

### A.0 Het actuele mechanisme-landschap (officiële ankerlijst)

Per `code.claude.com/docs/en/features-overview` (officieel, geraadpleegd 28 mei 2026) kent Claude Code de volgende extensielagen:

| Mechanisme | Wat het doet | Laad-moment / context-kost |
|---|---|---|
| **CLAUDE.md** (+ `.claude/rules/`) | Persistente context elke sessie; rules zijn path-scopebaar | Sessiestart, volledig — elke request |
| **Skills** | Herbruikbare kennis + aanroepbare workflows (`/<naam>`); model- of handmatig-getriggerd | Beschrijvingen bij start, volledige inhoud bij gebruik (laag) |
| **Code intelligence (LSP)** | Language-server-navigatie + diagnostics | Na file-edits / on-demand (laag) |
| **MCP** | Koppeling naar externe services/tools | Tool-namen bij start, schema's deferred (laag; tool-search default aan) |
| **Subagents** | Geïsoleerde sub-loops, retourneren samenvatting | On-demand; eigen contextvenster |
| **Agent teams** | Coördinatie van meerdere onafhankelijke sessies (gedeelde takenlijst + peer-messaging) | On-demand; **experimenteel, default uit** |
| **Hooks** | Script/HTTP/prompt/subagent op lifecycle-events | Op trigger; context-kost nul tenzij output |
| **Plugins + marketplaces** | Bundeling + distributie van bovenstaande | Installatie-eenheid |

*Bron: code.claude.com/docs/en/features-overview (officieel, 28-05-2026).*

**Kernobservatie voor dit project (uit `.claude/`-inspectie via GitHub-MCP, 28-05-2026):** de repo benut **CLAUDE.md** + **drie subagents** (`.claude/agents/tech|brein|dashboard.md`) + **GitHub-MCP**. De mappen `.claude/skills/`, `.claude/commands/`, `.claude/hooks/` en een `.claude/settings.json` **ontbreken**. Dat is geen tekortkoming op zich — maar de lege ruimte mapt opvallend precies op een aantal bestaande, gedocumenteerde pijnpunten (Protocol 14, canonical-metrics-discipline, het PAT-incident, scope-pauze-handhaving). Dáár zit de waarde, niet in "alles invullen".

> **Nieuw t.o.v. mijn kennisgrens (jan 2026), geverifieerd:** Agent teams (feb 2026), `.claude/rules/` met path-frontmatter, bundled skills `/code-review` `/batch` `/debug`, `disable-model-invocation`/`skillOverrides`, `context: fork` voor skills, native-binary-installatie (npm gedeprecieerd), Agent View (`claude agents`) + `/goal` (research preview, community-cheat-sheet 24-05-2026).

---

### A.1 CLAUDE.md + `.claude/rules/`

**Inventarisatie**

| Aspect | Waarde |
|---|---|
| Herkomst | Officieel Claude Code-kernmechanisme |
| Status | GA |
| Huidige invulling | `CLAUDE.md` v1.5 (19,3 kB) + `brain/brain__CLAUDE.md` (vault-spec) |
| Volgende volwassenheidsstap | CLAUDE.md is ~groot; docs adviseren **<200 regels** en reference-materiaal naar skills/`.claude/rules/` te verplaatsen |
| `.claude/rules/` | NIEUW: per-sessie of bij matchende file-paden ladende regelbestanden met `paths`-frontmatter — bespaart context |
| Bron | code.claude.com/docs/en/features-overview + /en/memory (officieel, 28-05-2026) |

**NEN-discipline-risico:** 🟢 nul (eigen projectcontext, geen normtekst).

**Overlap/toepasbaarheid:** Raakt alle drie subagents. Concreet: CLAUDE.md draagt nu zowel "altijd-aan"-regels (D9, geen organisatienaam, NEN-discipline) als veel reference-materiaal (repo-structuur, Karpathy-laag, optional tooling). De docs-richtlijn pleit voor splitsing: invarianten in CLAUDE.md, path-gebonden regels in `.claude/rules/` (bv. een rule die alléén laadt bij `ontology/*.ttl`-werk met D1–D12-conformance, of bij `output/reports/*` met patch-rapport-structuur). Dat verlaagt context-kost per sessie en maakt de "altijd-aan"-laag scherper. Geen conflict met brain-vault — `.claude/rules/` is de schema-laag, niet de wiki-laag.

**Rubriek-score:** Waarde 4 · Effort 4 (laag, herstructurering) · Invarianten 5 · Overlap 5 · Reversibiliteit 5.

**🟢 GO (Spoor A en B).**
- *Waarom geen HOLD:* puur additief/herstructurerend, nul invariant-risico, direct nut (kleinere always-on-context = betrouwbaardere regel-naleving door subagents).
- *Voorbehoud:* geen big-bang. Splits alleen wat aantoonbaar reference-materiaal is; invarianten blijven in CLAUDE.md. Dit is een Brein-/masterchat-taak, geen sprint.

---

### A.2 Skills (`.claude/skills/`)

**Inventarisatie**

| Aspect | Waarde |
|---|---|
| Herkomst | Officieel; "meest flexibele extensie" |
| Status | GA |
| Huidige invulling | **Geen eigen skills** (`.claude/skills/` ontbreekt) |
| Mechaniek | SKILL.md + frontmatter; model-getriggerd óf `/<naam>`; `disable-model-invocation: true` voor handmatig-only; `context: fork` voor isolatie; preloadbaar in subagent via `skills:`-veld |
| Bundled out-of-the-box | `/code-review`, `/batch`, `/debug` |
| Bron | code.claude.com/docs/en/features-overview + /en/skills (officieel, 28-05-2026) |

**NEN-discipline-risico:** 🟢 voor eigen-gebouwde GRC/ontologie-skills mits parafrase-discipline; het mechanisme zelf draagt geen content.

**Overlap/toepasbaarheid:** Dit is dé onbenutte hoofdas. Skills zijn precies het juiste mechanisme voor de project-specifieke, herhaalde workflows die nu in proza in CLAUDE.md/sprint-protocollen staan (canonical metrics, gesplitste SHACL, patch-rapport-structuur, SKOS-classificatie, brain-lint). Concrete kandidaten worden uitgewerkt in **domein D**. Belangrijk onderscheid uit de docs: *reference-skill* (kennis, bv. D-decision-conventies) vs *action-skill* (`/<naam>`-workflow met side-effects → zet `disable-model-invocation: true` zodat alléén jij/Steven hem triggert — sluit aan bij scope-discipline).

**Rubriek-score (mechanisme):** Waarde 5 · Effort 3 · Invarianten 4 (action-skills met side-effects vereisen discipline) · Overlap 4 · Reversibiliteit 5.

**🟢 GO als mechanisme (Spoor A).** De *concrete skills* krijgen elk een eigen GO/HOLD/NO-GO in domein D.
- *Waarom geen NO-GO:* de project-workflow ís al een verzameling herhaalbare procedures; skills zijn de native vorm daarvoor. Reversibel (bestand verwijderen).
- *Waarom geen onvoorwaardelijke GO op alles:* model-invocable skills met side-effects (bv. een skill die files schrijft) kunnen autonomie introduceren die botst met "geen autonome commits". Mitigatie: `disable-model-invocation: true` standaard voor alles met side-effects.

---

### A.3 Slash-commands (`.claude/commands/`)

**Inventarisatie**

| Aspect | Waarde |
|---|---|
| Herkomst | Officieel |
| Status | GA |
| Huidige invulling | Geen (`.claude/commands/` ontbreekt) |
| Mechaniek | `.claude/commands/<naam>.md` (project) of `~/.claude/commands/` (persoonlijk), aangeroepen met `/<naam>`; ondersteunt argumenten/frontmatter. Skills en commands convergeren: een skill is aanroepbaar als `/<naam>` |
| Bron | code.claude.com/docs/en/features-overview; community-cheat-sheet (blakecrosley.com, 24-05-2026) |

**NEN-discipline-risico:** 🟢 nul.

**Overlap/toepasbaarheid:** De 17 sprint-protocollen zijn deels deterministische checklists die zich lenen voor `/<naam>`-commands — bv. `/presprint-inventarisatie` (Protocol 1), `/patch-rapport-check` (§0–§13-skelet + §9 geparkeerde-items), `/disclosure-check` (Protocol 14 vijf categorieën). Belangrijk: commands/skills zijn *prompted* (Claude interpreteert), dus geschikt voor protocollen die redenering vragen — níet voor protocollen die gegarandeerd moeten vuren (dáárvoor hooks, zie A.5).

**Rubriek-score:** Waarde 4 · Effort 4 · Invarianten 4 · Overlap 5 · Reversibiliteit 5.

**🟢 GO (Spoor A), gefaseerd.** Begin met de protocollen die nu het meest met de hand worden uitgevoerd (patch-rapport-skelet, pre-sprint-inventarisatie). Zie domein D voor de uitwerking "17 protocollen → commands vs hooks".

---

### A.4 Subagents (`.claude/agents/`) — huidige invulling

**Inventarisatie**

| Aspect | Waarde |
|---|---|
| Herkomst | Officieel |
| Status | GA |
| Huidige invulling | **In gebruik:** `tech.md`, `brein.md`, `dashboard.md` (YAML-frontmatter, `model: claude-opus-4-7`, tools Read/Write/Edit/Bash/Glob/Grep) |
| Mechaniek | Eigen contextvenster; `skills:`-veld preloadt skills; tot 10 parallel; scope managed > CLI > project > user > plugin |
| Volgende stap | `skills:`-preloading benutten zodra eigen skills bestaan; per-subagent tool-permissions aanscherpen |
| Bron | code.claude.com/docs/en/sub-agents; community-cheat-sheet (24-05-2026); `.claude/agents/tech.md` (repo, 28-05-2026) |

**NEN-discipline-risico:** 🟢 (tech.md draagt expliciet de NEN-escalatieroute; sinds Protocol 17 lokale NEN-toegang met parafrase-discipline).

**Overlap/toepasbaarheid:** Dit is een sterk punt van de huidige opzet en hoeft niet te veranderen. Twee volwassenheidsstappen: (1) zodra eigen skills bestaan, het `skills:`-veld gebruiken om elke subagent zijn vaste discipline-skills te laten preloaden (bv. tech → canonical-metrics + SHACL-split skill); (2) tool-permissions per subagent expliciet beperken (Dashboard hoeft geen `ontology/`-write; tech hoeft geen `dashboard/`-write — staat nu als prozaregel in de config, kan hard via settings/permissions, zie A.8).

**Rubriek-score:** Waarde 5 · Effort 5 (al gedaan) · Invarianten 5 · Overlap 5 · Reversibiliteit 5.

**🟢 GO — reeds in gebruik; doorontwikkelen.** Geen wijziging aan de rolscheiding nodig; wel `skills:`-preloading en harde permission-scoping als incrementele verbetering.

---

### A.5 Hooks (`.claude/settings.json` → `hooks`)

**Inventarisatie**

| Aspect | Waarde |
|---|---|
| Herkomst | Officieel |
| Status | GA |
| Huidige invulling | **Geen** (`settings.json` ontbreekt) |
| Lifecycle-events (officieel, drie cadansen) | per-sessie: `SessionStart`, `SessionEnd`; per-turn: `UserPromptSubmit`, `Stop`, `StopFailure`; per-tool: `PreToolUse`, `PostToolUse` (+ o.a. `SubagentStop`, `PreCompact`, `PermissionRequest`, `Notification` — exact aantal varieert per bron 10–24; officiële referentie leidend) |
| Handler-types | command (shell), HTTP, prompt (LLM, Haiku default), agent (subagent) |
| Determinisme | `PreToolUse` exit-code 2 = **block** (de tool-call gaat niet door). Hooks vuren gegarandeerd op hun event |
| Bron | code.claude.com/docs/en/hooks (officieel, "Hooks reference"); SmartScope/Pixelmojo/blakecrosley (community, mrt 2026) |

**NEN-discipline-risico:** 🟢 — sterker nog, hooks zijn een *mitigatie* van NEN-risico (zie hieronder).

**Overlap/toepasbaarheid — dit is de hoogste-waarde-vondst van domein A, en de koers-correctie maakt hem groter, niet kleiner.** In een mens-per-stap-regime is de mens de veiligheidspoort. Zodra die poort verdwijnt (§0.5), worden **hooks + audit-trail dé veiligheidspoort** — het deterministische verificatielaag die de mens-per-stap vervangt. Hooks zijn daarmee niet langer "de handhaver van geen-commit", maar de **randvoorwaarde die autonome commits veilig en aantoonbaar maakt**:

- **Secret-hygiëne (PAT-incident) — kritischer zonder mens.** Een `PreToolUse`/pre-push-hook die `run_secret_scanning` (Anthropic levert dit; ook beschikbaar als `grc-kennismodel:run_secret_scanning` MCP-tool) of een regex-scan draait en bij een hit blokkeert, had het gelekte PAT tegengehouden. In een autonoom systeem is er **geen mens meer die dit per ongeluk opvangt** — dit verschuift van nuttig naar onmisbaar. Dit is een *durable* hook (sunset niet van toepassing).
- **Scope-grens-handhaving (vervangt de scope-pauze-mens deels).** Een `PreToolUse`-hook die een `ontology/*.ttl`-write blokkeert wanneer er geen corresponderende goedgekeurde `instructie-v4.X.Y.md` bestaat, maakt de scope-discipline deterministisch i.p.v. afhankelijk van of de subagent escaleert. Dit is precies hoe je "scope-pauze-discipline" behoudt zónder een mens die elke stap goedkeurt.
- **Audit-trail (maakt autonomie auditeerbaar — methode = missie).** `PostToolUse`/`SessionStart`/`Stop`-hooks die elke tool-call + commit append-loggen naar een audit-bestand, leveren de uitlegbaarheid/aantoonbaarheid die de behouden invariant vereist. Een GRC-model dat audit-trails *produceert* en wiens build-pijplijn zichzelf *audit-logt* is intern consistent. Dit is de concrete invulling van "mens-in-controle als toezicht i.p.v. per-stap".
- **Protocol 14 (disclosure-check, vijf categorieën).** Deterministische *command-hook* voor de hard-detecteerbare categorieën (lokale paden, organisatienaam, e-mail/TLD, credentials) + *prompt-hook* (Haiku) voor de semantische (NEN-tekst >10 woorden). In een autonoom regime draait dit gegarandeerd vóór elke push.
- **SessionStart-context-injectie.** Hook die `brain__log.md` (3 nieuwste entries) + `git status` injecteert — operationaliseert de "Bij sessie-start"-leesvolgorde uit `tech.md` automatisch.
- **Transitioneel (niet durable):** een `PreToolUse`-hook die `git commit`/`git push` blokkeert is bruikbaar in de huidige begin-fase, maar **sunset** zodra de autonome koers geformaliseerd is (§0.5). Bouw hem zó dat hij via een env-flag uit kan, zodat de overgang van "geblokkeerd" naar "toegestaan-mits-checks-groen" één configuratiewijziging is.

**Belangrijke nuance:** de durable hooks vormen samen een **green-gate**: autonome commit/push mag, mits secret-scan + disclosure-check + (waar van toepassing) SHACL/canonical-metrics groen zijn. Dat is "geen mens-per-stap" mét "mens-in-controle" — de mens stelt de gates en reviewt uitkomsten/audit, de pijplijn handelt binnen de gates.

**Rubriek-score:** Waarde 5 · Effort 3 (shell-scripts schrijven + testen) · Invarianten 5 (de hooks ZIJN de operationalisering van de behouden invariant) · Overlap 5 · Reversibiliteit 5 (settings.json-regel verwijderen).

**🟢 GO (Spoor A), hoogste prioriteit binnen domein A — en de fundering onder de autonomie-koers.**
- *Waarom geen NO-GO:* hooks zijn het mechanisme dat autonomie veilig maakt. Zonder deze laag is "geen mens-per-stap" onverantwoord (het PAT-incident bewijst dat prompt-instructie niet volstaat); mét deze laag is het verdedigbaar én auditeerbaar.
- *Waarom geen onvoorwaardelijke GO zonder ontwerp:* de green-gate moet zorgvuldig ontworpen (welke checks blokkeren hard, welke waarschuwen) en getest worden vóór activering; false-positives mogen een autonome pijplijn niet vastzetten. Eerst ontwerp + test, dan activeren. Dit is een masterchat-/Tech-ontwerpvraag.

---

### A.6 Plugins + marketplaces

**Inventarisatie**

| Aspect | Waarde |
|---|---|
| Herkomst | Officieel |
| Status | GA |
| Huidige invulling | Geen eigen plugin; geen marketplace-installs |
| Mechaniek | Plugin = bundeling van skills + hooks + subagents + MCP in één installeerbaar pakket; plugin-skills namespaced (`/plugin:command`); distributie via marketplace (GitHub-repo/npm/intern register) |
| Bron | code.claude.com/docs/en/plugins + /en/plugin-marketplaces (officieel, 28-05-2026); Medium-overview (13-04-2026) |
| **Disambiguatie** | Dit is de **Claude-Code-plugin** (distributie-mechanisme). De **Obsidian-plugin** (vault-uitbreiding) is een geheel andere categorie — zie installment 4, domein F |

**NEN-discipline-risico:** 🟢 voor een eigen-gebouwde plugin (alleen eigen disciplines); 🟡 voor *externe* plugins/marketplaces (zie Sushegaad/GRCEngClub, installment 4 — plugin-marketplace-installatie is hun install-mechanisme).

**Overlap/toepasbaarheid:** Een *eigen* GRC-Kennismodel-plugin (bundeling van de domein-D-skills + hooks + de drie subagent-configs) heeft pas waarde bij **een tweede repo/omgeving** die dezelfde setup nodig heeft. Dat is exact de organisatie-neutraliteit-invariant ("overdraagbaar naar vergelijkbare organisaties") en de Spoor-B-lab-test bij T&I. Voor één repo nu is een plugin overkill: skills + hooks + agents in `.claude/` volstaan zonder bundeling.

**Rubriek-score (eigen plugin):** Waarde 3 (pas bij 2e omgeving) · Effort 3 · Invarianten 5 · Overlap 4 · Reversibiliteit 5.

**🟡 HOLD (Spoor A) — 🟢 GO-kandidaat bij Spoor B / organisatie-overdracht.**
- *Waarom geen GO nu:* één repo heeft geen distributie-probleem; bundeling voegt onderhoud toe zonder huidig nut.
- *Waarom geen NO-GO:* zodra de Spoor-B-lab-test of organisatie-overdracht speelt, is een plugin het natuurlijke "one-click install"-mechanisme dat de organisatie-neutraliteit-invariant operationeel maakt. Parkeer als bekende kandidaat (mogelijk nieuw H-item).

---

### A.7 MCP-servers (in Claude Code)

**Inventarisatie (kort — diepte volgt in installment 2, domein E)**

| Aspect | Waarde |
|---|---|
| Huidige invulling | GitHub-MCP actief (masterchat + subagents); tool-search default aan (idle tools = minimale context) |
| Volgende stap | RDF/SPARQL/SHACL-MCP's + open-ontologies-MCP — volledige behandeling in installment 2 |
| Invariant-let-op | Lokaal-draaibaar (productie zonder cloud-internet); secret-hygiëne; vendor-lock-in |

**🟢 GO als mechanisme (reeds in gebruik via GitHub-MCP).** Specifieke server-kandidaten met GO/HOLD/NO-GO in installment 2.

---

### A.8 Settings.json + permission-rules

**Inventarisatie**

| Aspect | Waarde |
|---|---|
| Herkomst | Officieel |
| Status | GA |
| Huidige invulling | Geen `.claude/settings.json` (permissions staan nu als prozaregel in `tech.md`: "dashboard/** niet aanraken" etc.) |
| Mechaniek | allow/deny tool-regels per scope (local > project > user); host ook hooks-config en env-vars |
| Bron | code.claude.com/docs (officieel); blakecrosley-guide (community, "permissions" als één van vijf kernsystemen) |

**NEN-discipline-risico:** 🟢.

**Overlap/toepasbaarheid:** De rolscheiding tussen subagents is nu *beschreven* maar niet *afgedwongen*. Permission-deny-regels kunnen hard maken wat `tech.md` als prozaregel stelt: tech-subagent `deny` op `dashboard/**` en `.claude/**`, dashboard-subagent `deny` op `ontology/**`, allen `deny` op `git push` (zie A.5). Dit verkleint het oppervlak voor per-ongeluk-cross-domein-edits.

**Rubriek-score:** Waarde 4 · Effort 4 · Invarianten 5 · Overlap 5 · Reversibiliteit 5.

**🟢 GO (Spoor A), samen met A.5 (settings.json host beide).**

---

### A.9 Agent SDK / headless / CI

**Inventarisatie**

| Aspect | Waarde |
|---|---|
| Herkomst | Officieel (Agent SDK, voorheen "Claude Code SDK"); headless via `claude -p` |
| Status | GA (SDK + headless); GitHub Actions/GitLab CI-integratie gedocumenteerd voor hooks/checks |
| Huidige invulling | Geen CI; werkproces is interactief (Steven als tussenmens) |
| Bron | code.claude.com/docs (officieel); Pixelmojo (community, hooks↔GitHub Actions/GitLab CI, 30-03-2026). *SDK-specifics niet diepgaand geverifieerd in deze installment — te verifiëren bij activering* |

**NEN-discipline-risico:** 🟢 mechanisme; 🟡 bij CI als verificatie-scripts NEN-bron-toegang zouden vereisen (dat moet lokaal/handmatig blijven).

**Overlap/toepasbaarheid:** Headless/CI is dé natuurlijke uitvoeringslaag voor een autonoom systeem (§0.5). De canonical-metrics + SHACL-split-validatie als **green-gate-check op elke push/PR** (draait de Python-toolchain, vergelijkt met vorige `canonical_metrics_*.json`, faalt bij onverwachte triple-Δ) is precies de deterministische verificatie die de mens-per-stap vervangt. Onder de oude premisse was autonoom-mergen een invariant-conflict; onder de nieuwe koers is het het **doel** — mits gated. De nuance verschuift dus van "wel/niet autonoom" naar "**autonoom mergen alléén achter groene deterministische checks + audit-trail, nooit op rood of onbekend**". Twee resterende aandachtspunten: (1) **lokaal-draaibaar** — GitHub Actions is cloud-CI; voor Spoor A (publiek, geen organisatiedata) acceptabel, maar bij Spoor B/organisatiedata heroverwegen naar on-prem CI (GitLab-runner/organisatie-intern), consistent met de CLAUDE.md "Spoor B-overweging". (2) **mens-in-controle als toezicht** — de mens definieert de gates en reviewt de audit/uitkomsten; dat blijft, ook bij autonoom mergen.

**Rubriek-score:** Waarde 4 · Effort 3 (CI-pipeline opzetten + onderhouden) · Invarianten 4 (cloud-CI vraagt Spoor-B-heroverweging; verder aligned) · Overlap 4 · Reversibiliteit 4.

**🟢 GO-trajectorie (Spoor A) voor een check-gated autonome pijplijn — 🟡 HOLD voor cloud-CI bij Spoor B (on-prem heroverwegen).**
- *Waarom geen onvoorwaardelijke GO nu:* bouw eerst de green-gate-hooks (A.5) en de verificatie-skills (D.1/D.2); CI is de laag erbovenop. Autonoom mergen pas activeren als de deterministische checks bewezen betrouwbaar zijn (geen false-positive-blokkades, geen false-negative-doorlaat).
- *Waarom geen NO-GO meer (gewijzigd t.o.v. pre-correctie):* autonoom mergen is niet langer een invariant-conflict maar het ontwerpdoel; de eerdere 🔴 NO-GO op auto-merge is opgeheven en vervangen door de green-gate-voorwaarde.

---

### A.10 Overige mechanismen (kort, met onzekerheidslabels)

| Mechanisme | Status / oordeel |
|---|---|
| **Code intelligence (LSP)** | GA. 🔴 NO-GO praktisch — bedoeld voor getypeerde codebases; dit project is Turtle/Python-scripts, geen symbol-navigatie-probleem. Geen waarde. |
| **Checkpointing / rewind / Agent View / `/goal`** | Research preview (community-cheat-sheet 24-05-2026, v2.1.150). 🟡 HOLD — nuttig als interactieve veiligheidsnet/operatiescherm, maar research-preview-status = her-verifiëren; geen invariant-impact. *Status onzeker, te verifiëren bij activering.* |
| **Custom statusline / background tasks** | GA. 🟡 HOLD — kwaliteit-van-leven; geen projectprobleem dat ze oplossen. |
| **Output styles** | ⚠ **Status onzeker.** Output styles bestonden in eerdere Claude Code-versies maar staan **niet** in de huidige officiële `features-overview`-ankerlijst (28-05-2026). Mogelijk verouderd/vervangen. 🟡 HOLD met expliciet voorbehoud: niet bouwen op vóór status geverifieerd is in de live docs. Geen aanname als feit. |

---

## DOMEIN D — Zelf bouwen (concrete kandidaten)

Per kandidaat: bouw-effort + onderhoudslast + waarde, en GO/HOLD/NO-GO. Mechanisme-keuze (skill vs slash-command vs hook) volgt de docs-regel: **deterministisch-altijd → hook; redenering/kennis → skill; handmatige workflow → command/action-skill.**

### D.1 canonical-metrics-meetmethode-skill

**Wat:** reference+action-skill die de canonieke meetmethode codificeert (`owlrl.DeductiveClosure(OWLRL_Semantics, axiomatic_triples=False, datatype_axioms=False)`, NamedIndividual-telmethode, zes invariantie-metrics, versie-suffix-conventie) en als `/canonical-metrics`-workflow het script genereert/draait + JSON wegschrijft.
**Effort:** laag (de methode staat al uitgespeld in `tech.md` + sprint-protocollen). **Onderhoud:** laag. **Waarde:** hoog — borgt "§0 uit JSON, niet uit memorie" (leerpunt v4.3.3) en de canonieke instellingen tegen drift.
**Invarianten:** 🟢 lokaal-draaibaar (Python), mens-in-controle (Steven commit), geen NEN-content. **Reversibel:** ja.
**Score:** Waarde 5 · Effort 4 · Invarianten 5 · Overlap 5 · Reversibiliteit 5. **🟢 GO (Spoor A).** Beste eerste eigen skill — hoog nut, nul invariant-risico, dekt een gedocumenteerd leerpunt.

### D.2 gesplitste-SHACL-validatie-skill

**Wat:** action-skill `/shacl-split` die SECTIE A (`inference='none'`) en SECTIE B (`inference='owlrl'`) gescheiden draait en de bekende 290 COMBINED-false-positives expliciet als verwacht markeert.
**Effort:** laag. **Onderhoud:** laag. **Waarde:** hoog — voorkomt de terugkerende "290 = bug?"-verwarring; codificeert verplichte split.
**Score:** Waarde 5 · Effort 4 · Invarianten 5 · Overlap 5 · Reversibiliteit 5. **🟢 GO (Spoor A).** Bundel logisch met D.1 (samen: "release-verificatie-skill").

### D.3 patch-rapport-generator-skill

**Wat:** action-skill `/patch-rapport` die het §0–§13-skelet genereert, §0 dwingend uit `canonical_metrics_*.json` vult, en §9 (geparkeerde-items, Protocol 10) + §11 (deliverables-tabel, Protocol 16) afdwingt.
**Effort:** midden (skelet + JSON-koppeling). **Onderhoud:** midden (skelet evolueert met protocollen). **Waarde:** hoog — borgt structuur-consistentie en de "uit JSON"-discipline.
**Score:** Waarde 5 · Effort 3 · Invarianten 5 · Overlap 4 · Reversibiliteit 5. **🟢 GO (Spoor A).**

### D.4 SKOS-classificatie-skill

**Wat:** reference+action-skill die D4 + **D4.1** (disclaimer-handling) + beoordelings-protocol v1.2/v1.3 + cluster-discipline codificeert: gegeven een ctrl↔compl-paar, leid de juiste predicate af (exact/close/broad/narrow/related) met de C1–C3-criteria en de D4.1-disclaimer-regel (ENISA TIG R285 → geen exactMatch).
**Effort:** midden-hoog (de logica is genuanceerd; helper-script-classificatie is autoritatief per Protocol v1.3 §10.4). **Onderhoud:** midden. **Waarde:** hoog voor T3 (m14-paren) en latere T-sprints — borgt consistente toepassing.
**Invarianten:** 🟡 NEN-let-op — de skill mag géén verbatim ISO/NEN-tekst dragen; alleen de *methode* + clausule-verwijzing. Helper-script blijft autoritatief boven skill-oordeel.
**Score:** Waarde 5 · Effort 3 · Invarianten 4 · Overlap 4 · Reversibiliteit 5. **🟢 GO (Spoor A), maar bouwen wanneer T3 concreet wordt** (de skill is dan empirisch te toetsen aan de m10-precedent). Tot dan: 🟡 HOLD-on-timing.

### D.5 brain-vault-update-/lint-skill

**Wat:** action-skills voor de Karpathy Ingest/Query/Lint/File-back-operaties: `/brain-lint` (contradicties tussen registers, stale H-items, orphans, missing cross-refs, outdated baseline-cijfers) met severity-tiered output zoals de CLAUDE.md "Lint"-sectie al beschrijft.
**Effort:** midden. **Onderhoud:** midden. **Waarde:** midden-hoog — operationaliseert wat de Brein-subagent nu als prozaprocedure doet; maakt lint herhaalbaar/aanroepbaar.
**Overlap/conflict:** 🟡 — kfchou/wiki-skills (installment 4) doet iets vergelijkbaars; risico op twee lint-pijplijnen. Aanbeveling: één eigen lint-skill die kfchou's lint-rules als *referentie* gebruikt, geen tweede systeem.
**Score:** Waarde 4 · Effort 3 · Invarianten 5 · Overlap 3 · Reversibiliteit 5. **🟡 HOLD → 🟢 GO na kfchou-conventie-vergelijking** (installment 4). Niet twee lint-systemen bouwen.

### D.6 sprint-protocol-handhaving via hooks + slash-commands

**Wat:** de 17 protocollen splitsen naar het juiste mechanisme:
- **Hooks (deterministisch-altijd):** Protocol 14 disclosure-check (PreToolUse/pre-push); "geen autonome commit" (PreToolUse-block); secret-scan (PAT-incident); versie-suffix-conventie-check op output-filenames (PostToolUse).
- **Action-skills/commands (redenering/workflow):** Protocol 1 pre-sprint-inventarisatie, Protocol 10 §9-update, patch-rapport-skelet (D.3), Protocol 15 werkbare-applier-template, Protocol v1.3 §10.2 bottom-up rapport-bouw.
- **Reference-skills/rules (kennis):** D1–D12-conformance (`.claude/rules/` bij `ontology/*.ttl`), bron-typo-beleid (Protocol 13).
**Effort:** midden (cumulatief). **Waarde:** hoog — dit is de systematische vertaling van "prozaprotocol" naar "afgedwongen/aanroepbaar".
**Score:** Waarde 5 · Effort 3 · Invarianten 5 · Overlap 4 · Reversibiliteit 5. **🟢 GO (Spoor A), gefaseerd** — begin met de hook-categorie (hoogste invariant-waarde), dan de meest-herhaalde commands.

### D.7 GRC-domein-skill (NL-kaders)

**Wat:** reference-skill met de Nederlandse/Rijksoverheid-kaders die externe skills (Sushegaad e.a.) **missen**: BIO 2.0, VIR 2007, VIRBI 2025, CBW (in voorbereiding), Cbb (concept TK), ENSIA, COSO ICF/ERM, COBIT 2019, BVA-stelsel, CIO-stelsel — als parafrase + artikel/clausule-verwijzing, framework-neutraal (D9).
**Effort:** midden-hoog (zorgvuldige parafrase, status-discipline CBW/Cbb). **Onderhoud:** midden (wetgeving-in-voorbereiding wijzigt). **Waarde:** hoog en **uniek** — dit is precies de lacune die de eval van Sushegaad benoemde ("geen NL-context"). Vult een gat dat geen externe skill vult.
**Invarianten:** 🟡 NEN-let-op (BIO verwijst naar ISO 27002-attributen — parafrase, geen verbatim NEN); 🟢 D9 (alle kaders gelijkwaardig); 🟢 status-discipline (CBW "in voorbereiding", Cbb "concept").
**Score:** Waarde 5 · Effort 3 · Invarianten 4 · Overlap 5 · Reversibiliteit 5. **🟢 GO (Spoor A en B).** Hoogwaardig en niet-extern-verkrijgbaar. Tegelijk het zwaarste te bouwen; plan ná de verificatie-skills (D.1–D.3).

### D.8 Eigen RDF/SPARQL/SHACL-MCP-server (wrapper om bestaande Python-toolchain)

**Wat:** MCP-server (via mcp-builder) die rdflib+owlrl+pySHACL als tools blootstelt (load/reason/query/shacl-split/canonical-metrics) aan elke Claude-sessie.
**Effort:** hoog (server bouwen + onderhouden). **Onderhoud:** hoog. **Waarde:** midden — overlapt met wat skills (D.1/D.2) al bereiken zonder server-complexiteit; en met open-ontologies-MCP (installment 2) dat dit kant-en-klaar biedt.
**Invarianten:** 🟢 lokaal-draaibaar (eigen Python); maar Simplicity-First pleit tegen een eigen server als een skill volstaat.
**Score:** Waarde 2 · Effort 2 · Invarianten 4 · Overlap 2 (botst met D.1/D.2 + open-ontologies-MCP) · Reversibiliteit 4. **🔴 NO-GO (Spoor A).**
- *Waarom NO-GO:* skills (D.1/D.2) leveren hetzelfde nut zonder server-onderhoud; open-ontologies-MCP (te evalueren, installment 2) levert een kant-en-klare, academisch gevalideerde variant. Een eigen MCP-wrapper is dubbel werk dat de Simplicity-First-discipline schendt.
- *Waarom niet permanent uitsluiten:* als de open-ontologies-evaluatie negatief uitvalt én skills tekortschieten voor cross-sessie tool-toegang, kan dit heroverwogen worden — maar dat is een ver, voorwaardelijk scenario.

---

## DOMEIN I — Multi-agent / orchestratie + kritiek op de zeven-chat-opzet

### I.1 De huidige opzet, eerlijk beoordeeld

**Wat er staat:** 4 chats in claude.ai (Master, Documentatie, Analyse, Asset) + 3 subagents in Claude Code (Tech, Brein, Dashboard), met Steven als verplichte tussenmens bij scope-pauzes en commits.

**Wat sterk is:**
- De rolscheiding is scherp en gedocumenteerd; subagents hebben eigen contextvensters (geen context-blowout).
- Git + `brain__log.md` als shared-state-timeline is een degelijk coördinatiemechanisme zonder externe afhankelijkheid.
- De scheiding "strategisch/conversationeel (claude.ai) vs. uitvoerend/geïsoleerd (Claude Code)" volgt de officiële docs-heuristiek correct.

**Wat onder de nieuwe koers (§0.5) verandert:**
1. **Steven-als-tussenmens is bewust transitioneel — en nu juist het te automatiseren onderdeel.** In de begin-fase was de handmatige Master→Tech→Brein-overdracht via Steven de controle-borging. Onder de autonomie-koers is dit precies de bottleneck die wegmoet. De vraag is niet langer "hoe houden we de mens-per-stap betrouwbaar" maar "**welk orchestratie-substraat neemt de coördinatie over zonder de toezicht-/audit-invariant te verliezen**".
2. **De claude.ai↔Claude-Code-grens blijft een wrijvingspunt** (repo + copy-paste + "Anthropic bug #33875"-PK-sync). Een autonome uitvoeringslaag binnen Claude Code (waar repo-state native gedeeld wordt) verkleint die grens.
3. **De facto hot path is Master + Tech + Brein.** Dat is precies de keten die zich leent voor autonome orchestratie; Documentatie/Analyse/Asset blijven mens-facing/strategisch.

### I.2 Alternatieven, gewogen tegen de invarianten (herwogen op de autonomie-koers)

**(a) Claude Code-subagents vs. losse claude.ai-chats.** De docs-heuristiek bevestigt de huidige verdeling: subagents voor context-isolatie/uitvoering, chats voor strategisch/conversationeel werk. **Geen wijziging aan de scheiding zelf** — wel verschuift het zwaartepunt van "Steven routeert tussen lagen" naar "de uitvoeringslaag coördineert zichzelf binnen guardrails".

**(b) Agent teams (experimenteel) — onder de nieuwe koers van invariant-conflict naar GO-trajectorie.**

| Aspect | Waarde |
|---|---|
| Status | Experimenteel, **default uit**; activeren via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` in settings.json/env |
| Released | 5 feb 2026, met Opus 4.6 (community-corroboratie: heyuan110, claudefa.st, alexop.dev) |
| Mechaniek | Team-lead + onafhankelijke teammates (elk eigen ~1M-context), gedeelde takenlijst (markdown), mailbox-messaging (tekstbestanden), teammates kunnen elkaar challengen; teammates laden CLAUDE.md + MCP + `.claude/skills/` |
| Bekende limitaties (officieel) | Session-resumption, task-coordination, shutdown-gedrag; geen nesting; vereist tmux/iTerm2 of VS Code-terminal |
| Token-kost | Substantieel — elke teammate = eigen Claude-instance (community-test: 4 Sonnet-agents → credits op in 15–20 min) |
| Bron | code.claude.com/docs/en/agent-teams (officieel, 08-04-2026) + community (mei 2026) |

**Herweging.** Onder de oude premisse was agent teams' zelf-coördinatie een fundamenteel invariant-conflict (mens-per-stap). Onder de nieuwe koers (§0.5) is zelf-coördinatie juist het **doel**. Agent teams zijn daarmee het meest voor de hand liggende native orchestratie-substraat voor de post-mens-per-stap-workflow: een Master-lead die Tech/Brein/Dashboard-teammates spawnt die via gedeelde takenlijst + messaging zelf coördineren — exact de Master→Tech→Brein-keten, maar zonder Steven als handmatige router.

De resterende bezwaren zijn nu **praktisch, niet fundamenteel**:
- **Experimentele status** — limitaties rond shutdown/resumption/coordination; default uit. Niet bouwen op een experimentele feature voor een productiekritische keten vóór hij volwassen is.
- **Token-kost** — elke teammate is een volledige instance; substantieel duurder dan subagents. Voor een budget-bewuste Rijksoverheid-context een reële afweging.
- **Toezicht/audit-invariant (behouden, §0.5)** — agent teams mogen niet *in plaats van* de deterministische guardrails komen, maar *binnen* die envelop draaien. Cruciaal: hooks vuren ook voor teammate-/subagent-acties (o.a. `SubagentStop`; community noemt `SubagentStart`/`TeammateIdle` voor team-lifecycle), dus de green-gate (A.5) + audit-trail blijven gelden. Zo coördineert het team zichzelf, maar binnen deterministisch afgedwongen grenzen die de mens heeft gezet en kan reviewen.

🟡 **HOLD-op-volwassenheid → 🟢 GO-trajectorie (Spoor A), gesequenced ná de guardrail-laag.**
- *Waarom nog geen GO:* (1) experimentele status — wachten tot de feature stabiel/GA is; (2) de guardrail-/audit-laag (A.5-hooks + A.8-permissions) moet er éérst zijn, anders is zelf-coördinatie zonder deterministische envelop precies de black-box die de invariant verbiedt; (3) token-kost rechtvaardigt eerst een afgebakende pilot.
- *Waarom geen NO-GO meer (gewijzigd t.o.v. pre-correctie):* zelf-coördinatie is niet langer in strijd met de koers — het ís de koers. De eerdere 🔴 NO-GO-workflow is opgeheven. Concrete eerste stap: een afgebakende, read-only pilot (bv. parallelle SKOS-cluster-challenge: drie teammates beoordelen elk een cluster en challengen elkaars classificaties; uitkomst door masterchat-review) — als opstap naar bredere inzet zodra de feature volwassen is en de guardrails staan.

**(c) Plugin-gebaseerde orchestratie.** Zie A.6 — relevant bij Spoor B/organisatie-overdracht (bundeling van de autonome setup voor een tweede omgeving). 🟡 HOLD.

**(d) Hook-gedreven coördinatie/escalatie — de enabler van veilige autonomie.** In plaats van te vertrouwen op model-naleving van de scope-discipline, dwingt een hook de grens af: een `PreToolUse`-hook die een `ontology/*.ttl`-write blokkeert zonder goedgekeurde `instructie-v4.X.Y.md`, of een green-gate vóór push (A.5). Onder de autonomie-koers is dit niet langer "scope-pauze-naar-mens" maar "**scope-grens-als-deterministische-gate**" — de mens stelt de gate, het systeem handelt erbinnen. Dit is de mechanische invulling van "mens-in-controle zonder mens-per-stap". 🟢 **GO-kandidaat (Spoor A)** — ontwerp-gevoelig (false-positives mogen een autonome pijplijn niet verlammen); behandel als onderdeel van D.6 + A.5.

**(e) Parallelle subagents (binnen huidige model).** Tot 10 subagents parallel, zonder agent teams. Goedkoper dan agent teams (resultaat-samenvatting terug naar lead, geen peer-messaging). Voor veel autonome uitvoering volstaat dit mogelijk — bv. een lead die parallel pre-sprint-inventarisatie over meerdere modules laat draaien. 🟢 **GO-kandidaat (Spoor A)** als goedkoper, minder-experimenteel alternatief voor agent teams waar peer-communicatie niet nodig is. De officiële "transition point": pas naar agent teams als subagents tegen contextlimieten lopen óf onderling moeten communiceren.

### I.3 Aanbeveling domein I

De koers-correctie verandert het antwoord wezenlijk. De winst zit níet meer in "de bestaande mens-per-stap-discipline hard maken en behouden", maar in een **gefaseerde overgang naar een autonome uitvoeringslaag binnen een deterministische toezicht-envelop**:

1. **Eerst de envelop bouwen** (A.5-hooks green-gate + A.8-permissions + audit-trail + D.1/D.2-verificatie-skills). Zonder deze laag is autonomie black-box; mét deze laag is ze auditeerbaar en override-baar — de behouden invariant.
2. **Dan de uitvoeringslaag autonomiseren** — begin met parallelle subagents (I.2-e, goedkoop, GA) voor afgebakend werk; schaal naar agent teams (I.2-b) zodra die volwassen zijn en peer-coördinatie nodig is.
3. **Mens-facing strategisch blijft mens-facing.** Master/Documentatie/Analyse/Asset (claude.ai) blijven de laag waar de mens doelen stelt, uitkomsten reviewt en de audit-trail inspecteert. Dat is "mens-in-controle als toezicht" — precies wat de behouden invariant vraagt.

Het beoogde eindbeeld is dus niet "geen mens", maar **een strategische mens-laag (doel + review + override) boven een zichzelf-coördinerende uitvoeringslaag die binnen deterministische gates en een audit-trail opereert.** Dat verzoent "geen mens-per-stap" (Steven's doel) met "de mens altijd in controle" (de behouden invariant) — en het formaliseren van precies dit eindbeeld is het masterchat-architectuurbesluit dat §0.5 aanbeveelt.

---

## Deel-samenvatting installment 1 (A + D + I)

| # | Kandidaat | Domein | Recommendation | Korte reden |
|---|---|---|---|---|
| A.1 | CLAUDE.md + `.claude/rules/` | A | 🟢 GO | Herstructurering verlaagt always-on-context; nul risico |
| A.2 | Skills (mechanisme) | A | 🟢 GO | Native vorm voor herhaalde project-workflows |
| A.3 | Slash-commands | A | 🟢 GO gefaseerd | Protocollen-als-checklists → `/<naam>` |
| A.4 | Subagents | A | 🟢 GO (in gebruik) | Gezond; `skills:`-preload + permission-scoping toevoegen |
| A.5 | **Hooks** | A | 🟢 **GO — hoogste prioriteit** | Fundering onder autonomie: green-gate (secret-scan/disclosure/scope) + audit-trail vervangt mens-per-stap |
| A.6 | Plugins + marketplaces | A | 🟡 HOLD → GO bij Spoor B | Distributie-nut pas bij 2e omgeving/organisatie-overdracht |
| A.7 | MCP (mechanisme) | A | 🟢 GO (in gebruik) | Servers in installment 2 |
| A.8 | Settings/permissions | A | 🟢 GO | Maakt rolscheiding afdwingbaar i.p.v. prozaregel |
| A.9 | Agent SDK/headless/CI | A | 🟢 GO-trajectorie A / 🟡 HOLD cloud-CI bij Spoor B | Check-gated autonome pijplijn; auto-merge alléén achter groene checks |
| A.10 | Code intelligence | A | 🔴 NO-GO | Geen symbol-navigatie-probleem in dit project |
| A.10 | Checkpoint/AgentView/`/goal` | A | 🟡 HOLD | Research-preview; status her-verifiëren |
| A.10 | Output styles | A | 🟡 HOLD | Status onzeker — niet in huidige docs-ankerlijst |
| D.1 | canonical-metrics-skill | D | 🟢 GO | Beste eerste skill; borgt v4.3.3-leerpunt |
| D.2 | SHACL-split-skill | D | 🟢 GO | Codificeert verplichte split + 290-false-positives |
| D.3 | patch-rapport-generator-skill | D | 🟢 GO | Structuur + "§0 uit JSON"-discipline |
| D.4 | SKOS-classificatie-skill | D | 🟢 GO (timing: bij T3) | D4+D4.1+cluster-discipline; helper-script blijft autoritatief |
| D.5 | brain-lint-skill | D | 🟡 HOLD → GO na kfchou-vergelijking | Niet twee lint-systemen |
| D.6 | protocol-handhaving (hooks+commands) | D | 🟢 GO gefaseerd | Proza → afgedwongen/aanroepbaar |
| D.7 | GRC-domein-skill (NL-kaders) | D | 🟢 GO | Unieke lacune (geen externe skill dekt BIO/VIR/VIRBI/ENSIA) |
| D.8 | eigen RDF/SPARQL/SHACL-MCP | D | 🔴 NO-GO | Dubbel werk t.o.v. skills + open-ontologies-MCP |
| I.1 | Huidige zeven-chat-opzet | I | 🟢 behouden, met overgang | Scheiding gezond; Steven-als-router is het te automatiseren deel |
| I.2b | Agent teams | I | 🟡 HOLD-op-volwassenheid → 🟢 GO-trajectorie | Zelf-coördinatie = nu het doel; sequencen ná guardrail-laag + GA-status |
| I.2d | Hook-gedreven scope-grens-gate | I | 🟢 GO-kandidaat | Maakt veilige autonomie mogelijk (mens-in-controle zonder mens-per-stap) |
| I.2e | Parallelle subagents | I | 🟢 GO-kandidaat | Goedkoper/minder-experimenteel dan agent teams waar peer-comms niet nodig is |

**Rode draad installment 1 (herwogen op de autonomie-koers §0.5):** het doel is een autonoom systeem zonder mens-per-stap, mét behoud van de invariant "mens-in-controle als toezicht/uitlegbaar/auditeerbaar". De sleutel is dus niet autonomie blokkeren, maar autonomie *veilig en aantoonbaar* maken — "maak de verificatie deterministisch, niet de LLM". Daaruit volgt de prioriteitsvolgorde (Spoor A): **(1) de deterministische envelop bouwen** — A.5-hooks green-gate (secret-scan/disclosure/scope-grens) + audit-trail + A.8-permissions + D.1/D.2-verificatie-skills; **(2) de uitvoeringslaag autonomiseren binnen die envelop** — eerst parallelle subagents (I.2-e, GA, goedkoop), dan agent teams (I.2-b) zodra GA + envelop staan; **(3) check-gated CI** (A.9) als bovenliggende automatisering; **(4) domein-skills** D.3/D.6/D.7/D.4. Parallel: §0.5-aanbeveling om het nieuwe operating-model formeel als D-/scope-besluit vast te leggen (masterchat).

---

*Einde installment 1/4 (herzien 28-05-2026 op de autonomie-koers-correctie).*

---

## DOMEIN E — MCP-connectoren / -servers (breed)

### E.0 Filter en landschap

Drie invariant-filters per server: **lokaal-draaibaar** (productie zonder cloud-internet-afhankelijkheid — hard voor de toekomstige productielaag, soepel voor Spoor A), **security/secret-hygiëne** (PAT-incident-les), **vendor-lock-in**. Het RDF/SPARQL/SHACL-MCP-landschap valt uiteen in (a) één volwaardige engine (open-ontologies), (b) lichte query/explore-wrappers (mcp-rdf-explorer, SPARQL-MCP, GraphDB-MCP), (c) niet-RDF graph-DB's (Neo4j/FalkorDB/Wikidata — buiten scope). Onder de autonomie-koers stijgt de relevantie van MCP-servers die *reasoning/validatie als tools* blootstellen: een autonome Claude-orchestrator roept tools aan, en de arXiv-bevinding (zie H.3) toont dat tool-toegang fors beter werkt dan ruwe-OWL-in-context.

### E.1 GitHub-MCP (in gebruik — her-validatie)

| Aspect | Waarde |
|---|---|
| Status | GA, **actief** (masterchat + subagents; `grc-kennismodel:*`-tools) |
| Lokaal-draaibaar | 🔴 cloud (api.githubcopilot.com). Acceptabel Spoor A; bij Spoor B heroverwegen naar on-prem git (CLAUDE.md "Spoor B-overweging") |
| Security | PAT-hygiëne kritisch (incident); tokens scopen + secret-scan-hook (A.5). `run_secret_scanning`-tool is beschikbaar binnen deze MCP |
| Bron | repo-MCP-config + GitHub-MCP-tools (geverifieerd in gebruik, 28-05-2026) |

**🟢 GO — in gebruik.** Onder de autonomie-koers is GitHub-MCP precies wat autonoom committen/pushen mogelijk maakt zodra de "geen-commit"-regel sunset (§0.5) — mits achter de green-gate (A.5). Geen vendor-lock-in op modelniveau (standaard git-repo). Spoor-B-heroverweging blijft staan.

### E.2 open-ontologies-MCP (her-validatie — cross-ref H.1)

| Aspect | Waarde (her-gevalideerd 28-05-2026) |
|---|---|
| Status | **Nog actief** — README/releases 22 apr 2026; arXiv-paper 2605.09184 ~begin mei 2026 (peer-review-stijl) |
| Licentie | MIT (lage lock-in) |
| Lokaal-draaibaar | 🟢 **ja** — single Rust-binary, no JVM, in-memory Oxigraph; sterkste server op deze invariant |
| Tools | 21–43 (varieert per listing/versie; github noemt 43): core (validate/load/save/query/diff/lint/convert), data-pipeline (map/ingest/shacl/reason/extend), lifecycle (plan/apply/lock/drift/enforce/monitor/lineage), advanced (align/crosswalk/enrich/embed) |
| Reasoning-profielen | rdfs / owl-rl / **owl-rl-ext** (someValuesFrom/allValuesFrom/hasValue/intersectionOf/unionOf) / **owl-dl** (native SHOIQ tableaux: satisfiability, ABox-consistency, explanation traces, unsatisfiable-class-detectie) |
| Security-claim | Derde-partij-directory (codaone) noemt "8-point security audit, Verified" — **directory-self-report, niet door ons geaudit**; bij inzet zelf verifiëren |
| Bron | github.com/fabio-rovai/open-ontologies (officieel/auteur, 22-04-2026); arxiv.org/html/2605.09184v1 (academisch); lobehub/codaone (derde-partij-directory) |

**NEN-discipline-risico:** 🟢 (toolchain, geen content).

**Her-validatie t.o.v. eval-rapport (27-05-2026):** het eerdere oordeel was 🟡 **HOLD + evaluatie-sprint plannen** (gekoppeld aan H37/H38/H41). Dat oordeel **staat** — de repo is nog actief, MIT, lokaal-draaibaar. Twee aanvullingen sinds dat rapport: (1) de vier reasoning-profielen zijn nu expliciet gedocumenteerd — `owl-rl-ext` is een interessant *middenprofiel* tussen jullie huidige OWL-RL en volledige tableaux, en `owl-dl` levert ABox-consistency + **explanation traces** (uitlegbaarheid — relevant voor de behouden invariant §0.5); (2) de autonomie-koers **verhoogt de prioriteit** van de geplande evaluatie-sprint, want een MCP-server die reasoning/SHACL/SPARQL als tools aanbiedt past beter bij een autonome Claude-orchestrator dan losse, mens-aangeroepen Python-scripts.

**Belangrijk voorbehoud (overlap/conflict):** de `/build`-pijplijn van open-ontologies *auto-construeert* ontologieën in 13 stappen. Dat is **niet** wat dit project wil — jullie bouwen bewust, framework-neutraal (D9), met deliberate modellering. De waarde zit uitsluitend in de *reason/validate/query/SHACL/lineage*-tools, niet in auto-constructie. Bij evaluatie: alleen de runtime-tools toetsen op `grc-v4_6_2-merged.ttl`, niet de constructie-pijplijn.

**Rubriek-score:** Waarde 4 · Effort 3 (evaluatie; migratie zou hoog zijn) · Invarianten 5 (lokaal, MIT, explanation traces) · Overlap 3 (auto-construct ongewenst; reasoner-overlap met huidige stack) · Reversibiliteit 5 (binary verwijderen).

**🟡 HOLD + geplande evaluatie-sprint (bevestigt eval-rapport) — prioriteit verhoogd onder autonomie-koers.**
- *Waarom geen GO (migratie):* de huidige rdflib+owlrl+pySHACL-stack is bewezen over 14 sprints; geen aangetoonde OWL-RL-limitatie in productie; migratie-kost substantieel (canonical_metrics + SHACL-split herschrijven).
- *Waarom geen NO-GO:* drie H-items (H37/H38/H41) hebben dit als concrete trigger; `owl-dl` tableaux is de directe test voor H38 (derde reasoner) en H41 (laden SKOS-axiomas wel/niet onder tableaux?); de 50k-post-RL-drempel nadert (44.907); en de autonomie-koers maakt tool-georiënteerde reasoning aantrekkelijker. Plan de evaluatie-sprint (geen migratie-besluit) ná T3 of bij H41-trigger, zoals het eval-rapport al voorstelde — eventueel naar voren gehaald gezien de koers.

### E.3 mcp-rdf-explorer (emekaokoye) en lichte SPARQL-wrappers

| Aspect | Waarde |
|---|---|
| Wat | Conversationele SPARQL over lokale Turtle-file óf SPARQL-endpoint; query/full-text-search/stats/triple-count/health/schema-introspectie |
| Lokaal-draaibaar | 🟢 (local-file-mode) |
| Reasoner/SHACL | ✗ geen — puur query/explore |
| Bron | github.com/emekaokoye/mcp-rdf-explorer; pulsemcp/glama (directory) |

**Overlap/toepasbaarheid:** query/exploratie over de Turtle-modules is al opgelost door de Python-toolchain + de geplande D.1/D.2-skills. Een query-only MCP voegt weinig toe en introduceert een tweede SPARQL-pad. Soortgelijk: **SPARQL-MCP (Kludge Works)**, **Ontotext GraphDB-MCP** (read-only over GraphDB-repos) — beide vereisen/veronderstellen een triplestore-deployment die dit project (file-based Turtle) niet heeft.

**🔴 NO-GO (Spoor A) — 🟡 HOLD bij Spoor C (triplestore-deployment).**
- *Waarom NO-GO:* redundant t.o.v. bestaande query-capaciteit; geen reasoner/SHACL-meerwaarde; tweede SPARQL-pad = onnodige complexiteit (Simplicity-First).
- *Waarom geen permanente NO-GO:* zodra Spoor C een echte triplestore (bv. Oxigraph/GraphDB) draait voor het dashboard/bevraging, wordt een SPARQL-endpoint-MCP relevant als bevragings-laag. Parkeer als Spoor-C-kandidaat.

### E.4 OntoBricks / enterprise-KG-MCP's en niet-RDF graph-DB-MCP's

**OntoBricks** (Databricks→KG, R2RML, OWL 2 RL/SWRL/SHACL, GraphQL+MCP): vereist Databricks-stack — niet aanwezig. **Neo4j/FalkorDB/Wikidata-MCP's:** niet-RDF/OWL-native graph-DB's, passen niet bij de OWL 2 DL + Turtle-stack zonder bridge. **🔴 NO-GO (alle sporen)** — geen fit met de bestaande stack; vendor-/platform-lock-in.

---

## DOMEIN H — Ontologie / taxonomie / data-modelling-tooling & methoden

### H.1 open-ontologies reasoner-profielen vs. de huidige toolchain (H37/H38/H41)

Zie E.2 voor de server-inventarisatie. **Inhoudelijke koppeling aan de open H-items:**

| H-item | Wat open-ontologies' profielen leveren |
|---|---|
| **H38** (OWL RL ↔ HermiT-equivalentie) | `owl-dl` tableaux = een **derde reasoner** naast jullie OWL-RL (rdflib+owlrl) en Protégé/HermiT — directe vergelijkingsbasis |
| **H41** (SKOS-axioma-set-handling: skos:S46 symmetrie, S47 transitiviteit) | empirische test: laadt de tableaux-engine SKOS-axiomas wél, waar jullie OWL-RL ze niet laadt onder `axiomatic_triples=False`? Dit is dé open vraag uit het eval-rapport |
| **H37** (open-ontologies-integratie) | de evaluatie-sprint zelf |

Het **`owl-rl-ext`-profiel** is nieuw relevant: het voegt existentiële/universele restricties + boolean class-constructors toe bovenop OWL-RL, zónder de volle tableaux-kost. Voor een model dat OWL 2 DL-profiel claimt (D1) maar in productie OWL-RL draait, is dit een mogelijk middenpad — te toetsen in de evaluatie-sprint.

**🟡 HOLD — evaluatie-sprint (bevestigt eval-rapport, prioriteit verhoogd). Geen migratie zonder empirisch bewijs.**

### H.2 Huidige stack rdflib + owlrl + pySHACL — en waarom de split-discipline academisch klopt

| Aspect | Waarde |
|---|---|
| Status | Bewezen over 14 sprints (v4.0.0–v4.6.2); productie-stabiel |
| Academische context | OWL maakt de **open-world-assumptie** (OWA); SHACL de **closed-world-assumptie** (CWA). SHACL-validatie *in aanwezigheid van* OWL-inferentie is een bekend, niet-triviaal probleem (arXiv 2507.12286, 2025) — dit **verklaart** waarom de gecombineerde validatie 290 false-positives oplevert en waarom jullie SECTIE A (`inference='none'`) / SECTIE B (`inference='owlrl'`)-split methodologisch correct is |
| Bron | arxiv.org/pdf/2507.12286 ("SHACL Validation in the Presence of Ontologies", academisch, 2025) |

**🟢 GO — huidige stack behouden.** Geen migratie-trigger. De academische literatuur is hier *bevestigend*: de split-validatie-discipline is geen workaround maar de juiste manier om OWA-inferentie en CWA-validatie te scheiden. Bruikbaar als onderbouwing in patch-rapporten/brain-vault dat de 290-false-positives een verwacht OWA/CWA-fenomeen zijn, geen modeldefect.

### H.3 LLM-ondersteunde ontologie-engineering-methoden (referentie, geen tooling)

De 2025–2026-literatuur convergeert op een patroon dat dit project al belichaamt:

- **NeOn-GPT** (Fathallah e.a., 2024) en **LOT-methodologie→LLM-mapping**: LLM ondersteunt requirements→OWL-encoding→evaluatie→documentatie. Zwakte (gerapporteerd): twee-staps-fouten stapelen, hiërarchie-redenering is het zwakke punt, geen ingebouwde validatie.
- **Dual-validation-school**: elke nieuwe fact passeert SHACL (structuur) + reasoning (consistentie) vóór toevoeging.
- **Salovsky 2026 / hybride architectuur** (arXiv 2604.20795, 22-04-2026): LLM als "interpretatie/generatie/orchestratie-laag", het wereldmodel leeft in de RDF/OWL-graaf, verificatie is deterministisch (SHACL/OWL). Kernprincipe — ook in de ARIA-gatekeeper-framing — **"maak niet de LLM deterministisch, maak de verificatie deterministisch"**.
- **OAEI-alignment-bevinding** (open-ontologies-paper, arXiv 2605.09184): gestructureerde tool-toegang F1 = 0,717 vs. ruwe-OWL-in-context F1 = 0,323 vs. unaided F1 = 0,431 — tool-toegang verslaat zowel Turtle-in-context als blind redeneren.

**Toepasbaarheid (eerlijk afgebakend):** dit zijn **referentie/validatie, geen te-installeren tooling**, en met twee scherpe grenzen. (1) De *auto-constructie*-methoden (NeOn-GPT, entity-extraction-pijplijnen) zijn **niet** voor dit project — jullie bouwen bewust en framework-neutraal (D9); auto-constructie ondermijnt dat. (2) Het *deterministische-verificatie*-principe is precies wat jullie al doen (Karpathy compile-once + formele ontologie + SHACL-split + canonical-metrics) — en het is, zoals in §0.5 uitgewerkt, **de brug naar veilige autonomie**: de OAEI-bevinding onderbouwt bovendien waarom Claude ontologie-tools (skills/MCP) moet krijgen i.p.v. Turtle-in-context-plakken.

**🟢 GO als methodologische referentie/onderbouwing** (geen installatie). Concreet nut: citeerbare onderbouwing in brain-vault/masterchat dat de bestaande architectuur (deterministische verificatie + tool-toegang) aansluit bij de state-of-the-art en bij de autonomie-koers. Mogelijk file-back-kandidaat als concept-bestand.

### H.4 OWL+SHACL cross-referencing + SKOS-value-validatie-shapes (concrete techniek)

Het KCap-2025-werk ("Lessons Learned from the Combined Development of OWL and SHACL", dl.acm.org/doi/full/10.1145/3731443.3771340) beschrijft twee technieken die direct op jullie open H-items raken:

- **Annotatie-cross-referencing** tussen OWL-ontologie en SHACL-shapes, met consistency-queries die verifiëren dat beide synchroon zijn. Toepasbaar tussen jullie 22 modules en `grc-shacl.ttl`.
- **SHACL-patronen voor SKOS-value-validatie** — een shape die SKOS-predicate-gebruik valideert. Dit raakt **H39** (SHACL-blinde-vlek ctrl↔compl-mapping-distributie) direct: een SHACL-shape die de SKOS-distributie (exact/close/broad/narrow/related) per cluster valideert, zou de T1/T2-cluster-discipline *afdwingbaar* maken i.p.v. handmatig-via-helper-script-gecontroleerd.

**🟡 HOLD-kandidaat / mogelijk nieuw H-item (Spoor A).**
- *Waarom geen GO nu:* SHACL-shape-uitbreiding op SKOS-distributie is een ontologie-/modelleringsbeslissing (Tech + masterchat), geen Analyse-deliverable; en H39 staat bewust "active geparkeerd".
- *Waarom geen NO-GO:* het is een concrete, onderbouwde techniek die een bestaand H-item (H39) vooruithelpt en de SKOS-kwaliteitsdiscipline van handmatig naar afdwingbaar tilt — precies passend bij de "deterministische verificatie"-lijn van §0.5. Aanbeveling: agenderen bij H39-heroverweging.

### H.5 Protégé (desktop) — blijft de cross-check

Protégé (HermiT/Pellet) blijft de visuele desktop-cross-check, met name voor H38 (reasoner-equivalentie). open-ontologies positioneert zich expliciet als "no Protégé", maar dat is geen reden Protégé te schrappen — het blijft het onafhankelijke verificatiepunt naast de Python-stack en (mogelijk) de tableaux-engine. **🟢 GO — behouden als cross-check** (geen wijziging; HermiT-herrun staat al als openstaand item sinds v4.0.0).

---

## Deel-samenvatting installment 2 (E + H)

| # | Kandidaat | Domein | Recommendation | Korte reden |
|---|---|---|---|---|
| E.1 | GitHub-MCP | E | 🟢 GO (in gebruik) | Cloud; Spoor-B-heroverweging; enabler van autonoom committen achter green-gate |
| E.2 | open-ontologies-MCP | E | 🟡 HOLD + evaluatie-sprint (prio ↑) | Nog actief/MIT/lokaal; H37/H38/H41-trigger; auto-construct ongewenst, runtime-tools wel |
| E.3 | mcp-rdf-explorer / SPARQL-MCP / GraphDB-MCP | E | 🔴 NO-GO A / 🟡 HOLD Spoor C | Redundant t.o.v. toolchain+skills; relevant pas bij triplestore-deployment |
| E.4 | OntoBricks / Neo4j / FalkorDB-MCP | E | 🔴 NO-GO | Geen fit met OWL 2 DL + Turtle-stack; platform-lock-in |
| H.1 | open-ontologies reasoner-profielen (H37/H38/H41) | H | 🟡 HOLD — evaluatie-sprint | `owl-dl` tableaux = test voor H38+H41; `owl-rl-ext` mogelijk middenpad |
| H.2 | rdflib+owlrl+pySHACL (huidige stack) | H | 🟢 GO (behouden) | Bewezen; OWA/CWA-literatuur bevestigt split-discipline + verklaart 290-false-positives |
| H.3 | LLM-ontologie-engineering-methoden | H | 🟢 GO (referentie, geen installatie) | Bevestigt architectuur; auto-construct expliciet uitgesloten (D9) |
| H.4 | OWL+SHACL cross-ref + SKOS-validatie-shapes | H | 🟡 HOLD-kandidaat / mogelijk H-item | Helpt H39 vooruit; maakt SKOS-distributie afdwingbaar |
| H.5 | Protégé (desktop cross-check) | H | 🟢 GO (behouden) | Onafhankelijke reasoner-verificatie (H38); niet vervangen |

**Rode draad installment 2:** geen migratie van de bewezen Python-stack zonder trigger — de academische OWA/CWA-literatuur bevestigt zelfs dat jullie split-validatie-discipline correct is. De enige echte server-kandidaat blijft **open-ontologies-MCP**, en het eerdere 🟡 HOLD-met-evaluatie-sprint-oordeel houdt stand; de autonomie-koers + de nieuw-gedocumenteerde `owl-dl`/`owl-rl-ext`-profielen + de explanation-traces (uitlegbaarheid) verhogen de prioriteit van die evaluatie. De lichte SPARQL-wrappers zijn redundant tot Spoor C. Methodologisch bevestigt de literatuur de bestaande architectuur én levert ze het kernprincipe voor de autonomie-koers ("deterministische verificatie, niet deterministische LLM"). Eén concrete nieuwe denkrichting: een SHACL-shape voor SKOS-predicate-distributie (H.4 → H39).

---

## DOMEIN B — claude.ai-features (Master / Documentatie / Analyse / Asset)

### B.0 Twee cross-cutting observaties vooraf

1. **Skills draaien over claude.ai, Claude Code én de API** (support.claude.com/en/articles/12512180, officieel, geverifieerd 28-05-2026; pre-built skills sinds 2025-10-15, "Skills 2.0" met executable scripts Q1 2026). Dit betekent dat de zelf-gebouwde skills uit domein D (canonical-metrics, GRC-domein, SKOS-classificatie) **niet Claude-Code-only** zijn: één skill, gebouwd één keer, is bruikbaar door Master/Documentatie/Analyse (claude.ai) én Tech (Claude Code). Dat overbrugt de claude.ai↔Claude-Code-grens die in domein I als wrijvingspunt benoemd is. Dit is de belangrijkste structurele vondst van domein B.
2. **PK auto-RAG botst met de Karpathy-anti-RAG-architectuur.** Project Knowledge schakelt bij een grote knowledge base automatisch over op RAG-retrieval (officieel support-gedrag; bevestigd door meerdere bronnen, feb–mei 2026). De brain-vault (~115 markdown-bestanden) zou in PK dus via *niet-deterministische* RAG-retrieval bevraagd worden — terwijl CLAUDE.md expliciet RAG verwerpt ("index + register volstaat tot ~500 bestanden; Karpathy-pattern verwerpt RAG"). De migratie van brain naar GitHub + GitHub-MCP (`get_file_contents`) vervangt RAG-retrieval door *deterministische* file-fetch. Dit **onderbouwt de geplande PK-opschoning** (brain-vault uit PK verwijderen na GitHub-MCP-setup): het verwijdert de RAG-spanning en sluit aan bij de "deterministische verificatie"-lijn (§0.5).

### B.1 Projects + project knowledge

| Aspect | Waarde |
|---|---|
| Capaciteit | 200K context primair; auto-RAG-expansie tot ~10× bij grote knowledge base (betaald); 30 MB/bestand; per-chat 20 bestanden/30 MB |
| Eigenschap | Chats binnen een project delen géén context onderling — alleen de knowledge base + custom instructions zijn gedeeld; memory per project gescheiden |
| Bron | support.claude.com (Projects); espo.ai/aitoolsclub-guides (community, feb–mei 2026) |

**Toepasbaarheid:** Het project gebruikt PK al (brain-vault pre-migratie, NEN-restrictieve bronnen). Twee punten: (1) **NEN-restrictieve bronnen moeten in PK blijven** (licentie verbiedt git-publicatie) — dat is correct en verandert niet. (2) De **PK-opschoning** (brain-vault + publieke bronnen eruit na GitHub-MCP) is architectureel juist (B.0-punt 2). Custom instructions per project zijn de plek voor de always-on-conventies (Nederlands, geen organisatienaam, D9) voor de claude.ai-chats — analoog aan CLAUDE.md voor Claude Code.

**Rubriek-score:** Waarde 5 (in gebruik) · Effort 5 · Invarianten 4 (RAG-spanning bij grote PK; opgelost via migratie) · Overlap 5 · Reversibiliteit 5. **🟢 GO — in gebruik; voer de PK-opschoning uit na GitHub-MCP-setup.**

### B.2 Skills in claude.ai

| Aspect | Waarde |
|---|---|
| Mechaniek | Customize → Skills → + → Upload a skill (zip met SKILL.md); vereist Pro/Max/Team/Enterprise + code execution aan |
| Reikwijdte | Zelfde skill draait in claude.ai, Claude Code én API (/v1/skills) |
| Bron | support.claude.com/en/articles/12512180 (officieel, geverifieerd 28-05-2026) |

**Toepasbaarheid:** Dit is de operationalisering van B.0-punt 1. De GRC-domein-skill (D.7) en de SKOS-classificatie-skill (D.4) zijn juist in de **claude.ai-chats** waardevol: Master/Analyse krijgen de NL-kader-kennis + SKOS-beoordelingslogica zonder die elke keer in proza te herhalen. Let op de invariant: skills met side-effects krijgen `disable-model-invocation: true` (alleen handmatig), conform domein A.2.

**🟢 GO (Spoor A)** — bouw de domein-D-skills één keer, deploy in beide omgevingen. *Waarom geen onvoorwaardelijke GO:* code-execution moet aan staan (privacy-/security-afweging per chat); NEN-discipline blijft (skills dragen parafrase, geen verbatim).

### B.3 Connectors / MCP apps in claude.ai

| Aspect | Waarde |
|---|---|
| Status | Remote MCP-connectoren op Pro/Max/Team/Enterprise sinds jan 2026; lokale MCP met desktop-app op elk plan |
| Huidige invulling | GitHub-MCP actief in masterchat (`grc-kennismodel:*`) — gebruikt voor STAP 0 van dit rapport |
| Bron | suprmind/feature-overzicht (community, mei 2026); in-gebruik-verificatie 28-05-2026 |

**Toepasbaarheid:** GitHub-MCP geeft de masterchat directe repo-toegang (brain-vault, rapporten) — al in gebruik en bevestigd nuttig. Onder de autonomie-koers is dit ook het pad waarlangs claude.ai-chats repo-state lezen/schrijven. **🟢 GO — in gebruik.** Security: PAT-hygiëne (incident) + secret-scan-hook (A.5).

### B.4 Memory

| Aspect | Waarde |
|---|---|
| Modi | Chat-memory (samenvattingen van eerdere gesprekken, Settings → Capabilities → Memory, in te zien/bewerken) + file-system memory (/memory-folder, agentic) |
| Scope | Per project gescheiden; beschikbaar alle tiers sinds 2026-03-02 |
| Bron | suprmind (community, mei 2026); in-context memory-gedrag |

**Toepasbaarheid — met een scherpe grens.** Memory is een *gemaks*laag (project-state over chats heen), maar **niet het system of record**. Het authoritatieve geheugen van dit project is de brain-vault + ontologie + git-history — deterministisch, versiebeheerd, auditeerbaar. Memory-samenvattingen zijn afgeleid en kunnen verouderen. Aanbeveling: memory benutten voor continuïteit/gemak, maar bij elke architectuur-/historie-vraag **blijft brain-vault (via GitHub-MCP) de bron** (conform CLAUDE.md "raadplegen vóór andere bronnen"). Niet vertrouwen op memory voor D-/H-/versie-feiten.

**🟢 GO als gemakslaag — 🟡 met expliciete grens** (geen system of record; brain-vault blijft autoritatief). *Waarom geen NO-GO:* continuïteit over chats is nuttig. *Waarom de grens:* memory is afgeleid en niet-auditeerbaar op de manier die de GRC-context vereist.

### B.5 Research / deep research

| Aspect | Waarde |
|---|---|
| Wat | Agentic: meerdere op elkaar voortbouwende searches, citaties; vereist web search aan |
| Tiers | Pro/Max/Team/Enterprise (niet Free) |
| Bron | support.claude.com/en/articles/11088861 (officieel, 16-03-2026) |

**Toepasbaarheid:** Dit is de **Analyse-chat-feature bij uitstek** — exact het soort werk als dit extensie-landschap-rapport (brede, gedateerde multi-bron-inventarisatie). Voor framework-analyses (nieuwe kaders, externe tooling, crosswalk-bronnen) levert Research diepere dekking dan losse searches. De onderzoeks-prompt zelf noemt Research als alternatief voor >30-search-taken.

**Rubriek-score:** Waarde 5 (Analyse) · Effort 5 (toggle) · Invarianten 5 · Overlap 5 · Reversibiliteit 5. **🟢 GO (Analyse-chat).** *Voorbehoud:* Research-output blijft "informed", net als dit rapport — citaties zelf verifiëren; geen vervanger voor autoritatieve bron (NEN/EU-Publications/NIST.gov).

### B.6 Artifacts incl. AI-powered ("Claude-in-Claude")

| Aspect | Waarde |
|---|---|
| Gewone artifacts | HTML/React/markdown/SVG/Mermaid; persistente key-value-storage; geen browser-storage |
| AI-powered artifacts | Artifact roept de Anthropic API aan (Sonnet) — interactieve, AI-gedreven mini-apps in de chat |
| Bron | in-context productdocumentatie (28-05-2026) |

**Toepasbaarheid:** Gewone artifacts zijn nuttig voor Master/Documentatie (diagrammen, vergelijkingstabellen, een interactieve normenkader-visualisatie). **AI-powered artifacts** ("Claude-in-Claude") zijn verleidelijk voor een dashboard-prototype waarin een gebruiker natuurlijke-taal-vragen stelt die Claude tegen de ontologie-data beantwoordt — maar hier botst de **lokaal-draaibaar-invariant**: een AI-powered artifact roept de cloud-API aan. Voor Spoor A-demo/prototype acceptabel; voor de productie-AI-laag (visie: lokaal draaibaar, uitlegbaar) **niet**.

**🟡 HOLD voor AI-powered artifacts** (Spoor A-prototype 🟢 / productie 🔴 lokaal-draaibaar-conflict) — **🟢 GO voor gewone artifacts** (Master/Documentatie-visualisaties). *Waarom geen GO op AI-powered voor productie:* cloud-API-afhankelijkheid schendt de lokaal-draaibaar-invariant; bovendien is de read-only grc-explorer (Spoor A) bewust géén AI-laag.

### B.7 Custom writing styles

**Toepasbaarheid:** Direct nuttig voor de **Documentatie-chat**: een opgeslagen stijl die de Rijksoverheid-beleidsstijl, het Nederlands, en de "geen organisatienaam"-conventie borgt — zodat PID/beleid/management-communicatie consistent is zonder herhaalde instructie. Preset (Formeel/Beknopt/Uitleggend) of custom (voorbeeld uploaden of beschrijven). Bron: support/claudelab (officieel + community, mrt 2026).

**🟢 GO (Documentatie-chat).** Laag risico, direct nut; codificeert tone-conventies. *Voorbehoud:* stijl ≠ inhoudelijke discipline (D9, status-discipline CBW/Cbb blijven inhoudelijke regels, geen stijlkwestie).

### B.8 Analysis / code-execution tool

**Toepasbaarheid:** De code-execution/analysis-tool is nuttig voor de **Analyse-chat** bij ad-hoc bewerking van de xlsx-bronnen (CBW-Control-Framework, CSF 2.0, BIO was-wordt-lijst) — tellingen, cross-tabs, sanity-checks vóór een framework-analyse. Het is dezelfde laag die de domein-D-skills draaien. **🟢 GO (Analyse-chat)** voor verkennende data-bewerking; geen ontologie-mutatie (dat blijft Tech/Claude Code).

---

## DOMEIN C — Anthropic-native / officiële skills

Beoordeeld op waarde voor de concrete deliverables: patch-rapporten (Tech), beleidsdocumenten (Documentatie), dashboards (Dashboard), en skill-/MCP-bouw (enabler domein D). Bron: in-context skill-definities + suprmind (Anthropic shipped pre-built Excel/PowerPoint/Word/PDF-skills, 2026).

### C.1 docx
**Waarde:** Documentatie-chat formele deliverables (PID, beleid, management-communicatie als Word). Patch-rapporten/tussenrapporten blijven .md (geen docx nodig). **🟢 GO (Documentatie)** waar een Word-deliverable gevraagd is (bv. stuk voor CSO/bestuur). Effort laag (built-in). Reversibel.

### C.2 pptx
**Waarde:** management-/bestuurspresentaties (compliance-status, urgentie-overzicht voor CSO/CISO/bestuur). **🟢 GO (Documentatie/Master)** voor strategische communicatie. Past bij toepassing-prioriteit-1 (CSO/CISO/bestuur).

### C.3 xlsx
**Waarde:** de bron-stack is xlsx-zwaar (CBW-Control-Framework, CSF 2.0 + Implementation Examples, BIO was-wordt-lijst). De xlsx-skill helpt Analyse die bronnen te lezen/herstructureren; ook bruikbaar voor metric-exports. **🟢 GO (Analyse)**. NEN-let-op: de xlsx-bronnen zijn CC-BY/publiek (geen NEN), dus geen verbatim-risico hier.

### C.4 pdf / pdf-reading
**Waarde:** zeer veel PDF-bronnen (EU-recht, NIST, VIR/VIRBI/BVA, NEN-PDF's). pdf-reading voor extractie/parafrase. **🟢 GO (Analyse/Tech)** — **met NEN-caveat:** de skill verandert de NEN-discipline niet; ISO-PDF's blijven parafrase + clausule-verwijzing (Protocol 17), geen verbatim >10 woorden. De skill maakt lezen makkelijker, niet de licentie ruimer.

### C.5 frontend-design
**Waarde:** de grc-explorer-HTML (Cytoscape.js) en toekomstige dashboard-UI. Dashboard is naar Claude Code gemigreerd; de skill geldt daar ook. **🟢 GO (Dashboard)** voor UI-kwaliteit van de read-only explorer (Spoor A). Geen ontologie-impact.

### C.6 skill-creator
**Waarde:** **enabler van het hele domein D.** skill-creator + eval/benchmarking is de gestructureerde manier om de canonical-metrics-, SHACL-split-, patch-rapport-, GRC-domein- en SKOS-skills te bouwen én te testen op betrouwbaar triggeren. **🟢 GO (Spoor A)** — de aangewezen route om de domein-D-aanbevelingen uit te voeren. Hoge hefboom.

### C.7 mcp-builder
**Waarde:** alleen relevant als een eigen MCP-server gebouwd wordt — wat in domein D.8 een 🔴 NO-GO kreeg (dubbel werk t.o.v. skills + open-ontologies-MCP). **🔴 NO-GO / 🟡 HOLD** — geen huidige bouwbehoefte; her-overweeg alleen als de open-ontologies-evaluatie negatief is én skills tekortschieten (ver, voorwaardelijk scenario).

### C.x Infrastructuur-skills (file-reading, pdf-reading, product-self-knowledge)
Achtergrond-/router-skills die automatisch meedraaien; geen project-specifieke deliverable. Geen aparte GO/NO-GO — ze ondersteunen C.1–C.5.

---

## Deel-samenvatting installment 3 (B + C)

| # | Kandidaat | Domein | Recommendation | Korte reden |
|---|---|---|---|---|
| B.1 | Projects + project knowledge | B | 🟢 GO (in gebruik) | PK-opschoning na GitHub-MCP; NEN blijft in PK; RAG-spanning opgelost via migratie |
| B.2 | Skills in claude.ai | B | 🟢 GO | Domein-D-skills draaien óók hier → overbrugt claude.ai↔Claude-Code |
| B.3 | Connectors / MCP apps | B | 🟢 GO (in gebruik) | GitHub-MCP in masterchat; PAT-hygiëne via A.5 |
| B.4 | Memory | B | 🟢 GO als gemakslaag / 🟡 grens | Géén system of record; brain-vault blijft autoritatief |
| B.5 | Research / deep research | B | 🟢 GO (Analyse) | Dé Analyse-feature; citaties zelf verifiëren |
| B.6 | Artifacts (gewoon / AI-powered) | B | 🟢 GO gewoon / 🟡 HOLD AI-powered | AI-powered = cloud-API → lokaal-draaibaar-conflict productie |
| B.7 | Custom writing styles | B | 🟢 GO (Documentatie) | Borgt NL/Rijksoverheid-tone + geen-organisatienaam |
| B.8 | Analysis / code-execution | B | 🟢 GO (Analyse) | Ad-hoc xlsx-bron-bewerking; geen ontologie-mutatie |
| C.1 | docx | C | 🟢 GO (Documentatie) | Word-deliverables (PID/beleid); rapporten blijven .md |
| C.2 | pptx | C | 🟢 GO (Documentatie/Master) | Bestuurs-/management-presentaties |
| C.3 | xlsx | C | 🟢 GO (Analyse) | Bron-stack is xlsx-zwaar (CBW/CSF/BIO) |
| C.4 | pdf / pdf-reading | C | 🟢 GO (Analyse/Tech) | Veel PDF-bronnen; NEN-parafrase-discipline blijft |
| C.5 | frontend-design | C | 🟢 GO (Dashboard) | grc-explorer-UI-kwaliteit |
| C.6 | skill-creator | C | 🟢 GO | Enabler + eval voor alle domein-D-skills |
| C.7 | mcp-builder | C | 🔴 NO-GO / 🟡 HOLD | Geen bouwbehoefte (D.8 NO-GO) |

**Rode draad installment 3:** de claude.ai-laag is grotendeels GO en deels al in gebruik — de winst zit in twee dingen. (1) **Skills overbruggen de twee werelden**: bouw de domein-D-skills via skill-creator (C.6) één keer en ze draaien in zowel de claude.ai-chats als Claude Code — dat haalt een domein-I-wrijvingspunt weg. (2) **De claude.ai-features bedienen elk een specifieke chat**: Research → Analyse; custom styles + docx/pptx → Documentatie; analysis-tool + xlsx/pdf → Analyse; gewone artifacts → Master/Documentatie. Twee invariant-grenzen blijven hard: AI-powered artifacts (cloud-API) zijn geen productie-AI-laag (lokaal-draaibaar), en memory is geen system of record (brain-vault blijft autoritatief). De PK-auto-RAG-spanning onderbouwt de geplande PK-opschoning.

---

## DOMEIN F — Obsidian + plugins (operationaliseren)

### F.0 De realiteit: de migratiegids is deels achterhaald

`brain/brain__obsidian-migration-guide.md` (13-05-2026) beschrijft een migratie PK → **lokale Obsidian-vault** met *folder*-structuur (`brain__folder__slug.md` → `folder/slug.md`). Wat op 26-05-2026 werkelijk gebeurde is PK → **GitHub-repo** met de **platte** `brain__*`-structuur (compatibel met de claude.ai-PK-filelijst). Obsidian is **nooit toegepast**. De vraag is dus niet "voer de gids uit", maar: **wil je Obsidian als lokale browse-/visualisatie-laag bovenop de bestaande GitHub-repo `brain/`-folder?** Twee gevolgen:
- Obsidian-git pointend op de repo geeft een *platte* folder van ~115 bestanden. Wikilinks + Dataview werken; graph-view/folder-clustering geven minder dan in de folder-structuur die de gids veronderstelde.
- Een echte folder-transformatie zou de platte `brain__*`-conventie + de GitHub-MCP-paden + de entry-points (`brain__index.md`) breken — dus **niet** doen. Obsidian-op-de-platte-repo is de enige zinvolle variant.

**Kernpunt:** Obsidian voegt **niets toe voor de AI-agents** (die gebruiken GitHub-MCP + Claude Code direct file-access). Het is een **menselijke** browse-/visualisatielaag voor Steven — optioneel, laag-risico, reversibel. CLAUDE.md "Optional tooling" noemt Obsidian + Dataview al als optioneel.

### F.1 obsidian-git
**Wat:** synct de Obsidian-vault met de git-repo (auto-commit-interval). Omdat `brain/` al in de repo zit, geeft obsidian-git pointend op de repo lokale browsing + auto-commit zonder aparte migratie.
**Let op invariant:** auto-commit botst met de begin-fase "geen autonome commit" — maar onder de autonomie-koers (§0.5) is dat geen blokker meer; wel via de green-gate (A.5) laten lopen indien geactiveerd. Conflict-risico op `brain__log.md` (single-user-discipline, zie gids-troubleshooting).
**Score:** Waarde 3 · Effort 4 · Invarianten 4 · Overlap 4 · Reversibiliteit 5. **🟢 GO (optioneel, Spoor A)** als je lokaal in de vault wilt werken; anders overbodig naast GitHub-MCP.

### F.2 Dataview
**Wat:** query-bare tabellen over frontmatter (`status`, `date`, `type`, `id`). De brain-bestanden hébben consistente YAML-frontmatter (geverifieerd in de migratiegids + brain-bestand). Queries als "alle open H-items gesorteerd op datum", "alle sprints chronologisch", "modules per laag" werken direct.
**Toepasbaarheid:** dit is de **sterkste** Obsidian-meerwaarde — cross-cutting overzichten over de registers (H-/D-/sprint-/module-register) die nu handmatig worden bijgehouden. Werkt onafhankelijk van platte/folder-structuur.
**Score:** Waarde 4 · Effort 4 · Invarianten 5 · Overlap 5 · Reversibiliteit 5. **🟢 GO (optioneel, Spoor A)** — de aanbevolen eerste Obsidian-plugin als je Obsidian gebruikt. Vereist wél frontmatter-consistentie over de ~115 bestanden (mogelijk een Brein-lint-taak).

### F.3 Templater
**Wat:** templates voor nieuwe `brain__*`-bestanden per type (decision/sprint/H-item).
**Toepasbaarheid:** marginaal — de brain is **LLM-maintained** (Brein-subagent creëert bestanden via Claude Code), niet handmatig geauthored. Templater is voor handmatig aanmaken in Obsidian. **🟡 HOLD** — alleen nuttig als je af en toe handmatig bestanden maakt; anders overbodig.

### F.4 Graph view
**Wat:** visuele D-/H-/sprint-kruisverwijzingen.
**Toepasbaarheid:** nice-to-have voor menselijke navigatie; de **platte** repo-structuur (F.0) vermindert de helderheid (geen folder-clustering, tenzij wikilinks rijk onderhouden). **🟡 HOLD** — leuk, geen probleemoplosser.

### F.5 Obsidian-MCP
**Wat:** MCP-server die Claude de vault laat lezen/schrijven.
**Toepasbaarheid:** **redundant** — agents hebben al GitHub-MCP + Claude Code direct file-access. Een Obsidian-MCP voegt alleen iets toe als Obsidian de *primaire* vault wordt (dat is het niet; de GitHub-repo is dat). **🔴 NO-GO** — dubbele toegangs-laag, Simplicity-First.

### F.6 qmd (semantische BM25+vector-zoek)
**Wat:** hybride lex+vec-zoek over de markdown-vault; in meerdere Karpathy-stacks (Ar9av, ScrapingArt) als optionele accelerator met grep-fallback.
**Toepasbaarheid:** CLAUDE.md noemt qmd voor >150 bestanden; de vault is ~115 — **nadert, niet bereikt**. qmd is bovendien een retrieval-laag; het project is RAG-wars (Karpathy), maar qmd (BM25+vector over eigen markdown, met deterministische grep-fallback) is in CLAUDE.md expliciet als acceptabel-bij-drempel gemarkeerd, los van "vector-DB-RAG" (verworpen). **🟡 HOLD-op-drempel** — heroverweeg bij >150 bestanden; tot dan volstaan index + registers + grep.

### F.7 Karpathy-wiki community-implementaties (her-validatie kfchou + nieuw)

| Bron | Status (28-05-2026) | Wat |
|---|---|---|
| **kfchou/wiki-skills** | Actief (README ~1 mnd) — eval-oordeel bevestigd | wiki-lint (🔴/🟡/🔵-rapport), wiki-audit (parallelle subagent-fact-check per bron), wiki-update (diffs + bron-citatie + stale-claim-sweep) |
| AgriciDaniel/claude-obsidian | **Zeer recent** (~7 uur) | Claude + Obsidian, 11 skills, hot-cache, lint, multi-agent |
| Ar9av/obsidian-wiki | ~1 week | Tiered retrieval (titels/tags/summaries eerst), optionele qmd, integreert kepano/obsidian-skills |
| ScrapingArt/Karpathy-LLM-Wiki-Stack | actief | Build-ready Obsidian+Claude-Code-referentie; "Fallback Rule" (plugin faalt → ripgrep/grep/cat) |
| kepano/obsidian-skills | actief | Obsidian-format-mastery-skills (kepano = Obsidian-maker) |

**Her-validatie kfchou:** ongewijzigd; eval-oordeel **🟡 HOLD installatie + 🟢 GO passieve referentie** staat. De wiki-audit-verb (parallelle bron-fact-check) en de severity-tiered lint-output zijn concrete referenties voor de **Brein-subagent** + een eventuele eigen brain-lint-skill (D.5).

**Overlap/toepasbaarheid (alle):** het project **implementeert het Karpathy-pattern al** (brain-vault + Brein-subagent + sprint-protocollen). Deze community-skills zijn **referentie, geen vervanging** — en de eerdere waarschuwing geldt onverkort: niet een tweede lint-/wiki-pijplijn introduceren naast de Brein-cyclus (discipline-conflict). De project-Brein is bovendien gespecialiseerder (D-decisions, H-items, scope-pauzes, GRC-domein) dan generieke wiki-skills. De "Fallback Rule" van ScrapingArt (deterministische grep-fallback als een tool faalt) is wél een waardevol resilience-patroon dat past bij jullie omgeving.

**🟡 HOLD installatie / 🟢 GO als referentie** voor de eigen brain-lint-skill (D.5) — vergelijk kfchou + AgriciDaniel + ScrapingArt-conventies met de Brein-cyclus, neem bruikbare lint-regels + de Fallback-Rule over, bouw geen tweede systeem.

---

## DOMEIN G — GRC-community-tooling (her-valideer + nieuw)

### G.1 Sushegaad/Claude-Skills-GRC (her-validatie)
Ongewijzigd sinds eval (27-05): 300★/68 forks, actief (README ~22-05), nog geen SECURITY.md, plugin-marketplace-installatie. **Mild credibiliteits-vlaggetje:** de zelf-gerapporteerde benchmark varieert over snapshots (94/72, 95/80, 96/81, 99±4%) — behandel claims als marketing, niet als bewijs. Coverage onveranderd; **geen NL/Rijksoverheid-context** (geen BIO/VIR/VIRBI/CBW/Cbb/ENSIA). **🟡 HOLD** — eval-oordeel bevestigd. *Geen GO:* overlap-risico met formele modellering + NEN-risico ISO-skills onbekend + geen NL-context. *Geen NO-GO:* coverage ISO 42001 (M19-toekomst)/ISO 27701 kan later nut hebben; reversibel.

### G.2 GRCEngClub/claude-grc-engineering (her-validatie)
Actief (README ~2 wkn). SCF-crosswalk **1.468 controls → 249 frameworks**; expliciet *"refereert control-ID's + implementation guidance; reproduceert geen copyrighted normtekst"* (positief NEN-discipline-signaal). Evidence-collection-focus (cloud/SaaS-inspectors). **🟢 NO-GO Spoor A / 🟡 HOLD Spoor B** — eval-oordeel bevestigd: past niet bij formele ontologie-opbouw; relevant bij Spoor-B-lab-test met echte evidence-collection. *Naam-noot:* de marketplace verschijnt ook onder `ethanolivertroy/claude-grc-engineering` — vermoedelijk dezelfde auteur/org; canoniek blijft de GRCEngClub-repo.

### G.3 NIEUW — euCann/OSCAL-GRC-SKILLS
16 agent-skills voor OSCAL (parsing/validatie, control-analyse, **control-mapping via OSCAL 1.2.0 Control-Mapping-model**, risk-assessment, evidence, implementation-narratives, workflow-orchestratie); volgt de Anthropic Agent-Skills-spec; discipline-signaal *"never rely on training knowledge for compliance-critical content"*.
**Toepasbaarheid:** OSCAL's control-mapping is conceptueel verwant aan jullie SKOS-cross-framework-mappings, maar OSCAL is JSON/YAML/XML — een **serialisatie-mismatch** met jullie OWL/Turtle-stack (de eval noemde OSCAL al "past niet zonder bridge"). **🔴 NO-GO (Spoor A) / 🟢 referentie** — bruikbaar als *methodologische* referentie voor cross-framework-mapping-patronen, niet als tooling in de Turtle-stack. Mogelijk relevanter bij Spoor C als externe consumers OSCAL-output willen (bridge-vraag).

### G.4 NIEUW — mlunato47/claude-grc-plugin
Claude Code-plugin, "senior GRC-analist", 72+ reference-files, 15 frameworks, 24 slash-commands, document-review met 0-5 maturity-scoring. **Architectuur-kernpunt:** cross-framework-mapping **"door NIST 800-53 als hub"** — dat is precies een framework-geprivilegieerde architectuur die jullie **D9 (framework-neutraal)** verwerpt. Bovendien US-federaal-gericht (FedRAMP/FISMA/CMMC) — geen NL-relevantie.
**🔴 NO-GO (alle sporen)** — botst met D9 (hub-centrisch) + geen NL-context. *Waarde als contrast:* het illustreert scherp waaróm jullie D9-keuze (geen hub) bewust afwijkt van de gangbare GRC-tooling-aanpak. Geen NEN-/credibiliteits-GO-grond.

### G.5 NIEUW — grcengineering-org (Ayoub Fandi): GRC Companion / Daily Findings / gigachad-grc
GRC-leertools (Companion: vendor-reviews/audits → learning loops; Daily Findings: le-app) + **gigachad-grc** (volledig open-source GRC-platform: SOC2/ISO27001/HIPAA, risk-registers, vendor-assessments, AI-powered, containerized).
**Toepasbaarheid:** dit zijn **producten/platforms**, geen Claude-extensies voor ontologie-werk. gigachad-grc is conceptueel een *andere* invulling van "GRC-systeem" dan jullie ontologie-model (en geen ontologie-gedreven). **🔴 NO-GO** — verkeerde categorie; geen fit met het ontologie-/Spoor-A-doel. Hooguit inspiratie voor Spoor-B/C-UX.

### G.6 Overdraagbaarheids-observatie (de eigenlijke conclusie van domein G)
Alle gevonden GRC-tooling deelt drie eigenschappen die ze ongeschikt maken voor directe adoptie: (1) **EN/US-centrisch** — geen enkele dekt NL/Rijksoverheid (BIO/VIR/VIRBI/CBW/Cbb/ENSIA/COSO/COBIT/BVA/CIO-stelsel); (2) **framework-geprivilegieerd** — hub-centrisch (mlunato47: NIST 800-53-hub) of crosswalk-backbone (GRCEngClub: SCF), beide in spanning met **D9-neutraliteit**; (3) **andere serialisatie/doel** — OSCAL (JSON/XML), evidence-collection, of volledige GRC-platforms, geen OWL 2 DL-ontologie.

Dit **bevestigt twee dingen uit eerdere installments:** (a) de **D.7 GRC-domein-skill** (NL-kaders) is een echte, niet-extern-verkrijgbare lacune — geen van deze tools vult hem; (b) SCF/OSCAL-crosswalks zijn waardevolle **methodologische referenties** voor jullie eigen SKOS-cross-framework-werk, maar door D9 + de OWL/Turtle-stack niet als-is adopteerbaar.

---

## EIND-SAMENVATTING — alle domeinen A–I

Geconsolideerd overzicht (bottom-up-discipline: dit is de samenvatting ná alle detail).

| # | Kandidaat | Domein | Recommendation |
|---|---|---|---|
| A.1 | CLAUDE.md + `.claude/rules/` | A | 🟢 GO |
| A.2 | Skills (mechanisme) | A | 🟢 GO |
| A.3 | Slash-commands | A | 🟢 GO gefaseerd |
| A.4 | Subagents | A | 🟢 GO (in gebruik) |
| A.5 | **Hooks** | A | 🟢 **GO — hoogste prioriteit (fundering autonomie)** |
| A.6 | Plugins + marketplaces | A | 🟡 HOLD → GO bij Spoor B |
| A.7 | MCP (mechanisme) | A | 🟢 GO (in gebruik) |
| A.8 | Settings/permissions | A | 🟢 GO |
| A.9 | Agent SDK/headless/CI | A | 🟢 GO-trajectorie A / 🟡 HOLD cloud-CI Spoor B |
| A.10 | Code intelligence | A | 🔴 NO-GO |
| A.10 | Checkpoint/AgentView/`/goal` | A | 🟡 HOLD (research-preview) |
| A.10 | Output styles | A | 🟡 HOLD (status onzeker) |
| B.1 | Projects + project knowledge | B | 🟢 GO (in gebruik; PK-opschoning) |
| B.2 | Skills in claude.ai | B | 🟢 GO (overbrugt claude.ai↔Claude-Code) |
| B.3 | Connectors / MCP apps | B | 🟢 GO (in gebruik) |
| B.4 | Memory | B | 🟢 GO als gemakslaag / 🟡 grens (geen system of record) |
| B.5 | Research / deep research | B | 🟢 GO (Analyse) |
| B.6 | Artifacts gewoon / AI-powered | B | 🟢 GO gewoon / 🟡 HOLD AI-powered (lokaal-draaibaar) |
| B.7 | Custom writing styles | B | 🟢 GO (Documentatie) |
| B.8 | Analysis / code-execution | B | 🟢 GO (Analyse) |
| C.1 | docx | C | 🟢 GO (Documentatie) |
| C.2 | pptx | C | 🟢 GO (Documentatie/Master) |
| C.3 | xlsx | C | 🟢 GO (Analyse) |
| C.4 | pdf / pdf-reading | C | 🟢 GO (NEN-parafrase-discipline blijft) |
| C.5 | frontend-design | C | 🟢 GO (Dashboard) |
| C.6 | skill-creator | C | 🟢 GO (enabler domein D) |
| C.7 | mcp-builder | C | 🔴 NO-GO / 🟡 HOLD |
| D.1 | canonical-metrics-skill | D | 🟢 GO |
| D.2 | SHACL-split-skill | D | 🟢 GO |
| D.3 | patch-rapport-generator-skill | D | 🟢 GO |
| D.4 | SKOS-classificatie-skill | D | 🟢 GO (timing: T3) |
| D.5 | brain-lint-skill | D | 🟡 HOLD → GO na kfchou-vergelijking |
| D.6 | protocol-handhaving (hooks+commands) | D | 🟢 GO gefaseerd |
| D.7 | **GRC-domein-skill (NL-kaders)** | D | 🟢 **GO (unieke lacune — domein G bevestigt)** |
| D.8 | eigen RDF/SPARQL/SHACL-MCP | D | 🔴 NO-GO |
| E.1 | GitHub-MCP | E | 🟢 GO (in gebruik) |
| E.2 | open-ontologies-MCP | E | 🟡 HOLD + evaluatie-sprint (prio ↑) |
| E.3 | lichte SPARQL-/RDF-MCP-wrappers | E | 🔴 NO-GO A / 🟡 HOLD Spoor C |
| E.4 | OntoBricks / niet-RDF graph-DB-MCP | E | 🔴 NO-GO |
| H.1 | open-ontologies reasoner-profielen (H37/H38/H41) | H | 🟡 HOLD — evaluatie-sprint |
| H.2 | rdflib+owlrl+pySHACL (huidige stack) | H | 🟢 GO (behouden) |
| H.3 | LLM-ontologie-engineering-methoden | H | 🟢 GO (referentie) |
| H.4 | OWL+SHACL cross-ref + SKOS-validatie-shapes | H | 🟡 HOLD-kandidaat / mogelijk H-item |
| H.5 | Protégé (desktop cross-check) | H | 🟢 GO (behouden) |
| I.1 | Huidige zeven-chat-opzet | I | 🟢 behouden, met overgang |
| I.2b | Agent teams | I | 🟡 HOLD-op-volwassenheid → 🟢 GO-trajectorie |
| I.2d | Hook-gedreven scope-grens-gate | I | 🟢 GO-kandidaat |
| I.2e | Parallelle subagents | I | 🟢 GO-kandidaat |
| F.1 | obsidian-git | F | 🟢 GO (optioneel) |
| F.2 | Dataview | F | 🟢 GO (optioneel — sterkste Obsidian-meerwaarde) |
| F.3 | Templater | F | 🟡 HOLD |
| F.4 | Graph view | F | 🟡 HOLD |
| F.5 | Obsidian-MCP | F | 🔴 NO-GO (redundant) |
| F.6 | qmd | F | 🟡 HOLD-op-drempel (>150 bestanden) |
| F.7 | Karpathy-wiki-skills (kfchou e.a.) | F | 🟡 HOLD installatie / 🟢 GO referentie |
| G.1 | Sushegaad GRC-skills | G | 🟡 HOLD |
| G.2 | GRCEngClub | G | 🔴 NO-GO A / 🟡 HOLD B |
| G.3 | euCann/OSCAL-GRC-SKILLS | G | 🔴 NO-GO / 🟢 referentie |
| G.4 | mlunato47/claude-grc-plugin | G | 🔴 NO-GO (D9-conflict) |
| G.5 | grcengineering (platforms) | G | 🔴 NO-GO (verkeerde categorie) |

**De drie rode draden over A–I:**

1. **De grootste winst is intern, niet extern.** Vrijwel alle externe GRC-tooling (domein G) en de meeste MCP-servers (domein E) zijn NO-GO — wegens D9-conflict, NL-lacune, serialisatie-mismatch of redundantie. De waarde zit in het **invullen van je eigen lege `.claude/`-ruimte** (hooks, skills, permissions — domeinen A + D) en in een handvol claude.ai-features die elk een specifieke chat bedienen (domein B). De externe wereld levert vooral *referenties* (Karpathy-wiki-conventies, SCF/OSCAL-crosswalk-methode, ontologie-engineering-literatuur), geen kant-en-klare adoptie.

2. **De autonomie-koers (§0.5) ordent de prioriteiten.** Het pad is: éérst de deterministische toezicht-envelop (hooks-green-gate + audit-trail + permissions + verificatie-skills D.1/D.2), dán de uitvoeringslaag autonomiseren (parallelle subagents → agent teams), met check-gated CI erbovenop. Skills draaien over claude.ai én Claude Code, wat de twee werelden overbrugt. Twee invariant-grenzen blijven hard: lokaal-draaibaar (geen AI-powered-artifact/cloud-CI als productie-AI-laag) en mens-in-controle-als-toezicht (geen black-box; brain-vault blijft system of record, geen memory).

3. **Eén echt unieke bouwopdracht bevestigd.** Domein G bewijst dat geen externe tool de NL/Rijksoverheid-kaders dekt en dat de gangbare tooling framework-geprivilegieerd is — wat de **GRC-domein-skill (D.7)** tot de meest waardevolle eigen-bouw maakt, naast de verificatie-skills.

---

## Concrete vervolgstappen

### Onmiddellijk (geen ontologie-/architectuur-impact)
1. **Masterchat-besluit over §0.5** — formaliseer de operating-model-koers (autonomie-met-toezicht) als nieuw D-/scope-besluit, met expliciete definitie van "mens-in-controle in de eindfase" (toezicht/override/audit, niet per-stap). Dit is de voorwaarde waaronder alle autonomie-GO's gelden.
2. **Bouw de verificatie- + guardrail-laag eerst** (Spoor A): A.5-hooks (secret-scan/disclosure/scope-grens green-gate + audit-trail) via skill-creator (C.6), plus D.1 canonical-metrics-skill + D.2 SHACL-split-skill. Hoog nut, laag risico, dekt het PAT-leerpunt.
3. **A.8 settings/permissions** — maak de subagent-rolscheiding afdwingbaar (deny-regels per subagent).

### Middellange termijn
4. **D.3 patch-rapport-skill + D.6 protocol-handhaving** (hooks+commands) — codificeer de 17 protocollen naar het juiste mechanisme.
5. **D.7 GRC-domein-skill** (NL-kaders) — de unieke lacune; zwaarste bouw, hoogste eigenheid.
6. **open-ontologies-evaluatie-sprint (E.2/H.1)** — H37/H38/H41 tegelijk; `owl-dl`-tableaux testen op `grc-v4_6_2-merged.ttl`; geen migratie-besluit, alleen empirie. Prioriteit verhoogd door de autonomie-koers.
7. **D.4 SKOS-classificatie-skill** — bouwen wanneer T3 (m14) concreet wordt.

### Optioneel
8. **Obsidian (F.1+F.2)** als persoonlijke browse-laag op de repo (Dataview voor H-/sprint-overzichten) — alleen als je lokaal in de vault wilt werken.
9. **Agent teams (I.2b)** — afgebakende read-only pilot ná de guardrail-laag + zodra GA; begin eventueel met parallelle subagents (I.2e, goedkoper/GA).
10. **kfchou + AgriciDaniel + ScrapingArt-conventies** vergelijken met de Brein-cyclus → bruikbare lint-regels + de "Fallback-Rule" overnemen in D.5 (geen tweede systeem).
11. **Check-gated CI (A.9)** — non-merging/green-gate-CI als bovenliggende automatisering, ná hooks/skills.

---

## Werkstroom-status na deze analyse

| Item | Status |
|---|---|
| Extensie-oppervlakte-analyse A–I | ✓ afgerond (dit rapport, 4 installments) |
| Iets daadwerkelijk geactiveerd/geïnstalleerd | ✗ geen — Analyse-deliverable, geen Claude Code-/ontologie-actie |
| Her-validatie 4 eerdere kandidaten | ✓ Sushegaad/GRCEngClub/open-ontologies/kfchou — alle eval-oordelen bevestigd, geen wijziging sinds 27-05 |
| Nieuwe externe kandidaten gevonden | euCann/OSCAL-GRC-SKILLS, mlunato47/claude-grc-plugin, grcengineering-org, AgriciDaniel/claude-obsidian e.a. — alle NO-GO of referentie |
| **Mogelijk nieuw H-item** | **H42-kandidaat:** deterministische guardrail-/audit-laag (hooks-green-gate) als architectuur-fundament voor autonome uitvoering — koppelen aan §0.5-besluit |
| **Mogelijk nieuw H-item** | **H43-kandidaat:** SHACL-shape voor SKOS-predicate-distributie (H.4) — koppelen aan bestaand **H39** (SHACL-blinde-vlek SKOS-distributie) |
| Bestaande H-items geraakt | H37/H38/H41 (open-ontologies-evaluatie, prio ↑); H39 (SKOS-distributie-shape); H40 (UI-renderdekking — raakt frontend-design C.5) |
| Architectuurbesluit nodig (masterchat) | §0.5 operating-model-formalisering (autonomie-met-toezicht) als D-/scope-besluit |
| Brain-vault-update-suggestie | Dit rapport als `brain__scope__extensie-landschap-2026-05-28.md` of `brain__concepts__*` opnemen (Brein-cyclus, masterchat-besluit); §0.5-koers + H42/H43-kandidaten in de relevante registers |
| Invarianten geraakt | Lokaal-draaibaar (AI-powered artifacts / cloud-CI begrensd); mens-in-controle hercodeerd naar toezicht-niveau (§0.5); NEN-discipline (Sushegaad-risico, pdf/xlsx-skills, GRC-domein-skill) bewaakt; D9 (afwijzing hub-centrische GRC-tooling) |

---

*Einde rapport — installments 1–4 compleet, alle domeinen A–I gedekt. Dit is een Analyse-chat-deliverable: geen ontologie-mutatie, geen architectuurbesluit, geen autonome commit. Alle aanbevelingen — met name de §0.5-operating-model-formalisering en de H42/H43-kandidaten — gaan naar de masterchat. Steven inspecteert en commit handmatig.*
