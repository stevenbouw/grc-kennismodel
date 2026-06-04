---
type: concept
title: Spoor B-revival — B7/Q-M5/B9 (29 mei) + v7-laag reskin/DORA-correctie/IA-herinrichting (2–3 juni)
status: living
date: 2026-06-04
related:
  - dashboard-productlijnen
  - H40_dashboard-ui-renderdekking
  - skos-export-filter
sources:
  - dashboard-tussenrapport-b7-wiring-2026-05-29
  - dashboard-rapport-qm5-vendoring-b9-wcag-2026-05-29
  - besluitnotitie-qm-dashboard-2026-05-29
  - patch-rapport-dashboard-reskin-overzicht
  - patch-rapport-dashboard-ia-herinrichting
  - ia-voorstel-tab-consolidatie
  - instructie-dashboard-reskin-overzicht
  - instructie-dashboard-ia-herinrichting
  - design-tokens-grc-dashboard
chat-sources: []
confidence: high
---

# Spoor B-revival — grc-dashboard-v3-2 operationeel prototype (29 mei → 3 juni 2026)

## Wat het is

Het Spoor B-prototype (`dashboard/grc-dashboard-v3-2.html`, de operationele werkmap — zie [[brain__concepts__dashboard-productlijnen]]) is in twee opeenvolgende werkstromen gerevitaliseerd:

- **Iteratie-16-werkstroom (29 mei 2026):** B7-wiring + bron-split 1A + Q-M5 vendoring + B9 WCAG 47→0 — drie opeenvolgende, **niet-architecturale** verbeteringen onder de Q-M-besluiten.
- **v7-werkstroom (2–3 juni 2026):** reskin Overzicht + warm-papier-thema + DORA-correctie + IA-herinrichting (5→4 tabs + gelaagde kader-kiezer) — een gerichte CSO/CISO-demo-voorbereiding na een Claude-Design-referentieontwerp.

Beide werkstromen raken uitsluitend laad-bron, presentatie of wiring — geen organisatie-data, geen ontologie-mutatie. De ontologie-baseline blijft v4.6.4 ongewijzigd; dit is puur Spoor B / dashboard-werk.

**Brein-registratie alleen** — de dashboard-code is dashboard-subagent-werkgebied en is door Brein niet aangeraakt.

> **Brein-oordeel over registratie-vorm:** dit is géén ontologie-sprint (geen TBox/ABox/SKOS-mutatie, baseline-metrics niet geraakt). Het past daarom niet als `brain__sprints__v*`-bestand maar als concept-entry, parallel aan hoe iteratie 15 `cross-category-mappings` als concept registreerde i.p.v. als sprint. De bron-besluiten en de v7-IA-keuzes zijn masterchat-besluiten; Brein legt ze vast, interpreteert ze niet. De v7-werkstroom is wél als sessie-entry opgenomen in het sprint-register (chronologische vindbaarheid).

## De drie revival-componenten

| Component | Inhoud | Bron-rapport |
|---|---|---|
| **B7 — ontologie-structuur-import + bron-split 1A** | Header-knop "⬇ Ontologie-import" → kolom-migratie (`migreerStructuurKolommen()`, idempotent, non-destructief: verwijderde IRI → `orphan=1`, nooit hard-delete) → import van 316 controls / 52 frameworks / 20 rollen. **Bron-split 1A** (zie hieronder): twee expliciete helpers `wStruct()` (structuurlaag → ontologie canoniek) en `wOper()` (operationele laag → hand-seed primair), expliciet per query aangebracht. K3-header toont "· ontologie-structuur v4.6.0 · SKOS-status t/m v4.6.3". Kernregressie-bevestiging: compliance-% blijft de hand-seed-waarde (35%), níét ~0% na import | `dashboard-tussenrapport-b7-wiring-2026-05-29.md` |
| **Q-M5 — lokaal vendoren** | Third-party assets lokaal gevendord naar `dashboard/vendor/` voor offline werking (Rijksoverheid-machine kan CDN blokkeren): Chart.js 4.4.1 + sql.js 1.12.0 (`.js` + `.wasm`) + IBM Plex fonts (36× woff2). SRI-integrity op de script-tags (matcht cdnjs exact). Offline-verificatie (Playwright, alle niet-localhost geblokkeerd): 0 geblokkeerde/mislukte requests, 0 console-errors | `dashboard-rapport-qm5-vendoring-b9-wcag-2026-05-29.md` |
| **B9 — WCAG 2.1 AA-audit + fixes** | axe-core-scan over 5 nav-tabs: **47 → 0** bevindingen (2 critical `select-name` + 45 serious, w.v. 44 `color-contrast` + 1 `scrollable-region-focusable`). Fixes: `aria-label` op 2 selects, `--text4`-token `#4d5358` → `#9097a0` (≥4.54:1), status-pill-kleuren, font-floor 9/10px → 12px / 11px, `tabindex=0`+`role=region` op scroll-containers. Alle fixes in één gemarkeerd override-blok (reviewbaar/reverteerbaar); layout intact, geen regressie | `dashboard-rapport-qm5-vendoring-b9-wcag-2026-05-29.md` |

Alle drie raken uitsluitend laad-bron (Q-M5), presentatie (B9) of wiring (B7) — geen organisatie-data, geen ontologie-mutatie. Disclosure-check op v3-2: geen organisatienaam (alleen generieke roltitels/kaders); framework-neutraal (D9, geen kader bevoorrecht); geen Cytoscape in Spoor B (Q-M3).

## De drie Spoor B-bron-besluiten (één samenhangend pakket — masterchat)

De B7-wiring is het sluitstuk van drie opeenvolgende masterchat-bron-laag-besluiten. Het B7-tussenrapport §6 markeert ze expliciet als "het 3e bron-laag-besluit … als één samenhangend pakket vastleggen in de Brein-cyclus":

| # | Besluit | Inhoud |
|---|---|---|
| **Optie A** | bron-import | Het dashboard importeert de ontologie-**structuur** (frameworks, controls, rollen) als canonieke structuurlaag — niet de operationele status |
| **Optie 1** | co-existentie | De geïmporteerde ontologie-structuurlaag en de bestaande hand-seed-operationele laag **co-existeren** naast elkaar; import is non-destructief voor de hand-seed-laag |
| **1A** | bron-split | De twee lagen worden **expliciet per query** gescheiden via `wStruct()` (structuur → ontologie canoniek) en `wOper()` (operationeel → hand-seed primair); nergens stilzwijgend. Bij divergerende aantallen (316 structuur vs 23 operationeel) labelt de UI per teller ("· structuur" / "· operationele SoA" / "X van Y operationeel beoordeeld") zodat de CSO het niet als inconsistentie leest |

Deze split is de Spoor B-tegenhanger van de Spoor A meet-laag-discipline (ontologie-laag vs export-laag, zie [[brain__concepts__skos-export-filter]]): twee bewust gescheiden datalagen met expliciete labeling i.p.v. één vermengde telling.

## Twee bekende vervolgpunten (geen H-items — bekend-vervolgpunt)

Twee aandachtspunten zijn in de rapporten gemeld als bekend vervolg. Conform Brein-discipline declareer ik hiervoor **geen nieuw H-item** zonder masterchat (de masterchat-benoemde dashboard-kandidaten zijn H42/H43/H44 — zie [[brain__architecture__H-register]]); ze staan hier als bekend-vervolgpunt + in de open-punten-lijst van het brein-rapport iteratie 16:

| # | Vervolgpunt | Detail + fix-richting |
|---|---|---|
| 1 | **`file://`-laadgedrag** | Bij dubbelklik (`file://`) faalt het WASM-laden → "DB fout". Werkt wél via `python3 -m http.server`. **Demo-risico:** een bestuurder die het bestand dubbelklikt ziet een fout. Fix-richting: base64-embedded WASM, of een duidelijke foutmelding-met-instructie ("serveer via http.server / open via de meegeleverde launcher") |
| 2 | **`herkomst`-kolom bij verse load** | Vóór de eerste ontologie-import bestaat de `herkomst`-kolom nog niet (wordt toegevoegd door `migreerStructuurKolommen()` binnen de import) → `wOper()` verwijst dan naar een niet-bestaande kolom → compliance toont "—" i.p.v. %. **Pre-existing B7-gedrag**, niet door Q-M5/B9 veroorzaakt. Fix-richting: kolom-migratie ook in `laadSeedData()` draaien |

## Verifieer-/demo-discipline

Beide rapporten benadrukken een **menselijke visuele pass vóór een CSO/CISO-demo** (de subagent kon de live browser-render in de eigen omgeving niet end-to-end draaien — Chrome/puppeteer-launch-incompatibiliteit, geen codeprobleem; B9 is wél via Playwright met eigen Chromium gedraaid). Serveren via `python3 -m http.server` (relatieve paden + SRI werken zo correct); offline-check via DevTools → Network → Offline.

## v7-werkstroom — reskin + DORA-correctie + IA-herinrichting (2–3 juni 2026)

Drie opeenvolgende deel-ingrepen door de Dashboard-subagent onder masterchat-instructie, gericht op een naderend CSO/CISO-scharniermoment. Geen ontologie-mutatie; baseline blijft v4.6.4. Werkstroom officieel **niet in een eerdere Brein-cyclus verwerkt** — iteratie 17 dicht die geheugen-lag (zie [[brain__log]] iteratie 17 + lag-leerpunt onderaan).

### v7-1 — Reskin Overzicht (2 juni 2026)

| Aspect | Detail |
|---|---|
| Doel | Demo-klaar visueel niveau, warm-papier licht thema o.b.v. aangeleverde design-tokens |
| Tokens-bestand | `dashboard/design-tokens-grc-dashboard.css` (nieuw, ongewijzigd gekopieerd uit `docs/instructies/`) |
| Ramp-default | `data-ramp="contrast"` op `<html>` (WCAG 2.1 AA-onderbouwing: `--c-warn` #7a4e08 ≥4,5:1 op getinte oppervlakken; ratio's: 6,42 op `--surface-2`, 6,53 op `--bg`, 5,81 op canvas. De "aards"-variant `#9a6410` haalt 4,46/4,54 — net onder/op de grens) |
| Typografie | Koppen `--font-head` (Georgia-serif-stack), UI `--font-body` (system-ui-stack); geen externe fonts |
| Overzicht-tab herbouwd | KPI-tegelrij (4 tegels: 71/93 toegepast · 8 risico's w.v. 3 hoog · 5 urgente acties · 4 zonder eigenaar), donut + 100%-staaf-fallback (Mate van toepassing), risico-lijst, Status-per-kader-tabel (BIO 2.0 "primair"-badge bovenaan), Controls-die-aandacht-vragen-tabel |
| a11y | axe 0 over alle vijf tabs (eerste run 15 best-practice-items → structureel opgelost: `<main>`-landmark, `role="banner"`/`role="navigation"`, persistente visueel-verborgen `<h1>`, `:focus-visible` via `--focus`) |
| Offline | 0 externe requests; offline-vendoring (`dashboard/vendor/`), SQL.js-datalaag, verse-load-flow ongemoeid |

**Twee vooraf geautoriseerde scope-afwijkingen** (door subagent geëscaleerd naar Steven, door Steven geautoriseerd):

| # | Instructie zei | Besluit | Gevolg |
|---|---|---|---|
| A | "alleen Overzicht reskinnen; andere vier tabs blijven zoals ze zijn" | **Hele dashboard licht** | Lichte tokens globaal toegepast op alle 5 tabs; alleen Overzicht inhoudelijk herbouwd, overige vier behouden inhoud/functionaliteit (alleen thema gewijzigd) |
| B | §2 noemt tabs "Overzicht · Per perspectief · Risico's · Controls · Verantwoordelijkheid" | **Tab-consolidatie (5→3) doorgeschoven als IA-besluit naar masterchat** | Huidige 5 tabs (Overzicht/Governance/Risk/Compliance/ISMS) intact gelaten; IA-voorstel apart opgeleverd in `output/reports/ia-voorstel-tab-consolidatie.md`. Masterchat besloot uiteindelijk Overzicht + 3 domein-tabs (zie v7-3) |

### v7-2 — DORA-correctie (2 juni 2026)

**Aanleiding:** DORA verscheen op meerdere plekken in het dashboard als actief, bindend kader — op het Overzicht zelfs als meest kritieke kader ("kritiek, 38%, niet belegd"). Feitelijk onjuist: de organisatie valt **niet** onder DORA; DORA is uitsluitend **referentiekader · n.v.t.** Dit is consistent met het model — m12 DORA staat als referentie, geen bindende verplichting. Chirurgische correctie, geen andere wijzigingen.

| Plek | Wijziging |
|---|---|
| `DEMO_OVERZICHT.kaders` (Overzicht) | DORA-regel volledig verwijderd. Overzicht toont nu 5 kaders: BIO 2.0, ISO/IEC 27001, NIS2/Cyberbeveiligingswet, NIST SP 800-53 R5, AVG/GDPR |
| Seed-`frameworks` | DORA `bindend` 1→0; extra `UPDATE … SET bindend=0,toepasselijk=0,notitie='Referentiekader — niet van toepassing …'` |
| Governance-tab ("Governance-controls per framework") | DORA-rij gemarkeerd `referentie — n.v.t.`; kernverplichting-tekst + verantw. rol → "—" |
| Compliance-tab ("Status per framework") | DORA-rij niet langer getrackt; status-tellingen vervangen door referentie-tekst; deadline → n.v.t. |
| Kalender-seed `KAL-05` | DORA Art.6 → "ICT-risicobeoordeling (oriëntatie op DORA-good practice) / Intern — DORA als referentie (n.v.t.)"; eigenaar CIO→CISO |
| Framework-detail-metadata `dora.bind` (dormant) | "Verplicht voor financiële entiteiten" → "Referentiekader — niet van toepassing op deze organisatie" |

**Bewust behouden als referentie:** SoA-tabel-kolom "DORA" + control-`dora_ref`-velden + modal-formulierveld "DORA-referentie" blijven — dit zijn **cross-reference-mappings**, geen bindingsclaims. Consistent met m12 DORA als referentie-kader.

### v7-3 — IA-herinrichting (3 juni 2026)

**Van 5 naar 4 tabs:** Overzicht · Governance · Compliance · Risk. De losse ISMS-tab is opgeheven; inhoud herverdeeld. Verwerkt het IA-voorstel uit v7-1 (masterchat-besluit Overzicht + 3 domein-tabs).

| Inhoud | Van → Naar |
|---|---|
| PDCA · ISMS-scope · KRI/KPI · directiebeoordeling | ISMS-tab → Governance / ISMS-overkoepelend |
| Statement of Applicability (SoA) | Compliance → **Governance / SoA** (prominent vindbaar; SoA = kern-ISMS-artefact ISO 27001) |
| Compliancekalender | Compliance → Governance / Kalender |
| NC-register & corrigerende maatregelen | ISMS-tab → Compliance / Audit & Bevindingen |
| Rollen/RACI/structuur/documenten | (blijft) Governance |
| Controls + dekkingsgraad + status per framework | (blijft) Compliance |
| Risicoregister/heatmap/behandeling/bereidheid | (blijft) Risk |

**Gelaagde kader-kiezer** (perspectief-wissel, **D9-hard — geen hiërarchie**) — kernkenmerk van deze IA-ronde:

| Tab | Lagen | Kaders |
|---|---|---|
| Governance-kiezer | Laag 0 + Laag 1 | COSO ICF · COSO ERM · COBIT 2019 · BVA-stelsel · CIO-stelsel (5 kaders) |
| Compliance-kiezer | Laag 2 + Laag 3 + Laag 4 + Laag 5 | BIO 2.0 *(standaard, Rijksbaseline)* · ISO/IEC 27001:2022 · 27002:2022 · 27005:2024 · ISO 22301:2019 · 22313:2020 · NIS2 · VIR 2007 · VIRBI 2025 · AVG/GDPR · CBW · Cbb · NIST SP 800-53 R5 · NIST CSF 2.0 · ENSIA (15 kaders) |
| Risk | (geen aparte kiezer) | ISO 27005/31000 + NIST 800-30/39 blijven als risico-methodologie (Framework-koppelingen-blok behouden) |

**Statusdiscipline (hard, consistent met always-on invarianten):**

- CBW chip+detail = **"in voorbereiding"**
- Cbb = **"concept · Tweede Kamer"**
- **DORA verschijnt NIET in de Compliance-kiezer** (referentiekader n.v.t. — gecorrigeerd in v7-2; niet terugdraaien)
- Geen BBN als BIO 2.0-eigenschap (BBN komt uit de Handreiking; zie [[brain__concepts__bbn-correctie]])

**Kader-kiezer is een D9-conform perspectief-mechanisme** — chips zijn `<button>` met `aria-pressed`, toetsenbord-bedienbaar, expliciete subregel "perspectief-keuze — alle kaders gelijkwaardig (D9); BIO 2.0 standaard als Rijksbaseline". Geen enkel kader heeft architecturale voorrang; BIO 2.0 is operationeel-primair als view-keuze, geen hiërarchie. Zie [[brain__decisions__D09_framework-neutraliteit]] + [[brain__concepts__framework-neutraliteit]].

**Verificatie:** axe 0 over alle 4 tabs + alle inner-tabs/kiezer-states; CRUD-regressiematrix groen voor risico/control/rol/document/bevinding/kalender (open/opslaan/verwijderen); offline 0 externe requests; JS-syntax valide. a11y-fixes in deze sprint: 9× `aria-label` op filter-`<select>`-elementen; Risk-heatmap score-tekst-contrast + celranden gefixt.

**Pre-existing bug gefixt (buiten IA-scope, gemeld):** `modalDelete()` riep `closeModal()` (die `modalState={}` reset) vóór de toast-regel `modalState.record.id` → crash, geen `renderAll()`. Minimaal gefixt door id/record/table vóór `closeModal()` in lokale variabelen te bewaren. Noodzakelijk voor de §5-deletetest van de regressie-matrix; door subagent expliciet aan masterchat-review voorgelegd.

## Twee OPEN besluiten na de v7-werkstroom

De v7-werkstroom heeft het dashboard structureel demo-klaar gemaakt (IA + thema + DORA-positionering), maar **twee inhoudelijke besluiten staan open** en zijn cruciaal voor de volgende fase. Iteratie 17 legt deze expliciet vast als open items.

### Besluit 1 — Lege-huls-kernprobleem (Pad 1 vs Pad 2) — gekoppeld aan H40

**Probleem:** de gelaagde kader-kiezer toont placeholders i.p.v. echte controls/beschrijvingen/eisen. Klik op een kader → geen onderliggende controls, geen beschrijvingen van beheersmaatregelen, geen eis-teksten waaraan voldaan moet worden. **De structuur staat, de inhoud leeft niet.** Die inhoud zit in de ontologie, niet in de "dunne" import die het dashboard nu voedt.

| Pad | Inhoud | Kosten/baten | Aanbeveling in bronrapport |
|---|---|---|---|
| **Pad 1 — vanuit de ontologie** | Ontologie-export verrijken (control → beschrijving + eis + framework-koppeling) → via build-script naar dashboard | Architecturaal zuiver; raakt drie lagen (ontologie → export → dashboard-import); kost meer tijd; opvolging-werk voor latere fase | Opvolging |
| **Pad 2 — demo-seed verrijken** | Voor demo-relevante kaders (BIO 2.0, ISO 27001/27002) een representatieve control-set mét beschrijving + eis-tekst in de demo-seed | Snel, demo-klaar; raakt geen ontologie; geen architectuur-impact | **Nu (geadviseerd)** |

**Relatie tot H40:** [[brain__architecture__H40_dashboard-ui-renderdekking]] gaat over render-dekking van de **Spoor A explorer-UI** (Cytoscape-graaf rendert <10% van JSON-velden). Het lege-huls-probleem is een **aangrenzend maar distinct vraagstuk** in **Spoor B** (dashboard): niet "rendert de UI alles wat in de export zit", maar "bevat de dashboard-databron überhaupt de control-detail-content". H40-scope-afbakening (Spoor A only, zie H40 §"Scope-afbakening") blijft hard.

**Brein-oordeel:** geen nieuw H-item declareren (Brein-discipline; nieuwe H-items zijn masterchat-werk). Het lege-huls-probleem staat **bij H40 in de status-historie als aangrenzend Spoor-B-vraagstuk** opgenomen en blijft hier als open besluit in dit concept-bestand. Bij masterchat-besluit (Pad 1 vs Pad 2) kan een nieuw H-item alsnog overwogen worden — of het kan als sprint-scope landen zonder formeel H-nummer.

### Besluit 2 — Organisatiestructuur in dashboard (A/B/C) — gekoppeld aan H29 + CIO/BVA-stelsels

**Probleem:** de eigenaar wil dat het dashboard de realistische IV-organisatiestructuur weerspiegelt (een leverende, provider-consumer IV-organisatie met functionele afdelingen: integratie-/business-services, generieke voorzieningen, datacenter-services, bedrijfsvoering, technologie/CTO-office, directieondersteuning, en interne beheersing als tweede/derde lijn met auditfunctie). Drie opties, te kiezen:

| Optie | Inhoud | Risico | Discipline-impact |
|---|---|---|---|
| **A — generiek/demo** | Volledig generieke/abstracte functionele structuur | Veiligst; geen disclosure-risico | Conform §0.5-firewall + always-on invariant "organisatienaam NOOIT" |
| **B — echte functionele structuur, geanonimiseerd** | Realistische functionele afdelingen zonder organisatie-identiteit | Laag — geanonimiseerd; geen organisatienaam | **Geadviseerd in bronrapport** — waardevol modelwerk, geen disclosure-schending mits strikt geanonimiseerd |
| **C — volledig echt** | Echte organisatiestructuur, herkenbaar | Hoog — raakt §0.5-/disclosure-discipline; combinatie echte structuur + security-posture is gevoelig | Alleen als bewust vastgelegd masterchat-besluit; raakt Cat. 1 (organisatie-naam) van Protocol 14 |

**Relatie tot H29 + CIO/BVA-stelsels:** de interne-beheersingsfunctie sluit direct aan op het **Three Lines Model** (zie [[brain__architecture__H29_three-lines-model]], future-consideration) en de **CIO-stelsel/BVA-stelsel-RACI** (Laag 0+1 governance-kaders, in v7-3 onder Governance-kiezer beschikbaar). Optie B zou realistisch modelwerk leveren voor M04 (roles/RACI) — ongeacht wat finaal in het dashboard belandt.

**Brein-oordeel:** geen nieuw H-item; geen D-decision-aanraking; wachten op masterchat-besluit. Optie C raakt de §0.5-autonomie-firewall en de always-on invariant "organisatienaam wordt NOOIT genoemd" — Brein adviseert geen Optie C zonder expliciet masterchat-besluit met scope-pauze-route.

## v7-handover-artefacten (cross-sessie context)

| Artefact | Pad | Rol |
|---|---|---|
| **Overdrachtsrapport** *(actueel)* | `docs/handovers/overdrachtsrapport.md` | Volledig zelfstandig startpunt voor opvolgend beheerder; §5.3-5.5 beschrijven v7-dashboardspoor + de twee open besluiten |
| **Bootstrap-masterchat-v7** *(actueel)* | `docs/handovers/bootstrap-masterchat-v7.md` | Actuele Master-startprompt; verwijst naar overdrachtsrapport.md; STAP 3-bevestiging noemt v7-stand + lege-huls + organisatiestructuur als open besluiten |

Beide vervangen de eerdere v6-sessie-rapport-lijn. De brain-vault (deze file + sprint-register + log + index) blijft autoritatief boven beide handover-artefacten.

## Hangt samen met

- [[brain__concepts__dashboard-productlijnen]] — Spoor A vs Spoor B; Q-M-besluiten + Q-M2-reversal; v7-stand 4 tabs + kader-kiezer
- [[brain__architecture__H40_dashboard-ui-renderdekking]] — Spoor A render-dekking (Q-M4 latent/parked); kandidaten H42/H43/H44 masterchat-benoemd; lege-huls-aangrenzing iteratie 17 (Spoor B)
- [[brain__architecture__H29_three-lines-model]] — future-consideration; organisatiestructuur-besluit (Optie B levert M04 RACI-/structuur-modelwerk)
- [[brain__concepts__skos-export-filter]] — Spoor A meet-laag-analogie van de bron-split
- [[brain__concepts__framework-neutraliteit]] — D9 als fundament van de kader-kiezer (perspectief-wissel, geen hiërarchie)
- [[brain__decisions__D09_framework-neutraliteit]] — D9-decision waar de kader-kiezer expliciet aan voldoet
- [[brain__concepts__bbn-correctie]] — BBN niet als BIO-eigenschap in de kader-kiezer (statusdiscipline-bevestiging)

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-29 | living | Concept geboren in Brein-cyclus iteratie 16. Legt de Spoor B-revival vast (B7-wiring + bron-split 1A + Q-M5 vendoring + B9 WCAG 47→0), de drie Spoor B-bron-besluiten (Optie A · Optie 1 · 1A) als één pakket, en twee bekende vervolgpunten (`file://`-laadgedrag + `herkomst`-kolom verse load). Brein-registratie alleen; dashboard-code niet aangeraakt. |
| 2026-06-04 | living | **Iteratie 17 — v7-werkstroom (2–3 juni 2026) vastgelegd**: (1) reskin Overzicht-tab + warm-papier-thema o.b.v. nieuwe `dashboard/design-tokens-grc-dashboard.css`; `data-ramp="contrast"` als default met WCAG-AA-onderbouwing; twee vooraf geautoriseerde scope-afwijkingen (hele dashboard licht; tab-consolidatie doorgeschoven als IA-besluit); (2) DORA-correctie — overal verwijderd als actief/bindend kader → "referentiekader · n.v.t.", consistent met m12; SoA-kolom + `dora_ref`-cross-reference-velden bewust behouden; (3) IA-herinrichting 5→4 tabs (Overzicht · Governance · Compliance · Risk); ISMS-tab opgeheven, inhoud herverdeeld; **gelaagde kader-kiezer** (perspectief-wissel, D9-hard; Governance 5 kaders Laag 0+1, Compliance 15 kaders Laag 2-5; DORA niet in kiezer; CBW "in voorbereiding"; Cbb "concept"); risico-methodologie-normen (ISO 27005/31000, NIST 800-30/39) blijven in Risk; pre-existing `modalDelete`-bug gefixt buiten IA-scope. **Twee OPEN besluiten** expliciet vastgelegd: lege-huls-kernprobleem (Pad 1 ontologie-export verrijken vs Pad 2 demo-seed verrijken — Pad 2 geadviseerd nu, gekoppeld aan H40 als aangrenzend Spoor-B-vraagstuk) + organisatiestructuur (A generiek / B echte functionele structuur geanonimiseerd — geadviseerd / C volledig echt — gevoelig, raakt §0.5-discipline; gekoppeld aan H29 Three Lines Model + CIO/BVA-RACI). v7-handover-artefacten (overdrachtsrapport.md + bootstrap-masterchat-v7.md) genoteerd als actuele opvolgers van de v6-sessie-rapport-lijn. **Lag-leerpunt:** een werksessie zonder afsluitende Brein-cyclus creëert een geheugen-lag waar latere lezers over struikelen (tussen iteratie 16 op 29 mei en iteratie 17 op 4 juni liep de vault achter op de werkelijke stand) — Brein-cyclus hoort na elke betekenisvolle sessie, niet alleen na een ontologie-release. |

— Einde spoor-b-revival.
