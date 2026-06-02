# Instructie — Dashboard-reskin Overzicht (Spoor B)

**Van:** masterchat
**Voor:** Dashboard-subagent (Claude Code)
**Datum:** 2 juni 2026
**Doel-artefact:** `grc-dashboard-v3-2.html` (Spoor B, operationele werkmap)
**Status:** sprint-instructie — uitvoeren, opleveren; commit door Steven (subagent commit nooit zelf)

---

## 0. Context en grens

Aanleiding: er komt een CSO/CISO-scharniermoment; de operationele werkmap moet
visueel naar een demo-klaar niveau. Een ontwerp is gemaakt in Claude Design (alleen
als visuele referentie — NIET als bron-code overnemen; het bevat vervuilde,
dichtgeknepen HTML en meegelifte externe fonts). De waarde zit in (a) de
bijgeleverde design-tokens en (b) deze instructie.

**Harde grenzen:**
- Dit is een **reskin van het bestaande v3-2-skelet**, geen herbouw (Q-M1: zacht
  voortbouwen op v3.x). Behoud de SQL.js-datalaag, de offline-vendoring
  (`dashboard/vendor/`), en de verse-load-flow.
- **Spoor A/B-scheiding blijft hard (Q-M3):** GEEN Cytoscape, GEEN ontologie-graaf,
  GEEN netwerk-visualisatie in dit dashboard. Grafieken (verdeling, staaf, lijn op
  echte historische metingen) mogen; ontologie-grafen horen in `grc-explorer`
  (Spoor A).
- **Alleen representatieve demo-data.** Geen organisatiedata. Geen organisatienaam.
- **Volledig offline.** Geen CDN, geen externe fonts, geen externe icon-libraries.

---

## 1. Design-tokens (bron van waarheid)

Gebruik het losse bestand `design-tokens-grc-dashboard.css` (naast deze instructie
in `docs/instructies/`). Kopieer het ongewijzigd naar de dashboard-structuur (bv.
`dashboard/design-tokens-grc-dashboard.css`) en importeer/embed het. **Neem de
hex-waarden niet over uit proza — gebruik het bestand letterlijk**, om afwijkingen
te voorkomen.

**Ramp-besluit (masterchat):** gebruik **`[data-ramp="contrast"]` als standaard**,
niet de "aards"-ramp. Reden: WCAG 2.1 AA. De aards-`--c-warn` (#9a6410) zakt op de
getinte oppervlakken (`--surface-2`, `--bg`) net onder 4,5:1; de contrast-`--c-warn`
(#7a4e08) blijft ruim boven AA. Zet dus `data-ramp="contrast"` op `<html>`.

**Typografie:** koppen `--font-head` (Georgia-serif-stack, offline-veilig), UI
`--font-body` (system-ui-stack). Geen externe fonts laden.

---

## 2. Layout — Overzicht-tab (de scope van deze sprint)

Vijf tabs blijven: Overzicht · Per perspectief · Risico's · Controls ·
Verantwoordelijkheid. Deze sprint werkt **alleen het Overzicht-tab** volledig uit;
de andere vier tabs blijven functioneel zoals ze zijn (worden in latere sprints
gereskind).

Overzicht-tab, van boven naar onder:

1. **Kop:** "Overzicht" (serif), subregel "Naleving, openstaande risico's en
   verantwoordelijkheid van de organisatie — in één blik." Rechtsboven: badge
   "representatieve demo-data" + "bijgewerkt <datum>".

2. **KPI-tegelrij (4 tegels)** — variant **A · vlak getint**. Tegels: controls
   toegepast (71/93, "76% van de baseline"), openstaande risico's (8, "waarvan 3
   hoog"), urgente acties (5, "deadline < 30 dagen"), controls zonder eigenaar (4,
   "verantwoordelijkheid open"). Cijfers in serif. Status-kleur op het cijfer waar
   betekenisvol (risico's crit, urgent warn), niet op de tegel-achtergrond.

3. **Twee panelen naast elkaar:**
   - *Mate van toepassing* — **donut + legenda** (variant A) als primair. Categorieën
     toegepast / deels toegepast / niet toegepast / uitgesloten (met motivering) +
     exacte aantallen. **Fallback-eis:** als het aantal controls in scope laag is
     (richtgetal < ~15), val terug op de 100%-staaf-variant — een donut met enkele
     segmenten is onleesbaar. Bouw beide, schakel op datavolume.
   - *Openstaande risico's* — lijst gesorteerd op urgentie (hoog/middel/laag), kleur
     + label + icoon (nooit kleur alleen).

4. **Status per kader** — variant **A · tabel (pattern a)**. Kolommen: kader /
   status / mate van toepassing (balk + %) / open risico's (met "x hoog"-annotatie)
   / eigenaar. BIO 2.0 met "primair"-badge bovenaan, andere kaders gelijkwaardig
   eronder. Subregel rechtsboven: "BIO 2.0 is het primaire perspectief — andere
   kaders zijn gelijkwaardig oproepbaar" (D9-view-discipline, geen architectuur-
   hiërarchie). "niet belegd" in crit-kleur.

5. **Controls die aandacht vragen** — tabel, gesorteerd op urgentie. Kolommen:
   control / domein / eigenaar / status. Status met kleur + label.

---

## 3. Drill-down-architectuur (masterchat-besluit)

Verdieping (grafieken, detail) komt **NIET als losse tabbladen**, maar als
**drill-down vanuit bestaande elementen**:
- Klik op een kader-rij in "Status per kader" → verdiepingsweergave voor dat kader.
- Klik op een risico / heatmap-cel (Risico's-tab) → de onderliggende risico's.

Deze sprint hoeft de drill-down nog niet vol te bouwen; leg de **structuur/hook**
aan (klikbare rijen die naar een detailweergave kunnen routeren) zodat latere
sprints de verdieping invullen. Geen ontologie-grafen (Spoor A-grens).

**Inhoudelijke grens bij alle toekomstige grafieken:** het dashboard TOONT
uitkomsten, het BEREKENT niet. Trendlijnen alleen op echte historische metingen,
geen voorspelling. Een eventuele risk-heatmap (Risico's-tab) positioneert
handmatig gescoorde risico's en moet dat expliciet labelen — het dashboard scoort
zelf geen risico's.

---

## 4. Toegankelijkheid (verplicht, blokkerend voor demo)

- Eindresultaat **axe-clean (0 bevindingen)** — net als de vorige B9-ronde
  (47→0). Voer axe uit en rapporteer het resultaat in het patch-rapport.
- Status nooit op kleur alleen: altijd kleur + label (+ icoon waar passend).
- Focus-states zichtbaar (`--focus`).
- Met de contrast-ramp als standaard moet `--c-warn`-tekst op `--surface-2` en
  `--bg` boven 4,5:1 zitten — verifieer dit expliciet, niet op het oog.

---

## 5. Oplevering

- Gereskind `grc-dashboard-v3-2.html` + `design-tokens-grc-dashboard.css` in de
  dashboard-structuur.
- Patch-rapport met: axe-resultaat (0), bevestiging offline-werking (geen externe
  requests), bevestiging contrast-ramp-default, lijst gewijzigde bestanden + SHA256.
- **Commit door Steven** — lever op, commit niet zelf (`.claude/settings.json`-deny
  blijft van kracht). Steven inspecteert `git status`/`git diff` en commit handmatig.
- Protocol 18 (pre-sprint-dashboard-update-checklist): bevestig vóór start dat de
  dashboard-databron synchroon is met de actuele baseline.
