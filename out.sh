#!/usr/bin/env sh
set -e
CONCOURSE_URL="http://192.168.1.5:8080"
(>&2 echo ${CONCOURSE_URL})
if [ ! -f /usr/local/bin/fly ]; then
    echo "fly not found, retrieving latest from concourse ..."
    curl  ${CONCOURSE_URL}/api/v1/cli?arch=amd64\&platform=linux > /usr/local/bin/fly
    chmod +x /usr/local/bin/fly
fi

fly -t main login --concourse-url ${CONCOURSE_URL}

