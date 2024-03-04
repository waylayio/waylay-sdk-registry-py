from datetime import datetime
import pytest

from waylay.sdk import WaylayConfig, ApiClient, TokenCredentials, WaylayToken
from waylay.services.registry.service import RegistryService

MOCK_DOMAIN = "unittest.waylay.io"
MOCK_TOKEN_DATA = {
    "domain": MOCK_DOMAIN,
    "tenant": "9999999999999999999999",
    "sub": "users/999999999999999",
    "exp": datetime.now().timestamp() + 100000,
}


class WaylayTokenStub(WaylayToken):
    """A WaylayToken test stub with fixed data."""

    def __init__(self):
        """Create a WaylayTokenStub."""
        super().__init__("", MOCK_TOKEN_DATA)


@pytest.fixture
def waylay_token_credentials() -> TokenCredentials:
    return TokenCredentials(token="dummy_token", gateway_url="https://api-example.io")


@pytest.fixture
def waylay_config(waylay_token_credentials: TokenCredentials) -> WaylayConfig:
    return WaylayConfig(credentials=waylay_token_credentials)


@pytest.fixture
def waylay_api_client(waylay_config: WaylayConfig) -> ApiClient:
    return ApiClient(waylay_config)


@pytest.fixture
def registry_service(waylay_api_client: ApiClient) -> RegistryService:
    return RegistryService(waylay_api_client)


@pytest.fixture
def gateway_url(waylay_api_client: ApiClient) -> str:
    return waylay_api_client.config.waylay_config.gateway_url or ""
