# Instructie — Brein-cyclus T3-afsluiting (iteratie 15)

Trigger: T3-sprint afgerond + masterchat-sign-off op v4.6.3 (28 mei 2026).
Bron-rapporten: `output/reports/t3-stap3-eindrapport.md` + `output/reports/patch-rapport-v4_6_3.md`
+ `output/reports/t3-pilot-rapport.md` + `output/reports/t3-pre-sprint-inventarisatie.md`.
Baseline: v4.6.2 → **v4.6.3**.

Brein-rol-grens (ongewijzigd): brain-vault-onderhoud o.b.v. patch-rapport + cross-referentie-
register-bewaking + autonoom bepalen welke bestanden bijwerken. GEEN architectuurbeslissingen,
GEEN ontologie-wijzigingen, GEEN beleid, GEEN strategische interpretatie van patch-rapporten.
Feiten vastleggen, niet herinterpreteren. Subagent commit niet zelfstandig — Steven inspecteert
+ commit handmatig.

## Deel A — Errata-correctie (surgisch, vóór brain-propagatie)

In de T3-rapporten staat een confidence-tellings-discrepantie (door masterchat geconstateerd
bij sign-off). De per-paar-tabel `t3-stap3-eindrapport.md §6.1` is bron-van-waarheid
(Protocol v1.3 §10.4). Correcte cumulatieve stand m14 (31 paren):

- **hoog 27 / middel 4 / laag 0**
- De vier middel-paren: T3-014, T3-026, T3-028, T3-030
- T3-002 is post-masterchat-besluit **hoog** (niet middel) — analoog aan zusterpaar T3-001

Toe te passen via **surgische edit + errata-aantekening** (T-historie bewaren, geen herschrijven
van §-detailtekst — Protocol v1.3 §10.4):

1. `t3-stap3-eindrapport.md`:
   - §6.3 is een verouderde dubbele tabel (20/11) — markeer als errata/verwijder; §6.4 is de
     bedoelde tabel maar telt T3-002 onterecht als middel → corrigeer §6.4 naar 27/4/0
   - §3.2 (T3-004) bevat redactie-restje "5.30 niet relevant" → opschonen
   - Errata-blok bovenaan met verwijzing naar masterchat-sign-off 28-05-2026
2. `patch-rapport-v4_6_3.md §6.4`: corrigeer "Middel 5" → "Middel 4" (27 hoog / 4 middel),
   verwijder T3-002 uit de middel-opsomming; errata-blok bovenaan
3. Patch-impact onveranderd — dit raakt alleen rapport-classificatie-kolommen, niet de TTL-state
   of de canonical metrics (die zijn correct).

## Deel B — Brain-vault T3-close (verwachte set; bevestig autonoom via register-bewaking)

| Bestand | Actie |
|---|---|
| `brain__sprints__T3-skos-bidirectional-audit-m14.md` | NIEUW — T3-sprint-record (3 stappen, 2 mutaties, cross-category-rationale, v4.6.3) |
| `brain__sprints__-register.md` | append T3-entry |
| `brain__decisions__D04_skos-cross-framework.md` | cross-category-rationale als toepassings-precedent; m14-scope toegevoegd aan D4-validatie-historie (D4.1 inactief in T3 — feit vastleggen) |
| `brain__architecture__H36_skos-exactmatch-ctrl-compl-audit.md` | status → **fully closed** (m10 via T1+T2, m14 via T3) |
| `brain__architecture__H39...` | T3-bevestiging SHACL-blinde-vlek voor beide richtingen (active geparkeerd, ongewijzigd) |
| `brain__concepts__skos-beoordelings-protocol.md` | v1.3 = FINAL + toegepast op m14 (31 paren) |
| `brain__modules__M14_avg-gdpr.md` | post-patch SKOS-distributie: 2 closeMatch / 0 broadMatch / 29 relatedMatch |
| `brain__log.md` + `brain__index.md` | T3-entry + baseline → v4.6.3 |

## Deel C — Cross-category-principe (precedent vastleggen, NIET formaliseren)

- NIEUW `brain__concepts__cross-category-mappings.md`: leg het principe vast als T3-empirisch
  precedent — control ↔ legal-obligation = associatief (relatedMatch) als basislijn; broad/narrow
  is categorie-fout; closeMatch-uitzondering bij retrieval-interchangeability (T3-014 + T3-026).
- Markeer expliciet als **kandidaat v1.3.1-precedent** — formele protocol-tekst-wijziging is
  masterchat-werk bij volgende sprint-scoping, NIET nu door Brein.
- H41-kandidaat: declared-evidence uitbreiden met T3 (informatief, ongewijzigde status).

## Deel D — Workflow-wijziging vastleggen (governance-record)

NIEUW of update `brain__workflow__commit-push-werkverdeling.md` (Brein bepaalt exacte bestandsnaam
via register):

- **Werkflow-wijziging 28-05-2026:** masterchat mag voortaan zelf committen + pushen naar de repo
  (eerder uitsluitend Steven). Vastgesteld door Steven.
- **Onveranderd:** subagents (Tech/Brein/Dashboard) committen NOOIT zelfstandig — Steven inspecteert
  + commit handmatig. Deze invariant blijft hard.
- Noteer dat de prozaregels in `projectinstructie` (§ZEVEN CHATS + gedeelde gedragsregels) en het
  overdrachtsrapport hier nog niet op zijn bijgewerkt — dat is een masterchat-actie bij de volgende
  versie-cut (projectinstructie v1.11 / volgend overdrachtsrapport), NIET een Brein-taak.

## Discipline

- Geen autonome commit — Steven inspecteert git status/diff + commit handmatig
- Protocol 14 pre-push disclosure-check (5 categorieën incl. NEN-tekst >10 woorden) op alle nieuwe/
  gewijzigde brain-bestanden
- Cross-referentie-integriteit: registers + index consistent na de updates (geen dangling verwijzingen)
- Geen ontologie-, beleids- of architectuur-wijziging
