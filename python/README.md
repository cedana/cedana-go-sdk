# cedana-propagator-sdk (Python)

Python SDK for the Cedana Propagator API, generated using
[kiota](https://github.com/microsoft/kiota) from the shared OpenAPI spec at the
repo root.

```sh
pip install "git+https://github.com/cedana/cedana-propagator-sdk.git#subdirectory=python"
```

## Usage

The client is async (kiota's Python HTTP adapter is built on httpx):

```python
import asyncio
import os

from cedana_propagator_sdk import new_client

client = new_client(
    os.environ.get("CEDANA_URL_TEST", "http://localhost:1324"),
    os.environ["CEDANA_AUTH_TOKEN_TEST"],
)


async def main():
    user = await client.v1.user.get()
    print(f"user: {user}")

    jobs = await client.v1.jobs.get()
    for i, job in enumerate(jobs):
        print(f"job {i}: {job.name} {job.status}")

    checkpoints = await client.v1.checkpoints.get()
    for i, checkpoint in enumerate(checkpoints):
        print(f"checkpoint {i}: {checkpoint.id} {checkpoint.status}")


asyncio.run(main())
```

## Errors

Every 4xx/5xx response raises `cedana_propagator_sdk.models.http_error.HttpError`
(a subclass of kiota's `APIError`) carrying the server's error message:

```python
from kiota_abstractions.api_error import APIError

try:
    await client.v1.user.get()
except APIError as e:
    print(f"request failed with status {e.response_status_code}: {e.message}")
```

## Regenerating

`./generate.sh` regenerates the client from `../openapi.json` via kiota, patches
a kiota codegen bug in `models/http_error.py`, and syntax-checks the result.

Hand-written files (`cedana_propagator_sdk/__init__.py`,
`cedana_propagator_sdk/client_cedana.py`, `pyproject.toml`, this README) are not
touched by `generate.sh`.
