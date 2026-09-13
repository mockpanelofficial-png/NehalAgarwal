#!/usr/bin/env python3
"""Lists every `CONFIRM:` note left in the portfolio content, plus missing
profile details. Run this before showing the site to Nehal.

    python3 scripts/list_todos.py
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
db = json.loads((ROOT / "server" / "data" / "db.json").read_text())

site = db["site"]
items = db["items"]

missing = []
if site.get("email", "").endswith("example.com") or not site.get("email"):
    missing.append(f"site.email  -> currently {site.get('email')!r}")
if not site.get("phone"):
    missing.append("site.phone   -> empty (optional)")
if not site.get("resumeUrl"):
    missing.append("site.resumeUrl -> empty (CV/resume PDF link, optional)")
if not site.get("pressUrl"):
    missing.append("site.pressUrl -> empty (hide the hero 'Press Feature' button, optional)")
if site.get("profileImage", "").endswith(".svg"):
    missing.append("site.profileImage -> still the SVG placeholder, needs her real photo")

photo = ROOT / "client" / "public" / "profile-photo.png"
if not photo.exists():
    missing.append("client/public/profile-photo.png -> not present (drop her photo here)")

print("=" * 74)
print(f" NEHAL PORTFOLIO — CONTENT CHECK   ({len(items)} entries, {len(db['timeline'])} timeline steps)")
print("=" * 74)

print("\n[1] PROFILE DETAILS NEEDED FROM NEHAL")
if missing:
    for m in missing:
        print("   -", m)
else:
    print("   all filled in")

print("\n[2] 'CONFIRM:' NOTES INSIDE ENTRIES  (facts to verify / replace)")
found = 0
for it in items:
    notes = re.findall(r"CONFIRM:\s*([^\n]+?)(?:\s*$)", it.get("description", ""), re.S)
    for n in notes:
        found += 1
        print(f"\n   #{found}  [{it['category']}] {it['title']}")
        print("        id:", it["id"])
        print("        ", " ".join(n.split()))
if not found:
    print("   none left")

print("\n[3] PLACEHOLDER ENTRIES  (fill with real items, or delete from /admin)")
placeholders = [i for i in items if "To be added" in i.get("org", "") or "Placeholder" in i.get("summary", "")]
for p in placeholders:
    print(f"   - [{p['category']}] {p['title']}  (id: {p['id']})")
if not placeholders:
    print("   none")

print("\n[4] ENTRIES WITH NO PROOF ATTACHED")
no_proof = [i for i in items if not i.get("proofs")]
print(f"   {len(no_proof)} of {len(items)} entries have no proof file/link yet.")
print("   Attach certificates, photos or links from /admin -> Entries -> edit -> Proof files.")

print("\n[5] CATEGORY BREAKDOWN")
from collections import Counter
for cat, n in Counter(i["category"] for i in items).most_common():
    print(f"   {cat:<18} {n}")

sys.exit(0)
