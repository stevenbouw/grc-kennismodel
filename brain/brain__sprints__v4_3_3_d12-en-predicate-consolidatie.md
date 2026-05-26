---
type: sprint
id: v4.3.3
title: v4.3.3 — D12 + predicate-consolidatie α (huidige staat)
status: active
date: 2026-04-22
related:
  - v4_3_2_smart-quotes-en-asymmetrie
  - D12_drie-laags-compliance
  - H25_compl-articleRef-domain-spanning
sources:
  - patch-rapport-v4_3_3
  - migratierapport-technisch-v4_3_3
chat-sources:
  - https://claude.ai/chat/7ec4a4dc-7230-4135-96f4-c791e7271656
confidence: high
---

# v4.3.3 — D12 + predicate-consolidatie α

## Status

**Rijke reconstructie.** Huidige actieve baseline van de ontologie (`status: active`, niet superseded).

Bron: `patch-rapport-v4_3_3.md`, `migratierapport-technisch-v4_3_3.md`, tech-chat 13 mei 2026.

## Scope: vijf items

| Item | Inhoud | Triple-impact |
|---|---|---:|
| 1 | D12 formalisering — drie-laags compliance-architectuur | +6 rdfs:comment |
| 2 | 15 REQ_NIS2_*-subjects tweetalige labels | +30 |
| 3 | Predicate-consolidatie α — ext:articleNumber → compl:articleRef | hard delete + 20 migratiees |
| 4 | 6 plain NIS2Req-subjects compl:requirementText@en | +6 |
| 5 | 15 expliciete owl:NamedIndividual-declaraties op REQ_NIS2_* | +15 |

## Item 1 — D12 vastgelegd

[[brain__decisions__D12_drie-laags-compliance]] formeel geregistreerd. Drie lagen:

1. `compl:RegulatoryObligation` — wettelijke verplichting op kader-niveau
2. `compl:LegalObligation` — juridische verplichting op artikel-niveau
3. `compl:ComplianceRequirement` (+ subklasse `ext:NIS2Requirement`) — concrete eis

Implementatie: 3e/4e `rdfs:comment` toegevoegd op drie ankerklassen (`compl:LegalObligation`, `compl:RegulatoryObligation`, `ext:NIS2Requirement`) met expliciete D12-laag-aanduiding tweetalig.

## Item 2 — 15 REQ_NIS2_* tweetalige labels

15 `compl:REQ_NIS2_Art*`-subjects in `m05-compliance.ttl` kregen `rdfs:label@nl` en `rdfs:label@en`. Format: `"Requirement: NIS2 art. X ..."`.

**Subjects:**

- `REQ_NIS2_Art20_1`, `_Art20_2` (2)
- `REQ_NIS2_Art21_a` t/m `_Art21_j` (10)
- `REQ_NIS2_Art23_1`, `_Art23_2`, `_Art23_3` (3)

**Namespace-prefix correctie tijdens uitvoering:** instructie-voorbeelden gebruikten `isms:REQ_NIS2_*`; werkelijke IRI is `compl:REQ_NIS2_*`. Doorgaan zonder pauze (instructie-veld §3.2).

## Item 3 — Predicate-consolidatie α (scope-uitbreiding)

**Oorspronkelijke instructie:** `ext:articleNumber` → `compl:articleRef` op 6 NIS2-subjects.

**Inventarisatie bij uitvoering:** 20 uses (niet 6) — 6 NIS2 + 14 DORA. Masterchat-pauze met Optie A/B/C voorgelegd.

**Masterchat-GO Optie A** (D9-motivatie — framework-neutraliteit vereist gelijke behandeling NIS2 en DORA): volledige consolidatie naar 20 subjects.

### Stap 3a + 3b in m10-nis2-ext.ttl (6 subjects)

`NIS2_Art18`, `_Art19`, `_Art20`, `_Art22`, `_Art23`, `_Art24` → `compl:articleRef "art. N"` (kleine letter, conform NIS2_Art21_a..j-conventie).

### Stap 3a + 3b in m12-dora.ttl (14 subjects)

`DORA_Art5..14, 16..19` → `compl:articleRef "art. N"`. Geen DORA_Art15 in bronmodel.

### Stap 3c in grc-core.ttl

`ext:articleNumber` **hardverwijderd**: TBox-declaratie (5 triples: rdf:type owl:DatatypeProperty + domain compl:ComplianceRequirement + range xsd:string + 2× rdfs:label).

DatatypeProperty-count: 85 → **84**.

## Item 4 — 6 plain NIS2Req requirementText@en

6 `compl:NIS2_Art{18,19,20,22,23,24}`-subjects in `m10-nis2-ext.ttl` kregen `compl:requirementText@en` (was: alleen @nl). **+6 triples.**

## Item 5 — 15 expliciete owl:NamedIndividual-declaraties

15 `compl:REQ_NIS2_*`-subjects kregen expliciete `rdf:type owl:NamedIndividual` (was: geïnferreerd onder OWL RL). Symmetrie met RO (10) en plain NIS2Req (6) die het al expliciet hadden. **+15 triples.**

## Eindstaat v4.3.3 (huidige baseline)

| Metric | Waarde |
|---|---:|
| Pre-inferentie triples | 12.739 |
| Post OWL RL | 29.863 |
| owl:Class | 186 |
| owl:NamedIndividual | 637 |
| owl:ObjectProperty | 140 |
| owl:DatatypeProperty | 84 |
| owl:sameAs | 98 (93 D5 + 5 D11) |
| SKOS-mappings | 346 |
| Inconsistencies | 0 |
| SHACL RUN 1 | 0 |
| SHACL RUN 2 | 290 (bekende false-positives) |

## Geparkeerde bevindingen v4.3.3

- **11 NL-apostrof-hits in m08 lopende tekst** — administratief gesloten. U+2019 is correcte Nederlandse typografie in @nl-annotaties; geen model-wijziging vereist.
- **NamedIndividual-telmethode geformaliseerd:** canonical_metrics-JSON als enige autoritatieve bron; patch-rapport-baselines vanaf nu direct uit JSON, niet uit memoire. Trigger was tellingsdiscrepantie (607→622 in patch-rapport vs 637 in canonical_metrics — patch-rapport was foutief uit memoire opgesteld). Reconciliatie: canonieke definitie `len(set(g.subjects(RDF.type, OWL.NamedIndividual)))` per-module-geparste graph, pre-inference.

## Open architectuur-aandachtspunten post-v4.3.3

- [[brain__architecture__H25_compl-articleRef-domain-spanning]] — `compl:articleRef` heeft `rdfs:domain compl:Obligation`, propageert onder OWL RL op alle 51 articleRef-dragers
- [[brain__architecture__H26_OBL-laag-gap-NIS2]] — art. 18, 19, 22, 24 hebben geen OBL-laag-individual. Bewust of gap?
- [[brain__architecture__H27_gamma-migratie-articleIdentifier]] — voorwaardelijke γ-migratie pen-klaar

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-04-22 | active | v4.3.3 oplevering (huidige baseline) |

— Einde v4.3.3.
