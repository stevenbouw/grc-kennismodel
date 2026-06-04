# START HIER — GRC Kennismodel

*Korte wegwijzer voor wie het project (opnieuw) oppakt. Dit bestand legt niets inhoudelijks uit — het wijst je naar de juiste documenten in de juiste volgorde. Voor de inhoud: volg de links.*

---

## Ben je nieuw? Lees in deze volgorde

1. **`docs/handovers/overdrachtsrapport.md`** — het brede, beginner-gerichte startpunt. Gaat ervan uit dat je nieuw bent met Claude/Claude Code en neemt je mee door doel, setup, repo-structuur, werkwijze (chats/agents/hooks), de brain-vault en de actuele stand. **Lees dit één keer volledig vóór je iets doet.**
2. **`docs/projectinstructie-v1_12.md`** — de autoritatieve, volledig zelfstandige projectinstructie (missie/visie, normenkader, D-decisions, sprint-protocollen, dashboard-stand, open items). Naslag.
3. **`brain/brain__index.md`** — het collectieve geheugen van het project. Toont de actuele iteratie-stand (nu **17**) en verwijst naar alle registers (decisions, sprints, architecture, concepts, modules, sources, workflow, scope).
4. **`docs/handovers/bootstrap-masterchat-v7.md`** — de Master-startprompt. Geef deze aan een nieuwe masterchat in claude.ai om de rol correct op te starten (laadt context, verifieert GitHub-MCP, bevestigt de stand).

Subagent-rollen (Tech/Brein/Dashboard) starten niet via een prompt maar via hun config in `.claude/agents/*.md`, die Claude Code automatisch inleest.

---

## Welke bron heeft gelijk als ze afwijken?

**De brain-vault (`brain/`) is te allen tijde autoritatief** boven de projectinstructie, de README en de overdrachtsdocumenten. Die andere documenten zijn momentopnames; de brain-vault wordt na elke betekenisvolle sessie bijgewerkt (door de Brein-subagent). Bij twijfel: `brain/brain__index.md` + de registers.

---

## Let op — historie van de overdrachtsdocumenten

De actuele ingang is **`overdrachtsrapport.md`** + **`bootstrap-masterchat-v7.md`**. De oudere reeks `sessie-rapport-overdracht-masterchat-v3.md … v6.md` is **historisch** — gebruik die niet als startpunt; ze beschrijven een eerdere stand (vóór de v7-dashboardsessie). Een losse openingsprompt uit een eerdere sessie kan eveneens verouderd zijn; de bootstrap-v7 is leidend.

---

## Waar staat wat (mini-kaart)

| Wil je… | Ga naar |
|---|---|
| het project leren kennen | `docs/handovers/overdrachtsrapport.md` |
| de autoritatieve projectinstructie | `docs/projectinstructie-v1_12.md` |
| de actuele stand + geschiedenis | `brain/brain__index.md` · `brain/brain__log.md` |
| een masterchat starten | `docs/handovers/bootstrap-masterchat-v7.md` |
| de ontologie + validatie | `ontology/` · `output/verification/` |
| het dashboard (Spoor B) | `dashboard/grc-dashboard-v3-2.html` (lokaal draaien — zie README §Quick-start) |
| publieke projectbeschrijving | `README.md` |
| waarom een beslissing zo is | `brain/brain__decisions__D-register.md` |
| open architectuur-vragen | `brain/brain__architecture__H-register.md` |

---

*Actuele stand (4 juni 2026): ontologie-baseline v4.6.4 (stabiel); Spoor B-dashboardwerk actief (v7: reskin + DORA-correctie + IA-herinrichting); twee open besluiten — lege-huls (Pad 1/2) en organisatiestructuur (A/B/C). Voor detail: projectinstructie v1.12 §"OPENSTAANDE ITEMS".*
