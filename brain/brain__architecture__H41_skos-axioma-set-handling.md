---
type: architecture
id: H41
title: H41 — SKOS-axioma-set-handling onder OWL-RL (S46-symmetrie, S47-transitiviteit niet geïnferreerd)
status: parked
date: 2026-05-28
related:
  - owl-rl-reasoning
  - canonical-metrics
  - skos-beoordelings-protocol
  - T1_skos-kwaliteitsanalyse-fase-1
  - T2-skos-bidirectional-audit-m10
  - T3-skos-bidirectional-audit-m14
  - D04_skos-cross-framework
sources:
  - t1-eindrapport-v4_6_1
  - patch-rapport-v4_6_1
  - patch-rapport-v4_6_2
  - patch-rapport-v4_6_3
  - projectinstructie-v1_10
chat-sources: []
confidence: high
---

# H41 — SKOS-axioma-set-handling onder OWL-RL

## Status

**Parked (nieuw geregistreerd iteratie 14)** — eerste registratie 27 mei 2026 na T2-sprint. Trigger: substantiële SKOS-mapping-uitbreiding waar transitiviteit of symmetrie auditief relevant wordt, of overstap-besluit naar reasoner-configuratie die SKOS-axiomas wel laadt.

T1 markeerde dit reeds als werkflow-leerpunt (zonder H-registratie); T2 leverde productie-schaal empirisch bewijs dat H-registratie rechtvaardigt. Formeel vastgesteld als parked H-item per masterchat-besluit bij T2-afsluiting (projectinstructie v1.10).

## Wat het is

`owlrl`-package laadt in de canonieke project-configuratie (`axiomatic_triples=False`, `datatype_axioms=False`) **geen SKOS-axiomas**. Concreet niet geladen:

| Axioma | Inhoud | Effect |
|---|---|---|
| skos:S46 | `skos:exactMatch a owl:SymmetricProperty` | Symmetrische inverse-triple wordt **niet** geïnferreerd. Als `A skos:exactMatch B` is geassserteerd, ontstaat geen impliciete `B skos:exactMatch A`. |
| skos:S47 | `skos:exactMatch a owl:TransitiveProperty` | Transitiviteits-keten wordt **niet** geïnferreerd. Als `A skos:exactMatch B` en `B skos:exactMatch C`, ontstaat geen impliciete `A skos:exactMatch C`. |
| (vergelijkbaar) | skos:closeMatch + skos:relatedMatch eigenschappen (symmetrie) | Niet geïnferreerd onder huidige configuratie |

Effect: SKOS-mappings worden behandeld als asymmetrische, niet-transitieve triples. Audit van SKOS-mapping-correctheid blijft dus per-paar werkbaar, maar SKOS-vocabulaire-eigenschappen die in de formele SKOS-specificatie zijn vastgelegd (W3C SKOS Reference §S46-S47) krijgen geen formele inferentie-status in de canonical metrics + SHACL-validatie van dit project.

## Empirisch bewijs uit T1 + T2 + T3

| Sprint | SKOS-mutaties | Triples-Δ pre-inferentie | Triples-Δ post-OWL-RL | Bron |
|---|---:|---:|---:|---|
| T1 (v4.6.1) | 28 (`exactMatch` → `broadMatch`) | 0 | 0 | patch-rapport-v4_6_1 §4-5 |
| T2 (v4.6.2) | 65 (32× close→broad + 33× related→broad) | 0 | 0 | patch-rapport-v4_6_2 §0.1 + §4.1 |
| **T3 (v4.6.3)** | **2 (broad→related; cross-category)** | **0** | **0** | **patch-rapport-v4_6_3 §0.1 + §4.1** |

T2 levert sterkste bewijs (per patch-rapport v4.6.2 §4.1):

> *"Post-OWL-RL-inferentie is eveneens stabiel omdat owlrl in deze configuratie geen SKOS-axiomas laadt (skos:S46/S47 e.d. niet geactiveerd; bekende beperking gedocumenteerd in v4.6.1-rapport §5.2). Predicate-naamverandering raakt geen RDFS/OWL-inferentie-pad."*

Bij 65 predicate-substituties — waarvan 32 closeMatch ↔ broadMatch (symmetrie-relevant indien S46-equivalent voor closeMatch wel geladen zou zijn) — blijft post-OWL-RL Δ exact 0. Bevestigt empirisch dat SKOS-axiomas niet geactiveerd zijn in de huidige reasoner-configuratie.

**T3-bevestiging (informatief, status ongewijzigd):** derde sprint-bewijs op kleinere schaal (2 mutaties), maar nu in **cross-category-context** (control ↔ legal-obligation, compl→ctrl-richting in m14) — eerste cross-category-bewijs voor H41. broadMatch→relatedMatch-substituties (waarbij beide predicates symmetrisch zijn onder W3C SKOS-Reference indien S46-equivalenten geladen zouden zijn) leveren Δ post-OWL-RL = 0. Confirmeert H41 over T1+T2+T3 = drie sprint-context-bewijzen (exactMatch-omzetting, close/related/broad bidirectional, broad/related cross-category).

## Waarom dit een open vraag is

| Aspect | Risico onder huidige config | Risico bij activering SKOS-axiomas |
|---|---|---|
| Audit-rigour SKOS-mappings | Asymmetrische modellering vereist expliciete inverse-triples voor bilateraal gebruik (T1: alle 28 ctrl→compl mappings zonder inverse compl→ctrl) | Inverse-triples automatisch; minder ABox-volume maar wel impact op canonical metrics |
| Cross-namespace-redenering | SKOS-mapping-keten A→B→C zonder transitieve closure | Transitiviteits-closure kan onbedoelde implicaties opleveren bij cross-framework-mappings (bv. NIST → ISO → BIO transitief) |
| Performance (post-OWL-RL) | Huidige 44.907 post-inferentie-triples; T1+T2 stabiel | SKOS-axioma-activering vergroot triple-totaal; impact op grc-explorer + dashboard-export niet ingeschat |
| H38 (HermiT-equivalentie) | Geen SKOS-axiomas wijkt af van strikte W3C SKOS-Reference | HermiT laadt SKOS-axiomas mogelijk wel — verschil tussen OWL-RL- en HermiT-uitkomst op SKOS-pad zou H38-relevantie vergroten |
| Externe SKOS-audit | DCAT-AP-publicatie of externe linked-data-validatie zou symmetrie + transitiviteit kunnen verwachten | Conformer aan W3C SKOS-Reference |
| Modelleringsdiscipline ctrl:↔compl: | Alle T1+T2 mappings zijn ctrl: → compl:; geen compl: → ctrl: m.u.v. m14 (waar modelleringsconventie omgekeerd is) | Symmetrie-activering zou m10 + m14 inverses creëren; cross-module-effect onbekend |

Niet vervangen op basis van "conformer is beter" — eerst evalueren wanneer concrete trigger zich voordoet (zie hieronder).

## Trigger-criterium

| Trigger | Wanneer evaluatie starten |
|---|---|
| Substantiële SKOS-mapping-uitbreiding | Bv. m14-sprint (31 paren in andere modelleringsconventie) of cross-framework-uitbreiding waar symmetrie/transitiviteit auditief relevant wordt |
| Externe SKOS-audit aangekondigd | DCAT-AP-publicatie, W3C linked-data-conformiteit, externe audit op SKOS-rigour |
| H38 (HermiT-equivalentie) toont SKOS-pad-delta | Bij HermiT-run met SKOS-axiomas wel geladen — significant delta motiveert reasoner-configuratie-herziening |
| Spoor B-overgang | Operationele dashboard-vraag waar transitieve mapping-keten naar evidence-uitkomst leidt |
| MCP-toolchain-evaluatie (H37) | Open-ontologies-MCP met Oxigraph + tableaux-reasoner laadt mogelijk wel SKOS-axiomas — vergelijking met huidige stack relevant |

## Aanpak bij activering (toekomst, niet nu)

1. **Configuratie-aanpassing** — `owlrl`-instelling `axiomatic_triples=True` of expliciet SKOS-axioma-graph laden vóór reasoning
2. **Canonical-metrics-impact-meting** — vergelijk post-OWL-RL triples met en zonder SKOS-axiomas; documenteer Δ per cluster
3. **SHACL-impact-meting** — combined-mode SHACL met geactiveerde SKOS-axiomas vs huidige 290 false-positives baseline; uitsplitsen welke shapes raakvlak hebben met SKOS-inverse-triples
4. **Cross-namespace-transitiviteits-check** — query op transitiviteits-ketens die nu impliciet ontstaan (bv. CSF → ISO → BIO via skos:exactMatch + skos:broadMatch); evalueer of dit gewenste of ongewenste implicaties oplevert
5. **D-decision-overweging** — eventueel nieuwe D-decision over reasoner-configuratie-keuze (huidige is impliciet via canonical-metrics-discipline)

## Relatie tot andere H-items

| H | Relatie |
|---|---|
| [[brain__architecture__H37_open-ontologies-mcp]] | Alternatieve reasoner-stack (Oxigraph + tableaux) — kandidaat-trigger voor H41-evaluatie indien Oxigraph SKOS-axiomas wel laadt |
| [[brain__architecture__H38_owlrl-vs-hermit-equivalentie]] | HermiT-run zou SKOS-axioma-pad-delta zichtbaar maken; H38-evaluatie zou H41-trigger kunnen activeren |
| [[brain__architecture__H39_shacl-run2-290-false-positives-uitsplitsing]] | SHACL-uitsplitsing zou SKOS-axioma-activering moeten herhalen om volledige false-positive-set te begrijpen |

## Confidence: high

T2-empirisch bewijs (32 closeMatch ↔ broadMatch-mutaties zonder Δ post-OWL-RL) bewijst onomstotelijk dat SKOS-axiomas niet geactiveerd zijn in huidige configuratie. Geen interpretatie-onzekerheid over de feitelijke staat van de reasoner-configuratie. Confidence-onzekerheid betreft uitsluitend toekomstige beslissingen (wel/niet activeren), niet de feitelijke vaststelling.

## Bron-traceerbaarheid

- T1-eindrapport v4.6.1 §5.2 — eerste expliciete vermelding van SKOS-axioma-set-handling als T1-werkflow-leerpunt
- Patch-rapport v4.6.1 §5.2 — markering "skos:exactMatch is owl:SymmetricProperty (skos:S46) wordt niet geïnferreerd"
- Patch-rapport v4.6.2 §4.1 — productie-schaal bevestiging op 65 SKOS-mutaties
- Patch-rapport v4.6.3 §4.1 — derde sprint-bewijs, eerste cross-category-context (2 mutaties broad→related in compl→ctrl-richting)
- Projectinstructie v1.10 — formele H41-declaratie + parked-status

## Hangt samen met

- [[brain__concepts__owl-rl-reasoning]] — waarom OWL RL het minimum is in huidige toolchain
- [[brain__concepts__canonical-metrics]] — meet-discipline die de Δ-stabiliteit zichtbaar maakt
- [[brain__concepts__skos-beoordelings-protocol]] — methode-concept waarbinnen SKOS-vocabulaire wordt toegepast (Protocol v1.3 §12 noemt H41-kandidaat-status expliciet)
- [[brain__decisions__D04_skos-cross-framework]] — D4 vereist SKOS-modellering maar specificeert geen reasoner-configuratie voor SKOS-axiomas
- [[brain__sprints__T1_skos-kwaliteitsanalyse-fase-1]] — eerste markering (zonder registratie)
- [[brain__sprints__T2-skos-bidirectional-audit-m10]] — productie-schaal bewijs (T2)
- [[brain__sprints__T3-skos-bidirectional-audit-m14]] — derde sprint-bewijs in cross-category-context (informatief; status ongewijzigd)

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-26 | (niet geregistreerd) | T1-werkflow-leerpunt — kandidaat-overweging in H36-bestand vermeld, expliciet **NIET** als nieuw H-item geregistreerd; trigger ontbrak |
| 2026-05-27 | parked | Nieuw geregistreerd na T2-sprint; trigger gerechtvaardigd door productie-schaal bewijs (65 mutaties, Δ post-OWL-RL = 0); masterchat-besluit per projectinstructie v1.10 |
| 2026-05-28 | parked (T3-bevestiging informatief) | Derde sprint-bewijs op cross-category-context (2 mutaties broad→related compl→ctrl in m14); Δ post-OWL-RL = 0 bevestigd over drie sprint-contexten; status ongewijzigd (geen masterchat-besluit tot status-revisie of activering) |

— Einde H41.
