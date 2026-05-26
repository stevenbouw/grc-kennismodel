---
type: sprint
id: v4.2.2
title: v4.2.2 — SoA-canonisering Route A
status: superseded
date: 2026-04-13
related:
  - v4_2_0_M18-asset-module
  - v4_3_0_gap-sprint-d11
  - D08_canonieke-soa
sources:
  - patch-rapport-v4_2_2-soa-opschoning
  - g9-diagnostiek-soaentry-108
chat-sources: []
confidence: high
---

# v4.2.2 — SoA-canonisering Route A

## Status

**Rijke reconstructie** uit `patch-rapport-v4_2_2-soa-opschoning.md` en `g9-diagnostiek-soaentry-108.md` (beide 13 april 2026).

## Aanleiding: G9-diagnostiek

Tijdens risk-coupling nulmeting v4.2.1 (13 april 2026) viel een vreemde SoAEntry-count op: **108 in plaats van de verwachte 93**. G9-diagnostiek toonde aan dat dit géén duplicatie op control-niveau was en géén uitbreiding richting overheidsmaatregelen.

**Werkelijkheid:** twee parallelle SoA-structuren coexisteerden in `m06-isms.ttl`:

| Set | Aantal | Container | Koppelrichting | Controls |
|---|---:|---|---|---:|
| `isms:SOA_*` | 15 | `isms:SOA_v1` | `containsEntry` (top-down) | 15 (subset) |
| `isms:SoAEntry_*` | 93 | `isms:SoA_2026` | `forSoA` (bottom-up) | 93 (volledig) |

De 15 `SOA_*`-entries waren een **volledige subset** van de 93 `SoAEntry_*`-entries → 15 controls hadden twee SoAEntry-registraties.

Classificatie: **Scenario 2 — onbedoelde duplicatie** (regressie). Twee ontwerpiteraties waren over elkaar heen komen te liggen zonder consolidatie.

## Masterchat-keuze: Route A

Twee opties voorgelegd:

- **Route A — canonisering:** `SoA_2026` + 93 `SoAEntry_*` wordt enige SoA. `SOA_v1` + 15 `SOA_*` verwijderd.
- **Route B — formele co-existentie:** `SOA_v1` als "versie 1.0 — initiële selectie Q1-2026", `SoA_2026` als "versie 2.0 — volledige baseline" met `prov:wasRevisionOf`-triple.

**GO op Route A.** Reden: de 15 `SOA_*`-entries lijken initiële voorbeelden die na opstellen van de volledige 93-set hun functie verloren hebben. Geen externe verwijzingen (grep-pre-check: 0 hits buiten `m06-isms.ttl`).

## Uitgevoerd

### Verwijderd uit `m06-isms.ttl` (16 individuals)

- `isms:SOA_v1` (20 triples)
- 15× `isms:SOA_X_YY`: SOA_5_01, _5_02, _5_09, _5_15, _5_19, _5_24, _5_29, _5_35, _6_03, _8_05, _8_07, _8_08, _8_13, _8_24, _8_25

### Toegevoegd

**Eén canoniseringsspiegel-triple:**

```turtle
isms:ISMS_HoofdOrganisatie isms:hasSoA isms:SoA_2026 .
```

### Versiebump

`grc-core.ttl` `owl:versionInfo "4.2.1"` → `"4.2.2"`.

## Net-delta

**−123 triples** (124 verwijderd, 1 toegevoegd).

## Validatie

Alle vier validatiegates groen:

1. Parse-check: 21 bestanden foutloos
2. OWL RL reasoner: 0 inconsistenties, 0 disjointness-violations
3. Gesplitste SHACL: SECTIE A = 0 violations, SECTIE B = 0 violations
4. SPARQL smoke tests: Q1 = 80 controls (40+40), Q3 = 7 TBB — exact zoals v4.2.1

Alle zes semantische invariantie-metrics (klassen, individuals, properties, sameAs, appliesToAssetType) buiten doelmetrics identiek aan v4.2.1.

## Pre-check als precedent

§1.1 grep-resultaten introduceren een werkwijze die later standaard wordt voor v4.3.x:

- Letterlijke string-zoekopdracht op alle te-verwijderen IRI's
- Regex-zoekopdracht op patroon
- Controle op zowel `m06-isms.ttl` als alle andere bestanden
- GROEN-criterium: 0 hits buiten het edit-bestand

Vergelijkbare pre-checks in v4.3.3 voor `ext:articleNumber`-hardverwijdering.

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-04-13 | active | G9-diagnostiek opgeleverd |
| 2026-04-13 | active | Masterchat-GO Route A |
| 2026-04-13 | active | v4.2.2 oplevering |
| 2026-04-13 | superseded | Opgevolgd door v4.3.0 gap-sprint |

— Einde v4.2.2.
