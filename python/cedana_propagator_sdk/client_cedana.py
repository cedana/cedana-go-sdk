# Hand-written convenience constructor for the generated client (the Python
# counterpart of the Go SDK's NewCedanaClient). This file is not touched by
# generate.sh.
from kiota_abstractions.authentication.access_token_provider import AccessTokenProvider
from kiota_abstractions.authentication.allowed_hosts_validator import AllowedHostsValidator
from kiota_abstractions.authentication.base_bearer_token_authentication_provider import (
    BaseBearerTokenAuthenticationProvider,
)
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

from .propagator_client import PropagatorClient


class StaticAccessTokenProvider(AccessTokenProvider):
    """Provides a fixed bearer token (a Cedana API key) for every request."""

    def __init__(self, access_token: str) -> None:
        self._access_token = access_token
        self._validator = AllowedHostsValidator([])

    async def get_authorization_token(self, uri: str, additional_authentication_context: dict = {}) -> str:
        return self._access_token

    def get_allowed_hosts_validator(self) -> AllowedHostsValidator:
        return self._validator


def new_cedana_client(base_url: str, api_key: str) -> PropagatorClient:
    """Creates a PropagatorClient authenticated with the given API key.

    base_url is the propagator URL, e.g. "https://api.cedana.ai".
    """
    auth_provider = BaseBearerTokenAuthenticationProvider(StaticAccessTokenProvider(api_key))
    request_adapter = HttpxRequestAdapter(auth_provider)
    request_adapter.base_url = base_url
    return PropagatorClient(request_adapter)
