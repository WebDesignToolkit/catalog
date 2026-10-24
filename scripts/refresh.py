#!/usr/bin/env python3
"""Explicit local refresh; requires gh CLI; never reviews/promotes candidates."""
import datetime,json,subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
path=root/"data/resources.json"
records=json.loads(path.read_text(encoding="utf-8"))
today=datetime.datetime.now(datetime.timezone.utc).date().isoformat()
errors=[]
for item in records:
    result=subprocess.run(["gh","api","repos/"+item["repository"]],capture_output=True,text=True,encoding="utf-8")
    if result.returncode:
        errors.append(item["repository"]);continue
    obj=json.loads(result.stdout)
    lic=(obj.get("license") or {}).get("spdx_id")
    item.update(name=obj.get("name",item["name"]),description=obj.get("description") or "",
                license_spdx=lic,license_status="detected" if lic and lic!="NOASSERTION" else "unresolved",
                archived=bool(obj.get("archived")),stars=int(obj.get("stargazers_count") or 0),
                pushed_at=obj.get("pushed_at"),last_checked=today)
    # status is intentionally untouched
path.write_text(json.dumps(records,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(f"Updated {len(records)-len(errors)} records; {len(errors)} failed: {', '.join(errors)}")
if errors: sys.exit(1)
