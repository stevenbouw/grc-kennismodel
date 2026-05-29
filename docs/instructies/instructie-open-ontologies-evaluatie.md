# Instructie Tech-subagent — Open-ontologies / reasoner-toolchain-evaluatie (H37 + H38 + H41)

**Van:** masterchat
**Datum:** 29 mei 2026
**Doel-subagent:** Technisch (Claude Code)
**Sprint:** gecombineerde evaluatie-sprint — reasoner-/toolchain-cluster
**Aard:** **EVALUATIE, geen bouw, geen ontologie-mutatie.** Read-only + meet-runs. Geen TTL-wijziging, geen reasoner-configuratie-omschakeling, geen applier, geen patch, geen versie-bump.

---

## 0. Context en doel

Drie geparkeerde architectuur-vragen rond de reasoner-/toolchain raken elkaar en worden in één evaluatie-sprint onderzocht. Bron aan de bron: `brain/brain__architecture__H37_open-ontologies-mcp.md`, `H38_owlrl-vs-hermit-equivalentie.md`, `H41_skos-axioma-set-handling.md` + `brain__concepts__owl-rl-reasoning.md` + `brain__concepts__canonical-metrics.md`.

- **H38** — OWL RL (`owlrl`-package) vs HermiT (Protégé): equivalentie niet geverifieerd sinds v4.0.0. Geeft OWL RL dezelfde inferenties als een volledige DL-reasoner op de huidige baseline?
- **H41** — SKOS-axioma-set-handling: onder de canonieke config (`axiomatic_triples=False, datatype_axioms=False`) laadt `owlrl` geen SKOS-axiomas (skos:S46 symmetrie, skos:S47 transitiviteit). Empirisch bevestigd over T1+T2+T3 (Δ post-OWL-RL = 0). Open vraag: móéten die geactiveerd worden, en wat is de impact?
- **H37** — open-ontologies-MCP (Rust + Oxigraph + tableaux-reasoner, kandidaat `fabio-rovai/open-ontologies`) als alternatief voor de `rdflib`+`owlrl`+`pySHACL`-toolchain. Meerwaarde voor dít project?

**Doel:** een evaluatie-rapport met onderbouwde GO/HOLD/NO-GO per H-item + aanbevelingen aan masterchat. Niets activeren, omschakelen of muteren. De drie blijven geparkeerd tot masterchat op basis van dit rapport beslist.

## 1. Harde invarianten

- **Geen organisatienaam.**
- **Geen ontologie-mutatie, geen reasoner-config-omschakeling in productie.** Meet-runs mogen een SKOS-axioma-geladen variant *vergelijkenderwijs* draaien, maar de canonieke `canonical_metrics`-config blijft ongewijzigd; meet-varianten draaien in een apart script/output, niet als nieuwe baseline.
- **Canonical-metrics-discipline blijft toolchain-onafhankelijk reproduceerbaar** — elke meting met expliciete config + scope-annotatie (Protocol v1.3 §10.5).
- **§0.5-firewall** — evaluatie levert kennis voor een masterchat-besluit; opent geen autonoom pad, activeert niets.
- **Geen autonome commit** — lever op, de projecteigenaar inspecteert + commit handmatig.
- **D1 blijft staan** — H38 betreft de reasoner-*keuze* binnen D1 (OWL 2 DL-profiel), niet D1 zelf. Geen D-wijziging voorstellen zonder masterchat.

## 2. Interne volgorde (H38 → H41 → H37 — niet willekeurig)

H38 is de spil: zowel H41 als H37 noemen de HermiT-run als hun eigen referentie/trigger. Een DL-baseline maakt de andere twee pas meetbaar. Daarom:

### Stap 1 — H38 (HermiT-equivalentie, levert de DL-referentie)

Volg de aanpak uit `H38`-bestand §"Aanpak bij activering":
1. v4.6.3 merged graph laden in Protégé (Mac, lokaal — stand-by per tooling-status).
2. HermiT activeren, inferred axioms exporteren naar TTL.
3. Vergelijken met `owlrl`-output (triple-set-diff).
4. Per delta-triple: kritiek voor model-semantiek of randverschijnsel?
5. Rapport-sectie met de diff + oordeel.

**Realiteits-check:** Protégé/HermiT is een lokale-Mac-actie buiten Claude Code. Als de subagent dit niet zelf kan uitvoeren, lever dan een **exact uitvoerbaar runbook** voor de projecteigenaar (welke stappen, welke export, welk diff-script) + een `owlrl`-zijde-script dat de subagent wél kan draaien, zodat de diff zodra de HermiT-export er is met één commando volgt. Niet stilzwijgend overslaan — expliciet markeren wat subagent-uitvoerbaar is en wat projecteigenaar-actie vergt.

### Stap 2 — H41 (SKOS-axioma-impact, gemeten tegen de DL-referentie)

Volg `H41`-bestand §"Aanpak bij activering", **als vergelijkende meting, niet als omschakeling**:
1. Draai een meet-variant met SKOS-axiomas geladen (`axiomatic_triples=True` of expliciete SKOS-axioma-graph) — in apart script/output, canonieke baseline ongemoeid.
2. Δ post-OWL-RL triples mét vs. zonder SKOS-axiomas, per cluster.
3. SHACL-impact: combined-mode met geactiveerde SKOS-axiomas vs. de 290-false-positive-baseline — welke shapes raken SKOS-inverse/transitieve triples?
4. Cross-namespace-transitiviteits-check: welke ketens ontstaan impliciet (bv. CSF → ISO → BIO via exact/broadMatch)? Gewenst of ongewenst?
5. Koppel aan H38: laadt HermiT de SKOS-axiomas wél? Zo ja, is dat (deel van) de H38-delta?

### Stap 3 — H37 (alternatieve toolchain, met H38+H41 als input)

1. Karakteriseer `fabio-rovai/open-ontologies` op basis van publieke bron (README/docs) — reasoner-type, triplestore, MCP-interface, release-volwassenheid, licentie. **Niet installeren/integreren** — desk-evaluatie.
2. Weeg tegen de huidige toolchain op de assen uit het H37-bestand (reasoner-dekking, performance, Protégé-integratie, black-box-risico, migratie-kosten).
3. Gebruik de H38- + H41-uitkomsten: áls OWL RL relevante DL-inferenties mist (H38) óf SKOS-axioma-handling materieel blijkt (H41), stijgt de relevantie van een sterkere reasoner. Zo niet, dan bevestigt dat "geen trigger".
4. GO/HOLD/NO-GO met expliciet "waarom geen GO" én "waarom geen NO-GO".

## 3. Deliverable

- Rapport: `output/reports/evaluatie-reasoner-toolchain-h37-h38-h41.md` (bottom-up bouw, Protocol v1.3 §10.2; metrics met scope-annotatie §10.5; tabel-consistentie §10.3).
- Per H-item: bevinding + GO/HOLD/NO-GO + onderbouwing + (waar van toepassing) trigger-herijking.
- Eventuele meet-scripts in `scripts/` (read-only / vergelijkend; geen productie-config-wijziging).
- HermiT-runbook voor de projecteigenaar indien Protégé niet subagent-uitvoerbaar is.
- Oplevernotitie met disclosure-check (vijf categorieën).

## 4. Scope-pauze-condities

- Als de HermiT-diff (H38) een **substantiële, model-semantisch kritische** delta toont → stop, escaleer met Optie A/B/C; ga niet zelf een reasoner-config wijzigen.
- Als een meet-variant (H41) onverwacht de canonieke baseline raakt of de 290-SHACL-baseline verschuift → stop en meld.
- Als H37-evaluatie een installatie/integratie zou vereisen om zinvol te oordelen → stop; installatie is een apart masterchat-besluit, geen onderdeel van deze desk-evaluatie.
- Elke structurele verrassing buiten evaluatie-scope → Optie A/B/C naar masterchat.

## 5. Wat NIET

- Geen reasoner-configuratie omschakelen als productie-default.
- Geen open-ontologies-MCP installeren of integreren (desk-evaluatie only).
- Geen TTL-mutatie, geen SKOS-axioma's permanent activeren, geen patch/versie-bump.
- Geen D-decision wijzigen of voorstellen-als-besluit (alleen als overweging rapporteren).
- Geen autonome commit.

## 6. Afsluiting

Dit is een evaluatie die drie geparkeerde H-items van "vermoeden" naar "gemeten" brengt, zodat masterchat per item kan beslissen of de parked-status blijft, een trigger wordt geactiveerd, of een vervolgsprint nodig is. De drie blijven parked tot dat masterchat-besluit.
