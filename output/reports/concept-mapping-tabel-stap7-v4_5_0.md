# CONCEPT-MAPPING-TABEL — STAP 7 v4.5.0 FASE 3

**Versie:** 1.0
**Datum:** 19 mei 2026
**Opsteller:** Technische chat
**Type:** Ter masterchat-review (vóór SKOS-creatie)
**Basis:** v4.4.0-baseline + Stappen 2-6 voltooid

---

## 0. Scope

Concept-mapping van **6 GV-Categories** (NIST CSF 2.0 GOVERN-Function) naar de in m17 bestaande COSO/COBIT-individuals:
- **5 COSO ICF-componenten** (ControlEnvironment, RiskAssessment, ControlActivities, InformationCommunication, MonitoringActivities)
- **5 COSO ERM-pijlers** (GovernanceCulture, StrategyObjectiveSetting, Performance, ReviewRevision, InformationCommunicationReporting)
- **9 COBIT 2019-objectives** (APO12, APO13, DSS05, EDM01–05, MEA02)

Match-type uniform: `skos:relatedMatch` (besluit 7 instructie).
Eén richting: `csf:GV_* → ext:*`.

---

## 1. Samenvattingstabel — alle 13 voorgestelde paren

| # | CSF Category | Voorgestelde target | Match-type | Tech-chat-rationale |
|---:|---|---|---|---|
| 1 | **GV.OC** Organizational Context | `ext:COSO_ICF_ControlEnvironment` | `skos:relatedMatch` | Beide adresseren de organisatorische basis (normen, structuur, autoriteit-toewijzing) waarop risicobeheer rust |
| 2 | **GV.OC** Organizational Context | `ext:COBIT_EDM01` | `skos:relatedMatch` | EDM01 "governance-kader instellen en onderhouden" dekt expliciet het analyseren van governance-vereisten als context-vaststelling |
| 3 | **GV.RM** Risk Management Strategy | `ext:COSO_ICF_RiskAssessment` | `skos:relatedMatch` | Identiek concept: "dynamische en iteratieve proces voor het identificeren en analyseren van risico's" sluit aan op risk tolerance/appetite-vaststelling |
| 4 | **GV.RM** Risk Management Strategy | `ext:COSO_ERM_StrategyObjectiveSetting` | `skos:relatedMatch` | Expliciete match: "Risicobereidheid wordt vastgesteld in lijn met strategie en bedrijfsdoelstellingen" |
| 5 | **GV.RM** Risk Management Strategy | `ext:COBIT_EDM03` | `skos:relatedMatch` | Sterkste COBIT-match: "Zorg dat de risicotolerantie gedefinieerd is en dat risico's in lijn zijn met risicobereidheid" |
| 6 | **GV.RR** Roles, Responsibilities, and Authorities | `ext:COSO_ICF_ControlEnvironment` | `skos:relatedMatch` | ControlEnvironment dekt expliciet "toewijzing van autoriteit en verantwoordelijkheden" als kerncomponent |
| 7 | **GV.RR** Roles, Responsibilities, and Authorities | `ext:COSO_ERM_GovernanceCulture` | `skos:relatedMatch` | "Governance stelt de organisatietoon vast … stelt toezichtverantwoordelijkheden vast voor ERM" matcht roles/responsibilities/accountability |
| 8 | **GV.PO** Policy | `ext:COSO_ICF_ControlActivities` | `skos:relatedMatch` | "Acties die worden vastgelegd door beleid en procedures" — beleid als kernmechanisme |
| 9 | **GV.PO** Policy | `ext:COBIT_APO13` | `skos:relatedMatch` | "Definieer, exploiteer en moniteer een ISMS conform best practices" — informatiebeveiligingsbeleid expliciet |
| 10 | **GV.OV** Oversight | `ext:COSO_ICF_MonitoringActivities` | `skos:relatedMatch` | Identiek concept: "Doorlopende evaluaties … om vast te stellen of alle vijf componenten van interne beheersing aanwezig en werkzaam zijn" |
| 11 | **GV.OV** Oversight | `ext:COSO_ERM_ReviewRevision` | `skos:relatedMatch` | "Door de prestaties van ERM te evalueren kan de organisatie beoordelen hoe goed de ERM-componenten functioneren" — zelfde monitoring-loop |
| 12 | **GV.OV** Oversight | `ext:COBIT_MEA02` | `skos:relatedMatch` | "Monitor and evaluate the internal control environment … Directly references COSO ICF" — expliciete kruisverwijzing |
| 13 | **GV.SC** Cybersecurity Supply Chain Risk Management | *(optie)* `ext:COBIT_APO12` | `skos:relatedMatch` | "Integreer IT-risicobeheer in de algehele organisatorische risicobeheerpraktijken" — supply chain risk is specialisatie van risk management, geen exact-overlap. **Tech-chat-aanbeveling: SKIP** |

---

## 2. CSWP 29 Category-statements (context voor review)

### GV.OC — Organizational Context (2 mappings voorgesteld)
> *"The circumstances — mission, stakeholder expectations, dependencies, and legal, regulatory, and contractual requirements — surrounding the organization's cybersecurity risk management decisions are understood"*

→ Voorgesteld: `COSO_ICF_ControlEnvironment` + `COBIT_EDM01`

### GV.RM — Risk Management Strategy (3 mappings voorgesteld)
> *"The organization's priorities, constraints, risk tolerance and appetite statements, and assumptions are established, communicated, and used to support operational risk decisions"*

→ Voorgesteld: `COSO_ICF_RiskAssessment` + `COSO_ERM_StrategyObjectiveSetting` + `COBIT_EDM03`

### GV.RR — Roles, Responsibilities, and Authorities (2 mappings voorgesteld)
> *"Cybersecurity roles, responsibilities, and authorities to foster accountability, performance assessment, and continuous improvement are established and communicated"*

→ Voorgesteld: `COSO_ICF_ControlEnvironment` + `COSO_ERM_GovernanceCulture`

### GV.PO — Policy (2 mappings voorgesteld)
> *"Organizational cybersecurity policy is established, communicated, and enforced"*

→ Voorgesteld: `COSO_ICF_ControlActivities` + `COBIT_APO13`

### GV.OV — Oversight (3 mappings voorgesteld)
> *"Results of organization-wide cybersecurity risk management activities and performance are used to inform, improve, and adjust the risk management strategy"*

→ Voorgesteld: `COSO_ICF_MonitoringActivities` + `COSO_ERM_ReviewRevision` + `COBIT_MEA02`

### GV.SC — Cybersecurity Supply Chain Risk Management (SKIP-aanbeveling)
> *"Cyber supply chain risk management processes are identified, established, managed, monitored, and improved by organizational stakeholders"*

→ **Tech-chat-aanbeveling: SKIP**. COSO/COBIT-modellering bevat geen native supply-chain-component zoals nu in m17 gemodelleerd. APO12 ("Integreer IT-risicobeheer in de algehele organisatorische risicobeheerpraktijken") is wel optie maar de mapping zou geforceerd zijn want supply chain risk is specialisatie binnen algemeen risk management.

---

## 3. Bewust niet voorgesteld (zou geforceerd zijn)

| Niet-gebruikte target | Reden voor niet-mapping |
|---|---|
| `ext:COBIT_DSS05` (Manage Security Services) | Specifiek PROTECT-domein (CSF PR.* familie), niet GOVERN |
| `ext:COBIT_EDM02` (Benefits Delivery) | IT-waardecreatie, niet cybersecurity-governance |
| `ext:COBIT_EDM04` (Resource Optimisation) | IT-resources algemeen; GV.RR is specifieker over cybersecurity-rollen |
| `ext:COBIT_EDM05` (Stakeholder Engagement) | IT-prestatie-communicatie naar stakeholders; te ver weg van GV.OC's context-vaststelling |
| `ext:COSO_ERM_InformationCommunicationReporting` | Generieke informatiestromen; niet specifiek voor cybersecurity-governance |
| `ext:COSO_ERM_Performance` | Risico-prioritering algemeen; geen GV-specifieke overlap |
| `ext:COSO_ICF_InformationCommunication` | Generieke interne-beheersing-info; te abstract voor GV.* |

---

## 4. Beslissing-overzicht per GV-Category

| GV-Category | Voorgesteld | Geadviseerd | Voor GO/SKIP/optie |
|---|---:|---:|---|
| GV.OC | 2 | 2 sterk | GO beide |
| GV.RM | 3 | 3 sterk | GO alle drie |
| GV.RR | 2 | 2 sterk | GO beide |
| GV.PO | 2 | 2 sterk | GO beide |
| GV.OV | 3 | 3 sterk | GO alle drie |
| GV.SC | 1 optie | 0 (SKIP) | Tech-chat-aanbeveling SKIP; masterchat-keuze |
| **Totaal** | **13** | **12 sterk** | — |

---

## 5. Triple-impact bij masterchat-GO

- **Bij GO op alle 12 sterke + SKIP GV.SC**: +12 `skos:relatedMatch`-triples
- **Bij GO op alle 13 (incl. zwakke GV.SC)**: +13 triples
- **Bij selectieve GO**: ergens tussen +0 en +13

Marginale triple-impact. Sprint-totaal-prognose nauwelijks beïnvloed.

---

## 6. Open keuze voor masterchat — locatie SKOS-triples

| Optie | Locatie | Argument |
|---|---|---|
| A | `m21-csf.ttl` | Subject is `csf:GV_*` → source-module-locatie. Consistent met Stap 3+5. |
| B | `m17-coso-cobit.ttl` | Target is `ext:COSO_*`/`ext:COBIT_*` → target-module-locatie. Consistent met Stap 6-aanpak + v4.4.0-precedent. |

**Tech-chat-voorkeur**: B (m17), consistent met Stap 6. Maar 12 triples is klein genoeg dat A ook werkt.

---

## 7. Acties — wat tech-chat van masterchat nodig heeft

1. **Per-mapping GO/SKIP**: alle 13 doorlopen, of per blok GO/SKIP (bv. "GO alle 12 sterke, SKIP GV.SC")
2. **Locatie-keuze**: A (m21) of B (m17)
3. Daarna tech-chat: TTL-creatie + parse + SHACL + tussenrapport Stap 7

---

**Einde concept-mapping-tabel Stap 7 v4.5.0.**
