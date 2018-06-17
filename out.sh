#!/usr/bin/env sh
set -e

exec 3>&1
exec 1>&2

TEMPLATE=$1/multibranch/concourse-template-pipeline/pipeline.yml
cat $1/multibranch/dat
repo=$(cat /dev/stdin | jq ".source.repo")

CONCOURSE_URL="http://192.168.1.5:8080"
if [ ! -f /usr/local/bin/fly ]; then
    echo "fly not found, retrieving latest from concourse ..."
    curl -s ${CONCOURSE_URL}/api/v1/cli?arch=amd64\&platform=linux > /usr/local/bin/fly
    chmod +x /usr/local/bin/fly
fi

sed -i "s/\${JOB_NAME}/master/" ${TEMPLATE}
fly -t main login --concourse-url ${CONCOURSE_URL}
fly -t main sp --pipeline master-pipeline -c ${TEMPLATE} -n
echo "{}" >&3
