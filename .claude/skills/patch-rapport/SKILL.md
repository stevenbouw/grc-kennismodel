---
name: patch-rapport
description: Generate the canonical §0-§15 patch-rapport skeleton for a new ontology release (v4.X.Y) in output/reports/patch-rapport-v4_X_Y.md. Enforces: §0 metrics from output/verification/canonical_metrics_v*.json (not from memory — leerpunt v4.3.3), §7 SHACL split-results from shacl_results_v*.json, §9 deliverables-table with explicit locations (Protocol 16), §10 protocol-status-table, §11 parked-items-status (Protocol 10), §12 D1-D12 + D4.1 conformance-check, §15 GO-criteria checklist. Use when a sprint finishes and the patch-rapport needs to be written. Pairs with /canonical-metrics + /shacl-split + /ontology-conformance.
---

# patch-rapport — canoniek §0-§15-skelet

Genereert de v4.X.Y-patch-rapport-structuur conform v4.6.2/v4.6.3-precedent. Codificeert lessons learned (v4.3.3 §0-uit-JSON, v4.6.1 verificatie-scripts-lokatie, T2/T3 §10.2-§10.5 rapport-discipline).

## Wanneer aanroepen

- Sprint-afsluiting na patch-uitvoering
- Tussentijds als skelet-template (markeer §1+§2 "INITIEEL — bottom-up te bevestigen")
- Bij re-publicatie / errata-update van bestaand patch-rapport

## Vooraf — dependencies

Vóór skelet-vulling moet aanwezig zijn:

1. `output/verification/canonical_metrics_v4_X_Y.json` — gemeten via `/canonical-metrics`-skill
2. `output/verification/shacl_results_v4_X_Y.json` — gemeten via `/shacl-split`-skill
3. `output/verification/file_hashes_v4_X_Y.txt` (SHA256 pre/post pour gewijzigde modules)
4. Vorige-versie-baseline-JSON's voor delta-tabellen (v4_X_(Y-1).json)
5. D-conformance-checklist gelopen (`/ontology-conformance`-skill)

Bij ontbrekend dependency: STOP en genereer eerst. Geen "uit memorie" — leerpunt v4.3.3.

## Bottom-up bouw-volgorde (Protocol v1.3 §10.2)

| Volgorde | Sectie | Reden |
|---|---|---|
| 1 | §3 detail-werk per stap | Feitelijke basis-data |
| 2 | §4-§7 onderbouwing + analyse | Volgt uit §3 |
| 3 | §8-§11 hand-off + status | Volgt uit §3-§7 |
| 4 | §12-§13 conformiteit + leerpunten | Volgt uit §3-§11 |
| 5 | §14-§15 prognose-eval + GO-checklist | Volgt uit §3-§13 |
| 6 | §1 aanleiding + §2 scope LAATST | Afgeleid uit alle voorgaande |
| 7 | §0 metrics-tabel LAATST (JSON-vulling) | Synthese eindstaat |

## Canoniek skelet

```markdown
# Patch-rapport v4.X.Y — <korte-naam-sprint>

| Veld | Waarde |
|---|---|
| Versie | v4.X.Y |
| Vorige baseline | v4.X.(Y-1) |
| Sprint | <naam, bv. T3 m14 AVG/GDPR SKOS-audit> |
| Datum | YYYY-MM-DD |
| Uitvoerder | Tech-subagent (Claude Code) |
| Commit + push | Steven (handmatig) |

## §0. Versie + metrics-vergelijking
### §0.1 Vergelijking v4.X.(Y-1) → v4.X.Y
<tabel uit canonical_metrics JSON — UIT JSON, niet uit memorie>
| Metric | v4.X.(Y-1) | v4.X.Y | Δ | Scope |
|---|---:|---:|---:|---|
| triples (pre-inference) | N | N | Δ | global |
| owl:Class | N | N | Δ | global |
| owl:NamedIndividual | N | N | Δ | global |
| owl:ObjectProperty | N | N | Δ | global |
| owl:sameAs | N | N | Δ | D5+D11 |
| skos_mappings_total | N | N | Δ | global |
| skos_mappings_breakdown.exactMatch | N | N | Δ | global |
| skos_mappings_breakdown.closeMatch | N | N | Δ | global |
| skos_mappings_breakdown.broadMatch | N | N | Δ | global |
| skos_mappings_breakdown.relatedMatch | N | N | Δ | global |

### §0.2 <Sprint-specifieke> SKOS-paren-mutatie (scope-annotatie verplicht — §10.5)
<per cluster / module-scope>

### §0.3 File-hash-mutatie
<SHA256 pre/post per gewijzigd .ttl-bestand>

## §1. Aanleiding
<INITIEEL — te bevestigen in §3-§7-iteratie>

## §2. Scope
<INITIEEL — te bevestigen in §3-§7-iteratie>

## §3. Wijzigingen in <module>.ttl
### §3.1 Beschrijving
### §3.2 Mutatie-uitvoering — applier-output
### §3.3 Pre/post-hash <module>.ttl

## §4. Triples-impact + per-metric Δ-tabel
### §4.1 Globale triples
### §4.2 SKOS-breakdown-Δ
### §4.3 Stop-condities canonical metrics

## §5. Klassen / Individuals / Properties-impact
### §5.1 Integriteits-checks (canonical_metrics §integrity_checks)
- dangling_grc_references.count: N (verwacht 0)
- namespace_leakage.count: N (verwacht 0)
- grc_subjects_zonder_type.count: N
- empty_rdfs_labels / empty_rdfs_comments: N / N
- duplicate_owl_Class_decls.count: N (verwacht 0)

## §6. SKOS-mappings paar-uitkomsten + per-cluster-tabel
### §6.1 Pre/post-distributie per cluster (scope-annotatie verplicht — §10.5)
### §6.2 Mutatie-richting-verdeling
### §6.3 Per-paar-uitkomst-tabel (helper-script-output autoritatief — §10.4)
### §6.4 Confidence-verdeling (indien Protocol-v1.3-sprint)

## §7. SHACL-validatie-uitkomsten
### §7.1 Drie metingen (split-validatie — /shacl-split-skill)
| Sectie | Inference | Violations | Verwachting |
|---|---|---:|---:|
| SECTIE A | none | N | 0 |
| SECTIE B | owlrl | N | 0 |
| COMBINED | owlrl | N | ~290 (baseline OWA/CWA) |

### §7.2 COMBINED-meting-detail
<per sourceShape>

### §7.3 SHACL-blinde-vlek bevestiging (indien van toepassing — H39-context)

### §7.4 Stop-condities SHACL

## §8. Sprint-multiplier + sprint-precedent-vergelijking
<triple-multiplier + mutatie-multiplier t.o.v. vorige sprint(s)>

## §9. Deliverables-tabel (Protocol 16 verplicht — expliciete lokaties)
### §9.1 Productie-scripts + outputs
| Type | Lokatie | Beschrijving |
|---|---|---|
| Module | `ontology/<naam>.ttl` | ... |
| Applier | `scripts/apply_patch_v4_X_Y.py` (of equivalent) | ... |

### §9.2 Verificatie-scripts + outputs
| Type | Lokatie | Beschrijving |
|---|---|---|
| Canonical metrics script | `output/verification/canonical_metrics_v4_X_Y.py` | ... |
| Canonical metrics output | `output/verification/canonical_metrics_v4_X_Y.json` | ... |
| SHACL split script | `output/verification/shacl_split_validate_v4_X_Y.py` | ... |
| SHACL split output | `output/verification/shacl_results_v4_X_Y.json` | ... |
| File hashes | `output/verification/file_hashes_v4_X_Y.txt` | ... |

### §9.3 Rapporten
### §9.4 Backup + sprint-instructies

## §10. Sprint-protocollen — geactiveerd / aangepast
### §10.1 Geactiveerde protocollen
### §10.2 Niet-geactiveerde protocollen
### §10.3 Protocol-progressie (indien Protocol-v1.3-sprint)

## §11. Geparkeerde-items-status-update (Protocol 10)
<per H-item dat in deze sprint een status-wijziging kreeg>

## §12. D-decision-conformiteit-check (D1-D12 + D4.1)
<uitvoeren via /ontology-conformance-skill>
| D | Status | Onderbouwing |
|---|---|---|
| D1 | ✅ | Geen cycles in subClassOf; geen owl:Thing in domain/range |
| D2 | ✅ | Turtle-serialisatie behouden |
| D3 | ✅ | 11 namespaces ongewijzigd |
| D4 | ✅ | SKOS predicate-keuze conform §3.1-tabel |
| D4.1 | ✅ | Cross-category-mappings = relatedMatch (geen broadMatch/narrowMatch over categorie-grens) |
| D5 | ✅ | D5_ctrl_bio_sameAs_count = 93 (target = 93) |
| D6 | ✅ | Bilinguale annotaties @nl/@en aanwezig |
| D7 | ✅ | bio:BIOControl + bio:OverheidsMaatregel ongewijzigd |
| D8 | ✅ | Eén isms:SoA_2026 + 93 SoAEntry |
| D9 | ✅ | Framework-neutraliteit gehandhaafd |
| D10 | ✅ | COSO-positie ongewijzigd |
| D11 | ✅ | D11_asset_brug_count = 5 (target = 5) |
| D12 | ✅ | Drie-laags-compliance-patroon gehandhaafd |

## §13. Aandachtspunten + open issues / vervolg
<sprint-specifieke leerpunten, open issues, vervolg-overwegingen>

## §14. Sprint-prognose-evaluatie
<voorspelde-vs-werkelijke triple-Δ, klasse-Δ, mutatie-aantal>

## §15. GO-criteria-checklist
<exhaustieve checklist uit sprint-instructie + Protocol-v1.3-discipline>
| # | Criterium | Status |
|---|---|---|
| 1 | <uit instructie> | ✅ |
| ... | ... | ... |

— Einde patch-rapport v4.X.Y.
```

## Afgedwongen disciplines

### §0 — uit JSON, niet uit memorie (leerpunt v4.3.3)

Workflow:
1. Open `output/verification/canonical_metrics_v4_X_Y.json` + `canonical_metrics_v4_X_(Y-1).json`
2. Citeer rechtstreeks de `global_pre_inference`-velden in §0.1
3. Citeer `skos_mappings_breakdown` voor de SKOS-rij
4. Citeer `d_decision_conformance.D5_ctrl_bio_sameAs_count` + `D11_asset_brug_count` voor §0.1-tabel
5. Δ = nieuw − oud, exact (geen afronding)

NIET: "ik weet uit de vorige sprint dat..." — altijd JSON-bron.

### §7 — uit shacl_results JSON

Workflow:
1. Open `output/verification/shacl_results_v4_X_Y.json`
2. `section_a_none.violations` → §7.1 SECTIE A
3. `section_b_owlrl.violations` → §7.1 SECTIE B
4. `combined_owlrl.violations_total` + `delta_vs_v4_X_(Y-1)` → §7.1 COMBINED
5. `combined_owlrl.violations_per_shape` → §7.2 detail

Bij A>0 of B>0: STOP. Echte violation. Scope-pauze conform Protocol 15.

### §9 — expliciete lokaties (Protocol 16)

Elke deliverable: type + relatief pad vanaf repo-root + één-regel-beschrijving. Geen "zie verificatie-folder" — exacte path zoals `output/verification/canonical_metrics_v4_X_Y.json`.

### §12 — D-conformance via /ontology-conformance

Roep de skill aan: D1-D12 + D4.1-checklist. Bij ❌ of ⚠️: scope-pauze.

### §0+§4+§6 — metrics-tabel-scope-annotatie (Protocol v1.3 §10.5)

Elke metrics-tabel heeft scope-annotatie. Voorbeelden:
- "m14-scope: alleen mutaties in m14-avg-gdpr.ttl"
- "cumulatief T1+T2+T3: alle ctrl↔compl-paren"
- "global pre-inference"

## Wat de skill NIET doet

- Geen ontologie-mutaties
- Geen autonome commit (Steven commit handmatig — §0.5-firewall)
- Geen invulling van inhoudelijke §1+§2 / §3.1-tekst — dat is sprint-specifiek werk
- Geen NEN-verbatim-tekst — Protocol 17 parafrase-discipline geldt

## Trigger-test tegen v4.6.3

Ter validatie van skill-correctheid: het skelet hierboven matched 1:1 met `output/reports/patch-rapport-v4_6_3.md` (sectie-koppen via `grep -E "^## §|^### §"`). Verschil-velden: `<korte-naam-sprint>` / `<module>` / `<sprint-specifieke>` — sprint-afhankelijk in te vullen.

v4.6.3-cijfers (ter sanity-check; uit `canonical_metrics_v4_6_3.json`):

| Metric | v4.6.2 | v4.6.3 | Δ |
|---|---:|---:|---:|
| triples (pre-inference) | 20950 | 20950 | 0 |
| owl:NamedIndividual | 1383 | 1383 | 0 |
| owl:sameAs | 98 | 98 | 0 |
| skos_mappings_total | 1798 | 1798 | 0 |
| skos.broadMatch | 131 | 129 | −2 |
| skos.relatedMatch | 192 | 194 | +2 |
| D5 ctrl↔bio | 93 | 93 | 0 |
| D11 asset-brug | 5 | 5 | 0 |
| SHACL A / B / COMBINED | 0 / 0 / 290 | 0 / 0 / 290 | 0 / 0 / 0 |

Predicate-substitutie binnen totaal (broadMatch → relatedMatch) per T3-besluit Optie C (cross-category D4.1).

## Cross-references

- Canonical metrics: `.claude/skills/canonical-metrics/`
- SHACL split: `.claude/skills/shacl-split/`
- D-conformance checklist: `.claude/skills/ontology-conformance/`
- Rapport-discipline (Protocol v1.3 §10.x): `.claude/skills/report-structure/`
- Sprint-protocollen (autoritatief): `docs/sprint-protocols.md`
- v4.6.3-referentie-rapport: `output/reports/patch-rapport-v4_6_3.md`
- v4.6.2-referentie-rapport: `output/reports/patch-rapport-v4_6_2.md`
