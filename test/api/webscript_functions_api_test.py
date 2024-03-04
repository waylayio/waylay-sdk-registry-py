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
from waylay.services.registry.api import WebscriptFunctionsApi
from waylay.services.registry.service import RegistryService


from ..types.post_webscript_job_sync_response_v2_stub import (
    PostWebscriptJobSyncResponseV2Stub,
)
from waylay.services.registry.models import PostWebscriptJobSyncResponseV2


from ..types.post_webscript_job_sync_response_v2_stub import (
    PostWebscriptJobSyncResponseV2Stub,
)
from waylay.services.registry.models import PostWebscriptJobSyncResponseV2


from ..types.get_webscript_response_v2_stub import GetWebscriptResponseV2Stub
from waylay.services.registry.models import GetWebscriptResponseV2


from ..types.get_webscript_response_v2_stub import GetWebscriptResponseV2Stub
from waylay.services.registry.models import GetWebscriptResponseV2


from ..types.jobs_for_webscript_response_v2_stub import JobsForWebscriptResponseV2Stub
from waylay.services.registry.models import JobsForWebscriptResponseV2


from ..types.webscript_versions_response_v2_stub import WebscriptVersionsResponseV2Stub
from waylay.services.registry.models import WebscriptVersionsResponseV2


from ..types.latest_webscripts_response_v2_stub import LatestWebscriptsResponseV2Stub
from waylay.services.registry.models import LatestWebscriptsResponseV2


from ..types.function_meta_stub import FunctionMetaStub


from ..types.get_webscript_response_v2_stub import GetWebscriptResponseV2Stub
from waylay.services.registry.models import GetWebscriptResponseV2


from ..types.post_webscript_job_sync_response_v2_stub import (
    PostWebscriptJobSyncResponseV2Stub,
)
from waylay.services.registry.models import PostWebscriptJobSyncResponseV2


from ..types.rebuild_webscript_sync_response_v2_stub import (
    RebuildWebscriptSyncResponseV2Stub,
)
from waylay.services.registry.models import RebuildWebscriptSyncResponseV2


from ..types.undeployed_response_v2_stub import UndeployedResponseV2Stub
from waylay.services.registry.models import UndeployedResponseV2


from ..types.undeployed_response_v2_stub import UndeployedResponseV2Stub
from waylay.services.registry.models import UndeployedResponseV2


from ..types.file_upload_stub import FileUploadStub


from ..types.post_webscript_job_sync_response_v2_stub import (
    PostWebscriptJobSyncResponseV2Stub,
)
from waylay.services.registry.models import PostWebscriptJobSyncResponseV2


from ..types.post_webscript_job_sync_response_v2_stub import (
    PostWebscriptJobSyncResponseV2Stub,
)
from waylay.services.registry.models import PostWebscriptJobSyncResponseV2


from ..types.verify_webscript_sync_response_v2_stub import (
    VerifyWebscriptSyncResponseV2Stub,
)
from waylay.services.registry.models import VerifyWebscriptSyncResponseV2


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


@pytest.fixture
def webscript_functions_api(waylay_api_client: ApiClient) -> WebscriptFunctionsApi:
    return WebscriptFunctionsApi(waylay_api_client)


def test_registered(waylay_client: WaylayClient):
    """Test that WebscriptFunctionsApi api is registered in the sdk client."""
    assert isinstance(waylay_client.registry.webscript_functions, WebscriptFunctionsApi)


@pytest.mark.asyncio
async def test_create(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for create
    Create Webscript Version
    """
    # set path params
    # set files param
    files = {
        "myFile1": b"...first file content...",
        "myFile2": b"...second file content...",
    }

    mock_response = PostWebscriptJobSyncResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "POST",
        "url": gateway_url + f"/registry/v2/webscripts/",  # noqa: F541
        "content": json.dumps(mock_response, default=str),
        "status_code": 201,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        "files": files,
    }
    resp = await service.webscript_functions.create(**kwargs)
    check_type(resp, PostWebscriptJobSyncResponseV2)


@pytest.mark.asyncio
async def test_delete_asset(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for delete_asset
    Delete Webscript Asset
    """
    # set path params
    name = "name_example"

    version = "version_example"

    wildcard = "wildcard_example"

    mock_response = PostWebscriptJobSyncResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "DELETE",
        "url": gateway_url
        + f"/registry/v2/webscripts/{name}/versions/{version}/content/{wildcard}",  # noqa: F541
        "content": json.dumps(mock_response, default=str),
        "status_code": 201,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        "name": name,
        "version": version,
        "wildcard": wildcard,
    }
    resp = await service.webscript_functions.delete_asset(**kwargs)
    check_type(resp, PostWebscriptJobSyncResponseV2)


@pytest.mark.asyncio
async def test_get_archive(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for get_archive
    Get Webscript Archive
    """
    # set path params
    name = "name_example"

    version = "version_example"

    mock_response = bytes(b"blah")
    httpx_mock_kwargs = {
        "method": "GET",
        "url": gateway_url
        + f"/registry/v2/webscripts/{name}/versions/{version}/content",  # noqa: F541
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        "name": name,
        "version": version,
    }
    resp = await service.webscript_functions.get_archive(**kwargs)
    check_type(resp, bytes)


@pytest.mark.asyncio
async def test_get_asset(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for get_asset
    Get File From Webscript Archive
    """
    # set path params
    name = "name_example"

    version = "version_example"

    wildcard = "wildcard_example"

    mock_response = bytes(b"blah")
    httpx_mock_kwargs = {
        "method": "GET",
        "url": gateway_url
        + f"/registry/v2/webscripts/{name}/versions/{version}/content/{wildcard}",  # noqa: F541
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        "name": name,
        "version": version,
        "wildcard": wildcard,
    }
    resp = await service.webscript_functions.get_asset(**kwargs)
    check_type(resp, bytes)


@pytest.mark.asyncio
async def test_get_latest(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for get_latest
    Get Latest Webscript Version
    """
    # set path params
    name = "name_example"

    mock_response = GetWebscriptResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": gateway_url + f"/registry/v2/webscripts/{name}",  # noqa: F541
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        "name": name,
    }
    resp = await service.webscript_functions.get_latest(**kwargs)
    check_type(resp, GetWebscriptResponseV2)


@pytest.mark.asyncio
async def test_get(service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for get
    Get Webscript Version
    """
    # set path params
    name = "name_example"

    version = "version_example"

    mock_response = GetWebscriptResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": gateway_url + f"/registry/v2/webscripts/{name}/versions/{version}",  # noqa: F541
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        "name": name,
        "version": version,
    }
    resp = await service.webscript_functions.get(**kwargs)
    check_type(resp, GetWebscriptResponseV2)


@pytest.mark.asyncio
async def test_jobs(service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for jobs
    List Webscript Jobs
    """
    # set path params
    name = "name_example"

    version = "version_example"

    mock_response = JobsForWebscriptResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": gateway_url + f"/registry/v2/webscripts/{name}/versions/{version}/jobs",  # noqa: F541
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        "name": name,
        "version": version,
    }
    resp = await service.webscript_functions.jobs(**kwargs)
    check_type(resp, JobsForWebscriptResponseV2)


@pytest.mark.asyncio
async def test_list_versions(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for list_versions
    List Webscript Versions
    """
    # set path params
    name = "name_example"

    mock_response = WebscriptVersionsResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": gateway_url + f"/registry/v2/webscripts/{name}/versions",  # noqa: F541
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        "name": name,
    }
    resp = await service.webscript_functions.list_versions(**kwargs)
    check_type(resp, WebscriptVersionsResponseV2)


@pytest.mark.asyncio
async def test_list(service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock):
    """Test case for list
    List Webscripts
    """
    # set path params

    mock_response = LatestWebscriptsResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": gateway_url + f"/registry/v2/webscripts/",  # noqa: F541
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {}
    resp = await service.webscript_functions.list(**kwargs)
    check_type(resp, LatestWebscriptsResponseV2)


@pytest.mark.asyncio
async def test_patch_metadata(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for patch_metadata
    Patch Webscript Metadata
    """
    # set path params
    name = "name_example"

    version = "version_example"

    # set body param
    body = FunctionMetaStub.create_instance()
    content_type = None
    # content_type = 'application/json'

    mock_response = GetWebscriptResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "PATCH",
        "url": gateway_url
        + f"/registry/v2/webscripts/{name}/versions/{version}/metadata",  # noqa: F541
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        "name": name,
        "version": version,
        "body": body,
        "headers": {"content-type": content_type} if content_type else None,
    }
    resp = await service.webscript_functions.patch_metadata(**kwargs)
    check_type(resp, GetWebscriptResponseV2)


@pytest.mark.asyncio
async def test_publish(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for publish
    Publish Draft Webscript
    """
    # set path params
    name = "name_example"

    version = "version_example"

    mock_response = PostWebscriptJobSyncResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "POST",
        "url": gateway_url
        + f"/registry/v2/webscripts/{name}/versions/{version}/publish",  # noqa: F541
        "content": json.dumps(mock_response, default=str),
        "status_code": 201,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        "name": name,
        "version": version,
    }
    resp = await service.webscript_functions.publish(**kwargs)
    check_type(resp, PostWebscriptJobSyncResponseV2)


@pytest.mark.asyncio
async def test_rebuild(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for rebuild
    Rebuild Webscript
    """
    # set path params
    name = "name_example"

    version = "version_example"

    mock_response = RebuildWebscriptSyncResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "POST",
        "url": gateway_url
        + f"/registry/v2/webscripts/{name}/versions/{version}/rebuild",  # noqa: F541
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        "name": name,
        "version": version,
    }
    resp = await service.webscript_functions.rebuild(**kwargs)
    check_type(resp, RebuildWebscriptSyncResponseV2)


@pytest.mark.asyncio
async def test_remove_version(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for remove_version
    Remove Webscript Version
    """
    # set path params
    name = "name_example"

    version = "version_example"

    mock_response = UndeployedResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "DELETE",
        "url": gateway_url + f"/registry/v2/webscripts/{name}/versions/{version}",  # noqa: F541
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        "name": name,
        "version": version,
    }
    resp = await service.webscript_functions.remove_version(**kwargs)
    check_type(resp, UndeployedResponseV2)


@pytest.mark.asyncio
async def test_remove_versions(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for remove_versions
    Remove Webscript
    """
    # set path params
    name = "name_example"

    mock_response = UndeployedResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "DELETE",
        "url": gateway_url + f"/registry/v2/webscripts/{name}",  # noqa: F541
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        "name": name,
    }
    resp = await service.webscript_functions.remove_versions(**kwargs)
    check_type(resp, UndeployedResponseV2)


@pytest.mark.asyncio
async def test_update_asset(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for update_asset
    Update Webscript Asset
    """
    # set path params
    name = "name_example"

    version = "version_example"

    wildcard = "wildcard_example"

    # set body param
    body = FileUploadStub.create_instance()
    content_type = None
    # content_type = 'application/octet-stream'

    mock_response = PostWebscriptJobSyncResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "PUT",
        "url": gateway_url
        + f"/registry/v2/webscripts/{name}/versions/{version}/content/{wildcard}",  # noqa: F541
        "content": json.dumps(mock_response, default=str),
        "status_code": 201,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        "name": name,
        "version": version,
        "wildcard": wildcard,
        "body": body,
        "headers": {"content-type": content_type} if content_type else None,
    }
    resp = await service.webscript_functions.update_asset(**kwargs)
    check_type(resp, PostWebscriptJobSyncResponseV2)


@pytest.mark.asyncio
async def test_update_assets(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for update_assets
    Update Webscript Assets
    """
    # set path params
    name = "name_example"

    version = "version_example"

    # set files param
    files = {
        "myFile1": b"...first file content...",
        "myFile2": b"...second file content...",
    }

    mock_response = PostWebscriptJobSyncResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "PUT",
        "url": gateway_url
        + f"/registry/v2/webscripts/{name}/versions/{version}/content",  # noqa: F541
        "content": json.dumps(mock_response, default=str),
        "status_code": 201,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        "name": name,
        "version": version,
        "files": files,
    }
    resp = await service.webscript_functions.update_assets(**kwargs)
    check_type(resp, PostWebscriptJobSyncResponseV2)


@pytest.mark.asyncio
async def test_verify(
    service: RegistryService, gateway_url: str, httpx_mock: HTTPXMock
):
    """Test case for verify
    Verify Health Of Webscript
    """
    # set path params
    name = "name_example"

    version = "version_example"

    mock_response = VerifyWebscriptSyncResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "POST",
        "url": gateway_url
        + f"/registry/v2/webscripts/{name}/versions/{version}/verify",  # noqa: F541
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        "name": name,
        "version": version,
    }
    resp = await service.webscript_functions.verify(**kwargs)
    check_type(resp, VerifyWebscriptSyncResponseV2)
