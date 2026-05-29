---
type: workflow
title: Sprint-protocollen — gestructureerde discipline per sprint
status: living
date: 2026-05-21
related:
  - scope-discipline
  - opleveringsprotocol
  - v4_4_0_fase-2-cbw-cbb
  - v4_5_0_fase-3-nist-csf-2-0
  - v4_6_0_fase-4-ensia-en-volwassenheid
sources:
  - projectinstructie-v1.9
chat-sources: []
confidence: high
---

# Sprint-protocollen

Cumulatief overzicht van geformaliseerde sprint-protocollen. Geboren uit concrete leerpunten over meerdere sprints; geformaliseerd in projectinstructie v1.7 (basis), v1.8 (uitbreiding), v1.9 (vier nieuwe + één gedragsregel).

> **Canonieke set — `docs/sprint-protocols.md` (autoritatief):** de canonieke protocollen-set is sinds v1.9 verder gegroeid en telt nu **18 protocollen + 1 gedragsregel**. Protocollen 14-17 zijn toegevoegd in iteraties 12-13 (Protocol 14 pre-push-disclosure; 15 werkbare-applier; 16 lokatie-verificatie-scripts; 17 NEN-werkverdeling), en **Protocol 18 — Pre-sprint-dashboard-update-discipline** in iteratie 16 (29 mei 2026; dashboard-tegenhanger van Protocol 1: checklist vóór build-script-aanraking bij nieuwe baseline). De detail-uitwerking hieronder (12 protocollen) is een momentopname uit v1.9 en is **niet** bijgewerkt voor 13-18 — raadpleeg `docs/sprint-protocols.md` voor de actuele set en `docs/instructies/protocol-18-concept.md` voor de Protocol-18-bron.

## Overzicht — 12 protocollen + 1 gedragsregel *(v1.9-momentopname; canoniek = 18, zie docs/sprint-protocols.md)*

| Protocol | Bron-leerpunt | Geformaliseerd in | Toepassings-bewijs |
|---|---|---|---|
| **Protocol B** — Pre-sprint-inventarisatie | v4.4.0 v1.6 | v1.7 | v4.4.0, v4.5.0, v4.6.0 |
| Bron-verificatie vóór TBox-declaratie | v4.4.0 ENISA-Route-correctie | v1.7 | ext:hasENISAGuidance, ext:belongsToFramework |
| Bron-verificatie vóór raming-opstelling | v4.5.0 §12.4 | v1.8 | v4.5.0 cumulatief |
| Bron-bereikbaarheid in uitvoerings-omgeving | v4.5.0 Stap 1-pauze | v1.8 | v4.5.0 csrc.nist.gov-403 |
| Precedent-discipline bij nieuw framework-cluster | v4.5.0 ext:isComponentOf-vondst | v1.8 | v4.5.0 m21-template uit m17 |
| Raming-discipline bij aggregatie-mappings | v4.4.0 sheet 9 (37% dedup), v4.5.0 cross-bron-overlap | v1.8 | v4.4.0, v4.5.0 |
| Patch-rapport §9 verplicht — geparkeerde-items-status | v4.4.0 | v1.7 | v4.4.0, v4.5.0, v4.6.0 |
| Brain-vault-update verplicht na elke minor-release | iteratie 10 + v1.8 cyclus | v1.8 | iteratie 10b (v4.5.0), **iteratie 11 (v4.6.0)** |
| **Protocol B-multi-module-discipline** *(v1.9)* | v4.6.0 §8.1 | **v1.9** | **v4.6.0 Stap 5 scope-pauze** |
| **Ramings-baseline rdf:type-dubbele-telling** *(v1.9)* | v4.6.0 §8.4 | **v1.9** | **v4.6.0 Stap 4 +44% verklaarbaar** |
| **Instructie-consistentie code-block vs toelichting** *(v1.9)* | v4.6.0 §8.2 | **v1.9** | **v4.6.0 Stap 5 C2-correctie** |
| **Bron-typo-beleid patroon-criterium** *(v1.9)* | v4.6.0 §8.6 | **v1.9** | **v4.6.0 Stap 4: 4 typo's gecorrigeerd in label, comment behouden** |
| Property-semantiek-discipline *(gedragsregel v1.9)* | v4.6.0 §8.3 | **v1.9** | **v4.6.0 fw:Logius NIET als issuer** |

## Detail per protocol

### Protocol B — Pre-sprint-inventarisatie (verplicht)

Elke sprint die nieuwe klassen, properties of structurele wijzigingen introduceert opent met een gerichte read-only-inventarisatie door tech-chat.

**Doel:** voorkomen dat architectuurbesluiten op aannames over bestaande model-onderdelen worden gebouwd.

**Praktisch:**
- Inventarisatie-vragen vooraf opgenomen in sprint-instructie (sectie "Stap 1")
- Read-only — geen wijzigingen
- Resultaat als rapport naar masterchat
- Addenda mogelijk bij scope-implicaties

**v1.9-uitbreiding (multi-module-discipline):**

Pre-sprint-vragen naar "X bestaat in module Y" altijd uitbreiden naar "bestaat X model-breed?" wanneer architectuur-keuze hieraan vasthangt.

**Bewijs v4.6.0:** vraag D was te smal (alleen m01-context). Werkelijke m15 bevatte uitgebreide fw:ENSIA-declaratie incl. fw:toetst fw:BIO_2_0. Scope-pauze Stap 5 had voorkomen kunnen worden met multi-module-zoek. Vraag B (zoekopdracht) deed wél multi-module-zoek; vraag D had dat patroon moeten volgen.

### Bron-verificatie vóór TBox-declaratie

Bij property-namen of klasse-namen die naar een externe bron verwijzen: **bron-inhoud verifiëren** vóór TBox-declaratie. Niet alleen "domain/range klopt" maar ook "naam beschrijft wat het werkelijk is".

Voor instructies van masterchat aan tech-chat moet de naamcheck **een grep door bestaande modules** omvatten — voorkomt parallelle properties voor identiek doel.

**Toepassings-bewijs:** ext:hasENISAGuidance v4.4.0 (semantisch wezenlijk anders dan ext:hasUVInterpretation); ext:belongsToFramework v4.5.0 → ext:isComponentOf.

### Bron-verificatie vóór raming-opstelling

Bij triple-impact-ramingen: **bottom-up afleiden uit pre-sprint-cijfers**, niet top-down inschatten. Tel unieke (subject, predicate, object)-paren als doelmetric, niet bron-rijen of grof-geschatte gemiddelden.

**Toepassings-bewijs:** v4.5.0 cumulatief binnen prognose dankzij cross-bron-overlap-compensatie.

### Ramings-baseline rdf:type-dubbele-telling (v1.9)

**Rdflib telt rdf:type-triples dubbel:** class-membership + NamedIndividual-membership. Voor toekomstige ramingen op typed-individual-ABox-creatie:

> **5 triples per individual als base** (2 type-triples + 2 label-triples + 1 sourceAttribution-triple). Meer properties tellen daarbij op (bv. forCapability + atMaturityLevel + comment = 3 extra = 8 totaal per LevelDescription).

**Toepassings-bewijs v4.6.0:** Stap 4 +44% boven raming, volledig verklaard via deze dubbele-telling. Pre-stap-raming nam 4+6 per element; werkelijk 5+8. Geen bron-afwijking.

### Bron-bereikbaarheid in uitvoerings-omgeving

Vóór instructie-opstelling met externe bronnen: **verifieer bereikbaarheid** in tech-chat-omgeving, niet alleen existentie van de bron. Tech-chat's bash heeft beperkte allowed_domains.

**Toepassings-bewijs:** v4.5.0 Stap 1-pauze door csrc.nist.gov-403; opgelost via masterchat-uploads.

### Precedent-discipline bij nieuw framework-cluster

Bij introductie van nieuw framework-cluster: **vooraf-checken welk patroon eerdere framework-clusters hanteren**. Vier-vragen-checklist:

1. Welke property voor component → framework relatie?
2. Welke property voor parent-child binnen framework?
3. Welke SourceAttribution-aanpak?
4. Welke SKOS-mapping-conventies?

**Toepassings-bewijs:** v4.5.0 `ext:isComponentOf` precedent uit m17.

### Raming-discipline bij aggregatie-mappings

Bij aggregatie-mappings waarbij subject-grain grover is dan source-grain: **dedup-effect verwachten**. Tel unieke RDF-triples, niet bron-rijen.

**Toepassings-bewijs:** v4.4.0 sheet 9 (37% dedup-reductie). v4.5.0 Stap 6 cross-bron-overlap 105 mappings.

### Instructie-consistentie code-block vs toelichting (v1.9)

Bij opstellen sprint-instructie: code-block en toelichting **consistent maken**. Bij conflict prevaleert de toelichting (gevolgde semantiek), niet de sample-code.

**Toepassings-bewijs v4.6.0:** §6.3 toonde 2 fw:toetst-triples in code-block terwijl toelichting "ISO is referentieel" zei. Masterchat-correctie tijdens Stap 5: toelichting leidend (C2 gekozen).

### Bron-typo-beleid patroon-criterium (v1.9)

| Soort | Beleid |
|---|---|
| **Typo's in referentie-targets** | **NIET corrigeren** (G1, v4.5.0-precedent sheet 8 ISO-typo's). Mapping niet leggen. |
| **Typo's in nieuwe-individu rdfs:label** | **WEL corrigeren** (alleen presentatie, geen referentie-integriteit; v4.6.0-precedent sheet 6 typo's) |

**Patroon:** bron-getrouwheid op semantisch-kritische velden (target-IRIs, niveau-beschrijvingen-comments); correctie alleen op presentatie-velden (`rdfs:label@nl`) waar lezing in dashboard belangrijk is.

**Toepassings-bewijs v4.6.0:** 4 typo's gecorrigeerd in Capability-rdfs:label (Cbw_05/11/12/14). Niveau-beschrijvingen (rdfs:comment) bron-getrouw uit CBW-Excel behouden.

### Patch-rapport §9 verplicht — geparkeerde-items-status-update

Patch-rapport bevat §9 met **status-update van alle geparkeerde H-items + scope-besluiten**.

**Toepassings-bewijs:** v4.4.0, v4.5.0, v4.6.0 — allen met §9-tabel.

### Brain-vault-update verplicht na elke minor-release

Na elke minor-release: **brain-vault bijwerken** via Brein-chat. Werkwijze: Brein-chat krijgt patch-rapport + nieuwe projectinstructie als input en bepaalt autonoom welke `brain__*`-bestanden aangemaakt of bijgewerkt worden.

**Standaard activeringsmoment:** na opstellen nieuwe projectinstructie.

**Toepassings-bewijs:**
- v4.5.0 → v1.8 cyclus (uitzondering, parallel)
- **v4.6.0 → v1.9 cyclus = eerste reguliere cyclus** (iteratie 11)

## Gedragsregel — Property-semantiek-discipline (v1.9)

> **Rol-onderscheid bij framework-individual-properties: issuer ≠ beheerder; uitgever ≠ uitvoerder. Niet samenvoegen onder één property als rollen ontologisch verschillen.**

Geen sprint-protocol maar gedragsregel — toegevoegd aan alle chats vanuit v1.9.

**Toepassings-bewijs v4.6.0:** `fw:Logius` NIET als `fw:issuedBy` ENSIA. Logius beheert ENSIA (publiceert site, hosts vragenlijst); BZK/NOREA/VNG zijn formele issuers. Behoud 3 issuers; `fw:isManagedBy` toegevoegd aan overwegingen-pool (kandidaat-property bij toekomstige beheerder-rol-modellering).

## Sprint-protocollen — overstijgend principe

Alle protocollen delen één onderliggend principe: **discipline boven snelheid**. Pre-sprint-inventarisatie, bron-verificatie en raming-discipline kosten tijd vooraf, maar voorkomen scope-pauzes en verkeerde besluiten gedurende uitvoering.

**Tijd-investering vooraf wint van correctie-werk achteraf.**

## Cross-references

- [[brain__workflow__scope-discipline]] — generieke werkwijze bij scope-afwijking
- [[brain__workflow__opleveringsprotocol]] — sprint-afsluiting + brain-update
- [[brain__workflow__workflow-register]] — workflow-overzicht
- [[brain__sprints__v4_4_0_fase-2-cbw-cbb]] — Protocol B + bron-verificatie ontstaan
- [[brain__sprints__v4_5_0_fase-3-nist-csf-2-0]] — raming-discipline + precedent-discipline + bron-bereikbaarheid
- [[brain__sprints__v4_6_0_fase-4-ensia-en-volwassenheid]] — multi-module-discipline + ramings-baseline + instructie-consistentie + bron-typo + property-semantiek

— Einde sprint-protocollen.
