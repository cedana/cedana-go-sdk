package cedanagosdk_test

import (
	"context"
	"fmt"
	"os"
	"testing"

	sdk "github.com/cedana/cedana-go-sdk"
)

func FromEnvOrElse(key, def string) string {
	if value, found := os.LookupEnv(key); found {
		return value
	}
	return def
}

var (
	apiKey    = os.Getenv("CEDANA_AUTH_TOKEN")
	cedanaUrl = FromEnvOrElse("CEDANA_URL", "http://ui.cedana.ai/v1")
)

func TestUser(t *testing.T) {
	client := sdk.NewCedanaClient(cedanaUrl, apiKey)
	fmt.Println("url: ", client.V2().User().RequestAdapter.GetBaseUrl())
	user, err := client.V2().User().Get(context.Background(), nil)
	if err != nil {
		t.Errorf("failed to get user: %v", err)
	} else {
		fmt.Printf("user: %s\n", *user)
	}
}

func TestCheckpointsList(t *testing.T) {
	client := sdk.NewCedanaClient(cedanaUrl, apiKey)
	// testCheckpointsDownload(t)
	checkpoints, err := client.V2().Checkpoints().Get(context.Background(), nil)
	if err != nil {
		t.Errorf("failed to get checkpoints: %v", err)
	} else {
		for i, checkpoint := range checkpoints {
			fmt.Printf("checkpoint %d: %s %s\n", i, *checkpoint.GetId(), *checkpoint.GetStatus())
		}
	}
}

func TestCheckpointsAdd(t *testing.T) {
	client := sdk.NewCedanaClient(cedanaUrl, apiKey)
	uuid, err := client.V2().Checkpoints().Post(context.Background(), nil)
	if err != nil {
		t.Errorf("failed to add checkpoint: %v", err)
	} else {
		fmt.Printf("new checkpoint %v\n", *uuid)
	}
}
