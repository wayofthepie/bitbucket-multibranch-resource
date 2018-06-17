#!/usr/bin/env python3
import sys
import json
from subprocess import call

out_dir = sys.argv[1]
data = json.loads(sys.stdin.read())
sys.stderr.write("data")
sys.stderr.write(str(data))
sys.stderr.write("end data")

call(["git", "clone", "https://github.com/wayofthepie/concourse-template-pipeline",
      out_dir + "/concourse-template-pipeline"])

with open(out_dir + "/dat", "w+") as f:
    f.write(str(data))

sys.stdout.write(json.dumps({"version": data["version"] if "version" in data else {}, "metadata": []}))
