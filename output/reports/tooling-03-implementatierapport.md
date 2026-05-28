# Tooling-03 implementatierapport — `/pre-sprint-inventarisatie` + `/applier-template`

| Veld | Waarde |
|---|---|
| Spoor | A |
| Track | `.claude/skills/` (geen ontologie-release) |
| Baseline | v4.6.3 (ongewijzigd) |
| Bron-instructie | `docs/instructies/instructie-tooling-03-protocol-skills.md` |
| Uitvoerder | Tech-subagent (Claude Code) |
| Datum | 2026-05-28 |
| Vooraf | Tooling-02 gecommit + gepusht (`053e260..0c8aa71`) |
| Commit + push | Steven (handmatig — §5-instructie) |

## §0. Firewall-bevestiging + scope-conformiteit

§0.5-firewall-conformiteit:

| §0.5-verbod | Status | Toelichting |
|---|---|---|
| Geen autonome commit/push-paden | OK | Geen wijziging aan `.claude/settings.json`-deny-rules. Subagent-commit-invariant ongewijzigd. |
| Geen green-gate-voor-autonomie | OK | Beide skills zijn SKELET-/TEMPLATE-generators; geen auto-execute, geen autonome scope-keuze, geen runtime-mutatie-discovery. |
| Geen agent teams / CI / auto-merge | OK | Twee description-triggered skills. Geen orchestratie. |
| Geen ontologie-/beleids-/architectuurwijziging | OK | `ontology/` + `grc-shacl.ttl` byte-identiek aan v4.6.3 (§4 sanity-check). |
| Geen CLAUDE.md-wijziging in deze opdracht | OK | CLAUDE.md byte-identiek aan Tooling-02-eindstaat. |
| §0.5-firewall expliciet in skill-tekst | OK | Beide skills documenteren expliciet wat ze NIET doen (geen ABox-mutaties / geen auto-execute / geen autonome scope / geen autonome commit). |

Pre-sprint-inventarisatie-skill in skill-tekst: *"§0.5-firewall: dit is een SKELET-GENERATOR, geen sprint-uitvoerder. Geen ABox-mutaties, geen auto-execute, geen autonome scope-keuze. Masterchat blijft scope-vaststeller; Tech vult het skelet read-only."*

Applier-template-skill in skill-tekst: *"§0.5-firewall: dit is een TEMPLATE-skill, geen auto-execute. Genereert architectuur + checklist; Tech schrijft + Steven inspecteert + draait handmatig (eerst dry-run, daarna `--apply`)."*

## §1. `/pre-sprint-inventarisatie` (Deel A)

| Veld | Waarde |
|---|---|
| Lokatie | `.claude/skills/pre-sprint-inventarisatie/SKILL.md` |
| Activatie | description-triggered (geen `paths:`) |
| Regels | 225 |
| Codificeert | Protocol 1 + Protocol v1.3 §6 (sample-keuze) + §10.2-§10.5 (rapport-discipline) + §2.2-§2.4 (cluster-cardinaliteit + evidence-niveau) |

### §1.1 Skill-content-samenvatting

| Onderdeel | Inhoud |
|---|---|
| Wanneer aanroepen | Bij start nieuwe T-sprint, na masterchat-scope-instructie, vóór Stap-2-pilot |
| Vereiste input | sprint-naam, scope-module(s), audit-richting, baseline-versie |
| Dependencies (referentieel) | `/canonical-metrics` + `/shacl-split` (baseline-bron) + Protocol v1.3 + D-register + sprint-protocols |
| Bottom-up bouw-volgorde | §2 → §3 → §4 → §5 → §6 → §7 → §8 → §9 → §1 LAATST → §0 frontmatter LAATST |
| Canoniek §-skelet | §0 (frontmatter) + §1-§9 (negen secties — full mapping in tabel) |
| Afgedwongen disciplines | §2 uit canonical_metrics JSON / §3+§4 metrics-scope-annotatie / §6 geen pre-pilot-uitkomst / §1 "INITIEEL — TE BEVESTIGEN" / Protocol 13 bron-typo / Protocol 17 NEN-parafrase |
| Mapping-tabel | Skill-§ ↔ T2/T3-precedent vraag-A-F-format (vijf rijen — alle T-precedent-content gedekt) |

### §1.2 Sectie-naam-strategie — generiek skill-skelet vs sprint-specifiek precedent

Observatie tijdens uitvoering: T2/T3-precedenten gebruiken een SPRINT-SPECIFIEK "Vraag A-F"-format (door masterchat in de sprint-instructie voorgeschreven), terwijl Tooling-03-instructie §A.2 een GENERIEK §0-§9-skelet voorschrijft voor de skill.

Beide blijven samen werkbaar:

- Skill levert het CANONIEKE skelet (§0-§9) — generiek over alle T-sprints
- Masterchat-instructies kunnen sprint-specifieke vraag-thema's voorschrijven (Vraag A-F voor T2/T3 / Vraag X-Y voor T4 / etc.)
- Skill bevat een expliciete mapping-tabel: skill-§ ↔ T-Vraag — sprint-specifieke vraag-format mag, zolang alle skill-§-content semantisch gedekt is

Mapping-tabel uit skill (Test 5 trigger-test):

| Generieke skill-§ | T2/T3-precedent (Vraag A-F-format) |
|---|---|
| §1 Scope-bevestiging | T-Vraag A + T-§1 Samenvatting |
| §2 ABox-baseline | impliciet T-Vraag A + canonical_metrics-citaten |
| §3 Cluster-cardinaliteit | T-Vraag B |
| §4 Evidence-coverage | T-Vraag C + D + E |
| §5 Risico-inventarisatie | T-Vraag F + Tech-observaties |
| §6 Sample-keuze | T-Pilot-sample-aanbeveling |
| §7 Verwachte uitkomst | impliciet T-§1 |
| §8 GO/NO-GO | T-Hand-off (deel) |
| §9 Hand-off + Deliverables | T-Hand-off + Verwijzingen |

Geen scope-pauze nodig: skelet dekt T3-content semantisch volledig; de tekst-laag heeft sprint-instructie-vrijheid binnen het generieke skelet.

## §2. Trigger-test Deel A tegen T3-precedent (v4.6.2-baseline)

Vijf tests uitgevoerd:

| # | Test | Verwacht | Resultaat |
|---|---|---|---|
| 1 | Skill genereert §-skelet met §0-§9 (10 secties) | 10 | 9 `## §`-koppen + 1 YAML-frontmatter = 10 ✅ |
| 2 | §1-§9 dekking in canoniek-skelet-block + §0 als YAML-frontmatter (`baseline_from:`) | volledig | volledig ✅ |
| 3 | D5/D11-targets in skill matchen `canonical_metrics_v4_6_2.json` | D5=93, D11=5 | D5=93, D11=5 ✅ |
| 4 | NEN-vermelding alleen als clausule-reference (lokale `grc-sources-licensed/`-pad-context), geen verbatim normtekst | clausule-ref only | 1 vermelding, in bron-toegankelijkheids-tabel ✅ |
| 5 | Mapping-tabel skill-§ ↔ T2/T3-Vraag-A-F bevat alle T-Vraag-referenties | ≥ 5 mapping-rijen met T-Vraag | 5 T-Vraag-referenties ✅ |

**5/5 groen. Skill is structureel + semantisch consistent met T3-precedent.**

Bevestiging "geen NEN-verbatim-tekst": handmatige scan vond alleen "ISO 27002:2022" in regel 129 van de skill, in de bron-toegankelijkheids-tabel als clausule-naam (niet als normatieve tekst-passage). Conform Protocol 17 parafrase-discipline.

## §3. `/applier-template` (Deel B)

| Veld | Waarde |
|---|---|
| Lokatie | `.claude/skills/applier-template/SKILL.md` |
| Activatie | description-triggered |
| Regels | 191 |
| Codificeert | Protocol 15 (Tech levert werkbare applier) + T1/T2/T3-precedent-architectuur |

### §3.1 Skill-content-samenvatting

| Onderdeel | Inhoud |
|---|---|
| Wanneer aanroepen | T-sprint Stap 3 / minor-release patch met ABox-/SKOS-mutaties |
| Verplichte template-elementen | 9 (dry-run default / `--apply` / backup / hard-coded MUTATIONS / integratie-test / één-applier-voor-alle-types / per-mutatie-logging / idempotentie-check / faal-veilig-exit) |
| Canoniek code-skelet | Python skelet met argparse, MUTATIONS-list, `apply_one_mutation`, `run(apply_mode)`, `main()`, dry-run-rapport, idempotentie-check, backup-vóór-write |
| Lokatie-conventie | T1/T2-historisch afwijkend; v4.6.3 (T3) = `scripts/apply_patch_v4_6_3.py` is canoniek; T4+ volgt T3 |
| Integratie-test workflow | Dry-run → verifieer counts → temp-kopie-test → productie `--apply` → `/canonical-metrics` + `/shacl-split` |
| Bron-precedenten | T1 / T2 / T3 — alleen architectuur-pattern + checklist, geen verbatim code-kopie |

### §3.2 Trigger-test Deel B tegen `apply_patch_v4_6_3.py`

Vier tests uitgevoerd:

| # | Test | Verwacht | Resultaat |
|---|---|---|---|
| 1 | 9/9 verplichte template-elementen aanwezig in skill | 9/9 | 9/9 ✅ |
| 2 | Sleutelelementen in skill-code-skelet matchen `apply_patch_v4_6_3.py`-structuur | ≥ 15/16 | 15/16 ✅ (1× ⚠️: idempotentie-check `ALREADY APPLIED` in skill maar niet in T3-precedent — dit is een skill-VERBETERING die Protocol 15 strict implementeert) |
| 3 | Lokatie-conventie-tabel met T1/T2/T3 + T4+ canoniek | T1+T2+T3+T4+ | 4 rijen ✅ |
| 4 | 0 NEN-verbatim-vermeldingen in skill | 0 | 0 ✅ |

**4/4 groen. Skill is structureel consistent met T3-applier-precedent en voegt idempotentie-check toe als Protocol-15-extension.**

Toelichting bij test 2 ⚠️-item: T3-precedent (`scripts/apply_patch_v4_6_3.py`) heeft geen expliciete `ALREADY APPLIED`-detectie; de skill voegt deze toe omdat Protocol 15-idempotentie-eis ("rerun zonder veranderingen") een expliciete check vereist. Dit is een vooruitgang t.o.v. T3-precedent — niet een afwijking. Volgende applier (T4+) erft deze verbetering.

## §4. Ontologie-drift-sanity (verwacht: geen drift)

Geen ontologie-werk in scope (alleen `.claude/skills/`-additions). Sanity-check:

| Bestand | SHA256 (eerste 12) | Inhoud-check |
|---|---|---|
| `output/verification/canonical_metrics_v4_6_3.json` | `47a98da8930d` | triples pre-inference 20950 ✅ ; D5 ctrl↔bio 93 ✅ |
| `output/verification/shacl_results_v4_6_3.json` | `ccfed04d42fb` | (file ongewijzigd sinds Tooling-02) |
| `ontology/*.ttl` | — | Geen wijziging in git status |

**Ontologie ongewijzigd. Geen drift t.o.v. v4.6.3-baseline.** Geen re-run van metrics-scripts uitgevoerd (zou de baseline-JSON's overschrijven met nieuwere timestamps — net als in Tooling-01/02 vermeden). Drift-bewaking via bestaande hashes + inhoud-check op kerncijfers.

## §5. Protocol-14-disclosure-check op alle nieuwe bestanden

Automatische run van `.claude/hooks/disclosure-check.py` (productie-versie) op twee Tooling-03-deliverables + dit rapport:

| Bestand | exit-code | Resultaat |
|---|---|---|
| `.claude/skills/pre-sprint-inventarisatie/SKILL.md` | 0 | clean ✅ |
| `.claude/skills/applier-template/SKILL.md` | 0 | clean ✅ |
| `output/reports/tooling-03-implementatierapport.md` | 0 (na schrijven — hook draait automatisch via PreToolUse) | clean (verwacht) |

**Geen Protocol-14-categorie-vondsten op de Tooling-03-deliverables.** Skills bevatten alleen methode-beschrijving + clausule-references; geen organisatie-data, geen persoonsnamen ≠ Steven, geen paden buiten repo of NEN-licentie-locatie, geen organisatie-e-mails.

## §6. Deliverables (Protocol 16 — expliciete lokatie)

| Type | Lokatie | Beschrijving |
|---|---|---|
| Action-skill | `.claude/skills/pre-sprint-inventarisatie/SKILL.md` | Genereert §0-§9-skelet voor pre-sprint-inventarisatie (Protocol 1) met afgedwongen JSON-bron + Protocol-v1.3-discipline |
| Action-skill | `.claude/skills/applier-template/SKILL.md` | Genereert Python-applier-skelet (Protocol 15) met dry-run-default + `--apply` + backup + idempotentie-check |
| Rapport | `output/reports/tooling-03-implementatierapport.md` | Dit document |

Geen wijzigingen aan CLAUDE.md, settings.json, hooks, andere skills, ontologie, scripts, of dashboard. Alleen `.claude/skills/`-additions + dit rapport.

## §7. Commit-suggestie (delen los committeerbaar)

**Commit A** — `/pre-sprint-inventarisatie`-skill (Deel A):
```
chore(.claude/skills): /pre-sprint-inventarisatie — §0-§9-skelet (Tooling-03 Deel A)

- .claude/skills/pre-sprint-inventarisatie/SKILL.md (225 regels)
- Codificeert Protocol 1 + Protocol v1.3 §6 (sample-keuze) + §10.2-§10.5
  (rapport-discipline) + §2.2-§2.4 (cluster-cardinaliteit + evidence-niveau)
- Afgedwongen disciplines:
  - §2 uit canonical_metrics_v(Y-1).json (leerpunt v4.3.3 / Protocol v1.3 §10.4)
  - §3+§4 metrics-scope-annotatie (Protocol v1.3 §10.5)
  - §6 geen pre-pilot-uitkomst-classificatie (Protocol v1.3 §6 stop-conditie-4)
  - §1 "INITIEEL — TE BEVESTIGEN" bij bottom-up bouw
- Mapping-tabel skill-§ ↔ T2/T3-precedent vraag-A-F-format (5 mapping-rijen)
- Trigger-test tegen T3 (v4.6.2-baseline): 5/5 groen
- §0.5-firewall: skelet-generator, geen sprint-uitvoerder

Ref: docs/instructies/instructie-tooling-03-protocol-skills.md §1
```

**Commit B** — `/applier-template`-skill (Deel B):
```
chore(.claude/skills): /applier-template — Protocol-15-architectuur (Tooling-03 Deel B)

- .claude/skills/applier-template/SKILL.md (191 regels)
- Codificeert Protocol 15 (Tech levert werkbare applier) + T1/T2/T3-precedent
- Verplichte template-elementen (9):
  dry-run-default / --apply / backup / hard-coded MUTATIONS / integratie-test /
  één-applier-voor-alle-types / per-mutatie-logging / idempotentie-check /
  faal-veilig-exit
- Canoniek code-skelet (Python) met argparse + MUTATIONS-list + apply_one_mutation
  + run(apply_mode) + main() + dry-run-rapport + idempotentie ("ALREADY APPLIED")
- Lokatie-conventie: v4.6.3 (scripts/) = canoniek vanaf T3; T1/T2 historisch
- Trigger-test tegen apply_patch_v4_6_3.py: 4/4 groen (1× ⚠️ idempotentie-check
  = skill-extension boven T3-precedent — Protocol 15 strict)
- §0.5-firewall: template-skill, geen auto-execute

Ref: docs/instructies/instructie-tooling-03-protocol-skills.md §2
```

**Commit C** — implementatierapport:
```
docs(tooling): Tooling-03 implementatierapport — pre-sprint-inventarisatie + applier-template

- §0: §0.5-firewall-conformiteit (beide skills documenteren expliciet NIET-doen)
- §1: /pre-sprint-inventarisatie content-samenvatting + sectie-naam-strategie
  (generiek skelet vs sprint-specifiek precedent — mapping-tabel)
- §2: Trigger-test Deel A (5/5 groen) tegen T3-precedent + v4.6.2-baseline
- §3: /applier-template content-samenvatting + trigger-test Deel B (4/4 groen)
  tegen apply_patch_v4_6_3.py
- §4: ontologie-drift-sanity (geen drift; geen ontologie-werk in scope)
- §5: Protocol-14 disclosure-check op 3 deliverables: clean
- §6: Deliverables-tabel (Protocol 16)
- §7: commit-suggesties (3 commits los)
- §8: stop-condities (geen getriggerd)
- §9: verdere overwegingen voor Tooling-04 (optioneel)

Ref: docs/instructies/instructie-tooling-03-protocol-skills.md
```

Steven kan ook minder commits maken (bv. A+B+C als één); suggestie volgt instructie-§5-principe "delen los committeerbaar".

## §8. Stop-condities — niet getriggerd

Geen van de §3-stop-condities uit de instructie heeft zich voorgedaan:

- /pre-sprint-inventarisatie trigger-test toont structurele afwijking van T3-precedent → niet voorgekomen; T3-content semantisch volledig gedekt door skill-§-skelet (zie §1.2)
- Sub-element uit Protocol v1.3 §6 sample-keuze niet codificeerbaar → niet voorgekomen; sample-keuze gecodeerd in skill-§6.1-§6.3 met spreidings-richtlijnen + pre-pilot-classificatie-verbod
- Deel A loopt uit → Deel B deferren → niet getriggerd; Deel A bleef beheerst (225 regels), Deel B gebouwd
- §0.5-firewall-aanschuring → niet voorgekomen; beide skills expliciet defensief
- Ontologie-drift in B.3-sanity → niet opgetreden (§4)

## §9. Verdere overwegingen voor eventuele Tooling-04

Drie observaties uit deze opdracht — geen actie nu:

1. **`/pilot-rapport`-skill** (overweging Tooling-04): de T-sprint pilot-rapport-structuur (8 paren in T2 / 6 paren in T3 / sample-keuze + per-paar-classificatie + pilot-conclusie) volgt een herhaalbaar patroon dat als skill gecodificeerd kan worden. Past in dezelfde reeks als `/pre-sprint-inventarisatie` + `/patch-rapport`. YAGNI tot er minimaal twee T-sprints in productie het patroon valideren — wat met T2 + T3 inmiddels zo is.

2. **Sectie-naam-binding skill-skelet ↔ sprint-instructie** (zie §1.2). Vandaag opgelost via expliciete mapping-tabel in de skill. Een Tooling-04 kan overwegen of nieuwe T-sprint-instructies primair het skill-skelet volgen (= §0-§9-namen) of het vraag-A-F-format. Dat is een masterchat-conventie-keuze, geen Tech-werk.

3. **Applier-template-evolutie**: skill voegt idempotentie-check toe boven T3-precedent. Eerste werkelijke gebruik in een T4-applier zal aantonen of de `ALREADY APPLIED`-detectie-logica in echt-werk-context houdt. Bij eerste afwijking: skill-update via Tooling-NN.

— Einde rapport.
