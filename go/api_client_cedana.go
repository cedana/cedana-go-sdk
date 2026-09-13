package cedanapropagatorsdk

import (
	"context"
	"log"
	nethttp "net/http"
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

// NewClient builds a propagator API client. An optional *net/http.Client may be
// passed to customize the transport (e.g. to inject extra headers via a custom
// RoundTripper); wrap kiota's http.GetDefaultClient() to keep its default
// middleware (retries, redirects, compression). Without one, kiota's default
// client is used.
func NewClient(rawUrl, api_key string, httpClient ...*nethttp.Client) *ApiClient {
	authProvider := auth.NewBaseBearerTokenAuthenticationProvider(&StaticAccessTokenProvider{
		AccessToken: api_key,
	})
	url, err := url.Parse(rawUrl)
	if err != nil {
		log.Fatalf("Error parsing raw URL: %v\n", err)
	}

	var adapter *http.NetHttpRequestAdapter
	if len(httpClient) > 0 && httpClient[0] != nil {
		adapter, err = http.NewNetHttpRequestAdapterWithParseNodeFactoryAndSerializationWriterFactoryAndHttpClient(authProvider, nil, nil, httpClient[0])
	} else {
		adapter, err = http.NewNetHttpRequestAdapter(authProvider)
	}
	if err != nil {
		log.Fatalf("Error creating request adapter: %v\n", err)
	}

	client := NewApiClient(adapter)
	if client.BaseRequestBuilder.RequestAdapter.GetBaseUrl() == "" {
		client.BaseRequestBuilder.RequestAdapter.SetBaseUrl(url.Scheme + "://" + url.Host)
	}
	client.BaseRequestBuilder.PathParameters["baseurl"] = client.BaseRequestBuilder.RequestAdapter.GetBaseUrl()

	return client
}
