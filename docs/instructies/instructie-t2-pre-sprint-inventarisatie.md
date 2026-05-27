# T2 Pre-sprint-inventarisatie — instructie voor Tech-subagent

**Sprint:** T2 (SKOS-kwaliteitsanalyse Fase 2 — bidirectional audit ctrl:↔compl:)
**Fase:** Pre-sprint-inventarisatie (Stap 1 van sprint)
**Auteur:** Masterchat
**Datum:** 27 mei 2026
**Modus:** **READ-ONLY** — geen ontologie-wijzigingen, geen patches, geen SHACL-runs op gewijzigde files
**Autoritatief protocol:** `docs/skos-beoordelings-protocol-v1_2.md`
**Voorganger:** T1-precedent (`output/reports/t1-eindrapport-v4_6_1.md`)

---

## §0. Context

T2-scope is bij masterchat-sessie 27-05-2026 vastgesteld:

- **Cluster:** ctrl:↔compl: SKOS-mappings in `m10-nis2-ext.ttl`
- **Audit-frame:** bidirectional — mutaties zowel upgrade (zwakker → sterker) als downgrade (sterker → zwakker) als richtings-correctie (broadMatch ↔ narrowMatch) als behoud
- **Scope-uitbreiding:** 18 resterende `skos:exactMatch`-paren geïntegreerd; T1-28 (nu `broadMatch`) meegenomen onder v1.2-protocol
- **Verwachte totaal:** ~111 paren (te verifiëren via deze inventarisatie)
- **Werkomgeving:** Tech-autonomie via lokale NEN-toegang in `/Users/stevenbouwmeester/grc-sources-licensed/`; masterchat alleen bij twijfelgevallen-escalatie conform Protocol v1.2 §4

Protocol v1.2 (DRAFT, gesigned-off bij T2-scoping) is autoritatief voor alle T2-uitvoering. Lees `docs/skos-beoordelings-protocol-v1_2.md` integraal voor C1-C4-criteria, D4.1-vooraf-check, predicate-doel-tabel, en output-formaat.

---

## §1. Doel pre-sprint-inventarisatie

Vóór T2-uitvoering levert Tech een read-only rapport dat:

1. Scope verifieert (klopt de ~111-aanname?)
2. Cluster-structuur ontsluit (welke clusters bestaan, met welke cardinaliteit?)
3. Evidence-coverage in `sources/` vaststelt (hoeveel paren hebben evidence-niveau 1?)
4. D4.1-disclaimer-status per bron bevestigt
5. Eventuele blockers signaleert (bron-toegankelijkheid, ABox-anomalieën)

**Doel is niet:** pre-pilot-uitkomst-voorspelling. Protocol v1.2 §6 verbiedt expliciet pre-pilot-verwachting. Inventarisatie levert **structurele cijfers**, niet uitkomst-projecties.

**Modus:** read-only. Geen wijzigingen aan `m10-nis2-ext.ttl`, geen patches, geen test-applies. Wel toegestaan: SPARQL-queries op huidige graph, file-reads, bron-doorzoek.

---

## §2. Vragen A-E

### Vraag A — Scope-bevestiging

Tel exact aantal ctrl:↔compl: SKOS-mappings, per predicate-type, in alle ontologie-modules. Hoofdverwachting is dat alle mappings in `m10-nis2-ext.ttl` zitten — verifieer.

Lever een tabel:

| Predicate | Aantal in m10-nis2-ext | Aantal elders (specificeer module) | Totaal |
|---|---:|---:|---:|
| `skos:exactMatch` | ? | ? | ? |
| `skos:closeMatch` | ? | ? | ? |
| `skos:broadMatch` | ? | ? | ? |
| `skos:narrowMatch` | ? | ? | ? |
| `skos:relatedMatch` | ? | ? | ? |
| **Totaal** | ? | ? | ? |

**Verwachtingen ter referentie (te bevestigen of corrigeren):**

- `exactMatch` ≈ 18 (T1-residueel)
- `broadMatch` ≈ 28+ (T1-output + eventueel reeds bestaand)
- Totaal ≈ 111
- `narrowMatch` mogelijk 0 in ctrl:↔compl:-cluster

Indien afwijking >5% van verwachting: meld dit expliciet als opvallend in rapport-conclusie.

### Vraag B — Cluster-structuur per predicate

Voor elk predicate-type met >0 mappings: identificeer cluster-structuren. Een **cluster** definieert zich rond een gedeeld subject (ctrl:) of object (compl:) waaraan meerdere paren hangen.

Per cluster: identifier, cardinaliteit-type, cluster-grootte, lijst van paren.

Voorbeeld-format:

```
Cluster CL-001 — compl:NIS2_b (object) met meerdere ctrl:-subjects
  Cardinaliteit: veel↔1
  Cluster-grootte: 4 paren
  Predicate-mix in cluster: 4× broadMatch
  Paren:
    - ctrl:X_xxx skos:broadMatch compl:NIS2_b
    - ctrl:Y_yyy skos:broadMatch compl:NIS2_b
    ...

Cluster CL-002 — ctrl:Z_zzz (subject) met enkele compl:-target
  Cardinaliteit: 1↔1
  Cluster-grootte: 1 paar
  Predicate-mix in cluster: 1× exactMatch
  Paren:
    - ctrl:Z_zzz skos:exactMatch compl:UV_art_x
```

**Aanvullende metric per cluster:** bredere-cluster-cardinaliteit (over alle predicate-types samen) — relevant voor C2-toets conform v1.2 §2.2.

Belangrijk: clusters kunnen multi-predicate zijn (bv. één compl:-object met zowel broadMatch- als closeMatch-paren erop). Specificeer mix expliciet.

### Vraag C — Evidence-niveau-1-pre-stap (`sources/`-doorzoek)

Voer doorzoek uit op cross-walk-bronnen in `sources/`-folder. Primaire bron:

- `sources/adr-norea/Cbw_NIS2_Control_Framework.xlsx` — sheet "Mapping Uitvoeringsverordening" (T1-precedent: reproduceert ENISA TIG v1.0)

Eventuele andere bronnen om te checken:

- Andere sheets in `Cbw_NIS2_Control_Framework.xlsx` met mapping-content
- Eventuele BZK/NCSC-bronnen in `sources/` indien aanwezig

Per bron, lever:

| Bron-bestand | Sheet/sectie | Aantal mappings in bron | Aantal mappings overlap met model | Aantal model-mappings ZONDER bron-overlap |
|---|---|---:|---:|---:|

**Interpretatie:**
- Overlap = evidence-niveau-1-coverage
- Zonder-bron-overlap = model-paren die ofwel evidence-niveau-2-3-4 hebben (legitiem) ofwel geen bron-trace (rood vlaggetje voor T2-pilot-selectie)

### Vraag D — D4.1-disclaimer-overzicht per bron

Per bron in scope: verifieer disclaimer-aanwezigheid conform Protocol v1.2 §2.0.

| Bron | Bestand | Locatie disclaimer | Disclaimer-tekst (parafrase) | D4.1-implicatie |
|---|---|---|---|---|
| ENISA TIG v1.0 | extern (T1-bekend) | regel 285 | bron ontkent equivalence categorisch | exactMatch geblokkeerd voor paren met ENISA-evidence |
| CBW-Excel | `sources/adr-norea/Cbw_NIS2_Control_Framework.xlsx` | ? | ? | ? |
| Andere (specificeer) | ? | ? | ? | ? |

**T1-bekend:** ENISA TIG-disclaimer is bevestigd in T1; opnieuw verifiëren niet nodig — wel registreren met T1-verwijzing.

**Te verifiëren in T2:** CBW-Excel's eigen disclaimer-status (ADR/NOREA-uitgegeven publicatie; zou eigen caveat-clausule kunnen bevatten over interpretatieve aard van haar mapping-werk).

### Vraag E — Bron-toegankelijkheid + blockers

Verifieer toegankelijkheid van alle benodigde bronnen:

| Bron-type | Locatie | Status | Blocker? |
|---|---|---|---|
| Lokale NEN — ISO 27002:2022 | `/Users/stevenbouwmeester/grc-sources-licensed/` | ? | ? |
| Lokale NEN — ISO 27001:2022 | `/Users/stevenbouwmeester/grc-sources-licensed/` | ? | ? |
| CBW-Excel | `sources/adr-norea/` in repo | ? | ? |
| UV (EU) 2024/2690 | `sources/eur-lex/` of vergelijkbaar | ? | ? |
| ENISA TIG v1.0 PDF | repo of upload | ? | ? |
| Andere (specificeer) | ? | ? | ? |

**Discipline-reminder Protocol v1.2 §8:** parafrase + clausule-verwijzing wel; verbatim NEN-tekst >10 woorden niet. Geldt voor inventarisatie-rapport en alle latere T2-output.

---

## §3. Output-formaat

**Bestandsnaam:** `t2-pre-sprint-inventarisatie.md` in `output/reports/` (of conventie-passende locatie binnen repo)

**Structuur:**

```
# T2 Pre-sprint-inventarisatie-rapport

## §1. Samenvatting (max 10 regels — kerncijfers + conclusie scope-bevestiging)
## §2. Vraag A — Scope-bevestiging (tabel + analyse)
## §3. Vraag B — Cluster-structuur (per predicate-type)
## §4. Vraag C — Evidence-niveau-1-coverage
## §5. Vraag D — D4.1-disclaimer-overzicht
## §6. Vraag E — Bron-toegankelijkheid + blockers
## §7. Tech-observaties (eigen vondsten buiten de vijf vragen)
## §8. Pilot-sample-aanbeveling (8 paren conform §6 Protocol v1.2)
## §9. Hand-off-checklist
```

**§7 Tech-observaties:** ruimte voor eigen vondsten — onverwachte patronen, anomalieën, vermoedelijke bugs, ABox-inconsistenties. Niet over-engineeren; alleen daadwerkelijke observaties.

**§8 Pilot-sample-aanbeveling:** 8 paren conform Protocol v1.2 §6 (sample-grootte 8, gesigned-off bij T2-scoping). Spreiding-vereisten:

- Over alle aanwezige predicate-types (exact + close + broad + related; narrow indien aanwezig)
- Mix van cluster-representanten en cluster-volgers
- Verschillende evidence-niveau-bron-types
- Geen pre-pilot-uitkomst-verwachting expliciet (lees: Tech doet sample-keuze structureel, niet op basis van vermoede uitkomst)

**§9 Hand-off-checklist:**

- [ ] Pre-push disclosure-check Protocol 14 (vijf categorieën inclusief NEN-tekst >10 woorden)
- [ ] Geen patches/ontologie-wijzigingen toegepast
- [ ] Geen autonome commits (Steven commit handmatig)
- [ ] Rapport zelfstandig leesbaar voor masterchat
- [ ] §8 pilot-sample bevat IRI's + cluster-context per paar (geen alleen-IDs)

---

## §4. Wat NIET in deze fase

- Geen C1-C4-toetsing per paar — dat is pilot-fase (Stap 2) en hoofd-uitvoering (Stap 3)
- Geen patch-voorbereiding — Stap 4
- Geen masterchat-escalaties (tenzij scope-pauze door onverwacht structuur-issue conform sprint-protocollen)
- Geen pre-pilot-uitkomst-voorspelling — verboden door Protocol v1.2 §6

---

## §5. Scope-pauze-triggers

Pauzeer en escaleer naar masterchat indien:

- Totaal-aantal mappings >130 of <80 (significante afwijking van ~111-verwachting; mogelijke scope-mismatch)
- `narrowMatch`-paren aanwezig in ctrl:↔compl: (niet verwacht; vereist methode-overweging)
- D4.1-disclaimer ontdekt in CBW-Excel (impact op evidence-niveau-1-betrouwbaarheid)
- Bron-blocker die T2-uitvoering verhindert (bv. NEN-bron niet bereikbaar)
- ABox-anomalie (bv. zelfde paar met meerdere SKOS-predicates tegelijk; orphan-resources)

Format scope-pauze conform v1.2 §4 twee-zijdige analyse-format (Pro-X / Pro-Y / Tech-positie / Vraag).

---

## §6. Geschatte duur

T1-precedent voor pre-sprint-inventarisatie: ~1-1.5 uur Tech-werk. T2-inventarisatie is breder (~111 paren vs T1's 28 + bidirectional context) maar zelfde methodische omvang. Verwachting: ~1.5-2 uur.

Geen harde deadline. Kwaliteit boven snelheid.

---

*Einde instructie. Bij voltooiing: push rapport + wacht op masterchat-review. Geen verdere autonome actie.*
