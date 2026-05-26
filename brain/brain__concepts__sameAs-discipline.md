---
type: concept
title: owl:sameAs-discipline
status: living
date: 2026-05-13
related:
  - D05_sameAs-strikt-ctrl-bio
  - D11_sameAs-asset-convergentie
  - D04_skos-cross-framework
sources:
  - patch-rapport-v4_3_0
chat-sources: []
confidence: high
---

# owl:sameAs-discipline

## Wat het is

`owl:sameAs` is een **kracht­tig OWL-statement**: twee URIs verwijzen naar dezelfde entiteit. Onder OWL RL propageren alle properties tussen beide kanten — letterlijk alles wat aan kant A staat, geldt ook voor kant B.

In het GRC Kennismodel wordt sameAs **strikt gereguleerd** via twee scope-bounded toepassingen:

| Toepassing | Aantal asserties | Decision | Niveau |
|---|---:|---|---|
| D5 — ctrl: ↔ bio: ISO 27002-individuals | 93 | [[brain__decisions__D05_sameAs-strikt-ctrl-bio]] | ABox (instance) |
| D11 — asset: ↔ risk:/isms: asset-klassen | 5 | [[brain__decisions__D11_sameAs-asset-convergentie]] | TBox (klasse) |

**Totaal: 98 sameAs-asserties.** Uitbreiding zonder masterchat-GO is verboden.

## Waarom de discipline strikt is

sameAs is conceptueel sterk maar operationeel risicovol:

1. **Propagatie-impact:** elke property aan kant A wordt aan kant B geërfd (en omgekeerd). Een typo of inconsistentie aan één kant propageert direct.
2. **SHACL-shape-conflicten:** shapes die op kant A targets verwachten, krijgen onder OWL RL ook kant B-leden. Dat veroorzaakt false-positives (zie [[brain__concepts__gesplitste-shacl-validatie]]).
3. **Disjointness-clashes:** twee klassen kunnen niet tegelijk disjoint én sameAs zijn. Elke nieuwe sameAs vereist disjointness-impactanalyse.
4. **Reasoning-vereiste:** sameAs werkt alleen onder OWL RL of sterker — pure RDFS-inferentie ziet de brug niet. 128 BIO-mappings (D5-derived) blijven onzichtbaar zonder OWL RL.

## Wanneer wel sameAs, wanneer SKOS?

Beslis-criterium:

- **owl:sameAs** = "dit is *letterlijk dezelfde entiteit*, gewoon onder twee namen". Eén identiteit, twee URIs.
- **SKOS-property** = "deze twee concepten zijn *verwant* (gelijk / sterk overeenkomstig / breder / smaller / thematisch)". Twee identiteiten, één relatie.

Test: als A en B *altijd hetzelfde gedrag* zouden moeten vertonen onder elke OWL-property, gebruik sameAs. Als ze *gedeeltelijk* overlappen maar elk zijn eigen leven leiden, gebruik SKOS (zie [[brain__decisions__D04_skos-cross-framework]]).

## Praktische gevolgen voor toekomstige uitbreidingen

**Niet uitbreiden zonder masterchat-GO**:

- `risk:` ↔ `ctrl:` of `bio:` — geen identiteit, semantische verschillen
- Cross-framework framework-individuals: `fw:BIO_2_0` ≠ `fw:ISO_IEC_27002_2022` (verschillende juridische status)
- Control-objectives versus implementations

**Wanneer dat wel zou kunnen**:

- Toekomstige scope-uitbreidingen waar D9-framework-neutraliteit dwingt tot symmetrie (zoals D11 dwong na M18-integratie)
- ABox-population (Spoor B) waar fysieke assets via meerdere namespaces beschreven worden

In alle gevallen: masterchat-GO + **vooraf-denken aan afgeleide consequenties** (SHACL, disjointness, naming).

## Hangt samen met

- [[brain__decisions__D05_sameAs-strikt-ctrl-bio]] — instance-niveau ctrl ↔ bio
- [[brain__decisions__D11_sameAs-asset-convergentie]] — klasse-niveau asset ↔ risk/isms (ster-patroon)
- [[brain__concepts__owl-rl-reasoning]] — waarom OWL RL minimum is voor sameAs-werking
- [[brain__concepts__gesplitste-shacl-validatie]] — directe consequentie van sameAs-propagatie

— Einde sameAs-discipline.
