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
from waylay.services.registry.api import ModelFunctionsApi
from waylay.services.registry.service import RegistryService
from ..fixtures import WaylayTokenStub, waylay_api_client, waylay_config, waylay_token_credentials, gateway_url, registry_service


from ..types.multipart_file_upload_stub import MultipartFileUploadStub


from ..types.post_model_job_sync_response_v2_stub import PostModelJobSyncResponseV2Stub
from waylay.services.registry.models import PostModelJobSyncResponseV2


from ..types.post_model_job_sync_response_v2_stub import PostModelJobSyncResponseV2Stub
from waylay.services.registry.models import PostModelJobSyncResponseV2


from ..types.get_model_response_v2_stub import GetModelResponseV2Stub
from waylay.services.registry.models import GetModelResponseV2


from ..types.get_model_response_v2_stub import GetModelResponseV2Stub
from waylay.services.registry.models import GetModelResponseV2


from ..types.jobs_for_model_response_v2_stub import JobsForModelResponseV2Stub
from waylay.services.registry.models import JobsForModelResponseV2


from ..types.latest_models_response_v2_stub import LatestModelsResponseV2Stub
from waylay.services.registry.models import LatestModelsResponseV2


from ..types.model_versions_response_v2_stub import ModelVersionsResponseV2Stub
from waylay.services.registry.models import ModelVersionsResponseV2


from ..types.function_meta_stub import FunctionMetaStub


from ..types.get_model_response_v2_stub import GetModelResponseV2Stub
from waylay.services.registry.models import GetModelResponseV2


from ..types.post_model_job_sync_response_v2_stub import PostModelJobSyncResponseV2Stub
from waylay.services.registry.models import PostModelJobSyncResponseV2


from ..types.rebuild_model_sync_response_v2_stub import RebuildModelSyncResponseV2Stub
from waylay.services.registry.models import RebuildModelSyncResponseV2


from ..types.undeployed_response_v2_stub import UndeployedResponseV2Stub
from waylay.services.registry.models import UndeployedResponseV2


from ..types.undeployed_response_v2_stub import UndeployedResponseV2Stub
from waylay.services.registry.models import UndeployedResponseV2


from ..types.file_upload_stub import FileUploadStub


from ..types.post_model_job_sync_response_v2_stub import PostModelJobSyncResponseV2Stub
from waylay.services.registry.models import PostModelJobSyncResponseV2


from ..types.multipart_file_upload_stub import MultipartFileUploadStub


from ..types.post_model_job_sync_response_v2_stub import PostModelJobSyncResponseV2Stub
from waylay.services.registry.models import PostModelJobSyncResponseV2


from ..types.verify_model_sync_response_v2_stub import VerifyModelSyncResponseV2Stub
from waylay.services.registry.models import VerifyModelSyncResponseV2


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


@pytest.fixture
def model_functions_api(waylay_api_client: ApiClient) -> ModelFunctionsApi:
    return ModelFunctionsApi(waylay_api_client)


@pytest.mark.asyncio
async def test_create(registry_service: RegistryService, gateway_url: str, mocker, httpx_mock: HTTPXMock):
    """Test case for create
        Create Model
    """
    # set path params
    # set files param
    files = {
        'myFile1': b'...first file content...',
        'myFile2': b'...second file content...',
    }

    mocker.patch('waylay.sdk.WaylayTokenAuth.assure_valid_token', lambda *args: WaylayTokenStub())
    mock_response = PostModelJobSyncResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "POST",
        "url": gateway_url + f"/registry/v2/models/",
        "content": json.dumps(mock_response, default=str),
        "status_code": 201,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        'files': files,

    }
    resp = await registry_service.model_functions.create(**kwargs)
    assert isinstance(resp, PostModelJobSyncResponseV2)


@pytest.mark.asyncio
async def test_delete_asset(registry_service: RegistryService, gateway_url: str, mocker, httpx_mock: HTTPXMock):
    """Test case for delete_asset
        Delete Model Asset
    """
    # set path params
    name = 'name_example'

    version = 'version_example'

    wildcard = 'wildcard_example'

    mocker.patch('waylay.sdk.WaylayTokenAuth.assure_valid_token', lambda *args: WaylayTokenStub())
    mock_response = PostModelJobSyncResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "DELETE",
        "url": gateway_url + f"/registry/v2/models/{name}/versions/{version}/content/{wildcard}",
        "content": json.dumps(mock_response, default=str),
        "status_code": 201,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        'name': name,
        'version': version,
        'wildcard': wildcard,

    }
    resp = await registry_service.model_functions.delete_asset(**kwargs)
    assert isinstance(resp, PostModelJobSyncResponseV2)


@pytest.mark.asyncio
async def test_get_archive(registry_service: RegistryService, gateway_url: str, mocker, httpx_mock: HTTPXMock):
    """Test case for get_archive
        Get Model Archive
    """
    # set path params
    name = 'name_example'

    version = 'version_example'

    mocker.patch('waylay.sdk.WaylayTokenAuth.assure_valid_token', lambda *args: WaylayTokenStub())
    mock_response = bytes(b'blah')
    httpx_mock_kwargs = {
        "method": "GET",
        "url": gateway_url + f"/registry/v2/models/{name}/versions/{version}/content",
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        'name': name,
        'version': version,

    }
    resp = await registry_service.model_functions.get_archive(**kwargs)
    assert isinstance(resp, bytes)


@pytest.mark.asyncio
async def test_get_asset(registry_service: RegistryService, gateway_url: str, mocker, httpx_mock: HTTPXMock):
    """Test case for get_asset
        Get File From Model Archive
    """
    # set path params
    name = 'name_example'

    version = 'version_example'

    wildcard = 'wildcard_example'

    mocker.patch('waylay.sdk.WaylayTokenAuth.assure_valid_token', lambda *args: WaylayTokenStub())
    mock_response = bytes(b'blah')
    httpx_mock_kwargs = {
        "method": "GET",
        "url": gateway_url + f"/registry/v2/models/{name}/versions/{version}/content/{wildcard}",
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        'name': name,
        'version': version,
        'wildcard': wildcard,

    }
    resp = await registry_service.model_functions.get_asset(**kwargs)
    assert isinstance(resp, bytes)


@pytest.mark.asyncio
async def test_get_latest_version(registry_service: RegistryService, gateway_url: str, mocker, httpx_mock: HTTPXMock):
    """Test case for get_latest_version
        Get Latest Model Version
    """
    # set path params
    name = 'name_example'

    mocker.patch('waylay.sdk.WaylayTokenAuth.assure_valid_token', lambda *args: WaylayTokenStub())
    mock_response = GetModelResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": gateway_url + f"/registry/v2/models/{name}",
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        'name': name,

    }
    resp = await registry_service.model_functions.get_latest_version(**kwargs)
    assert isinstance(resp, GetModelResponseV2)


@pytest.mark.asyncio
async def test_get_version(registry_service: RegistryService, gateway_url: str, mocker, httpx_mock: HTTPXMock):
    """Test case for get_version
        Get Model Version
    """
    # set path params
    name = 'name_example'

    version = 'version_example'

    mocker.patch('waylay.sdk.WaylayTokenAuth.assure_valid_token', lambda *args: WaylayTokenStub())
    mock_response = GetModelResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": gateway_url + f"/registry/v2/models/{name}/versions/{version}",
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        'name': name,
        'version': version,

    }
    resp = await registry_service.model_functions.get_version(**kwargs)
    assert isinstance(resp, GetModelResponseV2)


@pytest.mark.asyncio
async def test_jobs(registry_service: RegistryService, gateway_url: str, mocker, httpx_mock: HTTPXMock):
    """Test case for jobs
        List Model Jobs
    """
    # set path params
    name = 'name_example'

    version = 'version_example'

    mocker.patch('waylay.sdk.WaylayTokenAuth.assure_valid_token', lambda *args: WaylayTokenStub())
    mock_response = JobsForModelResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": gateway_url + f"/registry/v2/models/{name}/versions/{version}/jobs",
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        'name': name,
        'version': version,

    }
    resp = await registry_service.model_functions.jobs(**kwargs)
    assert isinstance(resp, JobsForModelResponseV2)


@pytest.mark.asyncio
async def test_list_all(registry_service: RegistryService, gateway_url: str, mocker, httpx_mock: HTTPXMock):
    """Test case for list_all
        List Models
    """
    # set path params

    mocker.patch('waylay.sdk.WaylayTokenAuth.assure_valid_token', lambda *args: WaylayTokenStub())
    mock_response = LatestModelsResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": gateway_url + f"/registry/v2/models/",
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {

    }
    resp = await registry_service.model_functions.list_all(**kwargs)
    assert isinstance(resp, LatestModelsResponseV2)


@pytest.mark.asyncio
async def test_list_versions(registry_service: RegistryService, gateway_url: str, mocker, httpx_mock: HTTPXMock):
    """Test case for list_versions
        List Model Versions
    """
    # set path params
    name = 'name_example'

    mocker.patch('waylay.sdk.WaylayTokenAuth.assure_valid_token', lambda *args: WaylayTokenStub())
    mock_response = ModelVersionsResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "GET",
        "url": gateway_url + f"/registry/v2/models/{name}/versions",
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        'name': name,

    }
    resp = await registry_service.model_functions.list_versions(**kwargs)
    assert isinstance(resp, ModelVersionsResponseV2)


@pytest.mark.asyncio
async def test_patch_metadata(registry_service: RegistryService, gateway_url: str, mocker, httpx_mock: HTTPXMock):
    """Test case for patch_metadata
        Patch Model Metadata
    """
    # set path params
    name = 'name_example'

    version = 'version_example'

    # set body param
    body = FunctionMetaStub.create_instance()
    content_type = 'application/json'

    mocker.patch('waylay.sdk.WaylayTokenAuth.assure_valid_token', lambda *args: WaylayTokenStub())
    mock_response = GetModelResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "PATCH",
        "url": gateway_url + f"/registry/v2/models/{name}/versions/{version}/metadata",
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        'name': name,
        'version': version,

        'body': body,
        '_headers': {'content-type': content_type} if content_type else None,

    }
    resp = await registry_service.model_functions.patch_metadata(**kwargs)
    assert isinstance(resp, GetModelResponseV2)


@pytest.mark.asyncio
async def test_publish(registry_service: RegistryService, gateway_url: str, mocker, httpx_mock: HTTPXMock):
    """Test case for publish
        Publish Draft Model
    """
    # set path params
    name = 'name_example'

    version = 'version_example'

    mocker.patch('waylay.sdk.WaylayTokenAuth.assure_valid_token', lambda *args: WaylayTokenStub())
    mock_response = PostModelJobSyncResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "POST",
        "url": gateway_url + f"/registry/v2/models/{name}/versions/{version}/publish",
        "content": json.dumps(mock_response, default=str),
        "status_code": 201,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        'name': name,
        'version': version,

    }
    resp = await registry_service.model_functions.publish(**kwargs)
    assert isinstance(resp, PostModelJobSyncResponseV2)


@pytest.mark.asyncio
async def test_rebuild(registry_service: RegistryService, gateway_url: str, mocker, httpx_mock: HTTPXMock):
    """Test case for rebuild
        Rebuild Model
    """
    # set path params
    name = 'name_example'

    version = 'version_example'

    mocker.patch('waylay.sdk.WaylayTokenAuth.assure_valid_token', lambda *args: WaylayTokenStub())
    mock_response = RebuildModelSyncResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "POST",
        "url": gateway_url + f"/registry/v2/models/{name}/versions/{version}/rebuild",
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        'name': name,
        'version': version,

    }
    resp = await registry_service.model_functions.rebuild(**kwargs)
    assert isinstance(resp, RebuildModelSyncResponseV2)


@pytest.mark.asyncio
async def test_remove_version(registry_service: RegistryService, gateway_url: str, mocker, httpx_mock: HTTPXMock):
    """Test case for remove_version
        Remove Model Version
    """
    # set path params
    name = 'name_example'

    version = 'version_example'

    mocker.patch('waylay.sdk.WaylayTokenAuth.assure_valid_token', lambda *args: WaylayTokenStub())
    mock_response = UndeployedResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "DELETE",
        "url": gateway_url + f"/registry/v2/models/{name}/versions/{version}",
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        'name': name,
        'version': version,

    }
    resp = await registry_service.model_functions.remove_version(**kwargs)
    assert isinstance(resp, UndeployedResponseV2)


@pytest.mark.asyncio
async def test_remove_versions(registry_service: RegistryService, gateway_url: str, mocker, httpx_mock: HTTPXMock):
    """Test case for remove_versions
        Remove Model
    """
    # set path params
    name = 'name_example'

    mocker.patch('waylay.sdk.WaylayTokenAuth.assure_valid_token', lambda *args: WaylayTokenStub())
    mock_response = UndeployedResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "DELETE",
        "url": gateway_url + f"/registry/v2/models/{name}",
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        'name': name,

    }
    resp = await registry_service.model_functions.remove_versions(**kwargs)
    assert isinstance(resp, UndeployedResponseV2)


@pytest.mark.asyncio
async def test_update_asset(registry_service: RegistryService, gateway_url: str, mocker, httpx_mock: HTTPXMock):
    """Test case for update_asset
        Update Model Asset
    """
    # set path params
    name = 'name_example'

    version = 'version_example'

    wildcard = 'wildcard_example'

    # set body param
    body = FileUploadStub.create_instance()
    content_type = 'application/octet-stream'

    mocker.patch('waylay.sdk.WaylayTokenAuth.assure_valid_token', lambda *args: WaylayTokenStub())
    mock_response = PostModelJobSyncResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "PUT",
        "url": gateway_url + f"/registry/v2/models/{name}/versions/{version}/content/{wildcard}",
        "content": json.dumps(mock_response, default=str),
        "status_code": 201,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        'name': name,
        'version': version,
        'wildcard': wildcard,

        'body': body,
        '_headers': {'content-type': content_type} if content_type else None,

    }
    resp = await registry_service.model_functions.update_asset(**kwargs)
    assert isinstance(resp, PostModelJobSyncResponseV2)


@pytest.mark.asyncio
async def test_update_assets(registry_service: RegistryService, gateway_url: str, mocker, httpx_mock: HTTPXMock):
    """Test case for update_assets
        Update Model Assets
    """
    # set path params
    name = 'name_example'

    version = 'version_example'

    # set files param
    files = {
        'myFile1': b'...first file content...',
        'myFile2': b'...second file content...',
    }

    mocker.patch('waylay.sdk.WaylayTokenAuth.assure_valid_token', lambda *args: WaylayTokenStub())
    mock_response = PostModelJobSyncResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "PUT",
        "url": gateway_url + f"/registry/v2/models/{name}/versions/{version}/content",
        "content": json.dumps(mock_response, default=str),
        "status_code": 201,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        'name': name,
        'version': version,
        'files': files,

    }
    resp = await registry_service.model_functions.update_assets(**kwargs)
    assert isinstance(resp, PostModelJobSyncResponseV2)


@pytest.mark.asyncio
async def test_verify(registry_service: RegistryService, gateway_url: str, mocker, httpx_mock: HTTPXMock):
    """Test case for verify
        Verify Health Of Model
    """
    # set path params
    name = 'name_example'

    version = 'version_example'

    mocker.patch('waylay.sdk.WaylayTokenAuth.assure_valid_token', lambda *args: WaylayTokenStub())
    mock_response = VerifyModelSyncResponseV2Stub.create_instance().to_dict()
    httpx_mock_kwargs = {
        "method": "POST",
        "url": gateway_url + f"/registry/v2/models/{name}/versions/{version}/verify",
        "content": json.dumps(mock_response, default=str),
        "status_code": 200,
    }
    httpx_mock.add_response(**httpx_mock_kwargs)
    kwargs = {
        'name': name,
        'version': version,

    }
    resp = await registry_service.model_functions.verify(**kwargs)
    assert isinstance(resp, VerifyModelSyncResponseV2)
