# Brein-cyclus iteratie 14 — instructie

**Voor:** Brein-subagent in Claude Code
**Auteur:** Masterchat
**Datum:** 27 mei 2026
**Trigger:** T2-sprint afgesloten + projectinstructie v1.10 vastgesteld + Protocol v1.3-draft in repo
**Voorganger-iteratie:** 13 (post-migratie + T1-sprint)
**Doel-iteratie:** **14**
**Baseline-context:** v4.6.2 (productie sinds 27 mei 2026)
**Modus:** Brain-vault-update + cross-referentie-bewaking + register-onderhoud. Brein-autonomie binnen onderstaande scope-contouren conform projectinstructie v1.10 §"ZEVEN CHATS".

---

## §0. Context

Twee sprints + twee documenten zijn sinds iteratie 13 afgerond:

1. **T2-sprint** (27 mei 2026) — v4.6.1 → v4.6.2, 65 SKOS-mutaties in m10, cluster-discipline op 10 NIS2-letter-clusters gevalideerd, 13/13 GO-criteria groen, 14/14 sprint-prognose-metrics ✓ exact
2. **Protocol v1.3-draft** (27 mei 2026) — SKOS-beoordelings-protocol uitgebreid met 7 verfijningen op basis van T2-leerpunten + masterchat-werkflow-leerpunt
3. **Projectinstructie v1.10** (27 mei 2026) — verwerkt T1+T2-baselines + sprint-protocollen 14-17 + D4.1 + post-migratie + H41-kandidaat

T2-sprint-architectuur bevat één **nieuw** architectuur-element: **H41-kandidaat** (SKOS-axioma-set-handling). Empirisch bewijs uit T1+T2 dat Δ post-OWL-RL triples = 0 bij predicate-substitutie staaft de architectuur-vraag. Masterchat-besluit: H41 wordt **geparkeerd geregistreerd** als nieuw H-item.

**H36-status:** m10-component **closed** via T1+T2 (28+65 = 93 m10-paren conform cluster-discipline). m14-component blijft open subtask voor toekomstige T-sprint.

---

## §1. Doel van iteratie 14

Brain-vault bijwerken zodat:

1. T2-sprint volledig is gedocumenteerd als sprint-bestand met cross-references naar D4.1, H36, H39, H41
2. D4.1-toepassings-precedent is uitgebreid met T2-cluster-niveau-toepassing
3. H36 m10-component is gemarkeerd als closed; m14-component blijft open
4. H41 nieuw is aangemaakt als geparkeerd H-item
5. Protocol v1.2-toepassings-bewijs + v1.3-draft-status is verwerkt in concept-bestanden
6. Eén of twee nieuwe concept-bestanden zijn toegevoegd (cluster-discipline-bewijslast + optioneel bidirectional-audit-symmetrie)
7. Log + index + relevante registers zijn bijgewerkt naar iteratie 14 + baseline v4.6.2

**Brein-autonomie:** Brein bepaalt zelf welke bestanden precies bijgewerkt of nieuw aangemaakt worden binnen onderstaande scope-contouren. Cross-referentie-discipline wordt strikt gehandhaafd.

---

## §2. Inputs — autoritatieve bronnen

In volgorde van prioriteit:

| Bron | Pad | Rol |
|---|---|---|
| Patch-rapport v4.6.2 | `output/reports/patch-rapport-v4_6_2.md` | **Primaire bron** — alle T2-uitkomsten, GO-criteria, sprint-prognose-evaluatie, §11 H-status-mutaties, §13 open issues |
| Stap 3-eindrapport T2 | `output/reports/t2-stap3-eindrapport.md` | Cluster-beoordelingen per NIS2-letter, uitzondering-screening, §6 werkflow-leerpunten |
| Pilot-rapport T2 (met errata) | `output/reports/t2-pilot-rapport.md` | Pilot-uitkomsten 8 paren + 7 voorstellen voor Protocol v1.3 |
| Pre-sprint-inventarisatie T2 | `output/reports/t2-pre-sprint-inventarisatie.md` | T2-scope-bepaling Optie C |
| Protocol v1.3-draft | `docs/skos-beoordelings-protocol-v1_3.md` | Status DRAFT — toepassings-status v1.10-gedragsregel |
| Projectinstructie v1.10 | `docs/projectinstructie-v1_10.md` | Autoritatieve nieuwe baseline — leidend voor brain-vault-staat |
| Sprint-instructies T2 | `docs/instructies/instructie-t2-*.md` (5 bestanden) | Achtergrond voor sprint-narratief |
| Apply-script + verificatie | `output/scripts/apply_patch_v4_6_2.py`, `output/verification/canonical_metrics_v4_6_2.json`, `output/verification/shacl_results_v4_6_2.json` | Bewijs voor cijfer-claims |

**Discipline:** bij citaten of cijfers in brain-bestanden: bron-verwijzing expliciet (bv. "per patch-rapport v4.6.2 §0.1") zodat latere lezers de bron kunnen verifiëren.

---

## §3. Verwachte updates — richtlijnen per folder

### §3.1 — `brain/brain__sprints/`

**Nieuw bestand:** `brain__sprints__T2-skos-bidirectional-audit-m10.md`

Inhoud-richtlijn:

- Frontmatter conform brain-vault-conventie (type, sprint, baseline, datum, status, related-cross-refs)
- T2-sprint-overzicht: scope-besluit Optie C, 118 m10-paren over 10 clusters
- Vier-stappen-uitvoering:
  - Stap 1: pre-sprint-inventarisatie (149 → 118 m10 + 31 m14-deferral)
  - Stap 2: pilot 8 paren (cluster-discipline gevalideerd op NIS2_a-cluster)
  - Pre-Stap-4 errata-correctie (T-historie hygiëne)
  - Stap 3: hoofd-uitvoering 110 paren (alle 10 clusters → broadMatch)
  - Stap 4: productie-patch v4.6.2 (65 mutaties, 13/13 GO-criteria groen)
- Cluster-discipline-bewijs: 10/10 clusters convergeren naar broadMatch; 0 NEN-uitzonderingen op 10 heuristiek-flags
- Bidirectional mutatie-verdeling: 32 downgrade + 33 upgrade = symmetrisch bewijs Protocol v1.2
- Helper-script-classificatie autoritatief (errata-precedent: pilot-rapport + Stap 3-rapport §1.1)
- Masterchat-instructie-fout §13.2 (zelferkenning: §1 verwachtings-tabel inconsistent met §8 GO-criterium → Protocol v1.3 §10.5-leerpunt)
- Zeven Protocol v1.3-verfijning-voorstellen
- Sprint-multiplier 2,32× t.o.v. T1
- Tijdsraming-evaluatie (alle stappen onder raming dankzij T1-precedent-hergebruik)
- Cross-refs: D4.1, H36, H39, H41, Protocol v1.0/v1.2/v1.3

**Update bestaand register:** `brain__sprints__-register.md` (of analoge naam)

Append T2-entry. Update sprint-multiplier-tabel met v4.6.1 + v4.6.2-rijen (beide 0× multiplier — kwaliteitsanalyse-sprints).

### §3.2 — `brain/brain__decisions/`

**Update:** `brain__decisions__D04_skos-cross-framework.md`

Uitbreiden D4.1-toepassings-precedent-sectie:

- T1-precedent (al gedocumenteerd): 28 paren ENISA-TIG-erfde m10
- **T2-precedent (NIEUW):** 118-paren-cluster-niveau-toepassing
  - Cluster-niveau-D4.1-toepassing: één bevestiging per cluster bij homogene bron-stack volstaat
  - 10 NIS2-letter-clusters allen ENISA-TIG-erfd via CBW-Mapping-UV R3
  - Heterogene clusters (toekomstig) vereisen per-paar-toets
- D4.1-toepasbaarheid-praktijk: cluster-efficiëntie ~~5 sec per paar~~ → één bevestiging per cluster
- Cross-refs: T2-sprint-bestand, H36, Protocol v1.2/v1.3

### §3.3 — `brain/brain__architecture/`

**Update:** `brain__architecture__H36_skos-exactmatch-ctrl-compl-audit.md`

- Status: parent H36 wordt **"active met closed sub-component"**
- Sub-component breakdown:
  - **m10-component: closed** via T1 (v4.6.1) + T2 (v4.6.2) — 28+65 = 93 m10-paren conform cluster-discipline
  - m14-component: **open subtask** — 31 ctrl:↔compl: paren in m14-avg-gdpr.ttl wachten op toekomstige T-sprint (compl→ctrl-richting; AVG-cross-walk-bron-vraag)
  - m11-component: kandidaat-subtask (afhankelijk van H33-trigger)
  - ISO27001-component: kandidaat-subtask (afhankelijk van substantiële m09-uitbreiding)
- Cross-refs: T2-sprint-bestand, D4.1, H41

**Update:** `brain__architecture__H39_*.md` (SHACL-blinde vlek)

- T2 bevestigt opnieuw: SHACL-blinde-vlek op 118-paren-schaal in m10
- Status: active geparkeerd
- Trigger ongewijzigd: shape-uitbreiding op SKOS-distributie indien gewenst
- Cross-refs: T2-sprint-bestand (§7.3 patch-rapport)

**Nieuw bestand:** `brain__architecture__H41_skos-axioma-set-handling.md`

Inhoud-richtlijn:

- Frontmatter: type architecture, H-nummer 41, status geparkeerd, datum 27 mei 2026
- Beschrijving: OWL-RL met huidige instellingen (`axiomatic_triples=False`, `datatype_axioms=False`) laadt geen SKOS-axiomas (skos:S46 symmetrie, skos:S47 transitiviteit). Architectuur-vraag: of skos-axiomas geactiveerd moeten worden in OWL-RL.
- Empirisch bewijs: T1 (28 mutaties) + T2 (65 mutaties) beide Δ post-OWL-RL triples = 0 omdat SKOS-predicate-substitutie binnen één blok geen RDFS/OWL-inferentie-pad raakt
- Trigger voor heractivering: substantiële SKOS-mapping-uitbreiding waar transitiviteit/symmetrie auditief relevant wordt
- Status: geparkeerd (geen acute actie nodig)
- Cross-refs: T2-sprint-bestand, projectinstructie v1.10 "KRITIEKE TECHNISCHE CONVENTIES", patch-rapport v4.6.2 §11

**Update:** H-register (`brain__architecture__-register.md` of analoge naam)

- H36 status-update naar "active (m10 closed)"
- H41 als nieuwe entry toevoegen

### §3.4 — `brain/brain__concepts/`

**Update:** `brain__concepts__skos-beoordelings-protocol.md`

- v1.2-toepassings-bewijs: T2 succesvol gevalideerd op 118-paren-schaal over 10 clusters
- v1.3-draft-status: zeven verfijningen, vaststelling pending bij T3 of m14-sprint-scoping
- v1.3-werkflow-discipline §10.2-§10.5 als gedragsregel in projectinstructie v1.10 opgenomen
- Cross-refs: T2-sprint-bestand, Protocol-bestanden v1.0/v1.2/v1.3

**Update:** `brain__concepts__mapping-bron-disclaimer-effect.md`

- D4.1-cluster-niveau-toepassing toevoegen
- ENISA TIG R285-precedent (T1 al gedocumenteerd) uitbreiden met CBW-Mapping-UV R3-erf via cluster-niveau
- T2-praktijk: cluster-efficiëntie
- Cross-refs: D04, T2-sprint-bestand

**Nieuw bestand:** `brain__concepts__cluster-discipline-bewijslast.md`

Inhoud-richtlijn:

- Bewijslast-asymmetrie voor cluster-uitzondering (Protocol v1.3 §3.3)
- Drie scenario's: behoud cluster-default (geen bewijslast), uitzondering naar sterker mapping (streng), uitzondering naar zwakker mapping (streng)
- T2-empirisch bewijs: 0/10 succesvolle uitzonderingen op heuristiek-flags (alle cluster-conform na NEN-tekst-lezing)
- Streng kader voor cluster-uitzondering in veel↔1-clusters (object-cluster-cardinaliteit ≥2 maakt bilaterale containment structureel onmogelijk)
- Cross-refs: Protocol v1.2/v1.3, T2-sprint-bestand, T2-Stap-3-eindrapport §6.5

**Optioneel nieuw bestand:** `brain__concepts__bidirectional-audit-symmetrie.md`

Brein bepaalt zelf of dit als apart concept of als sub-sectie binnen `brain__concepts__skos-beoordelings-protocol.md` past. Inhoud:

- Protocol v1.2 §3.1-predicate-doel-tabel symmetrisch toepasbaar
- T2-empirisch bewijs: 32 downgrade + 33 upgrade = vrijwel symmetrische mutatie-verdeling
- Geen downgrade-bias zoals v1.1-draft veronderstelde
- Categorie 7-werkflow-leerpunt (Protocol v1.2 §10 + v1.3 §10.1)
- Cross-refs: Protocol v1.2 §3, T2-sprint-bestand, T2-pilot-rapport §6.7

### §3.5 — `brain/brain__workflow/`

**Mogelijke update:** indien bestand voor sprint-protocollen of werkflow-discipline aanwezig:

- Sprint-protocollen 14-17 referentie (al actief in `docs/sprint-protocols.md`; brain-vault-bestand kan korte samenvatting + cross-ref bevatten)
- Protocol v1.3 §10.2-§10.5 werkflow-discipline-status (opgenomen als gedragsregel in projectinstructie v1.10)
- Cross-refs: Protocol v1.3, projectinstructie v1.10

### §3.6 — Log + Index

**Update:** `brain/brain__log.md`

- Append iteratie 14-entry: datum 27 mei 2026, baseline v4.6.2, T2-sprint afsluiting, Protocol v1.3-draft, projectinstructie v1.10
- Lijst alle gewijzigde + nieuwe brain-bestanden in iteratie 14

**Update:** `brain/brain__index.md`

- Baseline-update naar v4.6.2
- Iteratie-teller naar 14
- Cross-ref-overzicht ververst

---

## §4. Cross-referentie-discipline

Bij elke update of nieuwe entry: verifieer dat **alle gerelateerde brain-bestanden** wederkerig naar elkaar verwijzen. Voorbeelden:

| Wijziging in | Verifieer cross-refs in |
|---|---|
| T2-sprint-bestand | D04 (D4.1-precedent), H36, H39, H41, skos-protocol-concept, mapping-bron-disclaimer, log, index |
| D04 (D4.1-update) | T2-sprint, H36, mapping-bron-disclaimer-concept, Protocol-cross-ref |
| H36 (m10 closed) | T2-sprint, D04, H39, H41, decisions-register, architecture-register |
| H41 (NIEUW) | T2-sprint, projectinstructie v1.10, patch-rapport v4.6.2, architecture-register, log, index |
| Cluster-discipline-bewijslast (NIEUW) | Protocol v1.2/v1.3, T2-sprint, T2-Stap-3-eindrapport, concepts-register |

**Discipline-test:** voor elk gewijzigd of nieuw bestand, doe `grep`-of-zoek op het bestand-pad / -naam in alle andere bestanden in brain/. Als een bestaand bestand zou moeten verwijzen maar niet doet: update toevoegen.

---

## §5. Iteratie-bookkeeping

| Item | Vóór iteratie 14 | Na iteratie 14 |
|---|---|---|
| Iteratie-teller | 13 | 14 |
| Baseline-context | v4.6.1 (post-T1) | v4.6.2 (post-T2) |
| Brain-bestand-totaal | ~115 | ~120 (geschat na nieuwe sprint-bestand + H41 + cluster-discipline-bewijslast + optioneel bidirectional-audit-symmetrie) |
| Laatste sprint-entry | T1-sprint v4.6.1 | T2-sprint v4.6.2 |
| Laatste D-decision-precedent | D4.1 T1-toepassing | D4.1 T2-cluster-niveau-toepassing |
| Laatst aangemaakt H-item | (laatste pre-T1) | H41 |
| Laatste closed H-component | (volgens H-register) | H36 m10-component |

---

## §6. Pre-push disclosure-check (Protocol 14)

Vóór hand-off aan Steven: 5-categorieën-check op alle brain-vault-mutaties:

1. **Organisatie-naam** — geen vermelding (gebruik "de organisatie" / "Rijksoverheidsorganisatie")
2. **Persoonsnamen** — alleen Steven Bouwmeester (publieke projecteigenaar); geen anderen
3. **Lokale paden** — alleen `/Users/stevenbouwmeester/grc-kennismodel/` (project) en `/Users/stevenbouwmeester/grc-sources-licensed/` (NEN-licentie) toegestaan; geen organisatie-interne paden
4. **Credentials/TLD/e-mail** — geen
5. **NEN-tekst-fragmenten >10 woorden** — geen verbatim ISO/NEN-tekst; parafrase + clausule-verwijzing wel toegestaan

Brain-vault is conceptueel-administratief (geen NEN-tekst-citaten verwacht); risico vooral op categorie 5 indien Brein verleid wordt om ISO-tekst over te nemen uit T2-rapporten. Strikte parafrase-discipline.

---

## §7. Hand-off-checklist

- [ ] Sprint-bestand `brain__sprints__T2-skos-bidirectional-audit-m10.md` aangemaakt
- [ ] Sprint-register T2-entry toegevoegd
- [ ] D04 D4.1-toepassings-precedent uitgebreid met T2-cluster-niveau
- [ ] H36 status-update naar "active met m10 closed"
- [ ] H39 status-update (T2 bevestigt SHACL-blinde-vlek)
- [ ] H41 nieuw bestand aangemaakt (geparkeerd)
- [ ] Architecture-register H36 + H41 bijgewerkt
- [ ] Concept skos-beoordelings-protocol bijgewerkt (v1.2-toepassings-bewijs + v1.3-draft-status)
- [ ] Concept mapping-bron-disclaimer-effect bijgewerkt (cluster-niveau-toepassing)
- [ ] Nieuw concept cluster-discipline-bewijslast aangemaakt
- [ ] Optioneel: nieuw concept bidirectional-audit-symmetrie
- [ ] Concepts-register bijgewerkt indien nieuwe concept-bestanden
- [ ] Eventueel workflow-bestanden voor sprint-protocollen 14-17 bijgewerkt
- [ ] Log iteratie 14-entry toegevoegd
- [ ] Index baseline-update + iteratie-teller
- [ ] Cross-referentie-test uitgevoerd (alle nieuwe + gewijzigde bestanden hebben wederkerige cross-refs)
- [ ] Pre-push disclosure-check Protocol 14 — 5 categorieën pass
- [ ] Geen autonome commits (Steven inspecteert + commit handmatig)

---

## §8. Wat NIET in scope iteratie 14

- **Geen architecturele beslissingen** — D1-D12 + D4.1 zijn vastgesteld; Brein documenteert toepassings-precedent maar wijzigt geen D-decision-tekst
- **Geen strategische interpretatie** van patch-rapport — neem feitelijke uitkomsten over, geen herinterpretatie
- **Geen wijziging Protocol v1.3-tekst** — v1.3 is masterchat-DRAFT, vaststelling bij T3-scoping
- **Geen `docs/sprint-protocols.md`-wijziging** — al actief sinds iteratie 12-13, geen nieuwe protocollen in T2
- **Geen ontologie-wijzigingen** — m10-nis2-ext.ttl is finaal v4.6.2 per patch-rapport
- **Geen m14-sprint-voorbereiding** — apart, later
- **Geen README.md-update** — apart spoor na Optie C voltooiing
- **Geen dashboard-inhaalslag** — separate Dashboard-werkstroom
- **Geen PK-opschoning** — afhankelijk van afstemming Steven (post-Brein-cyclus)

---

## §9. Bij voltooiing

Brein levert via `git status` overzicht van gewijzigde + nieuwe bestanden. Steven inspecteert + commit + pusht handmatig.

Masterchat reviewt na push:

- Sprint-bestand T2 conform autoritatieve bronnen?
- D4.1-precedent-uitbreiding consistent?
- H36 + H41-updates correct?
- Nieuwe concepten passen in brain-vault-architectuur?
- Cross-references consistent?

**Bij masterchat-GO: brain-vault-iteratie 14 formeel afgesloten.** Daarna stap 8 van Optie C: README.md-update naar v1.10/v4.6.2.

T2-sprint-cyclus is dan volledig afgesloten:

```
✓ Stap 1: T2 pre-sprint-inventarisatie  (26-27 mei)
✓ Stap 2: T2 pilot                      (27 mei)
✓ Pre-Stap-4 errata                     (27 mei)
✓ Stap 3: T2 hoofd-uitvoering           (27 mei)
✓ Stap 4: T2 productie-patch v4.6.2     (27 mei)
✓ Protocol v1.3-draft                   (27 mei)
✓ Projectinstructie v1.10               (27 mei)
○ Brein-cyclus iteratie 14              (volgende — Brein-actie via Claude Code)
○ README-update                          (na Brein-cyclus — Optie C voltooid)
```

---

## §10. Verwijzingen

| Document | Pad |
|---|---|
| Patch-rapport v4.6.2 (primair) | `output/reports/patch-rapport-v4_6_2.md` |
| T2 Stap 3-eindrapport | `output/reports/t2-stap3-eindrapport.md` |
| T2 pilot-rapport (met errata) | `output/reports/t2-pilot-rapport.md` |
| T2 pre-sprint-inventarisatie | `output/reports/t2-pre-sprint-inventarisatie.md` |
| Protocol v1.3-draft | `docs/skos-beoordelings-protocol-v1_3.md` |
| Projectinstructie v1.10 | `docs/projectinstructie-v1_10.md` |
| Sprint-protocollen v1.3 | `docs/sprint-protocols.md` |
| Apply-script v4.6.2 | `output/scripts/apply_patch_v4_6_2.py` |
| Cluster-overerving-helper | `output/scripts/t2-cluster-overerving-helper.py` |
| Canonical metrics-output | `output/verification/canonical_metrics_v4_6_2.json` |
| SHACL-validatie-output | `output/verification/shacl_results_v4_6_2.json` |
| Brain-vault root | `brain/` |
| Brain-vault index | `brain/brain__index.md` |
| Brain-vault log | `brain/brain__log.md` |
| Dit instructie-bestand | `docs/instructies/instructie-brein-iteratie-14.md` |

---

*Einde Brein-cyclus iteratie 14-instructie. Modus: brain-vault-onderhoud binnen contouren. Brein-autonomie op bestand-keuze + inhoud-detail. Steven commit handmatig.*
