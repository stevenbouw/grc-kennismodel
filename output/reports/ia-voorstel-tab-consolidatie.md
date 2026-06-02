# IA-voorstel — Tab-consolidatie Spoor B-dashboard (5 → 4)

**Van:** Dashboard-subagent (Claude Code)
**Voor:** masterchat (via Steven)
**Datum:** 2026-05-29
**Status:** voorstel — **architectuur-/IA-besluit, NIET uitgevoerd.** Vereist masterchat-GO vóór bouw.
**Aanleiding:** tijdens de Overzicht-reskin-sprint bleek de instructie-§2 een tab-structuur ("Overzicht · Per perspectief · Risico's · Controls · Verantwoordelijkheid") te veronderstellen die niet overeenkomt met het feitelijke `grc-dashboard-v3-2.html` ("Overzicht · Governance · Risk · Compliance · ISMS"). Projecteigenaar opperde tabs te combineren. Dit document maakt dat concreet als beslis-stuk; het is bewust losgekoppeld van de reskin (die is een visuele ingreep, dit is een informatie-architectuur-ingreep die functionaliteit raakt).

---

## 1. Huidige structuur (5 tabs)

| Tab | Inhoud (huidig) | Render-functies (JS) |
|---|---|---|
| **Overzicht** | (gereskind) KPI's, mate-van-toepassing, risico's, status per kader, controls | `renderOverzicht` (demo-data) |
| **Governance** | Rollen & RACI · Organisatiestructuur · Documenthiërarchie · Governance per framework | `renderRollen`, `renderRaci`, `renderGovModel`, `renderDocs` |
| **Risk** | Risicoregister · heatmap 5×5 · behandelingsverdeling · risicobereidheid (radar) · framework-koppelingen | `renderRisicos`, `renderHeatmap`, `c-radar`, `c-treat` |
| **Compliance** | Status per framework · ISO/BIO/NIST-tellingen · implementatiegrafieken | `renderControls`, compliance-KPI's, `c-comp-*` |
| **ISMS** | SoA (Statement of Applicability) · PDCA · auditbevindingen · kalender · NC | `renderSoA`, `renderFindings`, `renderKalender`, `renderNC` |

## 2. Voorgestelde structuur (Overzicht + 3 domein-tabs)

Op basis van het voorstel van de projecteigenaar:

| Nieuw tab | Bundelt | Sub-views (binnen tab) |
|---|---|---|
| **Overzicht** | (ongewijzigd — entry-point) | — |
| **Governance** | huidige Governance **+ ISMS** | Rollen/verantwoordelijkheden (RACI) · Beleids-/documentstructuur · Organisatiestructuur · ISMS (SoA, PDCA, directiebeoordeling) · perspectief-wissel per kader |
| **Compliance** | huidige Compliance **+ controls/dekkingsgraad** | Controls & implementatiestatus · dekkingsgraad per kader · verantwoordelijkheid (control-eigenaar) · auditbevindingen/NC · perspectief-wissel per kader |
| **Risk** | huidige Risk | Risicoregister · heatmap · behandeling · risicobereidheid · kalender van risico-acties |

"Verschillende perspectieven" = een **view-keuze per kader** binnen een tab (BIO 2.0 primair, andere kaders gelijkwaardig oproepbaar) — conform D9 (framework-neutraal, view-keuze ≠ architectuur-hiërarchie). Geen aparte tab per kader.

## 3. Mapping van bestaande functionaliteit (niets verliezen)

| Huidige functie | Nieuwe locatie |
|---|---|
| `renderRollen` / `renderRaci` / `renderGovModel` / `renderDocs` | Governance |
| `renderSoA` / `renderFindings` / `renderNC` | ISMS → **Governance** (SoA/PDCA) en deels **Compliance** (NC's bij controls) — keuze aan masterchat |
| `renderKalender` | Risk of Governance (acties) — keuze aan masterchat |
| `renderControls` + compliance-KPI's + `c-comp-*` | Compliance |
| `renderRisicos` / `renderHeatmap` / `c-radar` / `c-treat` | Risk |

## 4. Impact & risico

- **Functioneel, niet cosmetisch:** dit verplaatst CRUD-views, audit-trail-koppelingen en charts tussen tabs; raakt `goTab`/`iTab`-navigatie, de inner-tab (`itab`/`ipanel`)-structuur en mogelijk de bron-toggle. Hoger regressierisico dan een reskin.
- **ISMS-tab verdwijnt** als top-level → de SoA (kern-ISMS-artefact, ISO 27001) wordt een sub-view; vereist zorgvuldige herplaatsing zodat hij vindbaar blijft.
- **NC's/auditbevindingen** zitten semantisch tussen ISMS en Compliance — splitsing of dubbele ingang nodig.
- **D9-bewaking:** perspectief-wissel mag geen kader-hiërarchie introduceren.
- **Spoor A/B-grens** blijft: geen graaf in deze tabs.

## 5. Aanbeveling

Aparte **IA-sprint** ná masterchat-GO, met als deliverables: (1) definitieve 4-tab-mapping inclusief de open keuzes uit §3, (2) navigatie-/inner-tab-herinrichting, (3) regressietest op alle CRUD-paden + axe-herverificatie. Niet meeliften op een reskin-sprint.

**Beslispunten voor masterchat:**
1. Akkoord met Overzicht + 3 domein-tabs (Governance/Compliance/Risk)?
2. Waar landen SoA/PDCA, NC's en kalender (§3)?
3. Perspectief-wissel als view-keuze binnen tab (D9) — akkoord?
4. Aparte IA-sprint of gefaseerd?
