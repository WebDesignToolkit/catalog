#!/usr/bin/env python3
"""Validate the catalog using Python stdlib only."""
import datetime,json,re,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
records=json.loads((root/"data/resources.json").read_text(encoding="utf-8"))
taxonomy=json.loads((root/"data/taxonomy.json").read_text(encoding="utf-8"))
categories={entry["slug"] for entry in taxonomy["categories"]}
assert isinstance(records,list) and records,"empty catalog"
ids=set()
names=set()
for item in records:
    assert isinstance(item,dict)
    for key in ("id","repository","name","url","category","description","status","license_status","last_checked","source","tags","stars","archived"):
        assert key in item,(item.get("id"),key)
    assert item["id"] not in ids,item["id"]
    assert item["repository"].lower() not in names,item["repository"]
    ids.add(item["id"]);names.add(item["repository"].lower())
    assert item["url"].startswith("https://github.com/"),item["url"]
    assert re.match(r"^[^/]+/[^/]+$",item["repository"])
    assert item["category"] in categories,item["category"]
    assert item["status"] in {"candidate","reviewed","rejected"}
    assert item["license_status"] in {"detected","unresolved"}
    assert isinstance(item["archived"],bool) and type(item["stars"])==int
    assert isinstance(item["tags"],list)
    datetime.date.fromisoformat(item["last_checked"])
    assert item["source"]=="github-api"
print(f"PASS: {len(records)} unique records, {len(categories)} category labels")
