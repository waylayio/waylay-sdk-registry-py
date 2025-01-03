# coding: utf-8
"""Waylay Function Registry api tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json
import re
from importlib.util import find_spec
from typing import Union
from urllib.parse import quote

import pytest
from pytest_httpx import HTTPXMock
from typeguard import check_type
from waylay.sdk import ApiClient, WaylayClient
from waylay.sdk.api._models import Model
from waylay.services.registry.api import ModelTagsApi
from waylay.services.registry.service import RegistryService

from ..types.function_tag_response_stub import FunctionTagResponseStub
from ..types.function_tags_response_stub import FunctionTagsResponseStub
from ..types.update_tags_request_v2_stub import UpdateTagsRequestV2Stub

MODELS_AVAILABLE = (
    True if find_spec("waylay.services.registry.models") is not None else False
)

if MODELS_AVAILABLE:
    from waylay.services.registry.models import (
        FunctionTagResponse,
        FunctionTagsResponse,
    )
    from waylay.services.registry.queries.model_tags_api import (
        ClearAllQuery,
        FindAllQuery,
        ListAllQuery,
        ReplaceAllQuery,
    )


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


@pytest.fixture
def model_tags_api(waylay_api_client: ApiClient) -> ModelTagsApi:
    return ModelTagsApi(waylay_api_client)


def test_registered(waylay_client: WaylayClient):
    """Test that ModelTagsApi api is registered in the sdk client."""
    assert isinstance(waylay_client.registry.model_tags, ModelTagsApi)


def _add_all_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str, name: str):
    mock_response = FunctionTagsResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "PATCH",
        "url": re.compile(f"^{gateway_url}/registry/v2/models/{name}/tags(\\?.*)?"),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_add_all(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for add_all
    Add Tags On All
    """
    # set path params
    name = "name_example"

    kwargs = {
        "json": UpdateTagsRequestV2Stub.create_instance(),
    }
    _add_all_set_mock_response(httpx_mock, gateway_url, quote(str(name)))
    resp = await service.model_tags.add_all(name, **kwargs)
    check_type(resp, Union[FunctionTagsResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_add_all_without_types(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for add_all with models not installed
    Add Tags On All
    """
    # set path params
    name = "name_example"

    kwargs = {
        "json": UpdateTagsRequestV2Stub.create_json(),
    }
    _add_all_set_mock_response(httpx_mock, gateway_url, quote(str(name)))
    resp = await service.model_tags.add_all(name, **kwargs)
    check_type(resp, Model)


def _add_set_mock_response(
    httpx_mock: HTTPXMock, gateway_url: str, name: str, version: str
):
    mock_response = FunctionTagsResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "PATCH",
        "url": re.compile(
            f"^{gateway_url}/registry/v2/models/{name}/versions/{version}/tags(\\?.*)?"
        ),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_add(service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for add
    Add Tags
    """
    # set path params
    name = "name_example"

    version = "version_example"

    kwargs = {
        "json": UpdateTagsRequestV2Stub.create_instance(),
    }
    _add_set_mock_response(
        httpx_mock, gateway_url, quote(str(name)), quote(str(version))
    )
    resp = await service.model_tags.add(name, version, **kwargs)
    check_type(resp, Union[FunctionTagsResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_add_without_types(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for add with models not installed
    Add Tags
    """
    # set path params
    name = "name_example"

    version = "version_example"

    kwargs = {
        "json": UpdateTagsRequestV2Stub.create_json(),
    }
    _add_set_mock_response(
        httpx_mock, gateway_url, quote(str(name)), quote(str(version))
    )
    resp = await service.model_tags.add(name, version, **kwargs)
    check_type(resp, Model)


def _clear_all_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str, name: str):
    mock_response = FunctionTagsResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "DELETE",
        "url": re.compile(f"^{gateway_url}/registry/v2/models/{name}/tags(\\?.*)?"),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_clear_all(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for clear_all
    Clear Tags On Any/All
    """
    # set path params
    name = "name_example"

    kwargs = {
        # optionally use ClearAllQuery to validate and reuse parameters
        "query": ClearAllQuery(
            scope="any",
        ),
    }
    _clear_all_set_mock_response(httpx_mock, gateway_url, quote(str(name)))
    resp = await service.model_tags.clear_all(name, **kwargs)
    check_type(resp, Union[FunctionTagsResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_clear_all_without_types(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for clear_all with models not installed
    Clear Tags On Any/All
    """
    # set path params
    name = "name_example"

    kwargs = {
        "query": {
            "scope": "any",
        },
    }
    _clear_all_set_mock_response(httpx_mock, gateway_url, quote(str(name)))
    resp = await service.model_tags.clear_all(name, **kwargs)
    check_type(resp, Model)


def _clear_set_mock_response(
    httpx_mock: HTTPXMock, gateway_url: str, name: str, version: str
):
    mock_response = FunctionTagsResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "DELETE",
        "url": re.compile(
            f"^{gateway_url}/registry/v2/models/{name}/versions/{version}/tags(\\?.*)?"
        ),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_clear(service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for clear
    Clear Tags
    """
    # set path params
    name = "name_example"

    version = "version_example"

    kwargs = {}
    _clear_set_mock_response(
        httpx_mock, gateway_url, quote(str(name)), quote(str(version))
    )
    resp = await service.model_tags.clear(name, version, **kwargs)
    check_type(resp, Union[FunctionTagsResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_clear_without_types(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for clear with models not installed
    Clear Tags
    """
    # set path params
    name = "name_example"

    version = "version_example"

    kwargs = {}
    _clear_set_mock_response(
        httpx_mock, gateway_url, quote(str(name)), quote(str(version))
    )
    resp = await service.model_tags.clear(name, version, **kwargs)
    check_type(resp, Model)


def _find_all_set_mock_response(
    httpx_mock: HTTPXMock, gateway_url: str, tagName: str, name: str
):
    mock_response = FunctionTagResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": re.compile(
            f"^{gateway_url}/registry/v2/models/{name}/tags/{tagName}(\\?.*)?"
        ),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_find_all(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for find_all
    Find Tags On Any/All
    """
    # set path params
    tagName = "tag_name_example"

    name = "name_example"

    kwargs = {
        # optionally use FindAllQuery to validate and reuse parameters
        "query": FindAllQuery(
            scope="any",
        ),
    }
    _find_all_set_mock_response(
        httpx_mock, gateway_url, quote(str(tagName)), quote(str(name))
    )
    resp = await service.model_tags.find_all(tagName, name, **kwargs)
    check_type(resp, Union[FunctionTagResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_find_all_without_types(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for find_all with models not installed
    Find Tags On Any/All
    """
    # set path params
    tagName = "tag_name_example"

    name = "name_example"

    kwargs = {
        "query": {
            "scope": "any",
        },
    }
    _find_all_set_mock_response(
        httpx_mock, gateway_url, quote(str(tagName)), quote(str(name))
    )
    resp = await service.model_tags.find_all(tagName, name, **kwargs)
    check_type(resp, Model)


def _find_set_mock_response(
    httpx_mock: HTTPXMock, gateway_url: str, tagName: str, name: str, version: str
):
    mock_response = FunctionTagResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": re.compile(
            f"^{gateway_url}/registry/v2/models/{name}/versions/{version}/tags/{tagName}(\\?.*)?"
        ),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_find(service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for find
    Find Tag
    """
    # set path params
    tagName = "tag_name_example"

    name = "name_example"

    version = "version_example"

    kwargs = {}
    _find_set_mock_response(
        httpx_mock,
        gateway_url,
        quote(str(tagName)),
        quote(str(name)),
        quote(str(version)),
    )
    resp = await service.model_tags.find(tagName, name, version, **kwargs)
    check_type(resp, Union[FunctionTagResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_find_without_types(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for find with models not installed
    Find Tag
    """
    # set path params
    tagName = "tag_name_example"

    name = "name_example"

    version = "version_example"

    kwargs = {}
    _find_set_mock_response(
        httpx_mock,
        gateway_url,
        quote(str(tagName)),
        quote(str(name)),
        quote(str(version)),
    )
    resp = await service.model_tags.find(tagName, name, version, **kwargs)
    check_type(resp, Model)


def _list_all_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str, name: str):
    mock_response = FunctionTagsResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": re.compile(f"^{gateway_url}/registry/v2/models/{name}/tags(\\?.*)?"),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_list_all(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for list_all
    List Tags On Any/All
    """
    # set path params
    name = "name_example"

    kwargs = {
        # optionally use ListAllQuery to validate and reuse parameters
        "query": ListAllQuery(
            scope="any",
        ),
    }
    _list_all_set_mock_response(httpx_mock, gateway_url, quote(str(name)))
    resp = await service.model_tags.list_all(name, **kwargs)
    check_type(resp, Union[FunctionTagsResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_list_all_without_types(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for list_all with models not installed
    List Tags On Any/All
    """
    # set path params
    name = "name_example"

    kwargs = {
        "query": {
            "scope": "any",
        },
    }
    _list_all_set_mock_response(httpx_mock, gateway_url, quote(str(name)))
    resp = await service.model_tags.list_all(name, **kwargs)
    check_type(resp, Model)


def _list_set_mock_response(
    httpx_mock: HTTPXMock, gateway_url: str, name: str, version: str
):
    mock_response = FunctionTagsResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": re.compile(
            f"^{gateway_url}/registry/v2/models/{name}/versions/{version}/tags(\\?.*)?"
        ),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_list(service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for list
    List Tags
    """
    # set path params
    name = "name_example"

    version = "version_example"

    kwargs = {}
    _list_set_mock_response(
        httpx_mock, gateway_url, quote(str(name)), quote(str(version))
    )
    resp = await service.model_tags.list(name, version, **kwargs)
    check_type(resp, Union[FunctionTagsResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_list_without_types(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for list with models not installed
    List Tags
    """
    # set path params
    name = "name_example"

    version = "version_example"

    kwargs = {}
    _list_set_mock_response(
        httpx_mock, gateway_url, quote(str(name)), quote(str(version))
    )
    resp = await service.model_tags.list(name, version, **kwargs)
    check_type(resp, Model)


def _put_all_set_mock_response(
    httpx_mock: HTTPXMock, gateway_url: str, tagName: str, name: str
):
    mock_response = FunctionTagResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "PUT",
        "url": re.compile(
            f"^{gateway_url}/registry/v2/models/{name}/tags/{tagName}(\\?.*)?"
        ),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_put_all(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for put_all
    Put Tag On All
    """
    # set path params
    tagName = "tag_name_example"

    name = "name_example"

    kwargs = {}
    _put_all_set_mock_response(
        httpx_mock, gateway_url, quote(str(tagName)), quote(str(name))
    )
    resp = await service.model_tags.put_all(tagName, name, **kwargs)
    check_type(resp, Union[FunctionTagResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_put_all_without_types(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for put_all with models not installed
    Put Tag On All
    """
    # set path params
    tagName = "tag_name_example"

    name = "name_example"

    kwargs = {}
    _put_all_set_mock_response(
        httpx_mock, gateway_url, quote(str(tagName)), quote(str(name))
    )
    resp = await service.model_tags.put_all(tagName, name, **kwargs)
    check_type(resp, Model)


def _put_set_mock_response(
    httpx_mock: HTTPXMock, gateway_url: str, tagName: str, name: str, version: str
):
    mock_response = FunctionTagResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "PUT",
        "url": re.compile(
            f"^{gateway_url}/registry/v2/models/{name}/versions/{version}/tags/{tagName}(\\?.*)?"
        ),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_put(service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for put
    Put Tag
    """
    # set path params
    tagName = "tag_name_example"

    name = "name_example"

    version = "version_example"

    kwargs = {}
    _put_set_mock_response(
        httpx_mock,
        gateway_url,
        quote(str(tagName)),
        quote(str(name)),
        quote(str(version)),
    )
    resp = await service.model_tags.put(tagName, name, version, **kwargs)
    check_type(resp, Union[FunctionTagResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_put_without_types(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for put with models not installed
    Put Tag
    """
    # set path params
    tagName = "tag_name_example"

    name = "name_example"

    version = "version_example"

    kwargs = {}
    _put_set_mock_response(
        httpx_mock,
        gateway_url,
        quote(str(tagName)),
        quote(str(name)),
        quote(str(version)),
    )
    resp = await service.model_tags.put(tagName, name, version, **kwargs)
    check_type(resp, Model)


def _remove_all_set_mock_response(
    httpx_mock: HTTPXMock, gateway_url: str, tagName: str, name: str
):
    mock_response = FunctionTagResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "DELETE",
        "url": re.compile(
            f"^{gateway_url}/registry/v2/models/{name}/tags/{tagName}(\\?.*)?"
        ),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_remove_all(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for remove_all
    Remove Tag On Any/All
    """
    # set path params
    tagName = "tag_name_example"

    name = "name_example"

    kwargs = {}
    _remove_all_set_mock_response(
        httpx_mock, gateway_url, quote(str(tagName)), quote(str(name))
    )
    resp = await service.model_tags.remove_all(tagName, name, **kwargs)
    check_type(resp, Union[FunctionTagResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_remove_all_without_types(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for remove_all with models not installed
    Remove Tag On Any/All
    """
    # set path params
    tagName = "tag_name_example"

    name = "name_example"

    kwargs = {}
    _remove_all_set_mock_response(
        httpx_mock, gateway_url, quote(str(tagName)), quote(str(name))
    )
    resp = await service.model_tags.remove_all(tagName, name, **kwargs)
    check_type(resp, Model)


def _remove_set_mock_response(
    httpx_mock: HTTPXMock, gateway_url: str, tagName: str, name: str, version: str
):
    mock_response = FunctionTagResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "DELETE",
        "url": re.compile(
            f"^{gateway_url}/registry/v2/models/{name}/versions/{version}/tags/{tagName}(\\?.*)?"
        ),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_remove(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for remove
    Remove Tag
    """
    # set path params
    tagName = "tag_name_example"

    name = "name_example"

    version = "version_example"

    kwargs = {}
    _remove_set_mock_response(
        httpx_mock,
        gateway_url,
        quote(str(tagName)),
        quote(str(name)),
        quote(str(version)),
    )
    resp = await service.model_tags.remove(tagName, name, version, **kwargs)
    check_type(resp, Union[FunctionTagResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_remove_without_types(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for remove with models not installed
    Remove Tag
    """
    # set path params
    tagName = "tag_name_example"

    name = "name_example"

    version = "version_example"

    kwargs = {}
    _remove_set_mock_response(
        httpx_mock,
        gateway_url,
        quote(str(tagName)),
        quote(str(name)),
        quote(str(version)),
    )
    resp = await service.model_tags.remove(tagName, name, version, **kwargs)
    check_type(resp, Model)


def _replace_all_set_mock_response(httpx_mock: HTTPXMock, gateway_url: str, name: str):
    mock_response = FunctionTagsResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "PUT",
        "url": re.compile(f"^{gateway_url}/registry/v2/models/{name}/tags(\\?.*)?"),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_replace_all(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for replace_all
    Replace Tags On Any/All
    """
    # set path params
    name = "name_example"

    kwargs = {
        # optionally use ReplaceAllQuery to validate and reuse parameters
        "query": ReplaceAllQuery(
            scope="any",
        ),
        "json": UpdateTagsRequestV2Stub.create_instance(),
    }
    _replace_all_set_mock_response(httpx_mock, gateway_url, quote(str(name)))
    resp = await service.model_tags.replace_all(name, **kwargs)
    check_type(resp, Union[FunctionTagsResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_replace_all_without_types(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for replace_all with models not installed
    Replace Tags On Any/All
    """
    # set path params
    name = "name_example"

    kwargs = {
        "query": {
            "scope": "any",
        },
        "json": UpdateTagsRequestV2Stub.create_json(),
    }
    _replace_all_set_mock_response(httpx_mock, gateway_url, quote(str(name)))
    resp = await service.model_tags.replace_all(name, **kwargs)
    check_type(resp, Model)


def _replace_set_mock_response(
    httpx_mock: HTTPXMock, gateway_url: str, name: str, version: str
):
    mock_response = FunctionTagsResponseStub.create_json()
    httpx_mock_kwargs = {
        "method": "PUT",
        "url": re.compile(
            f"^{gateway_url}/registry/v2/models/{name}/versions/{version}/tags(\\?.*)?"
        ),
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)


@pytest.mark.asyncio
@pytest.mark.skipif(not MODELS_AVAILABLE, reason="Types not installed.")
async def test_replace(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for replace
    Replace Tags
    """
    # set path params
    name = "name_example"

    version = "version_example"

    kwargs = {
        "json": UpdateTagsRequestV2Stub.create_instance(),
    }
    _replace_set_mock_response(
        httpx_mock, gateway_url, quote(str(name)), quote(str(version))
    )
    resp = await service.model_tags.replace(name, version, **kwargs)
    check_type(resp, Union[FunctionTagsResponse,])


@pytest.mark.asyncio
@pytest.mark.skipif(MODELS_AVAILABLE, reason="Types installed.")
async def test_replace_without_types(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for replace with models not installed
    Replace Tags
    """
    # set path params
    name = "name_example"

    version = "version_example"

    kwargs = {
        "json": UpdateTagsRequestV2Stub.create_json(),
    }
    _replace_set_mock_response(
        httpx_mock, gateway_url, quote(str(name)), quote(str(version))
    )
    resp = await service.model_tags.replace(name, version, **kwargs)
    check_type(resp, Model)
