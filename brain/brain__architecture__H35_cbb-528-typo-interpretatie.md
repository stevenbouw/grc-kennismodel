---
type: architecture
id: H35
title: H35 — Cbb 5.28-typo-interpretatie (sheet 8)
status: open
date: 2026-05-19
related:
  - v4_5_0_fase-3-nist-csf-2-0
  - cbw-excel
sources:
  - patch-rapport-v4_5_0
chat-sources: []
confidence: medium
---

# H35 — Cbb 5.28-typo-interpretatie

## Status

**Open** — geregistreerd post-v4.5.0 (19 mei 2026). Trigger: optionele heroverweging bij latere sprint.

## Wat het is

In CBW-Excel **sheet 8 UV 10.4** komt **4× de reference `5.28`** voor zonder `A.`-prefix. ISO 27001-hoofdtekst kent **geen 5.28** (max clauses zijn 4-10), dus dit is vermoedelijk een **typo voor `A.5.28`** = `bio:ISO27002_5_28` (= Annex A-control "Information security in supplier relationships").

In v4.5.0 zijn deze 4 paren **niet gelegd** conform G1 ("bij twijfel niet leggen"). Ze zitten in de 16 unresolved van Stap 5.

## Wat de twee opties zijn

**Optie A — Interpretatieve correctie (manueel)**

`5.28` → `A.5.28` = `bio:ISO27002_5_28` voor deze 4 paren.

| Voor | Tegen |
|---|---|
| 4 extra valide mappings | Bron-aanname zonder bron-bevestiging — schending van bron-verificatie-discipline |
| Compleet beeld voor UV 10.4 | Risico op fout bij nieuwe sheet-versie ADR/NOREA |

**Optie B — Status quo (G1)**

Niet gelegd; gedocumenteerd in §8 van patch-rapport v4.5.0.

| Voor | Tegen |
|---|---|
| Discipline-conform | 4 mappings ontbreken in UV 10.4-cluster |
| Wachten op bron-correctie | — |

## Trigger-criterium

| Trigger | Wanneer Optie A overwegen |
|---|---|
| ADR/NOREA publiceert sheet 8 v2 met correctie | Bron-bevestiging beschikbaar — Optie A wordt automatisch toepasbaar |
| Spoor B-organisatie wil expliciete UV 10.4-mapping-volledigheid | Interpretatieve aanname kan gerechtvaardigd zijn als gedocumenteerde compromis |
| Latere sprint heeft interpretatieve-correctie-sectie | Eenvoudig mee te nemen |

## Confidence: medium

Het is **waarschijnlijk** een typo (hoofdtekst kent geen 5.28; A.5.28 bestaat wel; numeriek dichtbij; context UV 10.4 = supply-chain past bij A.5.28 = supplier relationships). Maar zonder bron-bevestiging niet zeker.

## Bredere context — ADR/NOREA bron-kwaliteits-patroon

H35 is één voorbeeld van een groter patroon: ADR/NOREA-bron is bruikbaar maar structureel licht inconsistent. Cumulatief sinds v4.4.0:

- v4.4.0: 2 typo-categorieën in CBW-Excel sheet 9
- v4.5.0: 19 ISO-normalisaties + 16 unresolved (incl. dit 5.28) + 3 CSF v1.x-namen (`GV.OC-07`, `ID.RM-01`, `PR.AC-02`) in een sept-2025-bron

Relevant voor toekomstig ADR/NOREA-bron-gebruik (bv. v4.6.0 Fase 4 — sheet 6 volwassenheidsmodel).

## Hangt samen met

- [[brain__sources__cbw-excel]] — bron-detail (sheet 8 UV 10.4)
- [[brain__sprints__v4_5_0_fase-3-nist-csf-2-0]] — sprint waar het is waargenomen
- [[brain__workflow__sprint-protocollen]] — bron-verificatie-discipline (rechtvaardigt G1-toepassing nu)

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-05-19 | open | Geregistreerd post-v4.5.0 als optionele heroverweging |

— Einde H35.
