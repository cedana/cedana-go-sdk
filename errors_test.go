package cedanagosdk

import (
	"errors"
	"fmt"
	"net/http"
	"testing"

	"github.com/cedana/cedana-go-sdk/models"
)

func TestErrorHelpersOnApiError(t *testing.T) {
	msg := "job not found"
	apiErr := models.NewHttpError()
	apiErr.SetMessage(&msg)
	apiErr.SetStatusCode(http.StatusNotFound)
	var err error = apiErr

	if err.Error() != msg {
		t.Errorf("Error() = %q, want %q", err.Error(), msg)
	}
	if ErrorMessage(err) != msg {
		t.Errorf("ErrorMessage() = %q, want %q", ErrorMessage(err), msg)
	}
	if !IsNotFound(err) {
		t.Error("IsNotFound() = false, want true")
	}

	wrapped := fmt.Errorf("listing jobs: %w", err)
	if StatusCode(wrapped) != http.StatusNotFound {
		t.Errorf("StatusCode(wrapped) = %d, want 404", StatusCode(wrapped))
	}
	if ErrorMessage(wrapped) != msg {
		t.Errorf("ErrorMessage(wrapped) = %q, want %q", ErrorMessage(wrapped), msg)
	}
}

func TestErrorMessageDoesNotPanicWithoutMessage(t *testing.T) {
	apiErr := models.NewHttpError()
	apiErr.SetStatusCode(http.StatusBadGateway)

	if got := ErrorMessage(apiErr); got != "Bad Gateway" {
		t.Errorf("ErrorMessage() = %q, want %q", got, "Bad Gateway")
	}
}

func TestErrorHelpersOnPlainError(t *testing.T) {
	err := errors.New("dial tcp: connection refused")

	if StatusCode(err) != 0 {
		t.Errorf("StatusCode() = %d, want 0", StatusCode(err))
	}
	if IsNotFound(err) {
		t.Error("IsNotFound() = true, want false")
	}
	if ErrorMessage(err) != err.Error() {
		t.Errorf("ErrorMessage() = %q, want %q", ErrorMessage(err), err.Error())
	}
	if ErrorMessage(nil) != "" {
		t.Errorf("ErrorMessage(nil) = %q, want empty", ErrorMessage(nil))
	}
}
