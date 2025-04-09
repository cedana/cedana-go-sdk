package cedanagosdk_test

import (
	"context"
	"fmt"
	"os"
	"testing"

	sdk "github.com/cedana/cedana-go-sdk"
	sdk_models "github.com/cedana/cedana-go-sdk/models"
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

func TestUser(t *testing.T) {
	client := sdk.NewCedanaClient(cedanaUrl, apiKey)
	user, err := client.V2().User().Post(context.Background(), nil)
	if err != nil {
		switch v := err.(type) {
		case *sdk_models.HttpError:
			t.Errorf("failed to get user: %s :error_code(%d)", *v.GetMessage(), *v.GetCedanaErrorCode())
		default:
			t.Errorf("unknown error: %v", v)
		}
	} else {
		fmt.Printf("user: %s\n", *user)
	}

}

func TestJobFetch(t *testing.T) {
	client := sdk.NewCedanaClient(cedanaUrl, apiKey)
	jobs, err := client.V2().Jobs().Get(context.Background(), nil)
	if err != nil {
		switch v := err.(type) {
		case *sdk_models.HttpError:
			t.Errorf("failed to get job: %s :error_code(%d)", *v.GetMessage(), *v.GetCedanaErrorCode())
		default:
			t.Errorf("unknown error: %v", v)
		}
	} else {
		for i, job := range jobs {
			fmt.Printf("job %d: %s %s\n", i, *job.GetJid(), *job.GetTypeEscaped())
		}
	}
}

func TestCheckpointsList(t *testing.T) {
	client := sdk.NewCedanaClient(cedanaUrl, apiKey)
	// testCheckpointsDownload(t)
	checkpoints, err := client.V2().Checkpoints().Get(context.Background(), nil)
	if err != nil {
		switch v := err.(type) {
		case *sdk_models.HttpError:
			t.Errorf("failed to get checkpoint: %s :error_code(%d)", *v.GetMessage(), *v.GetCedanaErrorCode())
		default:
			t.Errorf("unknown error: %v", v)
		}
	} else {
		for i, checkpoint := range checkpoints {
			fmt.Printf("checkpoint %d: %s %s\n", i, *checkpoint.GetId(), *checkpoint.GetStatus())
		}
	}
}

func testCheckpointsAdd(t *testing.T) {
	client := sdk.NewCedanaClient(cedanaUrl, apiKey)
	uuid, err := client.V2().Checkpoints().Post(context.Background(), nil)
	if err != nil {
		switch v := err.(type) {
		case *sdk_models.HttpError:
			t.Errorf("failed to create checkpoint: %s :error_code(%d)", *v.GetMessage(), *v.GetCedanaErrorCode())
		default:
			t.Errorf("unknown error: %v", v)
		}
	} else {
		fmt.Printf("new checkpoint %v\n", *uuid)
	}
}

func testCheckpointsUpload(t *testing.T) {
	client := sdk.NewCedanaClient(cedanaUrl, apiKey)
	uuid := "04ee4678-d934-4eeb-97ed-d4cf779ae4fc"
	upload_url, err := client.V2().Checkpoints().Upload().ById(uuid).Patch(context.Background(), nil)
	if err != nil {
		switch v := err.(type) {
		case *sdk_models.HttpError:
			t.Errorf("failed to get upload url for checkpoint: %s :error_code(%d)", *v.GetMessage(), *v.GetCedanaErrorCode())
		default:
			t.Errorf("unknown error: %v", v)
		}
	} else {
		fmt.Printf("uploading checkpoint %v\n", *upload_url)
	}
}

func testCheckpointsDownload(t *testing.T) {
	client := sdk.NewCedanaClient(cedanaUrl, apiKey)
	uuid := "04ee4678-d934-4eeb-97ed-d4cf779ae4fc"
	download_url, err := client.V2().Checkpoints().Download().ById(uuid).Get(context.Background(), nil)
	if err != nil {
		switch v := err.(type) {
		case *sdk_models.HttpError:
			t.Errorf("failed to get download url for checkpoint: %s :error_code(%d)", *v.GetMessage(), *v.GetCedanaErrorCode())
		default:
			t.Errorf("unknown error: %v", v)
		}
	} else {
		fmt.Printf("download checkpoint from %v\n", *download_url)
	}
}
