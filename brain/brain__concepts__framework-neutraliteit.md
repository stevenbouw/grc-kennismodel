---
type: concept
title: Framework-neutraliteit (D9)
status: living
date: 2026-05-19
related:
  - D09_framework-neutraliteit
  - D10_coso-enterprise-governance
  - D11_sameAs-asset-convergentie
  - D12_drie-laags-compliance
  - v4_4_0_fase-2-cbw-cbb
  - v4_5_0_fase-3-nist-csf-2-0
sources:
  - projectinstructie-v1.7
chat-sources: []
confidence: high
---

# Framework-neutraliteit (D9)

## Wat het is

**Framework-neutraliteit** is de architectuur-invariant dat **alle normen, wetten en kaders architectureel gelijkwaardig zijn**. Geen enkel framework krijgt een centraal organiserend privilege; alle worden gemodelleerd als individuals met onderlinge relaties.

Vastgelegd in [[brain__decisions__D09_framework-neutraliteit]] op 17 maart 2026 — initieel als principe-besluit, daarna aantoonbaar geverifieerd op concrete clusters.

## Wat het NIET betekent

| Misverstand | Werkelijkheid |
|---|---|
| Alle frameworks krijgen gelijke populatie-diepte | Nee — sommige zijn rijk uitgewerkt (BIO, NIS2), andere beperkt tot relevant subset (DORA, AVG) |
| BIO 2.0 is "onbelangrijk" geworden | Nee — voor *gebruik* (dashboard, rapportage) is BIO 2.0 primair perspectief |
| Geen prioriteit in implementatie | Nee — fase-planning bepaalt volgorde, maar geen architectuur-bias |

## Architectuur-test bij elke nieuwe module

> **De vraag:** *"Landt dit framework als gelijkwaardige individual naast de bestaande, of probeert het zich als 'centrum' te positioneren?"*

## Drie verificatie-clusters (cumulatief)

### Cluster 1 — NIS2-EU + CBW-NL (v4.4.0)

`fw:CBW fw:isTranspositieVan fw:NIS2_Directive` — horizontale transpositie-relatie, geen hiërarchie.

### Cluster 2 — CBW-NL + Cbb-AMvB (v4.4.0)

`fw:CBW fw:uitgewerktIn fw:Cbb` — cluster-relatie tussen wet en AMvB, gelijkwaardig.

### Cluster 3 — NIST CSF 2.0 als gemapt referentiekader (v4.5.0)

**Concrete Optie B-toepassing.** Twee modelleer-opties stonden open:

| Optie | Beschrijving | Status |
|---|---|---|
| **A** — CSF als organiserend kader | Bestaande controls zouden onder CSF Functions/Categories gepositioneerd worden | ❌ Schendt D9 |
| **B** — CSF als gemapt referentiekader | CSF-componenten staan náást bestaande kaders; SKOS-mappings beschrijven relaties | ✓ Gekozen |

**D9-compatibiliteits-bewijs voor M21:**

| Implementatie-keuze | D9-compatibel |
|---|---|
| 11e namespace náást ISO/NIST 800-53/BIO | ✓ gelijkwaardig, niet centraal |
| Geen CSF-eigen control-klassen | ✓ Subcategories blijven outcomes, niet beheersmaatregelen |
| 1.448 SKOS-mappings naar bestaande kaders | ✓ CSF positioneert zich relatief, niet als root |
| `ext:isComponentOf fw:NIST_CSF_2_0` | ✓ generiek componenten-pattern (m17-precedent) |

Per v4.5.0 dus **drie clusters aantoonbaar D9-conform**.

## Onderscheid model versus dashboard

| Laag | Discipline |
|---|---|
| **Model** | Framework-neutraal — geen privileges |
| **Dashboard / rapportage** | BIO 2.0 als primair perspectief (view-keuze, geen architectuur-keuze) |

> "Het model is het woordenboek (neutraal), het dashboard is het verhaal (perspectief)."

## Toekomstige tests

Bij elke nieuwe module/framework-uitbreiding wordt D9 opnieuw toegepast:

- **M19 ISO 42001** (AI, eventueel later Fase 4+) — D9-test moet slagen
- **M20 ISO 9001** (eventueel later) — D9-test moet slagen
- Nieuwe sector-specifieke frameworks (TPRM, SOC 2, etc.) — D9-test bij elke overweging

## Toepassingen tot dusver

| Framework | Implementatie | D9-status |
|---|---|---|
| BIO 2.0 | Operationeel kader Laag 3 | ✓ — gelijkwaardig, niet centraal |
| NIS2 | Toetskader Laag 2 | ✓ — gelijkwaardig |
| CBW + Cbb | NL-wetgeving Laag 2 | ✓ — clusters horizontaal gerelateerd |
| **NIST CSF 2.0** *(v4.5.0)* | **Gemapt referentiekader (Optie B)** | **✓ — concrete D9-toepassing** |
| UCF (overwogen) | Buiten scope | ❌ D9-conflict was één van vier redenen ([[brain__scope__UCF-uitgesloten]]) |

## Cross-references

- [[brain__decisions__D09_framework-neutraliteit]] — formele beslissing
- [[brain__decisions__D03_10-namespaces]] — csf:-uitbreiding conform D9
- [[brain__sprints__v4_4_0_fase-2-cbw-cbb]] — eerste twee clusters geverifieerd
- [[brain__sprints__v4_5_0_fase-3-nist-csf-2-0]] — derde cluster (CSF Optie B)
- [[brain__modules__M21_nist-csf-2-0-planned]] — concrete Optie B-implementatie
- [[brain__scope__UCF-uitgesloten]] — D9-conflict-reden

— Einde framework-neutraliteit.
