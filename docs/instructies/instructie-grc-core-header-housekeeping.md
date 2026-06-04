# Instructie — grc-core metadata-header housekeeping

**Voor:** Tech-subagent (Claude Code)
**Van:** Masterchat
**Datum:** 4 juni 2026
**Type:** cosmetische/metadata-hygiëne (geen model-semantiek)
**Bestand in scope:** `ontology/grc-core.ttl` (uitsluitend)
**Version-bump:** GEEN — de baseline blijft v4.6.4. Dit is metadata-hygiëne, geen release.

---

## Aanleiding

Bij masterchat-bronreview (4 juni 2026) bleek de metadata-header van `grc-core.ttl`
achtergebleven op pre-v4.x-waarden, terwijl de `owl:versionInfo`/`owl:versionIRI`
correct op 4.6.4 staan (v4.6.4-patch). Drift gladtrekken; geen functionele wijziging.

---

## §A — Comment-block (cosmetisch, 0 triple-delta) — VERPLICHT

In het header-commentblok bovenaan het bestand:

```
# =============================================================================
# GRC Ontologie — Core Module
# Versie: 4.0.0-alpha            <- VOOR
# Datum: 2026-03-19              <- VOOR
# Profiel: OWL 2 DL
# =============================================================================
```

Wijzig naar:

```
# =============================================================================
# GRC Ontologie — Core Module
# Versie: 4.6.4
# Datum: 2026-05-29 (laatste inhoudelijke wijziging; initieel 2026-03-09)
# Profiel: OWL 2 DL
# =============================================================================
```

> N.B. Dit zijn Turtle-`#`-comments, geen annotaties -> 0 triples, D6 niet van toepassing.
> De comment-`Datum` stond bovendien op 2026-03-19 terwijl `dcterms:created` 2026-03-09
> is; de nieuwe regel lijnt uit op `dcterms:created` voor de initiele datum.

---

## §B — `dcterms:modified` (object-vervanging, 0 triple-delta) — VERPLICHT

Op het ontologie-IRI-subject (`<https://grc.example.org/ontology/>`):

```
dcterms:modified "2026-05-21"^^xsd:date ;     <- VOOR
dcterms:modified "2026-05-29"^^xsd:date ;     <- NA  (v4.6.4-datum = laatste inhoudelijke wijziging)
```

`dcterms:created "2026-03-09"^^xsd:date` blijft ongemoeid. Dit vervangt uitsluitend
het object van een bestaande triple -> tellingen invariant.

---

## §C — `rdfs:comment` ontologie-omschrijving (OPTIONEEL — alleen na expliciete GO van projecteigenaar)

> LET OP: dit item is GEEN nul-delta en triggert D6. Voer §C ALLEEN uit als de
> projecteigenaar het expliciet meeneemt. Standaard: overslaan.

De ontologie-`rdfs:comment` is `@nl`-only en inhoudelijk verouderd:

```
rdfs:comment "Formele OWL 2 DL ontologie voor het GRC-domein van een Nederlandse
rijksoverheidsorganisatie. Framework-neutraal model (D9): alle normen, wetten en
kaders zijn gelijkwaardig gemodelleerd. Modules M1-M13 (+ M14-M17 gepland)."@nl ;
```

Vervang door een actuele, **tweetalige** omschrijving (D6 meeliftregel — `@nl` + `@en`
in dezelfde commit), bijvoorbeeld:

```
rdfs:comment "Formele OWL 2 DL ontologie voor het GRC-domein van een Nederlandse
Rijksoverheidsorganisatie. Framework-neutraal model (D9): alle normen, wetten en
kaders zijn gelijkwaardig gemodelleerd. Datamodules M01-M18 + M21 (NIST CSF 2.0);
M19 (ISO 42001) en M20 (ISO 9001) buiten huidige scope."@nl ,
              "Formal OWL 2 DL ontology for the GRC domain of a Dutch central-government
organisation. Framework-neutral model (D9): all standards, laws and frameworks are
modelled as equals. Data modules M01-M18 + M21 (NIST CSF 2.0); M19 (ISO 42001) and
M20 (ISO 9001) out of current scope."@en ;
```

**Effect op tellingen:** +1 `rdfs:comment` (een `@en`-triple erbij) -> pre-inferentie
20.950 -> 20.951; `rdfs_comment_total` en `…_per_lang.en` elk +1. Alle andere metrics
ongewijzigd. Vermeld dit expliciet in de oplever-notitie als §C wordt uitgevoerd.

---

## Conventies & disciplines

- **Geen autonome commit.** Lever de diff op; de projecteigenaar inspecteert
  `git status`/`git diff` en commit handmatig.
- **Scope strikt `grc-core.ttl`.** Raak geen andere module, geen `owl:imports`,
  geen `grc-shacl.ttl`.
- **D6:** §A/§B raken geen annotaties -> geen meelift. §C is zelf de meelift.
- **Geen NEN-/normtekst** geraakt; disclosure-check cat. 5 triviaal schoon.

## Verificatie (lichtgewicht — geen versioned artefacten nodig)

1. **Parse-check** `grc-core.ttl` na de edit (rdflib parse OK).
2. **Invariantie-check (§A+§B only):** draai `canonical_metrics`-telling ad hoc en
   bevestig pre-inferentie = **20.950**, post-OWL-RL = **44.907**, owl:Nothing = 0
   (ongewijzigd t.o.v. v4.6.4). GEEN nieuwe `canonical_metrics_v*.json`/`file_hashes`
   genereren — dit is geen release.
3. **Bij §C:** bevestig pre-inferentie = **20.951** (precies +1) en `rdfs_comment_total`
   +1; geen andere delta.

## GO-criteria

- [ ] §A comment-block bijgewerkt (Versie 4.6.4 / Datum-regel)
- [ ] §B `dcterms:modified` -> 2026-05-29 (object-vervanging)
- [ ] (alleen indien GO) §C `rdfs:comment` tweetalig + actuele module-lijst
- [ ] Parse-check OK
- [ ] Tellingen-invariantie bevestigd (20.950 / 44.907 / owl:Nothing 0 — of 20.951 bij §C)
- [ ] Diff klein en uitsluitend in `grc-core.ttl`
- [ ] Oplever-notitie met diff-samenvatting; geen autonome commit

---

*Einde instructie — grc-core header-housekeeping.*
