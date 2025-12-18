# Waylay Registry Service
V2 API to build and deploy Waylay functions (plugs, webscripts, BYOML models).

This Python package is automatically generated based on the 
Waylay Registry OpenAPI specification (API version: 2.24.1)
For more information, please visit [the openapi specification](https://docs.waylay.io/openapi/public/redocly/registry.html).

It consists of two sub-packages that are both plugins for the waylay-sdk-core package.
- The `waylay-sdk-registry` sub-package contains the Registry api methods.
- The `waylay-sdk-registry-types` sub-package is an extension that contains the typed model classes for all path params, query params, body params and responses for each of the api methods in `waylay-sdk-registry`.

## Requirements.
This package requires Python 3.10+.

## Installation

Normally this package is installed together with support for other services using the [waylay-sdk](https://pypi.org/project/waylay-sdk/) umbrella package:
* `pip install waylay-sdk` will install `waylay-sdk-registry` together with the SDK api packages for other services.
* `pip install waylay-sdk[types-registry]` will additionally install the types package `waylay-sdk-registry-types`.
* `pip install waylay-sdk[types]` will install the types packages for this and all other services.

Alternatively, you can install support for this _registry_ service only, installing or extending an existing [waylay-sdk-core](https://pypi.org/project/waylay-sdk-core/):

- `pip install waylay-sdk-registry` to only install api support for _registry_.
- `pip install waylay-sdk-registry[types]` to additionally install type support for _registry_.

## Usage

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.root_page_response import RootPageResponse
try:
    # Get Service Status
    # calls `GET /registry/v2/`
    api_response = await waylay_client.registry.about.get(
    )
    print("The response of registry.about.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.about.get: %s\n" % e)
```


For more information, please visit the [Waylay API documentation](https://docs.waylay.io/#/api/?id=software-development-kits).

## Documentation for API Endpoints

All URIs are relative to *https://api.waylay.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AboutApi* | [**get**](docs/AboutApi.md#get) | **GET** /registry/v2/ | Get Service Status
*JobsApi* | [**events**](docs/JobsApi.md#events) | **GET** /registry/v2/jobs/events | Stream Events
*JobsApi* | [**get**](docs/JobsApi.md#get) | **GET** /registry/v2/jobs/{type}/{id} | Get Job
*JobsApi* | [**list**](docs/JobsApi.md#list) | **GET** /registry/v2/jobs/ | List Jobs
*ModelTagsApi* | [**add_all**](docs/ModelTagsApi.md#add_all) | **PATCH** /registry/v2/models/{name}/tags | Add Tags On All
*ModelTagsApi* | [**add**](docs/ModelTagsApi.md#add) | **PATCH** /registry/v2/models/{name}/versions/{version}/tags | Add Tags
*ModelTagsApi* | [**clear_all**](docs/ModelTagsApi.md#clear_all) | **DELETE** /registry/v2/models/{name}/tags | Clear Tags On Any/All
*ModelTagsApi* | [**clear**](docs/ModelTagsApi.md#clear) | **DELETE** /registry/v2/models/{name}/versions/{version}/tags | Clear Tags
*ModelTagsApi* | [**find_all**](docs/ModelTagsApi.md#find_all) | **GET** /registry/v2/models/{name}/tags/{tagName} | Find Tags On Any/All
*ModelTagsApi* | [**find**](docs/ModelTagsApi.md#find) | **GET** /registry/v2/models/{name}/versions/{version}/tags/{tagName} | Find Tag
*ModelTagsApi* | [**list_all**](docs/ModelTagsApi.md#list_all) | **GET** /registry/v2/models/{name}/tags | List Tags On Any/All
*ModelTagsApi* | [**list**](docs/ModelTagsApi.md#list) | **GET** /registry/v2/models/{name}/versions/{version}/tags | List Tags
*ModelTagsApi* | [**put_all**](docs/ModelTagsApi.md#put_all) | **PUT** /registry/v2/models/{name}/tags/{tagName} | Put Tag On All
*ModelTagsApi* | [**put**](docs/ModelTagsApi.md#put) | **PUT** /registry/v2/models/{name}/versions/{version}/tags/{tagName} | Put Tag
*ModelTagsApi* | [**remove_all**](docs/ModelTagsApi.md#remove_all) | **DELETE** /registry/v2/models/{name}/tags/{tagName} | Remove Tag On Any/All
*ModelTagsApi* | [**remove**](docs/ModelTagsApi.md#remove) | **DELETE** /registry/v2/models/{name}/versions/{version}/tags/{tagName} | Remove Tag
*ModelTagsApi* | [**replace_all**](docs/ModelTagsApi.md#replace_all) | **PUT** /registry/v2/models/{name}/tags | Replace Tags On Any/All
*ModelTagsApi* | [**replace**](docs/ModelTagsApi.md#replace) | **PUT** /registry/v2/models/{name}/versions/{version}/tags | Replace Tags
*ModelsApi* | [**create**](docs/ModelsApi.md#create) | **POST** /registry/v2/models/ | Create Version
*ModelsApi* | [**delete_asset**](docs/ModelsApi.md#delete_asset) | **DELETE** /registry/v2/models/{name}/versions/{version}/content/{wildcard} | Delete Asset
*ModelsApi* | [**get_archive**](docs/ModelsApi.md#get_archive) | **GET** /registry/v2/models/{name}/versions/{version}/content | Get Archive
*ModelsApi* | [**get_asset_by_role**](docs/ModelsApi.md#get_asset_by_role) | **GET** /registry/v2/models/{name}/versions/{version}/{assetRole} | Get Asset By Role
*ModelsApi* | [**get_asset**](docs/ModelsApi.md#get_asset) | **GET** /registry/v2/models/{name}/versions/{version}/content/{wildcard} | Get Asset
*ModelsApi* | [**get_latest**](docs/ModelsApi.md#get_latest) | **GET** /registry/v2/models/{name} | Get Latest
*ModelsApi* | [**get**](docs/ModelsApi.md#get) | **GET** /registry/v2/models/{name}/versions/{version} | Get Version
*ModelsApi* | [**jobs**](docs/ModelsApi.md#jobs) | **GET** /registry/v2/models/{name}/versions/{version}/jobs | List Jobs
*ModelsApi* | [**list**](docs/ModelsApi.md#list) | **GET** /registry/v2/models/ | List
*ModelsApi* | [**list_versions**](docs/ModelsApi.md#list_versions) | **GET** /registry/v2/models/{name}/versions | List Versions
*ModelsApi* | [**patch_manifest**](docs/ModelsApi.md#patch_manifest) | **PATCH** /registry/v2/models/{name}/versions/{version}/manifest | Patch Manifest
*ModelsApi* | [**patch_metadata**](docs/ModelsApi.md#patch_metadata) | **PATCH** /registry/v2/models/{name}/versions/{version}/metadata | Patch Metadata
*ModelsApi* | [**protect**](docs/ModelsApi.md#protect) | **POST** /registry/v2/models/{name}/versions/{version}/protect | Protect Version
*ModelsApi* | [**protect_versions**](docs/ModelsApi.md#protect_versions) | **POST** /registry/v2/models/{name}/protect | Protect
*ModelsApi* | [**publish**](docs/ModelsApi.md#publish) | **POST** /registry/v2/models/{name}/versions/{version}/publish | Publish Draft
*ModelsApi* | [**rebuild**](docs/ModelsApi.md#rebuild) | **POST** /registry/v2/models/{name}/versions/{version}/rebuild | Rebuild
*ModelsApi* | [**remove_version**](docs/ModelsApi.md#remove_version) | **DELETE** /registry/v2/models/{name}/versions/{version} | Remove Version
*ModelsApi* | [**remove_versions**](docs/ModelsApi.md#remove_versions) | **DELETE** /registry/v2/models/{name} | Remove
*ModelsApi* | [**update_asset_by_role**](docs/ModelsApi.md#update_asset_by_role) | **PUT** /registry/v2/models/{name}/versions/{version}/{assetRole} | Update Asset By Role
*ModelsApi* | [**update_asset**](docs/ModelsApi.md#update_asset) | **PUT** /registry/v2/models/{name}/versions/{version}/content/{wildcard} | Update Asset
*ModelsApi* | [**update_assets**](docs/ModelsApi.md#update_assets) | **PUT** /registry/v2/models/{name}/versions/{version}/content | Update Assets
*ModelsApi* | [**verify**](docs/ModelsApi.md#verify) | **POST** /registry/v2/models/{name}/versions/{version}/verify | Verify Health
*PlugTagsApi* | [**add_all**](docs/PlugTagsApi.md#add_all) | **PATCH** /registry/v2/plugs/{name}/tags | Add Tags On All
*PlugTagsApi* | [**add**](docs/PlugTagsApi.md#add) | **PATCH** /registry/v2/plugs/{name}/versions/{version}/tags | Add Tags
*PlugTagsApi* | [**clear_all**](docs/PlugTagsApi.md#clear_all) | **DELETE** /registry/v2/plugs/{name}/tags | Clear Tags On Any/All
*PlugTagsApi* | [**clear**](docs/PlugTagsApi.md#clear) | **DELETE** /registry/v2/plugs/{name}/versions/{version}/tags | Clear Tags
*PlugTagsApi* | [**find_all**](docs/PlugTagsApi.md#find_all) | **GET** /registry/v2/plugs/{name}/tags/{tagName} | Find Tags On Any/All
*PlugTagsApi* | [**find**](docs/PlugTagsApi.md#find) | **GET** /registry/v2/plugs/{name}/versions/{version}/tags/{tagName} | Find Tag
*PlugTagsApi* | [**list_all**](docs/PlugTagsApi.md#list_all) | **GET** /registry/v2/plugs/{name}/tags | List Tags On Any/All
*PlugTagsApi* | [**list**](docs/PlugTagsApi.md#list) | **GET** /registry/v2/plugs/{name}/versions/{version}/tags | List Tags
*PlugTagsApi* | [**put_all**](docs/PlugTagsApi.md#put_all) | **PUT** /registry/v2/plugs/{name}/tags/{tagName} | Put Tag On All
*PlugTagsApi* | [**put**](docs/PlugTagsApi.md#put) | **PUT** /registry/v2/plugs/{name}/versions/{version}/tags/{tagName} | Put Tag
*PlugTagsApi* | [**remove_all**](docs/PlugTagsApi.md#remove_all) | **DELETE** /registry/v2/plugs/{name}/tags/{tagName} | Remove Tag On Any/All
*PlugTagsApi* | [**remove**](docs/PlugTagsApi.md#remove) | **DELETE** /registry/v2/plugs/{name}/versions/{version}/tags/{tagName} | Remove Tag
*PlugTagsApi* | [**replace_all**](docs/PlugTagsApi.md#replace_all) | **PUT** /registry/v2/plugs/{name}/tags | Replace Tags On Any/All
*PlugTagsApi* | [**replace**](docs/PlugTagsApi.md#replace) | **PUT** /registry/v2/plugs/{name}/versions/{version}/tags | Replace Tags
*PlugsApi* | [**create**](docs/PlugsApi.md#create) | **POST** /registry/v2/plugs/ | Create Version
*PlugsApi* | [**delete_asset**](docs/PlugsApi.md#delete_asset) | **DELETE** /registry/v2/plugs/{name}/versions/{version}/content/{wildcard} | Delete Asset
*PlugsApi* | [**get_archive**](docs/PlugsApi.md#get_archive) | **GET** /registry/v2/plugs/{name}/versions/{version}/content | Get Archive
*PlugsApi* | [**get_asset_by_role**](docs/PlugsApi.md#get_asset_by_role) | **GET** /registry/v2/plugs/{name}/versions/{version}/{assetRole} | Get Asset By Role
*PlugsApi* | [**get_asset**](docs/PlugsApi.md#get_asset) | **GET** /registry/v2/plugs/{name}/versions/{version}/content/{wildcard} | Get Asset
*PlugsApi* | [**get_latest**](docs/PlugsApi.md#get_latest) | **GET** /registry/v2/plugs/{name} | Get Latest
*PlugsApi* | [**get**](docs/PlugsApi.md#get) | **GET** /registry/v2/plugs/{name}/versions/{version} | Get Version
*PlugsApi* | [**jobs**](docs/PlugsApi.md#jobs) | **GET** /registry/v2/plugs/{name}/versions/{version}/jobs | List Jobs
*PlugsApi* | [**list**](docs/PlugsApi.md#list) | **GET** /registry/v2/plugs/ | List
*PlugsApi* | [**list_versions**](docs/PlugsApi.md#list_versions) | **GET** /registry/v2/plugs/{name}/versions | List Versions
*PlugsApi* | [**patch_interface**](docs/PlugsApi.md#patch_interface) | **PATCH** /registry/v2/plugs/{name}/versions/{version}/interface | Patch Interface
*PlugsApi* | [**patch_manifest**](docs/PlugsApi.md#patch_manifest) | **PATCH** /registry/v2/plugs/{name}/versions/{version}/manifest | Patch Manifest
*PlugsApi* | [**patch_metadata**](docs/PlugsApi.md#patch_metadata) | **PATCH** /registry/v2/plugs/{name}/versions/{version}/metadata | Patch Metadata
*PlugsApi* | [**protect**](docs/PlugsApi.md#protect) | **POST** /registry/v2/plugs/{name}/versions/{version}/protect | Protect Version
*PlugsApi* | [**protect_versions**](docs/PlugsApi.md#protect_versions) | **POST** /registry/v2/plugs/{name}/protect | Protect
*PlugsApi* | [**publish**](docs/PlugsApi.md#publish) | **POST** /registry/v2/plugs/{name}/versions/{version}/publish | Publish Draft
*PlugsApi* | [**rebuild**](docs/PlugsApi.md#rebuild) | **POST** /registry/v2/plugs/{name}/versions/{version}/rebuild | Rebuild
*PlugsApi* | [**remove_version**](docs/PlugsApi.md#remove_version) | **DELETE** /registry/v2/plugs/{name}/versions/{version} | Remove Version
*PlugsApi* | [**remove_versions**](docs/PlugsApi.md#remove_versions) | **DELETE** /registry/v2/plugs/{name} | Remove
*PlugsApi* | [**update_asset_by_role**](docs/PlugsApi.md#update_asset_by_role) | **PUT** /registry/v2/plugs/{name}/versions/{version}/{assetRole} | Update Asset By Role
*PlugsApi* | [**update_asset**](docs/PlugsApi.md#update_asset) | **PUT** /registry/v2/plugs/{name}/versions/{version}/content/{wildcard} | Update Asset
*PlugsApi* | [**update_assets**](docs/PlugsApi.md#update_assets) | **PUT** /registry/v2/plugs/{name}/versions/{version}/content | Update Assets
*PlugsApi* | [**verify**](docs/PlugsApi.md#verify) | **POST** /registry/v2/plugs/{name}/versions/{version}/verify | Verify Health
*RuntimesApi* | [**example_archive**](docs/RuntimesApi.md#example_archive) | **GET** /registry/v2/runtimes/{name}/versions/{version}/example | Get Runtime Example Archive
*RuntimesApi* | [**get_example_asset**](docs/RuntimesApi.md#get_example_asset) | **GET** /registry/v2/runtimes/{name}/versions/{version}/example/{wildcard} | Get File From Runtime Example Archive
*RuntimesApi* | [**get_latest**](docs/RuntimesApi.md#get_latest) | **GET** /registry/v2/runtimes/{name} | Get Latest Runtime Version
*RuntimesApi* | [**get**](docs/RuntimesApi.md#get) | **GET** /registry/v2/runtimes/{name}/versions/{version} | Get Runtime Version
*RuntimesApi* | [**list**](docs/RuntimesApi.md#list) | **GET** /registry/v2/runtimes/ | List Runtimes
*RuntimesApi* | [**list_versions**](docs/RuntimesApi.md#list_versions) | **GET** /registry/v2/runtimes/{name}/versions | List Runtime Versions
*RuntimesApi* | [**tag**](docs/RuntimesApi.md#tag) | **GET** /registry/v2/runtimeTags/{tagName} | Get Runtime Tag
*RuntimesApi* | [**tags**](docs/RuntimesApi.md#tags) | **GET** /registry/v2/runtimeTags/ | List Runtime Tags
*SchemasApi* | [**get_by_role**](docs/SchemasApi.md#get_by_role) | **GET** /registry/v2/schemas/{functionType}/{role}/schema | Get Asset Schema
*SchemasApi* | [**get**](docs/SchemasApi.md#get) | **GET** /registry/v2/schemas/{schemaId} | Get Asset Schema
*TagsApi* | [**get**](docs/TagsApi.md#get) | **GET** /registry/v2/tags/{tagName} | Get
*TagsApi* | [**list**](docs/TagsApi.md#list) | **GET** /registry/v2/tags/ | List
*TagsApi* | [**remove**](docs/TagsApi.md#remove) | **DELETE** /registry/v2/tags/ | Remove Unused
*WebscriptTagsApi* | [**add_all**](docs/WebscriptTagsApi.md#add_all) | **PATCH** /registry/v2/webscripts/{name}/tags | Add Tags On All
*WebscriptTagsApi* | [**add**](docs/WebscriptTagsApi.md#add) | **PATCH** /registry/v2/webscripts/{name}/versions/{version}/tags | Add Tags
*WebscriptTagsApi* | [**clear_all**](docs/WebscriptTagsApi.md#clear_all) | **DELETE** /registry/v2/webscripts/{name}/tags | Clear Tags On Any/All
*WebscriptTagsApi* | [**clear**](docs/WebscriptTagsApi.md#clear) | **DELETE** /registry/v2/webscripts/{name}/versions/{version}/tags | Clear Tags
*WebscriptTagsApi* | [**find_all**](docs/WebscriptTagsApi.md#find_all) | **GET** /registry/v2/webscripts/{name}/tags/{tagName} | Find Tags On Any/All
*WebscriptTagsApi* | [**find**](docs/WebscriptTagsApi.md#find) | **GET** /registry/v2/webscripts/{name}/versions/{version}/tags/{tagName} | Find Tag
*WebscriptTagsApi* | [**list_all**](docs/WebscriptTagsApi.md#list_all) | **GET** /registry/v2/webscripts/{name}/tags | List Tags On Any/All
*WebscriptTagsApi* | [**list**](docs/WebscriptTagsApi.md#list) | **GET** /registry/v2/webscripts/{name}/versions/{version}/tags | List Tags
*WebscriptTagsApi* | [**put_all**](docs/WebscriptTagsApi.md#put_all) | **PUT** /registry/v2/webscripts/{name}/tags/{tagName} | Put Tag On All
*WebscriptTagsApi* | [**put**](docs/WebscriptTagsApi.md#put) | **PUT** /registry/v2/webscripts/{name}/versions/{version}/tags/{tagName} | Put Tag
*WebscriptTagsApi* | [**remove_all**](docs/WebscriptTagsApi.md#remove_all) | **DELETE** /registry/v2/webscripts/{name}/tags/{tagName} | Remove Tag On Any/All
*WebscriptTagsApi* | [**remove**](docs/WebscriptTagsApi.md#remove) | **DELETE** /registry/v2/webscripts/{name}/versions/{version}/tags/{tagName} | Remove Tag
*WebscriptTagsApi* | [**replace_all**](docs/WebscriptTagsApi.md#replace_all) | **PUT** /registry/v2/webscripts/{name}/tags | Replace Tags On Any/All
*WebscriptTagsApi* | [**replace**](docs/WebscriptTagsApi.md#replace) | **PUT** /registry/v2/webscripts/{name}/versions/{version}/tags | Replace Tags
*WebscriptsApi* | [**create**](docs/WebscriptsApi.md#create) | **POST** /registry/v2/webscripts/ | Create Version
*WebscriptsApi* | [**delete_asset**](docs/WebscriptsApi.md#delete_asset) | **DELETE** /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard} | Delete Asset
*WebscriptsApi* | [**get_archive**](docs/WebscriptsApi.md#get_archive) | **GET** /registry/v2/webscripts/{name}/versions/{version}/content | Get Archive
*WebscriptsApi* | [**get_asset_by_role**](docs/WebscriptsApi.md#get_asset_by_role) | **GET** /registry/v2/webscripts/{name}/versions/{version}/{assetRole} | Get Asset By Role
*WebscriptsApi* | [**get_asset**](docs/WebscriptsApi.md#get_asset) | **GET** /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard} | Get Asset
*WebscriptsApi* | [**get_latest**](docs/WebscriptsApi.md#get_latest) | **GET** /registry/v2/webscripts/{name} | Get Latest
*WebscriptsApi* | [**get**](docs/WebscriptsApi.md#get) | **GET** /registry/v2/webscripts/{name}/versions/{version} | Get Version
*WebscriptsApi* | [**jobs**](docs/WebscriptsApi.md#jobs) | **GET** /registry/v2/webscripts/{name}/versions/{version}/jobs | List Jobs
*WebscriptsApi* | [**list_versions**](docs/WebscriptsApi.md#list_versions) | **GET** /registry/v2/webscripts/{name}/versions | List Versions
*WebscriptsApi* | [**list**](docs/WebscriptsApi.md#list) | **GET** /registry/v2/webscripts/ | List
*WebscriptsApi* | [**patch_manifest**](docs/WebscriptsApi.md#patch_manifest) | **PATCH** /registry/v2/webscripts/{name}/versions/{version}/manifest | Patch Manifest
*WebscriptsApi* | [**patch_metadata**](docs/WebscriptsApi.md#patch_metadata) | **PATCH** /registry/v2/webscripts/{name}/versions/{version}/metadata | Patch Metadata
*WebscriptsApi* | [**protect_versions**](docs/WebscriptsApi.md#protect_versions) | **POST** /registry/v2/webscripts/{name}/protect | Protect
*WebscriptsApi* | [**protect**](docs/WebscriptsApi.md#protect) | **POST** /registry/v2/webscripts/{name}/versions/{version}/protect | Protect Version
*WebscriptsApi* | [**publish**](docs/WebscriptsApi.md#publish) | **POST** /registry/v2/webscripts/{name}/versions/{version}/publish | Publish Draft
*WebscriptsApi* | [**rebuild**](docs/WebscriptsApi.md#rebuild) | **POST** /registry/v2/webscripts/{name}/versions/{version}/rebuild | Rebuild
*WebscriptsApi* | [**remove_version**](docs/WebscriptsApi.md#remove_version) | **DELETE** /registry/v2/webscripts/{name}/versions/{version} | Remove Version
*WebscriptsApi* | [**remove_versions**](docs/WebscriptsApi.md#remove_versions) | **DELETE** /registry/v2/webscripts/{name} | Remove
*WebscriptsApi* | [**update_asset_by_role**](docs/WebscriptsApi.md#update_asset_by_role) | **PUT** /registry/v2/webscripts/{name}/versions/{version}/{assetRole} | Update Asset By Role
*WebscriptsApi* | [**update_asset**](docs/WebscriptsApi.md#update_asset) | **PUT** /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard} | Update Asset
*WebscriptsApi* | [**update_assets**](docs/WebscriptsApi.md#update_assets) | **PUT** /registry/v2/webscripts/{name}/versions/{version}/content | Update Assets
*WebscriptsApi* | [**verify**](docs/WebscriptsApi.md#verify) | **POST** /registry/v2/webscripts/{name}/versions/{version}/verify | Verify Health


## Documentation For Models

 - [ActiveEventData](docs/ActiveEventData.md)
 - [ActiveEventSSE](docs/ActiveEventSSE.md)
 - [ActiveEventSSEEvent](docs/ActiveEventSSEEvent.md)
 - [AltEmbeddedVersionIKfservingResponseV2](docs/AltEmbeddedVersionIKfservingResponseV2.md)
 - [AltEmbeddedVersionIPlugResponseV2](docs/AltEmbeddedVersionIPlugResponseV2.md)
 - [AltEmbeddedVersionIWebscriptResponseWithInvokeLinkV2](docs/AltEmbeddedVersionIWebscriptResponseWithInvokeLinkV2.md)
 - [AltVersionHALLink](docs/AltVersionHALLink.md)
 - [AltVersionHALLinkDraft](docs/AltVersionHALLinkDraft.md)
 - [AltVersionHALLinkPublished](docs/AltVersionHALLinkPublished.md)
 - [AnyJobForFunction](docs/AnyJobForFunction.md)
 - [AnyJobResult](docs/AnyJobResult.md)
 - [AnyJobStatus](docs/AnyJobStatus.md)
 - [AnyJobStatusSummary](docs/AnyJobStatusSummary.md)
 - [ArchiveFormat](docs/ArchiveFormat.md)
 - [ArchiveFormatExclude](docs/ArchiveFormatExclude.md)
 - [ArchiveFormatFilter](docs/ArchiveFormatFilter.md)
 - [AssetCondition](docs/AssetCondition.md)
 - [AssetConditionContentType](docs/AssetConditionContentType.md)
 - [AssetConditionPattern](docs/AssetConditionPattern.md)
 - [AssetRole](docs/AssetRole.md)
 - [AssetSummaryWithHALLink](docs/AssetSummaryWithHALLink.md)
 - [AssetSummaryWithHALLinkLinks](docs/AssetSummaryWithHALLinkLinks.md)
 - [AssetsConditions](docs/AssetsConditions.md)
 - [Batch](docs/Batch.md)
 - [BatchArgs](docs/BatchArgs.md)
 - [BatchJobStatus](docs/BatchJobStatus.md)
 - [BatchJobStatusType](docs/BatchJobStatusType.md)
 - [BatchResult](docs/BatchResult.md)
 - [Build](docs/Build.md)
 - [Build1](docs/Build1.md)
 - [BuildArgs](docs/BuildArgs.md)
 - [BuildJobStatus](docs/BuildJobStatus.md)
 - [BuildResult](docs/BuildResult.md)
 - [BuildSpec](docs/BuildSpec.md)
 - [BuildType](docs/BuildType.md)
 - [CleanupResult](docs/CleanupResult.md)
 - [CompiledRuntimeVersion](docs/CompiledRuntimeVersion.md)
 - [CompletedEventData](docs/CompletedEventData.md)
 - [CompletedEventSSE](docs/CompletedEventSSE.md)
 - [CompletedEventSSEEvent](docs/CompletedEventSSEEvent.md)
 - [ContentValidationListing](docs/ContentValidationListing.md)
 - [CreateModelsCopyParameter](docs/CreateModelsCopyParameter.md)
 - [DelayedEventData](docs/DelayedEventData.md)
 - [DelayedEventSSE](docs/DelayedEventSSE.md)
 - [DelayedEventSSEEvent](docs/DelayedEventSSEEvent.md)
 - [Deploy](docs/Deploy.md)
 - [Deploy1](docs/Deploy1.md)
 - [DeployArgs](docs/DeployArgs.md)
 - [DeployArgsDeploySpecOverrides](docs/DeployArgsDeploySpecOverrides.md)
 - [DeployJobStatus](docs/DeployJobStatus.md)
 - [DeployResult](docs/DeployResult.md)
 - [DeploySpec](docs/DeploySpec.md)
 - [DeploySpecOpenfaasSpec](docs/DeploySpecOpenfaasSpec.md)
 - [DeployType](docs/DeployType.md)
 - [DeprecatePreviousPolicy](docs/DeprecatePreviousPolicy.md)
 - [DeprecatePreviousPolicyAnyOf](docs/DeprecatePreviousPolicyAnyOf.md)
 - [DeprecatePreviousPolicyAnyOf1](docs/DeprecatePreviousPolicyAnyOf1.md)
 - [DeprecatePreviousPolicyAnyOf2](docs/DeprecatePreviousPolicyAnyOf2.md)
 - [DeprecatePreviousPolicyAnyOf3](docs/DeprecatePreviousPolicyAnyOf3.md)
 - [Documentation](docs/Documentation.md)
 - [DocumentationExample](docs/DocumentationExample.md)
 - [DocumentationProperty](docs/DocumentationProperty.md)
 - [EntityWithLinksIKfservingResponseV2](docs/EntityWithLinksIKfservingResponseV2.md)
 - [EntityWithLinksIPlugResponseV2](docs/EntityWithLinksIPlugResponseV2.md)
 - [EntityWithLinksIWebscriptResponseWithInvokeLinkV2](docs/EntityWithLinksIWebscriptResponseWithInvokeLinkV2.md)
 - [ErrorAndStatusResponse](docs/ErrorAndStatusResponse.md)
 - [EventAck](docs/EventAck.md)
 - [EventClose](docs/EventClose.md)
 - [EventKeepAlive](docs/EventKeepAlive.md)
 - [EventWithCloseSSE](docs/EventWithCloseSSE.md)
 - [ExampleReference](docs/ExampleReference.md)
 - [ExposedOpenfaasDeploySpec](docs/ExposedOpenfaasDeploySpec.md)
 - [FailedEventData](docs/FailedEventData.md)
 - [FailedEventSSE](docs/FailedEventSSE.md)
 - [FailedEventSSEEvent](docs/FailedEventSSEEvent.md)
 - [FailureReason](docs/FailureReason.md)
 - [FileUpload](docs/FileUpload.md)
 - [FunctionDeployOverridesType](docs/FunctionDeployOverridesType.md)
 - [FunctionMeta](docs/FunctionMeta.md)
 - [FunctionRef](docs/FunctionRef.md)
 - [FunctionTagResponse](docs/FunctionTagResponse.md)
 - [FunctionTagsResponse](docs/FunctionTagsResponse.md)
 - [FunctionType](docs/FunctionType.md)
 - [FunctionTypeExclude](docs/FunctionTypeExclude.md)
 - [FunctionTypeFilter](docs/FunctionTypeFilter.md)
 - [GetAssetByRoleModelsAssetRoleParameter](docs/GetAssetByRoleModelsAssetRoleParameter.md)
 - [GetAssetByRoleModelsAssetRoleParameterAnyOf](docs/GetAssetByRoleModelsAssetRoleParameterAnyOf.md)
 - [GetAssetByRoleModelsAssetRoleParameterAnyOf1](docs/GetAssetByRoleModelsAssetRoleParameterAnyOf1.md)
 - [GetAssetByRoleModelsAssetRoleParameterAnyOf2](docs/GetAssetByRoleModelsAssetRoleParameterAnyOf2.md)
 - [GetModelResponseV2](docs/GetModelResponseV2.md)
 - [GetPlugResponseV2](docs/GetPlugResponseV2.md)
 - [GetPlugResponseV2Embedded](docs/GetPlugResponseV2Embedded.md)
 - [GetPlugResponseV2Links](docs/GetPlugResponseV2Links.md)
 - [GetWebscriptResponseV2](docs/GetWebscriptResponseV2.md)
 - [GetWebscriptResponseV2Links](docs/GetWebscriptResponseV2Links.md)
 - [HALLink](docs/HALLink.md)
 - [HALLinkHref](docs/HALLinkHref.md)
 - [HALLinks](docs/HALLinks.md)
 - [InvocationAttributes](docs/InvocationAttributes.md)
 - [InvocationAttributesAuth](docs/InvocationAttributesAuth.md)
 - [InvokeHALLink](docs/InvokeHALLink.md)
 - [JobAndFunctionHALLink](docs/JobAndFunctionHALLink.md)
 - [JobCause](docs/JobCause.md)
 - [JobCauses](docs/JobCauses.md)
 - [JobEventResponseActiveEventData](docs/JobEventResponseActiveEventData.md)
 - [JobEventResponseCompletedEventData](docs/JobEventResponseCompletedEventData.md)
 - [JobEventResponseDelayedEventData](docs/JobEventResponseDelayedEventData.md)
 - [JobEventResponseFailedEventData](docs/JobEventResponseFailedEventData.md)
 - [JobEventResponseWaitingChildrenEventData](docs/JobEventResponseWaitingChildrenEventData.md)
 - [JobEventResponseWaitingEventData](docs/JobEventResponseWaitingEventData.md)
 - [JobEventSSE](docs/JobEventSSE.md)
 - [JobEventsAndFunctionHALLink](docs/JobEventsAndFunctionHALLink.md)
 - [JobEventsHALLink](docs/JobEventsHALLink.md)
 - [JobHALLink](docs/JobHALLink.md)
 - [JobHALLinks](docs/JobHALLinks.md)
 - [JobHALLinksJob](docs/JobHALLinksJob.md)
 - [JobReference](docs/JobReference.md)
 - [JobResponse](docs/JobResponse.md)
 - [JobState](docs/JobState.md)
 - [JobStateActive](docs/JobStateActive.md)
 - [JobStateCompleted](docs/JobStateCompleted.md)
 - [JobStateDelayed](docs/JobStateDelayed.md)
 - [JobStateFailed](docs/JobStateFailed.md)
 - [JobStateFinished](docs/JobStateFinished.md)
 - [JobStatePrioritized](docs/JobStatePrioritized.md)
 - [JobStateResult](docs/JobStateResult.md)
 - [JobStateUnknown](docs/JobStateUnknown.md)
 - [JobStateWaiting](docs/JobStateWaiting.md)
 - [JobStateWaitingChildren](docs/JobStateWaitingChildren.md)
 - [JobStatus](docs/JobStatus.md)
 - [JobStatusAndEntityHALLinks](docs/JobStatusAndEntityHALLinks.md)
 - [JobStatusHALLink](docs/JobStatusHALLink.md)
 - [JobStatusProgress](docs/JobStatusProgress.md)
 - [JobType](docs/JobType.md)
 - [JobTypeBatch](docs/JobTypeBatch.md)
 - [JobTypeBuild](docs/JobTypeBuild.md)
 - [JobTypeDeploy](docs/JobTypeDeploy.md)
 - [JobTypeNotify](docs/JobTypeNotify.md)
 - [JobTypeScale](docs/JobTypeScale.md)
 - [JobTypeSchema](docs/JobTypeSchema.md)
 - [JobTypeUndeploy](docs/JobTypeUndeploy.md)
 - [JobTypeVerify](docs/JobTypeVerify.md)
 - [JobsForModelResponseV2](docs/JobsForModelResponseV2.md)
 - [JobsForModelResponseV2Links](docs/JobsForModelResponseV2Links.md)
 - [JobsForPlugResponseV2](docs/JobsForPlugResponseV2.md)
 - [JobsForPlugResponseV2Links](docs/JobsForPlugResponseV2Links.md)
 - [JobsForWebscriptResponseV2](docs/JobsForWebscriptResponseV2.md)
 - [JobsForWebscriptResponseV2Links](docs/JobsForWebscriptResponseV2Links.md)
 - [JobsResponse](docs/JobsResponse.md)
 - [KFServingManifest](docs/KFServingManifest.md)
 - [KFServingManifestPatch](docs/KFServingManifestPatch.md)
 - [KeepAliveEventSSE](docs/KeepAliveEventSSE.md)
 - [KfservingResponseV2](docs/KfservingResponseV2.md)
 - [LanguageRelease](docs/LanguageRelease.md)
 - [LatestModelsResponseV2](docs/LatestModelsResponseV2.md)
 - [LatestPlugsResponseV2](docs/LatestPlugsResponseV2.md)
 - [LatestVersionLevel](docs/LatestVersionLevel.md)
 - [LatestWebscriptsResponseV2](docs/LatestWebscriptsResponseV2.md)
 - [ListRuntimesTagsParameter](docs/ListRuntimesTagsParameter.md)
 - [Model](docs/Model.md)
 - [Model1](docs/Model1.md)
 - [Model2](docs/Model2.md)
 - [ModelVersionsResponseV2](docs/ModelVersionsResponseV2.md)
 - [NotifyResult](docs/NotifyResult.md)
 - [ParentKeys](docs/ParentKeys.md)
 - [Plug](docs/Plug.md)
 - [Plug1](docs/Plug1.md)
 - [Plug2](docs/Plug2.md)
 - [PlugInterface](docs/PlugInterface.md)
 - [PlugManifest](docs/PlugManifest.md)
 - [PlugManifestPatch](docs/PlugManifestPatch.md)
 - [PlugMeta](docs/PlugMeta.md)
 - [PlugProperty](docs/PlugProperty.md)
 - [PlugPropertyDataType](docs/PlugPropertyDataType.md)
 - [PlugPropertyFormat](docs/PlugPropertyFormat.md)
 - [PlugPropertyFormatType](docs/PlugPropertyFormatType.md)
 - [PlugResponseV2](docs/PlugResponseV2.md)
 - [PlugType](docs/PlugType.md)
 - [PlugVersionsResponseV2](docs/PlugVersionsResponseV2.md)
 - [PlugWithInvocationResponseV2](docs/PlugWithInvocationResponseV2.md)
 - [PostModelJobAsyncResponseV2](docs/PostModelJobAsyncResponseV2.md)
 - [PostModelJobSyncResponseV2](docs/PostModelJobSyncResponseV2.md)
 - [PostPlugJobAsyncResponseV2](docs/PostPlugJobAsyncResponseV2.md)
 - [PostPlugJobSyncResponseV2](docs/PostPlugJobSyncResponseV2.md)
 - [PostWebscriptJobAsyncResponseV2](docs/PostWebscriptJobAsyncResponseV2.md)
 - [PostWebscriptJobSyncResponseV2](docs/PostWebscriptJobSyncResponseV2.md)
 - [ProtectByNameResponseV2](docs/ProtectByNameResponseV2.md)
 - [ProvidedDependency](docs/ProvidedDependency.md)
 - [QueueEvents](docs/QueueEvents.md)
 - [RebuildModelAsyncResponseV2](docs/RebuildModelAsyncResponseV2.md)
 - [RebuildModelSyncResponseV2](docs/RebuildModelSyncResponseV2.md)
 - [RebuildPlugAsyncResponseV2](docs/RebuildPlugAsyncResponseV2.md)
 - [RebuildPlugSyncResponseV2](docs/RebuildPlugSyncResponseV2.md)
 - [RebuildPolicy](docs/RebuildPolicy.md)
 - [RebuildRequestV2](docs/RebuildRequestV2.md)
 - [RebuildWebscriptAsyncResponseV2](docs/RebuildWebscriptAsyncResponseV2.md)
 - [RebuildWebscriptSyncResponseV2](docs/RebuildWebscriptSyncResponseV2.md)
 - [RegistryErrorResponse](docs/RegistryErrorResponse.md)
 - [RequestOperation](docs/RequestOperation.md)
 - [ResourceLimits](docs/ResourceLimits.md)
 - [RootPageResponse](docs/RootPageResponse.md)
 - [RuntimeAttributes](docs/RuntimeAttributes.md)
 - [RuntimeSummary](docs/RuntimeSummary.md)
 - [RuntimeSummaryResponse](docs/RuntimeSummaryResponse.md)
 - [RuntimeSummaryResponseEmbedded](docs/RuntimeSummaryResponseEmbedded.md)
 - [RuntimeTag](docs/RuntimeTag.md)
 - [RuntimeTagFilter](docs/RuntimeTagFilter.md)
 - [RuntimeTagResponse](docs/RuntimeTagResponse.md)
 - [RuntimeTagsResponse](docs/RuntimeTagsResponse.md)
 - [RuntimeVersionInfo](docs/RuntimeVersionInfo.md)
 - [RuntimeVersionResponse](docs/RuntimeVersionResponse.md)
 - [Scale](docs/Scale.md)
 - [Scale1](docs/Scale1.md)
 - [ScaleArgs](docs/ScaleArgs.md)
 - [ScaleJobStatus](docs/ScaleJobStatus.md)
 - [ScaleType](docs/ScaleType.md)
 - [SemanticVersionRange](docs/SemanticVersionRange.md)
 - [ShowEmbedding](docs/ShowEmbedding.md)
 - [ShowInlineOrEmbedding](docs/ShowInlineOrEmbedding.md)
 - [ShowInlineOrEmbeddingAnyOf](docs/ShowInlineOrEmbeddingAnyOf.md)
 - [ShowLinkOrEmbedding](docs/ShowLinkOrEmbedding.md)
 - [ShowLinkOrEmbeddingAnyOf](docs/ShowLinkOrEmbeddingAnyOf.md)
 - [Status](docs/Status.md)
 - [StatusAny](docs/StatusAny.md)
 - [StatusExclude](docs/StatusExclude.md)
 - [StatusFilter](docs/StatusFilter.md)
 - [StreamClosing](docs/StreamClosing.md)
 - [StreamReady](docs/StreamReady.md)
 - [Tag](docs/Tag.md)
 - [TagOrTagReference](docs/TagOrTagReference.md)
 - [TaggingScopeOption](docs/TaggingScopeOption.md)
 - [TagsFilter](docs/TagsFilter.md)
 - [TimestampAbsolute](docs/TimestampAbsolute.md)
 - [TimestampAge](docs/TimestampAge.md)
 - [TimestampSpec](docs/TimestampSpec.md)
 - [Undeploy](docs/Undeploy.md)
 - [Undeploy1](docs/Undeploy1.md)
 - [UndeployArgs](docs/UndeployArgs.md)
 - [UndeployJobStatus](docs/UndeployJobStatus.md)
 - [UndeployResult](docs/UndeployResult.md)
 - [UndeploySubmittedResponseV2](docs/UndeploySubmittedResponseV2.md)
 - [UndeployType](docs/UndeployType.md)
 - [UndeployedResponseV2](docs/UndeployedResponseV2.md)
 - [UpdateMetadataRequestV2](docs/UpdateMetadataRequestV2.md)
 - [UpdatePlugMetadataRequestV2](docs/UpdatePlugMetadataRequestV2.md)
 - [UpdateRecord](docs/UpdateRecord.md)
 - [UpdateTagsRequestV2](docs/UpdateTagsRequestV2.md)
 - [Verify](docs/Verify.md)
 - [Verify1](docs/Verify1.md)
 - [VerifyArgs](docs/VerifyArgs.md)
 - [VerifyJobStatus](docs/VerifyJobStatus.md)
 - [VerifyModelSyncResponseV2](docs/VerifyModelSyncResponseV2.md)
 - [VerifyPlugSyncResponseV2](docs/VerifyPlugSyncResponseV2.md)
 - [VerifyResult](docs/VerifyResult.md)
 - [VerifyType](docs/VerifyType.md)
 - [VerifyWebscriptSyncResponseV2](docs/VerifyWebscriptSyncResponseV2.md)
 - [WaitingChildrenEventSSE](docs/WaitingChildrenEventSSE.md)
 - [WaitingChildrenEventSSEEvent](docs/WaitingChildrenEventSSEEvent.md)
 - [WaitingEventData](docs/WaitingEventData.md)
 - [WaitingEventSSE](docs/WaitingEventSSE.md)
 - [WaitingEventSSEEvent](docs/WaitingEventSSEEvent.md)
 - [Webscript](docs/Webscript.md)
 - [Webscript1](docs/Webscript1.md)
 - [Webscript2](docs/Webscript2.md)
 - [WebscriptManifest](docs/WebscriptManifest.md)
 - [WebscriptManifestPatch](docs/WebscriptManifestPatch.md)
 - [WebscriptResponseV2](docs/WebscriptResponseV2.md)
 - [WebscriptResponseWithInvokeLinkV2](docs/WebscriptResponseWithInvokeLinkV2.md)
 - [WebscriptVersionsResponseV2](docs/WebscriptVersionsResponseV2.md)

