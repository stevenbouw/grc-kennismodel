---
type: h-item
id: H27
title: Voorwaardelijke γ-migratie compl:articleRef → compl:articleIdentifier
status: open
date: 2026-04-22
related:
  - H25_compl-articleRef-domain-spanning
  - D12_drie-laags-compliance
  - v4_3_3_d12-en-predicate-consolidatie
sources:
  - patch-rapport-v4_3_3
  - projectinstructie-v1.6
chat-sources:
  - https://claude.ai/chat/7ec4a4dc-7230-4135-96f4-c791e7271656
confidence: high
---

# H27 — Voorwaardelijke γ-migratie compl:articleRef → compl:articleIdentifier

## Status

**Voorwaardelijk open**. Migratie-pad pen-klaar, uitvoer afhankelijk van trigger-criteria.

## Achtergrond

Predicate-consolidatie α (v4.3.3) heeft `ext:articleNumber` hardverwijderd en vervangen door `compl:articleRef`. Geslaagd op 20 subjects (6 NIS2 + 14 DORA), maar de naam `articleRef` is een tussenstap. Een formelere naam zou `compl:articleIdentifier` zijn — geen "Ref"-suggestie van verwijzing, wel een gestructureerd identifier.

## Trigger-criteria voor γ-uitvoering

Migratie wordt overwogen indien **één of meer** van deze condities zich voordoen:

1. **Fase 2 (CBW/Cbb)** of **Fase 4 (AVG)** voegt artikel-referenties toe waarbij "Ref"-naamgeving semantisch tekortschiet
2. **SPARQL-queries** of **dashboard** vereisen een gestructureerder format (decomposeerbaar in artikel/lid/onderdeel — bv. `art. 21, lid 2, onderdeel a`)
3. **VIRBI/BVA** bij implementatie passen niet comfortabel binnen `articleRef`-conventie
4. **[[brain__architecture__H25_compl-articleRef-domain-spanning]]** domain-versoepeling blijkt onvoldoende — γ lost beide problemen tegelijk op

## Migratie-pad (pen-klaar uit masterchat-reply 22 apr)

```turtle
# Stap 1 — TBox-declaratie
compl:articleIdentifier rdf:type owl:DatatypeProperty ;
    rdfs:label "artikel-identifier"@nl, "article identifier"@en ;
    rdfs:comment "Identifier voor artikel-referentie, structureel decomposeerbaar."@nl .

# Stap 2 — owl:equivalentProperty (overgangsfase)
compl:articleIdentifier owl:equivalentProperty compl:articleRef .

# Stap 3 — migratie data-triples
# 20 subjects krijgen compl:articleIdentifier "art. N" toegevoegd

# Stap 4 — deprecate compl:articleRef
compl:articleRef owl:deprecated "true"^^xsd:boolean .

# Stap 5 — na overgangsperiode: hardverwijdering compl:articleRef
```

## Voordelen γ versus H25 Optie 1

- Lost H25 (domain-spanning) op zonder union-domain — `articleIdentifier` is data-property zonder domain
- Naamgeving expressiever, future-proof
- Geen breaking-change tijdens overgangsperiode (equivalentProperty)

## Nadelen γ

- Tweede consolidatie binnen één jaar — administratieve last
- Externe consumers (dashboard) moeten queries aanpassen
- Risico op nieuwe scope-creep (waarom alleen articleRef, niet ook andere "Ref"-naamgevingen?)

## Voorwaardelijke status

Geen automatische trigger. Beslissing volgt na Fase 2-evaluatie wanneer CBW/Cbb-artikel-referenties zijn toegevoegd. Tot die tijd: hold.

## Status-historie

| Datum | Status | Wijziging |
|---|---|---|
| 2026-04-22 | open | Migratie-pad gedefinieerd in masterchat-reply, voorwaardelijk uitvoeren |

— Einde H27.
