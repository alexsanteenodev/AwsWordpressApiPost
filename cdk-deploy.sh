#!/usr/bin/env bash
if [[ $# -ge 5 ]]; then
    export ENDPOINT_URL=$1
    export AUTH_USERNAME=$2
    export AUTH_PASSWORD=$3
    export OPENAI_API_KEY=$4
    export STABILITY_API_KEY=$5
    shift; shift; shift; shift; shift
    npx cdk deploy "$@"
    exit $?
else
    echo 1>&2 "Provide ENDPOINT_URL and AUTH_USERNAME and AUTH_USERNAME and OPENAPI Api Key, Stabiliti AI key and as first four args."
    echo 1>&2 "Additional args are passed through to cdk deploy."
    exit 1
fi