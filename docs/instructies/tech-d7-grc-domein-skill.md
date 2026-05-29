# Instructie Tech-subagent — D.7 GRC-domein-skill (optie B)

**Van:** masterchat
**Datum:** 29 mei 2026
**Doel-subagent:** Technisch (Claude Code)
**Aanleiding:** extensie-landschap-rapport D.7-aanbeveling (unieke NL-kaders-lacune) + masterchat-prioritering 29-05. Parallel-track naast de dashboard-revival; geen bestandsoverlap.

---

## 0. Doel

Bouw een action-/reference-skill die de Nederlandse GRC-kaders kent en hun onderlinge relaties, zodat toekomstig ontologie- en analysewerk consistent naar de juiste kaders, lagen en clausules verwijst. Dit is de lacune die generieke GRC-skills niet vullen: de NL-specifieke kaders en hun hiërarchie.

Locatie: `.claude/skills/grc-domein/SKILL.md` (+ eventuele reference-bijlagen in dezelfde folder).

## 1. Harde invarianten

- **Geen organisatienaam.**
- **Framework-neutraal (D9)** — de skill beschrijft kaders als gelijkwaardig; geen kader als hub. BIO 2.0 alleen als operationeel toepassingsperspectief benoemen, niet als architecturale kern.
- **NEN-discipline** — voor ISO-normen (27001/27002/27005/31000/22301/22313) alleen parafrase + clausule-verwijzing; **geen verbatim NEN-tekst >10 woorden.** Lokale NEN-bron-toegang in `grc-sources-licensed/` mag gelezen worden voor parafrase; output respecteert de >10-woorden-grens.
- **§0.5-firewall in de skill-tekst zelf opnemen** (leerpunt §11.15): geen autonomie-bouw onder welke framing dan ook; mens-in-controle. Toekomstige aanroepingen exposen de firewall opnieuw.
- **Status-discipline wetgeving** — CBW = "in voorbereiding"; Cbb = "concept t.b.v. Tweede Kamer, nog niet vastgesteld".
- **Geen BBN als BIO 2.0-eigenschap** — BBN komt uit de Handreiking BIO2-opmaat, via `ext:hasHandreikingBBN`, waarden 1 of 2.

## 2. Scope — de kaders en hun lagen

Dek de vijf-lagen-hiërarchie en de relaties:

- **Laag 0** COSO ICF + COSO ERM
- **Laag 1** COBIT 2019, BVA-stelsel, CIO-stelsel 2026
- **Laag 2** NIS2, VIR 2007, VIRBI 2025, AVG (IB-raakvlakken), CBW (in voorbereiding), Cbb (concept), DORA (referentie, organisatie valt er niet onder)
- **Laag 3** BIO 2.0 (operationeel kader, view-perspectief)
- **Laag 4** ISO 27001/27002/27005/31000/22301/22313, NIST 800-53/39/30, NIST CSF 2.0, Annex SL
- **Laag 5** ENSIA (auditkader), volwassenheidsmodel

Plus de relatie-semantiek (fw:stelVerplicht, fw:geeftRichtlijnenVoor, fw:geeftITInvullingAan, fw:dektAf, fw:toetst, fw:transposedBy/isTranspositieVan, fw:uitgewerktIn/werktUit, ext:isComponentOf) en de SKOS-mapping-semantiek incl. het cross-category-principe (control ↔ legal-obligation = relatedMatch-basislijn, kandidaat v1.3.1).

## 3. Werkwijze + scope-pauze

- Verifieer kader-feiten aan de brain-vault (`brain/`) en de ontologie-modules vóór ze in de skill landen (Protocol 4-geest).
- **Scope-pauze-conditie:** als de skill-omvang of -reikwijdte substantieel groter blijkt dan een enkel SKILL.md + beperkte bijlagen (bijv. de relatie-matrix vraagt om gegenereerde data uit de ontologie), STOP en lever een Optie A/B/C-rapport aan de masterchat. Niet zelfstandig uitbreiden.
- Geen architectuurbeslissingen; die gaan via masterchat.

## 4. Wat NIET

- Geen verbatim NEN-tekst.
- Geen kader als architecturale hub (D9).
- Geen ontologie-mutaties als onderdeel van deze skill-bouw (de skill beschrijft, muteert niet).
- Geen autonome commit.

## 5. Deliverables

- `.claude/skills/grc-domein/SKILL.md` (+ eventuele reference-bijlagen).
- Trigger-test tegen een paar realistische vragen (bijv. "welke laag is VIRBI?", "wat is de relatie NIS2 ↔ CBW?").
- Korte oplevernotitie met disclosure-check (vijf categorieën, incl. NEN-tekst-detectie).
