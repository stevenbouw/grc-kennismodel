# Patch-rapport — IA-herinrichting Spoor B-dashboard (4 tabs + kader-kiezer)

**Subagent:** Dashboard (Claude Code)
**Sprint-instructie:** `docs/instructies/instructie-dashboard-ia-herinrichting.md` (masterchat, 2 juni 2026)
**Uitgevoerd:** 3 juni 2026
**Doel-artefact:** `dashboard/grc-dashboard-v3-2.html` (Spoor B — operationele werkmap)
**Aard:** functionele informatie-architectuur-ingreep (geen reskin). Verwerkt het IA-voorstel `output/reports/ia-voorstel-tab-consolidatie.md`.
**Status:** opgeleverd — **commit door Steven** (subagent committeert nooit zelf).

---

## 0. Samenvatting

Van 5 naar **4 tabs** (Overzicht · Governance · Compliance · Risk). De losse ISMS-tab is opgeheven; zijn inhoud is verhuisd. Elke domein-tab (Governance, Compliance) heeft een **gelaagde kader-kiezer** (perspectief-wissel, D9-conform — geen hiërarchie). Reskin-thema, design-tokens, contrast-ramp en offline-vendoring zijn niet aangeraakt. SQL.js-datalaag, bron-toggle, verse-load, DB-import/export en ontologie-structuur-import behouden.

De structurele verhuizing is uitgevoerd via een geverifieerde transform (div-balans, dup-ID-check, alle JS-getargete ID's exact één keer aanwezig), daarna handmatig de nav, kader-kiezer (CSS+JS) en a11y-fixes. Render-functies bleven ongewijzigd: ze targeten dezelfde ID's, die mee-verhuisden met hun DOM-subtree.

---

## 1. Doelstructuur (gerealiseerd)

| Tab | Inner-tabs (na herinrichting) |
|---|---|
| **Overzicht** | (ongewijzigd — entry-point) |
| **Governance** | Rollen & RACI · Organisatiestructuur · Documenten · **ISMS-overkoepelend** · **SoA** · **Kalender** · **Kader-perspectief** |
| **Compliance** | Overzicht · Beheersmaatregelen · Audit & Bevindingen (incl. **NC-register**) · **Kader-perspectief** |
| **Risk** | Risicocontext · Risicoregister · Heatmap · Ontologie-lens (ongewijzigd) |

## 2. Verhuizingen (niets verloren)

| Inhoud | Van → Naar | Render-fn / ID's (ongewijzigd) |
|---|---|---|
| PDCA · ISMS-scope · KRI/KPI · directiebeoordeling | ISMS-tab → **Governance / ISMS-overkoepelend** | `c-kri`, `kri-tb`, `isms-soa-cnt` |
| Statement of Applicability | Compliance → **Governance / SoA** (prominent, vindbaar) | `renderSoA` → `soa-tb`, `sf-soa*` |
| Compliancekalender | Compliance → **Governance / Kalender** | `renderKalender` → `kal-tl`, `sf-kal*` |
| NC-register & corrigerende maatregelen | ISMS-tab → **Compliance / Audit & Bevindingen** | `renderNC` → `nc-tb` |
| Rollen/RACI/structuur/documenten | (blijft) Governance | `renderRollen/Raci/GovModel/Docs` |
| Controls + dekkingsgraad + status per framework | (blijft) Compliance | `renderControls`, `comp-*-cnt`, `c-comp-impl` |
| Risicoregister/heatmap/behandeling/bereidheid | (blijft) Risk | `renderRisicos/Heatmap`, `c-radar/c-treat` |

**SoA-vindbaarheid (kritiek):** geverifieerd als prominente eigen inner-tab onder Governance (`gov-soa`), 23 rijen gerenderd.

## 3. Kader-kiezer (perspectief-wissel, D9-hard)

Per domein-tab een chip-rij + detailpaneel (`renderKaderKiezers` / `selKader`). Geselecteerd kader bepaalt het getoonde perspectief; geen enkel kader heeft architecturale voorrang. Subregel expliciet: "perspectief-keuze — alle kaders gelijkwaardig (D9)".

- **Governance-kiezer (Laag 0+1, 5 kaders):** COSO ICF · COSO ERM · COBIT 2019 · BVA-stelsel · CIO-stelsel.
- **Compliance-kiezer (Laag 2–5, 15 kaders):** BIO 2.0 **(standaard, Rijksbaseline)** · ISO/IEC 27001:2022 · 27002:2022 · 27005:2024 · ISO 22301:2019 · 22313:2020 · NIS2 · VIR 2007 · VIRBI 2025 · AVG/GDPR · CBW · Cbb · NIST SP 800-53 R5 · NIST CSF 2.0 · ENSIA.
- **Statusdiscipline (hard):** CBW chip+detail = "in voorbereiding"; Cbb = "concept · Tweede Kamer". **DORA verschijnt NIET in de Compliance-kiezer** (referentiekader n.v.t. — geverifieerd). Geen BBN als BIO-eigenschap.
- ISO 27005/31000 + NIST 800-30/39 blijven als risico-methodologie in de Risk-tab (Framework-koppelingen-blok behouden); ISO 27005 staat tevens als norm-referentie in de Compliance-kiezer.

Chips zijn `<button>` met `aria-pressed`; toetsenbord-bedienbaar; `:focus-visible`.

---

## 4. Verificatie (blokkerend — instructie §5)

Geautomatiseerd via headless Chrome + axe-core + SQL.js-DB-introspectie.

### 4.1 CRUD-regressiematrix (alle modals, na verhuizing)

| Entiteit | Openen | Opslaan | Verwijderen |
|---|---|---|---|
| Risico | ✓ | ✓ | ✓ |
| Control | ✓ | ✓ | ✓ |
| Rol | ✓ | ✓ | ✓ |
| Document | ✓ | ✓ | ✓ |
| Bevinding | ✓ | ✓ | ✓ |
| Kalender | ✓ | ✓ | ✓ |

Elke `+`-knop (ook de verhuisde) opent de juiste modal; opslaan voegt een rij toe en re-rendert; verwijderen verwijdert correct.

**Pre-existing bug gevonden & gefixt (vereist voor werkende delete):** `modalDelete()` riep `closeModal()` (die `modalState={}` reset) vóór de toast-regel `modalState.record.id` → crash, geen `renderAll()`. Onafhankelijk van deze IA-ingreep, maar blokkerend voor de §5-deletetest. Minimaal gefixt door id/record/table vóór `closeModal()` in lokale variabelen te bewaren.

### 4.2 Navigatie
- 4 top-tabs schakelen correct (`goTab`); ISMS-tab verwijderd, geen verwijzingen naar verdwenen tab.
- Alle 15 inner-tabs (`iTab`): geen dode/ontbrekende panelen.
- Bron-toggle (`wStruct`/`wOper` via `setBron`): werkt na verhuizing.

### 4.3 axe — **0 over alle tabs + inner-tab/kiezer-states**

| Tab | Violations (alle inner-tab-states) |
|---|---|
| Overzicht | **0** |
| Governance (7 inner-tabs, incl. kader-kiezer) | **0** |
| Compliance (4 inner-tabs, incl. kader-kiezer) | **0** |
| Risk (4 inner-tabs) | **0** |
| **Totaal** | **0** |

Ruleset `wcag2a + wcag2aa + wcag21a + wcag21aa + best-practice`. **a11y-fixes deze sprint** (latente issues, blootgelegd door de grondige per-inner-tab-scan):
- 9 filter-`<select>`-elementen zonder toegankelijke naam → `aria-label` toegevoegd.
- Risk-heatmap: score-tekst had `opacity:.7` op 9px → contrast onder AA op de getinte cellen; vervangen door volle 11px-tekst; witte (onzichtbare) celranden op licht thema → donker.

*Transparantienoot:* tijdens actieve CRUD verschijnt kort een "Verwijderd/Aangemaakt"-toast (live-region, position-fixed). Die toast kan tijdens de ~3s dat hij toont een color-contrast-hit geven; na uitklaren is de steady-state 0. De toast is pre-existing en niet door deze sprint geïntroduceerd; alle tab-/inner-tab-/kiezer-states zelf zijn 0.

### 4.4 Offline
- Runtime network-interceptie: **0 requests buiten `127.0.0.1`** (alle assets lokaal).
- Statisch: geen externe `src`/`href`/`@import`. Geen page-/console-errors.

### 4.5 JS-syntax
`node --check` op het inline-script: valide.

---

## 5. Gewijzigd bestand + SHA256

| Bestand | Status | SHA256 |
|---|---|---|
| `dashboard/grc-dashboard-v3-2.html` | gewijzigd (2051 → 2139 regels) | `6cb0d3405fc79100bdaf6217afc4d3881094f1e13daf9fe744ac60c53c4f8c8a` |
| `output/reports/patch-rapport-dashboard-ia-herinrichting.md` | nieuw (dit rapport) | — |

**Gewijzigde secties in de HTML:**
- Nav: 5 → 4 ntabs (Overzicht · Governance · Compliance · Risk; ISMS verwijderd).
- Governance-tab: inav 4 → 7 inner-tabs; nieuwe panelen `gov-isms` (uit ISMS), `gov-soa` (uit comp-soa), `gov-kal` (uit comp-kal), `gov-kader` (kiezer + per-framework-tabel).
- Compliance-tab: inav 5 → 4 inner-tabs; `comp-soa` en `comp-kal` verwijderd (verhuisd); NC-register toegevoegd aan `comp-audit`; nieuw `comp-kader` (kiezer).
- ISMS-tab: volledig verwijderd (inhoud herverdeeld).
- CSS: `.kz-*` kader-kiezer-blok; heatmap-celranden.
- JS: `KADER_INFO` + `selKader` + `renderKaderKiezers` (gewired in `renderAll`); 9× `aria-label`; heatmap-tekst/rand-fix; `modalDelete`-bugfix.

`git status`: ` M dashboard/grc-dashboard-v3-2.html`. **Niet gecommit** — Steven inspecteert `git status`/`git diff` en commit handmatig.

---

## 6. Protocol 18 — pre-sprint-dashboard-update-checklist

Deze sprint raakt **geen build-script** en geen nieuwe ontologie-baseline; het is een UI/IA-ingreep op demo-data. Checklist:

| # | Vraag | Antwoord |
|---|---|---|
| 1 | Gewijzigde modules in baseline? | n.v.t. — geen ontologie-mutatie |
| 2 | Nieuwe namespaces? | Nee |
| 3 | Nieuwe properties met SKOS-impact? | Nee |
| 4 | Nieuwe Laag? | Nee (de kader-kiezer ordent bestaande kaders naar de bekende lagen 0–5) |
| 5 | Nieuw framework-individual? | Nee — kiezer toont bestaande kaders (demo-data) |
| 6 | Build-script-bump nodig? | **Nee** — geen build-script aangeraakt |
| 7 | SKOS-meetlaag | n.v.t. |

**Conclusie:** baseline-databron synchroon (v4.6.4, ongewijzigd). Geen Protocol 18-blokkade.

---

## 7. Scope-discipline (instructie §7)

Het door masterchat vastgestelde ontwerp is gevolgd; geen autonome IA-keuzes. Geen scope-pauze nodig — geen onwerkbare kiezer-keuze of onverwacht hoge regressie-impact (de modal-/render-laag bleef intact; alleen DOM-herparentering + één pre-existing deletebug). Buiten de instructie-scope bewust **niet** gewijzigd: reskin-thema, tokens, contrast-ramp, offline-vendoring, Risk-tab-inhoud (m.u.v. de axe-verplichte heatmap-contrastfix).

## 8. Aandachtspunten voor masterchat-review

1. **Governance heeft nu 7 inner-tabs** — de inav scrollt horizontaal. Werkbaar, maar een latere sprint kan SoA/Kalender/ISMS desgewenst groeperen.
2. **NC-register** staat onder Compliance / Audit & Bevindingen, met expliciete vermelding "ingang ook vanuit Governance · ISMS-overkoepelend" (conform §3); een echte tweede ingang vanuit Governance kan later als deep-link.
3. **modalDelete-bugfix** is een correctie buiten de IA-scope maar noodzakelijk voor de §5-deletetest — graag bevestigen bij review.
4. Kader-kiezer-detailinhoud is representatieve demo-data; geen organisatiedata, geen organisatienaam.
