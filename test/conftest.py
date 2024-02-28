"""Automatic pytest fixtures."""

import pytest

from waylay.sdk import WaylayConfig, ApiClient, WaylayClient
from waylay.sdk.auth import NoCredentials
from waylay.services.registry.service import RegistryService

GATEWAY_URL = 'http://example.io'


@pytest.fixture(name='gateway_url')
def fixture_gateway_url() -> str:
    return GATEWAY_URL


@pytest.fixture(name='waylay_config')
def fixture_config(gateway_url) -> WaylayConfig:
    return WaylayConfig(credentials=NoCredentials(gateway_url=gateway_url))


@pytest.fixture(name='waylay_api_client')
def fixture_api_client(waylay_config: WaylayConfig) -> ApiClient:
    return ApiClient(waylay_config, {'auth': None})


@pytest.fixture(name='service')
def fixture_service(waylay_api_client: ApiClient) -> RegistryService:
    return RegistryService(waylay_api_client)


@pytest.fixture(name='waylay_client')
def fixture_waylay_client(waylay_config: WaylayConfig) -> WaylayClient:
    return WaylayClient(waylay_config, {'auth': None})
