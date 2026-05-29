# Sessie-rapport — Overdracht naar nieuwe masterchat (v6.0)

**Datum:** 29 mei 2026
**Versie:** v6.0 (opvolger van v5.0 d.d. 28 mei 2026 avond)
**Status:** Definitief — klaar voor overdracht
**Doel:** Volledige zelfstandige context voor nieuwe masterchat in claude.ai. Met dit document + GitHub-MCP-toegang tot `stevenbouw/grc-kennismodel` is het project zonder gaps voort te zetten.
**Volgende voorgenomen activiteit:** geen actieve sprint. Steven kiest tussen meerdere richtingen — zie §12.1 en §17.

---

## §0. Quick-start voor nieuwe masterchat

Lees eerst dit hele document. Bevestig daarna GitHub-MCP-toegang door één bestand uit `stevenbouw/grc-kennismodel` op te halen (suggestie: `brain/brain__index.md` voor vault-staat-overzicht). Wacht op Steven's volgende prompt — onderneem geen actie.

**Zeven meest-relevante punten om te onthouden:**

1. **Baseline is v4.6.4** (CSF-range-fix, 29 mei 2026). Niet v4.6.3 zoals v5-handover. De fix corrigeerde 2 datatype-ranges in m21 + een version-bump; alle canonieke metrics ongewijzigd.
2. **Geen actieve sprint.** T1+T2+T3 én de v4.6.4-patch én de reasoner-evaluatie én de dashboard-revival zijn alle voltooid. H36 én H38 zijn resolved. Steven kiest tussen kandidaten voor wat hierna komt. Zie §12.1.
3. **H38 is RESOLVED** — OWL RL ≡ HermiT empirisch bevestigd voor deze baseline. Dit was de grote vondst van de 29-mei-sessie: de reasoner-evaluatie leidde tot één reële DL-conformiteits-bevinding (datatype-range-mismatch), gefixt in v4.6.4, her-geverifieerd consistent onder HermiT. Zie §7.3 + §8.
4. **Projectinstructie v1.11 is de actuele versie** (`docs/projectinstructie-v1_11.md`, 29 mei). Vervangt v1.10 als autoritatief startdocument; verwerkt v4.6.4, H38-resolved, Protocol 18, commit-push-werkverdeling, D.7-skill, dashboard-revival.
5. **Sprint-protocollen zijn nu 1-18** (Protocol 18 = pre-sprint-dashboard-update-checklist, gemerged iteratie 16). v5 noemde nog 17.
6. **Dashboard-revival Spoor B is voltooid + gecommit** — `grc-dashboard-v3-2.html` werkt offline (gevendord), WCAG 2.1 AA-clean, met ontologie-structuur-import. Twee verse-load-fixes (file://-guard + herkomst-kolom) ook gefixt. Zie §8.6 + §14.4.
7. **Cross-category-principe heeft nu TWEE precedenten** (m14 control↔legal-obligation uit T3 + csf↔ISO27001 outcome↔requirement/measure uit T4). Nog steeds kandidaat v1.3.1, nog NIET formeel in protocol-tekst. Zie §11.12.

**Wat veranderde t.o.v. v5 (één-blik):** baseline v4.6.3→v4.6.4; H38 parked→resolved; Protocol-aantal 17→18; projectinstructie v1.10→v1.11; dashboard-revival van "kandidaat A" naar "voltooid"; D.7-skill van "kandidaat B" naar "gebouwd + geregistreerd"; T4 van "kandidaat" naar "afgesloten als Optie B"; reasoner-evaluatie (kandidaat D) van "open" naar "afgerond, H37/H41 HOLD".

---

## §1. Project-essentie (één-paragraaf-versie)

Steven is GRC-adviseur bij een Nederlandse Rijksoverheidsorganisatie (gebruik altijd "de organisatie" of "Rijksoverheidsorganisatie", nooit de daadwerkelijke naam). Hij bouwt het **GRC Kennismodel** — een OWL 2 DL ontologie die alle toepasselijke wet- en regelgeving, normen en best practices integreert in één machine-leesbare kennisbron met dashboard-bediening. Het model is de informatie-laag van het ISMS. Steven is "redelijke leek" in ontologie-engineering met sterke GRC-domeinkennis. Hij communiceert in het Nederlands, verwacht eerlijke pushback, geen diplomatieke omwegen. Formele Claude-toestemming verkregen maart 2026.

**Kernprincipe D9 — framework-neutraal:** alle normen/wetten/kaders zijn gelijkwaardig gemodelleerd; geen enkel framework heeft architecturaal privilege. BIO 2.0 is het operationele toepassings-perspectief voor dashboard + rapportage (verplichte Rijksoverheid-baseline), niet de architecturele kern. "Het model is het woordenboek (neutraal), het dashboard is het verhaal (perspectief)."

---

## §2. Project-architectuur — zeven chats

| Chat | Locatie | Rol | Doet wel | Doet niet |
|---|---|---|---|---|
| **Master** | claude.ai | Projectadviseur + GRC-architect | Strategie, sparring, architectuurbeslissingen, prioritering, scope-pauze-besluiten, eind-sign-off, sprint-instructies, **eigen commits + pushes voor docs-laag (sinds 28-05)** | Geen Turtle/SPARQL, geen documenten, geen dashboard-code, **geen pushes naar `ontology/`/scripts/dashboard-code** |
| **Technisch** | Claude Code | Ontologie-expert OWL/SPARQL/SHACL | Turtle, SPARQL, SHACL, reasoner-validatie, diagnostiek, patch-voorbereiding, applier-scripts, NEN-bron-lezing | Geen strategie, beleid, UI-code, geen autonome commits |
| **Documentatie** | claude.ai | Beleidsadviseur + schrijver | PID, managementcommunicatie, beleid (NL) | Geen ontologie-code, dashboard-code |
| **Dashboard** | Claude Code | Full-stack developer + visualisatie | HTML/JS dashboards, Cytoscape.js/Chart.js, SPARQL, export-scripts | Geen ontologie-wijzigingen, beleidsdocumenten |
| **Asset** | claude.ai | M18-specialist | M18 TBox, mappings, SHACL (afgerond; stand-by) | Geen wijzigingen andere modules |
| **Analyse** | claude.ai | Framework-analist + landschap-onderzoek | Externe frameworks analyseren, opties formuleren, landschap-onderzoek | Geen Turtle, geen architectuurbeslissingen, geen beleid |
| **Brein** | Claude Code | Brain-vault-onderhoud | Aanmaken/updaten brain__*-bestanden, cross-referentie-bewaking, autonoom bepalen welke bestanden bijwerken | Geen architectuurbeslissingen, geen ontologie-wijzigingen, geen beleid |

## §2a. Werkflow — masterchat-push-permissie (sinds 28-05-2026, ongewijzigd geldig)

Masterchat mag zelf committen + pushen naar `stevenbouw/grc-kennismodel`.

**Scope van de regel:**
- Geldt voor masterchat-eigen deliverables: `docs/instructies/`, `docs/skos-beoordelings-protocol-*.md` (status-bumps), `docs/handovers/`, `docs/projectinstructie-*.md`.
- Geldt NIET voor `ontology/`, `grc-shacl.ttl`, scripts, dashboard-code — die wegen alleen via Tech/Dashboard met Steven's handmatige commit.
- **De subagent-invariant blijft hard:** Tech/Brein/Dashboard committen NOOIT zelfstandig. Steven inspecteert `git status` + `git diff` en commit handmatig voor hun werk. Gecodificeerd in `.claude/settings.json`-deny op `Bash(git commit:*)` + `Bash(git push:*)`.

**Compensatie voor wegvallen menselijke diff-gate op masterchat-pushes:** masterchat kondigt vóór elke push expliciet aan WAT er gepushed wordt en WAAROM. Steven kan op elk moment onderbreken. Voor contested calls (overrulen van specialist-voorkeur, of wijzigingen aan autoritatieve docs): expliciete bevestiging vragen vóór push.

**Documentatie-staat van deze regel — nu BIJGEWERKT (was debt in v5):**
- ✓ Vastgelegd in brain-vault (Brein-cyclus iteratie 15, `brain__workflow__commit-push-werkverdeling`)
- ✓ **Verwerkt in `docs/projectinstructie-v1_11.md`** (§ZEVEN CHATS + gedeelde gedragsregels) — v1.10 noemde nog "Steven pusht"; v1.11 corrigeert dit
- ✓ **Verwerkt in dit overdrachtsrapport (v6)**
- Resteert: `docs/skos-beoordelings-protocol-v1_3.md` §7.3 (Steven's rol-beschrijving) — lage prioriteit, bij eerstvolgende protocol-touch

**Conform regel:** instructies voor Analyse- en Documentatie-chats (claude.ai-only, geen repo-toegang) lopen via masterchat **inline**, niet via GitHub. Steven kopieert ze handmatig naar de doel-chat. Subagent-instructies (Tech/Brein/Dashboard in Claude Code) gaan WEL via repo, want die hebben directe file-toegang.

**Werkproces-schema:**

```
Subagent-werk:
  Masterchat → push instructie naar docs/instructies/ → Tech/Brein/Dashboard leest
  → uitvoeren + leveren → Steven inspecteert + commit handmatig → masterchat review aan de bron

Analyse-/Documentatie-werk:
  Masterchat → inline prompt in chat → Steven kopieert naar claude.ai-doel-chat
  → uitvoeren + leveren → eventueel handmatig in repo

Master-overdracht (van masterchat naar volgende masterchat):
  Masterchat → overdrachtsrapport (.md) in chat één push naar docs/handovers/
  → Steven gebruikt het bij start van nieuwe sessie (upload of project-knowledge)
```

**Verificatie-discipline (kern-werkwijze masterchat):** masterchat reviewt subagent-opleveringen ALTIJD aan de bron via GitHub-MCP (`get_file_contents`), nooit op de subagent-claim alleen. De 29-mei-sessie bevestigde de waarde hiervan herhaaldelijk — cijfers, version-triples en breedte-checks werden steeds aan de bron geverifieerd vóór GO.

---

## §3. Vastgestelde ontwerpbeslissingen — D1 t/m D12 + D4.1

Wijzigingen vereisen masterchat-goedkeuring. Geen D-wijzigingen sinds D4.1 (27 mei). v4.6.4 **versterkte** D1 (zie hieronder) zonder de beslissing te wijzigen.

### §3.1 — D-decisions D1 t/m D12

| ID | Beslissing | Status |
|---|---|---|
| D1 | OWL 2 DL profiel | Initieel; **per v4.6.4 versterkt: OWL RL ≡ HermiT empirisch bevestigd voor deze baseline (H38 resolved)** |
| D2 | Turtle-serialisatie | Initieel |
| D3 | 11 namespaces (`fw:`, `ctrl:`, `bio:`, `risk:`, `roles:`, `compl:`, `isms:`, `biz:`, `ext:`, `asset:`, `csf:`) | Definitief sinds v4.5.0 |
| D4 | SKOS voor cross-framework mappings | Initieel; D4.1 toegevoegd 27-05-2026 |
| D5 | `owl:sameAs` strikt voor ctrl:↔bio: brug (93 paren) | Initieel |
| D6 | Tweetalige annotaties @nl/@en — meeliftregel | v4.1.0 |
| D7 | BIO 2.0 als twee klassen (BIOControl + OverheidsMaatregel) | Initieel |
| D8 | Eén canonieke SoA (isms:SoA_2026 + 93 SoAEntry_*) | v4.2.2 |
| D9 | Framework-neutraal model — alle kaders gelijkwaardig | 17-03-2026; bewijs verdiept v4.6.2 (T2), v4.6.3 (T3 cross-category) |
| D10 | COSO ICF/ERM als enterprise-governance-laag | 17-03-2026 |
| D11 | `owl:sameAs` asset-convergentie — ster-patroon (5 bruggen) | 13-04-2026 |
| D12 | Drie-laags compliance-architectuur | 22-04-2026 |

**D1-versterking (v4.6.4 / H38):** D1 koos OWL 2 DL als profiel maar er was sinds v4.0.0 geen HermiT-run op de modulaire baseline gedraaid — de aanname "OWL RL ≡ HermiT" was onbewezen (dit was H38). De 29-mei-evaluatie + v4.6.4-fix + HermiT-her-run sloten dit: OWL RL en HermiT geven nu beide een consistent model. D1 zelf onveranderd; het bewijs eronder is nu hard. Zie §8.

**Toekomstige D-decision-kandidaat (niet vastgesteld):** activering van SKOS-axiomas (skos:S46 symmetrie, skos:S47 transitiviteit) onder OWL-RL is een **toekomstige nieuwe D-decision** over reasoner-/SKOS-axioma-configuratie — niet impliciet te activeren. Reden: de reasoner-evaluatie kwantificeerde dat activering +2.831 triples (+6,3%) zou genereren, waaronder 12 cross-namespace exactMatch-claims die D4 schenden + de SKOS-identiteit met de owl:sameAs-identiteit (D5/D11) vermengen. Zie H41 + §8.

### §3.2 — D4.1 — Disclaimer-handling bij autoritatieve mapping-bronnen

Kern-regel onveranderd: bij een expliciete non-equivalence-disclaimer in een autoritatieve mapping-bron (zoals ENISA TIG regel 285) is `skos:exactMatch` niet verdedigbaar, ongeacht of C1-C3 sluitend voldoen; closeMatch/relatedMatch/broadMatch/narrowMatch blijven valide. Geldt vanaf vaststelling (27 mei), geen retroactieve audit. Was bij T3 niet van toepassing (geen ENISA-achtige disclaimer voor AVG↔ISO 27002). Blijft intact als regel voor toekomstige sprints.

---

## §4. Sprint-protocollen 1-18 (operationeel in `docs/sprint-protocols.md`)

**18 actieve protocollen** — v5 noemde 17; Protocol 18 is gemerged in iteratie 16. Een aantal protocollen is deterministisch geborgd via Tooling-01 hooks i.p.v. enkel proza-discipline.

| # | Protocol | Borging |
|---|---|---|
| 1 | Pre-sprint-inventarisatie | Proza + skill `/pre-sprint-inventarisatie` (Tooling-03) |
| 2 | Pre-sprint multi-module-discipline | Proza |
| 3 | Schema-meta-rapport | Proza |
| 4 | Bron-verificatie vóór TBox-declaratie | Proza |
| 5 | Bron-verificatie vóór raming-opstelling | Proza |
| 6 | Ramings-baseline rdf:type-dubbele-telling (5 triples/typed-individual) | Proza |
| 7 | Bron-bereikbaarheid in uitvoerings-omgeving | Proza |
| 8 | Precedent-discipline bij nieuw framework-cluster | Proza |
| 9 | Raming-discipline bij aggregatie-mappings | Proza |
| 10 | Patch-rapport §9 verplicht (geparkeerde-items-status) | Proza + skill `/patch-rapport` (Tooling-02) |
| 11 | Brain-vault-update na minor-release | Proza (Brein-cyclus) |
| 12 | Instructie-consistentie code-block versus toelichting | Proza |
| 13 | Bron-typo-beleid patroon-criterium | Proza + skill `report-structure` (Tooling-02) |
| 14 | Pre-push disclosure-check (5 categorieën) | Proza + hooks `secret-scan.py` + `disclosure-check.py` (Tooling-01) |
| 15 | Tech levert werkbare applier | Proza + skill `/applier-template` (Tooling-03) |
| 16 | Lokatie verificatie-scripts in patch-rapport §9 | Proza + skill `/patch-rapport` (Tooling-02) |
| 17 | NEN-werkverdeling Tech-autonomie | Proza (lokale NEN-toegang) |
| **18** | **Pre-sprint-dashboard-update-checklist** | **Proza (NIEUW iteratie 16) — controleert of dashboard-databestanden synchroon zijn met de actuele baseline vóór een dashboard-sprint** |

**Protocol v1.3-werkflow-disciplines (§10.2-§10.5)** — FINAL sinds T3:

- §10.2 Bottom-up rapport-bouw verplicht — geborgd via skill `report-structure` + `/patch-rapport`
- §10.3 Interne tabel-consistentie-discipline — geborgd via skill `report-structure`
- §10.4 Helper-script-classificatie autoritatief — geborgd via skill `report-structure`
- §10.5 Metrics-tabel-scope-annotatie verplicht — geborgd via skill `report-structure` + `/patch-rapport`

**Lint-kandidaat (Brein-leerpunt iteratie 16):** `brain__workflow__sprint-protocollen.md` toont nog de v1.9-momentopname (12 protocollen) met een pointer naar de canonieke 18 in `docs/sprint-protocols.md`. Volledige uitwerking van 13-18 in dat brain-bestand is een latere lint-actie.

---

## §5. SKOS-beoordelings-protocol — v1.3 is FINAL

v1.3 vastgesteld als FINAL door masterchat (28-05-2026, T3-scoping). `docs/skos-beoordelings-protocol-v1_3.md`. Bevat alle v1.2-inhoud + zeven verfijningen + de vier §10-werkflow-disciplines (zie §4). Toepassings-bewijs: operationeel toegepast op 31 m14-paren in T3 (6/6 pilot-behoud + 29 behoud + 2 mutaties).

### §5.1 — Kandidaat v1.3.1 (cross-category) — nu TWEE precedenten

**Cross-category-principe** (geboren uit T3, zie §11.12) is empirisch gevalideerd en als brain-precedent vastgelegd, maar nog **NIET formeel** in v1.3-protocol-tekst. Per 29 mei zijn er **twee precedenten**:

1. **m14 (T3):** control ↔ legal-obligation (AVG-artikel) — 31 paren, eindstand relatedMatch-basislijn
2. **csf↔ISO27001 (T4-inventarisatie):** outcome ↔ requirement/measure — 739 closeMatch-mappings, cross-category geconstateerd, geen mutatie (T4 was inventarisatie-only)

Het kandidaat-principe luidt: *"wanneer subject en object van een SKOS-mapping ontologisch verschillende categorieën zijn, is `relatedMatch` de associatieve basislijn; broad/narrowMatch alleen bij aantoonbare conceptuele subsumptie op paar-niveau, niet als cluster-default; closeMatch-uitzondering bij retrieval-interchangeability."* Formele protocol-tekst-wijziging (v1.3.1) is masterchat-werk bij volgende SKOS-sprint-scoping — nu met twee precedenten beter onderbouwd, maar nog steeds bewust uitgesteld.

---

## §6. NEN-bron-toegang voor Tech — 14 normen (ongewijzigd t.o.v. v5)

Locatie `/Users/stevenbouwmeester/grc-sources-licensed/`, 14 normen, discipline: parafrase + clausule-verwijzing, geen verbatim >10 woorden (Protocol 17). Toekomstige cross-walks (m11 NIST SP 800-53, m17 COSO/COBIT) gebruiken bronnen die niet-NEN zijn, dus niet onder dezelfde restrictie. Protocol 14 disclosure-check categorie 5 (NEN-tekst-detectie) blijft handmatig.

---

## §7. Actuele baseline — v4.6.4 (CSF-range-fix)

**Patch-datum:** 29 mei 2026
**Aanleiding:** DL-conformiteits-fix — HermiT meldde v4.6.3 inconsistent door een datatype-range-mismatch op 2 CSF-Tier-description-properties. v4.6.4 corrigeert de range; H38-lus gesloten.

### §7.1 — Kerncijfers v4.6.4

| Metric | v4.6.4 | Δ vs v4.6.3 |
|---|---:|---:|
| Triples pre-inferentie | 20.950 | 0 |
| Triples post OWL RL | 44.907 | 0 |
| Klassen | 199 | 0 |
| NamedIndividuals | 1.383 | 0 |
| ObjectProperties | 149 | 0 |
| DatatypeProperties | 96 | 0 |
| owl:sameAs | 98 (93 D5 + 5 D11) | 0 |
| SKOS-mappings totaal | 1.798 | 0 |
| — skos:exactMatch | 18 | 0 |
| — skos:closeMatch | 1.457 | 0 |
| — skos:broadMatch | 129 | 0 |
| — skos:narrowMatch | 0 | 0 |
| — skos:relatedMatch | 194 | 0 |
| owl:Nothing post-inf | 0 (consistent) | 0 |
| SHACL SECTIE A | 0 violations | 0 |
| SHACL SECTIE B | 0 violations | 0 |
| SHACL COMBINED | 290 (identiek aan v4.6.0-baseline) | 0 |
| **DL-consistentie (HermiT)** | **consistent, 0 owl:Nothing, geen justificaties** | **was: inconsistent (8 justificaties)** |

**Alle canonieke metrics identiek aan v4.6.3.** De fix vervangt alleen het *object* van 2 triples (`xsd:string` → `rdfs:Literal`). OWL RL ziet datatype-ranges niet streng → de metrics zijn invariant; de fix is puur DL-correctheid. Dit is een belangrijk leerpunt: een datatype-range-mismatch is onzichtbaar onder de canonieke OWL RL-metrics maar fataal onder HermiT.

### §7.2 — Module-impact v4.6.4

Twee bestanden gewijzigd:
- `m21-csf.ttl`: 2 range-correcties (`csf:riskGovernanceDescription` + `csf:riskManagementDescription`: `rdfs:range xsd:string` → `rdfs:Literal`). De `@en`-getagde waarden (NIST CSWP 29-tekst) blijven ongemoeid. 0 resterende `xsd:string`-ranges in m21 na de fix (breedte-check bevestigd aan de bron).
- `grc-core.ttl`: version-bump naar 4.6.4. **Bijvangst:** de version-triple stond op 4.6.0 — tijdens T1/T2/T3 nooit meegebumpt. Stille drift, nu gladgetrokken. Leerpunt: version-bump-stap wordt bij triple-neutrale T-sprints makkelijk overgeslagen.

20 overige modules + `grc-shacl.ttl`: byte-identiek aan v4.6.3.

### §7.3 — H38 status: RESOLVED

De volledige boog (de kern-werkstroom van de 29-mei-sessie):

1. **Blind spot:** sinds v4.0.0 geen HermiT-run op de modulaire baseline; "OWL RL ≡ HermiT" onbewezen.
2. **DL-construct-census** (reasoner-evaluatie): toonde één materialiseerbaarheids-complete DL-constructie (`asset:AssetOrComponent ≡ unionOf`); owlrl reproduceert exact 44.907 triples — voorspelling: housekeeping-only, equivalent.
3. **HermiT-run v4.6.3** (door Steven, Protégé): meldde **inconsistent** (`owl:Thing SubClassOf owl:Nothing`, 8 justificaties = 4 CSF-Tiers × 2 properties). De census-voorspelling werd dus weersproken door een reële bevinding.
4. **Diagnose** (masterchat, aan de bron): datatype-range-mismatch — de 2 CSF-description-properties hadden `rdfs:range xsd:string` maar droegen `@en`-getagde waarden (`rdf:langString`). HermiT ziet dat als botsing; OWL RL niet.
5. **Fix:** v4.6.4 — range → `rdfs:Literal` (omvat zowel `xsd:string` als `rdf:langString`).
6. **Her-verificatie:** HermiT-run op `merged_asserted_v4_6_4.ttl` → **consistent, 0 owl:Nothing, geen justificaties** (69 sec).

H38 is daarmee resolved: eerste empirisch bewijs OWL RL ≡ HermiT voor deze baseline, én eerste sprint waarin een HermiT-bevinding een TBox-fix in de canonieke baseline stuurde. De HermiT-her-run is nu onderdeel van de DL-conformiteits-discipline (vangnet voor datatype-mismatches die OWL RL mist).

---

## §8. Recente sessies-overzicht

### §8.1 — t/m 28 mei 2026: migratie + T1/T2/T3 + Brein 13/14/15 + Tooling-track 01-03

Volledig beschreven in v5 §8.1-§8.8. Niets veranderd aan die context. Kort: migratie naar Claude Code + GitHub (26 mei); T1 (v4.6.1, 28 exactMatch-herclassificaties m10); T2 (v4.6.2, 65 bidirectional-mutaties m10); T3 (v4.6.3, 2 mutaties m14, cross-category-principe geboren); Brein-cycli 13/14/15; Tooling-track 01-03 (`.claude/`-laag operationeel met hooks/permissions/skills, §0.5-firewall hard); SKOS-protocol v1.3 FINAL; masterchat-push-permissie.

### §8.2 — 29 mei 2026: multi-werkstroom-sessie (DEZE SESSIE)

Eén masterchat-sessie met **vijf werkstromen**, alle voltooid + gecommit. Dit is de inhoud die v6 toevoegt aan v5.

**Werkstroom 1 — Reasoner-toolchain-evaluatie (H37 + H38 + H41):**
Tech leverde `output/reports/evaluatie-reasoner-toolchain-h37-h38-h41.md`. Masterchat reviewde aan de bron. Uitkomst: alle drie HOLD/parked, met H38 doorgeschoven naar resolved via de v4.6.4-fix (zie §7.3).
- **H38** (OWL RL vs HermiT): DL-construct-census → één materialiseerbaarheids-complete constructie → leidde via de HermiT-run tot de v4.6.3-inconsistentie-vondst → v4.6.4-fix → resolved.
- **H41** (SKOS-axioma-handling): control-run bewees mechanistisch dat post-inferentie SKOS-groei (+956) **100% owl:sameAs-propagatie** is, **0% SKOS-axiomas** — dit verklaart waarom T1/T2/T3 Δ post-OWL-RL = 0 gaven. Hypothetische activering = +2.831 triples (+6,3%), 12 cross-namespace exactMatch-claims die D4 schenden, SHACL-impact 0. **Masterchat-regel: activering = nieuwe D-decision.**
- **H37** (open-ontologies-MCP, Rust + Oxigraph + tableaux + MCP, MIT, pre-1.0 v0.1.11): geen van 4 triggers actief (44.907 < 50k drempel; H38 toont geen reasoner-limitatie; pre-1.0; SKOS-impact hanteerbaar). HOLD.
Gecombineerde evaluatie-instructie was gepusht in `docs/instructies/instructie-open-ontologies-evaluatie.md`.

**Werkstroom 2 — v4.6.4 CSF-range-fix:**
Directe uitkomst van de HermiT-vondst. Instructie `docs/instructies/instructie-csf-range-fix-v4_6_4.md` (masterchat-besluit Optie A: range → rdfs:Literal). Tech leverde patch v4.6.4 + `output/reports/patch-rapport-v4_6_4.md`. Masterchat GO aan de bron. Steven draaide de HermiT-her-run → consistent. Zie §7.

**Werkstroom 3 — Dashboard-revival Spoor B:**
`grc-dashboard-v3-2.html` (operationele werkmap). Drie onderdelen: **B7** ontologie-structuur-import + bron-split 1A (wStruct() = ontologie canoniek voor structuur, wOper() = hand-seed primair voor operationeel); **Q-M5** vendoring (Chart.js/sql.js lokaal in `dashboard/vendor/`, offline-werkend); **B9** WCAG 2.1 AA (47→0 axe-bevindingen). Rapport `output/reports/dashboard-rapport-qm5-vendoring-b9-wcag-2026-05-29.md`. Steven deed visuele pass: dashboard werkt via `python3 -m http.server` (316 controls, 35% compliance, donut-grafieken, DB actief). Twee verse-load-fixes geïdentificeerd + gefixt (instructie `docs/instructies/instructie-dashboard-verse-load-fixes.md`): **Fix A** file://-guard (duidelijke instructie i.p.v. kale "DB fout" bij dubbelklik; WASM laadt niet onder file://), **Fix B** `migreerStructuurKolommen()` ook in init-flow (voorkomt "—" bij verse load vóór eerste import). Steven committe alles. Q-M-architectuurbesluiten in `docs/instructies/besluitnotitie-qm-dashboard-2026-05-29.md`.

**Werkstroom 4 — T4-inventarisatie (afgesloten als Optie B):**
Inventarisatie-only, geparkeerd, geen mutatie. De "105 cross-bron-overlap" bleek een bron-niveau-getal (v4.5.0, block-level provenance), niet machine-reproduceerbaar. Wat er ligt: 739 csf↔ISO27001 closeMatch-mappings, cross-category, geen prima-facie defect. Nieuw kandidaat-H-item (csf↔ISO cross-category-predicaat) **zonder formeel nummer** + open 699-vs-494-reconciliatie (§2.2 vs §3.1-B in t4-rapport onverklaard).

**Werkstroom 5 — Brein-cyclus iteratie 16 (eerste multi-werkstroom-cyclus):**
Instructie `docs/instructies/instructie-brein-cyclus-iteratie-16.md`. Brein leverde `output/reports/brein-rapport-iteratie-16.md` (15 bestanden: 2 nieuw + 12 brain-update + 1 docs). H38→resolved, H37/H41 verrijkt, H42/H43/H44 als masterchat-benoemde kandidaten geregistreerd, csf↔ISO als kandidaat-precedent zonder nummer, Protocol 18 gemerged, D.7-skill geregistreerd, twee leerpunten (settings.json-schemafix + version-drift). Steven committe. Brain-vault ~117 bestanden.

**Plus: projectinstructie v1.11 + D.7-skill.**
- `docs/projectinstructie-v1_11.md` gepusht — volledig zelfstandig document, vervangt v1.10 als startdocument. Verwerkt alle bovenstaande deltas + nieuwe gedragsregel (vrije-tekst→rdfs:Literal).
- D.7 GRC-domein-skill (`.claude/skills/grc-domein/SKILL.md` + `kaders-reference.md`) opgeleverd door Tech + GO. Één openstaande verificatie: bevestigen dat `fw:relatedTo`/`fw:alignsWith`/`fw:supersedes` echt in m01-framework.ttl staan.

### §8.3 — Referentiemateriaal in repo (autoritatief beschikbaar)

- `output/reports/patch-rapport-v4_6_4.md` — volledig v4.6.4-detail
- `output/reports/evaluatie-reasoner-toolchain-h37-h38-h41.md` — reasoner-evaluatie
- `output/reports/dashboard-rapport-qm5-vendoring-b9-wcag-2026-05-29.md` — dashboard-revival
- `output/reports/t4-pre-sprint-inventarisatie.md` + oplevernotitie — T4
- `output/reports/brein-rapport-iteratie-16.md` — Brein-cyclus
- `docs/instructies/besluitnotitie-qm-dashboard-2026-05-29.md` — Q-M-besluiten
- `output/reports/skill-eval-tier1-tier2-2026-05-27.md` + `extensie-landschap-claude-2026-05-28-3.md` — skill/MCP-besluiten (referentie, v5-erfenis)

---

## §9. Brain-vault — primaire kennisbron

**Structuur:** flat bestanden in `brain/`-folder met `__`-separator (decisions, sprints, architecture, concepts, modules, sources, workflow, scope).

**Entry-points:** `brain/brain__index.md`, `brain/brain__log.md`, folder-registers (`brain__*__-register.md`).

**Iteratie-stand** per 29-05-2026: **iteratie 16 afgesloten** (multi-werkstroom-cyclus), brain-vault **~117 bestanden** (v5 schatte ~125; de geverifieerde stand uit `brain__index.md` is ~117).

**Nieuwe brain-bestanden sinds v5:**
- `brain__sprints__v4_6_4_csf-range-fix-dl-conformiteit.md` (TBox-bugfix-sprint)
- `brain__concepts__spoor-b-revival.md` (dashboard-revival B7/Q-M5/B9 + 2 vervolgpunten)

**Belangrijke brain-updates iteratie 16:** H38→resolved + H37/H41 verrijkt (`brain__architecture__*`), H-register (H42/H43/H44 + csf↔ISO-kandidaat), `dashboard-productlijnen` (Q-M2-reversal), `cross-bron-overlap` + `cross-category-mappings` (T4), workflow-register (Protocol 18 + D.7 + leerpunten).

**Conventie ongewijzigd:** bij vragen over projecthistorie, architectuur of conventies → raadpleeg brain-vault via GitHub-MCP vóór andere bronnen.

---

## §10. Sprint-architectuur en huidige toestand

### §10.1 — Vijf doelen + drie sporen

| Spoor | Status |
|---|---|
| A — Technische ontologie-opbouw | Voltooid t/m v4.6.4 voor Fase 1-4 + T1+T2+T3 + DL-conformiteits-fix. H36 + H38 resolved. Productie-/kwaliteitsanalyse-fase actief. |
| B — Organisatiespecifieke invulling | Pending; T&I-lab-test gepland. **Dashboard-werkmap (`grc-dashboard-v3-2.html`) gerevitaliseerd 29 mei: ontologie-structuur-import + bron-split, offline-werkend, WCAG-clean, verse-load-fixes.** |
| C — Gebruik en governance | Pending; explorer op v4.6.0 (Spoor A); dashboard Spoor B gerevitaliseerd. Build-script-inhaalslag naar v4.6.4-snapshot is parallel/niet-blokkerend. |

### §10.2 — Sprint-historie

| Sprint | Datum | Scope | Status |
|---|---|---|---|
| v4.6.0 | 21-05-2026 | Fase 4 — ENSIA + volwassenheidsmodel + CSF Tiers | Afgerond |
| Migratie | 26-05-2026 | Tech/Brein/Dashboard naar Claude Code + GitHub | Afgerond |
| T1 | 26-05-2026 | SKOS Fase 1 — H36 m10-cluster (28 paren) | Afgerond — patch v4.6.1 |
| Brein 13 + mini-revisies | 27-05-2026 | T1-afronding + D4.1 + Protocol 17 | Afgerond |
| T2 | 27-05-2026 | SKOS Fase 2 — m10 bidirectional (118 paren, 65 mutaties) | Afgerond — patch v4.6.2 |
| Brein 14 + Optie C | 27/28-05 | T2-afronding + Protocol v1.3-draft + projectinstructie v1.10 | Afgerond |
| T3 | 28-05-2026 | SKOS Fase 3 — m14 AVG/GDPR (31 paren, 2 mutaties) | Afgerond — patch v4.6.3 |
| Brein 15 | 28-05-2026 | T3-close + errata + cross-category-precedent | Afgerond |
| Tooling-01/02/03 | 28-05-2026 | `.claude/`-laag (hooks + permissions + skills) | Afgerond |
| **Reasoner-evaluatie** | **29-05-2026** | **H37 + H38 + H41 (alle HOLD; H38 → resolved)** | **Afgerond** |
| **v4.6.4 CSF-range-fix** | **29-05-2026** | **DL-conformiteits-fix (2 range-correcties m21) + HermiT-her-run** | **Afgerond — patch v4.6.4** |
| **Dashboard-revival** | **29-05-2026** | **B7 + Q-M5 vendoring + B9 WCAG + verse-load-fixes (Spoor B)** | **Afgerond — gecommit** |
| **T4-inventarisatie** | **29-05-2026** | **csf↔ISO27001 cross-bron-overlap** | **Afgesloten als Optie B (geparkeerd)** |
| **Brein 16** | **29-05-2026** | **Multi-werkstroom-cyclus (5 werkstromen)** | **Afgerond** |

**Geen actieve sprint per 29-05-2026.**

### §10.3 — Tooling-laag overzicht (§14 voor detail)

| Laag | Inhoud |
|---|---|
| Hooks | `secret-scan`, `disclosure-check` (cat 1-4), `versie-suffix-check`, `sessionstart-context` |
| Permissions | Hard deny `git commit/push` voor subagents; `ask` destructieve git; `allow` read-only + python3 |
| Path-scoped skills | `ontology-conformance` (`ontology/*.ttl`), `report-structure` (`output/reports/*`) |
| Reference-skill | `repo-reference` (description-triggered) |
| Action-skills | `/canonical-metrics`, `/shacl-split`, `/patch-rapport`, `/pre-sprint-inventarisatie`, `/applier-template` |
| **Domein-skill** | **`grc-domein` (D.7, NIEUW 29 mei) + `kaders-reference.md` — NL-kaders-domeincontext** |
| Config | `.claude/settings.json`, `.claude/hooks/disclosure-config.json` (versioned, org-neutraal) + `.local.json` (gitignored) |

---

## §11. Werkflow-leerpunten — kritiek voor toekomstige sprints

Ongewijzigd t.o.v. v5: §11.1-§11.11 + §11.12-§11.15. Aangevuld met §11.16-§11.18.

### §11.12 — Cross-category-principe (T3-leerpunt, kandidaat v1.3.1)

Bij SKOS-mappings tussen ontologisch verschillende categorieën (control ↔ legal-obligation, control ↔ principe, outcome ↔ requirement) is **`relatedMatch` de semantische basislijn**, niet broad/narrowMatch. Cluster-cardinaliteit is een signaal, géén mandaat. Empirisch gevalideerd op 31 m14-paren (T3) + cross-category geconstateerd op 739 csf↔ISO27001-mappings (T4). Brain-precedent in `brain__concepts__cross-category-mappings.md`. **m10-versus-m14-onderscheid:** m10 (control ↔ NIS2-letter) is binnen-categorie (beide measures) → broadMatch is genuiene genus-species; m14 (control ↔ AVG-artikel) is cross-category → associatief correct.

### §11.13 — Masterchat-push-discipline (sinds 28-05-2026)

Voor elke push expliciet WAT en WAAROM aankondigen; bij contested calls bevestiging vragen; geen pushes naar `ontology/`/scripts/dashboard-code; bij grote bestanden (>200 regels) bij voorkeur surgische edit door Tech/Brein i.p.v. MCP full-file-rewrite. **29-mei-bevestiging:** alle masterchat-pushes (range-fix-instructie, brein-16-instructie, dashboard-verse-load, projectinstructie v1.11, dit rapport) volgden dit patroon.

### §11.14 — Sign-off-discipline op rapporten (T3-leerpunt)

Bij eindrapporten een interne tabel-consistentie-check (Protocol v1.3 §10.3). De 29-mei-patch-rapporten waren intern consistent (geen errata nodig, in tegenstelling tot T3).

### §11.15 — §0.5-firewall in skill-tekst inbouwen (Tooling-leerpunt)

De §0.5-firewall expliciet in skill-tekst opnemen biedt één laag dieper veiligheid. Patroon voor alle zelf-gebouwde skills die proza-discipline mechaniseren.

### §11.16 — HermiT-her-run als DL-conformiteits-vangnet (v4.6.4-leerpunt) — NIEUW

OWL RL controleert datatype-ranges niet streng. Een range-mismatch (bv. `xsd:string` op een property die `@en`-getagde waarden krijgt) is onzichtbaar onder de canonieke OWL RL-metrics (Δ=0, 0 owl:Nothing) maar maakt het model inconsistent onder HermiT. **Periodieke HermiT-her-run is daarom het DL-conformiteits-vangnet** — vooral na het toevoegen van datatype-properties of getagde literals. De 29-mei-sessie bewees de waarde: een evaluatie die "waarschijnlijk equivalent" voorspelde leverde één reële fix op.

### §11.17 — Vrije-tekst-properties krijgen `rdfs:Literal`-range (v4.6.4-gedragsregel) — NIEUW

Een property die taal-getagde (@nl/@en) waarden ontvangt moet `rdfs:range rdfs:Literal` hebben, niet `xsd:string` (dat sluit `rdf:langString` uit → DL-inconsistentie). Identifier-/code-velden zonder taal-tag mogen `xsd:string` houden. Dit is nu een gedeelde gedragsregel in projectinstructie v1.11. Bestaande vrije-tekst-properties (`ext:hasControlStatement`, `ext:hasUVInterpretation`, `ext:hasAttributionText`) volgden dit al; de CSF-descriptions waren de uitzondering die v4.6.4 herstelde.

### §11.18 — Version-bump-discipline bij triple-neutrale sprints (v4.6.4-leerpunt) — NIEUW

De grc-core version-triple stond sinds T1 op 4.6.0 — nooit meegebumpt tijdens T1/T2/T3 omdat die SKOS-substitutie-sprints geen TBox raakten. Controleer bij triple-neutrale sprints expliciet of de version-triple is bijgewerkt. Kandidaat voor een Protocol-aanvulling (niet geformaliseerd).

---

## §12. Open punten en roadmap

### §12.1 — Volgende voorgenomen activiteit — Steven kiest

**Geen actieve sprint.** De roadmap is verschoven t.o.v. v5: drie v5-kandidaten zijn afgehandeld (D reasoner-evaluatie → afgerond; B D.7-skill → gebouwd; dashboard-deel van A → gerevitaliseerd). Wat resteert:

| Kandidaat | Reden om nu te doen | Effort |
|---|---|---|
| **A. T4-vervolg — csf↔ISO27001 cross-category-sprint** | T4-inventarisatie ligt klaar; vereist masterchat-scope-besluit op scope-eindpunt (clausule/Annex-A/beide), overlap-definitie, cross-category-predicaat (relatedMatch-basislijn vs closeMatch-behoud), provenance-modellering. **Eerst de 699-vs-494-reconciliatie oplossen.** | Substantieel — scope-besluit + T-sprint |
| **B. Protocol v1.3.1-formalisering (cross-category)** | Nu twee precedenten (m14 + csf↔ISO). Formaliseren in protocol-tekst. | Beperkt — masterchat-werk, geen sprint |
| **C. Andere SKOS-kwaliteitsanalyse-T-sprint** | m17 COSO/COBIT, m11 NIST SP 800-53, m16 VIRBI, m12 DORA, of framework-niveau (fw:↔fw:) | Per kandidaat verschillend — scope-besluit nodig |
| **D. H33/H34 — m11 NIST SP 800-53 uitbreiding** | Substant. uitbreiding (124/~1000 in model) + enhancement-modellering | Substantieel — ontology-sprint |
| **E. Dashboard build-script-inhaalslag** | Spoor A explorer + Spoor B build-script naar v4.6.4-snapshot; parallel, niet-blokkerend | Beperkt — Dashboard-subagent |
| **F. m01-verificatie (D.7-skill-vooronderstelling)** | Bevestigen dat `fw:relatedTo`/`alignsWith`/`supersedes` echt in m01 staan | Klein — masterchat aan de bron |
| **G. Documentatie-debt restant** | `docs/skos-beoordelings-protocol-v1_3.md` §7.3 (Steven's rol); README v4.6.4; lint brain-sprint-protocollen naar 18 | Klein, gefaseerd |
| **H. §0.5 autonomie-koers verankeren** | Parked door Steven; vereist formeel D-/scope-besluit | Substantieel; raakt visie-invariant |
| **I. Tooling-04 `/pilot-rapport` + `/brein-cyclus`-skills** | YAGNI tot eerstvolgende T-sprint het triggert | Klein indien gewenst |

Geen sterke masterchat-voorkeur opgedrongen — dit is Steven's keuze. Als er een CSO/CISO-demo op de horizon staat, is **E** (dashboard build-script naar v4.6.4) het meest demo-relevant. Als de inhoudelijke kwaliteitsanalyse-lijn doorgezet wordt, is **A** (T4-vervolg) of **B** (v1.3.1-formalisering) de logische volgende stap.

### §12.2 — Documentatie-debt (verkleind sinds v5)

| Document | Status |
|---|---|
| `docs/projectinstructie-v1_11.md` | ✓ **Bijgewerkt 29 mei** — v4.6.4, H38-resolved, Protocol 18, commit-push-werkverdeling, D.7-skill, dashboard-revival, nieuwe rdfs:Literal-gedragsregel. Vervangt v1.10 als startdocument. |
| Dit overdrachtsrapport (v6) | ✓ **Vervangt v5** (v5 niet retroactief wijzigen) |
| `docs/skos-beoordelings-protocol-v1_3.md` §7.3 | Resteert — Steven's rol + masterchat-push-permissie; lage prioriteit |
| `README.md` | Resteert — v4.6.4-baseline, Tooling-laag, H36+H38-resolved; lage prioriteit |
| `brain__workflow__sprint-protocollen.md` | Resteert — lint: 13-18 volledig uitwerken (nu pointer naar canonieke 18) |

Niet urgent. Geen actieve werkstroom geblokkeerd.

### §12.3 — Bewust geparkeerd (geen urgentie)

| Item | Type | Trigger |
|---|---|---|
| H36 (ctrl↔compl SKOS-audit) | **RESOLVED** (T1+T2+T3) | — |
| H38 (OWL RL vs HermiT) | **RESOLVED** (v4.6.4) | — |
| H37 — open-ontologies MCP | Architectuur (HOLD) | >50k triples, of aangetoonde OWL RL-limitatie, of v1.0-release |
| H41 — SKOS-axioma-set-handling | Architectuur (parked, gekwantificeerd) | Activering = nieuwe D-decision (externe SKOS-audit / DCAT-AP / Spoor B-keten) |
| H39 — 290 SHACL false-positives uitsplitsen | Hygiëne | Rustige sprint of SHACL-shapes-wijziging |
| H40 — Dashboard-UI-renderdekking (Spoor A) | UX | UI-moderniseringssprint; Q-M4 latent/parked |
| H42/H43/H44 — dashboard-landschap-kandidaten | Architectuur (niet geactiveerd) | Spoor-B-operationeel / explorer-modernisering |
| csf↔ISO27001 cross-category-predicaat | Kandidaat-precedent (geen H-nummer) | T4-vervolg-sprint-scoping |
| H33 — m11 SP 800-53 uitbreiding | Inhoudelijk | T-sprint-kandidaat |
| H34 — m11 enhancement-modellering | Inhoudelijk | Serieuze SP 800-53-toepassing |
| H25/H26/H27/H32/H35 | Per H-register | Per-item triggers |
| H15 (governance-graafdekking) / H21 (implicit individuals) | Architectuur | Spoor B / consistentie-keuze |
| Cross-category-principe v1.3.1-formalisering | Protocol | Volgende SKOS-sprint-scoping (twee precedenten) |
| Confidence-verhoging mapping-bron-disclaimer-effect | Concept | Tweede onafhankelijke bron-bevestiging (open sinds iteratie 13) |
| Dashboard build-script naar v4.6.4-snapshot | Spoor C | Parallel, niet-blokkerend |
| 39-edge SKOS-discrepantie (v4.6.0-migratie) | Hygiëne | Bij dashboard-touch hermeten tegen v4.6.4 |
| PK-opschoning | Hygiëne | brain-vault + publieke bronnen verwijderbaar uit PK (nu in repo); NEN-restrictief moet blijven |
| Route 1/1-light (ISO-guidance parafrasering) | Inhoudelijk | Geparkeerd naar v5.x |
| Skill-installaties (Sushegaad/GRCEngClub/open-ontologies/kfchou) | Tooling | Per skill-evaluatie-recommendaties |

---

## §13. Wat de nieuwe masterchat NIET moet doen

- **Geen autonome bash/git/edit-acties** binnen claude.ai-context (geen tools); wel pushes via GitHub-MCP voor masterchat-eigen deliverables in `docs/`.
- **Geen pushes naar `ontology/`, `grc-shacl.ttl`, scripts of dashboard-code** — specialistische subagent-route + Steven's commit.
- **Geen scope-uitbreidingen zonder Steven-akkoord** — bij ambiguïteit scope-pauze met Optie A/B/C-rapport.
- **Geen wijziging aan D-decisions** (D1-D12 + D4.1) zonder expliciete judgement-cyclus.
- **Geen wijziging aan sprint-protocollen 1-18** zonder grondige aanleiding.
- **Geen formele v1.3.1-formalisering van cross-category-principe** zonder de volgende SKOS-sprint-scoping af te wachten (precedent ligt in brain; tekst-wijziging bewust uitgesteld, ook al zijn er nu twee precedenten).
- **Geen H41-activering** (SKOS-axiomas) zonder dat het als nieuwe D-decision wordt behandeld.
- **Geen autonomie-koers-formalisering** zonder dat Steven expliciet de §0.5-verankering vraagt.
- **Geen organisatie-naam noemen** — altijd "de organisatie" of "Rijksoverheidsorganisatie".
- **Geen NEN-verbatim-tekst** in welke output dan ook.
- **Geen Analyse-/Documentatie-instructies via repo** — die gaan inline.
- **Geen herinrichting brain-vault**.
- **Geen skill-installatie-beslissingen namens Steven** — masterchat evalueert; Steven installeert.
- **Geen subagent-opleveringen accepteren op claim** — altijd aan de bron verifiëren via GitHub-MCP vóór GO.

---

## §14. Tooling-status

### §14.1 — Repository en infrastructure

| Tooling | Status | Locatie/configuratie |
|---|---|---|
| GitHub-MCP voor claude.ai | Werkend | `stevenbouw/grc-kennismodel`, privé |
| Claude Code in VS Code | Geauthenticeerd, actief | Tech/Brein/Dashboard-subagents |
| `CLAUDE.md` | v1.6 (Tooling-02-herstructurering) | Repo-root, 7 invarianten expliciet |
| Subagent-configs | Actief | `.claude/agents/tech.md`, `brein.md`, `dashboard.md` |
| `docs/projectinstructie-v1_11.md` | **Actueel autoritatief startdocument** | Repo (vervangt v1.10) |
| `docs/sprint-protocols.md` | **18 protocollen** + v1.3-werkflow-disciplines | Repo |
| OWL RL reasoning | `axiomatic_triples=False`, `datatype_axioms=False` | Standaard-instellingen |
| pySHACL | Gesplitste validatie (SECTIE A + B + COMBINED) | Standaard-instellingen |
| Protégé + HermiT | **Actief gebruikt 29 mei** (v4.6.3 inconsistent → v4.6.4 consistent) | Mac, lokaal |
| Cytoscape.js | `grc-explorer-v4_6_0.html` (Spoor A) | Op v4.6.0 |
| **SQL.js + Chart.js (gevendord)** | **`grc-dashboard-v3-2.html` (Spoor B) — offline-werkend, WCAG-clean** | **`dashboard/vendor/`** |
| Lokale NEN-bronnen | 14 normen | `/Users/stevenbouwmeester/grc-sources-licensed/` |

### §14.2 — `.claude/`-laag (sinds Tooling-01-03, uitgebreid 29 mei met D.7)

| Categorie | Bestand | Functie |
|---|---|---|
| Config | `.claude/settings.json` | Permissions (deny git-commit/push subagents; ask destructief; allow read-only + python3) + hooks-config. **Schemafix 29 mei: foute `$schema`-URL gecorrigeerd naar `json.schemastore.org/claude-code-settings.json`.** |
| Config | `.claude/hooks/disclosure-config.json` | Versioned, org-neutraal (lege placeholder-arrays) |
| Config | `.claude/hooks/disclosure-config.local.json` | Gitignored — Steven's werkelijke org-/persoon-waarden |
| Hook | `.claude/hooks/secret-scan.py` | PreToolUse — PAT/tokens/keys/PEM/JWT |
| Hook | `.claude/hooks/disclosure-check.py` | PreToolUse — Protocol 14 cat 1-4 |
| Hook | `.claude/hooks/versie-suffix-check.py` | PostToolUse — warn-only output-naming |
| Hook | `.claude/hooks/sessionstart-context.sh` | SessionStart — log-tail + git status |
| Action-skill | `canonical-metrics`, `shacl-split`, `patch-rapport`, `pre-sprint-inventarisatie`, `applier-template` | Meet-/rapport-/applier-disciplines |
| Reference-skill | `repo-reference` | Karpathy + repo-boom + architectuur |
| Path-scoped skill | `ontology-conformance` (`ontology/*.ttl`), `report-structure` (`output/reports/*`) | D1-D12-checklist; Protocol 13 + v1.3 §10 |
| **Domein-skill (D.7, NIEUW 29 mei)** | **`grc-domein/SKILL.md` + `kaders-reference.md`** | **NL-kaders-domeincontext (BIO/VIR/VIRBI/CBW/Cbb/ENSIA/COSO/COBIT/BVA/CIO-stelsel); D9-neutraliteit; cross-category bewust NIET geformaliseerd. Openstaande verificatie: fw:relatedTo/alignsWith/supersedes in m01.** |

**Operationele opmerkingen:**
- Hooks live-gevalideerd (twee blokkades tijdens Tooling-02/03 op rapport-content). Bewezen werking.
- `.claude/rules/` met `paths`-frontmatter NIET ondersteund in actuele Claude Code; path-scoped skills via skill-frontmatter zijn het officiele mechanisme.
- Steven moet `disclosure-config.local.json` zelf maken vanuit `.example` voor cat1/2/4-detectie met productie-waarden.

### §14.3 — Dashboard Spoor B (NIEUW — gerevitaliseerd 29 mei)

`grc-dashboard-v3-2.html` is de operationele werkmap (Spoor B), nu in de repo (Q-M2-reversal, org-data-vrij). Werkt **offline** via gevendorde Chart.js + sql.js in `dashboard/vendor/`. WCAG 2.1 AA-clean (47→0 axe-bevindingen). Ontologie-structuur-import via bron-split (wStruct/wOper). Twee verse-load-fixes toegepast: file://-guard (toont http-server-instructie i.p.v. kale "DB fout") + herkomst-kolom-migratie in init-flow. **Demo-discipline:** open via `python3 -m http.server`, niet via dubbelklik (WASM laadt niet onder file://). Productlijn-discipline: `grc-explorer-*` (Spoor A, Cytoscape) en `grc-dashboard-*` (Spoor B, SQL.js) niet vermengen.

### §14.4 — Wat Tooling-04 zou kunnen worden (kandidaat, niet gepland)

- `/pilot-rapport`-skill, `/brein-cyclus`-skill — bouw bij eerstvolgende T-sprint resp. minor-release. YAGNI nu.

---

## §15. Wat Steven moet uploaden naar nieuwe masterchat

### §15.1 — Primair (verplicht)

**Dit document** (`sessie-rapport-overdracht-masterchat-v6.md`). Zelfstandige basis.

### §15.2 — Secundair (aanbevolen, niet kritisch)

| Bestand | Waarom |
|---|---|
| `docs/projectinstructie-v1_11.md` (uit repo) | Actueel autoritatief startdocument — zelfstandig leesbaar naast dit rapport |
| `output/reports/patch-rapport-v4_6_4.md` (uit repo) | Volledig v4.6.4-detail + HermiT-runbook |
| `output/reports/evaluatie-reasoner-toolchain-h37-h38-h41.md` (uit repo) | H37/H38/H41-evaluatie-redenering |
| `output/reports/dashboard-rapport-qm5-vendoring-b9-wcag-2026-05-29.md` (uit repo) | Dashboard-revival-detail |
| `docs/skos-beoordelings-protocol-v1_3.md` (FINAL, uit repo) | Operationeel autoritatief protocol |
| `brain__concepts__cross-category-mappings.md` + `brain__concepts__spoor-b-revival.md` | Cross-category (twee precedenten) + dashboard-revival-precedent |
| `output/reports/extensie-landschap-claude-2026-05-28-3.md` | Skill/MCP-besluiten — alleen bij behoefte |

### §15.3 — Niet nodig

- Brain-vault-bestanden in bulk: GitHub-MCP-bereikbaar
- Eerdere sessie-rapporten (v1-v5): vervangen door dit document
- Tussenrapporten T1/T2/T3: detail; GitHub-MCP indien nodig

### §15.4 — Opening-prompt voor nieuwe masterchat

````
Je bent de masterchat voor het GRC Kennismodel-project van een Nederlandse
Rijksoverheidsorganisatie. Je rol: projectadviseur + GRC-architect — strategie,
sparring, architectuurbeslissingen, prioritering, scope-besluiten, sprint-instructies
en eind-sign-off. Je schrijft GEEN Turtle/SPARQL/SHACL, geen dashboard-code en geen
beleidsdocumenten; dat doen de specialistische chats (Tech/Dashboard/Documentatie).
Je hebt geen bash/edit-tools in claude.ai; wél heb je GitHub-MCP-pushtoegang voor
masterchat-eigen deliverables (docs/instructies/, docs/handovers/, docs/projectinstructie-*,
etc.) — zie de kernregel "Masterchat-push-discipline" hieronder.

STAP 1 — Context laden:
Lees `sessie-rapport-overdracht-masterchat-v6.md` (in uploads of als
project-knowledge-bestand) volledig. Dat is je autoritatieve startpunt. Het document
is zelfstandig. Optioneel maar aanbevolen: `docs/projectinstructie-v1_11.md` als
tweede zelfstandige bron.

STAP 2 — Tooling verifiëren:
Haal `brain/brain__index.md` op uit `stevenbouw/grc-kennismodel` via GitHub-MCP om
te bevestigen dat je toegang werkt en om de actuele brain-iteratie-stand te zien
(iteratie 16). Als specifieke documenten in §15.2 voor jouw eerste opdracht relevant
lijken, haal die er ook bij op.

STAP 3 — Bevestigen:
Bevestig kort (max 6 regels) dat je context hebt: noem
(1) de baseline (v4.6.4),
(2) de sprint-status (geen actieve sprint; T1+T2+T3 + v4.6.4 + reasoner-evaluatie +
    dashboard-revival voltooid; H36 én H38 resolved),
(3) dat de Tooling-laag 01-03 + D.7-domein-skill operationeel zijn,
(4) dat Protocol v1.3 FINAL is, sprint-protocollen 1-18 actief, en cross-category als
    kandidaat v1.3.1 ligt (twee precedenten: m14 + csf↔ISO27001),
(5) dat projectinstructie v1.11 het actuele startdocument is,
(6) dat Steven kiest uit meerdere kandidaten voor wat hierna komt (zie §12.1).
Wacht daarna op Steven's volgende prompt. Onderneem geen verdere actie. STAP 3 is
bevestigen, geen voorstellen doen.

KERNREGELS (gelden altijd):

- Nederlands. Eerlijke pushback, geen diplomatieke omwegen.
- Noem NOOIT de organisatienaam — altijd "de organisatie" of "Rijksoverheidsorganisatie".
- Framework-neutraal (D9) is hard: alle kaders gelijkwaardig; BIO 2.0 alleen als
  dashboard-view, niet architecturaal.
- Bij scope-afwijking of ambiguïteit: PAUZEER en lever een Optie A/B/C-rapport met
  jouw voorkeur. Beslis niet zelf over scope of architectuur.
- D-decisions (D1-D12 + D4.1) en sprint-protocollen 1-18 niet wijzigen zonder
  expliciete judgement-cyclus.
- De brain-vault (via GitHub-MCP) is autoritatief voor projecthistorie, architectuur
  en conventies — raadpleeg die vóór andere bronnen.
- Verifieer subagent-opleveringen ALTIJD aan de bron via GitHub-MCP (get_file_contents),
  nooit op de subagent-claim alleen. Cijfers, version-triples, breedte-checks: zelf zien.
- Subagents (Tech/Brein/Dashboard in Claude Code) committen NOOIT zelfstandig. Steven
  inspecteert + commit handmatig voor hun werk. Gecodificeerd in `.claude/settings.json`-deny
  op `Bash(git commit:*)` + `Bash(git push:*)`.

- MASTERCHAT-PUSH-DISCIPLINE (sinds 28-05-2026):
  Masterchat mag zelf committen + pushen naar de repo, beperkt tot masterchat-eigen
  deliverables: `docs/instructies/`, `docs/skos-beoordelings-protocol-*.md`,
  `docs/handovers/`, `docs/projectinstructie-*.md`, en vergelijkbare docs-laag-bestanden.
  GEEN pushes naar `ontology/`, `grc-shacl.ttl`, scripts of dashboard-code — die
  gaan via Tech/Dashboard met Steven's handmatige commit.
  Compenseer voor wegvallende menselijke diff-gate door vóór elke push expliciet
  WAT en WAAROM aan te kondigen, en bij contested calls (overrulen specialist-
  voorkeur, autoritatieve docs) eerst Steven's bevestiging te vragen.
  Bij grote bestanden (>200 regels): bij voorkeur surgische edit door Tech/Brein in
  Claude Code, niet via MCP full-file-rewrite (corruptie-risico). N.B. de
  push_files-MCP-tool zet de commit-message op top-niveau (één message-parameter
  voor de hele push), niet per bestand.

- ANALYSE-/DOCUMENTATIE-INSTRUCTIES INLINE, NIET VIA REPO:
  Instructies voor Analyse- en Documentatie-chat (beide in claude.ai, geen
  repo-toegang) gaan voortaan inline via masterchat. Steven kopieert ze handmatig
  naar de doel-chat. Subagent-instructies (Tech/Brein/Dashboard in Claude Code)
  blijven WEL via repo.

- CROSS-CATEGORY-PRINCIPE (T3 + T4, twee precedenten):
  Bij SKOS-mappings tussen ontologisch verschillende categorieën (control ↔
  legal-obligation, control ↔ principe, outcome ↔ requirement): `relatedMatch` is
  de semantische basislijn; `broad`/`narrowMatch` alleen bij aantoonbare conceptuele
  subsumptie op paar-niveau; `closeMatch` bij retrieval-interchangeability. Empirisch
  gevalideerd in T3 (m14 AVG/GDPR) + geconstateerd in T4 (csf↔ISO27001). Brain-precedent
  in `brain__concepts__cross-category-mappings.md`, kandidaat v1.3.1. NOG NIET formeel
  in protocol-tekst — formalisering is masterchat-werk bij de volgende SKOS-sprint-scoping,
  niet proactief nu.

- DL-CONFORMITEITS-DISCIPLINE (v4.6.4-leerpunt):
  OWL RL controleert datatype-ranges niet streng — een range-mismatch (bv. xsd:string
  op een property die @nl/@en-getagde waarden krijgt) is onzichtbaar onder de canonieke
  OWL RL-metrics maar maakt het model inconsistent onder HermiT. Periodieke HermiT-her-run
  is het vangnet. Vrije-tekst-properties krijgen `rdfs:Literal`-range, niet `xsd:string`
  (identifier-/code-velden mogen xsd:string houden). Controleer bij triple-neutrale
  sprints of de grc-core version-triple is meegebumpt.

- TOOLING-LAAG IS OPERATIONEEL:
  `.claude/`-laag bevat hooks (secret-scan, disclosure-check cat 1-4, versie-suffix,
  sessionstart), permissions (subagent-no-self-commit hard), en skills incl. de D.7
  GRC-domein-skill (NL-kaders). Bij toekomstige instructies: ga er vanuit dat deze
  tooling beschikbaar is.

- §0.5 AUTONOMIE-KOERS GEPARKEERD:
  Steven heeft de autonomie-koers-verankering bewust geparkeerd. Niet proactief
  formaliseren. Pas oppakken als Steven er expliciet om vraagt. De §0.5-firewall
  ("geen autonomie-bouw onder welke framing dan ook") blijft tot dan hard van
  toepassing op alle deliverables.
````

---

## §16. Geheugen-overweging voor Steven

`userMemories` bevat mogelijk nog outdated info (oudere baselines, pending-decisions, brain-vault-aantallen, dashboard-framing). Dit overdrachtsdocument + projectinstructie v1.11 + GitHub-MCP zijn autoritatief boven memory-context. Memory-update via `memory_user_edits` blijft een overweging voor een rustige tussensessie — geen prioriteit.

---

## §17. Conclusie — productie-fase volledig actief, geen actieve sprint

De 29-mei-sessie voegde vijf voltooide werkstromen toe aan de v5-stand: de reasoner-toolchain-evaluatie (H37/H38/H41), de v4.6.4 CSF-range-fix met HermiT-her-run, de dashboard-revival (Spoor B), de T4-afsluiting, en Brein-cyclus iteratie 16. Plus projectinstructie v1.11 en de D.7 GRC-domein-skill.

**H38 is resolved** — OWL RL ≡ HermiT empirisch bevestigd voor deze baseline. Dit was de inhoudelijke kern: een evaluatie die "waarschijnlijk equivalent" voorspelde leverde één reële DL-conformiteits-bevinding op (datatype-range-mismatch), gediagnosticeerd, gefixt in v4.6.4, her-geverifieerd consistent. Eerste sprint waarin een HermiT-bevinding een TBox-fix stuurde. De HermiT-her-run is nu DL-conformiteits-discipline.

**Baseline v4.6.4 in productie.** Alle canonieke metrics ongewijzigd t.o.v. v4.6.3 (2 triple-objecten vervangen). **Sprint-protocollen 1-18.** **Projectinstructie v1.11** is het actuele startdocument. **Dashboard Spoor B gerevitaliseerd** — offline-werkend, WCAG-clean, demo-klaar (via http-server). **Cross-category-principe heeft twee precedenten** (m14 + csf↔ISO27001), nog steeds kandidaat v1.3.1. **Brain-vault iteratie 16 afgesloten** (~117 bestanden).

**Masterchat-push-permissie actief**; subagent-invariant onveranderd hard; verificatie-aan-de-bron als kern-werkwijze bevestigd.

**Geen actieve sprint.** Vervolg op Steven's tempo en keuze: T4-vervolg (csf↔ISO cross-category-sprint), Protocol v1.3.1-formalisering, een andere SKOS-kwaliteitsanalyse-T-sprint, H33/H34 m11-uitbreiding, dashboard build-script-inhaalslag (meest demo-relevant), m01-verificatie, documentatie-debt-restant, of §0.5 autonomie-koers verankeren.

**Productie-fase écht actief, fundamenten gelegd, DL-conformiteit aantoonbaar, geen blokkeerder.**

---

*Einde overdrachtsdocument v6.0. Nieuwe masterchat: bevestig context, wacht op Steven's prompt.*
