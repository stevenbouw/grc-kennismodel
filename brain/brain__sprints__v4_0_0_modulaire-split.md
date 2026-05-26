---
type: sprint
id: v4.0.0
title: v4.0.0 — modulaire split (16 → 19 bestanden)
status: superseded
date: 2026-04-01
related:
  - v3_0_monolithisch
  - v4_1_0-alpha_werkpakket-opschoning
  - D03_10-namespaces
sources: []
chat-sources:
  - https://claude.ai/chat/76420a5b-11ac-4f22-af7a-5e2404201bdd
  - https://claude.ai/chat/5ca3214f-1949-42ef-be10-10d2e91d648e
confidence: high
gaps:
  - "Exacte release-datum van v4.0.0 onbekend; ergens tussen 19 maart (briefing) en 9 april 2026 (operationeel in tech-chat)"
---

# v4.0.0 — modulaire split

## Status

**Rijke reconstructie.** v4.0.0 transformeerde de monolithische `grc-ontologie-v3.ttl` (één bestand, 13.292 regels) naar **16 modulaire bestanden** in een gestructureerd refactor-stappenplan van 22 stappen.

## Refactor-stappenplan (22 stappen, gegroepeerd)

| Groep | Stappen | Inhoud |
|---|---|---|
| 1. Structuur | 1 | Split monoliet naar modulaire bestanden |
| 2. Bugfixes | 2–3 | BUG-01 t/m BUG-06 oplossen |
| 3. Verrijking | 4–22 | Nieuwe modules, mappings, validatie |

### Stap 0 — Namespace-migratie

Alle 9 domein-namespaces gemigreerd van `https://grc.organisatie.nl/ontology/XXX#` naar `https://grc.example.org/XXX/` (slash-separator, organisatie-neutrale host). Voorbereiding voor toekomstige overdracht naar andere Rijksoverheidsorganisaties (architectuur-invariant).

### Stap 1 — Modulaire split

`grc-ontologie-v3.ttl` (13.292 regels) gesplitst in **16 bestanden**:

| Bestand | Inhoud | Bron in v3 |
|---|---|---|
| `grc-core.ttl` | Ontologie-metadata, owl:imports, gedeelde ext: TBox-klassen | Header + M9-M13 shared classes |
| `m01-framework.ttl` | 15 klassen, fw: individuals, SKOS-alignments | M1 + FIX 3 |
| `m02-control.ttl` | 93 ISO 27002-controls, BBN-klassen/properties | M2 |
| `m03-risk.ttl` | Risicomodel | M3 |
| `m04-roles.ttl` | Rollen, RACI-structuur | M4 |
| `m05-compliance.ttl` | Compliance-eisen + VIR/VIRBI/BVA-verplichtingen | M5 + FIX 3 |
| `m06-isms.ttl` | ISMS-structuur + 93 SoA-entries | M6 + SoA-blok |
| `m07-business.ttl` | Businesscontext | M7 |
| `m08-bio20.ttl` | 93 BIO controls + overheidsmaatregelen + BBN | M8 |
| `m09-iso27001-ext.ttl` | ISO 27001:2022 clausules 4-10 | M9 |
| `m10-nis2-ext.ttl` | NIS2 art. 18-24 + art. 21a-j + 118 SKOS-mappings | M10 |
| `m11-nist-800-53.ttl` | 20 NIST control families | M11 |
| `m12-dora.ttl` | DORA art. 5-19 | M12 |
| `m13-iso22301.ttl` | ISO 22301 BCM clausules | M13 |
| `grc-bridges.ttl` | 94 owl:sameAs ctrl:↔bio: (D5) | FIX 1 |
| `m-cobit-interim.ttl` | COBIT 2019 objectives (8 individuals), tijdelijk | FIX 3 (COBIT) |

**Validatie na split:** 157 klassen, 572 individuals, 94 owl:sameAs — **exact match met v3.0**. Inhoud ongewijzigd, alleen herverdeeld.

### Stap 2 — Bugfixes BUG-01 t/m BUG-05

- BUG-01: `fw:CyberBeveiligingswet` verwijderd, behoud `fw:CBW` met owl:sameAs als redirect
- BUG-02 t/m BUG-05: rdf:type-declaraties toegevoegd aan vier framework-individuals

### Stap 3 — Fix BUG-06 (BBN herlabelen)

`bio:bbnNiveau` data-property gemigreerd om correct naar Handreiking BIO2-opmaat te verwijzen i.p.v. BIO 2.0 zelf — voorbereiding voor latere `ext:hasHandreikingBBN`-consolidatie in v4.1.0-alpha.

### Stappen 4–22 — Verrijking

Nieuwe modules toegevoegd tijdens latere stappen:

- **M14** — AVG/GDPR (art. 5(1f), 25, 32–34)
- **M15** — ENSIA (stub, Laag 5 pending)
- **M16** — VIRBI-extensie
- **M17** — COSO/COBIT (uit `m-cobit-interim.ttl` geïntegreerd)

Eindtoestand v4.0.0: **19 modulaire bestanden** (16 originele + M14/M15/M16 + M17, met m-cobit-interim weggemerged in M17).

## v4.0.0-correctieve patch

Datum onbekend, vóór 10 april 2026. Inhoud: **27 HermiT-inconsistenties** opgelost door xsd:string-fix op data-properties met taalgetagde waarden. Geen versie-bump — bleef v4.0.0.

## Wat onbekend is

- Exacte release-datum van v4.0.0
- Of v4.0.0 één commit was of meerdere
- Of stap 4-22 in één doorlopende sprint of meerdere mini-sprints werden uitgevoerd

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-03-19 | active | Refactor-briefing v3 → v4 |
| ±2026-04-01 | active | v4.0.0 release (datum reconstructie) |
| ±2026-04-05 | active | Correctieve xsd:string-patch (27 inconsistenties) |
| 2026-04-10 | superseded | Opgevolgd door v4.1.0-alpha |

— Einde v4.0.0.
