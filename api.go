package cedanagosdk

import (
	"context"
	"log"
	"net/url"

	auth "github.com/microsoft/kiota-abstractions-go/authentication"
	http "github.com/microsoft/kiota-http-go"
)

type StaticAccessTokenProvider struct {
	AccessToken string
}

func (s *StaticAccessTokenProvider) GetAuthorizationToken(_ context.Context, _ *url.URL, _ map[string]any) (string, error) {
	return s.AccessToken, nil
}

// GetAllowedHostsValidator returns the hosts validator.
func (*StaticAccessTokenProvider) GetAllowedHostsValidator() *auth.AllowedHostsValidator {
	return nil
}

func NewCedanaClient(rawUrl, api_key string) *ApiClient {
	authProvider := auth.NewBaseBearerTokenAuthenticationProvider(&StaticAccessTokenProvider{
		AccessToken: api_key,
	})
	url, err := url.Parse(rawUrl)
	if err != nil {
		log.Fatalf("Error parsing raw URL: %v\n", err)
	}

	adapter, err := http.NewNetHttpRequestAdapter(authProvider)
	if err != nil {
		log.Fatalf("Error creating request adapter: %v\n", err)
	}

	client := NewApiClient(adapter)
	if client.BaseRequestBuilder.RequestAdapter.GetBaseUrl() == "" {
		client.BaseRequestBuilder.RequestAdapter.SetBaseUrl(url.Scheme + url.Host)
	}
	client.BaseRequestBuilder.PathParameters["baseurl"] = client.BaseRequestBuilder.RequestAdapter.GetBaseUrl()

	return client
}
