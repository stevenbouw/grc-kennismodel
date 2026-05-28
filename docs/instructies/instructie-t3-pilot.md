# Instructie — T3 Pilot (Stap 2): m14 AVG/GDPR SKOS-audit

Sprint: T3 | Stap: 2 (pilot) | Baseline: v4.6.2 | Mode: READ-ONLY (analyse, geen patch)
Protocol: skos-beoordelings-protocol-v1.3 (FINAL — vastgesteld door masterchat 28-05-2026)

## Doel
Beoordeel 6 representatieve m14-paren per-paar onder Protocol v1.3, om de methode te
valideren vóór hoofd-uitvoering op alle 31 paren. Geen patch, geen applier, geen
ontologie-wijziging in deze stap (analoog aan T2-pilot).

## Te beoordelen paren
| # | Paar-ID | Subject | Predicaat (huidig) | Object | Evidence-niveau |
|---|---|---|---|---|---|
| 1 | T3-002 | compl:AVG_Art5_1f | broadMatch | ctrl:ISO27002_5_12 | 1 (keten) |
| 2 | T3-014 | compl:AVG_Art32 | closeMatch | ctrl:ISO27002_5_01 | 2 |
| 3 | T3-024 | compl:AVG_Art32 | relatedMatch | ctrl:ISO27002_5_35 | 1 (keten) |
| 4 | T3-008 | compl:AVG_Art25 | relatedMatch | ctrl:ISO27002_8_25 | 1 (keten) |
| 5 | T3-028 | compl:AVG_Art33 | relatedMatch | ctrl:ISO27002_5_26 | 1 (keten) |
| 6 | T3-031 | compl:AVG_Art34 | relatedMatch | ctrl:ISO27002_5_34 | 3 (Tech-analyse) |

## Methode per paar (C1-C4 onder v1.3) + bindende T3-steer
1. GEEN D4.1-disclaimer-logica - er is geen AVG-equivalent van de ENISA-disclaimer.
   Beoordeel puur op SKOS-semantiek.
2. GEEN cluster-convergentie-aanname. Elk paar individueel toetsen. m14-clusters zijn
   semantisch heterogeen; m10-convergentie is NIET overdraagbaar.
3. SEMANTISCHE BASISLIJN = relatedMatch. compl:(legal-obligation) <-> ctrl:(control) is
   een associatieve, cross-schema-relatie. broadMatch/narrowMatch ALLEEN bij aantoonbare
   subsumptie (genus-species) op paar-niveau. Cluster-cardinaliteit (1<->veel) is een
   SIGNAAL, geen mandaat - leid er geen narrowMatch-default uit af.
4. EVIDENCE-HANTERING:
   - Niveau-1/2 (27701:2025 Annex D + Annex F twee-staps-keten): behandel als STERK
     ONDERSTEUNEND bewijs dat een relatie bestaat - NIET als bewijs van het predicaat-type.
     De keten transporteert PIMS-instantiatie-relevantie, niet de kale 27002-control.
     Documenteer de keten-stappen per paar waar gebruikt.
   - Niveau-3: C1+C3 op ISO 27002:2022-tekst + AVG-tekst (EUR-Lex / m14 rdfs:comment).
5. closeMatch-toets: de 2 closeMatch-paren claimen near-interchangeability tussen AVG-artikel
   en control - een sterke claim. Toets expliciet of closeMatch verdedigbaar blijft of naar
   relatedMatch moet (T3-014 in deze sample).

## Output: output/reports/t3-pilot-rapport.md
Per paar: huidig predicaat -> voorgesteld (behoud/mutatie) | confidence (hoog/midden/laag) |
evidence-niveau | C1-C4-oordeel | keten-stappen indien gebruikt | korte rationale.
Geen pre-pilot-projectie per paar (Protocol v1.3 §6).

## Stop-condities (pauze + escalatie naar masterchat)
- confidence "laag" op >=3 van 6 paren
- >=3 voorgestelde mutaties in de 6-sample (verwachting = bevestigings-sprint, overwegend behoud)
- onverwacht patroon dat de methode raakt

## Discipline
- Protocol 14 pre-push disclosure-check (5 categorieen incl. NEN-tekst >10 woorden)
- Parafrase + clausule-verwijzing; GEEN verbatim NEN-tekst >10 woorden
- READ-ONLY: geen patch, geen applier, geen ontologie-wijziging
- Geen autonome commit - Steven inspecteert git status/diff en commit handmatig
