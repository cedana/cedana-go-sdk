package cedanagosdk

import (
	"log"

	auth "github.com/microsoft/kiota-abstractions-go/authentication"
	bundle "github.com/microsoft/kiota-bundle-go"
	// http "github.com/microsoft/kiota-http-go"
)

func NewCedanaClient(url string) *ApiClient {
	authProvider := auth.AnonymousAuthenticationProvider{}

	// Create request adapter using the net/http-based implementation
	adapter, err := bundle.NewDefaultRequestAdapter(&authProvider)
	if err != nil {
		log.Fatalf("Error creating request adapter: %v\n", err)
	}

	client := NewApiClient(adapter)
	if client.BaseRequestBuilder.RequestAdapter.GetBaseUrl() == "" {
		client.BaseRequestBuilder.RequestAdapter.SetBaseUrl(url)
	}
	client.BaseRequestBuilder.PathParameters["baseurl"] = client.BaseRequestBuilder.RequestAdapter.GetBaseUrl()

	return client
}
