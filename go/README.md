# cedana-propagator-sdk (Go)

Go SDK for the Cedana Propagator API, generated using
[kiota](https://github.com/microsoft/kiota) from the shared OpenAPI spec at the
repo root.

```sh
go get github.com/cedana/cedana-propagator-sdk/go
```

## Errors

Every 4xx/5xx response from the API deserializes into `*models.HttpError`, which
implements `error` with the server's error message — so `err.Error()`, `%v` and
`%w` all print it directly, no type assertion needed.

For branching on the HTTP status, use the helpers in the root package instead of
casting:

```go
if err != nil {
	if sdk.IsNotFound(err) {
		// handle 404
	}
	if sdk.StatusCode(err) == 429 {
		// handle rate limiting; StatusCode returns 0 for transport errors
	}
	fmt.Println(sdk.ErrorMessage(err)) // nil-safe message extraction
}
```

Available helpers: `StatusCode(err) int`, `IsStatus(err, code) bool`,
`IsNotFound(err) bool`, `ErrorMessage(err) string`.

## Usage

```go
package example

import (
	"context"
	"fmt"
	"os"

	sdk "github.com/cedana/cedana-propagator-sdk/go"
)

func FromEnvOrElse(key, def string) string {
	if value, found := os.LookupEnv(key); found {
		return value
	}
	return def
}

var (
	apiKey    = os.Getenv("CEDANA_AUTH_TOKEN_TEST")
	cedanaUrl = FromEnvOrElse("CEDANA_URL_TEST", "http://localhost:1324")
)

func Main() {
	client := sdk.NewClient(cedanaUrl, apiKey)

	// get user
	user, err := client.V1().User().Get(context.Background(), nil)
	if err != nil {
		fmt.Printf("failed to get user: %v (status %d)\n", err, sdk.StatusCode(err))
	} else {
		fmt.Printf("user: %s\n", *user)
	}

	jobs, err := client.V1().Jobs().Get(context.Background(), nil)
	if err != nil {
		fmt.Printf("failed to get jobs: %v (status %d)\n", err, sdk.StatusCode(err))
	} else {
		for i, job := range jobs {
			fmt.Printf("job %d: %s %s\n", i, *job.GetName(), *job.GetStatus())
		}
	}

	checkpoints, err := client.V1().Checkpoints().Get(context.Background(), nil)
	if err != nil {
		fmt.Printf("failed to get checkpoints: %v (status %d)\n", err, sdk.StatusCode(err))
	} else {
		for i, checkpoint := range checkpoints {
			fmt.Printf("checkpoint %d: %s %s\n", i, checkpoint.GetId(), *checkpoint.GetStatus())
		}
	}

	uuid, err := client.V1().Checkpoints().Post(context.Background(), nil)
	if err != nil {
		if sdk.IsNotFound(err) {
			fmt.Println("no such job to checkpoint")
		} else {
			fmt.Printf("failed to create checkpoint: %v\n", err)
		}
	} else {
		fmt.Printf("new checkpoint %v\n", *uuid)
	}
}
```

## Regenerating

`./generate.sh` regenerates the client from `../openapi.json` via kiota. It also
renames the generated root package to `cedanapropagatorsdk` (kiota derives the
name from the last namespace segment, `go`, which is a Go keyword).

Hand-written files (`errors.go`, `api_client_cedana.go`, the tests, this README)
are not touched by `generate.sh`.
