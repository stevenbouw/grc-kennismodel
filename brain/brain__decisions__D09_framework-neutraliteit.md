---
type: decision
id: D9
title: D9 — Framework-neutraal model
status: active
date: 2026-05-21
related:
  - D03_10-namespaces
  - D10_coso-enterprise-governance
  - v4_4_0_fase-2-cbw-cbb
  - v4_5_0_fase-3-nist-csf-2-0
  - v4_6_0_fase-4-ensia-en-volwassenheid
  - framework-neutraliteit
sources:
  - projectinstructie-v1.9
chat-sources: []
confidence: high
---

# D9 — Framework-neutraal model

## Beslissing

**Alle normen, wetten en kaders zijn architectureel gelijkwaardig.** Geen enkel framework krijgt een centraal organiserend privilege. Alle worden gemodelleerd als individuals in `fw:`, met onderlinge relaties via SKOS-mappings en specifieke properties (`fw:isTranspositieVan`, `fw:uitgewerktIn`, `fw:toetst`, `ext:isComponentOf`, etc.).

## Datum

- **17 maart 2026** — formeel besluit
- **v4.4.0** (13 mei 2026) — twee verificatie-clusters geverifieerd
- **v4.5.0** (19 mei 2026) — derde cluster (NIST CSF 2.0 Optie B)
- **v4.6.0** (21 mei 2026) — vierde cluster (ENSIA audit-kader zonder privilege)

## Vier cumulatieve verificatie-clusters

### Cluster 1 — NIS2-EU + CBW-NL (v4.4.0)

Horizontale transpositie-relatie tussen EU-richtlijn en NL-wet:

```
fw:CBW fw:isTranspositieVan fw:NIS2_Directive
fw:NIS2_Directive fw:transposedBy fw:CBW
```

Geen hiërarchie — beide gelijkwaardige fw:GRCFramework-individuals.

### Cluster 2 — CBW-NL + Cbb-AMvB (v4.4.0)

Wet → AMvB-relatie:

```
fw:CBW fw:uitgewerktIn fw:Cbb
fw:Cbb fw:werktUit fw:CBW
```

Gelijkwaardig — Cbb is geen "ondergeschikte" van CBW maar een aparte rechts-instantie.

### Cluster 3 — NIST CSF 2.0 (v4.5.0)

**Optie B-keuze**: gemapt referentiekader, niet organiserend kader.

| Optie | Beschrijving | D9-status |
|---|---|---|
| **A** — CSF als organiserend kader | Bestaande controls onder CSF Functions positioneren | ❌ Schendt D9 |
| **B** — CSF als gemapt referentiekader | CSF-componenten náást bestaande kaders; SKOS-mappings | ✓ Gekozen |

Concrete implementatie:
- 11e namespace `csf:` náást ISO/NIST 800-53/BIO
- Geen CSF-eigen control-klassen — Subcategories blijven outcomes
- 1.448 SKOS-mappings naar bestaande kaders
- `ext:isComponentOf fw:NIST_CSF_2_0` (m17-precedent)

### Cluster 4 — ENSIA (v4.6.0) ✨

**Audit-kader zonder audit-kader-privilege.** ENSIA werd gepromoot van `fw:Guideline` naar `fw:GRCFramework`-individual.

Concrete keuzes conform D9:
- Geen aparte "audit:"-namespace — `fw:` is voldoende voor alle frameworks
- Geen "audit kader"-class — `fw:GRCFramework` volstaat
- Hybride locatie (A3+B3+C2): kerndeclaratie in m01, domeinspecifieke uitbreidingen (8 audit-domains, NB-comment) in m15
- `fw:ENSIA fw:toetst fw:BIO_2_0` als gelijkwaardige relatie (niet als hiërarchisch privilege)
- ISO-relatie via `skos:relatedMatch` (informatief), niet via 2e `fw:toetst` (zou gesuggereerd hebben dat ENSIA ISO toetst — niet de werkelijkheid)

D9-bewijs in v4.6.0: vier verschillende soorten frameworks (EU-richtlijn, NL-wet, US-cybersecurity-framework, NL-audit-kader) leven gelijkwaardig in dezelfde `fw:`-namespace zonder dat enig framework architectureel privileged is.

## Onderscheid model versus dashboard

| Laag | Discipline |
|---|---|
| **Model** | Framework-neutraal — D9 |
| **Dashboard / rapportage** | BIO 2.0 als primair perspectief — view-keuze (niet architectuur-keuze) |

> "Het model is het woordenboek (neutraal), het dashboard is het verhaal (perspectief)."

## Architectuur-test bij toekomstige toevoegingen

Bij elke overweging van een nieuw framework — M19 ISO 42001, M20 ISO 9001, sector-specifieke frameworks — geldt de **architectuur-test**:

> *"Landt dit framework als gelijkwaardige individual naast de bestaande, of probeert het zich als 'centrum' te positioneren?"*

Als kandidaat-framework zich als organiserend kader presenteert: D9-conflict, scope-pauze, masterchat-beoordeling.

## Toepassingen tot heden

| Framework | Implementatie | D9-status |
|---|---|---|
| BIO 2.0 | Operationeel kader Laag 3 | ✓ — gelijkwaardig, niet centraal |
| NIS2 | Toetskader Laag 2 | ✓ — gelijkwaardig |
| CBW + Cbb | NL-wetgeving Laag 2 | ✓ — clusters horizontaal gerelateerd |
| NIST CSF 2.0 (v4.5.0) | Gemapt referentiekader (Optie B) | ✓ — concrete D9-toepassing |
| **ENSIA (v4.6.0)** | **Audit-kader zonder audit-kader-privilege** | **✓ — vierde concrete D9-toepassing** |
| UCF (overwogen) | Buiten scope | ❌ D9-conflict was één van vier redenen |

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-03-17 | active | Formeel besluit |
| 2026-05-13 (v4.4.0) | active | Cluster 1+2 verificatie (NIS2-EU + CBW-NL) |
| 2026-05-19 (v4.5.0) | active | Cluster 3 verificatie (NIST CSF 2.0 Optie B) |
| 2026-05-21 (v4.6.0) | active | Cluster 4 verificatie (ENSIA audit-kader zonder privilege) |

## Hangt samen met

- [[brain__decisions__D03_10-namespaces]] — namespace-uitbreidingen conform D9
- [[brain__decisions__D10_coso-enterprise-governance]] — COSO als Laag 0 conform D9
- [[brain__concepts__framework-neutraliteit]] — uitleg & toepassings-bewijs
- [[brain__sprints__v4_4_0_fase-2-cbw-cbb]] — clusters 1+2
- [[brain__sprints__v4_5_0_fase-3-nist-csf-2-0]] — cluster 3
- [[brain__sprints__v4_6_0_fase-4-ensia-en-volwassenheid]] — cluster 4
- [[brain__scope__UCF-uitgesloten]] — D9-conflict-reden

— Einde D9.
