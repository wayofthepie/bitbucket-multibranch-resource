#!/usr/bin/env python3
import sys
import json
import stashy

source = json.loads(sys.stdin.read())["source"]
sys.stderr.write(str(source))
stash = stashy.connect(source["url"], source["username"], source["password"])

branches = []
for details in stash.projects[source["project"]].repos[source["repo"]].branches():
    branch = details["id"].split("/")[-1]
    branches.append(branch)

sys.stdout.write(json.dumps([{"version": str(branches)}]))

