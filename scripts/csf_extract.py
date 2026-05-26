#!/usr/bin/env python3
"""CSF Core extract uit CSWP 29 Appendix A — line-by-line state machine.

Structuur in bron:
    GOVERN (GV): <statement first line>
    <statement continuation>
    • <Category title> (XX.YY): <statement first line>
    <statement continuation>
    o XX.YY-NN: <statement first line>
    <statement continuation>
"""
import re
import json
from pathlib import Path

text = Path("/tmp/cswp29_full.txt").read_text(errors='replace')
text = text.replace("\r\n", "\n").replace("\r", "")

# Scope: from earliest "GOVERN (GV):" tot Appendix B
m_start = re.search(r'^GOVERN \(GV\): ', text, re.MULTILINE)
assert m_start, "GOVERN-section niet gevonden"
# Zoek Appendix B PAS NA GOVERN — eerste occurrence staat in TOC vooraan
remainder = text[m_start.start():]
m_end = re.search(r'\nAppendix B|\nCSF Tiers', remainder)
section = remainder[:m_end.start()] if m_end else remainder

# Filter page-headers/page-numbers per regel
def is_page_artifact(s: str) -> bool:
    s = s.strip()
    if not s: return False
    if re.match(r'^NIST CSWP 29\b', s): return True
    if re.match(r'^February \d+, \d{4}$', s): return True
    if re.match(r'^\d+$', s): return True  # bare page number
    if s == "The NIST Cybersecurity Framework (CSF) 2.0": return True
    return False

lines = [line for line in section.split("\n") if not is_page_artifact(line)]

# Regex per regel-type
FUNC_RE = re.compile(r'^([A-Z]+) \(([A-Z]{2})\): (.+)$')
CAT_RE  = re.compile(r'^•\s*(.+?)\s+\(([A-Z]{2}\.[A-Z]{2})\):\s*(.+)$')
SUB_RE  = re.compile(r'^o\s+([A-Z]{2}\.[A-Z]{2}-\d{2,3}):\s*(.+)$')

functions = []
categories = []
subcategories = []
current = None
state = None

def flush():
    global current
    if current is None: return
    current["statement"] = re.sub(r'\s+', ' ', ' '.join(current.pop("statement_lines"))).strip()

for line in lines:
    s = line.strip()
    if not s:
        continue
    
    fm = FUNC_RE.match(s)
    cm = CAT_RE.match(s)
    sm = SUB_RE.match(s)
    
    if fm and not cm and not sm:
        flush()
        current = {
            "code": fm.group(2),
            "name": fm.group(1).strip(),
            "statement_lines": [fm.group(3)],
        }
        functions.append(current)
        state = "function"
    elif cm:
        flush()
        current = {
            "code": cm.group(2),
            "title": cm.group(1).strip(),
            "function_code": cm.group(2).split(".")[0],
            "statement_lines": [cm.group(3)],
        }
        categories.append(current)
        state = "category"
    elif sm:
        flush()
        current = {
            "code": sm.group(1),
            "category_code": sm.group(1).rsplit("-", 1)[0],
            "function_code": sm.group(1).split(".")[0],
            "statement_lines": [sm.group(2)],
        }
        subcategories.append(current)
        state = "subcategory"
    elif state and current is not None:
        current["statement_lines"].append(s)

flush()

print(f"=== Extract-resultaten ===")
print(f"Functions:       {len(functions)} (verwacht 6)")
print(f"Categories:      {len(categories)} (verwacht 22)")
print(f"Subcategories:   {len(subcategories)} (verwacht 106)")

from collections import Counter
cat_per = Counter(c["function_code"] for c in categories)
sub_per = Counter(s["function_code"] for s in subcategories)
print(f"\n=== Verdeling per Function ===")
print(f"{'Func':<6} {'Cats':>6} {'Subs':>6}  {'Verwacht':<20}")
expected = {"GV": (6,31), "ID": (3,21), "PR": (5,22), "DE": (2,11), "RS": (4,13), "RC": (2,8)}
for fc in ["GV","ID","PR","DE","RS","RC"]:
    e_c, e_s = expected[fc]
    actual_c = cat_per.get(fc, 0)
    actual_s = sub_per.get(fc, 0)
    mark = "✓" if (actual_c, actual_s) == (e_c, e_s) else "✗"
    print(f"  {fc:<4} {actual_c:>4} {actual_s:>6}  expected {e_c}/{e_s} {mark}")

print(f"\n=== Sample statements ===")
if functions:
    print(f"Function {functions[0]['code']} ({functions[0]['name']}):")
    print(f"  {functions[0]['statement'][:200]}{'...' if len(functions[0]['statement'])>200 else ''}")
if categories:
    print(f"\nCategory {categories[0]['code']} ({categories[0]['title']}):")
    print(f"  {categories[0]['statement'][:200]}{'...' if len(categories[0]['statement'])>200 else ''}")
if subcategories:
    print(f"\nSubcategory {subcategories[0]['code']}:")
    print(f"  {subcategories[0]['statement'][:200]}{'...' if len(subcategories[0]['statement'])>200 else ''}")

print(f"\n=== Alle Category-titles (raw, voor CamelCase-conversie) ===")
for c in categories:
    print(f"  {c['code']:<6} | {c['title']!r}")

data = {"functions": functions, "categories": categories, "subcategories": subcategories}
Path("/home/claude/csf_core.json").write_text(json.dumps(data, indent=2, ensure_ascii=False))
print(f"\n✓ Saved /home/claude/csf_core.json")
