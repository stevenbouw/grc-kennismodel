# Overdrachtsrapport — GRC Kennismodel

*Dit document is geschreven voor de opvolgend beheerder van het GRC Kennismodel-project.
Het gaat ervan uit dat je redelijk nieuw bent met Claude en volledig nieuw met Claude
Code. Lees het één keer volledig door vóór je iets doet; daarna kun je het als naslag
gebruiken. Alles wat je nodig hebt om de workflow over te nemen staat hierin of wordt
hierin aangewezen.*

*Conventie: de organisatie wordt in dit project nooit bij naam genoemd — altijd
"de organisatie" of "de Rijksoverheidsorganisatie". Houd je daaraan in alle
deliverables; het is een harde projectregel, geen stijlkeuze.*

---

## DEEL 0 — Lees dit eerst (oriëntatie in 5 minuten)

**Wat is dit project?** Een *kennismodel*: een formele, computer-leesbare
representatie (een ontologie) die alle voor de organisatie relevante
informatiebeveiligings- en governance-kaders integreert — Nederlandse regelgeving
(BIO 2.0, NIS2/Cbb, VIRBI) en internationale standaarden (ISO 27001/27002, NIST
800-53, e.a.) — en de onderlinge relaties daartussen expliciet maakt. Bovenop dat
model staan twee gebruikersproducten: een grafverkenner (Spoor A) en een operationeel
dashboard (Spoor B).

**Hoe wordt eraan gewerkt?** Niet door één persoon in één chat. Het project gebruikt
een **meervoudige Claude-architectuur**: een coördinerende "masterchat" (strategie en
beslissingen) plus gespecialiseerde subagents in Claude Code (die het echte
schrijf-/codeerwerk doen). De mens (jij) is de spil: jij geeft opdrachten, inspecteert
resultaten en bent de enige die naar GitHub commit. Zie Deel 3.

**Waar staat alles?** In één publieke GitHub-repo: `stevenbouw/grc-kennismodel`. Daarin:
de ontologie (`ontology/`), het dashboard (`dashboard/`), de instructies (`docs/`),
de rapporten (`output/`), de scripts (`scripts/`), en — cruciaal — de **brain-vault**
(`brain/`): het collectieve geheugen van het project.

**De allerbelangrijkste regel om te onthouden:** de `brain/`-vault is de autoritatieve
bron voor projecthistorie, beslissingen en conventies. Als dit overdrachtsrapport ooit
afwijkt van de brain-vault, heeft de brain-vault gelijk (die wordt continu bijgewerkt;
dit rapport is een momentopname).

**Leesvolgorde die ik je aanraad:**
1. Dit Deel 0 + Deel 1 (waarom bestaat het project).
2. Deel 2 (setup van je gereedschap — Claude, Claude Code, GitHub).
3. Deel 3 (de werkwijze: chats, agents, commit-discipline).
4. Deel 4 (de repo-structuur in detail).
5. Deel 5 (waar het project nu staat + open werk).
6. Deel 6–8 (naslag: registers, valkuilen, eerste-week-checklist).

---

## DEEL 1 — Doel, visie, missie

### 1.1 Het probleem dat het oplost
Een Rijksoverheidsorganisatie moet aantoonbaar voldoen aan een groot aantal kaders
tegelijk: Nederlandse wet- en regelgeving (verplicht), plus internationale normen en
best practices. Die kaders overlappen, spreken elkaar soms tegen, en gebruiken
verschillende terminologie voor dezelfde onderliggende beheersmaatregel. In de praktijk
leidt dat tot losse spreadsheets per kader, dubbel werk, en gaten die niemand ziet.

### 1.2 De oplossing
Eén geïntegreerd kennismodel waarin elke beheersmaatregel (control), elke verplichting
en elk principe één keer bestaat, en waarin de relaties tussen kaders *expliciet en
machine-leesbaar* zijn gelegd (via SKOS-mappings: "deze ISO-control komt overeen met
die BIO-maatregel"). Daarbovenop:
- **Spoor A** (`grc-explorer`): een grafverkenner om het model visueel te
  doorzoeken (gebouwd met Cytoscape).
- **Spoor B** (`grc-dashboard`): een operationeel dashboard dat de *uitkomsten* toont —
  nalevingsstatus, openstaande risico's, verantwoordelijkheid — voor een CSO/CISO en
  bestuur.

### 1.3 De vijf oorspronkelijke projectdoelen
1. Geünificeerde control-taxonomie + cross-framework GRC-referentiemodel.
2. RACI-matrices afgestemd op Nederlandse governance-structuren (CIO-stelsel, BVA-stelsel).
3. Governance-dashboards die GRC aan bedrijfsdoelstellingen koppelen.
4. Een ISO 27001:2022-gebaseerd ISMS dat BIO 2.0 en NIST 800-53 Rev. 5 integreert.
5. Een formele OWL 2 DL-ontologie, Turtle-serialisatie, tweetalig (NL/EN), compatibel
   met Protégé en Apache Jena Fuseki.

### 1.4 Kernfilosofie (de "waarom zo"-principes)
- **Framework-neutraliteit (beslissing D9):** alle kaders zijn gelijkwaardig in het
  model. BIO 2.0 mag in het dashboard prominent als *primair perspectief* getoond
  worden, maar dat is een *weergavekeuze*, geen architecturale hiërarchie. Dit is een
  harde regel — zie `brain/brain__decisions__D09_framework-neutraliteit.md`.
- **Het dashboard toont, het model rekent niet.** Het is geen risico-rekenmachine en
  geen audit-tool die zelf oordeelt. Het positioneert uitkomsten van menselijk werk.
- **Comply or explain:** controls kunnen "uitgesloten met motivering" zijn — dat is een
  geldige status, geen gat.
- **§0.5 autonomie-firewall:** er wordt géén autonome AI-functionaliteit gebouwd, onder
  geen enkele framing. Dit is bewust geparkeerd en blijft hard tot de eigenaar er
  expliciet om vraagt.

### 1.5 Wat NIET in scope is
Bewust buiten de huidige fase gehouden (zie `brain/brain__scope__*`): ISO 42001
(AI-managementsysteem), ISO 9001 (kwaliteit), en de UCF (Unified Compliance Framework).
Deze staan gedocumenteerd als expliciete scope-uitsluitingen, zodat ze niet per ongeluk
weer instromen.

---

## DEEL 2 — Setup van A tot Z (Claude, Claude Code, GitHub)

*Dit deel neemt aan dat je nog niets hebt ingericht. Werk het in volgorde af.*

### 2.1 Wat je nodig hebt
- Een **Claude-account** (claude.ai) — voor de masterchat en de claude.ai-only chats.
- **Claude Code** — de tool waarmee de subagents code en bestanden bewerken op jouw
  machine. Dit is een apart programma dat je lokaal installeert.
- **Git + een GitHub-account** met toegang tot `stevenbouw/grc-kennismodel` (de repo
  staat publiek, dus lezen kan altijd; voor pushen heb je schrijfrechten of een eigen
  fork nodig — regel dit met de eigenaar).
- **Python 3** (de hooks en scripts draaien op Python 3; versie 3.11 is in gebruik
  geweest).
- **Node.js** (was al geïnstalleerd in de oorspronkelijke setup; Claude Code en enkele
  verificatietools gebruiken het).

### 2.2 Claude (claude.ai) inrichten
1. Maak/één Claude Project aan voor het GRC-werk. Een "Project" in claude.ai bundelt
   chats met gedeelde projectkennis.
2. Upload het **overdrachts-/sessierapport** als project-knowledge (zie Deel 5 over
   welk document de actuele start is). Dit is wat een nieuwe masterchat-sessie als
   eerste leest.
3. Begrijp het verschil tussen de chats die je gaat gebruiken (Deel 3.1). Je hebt
   minimaal een **masterchat** nodig; de subagents draaien in Claude Code, niet hier.
4. **Memory/geheugen:** Claude.ai kan een geheugen over gesprekken opbouwen. Dat is
   handig maar **niet** de autoritatieve projecthistorie — de brain-vault in de repo is
   dat. Vertrouw voor feiten altijd op de repo, niet op het chatgeheugen.

### 2.3 GitHub koppelen aan Claude (MCP)
De masterchat heeft toegang tot de repo via een **GitHub-MCP-koppeling** (MCP = Model
Context Protocol; het mechanisme waarmee Claude externe tools gebruikt). Hiermee kan de
masterchat bestanden lezen (`get_file_contents`) en — beperkt — pushen (`push_files`).
- Controleer in de Claude-instellingen dat de GitHub-connector actief is en naar
  `stevenbouw/grc-kennismodel` wijst.
- Test door de masterchat te vragen `brain/brain__index.md` op te halen. Krijg je de
  inhoud terug, dan werkt de koppeling.
- **Belangrijk:** de masterchat mag alleen naar de **docs-laag** pushen (zie 3.4). Alle
  code en ontologie gaat via Claude Code + jouw handmatige commit.

### 2.4 Claude Code installeren en koppelen
Claude Code is de agentische tool waarmee de subagents lokaal werken. Globaal:
1. Installeer Claude Code volgens de officiële instructies van Anthropic
   (docs.claude.com). Omdat je hier nieuw mee bent: neem de tijd voor de "getting
   started" en draai eerst een triviaal testproject voor je het op de echte repo
   loslaat.
2. **Kloon de repo lokaal:**
   `git clone https://github.com/stevenbouw/grc-kennismodel.git`
   Onthoud waar je 'm neerzet (in de oorspronkelijke setup stond hij op het Bureaublad:
   `~/Desktop/grc-kennismodel`). Je hebt dit pad vaak nodig.
3. Open de repo-map in Claude Code. Claude Code leest dan automatisch het
   **`CLAUDE.md`**-bestand in de repo-root (de projectinstructie voor Claude Code) én
   de **`.claude/`-laag** (instellingen, agents, skills, hooks — zie Deel 3).
4. **Verifieer dat de guardrails actief zijn** (zie 2.5). Dit is geen optie maar een
   voorwaarde.

### 2.5 De `.claude/`-guardrails begrijpen (vóór je een agent loslaat)
In `.claude/settings.json` staan deterministische beveiligingen die het project veilig
houden, ook als een agent iets verkeerds probeert:
- **`permissions.deny`** blokkeert `git commit` en `git push` volledig. Dit codificeert
  de harde regel: **subagents committen nooit zelf.** Jij commit, altijd, handmatig.
- **`permissions.ask`** vraagt bevestiging voor riskante commando's (`git add`,
  `git reset`, `git checkout`, `rm -r`, enz.).
- **`permissions.allow`** staat veilige lees-/inspectiecommando's toe (`git status`,
  `git diff`, `python3`, `ls`, `grep`, `cat`, enz.).
- **`hooks`** draaien automatisch bij bepaalde acties (zie Deel 3.6): een secret-scan en
  een disclosure-check vóór elke schrijf-/bewerk-actie, een versie-suffix-check ná een
  schrijfactie, en een context-injectie bij sessiestart.

Als deze guardrails niet actief lijken (bijv. een commit lukt zonder weerstand), stop
en zoek uit waarom voordat je verder werkt — de hele veiligheid van de workflow hangt
hieraan.

### 2.6 Het dashboard lokaal bekijken
Het dashboard (`dashboard/grc-dashboard-v3-2.html`) gebruikt een lokale database-engine
(SQL.js) die **niet** laadt vanaf een `file://`-pad. Je moet een lokale webserver
draaien:
```
cd ~/Desktop/grc-kennismodel/dashboard      # pas pad aan naar jouw kloon
python3 -m http.server 8100
```
Open daarna `http://127.0.0.1:8100/grc-dashboard-v3-2.html`.
- Krijg je `Address already in use`? Kies een ander poortnummer (8101, 8200, …) en pas
  dat ook in de URL aan.
- Krijg je `404`? Dan sta je in de verkeerde map of klopt de bestandsnaam niet. Ga naar
  `http://127.0.0.1:8100/` (zonder bestandsnaam) voor een klikbare bestandslijst.
- Laat het terminalvenster open zolang je kijkt; sluit het netjes met Ctrl+C.

---

## DEEL 3 — Werkwijze: chats, agents, skills, hooks, commit-discipline

*Dit is het hart van de workflow. Als je dit deel begrijpt, begrijp je hoe het project
draait.*

### 3.1 De meervoudige chat-architectuur
Het project gebruikt meerdere gespecialiseerde Claude-rollen (zie
`brain/brain__workflow__zes-chat-architectuur.md`). Twee soorten:

**A. Chats in claude.ai (geen directe repo-bewerking):**
- **Masterchat** — projectadviseur + GRC-architect. Strategie, sparring,
  architectuurbeslissingen, prioritering, scope-besluiten, sprint-instructies en
  eind-sign-off. Schrijft zelf géén ontologie-code, dashboard-code of beleid. Heeft
  GitHub-MCP-leestoegang + beperkte docs-push. **Dit is de chat waarin je het meeste
  zult werken.**
- **Analyse-chat** en **Documentatie-chat** — ondersteunend, zonder repo-toegang.
  Instructies hiervoor gaan *inline* via de masterchat; jij kopieert ze handmatig naar
  de doel-chat.

**B. Subagents in Claude Code (bewerken lokaal de repo):**
- **Tech** — ontologie-werk (Turtle/SPARQL/SHACL). Zie `.claude/agents/tech.md`.
- **Brein** — onderhoudt de brain-vault. Zie `.claude/agents/brein.md`.
- **Dashboard** — bouwt Spoor B. Zie `.claude/agents/dashboard.md`.

### 3.2 De gouden werkstroom (zo verloopt elke sprint)
1. **Masterchat** bespreekt met jou wát er moet gebeuren en schrijft een
   *sprint-instructie* (een markdown-bestand in `docs/instructies/`).
2. Masterchat pusht die instructie naar de repo (docs-laag — toegestaan).
3. **Jij** geeft de betreffende **subagent in Claude Code** opdracht die instructie uit
   te voeren (je verwijst naar het instructiebestand in de repo).
4. De subagent voert uit en levert een **patch-rapport** op (in `output/reports/`),
   maar **commit niet**.
5. **Jij** inspecteert `git status` en `git diff`, draait het dashboard/de tests
   desgewenst, en **commit + pusht handmatig**.
6. **Masterchat verifieert het resultaat aan de bron** via GitHub-MCP — niet op het
   patch-rapport vertrouwen, maar de echte bestanden lezen. Pas dan is een stap "klaar".

### 3.3 Verificatie-discipline (waarom stap 6 niet overgeslagen wordt)
Een subagent kan in een rapport "axe = 0" of "alle tests groen" schrijven terwijl de
werkelijkheid anders is — niet uit kwade wil, maar omdat een rapport een claim is, geen
bewijs. De masterchat verifieert daarom cijfers, version-triples en kernwijzigingen
zelf aan de bron. Neem deze gewoonte over: **vertrouw nooit blind op een rapport.**

### 3.4 Commit/push-werkverdeling (de belangrijkste veiligheidsregel)
Zie `brain/brain__workflow__commit-push-werkverdeling.md`. Kort:
- **Subagents committen NOOIT.** Hard afgedwongen via `.claude/settings.json`.
- **Masterchat** mag zelf pushen, maar **alleen naar de docs-laag**
  (`docs/instructies/`, `docs/handovers/`, `docs/projectinstructie-*`, e.d.). NOOIT naar
  `ontology/`, `dashboard/`, `scripts/` of `grc-shacl.ttl`.
- Vóór elke masterchat-push: expliciet aankondigen **wat** en **waarom**; bij
  gevoelige/contested beslissingen eerst jouw bevestiging vragen. (Dit compenseert dat
  er bij een directe push geen menselijke diff-controle is.)
- **Alle code en ontologie** gaat via een subagent + **jouw handmatige commit**.

### 3.5 De agents in detail
Elke agent is een markdown-bestand in `.claude/agents/` dat zijn rol, grenzen en
werkwijze vastlegt. Lees ze één keer volledig:
- **`tech.md`** (~11 kB) — de ontologie-specialist.
- **`brein.md`** (~12 kB) — de geheugenbeheerder (brain-vault).
- **`dashboard.md`** (~13 kB) — de dashboard-bouwer.
Ze delen de invarianten uit Deel 1.4 en de commit-discipline uit 3.4.

### 3.6 De hooks in detail (`.claude/hooks/`)
Hooks zijn scripts die Claude Code automatisch draait. Ze zijn je vangnet:
- **`secret-scan.py`** (PreToolUse, bij Write/Edit) — blokkeert het wegschrijven van
  geheimen (API-keys, wachtwoorden, tokens).
- **`disclosure-check.py`** (PreToolUse, bij Write/Edit) — controleert op ongewenste
  openbaarmaking (categorieën 1–4; denk aan de organisatienaam, gevoelige
  combinaties). Configuratie in `disclosure-config.json`; je kunt een lokale
  override maken met `disclosure-config.local.json` (zie het `.example`-bestand).
- **`versie-suffix-check.py`** (PostToolUse, bij Write) — bewaakt de versie-/
  bestandsnaamconventies.
- **`sessionstart-context.sh`** (SessionStart) — injecteert bij het starten/hervatten
  van een Claude Code-sessie automatisch de juiste projectcontext.

### 3.7 De skills in detail (`.claude/skills/`)
Skills zijn herbruikbare instructiepakketten die een agent kan inladen voor een
specifieke taak. Aanwezig:
- **`grc-domein`** — kennis van de Nederlandse kaders (de "D.7"-domeinskill).
- **`canonical-metrics`** — de gestandaardiseerde meetgetallen van het model.
- **`ontology-conformance`** — OWL/DL-conformiteitscontroles.
- **`shacl-split`** — gesplitste SHACL-validatie.
- **`pre-sprint-inventarisatie`** — de vaste pre-sprint-inventarisatie.
- **`patch-rapport`** en **`report-structure`** — de vaste vorm van opleverrapporten.
- **`repo-reference`** — repo-oriëntatie.
- **`applier-template`** — sjabloon voor patch-appliers.

### 3.8 De sprint-protocollen
Er bestaan genummerde sprint-protocollen (1–18) die de vaste stappen van een sprint
vastleggen — zie `brain/brain__workflow__sprint-protocollen.md` en `docs/sprint-protocols.md`.
Protocol 18 is bijvoorbeeld de pre-sprint-dashboard-checklist. Je hoeft ze niet uit je
hoofd te kennen; weet dat ze bestaan en dat instructies ernaar verwijzen.

---

## DEEL 4 — Repo-structuur in detail

Top-level van `stevenbouw/grc-kennismodel`:

| Map / bestand | Inhoud |
|---|---|
| `CLAUDE.md` | Projectinstructie die Claude Code automatisch leest (~14 kB). |
| `README.md` | Publieke projectbeschrijving. |
| `.claude/` | Agents, skills, hooks, `settings.json` (zie Deel 3). |
| `brain/` | De brain-vault — collectief projectgeheugen (zie 4.1). |
| `ontology/` | De ontologie zelf: modules m01–m18 in Turtle (zie 4.2). |
| `dashboard/` | Spoor B — het operationele dashboard + design-tokens + vendor. |
| `docs/` | Instructies, projectinstructie, handovers, protocollen. |
| `output/` | Rapporten (`output/reports/`): patch-, pilot-, sprint-, axe-rapporten. |
| `scripts/` | Build-/hulpscripts (o.a. de ontologie→dashboard-import). |
| `sources/` | Bronmateriaal-referenties (let op licentie; zie 4.4). |
| `apply_patch_v4_6_1.py` | Voorbeeld van een patch-applier-script. |

### 4.1 De brain-vault (`brain/`) — leer deze kennen
Dit is het belangrijkste deel om te begrijpen. De vault is een set markdown-bestanden
met een vaste naamconventie `brain__<categorie>__<onderwerp>.md`. Begin altijd bij:
- **`brain__index.md`** — de index + actuele iteratie-stand. **Je eerste leesbestand.**
- **`brain__CLAUDE.md`** — instructie voor de Brein-agent over hoe de vault te
  onderhouden.
- **`brain__log.md`** — chronologisch logboek (~66 kB; de geschiedenis).

Registers (overzichtsbestanden per categorie):
- **`brain__decisions__D-register.md`** + losse `D01`–`D12` — de architectuur-
  beslissingen. D9 (framework-neutraliteit) en D4 (SKOS cross-framework) zijn de
  belangrijkste. Wijzig een D-decision NOOIT zonder expliciete beslissing.
- **`brain__architecture__H-register.md`** + losse `H15`–`H41` — de "H-items":
  openstaande en opgeloste architectuur-/onderzoeksvragen.
- **`brain__modules__module-register.md`** + losse `M01`–`M18`/`M21` — per ontologie-
  module een notitie.
- **`brain__sprints__sprint-register.md`** + losse sprint-notities (v0 t/m v4.6.4, T1–T3)
  — de volledige sprinthistorie.
- **`brain__concepts__*`** — kernconcepten (framework-neutraliteit, drie-laags-
  compliance, cross-category-mappings, canonical-metrics, scope-discipline, dashboard-
  productlijnen, Spoor B-revival, enz.).
- **`brain__scope__*`** — wat bewust buiten scope is.
- **`brain__sources__*`** — per bron een notitie (BIO 2.0, ISO-bundle, NIST, NL-
  wetgeving, CBW, ENISA, enz.).
- **`brain__workflow__*`** — de werkwijze (zes-chat-architectuur, commit-push-
  werkverdeling, masterchat-interactie, opleveringsprotocol, sprint-protocollen,
  opzet/bestaan/werking, scope-discipline).
- **`brain__smoke-tests.md`** — snelle controles om te zien of het model nog klopt.
- **`brain__obsidian-migration-guide.md`** — de vault is ook als Obsidian-kluis te
  openen (handig om de wikilinks/graaf te navigeren).

### 4.2 De ontologie (`ontology/`)
De ontologie is modulair opgesplitst in Turtle-bestanden `m01`–`m18` (plus m21 gepland).
Globaal (zie `brain__modules__module-register.md` voor de precieze stand):
- m01 framework · m02 ISO 27002-control · m03 risk · m04 roles · m05 compliance ·
  m06 ISMS · m07 business · m08 BIO 2.0 · m09 ISO 27001-ext · m10 NIS2-ext ·
  m11 NIST 800-53 · m12 DORA (referentie, n.v.t.) · m13 ISO 22301 · m14 AVG/GDPR ·
  m15 ENSIA · m16 VIRBI-ext · m17 COSO/COBIT · m18 assets · m21 NIST CSF 2.0 (gepland).
- Validatie gebeurt via SHACL (`grc-shacl.ttl`) en reasoners (OWL RL + HermiT).
- **DL-conformiteitsregel:** vrije-tekst-properties krijgen `rdfs:Literal`-range, niet
  `xsd:string`; periodieke HermiT-her-run is het vangnet tegen onzichtbare
  inconsistenties.

### 4.3 Het dashboard (`dashboard/`)
- `grc-dashboard-v3-2.html` — het single-file operationele dashboard (Spoor B).
- `design-tokens-grc-dashboard.css` — de visuele tokens (kleuren, fonts, spacing).
- `vendor/` — lokaal gevendorde libraries (SQL.js, Chart.js, fonts) — want het
  dashboard moet **volledig offline** werken: geen CDN, geen externe fonts/iconen.
- Stand & ontwerpbeslissingen: zie 5.3 en `brain__concepts__dashboard-productlijnen.md`
  + `brain__concepts__spoor-b-revival.md`.

### 4.4 Bronnen (`sources/`) — let op
Sommige bronnen zijn licentie-restrictief (bv. NEN-normen). Die mogen niet vrij
verspreid worden. Wees voorzichtig met wat je uit `sources/` deelt of kopieert; de
disclosure-hook helpt, maar gebruik ook je eigen oordeel. De repo staat publiek — houd
licentie-restrictief en organisatie-identificeerbaar materiaal eruit.

---

## DEEL 5 — Voortgang: waar staat het project

### 5.1 Modelstand (baseline)
- **Baseline v4.6.4** (CSF-range-fix + DL-conformiteit). Consistent onder HermiT.
- Protocol v1.3 FINAL; sprint-protocollen 1–18 actief.
- Tooling-laag 01–03 + de GRC-domeinskill operationeel.
- Brain-vault op **iteratie 16** (controleer `brain__index.md` voor de actuele stand).

### 5.2 Afgesloten werk (selectie — zie sprint-register voor het volledige beeld)
- v0–v3: initiële fasen t/m monolithische ontologie.
- v4.0.0: modulaire split (de huidige module-architectuur).
- v4.2–v4.6: assets-module (M18), SoA-canonisering, gap-sprints, fase 2 (CBW/Cbb),
  fase 3 (NIST CSF 2.0), fase 4 (ENSIA + volwassenheid), v4.6.4 (CSF-range-fix).
- T1–T3: SKOS-kwaliteitsanalyse-sprints (T3 leverde het cross-category-precedent op m14).
- Reasoner-evaluatie + dashboard-revival voltooid; H36 en H38 opgelost.
- **Deze overdrachtssessie (dashboard-spoor):** zie 5.3.

### 5.3 Het dashboard-spoor van deze sessie (belangrijk voor je startpunt)
Aanleiding: een naderend CSO/CISO-moment; Spoor B moest visueel en functioneel
demo-klaar. Afgerond en in de repo:
1. **Reskin Overzicht-tab** + losse design-tokens-CSS. Besluit: gebruik de
   **`contrast`-ramp als standaard** (WCAG AA op getinte vlakken).
2. **DORA-correctie:** DORA is referentiekader (n.v.t.) — verwijderd als actief/kritiek
   kader; blijft alleen als "n.v.t." in referentietabellen.
3. **IA-herinrichting:** van 5 naar 4 tabs (Overzicht · Governance · Compliance · Risk);
   ISMS-inhoud verhuisd; **gelaagde kader-kiezer** (perspectief-wissel, D9-conform):
   governance-kaders (COSO/COBIT/BVA/CIO) onder Governance, operationele/normen-kaders
   (BIO standaard, ISO-reeks, NIS2, VIRBI, AVG, CBW "in voorbereiding", Cbb "concept",
   NIST, ENSIA) onder Compliance. Risico-methodologie-normen (ISO 27005/31000, NIST
   800-30/39) blijven in Risk. SoA → Governance; audit/NC → Compliance; kalender →
   Governance.

Bijbehorende instructies staan in `docs/instructies/`
(`instructie-dashboard-reskin-overzicht.md`, `design-tokens-grc-dashboard.css`,
`instructie-dashboard-ia-herinrichting.md`) en de patch-rapporten in `output/reports/`.

### 5.4 OPENSTAAND — het kernprobleem dat als eerste aandacht vraagt
Het dashboard is **nog niet presentabel.** De kader-kiezer toont nu placeholders: klik
je op een norm/kader, dan zie je niet de onderliggende controls, geen beschrijvingen van
de beheersmaatregelen en geen eisen waaraan voldaan moet worden. **De structuur staat,
de inhoud leeft niet** — die inhoud zit in de ontologie, niet in de "dunne" import die
het dashboard nu voedt.

Twee paden (nog te besluiten met de eigenaar/sponsor):
- **Pad 1 — vanuit de ontologie:** de export verrijken (control → beschrijving + eis +
  framework-koppeling) → via build-script naar het dashboard. Architecturaal zuiver,
  raakt drie lagen, kost tijd.
- **Pad 2 — demo-seed verrijken:** voor de demo-relevante kaders (BIO 2.0, ISO
  27001/27002) een representatieve control-set mét beschrijving + eis-tekst in de
  demo-seed zetten. Snel, demo-klaar. (Geadviseerd: Pad 2 nu, Pad 1 als opvolging.)

### 5.5 OPENSTAAND — organisatiestructuur in het dashboard
De eigenaar wilde de realistische IV-organisatiestructuur (een leverende, provider-
consumer IV-organisatie met functionele afdelingen: integratie-/business-services,
generieke voorzieningen, datacenter-services, bedrijfsvoering, technologie/CTO-office,
directieondersteuning, en interne beheersing als tweede/derde lijn met auditfunctie).
Drie opties, te kiezen:
- **A** — volledig generiek/demo (veiligst).
- **B** — de echte *functionele* structuur, geanonimiseerd (geadviseerd): realistische
  governance/RACI-structuur zonder organisatie-identiteit.
- **C** — volledig echt (intern-only; raakt de §0.5-/disclosure-discipline; de
  combinatie van echte structuur + security-posture is gevoelig — alleen als bewust
  vastgelegd besluit).

De interne-beheersingsfunctie sluit direct aan op het Three Lines Model (zie
`brain__architecture__H29_three-lines-model.md`) en de CIO/BVA-RACI-stelsels — waardevol
modelwerk, ongeacht wat in het dashboard belandt.

### 5.6 Overige open H-items en losse einden (naslag)
Raadpleeg `brain__architecture__H-register.md` voor de actuele status. Genoemd in de
recente projectstand: H25/H26/H27/H32/H33/H34/H35 (open); H37 (open-ontologies-MCP,
hold), H39 (290 SHACL false-positives uitsplitsen), H40 (dashboard-UI-renderdekking),
H41 (SKOS-axioma-set). Verder: protocol v1.3.1-formalisering van het cross-category-
principe (twee precedenten), documentatie-debt (README v4.6.4-baseline, sprint-
protocollen 13–18 uitwerken), en een tweede onafhankelijke bron voor de mapping-
confidence-verhoging (NIST OLIR of ISO Annex F).

---

## DEEL 6 — Valkuilen en lessen (zodat je ze niet opnieuw maakt)

1. **Vertrouw het dashboard-pad niet blind.** Een verkeerde map of poort geeft 404 of
   "address in use". Zie 2.6.
2. **Claude Design levert een plaat, geen leverbaar.** Als je ooit met Claude Design een
   ontwerp maakt: neem er de *look* en de *tokens* uit, niet de HTML. Die HTML kan
   vervuild zijn (ingebedde externe fonts) en hoort niet in de offline-repo.
3. **De DORA-val.** DORA is géén verplicht kader voor deze organisatie. Laat het nooit
   als actief/kritiek kader verschijnen; alleen als "referentie · n.v.t.".
4. **WCAG-oker.** De oker/amber-statuskleur zakt op getinte achtergronden net onder de
   AA-contrastgrens; daarom is de `contrast`-ramp standaard. Controleer contrast met een
   tool, niet op het oog.
5. **Subagent-scope-drift.** Een subagent kan "meeliftende" wijzigingen maken buiten de
   opdracht. Dat kan legitiem zijn (en wordt dan netjes gemeld), maar inspecteer altijd
   de volledige `git diff` voor je commit.
6. **Patch-rapport ≠ waarheid.** Verifieer kerncijfers aan de bron.
7. **Spoor A/B niet vermengen.** Geen ontologie-grafen in het dashboard (Spoor B); die
   horen in `grc-explorer` (Spoor A).
8. **Datumslordigheid.** Subagent-rapporten hebben weleens een verkeerde datum; let
   erop bij review.

---

## DEEL 7 — Hoe een nieuwe masterchat-sessie te starten

1. Open een masterchat in het Claude Project.
2. Geef de bootstrap-/openingsprompt (de masterchat-rolinstructie; de actuele versie
   staat in `docs/handovers/bootstrap-masterchat-v7.md`). Die laat de masterchat:
   (a) dit overdrachtsrapport lezen, (b) via GitHub-MCP `brain/brain__index.md` ophalen
   om de stand te bevestigen, (c) kort bevestigen dat de context geladen is.
3. Pas de bootstrap aan op de actuele stand vóór je 'm gebruikt — de stand verandert per
   sessie (baseline, open besluiten). Bewaar een verouderde versie als archief.
4. Werk daarna per sprint volgens de gouden werkstroom (3.2).

---

## DEEL 8 — Eerste-week-checklist voor de opvolger

- [ ] Repo lokaal gekloond; pad genoteerd.
- [ ] Claude Code geïnstalleerd; een triviaal testproject gedraaid om de tool te leren.
- [ ] `.claude/settings.json` gelezen; geverifieerd dat commit/push geblokkeerd zijn.
- [ ] De drie agent-bestanden (`tech/brein/dashboard.md`) één keer doorgelezen.
- [ ] `brain__index.md` gelezen; de actuele iteratie-stand genoteerd.
- [ ] `brain__decisions__D-register.md` doorgenomen (vooral D9 + D4).
- [ ] `brain__workflow__commit-push-werkverdeling.md` gelezen en begrepen.
- [ ] Het dashboard lokaal gedraaid (Deel 2.6); de vier tabs doorgeklikt; het lege-
      huls-probleem (5.4) met eigen ogen gezien.
- [ ] GitHub-MCP in de masterchat getest (kan `brain__index.md` ophalen).
- [ ] Eén keer de gouden werkstroom doorlopen met een kleine, veilige taak om de
      commit-discipline te oefenen.
- [ ] Met de eigenaar/sponsor de twee open besluiten besproken (5.4 content-diepte,
      5.5 organisatiestructuur).

---

## Afsluiting

Het project is zorgvuldig gestructureerd om kennis vast te houden buiten één persoon:
de brain-vault is het geheugen, de `.claude/`-laag dwingt de discipline af, en de
gescheiden chat-/agent-rollen houden strategie en uitvoering uit elkaar. Als je de
werkstroom in Deel 3 volgt en bij twijfel altijd de brain-vault raadpleegt, kun je het
project veilig overnemen en voortzetten zonder dat kennis verloren gaat.

Succes — en onthoud: bij twijfel is de `brain/`-vault de waarheid, en commit altijd zelf.

---

*Dit overdrachtsrapport is een momentopname. Voor de meest actuele stand: lees
`brain/brain__index.md` en de meest recente rapporten in `output/reports/`. De
brain-vault is te allen tijde autoritatief boven dit document.*
