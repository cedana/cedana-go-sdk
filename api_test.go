package cedanagosdk_test

import (
	"context"
	"fmt"
	"testing"

	sdk "github.com/cedana/cedana-go-sdk"
)

func TestHello(t *testing.T) {
	client := sdk.NewCedanaClient("http://localhost:1324")
	jobs, err := client.V2().Jobs().Get(context.Background(), nil)
	if err != nil {
		t.Fatalf("failed to get user: %v", err)
	}
	for i, job := range jobs {
		fmt.Printf("job %d: %s %s\n", i, *job.GetJid(), *job.GetTypeEscaped())
	}
}
