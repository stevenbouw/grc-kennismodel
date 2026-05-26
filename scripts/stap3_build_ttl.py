#!/usr/bin/env python3
"""Stap 3 v4.5.0 builder: 6 Functions + 22 Categories + 106 Subcategories naar m21-csf.ttl."""
import json
from pathlib import Path

data = json.loads(Path("/home/claude/csf_core.json").read_text())

FUNC_NL = {
    "GV": ("Sturen", "GOVERN"),
    "ID": ("Identificeren", "IDENTIFY"),
    "PR": ("Beschermen", "PROTECT"),
    "DE": ("Detecteren", "DETECT"),
    "RS": ("Reageren", "RESPOND"),
    "RC": ("Herstellen", "RECOVER"),
}

# (NL-label, EN-label, IRI-suffix)
CAT_NL = {
    "GV.OC": ("Organisatorische context",     "Organizational Context",                                "OrganizationalContext"),
    "GV.RM": ("Risicobeheersstrategie",        "Risk Management Strategy",                              "RiskManagementStrategy"),
    "GV.RR": ("Rollen, verantwoordelijkheden en bevoegdheden", "Roles, Responsibilities, and Authorities", "RolesResponsibilitiesAndAuthorities"),
    "GV.PO": ("Beleid",                        "Policy",                                                "Policy"),
    "GV.OV": ("Toezicht",                      "Oversight",                                             "Oversight"),
    "GV.SC": ("Risicobeheer cybersecurity-toeleveringsketen", "Cybersecurity Supply Chain Risk Management", "CybersecuritySupplyChainRiskManagement"),
    "ID.AM": ("Activabeheer",                  "Asset Management",                                      "AssetManagement"),
    "ID.RA": ("Risicobeoordeling",             "Risk Assessment",                                       "RiskAssessment"),
    "ID.IM": ("Verbetering",                   "Improvement",                                           "Improvement"),
    "PR.AA": ("Identiteitsbeheer, authenticatie en toegangscontrole", "Identity Management, Authentication, and Access Control", "IdentityManagementAuthenticationAndAccessControl"),
    "PR.AT": ("Bewustzijn en training",        "Awareness and Training",                                "AwarenessAndTraining"),
    "PR.DS": ("Gegevensbeveiliging",           "Data Security",                                         "DataSecurity"),
    "PR.PS": ("Platformbeveiliging",           "Platform Security",                                     "PlatformSecurity"),
    "PR.IR": ("Weerbaarheid technologie-infrastructuur", "Technology Infrastructure Resilience",        "TechnologyInfrastructureResilience"),
    "DE.CM": ("Continue monitoring",           "Continuous Monitoring",                                 "ContinuousMonitoring"),
    "DE.AE": ("Analyse van ongunstige gebeurtenissen", "Adverse Event Analysis",                        "AdverseEventAnalysis"),
    "RS.MA": ("Incidentbeheer",                "Incident Management",                                   "IncidentManagement"),
    "RS.AN": ("Incidentanalyse",               "Incident Analysis",                                     "IncidentAnalysis"),
    "RS.CO": ("Incidentrespons-rapportage en -communicatie", "Incident Response Reporting and Communication", "IncidentResponseReportingAndCommunication"),
    "RS.MI": ("Incidentmitigatie",             "Incident Mitigation",                                   "IncidentMitigation"),
    "RC.RP": ("Uitvoering incidentherstelplan", "Incident Recovery Plan Execution",                     "IncidentRecoveryPlanExecution"),
    "RC.CO": ("Communicatie over incidentherstel", "Incident Recovery Communication",                   "IncidentRecoveryCommunication"),
}
assert set(c["code"] for c in data["categories"]) == set(CAT_NL.keys())

func_iri = {f["code"]: f"csf:{f['name']}" for f in data["functions"]}
cat_iri  = {c["code"]: f"csf:{c['code'].split('.')[0]}_{CAT_NL[c['code']][2]}" for c in data["categories"]}
sub_iri  = {s["code"]: f"csf:{s['code'].replace('.', '_').replace('-', '_')}" for s in data["subcategories"]}


def ttl_literal(s, lang=None):
    assert '"' not in s, f"Unexpected double quote in: {s[:50]}"
    return f'"{s}"@{lang}' if lang else f'"{s}"'


ttl = ["""
# =============================================================================
# v4.5.0 Fase 3 — Stap 3: CSF Core Individuals
# Datum: 2026-05-19
# =============================================================================
# 6 Functions + 22 Categories + 106 Subcategories als csf:-individuals.
# Alle individuals:
#   - rdf:type (Function|Category|Subcategory), owl:NamedIndividual
#   - rdfs:label (bilingual NL/EN voor Function+Category; ID-form @en voor Subcategory)
#   - rdfs:comment @en (NIST CSWP 29 normative statement)
#   - csf:csfIdentifier (originele ID met punt/dash-conventie)
#   - ext:isComponentOf fw:NIST_CSF_2_0 (D-decision Optie A — bestaande precedent uit m17)
#   - ext:sourceAttribution ext:Attr_NIST_CSF_2_0_Core_2024
#   - csf:partOfFunction (Categories) / csf:partOfCategory (Subcategories)
"""]

ttl.append("# --- 6 Functions ---\n")
for f in data["functions"]:
    nl, en = FUNC_NL[f["code"]]
    iri = func_iri[f["code"]]
    ttl.append(f"""{iri}
    rdf:type csf:Function , owl:NamedIndividual ;
    rdfs:label {ttl_literal(nl, 'nl')} , {ttl_literal(en, 'en')} ;
    rdfs:comment {ttl_literal(f['statement'], 'en')} ;
    csf:csfIdentifier {ttl_literal(f['code'])} ;
    ext:isComponentOf fw:NIST_CSF_2_0 ;
    ext:sourceAttribution ext:Attr_NIST_CSF_2_0_Core_2024 .
""")

ttl.append("\n# --- 22 Categories ---\n")
for c in data["categories"]:
    nl_label, en_label, _ = CAT_NL[c["code"]]
    iri = cat_iri[c["code"]]
    parent = func_iri[c["function_code"]]
    ttl.append(f"""{iri}
    rdf:type csf:Category , owl:NamedIndividual ;
    rdfs:label {ttl_literal(nl_label, 'nl')} , {ttl_literal(en_label, 'en')} ;
    rdfs:comment {ttl_literal(c['statement'], 'en')} ;
    csf:csfIdentifier {ttl_literal(c['code'])} ;
    csf:partOfFunction {parent} ;
    ext:isComponentOf fw:NIST_CSF_2_0 ;
    ext:sourceAttribution ext:Attr_NIST_CSF_2_0_Core_2024 .
""")

ttl.append("\n# --- 106 Subcategories ---\n")
for s in data["subcategories"]:
    iri = sub_iri[s["code"]]
    parent = cat_iri[s["category_code"]]
    ttl.append(f"""{iri}
    rdf:type csf:Subcategory , owl:NamedIndividual ;
    rdfs:label {ttl_literal(s['code'], 'en')} ;
    rdfs:comment {ttl_literal(s['statement'], 'en')} ;
    csf:csfIdentifier {ttl_literal(s['code'])} ;
    csf:partOfCategory {parent} ;
    ext:isComponentOf fw:NIST_CSF_2_0 ;
    ext:sourceAttribution ext:Attr_NIST_CSF_2_0_Core_2024 .
""")

block = "\n".join(ttl)
m21_path = Path("/home/claude/v433/m21-csf.ttl")
current = m21_path.read_text()
m21_path.write_text(current + block)
print(f"✓ Block appended to m21-csf.ttl ({len(block):,} chars)")

iri_tab = {
    "functions": {f["code"]: func_iri[f["code"]] for f in data["functions"]},
    "categories": {c["code"]: cat_iri[c["code"]] for c in data["categories"]},
    "subcategories_sample": {s["code"]: sub_iri[s["code"]] for s in data["subcategories"][:5]},
}
Path("/home/claude/csf_iri_table.json").write_text(json.dumps(iri_tab, indent=2, ensure_ascii=False))
print("✓ Saved IRI-tabel")
