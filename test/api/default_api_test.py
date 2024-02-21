# coding: utf-8
"""Waylay Function Registry api tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import pytest
from typing import Dict, List
from pytest_httpx import HTTPXMock
import json
from waylay.sdk import ApiClient
from waylay.services.registry.api import DefaultApi
from waylay.services.registry.service import RegistryService
from ..fixtures import WaylayTokenStub, waylay_api_client, waylay_config, waylay_token_credentials, gateway_url, registry_service


from ..types.root_page_response_stub import RootPageResponseStub
from waylay.services.registry.models import RootPageResponse


@pytest.fixture
def default_api(waylay_api_client: ApiClient) -> DefaultApi:
    return DefaultApi(waylay_api_client)


@pytest.mark.asyncio
async def test_get(registry_service: RegistryService, gateway_url: str, mocker, httpx_mock: HTTPXMock):
    """Test case for get
        Version
    """
    # set path params

    mocker.patch('waylay.sdk.WaylayTokenAuth.assure_valid_token', lambda *args: WaylayTokenStub())
    mock_response = RootPageResponseStub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": gateway_url + f"/registry/v2/",
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {

    }
    resp = await registry_service.default.get(**kwargs)
    assert isinstance(resp, RootPageResponse)
