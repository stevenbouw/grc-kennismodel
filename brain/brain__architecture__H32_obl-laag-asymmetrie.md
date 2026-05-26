---
type: architecture
id: H32
title: H32 — OBL-laag modelleringsasymmetrie
status: open
date: 2026-05-13
related:
  - D12_drie-laags-compliance
  - H26_OBL-laag-gap-NIS2
  - v4_4_0_fase-2-cbw-cbb
sources:
  - projectinstructie-v1.7
chat-sources: []
confidence: high
---

# H32 — OBL-laag modelleringsasymmetrie

## Status

**Open** — geregistreerd post-v4.4.0 (13 mei 2026). Harmonisatie-richting onbeslist. Trigger: na v4.5.0 of bij Spoor B-organisatorische invulling van LegalObligation-individuals.

## Wat het is

Modelleringsasymmetrie tussen twee groepen `compl:LegalObligation`-individuals in de huidige ontologie:

| Groep | Aantal | Property-set |
|---|---:|---|
| **OBL_NIS2_Art{20,21,23}** | 3 | Uitgebreid: `hasObligationID`, `hasObligationTitle`, `hasArticleReference`, `isMandatory`, `sourcedFromFramework` |
| **Overige LegalObligations** | 35 | Minimaal: alleen `rdfs:label`/`rdfs:comment` + `articleRef` + `sourcedFromFramework` |

De drie OBL_NIS2-individuals hebben een rijker patroon dan de 35 overige. Beide groepen functioneren correct binnen D12-architectuur, maar de **inconsistentie in property-coverage** maakt cross-cluster queries en dashboard-rendering minder voorspelbaar.

## Hoe het ontstond

De OBL_NIS2_Art{20,21,23}-individuals zijn opgenomen in een vroegere sprint (v4.3.x) toen de drie-laags-architectuur nog werd ontwikkeld. Toen D12 in v4.3.3 werd geformaliseerd en uitgerold naar VIR, VIRBI, AVG, BVA-stelsel, en in v4.4.0 naar CBW + Cbb, hadden die latere LegalObligation-individuals geen vergelijkbaar property-detail nodig — minimale informatie volstond voor hun rol.

Resultaat: de eerste drie hebben "te veel" properties, de overige 35 hebben "net genoeg". Geen van beide is fout, maar samen vormen ze een patroon-inconsistentie.

## Twee harmonisatie-opties

**Optie A — Overige LegalObligations uitbreiden naar OBL_NIS2-patroon.**

| Voor | Tegen |
|---|---|
| Symmetrische property-coverage over alle 38 individuals | Vereist data-collectie: hasObligationID + hasObligationTitle + isMandatory voor 35 nieuwe individuals |
| Consistentere cross-cluster queries | Significant scope-werk; mogelijk Spoor B-afhankelijk voor sommige metadata |
| Dashboard kan generieke template gebruiken | Risico op verzonnen-data zonder bron-validatie |

**Optie B — OBL_NIS2 inkorten naar minimaal-patroon.**

| Voor | Tegen |
|---|---|
| Geen nieuwe data-collectie nodig | **Informatie-verlies** — bestaande detail-properties weggegooid (ondesirable) |
| Snelle implementatie | Strijdig met "rijker is beter" als architectuur-default |
| Lichter model | Cross-framework reasoning over OBL-detail wordt onmogelijk |

**Voorkeur (informeel):** geen van beide vandaag. Optie A is correct maar te duur zonder duidelijke trigger; Optie B is onaantrekkelijk vanwege informatie-verlies.

## Trigger voor beslissing

| Trigger | Implicatie |
|---|---|
| **Na v4.5.0** (Fase 3 M21 NIST CSF 2.0) | Mogelijk landen meer LegalObligations met CSF-context — uitgelezen moment om patroon-keuze te herzien |
| **Spoor B-activatie** | Bij organisatorische invulling worden specifieke LegalObligations gepopuleerd met operationele context — data-collectie wordt vanzelf relevant |
| **Dashboard-templates** | Indien dashboard-export rijke OBL-templates vereist, wordt Optie A onvermijdelijk |

## Verschil met H26

H26 ging over **ontbrekende OBL-laag voor NIS2 art. 18, 19, 22, 24** (Laag 2-gap binnen één cluster).

H32 gaat over **asymmetrie in property-set tussen bestaande OBL-individuals**: niet ontbrekende laag, wel inconsistent detail-niveau.

Beide blijven open totdat een GRC-inhoudelijke analyse triggert wat de gewenste eindstaat is.

## Hangt samen met

- [[brain__decisions__D12_drie-laags-compliance]] — drie-laags-architectuur die de OBL-laag definieert
- [[brain__architecture__H26_OBL-laag-gap-NIS2]] — gerelateerde OBL-laag-vraag (gap vs asymmetrie)
- [[brain__sprints__v4_4_0_fase-2-cbw-cbb]] — sprint waar H32 is ontdekt en geregistreerd

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-13 | open | Geregistreerd post-v4.4.0 op basis van inventarisatie tijdens Stap 1 Protocol B |

— Einde H32.
