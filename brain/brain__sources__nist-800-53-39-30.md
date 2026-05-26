---
type: source
title: NIST SP 800-53/39/30 + cross-mapping
status: living
date: 2026-05-13
related:
  - M11_nist-800-53
  - M03_risk
sources: []
chat-sources: []
confidence: high
---

# NIST Special Publications 800-53 / 39 / 30

## Drie bron-documenten

| Bestand | Volledige naam | Doel | Module |
|---|---|---|---|
| `NIST_SP_800-53r5.pdf` | NIST SP 800-53 Revision 5 — Security and Privacy Controls | Controls-bibliotheek | M11 |
| `nistspecialpublication80039.pdf` | NIST SP 800-39 — Managing Information Security Risk: Organization, Mission, and Information System View | Risk management process | M03 |
| `sp800-53r5-to-iso-27001-mapping.docx` | Officiële NIST-mapping NIST 800-53 ↔ ISO 27001 | Cross-framework SKOS-basis | M11 SKOS |

NIST SP 800-30 (Risk Assessment) is gebruikt voor M03-grondlaag maar niet als afzonderlijk bestand geüpload — de risk-vocabulary (Threat, ThreatSource, Vulnerability) is gangbaar bekend.

## Licentie

Alle NIST-publicaties zijn **publiek domein** (US federal government works). Geen attributie-eis. Goede praktijk wel: vermeld bron in module-headers.

## Toepassing per document

### NIST SP 800-53 R5

124 control-individuals in M11 (subset relevant voor IB-raakvlak). 20 control families: AC, AT, AU, CA, CM, CP, IA, IR, MA, MP, PE, PL, PM, PS, PT, RA, SA, SC, SI, SR.

### NIST SP 800-39

Risk management proces in drie tiers (Organization / Mission / Information System). Grondlaag voor M03-risico-vocabulary. Tier-onderscheid manifesteert zich in `risk:`-namespace als verschillende klassen.

### NIST 800-53 ↔ ISO 27001 mapping

Officieel mappings-document gebruikt als SKOS-mapping-basis. Bidirectioneel: voor elke ISO 27001-control welke 800-53-controls relevant zijn, en omgekeerd.

## Cross-framework-rol

NIST is **referentiekader**, geen wettelijke verplichting voor de organisatie. Gebruikt voor:

- Internationale audit-context (ADR, externe auditors)
- Verrijking van ISO 27002-controls met implementatie-detail
- Voorbereiding op toekomstige NIST CSF 2.0-integratie (M21)

— Einde NIST 800-53/39/30-bron.
