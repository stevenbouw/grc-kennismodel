# Instructie Brein-subagent — Brein-cyclus iteratie 16 (post-v4.6.4 + sessie-pakket 29 mei 2026)

**Van:** masterchat
**Datum:** 29 mei 2026
**Doel-subagent:** Brein (Claude Code)
**Cyclus:** iteratie 16 (volgt op iteratie 15 / post-T3)
**Aard:** brain-vault-onderhoud (Protocol 11). Administratieve verwerking van een **multi-werkstroom-sessie**. Geen architectuur-besluiten autonoom; alleen status-mutaties + registratie per masterchat-besluit.

---

## 0. Karakter van deze cyclus — lees dit eerst

Anders dan iteraties 12–15 (telkens één sprint → brain-update) bundelt iteratie 16 **meerdere werkstromen uit één masterchat-sessie** (29 mei 2026):

1. Een ontologie-patch: **v4.6.4** (CSF-description range-fix, DL-conformiteit, H38-lus gesloten)
2. Een **reasoner-toolchain-evaluatie** (H37 + H38 + H41, alle HOLD; H38 doorgeschoven naar resolved via v4.6.4)
3. Een **dashboard-revival** (Spoor B: B7 + Q-M5 vendoring + B9 WCAG) — gecommit
4. Een afgesloten inventarisatie: **T4** (Optie B, geparkeerd, geen mutatie)
5. Een reeks **losse besluiten** (Q-M-dashboard, Spoor B-bron-besluiten, Protocol 18, Q-M2-reversal, settings.json-fix, D.7-skill)

Verwerk dit in **werkpakketten** (WP's, hieronder). Splits in 2 batches zoals gebruikelijk (Protocol 11 Stap 3). Lees per werkstroom het bron-rapport aan de bron vóór je propageert — niet uit deze instructie alleen.

**Bron-rapporten (read-only input):**
- `output/reports/patch-rapport-v4_6_4.md` — de range-fix
- `output/reports/evaluatie-reasoner-toolchain-h37-h38-h41.md` — de evaluatie
- `output/reports/dashboard-rapport-qm5-vendoring-b9-wcag-2026-05-29.md` + `dashboard-tussenrapport-b7-wiring-2026-05-29.md` — dashboard
- `output/reports/t4-pre-sprint-inventarisatie.md` + `t4-pre-sprint-inventarisatie-oplevernotitie.md` — T4
- `docs/instructies/besluitnotitie-qm-dashboard-2026-05-29.md` — Q-M-besluiten
- `docs/instructies/protocol-18-concept.md` — Protocol 18
- `output/reports/d7-grc-domein-skill-oplevernotitie.md` — D.7-skill

## 1. Werkpakketten

### WP1 — v4.6.4-sprint registreren (verplicht kern)
- Nieuw sprint-bestand `brain__sprints__v4_6_4_*.md` (slug naar keuze, bv. `csf-range-fix-dl-conformiteit`). Patch-bump, TBox-bugfix. Karakteriseer als **eerste sprint waarin een HermiT-bevinding een TBox-fix in de canonieke baseline stuurde** (methodologisch precedent, patch-rapport §5).
- `brain__sprints__sprint-register.md` — v4.6.4-rij; T3 naar superseded. **Baseline-metrics ONGEWIJZIGD** (20.950 / 44.907 / 199 / 1.383 / 149 / 96 / 98 / SKOS 1.798) — de fix vervangt alleen 2 triple-objecten (`xsd:string` → `rdfs:Literal`). Multiplier-tabel: v4.6.4-rij triple-neutraal (net als T-sprints, maar dit is een TBox-fix geen SKOS-substitutie — maak dat onderscheid expliciet).
- `brain__index.md` — baseline v4.6.3 → v4.6.4; vault-staat-rij iteratie 16.
- `brain__log.md` — nieuwe entry bovenaan (iteratie 16).

### WP2 — H38 resolved + H37/H41 HOLD-status (verplicht)
- `brain__architecture__H38_owlrl-vs-hermit-equivalentie.md` — status **parked → resolved**. H38 is empirisch gesloten: de census voorspelde één DL-only-constructie (`asset:AssetOrComponent ≡ unionOf`, materialiseerbaarheids-compleet); de HermiT-run v4.6.3 vónd echter een reële divergentie (datatype-range-mismatch op de 2 CSF-description-properties), die in v4.6.4 is gefixt; de HermiT-her-run op v4.6.4 (merged_asserted_v4_6_4.ttl) bevestigde **consistent, 0 owl:Nothing, geen justificaties**. Leg de volledige boog vast: blind spot → evaluatie → bevinding → fix → her-verificatie. Dit is het eerste empirische bewijs dat OWL RL ≡ HermiT voor deze baseline (na de range-fix).
- `brain__architecture__H37_open-ontologies-mcp.md` — status **parked, ongewijzigd**. Voeg evaluatie-uitkomst toe: desk-evaluatie uitgevoerd (Rust + Oxigraph + tableaux + MCP, MIT, pre-1.0 v0.1.11); geen van 4 triggers actief; 44.907 < 50k. Trigger-herijking documenteren.
- `brain__architecture__H41_skos-axioma-set-handling.md` — status **parked, ongewijzigd**. Voeg de evaluatie-kwantificatie toe: SKOS-axioma-activering zou +2.831 triples (+6,3%) toevoegen, waaronder 12 cross-namespace exactMatch-claims die D4 schenden + SKOS/sameAs-identiteit vermengen; SHACL-impact 0. **Vastleggen als masterchat-regel:** eventuele toekomstige activering is een **nieuwe D-decision** over reasoner-/SKOS-axioma-configuratie (niet impliciet). Ook vastleggen: de control-run bewees mechanistisch dat de post-inferentie SKOS-groei (+956) 100% owl:sameAs-propagatie is, 0% SKOS-axiomas — dit verklaart T1/T2/T3's Δ=0.
- `brain__architecture__H-register.md` — H38 van parked naar resolved; H37 + H41 parked-rijen verrijkt met evaluatie-uitkomst; toolchain-cluster-sectie bijwerken; iteratie-16-status-mutaties-sectie.

### WP3 — dashboard-revival vastleggen (verplicht)
Dit raakt Spoor B (operationele werkmap). **Niet** de dashboard-code aanraken (dashboard-subagent-werkgebied) — alleen brain-registratie.
- Sprint- of concept-registratie naar Brein-oordeel (dit is geen ontologie-sprint; mogelijk past het beter als concept/workflow-entry dan als `brain__sprints__v*`-bestand). Leg vast: B7 ontologie-structuur-import + bron-split 1A (wStruct/wOper), Q-M5 vendoring (offline-werking, CDN → lokaal), B9 WCAG 2.1 AA (47 → 0 axe-bevindingen).
- **Twee dashboard-vervolgpunten** registreren (geen H-items declareren zonder masterchat — leg ze vast als bekend-vervolgpunt in het relevante concept/workflow-bestand of als open-punt, NIET als nieuw H-item):
  - `file://`-laadgedrag: bij dubbelklik (file://) faalt WASM-laden → "DB fout". Werkt wel via http.server. Demo-risico: bestuurder die dubbelklikt ziet een fout. Vervolg-fix-richting: base64-embedded WASM of duidelijke foutmelding-met-instructie.
  - `herkomst`-kolom bij verse load: vóór eerste import bestaat de kolom niet → wOper() toont "—" i.p.v. %. Pre-existing B7-gedrag. Fix-richting: kolom-migratie ook in laadSeedData().
- Verwerk de **Q-M-dashboard-architectuurbesluiten** (uit besluitnotitie) en de **3 Spoor B-bron-besluiten** (Optie A bron-import · Optie 1 co-existentie · 1A bron-split) als concept/scope-registratie. Dit zijn masterchat-besluiten; leg ze vast, interpreteer ze niet.
- **Q-M2-reversal:** het eerdere "v3-2 lokaal/niet-in-repo"-besluit (iteratie 12 open punt) is herzien — v3-2 mag in de repo (org-data-vrij). Werk de openstaande "locatie Spoor B-prototype"-vraag (open sinds iteratie 12, genoemd in iteraties 13/14/15) bij naar **opgelost**.

### WP4 — T4-afsluiting + csf↔ISO-kandidaat-H-item (verplicht)
- T4 als **inventarisatie-only, geparkeerd (Optie B)** registreren. Geen mutatie, baseline ongewijzigd. De "105 cross-bron-overlap" bleek niet machine-reproduceerbaar (bron-niveau-getal uit v4.5.0). Wat er ligt: 739 csf↔ISO27001 closeMatch-mappings, cross-category, geen prima-facie defect.
- **Nieuw kandidaat-H-item** — csf↔ISO27001 cross-category-predicaat-vraag. **LET OP de discipline:** masterchat heeft dit als *kandidaat* benoemd; jij legt het empirisch precedent + de open vraag vast, maar declareert geen formeel H-nummer zonder expliciete masterchat-instructie. Volg het patroon van iteratie 15 (cross-category-mappings als kandidaat v1.3.1-precedent, niet geformaliseerd). Drie open subvragen meenemen: (a) relatedMatch vs closeMatch retrieval-interchangeability voor csf↔ISO, (b) v1.3.1-formalisering, (c) de 699-vs-494-reconciliatie (§2.2 vs §3.1-B in t4-rapport onverklaard). Relateer aan het bestaande `cross-category-mappings`-concept (iteratie 15).

### WP5 — losse besluiten + protocollen (verplicht)
- **Protocol 18** (pre-sprint-dashboard-update-checklist) — merge surgisch in `docs/sprint-protocols.md` conform het concept in `docs/instructies/protocol-18-concept.md`. Workflow-register bijwerken. (Let op: dit is een echte protocol-toevoeging, geen kandidaat — masterchat heeft het concept aangeleverd; jouw taak is de merge + register-consistentie.)
- **D.7 GRC-domein-skill** registreren — `.claude/skills/grc-domein/SKILL.md` + `kaders-reference.md` zijn opgeleverd en GO gekregen. Registreer in het relevante workflow/concept-bestand. **Niet** de skill-bestanden zelf aanraken (buiten brain-scope). Één openstaande verificatie noteren: bevestigen dat `fw:relatedTo`/`fw:alignsWith`/`fw:supersedes` echt in m01 staan (masterchat-actie, niet Brein).
- **settings.json-schemafix** — voetnoot/leerpunt: de `.claude/settings.json` faalde te parsen door een foute `$schema`-URL (`claude.com/...` i.p.v. `json.schemastore.org/claude-code-settings.json`); opgelost. Leg vast als workflow-leerpunt; raak settings.json niet aan.
- **version-drift-leerpunt** — de grc-core version-triple stond sinds T1 op 4.6.0 (nooit meegebumpt bij T1/T2/T3 SKOS-substituties); v4.6.4 corrigeerde naar 4.6.4. Leg vast als leerpunt: version-bump-stap wordt bij triple-neutrale T-sprints makkelijk overgeslagen — aandachtspunt voor toekomstige kwaliteitsanalyse-sprints. Mogelijk relevant voor Protocol-aanvulling (kandidaat, niet formaliseren).

## 2. Discipline (Brein-rol-grens — hard)

- **Geen architectuur-besluiten autonoom.** H38 → resolved volgt masterchat-besluit (deze instructie). H37/H41 blijven parked. Het csf↔ISO-kandidaat-H-item krijgt **geen** formeel nummer zonder expliciete masterchat-instructie — vastleggen als kandidaat-precedent, net als iteratie 15.
- **Geen formaliseringen die masterchat-werk zijn:** Protocol v1.3.1 (cross-category) NIET formaliseren; csf↔ISO-predicaat-keuze NIET beslissen.
- **Niet aanraken:** `ontology/**`, `dashboard/**`, `scripts/**`, `output/verification/**`, `.claude/skills/**`, `.claude/settings.json`, `.claude/agents/**`. Protocol 18-merge in `docs/sprint-protocols.md` is wel toegestaan (workflow-doc, geen code).
- **Scope-pauze** bij: conflict tussen een bron-rapport en bestaande brain-content; twijfel of iets een formeel H-item moet worden; cross-folder-impact onduidelijk. Schrijf dan `output/reports/scope-pauze-v4_6_4-brein-<onderwerp>.md` en wacht.
- **Pre-push disclosure-check** (Protocol 14, vijf categorieën) op alle nieuwe/gewijzigde bestanden.
- **Geen autonome commit** — lever op, Steven inspecteert + commit handmatig (per WP of cumulatief; geef een voorstel in het brein-rapport).

## 3. Deliverable

- Brein-eindrapport `output/reports/brein-rapport-iteratie-16.md`: lijst aangepaste bestanden per WP (nieuw/update/restructure), cross-referentie-verificatie-resultaat, leerpunten, en eventuele file-back-voorstellen voor masterchat.
- `brain__log.md`-entry (iteratie 16, bovenaan) + `brain__index.md`-update (baseline v4.6.4).
- Open-punten-lijst voor masterchat (zoals iteraties 13–15 die hadden).

## 4. Volgorde

Batch 1 (kern): WP1 + WP2 + log + index + registers. Batch 2 (detail): WP3 + WP4 + WP5. Cross-referentie-coherentie-check vóór elke batch-afronding (Protocol 11 Stap 4).

Bevestig kort dat je de context + alle bron-rapporten hebt gelezen, en begin met Batch 1.
