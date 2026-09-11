#!/usr/bin/env bash
# Regenerates the Go SDK from ../openapi.json (the shared spec at the repo root).
set -euo pipefail
cd "$(dirname "$0")"

rm -rf models/ v1/ v2/ api_client.go kiota-lock.json
docker run --rm --user $(id -u):$(id -g) \
  -v "${PWD}":/app/output \
  -v "${PWD}/../openapi.json":/app/openapi.json \
  mcr.microsoft.com/openapi/kiota:1.35.0 generate --language go \
  -n github.com/cedana/cedana-propagator-sdk/go -d /app/openapi.json -o /app/output

# kiota derives the package name from the last namespace segment ("go"), which
# is a Go keyword; rename it to match the hand-written files.
sed -i 's/^package go$/package cedanapropagatorsdk/' api_client.go
