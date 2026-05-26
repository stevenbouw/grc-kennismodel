---
type: sprint
id: v4.3.1
title: v4.3.1 — patch-bump (H18, F, A, B₂, C)
status: superseded
date: 2026-04-20
related:
  - v4_3_0_gap-sprint-d11
  - v4_3_2_smart-quotes-en-asymmetrie
sources:
  - patch-rapport-v4_3_1
chat-sources: []
confidence: high
---

# v4.3.1 — patch-bump

## Status

**Rijke reconstructie** uit `patch-rapport-v4_3_1.md` (20 april 2026).

## Scope: zes items met drie scope-pauzes

| Item | Inhoud | Scope-pauze? |
|---|---|---|
| **H18** | Dangling HSClause-refs + nieuwe klasse ext:HSClause | Ja (1) |
| **F** | `isms:containsEntry owl:inverseOf isms:forSoA` | Nee |
| **A** | 93 tweetalige `rdfs:label` op ISO 27002-controls (Route X) | Nee |
| **B₂** | 93 SoAEntry-labels vervangen (afkappingsbug opgelost) | Ja (2) |
| **C** | `rdfs:domain` op drie DatatypeProperties (H22) | Ja (3) |
| **Canonieke meetmethode** | Scripts opgeleverd | Nee |

## H18 — Dangling HSClause-refs (scope-pauze 1)

**Probleem v4.3.0:** 41 triples verwezen naar 7 `ext:HSClause_*`-individuals die nooit gedeclareerd waren.

**Pauze:** instructie-tekst §3.1 was slordig in IRI-notatie (`ext:HSClause_4` t/m `_10`), terwijl feitelijke dangling IRIs beschrijvende suffixen hadden (`ext:HSClause_4_Context` etc.). Daarnaast bestond geen passende klasse.

**Twee opties voorgelegd, masterchat-GO:**

- **Optie 1A** — declareren onder feitelijke IRIs met suffix
- **Optie 2B** — nieuwe klasse `ext:HSClause` (subClassOf `ext:FrameworkComponent`)

Masterchat voegde **scope-completion** toe: TBox-declaratie van `ext:alignsWithHSClause` als ObjectProperty.

**Uitgevoerd in `m09-iso27001-ext.ttl`:**

- Klasse `ext:HSClause` (subClassOf `ext:FrameworkComponent`) + tweetalige label/comment
- ObjectProperty `ext:alignsWithHSClause` (domain `ext:ISMSRequirement`, range `ext:HSClause`)
- 7 individuals: `HSClause_{4_Context, 5_Leadership, 6_Planning, 7_Support, 8_Operation, 9_PerformanceEvaluation, 10_Improvement}` met tweetalige labels
- D6-meelift: module-header EN-label toegevoegd

**Delta m09:** +42 triples.

## F — `containsEntry owl:inverseOf forSoA`

Toegevoegd aan `m06-isms.ttl`. **Onder OWL RL propageert dit tot +93 inferred `containsEntry`-asserties** (forSoA had 93 asserties, containsEntry had 0). Post-inferentie: containsEntry = forSoA = 93.

Cumulatief effect: `isms:SoA_2026` "ziet" nu zijn 93 entries via inverse-relatie.

D6-meelift edit-scope: `rdfs:comment@nl/@en` toegevoegd op `containsEntry` (pariteit met `forSoA`).

**Delta m06:** +3 triples.

## A — 93 tweetalige labels op ISO 27002-controls (Route X)

**Bron NL:** bestaande `ctrl:hasControlTitle@nl` op de 93 controls. 93/93 schoon.
**Bron EN:** `NEN-EN-ISO_IEC_27002_2022_en.pdf` (door projecteigenaar geleverd). Regex-extractie met sanity-check.

**Bijvangst:** `ctrl:ISO27002_7_07` en `ctrl:ISO27002_8_01` gebruikten smart quotes (U+2018/U+2019). Verbatim overgenomen conform §3.2 (bron-getrouw); **geen reparatie binnen v4.3.1**. (Reparatie volgt in v4.3.2.)

**Extractie-correctie 5.29:** regex trof aanvankelijk een legacy ISO 27002:2013-mapping ("17.1.1, 17.1.2, 17.1.3") als prefix. Directe PDF-lezing pagina 64 bevestigde correcte titel "Information security during disruption". Gecorrigeerd.

**Delta m02:** +186 triples (93 × 2 talen).

## B₂ — 93 SoAEntry-labels vervangen (scope-pauze 2)

**Pre-check toonde:** alle 93 `isms:SoAEntry_*` hadden al een `rdfs:label`-triple, in format `"SoA: <titel>"@nl` (prefix "SoA:", niet "SoA-entry:" zoals §3.3 voorschreef).

**Latent defect ontdekt:** `SoAEntry_5_02` had afgekapte NL-label: `"SoA: Rollen en verantwoordelijkheden bij informatiebeveiligi"@nl` (laatste drie letters `ng` ontbraken mid-woord).

**Drie opties voorgelegd, masterchat-GO B₂:** vervangen (niet toevoegen of behouden).

**Uitgevoerd in `m06-isms.ttl`:** 93 × vervangen van `rdfs:label "SoA: ..."@nl ;` door `rdfs:label "SoA-entry: <NL>"@nl , "SoA entry: <EN>"@en ;`.

| IRI | v4.3.0 label | v4.3.1 label |
|---|---|---|
| `isms:SoAEntry_5_02` | `"SoA: Rollen en verantwoordelijkheden bij informatiebeveiligi"@nl` | `"SoA-entry: Rollen en verantwoordelijkheden bij informatiebeveiliging"@nl` (+ EN) |

**Delta m06 netto:** +93 triples (−93 oude, +186 nieuwe). Cumulatief m06: +96.

## C — rdfs:domain op drie DatatypeProperties (scope-pauze 3)

§3.4 procedure: per property SPARQL op type-distributie + voorstel minst-inclusieve gemeenschappelijke superklasse + per-property GO. Masterchat gaf drie GO's tegelijk.

Drie properties in `grc-core.ttl` kregen `rdfs:domain`-restrictie. (Detail: `clauseNumber`, `articleNumber`, `controlFamilyCode` — vermoedelijk, basis van H22-context.)

## §10.2 meetcorrectie (administratief)

SPARQL-verificatie 0 hits op "556" in model-annotaties; canonieke waarde **973** (`asset:appliesToAssetType` inferred onder OWL RL). Geen model-wijziging.

## Eindstaat v4.3.1

- Pre-inferentie: 12.354 → **12.681** (+327)
- Post-inferentie: 29.054 → **29.703** (+649)
- SHACL RUN 1 = 0, RUN 2 = 290 (identiek aan v4.3.0)
- 0 nieuwe inconsistenties, 0 `owl:Nothing` post-inferentie
- Drie data-bestanden gewijzigd: `m02-control.ttl`, `m06-isms.ttl`, `m09-iso27001-ext.ttl`
- Plus `grc-core.ttl` (C1/C2/C3 domains + versie-metadata)

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-04-20 | active | v4.3.1 oplevering |
| ±2026-04-21 | superseded | Opgevolgd door v4.3.2 |

— Einde v4.3.1.
