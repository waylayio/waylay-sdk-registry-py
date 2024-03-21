# coding: utf-8
"""Waylay Function Registry api tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import pytest
from typing import Dict, List, get_args, Union
from typeguard import check_type
from pytest_httpx import HTTPXMock
import json
import sys
import re
from unittest.mock import patch
from importlib import reload
from importlib.util import find_spec
from urllib.parse import quote

from waylay.sdk import ApiClient, WaylayClient
from waylay.sdk.api._models import Model
from waylay.services.registry.api import SchemasApi
from waylay.services.registry.service import RegistryService

from ..types.function_type_stub import FunctionTypeStub

from ..types.asset_role_stub import AssetRoleStub


try:
    MODELS_AVAILABLE = find_spec("waylay.services.registry.models") is not None
except ImportError:
    MODELS_AVAILABLE = False


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


@pytest.fixture
def schemas_api(waylay_api_client: ApiClient) -> SchemasApi:
    return SchemasApi(waylay_api_client)


def test_registered(waylay_client: WaylayClient):
    """Test that SchemasApi api is registered in the sdk client."""
    assert isinstance(waylay_client.registry.schemas, SchemasApi)


def _get_by_role_set_mock_response(
    httpx_mock: HTTPXMock, gateway_url: str, functionType: str, role: str
):
    mock_response = {}
    httpx_mock_kwargs = {
        "method": "GET",
        "url": re.compile(
            f"^{gateway_url}/registry/v2/schemas/{functionType}/{role}/schema(\\?.*)?"
        ),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_get_by_role(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for get_by_role
    Get Asset Schema
    """
    # set path params
    functionType = "plugs"

    role = "manifest"

    kwargs = {}
    _get_by_role_set_mock_response(
        httpx_mock, gateway_url, quote(str(functionType)), quote(str(role))
    )
    resp = await service.schemas.get_by_role(functionType, role, **kwargs)
    check_type(resp, Union[Dict[str, object],])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_get_by_role_without_types(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for get_by_role with models not installed
    Get Asset Schema
    """
    # set path params
    functionType = "plugs"

    role = "manifest"

    kwargs = {}
    _get_by_role_set_mock_response(
        httpx_mock, gateway_url, quote(str(functionType)), quote(str(role))
    )
    resp = await service.schemas.get_by_role(functionType, role, **kwargs)
    check_type(resp, Model)


def _get_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str, schemaId: str):
    mock_response = {}
    httpx_mock_kwargs = {
        "method": "GET",
        "url": re.compile(f"^{gateway_url}/registry/v2/schemas/{schemaId}(\\?.*)?"),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_get(service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for get
    Get Asset Schema
    """
    # set path params
    schemaId = "schema_id_example"

    kwargs = {}
    _get_set_mock_response(httpx_mock, gateway_url, quote(str(schemaId)))
    resp = await service.schemas.get(schemaId, **kwargs)
    check_type(resp, Union[Dict[str, object],])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_get_without_types(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for get with models not installed
    Get Asset Schema
    """
    # set path params
    schemaId = "schema_id_example"

    kwargs = {}
    _get_set_mock_response(httpx_mock, gateway_url, quote(str(schemaId)))
    resp = await service.schemas.get(schemaId, **kwargs)
    check_type(resp, Model)
