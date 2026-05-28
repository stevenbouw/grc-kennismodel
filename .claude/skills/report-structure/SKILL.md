---
name: report-structure
description: Rapport-discipline voor patch-rapporten, tussenrapporten en inventarisaties in output/reports/. Bevat de patch-rapport-skelet-verwijzing (zie /patch-rapport-skill), bron-typo-beleid (Protocol 13), en Protocol v1.3 §10.2-§10.5 (bottom-up rapport-bouw, interne tabel-consistentie, helper-script-autoritatief, metrics-tabel-scope-annotatie). Auto-load bij output/reports/*.
paths: output/reports/*, output/reports/**/*
---

# report-structure — schrijfdiscipline voor output/reports/

Voor elke nieuwe of bijgewerkte file in `output/reports/`: deze checklist langs. Geen NEN-verbatim-tekst; alle methodische discipline + verwijzingen.

## 1. File-naming-conventie

Versie-suffix `v4_X_Y` verplicht voor versie-gebonden output (afgedwongen door `versie-suffix-check.py` PostToolUse-hook in `output/reports/inventarisatie-*`, `tussenrapport-*`, `patch-rapport-*`, `scope-pauze-*`, `brein-rapport-*`, `patchnotitie-export-*`, `skos-kwaliteitsanalyse-*`).

Niet versie-gebonden (skip-prefixen): `dashboard-*`, `tooling-*`, `lint-*`, `extensie-*`, `skill-eval-*`, `handover*`, `T2-*`, `T3-*`.

## 2. Patch-rapport — gebruik de skill

Voor `output/reports/patch-rapport-v4_X_Y.md`: roep de skill `/patch-rapport` aan. Die genereert het canonieke §0-§15-skelet conform v4.6.2/v4.6.3-precedent, met §0 dwingend uit `output/verification/canonical_metrics_v*.json` (niet uit memorie — leerpunt v4.3.3) en §9 Deliverables-tabel met expliciete lokaties (Protocol 16).

Skelet-secties (verkort overzicht; voor details: skill `/patch-rapport`):

| § | Inhoud |
|---|---|
| §0 | Tellingen-vergelijking vorige → nieuwe versie — uit canonical_metrics JSON |
| §1-7 | Per Stap delta's + verificaties + samples |
| §8 | Aandachtspunten (Methodologisch / Bron-specifiek / Kwaliteits-indicatoren / Architectuur) |
| §9 | Geparkeerde-items-status-update (Protocol 10) + Deliverables-tabel (Protocol 16) |
| §10 | D-decision-conformiteit-check (D1-D12 + D4.1) |
| §11 | Deliverables |
| §12 | Sprint-prognose-evaluatie |
| §13 | GO-criteria-checklist |
| §14-15 | Optioneel: errata, T-historie |

## 3. Bron-typo-beleid (Protocol 13)

Twee categorieën typo's, verschillende behandeling:

| Categorie | Behandeling | Voorbeeld |
|---|---|---|
| Typo in nieuwe-individu `rdfs:label` | Corrigeer in label; comment behoudt bron-typo | v4.6.0 sheet 6: 4 Cbw-typo's gecorrigeerd in labels |
| Typo in referentie-target (mapping naar bestaand individu) | Behoud typo — referentie-integriteit gaat boven leesbaarheid | v4.5.0 sheet 8 ISO-typo's (categorie 1: niet gemapped, G1) |

**Escalatie:** bij twijfel over categorie-keuze → scope-pauze met voorstel.

## 4. Protocol v1.3 §10.2 — Bottom-up rapport-bouw (verplicht)

Volgorde van rapport-bouw:

| Sectie-volgorde | Reden |
|---|---|
| §3 detail-werk eerst (cluster-beoordelingen, paar-tabellen) | Feitelijke basis-data |
| §4-§7 onderbouwing + analyse | Volgt uit §3 |
| §8-§9 hand-off + verwijzingen | Volgt uit §3-§7 |
| §1 samenvatting + §2 methode LAATST | Afgeleid uit alle voorgaande secties |

**Indien §1 vroeg-invullen onvermijdelijk** (bv. bij raming-werk): expliciet markeren "INITIEEL, TE BEVESTIGEN IN §3-§7-ITERATIE" en in finale versie corrigeren via iteratie-loop.

**Anti-patroon:** §1.1 distributie-tabel invullen vóór §4 detail-werk leidde in T2-pilot tot classificatie-fout (initieel "behoud" → "upgrade" → "behoud" loop). Bottom-up volgorde voorkomt herhaling.

## 5. Protocol v1.3 §10.3 — Interne tabel-consistentie-discipline

Bij rapporten + instructies met meerdere metrics-tabellen die naar elkaar verwijzen of overlappen: **expliciete consistentie-check voorafgaand aan hand-off.**

Praktische test — voor elke twee tabellen die dezelfde metric in andere context tonen:

- Optellingen moeten kloppen: Σ(deelverzamelingen) = totaal
- Definitie-grenzen moeten compatibel zijn (zelfde scope-aanname)
- Bij discrepantie: bron-van-waarheid expliciet aanwijzen (helper-script / canonical metrics JSON)

T2-instructie-leerpunt (patch-rapport §13.2): masterchat-instructie §1 verwachtings-tabel ("m10 related 27") niet consistent met §8 GO-criterium ("m10 related 0") door impliciete cumulatieve-scope-formulering.

## 6. Protocol v1.3 §10.4 — Helper-script-classificatie als bron-van-waarheid

Bij discrepantie tussen handmatige rapport-classificatie en helper-script-output: **helper-script autoritatief** (strikt protocol-letter, §3.1 predicate-doel-tabel + §3.2 sterkte-ordening).

Werkwijze bij discrepantie-vondst:

1. Helper-script-output documenteren in patch-rapport
2. Handmatige rapport-classificatie vergelijken
3. Discrepantie expliciet noemen (welke paren, welke afwijking)
4. Helper-script-classificatie als finale toepassen
5. Bron-rapporten corrigeren via **errata-aantekening** (T-historie bewaren; geen herschrijven van §-detail-tekst)

T2-precedent: T2-S03 + T2-S08-alt-discrepanties in pilot-rapport → errata-blok bovenaan + correctie in Stap 3-rapport §1.1 pilot-referentie-rij. Patch-impact identiek; classificatie-kolom gecorrigeerd voor methodische hygiëne.

## 7. Protocol v1.3 §10.5 — Metrics-tabel-scope-annotatie verplicht

Bij metrics-tabellen in rapporten + instructies: **expliciete scope-annotatie verplicht** (bv. "m10-only" / "m10+m14 cumulatief" / "T-sprint-totaal" / "module-X-scope").

Praktisch:

- Tabel-titel of -caption noemt scope expliciet
- Bij multi-scope-tabellen: rijen of kolommen apart annoteren
- Bij Δ-tabellen (vergelijking v_a vs v_b): scope-grenzen voor beide versies expliciet

Onderbouwing: patch-rapport v4.6.2 §13.2-leerpunt toonde dat impliciete scope-aanname in metrics-tabel-cellen leidt tot interpretatie-discrepantie tussen instructie-secties en tussen instructie en werkelijke uitkomst.

## 8. Pre-hand-off checklist

- [ ] File-naming volgt versie-suffix-conventie (`v4_X_Y`) waar van toepassing
- [ ] Bottom-up gebouwd (§3+ eerst, §1+§2 laatst)
- [ ] Alle metrics-tabellen hebben expliciete scope-annotatie
- [ ] Interne tabel-consistentie geverifieerd (Σ-checks + scope-compatibiliteit)
- [ ] Helper-script-output (canonical_metrics JSON) is bron-van-waarheid voor §0
- [ ] Discrepanties helper-script ↔ handmatig: errata-aantekening, T-historie bewaard
- [ ] Bron-typo's per Protocol 13 (nieuwe label corrigeren; referentie-targets behouden)
- [ ] Protocol 14 disclosure-check (cat 1-4): hook draait automatisch op Write/Edit
- [ ] §9 Deliverables-tabel met expliciete relatieve lokaties (Protocol 16)

## Cross-references

- Patch-rapport-skelet-generator: `.claude/skills/patch-rapport/SKILL.md`
- Verificatie-skills: `.claude/skills/canonical-metrics/`, `.claude/skills/shacl-split/`
- Versie-suffix-conventie + hook: `.claude/hooks/versie-suffix-check.py`
- Disclosure-check: `.claude/hooks/disclosure-check.py` + `disclosure-config.json` (+ lokale override)
- Sprint-protocollen (autoritatief): `docs/sprint-protocols.md`
- Protocol v1.3 (volledige tekst): `docs/skos-beoordelings-protocol-v1_3.md`
- D-conformance (D1-D12 + D4.1): `.claude/skills/ontology-conformance/SKILL.md`
