# Patch-rapport — Dashboard-reskin Overzicht (Spoor B)

**Subagent:** Dashboard (Claude Code)
**Sprint-instructie:** `docs/instructies/instructie-dashboard-reskin-overzicht.md` (masterchat, gedateerd 2 jun 2026)
**Uitgevoerd:** 2026-05-29
**Doel-artefact:** `dashboard/grc-dashboard-v3-2.html` (Spoor B — operationele werkmap)
**Status:** opgeleverd — **commit door Steven** (subagent committeert nooit zelf; `.claude/settings.json`-deny van kracht)

---

## 0. Samenvatting

Reskin van het bestaande `grc-dashboard-v3-2.html` naar een licht "warm-papier"-thema op basis van de aangeleverde design-tokens, met het **Overzicht-tab volledig herbouwd** conform instructie §2. SQL.js-datalaag, offline-vendoring (`dashboard/vendor/`) en de verse-load-flow zijn ongewijzigd behouden. Geen herbouw, geen Cytoscape/ontologie-graaf (Spoor A-grens), geen organisatiedata, volledig offline.

**Twee scope-afwijkingen t.o.v. de letterlijke instructie — vooraf geëscaleerd naar Steven (projecteigenaar) en geautoriseerd:**

| # | Instructie zei | Besluit Steven | Gevolg |
|---|---|---|---|
| A | "alleen Overzicht reskinnen; andere vier tabs blijven zoals ze zijn" | **Hele dashboard licht** | Lichte tokens globaal toegepast op alle 5 tabs; alleen Overzicht inhoudelijk herbouwd, overige vier behouden hun inhoud/functionaliteit (alleen thema gewijzigd) |
| B | §2 noemt tabs "Overzicht · Per perspectief · Risico's · Controls · Verantwoordelijkheid" | **Tab-consolidatie (5→3) is IA-besluit → naar masterchat** | Huidige 5 tabs (Overzicht/Governance/Risk/Compliance/ISMS) intact gelaten; IA-voorstel apart opgeleverd: `output/reports/ia-voorstel-tab-consolidatie.md` |

---

## 1. Verificatie (blokkerend — instructie §4/§5)

### 1.1 axe — eindresultaat **0 bevindingen**

Headless Chrome + `axe-core` 4.x, ruleset `wcag2a + wcag2aa + wcag21a + wcag21aa + best-practice`, gescand over **alle vijf tabs** (het hele dashboard werd licht, dus alle tabs geverifieerd):

| Tab | Violations |
|---|---|
| Overzicht | **0** |
| Governance | **0** |
| Risk | **0** |
| Compliance | **0** |
| ISMS | **0** |
| **Totaal** | **0** |

Stabiliteit bevestigd: Overzicht 3× herhaald = 0. Geen console-/page-errors.

**Tussenstap (transparantie):** een eerste run gaf 15 bevindingen — 14 best-practice (ontbrekende `main`-landmark, `region`, `page-has-heading-one`) + 1 transient `color-contrast` op de Compliance-iteratie die in latere runs niet reproduceerde (een seed-`toast`/chart-init-race tijdens de sequentiële scan, geen stabiele DOM-fout). De best-practice-items zijn structureel opgelost (zie §2.4); daarna 0 over alle tabs.

### 1.2 Offline-werking — **geen externe requests**

- Statisch: geen externe `src`/`href`, geen `@import`/`url(http…)`. Enige `https://…`-strings zijn ontologie-IRI's (data, geen netwerk).
- Runtime: network-interceptie in headless Chrome → **0 requests buiten `127.0.0.1`** (alle assets lokaal: `vendor/` chart.umd, sql-wasm(.js/.wasm), fonts, plus de nieuwe lokale token-CSS).

### 1.3 Contrast-ramp default + `--c-warn`-eis

- `data-ramp="contrast"` staat op `<html>` (geverifieerd runtime: `data-ramp=contrast`, `--c-warn` → `#7a4e08`).
- `--c-warn` (#7a4e08) op getinte oppervlakken (expliciet berekend, WCAG-formule):

| Oppervlak | Ratio | Eis ≥4,5:1 |
|---|---|---|
| `--surface-2` (#f4f2ea) | **6,42:1** | ✅ |
| `--bg` (#f5f4ef) | **6,53:1** | ✅ |
| canvas (#e9e7e0) | **5,81:1** | ✅ |

Ter vergelijking: de "aards"-`--c-warn` (#9a6410) haalt 4,46/4,54 — net onder/op de grens, conform de masterchat-onderbouwing voor de contrast-ramp-keuze. Alle tekst- en statuskleuren in de light-palette zijn vooraf op ≥4,5:1 geverifieerd; axe (rendered-contrast) bevestigt 0 contrastfouten.

---

## 2. Wijzigingen

### 2.1 Design-tokens (instructie §1)
`design-tokens-grc-dashboard.css` **ongewijzigd** gekopieerd van `docs/instructies/` naar `dashboard/` (SHA256 identiek, zie §3) en als eerste stylesheet ge-`<link>`d. `data-ramp="contrast"` op `<html>` als standaard.

### 2.2 Hele dashboard licht
Het oorspronkelijke donkere carbon-`:root`-palet is geremapt op de tokens (surfaces licht; `--green/--red/--yellow/--orange/--blue/--cyan/--purple/--teal` → `var(--c-ok/--c-crit/--c-warn/--c-info)` zodat ze de contrast-ramp volgen). Het B9-override-blok is herzien voor licht (badge-tekst → donkere statushue; `--text4` weer donker; focus-`outline` via `--focus`). Chart.js-kleuren (legenda/assen/grid) van donker naar licht omgebogen. Koppen gebruiken `--font-head` (Georgia-stack), UI `--font-body` (system-ui); geen externe fonts.

### 2.3 Overzicht-tab volledig herbouwd (instructie §2) — representatieve demo-data
1. **Kop** "Overzicht" (serif) + subregel + badges "representatieve demo-data" / "bijgewerkt &lt;datum&gt;".
2. **KPI-tegelrij (4) — variant A vlak getint**: controls toegepast 71/93 ("76% van de baseline"), openstaande risico's 8 ("waarvan 3 hoog", cijfer in crit-kleur), urgente acties 5 ("deadline < 30 dagen", warn-kleur), controls zonder eigenaar 4. Cijfers in serif; statuskleur op het cijfer, niet op de tegel.
3. **Mate van toepassing — donut primair (variant A)** met legenda (kleur + label + exact aantal) + **100%-staaf-fallback** (gebouwd; schakelt bij <15 controls in scope). Demo: toegepast 71 / deels 12 / niet 6 / uitgesloten 4 (= 93).
4. **Openstaande risico's** — lijst op urgentie, kleur + label + icoon (nooit kleur alleen).
5. **Status per kader — tabel (pattern a)**: kader / status / mate-van-toepassing (balk + %) / open risico's ("x hoog") / eigenaar. BIO 2.0 met "primair"-badge bovenaan; D9-subregel rechtsboven; "niet belegd" in crit-kleur.
6. **Controls die aandacht vragen** — tabel, status met kleur + label.

### 2.4 Toegankelijkheid (instructie §4)
`<main>`-landmark, `role="banner"` op header, `role="navigation"` op nav, `role="status"`-live-region op toast-stack, persistente visueel-verborgen `<h1>` (paginakop op elk tab); zichtbare Overzicht-kop als `<h2>`. Status overal kleur + label (+ icoon). Drill-down-rijen zijn toetsenbord-bedienbaar (`role="button"`, `tabindex=0`, Enter/Space). `:focus-visible`-outline via `--focus`.

### 2.5 Drill-down-hooks (instructie §3 — hook, niet volbouwen)
Klikbare rijen in "Status per kader" en "Controls die aandacht vragen" routeren naar `ovDrill(type, label)` → opent een detail-placeholder ("wordt in latere sprint ingevuld"). Geen ontologie-graaf (Spoor A-grens). Verdieping zelf bewust niet gebouwd.

### 2.6 Behoud (niet aangeraakt in functionaliteit)
SQL.js-engine, `vendor/`-offline-vendoring, verse-load-flow (`initApp` + `file://`-guard + `migreerStructuurKolommen` bij verse load), DB import/export, bron-toggle, ontologie-structuur-import, en de vier overige tabs (Governance/Risk/Compliance/ISMS — inhoud/CRUD ongewijzigd, alleen licht gethematiseerd). `updateKPIs()` is null-safe gemaakt (de oude `kpi-*`-knooppunten bestaan niet meer op het herbouwde Overzicht); `mkChart` guardde al op ontbrekende canvas.

---

## 3. Gewijzigde/nieuwe bestanden + SHA256

| Bestand | Status | SHA256 |
|---|---|---|
| `dashboard/grc-dashboard-v3-2.html` | gewijzigd (1838 → 2050 regels) | `c283f55b40ef26f7d58be28a45e0856b6e4bcd55fab190dace7a0a9554a82c4f` |
| `dashboard/design-tokens-grc-dashboard.css` | **nieuw** (ongewijzigde kopie uit `docs/instructies/`) | `68c32dd424283d96c45609cd39774102884d864784d0f2898fe3cd74bcc48221` |
| `output/reports/patch-rapport-dashboard-reskin-overzicht.md` | nieuw (dit rapport) | — |
| `output/reports/ia-voorstel-tab-consolidatie.md` | nieuw (IA-voorstel voor masterchat) | — |

`git status`: ` M dashboard/grc-dashboard-v3-2.html` · `?? dashboard/design-tokens-grc-dashboard.css` (+ de twee rapporten). **Niet gecommit** — Steven inspecteert `git status`/`git diff` en commit handmatig.

---

## 4. Protocol 18 — pre-sprint-dashboard-update-checklist

Deze sprint raakt **geen build-script** aan en is een reskin op representatieve demo-data; de trigger ("build-script-aanraking bij nieuwe baseline") is strikt genomen niet geraakt. Checklist niettemin doorlopen:

| # | Vraag | Antwoord / impact |
|---|---|---|
| 1 | Gewijzigde modules in v4.6.4? | Alleen `m21-csf.ttl` (CSF-Tier range-fix) + `grc-core` version-bump — TBox-bugfix. Geen dashboard-impact |
| 2 | Nieuwe namespaces? | Nee |
| 3 | Nieuwe properties met SKOS-impact? | Nee (range-fix, geen predicate-substitutie) |
| 4 | Nieuwe Laag? | Nee |
| 5 | Nieuw framework-individual? | Nee |
| 6 | Build-script-bump nodig? | **Nee** — geen build-script aangeraakt |
| 7 | SKOS-meetlaag | n.v.t. — Overzicht toont demo-data, geen SKOS-export |

**Conclusie:** baseline-databron synchroon. v4.6.4 ≡ v4.6.3 in baseline-metrics (alle Δ=0; bron `output/verification/canonical_metrics_v4_6_4.json`). De dashboard-structuurbron `structure-import-v4_6_0.js` is structureel synchroon: frameworks/controls/rollen-tellingen zijn sinds v4.6.0 onveranderd (T1–T3 + TBox-fix raakten alleen SKOS-mappings resp. één range, niet de structuur). De demo-KPI 71/93 sluit aan op de baseline (`ctrl`-namespace = 93 controls, D8 SoAEntry = 93). Geen Protocol 18-blokkade.

---

## 5. GO-criteria (instructie §5)

- [x] Gereskind `grc-dashboard-v3-2.html` + `design-tokens-grc-dashboard.css` in `dashboard/`
- [x] axe-resultaat **0** (gerapporteerd, alle tabs)
- [x] Offline-werking bevestigd (0 externe requests, runtime + statisch)
- [x] Contrast-ramp-default bevestigd + `--c-warn` >4,5:1 op `--surface-2`/`--bg`
- [x] Gewijzigde bestanden + SHA256
- [x] Protocol 18-checklist
- [x] **Niet gecommit** — commit door Steven
- [x] Scope-afwijkingen (hele-dashboard-licht; tab-consolidatie) vooraf geëscaleerd + geautoriseerd; IA-voorstel apart opgeleverd

---

## 6. Aandachtspunten voor masterchat-review

1. **Hele dashboard licht** is een geautoriseerde afwijking van de geschreven instructie ("andere vier blijven zoals ze zijn"). De vier overige tabs zijn functioneel ongemoeid maar visueel licht; volledige inhoudelijke reskin van die tabs is een latere sprint.
2. **Tab-consolidatie (5→3)** is bewust NIET in deze sprint uitgevoerd — IA-besluit voor masterchat (zie `output/reports/ia-voorstel-tab-consolidatie.md`).
3. **Transitionele staat:** de vier overige tabs gebruiken nog de oude Spoor-B-componentstructuur (carbon-classes, nu licht gethematiseerd via de var-remap). Een latere sprint kan ze op de token-componenten van Overzicht trekken.
4. Drill-down is alleen een **hook**; verdieping (grafieken/detail) volgt in een latere sprint, conform §3.
