# coding: utf-8
"""Waylay Function Registry api tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import pytest
from typeguard import check_type
from pytest_httpx import HTTPXMock
import json
from waylay.sdk import ApiClient, WaylayClient
from waylay.services.registry.api import DefaultApi
from waylay.services.registry.service import RegistryService


from ..types.root_page_response_stub import RootPageResponseStub
from waylay.services.registry.models import RootPageResponse


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


@pytest.fixture
def default_api(waylay_api_client: ApiClient) -> DefaultApi:
    return DefaultApi(waylay_api_client)


def test_registered(waylay_client: WaylayClient):
    """Test that DefaultApi api is registered in the sdk client."""
    assert isinstance(waylay_client.registry.default, DefaultApi)


@pytest.mark.asyncio
async def test_get(service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for get
    Version
    """
    # set path params

    mock_response = RootPageResponseStub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": gateway_url + f"/registry/v2/",  # noqa: F541
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {}
    resp = await service.default.get(**kwargs)
    check_type(resp, RootPageResponse)
