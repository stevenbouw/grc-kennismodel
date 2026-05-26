# Export patchnotitie — v4.3.1 → v4.6.0
**Script:** `build_grc_explorer_v3.py` (nieuwe versie — zie wijzigingslog)
**Datum:** 21 mei 2026
**Basis:** v4.6.0-snapshot (21 TTL-bestanden, 20.950 triples)
**Source hash (SHA256, gecombineerd):** `3b8d07fc6167514e...`

---

## Delta-overzicht v4.3.1 → v4.6.0

| Metric | v4.3.1 | v4.6.0 | Δ |
|---|---:|---:|---:|
| TTL-modules geladen | 20 | **21** (+m21-csf.ttl) | +1 |
| Triples geladen | 12.681 | **20.950** | +8.269 (+65%) |
| Individuals (nodes in export) | 1.043 | **1.788** | +745 |
| Klassen | — | 199 | — |
| Edges totaal | 3.712 | **7.249** | +3.537 |
| Governance-edges | 147 | **677** | +530 |
| SKOS-edges (export, individual-niveau) | 307 | **1.759** | +1.452 |
| Equivalence-edges (owl:sameAs) | 93 | **93** | 0* |
| CSF-hierarchie-edges | 0 | **491** | +491 |
| Maturity-edges | 0 | **320** | +320 |
| Attribution-edges | 0 | **725** | +725 |
| Namespaces actief | 10 | **11** (+csf:) | +1 |
| Nodes met `csf_id` | 0 | **501** | +501 |
| Nodes met `law_article` | 20† | **65** | +45 |
| Nodes met `description` | 320 | **1.010** | +690 |

\* D11-bruggen zijn class-niveau — architectureel correct niet zichtbaar als edges (zie export-rapport v4.3.0).
† `ext:articleNumber` vervangen door `compl:articleRef` per predicate-consolidatie α (v4.3.3); v3-script gebruikt correct `compl:articleRef`.

---

## Impact per sprint

### v4.3.2 (21 april 2026) — Smart quotes
Geen export-impact: smart quotes zijn label-correcties in rdfs:label-literals. Automatisch meegenomen in v4.6.0-snapshot.

### v4.3.3 (22 april 2026) — D12 + predicate-consolidatie α
**Script-correctie vereist (verwerkt in v3):** `ext:articleNumber` → `compl:articleRef`. In v2 exporteerde `law_article` 0 nodes voor v4.6.0; v3 exporteert 65 nodes correct.

### v4.4.0 — Fase 2: CBW/Cbb
- 26 `ctrl:CBWControl`-individuals → laag 2 (Wet/regelgeving) ✓
- `compl:SupplierExclusionOrder`-individual → laag 2 ✓
- `fw:uitgewerktIn` + `fw:werktUit` → governance-categorie (1+1 triples) ✓
- `ext:hasUVInterpretation` → enrichment-categorie ✓

### v4.5.0 — Fase 3: NIST CSF 2.0
Grootste sprint-impact:
- `csf:`-namespace toegevoegd als 11e namespace ✓
- 497 csf:-individuals (6 Functions + 22 Categories + 106 Subcategories + 363 Implementation Examples + 4 Tiers + 2 TBox) → laag 4 ✓
- `csf:csfIdentifier` op alle 501 csf:-individuals → `csf_id`-veld ✓
- 1.448 nieuwe SKOS-mappings (csf→ext: 749, csf→bio: 699, csf→isms: 4 Tier-mappings) ✓
- CSF-hierarchie-properties (`csf:partOfFunction`, `csf:partOfCategory`, `csf:exemplifies`) → categorie `csf-hierarchy` (491 edges) ✓
- 0 IRI-fragment-fallbacks op 501 csf:-nodes ✓

### v4.6.0 — Fase 4: ENSIA + volwassenheidsmodel
- `fw:ENSIA` gepromoot naar `fw:GRCFramework` → laag 5 ✓ (eerder laag 9 als Guideline)
- `fw:hasAuditDomain` toegevoegd aan GOVERNANCE_PROPS (8 ENSIA-audit-domain-edges) ✓
- 197 isms:-maturity-individuals (5 Levels + 4 Tiers + 32 Capabilities + 160 LevelDescriptions) → laag 5 ✓
- `isms:forCapability` + `isms:atMaturityLevel` + `isms:hasLevelDescription` → categorie `maturity` (320 edges) ✓
- `ext:sourceAttribution` → categorie `attribution` (725 edges, alle nieuwe individuals geattribueerd) ✓
- `csf:CSFTier`-individuals (`Tier_1_Partial` t/m `Tier_4_Adaptive`) → laag 4 ✓
- 2 nieuwe SourceAttribution-individuals correct als nodes aanwezig ✓

---

## Verificatie tegen canonical_metrics_v4_6_0

| Metric | Canonical | Export | Status |
|---|---:|---:|---|
| Triples | 20.950 | 20.950 | ✅ |
| owl:NamedIndividual | 1.383 | 1.788* | ✅ verwacht |
| owl:sameAs | 98 | 93† | ✅ verwacht |
| SKOS-mappings (model) | 1.798 | 1.759‡ | ✅ verwacht |
| Ontologieversie | 4.6.0 | 4.6.0 | ✅ |

\* 1.788 = 1.383 declared NamedIndividuals + 405 implicit individuals (H21, consistent gedrag sinds v4.3.x).
† 5 D11 class-niveau sameAs-bruggen (asset:↔risk:↔isms: OWL Classes) niet in export — architectureel correct.
‡ 39 class-niveau SKOS-mappings niet in export — zelfde patroon als v4.3.x.

---

## Script-wijzigingen v2 → v3 (samenvatting)

| Wijziging | Reden |
|---|---|
| `csf:` namespace + `NS_PREFIX` | D3-revisie v4.5.0 |
| `bepaal_laag()`: csf:→4, isms:maturity→5, ctrl:CBW→2 | Nieuwe node-types |
| `GOVERNANCE_PROPS` uitgebreid (+4 properties) | fw:uitgewerktIn/werktUit/hasAuditDomain, fw:isTranspositieVan |
| `CSF_HIERARCHY_PROPS` nieuw | csf:partOf*, csf:exemplifies |
| `MATURITY_PROPS` nieuw | isms:forCapability/atMaturityLevel/hasLevelDescription |
| `ATTRIBUTION_PROPS` nieuw | ext:sourceAttribution |
| `ENRICHMENT_PROPS` nieuw | ext:hasUVInterpretation |
| `LAAG_NAMEN[5]` bijgewerkt | "Audit & Volwassenheid" |
| `law_article` → `compl:articleRef` | Predicate-consolidatie α (v4.3.3) |
| `csf_id` → `csf:csfIdentifier` | Correcte property-naam |
| Verificatie-targets bijgewerkt | Correcte IRI-namen nieuwe individuals |

---

## Twee architecturele bevindingen (door-rol met heads-up)

**B1 — Laag 5 bevat nu zowel ENSIA als volwassenheidsmodel.** Per instructie §3 aanbeveling is dit correct verwerkt: Laag 5 hernoemd naar "Audit & Volwassenheid". Masterchat kan dit bekrachtigen of alsnog splitsen in Laag 5 (Audit) en Laag 6 (Volwassenheid).

**B2 — "other"-categorie groot (2.819 edges).** Dit zijn inter-individual-properties die niet in een gedefinieerde categorie vallen. Vertegenwoordigt rijke relationele data (hasControlDomain, derivedFrom, responsibleRole, etc.) die momenteel niet gefilterd wordt in de explorer-view. Na UI-modernisering is verdere categorisatie zinvol.

---

**Pre-conditie 3 voor migratie naar Claude Code: VOLDAAN.**
*Dashboard-chat stand-by voor verhuizing naar Claude Code in volgende fase.*
