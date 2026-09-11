// Hand-written helpers for working with errors returned by the generated
// client. This file is not touched by generate.sh.
package cedanagosdk

import (
	"errors"
	"net/http"

	abstractions "github.com/microsoft/kiota-abstractions-go"

	"github.com/cedana/cedana-go-sdk/models"
)

// StatusCode returns the HTTP status code of an error returned by this SDK,
// unwrapping as needed. It returns 0 when err did not come from an API
// response (e.g. a transport failure or a non-SDK error).
//
// Note that for the error message alone no helper is needed: API errors
// implement error with the server-provided message, so err.Error(), %v and
// %w all print it directly.
func StatusCode(err error) int {
	var apiErr abstractions.ApiErrorable
	if errors.As(err, &apiErr) {
		return apiErr.GetStatusCode()
	}
	return 0
}

// IsStatus reports whether err is an API error with the given HTTP status.
func IsStatus(err error, code int) bool {
	return StatusCode(err) == code
}

// IsNotFound reports whether err is an API error with status 404.
func IsNotFound(err error) bool {
	return IsStatus(err, http.StatusNotFound)
}

// ErrorMessage returns the server-provided error message, unwrapping as
// needed. Unlike calling Error() on the API error directly, it never panics
// when the response body lacked a message, falling back to the HTTP status
// text. For non-API errors it returns err.Error().
func ErrorMessage(err error) string {
	if err == nil {
		return ""
	}
	var httpErr *models.HttpError
	if errors.As(err, &httpErr) {
		if msg := httpErr.GetMessage(); msg != nil {
			return *msg
		}
		if reason := http.StatusText(httpErr.GetStatusCode()); reason != "" {
			return reason
		}
		return "unknown API error"
	}
	return err.Error()
}
