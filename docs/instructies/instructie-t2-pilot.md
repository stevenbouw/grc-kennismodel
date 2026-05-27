# T2 Pilot — instructie voor Tech-subagent

**Sprint:** T2 (SKOS-kwaliteitsanalyse Fase 2 — bidirectional audit ctrl:↔compl:)
**Fase:** Stap 2 — pilot van 8 paren
**Auteur:** Masterchat
**Datum:** 27 mei 2026
**Modus:** Read-only beoordeling — geen patches, geen TTL-wijzigingen
**Autoritatief protocol:** `docs/skos-beoordelings-protocol-v1_2.md`
**Voorganger:** `output/reports/t2-pre-sprint-inventarisatie.md`

---

## §0. Context — wat is besloten bij masterchat-review

Pre-sprint-inventarisatie-rapport is door masterchat gereviewd. Drie besluiten:

**Besluit 1 — Scope:** **Optie C** — T2 = m10-only (118 paren). m14-AVG/GDPR (31 paren) wordt logische opvolger-sprint (T-nummer nog niet vastgesteld; Protocol v1.2 wordt eerst gevalideerd op één bron-context).

**Besluit 2 — Werkflow §7.1:** Tech-keuze B (geen aparte scope-pauze-md, rapport ís signaal) is conform protocol-intent. Bevestiging in instructie-stijl voor Protocol v1.3-overweging na T2.

**Besluit 3 — Pilot-sample:** 8 m10-paren geaccepteerd (combinatie §8.1 m10-paren + §8.3 alternatief).

Structurele bevinding inventarisatie die pilot-context bepaalt:

- **0 singletons in totale ctrl:↔compl:-cluster.** Alle 118 m10-paren zitten in cluster >1.
- Implicatie Protocol v1.2 §3.1 rij 1-3: doel-predicate `exactMatch` en `closeMatch` zijn structureel niet-toepasselijk in deze cluster (C2-failure)
- Mogelijke doel-predicates: `broadMatch`, `narrowMatch`, `relatedMatch`, of "verwijderen"
- **Dit is geen pre-pilot-uitkomst-voorspelling** (Protocol v1.2 §6 verbiedt dat); dit is een **structureel feit** uit inventarisatie

---

## §1. Doel pilot

Toepassing van Protocol v1.2 op 8 representatieve m10-paren. Output:

1. Per paar: D4.1-status + C1-C4-toets + doel-predicate (§3.1-tabel) + mutatie-richting + confidence
2. Cluster-discipline-toepassing geverifieerd in praktijk (Protocol v1.2 §3.3) — 3 pilot-paren zitten in zelfde cluster
3. Stop-conditie-monitoring (Protocol v1.2 §6)
4. Werkflow-leerpunten gemarkeerd voor §10 eindrapport (Protocol v1.2 §10, 7 categorieën)

**Doel is niet:**

- Patch-voorbereiding — dat is Stap 4 na masterchat-review
- Cluster-overerving op de overige 110 m10-paren — dat is Stap 3 hoofd-uitvoering
- Pre-pilot-uitkomst-voorspelling — verboden door Protocol v1.2 §6

**Modus:** read-only beoordeling. Geen wijzigingen aan `m10-nis2-ext.ttl`, geen test-applies, geen SHACL-runs op gewijzigde files.

---

## §2. Pilot-sample — 8 paren

### §2.1 — Tabel met volledige paar-context

| # | Paar-ID | Subject IRI | Object IRI | Huidige | Cluster-context | Module |
|---|---|---|---|---|---|---|
| 1 | T2-S01 | `ctrl:ISO27002_5_09` | `compl:NIS2_Art21_i` | `broadMatch` | object-cluster 32 (groot, mixed) | m10 |
| 2 | T2-S02 | `ctrl:ISO27002_5_28` | `compl:NIS2_Art21_b` | `closeMatch` | object-cluster 10 | m10 |
| 3 | T2-S03 | `ctrl:ISO27002_5_03` | `compl:NIS2_Art21_a` | `relatedMatch` | object-cluster 12 + subject-cluster 3 | m10 |
| 4 | T2-S04 | `ctrl:ISO27002_5_08` | `compl:NIS2_Art21_a` | `broadMatch` | object-cluster 12 + subject-cluster 2 | m10 |
| 5 | T2-S05 | `ctrl:ISO27002_5_05` | `compl:NIS2_Art21_a` | `relatedMatch` | object-cluster 12 + subject singleton | m10 |
| 6 | T2-S06-alt | `ctrl:ISO27002_8_27` | `compl:NIS2_Art21_e` | `broadMatch` | object-cluster 17 | m10 |
| 7 | T2-S07-alt | `ctrl:ISO27002_5_15` | `compl:NIS2_Art21_j` | `closeMatch` | object-cluster 9 + subject-cluster 2 | m10 |
| 8 | T2-S08-alt | `ctrl:ISO27002_5_30` | `compl:NIS2_Art21_c` | `relatedMatch` | object-cluster 8 + subject singleton | m10 |

### §2.2 — Cluster-discipline-aanleiding in pilot

**Drie pilot-paren zitten in zelfde object-cluster compl:NIS2_Art21_a (cluster-grootte 12):** T2-S03, T2-S04, T2-S05.

Inventarisatie §3.1 toont mix in deze cluster: 4× broadMatch + 4× closeMatch + 4× relatedMatch.

**Cluster-discipline-toets (Protocol v1.2 §3.3):**

- Beoordeel cluster-representant eerst (suggestie: T2-S03 vanwege middel-positie — niet meest extreme cluster-context). Bepaal cluster-niveau-doel-predicate.
- Toets vervolgens T2-S04 en T2-S05 op cluster-conformiteit. Indien individuele afwijking: motiveer expliciet vanuit NEN-tekst of evidence-niveau-1-bron.
- Documenteer in §3 van pilot-rapport: was cluster-discipline-overerving toepasselijk, of waren individuele uitzonderingen aantoonbaar?

Dit is **belangrijke validatie** van Protocol v1.2 §3.3 in praktijk. Werkflow-leerpunt categorie 5 (cluster-discipline-toepassings-ervaringen).

### §2.3 — Bron-evidence-status voor §8.3-alternatieven

Inventarisatie-rapport §8.1 specificeerde bron-evidence-status voor T2-S01-T2-S05. Voor §8.3-alternatieven (T2-S06-alt / T2-S07-alt / T2-S08-alt) moet evidence-niveau-1-status tijdens pilot worden vastgesteld via doorzoek op CBW-Mapping-UV-sheet en eventuele andere bronnen.

---

## §3. Toepassings-volgorde per paar

Voor elk paar, in onderstaande volgorde:

### §3.1 — Stap A: D4.1-vooraf-check

Conform Protocol v1.2 §2.0.

- Bron-evidence voor het paar identificeren (CBW-Mapping-UV / model-eigen / andere)
- Disclaimer-status: aanwezig / afwezig / niet-onderzocht
- Voor m10-paren: ENISA TIG-disclaimer (T1-bekend) is van toepassing op paren met ENISA-evidence; CBW-Mapping-UV erft deze (inventarisatie §5.1 #2). Registratie volstaat — geen herverificatie nodig.

### §3.2 — Stap B: C1-C4-toets

Conform Protocol v1.2 §2.1-2.4.

- **C1 definitionele overlap:** lees ISO 27002:2022 (lokaal in `/Users/stevenbouwmeester/grc-sources-licensed/`) en NIS2 Art21-letter-tekst (in `sources/eu-recht/EU-nis2-richtlijn.pdf` of via UV-decompositie in CBW-Mapping-UV). Bepaal: bilateraal / partieel / gefaald.
- **C2 cardinaliteit cluster:** uit inventarisatie §3.1/3.2 bekend. Vermeld cluster-grootte expliciet.
- **C3 inclusie-richting:** bilateraal / A⊂B / B⊂A / geen. NEN-bron-lezing verplicht voor onderbouwing.
- **C4 bron-evidence:** niveau 1-4 + bron-verwijzing.

**NEN-discipline (Protocol v1.2 §8):** parafrase + clausule-verwijzing in pilot-rapport, geen verbatim NEN-tekst >10 woorden.

### §3.3 — Stap C: Doel-predicate uit §3.1-tabel

Hanteer Protocol v1.2 §3.1 predicate-doel-tabel. Geef voor elk paar expliciet aan welke rij van toepassing is.

### §3.4 — Stap D: Mutatie-richting via §3.2-ordening

Bepaal mutatie-richting via Protocol v1.2 §3.2:

- Doel = huidige → **behoud**
- Doel sterker dan huidige → **upgrade**
- Doel zwakker dan huidige → **downgrade**
- broadMatch ↔ narrowMatch → **richtings-correctie**
- Doel = "verwijderen" → **verwijderen**
- Onzekerheid → **twijfel-escaleer** conform Protocol v1.2 §4

### §3.5 — Stap E: Confidence-classificatie

Hoog / middel / laag conform Protocol v1.2 §5.

---

## §4. Output-formaat — pilot-rapport

**Bestandsnaam:** `output/reports/t2-pilot-rapport.md` (of conventie-passende lokatie)

**Structuur:**

```
# T2 Pilot-rapport — 8 paren m10

## §1. Samenvatting (kerncijfers + mutatie-richting-distributie + cluster-discipline-uitkomst)
## §2. Methode (Protocol v1.2-toepassing + cluster-discipline-aanpak)
## §3. Cluster-discipline-toepassing in compl:NIS2_Art21_a-cluster (T2-S03+S04+S05)
## §4. Paar-voor-paar-beoordeling (T2-S01 t/m T2-S08-alt)
## §5. Stop-conditie-monitoring
## §6. Werkflow-leerpunten (alle 7 categorieën Protocol v1.2 §10)
## §7. Aanbeveling voor Stap 3 hoofd-uitvoering
## §8. Hand-off-checklist
```

### §4.1 — Output-formaat per paar (Protocol v1.2 §5)

Per paar in §4 van pilot-rapport: volledige tabel zoals gespecificeerd in Protocol v1.2 §5 — alle 13 velden ingevuld.

```
| Veld | T2-Sxx |
|---|---|
| Paar-ID | T2-Sxx |
| Subject IRI | ... |
| Object IRI | ... |
| Huidige predicate | ... |
| Cluster-context | ... |
| D4.1-disclaimer-check | aanwezig / afwezig + bron + 1 zin |
| C1 (definitioneel) | ✓/✗ + 1-2 zin parafrase NEN-clausule (geen verbatim >10 woorden) |
| C2 (cardinaliteit cluster) | 1↔1 / veel↔1 / 1↔veel + cluster-grootte |
| C3 (inclusie) | bilateraal / A⊂B / B⊂A / geen |
| C4 (bron-evidence) | niveau 1-4 + bron-verwijzing |
| Doel-predicate | uit §3.1-tabel + rij-verwijzing |
| Mutatie-richting | upgrade / downgrade / richtings-correctie / behoud / verwijderen / twijfel |
| Confidence | hoog / middel / laag |
| Patch-vereist | ja / nee |
```

Per paar plus 2-4 zin Tech-toelichting bij niet-triviale uitkomst (cluster-overerving, evidence-zwakte, twijfelgevallen).

### §4.2 — Aanbeveling voor Stap 3 (§7 pilot-rapport)

Tech adviseert masterchat over Stap 3 hoofd-uitvoering:

- Cluster-discipline-aanpak voor 110 resterende m10-paren (vermoedelijk cluster-representant + overerving)
- Geschatte duur Stap 3
- Eventuele protocol-aanpassings-suggesties op basis van pilot-ervaring
- Eventuele scope-aanbevelingen (bv. clusters die individuele aandacht vragen)

---

## §5. Stop-condities (Protocol v1.2 §6)

Pauzeer en rapporteer aan masterchat indien tijdens pilot:

| # | Conditie | Wat te doen |
|---|---|---|
| 1 | Confidence "laag" op ≥3 van 8 paren | Pauze; protocol-criteria-bijstelling nodig |
| 2 | Evidence-niveau 4 op ≥3 van 8 paren | Pauze; bron-discipline-probleem |
| 3 | D4.1-disclaimer-status "niet-onderzocht" op ≥3 paren | Pauze; evidence-pre-stap onvoldoende |
| 4 | Onverwacht-patroon — uitkomst sterk wijkt af van scope-aanname | Pauze; masterchat-input nodig |

**Scope-pauze-format:** twee-zijdige analyse conform Protocol v1.2 §4 (Pro-X / Pro-Y / Tech-positie / Vraag). In pilot-rapport zelf rapporteren — geen aparte scope-pauze-md (Tech-keuze §7.1 inventarisatie bevestigd door masterchat).

**Specifieke aandacht:**

- **Stop-conditie 4** is interpretatief. "Onverwacht-patroon" betekent niet "veel downgrades" (dat is structureel verwacht door 0-singleton-feit). Wel een trigger als: bv. >2 verwijder-doelen, bv. alle 3 paren in compl:NIS2_Art21_a-cluster krijgen verschillende doel-predicate (cluster-discipline-failure), bv. >2 twijfel-escalaties.

---

## §6. Werkflow-leerpunten — markeren tijdens pilot (Protocol v1.2 §10)

Markeer voortdurend, niet alleen achteraf. Zeven categorieën:

1. **Tooling-gaten** — welke automation/scripts ontbraken voor pilot?
2. **Bron-toegankelijkheid** — welke NEN-clausules waren niet goed vindbaar?
3. **Protocol-criteria-onduidelijkheden** — welke C1-C4-formulering bleek ambigu in praktijk?
4. **Werkverdeling-momenten** — waar Tech-autonomie of escalatie aan masterchat-discussie waard?
5. **Cluster-discipline-toepassings-ervaringen** — werkte cluster-overerving in praktijk?
6. **D4.1-pre-stap-praktijk** — hoeveel tijd kostte disclaimer-detectie? Was T1-bekend-status voldoende?
7. **Upgrade-detectie-praktijk** (NIEUW v1.2) — kwamen er upgrade-kandidaten boven? Was Protocol v1.2 §3.1-tabel symmetrisch toepasbaar in praktijk?

Categorie 7 is **eerste testcase** voor v1.2's bidirectional uitbreiding. Extra aandacht.

---

## §7. Hand-off-checklist

- [ ] Pre-push disclosure-check Protocol 14 (vijf categorieën inclusief NEN-tekst >10 woorden)
- [ ] Geen patches / ontologie-wijzigingen toegepast (read-only beoordeling)
- [ ] Geen autonome commits (Steven commit handmatig)
- [ ] Alle 8 paren beoordeeld met volledige Protocol v1.2 §5-output
- [ ] Cluster-discipline §3 expliciet gerapporteerd (compl:NIS2_Art21_a-cluster)
- [ ] Werkflow-leerpunten §6 met alle 7 categorieën
- [ ] Aanbeveling Stap 3 §7 specifiek + actionable
- [ ] Rapport zelfstandig leesbaar voor masterchat

---

## §8. Wat NIET in deze fase

- Geen patch-voorbereiding — Stap 4
- Geen cluster-overerving op overige 110 m10-paren — Stap 3
- Geen TTL-wijzigingen / SHACL-runs op gemuteerde files
- Geen m14-paren — buiten T2-scope per Optie C
- Geen pre-pilot-uitkomst-voorspelling — Protocol v1.2 §6 verbiedt
- Geen brain-vault-updates — gebeurt in Brein-cyclus na T2-afsluiting

---

## §9. Geschatte duur

T1-precedent (pilot van 5 paren): ~1.5 uur Tech-werk. T2-pilot is 8 paren bidirectional + cluster-discipline-validatie. Verwachting: **~2-3 uur**.

Geen harde deadline. Kwaliteit + correcte protocol-toepassing boven snelheid.

---

## §10. Bij voltooiing

Tech pushed pilot-rapport. Steven commit handmatig. Masterchat reviewt:

- Cluster-discipline-toepassing valide? Lessons voor Stap 3?
- Stop-condities geraakt? Protocol-aanpassing nodig vóór Stap 3?
- Werkflow-leerpunten reden voor instructie-aanpassing Stap 3?
- Aanbeveling Stap 3 acceptabel?

Na masterchat-review: **Stap 3 hoofd-uitvoering** wordt geïnstrueerd voor de overige 110 m10-paren met cluster-discipline-overerving.

---

*Einde T2 Pilot-instructie. Modus: read-only beoordeling. Geen verdere autonome actie na rapport-push.*
