#!/usr/bin/env bash
if [[ $# -ge 3 ]]; then
    export ENDPOINT_URL=$1
    export AUTH_USERNAME=$2
    export AUTH_PASSWORD=$3
    shift; shift; shift
    npx cdk deploy "$@"
    exit $?
else
    echo 1>&2 "Provide ENDPOINT_URL and AUTH_USERNAME and AUTH_USERNAME and as first three args."
    echo 1>&2 "Additional args are passed through to cdk deploy."
    exit 1
fi