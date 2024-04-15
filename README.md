# Waylay Registry Service
V2 API to build and deploy Waylay functions (plugs, webscripts, BYOML models).

This Python package is automatically generated based on the 
Waylay Registry OpenAPI specification (API version: 2.13.0)
For more information, please visit [the openapi specification](https://docs.waylay.io/openapi/public/redocly/registry.html).

It consists of two sub-packages that are both plugins for the waylay-sdk-core package.
- The `waylay-sdk-registry` sub-package contains the Registry api methods.
- The `waylay-sdk-registry-types` sub-package is an extension that contains the typed model classes for all path params, query params, body params and responses for each of the api methods in `waylay-sdk-registry`.

## Requirements.
This package requires Python 3.9+.

## Installation
Typically this package is installed when installing the [waylay-sdk-core](https://pypi.org/project/waylay-sdk/) package to enable the service's functionality.
When the service api methods are required, waylay-sdk-registry is included in:
- ```pip install waylay-sdk-core[registry]``` to install `waylay-sdk-core` along with only this service, or
- ```pip install waylay-sdk-core[services]``` to install `waylay-sdk-core` along with all services.
When the typed models are required, both waylay-sdk-registry and waylay-sdk-registry-types are included in:
- ```pip install waylay-sdk-core[registry,registry-types]``` to install `waylay-sdk-core` along with only this service including the typed models, or
- ```pip install waylay-sdk-core[services,services-types]``` to install `waylay-sdk-core` along with all services along with the typed models.

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

All URIs are relative to *https://api-aws-dev.waylay.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AboutApi* | [**get**](docs/AboutApi.md#get) | **GET** /registry/v2/ | Get Service Status
*JobsApi* | [**events**](docs/JobsApi.md#events) | **GET** /registry/v2/jobs/events | Stream Events
*JobsApi* | [**get**](docs/JobsApi.md#get) | **GET** /registry/v2/jobs/{type}/{id} | Get Job
*JobsApi* | [**list**](docs/JobsApi.md#list) | **GET** /registry/v2/jobs/ | List Jobs
*ModelsApi* | [**create**](docs/ModelsApi.md#create) | **POST** /registry/v2/models/ | Create Model
*ModelsApi* | [**delete_asset**](docs/ModelsApi.md#delete_asset) | **DELETE** /registry/v2/models/{name}/versions/{version}/content/{wildcard} | Delete Model Asset
*ModelsApi* | [**get_archive**](docs/ModelsApi.md#get_archive) | **GET** /registry/v2/models/{name}/versions/{version}/content | Get Model Archive
*ModelsApi* | [**get_asset**](docs/ModelsApi.md#get_asset) | **GET** /registry/v2/models/{name}/versions/{version}/content/{wildcard} | Get File From Model Archive
*ModelsApi* | [**get_latest**](docs/ModelsApi.md#get_latest) | **GET** /registry/v2/models/{name} | Get Latest Model Version
*ModelsApi* | [**get**](docs/ModelsApi.md#get) | **GET** /registry/v2/models/{name}/versions/{version} | Get Model Version
*ModelsApi* | [**jobs**](docs/ModelsApi.md#jobs) | **GET** /registry/v2/models/{name}/versions/{version}/jobs | List Model Jobs
*ModelsApi* | [**list**](docs/ModelsApi.md#list) | **GET** /registry/v2/models/ | List Models
*ModelsApi* | [**list_versions**](docs/ModelsApi.md#list_versions) | **GET** /registry/v2/models/{name}/versions | List Model Versions
*ModelsApi* | [**patch_metadata**](docs/ModelsApi.md#patch_metadata) | **PATCH** /registry/v2/models/{name}/versions/{version}/metadata | Patch Model Metadata
*ModelsApi* | [**publish**](docs/ModelsApi.md#publish) | **POST** /registry/v2/models/{name}/versions/{version}/publish | Publish Draft Model
*ModelsApi* | [**rebuild**](docs/ModelsApi.md#rebuild) | **POST** /registry/v2/models/{name}/versions/{version}/rebuild | Rebuild Model
*ModelsApi* | [**remove_version**](docs/ModelsApi.md#remove_version) | **DELETE** /registry/v2/models/{name}/versions/{version} | Remove Model Version
*ModelsApi* | [**remove_versions**](docs/ModelsApi.md#remove_versions) | **DELETE** /registry/v2/models/{name} | Remove Model
*ModelsApi* | [**update_asset**](docs/ModelsApi.md#update_asset) | **PUT** /registry/v2/models/{name}/versions/{version}/content/{wildcard} | Update Model Asset
*ModelsApi* | [**update_assets**](docs/ModelsApi.md#update_assets) | **PUT** /registry/v2/models/{name}/versions/{version}/content | Update Model Assets
*ModelsApi* | [**verify**](docs/ModelsApi.md#verify) | **POST** /registry/v2/models/{name}/versions/{version}/verify | Verify Health Of Model
*PlugsApi* | [**create**](docs/PlugsApi.md#create) | **POST** /registry/v2/plugs/ | Create Plug
*PlugsApi* | [**delete_asset**](docs/PlugsApi.md#delete_asset) | **DELETE** /registry/v2/plugs/{name}/versions/{version}/content/{wildcard} | Delete Plug Asset
*PlugsApi* | [**get_archive**](docs/PlugsApi.md#get_archive) | **GET** /registry/v2/plugs/{name}/versions/{version}/content | Get Plug Archive
*PlugsApi* | [**get_asset**](docs/PlugsApi.md#get_asset) | **GET** /registry/v2/plugs/{name}/versions/{version}/content/{wildcard} | Get File From Plug Archive
*PlugsApi* | [**get_latest**](docs/PlugsApi.md#get_latest) | **GET** /registry/v2/plugs/{name} | Get Latest Plug Version
*PlugsApi* | [**get**](docs/PlugsApi.md#get) | **GET** /registry/v2/plugs/{name}/versions/{version} | Get Plug Version
*PlugsApi* | [**jobs**](docs/PlugsApi.md#jobs) | **GET** /registry/v2/plugs/{name}/versions/{version}/jobs | List Plug Jobs
*PlugsApi* | [**list**](docs/PlugsApi.md#list) | **GET** /registry/v2/plugs/ | List Plugs
*PlugsApi* | [**list_versions**](docs/PlugsApi.md#list_versions) | **GET** /registry/v2/plugs/{name}/versions | List Plug Versions
*PlugsApi* | [**patch_interface**](docs/PlugsApi.md#patch_interface) | **PATCH** /registry/v2/plugs/{name}/versions/{version}/interface | Patch Plug Interface
*PlugsApi* | [**patch_metadata**](docs/PlugsApi.md#patch_metadata) | **PATCH** /registry/v2/plugs/{name}/versions/{version}/metadata | Patch Plug Metadata
*PlugsApi* | [**publish**](docs/PlugsApi.md#publish) | **POST** /registry/v2/plugs/{name}/versions/{version}/publish | Publish Draft Plug
*PlugsApi* | [**rebuild**](docs/PlugsApi.md#rebuild) | **POST** /registry/v2/plugs/{name}/versions/{version}/rebuild | Rebuild Plug
*PlugsApi* | [**remove_version**](docs/PlugsApi.md#remove_version) | **DELETE** /registry/v2/plugs/{name}/versions/{version} | Remove Plug Version
*PlugsApi* | [**remove_versions**](docs/PlugsApi.md#remove_versions) | **DELETE** /registry/v2/plugs/{name} | Remove Plug
*PlugsApi* | [**update_asset**](docs/PlugsApi.md#update_asset) | **PUT** /registry/v2/plugs/{name}/versions/{version}/content/{wildcard} | Update Plug Asset
*PlugsApi* | [**update_assets**](docs/PlugsApi.md#update_assets) | **PUT** /registry/v2/plugs/{name}/versions/{version}/content | Update Plug Assets
*PlugsApi* | [**verify**](docs/PlugsApi.md#verify) | **POST** /registry/v2/plugs/{name}/versions/{version}/verify | Verify Health Of Plug
*RuntimesApi* | [**example_archive**](docs/RuntimesApi.md#example_archive) | **GET** /registry/v2/runtimes/{name}/versions/{version}/example | Get Runtime Example Archive
*RuntimesApi* | [**get_example_asset**](docs/RuntimesApi.md#get_example_asset) | **GET** /registry/v2/runtimes/{name}/versions/{version}/example/{wildcard} | Get File From Runtime Example Archive
*RuntimesApi* | [**get_latest**](docs/RuntimesApi.md#get_latest) | **GET** /registry/v2/runtimes/{name} | Get Latest Runtime Version
*RuntimesApi* | [**get**](docs/RuntimesApi.md#get) | **GET** /registry/v2/runtimes/{name}/versions/{version} | Get Runtime Version
*RuntimesApi* | [**list**](docs/RuntimesApi.md#list) | **GET** /registry/v2/runtimes/ | List Runtimes
*RuntimesApi* | [**list_versions**](docs/RuntimesApi.md#list_versions) | **GET** /registry/v2/runtimes/{name}/versions | List Runtime Versions
*SchemasApi* | [**get_by_role**](docs/SchemasApi.md#get_by_role) | **GET** /registry/v2/schemas/{functionType}/{role}/schema | Get Asset Schema
*SchemasApi* | [**get**](docs/SchemasApi.md#get) | **GET** /registry/v2/schemas/{schemaId} | Get Asset Schema
*WebscriptsApi* | [**create**](docs/WebscriptsApi.md#create) | **POST** /registry/v2/webscripts/ | Create Webscript Version
*WebscriptsApi* | [**delete_asset**](docs/WebscriptsApi.md#delete_asset) | **DELETE** /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard} | Delete Webscript Asset
*WebscriptsApi* | [**get_archive**](docs/WebscriptsApi.md#get_archive) | **GET** /registry/v2/webscripts/{name}/versions/{version}/content | Get Webscript Archive
*WebscriptsApi* | [**get_asset**](docs/WebscriptsApi.md#get_asset) | **GET** /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard} | Get File From Webscript Archive
*WebscriptsApi* | [**get_latest**](docs/WebscriptsApi.md#get_latest) | **GET** /registry/v2/webscripts/{name} | Get Latest Webscript Version
*WebscriptsApi* | [**get**](docs/WebscriptsApi.md#get) | **GET** /registry/v2/webscripts/{name}/versions/{version} | Get Webscript Version
*WebscriptsApi* | [**jobs**](docs/WebscriptsApi.md#jobs) | **GET** /registry/v2/webscripts/{name}/versions/{version}/jobs | List Webscript Jobs
*WebscriptsApi* | [**list_versions**](docs/WebscriptsApi.md#list_versions) | **GET** /registry/v2/webscripts/{name}/versions | List Webscript Versions
*WebscriptsApi* | [**list**](docs/WebscriptsApi.md#list) | **GET** /registry/v2/webscripts/ | List Webscripts
*WebscriptsApi* | [**patch_metadata**](docs/WebscriptsApi.md#patch_metadata) | **PATCH** /registry/v2/webscripts/{name}/versions/{version}/metadata | Patch Webscript Metadata
*WebscriptsApi* | [**publish**](docs/WebscriptsApi.md#publish) | **POST** /registry/v2/webscripts/{name}/versions/{version}/publish | Publish Draft Webscript
*WebscriptsApi* | [**rebuild**](docs/WebscriptsApi.md#rebuild) | **POST** /registry/v2/webscripts/{name}/versions/{version}/rebuild | Rebuild Webscript
*WebscriptsApi* | [**remove_version**](docs/WebscriptsApi.md#remove_version) | **DELETE** /registry/v2/webscripts/{name}/versions/{version} | Remove Webscript Version
*WebscriptsApi* | [**remove_versions**](docs/WebscriptsApi.md#remove_versions) | **DELETE** /registry/v2/webscripts/{name} | Remove Webscript
*WebscriptsApi* | [**update_asset**](docs/WebscriptsApi.md#update_asset) | **PUT** /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard} | Update Webscript Asset
*WebscriptsApi* | [**update_assets**](docs/WebscriptsApi.md#update_assets) | **PUT** /registry/v2/webscripts/{name}/versions/{version}/content | Update Webscript Assets
*WebscriptsApi* | [**verify**](docs/WebscriptsApi.md#verify) | **POST** /registry/v2/webscripts/{name}/versions/{version}/verify | Verify Health Of Webscript


## Documentation For Models

 - [ActiveEventData](docs/ActiveEventData.md)
 - [ActiveEventSSE](docs/ActiveEventSSE.md)
 - [ActiveEventSSEEvent](docs/ActiveEventSSEEvent.md)
 - [AltEmbeddedVersionIKfservingResponseV2](docs/AltEmbeddedVersionIKfservingResponseV2.md)
 - [AltEmbeddedVersionIPlugResponseV2](docs/AltEmbeddedVersionIPlugResponseV2.md)
 - [AltEmbeddedVersionIWebscriptResponseWithInvokeLinkV2](docs/AltEmbeddedVersionIWebscriptResponseWithInvokeLinkV2.md)
 - [AltVersionHALLink](docs/AltVersionHALLink.md)
 - [AnyFunctionResponse](docs/AnyFunctionResponse.md)
 - [AnyJobForFunction](docs/AnyJobForFunction.md)
 - [AnyJobResult](docs/AnyJobResult.md)
 - [AnyJobStatus](docs/AnyJobStatus.md)
 - [AnyJobStatusSummary](docs/AnyJobStatusSummary.md)
 - [ArchiveFormat](docs/ArchiveFormat.md)
 - [AssetCondition](docs/AssetCondition.md)
 - [AssetConditionContentType](docs/AssetConditionContentType.md)
 - [AssetConditionPattern](docs/AssetConditionPattern.md)
 - [AssetPathParamsV2](docs/AssetPathParamsV2.md)
 - [AssetRole](docs/AssetRole.md)
 - [AssetSummary](docs/AssetSummary.md)
 - [AssetSummaryWithHALLink](docs/AssetSummaryWithHALLink.md)
 - [AssetSummaryWithHALLinkLinks](docs/AssetSummaryWithHALLinkLinks.md)
 - [AssetsConditions](docs/AssetsConditions.md)
 - [AsyncDeployQueryV1](docs/AsyncDeployQueryV1.md)
 - [AsyncQueryDefaultFalse](docs/AsyncQueryDefaultFalse.md)
 - [AsyncVerifyQuery](docs/AsyncVerifyQuery.md)
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
 - [ContentQueryV2](docs/ContentQueryV2.md)
 - [ContentValidationListing](docs/ContentValidationListing.md)
 - [CreateFunctionQueryV2](docs/CreateFunctionQueryV2.md)
 - [CreateFunctionQueryV2Copy](docs/CreateFunctionQueryV2Copy.md)
 - [CreateKFServingAsyncResponse](docs/CreateKFServingAsyncResponse.md)
 - [CreatePlugAsyncResponse](docs/CreatePlugAsyncResponse.md)
 - [CreateWebscriptAsyncResponse](docs/CreateWebscriptAsyncResponse.md)
 - [CreateWebscriptsCopyParameter](docs/CreateWebscriptsCopyParameter.md)
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
 - [Documentation](docs/Documentation.md)
 - [DocumentationProperty](docs/DocumentationProperty.md)
 - [EntityResponse](docs/EntityResponse.md)
 - [EntityWithLinksIKfservingResponseV2](docs/EntityWithLinksIKfservingResponseV2.md)
 - [EntityWithLinksIPlugResponseV2](docs/EntityWithLinksIPlugResponseV2.md)
 - [EntityWithLinksIWebscriptResponseWithInvokeLinkV2](docs/EntityWithLinksIWebscriptResponseWithInvokeLinkV2.md)
 - [ErrorAndStatusResponse](docs/ErrorAndStatusResponse.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [EventAck](docs/EventAck.md)
 - [EventClose](docs/EventClose.md)
 - [EventKeepAlive](docs/EventKeepAlive.md)
 - [EventSSE](docs/EventSSE.md)
 - [EventTypeSSE](docs/EventTypeSSE.md)
 - [EventWithCloseSSE](docs/EventWithCloseSSE.md)
 - [ExampleReference](docs/ExampleReference.md)
 - [ExposedOpenfaasDeploySpec](docs/ExposedOpenfaasDeploySpec.md)
 - [FailedEventData](docs/FailedEventData.md)
 - [FailedEventSSE](docs/FailedEventSSE.md)
 - [FailedEventSSEEvent](docs/FailedEventSSEEvent.md)
 - [FailureReason](docs/FailureReason.md)
 - [FileUpload](docs/FileUpload.md)
 - [ForceDeleteQueryV1](docs/ForceDeleteQueryV1.md)
 - [FunctionDeployOverrides](docs/FunctionDeployOverrides.md)
 - [FunctionDeployOverridesType](docs/FunctionDeployOverridesType.md)
 - [FunctionJobArgs](docs/FunctionJobArgs.md)
 - [FunctionManifest](docs/FunctionManifest.md)
 - [FunctionMeta](docs/FunctionMeta.md)
 - [FunctionNameVersion](docs/FunctionNameVersion.md)
 - [FunctionRef](docs/FunctionRef.md)
 - [FunctionSpec](docs/FunctionSpec.md)
 - [FunctionType](docs/FunctionType.md)
 - [GetContentParamsV2](docs/GetContentParamsV2.md)
 - [GetInvokableWebscriptQuery](docs/GetInvokableWebscriptQuery.md)
 - [GetModelResponseV2](docs/GetModelResponseV2.md)
 - [GetPlugResponseV2](docs/GetPlugResponseV2.md)
 - [GetPlugResponseV2Links](docs/GetPlugResponseV2Links.md)
 - [GetPlugResponseV2LinksDraft](docs/GetPlugResponseV2LinksDraft.md)
 - [GetPlugResponseV2LinksPublished](docs/GetPlugResponseV2LinksPublished.md)
 - [GetRuntimeByNameAndVersionQuery](docs/GetRuntimeByNameAndVersionQuery.md)
 - [GetRuntimeByNameQuery](docs/GetRuntimeByNameQuery.md)
 - [GetRuntimeExampleQuery](docs/GetRuntimeExampleQuery.md)
 - [GetRuntimeVersionsQuery](docs/GetRuntimeVersionsQuery.md)
 - [GetWebscriptResponseV2](docs/GetWebscriptResponseV2.md)
 - [GetWebscriptResponseV2Links](docs/GetWebscriptResponseV2Links.md)
 - [HALLink](docs/HALLink.md)
 - [InvokableWebscriptResponse](docs/InvokableWebscriptResponse.md)
 - [InvokableWebscriptResponseEntity](docs/InvokableWebscriptResponseEntity.md)
 - [InvokableWebscriptResponseEntityWebscript](docs/InvokableWebscriptResponseEntityWebscript.md)
 - [InvokeHALLink](docs/InvokeHALLink.md)
 - [InvokeInternalHALLink](docs/InvokeInternalHALLink.md)
 - [JobAndFunctionHALLink](docs/JobAndFunctionHALLink.md)
 - [JobCause](docs/JobCause.md)
 - [JobCauses](docs/JobCauses.md)
 - [JobEventPayloadActiveEventData](docs/JobEventPayloadActiveEventData.md)
 - [JobEventPayloadCompletedEventData](docs/JobEventPayloadCompletedEventData.md)
 - [JobEventPayloadDelayedEventData](docs/JobEventPayloadDelayedEventData.md)
 - [JobEventPayloadFailedEventData](docs/JobEventPayloadFailedEventData.md)
 - [JobEventPayloadWaitingChildrenEventData](docs/JobEventPayloadWaitingChildrenEventData.md)
 - [JobEventPayloadWaitingEventData](docs/JobEventPayloadWaitingEventData.md)
 - [JobEventResponseActiveEventData](docs/JobEventResponseActiveEventData.md)
 - [JobEventResponseCompletedEventData](docs/JobEventResponseCompletedEventData.md)
 - [JobEventResponseDelayedEventData](docs/JobEventResponseDelayedEventData.md)
 - [JobEventResponseFailedEventData](docs/JobEventResponseFailedEventData.md)
 - [JobEventResponseWaitingChildrenEventData](docs/JobEventResponseWaitingChildrenEventData.md)
 - [JobEventResponseWaitingEventData](docs/JobEventResponseWaitingEventData.md)
 - [JobEventSSE](docs/JobEventSSE.md)
 - [JobEventsAndFunctionHALLink](docs/JobEventsAndFunctionHALLink.md)
 - [JobEventsFilterQuery](docs/JobEventsFilterQuery.md)
 - [JobEventsHALLink](docs/JobEventsHALLink.md)
 - [JobHALLinks](docs/JobHALLinks.md)
 - [JobQuery](docs/JobQuery.md)
 - [JobReference](docs/JobReference.md)
 - [JobReferenceParams](docs/JobReferenceParams.md)
 - [JobResponse](docs/JobResponse.md)
 - [JobState](docs/JobState.md)
 - [JobStateActive](docs/JobStateActive.md)
 - [JobStateCompleted](docs/JobStateCompleted.md)
 - [JobStateDelayed](docs/JobStateDelayed.md)
 - [JobStateFailed](docs/JobStateFailed.md)
 - [JobStateFinished](docs/JobStateFinished.md)
 - [JobStateResult](docs/JobStateResult.md)
 - [JobStateUnknown](docs/JobStateUnknown.md)
 - [JobStateWaiting](docs/JobStateWaiting.md)
 - [JobStateWaitingChildren](docs/JobStateWaitingChildren.md)
 - [JobStatus](docs/JobStatus.md)
 - [JobStatusAndEntityHALLinks](docs/JobStatusAndEntityHALLinks.md)
 - [JobStatusHALLink](docs/JobStatusHALLink.md)
 - [JobStatusProgress](docs/JobStatusProgress.md)
 - [JobSubmittedResponse](docs/JobSubmittedResponse.md)
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
 - [JobsHALLink](docs/JobsHALLink.md)
 - [JobsResponse](docs/JobsResponse.md)
 - [KFServingDeleteMultipleResponse](docs/KFServingDeleteMultipleResponse.md)
 - [KFServingDeleteMultipleWithJobResponse](docs/KFServingDeleteMultipleWithJobResponse.md)
 - [KFServingDeleteQueryV1](docs/KFServingDeleteQueryV1.md)
 - [KFServingDeleteQueryV2](docs/KFServingDeleteQueryV2.md)
 - [KFServingDeleteResponse](docs/KFServingDeleteResponse.md)
 - [KFServingDeleteWithJobResponse](docs/KFServingDeleteWithJobResponse.md)
 - [KFServingLatestVersionQueryV2](docs/KFServingLatestVersionQueryV2.md)
 - [KFServingLatestVersionsQueryV1](docs/KFServingLatestVersionsQueryV1.md)
 - [KFServingLatestVersionsQueryV2](docs/KFServingLatestVersionsQueryV2.md)
 - [KFServingManifest](docs/KFServingManifest.md)
 - [KFServingModelsResponse](docs/KFServingModelsResponse.md)
 - [KFServingResponse](docs/KFServingResponse.md)
 - [KFServingVersionsQueryV1](docs/KFServingVersionsQueryV1.md)
 - [KeepAliveEventSSE](docs/KeepAliveEventSSE.md)
 - [KfservingResponseV2](docs/KfservingResponseV2.md)
 - [LanguageRelease](docs/LanguageRelease.md)
 - [LatestFunctionVersionsQuery](docs/LatestFunctionVersionsQuery.md)
 - [LatestFunctionVersionsQueryShowRelated](docs/LatestFunctionVersionsQueryShowRelated.md)
 - [LatestFunctionsQuery](docs/LatestFunctionsQuery.md)
 - [LatestModelsResponseV2](docs/LatestModelsResponseV2.md)
 - [LatestPlugQuery](docs/LatestPlugQuery.md)
 - [LatestPlugVersionQueryV2](docs/LatestPlugVersionQueryV2.md)
 - [LatestPlugVersionsQuery](docs/LatestPlugVersionsQuery.md)
 - [LatestPlugVersionsQueryV2](docs/LatestPlugVersionsQueryV2.md)
 - [LatestPlugsQuery](docs/LatestPlugsQuery.md)
 - [LatestPlugsResponseV2](docs/LatestPlugsResponseV2.md)
 - [LatestVersionLevel](docs/LatestVersionLevel.md)
 - [LatestWebscriptsResponseV2](docs/LatestWebscriptsResponseV2.md)
 - [LegacyConfigurationObject](docs/LegacyConfigurationObject.md)
 - [LegacyConfigurationObjectFormat](docs/LegacyConfigurationObjectFormat.md)
 - [LegacyConfigurationResponseObject](docs/LegacyConfigurationResponseObject.md)
 - [LegacyCreateDebugResponse](docs/LegacyCreateDebugResponse.md)
 - [LegacyDebugPlugManifest](docs/LegacyDebugPlugManifest.md)
 - [LegacyDebugPlugRequest](docs/LegacyDebugPlugRequest.md)
 - [LegacyDocumentation](docs/LegacyDocumentation.md)
 - [LegacyDocumentationRequest](docs/LegacyDocumentationRequest.md)
 - [LegacyFunctionMeta](docs/LegacyFunctionMeta.md)
 - [LegacyPlugCreateQuery](docs/LegacyPlugCreateQuery.md)
 - [LegacyPlugCreateRequest](docs/LegacyPlugCreateRequest.md)
 - [LegacyPlugCreateResponse](docs/LegacyPlugCreateResponse.md)
 - [LegacyPlugMetaRequest](docs/LegacyPlugMetaRequest.md)
 - [LegacyPlugQuery](docs/LegacyPlugQuery.md)
 - [LegacyPlugRequest](docs/LegacyPlugRequest.md)
 - [LegacyPlugRequestMetadata](docs/LegacyPlugRequestMetadata.md)
 - [LegacyPlugRequestMetadataDocumentation](docs/LegacyPlugRequestMetadataDocumentation.md)
 - [LegacyPlugRequestMetadataDocumentationAnyOf](docs/LegacyPlugRequestMetadataDocumentationAnyOf.md)
 - [LegacyPlugRequestMetadataRawDataInner](docs/LegacyPlugRequestMetadataRawDataInner.md)
 - [LegacyPlugResponse](docs/LegacyPlugResponse.md)
 - [LegacyPlugResponseMetadata](docs/LegacyPlugResponseMetadata.md)
 - [LegacyPlugScriptMeta](docs/LegacyPlugScriptMeta.md)
 - [LegacyPlugScriptMetaRawDataInner](docs/LegacyPlugScriptMetaRawDataInner.md)
 - [LegacyPlugScriptResponse](docs/LegacyPlugScriptResponse.md)
 - [LegacyRequiredPropertiesInner](docs/LegacyRequiredPropertiesInner.md)
 - [LegacyRequiredPropertyObject](docs/LegacyRequiredPropertyObject.md)
 - [MediaType](docs/MediaType.md)
 - [MessageAndStatusResponse](docs/MessageAndStatusResponse.md)
 - [MessageResponse](docs/MessageResponse.md)
 - [Model](docs/Model.md)
 - [Model1](docs/Model1.md)
 - [Model2](docs/Model2.md)
 - [ModelVersionsResponseV2](docs/ModelVersionsResponseV2.md)
 - [Name](docs/Name.md)
 - [NameAndVersion](docs/NameAndVersion.md)
 - [NamedKFServingVersionsQueryV2](docs/NamedKFServingVersionsQueryV2.md)
 - [NamedParametersTypeofAsJobReference](docs/NamedParametersTypeofAsJobReference.md)
 - [NamedParametersTypeofAsJobReferenceJobStatus](docs/NamedParametersTypeofAsJobReferenceJobStatus.md)
 - [NamedParametersTypeofFromLegacy](docs/NamedParametersTypeofFromLegacy.md)
 - [NamedParametersTypeofFromLegacyDocumentation](docs/NamedParametersTypeofFromLegacyDocumentation.md)
 - [NamedParametersTypeofIsNotLegacy](docs/NamedParametersTypeofIsNotLegacy.md)
 - [NamedPlugVersionsQueryV2](docs/NamedPlugVersionsQueryV2.md)
 - [NamedWebscriptVersionsQueryV2](docs/NamedWebscriptVersionsQueryV2.md)
 - [NotifyResult](docs/NotifyResult.md)
 - [OpenfaasDeployArgs](docs/OpenfaasDeployArgs.md)
 - [OpenfaasFunctionRef](docs/OpenfaasFunctionRef.md)
 - [Operation](docs/Operation.md)
 - [OperationStatus](docs/OperationStatus.md)
 - [OperationStatusError](docs/OperationStatusError.md)
 - [PagingResponse](docs/PagingResponse.md)
 - [ParentKeys](docs/ParentKeys.md)
 - [PatchInterfaceQuery](docs/PatchInterfaceQuery.md)
 - [PatchMetadataQuery](docs/PatchMetadataQuery.md)
 - [PatchPlugRequestV1](docs/PatchPlugRequestV1.md)
 - [Plug](docs/Plug.md)
 - [Plug1](docs/Plug1.md)
 - [Plug2](docs/Plug2.md)
 - [PlugDeleteForceQuery](docs/PlugDeleteForceQuery.md)
 - [PlugInterface](docs/PlugInterface.md)
 - [PlugListingAndQueryResponse](docs/PlugListingAndQueryResponse.md)
 - [PlugListingResponse](docs/PlugListingResponse.md)
 - [PlugManifest](docs/PlugManifest.md)
 - [PlugMeta](docs/PlugMeta.md)
 - [PlugProperty](docs/PlugProperty.md)
 - [PlugPropertyDataType](docs/PlugPropertyDataType.md)
 - [PlugPropertyFormat](docs/PlugPropertyFormat.md)
 - [PlugPropertyFormatType](docs/PlugPropertyFormatType.md)
 - [PlugResponse](docs/PlugResponse.md)
 - [PlugResponseV2](docs/PlugResponseV2.md)
 - [PlugType](docs/PlugType.md)
 - [PlugVersionsResponseV2](docs/PlugVersionsResponseV2.md)
 - [PostModelJobAsyncResponseV2](docs/PostModelJobAsyncResponseV2.md)
 - [PostModelJobSyncResponseV2](docs/PostModelJobSyncResponseV2.md)
 - [PostPlugJobAsyncResponseV2](docs/PostPlugJobAsyncResponseV2.md)
 - [PostPlugJobSyncResponseV2](docs/PostPlugJobSyncResponseV2.md)
 - [PostWebscriptJobAsyncResponseV2](docs/PostWebscriptJobAsyncResponseV2.md)
 - [PostWebscriptJobSyncResponseV2](docs/PostWebscriptJobSyncResponseV2.md)
 - [ProvidedDependency](docs/ProvidedDependency.md)
 - [PublishFunctionQuery](docs/PublishFunctionQuery.md)
 - [QueueEvents](docs/QueueEvents.md)
 - [RebuildComputedResponse](docs/RebuildComputedResponse.md)
 - [RebuildModelAsyncResponseV2](docs/RebuildModelAsyncResponseV2.md)
 - [RebuildModelSyncResponseV2](docs/RebuildModelSyncResponseV2.md)
 - [RebuildPlugAsyncResponseV2](docs/RebuildPlugAsyncResponseV2.md)
 - [RebuildPlugSyncResponseV2](docs/RebuildPlugSyncResponseV2.md)
 - [RebuildPolicy](docs/RebuildPolicy.md)
 - [RebuildQueryV2](docs/RebuildQueryV2.md)
 - [RebuildSubmittedResponse](docs/RebuildSubmittedResponse.md)
 - [RebuildWebscriptAsyncResponseV2](docs/RebuildWebscriptAsyncResponseV2.md)
 - [RebuildWebscriptSyncResponseV2](docs/RebuildWebscriptSyncResponseV2.md)
 - [RegistryErrorResponse](docs/RegistryErrorResponse.md)
 - [RemoveFunctionQueryV2](docs/RemoveFunctionQueryV2.md)
 - [RemovePlugQueryV2](docs/RemovePlugQueryV2.md)
 - [RequestDeployQuery](docs/RequestDeployQuery.md)
 - [RequestOperation](docs/RequestOperation.md)
 - [ResourceLimits](docs/ResourceLimits.md)
 - [RootPageResponse](docs/RootPageResponse.md)
 - [RuntimeAttributes](docs/RuntimeAttributes.md)
 - [RuntimeInfo](docs/RuntimeInfo.md)
 - [RuntimeNameQuery](docs/RuntimeNameQuery.md)
 - [RuntimeParams](docs/RuntimeParams.md)
 - [RuntimeQuery](docs/RuntimeQuery.md)
 - [RuntimeReference](docs/RuntimeReference.md)
 - [RuntimeSpecification](docs/RuntimeSpecification.md)
 - [RuntimeSummary](docs/RuntimeSummary.md)
 - [RuntimeSummaryAttrs](docs/RuntimeSummaryAttrs.md)
 - [RuntimeSummaryResponse](docs/RuntimeSummaryResponse.md)
 - [RuntimeVersionAndPathParams](docs/RuntimeVersionAndPathParams.md)
 - [RuntimeVersionInfo](docs/RuntimeVersionInfo.md)
 - [RuntimeVersionParams](docs/RuntimeVersionParams.md)
 - [RuntimeVersionQuery](docs/RuntimeVersionQuery.md)
 - [RuntimeVersionResponse](docs/RuntimeVersionResponse.md)
 - [RuntimeVersionSpecification](docs/RuntimeVersionSpecification.md)
 - [RuntimeVersionStatus](docs/RuntimeVersionStatus.md)
 - [RuntimeVersionSummary](docs/RuntimeVersionSummary.md)
 - [Scale](docs/Scale.md)
 - [Scale1](docs/Scale1.md)
 - [ScaleArgs](docs/ScaleArgs.md)
 - [ScaleJobStatus](docs/ScaleJobStatus.md)
 - [ScaleType](docs/ScaleType.md)
 - [SchemaByIdParams](docs/SchemaByIdParams.md)
 - [SchemaParams](docs/SchemaParams.md)
 - [SemanticVersionRange](docs/SemanticVersionRange.md)
 - [ShowRelatedType](docs/ShowRelatedType.md)
 - [Status](docs/Status.md)
 - [StatusAny](docs/StatusAny.md)
 - [StatusExclude](docs/StatusExclude.md)
 - [StatusFilter](docs/StatusFilter.md)
 - [StatusInclude](docs/StatusInclude.md)
 - [StatusResponse](docs/StatusResponse.md)
 - [StreamClosing](docs/StreamClosing.md)
 - [StreamReady](docs/StreamReady.md)
 - [SupportedEvents](docs/SupportedEvents.md)
 - [Tag](docs/Tag.md)
 - [TagQuery](docs/TagQuery.md)
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
 - [UnhealthyInvokableWebscriptError](docs/UnhealthyInvokableWebscriptError.md)
 - [UpdateDraftQuery](docs/UpdateDraftQuery.md)
 - [UpdateMetadataRequestV1](docs/UpdateMetadataRequestV1.md)
 - [UpdateMetadataRequestV2](docs/UpdateMetadataRequestV2.md)
 - [UpdateRecord](docs/UpdateRecord.md)
 - [UserPlugMeta](docs/UserPlugMeta.md)
 - [Verify](docs/Verify.md)
 - [Verify1](docs/Verify1.md)
 - [VerifyArgs](docs/VerifyArgs.md)
 - [VerifyJobStatus](docs/VerifyJobStatus.md)
 - [VerifyModelSyncResponseV2](docs/VerifyModelSyncResponseV2.md)
 - [VerifyPlugSyncResponseV2](docs/VerifyPlugSyncResponseV2.md)
 - [VerifyQueryV1](docs/VerifyQueryV1.md)
 - [VerifyResult](docs/VerifyResult.md)
 - [VerifyType](docs/VerifyType.md)
 - [VerifyWebscriptSyncResponseV2](docs/VerifyWebscriptSyncResponseV2.md)
 - [VersionIncludes](docs/VersionIncludes.md)
 - [VersionsQueryV2](docs/VersionsQueryV2.md)
 - [VersionsResponseV2](docs/VersionsResponseV2.md)
 - [WaitingChildrenEventSSE](docs/WaitingChildrenEventSSE.md)
 - [WaitingChildrenEventSSEEvent](docs/WaitingChildrenEventSSEEvent.md)
 - [WaitingEventData](docs/WaitingEventData.md)
 - [WaitingEventSSE](docs/WaitingEventSSE.md)
 - [WaitingEventSSEEvent](docs/WaitingEventSSEEvent.md)
 - [Webscript](docs/Webscript.md)
 - [Webscript1](docs/Webscript1.md)
 - [Webscript2](docs/Webscript2.md)
 - [WebscriptLatestVersionQueryV2](docs/WebscriptLatestVersionQueryV2.md)
 - [WebscriptLatestVersionsQueryV1](docs/WebscriptLatestVersionsQueryV1.md)
 - [WebscriptLatestVersionsQueryV2](docs/WebscriptLatestVersionsQueryV2.md)
 - [WebscriptManifest](docs/WebscriptManifest.md)
 - [WebscriptResponse](docs/WebscriptResponse.md)
 - [WebscriptResponseV2](docs/WebscriptResponseV2.md)
 - [WebscriptResponseWithInvokeLinkV2](docs/WebscriptResponseWithInvokeLinkV2.md)
 - [WebscriptVersionsResponseV2](docs/WebscriptVersionsResponseV2.md)
 - [WithAssetHALLink](docs/WithAssetHALLink.md)
 - [WithEmbeddedAltVersionsIKfservingResponseV2](docs/WithEmbeddedAltVersionsIKfservingResponseV2.md)
 - [WithEmbeddedAltVersionsIPlugResponseV2](docs/WithEmbeddedAltVersionsIPlugResponseV2.md)
 - [WithEmbeddedAltVersionsIWebscriptResponseWithInvokeLinkV2](docs/WithEmbeddedAltVersionsIWebscriptResponseWithInvokeLinkV2.md)
 - [WithEntityAttributes](docs/WithEntityAttributes.md)
 - [WithLimit](docs/WithLimit.md)
 - [WithPaging](docs/WithPaging.md)

