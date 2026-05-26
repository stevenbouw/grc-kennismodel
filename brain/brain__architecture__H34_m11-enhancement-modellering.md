---
type: architecture
id: H34
title: H34 — m11 enhancement-modellering
status: open
date: 2026-05-19
related:
  - H33_m11-sp800-53-substantiele-uitbreiding
  - v4_5_0_fase-3-nist-csf-2-0
  - M11_nist-800-53
sources:
  - patch-rapport-v4_5_0
chat-sources: []
confidence: high
---

# H34 — m11 enhancement-modellering

## Status

**Open** — geregistreerd post-v4.5.0 (19 mei 2026). Trigger: serieus SP 800-53-gebruik waar enhancements auditief relevant zijn.

## Wat het is

SP 800-53 Rev 5 controls hebben **enhancements** — sub-eisen die controls verfijnen. Voorbeelden:

| Notatie | Wat het betekent |
|---|---|
| `AC-2` | Hoofd-control: Account Management |
| `AC-2(1)` | Enhancement 1: Account Management — Automated System Account Management |
| `CM-07` | Hoofd-control: Least Functionality |
| `CM-07(02)` | Enhancement 2: Least Functionality — Authorized Software |

In Stap 6 van v4.5.0 dook **17 unique enhancements** op vanuit CSF Reference Tool-mappings die NIET in M11 aanwezig zijn. Het model bevat alleen hoofd-controls (`AC-2`), geen enhancements (`AC-2(1)`).

## Waarom dit een open vraag is

Enhancements zijn audit-relevant: een organisatie kan voldoen aan `AC-2` zonder te voldoen aan `AC-2(1)`. Voor compliance-statements is het verschil belangrijk.

| Optie | Voor | Tegen |
|---|---|---|
| **A — Enhancements als sub-individuals** | Compliance-precisie op enhancement-niveau | Significant veel triples (1000+ enhancements over alle controls); naamgevingsconventie te bepalen |
| **B — Enhancements als attribuut van hoofd-control** | Compacter | Verlies van afzonderlijke audit-targeting |
| **C — Status quo behouden** | Geen werk | Compliance-claims op hoofd-control-niveau missen detail-precisie |

## Trigger-criterium

Serieus SP 800-53-gebruik waar enhancements auditief relevant zijn — bijvoorbeeld bij organisatie-eis "FedRAMP Moderate" waar specifieke enhancement-controls verplicht zijn.

## Verschil met H33

H33 = **breedte** (meer hoofd-controls van de ~1000 totaal). H34 = **diepte** (enhancement-niveau detail per control).

Bij gezamenlijke activatie kunnen beide in één M11-uitbreidings-sprint worden aangepakt.

## Naamgevings-conventie (kandidaat)

Niet vastgelegd. Mogelijk patroon:

- `ctrl:NIST_AC_02_E01` (enhancement 1 — onderscheid via `_E` infix)
- `ctrl:NIST_CM_07_E02`

Behoeft afstemming met bestaande M11-naamgeving voorafgaand aan implementatie.

## Hangt samen met

- [[brain__architecture__H33_m11-sp800-53-substantiele-uitbreiding]] — gerelateerde M11-modelbeperking (breedte)
- [[brain__modules__M11_nist-800-53]] — module
- [[brain__sprints__v4_5_0_fase-3-nist-csf-2-0]] — sprint waar 17 unique enhancements zijn waargenomen

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-19 | open | Geregistreerd post-v4.5.0 op basis van 17 unique enhancements in Stap 6 |

— Einde H34.
