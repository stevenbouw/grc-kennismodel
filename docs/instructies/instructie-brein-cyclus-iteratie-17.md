# Instructie — Brein-cyclus iteratie 17 (v7-dashboardlaag officieel maken)

**Voor:** Brein-subagent (Claude Code)
**Van:** Masterchat
**Datum:** 4 juni 2026
**Type:** brain-vault-onderhoud (Protocol 11 — maar achteraf: de sessie was niet brain-verwerkt)
**Commit:** door Steven (Brein committeert nooit zelf)

---

## Aanleiding (lees dit eerst)

Tussen brain-iteratie 16 (29 mei 2026) en nu heeft een **dashboard-werksessie (2–3 juni 2026)** plaatsgevonden die **nooit door een Brein-cyclus is verwerkt**. Daardoor liep de brain-vault (iteratie 16, "geen actieve sprint", dashboard-*revival* B7/Q-M5/B9) achter op de werkelijke stand. `bootstrap-masterchat-v7.md` en `docs/handovers/overdrachtsrapport.md` beschrijven die latere stand al, maar de brain-vault — de gezaghebbende bron — niet. **Deze iteratie 17 dicht die lag.** De ontologie-baseline blijft ongewijzigd v4.6.4 (dit is dashboard-/Spoor-B-werk, geen ontologie-mutatie).

**Leerpunt om expliciet vast te leggen:** een werksessie zonder afsluitende Brein-cyclus creëert een geheugen-lag waar latere lezers over struikelen. Brein-cyclus na elke betekenisvolle sessie (niet alleen na een ontologie-release) voorkomt dit.

---

## Bronnen — lees deze volledig aan de bron (niet op samenvatting vertrouwen)

1. `output/reports/patch-rapport-dashboard-reskin-overzicht.md` — reskin Overzicht + DORA-correctie (2 juni).
2. `output/reports/patch-rapport-dashboard-ia-herinrichting.md` — IA-herinrichting 5→4 tabs + kader-kiezer (3 juni).
3. `output/reports/ia-voorstel-tab-consolidatie.md` — het onderliggende IA-voorstel.
4. `docs/handovers/overdrachtsrapport.md` §5.3/§5.4/§5.5 — de v7-stand + de twee open besluiten.
5. `docs/handovers/bootstrap-masterchat-v7.md` — de actuele Master-startprompt (verwijst naar overdrachtsrapport.md).
6. Bijbehorende instructies (referentie): `docs/instructies/instructie-dashboard-reskin-overzicht.md`, `docs/instructies/instructie-dashboard-ia-herinrichting.md`, `dashboard/design-tokens-grc-dashboard.css`.

---

## Wat iteratie 17 minimaal moet vastleggen

Je bepaalt zelf de precieze bestandsplaatsing (autonomie + kruisverwijzing-bewaking), maar de volgende inhoud moet in de vault landen:

### 1. De v7-dashboardsessie (de drie deel-ingrepen)
Leg de sessie vast — als uitbreiding van `brain__concepts__spoor-b-revival.md` of als nieuw `brain__concepts__`/`brain__sprints__`-bestand, jouw keuze, mits in het sprint-register opgenomen:
- **Reskin Overzicht (2 juni):** warm-papier licht thema o.b.v. `dashboard/design-tokens-grc-dashboard.css` (nieuw bestand); Overzicht-tab herbouwd; `data-ramp="contrast"` als default (WCAG-AA-onderbouwing: `--c-warn` #7a4e08 ≥4,5:1 op getinte oppervlakken; de "aards"-variant haalde net niet); axe 0; offline-vendoring + SQL.js + verse-load ongemoeid. Twee **vooraf geautoriseerde scope-afwijkingen**: (A) hele dashboard licht i.p.v. alleen Overzicht; (B) tab-consolidatie doorgeschoven als IA-besluit naar masterchat.
- **DORA-correctie (2 juni):** DORA overal verwijderd als actief/bindend kader → uitsluitend "referentiekader · n.v.t." (de organisatie valt niet onder DORA). SoA-kolom + `dora_ref`-cross-reference-velden bewust behouden (mappings, geen bindingsclaims). Consistent met het model (m12 DORA = referentie).
- **IA-herinrichting (3 juni):** 5→4 tabs (Overzicht · Governance · Compliance · Risk); ISMS-tab opgeheven, inhoud herverdeeld (PDCA/ISMS-scope/KRI-KPI/directiebeoordeling → Governance/ISMS-overkoepelend; SoA → Governance; Kalender → Governance; NC-register → Compliance/Audit & Bevindingen). **Gelaagde kader-kiezer** (perspectief-wissel, D9-hard, geen hiërarchie): Governance-kiezer 5 kaders (Laag 0+1: COSO ICF/ERM, COBIT 2019, BVA-stelsel, CIO-stelsel); Compliance-kiezer 15 kaders (Laag 2–5: BIO 2.0 standaard, ISO 27001/27002/27005, ISO 22301/22313, NIS2, VIR 2007, VIRBI 2025, AVG, CBW "in voorbereiding", Cbb "concept", NIST 800-53 R5, NIST CSF 2.0, ENSIA). DORA verschijnt NIET in de kiezer. Risico-methodologie-normen (ISO 27005/31000, NIST 800-30/39) blijven in Risk. Pre-existing `modalDelete`-bug gefixt (buiten IA-scope, gemeld). axe 0.

### 2. Open items (cruciaal — deze ontbreken nu volledig in het geheugen)
- **Lege-huls-kernprobleem:** de kader-kiezer toont placeholders i.p.v. echte controls/beschrijvingen/eisen. Open besluit: **Pad 1** (ontologie-export verrijken: control → beschrijving + eis + framework-koppeling → build-script) vs **Pad 2** (demo-seed verrijken voor demo-relevante kaders BIO 2.0 / ISO 27001-27002). Advies in de bron: Pad 2 nu (demo-klaar), Pad 1 als opvolging. Relateer aan **H40** (dashboard-UI-renderdekking) — beoordeel of dit H40 is of een nieuw/aangrenzend H-item; jouw oordeel, leg de keuze vast.
- **Organisatiestructuur in dashboard:** open besluit optie **A** (generiek/demo, veiligst) / **B** (echte functionele structuur, geanonimiseerd — geadviseerd) / **C** (volledig echt, gevoelig; raakt §0.5-/disclosure-discipline). Relateer aan **H29** (Three Lines Model) + CIO/BVA-RACI-stelsels.

### 3. Registers + log + index
- `brain__sprints__sprint-register.md` — sessie-entry toevoegen.
- `brain__concepts__dashboard-productlijnen.md` — Spoor B bijwerken (4-tabs-IA + kader-kiezer + reskin-thema/tokens).
- `brain__architecture__H-register.md` — H40 + lege-huls + organisatiestructuur-besluit verwerken; eventueel nieuwe H-items.
- `brain__log.md` — nieuwe iteratie-17-entry (append-only, nieuwste bovenaan).
- `brain__index.md` — vault-staat-tabel "16 → 17 iteraties"; status-overzicht-sectie aanvullen met de v7-dashboardstand + de twee open besluiten; "Volgende activiteit" bijwerken (lege-huls-besluit is nu de eerste prioriteit, niet "geen actieve sprint").

### 4. Meta
- Leg het lag-leerpunt vast (zie Aanleiding): Brein-cyclus hoort na elke betekenisvolle sessie, niet alleen na een ontologie-release.
- Noteer dat `bootstrap-masterchat-v7.md` + `docs/handovers/overdrachtsrapport.md` de actuele handover-artefacten zijn (opvolgers van de v6-sessie-rapport-lijn).

---

## Wat NIET doen
- **Geen ontologie-claims wijzigen** — baseline blijft v4.6.4, alle metrics ongewijzigd. Dit is puur dashboard-/Spoor-B-historie + open besluiten.
- **Geen D-decisions of sprint-protocollen wijzigen.**
- **Geen organisatienaam**, geen organisatiedata (het dashboard gebruikt representatieve demo-data — leg dat zo vast).
- **Niet zelf committen** — lever op, Steven inspecteert `git status`/`git diff` en commit handmatig.

## GO-criteria
- [ ] v7-dashboardsessie (reskin + DORA-correctie + IA-herinrichting) vastgelegd, met de twee geautoriseerde scope-afwijkingen benoemd
- [ ] Lege-huls-besluit (Pad 1/2) + organisatiestructuur-besluit (A/B/C) als expliciete open items vastgelegd, gekoppeld aan H40 resp. H29
- [ ] DORA-correctie vastgelegd (referentiekader · n.v.t., consistent met m12)
- [ ] Kader-kiezer als D9-conform perspectief-mechanisme beschreven (geen hiërarchie)
- [ ] sprint-register + dashboard-productlijnen + H-register + log + index bijgewerkt
- [ ] Lag-leerpunt + v7-handover-artefacten genoteerd
- [ ] iteratie-stand in `brain__index.md`: 16 → 17
- [ ] Niet gecommit; oplever-rapport met gewijzigde-bestanden-lijst

---

*Einde instructie — Brein-cyclus iteratie 17. Na uitvoering + commit spiegelt masterchat de stand in projectinstructie v1.12 + README (brain-first-volgorde).*
