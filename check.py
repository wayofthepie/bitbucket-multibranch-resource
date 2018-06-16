#!/usr/bin/env python3
import sys
import json
import stashy

source = json.loads(sys.stdin.read())
sys.stderr.write(str(source))

stash = stashy.connect("http://192.168.1.5:7990", "admin", "admin")

for l in stash.projects["TEST"].repos["test"].branches():
    sys.stderr.write(str(l))

versions = [{"id": "1234"}]
sys.stdout.write(json.dumps(versions))
