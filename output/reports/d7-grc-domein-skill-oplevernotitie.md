# Oplevernotitie — D.7 GRC-domein-skill

**Subagent:** Technisch (Claude Code)
**Datum:** 29 mei 2026
**Opdracht:** `docs/instructies/tech-d7-grc-domein-skill.md` (masterchat, optie B)
**Aard:** skill-bouw, parallel aan dashboard-revival — **geen ontologie-mutatie**

---

## 1. Wat is opgeleverd

| Deliverable | Locatie | Regels |
|---|---|---|
| Skill-hoofdbestand | `.claude/skills/grc-domein/SKILL.md` | 116 |
| Reference-bijlage | `.claude/skills/grc-domein/kaders-reference.md` | 93 |

De skill is **description-triggered** (verschijnt in de skills-lijst zodra `.claude/skills/grc-domein/` bestaat). Geen ontologie-, brain- of dashboard-bestand aangeraakt.

**Inhoud SKILL.md:** §0.5-firewall · §1 D9-neutraliteit (lagen = functioneel, geen hiërarchie) · §2 vijf-lagen-ordening · §3 relatie-semantiek (9 properties + 2 ketens) · §4 SKOS cross-category-basislijn · §5 status-discipline wetgeving · §6 BBN-discipline · §7 NEN-discipline · verificatie-anker.

**Inhoud kaders-reference.md:** §1 per-kader-tabel (26 rijen, type-klasse + jurisdictie + module) · §2 letterlijke geverifieerde relatie-triples met regelnummers · §3 property-definities (domain/range/label) · §4 SKOS cross-category-basislijn-tabel.

## 2. Bron-verificatie (Protocol 4-geest)

Elk feit is aan de bron geverifieerd vóór opname — geen geheugen-tellingen:

| Feit | Bron |
|---|---|
| 9 relatie-properties + domain/range/comment | `ontology/m01-framework.ttl` r.196-291 + `m17-coso-cobit.ttl` r.81-97 |
| Feitelijke relatie-triples (8 fw: + component-relaties) | grep over `ontology/*.ttl` — regelnummers in reference §2 |
| CBW "in voorbereiding" / Cbb "concept t.b.v. Tweede Kamer" | `m01-framework.ttl` r.687, r.707-708 (`fw:status`) |
| BBN via `ext:hasHandreikingBBN`, waarde 1/2 | `grc-shacl.ttl` r.150-163 + `grc-core.ttl` r.272 |
| 11 namespaces | `grc-core.ttl` r.1-11 |
| D9-neutraliteit / BIO 2.0 = view | `brain__concepts__framework-neutraliteit.md` |
| Cross-category relatedMatch-basislijn (kandidaat v1.3.1) | `brain__concepts__cross-category-mappings.md` |

## 3. Trigger-test (4 realistische vragen)

| Vraag | Antwoord uit skill | Sectie | Resultaat |
|---|---|---|---|
| Welke laag is VIRBI? | Laag 2, `fw:VIRBI_2025`, `fw:NationalLaw`, NL, m01+m16 | §2 + ref §1 | ✓ |
| Relatie NIS2 ↔ CBW? | `transposedBy`/`isTranspositieVan`; horizontaal; CBW = "in voorbereiding" | §3 + §5 | ✓ |
| Hoort BBN bij BIO 2.0? | Nee — Handreiking, `ext:hasHandreikingBBN`, 1/2, BBN 3 bestaat niet | §6 | ✓ |
| Is BIO 2.0 het centrale kader? | Nee — D9; view-keuze, geen kern; lagen = functie niet gewicht | §1 | ✓ |

## 4. Disclosure-check (vijf categorieën)

| # | Categorie | Resultaat |
|---|---|---|
| 1 | **Organisatienaam** | ✓ Schoon — grep op ministerie/gemeente/provincie/B.V. levert 0; alleen "de organisatie" / "Rijksoverheidsorganisatie" |
| 2 | **Secrets** (keys/tokens/wachtwoorden) | ✓ Schoon — 0 hits |
| 3 | **NEN-verbatim >10 woorden** | ✓ Schoon — uitsluitend parafrase + clausule-/property-verwijzing; geen geciteerde ISO-normtekst; NEN-discipline expliciet als §7 opgenomen |
| 4 | **Status-discipline** | ✓ CBW "in voorbereiding" + Cbb "concept t.b.v. Tweede Kamer, nog niet vastgesteld" letterlijk conform `fw:status`; DORA als "referentie — organisatie valt er niet onder" |
| 5 | **BBN-correctie + D9** | ✓ BBN expliciet níet als BIO 2.0-eigenschap (§6); D9-neutraliteit als §1 vooropgesteld, BIO 2.0 = view; geen kader als hub |

## 5. Scope-bewaking

Scope-pauze-conditie (skill substantieel groter dan één SKILL.md + beperkte bijlagen, of relatie-matrix vereist gegenereerde ontologie-data) is **niet getriggerd**: de relatie-matrix is volledig af te leiden uit bestaande, in de modules aanwezige triples (geen reasoner-run of data-generatie nodig). Geleverd binnen één SKILL.md + één reference-bijlage, conform §3 van de instructie.

Geen architectuurbeslissing genomen. Het cross-category-principe is uitsluitend als **kandidaat v1.3.1 (niet geformaliseerd — masterchat-werk)** beschreven, niet als vastgesteld protocol.

## 6. Voor de commit (Steven)

Twee nieuwe bestanden, geen wijziging aan bestaande. Voorgestelde message-strekking:

```
docs(.claude/skills): /grc-domein — NL-kaders + vijf-lagen + relatie-semantiek (D.7)
```

Subagent commit niet zelfstandig (invariant). `git status`/`git diff` ter inspectie.

— Einde oplevernotitie.
