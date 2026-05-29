# Instructie Tech-subagent — CSF-description range-fix (v4.6.4)

**Van:** masterchat
**Datum:** 29 mei 2026
**Doel-subagent:** Technisch (Claude Code)
**Sprint:** v4.6.4 — DL-conformiteits-fix (datatype-range-correctie)
**Aard:** **TBox-correctie**, surgisch. Twee range-declaraties wijzigen in één module. Geen ABox-mutatie, geen nieuwe properties/klassen, geen SKOS-wijziging.

---

## 0. Aanleiding

De HermiT-run (Protégé, projecteigenaar, 29 mei 2026) op de volledige merged graph v4.6.3 meldde de ontologie **inconsistent** (`owl:Thing SubClassOf owl:Nothing`), met 8 justificaties. Diagnose (masterchat, geverifieerd aan de bron):

De twee CSF-Tier-description-properties in `m21-csf.ttl` zijn gedeclareerd met `rdfs:range xsd:string`, maar krijgen taal-getagde waarden (`@en`, dus `rdf:langString`). Een volledige DL-reasoner (HermiT) ziet `rdf:langString`-waarden op een `xsd:string`-range als datatype-botsing en verklaart het model inconsistent. OWL RL controleert datatype-ranges niet streng — vandaar `owl:Nothing` = 0 onder de canonieke owlrl-config en 44.907 schone triples; de botsing is onzichtbaar onder OWL RL en zichtbaar onder HermiT. Dit is de H38-vondst (echte OWL-RL/DL-divergentie).

**Breedte vastgesteld (masterchat):** dit is **m21-only, twee properties**. Bewijslijnen:
- HermiT op de volledige merged graph (alle 21 modules), modus "All justifications", gaf precies 8 justificaties = 4 Tiers × 2 properties. Een tagged-waarde-op-`xsd:string` elders zou onafhankelijke justificaties hebben opgeleverd — die zijn er niet.
- Ontwerp-conventie in `grc-core.ttl` is consistent: vrije-tekst-velden gebruiken bewust `rdfs:Literal` (`ext:hasControlStatement`, `ext:hasUVInterpretation`, `ext:hasAttributionText`); `xsd:string` is gereserveerd voor identifier-/code-velden (`csf:csfIdentifier`, `ext:clauseNumber`, `ext:hasCbwArticle`, etc.) die nooit taal-tags dragen.
- m21-scan: de enige taal-getagde waarden buiten label/comment zijn de 8 description-waarden + 2 `ext:hasAttributionText`-waarden — en die laatste zijn veilig omdat `ext:hasAttributionText` al `rdfs:Literal`-ranged is.

De twee description-properties zijn dus de afwijking: vrije-tekst die per ongeluk `xsd:string` kreeg i.p.v. `rdfs:Literal`. Masterchat-besluit: **Optie A — range corrigeren naar `rdfs:Literal`**, conform de bestaande projectconventie.

## 1. De wijziging (exact)

In **`ontology/m21-csf.ttl`**, in de declaraties van `csf:riskGovernanceDescription` (±regel 5436) en `csf:riskManagementDescription` (±regel 5444), wijzig de range:

- **van:** `    rdfs:range xsd:string ;`
- **naar:** `    rdfs:range rdfs:Literal ;`

Tweemaal — één keer per property. Beide declaratie-blokken bevatten verder identieke regels; gebruik genoeg context (de property-naam + omringende regels) om de juiste `rdfs:range`-regel per blok te raken. De `@en`-tags op de waarden blijven ongemoeid; alleen de range-declaratie verandert.

**Niets anders wijzigen.** Geen `@nl`-vertalingen toevoegen (dat is een aparte, latere inhoudelijke keuze — zie §5). Geen andere properties aanraken. `ext:hasAttributionText` is al `rdfs:Literal` en blijft zoals het is.

## 2. Verificatie (verplicht)

### 2.1 Canonieke meet-cyclus (versie-suffix v4_6_4)
- `canonical_metrics_v4_6_4.py` → `canonical_metrics_v4_6_4.json`
- `shacl_split_validate_v4_6_4.py` → `shacl_results_v4_6_4.json`
- `file_hashes_v4_6_4.txt`

**Verwachting (te bevestigen, niet aannemen):** pre-inferentie 20.950 en post-OWL-RL 44.907 **ongewijzigd**. De wijziging vervangt in twee triples het object (`xsd:string` → `rdfs:Literal`) — geen triple erbij/eraf, dus tellingen identiek. Klassen/individuals/OP/DP/sameAs/SKOS ongewijzigd. SHACL: SECTIE A = 0, SECTIE B = 0, COMBINED = 290 (identiek). **Als een van deze afwijkt: scope-pauze, meld aan masterchat — dan is er iets anders aan de hand dan een pure range-correctie.**

### 2.2 De bevestigende meting — HermiT moet nu consistent zijn
Na de fix hoort de DL-inconsistentie weg te zijn. Lever een **runbook-stap** voor de projecteigenaar: opnieuw mergen tot `output/verification/merged_asserted_v4_6_4.ttl`, in Protégé laden, HermiT starten — verwacht: **consistent, 0 `owl:Nothing`**. Dit sluit de lus van de H38-vondst. (Subagent kan dit niet zelf draaien; lever de exacte stap.)

De owlrl-zijde mag de subagent wél bevestigen: 0 inconsistenties onder de canonieke owlrl-closure (zoals altijd — OWL RL zag de botsing toch al niet).

## 3. Versie + administratie

- Baseline-bump **v4.6.3 → v4.6.4**. Patch-bump-classificatie (TBox-bugfix, geen functionele uitbreiding).
- `owl:versionInfo` + `owl:versionIRI` in `grc-core.ttl` bijwerken naar 4.6.4 (let op: dit is een tweede gewijzigd bestand naast m21 — meld dat expliciet in het patch-rapport §9 deliverables-tabel, Protocol 16).
- D6-meeliftregel: de edit-scope is de twee property-declaraties in m21 + de version-triples in grc-core. Binnen die scope zijn alle annotaties al tweetalig — geen meelift-schuld.
- Patch-rapport `patch-rapport-v4_6_4.md`, bottom-up (Protocol v1.3 §10.2), §0 uit canonical_metrics-JSON, metrics met scope-annotatie (§10.5), deliverables-tabel met lokaties (Protocol 16).

## 4. Disclosure-check + commit

- Pre-push disclosure-check, vijf categorieën (Protocol 14).
- **Geen autonome commit.** Lever op; de projecteigenaar inspecteert `git status`/`git diff` en commit handmatig. Twee gewijzigde bestanden verwacht: `ontology/m21-csf.ttl` + `ontology/grc-core.ttl` (version-triples), plus de meet-deliverables in `output/`.

## 5. Bewust BUITEN scope

- **Geen `@nl`-vertaling** van de 8 CSF-Tier-descriptions. Dat is een inhoudelijke vertaalkeuze van NIST CSWP 29-tekst, geen conformiteits-fix. Eventueel later als aparte meelift; niet nu.
- Geen wijziging aan andere `xsd:string`-range-properties — die zijn identifier-/code-velden en dragen terecht geen taal-tags.
- Geen SKOS-, ABox- of shape-wijziging.

## 6. Scope-pauze-condities

- Canonical-metrics of SHACL wijkt af van de verwachting in §2.1 → stop, meld.
- HermiT meldt ná de fix nog steeds een inconsistentie (andere bron) → stop, meld met de nieuwe justificaties.
- Meer dan de twee genoemde `rdfs:range xsd:string`-regels blijken op tagged-waarden te botsen → stop, meld (zou de m21-only-conclusie weerleggen).

## 7. H38-uitkomst (context)

Deze fix herziet de H38-evaluatie van "waarschijnlijk equivalent, HOLD" naar "één reële DL-conformiteits-bevinding gevonden en gefixt, daarna her-geverifieerd". De HermiT-her-run (§2.2) levert het bewijs dat de divergentie tussen OWL RL en HermiT op deze constructie is opgelost. Masterchat verwerkt de H38-status + deze fix in het Brein-pakket.
