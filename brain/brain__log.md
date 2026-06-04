---
type: log
title: GRC Kennismodel Brain — Chronologisch logboek
status: living
date: 2026-06-04
---

# GRC Kennismodel Brain — Chronologisch logboek

Per Karpathy's pattern: chronologisch operationeel record. Append-only. **Nieuwste entry bovenaan.**

---

## 2026-06-04 — Iteratie 17: v7-dashboardwerksessie officieel maken (geheugen-lag dichten — reskin + DORA-correctie + IA-herinrichting + twee open besluiten)

**Zesde post-migratie Brein-cyclus** — speciaal karakter: **achteraf-cyclus** die een **geheugen-lag** dicht. Tussen iteratie 16 (29 mei, "geen actieve sprint", dashboard-revival B7/Q-M5/B9) en deze iteratie 17 (4 juni) heeft een v7-dashboardwerksessie (2–3 juni 2026) plaatsgevonden die nooit door een Brein-cyclus is verwerkt. `bootstrap-masterchat-v7.md` + `docs/handovers/overdrachtsrapport.md` beschreven die latere stand al; de brain-vault (gezaghebbend) niet. Iteratie 17 dicht die lag.

**Ontologie-baseline:** v4.6.4 **ONGEWIJZIGD** (dit is puur dashboard-/Spoor-B-werk, geen ontologie-mutatie). Geen D-decisions gewijzigd, geen sprint-protocollen gewijzigd, geen claims op ontologie-niveau aangeraakt. Brein-discipline: geen autonome interpretatie; alle vastlegging volgt de bronrapporten + de instructie.

**WP1 — v7-werkstroom vastleggen (drie deel-ingrepen + lag-leerpunt):**
- [[brain__concepts__spoor-b-revival]] *(update — uitgebreid met v7-werkstroom)* — Nieuwe sectie "v7-werkstroom — reskin + DORA-correctie + IA-herinrichting (2–3 juni 2026)" met drie deel-ingrepen: (v7-1) reskin Overzicht + warm-papier-thema o.b.v. `dashboard/design-tokens-grc-dashboard.css` (nieuw bestand); `data-ramp="contrast"` als default met WCAG 2.1 AA-onderbouwing (`--c-warn` #7a4e08 ≥4,5:1 op getinte oppervlakken; "aards"-`--c-warn` #9a6410 haalt 4,46/4,54 — net onder/op de grens); axe 0 over alle 5 tabs; offline-vendoring + SQL.js + verse-load ongemoeid; twee vooraf geautoriseerde scope-afwijkingen (A hele dashboard licht; B tab-consolidatie doorgeschoven als IA-besluit naar masterchat). (v7-2) DORA-correctie — overal verwijderd als actief/bindend kader → uitsluitend "referentiekader · n.v.t.", consistent met m12 DORA als referentie; SoA-kolom + control-`dora_ref`-velden + modal-veld "DORA-referentie" bewust behouden als cross-reference-mappings (geen bindingsclaims); kalender-seed + framework-detail-metadata reframed naar referentie. (v7-3) IA-herinrichting 5→4 tabs (Overzicht · Governance · Compliance · Risk); ISMS-tab opgeheven, inhoud herverdeeld (PDCA/ISMS-scope/KRI-KPI/directiebeoordeling → Governance/ISMS-overkoepelend; SoA → Governance prominent; Kalender → Governance; NC-register → Compliance/Audit & Bevindingen); **gelaagde kader-kiezer** (Governance 5 kaders Laag 0+1: COSO ICF/ERM, COBIT 2019, BVA-stelsel, CIO-stelsel; Compliance 15 kaders Laag 2-5: BIO 2.0 *(standaard, Rijksbaseline)*, ISO 27001/27002/27005, ISO 22301/22313, NIS2, VIR 2007, VIRBI 2025, AVG/GDPR, CBW "in voorbereiding", Cbb "concept t.b.v. Tweede Kamer", NIST 800-53 R5, NIST CSF 2.0, ENSIA); **DORA verschijnt NIET in de kiezer**; risico-methodologie-normen (ISO 27005/31000, NIST 800-30/39) blijven in Risk; pre-existing `modalDelete`-bug gefixt (buiten IA-scope, gemeld); axe 0 over alle 4 tabs + alle inner-tabs/kiezer-states; CRUD-regressiematrix groen voor risico/control/rol/document/bevinding/kalender. **Kader-kiezer expliciet als D9-conform perspectief-mechanisme** beschreven: chips zijn view-switch zonder hiërarchie; subregel "perspectief-keuze — alle kaders gelijkwaardig (D9); BIO 2.0 standaard als Rijksbaseline"; BIO-default = operationele view-keuze, geen architectuur. Twee OPEN besluiten expliciet vastgelegd (zie WP2). **Lag-leerpunt** vastgelegd in status-historie van dit concept-bestand
- [[brain__concepts__dashboard-productlijnen]] *(update)* — Nieuwe sectie "Spoor B v7-stand — 4 tabs + gelaagde kader-kiezer + warm-papier-thema (2–3 jun 2026)" met tab-structuur 5→4, kader-kiezer per tab als D9-conform perspectief-mechanisme zonder hiërarchie, statusdiscipline (CBW/Cbb/DORA), reskin-thema + tokens, DORA-correctie als cross-reference-behoud, en de twee open besluiten. Status-rij geactualiseerd van 29 mei → 4 jun 2026. Status-historie-rij toegevoegd. Frontmatter `date` + `related` (framework-neutraliteit toegevoegd) + `sources` (drie nieuwe rapporten) bijgewerkt

**WP2 — Twee OPEN besluiten + H-koppelingen (Brein-discipline: GEEN nieuwe H-items declareren):**
- [[brain__concepts__spoor-b-revival]] *(update — nieuwe sectie "Twee OPEN besluiten")* — Twee inhoudelijke besluiten cruciaal voor volgende fase: **(1) Lege-huls-kernprobleem** — de gelaagde kader-kiezer toont placeholders i.p.v. echte controls/beschrijvingen/eisen ("structuur staat, inhoud leeft niet"); Pad 1 (ontologie-export verrijken via build-script — architecturaal zuiver, raakt drie lagen, opvolging) vs Pad 2 (demo-seed verrijken voor BIO 2.0 + ISO 27001/27002 — snel, demo-klaar, geen ontologie-impact; **geadviseerd nu**); gekoppeld aan [[brain__architecture__H40_dashboard-ui-renderdekking]] als **aangrenzend Spoor-B-vraagstuk** (H40-scope blijft Spoor A explorer-UI hard); Brein declareert geen nieuw H-item zelfstandig. **(2) Organisatiestructuur in dashboard** — A (volledig generiek/demo, veiligst) / B (echte functionele structuur, geanonimiseerd — **geadviseerd**) / C (volledig echt, gevoelig — raakt §0.5-/disclosure-discipline + always-on invariant "organisatienaam NOOIT"); gekoppeld aan [[brain__architecture__H29_three-lines-model]] (future-consideration) + CIO/BVA-RACI-stelsels (Laag 0+1, in v7-3 onder Governance-kiezer); Optie B levert realistisch modelwerk voor M04
- [[brain__architecture__H-register]] *(update)* — Datum-frontmatter naar 2026-06-04. Iteratie-17-status-mutaties-sectie toegevoegd: H40 (parked, lege-huls-aangrenzing iteratie 17), H29 (future-consideration, organisatiestructuur-koppeling iteratie 17). H40-rij in parked-tabel bijgewerkt met lege-huls-aangrenzing en open Pad 1/2-besluit. H-items-per-D-decision-tabel "dashboard-cluster" bijgewerkt: H40 (lege-huls-aangrenzing Spoor B), H29 (organisatiestructuur). **Geen nieuwe H-items gedeclareerd** — Brein-discipline expliciet vastgelegd in mutaties-sectie

**WP3 — Sprint-register + handover-artefacten:**
- [[brain__sprints__sprint-register]] *(update)* — Datum-frontmatter naar 2026-06-04. Header-context-regel uitgebreid met v7-dashboardwerksessie (2–3 jun 2026, Spoor B, geen ontologie-sprint, baseline v4.6.4 ongewijzigd). Nieuwe sessie-rij in major-milestones-tabel ("v7-dashboardwerksessie (Spoor B)" — "sessie (geen ontologie-sprint)") met drie deel-ingrepen + twee open besluiten. Detail-per-sprint-tabel uitgebreid met verwijzing naar [[brain__concepts__spoor-b-revival]] §"v7-werkstroom" (geen aparte sprint-file aangelegd — concept-registratie, analoog aan iteratie 16's spoor-b-revival-concept)
- v7-handover-artefacten (cross-sessie context, niet door Brein gemaakt — masterchat-werk) genoteerd in [[brain__concepts__spoor-b-revival]] §"v7-handover-artefacten": `docs/handovers/overdrachtsrapport.md` (volledig zelfstandig startpunt; §5.3-5.5 v7-dashboardspoor + open besluiten) + `docs/handovers/bootstrap-masterchat-v7.md` (actuele Master-startprompt, opvolger van v6-sessie-rapport-lijn). Beide ongewijzigd door Brein gelezen

**WP4 — Log + Index:**
- [[brain__log]] *(deze entry)* — nieuwste entry bovenaan, iteratie 17. Datum-frontmatter naar 2026-06-04
- [[brain__index]] *(update)* — Vault-staat-rij iteratie 17 toegevoegd (16 → 17); ontologie-status-overzicht-tabel ONGEWIJZIGD (baseline v4.6.4); status-overzicht-sectie uitgebreid met v7-dashboardstand + de twee open besluiten; "Volgende activiteit" omgegooid: lege-huls-besluit (Pad 1/2) is nu eerste prioriteit i.p.v. "geen actieve sprint" / "T4 afgesloten"; folder-tellingen ongewijzigd (geen nieuwe brain-bestanden — alleen updates); meta-project-tabel (17 iteraties / zesde cyclus)

**File-count iteratie 17:**

| WP | Nieuw | Update | Bestanden |
|---|---:|---:|---|
| WP1 v7-werkstroom | 0 | 2 | `brain__concepts__spoor-b-revival.md` (v7-werkstroom-sectie + status-historie + frontmatter), `brain__concepts__dashboard-productlijnen.md` (v7-stand-sectie + status-historie + frontmatter) |
| WP2 open besluiten + H-koppelingen | 0 | 1 | `brain__architecture__H-register.md` (iteratie-17-mutaties-sectie + H40-rij + H29-koppeling + dashboard-cluster + frontmatter); de twee open besluiten zelf staan in spoor-b-revival (al onder WP1 geteld) |
| WP3 sprint-register + concept-register-consistentie | 0 | 2 | `brain__sprints__sprint-register.md` (v7-sessie-rij + detail-tabel + header + frontmatter), `brain__concepts__concept-register.md` (spoor-b-revival + dashboard-productlijnen-rijen + clusters + frontmatter) |
| WP4 log + index | 0 | 2 | `brain__log.md` (deze entry + frontmatter), `brain__index.md` (vault-staat-rij iteratie 17 + status-overzicht + volgende-activiteit + meta-project + frontmatter) |
| **Totaal** | **0** | **7** | **alle brain (geen docs/scripts/ontology aangeraakt)** |

**Geen nieuwe brain-bestanden aangemaakt.** v7-werkstroom is vastgelegd als uitbreiding van het bestaande [[brain__concepts__spoor-b-revival]]-concept-bestand (Brein-oordeel autonomie: thematische coherentie + sprint-register-vindbaarheid via concept-verwijzing, analoog aan iteratie-16-aanpak voor de 29-mei Spoor B-revival).

**Cross-referentie-verificatie (Brein-discipline):**
- spoor-b-revival uitgebreid met v7-sectie + twee-open-besluiten-sectie + handover-artefacten-sectie + nieuwe sources in frontmatter (patch-rapport-dashboard-reskin-overzicht, patch-rapport-dashboard-ia-herinrichting, ia-voorstel-tab-consolidatie, instructie-dashboard-reskin-overzicht, instructie-dashboard-ia-herinrichting, design-tokens-grc-dashboard) — wikilinks naar D09-framework-neutraliteit, H40, H29, framework-neutraliteit, bbn-correctie, log allemaal aanwezig
- dashboard-productlijnen ↔ spoor-b-revival: wederzijdse wikilinks aanwezig en aangevuld; status-rij synchroon 4 jun 2026
- H-register: H40-rij in parked-tabel + iteratie-17-mutaties-sectie + dashboard-cluster-tabel + H29-koppeling consistent
- Sprint-register: v7-sessie-rij in major-milestones + detail-per-sprint-tabel; verwijst naar concept (geen sprint-file aangelegd)
- Index: iteratie-17-rij + status-overzicht-sectie + volgende-activiteit-aanpassing + meta-project-tabel consistent
- Ontologie-baseline v4.6.4 ONGEWIJZIGD over alle 6 bestanden — geen Δ in canonical-metrics-tabel in index, geen module-mutaties

**Pre-push disclosure-check (Protocol 14, 5 categorieën) op alle gewijzigde bestanden:**
1. **Organisatie-naam:** niet genoemd; "de organisatie" / "Rijksoverheidsorganisatie" waar relevant. Optie C in organisatiestructuur-besluit expliciet gemarkeerd als raakt-§0.5-discipline
2. **Persoonsnamen:** alleen Steven (publieke projecteigenaar) waar relevant. Geen andere namen
3. **Lokale paden:** alleen repo-relatief. Geen credentials in paden
4. **Credentials / TLD / e-mail:** geen
5. **NEN-tekst-fragmenten verbatim >10 woorden:** geen. Frameworks-aanduidingen zijn factuele identifiers + clausule-/Annex-A-stijl; CBW "in voorbereiding" + Cbb "concept" zijn status-aanduidingen (always-on invariant); BBN-correctie expliciet gerefereerd

**Karakter-bevestiging:** geen architectuurbeslissingen autonoom door Brein. **Geen D-decisions** aangeraakt. **Geen sprint-protocollen** aangeraakt. **Geen ontologie-claims** gewijzigd (baseline v4.6.4 ongewijzigd; canonical-metrics-tabel in index ongewijzigd). **Geen nieuwe H-items** gedeclareerd (lege-huls + organisatiestructuur vastgelegd als aangrenzende open besluiten bij H40 resp. H29). **Geen organisatienaam, geen organisatiedata** (dashboard gebruikt representatieve demo-data — zo expliciet vastgelegd). **Niet aangeraakt:** `ontology/`, `dashboard/`, `scripts/`, `output/verification/`, `.claude/skills/`, `.claude/settings.json`, `.claude/agents/`, `docs/sprint-protocols.md`, `docs/handovers/*`, `docs/instructies/*` (referentie-lezen alleen), patch-rapporten in `output/reports/` (referentie-lezen alleen). **Niet gecommit** — Steven inspecteert + commit handmatig.

**Lag-leerpunt iteratie 17 (kernpunt):** Een werksessie zonder afsluitende Brein-cyclus creëert een geheugen-lag waar latere lezers (volgende masterchat-sessie, opvolgend beheerder) over struikelen. Tussen 29 mei (iteratie 16) en 4 juni (iteratie 17) liep de brain-vault — de **gezaghebbende bron** — achter op de werkelijke stand. De handover-artefacten beschreven al de v7-stand; de vault niet. Conclusie: **Brein-cyclus na elke betekenisvolle sessie**, niet alleen na een ontologie-release. Spoor B-werk telt ook als betekenisvol. Voor toekomstige projectinstructie-update (masterchat-werk, niet Brein) is dit een kandidaat-aanvulling op de werkproces-/cyclus-discipline.

**Volgende:** Steven inspecteert + commit handmatig. Masterchat spiegelt na commit de stand in projectinstructie v1.12 + README (brain-first-volgorde) — zie sluitzin instructie iteratie 17. Eerste prioriteit voor de volgende sessie: **lege-huls-besluit (Pad 1 vs Pad 2)** — gevolg bij keuze Pad 2 = demo-seed-verrijkings-sprint voor BIO 2.0 + ISO 27001/27002; gevolg bij Pad 1 = ontologie-export-verrijkings-sprint (drie-lagen-werk). Tweede prioriteit: **organisatiestructuur-besluit (A/B/C)** — gevolg bij Optie B = M04 RACI-/structuur-modelwerk (waardevol ongeacht dashboard-bestemming).

---

## 2026-05-29 — Iteratie 16: multi-werkstroom-Brein-cyclus (v4.6.4 TBox-bugfix + H38 resolved + reasoner-evaluatie + dashboard-revival + T4-afsluiting + Protocol 18 + losse besluiten)

**Vijfde post-migratie Brein-cyclus** — en de **eerste multi-werkstroom-cyclus**: anders dan iteraties 12-15 (telkens één sprint → brain-update) bundelt iteratie 16 vijf werkstromen uit één masterchat-sessie (29 mei 2026). Geen architectuur-besluiten autonoom door Brein; alleen status-mutaties + registratie per masterchat-besluit. Verwerkt in twee batches (kern: WP1+WP2; detail: WP3+WP4+WP5). 15 bestanden geraakt (2 nieuw + 12 update brain + 1 docs).

**WP1 — v4.6.4 TBox-bugfix-sprint registreren (baseline ONGEWIJZIGD):**
- [[brain__sprints__v4_6_4_csf-range-fix-dl-conformiteit]] *(nieuw)* — TBox-bugfix-patch (geen T-sprint): 2× CSF-Tier-vrije-tekst-property `rdfs:range xsd:string` → `rdfs:Literal` in `m21-csf.ttl` (Optie A) + version-bump `grc-core`. Baseline-metrics 100% identiek aan v4.6.3 (20.950 / 44.907 / 199 / 1.383 / 149 / 96 / SKOS 1.798). Eerste sprint waarin een HermiT-bevinding een TBox-fix in de canonieke baseline stuurde. Onderscheid met T1/T2/T3 expliciet (TBox-range-fix, géén SKOS-predicate-substitutie)
- [[brain__sprints__sprint-register]] *(update)* — v4.6.4-rij active; T3 → superseded; v4.6.4 baseline-metrics-blok (alle Δ=0); multiplier-tabel (v4.6.4 0×, ander mutatie-type); D-cross-reference-rij (D1 versterkt); geplande-sprints-tabel (T4 afgesloten Optie B; csf↔ISO27001 mogelijk terugkerend)

**WP2 — H38 resolved + H37/H41 evaluatie-uitkomst (parked):**
- [[brain__architecture__H38_owlrl-vs-hermit-equivalentie]] *(update — parked → resolved)* — OWL RL ≡ HermiT empirisch bevestigd voor deze baseline. Volledige boog vastgelegd: blind spot → DL-construct-census (1 materialiseerbaarheids-complete constructie) → HermiT-run v4.6.3 vond reële divergentie (datatype-range-mismatch, 8 justificaties) → v4.6.4-fix → HermiT-her-run v4.6.4 consistent (0 owl:Nothing). Methodologisch precedent + status-historie-rij
- [[brain__architecture__H37_open-ontologies-mcp]] *(update — parked, ongewijzigd)* — desk-evaluatie-uitkomst toegevoegd: Rust + Oxigraph + tableaux + MCP, MIT, pre-1.0 v0.1.11; oordeel HOLD, geen van 4 triggers actief (44.907 < 50k; H38 resolved). Trigger-herijking + status-historie
- [[brain__architecture__H41_skos-axioma-set-handling]] *(update — parked, impact gekwantificeerd)* — control-run bewijst mechanistisch dat post-inferentie SKOS-groei (+956) 100% owl:sameAs-propagatie is, 0% SKOS-axiomas (verklaart T1/T2/T3's Δ=0). Hypothetische activering = +2.831 triples (+6,3%), 12 cross-namespace exactMatch-claims die D4 schenden + SKOS/sameAs-identiteit vermengen; SHACL 0. Masterchat-regel: activering = nieuwe D-decision. Status-historie
- [[brain__architecture__H-register]] *(update)* — H38 van parked naar resolved (parked 7→6, resolved 5→6); H37 + H41 parked-rijen verrijkt; iteratie-16-status-mutaties-sectie; H42/H43/H44 als masterchat-benoemde kandidaten + csf↔ISO27001-kandidaat-precedent (geen formeel nummer); toolchain-cluster + D1-tabel bijgewerkt

**WP3 — dashboard-revival + Q-M-besluiten + Q-M2-reversal:**
- [[brain__concepts__spoor-b-revival]] *(nieuw)* — Spoor B-revival grc-dashboard-v3-2 (29 mei): B7-wiring + bron-split 1A (wStruct/wOper) + Q-M5 lokaal vendoren (offline) + B9 WCAG 47→0. Drie Spoor B-bron-besluiten (Optie A · Optie 1 · 1A) als één pakket. Twee bekende vervolgpunten: `file://`-laadgedrag (WASM faalt bij dubbelklik → demo-risico) + `herkomst`-kolom verse load (pre-existing B7-gedrag). Brein-registratie alleen; dashboard-code niet aangeraakt
- [[brain__concepts__dashboard-productlijnen]] *(update)* — **Q-M2-reversal**: locatie-besluit herzien, v3-2 mag in repo (org-data-vrij); openstaande "locatie Spoor B"-vraag (sinds iteratie 12) opgelost. Zes Q-M-architectuurbesluiten (Q-M1..Q-M6) vastgelegd. Naam-actueel- + status-rij + status-historie bijgewerkt
- [[brain__concepts__concept-register]] *(update)* — nieuwe rij spoor-b-revival + dashboard-productlijnen-rij bijgewerkt; product-scope-discipline-cluster + D-cross-references + sprint-cross-references

**WP4 — T4-afsluiting + csf↔ISO27001-kandidaat-precedent:**
- [[brain__concepts__cross-bron-overlap]] *(update)* — T4-bevinding: de 105-overlap is een bron-niveau-getal (v4.5.0), niet machine-reproduceerbaar (block-level provenance → detection-query levert 0). Model-meetbaar: 245 clausule-unie (intersectie 19) + 494 Annex A (m21-only). Per-triple-provenance = open architectuur-vraag (masterchat). T4 afgesloten als inventarisatie-only, geparkeerd (Optie B); baseline ongewijzigd
- [[brain__concepts__cross-category-mappings]] *(update)* — tweede cross-category-kandidaat-precedent: csf↔ISO27001 (739 paren, gesplitste categorie outcome↔requirement + outcome↔measure). Drie open subvragen: (a) relatedMatch-vs-closeMatch retrieval-interchangeability, (b) v1.3.1-formalisering, (c) 699-vs-494-reconciliatie (T4-rapport §2.2 vs §3.1-B onverklaard). **Geen formeel H-nummer** (Brein-discipline, analoog iteratie 15)

**WP5 — Protocol 18-merge + D.7-skill + twee leerpunten:**
- `docs/sprint-protocols.md` *(update)* — **Protocol 18 — Pre-sprint-dashboard-update-discipline** surgisch gemerged (kop 17 → 18; canonieke 1-17 ongewijzigd); overzichtstabel-rij + wijzigingsgeschiedenis v1.4. Dashboard-tegenhanger van Protocol 1
- [[brain__workflow__workflow-register]] *(update)* — iteratie-16-additions-sectie: Protocol 18 + D.7 GRC-domein-skill (`.claude/skills/grc-domein/` — description-triggered, Brein niet aangeraakt; openstaande verificatie `fw:relatedTo`/`alignsWith`/`supersedes` in m01 = masterchat) + settings.json-leerpunt (foute `$schema`-URL brak parse) + version-drift-leerpunt (grc-core version stond sinds T1 op 4.6.0; v4.6.4 corrigeerde; kandidaat voor Protocol-aanvulling, niet formaliseren)
- [[brain__workflow__sprint-protocollen]] *(update)* — pointer toegevoegd: canonieke set = 18 protocollen (docs/sprint-protocols.md autoritatief); de v1.9-momentopname (12) niet bijgewerkt voor 13-18

**WP6 — Log + Index:**
- [[brain__log]] *(deze entry)* — nieuwste entry bovenaan, iteratie 16
- [[brain__index]] *(update)* — vault-staat-rij iteratie 16; baseline v4.6.3 → v4.6.4; status-overzicht-ontologie ververst; v4.6.4 wijzigingen-blok; H-register-entry-blok (H38 resolved); volgende-fase-status iteratie 16; open-punten (locatie Spoor B opgelost); meta-project-tabel (16 iteraties / vijfde cyclus); folder-tellingen (sprints 18, concepts 20)

**File-count iteratie 16:**

| WP | Nieuw | Update | Totaal |
|---|---:|---:|---:|
| WP1 v4.6.4-sprint | 1 | 1 (sprint-register) | 2 |
| WP2 H-items | 0 | 4 (H38, H37, H41, H-register) | 4 |
| WP3 dashboard | 1 (spoor-b-revival) | 2 (dashboard-productlijnen, concept-register) | 3 |
| WP4 T4 | 0 | 2 (cross-bron-overlap, cross-category-mappings) | 2 |
| WP5 protocollen + leerpunten | 0 | 2 brain (workflow-register, sprint-protocollen) + 1 docs (sprint-protocols.md) | 3 |
| WP6 log + index | 0 | 2 (log + index) | 2 |
| **Totaal** | **2** | **13** (12 brain + 1 docs) | **15** |

**Cross-referentie-verificatie (Brein-discipline):**
- [[brain__sprints__v4_6_4_csf-range-fix-dl-conformiteit]]: related → T3, D01, H38, H37, H41, M21, owl-rl-reasoning — alle aanwezig
- [[brain__concepts__spoor-b-revival]]: related → dashboard-productlijnen, H40, skos-export-filter — alle aanwezig
- H38: status resolved consistent over H38-bestand, H-register status-overzicht, parked-tabel (H38 verwijderd), resolved-tabel, iteratie-16-mutaties-sectie, D1-tabel, index-entry, sprint-register, sprint-bestand
- H37 + H41: parked-status ongewijzigd; evaluatie-uitkomst + status-historie consistent; related-frontmatter uitgebreid met evaluatie-rapport
- dashboard-productlijnen ↔ spoor-b-revival: wederzijdse wikilinks aanwezig
- cross-category-mappings ↔ cross-bron-overlap: wederzijdse wikilinks aanwezig (T4-context)
- Protocol 18: docs/sprint-protocols.md (kop 18 + tabel + §18 + wijzigingsgeschiedenis) ↔ workflow-register ↔ sprint-protocollen-pointer consistent
- Baseline v4.6.4 (alle Δ=0) consistent over index + sprint-register + sprint-bestand + patch-rapport v4.6.4 §0

**Pre-push disclosure-check (Protocol 14, 5 categorieën) op alle nieuwe/gewijzigde bestanden:**
1. **Organisatie-naam:** niet genoemd; "de organisatie"/"Rijksoverheidsorganisatie" waar relevant
2. **Persoonsnamen:** alleen Steven Bouwmeester (publieke projecteigenaar) waar relevant. Geen andere namen
3. **Lokale paden:** alleen repo-relatief + `/tmp/grc-wcag-tooling/` (geciteerd uit dashboard-rapport, geen credential). Geen credentials in paden
4. **Credentials / TLD / e-mail:** geen
5. **NEN-tekst-fragmenten verbatim >10 woorden:** geen. ISO 27001-eindpunten alleen via clausule-/Annex-A-verwijzing + parafrase (T4-context); CSF-Tier-descriptions zijn NIST CSWP 29 (publiek domein); control-name-strings zijn factuele identifiers. Geen ISO-normtekst geciteerd

**Karakter-bevestiging:** geen architectuurbeslissingen autonoom door Brein. H38→resolved volgt masterchat-besluit (deze instructie) op basis van de gemeten boog. H37/H41 blijven parked (geen masterchat-besluit tot status-revisie of activering). Het csf↔ISO27001-kandidaat-H-item krijgt **geen formeel nummer** — vastgelegd als kandidaat-precedent (analoog iteratie 15). H42/H43/H44 zijn **door masterchat** benoemd (besluitnotitie), niet door Brein gedeclareerd. Protocol v1.3.1 (cross-category) + csf↔ISO27001-predicaat-keuze NIET geformaliseerd (masterchat-werk). Niet aangeraakt: ontology/, dashboard/, scripts/, output/verification/, .claude/skills/, .claude/settings.json, .claude/agents/. Protocol 18-merge in docs/sprint-protocols.md is workflow-doc (toegestaan). Geen autonome commits.

**Volgende:** Steven inspecteert + commit handmatig. Voorstel-commits: zie brein-rapport iteratie 16 §commit-voorstel. Open-punten-lijst voor masterchat in het brein-rapport. Daarna: HermiT-her-run-bevestiging formeel terugmelden, csf↔ISO27001-scope-besluit, projectinstructie v1.11 (commit-push + Protocol 18 + D.7 + Q-M).

---

## 2026-05-28 — Iteratie 15: post-T3-Brein-cyclus (T3-sprint + Protocol v1.3 FINAL + H36 fully closed + cross-category-mappings-concept + commit-push-werkverdeling-workflow + errata-correctie T3-rapporten)

**Vierde post-migratie Brein-cyclus** uitgevoerd via brein-subagent in Claude Code. Administratieve nasleep van T3-sprint (SKOS-bidirectional-audit m14 AVG/GDPR, patch v4.6.3, opgeleverd 28 mei 2026 dezelfde dag) + masterchat-sign-off op v4.6.3 + werkflow-wijziging commit-push-werkverdeling. T3 is **derde post-migratie productie-sprint** en eerste sprint die Protocol v1.3 FINAL in cross-category-context (control ↔ legal-obligation) heeft toegepast.

**Karakter:** administratieve verwerking van besluiten + errata-correctie. Drie hoofdcomponenten:
- **Deel A:** surgische errata-correctie op T3-rapport-bestanden (vóór brain-propagatie) — confidence-tellings-discrepantie m14 corrigeren naar 27 hoog / 4 middel / 0 laag; T3-002 = hoog post-besluit (analoog T3-001); §6.3 verouderde dubbele tabel markeren als errata; §3.1 T3-004 redactie-restje opschonen. Bewaart T-historie (Protocol v1.3 §10.4)
- **Deel B:** brain-vault T3-close + verplichte register-updates
- **Deel C:** nieuw concept `cross-category-mappings` als T3-empirisch precedent (kandidaat v1.3.1 — formalisering = masterchat-werk, NIET nu)
- **Deel D:** nieuw workflow-bestand `commit-push-werkverdeling` (werkflow-wijziging 28-05-2026: masterchat-commit-autonomie; subagent-invariant blijft hard)

Geen architectuur-wijzigingen autonoom door Brein; alleen status-mutaties + nieuwe concept- en workflow-registratie per masterchat-besluit op T3-leerpunt + werkflow-wijziging. 14 bestanden geraakt: 3 nieuw + 11 update.

**Deel A — Errata-correctie (surgisch, vóór brain-propagatie):**

- `output/reports/t3-stap3-eindrapport.md` *(update)* — errata-blok bovenaan + §6.3 markeren als verouderde dubbele tabel (~~doorhaling~~) + §6.4 corrigeren (Pilot: 4/2/0; Stap 3: 23/2/0; cumulatief: 27/4/0) + T3-002 hoog post-besluit + §3.1 T3-004 redactie-restje "5.30 niet relevant" verwijderd. T-historie bewaard (Protocol v1.3 §10.4); detail-tekst §-paren niet herschreven. Patch-impact onveranderd
- `output/reports/patch-rapport-v4_6_3.md` *(update)* — errata-blok bovenaan + §6.4 cumulatieve confidence-tabel gecorrigeerd (26 hoog → 27 hoog; 5 middel → 4 middel; T3-002 niet meer in middel-opsomming). Bron-van-waarheid expliciet aangegeven (§6.1 per-paar-classificatie autoritatief)

**Deel B — Brain-vault T3-close (B1-B12):**

- [[brain__sprints__T3-skos-bidirectional-audit-m14]] *(nieuw)* — Derde post-migratie productie-sprint. Scope: 31 m14 compl→ctrl-paren over 5 AVG-clusters (cross-category control ↔ legal-obligation). Drie-stappen-uitvoering: pre-sprint-inventarisatie + pilot 6 paren (escalatie SKOS-broadMatch-richting → masterchat) + Stap 3 hoofd-uitvoering 25 paren (handmatige scope) + productie-patch v4.6.3 (2 mutaties via masterchat-besluit Optie C; 27 behoud relatedMatch + 2 behoud closeMatch op retrieval-interchangeability). 15/15 GO-criteria groen. Sprint-multiplier 0,03× t.o.v. T2 (smal mutatie-spectrum, breed methodisch leerpunt). Cross-refs: D4 + D4.1-inactief, H36 fully closed, H39 bidirectional, H41 informatief, Protocol v1.0/v1.2/v1.3 FINAL, cross-category-mappings, mapping-bron-disclaimer-effect, cluster-discipline-bewijslast
- [[brain__sprints__sprint-register]] *(update)* — T3-rij toegevoegd als active; T2 verschoven naar superseded. v4.6.3 baseline-metrics-blok geheel (predicate-substitutie: broadMatch −2, relatedMatch +2; SKOS-totaal 1.798 ongewijzigd). Multiplier-tabel uitgebreid met T3-rij (0× triple-multiplier; 0,03× t.o.v. T2 mutatie-multiplier). D-cross-reference-tabel: T3-rij D4 cross-category-rationale-precedent. Geplande-sprints-tabel: T4-kandidaten + Protocol v1.3.1-Brein-cyclus
- [[brain__decisions__D04_skos-cross-framework]] *(update)* — D4.1-inactief-in-T3-sectie + cross-category-rationale-toepassings-precedent-sectie toegevoegd. m14-scope toegevoegd aan D4-validatie-historiek. D4-tekst zelf onveranderd; alleen precedent-uitbreiding. related-frontmatter uitgebreid met T3, cross-category-mappings. Status-historie-rij toegevoegd
- [[brain__architecture__H36_skos-exactmatch-ctrl-compl-audit]] *(update)* — Status active (m10 closed, m14 open subtask) → **fully closed (resolved)**. Title aangepast naar "ctrl:↔compl: SKOS-mappings audit (fully closed via T1+T2+T3)". Status-evolutie-tabel + status-historie-rij. T3-uitkomst-sectie toegevoegd met 2 mutaties + cluster-stand + 0/5 cluster-convergentie + 4 cumulatieve middel-paren. Cumulatief T1+T2+T3 = 95 mutaties op 149 ctrl:↔compl:-paren. Architectuur-impact-tabel uitgebreid (D4 cross-category-rationale, H39 bidirectional, H41 informatief, Protocol v1.3 FINAL, cluster-discipline-bewijslast complementair). related-frontmatter uitgebreid met T3, cross-category-mappings, patch-rapport-v4_6_3, t3-stap3-eindrapport
- [[brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing]] *(update)* — Status onveranderd (parked). Versterking T3-sectie toegevoegd: blinde-vlek nu **bidirectional vastgesteld** over T1+T2+T3 (eerder eenzijdig ctrl→compl; T3 bevestigt compl→ctrl). Status-historie-rij toegevoegd. related-frontmatter uitgebreid met T3
- [[brain__architecture__H41_skos-axioma-set-handling]] *(update)* — Status onveranderd (parked). Empirisch-bewijs-tabel uitgebreid met T3-rij (2 mutaties broad→related cross-category; Δ post-OWL-RL = 0). T3-bevestiging-paragraaf: derde sprint-bewijs op cross-category-context (eerste cross-category-bewijs voor H41). Status-historie-rij toegevoegd. related-frontmatter uitgebreid met T3
- [[brain__architecture__H-register]] *(update)* — Status-overzicht: H36 verschuift van "Active (gedeeltelijk closed)" naar "Resolved" (5 totaal). Active-tabel leeggemaakt. Parked-tabel H39 + H41-rijen versterkt voor T3. Iteratie-15-status-mutaties-sectie toegevoegd (H36 fully closed, H39 bidirectional, H41 T3-bevestiging). H-items-per-D-decision-tabel: D4 H36 fully closed
- [[brain__concepts__skos-beoordelings-protocol]] *(update)* — Versie-evolutie expliciet: v1.0 (T1) → v1.2 (T2) → v1.3 DRAFT (post-T2) → **v1.3 FINAL (T3, vastgesteld masterchat 28 mei 2026)** → v1.3.1 kandidaat-aanvulling cross-category. Nieuwe sectie "T3-toepassing — 2 cross-category-mutaties op m14 AVG/GDPR (Protocol v1.3 FINAL)" toegevoegd. Bindende T3-steers (5) gedocumenteerd. Protocol-versie-roadmap uitgebreid. T4-kandidaten-tabel bijgewerkt (m14 afgehandeld). Cross-refs naar cross-category-mappings + T3 toegevoegd. Status-historie-rij toegevoegd
- [[brain__concepts__cross-category-mappings]] *(nieuw, kandidaat v1.3.1-precedent, confidence high)* — Cross-category-rationale: wanneer subject en object van een SKOS-mapping ontologisch verschillende categorieën zijn (control ↔ legal-obligation), is `relatedMatch` de associatieve basislijn. broad/narrowMatch is categorie-fout in de meeste gevallen; closeMatch-uitzondering op retrieval-interchangeability; exactMatch structureel uitgesloten. T3-empirisch bewijs: 0/5 cluster-convergentie naar narrowMatch op 31 m14-paren. Distinctie van T2 (m10): m10 = framework-specifieke convergentie (zelfde categorie); m14 = categorie-specifieke non-convergentie. Cluster-discipline-bewijslast complementair (binnen één categorie; cross-category-rationale tussen categorieën). closeMatch-uitzondering-precedent: T3-014 governance/policy + T3-026 incident-planning. Kandidaat-formalisering Protocol v1.3.1 (NIET nu uitvoeren — masterchat-werk). Cross-refs naar D4, T3, skos-beoordelings-protocol, cluster-discipline-bewijslast, mapping-bron-disclaimer-effect, H36
- [[brain__modules__M14_avg-gdpr]] *(update)* — SKOS-mapping-stand-post-T3-sectie toegevoegd: 2 closeMatch + 0 broadMatch + 29 relatedMatch (eindstand v4.6.3). Per-cluster-stand (5 AVG-clusters) gedocumenteerd. T3-mutaties expliciet (T3-001 + T3-002). Cross-category-rationale als T3-leerpunt gerefereerd. File-hash-mutatie m14-avg-gdpr.ttl v4.6.2 → v4.6.3. Bronlicentie-sectie uitgebreid met evidence-bronnen ISO 27701:2025 + 27002:2022 + AVG EUR-Lex. related-frontmatter geheel uitgebreid (was leeg op SKOS-context); 6 wikilinks. sources-frontmatter toegevoegd
- [[brain__concepts__concept-register]] *(update)* — Drie bestaande concept-rijen bijgewerkt voor T3-update (skos-beoordelings-protocol naar v1.3 FINAL; mapping-bron-disclaimer-effect met T3-inactief-context; cluster-discipline-bewijslast met T3-complementair-context); één nieuwe rij toegevoegd (cross-category-mappings). Cluster-sectie "SKOS-kwaliteits-methode" uitgebreid van T1+T2-cluster naar T1+T2+T3-cluster. D-cross-reference-tabel + sprint-cross-reference-tabel bijgewerkt

**Deel C — Cross-category-precedent vastleggen:**

Uitgevoerd via [[brain__concepts__cross-category-mappings]] *(nieuw, kandidaat v1.3.1-precedent)*. Concept-bestand markeert expliciet:
- Status: kandidaat-formalisering voor Protocol v1.3.1
- Niet uitgevoerd in T3 (Tech-rol-grens)
- **Niet uitgevoerd in Brein-cyclus iteratie 15** (formalisering blijft masterchat-werk; Brein legt het principe als T3-empirisch precedent vast in vault)
- Aanbevolen voor masterchat-besluit bij volgende sprint-scoping

**Deel D — Werkflow-wijziging vastleggen:**

- [[brain__workflow__commit-push-werkverdeling]] *(nieuw, confidence high)* — Werkflow-wijziging 28-05-2026: masterchat mag voortaan zelf committen + pushen naar de repo. Vastgesteld door Steven. Onveranderd: subagents (Tech/Brein/Dashboard) committen NOOIT zelfstandig — invariant blijft hard. Onderbouwing invariant (disclosure-discipline, scope-discipline, cross-chat-state, niet-omkeerbare hist). Pending documentatie-bijwerking expliciet genoemd als masterchat-actie bij volgende versie-cut (projectinstructie v1.11 + volgend overdrachtsrapport) — NIET een Brein-taak. Cross-refs naar zes-chat-architectuur, sprint-protocollen, opleveringsprotocol, scope-discipline
- [[brain__workflow__workflow-register]] *(update)* — Workflow-rij toegevoegd voor commit-push-werkverdeling. Workflow-aantal-totaal: 6 → 7. Post-sprint-cluster aangevuld

**Deel B — Log + Index (afsluiten):**

- [[brain__log]] *(deze entry)* — nieuwste entry bovenaan, iteratie 15
- [[brain__index]] *(update)* — vault-staat-tabel rij iteratie 15 toegevoegd; baseline van v4.6.2 → v4.6.3; status-overzicht-ontologie ververst; v4.6.3 wijzigingen-blok bijgevoegd; v4.6.2 verschoven naar vorige baseline; H-register-entry-blok bijgewerkt (H36 resolved); cross-ref-overzicht uitgebreid met T3 + cross-category-mappings + commit-push-werkverdeling; volgende-fase-status bijgewerkt naar iteratie 15

**File-count iteratie 15:**

| Onderdeel | Nieuw | Update | Totaal |
|---|---:|---:|---:|
| Deel A errata-rapporten | 0 | 2 (t3-stap3-eindrapport + patch-rapport-v4_6_3) | 2 |
| Deel B T3-sprint | 1 | 1 (sprint-register) | 2 |
| Deel B D04 | 0 | 1 (D04) | 1 |
| Deel B H-items | 0 | 4 (H36, H39, H41, H-register) | 4 |
| Deel B concepts | 0 | 2 (skos-protocol, concept-register) | 2 |
| Deel B modules | 0 | 1 (M14) | 1 |
| Deel C cross-category-mappings | 1 | 0 | 1 |
| Deel D commit-push-werkverdeling | 1 | 1 (workflow-register) | 2 |
| Deel B log + index | 0 | 2 (log + index) | 2 |
| **Totaal brain-vault** | **3** | **11** | **14** |
| Plus errata rapporten | — | 2 | 2 |
| **Grand total** | **3** | **13** | **16** |

(Bestandstelling brain-vault excl. errata-rapporten — die staan in `output/reports/` en zijn formeel geen vault-bestanden.)

**Cross-referentie-verificatie (Brein-discipline):**

- [[brain__sprints__T3-skos-bidirectional-audit-m14]]: related-frontmatter wijst naar T2, T1, D04, H36, H39, H41 (alle bestaand), skos-beoordelings-protocol (bestaat), cross-category-mappings (nieuw, geen forward-rot), mapping-bron-disclaimer-effect (bestaat), cluster-discipline-bewijslast (bestaat), M14_avg-gdpr (bestaat). Alle targets aanwezig in vault na iteratie 15
- [[brain__concepts__cross-category-mappings]]: related-frontmatter wijst naar D04, T3, skos-beoordelings-protocol, cluster-discipline-bewijslast, mapping-bron-disclaimer-effect, H36 — alle aanwezig na iteratie 15
- [[brain__workflow__commit-push-werkverdeling]]: related-frontmatter wijst naar zes-chat-architectuur, sprint-protocollen, opleveringsprotocol, scope-discipline — alle aanwezig
- D04: related-frontmatter uitgebreid met T3 + cross-category-mappings — alle aanwezig na iteratie 15
- H36: title + status + related-frontmatter consistent met fully-closed-status; T3 + cross-category-mappings + patch-rapport-v4_6_3 + t3-stap3-eindrapport toegevoegd
- H39: related-frontmatter uitgebreid met T3 + patch-rapport-v4_6_3 — alle aanwezig
- H41: related-frontmatter uitgebreid met T3 + patch-rapport-v4_6_3 — alle aanwezig
- skos-beoordelings-protocol: related-frontmatter uitgebreid met T3 + cross-category-mappings — alle aanwezig
- M14: related-frontmatter uitgebreid (van 1 naar 6 wikilinks); was zeer minimaal vóór iteratie 15
- H-register: H36 in Resolved-tabel + iteratie-15-status-mutaties-sectie; H39 + H41 in iteratie-15-mutaties-sectie; H-items-per-D-decision-tabel H36 fully closed onder D4
- sprint-register: T3-rij in major-milestones (active) + detail-tabel + v4.6.3 baseline-metrics-blok + multiplier-tabel + D-cross-reference-tabel + geplande-sprints-tabel allen consistent
- concept-register: nieuwe entry-rij (cross-category-mappings) + drie bestaande rijen bijgewerkt + SKOS-kwaliteits-methode-cluster bijgewerkt + D-cross-references + sprint-cross-references
- workflow-register: nieuwe entry-rij (commit-push-werkverdeling) + post-sprint-cluster aangevuld

**Pre-push disclosure-check (Protocol 14, 5 categorieën) op alle nieuwe/gewijzigde brain-bestanden:**

- (1) **Organisatie-naam:** niet genoemd in enige nieuw of geüpdatet bestand. "De organisatie" of "Rijksoverheidsorganisatie" niet eens gebruikt
- (2) **Persoonsnamen:** alleen Steven Bouwmeester (publieke projecteigenaar) waar relevant in commit-push-werkverdeling-workflow. Geen andere namen
- (3) **Lokale paden:** alleen `/Users/stevenbouwmeester/grc-kennismodel/` (project) en `/Users/stevenbouwmeester/grc-sources-licensed/` (NEN-licentie) — referenties via T3-rapporten + M14-bronlicentie-sectie + sprint-bestand. Geen credentials in paden
- (4) **Credentials / TLD / e-mail-domeinen:** geen
- (5) **NEN-tekst-fragmenten verbatim >10 woorden:** geen. Alle ISO-citaten zijn parafrase + clausule-verwijzing. Control-name-strings ("Beleidsregels IB", "Use of cryptography", "Plannen incidentbeheer", "Response to information security incidents", "Application security requirements" e.d.) zijn factuele identifier-strings op control-name-niveau, geen guidance- of Control+Purpose-tekst. AVG-artikel-parafrases via m14-rdfs:comment (project-vault, niet NEN-licentie). Strikt gehandhaafd vanwege risico-vermelding in instructie discipline-sectie

**Cross-referentie-integriteits-check uitkomst:**

- Geen dangling wikilinks ontdekt in nieuwe of geüpdatete bestanden
- Alle nieuwe bestanden (T3-sprint, cross-category-mappings, commit-push-werkverdeling) hebben volledige cross-referenties naar bestaande targets
- Registers (sprint-register, H-register, concept-register, workflow-register) consistent bijgewerkt met nieuwe entries en status-mutaties
- Baseline-cijfers M14 SKOS-distributie (2 close / 0 broad / 29 related = 31 totaal) consistent met sprint-bestand + patch-rapport v4.6.3 §0.2
- Index baseline-metrics v4.6.3 consistent met sprint-register baseline-metrics-blok + patch-rapport v4.6.3 §0.1
- H36-status-mutatie consistent over H36-bestand, H-register status-overzicht, H-register active-tabel (leeg), H-register resolved-tabel, H-register iteratie-15-status-mutaties-sectie, H-register H-items-per-D-decision-tabel, log-entry, index-entry

**Open punten voor masterchat (niet door Brein opgepakt):**

1. **Protocol v1.3.1-formalisering** — cross-category-mappings-principe expliciet opnemen in `docs/skos-beoordelings-protocol-v1_3_1.md` of als §3.4-aanvulling op v1.3 — masterchat-werk bij volgende sprint-scoping. Brein heeft alleen het empirisch precedent vastgelegd in concept-bestand
2. **T4-scope-bepaling** — andere SKOS-mapping-clusters (cross-bron-overlap-105, m11, m17, m09, m16 VIRBI, m12 DORA, framework-niveau)
3. **Projectinstructie v1.11-bijwerking** — commit-push-werkverdeling-update (28-05-2026 masterchat-commit-autonomie) opnemen in §ZEVEN CHATS + gedeelde gedragsregels-sectie
4. **Volgend overdrachtsrapport** — werkflow-update incorporeren
5. **Locatie Spoor B-prototype `grc-dashboard-v3-2.html`** — open sinds iteratie 12; niet in deze cyclus opgepakt
6. **Confidence-verhoging mapping-bron-disclaimer-effect** — vereist tweede onafhankelijke bron-bevestiging
7. **Dashboard-inhaalslag** — 7 sprints achterstand (parallel, niet-blokkerend)

**Karakter-bevestiging:** geen architectuurbeslissingen autonoom genomen door Brein. H36-status-revisie volgt T3-scope-afsluiting (m14 afgehandeld). H39-versterking volgt T3-empirisch bewijs (bidirectional). H41-T3-bevestiging is informatief (status ongewijzigd; geen masterchat-besluit tot revisie of activering). D4-tekst onveranderd (alleen toepassings-precedent uitgebreid). Cross-category-mappings als concept gemarkeerd als **kandidaat v1.3.1-precedent** — formele protocol-tekst-wijziging is masterchat-werk en NIET door Brein uitgevoerd. Commit-push-werkverdeling-workflow legt vastgestelde werkflow-wijziging vast zonder eigen interpretatie; subagent-invariant blijft hard. Geen ontologie-impact. Geen autonome commits. Errata-correctie is surgisch (T-historie bewaard, §-detail-tekst niet herschreven, patch-impact onveranderd). Discipline-conform instructie-rol-grens (Brein-rol-afbakening + Protocol 11 + Protocol 14 + Protocol v1.3 §10.4).

**Volgende:** Steven inspecteert Deel A errata + Deel B brain-update + Deel C nieuw concept + Deel D nieuw workflow + commit handmatig (per deel of cumulatief — voorstel: één commit per deel of één cumulatieve commit voor brein-cyclus-iteratie-15). Daarna T4-scope-bepaling of Protocol v1.3.1-formalisering in verse masterchat-sessie.

---

## 2026-05-27 — Iteratie 14: post-T2-Brein-cyclus (T2-sprint + Protocol v1.3-draft + H36 m10-component closed + H41 nieuw + cluster-discipline-bewijslast-concept)

**Derde post-migratie Brein-cyclus** uitgevoerd via brein-subagent in Claude Code. Administratieve nasleep van T2-sprint (SKOS-bidirectional-audit m10, patch v4.6.2, opgeleverd 27 mei 2026 dezelfde dag) + projectinstructie v1.10 + Protocol v1.3-draft. T2 is **tweede post-migratie productie-sprint** en eerste sprint die Protocol v1.2 bidirectional in productie heeft toegepast.

**Karakter:** uitsluitend administratieve verwerking van besluiten die in T2 al waren genomen (Tech-uitvoering volledig autonoom via Protocol 17 v1.3 NEN-Tech-autonomie + masterchat-protocol-vaststelling + Steven-patch-toepassing). Geen architectuur-wijzigingen autonoom door Brein; alleen status-mutaties + nieuwe H-registratie per masterchat-besluit projectinstructie v1.10. 12 bestanden geraakt: 3 nieuw + 9 update.

**WP1 — T2-sprint registreren:**

- [[brain__sprints__T2-skos-bidirectional-audit-m10]] *(nieuw)* — Tweede post-migratie productie-sprint. Scope: 118 m10 ctrl→compl-paren over 10 NIS2-art.21-letter-clusters (m14-deferral per Optie C). Vier-stappen-uitvoering: pre-sprint-inventarisatie (149 → 118 m10 + 31 m14-deferral) → pilot 8 paren over 10 clusters → pre-Stap-4 errata-correctie (helper-script-classificatie autoritatief) → Stap 3 hoofd-uitvoering 110 paren (alle 10 clusters → broadMatch) → Stap 4 productie-patch v4.6.2 (65 mutaties = 32 downgrade + 33 upgrade, 13/13 GO-criteria groen). Sprint-multiplier 2,32× t.o.v. T1. Cross-refs: D4 + D4.1, H36, H39, H41, Protocol v1.0/v1.2/v1.3, bidirectional-audit-symmetrie, cluster-discipline-bewijslast.
- [[brain__sprints__sprint-register]] *(update)* — T2-rij toegevoegd als active; T1 verschoven naar superseded. v4.6.2 baseline-metrics-blok geheel (predicate-substitutie: closeMatch −32, broadMatch +65, relatedMatch −33; SKOS-totaal 1.798 ongewijzigd). Multiplier-tabel uitgebreid met T1 + T2-rijen (beide 0× — kwaliteits-sprints; T2-mutatie-multiplier 2,32× t.o.v. T1). Geplande-sprints-tabel: T2 vervangen door m14-T-sprint. D-cross-reference-tabel: T2-rij D4.1-cluster-niveau-toepassings-precedent.

**WP2 — D04-decision: D4.1-toepassings-precedent uitbreiden:**

- [[brain__decisions__D04_skos-cross-framework]] *(update)* — D4.1-toepassings-precedent uitgebreid van paar-niveau (T1) naar cluster-niveau (T2, 118 paren over 10 m10-clusters). Bij homogene cluster-bron-stack volstaat één D4.1-bevestiging per cluster. Heterogene clusters vereisen per-paar-toets. D4-tekst zelf onveranderd; alleen precedent-uitbreiding gedocumenteerd. Status-historie-rij toegevoegd. related-frontmatter uitgebreid met T2, H41, cluster-discipline-bewijslast.

**WP3 — H-items bijwerken:**

- [[brain__architecture__H36_skos-exactmatch-ctrl-compl-audit]] *(update)* — Status closed (iteratie 13) → **active (m10 closed, m14 open subtask)** (iteratie 14). T2 voltooide m10-scope volledig (cumulatief 93 m10-paren via T1+T2); m14 (31 compl→ctrl-paren in `m14-avg-gdpr.ttl`, omgekeerde modelleringsconventie) blijft open subtask voor toekomstige T-sprint. T2-uitkomst-sectie toegevoegd met 65 mutaties + 10/10 cluster-convergentie + 0 NEN-uitzonderingen. Architectuur-impact-tabel uitgebreid (D4 + D4.1, H39, H41, methode-protocol, cluster-discipline-bewijslast). Status-historie-rij toegevoegd. related-frontmatter uitgebreid met T2, H41, cluster-discipline-bewijslast.
- [[brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing]] *(update)* — Status onveranderd (parked). Versterking T2-sectie toegevoegd: T2 bevestigt SHACL-blinde-vlek op 118-paren-schaal; 65 SKOS-predicate-mutaties → Δ SHACL = 0 in alle drie metingen (SECTIE A / B / COMBINED). Trigger-relevantie verder verhoogd. Status-historie-rij toegevoegd.
- [[brain__architecture__H41_skos-axioma-set-handling]] *(nieuw)* — Nieuw geregistreerd parked H-item per masterchat-besluit projectinstructie v1.10. T1-werkflow-leerpunt (zonder H-registratie) wordt geactiveerde H-item door T2-empirisch bewijs: post-OWL-RL Δ-triples = 0 ondanks 65 SKOS-predicate-mutaties. `owlrl`-package laadt in canonieke configuratie geen SKOS-axiomas (S46-symmetrie, S47-transitiviteit). Confidence high op feitelijke vaststelling; toekomstige beslissing wel/niet activeren blijft open. Trigger: substantiële SKOS-mapping-uitbreiding waar symmetrie/transitiviteit auditief relevant wordt. Cross-refs: H37 (open-ontologies-MCP), H38 (HermiT-equivalentie), H39 (SHACL-uitsplitsing), Protocol v1.3 §12.
- [[brain__architecture__H-register]] *(update)* — Status-overzicht: nieuwe categorie "Active (gedeeltelijk closed)" met H36; Parked-aantal 6 → 7 (H41 toegevoegd); Resolved 5 → 4 (H36 weer uit resolved). Active-tabel + Parked-tabel + iteratie-14-status-mutaties-sectie + H-items-per-D-decision-tabel allemaal bijgewerkt. Reikwijdte-vermelding bij H36-status-correctie expliciet opgenomen.

**WP4 — Concepts bijwerken + nieuw concept:**

- [[brain__concepts__skos-beoordelings-protocol]] *(update)* — Versie-evolutie expliciet: v1.0 (T1) → v1.2 (T2 operationeel) → v1.3 DRAFT. Sectie "T2-toepassing — 65 bidirectional mutaties over 10 clusters" toegevoegd. Nieuwe sub-sectie "Bidirectional-audit-symmetrie" als sub-aspect Protocol v1.2 §3.1-§3.2 met sterkte-ordening-tabel + mutatie-richting-classificatie + T2-empirisch bewijs (Brein-keuze B: sub-sectie i.p.v. apart concept-bestand — zie motivering). Protocol-versie-roadmap uitgebreid met zeven v1.3-verfijningen + v1.3-werkflow-discipline §10.2-§10.5 als gedragsregel in projectinstructie v1.10. T3 + m14-relevantie-tabel uitgebreid met nieuwe kandidaten. Cross-refs naar H41 + cluster-discipline-bewijslast toegevoegd.
- [[brain__concepts__mapping-bron-disclaimer-effect]] *(update)* — Nieuwe sectie "D4.1-toepassing op cluster-niveau — T2" toegevoegd. Bron-erf-relatie ENISA TIG R285 + CBW-Mapping-UV R3 expliciet als één-context-keten erkend. Reikwijdte-beperking (homogene vs heterogene clusters) gedocumenteerd. Status-historie-rij voor T2-cluster-niveau-toepassings-precedent toegevoegd. Cross-refs naar T2 + cluster-discipline-bewijslast toegevoegd.
- [[brain__concepts__cluster-discipline-bewijslast]] *(nieuw, confidence high)* — Bewijslast-asymmetrie voor uitzonderingen binnen veel↔1-clusters. Drie scenario's: sterker mapping (streng bewijs vereist via bilaterale containment), zwakker mapping (streng bewijs vereist via C3-falen), behoud cluster-default (geen aanvullende bewijslast). T2-empirisch bewijs: 10 heuristiek-flags op 6 cluster-leden → 0 succesvolle uitzonderingen. Cluster-cardinaliteit als structurele blokkade voor sterker mapping. Heuristiek-screening als prioriteits-mechanisme (niet beslis-mechanisme). Werkflow-discipline rond bewijslast in zes stappen. Cross-refs naar D4 + D4.1, T1, T2, skos-beoordelings-protocol, mapping-bron-disclaimer-effect.
- [[brain__concepts__concept-register]] *(update)* — Twee bestaande concept-rijen bijgewerkt voor T2-update (skos-beoordelings-protocol + mapping-bron-disclaimer-effect); één nieuwe rij toegevoegd (cluster-discipline-bewijslast). Cluster-sectie "SKOS-kwaliteits-methode" uitgebreid van T1-cluster naar T1+T2-cluster. D-cross-reference-tabel + sprint-cross-reference-tabel bijgewerkt.

**WP5 — Log + Index:**

- [[brain__log]] *(deze entry)* — nieuwste entry bovenaan, iteratie 14.
- [[brain__index]] *(update)* — vault-staat-tabel rij iteratie 14 toegevoegd; baseline van v4.6.1 → v4.6.2; status-overzicht-ontologie ververst; cross-ref-overzicht uitgebreid met T2 + H41 + cluster-discipline-bewijslast.

**Motivering Brein-keuze A vs B voor bidirectional-audit-symmetrie:**

Briefing §1.4 vroeg om Brein-autonome keuze tussen (A) apart concept-bestand `brain__concepts__bidirectional-audit-symmetrie.md` of (B) sub-sectie in `brain__concepts__skos-beoordelings-protocol.md`. **Gekozen: B (sub-sectie).** Motivering:

- Bidirectional-audit-symmetrie is een methodisch sub-aspect van het SKOS-beoordelings-protocol, niet een eigenstandig concept-domein
- Het concept "skos-beoordelings-protocol" is reeds een methode-concept; symmetrie hoort daarbij (Protocol v1.2 §3.1 + §3.2)
- Cluster-discipline-bewijslast komt al apart in nieuw concept; twee parallel nieuwe concepten voor één T2-cluster zou de concept-vault uithollen
- Scope-passend voor T2 (één bewijscluster: 32 downgrade + 33 upgrade)
- Bij uitbreiding naar meerdere modules of bron-contexten kan dit alsnog uitgesplitst (toekomst-trigger documenteerd in concept)

**File-count iteratie 14:**

| WP | Nieuw | Update | Totaal |
|---|---:|---:|---:|
| WP1 T2-sprint | 1 | 1 (sprint-register) | 2 |
| WP2 D04 | 0 | 1 (D04) | 1 |
| WP3 H-items | 1 (H41) | 3 (H36, H39, H-register) | 4 |
| WP4 concepts | 1 (cluster-discipline-bewijslast) | 3 (skos-protocol, mapping-bron-disclaimer, concept-register) | 4 |
| WP5 log + index | 0 | 2 (log + index) | 2 |
| **Totaal** | **3** | **10** | **13** |

**Cross-referentie-verificatie (Brein-discipline):**

- [[brain__sprints__T2-skos-bidirectional-audit-m10]]: related-frontmatter wijst naar T1, D04, H36, H39, H41 (nieuw, geen forward-rot), skos-beoordelings-protocol, mapping-bron-disclaimer-effect, cluster-discipline-bewijslast (nieuw, geen forward-rot). Alle targets aanwezig in vault na iteratie 14.
- [[brain__architecture__H41_skos-axioma-set-handling]]: related-frontmatter wijst naar owl-rl-reasoning (bestaat), canonical-metrics (bestaat), skos-beoordelings-protocol (bestaat), T1, T2 (nieuw), D04 (bestaat). Cross-refs naar H37 + H38 + H39 expliciet in body-tekst.
- [[brain__concepts__cluster-discipline-bewijslast]]: related-frontmatter wijst naar skos-beoordelings-protocol, mapping-bron-disclaimer-effect, D04, T1, T2 — alle aanwezig. body-tekst-cross-refs consistent.
- D04: related-frontmatter uitgebreid met T2 + H41 + cluster-discipline-bewijslast — alle aanwezig na iteratie 14.
- H36: related-frontmatter uitgebreid met T2 + H41 + cluster-discipline-bewijslast — alle aanwezig.
- H39: related-frontmatter uitgebreid met T2 — aanwezig.
- skos-beoordelings-protocol: related-frontmatter uitgebreid met T2 + H41 + cluster-discipline-bewijslast — alle aanwezig.
- mapping-bron-disclaimer-effect: related-frontmatter uitgebreid met T2 + cluster-discipline-bewijslast — alle aanwezig.
- H-register: H36 expliciet in Active (gedeeltelijk closed)-tabel + iteratie-14-status-mutaties-sectie; H41 in Parked-tabel + iteratie-14-status-mutaties-sectie; H-items-per-D-decision-tabel H36 + H41 onder D4.
- sprint-register: T2-rij in major-milestones (active) + detail-tabel + v4.6.2 baseline-metrics-blok + multiplier-tabel + D-cross-reference-tabel + geplande-sprints-tabel allen consistent.
- concept-register: drie nieuwe entry-rijen + SKOS-kwaliteits-methode-cluster bijgewerkt + D-cross-references + sprint-cross-references.

**Pre-push disclosure-check (Protocol 14, 5 categorieën):**

- (1) Organisatie-naam: niet genoemd in enige nieuw of geüpdatet bestand. "De organisatie" of "Rijksoverheidsorganisatie" niet eens gebruikt.
- (2) Persoonsnamen: alleen Steven Bouwmeester (publieke projecteigenaar). Geen andere namen.
- (3) Lokale paden: alleen `/Users/stevenbouwmeester/grc-kennismodel/` (project) en `/Users/stevenbouwmeester/grc-sources-licensed/` (NEN-licentie) — beide in T2-rapporten gerefereerd, hier overgenomen voor ISO-bron-verwijzing.
- (4) Credentials / TLD / e-mail: geen.
- (5) NEN-tekst-fragmenten >10 woorden: geen verbatim ISO/NEN-tekst opgenomen in brain-bestanden. Verwijzingen naar ISO 27002:2022 §-clausules (bv. §5.2, §5.4, §5.30, §5.36, §6.5, §8.3, §8.24) zijn parafrases of pure clausule-referenties zonder citaat. Strikt gehandhaafd vanwege risico-vermelding in briefing §3.

**Open punten voor masterchat (niet door Brein opgepakt):**

1. **Protocol v1.3-vaststelling** — DRAFT-status; vaststelling pending bij eerstvolgende sprint-scoping (T3 of m14)
2. **m14-T-sprint-scope** — open subtask van H36; verse masterchat-sessie nodig voor scope-bepaling incl. AVG-cross-walk-bron-upload-keuze
3. **T3-scope-bepaling** — andere SKOS-mapping-clusters (cross-bron-overlap-105, m11, m17, m09)
4. **D4-aanvulling-overweging confidence-verhoging** — verhoging naar high vereist tweede onafhankelijke bron-bevestiging (NIST OLIR of ISO Annex F-tekstverificatie)
5. **Locatie Spoor B-prototype `grc-dashboard-v3-2.html`** — open sinds iteratie 12; niet in deze cyclus opgepakt conform briefing §5

**Karakter-bevestiging:** geen architectuurbeslissingen autonoom genomen; H41-registratie volgt masterchat-besluit (projectinstructie v1.10); H36-status-revisie volgt T2-scope-realiteit; geen D-decision-tekst-wijzigingen (alleen toepassings-precedent); geen Protocol v1.3-tekst-wijziging (DRAFT, vaststelling pending); geen ontologie-impact; geen autonome commits. Discipline-conform briefing §0-§7.

**Volgende:** Steven inspecteert WP1-WP5 en commit handmatig (per WP of cumulatief — voorstel staat in eindrapport-output). Daarna Protocol v1.3-vaststelling of m14-T-sprint-scoping of T3-scope-bepaling in verse masterchat-sessie.

---

## 2026-05-26 — Iteratie 13: post-T1-Brein-cyclus (T1-sprint + methode-protocol-concept + H36 closed + drie sprint-protocollen)

**Tweede post-migratie Brein-cyclus** uitgevoerd via brein-subagent in Claude Code. Administratieve nasleep van T1-sprint (SKOS-kwaliteitsanalyse Fase 1, patch v4.6.1, opgeleverd 26 mei 2026 dezelfde dag). T1 is **eerste post-migratie productie-sprint** en eerste sprint waarvoor Brein-cyclus regulier verloopt na sprint-afsluiting.

**Karakter:** uitsluitend administratieve verwerking van besluiten die in T1 al waren genomen (Tech-uitvoering + masterchat-NEN-PK-toetsen + Steven-patch-toepassing). Geen architectuur-wijzigingen, geen ontologie-impact, geen D-decision-mutaties. 11 bestanden geraakt: 3 nieuw + 8 update.

**WP1 — T1-sprint registreren:**

- [[brain__sprints__T1_skos-kwaliteitsanalyse-fase-1]] *(nieuw)* — Eerste post-migratie productie-sprint. Scope: 28 ctrl:↔compl: SKOS-exactMatch-paren in `m10-nis2-ext.ttl`. Uitkomst: 28× herclassificatie naar broadMatch via patch v4.6.1. Sprint-duur ~5 uur (raming 3-4, +25% door tooling-incident applier). Methode-protocol v1.0 vastgesteld. D4-conformance verbeterd. Vijf overhandigings-momenten Tech↔Masterchat succesvol. Productie-fase actief.
- [[brain__sprints__sprint-register]] *(update)* — Nieuwe rij T1 (v4.6.1) als active; v4.6.0 verschuift naar superseded. Baseline-metrics-blok v4.6.1 toegevoegd (predicate-mutatie zonder triple-totaal-impact: exactMatch 46 → 18, broadMatch 38 → 66, SKOS-totaal 1.798 ongewijzigd). Geplande-sprints-tabel bijgewerkt (T2/T3-kandidaten). Sprint-protocollen-tabel uitgebreid met Protocol 14/15/16/17.

**WP2 — Methode-protocol als concept:**

- [[brain__concepts__skos-beoordelings-protocol]] *(nieuw)* — Concept-bestand voor methode-protocol v1.0. Onderscheid expliciet: operationeel document `docs/skos-beoordelings-protocol-v1_0.md` blijft autoritatief; concept-bestand beschrijft methode-overzicht + architectuur-context + T2/T3-relevantie. Cross-references naar D4, T1, H36, mapping-bron-disclaimer-effect. Protocol-versie-roadmap (v1.0 huidig, v1.1 bij T2-start, v2.0 toekomst) opgenomen.

**WP3 — H-items bijwerken:**

- [[brain__architecture__H36_skos-exactmatch-ctrl-compl-audit]] *(update)* — Status parked → **closed**. Uitkomst-sectie toegevoegd (28× broadMatch, evidence-niveau 1, cluster-consistentie, D4-verbetering). H41-kandidaat (SKOS-axioma-set / skos:S46) gemarkeerd als T1-leerpunt, niet als nieuw H-item. Status-historie-rij toegevoegd.
- [[brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing]] *(update)* — Status onveranderd (parked). Versterking-sectie toegevoegd: T1-pre-sprint-inventarisatie Vraag D bevestigt SHACL-blinde vlek op alle 28 ctrl:↔compl:-paren. Trigger-relevantie verhoogd voor T2 (uitbreiding 121-set). Status-historie-rij toegevoegd.
- [[brain__architecture__H-register]] *(update)* — Status-overzicht-tabel: Parked 7 → 6, Resolved 4 → 5 (incl. H36). H-items-per-D-decision-tabel: D4-rij gemarkeerd als afgehandeld. Resolved-tabel: H36-rij toegevoegd met expliciete verwijzing dat bestand met closed-status behouden blijft. Versterkings-sectie iteratie 13 toegevoegd na iteratie-12-sectie, met expliciete H41-kandidaat-NIET-registratie.

**WP4 — ENISA-disclaimer-effect als concept (Optie A gekozen):**

- [[brain__concepts__mapping-bron-disclaimer-effect]] *(nieuw, confidence medium)* — Generaliseerbaar patroon: autoritatieve mapping-bronnen met expliciete non-equivalence-disclaimer ondergraven `skos:exactMatch` zelfs bij sluitende C1-C3. Eerste-bewijs-cluster: ENISA TIG regel 285. Kandidaat-bronnen vermoed (NIST OLIR, ISO Annex F) maar niet geverifieerd in dit project. D4-aanvulling-overweging open. Confidence-verhoging naar high vereist tweede onafhankelijke bron of D4-formalisatie.
- [[brain__concepts__concept-register]] *(update)* — Twee nieuwe rijen in snelle navigatie (skos-beoordelings-protocol + mapping-bron-disclaimer-effect). Nieuw cluster "SKOS-kwaliteits-methode (T1-cluster)". D-cross-reference-tabel en sprint-cross-reference-tabel uitgebreid.

**Motivering Optie A (concept-bestand nu vs. Optie B uitstellen tot T2):**

- Masterchat-aanbeveling expliciet Optie A
- Patroon-herbruikbaarheid hoog (alle cross-norm-mapping-bronnen kandidaat)
- T1-sprint-bestand verwijst er al naar — consistente vault-structuur vereist concept-bestand
- Confidence-status medium (niet hoog) markeert dat tweede bron-bevestiging nog ontbreekt — voorkomt over-claiming
- Verlies-risico bij Optie B reëel: tussen T1 en T2 kunnen masterchat-sessies plaatsvinden waarbij dit patroon opnieuw opduikt zonder centrale documentatie

**WP5 — Drie sprint-protocollen formeel:**

- `docs/sprint-protocols.md` *(update)* — Drie protocollen toegevoegd tussen Protocol 14 en GR-gedragsregel, conform bestaande nummering. Versie 1.1 → 1.2.
  - Protocol 15 — Tech levert werkbare applier (T1 §8 leerpunt 5)
  - Protocol 16 — Lokatie verificatie-scripts expliciet in patch-rapport (T1 §8 leerpunt 6)
  - Protocol 17 — NEN-werkverdeling Tech↔Masterchat (T1 §8 leerpunt 4)
  - Overzichts-tabel uitgebreid van 14 naar 17 protocollen + GR
  - Wijzigingsgeschiedenis-rij 1.2 toegevoegd

**WP6 — Register-coherentie + log/index:**

- [[brain__log]] *(deze entry)* — nieuwste entry bovenaan, iteratie 13.
- [[brain__index]] *(update)* — vault-staat-tabel rij iteratie 13 + totaal brain-bestanden ~107 → ~110 + status-overzicht-ontologie naar v4.6.1 baseline + volgende-fase-sectie bijgewerkt (T1 afgerond, T2-scoping als volgende activiteit).

**File-count iteratie 13:**

| WP | Nieuw | Update | Totaal |
|---|---:|---:|---:|
| WP1 T1-sprint | 1 | 1 (sprint-register) | 2 |
| WP2 methode-concept | 1 | 0 | 1 |
| WP3 H-items | 0 | 3 (H36, H39, H-register) | 3 |
| WP4 disclaimer-concept | 1 | 1 (concept-register) | 2 |
| WP5 sprint-protocollen | 0 | 1 (sprint-protocols.md) | 1 |
| WP6 log + index | 0 | 2 (log + index) | 2 |
| **Totaal** | **3** | **8** | **11** |

**Cross-referentie-verificatie:**

- Alle drie nieuwe bestanden hebben `related:`-frontmatter die naar bestaande bestanden wijst.
- T1-sprint-bestand verwijst naar [[brain__modules__M10_nis2-ext]] (bestaat als `brain/brain__modules__M10_nis2-ext.md`).
- T1-sprint-bestand verwijst naar [[brain__concepts__skos-beoordelings-protocol]] (nieuw in deze cyclus, geen forward-rot).
- T1-sprint-bestand verwijst naar [[brain__concepts__mapping-bron-disclaimer-effect]] (nieuw in deze cyclus, geen forward-rot).
- skos-beoordelings-protocol concept-bestand verwijst naar mapping-bron-disclaimer-effect (nieuw in deze cyclus, geen forward-rot).
- mapping-bron-disclaimer-effect concept-bestand verwijst naar skos-beoordelings-protocol (nieuw in deze cyclus, geen forward-rot).
- H36-bestand `related:`-frontmatter uitgebreid met T1, skos-beoordelings-protocol, mapping-bron-disclaimer-effect. Status closed weerspiegeld in zowel frontmatter als statussectie als status-historie-tabel.
- H39-bestand `related:`-frontmatter uitgebreid met T1; status parked behouden maar versterking gedocumenteerd.
- H-register: H36 verschijnt nu in Resolved-sectie, **niet** in Parked-sectie; iteratie-13-mutaties-sectie expliciet aanwezig.
- Sprint-register: T1 als active in major-milestones + detail-tabel; baseline-metrics-blok v4.6.1 nieuw + v4.6.0 als vorige active behouden.
- Concept-register: drie nieuwe rijen + nieuwe cluster "SKOS-kwaliteits-methode (T1-cluster)".
- Sprint-protocols.md: tabel-totaal-aanpassing (14 → 17 protocollen + GR) consistent in inleidende tabel én uitwerkings-secties én wijzigingsgeschiedenis.

**H41-kandidaat niet geregistreerd (conform briefing):**

SKOS-axioma-set / `skos:S46` symmetrie-afwezigheid (owlrl-package laadt geen SKOS-axiomas, dus `skos:exactMatch is owl:SymmetricProperty` wordt niet geïnferreerd). Alle 28 ctrl:→compl: mappings asymmetrisch gemodelleerd (0 inverse). Geen impact op T1-patch (predicate-mutatie blijft asymmetrisch). Markering als T1-werkflow-leerpunt op drie plekken: H36-bestand (kandidaat-overweging-sectie), H-register (iteratie-13-versterkings-sectie), T1-sprint-bestand (H-impact-sectie). **Geen nieuw H-item nu.** Trigger voor latere herregistratie: overstap-besluit owlrl-incl-SKOS-axioma-reasoning.

**Karakter-bevestiging:** geen architectuurbeslissingen genomen; geen ontologie-impact; geen D-mutaties; geen scope-pauzes. Discipline-conform. Briefing strict gevolgd.

**Pre-push disclosure-check** (Protocol 14): toegepast op alle 3 nieuwe bestanden + 8 updates — geen organisatie-naam, geen persoonsnamen anders dan Steven, geen credentials, geen lokale paden, geen NEN-tekst-citaten (alleen verwijzingen naar PK).

**Open punten voor masterchat (niet door Brein opgepakt):**

1. **D4-aanvulling-uitvoering** — concept `mapping-bron-disclaimer-effect` is geregistreerd met confidence medium; daadwerkelijke D4-tekstwijziging is masterchat-werk bij T2-voorbereiding
2. **Protocol-v1.1-tekst** voor skos-beoordelings-protocol — masterchat-werk bij T2-start
3. **T2-scope-bepaling** — verse masterchat-sessie volgens briefing
4. **Locatie Spoor B-prototype `grc-dashboard-v3-2.html`** — open sinds iteratie 12; niet in deze cyclus opgepakt conform briefing §10

**Volgende:** Steven inspecteert WP1-WP6 en commit handmatig (per WP of cumulatief — voorstel staat in eindrapport-output). Daarna T2-scoping in verse masterchat-sessie.

---

## 2026-05-26 — Iteratie 12: post-v4.6.0 polish-mini-sprint (H36–H40 + pre-push-protocol + productlijn-concept)

**Eerste post-migratie Brein-cyclus** uitgevoerd via brein-subagent in Claude Code (Anthropic). Polish-mini-sprint na v4.6.0 + Fase 0 GitHub-MCP-setup leverden vijf H-kandidaten en twee structurele documentatie-acties op die administratieve schuld waren geworden. Deze iteratie klaart het bord vóór de eerste post-migratie-test-sprint (T1).

**Karakter:** uitsluitend administratieve verwerking van besluiten die elders al waren genomen (masterchat + handovers). Geen architectuur-wijzigingen, geen ontologie-impact, geen D-decision-mutaties. 11 bestanden geraakt: 6 nieuw + 5 update.

**WP1 — vijf H-items registreren (H36–H40):**

- [[brain__architecture__H36_skos-exactmatch-ctrl-compl-audit]] *(nieuw)* — 28 ctrl→compl `skos:exactMatch`-pairs, audit-vraag voor SKOS-kwaliteitsanalyse-sprint of externe audit. Status: parked. Trigger: SKOS-kwaliteitsanalyse-sprint. Bron: sessie-rapport v2.0 §9.1.
- [[brain__architecture__H37_open-ontologies-mcp]] *(nieuw)* — open-ontologies MCP-server (Rust + Oxigraph + tableaux) als toolchain-alternatief voor rdflib + owlrl + pySHACL. Status: parked. Trigger: aangetoonde OWL RL-limitatie of >50.000 triples (huidig 44.907). Bron: sessie-rapport v1.0.
- [[brain__architecture__H38_owlrl-vs-hermit-equivalentie]] *(nieuw)* — geen HermiT-run sinds v4.0.0 op modulaire baseline; OWL RL ≡ HermiT-aanname niet aantoonbaar. Raakt D1, wijzigt D1 niet. Status: parked. Trigger: >10% triple-toename of nieuwe module of DL-conformance-twijfel. Bron: Fase 0 Tech-handover-rapport.
- [[brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing]] *(nieuw)* — 290 SHACL RUN 2 false-positives nog niet individueel uitgesplitst; masking-risico bij shape-wijziging. Status: parked. Trigger: rustige sprint als sanity-check of sprint die SHACL-shapes wijzigt. Bron: Fase 0 Tech-handover-rapport.
- [[brain__architecture__H40_dashboard-ui-renderdekking]] *(nieuw)* — grc-explorer-UI rendert <10% van JSON-export-velden; rdfs:comment + SourceAttribution + classificatie-attributen onzichtbaar. Status: parked. Trigger: UI-moderniseringssprint post-Fase 4. Scope: uitsluitend Spoor A explorer (zie WP3). Bron: Fase 0 Dashboard-handover-rapport.
- [[brain__architecture__H-register]] *(update)* — vijf nieuwe rijen onder Parked-categorie; nieuwe sectie "Nieuw geregistreerd in iteratie 12"; H-items-per-D-decision-tabel uitgebreid met toolchain-cluster (H37, H38), validatie-cluster (H39), dashboard-cluster (H40), D4 (H36), D1 (H38 — geen D1-wijziging).

**WP2 — pre-push disclosure-check als werkflow-regel:**

- `docs/sprint-protocols.md` *(update)* — Protocol 14 toegevoegd tussen Protocol 13 (Bron-typo-beleid) en GR (Property-semantiek-discipline). Aanleiding: PAT-blunder voorgaande sessie + handovers ongetoetst gepusht in Fase 0. Reikwijdte: alle subagents + Steven, vóór elke push van documenten met chat-historie of subagent-output. Niet retroactief. Versie 1.0 → 1.1.
- [[brain__workflow__opleveringsprotocol]] *(update)* — korte verwijzing naar Protocol 14 toegevoegd vóór Cross-references-sectie + wikilink naar sprint-protocollen.

**WP3 — productlijn-scheiding documenteren (Optie C):**

- [[brain__concepts__dashboard-productlijnen]] *(nieuw)* — `grc-explorer-*` (Spoor A — ontologie-graaf-verkenner, Cytoscape, beweegt mee met ontologie-versie) versus `grc-dashboard-*` (Spoor B — operationele werkmap, SQL.js + Chart.js, eigen versie-track). Discipline-paragraaf "niet vermengen". Cross-references naar [[brain__architecture__H40_dashboard-ui-renderdekking]], [[brain__concepts__skos-export-filter]], [[brain__concepts__namedindividual-telmethode]]. **Open punt**: locatie Spoor B-prototype in repo (Optie A eigen repo / B sources/spoor-b/ / C dashboard/spoor-b/) — wacht op masterchat-beslissing, Brein-subagent neemt geen eigen voorkeur in.
- [[brain__concepts__concept-register]] *(update)* — nieuwe rij in snelle navigatie + nieuwe cluster "Product-scope-discipline" + D-cross-reference-tabel + sprint-cross-reference-tabel.
- `CLAUDE.md` *(update)* — nieuwe korte sectie "Dashboard-productlijnen (Spoor A vs Spoor B)" tussen repo-structuur en brain-vault-organisatie (4-6 regels). Verwijst naar concept-bestand voor detail. Versie 1.3 → 1.4.

**WP4 — register-coherentie + log-iteratie 12:**

- [[brain__log]] *(deze entry)* — nieuwste entry bovenaan, iteratie 12.
- [[brain__index]] *(update)* — vault-staat-tabel rij iteratie 12 + totaal brain-bestanden bijgewerkt + "Volgende fase"-sectie heroverwogen (Brein-cyclus-pre-conditie nu voldaan; klaar voor T1-test-sprint).

**File-count iteratie 12:**

| WP | Nieuw | Update | Totaal |
|---|---:|---:|---:|
| WP1 H-items | 5 | 1 (H-register) | 6 |
| WP2 pre-push | 0 | 2 (sprint-protocols.md + opleveringsprotocol) | 2 |
| WP3 productlijn | 1 | 2 (concept-register + CLAUDE.md) | 3 |
| WP4 log + index | 0 | 2 (log + index) | 2 |
| **Totaal** | **6** | **7** | **13** |

**Cross-referentie-verificatie:**

- Alle vijf H-bestanden hebben `related:`-frontmatter die naar bestaande bestanden wijst (H36 → D4, skos-export-filter, sameAs-discipline; H37 → owl-rl-reasoning, canonical-metrics; H38 → D01, owl-rl-reasoning, H37; H39 → gesplitste-shacl-validatie, sameAs-discipline; H40 → skos-export-filter, namedindividual-telmethode, dashboard-productlijnen).
- H40 verwijst naar `dashboard-productlijnen` — concept bestaat (geen forward-reference-rot).
- `dashboard-productlijnen` verwijst naar H40 — H40 bestaat (geen forward-reference-rot).
- Concept-register heeft drie nieuwe consistent-bijgewerkte tabellen (snelle navigatie + clusters + D-cross-references + sprint-cross-references).
- H-register heeft H36-H40 in zowel Parked-status-tabel als nieuwe "iteratie 12"-sectie als per-D-decision-tabel.
- `CLAUDE.md` §Dashboard-productlijnen verwijst naar `brain/brain__concepts__dashboard-productlijnen.md` (bestaat).
- `docs/sprint-protocols.md` Protocol 14 is benoemd in overzichts-tabel (#14) én uitgewerkt in eigen sectie én vermeld in wijzigingsgeschiedenis (v1.0 → v1.1).

**Belangrijkste open punten voor masterchat:**

1. **Locatie Spoor B-prototype in repo** (WP3 — A/B/C-keuze, niet door Brein gedaan)
2. **Eventuele restpunten** uit sessie-rapport v2.0 die niet in deze cyclus zijn meegenomen — Brein heeft strikt de briefing gevolgd; aanvullende WP's zijn aan masterchat

**Karakter-bevestiging:** geen architectuurbeslissingen genomen; geen ontologie-impact; geen D-mutaties; geen ramp om scope. Discipline-conform.

**Pre-push disclosure-check** (Protocol 14, vandaag vastgelegd in WP2) is **op deze iteratie zelf toegepast**: log-entry, index-update, H-bestanden, concept-bestand, CLAUDE.md-sectie — geen organisatie-naam, geen persoonsnamen anders dan Steven, geen credentials, geen lokale paden.

**Volgende:** Steven inspecteert WP1-WP4 en commit handmatig (per WP of cumulatief — Brein-voorstel staat in eindrapport-output). Daarna eerste post-migratie-test-sprint (T1) kan aanvangen.

---

## 2026-05-21 — Iteratie 11b: v4.6.0-update detail (modules, sources, workflow)

**Tweede batch van iteratie 11** — vervolg op 11a (kern). 10 bestanden opgeleverd: 0 nieuw + 10 vervangen. Iteratie 11 nu volledig afgerond. Brain klaar voor migratie naar Claude Code + GitHub.

**Module-updates (5):**

- [[brain__modules__M01_framework]] — `fw:ENSIA` gepromoot van fw:Guideline → fw:GRCFramework (verplaatst uit m15) + `ext:Attr_ENSIA_Logius_2024` SourceAttribution. Vier-cluster D9-bewijs in M01 zichtbaar (NIS2/CBW + CBW/Cbb + NIST CSF + ENSIA-toetst-BIO)
- [[brain__modules__M06_isms]] — Volwassenheidsmodel-cluster: 5 isms-klassen + 3 OP + 5 Levels (NBA-LIO/NOREA-schaal) + 32 Capabilities (23 Cbw + 9 ISMS) + 160 LevelDescriptions + `ext:Attr_NBA_LIO_NOREA` SourceAttribution (SHA256). Triple-impact-decompositie (5+8 per element ipv 4+6 — rdf:type-dubbele-telling)
- [[brain__modules__M07_business]] — biz:MaturityAssessment-cluster ONGEWIJZIGD. Sectie "Parallelle clusters — niet samenvoegen" + V1-keuze-onderbouwing met vier conflict-redenen + SPARQL-aandachtspunt met namespace-onderscheid
- [[brain__modules__M15_ensia]] — Promotie uit stub. Hybride locatie A3+B3+C2 uitgelegd. Behoud NB-comment + 8 ext:hasAuditDomain + 2 skos:relatedMatch in M15. Issuers BZK/NOREA/VNG bevestigd; fw:Logius NIET als issuer (property-semantiek-discipline)
- [[brain__modules__M21_nist-csf-2-0-planned]] — Tiers-cluster v4.6.0: csf:CSFTier-klasse + 2 DP + 4 Tier-individuals + 4 SKOS Tier↔Level. EERSTE concrete D6-symmetrische toepassing v1.9 (riskGovernance/Management-Description @en-only). Naam-discipline CSFTier vs risk:RiskManagementTier

**Source-updates (2):**

- [[brain__sources__cbw-excel]] — Sheet 6 verwerking (1.440 triples, 32 Capabilities + 160 LevelDescriptions, +44% boven raming verklaarbaar). Eigen SourceAttribution voor Sheet 6 (NBA-LIO/NOREA-volwassenheidsmodel) náást de bestaande voor Sheet 3/8/9 (ADR/NOREA). 4 typo-correcties Cbw_05/11/12/14. ADR/NOREA bron-kwaliteits-patroon cumulatief over drie sprints
- [[brain__sources__source-register]] — 5 SourceAttribution-individuals tabel (2 nieuw v4.6.0: NBA-LIO-NOREA + ENSIA-Logius). Bronnen-overzicht per sprint. Twee nieuwe licentie-categorieën in tabellen: "Vrij gebruik met bronvermelding" (ENSIA-handreiking) + "CC-BY 4.0 via Sheet 6"

**Workflow-updates (2):**

- [[brain__workflow__sprint-protocollen]] — Cumulatieve tabel van 12 protocollen + 1 gedragsregel. Vier NIEUWE protocollen v1.9 (Protocol B-multi-module-discipline, Ramings-baseline rdf:type-dubbele-telling, Instructie-consistentie code-block vs toelichting, Bron-typo-beleid patroon-criterium). Eén nieuwe gedragsregel (Property-semantiek-discipline)
- [[brain__workflow__zes-chat-architectuur]] — Update naar 7-chat-architectuur (Brein-chat geactiveerd na v4.5.0). Filename behouden (`zes-chat-architectuur.md`), inhoud beschrijft 7 chats. Post-migratie-perspectief uitgewerkt (Tech/Brein/Dashboard naar Claude Code + GitHub; Master/Documentatie/Analyse/Asset blijven claude.ai)

**Log (1):**

- [[brain__log]] (deze) — iteratie 11b entry

**Karakter:**

Iteratie 11b is **detail-update** — alle module-specifieke, source-specifieke en workflow-specifieke wijzigingen die uit v4.6.0 + projectinstructie v1.9 volgen.

**Belangrijkste verfijningen uit v4.6.0 + v1.9:**

1. D9 vierde verificatie-cluster ENSIA-detail in M01 en M15 zichtbaar
2. Volwassenheidsmodel-cluster volledig gedocumenteerd in M06 + parallel-onderhoud van M07
3. CSF Tiers met D6-symmetrische toepassing (eerste concrete @en-only normatieve descriptions)
4. Vier nieuwe sprint-protocollen formeel met v4.6.0-toepassings-bewijs
5. 7-chat-architectuur met expliciete Brein-chat-rol en post-migratie-perspectief
6. Cumulatief ADR/NOREA bron-kwaliteits-patroon over drie sprints zichtbaar in source-register

**Brain-staat na iteratie 11 (compleet):**

| Folder | Files | Wijziging in iteratie 11 |
|---|---:|---|
| Root | 7 | log + index vervangen |
| decisions/ | 13 | D6 + D9 vervangen + register vervangen |
| sprints/ | 14 | +v4.6.0 nieuw + register vervangen |
| architecture/ | 12 | onveranderd (geen nieuwe H-items v4.6.0) |
| concepts/ | 13 | +parallelle-maturity-clusters nieuw + register vervangen |
| modules/ | 19 | M01/M06/M07/M15/M21 vervangen + register vervangen |
| sources/ | 8 | cbw-excel + register vervangen |
| workflow/ | 6 | sprint-protocollen + zes-chat-architectuur vervangen |
| scope/ | 5 | onveranderd |
| **Totaal** | **~100** | **20 wijzigingen** (2 nieuw + 18 vervangen) |

**Volgende:** vault-zip v4.6.0 wordt na deze iteratie aangeleverd voor migratie naar Claude Code + GitHub. Brain is volledig consistent met v4.6.0-baseline + projectinstructie v1.9 én klaar voor productie-test in eerste post-migratie-sprint (v4.7.0).

**Belangrijk:** iteratie 11 is **de laatste iteratie in claude.ai PK voor de Brein-chat**. Vanaf v4.7.0 (post-migratie) wordt brain-onderhoud uitgevoerd via de brein-subagent in Claude Code, met git als audit trail.

---

## 2026-05-21 — Iteratie 11a: v4.6.0 + v1.9-update kern

**Eerste batch van iteratie 11** — verwerking van v4.6.0 Fase 4 (M15-ENSIA + Volwassenheidsmodel) + projectinstructie v1.9 in de brain. 10 bestanden opgeleverd (2 nieuw + 8 vervangen). Batch 11b volgt na verificatie.

**Aanleiding:** v4.6.0 Fase 4 opgeleverd 21 mei 2026 — laatste geplande Spoor A-sprint vóór migratie naar Claude Code + GitHub. Schaal-multiplier 2,7× v4.4.0 (onder oorspronkelijke prognose dankzij hergebruik bestaande m15-structuur). +1.610 triples, +204 individuals, 5 modules gewijzigd.

**Nieuwe (2):** sprint v4.6.0, parallelle-maturity-clusters concept. **Vervangen (8):** D6, D9, D-register, sprint-register, module-register, concept-register, index, log iteratie 11a.

---

## 2026-05-19 — Iteratie 10b: v4.5.0-update detail (modules, sources, concepts, nieuw cross-bron-overlap)

Tweede batch van iteratie 10 — vervolg op 10a. 14 bestanden: 1 nieuw (cross-bron-overlap) + 13 vervangen.

---

## 2026-05-19 — Iteratie 10a: v4.5.0-update kern (sprint v4.5.0 + 3 H-items + D3-uitbreiding)

11 bestanden (5 nieuw + 6 vervangen). Nieuwe: sprint v4.5.0, H33, H34, H35.

---

## 2026-05-13 — Iteratie 9b: v1.7-update detail

Tweede batch iteratie 9. 10 bestanden (1 nieuw + 9 vervangen).

---

## 2026-05-13 — Iteratie 9a: v1.7-update kern (sprint v4.4.0 + D-updates + H32)

11 bestanden (2 nieuw + 9 vervangen).

---

## 2026-05-13 — Iteratie 8: Migratie-prep + future-concepts

7 bestanden.

---

## 2026-05-13 — Iteratie 7: Index-update + smoke-tests

3 bestanden.

---

## 2026-05-13 — Iteratie 6: Sources + Workflow + Scope

19 bestanden in drie folders.

---

## 2026-05-13 — Iteratie 5: Modules

20 nieuwe bestanden M01-M18 + M21-stub + register.

---

## 2026-05-13 — Iteratie 4: Concepts

10 bestanden: 9 concepts + register.

---

## 2026-05-13 — Iteratie 3: H-items + D-correcties

11 bestanden.

---

## 2026-05-13 — Iteratie 2: Sprint-files v0.x → v4.3.3 + register

12 bestanden.

---

## 2026-05-13 — Iteratie 1: D-decisions D1–D12 + register

12 bestanden.

---

## 2026-05-13 — Iteratie 0: vault-foundation

4 bestanden initiële opzet.

---

*(Iteratie 1.5 = archeologie-rapport, niet als log-entry maar als apart document [[brain__archeology-report]].)*
