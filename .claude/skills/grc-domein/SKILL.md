---
name: grc-domein
description: NL GRC-kaders-domeinkennis voor het GRC Kennismodel — de Nederlandse normen/wetten/kaders (COSO, COBIT, BVA/CIO-stelsel, NIS2, VIR/VIRBI, AVG, CBW/Cbb, DORA, BIO 2.0, ISO-reeks, NIST, NIST CSF 2.0, ENSIA, volwassenheidsmodel), hun functionele vijf-lagen-ordening, en de relatie-semantiek (fw:stelVerplicht / geeftRichtlijnenVoor / geeftITInvullingAan / dektAf / toetst / transposedBy / isTranspositieVan / uitgewerktIn / werktUit / ext:isComponentOf) plus de SKOS cross-category-basislijn. Use when een vraag, sprint of analyse moet weten welke laag een kader heeft, welke relatie tussen twee kaders geldt, welke status een wet heeft, of hoe NL-kaders onderling samenhangen — zodat ontologie- en analysewerk consistent naar de juiste kaders, lagen en clausules verwijst. Beschrijft; muteert de ontologie niet.
---

# grc-domein — NL GRC-kaders + relatie-semantiek

Domeinkennis-skill over de Nederlandse GRC-kaders en hun onderlinge relaties. Vult de lacune die generieke GRC-skills niet vullen: de **NL-specifieke kaders, hun functionele ordening en de project-eigen relatie-semantiek**. Alle feiten hieronder zijn geverifieerd tegen de ontologie-modules (`ontology/m01-framework.ttl`, `m17-coso-cobit.ttl`, `m15-ensia.ttl`) en de brain-vault (`brain__concepts__framework-neutraliteit`, `brain__concepts__cross-category-mappings`). Detail-tabellen + de letterlijke triples: zie `kaders-reference.md` in deze folder.

---

## §0.5 — Firewall (niet-onderhandelbaar, exposeert opnieuw bij elke aanroep)

Deze skill is **beschrijvend**. Aanroepen ervan verandert niets aan deze grenzen:

- **Geen autonomie-bouw onder welke framing dan ook.** Mens-in-controle. Deze skill levert kennis voor menselijk/begeleid werk; ze opent geen autonoom pad.
- **Geen autonome commit / push** — Steven inspecteert `git status`/`git diff` en commit handmatig (hard deny in `.claude/settings.json`).
- **Geen ontologie-mutatie als gevolg van deze skill** — de skill beschrijft kaders en relaties; ze muteert geen TTL.
- **Geen architectuurbeslissingen** — D1–D12 wijzigen, een D toevoegen, een kandidaat-precedent (bv. v1.3.1 cross-category) formaliseren = masterchat-werk via Steven. Bij twijfel: scope-pauze, niet zelf interpreteren.
- **Geen organisatienaam** — altijd "de organisatie" of "Rijksoverheidsorganisatie".

---

## 1. Framework-neutraliteit eerst (D9) — de lagen zijn géén hiërarchie

De vijf-lagen-ordening hieronder is een **functioneel leeshulpmiddel**: ze beschrijft het *abstractie-niveau en de rol* van een kader (enterprise-governance → IT-governance → wet/richtlijn → operationele baseline → norm/best-practice → auditkader). Ze is **geen architectureel privilege en geen subsumptie**.

> **D9-invariant:** alle kaders zijn architectureel gelijkwaardige individuals. Geen kader is "het centrum". In het model bestaan alleen individuals met onderlinge relaties.
>
> **BIO 2.0 = view-keuze, geen kern.** Voor *gebruik* (dashboard, rapportage) mag BIO 2.0 het primaire perspectief zijn; dat is een dashboard-view, geen architectuur-keuze. "Het model is het woordenboek (neutraal), het dashboard is het verhaal (perspectief)."

Bij een vraag "is kader X belangrijker / de basis?" — nee. De lagen ordenen functie, niet gewicht.

---

## 2. De vijf-lagen-ordening (snelle plaatsing)

| Laag | Rol | Kaders |
|---|---|---|
| **0** | Enterprise-governance | COSO ICF, COSO ERM |
| **1** | IT-/organisatie-governance | COBIT 2019, BVA-stelsel (Besluit BVA-stelsel Rijksdienst), CIO-stelsel (Besluit CIO-stelsel Rijksdienst) |
| **2** | Wet & richtlijn | NIS2 (EU-richtlijn), VIR 2007, VIRBI 2025, AVG (IB-raakvlakken), CBW *(in voorbereiding)*, Cbb *(concept t.b.v. Tweede Kamer)*, DORA *(referentie — de organisatie valt er niet onder)* |
| **3** | Operationele baseline | BIO 2.0 *(operationeel kader; dashboard-view-perspectief)* |
| **4** | Norm & best-practice | ISO/IEC 27001, 27002, 27005, 31000, 22301, 22313; NIST SP 800-53 / 800-39 / 800-30; NIST CSF 2.0; Annex SL |
| **5** | Auditkader & meting | ENSIA (auditkader), volwassenheidsmodel |

Volledige per-kader-tabel met issuing body, jurisdictie, namespace en module: `kaders-reference.md` §1.

---

## 3. Relatie-semantiek — de project-eigen properties

Deze ObjectProperties (gedeclareerd in `m01-framework.ttl` / `m17-coso-cobit.ttl`, namespace `fw:` resp. `ext:`) drukken de inhoudelijke samenhang uit. Domain/range + de geverifieerde feitelijke triples staan in `kaders-reference.md` §2.

| Property | Betekenis (parafrase rdfs:comment) | Richting | Geverifieerd voorbeeld in het model |
|---|---|---|---|
| `fw:stelVerplicht` | Subject stelt object wettelijk verplicht | niet-symmetrisch | VIR 2007 → BIO 2.0 |
| `fw:geeftRichtlijnenVoor` | Subject geeft implementatierichtlijnen voor de controls van object | niet-symmetrisch | ISO 27002 → ISO 27001 |
| `fw:geeftITInvullingAan` | Subject biedt de IT-specifieke invulling van het bredere object | niet-symmetrisch | COBIT 2019 → COSO ICF + COSO ERM |
| `fw:dektAf` | Naleving van subject dekt (het merendeel van) de eisen van object af | niet-symmetrisch | BIO 2.0 → NIS2 |
| `fw:toetst` | Subject is audit-/toetsingsinstrument voor object | niet-symmetrisch | ENSIA → BIO 2.0 |
| `fw:transposedBy` / `fw:isTranspositieVan` | EU-richtlijn ↔ nationale omzettingswet (inverse-paar) | inverse | NIS2 ↔ CBW |
| `fw:uitgewerktIn` / `fw:werktUit` | Wet ↔ AMvB-uitwerking (inverse-paar) | inverse | CBW ↔ Cbb |
| `ext:isComponentOf` | Component (principe / objective / subcategory) → het kader waartoe het behoort | component-relatie | COSO-principes → COSO ICF/ERM; COBIT-objectives → COBIT 2019; CSF-subcategories → NIST CSF 2.0 |

Ondersteunend (generiek, geen inhoudelijke afhankelijkheid): `fw:relatedTo` (symmetrisch), `fw:alignsWith`, `fw:supersedes`.

**Twee veelgevraagde ketens:**
- **NIS2 → CBW → Cbb:** NIS2 (EU-richtlijn) wordt nationaal omgezet door de CBW (`fw:transposedBy`); de CBW wordt operationeel uitgewerkt in de Cbb-AMvB (`fw:uitgewerktIn`). Horizontale transpositie/uitwerking — géén hiërarchie (D9). BIO 2.0 dekt NIS2-eisen af (`fw:dektAf`); VIR 2007 stelt BIO 2.0 verplicht (`fw:stelVerplicht`).
- **COSO → COBIT → ISO/BIO:** COBIT geeft IT-invulling aan COSO (`fw:geeftITInvullingAan`); ISO 27002 geeft richtlijnen voor ISO 27001 (`fw:geeftRichtlijnenVoor`); ENSIA toetst BIO 2.0 (`fw:toetst`).

---

## 4. SKOS-mapping-semantiek + cross-category-basislijn

Cross-framework-overlap wordt **niet** met `fw:`-relaties maar met SKOS-mappings gemodelleerd (D4). Default `skos:closeMatch`; `relatedMatch` voor partiële overlap; `exactMatch` zeldzaam.

**Cross-category-principe** (T3-precedent, **kandidaat v1.3.1 — nog niet geformaliseerd, masterchat-werk**): wanneer subject en object in ontologisch verschillende categorieën zitten — bv. **control ↔ legal-obligation** (ISO 27002-control ↔ AVG-artikel) — is de **basislijn `skos:relatedMatch`** (associatief). `broadMatch`/`narrowMatch` is daar meestal een categorie-fout (operationele implementatie ≠ conceptuele subsumptie); `exactMatch` is structureel uitgesloten. Uitzondering naar `closeMatch` alleen bij **retrieval-interchangeability** (control is de canonieke implementatie-equivalent van de verplichting in een audit-context). Binnen-categorie-mappings (control ↔ control-eis) volgen gewoon de cluster-discipline-default. Detail: `brain__concepts__cross-category-mappings.md`.

---

## 5. Status-discipline wetgeving (status-conform, geen anachronisme)

Bij verwijzing naar wetgevingsstatus exact aanhouden — geverifieerd tegen `fw:status` in `m01-framework.ttl`:

| Kader | Status (mei 2026) |
|---|---|
| **CBW** (Cyberbeveiligingswet) | **"in voorbereiding"** — nog niet van kracht |
| **Cbb** (Cyberbeveiligingsbesluit, AMvB) | **"concept t.b.v. Tweede Kamer, nog niet vastgesteld"** — inwerkingtreding bij koninklijk besluit |

Andere bronnen status-conform behandelen; geen anachronistische status-toekenning.

---

## 6. BBN — niet een BIO 2.0-eigenschap

**BBN (Basisbeveiligingsniveau) komt NIET uit BIO 2.0.** Het is afkomstig uit de **Handreiking BIO2-opmaat** en wordt in het model gedragen door de datatype-property **`ext:hasHandreikingBBN`**, met **uitsluitend waarden 1 of 2** (SHACL `ctrl:HandreikingBBNValueShape` dwingt dit af). **BBN 3 bestaat niet.** Schrijf BBN dus nooit toe aan BIO 2.0 als kader-eigenschap; verwijs naar de Handreiking + `ext:hasHandreikingBBN`.

---

## 7. NEN-discipline (bij elke output over ISO-normen)

ISO 27001/27002/27005/31000/22301/22313 zijn NEN-restrictief. In skill-output, rapporten, commits of Turtle: **alleen parafrase + clausule-verwijzing, nooit verbatim NEN-tekst >10 woorden.** Lokale NEN-bron (`grc-sources-licensed/`) mag gelezen worden voor parafrase; de output respecteert de grens. Bij behoefte aan letterlijke ISO-clausule die niet lokaal beschikbaar is: scope-pauze naar Steven, niet web-zoeken, geen geheugen-aannames.

---

## Verificatie-anker

Bij twijfel over een feit in deze skill: terug naar de bron, niet naar het geheugen (Protocol 4-geest).
- Lagen + per-kader-detail → `kaders-reference.md` + `ontology/m01-framework.ttl`
- Relatie-property-definities → `ontology/m01-framework.ttl` SECTIE 2 + `ontology/m17-coso-cobit.ttl`
- D9-neutraliteit → `brain/brain__concepts__framework-neutraliteit.md` + `brain__decisions__D09_*`
- SKOS cross-category → `brain/brain__concepts__cross-category-mappings.md`
- BBN → `ontology/grc-shacl.ttl` (`HandreikingBBNValueShape`) + `brain__concepts__bbn-correctie.md`

— Einde grc-domein SKILL.
