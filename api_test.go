package cedanagosdk_test

import (
	"context"
	"fmt"
	"testing"

	sdk "github.com/cedana/cedana-go-sdk"
	sdk_models "github.com/cedana/cedana-go-sdk/models"
)

func TestHello(t *testing.T) {
	client := sdk.NewCedanaClient("http://localhost:1324", "<bad-api-key>")

	user, err := client.V2().User().Post(context.Background(), nil)
	if err != nil {
		switch v := err.(type) {
		case *sdk_models.HttpError:
			t.Errorf("failed to get user: %s %d", *v.GetMessage(), v.GetCedanaErrorCode())
		default:
			t.Errorf("unknown error: %v", v)
		}
	} else {
		fmt.Printf("user: %s\n", *user)
	}

	jobs, err := client.V2().Jobs().Get(context.Background(), nil)
	if err != nil {
		t.Errorf("failed to get jobs: %v", err)
	} else {
		for i, job := range jobs {
			fmt.Printf("job %d: %s %s\n", i, *job.GetJid(), *job.GetTypeEscaped())
		}
	}
}
