# Brein-rapport — iteratie 16 (multi-werkstroom-cyclus, 29 mei 2026)

**Subagent:** Brein (Claude Code)
**Datum:** 2026-05-29
**Cyclus:** iteratie 16 (vijfde post-migratie Brein-cyclus; eerste **multi-werkstroom**-cyclus)
**Instructie:** `docs/instructies/instructie-brein-cyclus-iteratie-16.md`
**Aard:** brain-vault-onderhoud (Protocol 11). Administratieve verwerking van vijf werkstromen uit één masterchat-sessie. Geen architectuur-besluiten autonoom.

---

## §0. Karakter

Anders dan iteraties 12-15 (telkens één sprint → brain-update) bundelt iteratie 16 vijf werkstromen: (1) v4.6.4 TBox-bugfix, (2) reasoner-toolchain-evaluatie H37/H38/H41, (3) dashboard-revival Spoor B, (4) T4-inventarisatie-afsluiting, (5) losse besluiten (Q-M, Protocol 18, Q-M2-reversal, settings.json, D.7-skill, version-drift). Verwerkt in twee batches; alle bron-rapporten aan de bron gelezen vóór propagatie.

**15 bestanden geraakt: 2 nieuw + 12 update brain + 1 docs.**

---

## §1. Aangepaste bestanden per WP

### WP1 — v4.6.4-sprint (baseline ONGEWIJZIGD)

| Bestand | Aard | Wijziging |
|---|---|---|
| `brain__sprints__v4_6_4_csf-range-fix-dl-conformiteit.md` | **nieuw** | TBox-bugfix-sprint; 2× range-fix m21 + version-bump grc-core; baseline 100% identiek aan v4.6.3; H38-lus gesloten; methodologisch precedent (HermiT stuurt TBox-fix); onderscheid met T1/T2/T3 (TBox-range-fix ≠ SKOS-substitutie) expliciet |
| `brain__sprints__sprint-register.md` | update | v4.6.4-rij active; T3 → superseded; v4.6.4 baseline-metrics-blok (alle Δ=0); multiplier-tabel (0×, ander mutatie-type); D-cross-reference (D1 versterkt); geplande-sprints (T4 afgesloten Optie B) |

### WP2 — H38 resolved + H37/H41 parked-met-evaluatie-uitkomst

| Bestand | Aard | Wijziging |
|---|---|---|
| `brain__architecture__H38_owlrl-vs-hermit-equivalentie.md` | update | **parked → resolved**. Volledige boog (blind spot → DL-census → HermiT-vondst datatype-range-mismatch (8 justificaties) → v4.6.4-fix → her-verificatie consistent). Eerste empirisch bewijs OWL RL ≡ HermiT. Frontmatter + status-historie |
| `brain__architecture__H37_open-ontologies-mcp.md` | update | parked, ongewijzigd. Desk-evaluatie-uitkomst (HOLD; Rust+Oxigraph+tableaux+MCP, MIT, v0.1.11; 4 triggers niet actief) + trigger-herijking + status-historie |
| `brain__architecture__H41_skos-axioma-set-handling.md` | update | parked, ongewijzigd. Control-run (SKOS-groei +956 = 100% sameAs, 0% axiomas → verklaart T1/T2/T3 Δ=0) + activerings-impact (+2.831 triples, 12 D4-schendende exactMatch-claims, SHACL 0) + masterchat-regel (activering = nieuwe D-decision) + status-historie |
| `brain__architecture__H-register.md` | update | H38 parked → resolved (parked 7→6, resolved 5→6); H37/H41 parked-rijen verrijkt; iteratie-16-mutaties-sectie; H42/H43/H44 + csf↔ISO27001-kandidaat geregistreerd; toolchain-cluster + D1-tabel |

### WP3 — dashboard-revival + Q-M-besluiten + Q-M2-reversal

| Bestand | Aard | Wijziging |
|---|---|---|
| `brain__concepts__spoor-b-revival.md` | **nieuw** | B7-wiring + bron-split 1A + Q-M5 vendoring + B9 WCAG 47→0; drie Spoor B-bron-besluiten (Optie A·1·1A) als één pakket; twee vervolgpunten (file://-laadgedrag + herkomst-kolom verse load); Brein-registratie alleen |
| `brain__concepts__dashboard-productlijnen.md` | update | Q-M2-reversal (v3-2 mag in repo; locatie-vraag opgelost); zes Q-M-besluiten; naam-actueel- + status-rij; status-historie |
| `brain__concepts__concept-register.md` | update | nieuwe rij spoor-b-revival; dashboard-productlijnen-rij bijgewerkt; cluster + D-cross-refs + sprint-cross-refs |

### WP4 — T4-afsluiting + csf↔ISO27001-kandidaat-precedent

| Bestand | Aard | Wijziging |
|---|---|---|
| `brain__concepts__cross-bron-overlap.md` | update | T4-bevinding: 105 = bron-niveau-getal (v4.5.0), niet machine-reproduceerbaar (block-level provenance); model-meetbaar 245 + 494; per-triple-provenance = open architectuur-vraag; T4 geparkeerd (Optie B); status-historie |
| `brain__concepts__cross-category-mappings.md` | update | tweede cross-category-kandidaat (csf↔ISO27001, 739 paren, gesplitste categorie); drie open subvragen incl. 699-vs-494-reconciliatie; **geen formeel H-nummer**; cross-category-paren-tabel + sprint-cross-refs + status-historie |

### WP5 — Protocol 18-merge + D.7-skill + twee leerpunten

| Bestand | Aard | Wijziging |
|---|---|---|
| `docs/sprint-protocols.md` | update | **Protocol 18** surgisch gemerged (kop 17→18; §18 toegevoegd; canonieke 1-17 ongewijzigd; overzichtstabel-rij; wijzigingsgeschiedenis v1.4) |
| `brain__workflow__workflow-register.md` | update | iteratie-16-additions-sectie: Protocol 18 + D.7-skill (+ openstaande m01-verificatie) + settings.json-leerpunt + version-drift-leerpunt; intro-count → 18 |
| `brain__workflow__sprint-protocollen.md` | update | pointer: canonieke set = 18 (docs/sprint-protocols.md autoritatief); v1.9-momentopname (12) niet bijgewerkt voor 13-18 |

### WP6 — Log + Index

| Bestand | Aard | Wijziging |
|---|---|---|
| `brain__log.md` | update | nieuwe entry bovenaan (iteratie 16, append-only) |
| `brain__index.md` | update | vault-staat-rij 16; baseline v4.6.3→v4.6.4; status-overzicht ververst; v4.6.4 wijzigingen-blok; H-register-entry; volgende-fase; open-punten (locatie Spoor B opgelost); meta-project; folder-tellingen |

---

## §2. Cross-referentie-verificatie-resultaat

- **Wikilink-integriteit:** alle nieuwe wikilink-targets bestaan (geverifieerd: v4_6_4-sprint, spoor-b-revival, D01, M21, skos-export-filter, cross-bron-overlap, cross-category-mappings, H40 — alle OK). Geen dangling links.
- **H38-status-consistentie:** resolved over 8 plekken (H38-bestand, H-register status-overzicht + parked-tabel (verwijderd) + resolved-tabel + iteratie-16-mutaties + D1-tabel, index-entry, sprint-register, sprint-bestand) — consistent.
- **Baseline v4.6.4-consistentie:** alle Δ=0 over index + sprint-register + sprint-bestand + patch-rapport v4.6.4 §0 — consistent.
- **Wederzijdse concept-links:** dashboard-productlijnen ↔ spoor-b-revival; cross-category-mappings ↔ cross-bron-overlap — aanwezig.
- **Protocol 18:** docs/sprint-protocols.md (kop + tabel + §18 + wijzigingsgeschiedenis) ↔ workflow-register ↔ sprint-protocollen-pointer — consistent.
- **Geen orphans:** beide nieuwe bestanden vindbaar via sprint-register resp. concept-register.

---

## §3. Disclosure-check (Protocol 14, vijf categorieën)

| # | Categorie | Resultaat |
|---|---|---|
| 1 | Organisatie-naam | Schoon — "de organisatie"/"Rijksoverheidsorganisatie" waar relevant |
| 2 | Persoonsnamen ≠ Steven | Schoon |
| 3 | Lokale paden buiten repo | Schoon — repo-relatief + `/tmp/grc-wcag-tooling/` (geciteerd uit dashboard-rapport, geen credential) |
| 4 | E-mail / TLD's | Schoon |
| 5 | NEN-tekst-fragment verbatim >10 woorden | Schoon — ISO 27001 alleen clausule-/Annex-A-verwijzing + parafrase (T4); CSF-Tier-descriptions = NIST CSWP 29 publiek domein; control-name-strings = factuele identifiers |

---

## §4. Discipline-bevestiging (rol-grens)

- **Geen architectuur-besluiten autonoom.** H38→resolved volgt masterchat-instructie op de gemeten boog. H37/H41 blijven parked (geen masterchat-besluit tot revisie/activering). H41-activering expliciet vastgelegd als **toekomstige nieuwe D-decision** (niet door Brein/subagent).
- **Geen zelf-gedeclareerde H-items.** csf↔ISO27001 = kandidaat-precedent **zonder formeel nummer** (analoog iteratie 15). H42/H43/H44 zijn **door masterchat** benoemd (besluitnotitie) en als zodanig geregistreerd — niet door Brein gedeclareerd.
- **Geen masterchat-formaliseringen uitgevoerd:** Protocol v1.3.1 (cross-category) niet geformaliseerd; csf↔ISO27001-predicaat-keuze niet beslist.
- **Niet aangeraakt** (buiten brain-scope): `ontology/`, `dashboard/`, `scripts/`, `output/verification/`, `.claude/skills/`, `.claude/settings.json`, `.claude/agents/`. De git-status toont wijzigingen in `output/verification/merged_asserted_v4_6_4.ttl` + nieuwe `catalog-v001.xml`/`merged_asserted_v4_6_3.ttl` — **die zijn NIET van Brein** (tech-werkgebied; vermoedelijk uit de HermiT-runbook-/reasoner-werkstroom). Protocol 18-merge in `docs/sprint-protocols.md` is workflow-doc (toegestaan per instructie).
- **Geen autonome commit.**

---

## §5. Leerpunten voor volgende Brein-cyclus

1. **Multi-werkstroom-cyclus werkt** met WP-structuur + twee batches. Aandachtspunt: de log-entry + index zijn bewust aan het eind in één keer geschreven (i.p.v. half in batch 1) zodat de append-only-entry de volledige iteratie dekt — dit is een afwijking van de strikte batch-1-volgorde uit de instructie, maar voorkomt een onvolledige log-entry. Aanbevolen als standaard bij multi-werkstroom-cycli.
2. **Stale brain-file gesignaleerd:** `brain__workflow__sprint-protocollen.md` liep al achter (lijst 12 protocollen; canoniek 18). Ik heb een pointer toegevoegd i.p.v. de hele lijst te herschrijven (buiten WP5-scope). **Kandidaat voor een lint-/bijwerk-actie** in een latere cyclus: protocollen 13-18 volledig uitwerken in dit workflow-bestand.
3. **version-drift-leerpunt** (grc-core version stond sinds T1 op 4.6.0) is een reëel kandidaat voor een Protocol-aanvulling (version-bump-check bij triple-neutrale sprints) — masterchat-werk.

---

## §6. Open-punten-lijst voor masterchat

1. **HermiT-her-run v4.6.4** — formeel terugmelden dat de her-run consistent was (0 owl:Nothing), om H38-resolved-status definitief te bevestigen (patch-rapport v4.6.4 §8 laatste open checkbox).
2. **csf↔ISO27001 (T4-beslispunten)** — scope-eindpunt (clausule/Annex-A/beide), overlap-definitie (model-19 vs XLSX-her-afleiding), cross-category-predicaat (relatedMatch-basislijn vs closeMatch-behoud), provenance-modellering (block-level vs per-triple). Plus de **699-vs-494-reconciliatie** (T4-rapport §2.2 vs §3.1-B onverklaard) — vóór een eventuele pilot oplossen.
3. **H41-activering** — indien ooit (externe SKOS-audit / DCAT-AP / Spoor B-keten): behandel als **nieuwe D-decision** over reasoner-/SKOS-axioma-configuratie; let op D4-spanning (12 auto-exactMatch-claims) + SKOS↔sameAs-vermenging.
4. **Protocol v1.3.1-formalisering** — cross-category-principe, nu met **twee** precedenten (m14 control↔legal-obligation + csf↔ISO27001 outcome↔requirement/measure). Masterchat-werk.
5. **D.7-skill openstaande verificatie** — bevestigen dat `fw:relatedTo` / `fw:alignsWith` / `fw:supersedes` daadwerkelijk in `m01-framework.ttl` staan (skill veronderstelt dit; masterchat-actie, niet Brein).
6. **Projectinstructie v1.11** — verwerk: commit-push-werkverdeling (28-05), Protocol 18, D.7-skill, Q-M-besluiten + Q-M2-reversal.
7. **Dashboard-vervolgpunten** (geen H-items) — `file://`-laadgedrag (demo-risico) + `herkomst`-kolom verse load. Fix-richtingen in [[brain__concepts__spoor-b-revival]].
8. **Lint-kandidaat** — `brain__workflow__sprint-protocollen.md` bijwerken naar 18 protocollen (zie leerpunt 2).
9. **Confidence-verhoging mapping-bron-disclaimer-effect** (open sinds iteratie 13-15) — vereist tweede onafhankelijke bron-bevestiging.

---

## §7. Commit-voorstel (Steven inspecteert + commit handmatig)

Voorstel: **één cumulatieve commit** voor de Brein-cyclus (de WP's hangen samen via log/index), bv.:

```
docs(brain): Brein-cyclus iteratie 16 — v4.6.4 + H38 resolved + dashboard-revival + T4-afsluiting + Protocol 18
```

Alternatief: per-WP-commits (WP1 sprint, WP2 H-items, WP3 dashboard, WP4 T4, WP5 protocollen/leerpunten, WP6 log+index). **Let op:** de gewijzigde `output/verification/`-bestanden + `catalog-v001.xml`'s in `git status` zijn **niet van Brein** — beslis apart of die meegaan (tech-/reasoner-werkstroom).

— Einde brein-rapport iteratie 16.
