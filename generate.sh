#!/usr/bin/env bash
# Regenerates every language SDK from the shared openapi.json at the repo root.
set -euo pipefail
cd "$(dirname "$0")"

./go/generate.sh
./python/generate.sh
