---
type: module
id: M02
title: M02 — Controls ISO 27002 (ctrl:)
status: active
date: 2026-05-19
related:
  - D05_sameAs-strikt-ctrl-bio
  - D06_meeliftregel-tweetalig
  - meeliftregel-edit-scope
  - v4_5_0_fase-3-nist-csf-2-0
sources:
  - NEN-EN-ISO_IEC_27002_2022_nl
chat-sources: []
confidence: high
---

# M02 — Controls (ISO 27002)

## Bestand
`m02-control.ttl`

## Namespace
`ctrl: <https://grc.example.org/control/>`

## Wat het bevat

Generieke control-laag voor ISO 27002:2022 (93 controls) + ondersteunende ISO 27002-attributen.

| Inhoud | Aantal |
|---|---:|
| `ctrl:ISO27002_X_YY`-individuals (93 controls) | 93 |
| Klassen | `ctrl:Control`, `ctrl:ISO27002Control`, `ctrl:CBWControl` (v4.4.0), `ctrl:CybersecurityConcept`, en attributen-klassen |
| ISO 27002-attributen | `ctrl:controlType`, `ctrl:operationalCapability`, `ctrl:securityDomain`, `ctrl:cybersecurityConcept`, `ctrl:cia` |
| Cybersecurity-concepten (ConceptScheme) | 6 (Govern + 5 originelen — zie v4.5.0 update) |

## v4.5.0-update — D6 meeliftregel toegepast

In v4.5.0 is de **CSF v1.x → v2.0-uitbreiding** verwerkt in `ctrl:CybersecurityConcept`:

| Aspect | Wijziging |
|---|---|
| Annotatie-doelwit | `ctrl:CybersecurityConcept` ConceptScheme |
| Wijziging | comment-tekst van 5 Functions (Identify/Protect/Detect/Respond/Recover) → 6 Functions (incl. **GOVERN**) |
| Edit-scope | Alleen deze ConceptScheme — overige M02-content ongemoeid |
| Tweetaligheid | Comment bijgewerkt in @nl én @en (korte titel-fraseringen, conform D6 vertaling-scope v1.7) |

Concrete toepassing van [[brain__decisions__D06_meeliftregel-tweetalig]] edit-scope-discipline.

### Kandidaat-H-item voor latere overweging

`ctrl:CybersecurityConcept` modelleert nu dezelfde 6 categorieën als `csf:Function` (GOVERN/IDENTIFY/PROTECT/DETECT/RESPOND/RECOVER). **Overlap-vraag**: beide modelleren outcomes-niveau cybersecurity-concept.

**Niet als formeel H-item geregistreerd** in v4.5.0, maar gedocumenteerd als kandidaat voor latere SKOS-mapping (mogelijk `skos:exactMatch` `ctrl:Cyber*` ↔ `csf:*`-Functions). Zie sprint v4.5.0 §8 punt 16 voor context.

## Naamgevingsconventie

Canoniek `ISO27002_X_YY` met YY zero-padded (vastgelegd v4.1.0 Actie D). SHACL-pattern `^https://grc\.example\.org/control/ISO27002_[5-8]_[0-9]{2}$` bewaakt naming.

## D-relaties

- [[brain__decisions__D05_sameAs-strikt-ctrl-bio]] — 93 owl:sameAs-asserties brug naar bio: (in `grc-bridges.ttl`)
- [[brain__decisions__D06_meeliftregel-tweetalig]] — edit-scope-discipline; toegepast in v4.5.0

## SHACL

ctrl:ISO27002NamingShape (SECTIE A, inference='none') — 93 violations onder combined SHACL-run = bekend false-positive door sameAs-propagatie. Zie [[brain__concepts__gesplitste-shacl-validatie]].

## Bronlicentie

ISO 27002:2022 valt onder NEN-restrictief — geen verbatim tekstreproductie. M02 bevat alleen de IRI-conventies + ondersteunende klassen, geen ISO-tekst.

## Cross-references

- [[brain__sources__iso-normen-bundle]] — NEN-licentie-context
- [[brain__sprints__v4_1_0-alpha_werkpakket-opschoning]] — Actie D naamgevings-canonisering
- [[brain__sprints__v4_5_0_fase-3-nist-csf-2-0]] — D6 meeliftregel-toepassing v1.x→v2.0
- [[brain__concepts__sameAs-discipline]] — D5-context (ctrl:↔bio: 93 sameAs)

— Einde M02.
