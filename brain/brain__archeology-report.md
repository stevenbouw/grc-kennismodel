---
type: report
title: Archeologie-assessment GRC Kennismodel v0.1 → v4.3.3
status: complete
date: 2026-05-13
related:
  - D-register
sources:
  - projectinstructie-v1.6
chat-sources:
  - https://claude.ai/chat/7b0a059c-d625-4942-9dbd-55e99c89e71c
  - https://claude.ai/chat/5ca3214f-1949-42ef-be10-10d2e91d648e
  - https://claude.ai/chat/76420a5b-11ac-4f22-af7a-5e2404201bdd
  - https://claude.ai/chat/95d2b45f-4d7a-48f2-a4c2-e47d6e4d4a0f
  - https://claude.ai/chat/f527e7ab-bc17-44f4-a878-598e8ca7a632
  - https://claude.ai/chat/2c28d805-a69b-4cf2-9fd1-01771bdaa779
  - https://claude.ai/chat/7ec4a4dc-7230-4135-96f4-c791e7271656
---

# Archeologie-assessment GRC Kennismodel v0.1 → v4.3.3

Per-versie reconstructie-assessment ter voorbereiding van iteratie 2 (sprint-files). Doel: vóór generatie inzichtelijk maken welke versies rijk reconstrueerbaar zijn en welke noodzakelijkerwijs skelet-only blijven.

## Samenvattingstabel

| Versie | Datum | Confidence | Bron-chats | Aanbeveling iteratie 2 |
|---|---|---|---|---|
| v0.1 | onbekend (pre-mrt 2026) | **low** | indirect via v2.0-refs | skelet-only |
| v1.x | onbekend (pre-mrt 2026) | **low** | indirect via v2.0-refs | skelet-only, samen met v0.1 |
| v2.0 | onbekend (pre-16 mrt 2026) | **medium** | 1 (taxonomie-chat 16/3) | medium-reconstructie |
| v3.0 | pre-19 mrt 2026 | **high** | 1 (refactor-briefing 19/3) | rijke reconstructie |
| v3.x | mrt–apr 2026 | **medium** | 2 (tech-chats 9/4) | korte note bij v3.0 of skip |
| v4.0.0 | eind mrt–begin apr 2026 | **high** | 2 (masterchat + tech 9/4) | rijke reconstructie |
| v4.0.0-patch | onbekend (pre-10 apr) | **medium** | 1 (tech 9/4) | korte note bij v4.0.0 |
| v4.1.0-alpha | 2026-04-10 | **high** | 1 (tech 13/4) | rijke reconstructie |
| v4.2.0 | 2026-04-13 | **high** | 1 (tech 13/4) | rijke reconstructie |
| v4.2.1 | 2026-04-13 | **high** | 1 (tech 13/4) | korte note bij v4.2.0 (M18-consolidatie, geen contentwijziging) |
| v4.2.2 | 2026-04-13 | **high** | 1 (tech 13/4) | rijke reconstructie (Route A canonisering) |
| v4.3.0 | 2026-04-14 | **high** | 1 (tech 14/4) + projectinstructie | rijke reconstructie |
| v4.3.1 | 2026-04-20 | **high** | userMemories + projectinstructie | rijke reconstructie |
| v4.3.2 | ±2026-04-21 | **high** | userMemories | medium-reconstructie |
| v4.3.3 | 2026-04-22 | **high** | tech 13/5, patch-rapport-v4_3_3.md | rijke reconstructie |

**Totaal kandidaat sprint-files iteratie 2: 10–12** (afhankelijk van aanbeveling-keuze per patch-bump).

## Per-versie detail

### v0.1 — eerste ontologie (confidence: low)

**Wat bekend is:**

- Eerste werkversie zonder owl:sameAs-discipline tussen ctrl: en bio:-namespaces
- Module-niveau versionering toegepast (bv. M3 v0.1 als afzonderlijke marker in vroege ontwerpkeuzes)
- Modelleer-keuzes per module gedocumenteerd in taxonomie-chat 16/3 (`risk:ResidualRisk` als subklasse, `mitigatedBy` cross-module property, Threat vs ThreatSource split, kwalitatieve schaal als named individuals)

**Wat onbekend is:**

- Exacte datum vaststelling
- Totaal aantal modules, klassen, individuals
- Of v0.1 ooit één samenhangend bestand was, of een verzameling parallel-ontwikkelde module-stubs

**Bron-chats:** geen directe vondst; alleen retrospectieve referenties in tech-chat 16/3 ("v0.1/v1.x") en v2.0-fixes-paragraaf ("ten opzichte van de initiële ontologie")

**Aanbeveling:** skelet-only file in iteratie 2, gecombineerd met v1.x

### v1.x — incrementele uitbouw (confidence: low)

**Wat bekend is:**

- Stage tussen v0.1 (initieel) en v2.0 (fix-release)
- Bevatte nog steeds de ctrl: ↔ bio: namespace-disconnect die v2.0 ging fixen

**Wat onbekend is:**

- Concrete versie-nummers (was er v1.0, v1.1, v1.x?)
- Welke modules toegevoegd, welke veranderd

**Bron-chats:** geen directe vondst

**Aanbeveling:** skelet-only, samen met v0.1 in één file `v0_x-v1_x_initiele-fase.md`

### v2.0 — fix-release (confidence: medium)

**Wat bekend is:**

Drie categorieën fixes ten opzichte van v0.1/v1.x:

1. **Fix 1 — owl:sameAs namespace-brug (M2 ↔ M8):** 94 owl:sameAs-axioma's toegevoegd (86 directe matches + 7 handmatige ID-notatie-mappings). Patroon: `ctrl:ISO27002_X_YY owl:sameAs bio:ISO27002_X_YY` (93×). Dit is de oorsprong van [[brain__decisions__D05_sameAs-strikt-ctrl-bio]].
2. **Fix 2A — Ontologie-header:** volledige `owl:Ontology` declaratie met dcterms-metadata, owl:versionIRI, PROV-O provenance en `owl:versionInfo "2.0.0"`.
3. **Fix 2B — BVC-rol:** `roles:BVC` als expliciete OWL-klasse en named individual, gegrond in Besluit BVA-stelsel Rijksdienst 2021.

**Namespace-conventie v2.0:** nog `#`-separator en `grc.organisatie.nl`-host.

**Wat onbekend is:**

- Exacte datum vaststelling
- Of er nog Fix 3 / Fix 4 was

**Bron-chats:** taxonomie-chat 16/3/2026 (`7b0a059c...`) bevat de v2.0-fixes-paragraaf

**Aanbeveling:** medium-reconstructie file (~200 woorden) `v2_0_fix-release.md`

### v3.0 — monolithisch (confidence: high)

**Wat bekend is:**

Volledig gedocumenteerd in refactor-briefing 19 maart 2026:

- **Bestand:** `grc-ontologie-v3.ttl` (monolithisch)
- **Omvang:** 13.292 regels Turtle, 618 KB
- **Inhoud:** 572 named individuals, 157 klassen, 119 object properties
- **Modules:** M1–M13 in 9 namespaces (nog `grc.example.org/`-host met slash-separator — host-migratie heeft dus vóór v3.0 plaatsgevonden, of in de refactor zelf)
- **Mappings:** 179 SKOS-mappings, 94 owl:sameAs
- **Completeness:** TBox ~87%, ABox ~49%

**Bekende bugs in v3.0** (later opgelost in v4.0.0 stap 2):

- BUG-01: duplicate fw:CBW + fw:CyberBeveiligingswet
- BUG-02–05: ontbrekende rdf:type-declaraties op vier framework-individuals
- BUG-06: BBN-properties verwezen naar BIO 2.0 i.p.v. Handreiking BIO2-opmaat

**Aanbeveling:** rijke reconstructie `v3_0_monolithisch.md` (~400 woorden)

### v3.x — toepassingsfase (confidence: medium)

**Wat bekend is:**

- Tech-chat 9 april 2026 werkt nog op `grc-ontologie-v3.ttl`
- 27 HermiT-inconsistenties opgelost via xsd:string-fix (correctieve patch, geen versie-bump)
- 26 mrt 2026: ISO 27001/27002/BIO 2.0 relatieverduidelijking — `fw:geeftRichtlijnenVoor` toegevoegd, ISO 27002 → ISO 27001 relatie expliciet gemaakt

**Aanbeveling:** korte note in `v3_0_monolithisch.md` of aparte skip — geen versie-nummer bump in deze fase

### v4.0.0 — modulaire split (confidence: high)

**Wat bekend is:**

- Datum: tussen 19 maart (briefing) en 9 april 2026 (operationeel in tech-chat)
- **Refactor-stappenplan:** 22 stappen, gegroepeerd in Structuur (1), Bugfixes (2-3), Verrijking (4-22)
- **Stap 0:** namespace-migratie naar `https://grc.example.org/XXX/` met slash-separator (host-migratie geconfirmeerd in deze stap)
- **Stap 1:** split naar 16 bestanden (grc-core, M01–M13, grc-bridges, m-cobit-interim)
- **Validatie na split:** 157 klassen, 572 individuals, 94 owl:sameAs — exact match met v3.0
- Klassen-hiërarchie uitgebreid met M14 (AVG), M15 (ENSIA), M16 (VIRBI-ext), M17 (COSO/COBIT) tijdens latere stappen

**Wat onbekend is:**

- Exacte datum van v4.0.0-release-stamp
- Of v4.0.0 één commit was of meerdere

**Aanbeveling:** rijke reconstructie `v4_0_0_modulaire-split.md` (~400 woorden)

### v4.0.0 correctieve patch (confidence: medium)

**Wat bekend is:**

- Datum onbekend, vóór 10 april 2026
- Inhoud: 27 HermiT-inconsistenties opgelost door xsd:string-fix op data-properties met taalgetagde waarden
- Geen versie-bump — bleef v4.0.0

**Aanbeveling:** korte note in `v4_0_0_modulaire-split.md`

### v4.1.0-alpha — werkpakket opschoning (confidence: high)

**Datum:** 10 april 2026

**Inhoud:** Acties A, D, C, H2, B, F, G, E:

- **BBN-consolidatie:** via `ext:hasHandreikingBBN` (i.p.v. BIO 2.0-property)
- **ISO27002 naming-canonicalisatie:** 29 renames (Actie D)
- **CBW-alias opgeruimd**
- **fw:toetst verplaatst** m15 → m01
- **grc-core-mapping verwijderd**
- **M15 scope-comment** toegevoegd
- **D6 meeliftregel** vastgelegd (Actie G) — zie [[brain__decisions__D06_tweetalige-annotaties-meeliftregel]]
- **Laag 5 scope-noot** vastgelegd (Actie E): 331 SKOS-mappings als startpunt voor kwaliteitsanalyse

**Aanbeveling:** rijke reconstructie `v4_1_0-alpha_werkpakket-opschoning.md` (~400 woorden)

### v4.2.0 — M18 Asset-module (confidence: high)

**Datum:** 13 april 2026

**Inhoud:**

- **M18 Asset-module geïntegreerd** — nieuwe `asset:`-namespace
- **Drie nieuwe modules:** m18-assets, m18-mappings-iso27002, m18-mappings-bio2-overheidsmaatregelen + stub bio2-controls
- **Module-patches:** M01/M04/M06 voor BVA Te Beschermen Belangen en wederzijdse seeAlso-relaties
- Namespaces consolideerden naar 9 → 10 (`asset:` toegevoegd) — voorloper [[brain__decisions__D03_10-namespaces]]

**Aanbeveling:** rijke reconstructie `v4_2_0_M18-asset-module.md` (~400 woorden)

### v4.2.1 — M18-consolidatie (confidence: high)

**Datum:** 13 april 2026 (zelfde dag als v4.2.0)

**Inhoud:**

- M18 5 bestanden → 1 bestand (`m18-assets.ttl`) — pure consolidatie, geen contentwijziging
- **Risk-coupling baseline measurement (nulmeting)** uitgevoerd, identificeerde structurele gaps G1–G9 ter input voor v4.3.0
- Geen eigen `opleveringsrapportage-v4.2.1.md` (zoals later vastgesteld in masterchat 20/4)

**Aanbeveling:** korte note bij v4.2.0, geen aparte sprint-file

### v4.2.2 — SoA-cleanup Route A (confidence: high)

**Datum:** 13 april 2026

**Inhoud:**

- Route A canonisering: 15 duplicate `SoAEntry`-individuals + 1 `SOA_v1` container verwijderd (Scenario 2 unintended duplication)
- Eén canonisering-mirror-triple toegevoegd na expliciete masterchat-GO
- Resultaat: schone `isms:SoA_2026` + 93 unieke `SoAEntry_*` — zie [[brain__decisions__D08_canonieke-soa]]

**Aanbeveling:** rijke reconstructie `v4_2_2_soa-canonisering-route-a.md` (~300 woorden)

### v4.3.0 — gap-sprint + D11 (confidence: high)

**Datum:** 14 april 2026

**Inhoud:**

- **G1 (D11):** 5 owl:sameAs asset-bridges (`asset:↔risk:/isms:`) — zie [[brain__decisions__D11_sameAs-asset-convergentie]]
- **G2:** `isms:forRisk` ObjectProperty
- **G4 (Optie B):** `risk:ReportingRisk` klasse, `AllDisjointClasses` uitgebreid 4 → 5 leden
- **G5:** `skos:altLabel "Consequence"@en` op `risk:Impact`
- **SHACL-impact:** `asset:NamespaceShape` verplaatst SECTIE B → SECTIE A wegens D11 sameAs-propagatie
- **Contextdiepte-diagnostiek:** 23 bevindingen H1–H23
- **Canonieke meetmethode** vastgelegd: `canonical_metrics_v[versie].py` + `shacl_split_validate_v[versie].py`

**Aanbeveling:** rijke reconstructie `v4_3_0_gap-sprint-d11.md` (~500 woorden)

### v4.3.1 — patch-bump (confidence: high)

**Datum:** 20 april 2026

**Inhoud:**

- H18: nieuwe klasse `ext:HSClause` + `ext:alignsWithHSClause` TBox (scope-completion)
- H22, F, A, C: overige patch-items
- B₂: afkappingsbug `SoAEntry_5_02` opgelost
- §10.2-meetcorrectie: `asset:appliesToAssetType` inferred 556 → 973 (administratief, geen model-wijziging)

**Aanbeveling:** rijke reconstructie `v4_3_1_patch-bump.md` (~300 woorden)

### v4.3.2 — smart quotes + asymmetrie (confidence: high)

**Datum:** circa 21 april 2026 (tussen v4.3.1 en v4.3.3)

**Inhoud:**

- **Item 1:** Smart quotes (U+2018/U+2019) vervangen door ASCII (U+0027) op `ctrl:ISO27002_7_07 + _8_01` plus spiegels in `isms:` en `bio:` (D5-brug-completion). Totaal 10 triples gewijzigd.
- **Item 2:** `ext:NIS2Requirement`-klasse toegevoegd (subClassOf `compl:ComplianceRequirement`). 21 NIS2-subjects geretypeerd. Klassen-count 185 → 186.
- **Item 3:** §10.2-meetcorrectie administratief gemarkeerd

**Aanbeveling:** medium-reconstructie `v4_3_2_smart-quotes-en-asymmetrie.md` (~250 woorden)

### v4.3.3 — D12 + predicate-consolidatie α (confidence: high)

**Datum:** 22 april 2026

**Inhoud:**

- **D12 vastgelegd:** drie-laags compliance-architectuur — zie [[brain__decisions__D12_drie-laags-compliance]]
- **NIS2-hygiëne:** 15 `REQ_NIS2_Art*`-subjects `rdfs:label@nl/@en` toegevoegd (+30 triples)
- **Predicate-consolidatie α:** `ext:articleNumber` hardverwijderd (TBox + 20 data-uses), gemigreerd naar `compl:articleRef` op 6 NIS2 + 14 DORA-subjects. Scope-uitbreiding Optie A na masterchat-GO (D9-motivatie)
- **6 plain NIS2Req-subjects:** `compl:requirementText@en` toegevoegd (+6 triples)
- **15 expliciete `owl:NamedIndividual`-declaraties** op REQ_NIS2_* (+15 triples)
- **Geparkeerde bevinding gesloten:** 11 NL-apostrof-hits in m08 (correcte NL-typografie)
- **NamedIndividual-telmethode geformaliseerd:** canonical_metrics-JSON als enige autoritatieve bron

**Eindstaat:** 12.739 / 29.863 / 186 / 637 / 140 / 84 / 98 / 346

**Aanbeveling:** rijke reconstructie `v4_3_3_d12-en-predicate-consolidatie.md` (~500 woorden)

## Aanbevelingen voor iteratie 2

**Voorgestelde 10 sprint-files:**

1. `v0_x-v1_x_initiele-fase.md` (skelet-only, gecombineerd)
2. `v2_0_fix-release.md` (medium)
3. `v3_0_monolithisch.md` (rijk, bevat v3.x als note)
4. `v4_0_0_modulaire-split.md` (rijk, bevat 22-stappen-refactor en v4.0.0-patch als note)
5. `v4_1_0-alpha_werkpakket-opschoning.md` (rijk)
6. `v4_2_0_M18-asset-module.md` (rijk, bevat v4.2.1 als note)
7. `v4_2_2_soa-canonisering-route-a.md` (rijk)
8. `v4_3_0_gap-sprint-d11.md` (rijk)
9. `v4_3_1_patch-bump.md` (rijk)
10. `v4_3_2_smart-quotes-en-asymmetrie.md` (medium)
11. `v4_3_3_d12-en-predicate-consolidatie.md` (rijk)

**Plus** `brain__sprints__sprint-register.md` als overzichtsbestand met versie-timeline en cross-references — analoog aan [[brain__decisions__D-register]].

**Totaal: 11 sprint-files + 1 register = 12 bestanden voor iteratie 2.**

**Alternatieve aggregatie-keuzes (jouw beslissing):**

- *Optie compact:* combineer v4.2.0 + v4.2.1 + v4.2.2 in één `v4_2_x_M18-en-soa.md` → 10 sprint-files totaal
- *Optie patches:* combineer v4.3.1 + v4.3.2 in één `v4_3_1-v4_3_2_patch-bumps.md` → 9 sprint-files totaal
- *Optie maximaal:* split v4.0.0 in initiële split + bugfix-stappen + verrijking-stappen → 13+ sprint-files

## Open vragen vóór iteratie 2

1. **Aggregatie-keuze:** compact (10), patches-gecombineerd (9), of voorstel-default (11)?
2. **Skelet-aanpak v0.x/v1.x:** acceptabel als skelet-only met expliciete gaps, of wil je nog handmatig content aanleveren vanuit jouw eigen herinnering?
3. **v3.x toepassingsfase:** als note in v3.0-file of als aparte mini-file `v3_x_toepassingsfase.md`?
4. **Sprint-register:** akkoord met als laatste file bij iteratie 2, analoog aan D-register?

— Einde archeologie-rapport iteratie 1.5.
