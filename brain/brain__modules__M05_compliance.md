---
type: module
id: M05
title: M05 — Compliance (compl:)
status: active
date: 2026-05-13
related:
  - D12_drie-laags-compliance
  - drie-laags-compliance
  - H25_compl-articleRef-domain-spanning
  - H26_OBL-laag-gap-NIS2
  - H32_obl-laag-asymmetrie
  - v4_3_3_d12-en-predicate-consolidatie
  - v4_4_0_fase-2-cbw-cbb
sources:
  - projectinstructie-v1.7
chat-sources: []
confidence: high
---

# M05 — Compliance

## Bestand
`m05-compliance.ttl`

## Namespace
`compl: <https://grc.example.org/compliance/>`

## Wat het bevat

De **drie-laags-compliance-architectuur** uit [[brain__decisions__D12_drie-laags-compliance]]: regulatory / legal / requirement-laag. Compliance-eisen + VIR/VIRBI/BVA-verplichtingen + **Cbb-zorgplichtartikelen** *(v4.4.0)*.

| Inhoud | Aantal v4.4.0 |
|---|---:|
| `compl:RegulatoryObligation`-individuals (Laag 1) | bv. 10 NIS2_Art21_a..j |
| `compl:LegalObligation`-individuals (Laag 2) | 38 (3 OBL_NIS2 + 35 overige incl. 14 nieuwe Cbb-Art) |
| **`compl:SupplierExclusionOrder`-klasse** *(v4.4.0, nieuw)* | Subklasse van `compl:LegalObligation` voor Cbb art. 18 |
| **14 Cbb-Art-individuals** *(v4.4.0, nieuw)* | art. 6 t/m 19 (incl. art. 18 als `compl:SupplierExclusionOrder`) |
| `compl:ComplianceRequirement`-tak | NIS2_REQ_*, DORA_REQ_*, ISMS_REQ, BCM_REQ |
| `ext:NIS2Requirement`-subjects | 15 (REQ_NIS2_Art20_1/2, _Art21_a..j, _Art23_1/2/3) |
| `ext:DORARequirement`-subjects | 14 (DORA_Art5..14, 16..19) |

## v4.4.0-uitbreiding — CBW/Cbb compliance-cluster

### Nieuwe klasse

```turtle
compl:SupplierExclusionOrder rdfs:subClassOf compl:LegalObligation .
```

Specifieke subklasse voor Cbb art. 18 (uitsluiting van leveranciers). Reden voor aparte klasse: art. 18 heeft een procedure-aard die kwalitatief verschilt van de andere 13 zorgplichtartikelen — het is een **vrijwillige maatregel-mogelijkheid voor de overheid**, niet een **verplichting voor entiteiten**.

### 14 Cbb-zorgplichtartikelen

| Cbb-Art | Klasse | Onderwerp (kort) |
|---|---|---|
| 6 | `compl:LegalObligation` | Risico-aanpak |
| 7 | `compl:LegalObligation` | Beleid IB |
| 8 | `compl:LegalObligation` | Incident-management |
| 9 | `compl:LegalObligation` | Bedrijfscontinuïteit |
| 10 | `compl:LegalObligation` | Supply-chain-beveiliging |
| 11 | `compl:LegalObligation` | Network/system-acquisitie + ontwikkeling |
| 12 | `compl:LegalObligation` | Beoordelings-effectiviteit |
| 13 | `compl:LegalObligation` | Cyber-hygiëne + training |
| 14 | `compl:LegalObligation` | Crypto |
| 15 | `compl:LegalObligation` | HR-beveiliging + toegang + asset-management |
| 16 | `compl:LegalObligation` | Authenticatie + beveiligde communicatie |
| 17 | `compl:LegalObligation` | Vulnerability disclosure |
| **18** | **`compl:SupplierExclusionOrder`** | **Leveranciers-uitsluiting** |
| 19 | `compl:LegalObligation` | Naleving + toezicht |

Art. 5 is een verwijzings-artikel naar art. 6–19 en wordt niet als zelfstandige zorgplicht-individual gemodelleerd. Totaal: **14** Cbb-Art-individuals — niet 13 zoals v1.6 parafraseerde.

### Status-markering

Alle Cbb-Art-individuals krijgen status-markering "concept t.b.v. Tweede Kamer, nog niet vastgesteld" via `rdfs:comment` of `ext:status`-property. Inwerkingtreding bij koninklijk besluit; monitoring is Spoor C (governance-beheer).

## Properties

- `compl:articleRef` — artikel-referentie als string ("art. N"), domain `compl:Obligation` (spanning issue, zie H25)
- `compl:requirementText` — eis-tekst (NL/EN)
- `compl:derivedFrom` — relatie REQ → OBL → RO

## D-relaties

- [[brain__decisions__D12_drie-laags-compliance]] — architectuur-fundament; CBW/Cbb als legal-only-keten (verfijning v4.4.0)
- [[brain__concepts__drie-laags-compliance]] — uitgebreide uitleg

## Open architectuur-vragen

- [[brain__architecture__H25_compl-articleRef-domain-spanning]] — domain-spanning probleem (status: onveranderd — 14 Cbb-Art zijn domain-conform)
- [[brain__architecture__H26_OBL-laag-gap-NIS2]] — Laag 2-gap voor 4 NIS2-artikelen
- [[brain__architecture__H27_gamma-migratie-articleIdentifier]] — voorwaardelijke γ-migratie (status: geen trigger geactiveerd)
- [[brain__architecture__H32_obl-laag-asymmetrie]] — modelleringsasymmetrie tussen OBL_NIS2 (uitgebreid) en overige LegalObligations (minimaal patroon — incl. 14 Cbb-Art)

## Module-grootte

Pre-v4.4.0: 758 triples. Post-v4.4.0: significant gegroeid door 14 nieuwe Cbb-Art-individuals + `compl:SupplierExclusionOrder`-TBox-declaratie.

— Einde M05.
