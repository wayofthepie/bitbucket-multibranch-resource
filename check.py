#!/usr/bin/env python3
import sys
import json
import stashy
import socket
from subprocess import call

# data is a json object containing source and version top-level keys
data = json.loads(sys.stdin.read())

# source is the value of source set on the configured resource
source = data["source"]

# version is either None or the previous version
prev_version = data["version"]
sys.stderr.write(str(prev_version))

# connect to bitbucket
stash = stashy.connect(source["url"], source["username"], source["password"])

# build a list of all branches in the given repo under the given project
branches = []
for details in stash.projects[source["project"]].repos[source["repo"]].branches():
    branch = details["id"].replace("refs/heads/", "")
    branches.append(branch)

# compute the difference between the previous list of branches and the current list
difference = list(set(branches).difference(
    set({} if prev_version is None else json.loads(prev_version["branches"].replace("'", '"')))))

# send on the branches we should create
sys.stdout.write(json.dumps([{"branches": str(difference)}]))
