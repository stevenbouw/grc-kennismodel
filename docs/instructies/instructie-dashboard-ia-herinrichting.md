# Instructie — IA-herinrichting Spoor B-dashboard (tabs + kader-kiezer)

**Van:** masterchat
**Voor:** Dashboard-subagent (Claude Code)
**Datum:** 2 juni 2026
**Doel-artefact:** `dashboard/grc-dashboard-v3-2.html` (Spoor B, operationele werkmap)
**Status:** sprint-instructie — uitvoeren, opleveren; commit door Steven (subagent commit nooit zelf)
**Aard:** **functionele informatie-architectuur-ingreep, GEEN reskin.** Hoger regressierisico
dan de vorige sprint. Reken op iteratie.

---

## 0. Context en aanleiding

Het gereskinde dashboard heeft nu 5 tabs (Overzicht · Governance · Risk · Compliance ·
ISMS). De projecteigenaar wil dat álle relevante normenkaders ontsloten zijn — niet
alleen de kaders op het Overzicht, maar ook ISO 27005/31000/22301/22313, VIRBI, BVA-
stelsel, CIO-stelsel, COSO, COBIT, NIST CSF, ENSIA, enz.

**Niet via een tab-per-kader** — dat zou de tab-balk vervuilen én een framework-
hiërarchie introduceren die D9 (framework-neutraliteit) schendt. **Wel via een
perspectief/kader-kiezer binnen de relevante domein-tab.** Dit verwerkt tegelijk het
IA-voorstel `output/reports/ia-voorstel-tab-consolidatie.md` (masterchat-besluit:
Overzicht + 3 domein-tabs).

---

## 1. Doelstructuur: Overzicht + 3 domein-tabs

Van 5 tabs naar **4**: Overzicht · Governance · Compliance · Risk. De huidige losse
ISMS-tab verdwijnt als top-level; zijn inhoud verhuist (zie §3).

```
Overzicht   — samenvatting (entry-point)
Governance  — governance-kaders + ISMS-overkoepelend + SoA + kalender
Compliance  — operationele/normen-kaders + controls + dekkingsgraad + audit/NC
Risk        — risicoregister + heatmap + behandeling + bereidheid + risico-norm-koppelingen
```

---

## 2. De kader-kiezer — gelaagd, NIET universeel (D9-hard)

Elke domein-tab krijgt een **kader-kiezer** (view-switch) die de frameworks toont die
bij die laag van het normenkader horen. De kiezer is een *perspectief-wissel*, geen
hiërarchie: het geselecteerde kader bepaalt de getoonde view, maar geen enkel kader
heeft architecturaal voorrang. BIO 2.0 is standaard geselecteerd in Compliance (het
operationeel primaire perspectief), maar elk ander kader is één klik gelijkwaardig
oproepbaar. Toon dit expliciet met een subregel in de geest van "perspectief-keuze —
alle kaders gelijkwaardig; BIO 2.0 standaard als Rijksbaseline".

**Governance-tab kiezer (Laag 0 + Laag 1):**
COSO ICF · COSO ERM · COBIT 2019 · BVA-stelsel · CIO-stelsel

**Compliance-tab kiezer (Laag 2 + Laag 3 + Laag 4 + Laag 5):**
BIO 2.0 (standaard) · ISO/IEC 27001:2022 · ISO/IEC 27002:2022 · ISO/IEC 27005:2024\*
· ISO 22301:2019 · ISO 22313:2020 · NIS2 · VIR 2007 · VIRBI 2025 · AVG/GDPR
· CBW (in voorbereiding) · Cbb (concept t.b.v. Tweede Kamer) · NIST SP 800-53 R5
· NIST CSF 2.0 · ENSIA

\* ISO 27005/31000 en NIST 800-30/39 zijn risico-methodologie en surfacen primair in
de **Risk-tab** (zie §2.1), niet als nalevingsverplichting in Compliance. ISO 27005
mag in Compliance als norm-referentie verschijnen, maar de risico-methode-context
hoort in Risk.

### 2.1 Risk-tab — risico-norm-koppelingen blijven waar ze horen
De bestaande Risk-tab heeft al een "Framework-koppelingen risicobeheer"-blok (ISO
27005:2024, ISO 31000:2018, NIST 800-30, NIS2 Art.21(a), BIO 2.0 5.07). Behoud dit;
breid desgewenst uit met NIST 800-39. Géén aparte kader-kiezer nodig in Risk tenzij
het natuurlijk past — risicomethoden zijn context, geen nalevings-perspectief.

### 2.2 Statusdiscipline in de kiezer (hard)
- **CBW** altijd "in voorbereiding"; **Cbb** altijd "concept t.b.v. Tweede Kamer".
- **DORA** is referentiekader (n.v.t.) — verschijnt NIET in de Compliance-kiezer als
  na te leven kader (al gecorrigeerd in de vorige ronde; niet terugdraaien).
- Geen BBN als BIO 2.0-eigenschap (BBN komt uit de Handreiking; hier niet relevant).

---

## 3. Verhuizing bestaande functionaliteit (niets verliezen)

| Huidige functie / inhoud | Nieuwe locatie |
|---|---|
| `renderRollen` / `renderRaci` / `renderGovModel` / `renderDocs` | **Governance** |
| ISMS-inhoud: PDCA, ISMS-scope, KRI/KPI, directiebeoordeling | **Governance** (ISMS-overkoepelend, sub-view) |
| `renderSoA` (Statement of Applicability) | **Governance** (ISMS-overkoepelend sturingsdocument — masterchat-besluit) |
| `renderControls` + compliance-KPI's + dekkingsgraad | **Compliance** |
| `renderFindings` / `renderNC` (audit & non-conformiteiten) | **Compliance**, bij de controls waarop ze betrekking hebben; ingang vanuit Governance behouden |
| `renderKalender` (compliancekalender) | **Governance** (governance-acties/deadlines — masterchat-besluit) |
| `renderRisicos` / `renderHeatmap` / `c-radar` / `c-treat` | **Risk** (ongewijzigd) |

**SoA-vindbaarheid (kritiek):** de SoA is het kern-ISMS-artefact (ISO 27001). Bij het
verdwijnen van de ISMS-top-level-tab MOET de SoA prominent en vindbaar blijven onder
Governance — niet weggestopt in een sub-sub-view.

---

## 4. Harde grenzen (ongewijzigd)

- **Reskin-thema, tokens, contrast-ramp, offline-vendoring: niet aanraken.** Deze
  sprint verhuist en herstructureert; het visuele thema uit de vorige sprint blijft.
- **Spoor A/B-grens (Q-M3):** geen Cytoscape, geen ontologie-graaf, geen netwerk-
  visualisatie. Grafieken (verdeling/staaf/lijn op echte data) mogen.
- **Alleen demo-data; geen organisatienaam; volledig offline** (geen CDN/externe fonts).
- **D9:** kader-kiezer = view-switch, nooit hiërarchie.
- Behoud SQL.js-datalaag, bron-toggle (`wStruct`/`wOper`), verse-load-flow, DB
  import/export, ontologie-structuur-import.

---

## 5. Verificatie (blokkerend)

Dit is een functionele herinrichting — regressie is het hoofdrisico:

- **Regressietest op ALLE CRUD-paden:** elke modal (risico/control/rol/document/
  bevinding/kalender) opent, slaat op, verwijdert en bewaart correct ná de verhuizing.
  Rapporteer per entiteit: open ✓ / opslaan ✓ / verwijderen ✓.
- **Navigatie:** `goTab`/`iTab` werken voor de nieuwe 4-tab-structuur + alle inner-tabs;
  geen dode panelen, geen knooppunten die naar verdwenen tabs verwijzen.
- **Bron-toggle** (`wStruct`/`wOper`) werkt nog op alle verplaatste views.
- **SoA vindbaar** onder Governance, getest.
- **axe = 0** over alle 4 tabs + alle inner-tabs/kiezer-states. Rapporteer per tab.
- **Offline:** 0 externe requests (runtime + statisch).
- **JS-syntax valide** (`node --check`).

---

## 6. Oplevering

- Geherstructureerd `grc-dashboard-v3-2.html`.
- Patch-rapport met: regressie-matrix (CRUD per entiteit), axe per tab, offline-
  bevestiging, lijst gewijzigde regels/secties + SHA256, correcte datum.
- **Commit door Steven.** Subagent commit niet zelf.
- Protocol 18-checklist vóór start.

## 7. Scope-discipline

Dit ontwerp is vastgesteld door masterchat. Wijk je af (bv. een functie past
natuurlijker elders, of een kader-kiezer-keuze blijkt onwerkbaar): **pauzeer en
escaleer met Optie A/B/C naar Steven** — beslis niet zelf over IA. Bij onverwacht
hoge regressie-impact op een CRUD-pad: stop, rapporteer, vraag GO.
