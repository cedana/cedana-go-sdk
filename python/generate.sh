#!/usr/bin/env bash
# Regenerates the Python SDK from ../openapi.json (the shared spec at the repo root).
set -euo pipefail
cd "$(dirname "$0")"

rm -rf cedana_propagator_sdk/models cedana_propagator_sdk/v1 \
  cedana_propagator_sdk/propagator_client.py cedana_propagator_sdk/kiota-lock.json
docker run --rm --user $(id -u):$(id -g) \
  -v "${PWD}/cedana_propagator_sdk":/app/output \
  -v "${PWD}/../openapi.json":/app/openapi.json \
  mcr.microsoft.com/openapi/kiota:1.35.0 generate --language python \
  -c PropagatorClient -n cedana_propagator_sdk -d /app/openapi.json -o /app/output

# kiota's python generator emits invalid syntax ("if self. is not None:") for
# the primary_message property derived from x-ms-primary-error-message.
sed -i 's/if self\. is not None:/if self.message is not None:/' \
  cedana_propagator_sdk/models/http_error.py

# Fail loudly if the generated tree has syntax errors.
python3 -m compileall -q cedana_propagator_sdk
