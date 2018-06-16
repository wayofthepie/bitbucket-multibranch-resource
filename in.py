#!/usr/bin/env python3
import sys
import json

outdir = sys.argv[1]
source = json.loads(sys.stdin.read())
version = source["version"]
sys.stderr.write(str(version))

f = open(outdir + "/versions", "w")
f.write(json.dumps([version]))
sys.stdout.write(json.dumps({"version": version, "metadata": []}))
