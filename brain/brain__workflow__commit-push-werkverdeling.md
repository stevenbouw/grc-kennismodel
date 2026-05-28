---
type: workflow
title: Commit + push-werkverdeling — wie commit en pusht naar de repo
status: living
date: 2026-05-28
related:
  - zes-chat-architectuur
  - sprint-protocollen
  - opleveringsprotocol
  - scope-discipline
sources:
  - masterchat-besluit-28-05-2026
chat-sources: []
confidence: high
---

# Commit + push-werkverdeling — wie commit en pusht naar de repo

## Wat dit regelt

Dit document legt de operationele werkverdeling vast voor `git commit` + `git push` naar de project-repository (`grc-kennismodel`). Onderscheid tussen wie autonoom mag committen + pushen en wie via Steven moet (subagents).

## Werkverdeling 28-05-2026 (huidige stand)

| Actor | Mag autonoom commit + push? | Voorwaarde |
|---|---|---|
| **Masterchat (claude.ai)** | **Ja, sinds 28-05-2026** | Voldoende inzicht in repo-state; gebruikt eigen `bash`-tool via Steven's terminal-sessie waar nodig of via repo-toegang |
| **Steven (projecteigenaar)** | Ja, altijd | Tussenmens-rol blijft mogelijk (handmatige commit na inspectie) |
| **Tech-subagent (Claude Code)** | **Nee, NOOIT zelfstandig** | Levert wijzigingen op werkende-tree; Steven inspecteert + commit handmatig |
| **Brein-subagent (Claude Code)** | **Nee, NOOIT zelfstandig** | Levert brain-vault-wijzigingen op werkende-tree; Steven inspecteert + commit handmatig |
| **Dashboard-subagent (Claude Code)** | **Nee, NOOIT zelfstandig** | Levert dashboard-wijzigingen op werkende-tree; Steven inspecteert + commit handmatig |

**Vastgesteld door:** Steven (projecteigenaar) op 28 mei 2026, na T3-sprint-afsluiting.

## Onderbouwing van het invariant — subagents committen NOOIT zelfstandig

De **hard invariant** dat subagents niet zelfstandig committen blijft van kracht ondanks de werkflow-wijziging voor masterchat. Onderbouwing:

1. **Disclosure-discipline** — Protocol 14 pre-push-disclosure-check (5 categorieën inclusief NEN-tekst >10 woorden) vereist menselijke inspectie vóór elke push. Subagents kunnen deze check zelf uitvoeren maar de **finale verantwoordelijkheid voor push** blijft bij Steven (projecteigenaar) wegens publiek-domein-licentie-risico.
2. **Scope-discipline** — subagents kunnen tijdens uitvoering scope-pauze-momenten missen of verkeerd interpreteren; Steven's inspectie van diff vangt dit op vóór git-history-vervuiling.
3. **Cross-chat-state-bewustzijn** — subagents zien repo-state op moment van sessie-start; tussen-sessie-wijzigingen (van masterchat of andere subagent) vereisen Steven als sync-controleur.
4. **Niet-omkeerbare hist** — git-history is publiek-zichtbaar; verkeerd commit-bericht of NEN-tekst-lekkage is niet stilletjes terug te draaien.

Subagents leveren dus op werkende-tree (file edits + `output/reports/*.md`-rapporten); Steven doet de inspectie + `git add` + `git commit -m "..."` + `git push` handmatig op zijn lokale terminal.

## Werkflow-wijziging 28-05-2026 — masterchat mag voortaan zelf committen + pushen

**Eerdere stand:** uitsluitend Steven committed + pushed naar de repo. Masterchat schreef sprint-instructies + reviewde patch-rapporten; commit + push verliep via Steven's handmatige inspectie + uitvoering.

**Nieuwe stand sinds 28-05-2026:** **masterchat mag voortaan zelf committen + pushen naar de repo**. Vastgesteld door Steven na T3-sprint-afsluiting. Operationele context: masterchat heeft repo-toegang via terminal-tool of via Steven's machine-sessie en kan inspectie + commit + push direct uitvoeren wanneer praktisch.

**Onveranderd:** Steven blijft tussenmens-rol kunnen vervullen wanneer hij wil; masterchat-autonomie is een toegestane optie, niet een verplichting.

**Onveranderd:** subagents committen NOOIT zelfstandig — invariant blijft hard (zie onderbouwing hierboven).

## Pending documentatie-bijwerking (niet Brein-taak)

Volgende documenten zijn **nog niet bijgewerkt** op deze werkflow-wijziging — dit is masterchat-actie bij volgende versie-cut, NIET een Brein-taak:

| Document | Vereiste wijziging | Wie |
|---|---|---|
| `docs/instructies/projectinstructie-v1_*.md` (volgende versie v1.11) | §ZEVEN CHATS-rolverdeling + gedeelde gedragsregels-sectie aanvullen met masterchat-commit-autonomie + subagent-invariant | Masterchat bij volgende versie-cut |
| Volgend overdrachtsrapport / master-handover | Werkflow-update incorporeren in overdrachtsbeschrijving | Masterchat bij volgende overdrachtsrapport |
| [[brain__workflow__zes-chat-architectuur]] post-migratie-werkproces-blok | Stap 2 + 4 + 7 (push naar GitHub) explicieter koppelen aan masterchat-autonomie | Brein bij volgende cyclus indien projectinstructie bijgewerkt is (chronologisch volgens leidend principe: projectinstructie is autoritatief, brain volgt) |

**Brein-cyclus iteratie 15 (28-05-2026):** dit workflow-bestand vastgelegd. Bijwerking projectinstructie en overdrachtsrapport blijft expliciet buiten Brein-scope conform werkverdeling Tech/Brein/Dashboard ↔ Master/Documentatie ([[brain__workflow__zes-chat-architectuur]]).

## Activerings-momenten

Werkflow-wijziging is **direct van kracht** sinds vaststelling 28-05-2026. Subagents (Tech/Brein/Dashboard) blijven ongewijzigd opereren — leveren op werkende-tree, geen autonome commits. Het verschil is zichtbaar in de git log: commits zullen vanaf 28-05-2026 zowel van Steven als van masterchat kunnen komen (commit-author en commit-message-conventie kan masterchat-eigen worden).

**Commit-message-conventie (ongewijzigd):**

- Onveranderd; volgt bestaande projectconventies in `docs/sprint-protocols.md` en bestaande git-history-stijl (semantische type-prefix: `feat:`, `fix:`, `docs:`, `release:`, `chore:`, etc.)
- Masterchat-commits hoeven niet expliciet "via masterchat" te taggen — git-author-velden zijn voldoende voor herleiding

## Wat NIET in dit workflow-bestand zit

- **Branch-strategie** (master vs feature-branches) — niet gewijzigd door deze werkflow-update; main blijft enige werkbranch tot organisatorische trigger voor branching opdoemt
- **PR-procedure** — geen PRs gebruikt; commits gaan direct naar main
- **CI/CD-trigger-discipline** — geen CI in repo; lokale verificatie blijft norm
- **Spoor B-overgang-werkflow** — bij verschuiving naar GitLab-on-prem of organisatie-interne git wordt deze werkverdeling herzien (zie CLAUDE.md Spoor B-overweging)

## Cross-references

- [[brain__workflow__zes-chat-architectuur]] — rolverdeling tussen chats; commit-werkverdeling is operationele uitwerking daarvan
- [[brain__workflow__sprint-protocollen]] — Protocol 14 (pre-push disclosure-check) blijft toepasselijk op alle commits ongeacht actor
- [[brain__workflow__opleveringsprotocol]] — release-artefacten-conventie blijft van kracht
- [[brain__workflow__workflow-register]] — workflow-overzicht
- [[brain__workflow__scope-discipline]] — scope-pauze-route bij twijfel (subagent → Steven → masterchat)
- CLAUDE.md repo-root — cross-chat-bewustzijn + sprint-werkproces (samenvatting)

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-28 | living | Concept ontstaan uit Brein-cyclus iteratie 15 (T3-afsluiting) — werkflow-wijziging vastgesteld door Steven: masterchat mag voortaan zelf committen + pushen; subagents committen NOOIT zelfstandig (invariant blijft hard); pending documentatie-bijwerking voor projectinstructie + overdrachtsrapport bij volgende versie-cut (masterchat-taak, niet Brein) |

— Einde commit-push-werkverdeling.
