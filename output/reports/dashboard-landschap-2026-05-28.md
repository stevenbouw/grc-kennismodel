# Dashboard-landschap GRC Kennismodel — 28 mei 2026

**Type:** Architectuur- en bouwsteen-analyse voor twee dashboard-producten
**Scope:** Spoor A `grc-explorer` (incrementele verbetering, in repo) + Spoor B `grc-dashboard` (green-field operationele werkmap) + koppeling A↔B (denkwerk)
**Doel:** Probleem-eerst-analyse + onderbouwde bouwsteen-aanbevelingen
**Status:** Analyse-chat-deliverable; geen sprint-mutatie, geen ontologie-impact, geen architectuurbesluit. Aanbevelingen gaan naar de masterchat. Geen autonome commit — Steven inspecteert en commit handmatig conform `brain__workflow__commit-push-werkverdeling`.

---

## 0. Werkwijze + scope + invarianten + besliscriteria

### 0.1 Onderzoeksmethode

STAP 0 ("bouw voort, herontdek niet") is uitgevoerd vóór nieuw onderzoek. Via GitHub-MCP (`stevenbouw/grc-kennismodel`, ref `8bd33d0…`, 28 mei 2026) gelezen:

- Projectinstructie v1.10 (27 mei 2026) — al in chat-context — voor missie/visie/invarianten/D1–D12+D4.1
- `CLAUDE.md` v1.6 (28-05) — repo-grounding, §"Dashboard-productlijnen"
- `brain/brain__concepts__dashboard-productlijnen.md` — Spoor A vs B onderscheid + locatie-besluit 27-05
- `.claude/agents/dashboard.md` v1.0 — Dashboard-subagent-rol + sprint-werkproces + conventies
- `brain/brain__architecture__H40_dashboard-ui-renderdekking.md` — UI-renderdekking <10%, parked
- `brain/brain__concepts__skos-export-filter.md` — 39-edge-discrepantie verklaring + filter-keten
- `brain/brain__index.md` — actuele staat ontologie + brain-vault (15 iteraties)
- `output/reports/extensie-landschap-claude-2026-05-28-3.md` — voorganger-rapport (dashboard onder-belicht)
- `dashboard/`-folder listing — alle bestanden geïnventariseerd
- `dashboard/grc-explorer-v4_6_0.html` — volledig gelezen (39,7 kB, drie tabs + Cytoscape)

### 0.2 Actuele staat (verifiërend)

Twee feiten uit de repo-verificatie die afwijken van de projectinstructie v1.10 zoals die in context staat:

- **Baseline is v4.6.3** (T3 m14 AVG/GDPR-sprint, 28 mei 2026), niet v4.6.2. Brain-index iteratie 15 bevestigt dit. Twee SKOS-predicate-substituties in `m14-avg-gdpr.ttl` (broadMatch → relatedMatch op Art5_1f-cluster). Triple-totalen ongewijzigd. **Gevolg voor explorer-gap**: niet 2 sprints achterstand maar inmiddels 3 (v4.6.1 → v4.6.2 → v4.6.3 onverwerkt), parallel met inhaalslag van eerdere release-jumps.
- **`grc-dashboard-v3-2.html` staat tóch in de repo** (`dashboard/grc-dashboard-v3-2.html`, 127 kB), ondanks het 27-mei-besluit dat Spoor B-prototype lokaal blijft (concept-bestand §"Locatie-besluit"). Ook `grc-dashboard-2.html`, `-3.html`, `-v2.html`, `-v3.html` en `grc-dashboard.html` staan in `dashboard/`. **Gevolg**: status onduidelijk — is de locatie-keuze sinds 27 mei teruggedraaid, was de "lokaal"-status nooit operationeel, of zijn dit historische artefacten van vóór de locatie-discussie? Zie vragen-bijlage Q-M2.

### 0.3 Scope-disclaimer

Publieke documentatie + brain-vault + één file-lezing van de explorer is **geen vervanger voor een installatie-/render-test**. Elk oordeel in dit rapport is "informed assessment" gebaseerd op de gelezen artefacten. Drie specifieke beperkingen:

- Ik heb de explorer niet in een browser gerenderd — gedrag onder interactie (search, expand, layout-switch) ken ik uit code, niet uit observatie.
- Ik heb `dashboard/build_grc_explorer_v3.py` niet gedraaid — de Filter A/B/C-mechaniek ken ik uit het concept-bestand `skos-export-filter`, niet uit hands-on inspectie.
- Ik heb Spoor B (`grc-dashboard-v3-2.html`) niet diepgaand geïnspecteerd — alleen het feit dat het bestand in de repo staat is verificeerbaar; inhoudelijke claims over Spoor B steunen op de CLAUDE.md-omschrijving en het productlijnen-concept, niet op file-inspectie.

Waar oordelen op aannames steunen, is dat expliciet gelabeld.

### 0.4 Invarianten (hard, niet-onderhandelbaar)

Per projectinstructie v1.10 + CLAUDE.md §Werk-conventies + §Architectuur-invarianten:

- **Lokaal-draaibaar** — productie zónder cloud-internet-afhankelijkheid (hard voor toekomstige productielaag; soepel voor Spoor A in huidige fase)
- **Geen black-box / mens-in-controle** — onder de §0.5-koers van het voorganger-rapport hercodeerd naar "mens-in-controle als toezicht/uitlegbaarheid/override, niet per-stap" (masterchat-besluit pending). Dit rapport hanteert de behoudens-formulering, niet de pre-correctie-formulering
- **Framework-neutraal (D9)** — geen visualisatie-keuze die één framework architecturaal privilegeert (BIO als view-keuze in dashboard is toegestaan; framework-als-hub is dat niet)
- **Geen organisatie-data extern** — Spoor B-data blijft lokaal
- **NEN-discipline** — geen verbatim ISO-tekst >10 woorden in dashboard-output; parafrase + clausule-verwijzing
- **Geen autonome commit** (begin-fase-transitionele invariant uit CLAUDE.md; sunset-pad bekend); subagents nooit zelfstandig; masterchat sinds 28-05 wel, Analyse-chat (deze deliverable) commit niet

### 0.5 Beslis-rubriek (consistent toegepast)

Per bouwsteen scoor ik op vijf criteria, 1 (laag) – 5 (hoog):

1. **Toegevoegde waarde** tegen welk concreet, in §2.1/§3.1 geïdentificeerd knelpunt
2. **Effort + onderhoud + leercurve** voor Dashboard-chat en Steven
3. **Invariant-toetsing** tegen de vijf invarianten uit §0.4
4. **Overlap/conflict** met huidige workflow, bestaande T01–T03-tooling, sprint-protocollen, brain-vault, dashboard-subagent-config
5. **Reversibiliteit** — makkelijk terug te draaien? Vendor-lock-in?

GO/HOLD/NO-GO volgt, gesplitst Spoor A / Spoor B / koppeling waar relevant. Emoji: 🟢 GO · 🟡 HOLD · 🔴 NO-GO. Voor elke aanbeveling expliciet "waarom geen GO" én "waarom geen NO-GO" (dialectiek) — geen forced recommendation als de eerlijke uitkomst "eerst architectuur-besluit" is.

---

## 1. Vragen-bijlage

De onderzoeks-prompt MAG en MOET vragen terugleggen wanneer publieke bronnen onvoldoende zijn. Hieronder de vragen die ik in deze ronde zou stellen, gegroepeerd per ontvanger, met expliciet gevolg voor aanbevelingen wanneer onbeantwoord. Geen van de vragen heeft Steven nu beantwoord — alle aanbevelingen hieronder zijn gemarkeerd met conditional-gevolg.

### 1.1 Aan Dashboard-chat (via Steven als tussenmens)

| ID | Vraag | Gevolg indien onbeantwoord |
|---|---|---|
| **Q-D1** | Wat zijn de drie grootste frictiepunten bij de explorer-build per nieuwe ontologie-baseline (build-script-aanpassing, namespace-uitbreiding, label-strings, regex-detectie, JSON-grootte-impact)? | Knelpunt-prioritering in §2.1 is hypothetisch i.p.v. ervaring-gevoed; aanbevelingen in §2.2 zijn deels theoretisch in plaats van pijn-gestuurd |
| **Q-D2** | Welke Cytoscape-conventies hanteer je impliciet die formalisering verdienen (kleur-toewijzing per laag/framework, edge-styling per predicate-type, layout-keuze per scenario)? | Aanbeveling §2.2-B (render-conventies-document) gaat over een vermoede lacune; mogelijk al impliciet gedekt |
| **Q-D3** | Hoe bewaak je nu dat een nieuwe baseline geen onbedoelde render-regressie oplevert — handmatige visuele inspectie, alleen Tab 3-spot-check, helemaal niet? | Aanbeveling §2.2-D (visuele regressie) is high-leverage als er geen check is; redundant als handmatige inspectie betrouwbaar werkt voor de huidige schaal |
| **Q-D4** | Werkt de huidige hardcoded framework-detectie via regex op IRI-substrings (`/nis2/i.test(id)` etc.) betrouwbaar door alle releases heen, of zijn er IRI-veranderingen geweest die de regex-set hebben gebroken? | Bouwsteen-aanbeveling §2.2-C (data-driven framework-config) is een directe oplossing voor regex-broosheid, maar de prioriteit hangt af van of dit al pijn doet |
| **Q-D5** | Wat zit er in `grc-dashboard-v3-2.html` (127 kB in de repo) qua daadwerkelijke functionaliteit — alleen de CLAUDE.md-spec (CRUD/audit-trail/RACI/kalender) of meer/minder? Welke onderdelen zijn werkend, welke stub, welke geparkeerd? | §3-aanbevelingen over Spoor B zijn op CLAUDE.md-richtinggeving gebaseerd; werkelijke v3-2-inhoud kan de aanbevelingen substantieel doen verschuiven (mogelijk meer dan ik nu uit publieke artefacten kan zien) |
| **Q-D6** | Kan de Dashboard-subagent in Claude Code zelfstandig de explorer renderen en bekijken (bv. via Playwright/Puppeteer headless of een eenvoudige `python -m http.server` + manual check), of moet alles via Steven's browser? | Aanbeveling §2.2-D (visuele regressie) en §2.2-G (lokale ontwikkel-loop) verschillen sterk afhankelijk van of de subagent al een lokale render-omgeving heeft |
| **Q-D7** | Welke van de aangrenzende `grc-dashboard-*.html`-bestanden (`-2`, `-3`, `-v2`, `-v3`, base, `-v3-2`) zijn nog actief werkbestanden vs. historische artefacten? | §3.0-statusbeoordeling voor Spoor B is nu onzeker — de versie-historie is onduidelijk vanuit de bestandsnamen alleen |

### 1.2 Aan masterchat (via Steven als tussenmens)

| ID | Vraag | Gevolg indien onbeantwoord |
|---|---|---|
| **Q-M1** | Welke elementen van de CLAUDE.md-richtinggeving voor Spoor B (SQL.js, Chart.js, CRUD, audit-trail, RACI, kalender) zijn **hard** (architectuurbesluit) en welke **zacht** (richtinggevend, herziening welkom)? | §3.1 kritische beoordeling moet anders verdedigd worden: bij "alles zacht" mag ik scherp tegenspreken; bij "tech-stack hard" beperkt mijn ruimte tot het ontwerpen rond die stack |
| **Q-M2** | Is het 27-mei-besluit dat `grc-dashboard-v3-2.html` lokaal blijft (concept-bestand `dashboard-productlijnen`) sindsdien teruggedraaid, of staat het bestand in de repo zonder geldend besluit? | Aanbeveling §3.4 over Spoor B-locatie heeft direct effect: bij actief besluit "lokaal" moet ik de huidige repo-aanwezigheid markeren als afwijking; bij teruggedraaid besluit is de locatie-vraag formeel heropend |
| **Q-M3** | Is de graph-verkenning-architectuur van Spoor A (Cytoscape.js + JSON-export uit ontologie) **bewust** niet bedoeld voor Spoor B, of is het een open vraag of Spoor B ook een Cytoscape-laag krijgt? | §4.2 ontwerp-implicaties verschillen substantieel — bij bewust-geen-graaf-in-Spoor-B blijft de koppeling smaller (alleen IRI-referenties); bij open-vraag is een gedeelde Cytoscape-laag een geen-spijt-keuze |
| **Q-M4** | Is het H40-trigger-criterium "externe demo-vraag met audit-aspect" actief of latent? Anders gezegd: is een UI-moderniserings-sprint deze maanden/dit kwartaal te verwachten, of zit het verder weg? | §2.4 prioritering: bij latent → renderdekking-werk is HOLD; bij actief (demo voor CSO/auditor gepland) → renderdekking opschuiven naar Onmiddellijk |
| **Q-M5** | Welk gewicht heeft de "lokaal-draaibaar"-invariant voor Spoor B in **de prototype-fase**? Strict (zelfs prototype mag geen cloud-CDN voor Cytoscape) of soepel (prototype mag cloud-CDN, productie niet)? | §3 tech-stack-overwegingen verschillen — strict betekent vendor-pakket lokaal hosten of alternatieven kiezen; soepel betekent CDN nu, vendoren later |
| **Q-M6** | Hoeveel inspanning is verantwoord voor de Spoor-A-explorer **vóór** de Spoor-B-lab-test bij T&I? Anders: is Spoor A "behouden zoals het is, kleine bijhouding" of "actief moderniseren omdat het de eerste demonstratie-laag is"? | §7 vervolgstappen-fasering hangt hieraan: bij "behouden" geen UI-modernisering nu; bij "actief moderniseren" parallel met T-sprints |

### 1.3 Onbeantwoorde vragen — gemarkeerd in aanbevelingen

Alle zeven Q-D's en zes Q-M's zijn onbeantwoord op het moment van schrijven. De aanbevelingen hieronder gaan **niet** uit van een bepaalde uitkomst — waar de aanbeveling sterk afhangt van een specifiek antwoord, label ik dat expliciet als "afhankelijk van Q-Xn". Dat betekent ook: dit rapport is geen eindoordeel maar een **gestructureerd startpunt** voor een Dashboard-chat-/masterchat-ronde waarna een definitievere afweging mogelijk is.

---

## 2. Spoor A — `grc-explorer`

### 2.1 Knelpunten-inventarisatie (probleem-eerst)

Vóór bouwstenen voorgesteld worden, eerst de knelpunten — vermoed, gevalideerd waar mogelijk uit code/brain-vault, of expliciet hypothetisch gelabeld waar Dashboard-chat-bevestiging ontbreekt.

#### K1 — Hardcoded versie-strings en framework-detectie

**Bewijs:** in `grc-explorer-v4_6_0.html` (gelezen 28-05-2026) staat:

- Title: `GRC Kennismodel Explorer v4.6.0 — Rijksoverheidsorganisatie`
- Subtitle: `Rijksoverheidsorganisatie — Informatiebeveiliging v4.6.0`
- Header meta: `GRC Kennismodel v4.6.0`
- Fout-melding: `Zorg dat grc-data-v4_6_0.js naast dit bestand staat`
- Build-script-verwijzing: `python3 build_grc_explorer_v3.py`
- Script-tag: `<script src="grc-data-v4_6_0.js">`

Bij elke release (v4.6.0 → v4.6.1 → v4.6.2 → v4.6.3) moeten deze zes strings op zes plekken handmatig aangepast — anders breekt de loader of toont de UI verouderde info. Dat is brittle. Verder is **framework-detectie regex-gebaseerd op IRI-substrings** (regel 188–206):

```javascript
{ key:'NIS2', label:'NIS2', fn: id => /nis2/i.test(id) },
{ key:'VIR',  label:'VIR 2007', fn: id => /vir_/i.test(id) && !/virbi/i.test(id) },
// ... (9 frameworks scorecard + 5 matrix-kolommen, alle regex)
```

Een nieuwe namespace of een IRI-rename in de ontologie kan deze regex-set stil breken — er is geen tegen-controle dat een framework dat in de ontologie staat ook in de scorecard verschijnt. **Status: hoog-waarschijnlijk pijn**, maar Dashboard-chat-bevestiging (Q-D4) ontbreekt of dit al gebeurd is.

#### K2 — Build-script-versie ontkoppeld van ontologie-versie

**Bewijs:** in dashboard-subagent-config §"Build-script versionering":

> Build-script-versie (v3, v4, ...) loopt onafhankelijk van ontologie-versie (v4.X.Y); ontologie-versie staat in data-bestanden + HTML.

In `dashboard/`-folder: `build_grc_explorer_v2.py` (22,7 kB) én `v3.py` (23,7 kB) — twee versies in repo, mogelijk niet beide actueel. De relatie tussen build-script-versie en ontologie-versie is impliciet ("v3 hoort bij v4.6.0"); een nieuwe sprint (T1/T2/T3 in mei 2026) heeft geen nieuwe build-script-versie nodig (predicate-substitutie, geen nieuwe namespace), maar dat is alleen achteraf vast te stellen.

**Status: matige pijn**, manifest als achterstand: per brain-index "Dashboard-inhaalslag 7 sprints (parallel, niet-blokkerend; nu incl. v4.6.3)". Zeven sprints achterstand betekent niet dat het script ze niet aankan; het betekent dat ze nog niet gedraaid zijn.

#### K3 — Build-pipeline-stappen niet automatisch sluitend per release

**Vermoed knelpunt (Dashboard-chat-bevestiging via Q-D1):** een Dashboard-cyclus bestaat per subagent-config uit 7 stappen (lees patch-rapport → impact-analyse → script-update → run build → HTML-update → smoke-test → patchnotitie-rapport). Geen van die stappen heeft een hard gate die de volgende stap dwingt; smoke-test is een browser-actie van Steven; er is geen file-back-controle dat `grc-data-vX_Y_Z.json` byte-consistent is met `vX_Y_Z.js` (de JS is een wrapper om dezelfde JSON).

**Status: hypothetisch — Q-D1.** Mogelijk al gemitigeerd door de subagent-protocollen.

#### K4 — UI-renderdekking <10% van JSON-velden (H40)

**Bewijs:** brain-vault `H40_dashboard-ui-renderdekking.md` documenteert dat de JSON-export rdfs:comment, sourceAttribution, BBN-niveau, Tier, CapabilityLevel, alle types, cross-framework-context bevat — en de UI toont voornamelijk `label`, `laag`, `type`, edges. Het percentage "<10%" is conservatief, niet gemeten. De drie gevolgen uit H40:

- Demonstratie-waarde beperkt (externe stakeholders zien graaf, niet de rijkdom)
- Audit-spoor onzichtbaar (SourceAttribution = het verschil tussen "willekeurige RDF" en "verifieerbare GRC-kennisbasis", maar wordt niet getoond)
- Cross-framework-uitleg ontbreekt (D9-framework-neutraliteit + D11-asset-convergentie zijn architecturaal kern, maar zichtbaar alleen via edge-tracing)

**Status: bewust geparkeerd**, niet "pijn" in operationele zin. Wel hard-pijn bij specifieke trigger (Q-M4: externe demo voor auditor).

#### K5 — 39-edge SKOS-discrepantie als symptoom van een dieper meet-onderscheid

**Bewijs:** brain-concept `skos-export-filter.md` ontleedt het exact: drie filter-stappen in `build_grc_explorer_v3.py` (regel 77-86 SCHEMA_TYPES, 411-422 individuals-set, 482 edge-endpoint-validatie) sluiten 39 SKOS-tripels uit waarvan minstens één endpoint `owl:Class` is. **Dit is geen bug** — het is een bewuste architecturale keuze (de explorer toont alleen ABox-individuen) — maar het is wel een **meet-laag-discrepantie** die opduikt zodra je 1.798 (ontologie) vs 1.759 (export) ziet en niet weet dat het twee verschillende metingen zijn.

**Status: niet-blokkerend**, expliciet als zodanig in brain-concept gedocumenteerd. Aanleiding voor patch-rapport-discipline ("voortaan expliciet de laag noemen bij SKOS-tellingen"). Geen render-aanpassing nodig zolang je het weet.

#### K6 — Geen Dashboard-skills in Tooling-laag (T01–T03 was Tech-gericht)

**Bewijs:** uit het voorganger-rapport §A.2 en uit CLAUDE.md §"Action-skills": het project heeft inmiddels skills `canonical-metrics`, `shacl-split`, `patch-rapport`, `ontology-conformance`, `report-structure`, `repo-reference` — allemaal Tech-/Brein-gericht. **Geen enkele skill is dashboard-specifiek.** De dashboard-subagent leunt volledig op zijn `.claude/agents/dashboard.md`-prozaregel + cyclische sprint-werkproces; er is geen herhaalbaar `/<naam>`-mechanisme voor dashboard-werkstromen.

**Status: lacune**, niet pijn in operationele zin, wel een gemiste hefboom voor consistentie.

#### K7 — Render-conventies impliciet in code

**Bewijs:** in `grc-explorer-v4_6_0.html` regel 178-186:

```javascript
const LAAG = {
  0: { name:'COSO/Enterprise',    color:'#7c3aed' },
  1: { name:'IT-governance',      color:'#2563eb' },
  // ...
};
```

Kleur-toewijzing per laag leeft alleen in deze constant; er is geen `brain__concepts__render-conventies.md` of vergelijkbaar. Hetzelfde voor edge-style, layout-keuze (`cose` boven 15 nodes, `concentric` daaronder), MAX_N=60 voor explorer-canvas. **Status: hypothetisch lacune** — Q-D2 (zijn er impliciete conventies die formalisering verdienen?) is een vraag aan Dashboard-chat. Kan zijn dat de conventies in dashboard.md beschreven staan en ik ze gemist heb; bij scan vond ik wel Cytoscape-conventies-paragraaf maar zonder kleur-/edge-toewijzing per framework.

#### K8 — JSON-grootte-progressie als latent prestatie-risico

**Bewijs:** uit `dashboard/`-folder listing:

- `grc-data-v4.3.0.json` = 1.345 kB
- `grc-data-v4.3.1.json` = 1.364 kB
- `grc-data-v4_6_0.json` = 2.604 kB

De JSON is bijna verdubbeld over drie sprints. Voor 1.383 individuals + 1.759 edges is dat nog browser-handelbaar, maar de groei is monotoon. Een UI-modernisering (H40 dekking-uitbreiding) voegt per-node-payload toe — rdfs:comment-bilinguaal + sourceAttribution-IRI per node tikt makkelijk x2 verder.

**Status: latent**, niet pijn nu. Wel ontwerp-relevant bij H40-activering: voeg detail toe via on-demand-fetch (per node), niet door alles in de initiële payload te stoppen.

#### K9 — Hardcoded "Rijksoverheidsorganisatie" als label

**Bewijs:** subtitle in HTML: `Rijksoverheidsorganisatie — Informatiebeveiliging v4.6.0`. Dit voldoet aan de organisatienaam-invariant (nooit de echte naam). Maar bij **organisatie-overdracht** (architectuur-invariant: overdraagbaar naar vergelijkbare organisaties) is dit punt waar geparametriseerd moet worden — niet erg, maar te onthouden bij Spoor-B-/plugin-evaluatie.

**Status: latent**, mogelijke vondst bij Spoor-B-tijd of plugin-bundeling.

### 2.2 Bouwsteen-aanbevelingen per knelpunt (oplossings-laag)

Per knelpunt: welke bouwsteen (skill, slash-command, hook, conventie, render-discipline-document, externe library) past en hoe.

#### Bouwsteen A — Versie-suffix-templating in HTML + build-script

**Doel:** K1 (hardcoded versie-strings) wegnemen.
**Wat:** in plaats van zes strings handmatig aanpassen per release, één variabele `__VERSION__` in HTML die door build-script wordt vervangen tijdens build. Drie concrete varianten:

1. **Server-side substitutie in `build_grc_explorer_v3.py`** — het script kopieert een `grc-explorer-template.html` met `__VERSION__`-placeholders naar `grc-explorer-vX_Y_Z.html` met versie ingevuld. Laagdrempelig, Python-only, geen JS-framework.
2. **Runtime-substitutie via `<meta name="grc-version" content="v4.6.0">`** in HTML + JS dat alle plekken vervangt. Vereist minder build-discipline, meer client-werk.
3. **Inject vanuit `grc-data-vX_Y_Z.js`** — DATA.meta.version is al beschikbaar (zie HTML regel `DATA.meta.generated`); voeg `version` toe en lees uit in `initTab1()`. Variant 3 is dichtst bij wat al gebeurt en vraagt minimale build-script-aanpassing.

**Rubriek:** Waarde 4 (K1 directe oplossing; voorkomt verouderde versie-labels) · Effort 4 (laag — Python + JS-aanpassing, geen framework) · Invarianten 5 (lokaal, geen externe afhankelijkheid) · Overlap 5 (geen) · Reversibiliteit 5 (terugzetten = template restoren).

**🟢 GO (Spoor A), variant 3 (uit DATA.meta).** Pijnloos, direct nut, dekt elke nieuwe sprint. Onderdeel van eerstvolgende build-script-aanraking (geen aparte sprint nodig).

- *Waarom geen NO-GO:* zes plekken handmatig is gewoon brittle; één variabele verlaagt fout-oppervlak structureel.
- *Voorbehoud:* alleen waarde als de build-pipeline-update echt automatisch elke release draait. Bij "we komen er pas aan toe als er een nieuwe release gevraagd wordt" is het marginaal — dan is per-release "find/replace v4.6.0" net zo snel.

#### Bouwsteen B — Render-conventies-document (`brain__concepts__render-conventies.md`)

**Doel:** K7 (impliciete conventies) expliciteren.
**Wat:** een brain-vault-concept-bestand dat formaliseert: kleur-toewijzing per laag (de 7 LAAG-kleuren), edge-styling per predicate-categorie, layout-strategie (wanneer cose vs concentric vs preset), MAX_N=60-rationale, ellipsis-cutoffs, framework-detectie-strategie. Dit document is *referentie* voor Dashboard-chat én *audit-trail* voor toekomstige UI-moderniseringen.

Verwante: zou symmetrisch zijn met `brain__concepts__canonical-metrics`, `skos-beoordelings-protocol`, etc. — Karpathy-wiki-pattern: "compile once, keep current".

**Rubriek:** Waarde 4 (afhankelijk van Q-D2; bij "ja, impliciet"-antwoord = waarde 5; bij "nee, allemaal expliciet in subagent-config" = waarde 2) · Effort 4 (één document, Brein-subagent-cycle of dashboard-subagent-zelf) · Invarianten 5 · Overlap 4 (geringe overlap met dashboard.md-subagent-config; verschil: subagent-config = werkwijze, concept-bestand = besluiten + rationale) · Reversibiliteit 5.

**🟢 GO (Spoor A), afhankelijk van Q-D2.** Wel uitvoerbaar zonder Q-D2-antwoord, maar de inhoud wordt eerder hypothese-gevoed dan praktijk-gevoed.

- *Waarom geen onvoorwaardelijke GO nu:* als de conventies al voldoende in dashboard.md staan (Q-D2 antwoord "ja, het is allemaal expliciet"), dan is een nieuw concept-bestand redundant. Subagent-config en concept-bestand zijn niet hetzelfde, maar overlap is reëel.
- *Waarom geen NO-GO:* zelfs in het "al expliciet"-geval is een concept-bestand het juiste medium voor *rationale* (waarom deze kleur voor laag 2 en niet die), wat de subagent-config terecht niet draagt.

#### Bouwsteen C — Data-driven framework-config (uit ontologie i.p.v. regex)

**Doel:** K1 (regex-broosheid van framework-detectie) en deels K7 (conventies expliciet maken).
**Wat:** de 9 frameworks in `FWS` + 5 in `MCOLS` zijn nu hardcoded met regex op IRI-substrings. Alternatief: een aparte JSON `grc-framework-config-vX_Y_Z.json` die per framework declareert:

```json
{
  "frameworks": [
    {
      "key": "NIS2",
      "label": "NIS2",
      "sub": "Laag 2 — EU-richtlijn",
      "iri_match": "https://grc.example.org/framework/NIS2",
      "color": "#dc2626",
      "show_in_scorecard": true,
      "show_in_matrix": true
    },
    ...
  ]
}
```

Build-script genereert deze JSON uit `m01-framework.ttl` + de fw:GRCFramework-individuals. Explorer leest de config; geen regex meer. Bij nieuwe framework-individual (bv. ENSIA promotie in v4.6.0) verschijnt het automatisch.

**Rubriek:** Waarde 5 (K1 hoofdoorzaak weggenomen; future-proof) · Effort 3 (build-script-uitbreiding + HTML-refactor) · Invarianten 5 · Overlap 4 (overlap met huidige `LAAG`/`FWS`/`MCOLS`-constants — die kunnen weg) · Reversibiliteit 4 (refactor terugzetten = hardcoded constants restoren).

**🟢 GO (Spoor A), middellange termijn.** Sterke architecturale verbetering, maar geen quick-fix; vraagt ontwerp + bouw + smoke-test. Logische bundeling: Bouwsteen A + B + C in één UI-modernisering-mini-sprint vóór of als onderdeel van H40-activering.

- *Waarom geen NO-GO:* de regex-broosheid is een latente bug die ooit toeslaat; data-driven is hygiëne, niet luxe.
- *Voorbehoud:* niet in isolatie — koppelen aan een grotere refactor-/H40-stap zodat het build-script niet drie keer aangeraakt wordt.

#### Bouwsteen D — Visuele regressie-detectie (screenshot-diff)

**Doel:** K3 (geen automatische regressie-controle), K8 (latent prestatie/render-risico bij data-groei).
**Wat:** een lichte screenshot-diff-pijplijn. Twee niveaus:

- **Niveau 1 — Playwright headless + diff.** Open de explorer in headless browser, render alle drie tabs, screenshot per tab, vergelijk met baseline-PNG. Een sprint die de scorecard kapot maakt of een Cytoscape-init-fout introduceert, faalt visueel direct zichtbaar. Open-source (Playwright/Puppeteer), draait lokaal, geen cloud.
- **Niveau 2 — DOM-snapshot in plaats van pixel-diff.** Sneller, minder false-positives bij sub-pixel-rendering-verschillen, maar minder gevoelig voor visuele regressies. Voor dit project (waar render-discipline belangrijker is dan pixel-perfect-symmetrie) is een DOM-snapshot waarschijnlijk de juiste keuze.

Belangrijk: Q-D6 (kan de subagent zelf in een browser renderen?) bepaalt of dit volwassen-toepasbaar is. Als Steven de enige is die de browser opent, is regressie-detectie een handmatige-pijplijn (Dashboard-subagent levert screenshots; Steven vergelijkt) wat realiseerbaar maar onbevredigend is.

**Rubriek:** Waarde 4 (K3 directe oplossing; ook K8-monitoring) · Effort 2 (Playwright opzetten + baseline-set + diff-tool) · Invarianten 5 (lokaal-draaibaar) · Overlap 5 (geen — nieuw vermogen) · Reversibiliteit 4 (configuratie verwijderen).

**🟡 HOLD → 🟢 GO afhankelijk van Q-D6 + Q-D3.** Bij Q-D6 = "subagent kan headless renderen": GO. Bij Q-D6 = "alles via Steven's browser": effort verschuift; nog steeds GO maar gefaseerder. Bij Q-D3 = "handmatige inspectie werkt prima": HOLD totdat de schaal het breekt.

- *Waarom geen onvoorwaardelijke GO:* effort/onderhoud is reëel (false-positives bij font-renderings-verschillen tussen versies); zonder probleem-druk is investering niet gerechtvaardigd.
- *Waarom geen NO-GO:* "regressie-vrij" is geen luxe voor een UI die met elke ontologie-release meegaat; de huidige stilzwijgende vertrouwens-loop tussen ontologie-verandering en visuele-stabiliteit zal ooit breken.

#### Bouwsteen E — Pre-sprint-explorer-update-protocol

**Doel:** K2 + K3 (sprint-overgang-discipline voor dashboard-zijde).
**Wat:** analogie aan Protocol 1 (pre-sprint-inventarisatie voor Tech-subagent), maar dan voor de Dashboard-subagent. Een checklist die élke release vóór build-script-aanraking doorlopen wordt:

- Welke modules zijn gewijzigd in deze sprint (uit patch-rapport §"Gewijzigde modules")
- Zijn er nieuwe namespaces (raakt namespace-binding in build_v3 + Cytoscape-class-mapping)
- Zijn er nieuwe properties met SKOS-impact (raakt edge-export)
- Is er een nieuwe Laag (raakt LAAG-config in HTML)
- Is er een nieuw framework-individual (raakt FWS-config)
- Build-script-versie-bump nodig of niet?

Output: ja/nee per regel + impact-tabel die naar patchnotitie-export-rapport gaat (zoals dashboard-subagent-config §"Patchnotitie-export-conventies" al beschrijft, maar dit zou een gestructureerde pre-stap zijn).

**Rubriek:** Waarde 4 · Effort 4 · Invarianten 5 · Overlap 4 (sluit aan op bestaande dashboard-subagent-cyclus, voegt structuur toe) · Reversibiliteit 5 (protocol kan weg).

**🟢 GO (Spoor A).** Past in de "17 protocollen + dashboard-extensie"-lijn. Zet als Protocol 18 of dashboard-specifiek annex bij Protocol 1.

- *Waarom geen NO-GO:* sprint-overgang is precies waar dingen mis gaan; een pre-checklist dwingt impact-bewustzijn af.
- *Voorbehoud:* moet niet bureaucratisch worden — vier vragen volstaan, twintig is overkill.

#### Bouwsteen F — Skill `/dashboard-build` (action-skill voor Dashboard-subagent)

**Doel:** K6 (geen Dashboard-skills).
**Wat:** een action-skill (analoog aan `/canonical-metrics` en `/shacl-split` voor Tech) die de Dashboard-build-cyclus codificeert: lees `output/reports/patch-rapport-vX_Y_Z.md`, draai `build_grc_explorer_vN.py`, valideer dat `grc-data-vX_Y_Z.json` en `.js` zijn weggeschreven, log triple-counts uit nieuwe JSON, vergelijk met `canonical_metrics_vX_Y_Z.json` voor consistentie. Eén `/dashboard-build vX_Y_Z` draait de hele keten.

**Rubriek:** Waarde 4 · Effort 3 (skill-structuur + Python-wrapper) · Invarianten 5 · Overlap 4 (overlap met dashboard-subagent-sprint-werkproces 7-stappen; skill is het uitvoerbare deel daarvan) · Reversibiliteit 5.

**🟢 GO (Spoor A), na Bouwsteen E.** De skill heeft pas waarde als de protocol-checklist (Bouwsteen E) operationeel is — zonder dat is `/dashboard-build` mogelijk een blackbox die de impact-analyse overslaat.

#### Bouwsteen G — Lokale ontwikkel-loop voor Dashboard-subagent

**Doel:** K3 + K4 (regressie-bewustzijn, render-validatie).
**Wat:** afhankelijk van Q-D6. Twee scenarios:

- **Q-D6 = "subagent kan headless renderen"**: bevestig dat `npm install playwright` + scriptje (`render-explorer.js`) werkt; documenteer in dashboard.md. De subagent draait dan na build automatisch `playwright test render-smoke` en levert pass/fail + screenshot-array bij patchnotitie.
- **Q-D6 = "alles via Steven's browser"**: lichter — een `python -m http.server` in dashboard/, met instructie aan Steven om link te openen. De subagent kan dat starten (Bash-tool aanwezig). Geen automatische render-validatie, wel snelle preview-loop.

**Rubriek:** Waarde 4 · Effort variërend (headless: 3 / browser-link: 5 = laag) · Invarianten 5 · Overlap 5 · Reversibiliteit 5.

**🟡 HOLD → 🟢 GO afhankelijk van Q-D6.** Niet bouwen zonder Dashboard-chat-input over wat werkbaar is in de huidige opzet.

#### Bouwsteen H — Cytoscape-alternatief evalueren (Sigma.js, vis-network)

**Doel:** K8 (latent prestatie-risico bij data-groei), geen acute pijn maar architectuur-toekomstig.
**Wat:** Cytoscape.js is voor 1.383 individuals + ±2.000 zichtbare edges ruim genoeg, maar groeit de explorer naar 5.000+ nodes (bij Spoor B-koppeling of bij m11 SP800-53-uitbreiding H33), dan kan Sigma.js (WebGL-based, schaalt naar 100k+ nodes) of vis-network (lichter, native physics) relevant worden. Geen aanbeveling nú om te wisselen — wel: parkeer als kandidaat bij groei-trigger.

**Rubriek:** Waarde 2 (geen huidige pijn) · Effort 1 (migratie zou hoog zijn) · Invarianten 5 · Overlap 2 (botst met huidige stack) · Reversibiliteit 3.

**🔴 NO-GO nu / 🟡 HOLD-als-kandidaat-bij-groei (Spoor A).**

- *Waarom NO-GO nu:* Cytoscape werkt, er is geen schaal-pijn aangetoond, een Simplicity-First-discipline pleit voor "behouden wat werkt".
- *Waarom geen permanente NO-GO:* bij H33-uitvoering (SP800-53 substantiële uitbreiding) of bij Spoor B-koppeling met operationele datasets is herevaluatie passend.

#### Bouwsteen I — On-demand detail-fetch i.p.v. alles-in-initiële-payload

**Doel:** K8 (latent prestatie) + K4 (H40-uitbreiding zonder JSON-explosie).
**Wat:** bij H40-activering (UI-renderdekking uitbreiden naar rdfs:comment, sourceAttribution, etc.): niet alle velden in `grc-data-vX_Y_Z.json` initieel laden, maar per-node lazy load via `grc-node-details/<nodeId>.json` of via een single JSON met index. Houdt initial-load licht, levert detail bij interactie. Past bij Cytoscape-flow waar je sowieso per-node-detail-paneel hebt.

**Rubriek:** Waarde 3 (geen huidige pijn) · Effort 2 (forse refactor) · Invarianten 5 · Overlap 3 (build-script-impact: meerdere JSON's i.p.v. één) · Reversibiliteit 3.

**🟡 HOLD — koppelen aan H40-activering (Spoor A).** Niet stand-alone bouwen. Wel als ontwerp-overweging vastleggen voor wanneer H40 aanpakt wordt.

#### Bouwsteen J — frontend-design skill voor Dashboard-subagent

**Doel:** K4 (H40 UI-uitbreiding) + algemene UI-kwaliteit.
**Wat:** Anthropic-native skill `frontend-design` (geconstateerd in voorganger-rapport §C.5) is een GO voor Dashboard. Bij UI-modernisering (H40) geeft deze skill de juiste tokens, styling-discipline, accessibility-overwegingen.

**Rubriek:** Waarde 4 · Effort 5 (built-in) · Invarianten 5 (skill draagt geen content, alleen guidance) · Overlap 5 (geen) · Reversibiliteit 5.

**🟢 GO (Spoor A), bij H40-activering.** Activeren zodra renderdekking-werk start; eerder is geen aanleiding.

### 2.3 Specifieke aandachts-punten (uit de prompt)

#### 2.3.1 v4.6.0 → v4.6.3-gap

**Status:** drie sprints achterstand (T1 v4.6.1 → T2 v4.6.2 → T3 v4.6.3). De ontologie-baseline is verschoven, de explorer staat op v4.6.0 (zowel filename als interne metadata). Mathematisch: triple-totalen ongewijzigd (alle T-sprints zijn predicate-substitutie), zes metrics in canonical_metrics identiek. **Praktisch:** SKOS-distributie is wel verschoven (exact 18, close 1.457, broad 129, narrow 0, related 194 — per brain-index v4.6.3). De crosswalk-matrix Tab 2 toont mappings; de **predicate-substituties beïnvloeden welke rij in de matrix welke kleur/dot-zwaarte krijgt** *als* het dashboard onderscheid maakt tussen exact/close/broad/narrow/related — wat het nu **niet** doet (alle SKOS-mappings worden als generieke "●"-dot getoond). Dat is een impliciete render-keuze (K7) die door de T1-T3 SKOS-werkdiscipline mogelijk heroverwogen moet worden.

**Onhandig is**: een full rebuild voor T1/T2/T3 (`build_grc_explorer_v3.py` opnieuw draaien) genereert nieuwe `grc-data-v4_6_3.js/json`, maar de **HTML-shell** moet hand-aangeraakt voor de zes versie-strings. Bouwsteen A (versie-templating) lost dit structureel op.

**Beter zou kunnen**: één run-script `dashboard/rebuild-all-baselines.sh` of `rebuild_dashboard.py` dat voor elke gegeven versie de hele keten uitvoert (data-build + HTML-shell-templating + smoke-test). De Dashboard-inhaalslag (7 sprints) is dan één commando per missing baseline — nu vraagt het zeven keer handmatige cycli.

#### 2.3.2 39-edge SKOS-discrepantie

**Status:** **niet-blokkerend** en **geen bug**. Brain-concept `skos-export-filter.md` is autoritatief: het is een meet-laag-discrepantie tussen ontologie (1.798) en dashboard-export (1.759). De drie filter-stappen (Filter A SCHEMA_TYPES, Filter B individuals-set, Filter C edge-endpoint-validatie) zijn een bewuste architecturale keuze, niet defect.

**Hoe de oplossings-laag dit adresseert**: Bouwsteen B (render-conventies-document) bevat een sub-sectie "meet-laag-onderscheid" die formeel vastlegt dat de explorer op de dashboard-laag opereert, niet de ontologie-laag. Bouwsteen E (pre-sprint-explorer-update-protocol) bevat een check "patch-rapport noemt 1.798 SKOS — dashboard exporteert 1.759 — verschil is verwacht" die voorkomt dat dit elke release opnieuw als "discrepantie" opduikt. Geen build-script-wijziging.

**Indien Spoor B er ooit anders mee om wil gaan** (Spoor B toont wel klasse-niveau-relaties): dat is een ander product, geen reden om Spoor A te wijzigen — zie ook §4.

#### 2.3.3 Lokale ontwikkel-loop

Direct gekoppeld aan Bouwsteen G + Q-D6. Antwoord op Q-D6 bepaalt:

- Zo ja (subagent kan headless renderen) → Bouwsteen G niveau 1 (Playwright) → activeert Bouwsteen D (visuele regressie) op een natuurlijke manier.
- Zo nee → Bouwsteen G niveau 2 (HTTP-server + Steven's browser) → handmatigere regressie-loop, lager rendement op Bouwsteen D.

Mijn vermoeden (niet geverifieerd): Claude Code heeft Bash-tool en kan Playwright `npm install`-en + draaien, dus *technisch* is niveau 1 mogelijk. Of het *praktisch* werkbaar is in de subagent-context (rendering vraagt headed of headless display, en in een container kan dat haperen) is een test-vraag.

### 2.4 GO/HOLD/NO-GO-overzicht Spoor A

| ID | Bouwsteen | Status | Voorwaarde / opmerking |
|---|---|---|---|
| A | Versie-suffix-templating (uit DATA.meta) | 🟢 GO | Onderdeel van eerstvolgende build-script-aanraking; geen aparte sprint |
| B | Render-conventies-document (brain-concept) | 🟢 GO | Q-D2 valideert focus; toch uitvoerbaar bij Brein-cyclus |
| C | Data-driven framework-config (uit ontologie) | 🟢 GO middellange termijn | Bundelen met UI-mini-sprint A+B+C, ideaal vóór H40-activering |
| D | Visuele regressie (Playwright headless) | 🟡 HOLD → GO | Afhankelijk van Q-D6 + Q-D3 |
| E | Pre-sprint-explorer-update-protocol | 🟢 GO | Protocol 18 of annex bij Protocol 1; geringe overhead, hoog rendement |
| F | Skill `/dashboard-build` | 🟢 GO ná E | Geen waarde zonder Bouwsteen E; gebundeld als één werkstroom |
| G | Lokale ontwikkel-loop | 🟡 HOLD | Afhankelijk van Q-D6 |
| H | Cytoscape-alternatief (Sigma/vis-network) | 🔴 NO-GO nu / 🟡 HOLD-bij-groei | Heroverwegen bij H33 of Spoor-B-koppeling |
| I | On-demand detail-fetch | 🟡 HOLD | Koppelen aan H40-activering |
| J | frontend-design skill | 🟢 GO bij H40 | Activeren bij UI-modernisering, niet eerder |

**Rode draad Spoor A:** de meeste waarde zit niet in nieuwe tooling maar in **discipline-formalisering** (B + E + F) en **versie-templating** (A + C). H40 (renderdekking) blijft de grote latente sprint die *separate* aandacht vraagt — bouwsteen I + J horen daar; voorbereidende bouwstenen (A + C) maken H40 makkelijker. Visuele regressie (D) is hoog-waarde maar afhankelijk van of de subagent zelf kan renderen — dat is een operationele Q-D6-vraag.

---

## 3. Spoor B — `grc-dashboard`

### 3.0 Status-uitgangspunt

Per CLAUDE.md + productlijnen-concept: operationele werkmap-prototype (CRUD/audit-trail/RACI/kalender) met SQL.js + Chart.js. Lokaal-prototype `grc-dashboard-v3-2.html` blijkbaar 127 kB in de repo (afwijking van het 27-mei-besluit — zie Q-M2). **Belangrijk discipline-punt**: dit hoofdstuk is geschreven onder de premisse dat Spoor B een **green-field herstart** krijgt bij de T&I-lab-test, ongeacht de status van de bestaande v3-2. Als de v3-2 al substantieel werkt (Q-D5), kunnen sommige aanbevelingen hier overslaan; dat is een Dashboard-chat-input-vraag.

### 3.1 Architectuur-overwegingen (kritisch op CLAUDE.md-richtinggeving)

CLAUDE.md schrijft (richtinggevend, niet vastgesteld — Q-M1): operationele werkmap met CRUD, audit-trail, RACI, kalender, lokale SQL.js, Chart.js. Hieronder per element een eerlijke beoordeling.

#### O1 — Tech-stack: SQL.js + Chart.js + lokale HTML

**Sterke punten:**

- **SQL.js** is een SQLite-compilation naar WebAssembly: volledige SQL in de browser, geen server. Voor een **single-user-prototype** is dit het minst-kwetsbare pad: één `.db`-bestand op disk, SQL-export-trivialiteit, geen runtime-afhankelijkheid behalve een browser. Past bij **lokaal-draaibaar** (invariant 1).
- **Chart.js** is bewezen, accessibility-bewust, lichte footprint. Voor de soort grafieken die een operationele werkmap nodig heeft (status-bars per control, kalender-heatmap voor deadlines, RACI-matrices als gekleurde tabellen) volstaat het.

**Twijfels:**

- **Gebruikersgroep-mismatch**: CLAUDE.md positioneert Spoor B voor "compliance-officers". Lokale HTML + `.db`-bestand vraagt dat een gebruiker een file op disk heeft, in browser opent, niet vergeet om te saven. Dat is een **single-user-thuiswerk-workflow**, geen team-werkmap. Voor T&I-lab-test (één persoon, één PoC) prima; voor latere productie met meerdere compliance-officers fundamenteel ondergeschikt aan zelfs een minimale server-laag.
- **Audit-trail vs SQL.js**: een SQL.js-werkmap heeft `.db`-file als waarheid. Bij crash, accidentele close-zonder-save, of file-overschrijving is data verloren. Een audit-trail die *zelf* in dezelfde `.db` zit, valt mee weg. Voor een **Rijksoverheid-werkmap** met compliance-bewaartermijnen (sommige tot 7 of 10 jaar) is dat ontoereikend, ook in prototype-fase als de prototype-data niet weggegooid mag worden.
- **CRUD-discipline**: SQL.js heeft volledige SQL — INSERT/UPDATE/DELETE inclusief. Voor een operationele werkmap is dat het juiste niveau van vermogen, maar het zet ook geen rem op data-corruptie zonder app-niveau-discipline (transactions, validation, history-table-pattern). De CLAUDE.md-stack levert geen audit-/history-engine; die moet bovenop SQL.js gebouwd worden.

**Alternatieven:**

- **PWA met IndexedDB + lokale fallback**: Progressive Web App = installeerbaar lokaal, offline-first, IndexedDB als store. Voordeel: geen `.db`-file-management voor de gebruiker, browser-managed persistence, native sync-mogelijkheid (toekomstig). Nadeel: minder SQL-vermogen (IndexedDB is key-value+index, geen relational), meer code voor query-patronen.
- **Electron app**: lokaal-draaibaar 100% (geen browser-vereiste), Node.js-backend mogelijk (lokale SQLite native met betere persistence-garanties). Nadeel: zwaardere stack, vendor-lock-in op Electron-ecosysteem, installer-distributie-vraagstuk binnen Rijksoverheid.
- **Statische generator + lokale state**: een 11ty/Astro-build die de read-only-laag uit ontologie genereert + lichte JS voor lokale state (CRUD in localStorage/IndexedDB). Komt dicht bij Spoor A maar met operationele toevoegingen. Risico: vermenging Spoor A/B (discipline-punt productlijnen-concept).
- **Plain HTML + JS + JSON-file**: simpelste denkbare — geen SQL-engine, geen framework, JSON-bestand als store, fetch+save via download-link. Past bij Karpathy-Simplicity-First. Nadeel: geen native relational queries; veel JS-werk voor wat SQL gratis geeft.

**Mijn beoordeling (afhankelijk van Q-M1):** als de tech-stack-keuze (SQL.js + Chart.js) "hard" is, prima — bouw dan een degelijke audit-trail-laag bovenop SQL.js (zie O3). Als het "zacht" is, verdient een **PWA met IndexedDB** serieuze overweging voor de productie-fase, met SQL.js voor de prototype-fase als pragmatische tussenstap. Electron is een gerede optie voor productie als lokaal-installeerbaar pakket gewenst is.

#### O2 — Data-laag: hoe stroomt ontologie-data naar dashboard?

**Drie patronen:**

- **Patroon A — Read-only export vanuit Spoor A.** Spoor B haalt structuur (frameworks, controls, IRIs) uit `grc-data-vX_Y_Z.json` of een gerichte export, ontkoppeld van Spoor A's render-keten. Voordeel: één bron van waarheid voor structuur. Nadeel: koppeling A↔B die wijzigingen synchroon moet houden (zie §4).
- **Patroon B — Eigen lokale ABox in `.db`.** Spoor B heeft zijn eigen tabellen die organisatie-data dragen (`risicos`, `controls`, `eigenaren`, deadlines), met IRI als foreign-key terug naar ontologie. Voordeel: schone scheiding (ontologie = woordenboek, Spoor B = operationele staat). Nadeel: data-laag-divergentie als ontologie IRIs hernoemt zonder Spoor B-impact-check.
- **Patroon C — Hybride.** Structuur (frameworks/controls) uit ontologie, operationele velden (eigenaar/deadline/voortgang) in Spoor B. Praktisch het werkbaarste, maar vraagt expliciete update-discipline voor structuur.

Per productlijnen-concept: Spoor B "heeft eigen versie-track (`v3-2`-suffix, los van ontologie)" — dat suggereert sterk Patroon B of C. Patroon A werkt alleen als Spoor B continu synchroniseert, wat tegen de "los van ontologie"-conventie ingaat.

**Aanbeveling:** Patroon C (hybride). Structuur-import uit ontologie (eenmalig per versie-bump, handmatig getriggerd of via een dashboard-import-script); organisatie-data in eigen tabellen. Update-pad: bij elke ontologie-versie-bump een impact-script dat nieuwe controls toevoegt (insert), gewijzigde IRIs flagt (warning), verwijderde IRIs orphan-markeert (decline-to-delete-zonder-handmatige-actie).

#### O3 — Audit-trail-design (Rijksoverheid-context)

**Eisen voor een Rijksoverheid-audit-trail** (uit invariant-set + algemene compliance-discipline):

- **Append-only** — geen UPDATE/DELETE op audit-rijen, alleen INSERT
- **Bewaartermijn** — sommige Rijksoverheid-contexten 7 of 10 jaar; auditor-aantoonbaarheid
- **Integriteit** — manipulatie-detectie (hash-chain, signed-entries, of minimaal logical-key-pattern)
- **Reproduceerbaarheid** — kunnen reconstrueren wie wat wanneer wijzigde

**Implementatie-opties in SQL.js (Patroon C-context):**

- **Append-only-tabel** `audit_trail` met INSERT-only-trigger; row-format `(id, timestamp, user_alias, action, entity_type, entity_id, before_value, after_value, hash_prev_row)`. Hash van vorige rij in elke nieuwe rij = lichte chain-integrity zonder cryptografische signing.
- **Bewaartermijn** is een data-management-vraag, niet een tech-vraag: het is in de stack inherent dat data blijft staan tenzij explicit weggegooid. Wel: een **back-up-strategie** voor het `.db`-bestand is essentieel (regelmatige snapshot naar versie-gestempelde file). Geen automatische cloud-back-up (invariant lokaal-draaibaar), wel manual export (Steven exporteert wekelijks `.db` naar versie-folder).
- **Integriteit** via hash-chain is een prototype-niveau. Voor productie zou cryptografische signing (lokaal key-pair, niet centraal) overwogen moeten worden — maar dat is een productie-fase-overweging.
- **Reproduceerbaarheid** vraagt `user_alias`-field. In single-user-prototype is dat één alias; bij multi-user wordt het auth-laag-vraag (O4).

**Tweede aandachtspunt — audit-trail-bewaring overleeft een Spoor-B-rewrite niet automatisch.** Als Spoor B-prototype v3-2 wegvalt of in andere stack wordt herbouwd, hangt de audit-trail-historie in een file. Documentatie + export-discipline (CSV-export bij elke schema-wijziging) is een minimale veiligheidsmaatregel.

#### O4 — Authenticatie/autorisatie

**Spoor B-richtinggeving CLAUDE.md noemt dit niet expliciet.** Twee scenario's:

- **Single-user prototype** (huidige status): geen auth nodig. `.db`-bestand staat op Steven's of een individuele compliance-officer's machine. Toegangscontrole = file-system-toegang.
- **Multi-user productie**: vraagt server-laag (REST-API + identity-provider) of een gedistribueerd patroon (lokale auth + sync naar centraal store). Beide zijn substantiële architectuur-keuzes die het CLAUDE.md-prototype-pad verlaten.

**Aanbeveling:** prototype-fase = geen auth. Productie-fase = nieuwe architectuur-keuze. Bewust **niet** in het prototype een lichte-auth toevoegen die later vervangen wordt — dat is dood gewicht.

#### O5 — Offline-mode (lokaal-draaibaar invariant)

**Wat de invariant vraagt:** productie-toepassingen mogen geen cloud-internet-afhankelijkheid hebben. Voor Spoor B-prototype is dat 100% haalbaar (HTML+SQL.js+Chart.js = lokaal te draaien zonder netwerk; CDN-load kan vervangen door lokale vendor-bundles). **Aandachtspunt:** Q-M5 — in **prototype-fase** mag CDN-load? Bij strict-lokaal: vendor-pakket lokaal hosten in `dashboard/vendor/`. Bij soepel: CDN nu, vendoren bij productie-overgang.

#### O6 — Update-pad bij ontologie-evolutie

**Het probleem:** ontologie release-cadans is hoog (v4.X.Y, plus T-sprints). Spoor B mag niet bij elke release breken.

**Patroon (uit O2 Patroon C):** Spoor B importeert structuur uit ontologie bij een versie-bump-actie. Een **import-script** dat:

- Nieuwe controls/frameworks toevoegt (insert in structuur-tabellen)
- Gewijzigde IRIs flagt (warning aan gebruiker)
- Verwijderde IRIs orphan-markeert (decline-to-delete zonder handmatige actie — voorkomt data-verlies bij ontologie-cleanup)

Dit hoort bij **bouwsteen B7** hieronder (data-import-pijplijn Spoor A → Spoor B).

### 3.2 Bouwsteen-inventarisatie

Spoor B-bouwstenen, beoordeeld tegen O1–O6 + invarianten. Probleem-gerichte ordening (welke bouwsteen lost welke architectuur-overweging op).

#### B1 — SQL.js + lichte schema-laag

**Lost op:** O1 (tech-stack), O2 (data-laag-Patroon-C operationele kant).
**Wat:** SQL.js geladen via CDN of lokaal-gevendored. Schema: `frameworks`, `controls` (imported uit ontologie), `risicos`, `eigenaren`, `deadlines`, `voortgang`, `kalender_events`, `racis`, `audit_trail`. Migrations-discipline: numerieke versie in `schema_version`-tabel; per release-bump een idempotente UP-migration.

**Beoordeling:** waarde 4 / effort 4 / invariant 4 (lokaal-draaibaar mits vendor-gehost; auth ontbreekt = single-user-only) / overlap 5 (CLAUDE.md-richtinggevend; geen botsing) / reversibel 4.

**🟢 GO mits Q-M1 = "tech-stack hard"; bij "zacht" → 🟡 HOLD pending PWA-overweging.**

#### B2 — Chart.js voor visualisaties

**Lost op:** O1 (visualisatie-laag).
**Wat:** Chart.js voor bar/line/doughnut/heatmap. Past goed bij operational dashboards (status-per-control, deadlines-per-maand, voortgang-trends).

**Beoordeling:** waarde 4 / effort 5 (built-in) / invariant 5 (vendor lokaal te hosten) / overlap 5 / reversibel 5.

**🟢 GO.** Geen specifieke voorbehouden — accessibility-bewust, breed gebruikt, weinig surprises.

#### B3 — Append-only audit-trail-laag (eigen-bouwd)

**Lost op:** O3 (audit-trail).
**Wat:** SQL-trigger op INSERT-only voor `audit_trail`; per CRUD-actie elders in app een audit-row schrijven; hash-chain als lichte integriteit; CSV-export-knop voor handmatige back-up.

**Beoordeling:** waarde 5 (Rijksoverheid-essentie) / effort 3 (zorgvuldige implementatie nodig — triggers, hash, export) / invariant 5 / overlap 4 (geen botsing, vraagt discipline) / reversibel 4.

**🟢 GO — kritiek voor Rijksoverheid-context.** Geen NO-GO denkbaar (productie zonder audit-trail is per definitie ontoereikend in deze context).

#### B4 — RACI-component (uit ontologie + eigen UI)

**Lost op:** operationele RACI-zichtbaarheid.
**Wat:** ontologie heeft M04-rollen + RACI-property-set (uit eerdere sprints). Spoor B-UI toont per control een RACI-matrix (Responsible/Accountable/Consulted/Informed) met persoonsnamen (lokale tabel). Klik op rol → details.

**Beoordeling:** waarde 4 / effort 3 / invariant 5 / overlap 5 (bouwt op M04, behoort tot Spoor-B-werkstroom) / reversibel 4.

**🟢 GO.** Vereist Spoor-A-export-pad voor M04-rollen (zie B7).

#### B5 — Kalender-component (deadlines + audit-events)

**Lost op:** operationele tijdas-zichtbaarheid.
**Wat:** maand-/weekkalender (FullCalendar.js is een rijpe optie, MIT-licentie, lokaal te hosten). Events uit `deadlines` + `kalender_events` + `audit_trail` (laatste 30 dagen). Klik → detail-paneel.

**Beoordeling:** waarde 4 / effort 3 / invariant 4 (FullCalendar vendor toevoegen aan stack — kleine afwijking van Chart.js-minimum) / overlap 4 (introduceert vendor) / reversibel 4.

**🟢 GO, met voorbehoud:** als de stack-discipline "alleen SQL.js + Chart.js + vanilla JS" hard is (Q-M1), dan vervalt FullCalendar en moet kalender met `<table>`-grid + Chart.js heatmap gebouwd worden. Effort verschuift dan naar 2; waarde naar 3.

#### B6 — Form-libraries / validatie

**Lost op:** CRUD-betrouwbaarheid.
**Wat:** voor CRUD-formulieren een lichte form-validatie-bibliotheek. Just-Validate (MIT, vanilla JS, ~10 kB) is een passende keuze; of helemaal zelf met HTML5 native validation + custom JS.

**Beoordeling:** waarde 3 / effort 4 / invariant 5 / overlap 5 / reversibel 5.

**🟢 GO, kies dunste optie.** Geen frameworks; native HTML5-validatie + 50 regels custom JS is genoeg voor prototype-CRUD. Just-Validate als upgrade-pad bij complexere forms.

#### B7 — Data-import-pijplijn Spoor A → Spoor B

**Lost op:** O6 (update-pad).
**Wat:** Python-script `import-from-ontology-vX_Y_Z.py` dat uit `grc-data-vX_Y_Z.json` (of een dashboard-specifieke export, zie §4) de structuur extraheert (frameworks, controls, IRIs, labels, RACI-rollen) en als idempotente SQL-INSERT-bundle exporteert (`structure-import-vX_Y_Z.sql`). Spoor B-app heeft een import-knop die deze SQL uitvoert via SQL.js + migration-versie bumpt.

**Beoordeling:** waarde 5 (de keten zonder dit punt is broken: handmatig invoeren = onverdedigbaar) / effort 3 / invariant 5 / overlap 4 (raakt Spoor-A-build-pipeline) / reversibel 4.

**🟢 GO.** Belangrijke detail: import-script moet **idempotent** zijn (re-import van dezelfde versie veroorzaakt geen data-verlies) en **non-destructive** (verwijderde controls in nieuwe ontologie-versie worden orphan-markered, niet hard-gedelete).

#### B8 — NL Design System-componenten (NLDS, nldesignsystem.nl)

**Lost op:** UI-consistentie + WCAG/toegankelijkheid.
**Wat:** het Nederlandse overheids-design-system (open-source, MIT-achtig licenties per component) levert UI-componenten gebouwd voor Rijksoverheid-context (toegankelijk, herkenbare iconografie, kleurpalet, formulier-patronen, navigatie). Daarbij Rijkshuisstijl (rijkshuisstijl.nl) als visuele identiteit-bron. Voor een Rijksoverheid-werkmap is dit potentieel de meest natuurlijke UI-basis.

Belangrijk: NLDS is **niet één framework** maar een set componenten in meerdere implementaties (web components, React, Vue). Voor een vanilla-stack zijn de **NLDS Web Components** waarschijnlijk de juiste keuze (geen build-tool nodig, native browser, lokaal-draaibaar).

**Beoordeling:** waarde 4 (toegankelijkheid + Rijksoverheid-passing) / effort 3 (leercurve + integratie + selectie welke componenten) / invariant 5 (lokaal te hosten, MIT-achtig, geen black-box) / overlap 4 (vervangt deel van eigen UI-code) / reversibel 4.

**🟡 HOLD → 🟢 GO afhankelijk van Q-M1 + Q-M5.** Bij "stack zacht" + "lokaal-draaibaar soepel in prototype" = GO; bij "vanilla-only hard" = vervalt.

- *Waarom geen onvoorwaardelijke GO:* NLDS toevoegen is een stack-keuze; in een vanilla-stack-context betekent het een componentenbibliotheek toevoegen waar geen andere is. Niet doen als de Simplicity-First-discipline strikt is.
- *Waarom geen NO-GO:* een Rijksoverheid-werkmap UI bouwen met willekeurige stijl is een **gemiste kans**; NLDS bestaat juist voor deze context.

#### B9 — WCAG-toegankelijkheid (eis, niet bouwsteen)

**Lost op:** Rijksoverheid-vereiste (digitoegankelijk.nl + WCAG 2.1 AA minimum).
**Wat:** geen aparte bouwsteen — een eis die op alle UI-bouwstenen weegt. Test-tools: axe-core (MIT, lokaal te draaien, accessibility-linter); WAVE (browser-extension); manual checks (toetsenbord-navigatie, screen-reader). Belangrijke implicatie voor stack-keuze: Chart.js heeft een accessibility-plugin; native HTML-tabellen zijn van nature toegankelijker dan ARIA-rich-custom-widgets. NLDS-componenten zijn voor toegankelijkheid getest.

**Beoordeling:** waarde 5 / effort 3 / invariant 5 / overlap 5 / reversibel 5.

**🟢 GO — verplichting, geen optie.** Plan axe-core in CI/check-stappen vanaf dag 1 van Spoor-B-bouw.

#### B10 — Audit-/compliance-georiënteerde OS-componenten

**Lost op:** specifieke patronen (status-bewijsvoering, evidence-attach, control-status-flow).
**Wat:** open-source GRC-compatibele componenten — zoals genoemd in voorganger-rapport §G (Sushegaad, GRCEngClub). **Per de voorganger-evaluatie zijn deze beperkt bruikbaar voor Spoor B:**

- Sushegaad/Claude-Skills-GRC: 🟡 HOLD (geen NL-context, ISO-skill-overlap-risico, marketing-benchmarks).
- GRCEngClub/claude-grc-engineering: 🟡 HOLD-Spoor-B (focus is evidence-collection cloud/SaaS — past gedeeltelijk; SCF-crosswalk-laag conceptueel relevant maar OWL/Turtle-mismatch).
- euCann/OSCAL-GRC-SKILLS: methodologische referentie, geen tooling-fit (OSCAL JSON/XML, mismatch met Spoor-B-SQL).
- mlunato47/claude-grc-plugin: 🔴 NO-GO (NIST-hub schendt D9).
- gigachad-grc: full GRC-platform — verkeerde categorie (vervangt het project, niet vult een lacune).

**Beoordeling:** waarde 1–3 per kandidaat / effort 1–3 / invariant 2–4 / overlap 2 (vooral D9-conflict) / reversibel 4.

**🔴 NO-GO als directe tooling, 🟢 GO als methodologische referentie.** De *patronen* (evidence-attach UI, status-flow, control-mapping) zijn waardevol om te ontlenen; de *implementaties* passen niet bij D9 + lokaal-draaibaar + NL-context.

#### B11 — Spoor-B-data-export (back-up + auditor-deliverable)

**Lost op:** O3 (audit-trail-bewaring-overleeft-rewrite), O5 (offline-back-up).
**Wat:** elke versie van Spoor B heeft een "Export"-knop die `.db`-dump + CSV-versies (per tabel) + JSON-snapshot levert. Daarbij timestamped-folder-naam-conventie zodat versie-historie inherent is. Voor auditor-deliverable: extra CSV-template "audit-trail-vN-export-YYYY-MM-DD.csv".

**Beoordeling:** waarde 4 / effort 4 / invariant 5 / overlap 5 / reversibel 5.

**🟢 GO.** Past bij Spoor-B-discipline van "export-conventies" (analoog aan dashboard-subagent-config §"Hash-bestand-padding-conventie", maar dan voor data-export).

### 3.3 Aanbevolen architectuur-besluit-volgorde

Spoor B mag niet beginnen met tooling-keuzes zonder eerst een paar architectuur-besluiten te nemen. Volgorde-afhankelijk:

1. **B0 — Spoor-B-locatie-besluit definitief maken (Q-M2)** — staat de v3-2 nu wel of niet in de repo? Tot dit besluit duidelijk is, is alles wat over Spoor-B-data-laag gaat onzeker (publieke repo ≠ Rijksoverheid-werkmap).
2. **B0b — Hard/zacht-status van CLAUDE.md-tech-stack (Q-M1)** — SQL.js + Chart.js + vanilla HTML hard of zacht? Bepaalt of PWA/Electron-alternatieven serieus mee-evalueren of buiten scope blijven.
3. **B0c — Lokaal-draaibaar-invariant in prototype-fase (Q-M5)** — strict (vendor-only) of soepel (CDN-prototype, vendor-productie)? Bepaalt of NLDS / FullCalendar / Cytoscape op CDN gebruikt mag worden.
4. **B0d — Single-user-prototype vs latere multi-user — bewust geaccepteerd?** Geen auth in prototype = geaccepteerd. Productie-pad ("vanuit prototype migreren of green-field-herbouwen") = nieuwe masterchat-vraag op zijn tijd; geen prototype-impact nu.
5. **Dan pas tooling-keuzes**: B1 SQL.js, B2 Chart.js, B3 audit-trail-laag, B7 import-pijplijn (cruciaal: zonder import-pijplijn is Spoor B niet leverbaar — vroeg in volgorde).
6. **Daarna UI-componenten**: B4 RACI, B5 kalender, B6 form-validatie, B8 NLDS (afhankelijk van B0b/B0c).
7. **WCAG vanaf dag 1**: B9 niet uitstellen — accessibility-debt is duurder dan accessibility-investering.
8. **Eind-fase prototype**: B11 export-discipline.

### 3.4 GO/HOLD/NO-GO-overzicht Spoor B

| ID | Bouwsteen | Status | Voorwaarde / opmerking |
|---|---|---|---|
| **B0** | Spoor-B-locatie-besluit | 🔴 BLOKKEREND | Q-M2: lokaal of repo? Zonder antwoord geen aanbevelingen mogelijk |
| **B0b** | Tech-stack hard/zacht | 🔴 VRAAG | Q-M1 bepaalt range van bouwstenen |
| **B0c** | Lokaal-draaibaar strict/soepel | 🔴 VRAAG | Q-M5 bepaalt CDN-/vendor-keuzes |
| B1 | SQL.js + schema | 🟢 GO mits stack hard | PWA/IndexedDB als alternatief bij zacht |
| B2 | Chart.js | 🟢 GO | Past in alle scenario's |
| B3 | Append-only audit-trail | 🟢 GO | Niet-onderhandelbaar voor Rijksoverheid |
| B4 | RACI-component | 🟢 GO | Vereist B7 (import) |
| B5 | Kalender | 🟢 GO (FullCalendar) of 2-prio (native) | Afhankelijk van Q-M1 |
| B6 | Form-validatie (dun) | 🟢 GO | Begin native, escaleer naar Just-Validate |
| B7 | Import-pijplijn Spoor A → B | 🟢 GO (kritiek-pad) | Zonder dit geen werkende Spoor B |
| B8 | NLDS Web Components | 🟡 HOLD → GO | Afhankelijk van Q-M1 + Q-M5 |
| B9 | WCAG-toegankelijkheid | 🟢 GO (verplichting) | Dag 1, niet later; axe-core in CI |
| B10 | Externe GRC-OS-tooling | 🔴 NO-GO direct / 🟢 referentie | Per voorganger-rapport bevestigd |
| B11 | Spoor-B-export-discipline | 🟢 GO | Eind-fase prototype |

**Rode draad Spoor B:** drie architectuur-vragen (Q-M1, Q-M2, Q-M5) moeten beantwoord vóór bouwsteen-selectie zin heeft. Eenmaal beantwoord is de set robuust: B1 (SQL.js) + B2 (Chart.js) + B3 (audit-trail) + B7 (import) zijn de kritieke-pad-vier. B8 (NLDS) is de grootste hefboom voor UI-kwaliteit en Rijksoverheid-passing maar afhankelijk van stack-soepelheid. B9 (WCAG) is verplichting, niet keuze. B10 (externe GRC-tools) blijft NO-GO direct — referentie wel.

**Bewust niet geadresseerd:** server-laag / multi-user / sync. Dat is buiten prototype-scope, dat blijft buiten dit rapport.

---

## 4. Koppeling Spoor A ↔ Spoor B

### 4.1 Koppel-patronen + voor/nadelen

Zes patronen, beoordeeld tegen invarianten (lokaal-draaibaar, mens-in-controle, framework-neutraliteit D9, geen organisatie-data extern).

#### P1 — Embedded link (Spoor B → Spoor A per concept)

**Wat:** elk Spoor-B-record met een IRI-veld krijgt een hyperlink naar de Spoor-A-explorer (`grc-explorer-vX_Y_Z.html#nodeId=<IRI>`). Klik in Spoor B → opent Spoor A in nieuw tabblad, scrollt naar concept.
**Voor:** simpelst denkbare koppeling. Spoor A en B blijven volledig onafhankelijk; Spoor A heeft geen weet van Spoor B. Geen sync-vereiste. Werkt lokaal (allebei lokale HTML).
**Tegen:** vereist dat Spoor A deep-linking ondersteunt (URL-parameter → preselect node in verkenner-tab). Dat is nu **niet** geïmplementeerd in de explorer (gelezen code: geen URL-param-handler). Toevoeging is laagdrempelig.
**Invarianten:** 🟢 alle.

**🟢 GO als geen-spijt-eerste-koppeling.** Voeg `?node=<IRI>` URL-param-handler aan Spoor A toe (Bouwsteen K1 hieronder); Spoor B kan dan vandaag of morgen al linken.

#### P2 — Read-API (Spoor A exposeert lichte SPARQL-/JSON-endpoint)

**Wat:** een lichte HTTP-server (Python+Flask of statisch via `python -m http.server`) bovenop `grc-data-vX_Y_Z.json` die endpoints biedt zoals `/api/individual/<id>`, `/api/skos-mappings/<id>`. Spoor B raadpleegt op-aanroep.
**Voor:** dynamisch — Spoor B kan altijd de meest actuele Spoor-A-data ophalen. Bevattelijk voor uitbreiding (eigen SPARQL-endpoint via een lokale Oxigraph).
**Tegen:** **server-laag** — botst met lokaal-draaibaar zonder server. Spoor A is nu een statische HTML-app; toevoegen van API-server verschuift het paradigma.
**Invarianten:** 🟡 lokaal-draaibaar (mits lokale server, niet cloud); rest 🟢.

**🟡 HOLD.** Past pas bij **Spoor C** (CLAUDE.md noemt triplestore-overweging) waar een server-laag sowieso erbij komt; niet bij Spoor-B-prototype.

#### P3 — Gedeelde data-laag (beide producten lezen dezelfde export)

**Wat:** één canonical export-set (`grc-data-vX_Y_Z.json` + een vergelijkbare `grc-structure-vX_Y_Z.json` voor Spoor B) die door beide producten geconsumeerd wordt. Geen runtime-koppeling.
**Voor:** versie-consistentie via export-discipline. Geen sync-mechanismen.
**Tegen:** twee read-only-consumers van dezelfde data — Spoor B's operationele data (eigenaren, deadlines, voortgang) is niet in deze export en moet apart blijven. Patroon C uit §3.1-O2 in de praktijk.
**Invarianten:** 🟢 alle.

**🟢 GO — feitelijk wat Bouwsteen B7 (import-pijplijn) al doet, alleen op een ander niveau geformaliseerd.** Spoor B's import-pijplijn (B7) is precies een implementatie van P3. Geen extra werk; dit ís het al.

#### P4 — Bidirectional sync (Spoor B kan annotaties terugschrijven naar ontologie)

**Wat:** een Spoor-B-record over een control kan een "vragen/annotaties bij dit concept" veld krijgen dat *terug* naar de ontologie wordt gesynchroniseerd (mogelijk als rdfs:comment of een aparte ext:annotation-property).
**Voor:** organisatie-feedback wordt onderdeel van het kennismodel. Sluit aan bij toekomst-visie (operationele inzichten beïnvloeden referentie-laag).
**Tegen:** **schendt het framework-neutraal-principe** als de annotaties één bepaalde organisatie-context dragen die het generieke model vervuilt. Bovendien is dit een **schrijfrichting van organisatie-data naar publieke (open-source) ontologie** — bij Spoor-B-met-organisatiedata is dat een potentieel grote organisatie-data-lek-vector (invariant: geen organisatie-data extern, en de repo is publiek GitHub).
**Invarianten:** 🔴 organisatie-data extern (bij Rijksoverheid-werkmap-data in publieke repo); 🟡 framework-neutraliteit; rest 🟢.

**🔴 NO-GO (Spoor A). 🟡 HOLD-toekomst** alleen bij interne GitLab-on-prem + heldere annotatie-scheiding (organisatie-laag vs referentie-laag).

#### P5 — Embedded iframe / micro-frontend

**Wat:** Spoor B embeddet de Spoor-A-explorer in een iframe of via een micro-frontend-pattern, zodat een gebruiker beide in één scherm ziet.
**Voor:** UX-eenheid voor gebruiker.
**Tegen:** **schendt het twee-producten-discipline** uit het productlijnen-concept ("niet vermengen in één UI"). Conceptueel verwarrend (gebruiker ziet ontologie-graaf + operationele werkmap door elkaar). Bovendien heeft Spoor A render-conventies die niet matchen met operationele-werkmap-conventies (kleuren per laag vs status-per-control).
**Invarianten:** 🟡 framework-neutraliteit (Spoor A is neutraal, Spoor B is BIO-perspectief — mengen zou framework-bias introduceren).

**🔴 NO-GO.** Het productlijnen-concept verbiedt expliciet menging in één UI. Niet doen.

#### P6 — Sidecar-tool (Spoor A kan Spoor B-records tonen als visit-targets)

**Wat:** in Spoor A, in het detail-paneel van een control, een knop "Bekijk in werkmap" die de gebruiker naar Spoor B brengt mét voorgeselecteerde control-context.
**Voor:** spiegel van P1 — Spoor B → Spoor A bestaat al; Spoor A → Spoor B is de andere kant.
**Tegen:** Spoor A wordt **bewust niet** aan organisatie-data gekoppeld. Een knop "bekijk in werkmap" suggereert dat de werkmap context "kent" die hij niet altijd heeft. Bovendien: Spoor A is publiek (in repo), Spoor B is in essence organisatie-specifiek — een directe knop kan een gebruiker ertoe verleiden organisatie-data te verwachten in een neutraal product.
**Invarianten:** 🟡 — niet hard fout, wel discipline-spanning.

**🟡 HOLD.** Niet als prio; mogelijk later als Spoor B volwassen is en gebruik-pattern duidelijk.

### 4.2 Spoor-B-ontwerp-implicaties (geen-spijt-keuzes nu)

Wat **nu** in Spoor-B-ontwerp opgenomen kan worden zonder een specifieke koppeling vast te leggen, maar wat **latere koppeling makkelijker** maakt:

#### K1 — IRI-velden in Spoor B-tabellen vanaf dag 1

Elk record over een ontologie-concept (control, framework, rol) draagt een `iri`-veld dat exact de IRI uit de ontologie matcht. Zonder dit veld is geen P1/P3/P6-koppeling mogelijk. Voeg dit toe vóór data-population, niet erna.

**🟢 GO.** Triviale toevoeging; vermijdt grote refactor later.

#### K2 — Deep-linking-support in Spoor A (URL-param `?node=<IRI>`)

Een 30-regel-toevoeging aan de Verkenner-tab van Spoor A: bij page-load lees URL-param, indien aanwezig zoek node, selecteer en loadEgo(). Zo werkt P1 (embedded link) zonder Spoor-B-aanpassing.

**🟢 GO.** Geringe Spoor-A-aanraking; opent expliciete koppel-mogelijkheid.

#### K3 — Versie-aanduiding zichtbaar in beide producten

Zowel Spoor A als Spoor B tonen prominent welke ontologie-versie (vX_Y_Z) ze representeren. Bij een gebruiker die A → B linkt, mag onverwacht versie-verschil niet onopgemerkt blijven.

**🟢 GO.** Spoor A heeft dit (header-meta). Spoor B moet dit krijgen via Bouwsteen B7-import-pijplijn — log de geïmporteerde ontologie-versie als zichtbare metadata.

#### K4 — Spoor-A-export geschikt voor Spoor-B-import (Patroon C)

Zoals al gezegd: B7 (import-pijplijn) is de feitelijke implementatie van P3. Zorg dat de Spoor-A-export-pipeline (build_grc_explorer_v3.py) **óók een Spoor-B-vriendelijke variant produceert** — niet alle Cytoscape-nodes/edges, maar een minimale structuur-export (frameworks, controls, IRIs, labels, RACI-rollen, nothing operational). Bouwsteen-verfijning: in plaats van twee aparte export-paden, één parameterizable script `dashboard/build_exports_vN.py` met flags `--explorer` (Cytoscape-rijk) en `--structure` (Spoor-B-mager).

**🟢 GO** — gestructureerd in plaats van twee parallelle exporten te onderhouden.

### 4.3 Niet-aanbevolen patronen

Expliciet wat **niet** moet:

#### N1 — Spoor B-data in Spoor A injecteren

Geen embedding van operationele eigenaren/deadlines in de explorer. Zou D9 (neutraliteit) schenden en publieke-repo-organisatie-data-lek introduceren. P5 expliciet NO-GO.

#### N2 — Spoor B schrijft naar ontologie-modules

Annotaties die organisatie-context dragen, mogen niet als rdfs:comment of vergelijkbaar in ontologie-modules belanden. Als feedback uit Spoor B naar ontologie moet, dan via een **scope-pauze-route**: Steven beoordeelt, en organisatie-neutrale verbeteringen gaan via Tech-subagent in een formele sprint. Zie P4 NO-GO.

#### N3 — Spoor A wordt versie-gebonden aan Spoor B

Spoor A volgt ontologie-versie (v4.6.X); Spoor B heeft eigen versie-track (v3-X per productlijnen-concept). Bij koppeling mag Spoor A's versie-cadans **niet** vertragen voor Spoor B-readiness. Spoor A blijft de leader; Spoor B importeert als consumer.

#### N4 — Eén UI voor beide producten

Productlijnen-concept is autoritatief: niet vermengen in één UI. Een tweede tab in Spoor A die "operationele view" toont, of een Spoor-B-pagina die ontologie-graaf embed, is een schending. Aparte producten blijven aparte producten.

### 4.4 Aanbevolen geen-spijt-keuzes nu

Samenvattend de geen-spijt-keuzes (los van welke koppel-patroon ooit gekozen wordt):

| ID | Keuze | Onderbouwing |
|---|---|---|
| K1 | IRI-velden in Spoor B-tabellen vanaf dag 1 | Opent P1 / P3 / P6 zonder refactor; nul-kost nu |
| K2 | Deep-link-support in Spoor A (`?node=<IRI>`) | Triviale toevoeging; opent embedded link-patroon (P1) |
| K3 | Versie-aanduiding zichtbaar in beide | Voorkomt versie-mismatch-verwarring bij koppeling |
| K4 | Spoor-A-export parameterizable (--explorer / --structure) | Voorkomt twee parallelle export-paden |

**Wat expliciet géén geen-spijt-keuze is:** bidirectional sync, micro-frontend, gedeelde UI. Die mogen wachten op een specifieke trigger (Spoor B-productie, organisatie-overdracht, of een usability-test-finding) — niet preventief opbouwen.

---

## 5. Domein-deep-dive (A–G)

Kort per domein: inventarisatie + relevantie + aanbeveling.

### 5.A — Graph-visualisatie-state-of-the-art (2025–2026)

| Library | Sterkten | Zwakten | Past bij | Aanbeveling |
|---|---|---|---|---|
| **Cytoscape.js** (huidig) | Rijp, accessibility-bewust, graph-theorie-features, MIT, breed gebruikt | DOM-renderer (SVG/canvas) — schaalt tot ±5–10k nodes vlot, daarboven traag | OWL-/ontologie-graph van ~1.400 individuen | 🟢 Behouden (Spoor A) |
| **Sigma.js** v2/v3 | WebGL-renderer, schaalt naar 100k+ nodes, lichtere voetafdruk | Minder rijpe interactie-API, smaller community | Grote graph-visualisatie | 🔴 NO-GO nu / 🟡 bij groei (H33 of A↔B-koppeling) |
| **vis-network** | Native physics-simulatie, makkelijk te starten | Minder graph-theorie-tools, kleinere community | Snelle prototypes | 🔴 NO-GO (geen reden te wisselen) |
| **D3-force** | Maximaal flexibel, programmeer-paradigma | Hoge leercurve, geen "out-of-the-box" graph-component | Custom visualisaties | 🔴 NO-GO (Cytoscape is voor dit doel een betere fit) |
| **ELK-layout** | Excellent voor hiërarchische layouts (compound graphs) | Server-side processing in Java, of via elkjs (WASM) | Architectuur-diagrammen met hiërarchie | 🟡 HOLD-kandidaat als hiërarchische framework-layouts gewenst worden |

**Aanbeveling:** Cytoscape blijft. Bij data-groei of A↔B-koppeling met groter dataset: Sigma.js als migratie-kandidaat. Geen pre-emptive switch.

### 5.B — Visuele regressie / render-test-strategieën

| Strategie | Hoe het werkt | Past bij dit project |
|---|---|---|
| **Playwright + pixel-diff** | Headless browser-screenshot per test, vergelijk met baseline-PNG | 🟢 GO (Bouwsteen D niveau 1) — open-source, lokaal-draaibaar, MIT |
| **Playwright + DOM-snapshot** | Vergelijk DOM-serialisatie i.p.v. pixels | 🟢 GO (Bouwsteen D niveau 2) — minder false-positives, sneller |
| **Percy / Chromatic** | Cloud-based visual regression services | 🔴 NO-GO — cloud-afhankelijk, licht commercieel, schendt lokaal-draaibaar |
| **Storybook + Chromatic** | Component-isolation-test | 🔴 NO-GO — overkill voor één HTML-pagina; vendor-lock |

**Aanbeveling:** Playwright niveau 1 (pixel-diff voor Tab 1+2 static layouts) + niveau 2 (DOM-snapshot voor Tab 3 dynamische graph). Lokaal, open-source, geen vendor-binding.

### 5.C — Operationele compliance-werkmappen (Spoor B)

Per voorganger-rapport §G + extra inventarisatie:

| Project | Past bij Spoor B? | Reden |
|---|---|---|
| **Sushegaad/Claude-Skills-GRC** | 🟡 HOLD | Geen NL-context, ISO-skill-overlap-risico — referentie OK, directe inzet niet |
| **GRCEngClub/claude-grc-engineering** | 🟡 HOLD-Spoor-B | Evidence-collection-focus past gedeeltelijk; SCF-crosswalk methodologisch relevant maar OWL-mismatch |
| **euCann/OSCAL-GRC-SKILLS** | 🟢 referentie | OSCAL-control-mapping-model conceptueel verwant; serialisatie-mismatch — geen tooling-fit |
| **mlunato47/claude-grc-plugin** | 🔴 NO-GO | NIST-hub schendt D9 |
| **gigachad-grc** | 🔴 NO-GO | Volledig GRC-platform — verkeerde categorie (vervangt project) |
| **NLDS Web Components** (nldesignsystem.nl) | 🟡 HOLD → 🟢 GO afhankelijk van Q-M1 | Rijksoverheid-design-system; toegankelijkheid built-in |
| **OSCAL-tooling generiek** (NIST) | 🔴 referentie | JSON/XML-stack mismatch met OWL/Turtle/SQL.js |
| **Open Policy Agent (OPA) + Rego** | 🔴 NO-GO | Policy-as-code-engine — past niet bij dashboard-werkmap |

**Aanbeveling:** geen externe GRC-tool als drop-in voor Spoor B. NLDS (NL-specifiek) is de enige potentieel-passende externe component, afhankelijk van stack-soepelheid.

### 5.D — NL Design System + Rijksoverheid-componenten

**NL Design System (NLDS)** — `nldesignsystem.nl`:

- Open-source design-system voor overheidsdiensten (gemeenten, ministeries, ZBO's, etc.)
- Web components (`@utrecht/component-library-web-components`) + React-variant
- Built-in toegankelijkheid (WCAG 2.1 AA)
- Componenten relevant voor compliance-werkmap: form-controls, tables, alerts, button-patronen, navigation, breadcrumbs, page-layouts
- MIT-licensed of EUPL voor kerncomponenten — open

**Rijkshuisstijl** (`rijkshuisstijl.nl`):

- Visuele identiteit-handboek (typografie, kleuren, logo-richtlijnen)
- Niet één pakket maar een referentie

**Relevantie voor Spoor B:**

- Bij stack "zacht": NLDS Web Components zijn de logische UI-basis. Rijksoverheid-context, toegankelijkheid gegarandeerd, geen design-werk vanaf nul.
- Bij stack "hard" (vanilla only): NLDS-tokens (CSS-variabelen) kunnen wel hergebruikt zonder de componenten — kleur-palet, typografie, spacing-schaal.

**Aanbeveling:** zelfs in het hardst-vanilla-scenario zijn NLDS' design-tokens (CSS-variabelen, typografie-schaal, kleur-palet) opname-waardig. Componenten erbij is een afzonderlijke beslissing.

### 5.E — Audit-trail-patronen + data-laag voor lokale werkmap

| Patroon | Implementatie | Past bij Spoor B prototype |
|---|---|---|
| **Append-only logging** | SQL-trigger op INSERT-only-tabel | 🟢 GO (Bouwsteen B3) |
| **Event-sourcing** | Events als first-class; state derived | 🟡 HOLD — krachtig maar overkill voor prototype |
| **CQRS-light** | Read- en write-models gescheiden | 🟡 HOLD — past bij groei |
| **Lokale SQLite via sql.js** | WASM-compilatie van SQLite, in-browser | 🟢 GO (Bouwsteen B1) |
| **IndexedDB** | Browser-native key-value+index | 🟢 alternatief bij Q-M1 "zacht" |
| **PWA-storage met Service Worker** | Offline-first, sync-when-online | 🟡 HOLD — relevant bij multi-user / online-sync-fase |
| **Hash-chain integrity** | Elke rij hash van vorige | 🟢 GO (Bouwsteen B3 sub-detail) |
| **Cryptographische signing per entry** | Lokaal key-pair, GPG-style | 🟡 HOLD — productie-fase |

**Aanbeveling:** append-only + hash-chain voor prototype (B3). Event-sourcing en signing pas bij productie-overweging.

### 5.F — Anthropic-native + community skills relevant voor dashboards

Per voorganger-rapport §C + §F:

| Skill | Relevantie Spoor A / B |
|---|---|
| **frontend-design** (Anthropic native) | 🟢 GO Spoor A bij H40; 🟢 GO Spoor B bij UI-bouw |
| **docx** (Anthropic native) | 🟢 GO Spoor B voor export-rapporten (compliance-status-doc) |
| **pptx** (Anthropic native) | 🟢 GO Spoor B voor management-presentatie-export |
| **xlsx** (Anthropic native) | 🟢 GO Spoor B voor data-export (audit-deliverable) |
| **pdf** (Anthropic native) | 🟢 GO Spoor B voor PDF-rapportages |
| **skill-creator** (Anthropic native) | 🟢 GO als enabler voor Bouwsteen F (`/dashboard-build`) |
| **kfchou/wiki-skills** (community) | 🟡 referentie voor brain-lint-skill, geen Spoor A/B-installatie |
| **kepano/obsidian-skills** (community) | 🔴 NO-GO (Obsidian-specifiek, niet dashboard-relevant) |
| **AgriciDaniel/claude-obsidian** (community) | 🟡 referentie alleen |

**Aanbeveling:** Anthropic-native skills (frontend-design, document-export-set, skill-creator) zijn voor zowel A als B nuttig; community-wiki-skills blijven referentie.

### 5.G — MCP-servers relevant voor dashboards

Per voorganger-rapport §E + nieuw geanalyseerd:

| MCP-server | Spoor A | Spoor B | Reden |
|---|---|---|---|
| **GitHub-MCP** (in gebruik) | 🟢 | 🟢 | Repo-toegang voor beide |
| **open-ontologies-MCP** | 🟡 (HOLD: evaluatie-sprint pending) | 🟡 (zelfde) | Reasoning/SHACL/SPARQL als tools — past meer bij Spoor B-import-pijplijn dan bij Spoor A-render |
| **mcp-rdf-explorer (lichte SPARQL)** | 🔴 NO-GO | 🔴 NO-GO | Redundant; geen render-/CRUD-meerwaarde |
| **Playwright/Browser-automation MCP** | 🟢 GO-kandidaat | 🟢 GO-kandidaat | Voor Bouwsteen D (visuele regressie) en Spoor B-UI-test |
| **Filesystem-MCP** (Anthropic of community) | 🟡 HOLD | 🟡 HOLD | Voor dashboard-deploy zonder shell — overkill voor één HTML |

**Aanbeveling:** GitHub-MCP behouden (in gebruik). Playwright-MCP overwegen voor Bouwsteen D + Spoor-B-toegankelijkheidstests (axe-core via Playwright). Open-ontologies-MCP: blijf bij voorganger-rapport-oordeel (evaluatie-sprint pending).

---

## 6. Samenvatting (bottom-up — pas na alle detail)

Cumulatief overzicht van aanbevelingen per sub-vraag, met sub-vraag-toewijzing en korte reden.

| # | Aanbeveling | Sub-vraag | Recommendation | Korte reden |
|---|---|---|---|---|
| A | Versie-suffix-templating (uit DATA.meta) | 1 | 🟢 GO | K1; onderdeel volgende build-aanraking |
| B | Render-conventies-document (brain-concept) | 1 | 🟢 GO afh. Q-D2 | K7; expliciteert impliciete conventies |
| C | Data-driven framework-config | 1 | 🟢 GO middellange termijn | K1-hoofdoorzaak; bundel met UI-mini-sprint |
| D | Visuele regressie (Playwright headless) | 1 | 🟡 HOLD → GO afh. Q-D6+Q-D3 | K3; effort/onderhoud reëel |
| E | Pre-sprint-explorer-update-protocol (Protocol 18) | 1 | 🟢 GO | K2/K3; analoog aan Tech-Protocol 1 |
| F | Skill `/dashboard-build` | 1 | 🟢 GO ná E | K6; codificeert 7-stappen-cyclus |
| G | Lokale ontwikkel-loop subagent | 1 | 🟡 HOLD afh. Q-D6 | K3/K4; afhankelijk van render-capaciteit |
| H | Cytoscape-alternatief (Sigma) | 1 | 🔴 NO-GO nu / 🟡 bij groei | K8 latent; geen pijn |
| I | On-demand detail-fetch | 1 | 🟡 HOLD bij H40 | K8/K4; koppelen aan H40-activering |
| J | frontend-design skill | 1 | 🟢 GO bij H40 | K4; geen waarde vóór UI-modernisering |
| **B0** | **Spoor-B-locatie-besluit (Q-M2)** | **2** | **🔴 BLOKKEREND** | **Repo-aanwezigheid v3-2 onverklaard** |
| **B0b** | **Tech-stack hard/zacht (Q-M1)** | **2** | **🔴 VRAAG** | **Bepaalt range van bouwstenen** |
| **B0c** | **Lokaal-draaibaar in prototype (Q-M5)** | **2** | **🔴 VRAAG** | **Bepaalt CDN/vendor-keuzes** |
| B1 | SQL.js + schema | 2 | 🟢 GO mits stack hard | O1; PWA als alternatief |
| B2 | Chart.js | 2 | 🟢 GO | O1; alle scenarios |
| B3 | Append-only audit-trail (hash-chain) | 2 | 🟢 GO | O3; Rijksoverheid-essentie |
| B4 | RACI-component | 2 | 🟢 GO | Vereist B7 |
| B5 | Kalender (FullCalendar of native) | 2 | 🟢 GO | Afh. Q-M1 |
| B6 | Form-validatie (dun) | 2 | 🟢 GO | Begin native, escaleer naar Just-Validate |
| B7 | Import-pijplijn A → B | 2 | 🟢 GO (kritiek-pad) | O6; zonder dit geen werkende B |
| B8 | NLDS Web Components | 2 | 🟡 HOLD → GO afh. Q-M1+Q-M5 | Rijksoverheid-passing UI |
| B9 | WCAG-toegankelijkheid (axe-core) | 2 | 🟢 GO (verplichting) | Dag 1 |
| B10 | Externe GRC-OS-tooling | 2 | 🔴 direct / 🟢 referentie | Per voorganger bevestigd |
| B11 | Spoor-B-export-discipline | 2 | 🟢 GO | Eind-fase prototype |
| K1 | IRI-veld in Spoor B vanaf dag 1 | 3 | 🟢 GO | Opent koppeling zonder refactor |
| K2 | Deep-link Spoor A (`?node=<IRI>`) | 3 | 🟢 GO | Triviale toevoeging |
| K3 | Versie-aanduiding in beide | 3 | 🟢 GO | Voorkomt versie-mismatch |
| K4 | Spoor-A-export parameterizable | 3 | 🟢 GO | Eén script, twee outputs |
| P1 | Embedded link (B → A per concept) | 3 | 🟢 GO | Eenvoudigste koppeling |
| P2 | Read-API (Spoor A server) | 3 | 🟡 HOLD-Spoor-C | Server-laag botst met huidig statisch |
| P3 | Gedeelde data-laag (Patroon C) | 3 | 🟢 GO (= B7) | Wordt door B7 al gedaan |
| P4 | Bidirectional sync | 3 | 🔴 NO-GO | Organisatie-data-extern-risico |
| P5 | Iframe / micro-frontend | 3 | 🔴 NO-GO | Schendt twee-producten-discipline |
| P6 | Sidecar Spoor A → Spoor B | 3 | 🟡 HOLD | Niet als prio |

**Drie rode draden over de hele analyse:**

1. **Voor Spoor A zit de meeste waarde in formalisering** — niet in nieuwe libraries. Bouwsteen A (versie-templating), B (render-conventies), E (pre-sprint-protocol) zijn discipline-werk dat geen architectuurbeslissing vraagt en de Dashboard-cyclus per release vergemakkelijkt. H40 (renderdekking) blijft de grote latente UI-modernisering die als afzonderlijke sprint behandeld moet worden, met C (data-driven framework-config) en I (on-demand fetch) als voorbereiding.

2. **Voor Spoor B is de architectuurbeslissing-volgorde belangrijker dan de tooling-keuze.** Drie vragen (Q-M1, Q-M2, Q-M5) zijn blokkerend voor verantwoorde bouwsteen-selectie. Eenmaal beantwoord is de set robuust en niet-controversieel: SQL.js + Chart.js + audit-trail + import-pijplijn vormen het kritieke pad; NLDS is de grootste hefboom voor UI-Rijksoverheid-passing; WCAG (axe-core) is verplichting vanaf dag 1.

3. **Voor de koppeling A↔B zijn vier geen-spijt-keuzes nu uitvoerbaar zonder een specifiek patroon te kiezen.** IRI-veld in B, deep-link in A, versie-aanduiding in beide, parameterizable export — alle vier los uitvoerbaar, alle vier openen latere koppel-opties. Bidirectional sync (P4), iframe-vermenging (P5), Spoor-A-bidirectional-richting (N1/N2) zijn expliciet NO-GO uit principes-handhaving, niet uit techniek-onmogelijkheid.

**Wat ik bewust niet aanbeveel:** een grote-bang-modernisering van Spoor A, een green-field-herstart van Spoor B zonder eerst Q-M1..Q-M5 te beantwoorden, of een specifiek koppel-patroon (P1–P6) te bouwen vóór Spoor B operationeel is. Forced-recommendation is hier de verleiding — de eerlijke uitkomst is dat **eerst architectuur-vragen beantwoord moeten worden, dan pas tooling**.

---

## 7. Concrete vervolgstappen

Gegroepeerd naar tijdshorizon + besluit-vereiste.

### 7.1 Onmiddellijk (geen impact, geen besluit nodig)

1. **Bouwsteen A (versie-templating uit DATA.meta)** — onderdeel van eerstvolgende Dashboard-cyclus; nul-risico, dekt zes hardcoded plekken per release.
2. **Bouwsteen B (render-conventies-document)** — Brein-cyclus-werk; onafhankelijk uitvoerbaar; eventueel parallel aan Bouwsteen E voor consistente discipline-laag.
3. **K1 (IRI-veld in toekomstige Spoor-B-tabellen reserveren)** — geen huidige actie, wel ontwerp-discipline-aantekening voor Spoor B.
4. **K2 (deep-link support in Spoor A)** — 30 regels JS toevoegen aan Verkenner-tab; geen architectuurbeslissing.
5. **Vragen Q-D1..Q-D7 + Q-M1..Q-M6 terugleggen bij respectievelijk Dashboard-chat en masterchat** — dit rapport heeft 13 onbeantwoorde vragen; veel aanbevelingen worden scherper of verdwijnen pas na deze ronde.

### 7.2 Korte termijn (besluit nodig, dan uitvoerbaar)

6. **Q-M2-besluit "v3-2 in repo of lokaal?"** — herbevestigen of intrekken van 27-mei-locatie-besluit. Direct effect op Spoor-B-bouwsteen-selectie.
7. **Q-M1-besluit "tech-stack hard of zacht?"** — bepaalt of PWA/Electron/NLDS-overweging in scope is.
8. **Q-M5-besluit "lokaal-draaibaar strict of soepel in prototype?"** — bepaalt CDN-/vendor-keuze.
9. **Bouwsteen E (Protocol 18 of annex bij Protocol 1)** — uitwerken pre-sprint-explorer-update-checklist; masterchat-aanvulling sprint-protocollen.
10. **Bouwsteen J (frontend-design skill in Dashboard-subagent)** — `skills:`-veld in dashboard.md preloaden; geen architectuur-impact, voorbereidt H40.

### 7.3 Middellange termijn (afhankelijk van eerdere besluiten)

11. **UI-mini-sprint A+C+J (versie-templating + data-driven config + frontend-design-prep)** — gebundeld vóór H40-activering; één Dashboard-sprint die de explorer "release-vriendelijk" maakt.
12. **Bouwsteen F (skill `/dashboard-build`)** — ná Bouwsteen E (protocol-checklist eerst, dan automatisering).
13. **Bouwsteen D (visuele regressie Playwright)** — ná Q-D6 (subagent-render-capaciteit) en Q-D3 (huidige regressie-bewustzijn); start klein (Tab 1+2 pixel-diff), schaal naar Tab 3.
14. **Spoor-B-bouwfase** (B1+B2+B3+B7 als kritiek-pad; B4/B5/B6 als operationele uitbouw; B8/B9 als kwaliteit-laag; B11 als sluit-discipline) — afhankelijk van B0/B0b/B0c-besluiten.
15. **K3 + K4 (versie-aanduiding in beide; export parameterizable)** — uitvoerbaar zodra Spoor B-bouw start.
16. **H40-activering (UI-renderdekking)** — eigen sprint, in stappen (inventarisatie velden / per-veld-prioriteit / UI-component-keuze / performance-impact-test); Bouwsteen I (on-demand fetch) is dan ontwerp-overweging.

### 7.4 Bewust niet nu (gemotiveerd uitstellen)

17. **Cytoscape-alternatief (Sigma.js)** — geen schaal-pijn aangetoond; heroverwegen bij H33 of A↔B-koppeling met groot dataset.
18. **Bidirectional sync (P4)** — fundamenteel organisatie-data-extern-risico; alleen heroverwegen bij interne git-on-prem + heldere annotatie-scheiding.
19. **Eén UI voor beide producten (P5)** — schendt productlijnen-concept; geen activatie-trigger denkbaar.
20. **Externe GRC-OS-tooling direct gebruiken** — Sushegaad/GRCEngClub/mlunato47/euCann: methodologisch referentie, geen drop-in.
21. **Server-laag bovenop Spoor A (P2 read-API)** — past bij Spoor C, niet bij huidige fase.
22. **Spoor-B-multi-user / auth-laag** — productie-fase-vraag, niet prototype.

---

## 8. Werkstroom-status na deze analyse

| Item | Status |
|---|---|
| Dashboard-landschap-analyse Spoor A + B + koppeling | ✓ afgerond (dit rapport) |
| Iets daadwerkelijk geactiveerd/gebouwd | ✗ geen — Analyse-deliverable, geen Dashboard-/ontologie-actie |
| Beantwoorde vragen | 0 van 13 (Q-D1..Q-D7 + Q-M1..Q-M6) — vragen-ronde pending |
| Vergelijk met voorganger-rapport (28-05) | ✓ — dit rapport vult de dashboard-lacune in §0–§N van voorganger (waar dashboard onder-belicht was) |
| Nieuwe kandidaat-H-items | **H42-kandidaat:** SKOS-distributie-visualisatie in explorer (T1/T2/T3 hebben distributie verschoven; explorer toont geen onderscheid). Koppelen aan H40 of als sub-H. **H43-kandidaat:** versie-templating-discipline voor explorer-HTML (Bouwsteen A) — als formele conventie. **H44-kandidaat:** Spoor-A↔Spoor-B-koppel-architectuur (P1+P3+K1..K4) — als formeel architectuur-vraagstuk wanneer Spoor B operationeel wordt |
| Bestaande H-items geraakt | **H40** (UI-renderdekking) — directe trigger-context aangereikt; **H33** (m11 SP800-53 uitbreiding) — herinnerd als groei-trigger voor Cytoscape-heroverweging |
| Architectuurbesluiten nodig (masterchat) | **B0** Spoor-B-locatie (Q-M2); **B0b** tech-stack hard/zacht (Q-M1); **B0c** lokaal-draaibaar prototype-versie (Q-M5); **Q-M3** Cytoscape-architectuur in Spoor B; **Q-M4** H40-trigger-status |
| Brain-vault-update-suggestie | Dit rapport opnemen als `brain__scope__dashboard-landschap-2026-05-28.md` of opsplitsen naar: `brain__concepts__spoor-a-discipline.md` (Bouwsteen-A+B+E) + `brain__concepts__spoor-b-architectuur.md` (Bouwsteen B0..B11 + O1..O6) + `brain__concepts__koppeling-spoor-ab.md` (P1..P6 + K1..K4). Splitsing vraagt Brein-cyclus + masterchat-besluit; opnemen-als-monoliet kan ook |
| Invarianten geraakt | Lokaal-draaibaar (P2 server-laag, P4 sync); D9 framework-neutraliteit (P4 bidirectional, P5 iframe-mengeling, N1 Spoor-B-data-in-A); twee-producten-discipline uit productlijnen-concept (P5); NEN-discipline (geen verbatim ISO in dashboard-output — geen specifieke trigger in deze analyse maar bouwsteen-B-skills moeten dit blijven respecteren); geen-organisatienaam (Bouwsteen plugin/overdracht: K9-aandacht); geen-autonome-commit (dit rapport zelf wordt niet door Analyse-chat gecommit) |
| Vragen-bijlage status | 13 vragen open (7 Q-D, 6 Q-M); aanbevelingen gemarkeerd met conditional-afhankelijkheid; vervolg-ronde nodig om uit "informed assessment" naar "praktijk-gevoede aanbeveling" te komen |
| Volgende stap | **Steven** stelt Q-D-vragen aan Dashboard-chat (Claude Code) en Q-M-vragen aan masterchat; antwoorden verwerken in herziene Analyse-deliverable (v2) of direct in masterchat-architectuurbesluit-traject |

---

*Einde rapport — drie sub-vragen (Spoor A + Spoor B + koppeling) gedekt, alle domeinen A–G geadresseerd, 13 vragen expliciet teruggelegd. Dit is een Analyse-chat-deliverable: geen sprint-mutatie, geen ontologie-impact, geen architectuurbesluit. Alle aanbevelingen — met name de drie blokkerende vragen Q-M1/Q-M2/Q-M5 voor Spoor B — gaan naar de masterchat. Conform commit-push-werkverdeling (28-05-2026) commit de Analyse-chat niet zelfstandig; Steven inspecteert het rapport en commit handmatig indien akkoord.*
