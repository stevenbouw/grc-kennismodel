---
type: smoke-test
title: Brain smoke-tests — vault-functionaliteit-validatie
status: living
date: 2026-05-13
related:
  - brain-index
sources: []
chat-sources: []
confidence: high
---

# Brain smoke-tests

## Doel

**Pragmatische validatie** dat de brain-vault niet alleen technisch compleet is, maar ook **functioneel werkt** voor de doelen waarvoor hij is gebouwd. Karpathy-conform: elke test is een realistische gebruiksvraag met verwachte uitkomst.

## Hoe te gebruiken

Plak één van de test-vragen hieronder in een nieuwe Master/Tech-chat-prompt. Vergelijk het antwoord met de verwachte uitkomst. Discrepantie = brain heeft een gap of inconsistentie die opgelost moet worden.

Een werkende brain levert deze antwoorden zonder dat de gebruiker bron-bestanden hoeft aan te wijzen.

## Test 1 — Open architectuur-vragen (H-register)

**Vraag:** *"Wat zijn de huidige openstaande architectuur-vragen voor het GRC Kennismodel?"*

**Verwachte uitkomst:** drie open H-items + drie future-consideration H-items:

- **Open:** H25 (compl:articleRef domain-spanning), H26 (OBL-laag gap NIS2), H27 (γ-migratie articleRef → articleIdentifier, voorwaardelijk)
- **Future-consideration:** H29 (Three Lines Model), H30 (GITC auditkader), H31 (Toetsingskader Algoritmes)

**Brain-pad:** `brain__architecture__H-register.md` → individuele H-files

## Test 2 — D-decision cross-references

**Vraag:** *"Welke D-decisions hangen samen met D11 asset-convergentie?"*

**Verwachte uitkomst:**

- D5 (owl:sameAs ctrl:↔bio:) — voorganger-conventie van sameAs-gebruik
- D9 (framework-neutraliteit) — D11 ster-patroon is consistent met D9
- D3 (10 namespaces) — D11 vereist asset:-namespace die in v4.2.0 is toegevoegd

**Plus:** geen extensie van sameAs-paren zonder Master-GO; precies 5 bridges (Asset, InformationAsset 2×, HumanAsset, PhysicalAsset).

**Brain-pad:** `brain__decisions__D11_sameAs-asset-convergentie.md` → `brain__concepts__sameAs-discipline.md`

## Test 3 — Layer-query

**Vraag:** *"Welke modules zitten op Laag 2 (wet- en regelgeving)?"*

**Verwachte uitkomst:** M10 (NIS2), M14 (AVG IB-raakvlak), M16 (VIRBI 2025). Plus geplande CBW/Cbb-uitbouw v4.4.0 die ook Laag 2 raakt.

**Brain-pad:** `brain__modules__module-register.md` → "Modules per laag"-tabel

## Test 4 — Licentie-query

**Vraag:** *"Welke bronnen in het kennismodel zijn CC-BY 4.0 en wat zijn de gevolgen?"*

**Verwachte uitkomst:**

- CBW NIS2 Control Framework v1.0 (ADR & NOREA, 30 sept 2025)
- ENISA Technical Implementation Guidance v1.0

Beide vereisen attributie via `ext:sourceAttribution`-property (gepland v4.4.0). Eerste verplichte toepassing: Route 5 ENISA-guidance attachment op 73 van 93 BIO-controls.

**Brain-pad:** `brain__sources__source-register.md` → categorie "CC-BY 4.0"

## Test 5 — Status-discipline wetgeving

**Vraag:** *"Wat is de juridische status van CBW en Cbb?"*

**Verwachte uitkomst:**

- **CBW** (Cyberbeveiligingswet) — **"in voorbereiding"**, Nederland heeft NIS2-transpositiedeadline gemist
- **Cbb** (Cyberbeveiligingsbesluit / AMvB) — **"concept t.b.v. Tweede Kamer, nog niet vastgesteld"**, inwerkingtreding bij koninklijk besluit
- Monitoring valt onder Spoor C (governance-beheer)
- 14 zorgplichtartikelen (art. 6–17, 19) + art. 18 (supplier-exclusion)

**Brain-pad:** `brain__sources__nl-wetgeving-bundle.md` + `brain__modules__M10_nis2-ext.md`

## Test 6 — Sprint-historie

**Vraag:** *"Wat is precies gewijzigd tussen v4.3.2 en v4.3.3?"*

**Verwachte uitkomst:** zes items uitgevoerd:

1. D12 drie-laags-compliance-architectuur formaliseren
2. 15 `compl:REQ_NIS2_*` tweetalige labels (+30 triples)
3. Predicate-consolidatie α — `ext:articleNumber` hardverwijderd, 20 uses → `compl:articleRef` (6 NIS2 + 14 DORA via Optie A scope-uitbreiding)
4. 6 plain NIS2Req `requirementText@en` (+6 triples)
5. 15 expliciete `owl:NamedIndividual` op REQ_* (+15 triples)
6. Parkeerlijst-item 1 (NL-apostrof in m08) administratief gesloten

Net-delta: +52 triples; NamedIndividual-count 622 → 637.

**Brain-pad:** `brain__sprints__v4_3_3_d12-en-predicate-consolidatie.md`

## Test 7 — Scope-uitsluiting

**Vraag:** *"Waarom is UCF (Unified Compliance Framework) niet opgenomen in het kennismodel?"*

**Verwachte uitkomst:** vier redenen:

1. Conceptuele overlap — UCF doet vrijwel hetzelfde als ons model (meta-mapping van authority documents)
2. IP- en licentiebeperkingen — Network Frontiers LLC, patent + licentie-overeenkomst
3. Commerciële afhankelijkheid — enterprise-tier licenties (tienduizenden dollars/jaar)
4. Geen Rijksoverheid-specifieke meerwaarde — internationaal-generiek

Mag wel als marktbenchmark genoemd worden in projectdocumentatie.

**Brain-pad:** `brain__scope__UCF-uitgesloten.md`

## Test 8 — Concept-uitleg

**Vraag:** *"Wat betekent framework-neutraliteit in dit project en waar komt het vandaan?"*

**Verwachte uitkomst:**

Alle normen/wetten/kaders zijn architectureel gelijkwaardig — geen privilege voor BIO of NIS2 of welk framework dan ook. BIO 2.0 is *toepassingsperspectief* voor dashboard/rapportage, geen architectuur-centrum.

Vastgelegd 17 maart 2026 (D9) na correctie van eerdere "NIS2 als primaire driver" en "BIO 2.0 als operationeel uitgangspunt"-framings. Sindsdien architectuur-invariant.

Architectuur-test bij elke module-uitbreiding: *"Landt dit framework als gelijkwaardige individual naast bestaande, of probeert het zich als centrum te positioneren?"*

**Brain-pad:** `brain__decisions__D09_framework-neutraliteit.md` + `brain__concepts__framework-neutraliteit.md`

## Test 9 — Workflow-procedure

**Vraag:** *"Wat moet ik doen als ik tijdens een sprint een scope-afwijking ontdek?"*

**Verwachte uitkomst:** vier-stappen-pauzeer-protocol:

1. **Pauzeren vóór wijziging** — geen edits, geen voor-uit-werk
2. **Rapporteren aan Master** met Optie A/B/C + korte voor/tegen per optie
3. **Wachten op GO** — geen vooruitlopen
4. **Uitvoeren + documenteren** in patch-rapport

Vier trigger-categorieën die pauze rechtvaardigen: inventaris-discrepantie, onbekende scope-uitbreiding, architectuur-aanrakingspunt, telling-discrepantie.

**Brain-pad:** `brain__workflow__scope-discipline.md`

## Test 10 — Meta-vraag (vault-functionaliteit)

**Vraag:** *"Welke iteraties zijn er gedaan om deze brain-vault op te bouwen?"*

**Verwachte uitkomst:** 7 iteraties (0-6) + iteratie 7 (deze), ~93 brain-bestanden in 8 folders. Volgende: iteratie 8 (Claude Code / Obsidian migratie-prep, optioneel).

**Brain-pad:** `brain__log.md` + `brain__index.md`

## Interpretatie van smoke-test-resultaten

| Uitkomst | Betekenis |
|---|---|
| Antwoord matcht 100% met verwachte uitkomst | Brain werkt voor deze gebruiks-vraag ✓ |
| Antwoord matcht in essentie maar mist details | Brain werkt, maar specifieke file is mogelijk niet retrieved — overweeg betere wikilinks |
| Antwoord matcht hoofdpunten maar voegt verkeerde info toe | Mogelijk inconsistentie tussen brain-files — onderzoeken |
| Antwoord wijst de gebruiker terug naar bron-bestanden | Brain heeft gat — bestand ontbreekt of is niet vindbaar |
| Antwoord faalt volledig | Brain niet bereikt — Project Knowledge ingeschakeld? Files geüpload? |

## Periodieke check

Aanbevolen: smoke-tests jaarlijks of na elke 5 nieuwe brain-files opnieuw uitvoeren. Daarmee vang je drift (gewijzigde files, nieuwe info die elders nog niet is bijgewerkt) op.

## Cross-references

- [[brain__index]] — masterindex
- [[brain__CLAUDE]] — vault-spec
- [[brain__log]] — historisch logboek

— Einde smoke-tests.
