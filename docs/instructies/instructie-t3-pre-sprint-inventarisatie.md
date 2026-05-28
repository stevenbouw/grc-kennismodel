# T3 Pre-sprint-inventarisatie — instructie voor Tech-subagent

**Sprint:** T3 (SKOS-kwaliteitsanalyse Fase 3 — compl:↔ctrl: audit in m14 AVG/GDPR)
**Fase:** Pre-sprint-inventarisatie (Stap 1 van sprint)
**Auteur:** Masterchat
**Datum:** 28 mei 2026
**Modus:** **READ-ONLY** — geen ontologie-wijzigingen, geen patches, geen SHACL-runs op gewijzigde files
**Autoritatief protocol:** `docs/skos-beoordelings-protocol-v1_2.md` (operationeel) + `docs/skos-beoordelings-protocol-v1_3.md` (DRAFT — werkflow-disciplines §10.2-§10.5)
**Voorgangers:** T1 (`output/reports/t1-eindrapport-v4_6_1.md`) + T2 (`output/reports/patch-rapport-v4_6_2.md`)

---

## §0. Context

T3-scope is bij masterchat-sessie 28-05-2026 vastgesteld. T3 sluit de open subtask van H36 af (m14-component) en is daarmee de laatste geregistreerde ctrl:↔compl:-audit-sprint.

- **Module:** `m14-avg-gdpr.ttl`
- **Cluster:** compl:↔ctrl: SKOS-mappings (AVG/GDPR ↔ ISO 27002-controls)
- **Richting:** **compl: → ctrl:** — LET OP: omgekeerd t.o.v. m10's ctrl: → compl: (T1+T2). Dit heeft methodische gevolgen, zie §0.2
- **Verwachte scope:** 31 paren (per H36-registratie: 27 relatedMatch + 2 closeMatch + 2 broadMatch — te verifiëren via deze inventarisatie)
- **AVG-scope:** alleen de 5 IB-raakvlakartikelen — art. 5(1f), 25, 32, 33, 34 (zie `brain/brain__modules__M14_avg-gdpr.md`)
- **Werkomgeving:** Tech-autonomie via lokale NEN-toegang in `/Users/stevenbouwmeester/grc-sources-licensed/`

### §0.1 Bron-situatie — fundamenteel anders dan m10

T1+T2 dreven op de ENISA TIG-disclaimer (via CBW-Excel): één autoritatieve bron ontkende equivalence categorisch, waardoor alle m10-clusters naar `broadMatch` convergeerden (D4.1). **Voor m14 bestaat geen vergelijkbare bron.** ENISA heeft geen GDPR↔ISO-control-cross-walk; ENISA's GDPR-werk is een risico-gebaseerde eigen maatregelen-catalogus.

De m14-evidence-basis is daarom **gelaagde triangulatie**:

| Bron | Type | Status | Locatie |
|---|---|---|---|
| ISO/IEC 27701:2025 (PIMS) | Autoritatief (NEN-restrictief) | Net opgenomen | `/Users/stevenbouwmeester/grc-sources-licensed/ISO27701.pdf` (2025-editie) |
| ISO 27701-conformiteitsbeoordeling | Autoritatief-aanvullend | Net opgenomen | lokale folder (apart bestand, ~675 KB) |
| ISO/IEC 29100:2011 (privacy framework) | Autoritatief-terminologie | Opgenomen | lokale folder |
| Publieke 2022-cross-walks (ISMS.online e.a.) | Secundair / indicatief | Web-referentie | n.v.t. (niet in repo) |
| ISO 27002:2022 | Autoritatief (control-semantiek) | Reeds beschikbaar | lokale folder |
| AVG/GDPR-tekst | Publiek EU-recht | Beschikbaar | `sources/eu-recht/` (verifieer) |

**Belangrijke bron-nuance:** ISO 27701 is primair een PIMS-standaard, geen kant-en-klare "GDPR-artikel → ISO 27002-control"-tabel. De 2019-editie had een GDPR-mapping in Annex D (naar 27701-clausules); de 2025-editie is een standalone standaard met herziene Annex-structuur (Annex A privacy-controls controllers/processors + information security controls). **Vraag C vraagt expliciet om te verifiëren wáár in 27701:2025 — of in de conformiteitsbeoordeling — de bruikbare GDPR-artikel↔control-relatie staat.** Dit is geen aanname; het moet vastgesteld worden.

### §0.2 Methodische waarschuwing — GEEN convergentie-aanname

T2's cluster-discipline (binnen homogene-bron-cluster volstaat één cluster-toets; alle paren convergeren naar één match-type) is een **m10-specifiek resultaat**, gedreven door de ENISA-disclaimer. **Pas dit NIET klakkeloos toe op m14.**

Reden: de AVG↔control-relatie is semantisch heterogeen. AVG-artikelen zijn juridische verplichtingen; ISO-controls zijn maatregelen die eraan bijdragen. Per control verschilt de relatie:
- art. 32 → encryptie-control (8.24): mogelijk `closeMatch` (specifieke maatregel sluit nauw aan)
- art. 32 → governance-control: mogelijk `relatedMatch` (ondersteunend, niet specifiek)
- art. 33 → incident-management-control: mogelijk `relatedMatch` (control ondersteunt de meldplicht-verplichting)

**Verwachting masterchat (niet sturend voor uitkomst):** de bestaande 27 relatedMatch zijn vermoedelijk grotendeels verdedigbaar. T3 is naar verwachting een **bevestigings-sprint met laag mutatie-volume** (0-4 mutaties), geen herclassificatie-golf zoals T1/T2. Dit is een verwachting, geen instructie — Tech beoordeelt op eigen merites.

**Consequentie voor methode:** per-paar-toetsing (C1-C4) is waarschijnlijk nodig i.p.v. cluster-convergentie. Vraag F onderzoekt of het protocol een aanvulling nodig heeft voor (a) de compl→ctrl-richting en (b) heterogene-cluster-handling.

---

## §1. Doel pre-sprint-inventarisatie

Vóór T3-uitvoering levert Tech een read-only rapport dat:

1. Scope verifieert (klopt de 31-paren-aanname? 27 related + 2 close + 2 broad?)
2. Cluster-structuur ontsluit (per AVG-artikel: welke controls, welke match-types?)
3. **Bron-structuur vaststelt** — wáár in 27701:2025 + conformiteitsbeoordeling staat de GDPR↔control-relatie? (kern-vraag T3)
4. Evidence-coverage vaststelt (hoeveel van de 31 paren worden gedekt door 27701-mapping + publieke cross-walks?)
5. Symmetrie-methode-vraag beantwoordt (werkt Protocol v1.2/v1.3 voor compl→ctrl, of is aanvulling nodig?)
6. Blockers signaleert

**Doel is niet:** pre-pilot-uitkomst-voorspelling per paar. Inventarisatie levert structurele cijfers + bron-bevindingen, geen uitkomst-projecties.

**Modus:** read-only. Geen wijzigingen aan `m14-avg-gdpr.ttl`, geen patches, geen test-applies. Wel toegestaan: SPARQL-queries op huidige graph, file-reads, lokale NEN-bron-lezing, web-referentie publieke cross-walks.

---

## §2. Vragen A-F

### Vraag A — Scope-bevestiging

Tel exact aantal compl:↔ctrl: SKOS-mappings in `m14-avg-gdpr.ttl`, per predicate-type. Verifieer of alle m14-AVG-mappings in dit bestand zitten (geen verstrooiing naar andere modules).

| Predicate | Aantal in m14 | Aantal elders (specificeer) | Totaal |
|---|---:|---:|---:|
| `skos:exactMatch` | ? | ? | ? |
| `skos:closeMatch` | ? | ? | ? |
| `skos:broadMatch` | ? | ? | ? |
| `skos:narrowMatch` | ? | ? | ? |
| `skos:relatedMatch` | ? | ? | ? |
| **Totaal** | ? | ? | ? |

**Verwachting ter referentie (te bevestigen of corrigeren):** 27 related + 2 close + 2 broad = 31. Indien afwijking: meld expliciet.

**Let op richting:** verifieer of de paren daadwerkelijk compl:→ctrl: geserialiseerd zijn (subject = compl:AVGRequirement, object = ctrl:). Documenteer indien gemengd.

### Vraag B — Cluster-structuur per AVG-artikel

Groepeer de paren per AVG-artikel (subject-zijde). Per artikel: welke ctrl:-controls, welke match-types.

```
Cluster AVG-art-32 — compl:AVG_art32_xxx (subject)
  Cardinaliteit: 1↔veel (één artikel → meerdere controls)
  Cluster-grootte: N paren
  Predicate-mix: a× related, b× close, c× broad
  Paren:
    - compl:AVG_art32_xxx skos:relatedMatch ctrl:8_24
    - compl:AVG_art32_xxx skos:closeMatch ctrl:...
    ...
```

**Aanvullend:** noteer per cluster of de predicate-mix homogeen is (alle paren zelfde type) of heterogeen (gemengd). Heterogene clusters bevestigen de §0.2-verwachting dat per-paar-toetsing nodig is.

### Vraag C — Bron-structuur-verificatie (KERN-vraag T3)

Dit is de bepalende vraag voor T3-haalbaarheid. Verifieer in de lokale NEN-folder:

**C.1 — ISO 27701:2025 structuur:**
- Bevestig editie (titelpagina: "ISO/IEC 27701:2025"?)
- Bevat 27701:2025 een expliciete GDPR-artikel-mapping? Zo ja, in welke Annex/sectie?
- Indien geen directe GDPR-artikel-mapping: bevat het een mapping naar ISO 27002-controls die indirect bruikbaar is?
- Parafraseer de structuur (geen verbatim >10 woorden)

**C.2 — Conformiteitsbeoordeling (~675 KB bestand):**
- Identificeer wat dit document precies is (ISO 27006-2? ISO 27706:2025? een mapping-document? een conformity-assessment-checklist?)
- Bevat het een GDPR↔control-mapping of cross-reference die bruikbaar is voor de 31 paren?

**C.3 — Bruikbaarheids-conclusie:**
- Welke van de twee documenten (of combinatie) levert de sterkste evidence voor compl:AVG→ctrl:-relaties?
- Is de evidence niveau-1 (autoritatieve directe mapping), of niveau-2 (indirecte/afgeleide mapping die interpretatie vereist)?

### Vraag D — Evidence-coverage per paar

Voor de 31 paren: hoeveel worden gedekt door welke bron?

| Evidence-bron | Aantal paren gedekt | Niveau |
|---|---:|---|
| ISO 27701:2025 directe mapping | ? | 1 |
| ISO 27701:2025 indirecte/afgeleide mapping | ? | 2 |
| Conformiteitsbeoordeling | ? | 1 of 2 |
| Publieke 2022-cross-walk (ISMS.online e.a.) | ? | 2 |
| Alleen Tech-analyse (27002:2022 + AVG-tekst, geen externe mapping) | ? | 3 |
| Geen evidence-trace | ? | — (rood vlaggetje) |

**Interpretatie:** paren zonder enige evidence-trace zijn rode vlaggetjes voor pilot-selectie.

### Vraag E — Bron-toegankelijkheid + blockers

| Bron-type | Locatie | Status | Blocker? |
|---|---|---|---|
| ISO 27701:2025 | lokale folder | ? | ? |
| ISO 27701-conformiteitsbeoordeling | lokale folder | ? | ? |
| ISO 29100:2011 | lokale folder | ? | ? |
| ISO 27002:2022 | lokale folder | ? | ? |
| AVG/GDPR-tekst | `sources/eu-recht/` | ? | ? |
| Publieke cross-walks | web-referentie | ? | ? |

**Discipline-reminder Protocol 14 + 17:** parafrase + clausule-verwijzing wel; verbatim NEN-tekst >10 woorden niet. Geldt voor 27701, 29100, 27002 (alle NEN-restrictief). Publieke cross-walks zijn niet-NEN maar wel auteursrechtelijk — ook parafraseren.

### Vraag F — Symmetrie- en heterogeniteit-methode-check

Beoordeel of het bestaande protocol (v1.2 operationeel + v1.3-draft) toereikend is voor T3, of dat een aanvulling nodig is. Twee specifieke aandachtspunten:

**F.1 — Richtings-symmetrie (compl→ctrl):** v1.2 is ontwikkeld voor m10's ctrl→compl. Werken de C1-C4-criteria symmetrisch bij omgekeerde richting? Identificeer eventuele asymmetrie in de criteria-toepassing.

**F.2 — Heterogene-cluster-handling:** v1.2's cluster-discipline (T2) gaat uit van convergentie binnen homogene-bron-clusters. m14-clusters zijn vermoedelijk heterogeen (zie §0.2). Vereist dit een protocol-aanvulling (per-paar-toetsing expliciet vastleggen), of dekt v1.2/v1.3 dit al af?

**Lever:** een korte aanbeveling — "v1.2/v1.3 toereikend" OF "aanvulling nodig op punt X". Dit informeert de masterchat-beslissing over protocol-versie vóór de pilot.

---

## §3. Output-formaat

**Bestandsnaam:** `t3-pre-sprint-inventarisatie.md` in `output/reports/`

**Structuur:**

```
# T3 Pre-sprint-inventarisatie-rapport

## §1. Samenvatting (max 10 regels — kerncijfers + scope-bevestiging + bron-bruikbaarheids-conclusie)
## §2. Vraag A — Scope-bevestiging
## §3. Vraag B — Cluster-structuur per AVG-artikel
## §4. Vraag C — Bron-structuur-verificatie (27701:2025 + conformiteitsbeoordeling)
## §5. Vraag D — Evidence-coverage per paar
## §6. Vraag E — Bron-toegankelijkheid + blockers
## §7. Vraag F — Symmetrie- en heterogeniteit-methode-check
## §8. Tech-observaties (eigen vondsten buiten de zes vragen)
## §9. Pilot-sample-aanbeveling
## §10. Hand-off-checklist
```

Volg Protocol v1.3 §10.2 (bottom-up rapport-bouw: §2-§7 details vóór §1-samenvatting; markeer §1 als "INITIEEL, TE BEVESTIGEN" indien vroeg ingevuld).

**§9 Pilot-sample-aanbeveling:** gezien de kleine totaal-scope (31) een sample van **6 paren** met spreiding over:
- Alle aanwezige predicate-types (related + close + broad)
- Verschillende AVG-artikelen (spreid over art. 5(1f)/25/32/33/34)
- Verschillende evidence-niveaus (niveau-1 27701-gedekt + niveau-2/3)
- Lever IRI's + cluster-context per paar (geen alleen-IDs)

**§10 Hand-off-checklist:**

- [ ] Pre-push disclosure-check Protocol 14 (vijf categorieën inclusief NEN-tekst >10 woorden — extra aandacht: 27701/29100/27002 zijn alle NEN)
- [ ] Geen patches/ontologie-wijzigingen toegepast
- [ ] Geen autonome commits (Steven commit handmatig)
- [ ] Rapport zelfstandig leesbaar voor masterchat
- [ ] §9 pilot-sample bevat IRI's + cluster-context per paar
- [ ] §4 bron-bruikbaarheids-conclusie expliciet (niveau-1 of niveau-2)

---

## §4. Wat NIET in deze fase

- Geen C1-C4-toetsing per paar — dat is pilot-fase (Stap 2) en hoofd-uitvoering (Stap 3)
- Geen patch-voorbereiding — Stap 4
- Geen protocol-aanvulling schrijven — Vraag F levert alleen een *aanbeveling*; masterchat beslist
- Geen pre-pilot-uitkomst-voorspelling per paar
- Geen toepassing van m10-cluster-convergentie-discipline zonder per-cluster-rechtvaardiging (zie §0.2)

---

## §5. Scope-pauze-triggers

Pauzeer en escaleer naar masterchat indien:

- Totaal-aantal m14-mappings >40 of <25 (significante afwijking van 31-verwachting)
- `exactMatch`- of `narrowMatch`-paren aanwezig in m14 (niet verwacht; vereist methode-overweging)
- ISO 27701:2025 blijkt **geen** bruikbare GDPR↔control-relatie te bevatten (noch direct, noch indirect, noch via conformiteitsbeoordeling) — dan valt de niveau-1-basis weg en moet masterchat beslissen over niveau-2-only-route
- Bron-blocker die T3-uitvoering verhindert
- ABox-anomalie (zelfde paar met meerdere SKOS-predicates; orphan-resources; verkeerde richting-serialisatie)
- Vraag F concludeert dat een substantiële protocol-aanvulling nodig is vóór de pilot kan starten

Format scope-pauze: probleem + Optie A/B/C met rationale + Tech-voorkeur + vraag aan masterchat.

---

## §6. Geschatte duur

T1/T2-precedent pre-sprint-inventarisatie: ~1.5-2 uur. T3 is kleinere paren-scope (31 vs 118) maar zwaardere bron-verificatie (Vraag C is nieuw en substantieel — 27701:2025-structuur uitpluizen). Verwachting: ~1.5-2 uur.

Geen harde deadline. Kwaliteit boven snelheid — met name Vraag C verdient zorgvuldigheid, want die bepaalt de hele sprint-evidence-basis.

---

*Einde instructie. Bij voltooiing: push rapport + wacht op masterchat-review. Geen verdere autonome actie. Na review volgt protocol-beslissing (v1.3-vaststelling of v1.4-aanvulling) + pilot-instructie (Stap 2).*
