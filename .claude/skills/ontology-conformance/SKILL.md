---
name: ontology-conformance
description: D1–D12 + D4.1 design-decision-conformance-checklist voor OWL/Turtle-werk in de GRC Kennismodel-ontologie. Auto-load bij ontology/*.ttl-bewerkingen. Codificeert de architecturale regels die voor elke TTL-wijziging gelden, zonder verbatim normtekst.
paths: ontology/*.ttl, ontology/**/*.ttl
---

# ontology-conformance — D-decision-checklist voor TTL-werk

Voor elke wijziging in `ontology/*.ttl`: D1-D12 + D4.1 lopen langs als deterministische checklist. Bij vermoedelijke schending: scope-pauze conform `docs/sprint-protocols.md` §15.

Geen NEN-verbatim-tekst. Alleen de architecturale design-decision-regels + waar de full decision staat (brain-vault).

## D-decisions verkorte conventies

| D | Korte conventie | Authoritatieve bron |
|---|---|---|
| D1 | **OWL 2 DL profiel** — geen `rdfs:subClassOf`-cycles; geen `owl:Thing` als `rdfs:domain`/`rdfs:range`; geen disjoint between intersection-classes onder DL-restricties | `brain/brain__decisions__D01_owl2-dl-profiel.md` |
| D2 | **Turtle-serialisatie** — geen RDF/XML, geen JSON-LD; UTF-8; ttl-extensie | `brain/brain__decisions__D02_turtle-serialisatie.md` |
| D3 | **11 namespaces** — `fw / ctrl / risk / roles / compl / isms / biz / bio / ext / asset / csf` — geen nieuwe namespace zonder masterchat-besluit | `brain/brain__decisions__D03_namespaces.md` |
| D4 | **SKOS voor cross-framework mappings** — `closeMatch` default, `relatedMatch` voor partial/cross-category, `exactMatch` zeldzaam (alleen bij bewezen semantische identiteit) | `brain/brain__decisions__D04_skos-cross-framework.md` |
| D4.1 | **Cross-category-mappings = relatedMatch** (T3-precedent v4.6.3) — control ↔ legal-obligation is associatief, NIET subsumptief. `broadMatch`/`narrowMatch` UITSLUITEND binnen dezelfde categorie (control↔control, obligation↔obligation). T3 m14 AVG/GDPR: 2 mutaties `broadMatch → relatedMatch`. | `brain/brain__decisions__D04_skos-cross-framework.md` §"D4.1-cross-category-rationale" + `brain/brain__concepts__cross-category-mappings.md` |
| D5 | **`owl:sameAs` strikt `ctrl:↔bio:`** — exact 93 paren — geen uitbreiding zonder masterchat-besluit | `brain/brain__decisions__D05_owl-sameas-ctrl-bio.md` |
| D6 | **Bilinguale annotaties `@nl/@en`** — meeliftregel + vertaling-scope-uitbreiding (symmetrisch `@en`-only voor lange normatieve EN-tekst); annotaties NOOIT taal-loos behalve `ext:sourceAttribution` + technical strings | `brain/brain__decisions__D06_bilinguale-annotaties.md` |
| D7 | **BIO 2.0 als twee klassen** — `bio:BIOControl` + `bio:OverheidsMaatregel`; geen samenvoeging tot één klasse | `brain/brain__decisions__D07_bio2-twee-klassen.md` |
| D8 | **Eén canonieke SoA** — `isms:SoA_2026` + 93 `SoAEntry_*`; geen tweede SoA-container | `brain/brain__decisions__D08_canonieke-soa.md` |
| D9 | **Framework-neutraal** — geen architectureel centraal kader; alle frameworks (ISO 27001, BIO, NIST CSF, NIS2, DORA, GDPR, ENSIA, COSO, ISO 22301, ISO 27701) gelijkwaardig in TBox-positie; BIO 2.0 alleen als view-keuze in dashboard | `brain/brain__decisions__D09_framework-neutraal.md` |
| D10 | **COSO ICF/ERM als enterprise-governance-laag** — boven tactische frameworks, niet daarnaast | `brain/brain__decisions__D10_coso-governance-laag.md` |
| D11 | **`owl:sameAs` asset-convergentie** — ster-patroon (5 bruggen) — geen uitbreiding zonder masterchat-besluit | `brain/brain__decisions__D11_asset-convergentie.md` |
| D12 | **Drie-laags compliance** — regulatory obligation / legal obligation / requirement — patroon, geen starre symmetrie | `brain/brain__decisions__D12_drie-laags-compliance.md` |

## Pre-edit-checklist (verplicht vóór elke TTL-wijziging)

1. **D1** — produceert deze edit een cycle in `rdfs:subClassOf` of `owl:equivalentClass`? Plaatst `owl:Thing` in domain/range? → STOP
2. **D2** — bewaar Turtle-serialisatie; geen ttl→jsonld-conversie
3. **D3** — gebruik je een nieuwe namespace? → scope-pauze
4. **D4** — kies je predicate-precision: `closeMatch` (semantische overlap), `relatedMatch` (partial of cross-category), `broadMatch`/`narrowMatch` (subsumptief, ALLEEN binnen dezelfde categorie per D4.1), `exactMatch` (semantische identiteit, zeldzaam)
5. **D4.1** — kruist deze mapping een categorie-grens (bv. control ↔ legal-obligation)? → `relatedMatch` ONGEACHT vermeende inclusie-richting
6. **D5** — voeg je `owl:sameAs` toe op `ctrl:↔bio:`? → controleer 93-paren-limit; uitbreiding = masterchat
7. **D6** — bevat de nieuwe entity bilinguale `@nl/@en`-annotaties? → meeliftregel toepassen
8. **D7** — gebruik je `bio:BIOControl` of `bio:OverheidsMaatregel`? → niet samenvoegen
9. **D8** — voeg je SoA-entry toe? → in `isms:SoA_2026`, geen nieuwe container
10. **D9** — beweeg je een framework architecturaal centraler? → STOP, framework-neutraliteit invariant
11. **D11** — voeg je `owl:sameAs` toe op asset-niveau? → controleer ster-patroon (5 bruggen)
12. **D12** — modelleer je compliance? → drie-laags-patroon: regulatory obligation / legal obligation / requirement

## Post-edit-verificatie

- Triple-Δ-raming opgesteld vóór edit? Werkelijk-Δ binnen 30% van raming?
- Parse-check: `g.parse(fp, format="turtle")` zonder errors?
- `/canonical-metrics`-skill draaien: zes invariantie-metrics consistent met verwachting?
- `/shacl-split`-skill draaien: SECTIE A=0 + SECTIE B=0 (COMBINED ≈ 290 ±k baseline)?
- Drift t.o.v. vorige versie expliciet declareren in patch-rapport §0

## Conformance-check-output

Bij rapportage in patch-rapport §10 (D-conformiteit):

| D | Status | Onderbouwing |
|---|---|---|
| D1 | ✅ / ⚠️ / ❌ | (kort) |
| ... | ... | ... |

Bij ❌ of ⚠️: scope-pauze conform Protocol 15.

## Vermijdingen

- Geen `rdfs:subClassOf` met `owl:Thing` als target
- Geen `owl:equivalentClass` zonder bilaterale onderbouwing
- Geen `skos:broadMatch` over categorie-grenzen (D4.1)
- Geen nieuwe namespace zonder D3-uitbreidings-besluit
- Geen `owl:sameAs` buiten D5 / D11-scope

## Cross-references

- D-register: `brain/brain__decisions__D-register.md`
- Sprint-protocollen (scope-pauze): `docs/sprint-protocols.md` §15
- Concept (cross-category): `brain/brain__concepts__cross-category-mappings.md`
- Verificatie-skills: `/canonical-metrics`, `/shacl-split`
