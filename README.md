# Waylay Registry Service
V2 API to build and deploy Waylay functions (plugs, webscripts, BYOML models).

This Python package is automatically generated based on the 
Waylay Registry OpenAPI specification (API version: 2.12.3)

It consists of two sub-packages that are both plugins for the waylay-sdk package.
- The `waylay-sdk-registry` sub-package contains the Registry api methods.
- The `waylay-sdk-registry-types` sub-package is an extension that contains the typed model classes for all path params, query params, body params and responses for each of the api methods in `waylay-sdk-registry`.

## Requirements.
This package requires Python 3.9+.

## Installation
Typically this package is installed when installing the [waylay-sdk](https://github.com/waylayio/waylay-sdk-py) package to enable the service's functionality.
When the service api methods are required, waylay-sdk-registry is included in:
- ```pip install waylay-sdk[registry]``` to install `waylay-sdk` along with only this service, or
- ```pip install waylay-sdk[services]``` to install `waylay-sdk` along with all services.
When the typed models are required, both waylay-sdk-registry and waylay-sdk-registry-types are included in:
- ```pip install waylay-sdk[registry,registry-types]``` to install `waylay-sdk` along with only this service including the typed models, or
- ```pip install waylay-sdk[services,services-types]``` to install `waylay-sdk` along with all services along with the typed models.

## Usage


```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.function_type import FunctionType
from waylay.services.registry.models.job_state_result import JobStateResult
from waylay.services.registry.models.job_type_schema import JobTypeSchema
from waylay.services.registry.models.jobs_response import JobsResponse
try:
    # List Jobs
    # calls `GET /registry/v2/jobs/`
    api_response = await waylay_client.registry.jobs.list(
        # query parameters:
        query = {
        },
    )
    print("The response of registry.jobs.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.jobs.list: %s\n" % e)
```


## Documentation for API Endpoints

All URIs are relative to *https://api.waylay.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*JobsApi* | [**events**](docs/JobsApi.md#events) | **GET** /registry/v2/jobs/events | Stream Events
*JobsApi* | [**get**](docs/JobsApi.md#get) | **GET** /registry/v2/jobs/{type}/{id} | Get Job
*JobsApi* | [**list**](docs/JobsApi.md#list) | **GET** /registry/v2/jobs/ | List Jobs
*ModelFunctionsApi* | [**create**](docs/ModelFunctionsApi.md#create) | **POST** /registry/v2/models/ | Create Model
*ModelFunctionsApi* | [**delete_asset**](docs/ModelFunctionsApi.md#delete_asset) | **DELETE** /registry/v2/models/{name}/versions/{version}/content/{wildcard} | Delete Model Asset
*ModelFunctionsApi* | [**get_archive**](docs/ModelFunctionsApi.md#get_archive) | **GET** /registry/v2/models/{name}/versions/{version}/content | Get Model Archive
*ModelFunctionsApi* | [**get_asset**](docs/ModelFunctionsApi.md#get_asset) | **GET** /registry/v2/models/{name}/versions/{version}/content/{wildcard} | Get File From Model Archive
*ModelFunctionsApi* | [**get_latest**](docs/ModelFunctionsApi.md#get_latest) | **GET** /registry/v2/models/{name} | Get Latest Model Version
*ModelFunctionsApi* | [**get**](docs/ModelFunctionsApi.md#get) | **GET** /registry/v2/models/{name}/versions/{version} | Get Model Version
*ModelFunctionsApi* | [**jobs**](docs/ModelFunctionsApi.md#jobs) | **GET** /registry/v2/models/{name}/versions/{version}/jobs | List Model Jobs
*ModelFunctionsApi* | [**list**](docs/ModelFunctionsApi.md#list) | **GET** /registry/v2/models/ | List Models
*ModelFunctionsApi* | [**list_versions**](docs/ModelFunctionsApi.md#list_versions) | **GET** /registry/v2/models/{name}/versions | List Model Versions
*ModelFunctionsApi* | [**patch_metadata**](docs/ModelFunctionsApi.md#patch_metadata) | **PATCH** /registry/v2/models/{name}/versions/{version}/metadata | Patch Model Metadata
*ModelFunctionsApi* | [**publish**](docs/ModelFunctionsApi.md#publish) | **POST** /registry/v2/models/{name}/versions/{version}/publish | Publish Draft Model
*ModelFunctionsApi* | [**rebuild**](docs/ModelFunctionsApi.md#rebuild) | **POST** /registry/v2/models/{name}/versions/{version}/rebuild | Rebuild Model
*ModelFunctionsApi* | [**remove_version**](docs/ModelFunctionsApi.md#remove_version) | **DELETE** /registry/v2/models/{name}/versions/{version} | Remove Model Version
*ModelFunctionsApi* | [**remove_versions**](docs/ModelFunctionsApi.md#remove_versions) | **DELETE** /registry/v2/models/{name} | Remove Model
*ModelFunctionsApi* | [**update_asset**](docs/ModelFunctionsApi.md#update_asset) | **PUT** /registry/v2/models/{name}/versions/{version}/content/{wildcard} | Update Model Asset
*ModelFunctionsApi* | [**update_assets**](docs/ModelFunctionsApi.md#update_assets) | **PUT** /registry/v2/models/{name}/versions/{version}/content | Update Model Assets
*ModelFunctionsApi* | [**verify**](docs/ModelFunctionsApi.md#verify) | **POST** /registry/v2/models/{name}/versions/{version}/verify | Verify Health Of Model
*PlugFunctionsApi* | [**create**](docs/PlugFunctionsApi.md#create) | **POST** /registry/v2/plugs/ | Create Plug
*PlugFunctionsApi* | [**delete_asset**](docs/PlugFunctionsApi.md#delete_asset) | **DELETE** /registry/v2/plugs/{name}/versions/{version}/content/{wildcard} | Delete Plug Asset
*PlugFunctionsApi* | [**get_archive**](docs/PlugFunctionsApi.md#get_archive) | **GET** /registry/v2/plugs/{name}/versions/{version}/content | Get Plug Archive
*PlugFunctionsApi* | [**get_asset**](docs/PlugFunctionsApi.md#get_asset) | **GET** /registry/v2/plugs/{name}/versions/{version}/content/{wildcard} | Get File From Plug Archive
*PlugFunctionsApi* | [**get_latest**](docs/PlugFunctionsApi.md#get_latest) | **GET** /registry/v2/plugs/{name} | Get Latest Plug Version
*PlugFunctionsApi* | [**get**](docs/PlugFunctionsApi.md#get) | **GET** /registry/v2/plugs/{name}/versions/{version} | Get Plug Version
*PlugFunctionsApi* | [**jobs**](docs/PlugFunctionsApi.md#jobs) | **GET** /registry/v2/plugs/{name}/versions/{version}/jobs | List Plug Jobs
*PlugFunctionsApi* | [**list**](docs/PlugFunctionsApi.md#list) | **GET** /registry/v2/plugs/ | List Plugs
*PlugFunctionsApi* | [**list_versions**](docs/PlugFunctionsApi.md#list_versions) | **GET** /registry/v2/plugs/{name}/versions | List Plug Versions
*PlugFunctionsApi* | [**patch_interface**](docs/PlugFunctionsApi.md#patch_interface) | **PATCH** /registry/v2/plugs/{name}/versions/{version}/interface | Patch Plug Interface
*PlugFunctionsApi* | [**patch_metadata**](docs/PlugFunctionsApi.md#patch_metadata) | **PATCH** /registry/v2/plugs/{name}/versions/{version}/metadata | Patch Plug Metadata
*PlugFunctionsApi* | [**publish**](docs/PlugFunctionsApi.md#publish) | **POST** /registry/v2/plugs/{name}/versions/{version}/publish | Publish Draft Plug
*PlugFunctionsApi* | [**rebuild**](docs/PlugFunctionsApi.md#rebuild) | **POST** /registry/v2/plugs/{name}/versions/{version}/rebuild | Rebuild Plug
*PlugFunctionsApi* | [**remove_version**](docs/PlugFunctionsApi.md#remove_version) | **DELETE** /registry/v2/plugs/{name}/versions/{version} | Remove Plug Version
*PlugFunctionsApi* | [**remove_versions**](docs/PlugFunctionsApi.md#remove_versions) | **DELETE** /registry/v2/plugs/{name} | Remove Plug
*PlugFunctionsApi* | [**update_asset**](docs/PlugFunctionsApi.md#update_asset) | **PUT** /registry/v2/plugs/{name}/versions/{version}/content/{wildcard} | Update Plug Asset
*PlugFunctionsApi* | [**update_assets**](docs/PlugFunctionsApi.md#update_assets) | **PUT** /registry/v2/plugs/{name}/versions/{version}/content | Update Plug Assets
*PlugFunctionsApi* | [**verify**](docs/PlugFunctionsApi.md#verify) | **POST** /registry/v2/plugs/{name}/versions/{version}/verify | Verify Health Of Plug
*RuntimesApi* | [**example_archive**](docs/RuntimesApi.md#example_archive) | **GET** /registry/v2/runtimes/{name}/versions/{version}/example | Get Runtime Example Archive
*RuntimesApi* | [**get_example_asset**](docs/RuntimesApi.md#get_example_asset) | **GET** /registry/v2/runtimes/{name}/versions/{version}/example/{wildcard} | Get File From Runtime Example Archive
*RuntimesApi* | [**get_latest**](docs/RuntimesApi.md#get_latest) | **GET** /registry/v2/runtimes/{name} | Get Latest Runtime Version
*RuntimesApi* | [**get**](docs/RuntimesApi.md#get) | **GET** /registry/v2/runtimes/{name}/versions/{version} | Get Runtime Version
*RuntimesApi* | [**list**](docs/RuntimesApi.md#list) | **GET** /registry/v2/runtimes/ | List Runtimes
*RuntimesApi* | [**list_versions**](docs/RuntimesApi.md#list_versions) | **GET** /registry/v2/runtimes/{name}/versions | List Runtime Versions
*SchemasApi* | [**get_by_role**](docs/SchemasApi.md#get_by_role) | **GET** /registry/v2/schemas/{functionType}/{role}/schema | Get Asset Schema
*SchemasApi* | [**get**](docs/SchemasApi.md#get) | **GET** /registry/v2/schemas/{schemaId} | Get Asset Schema
*WebscriptFunctionsApi* | [**create**](docs/WebscriptFunctionsApi.md#create) | **POST** /registry/v2/webscripts/ | Create Webscript Version
*WebscriptFunctionsApi* | [**delete_asset**](docs/WebscriptFunctionsApi.md#delete_asset) | **DELETE** /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard} | Delete Webscript Asset
*WebscriptFunctionsApi* | [**get_archive**](docs/WebscriptFunctionsApi.md#get_archive) | **GET** /registry/v2/webscripts/{name}/versions/{version}/content | Get Webscript Archive
*WebscriptFunctionsApi* | [**get_asset**](docs/WebscriptFunctionsApi.md#get_asset) | **GET** /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard} | Get File From Webscript Archive
*WebscriptFunctionsApi* | [**get_latest**](docs/WebscriptFunctionsApi.md#get_latest) | **GET** /registry/v2/webscripts/{name} | Get Latest Webscript Version
*WebscriptFunctionsApi* | [**get**](docs/WebscriptFunctionsApi.md#get) | **GET** /registry/v2/webscripts/{name}/versions/{version} | Get Webscript Version
*WebscriptFunctionsApi* | [**jobs**](docs/WebscriptFunctionsApi.md#jobs) | **GET** /registry/v2/webscripts/{name}/versions/{version}/jobs | List Webscript Jobs
*WebscriptFunctionsApi* | [**list_versions**](docs/WebscriptFunctionsApi.md#list_versions) | **GET** /registry/v2/webscripts/{name}/versions | List Webscript Versions
*WebscriptFunctionsApi* | [**list**](docs/WebscriptFunctionsApi.md#list) | **GET** /registry/v2/webscripts/ | List Webscripts
*WebscriptFunctionsApi* | [**patch_metadata**](docs/WebscriptFunctionsApi.md#patch_metadata) | **PATCH** /registry/v2/webscripts/{name}/versions/{version}/metadata | Patch Webscript Metadata
*WebscriptFunctionsApi* | [**publish**](docs/WebscriptFunctionsApi.md#publish) | **POST** /registry/v2/webscripts/{name}/versions/{version}/publish | Publish Draft Webscript
*WebscriptFunctionsApi* | [**rebuild**](docs/WebscriptFunctionsApi.md#rebuild) | **POST** /registry/v2/webscripts/{name}/versions/{version}/rebuild | Rebuild Webscript
*WebscriptFunctionsApi* | [**remove_version**](docs/WebscriptFunctionsApi.md#remove_version) | **DELETE** /registry/v2/webscripts/{name}/versions/{version} | Remove Webscript Version
*WebscriptFunctionsApi* | [**remove_versions**](docs/WebscriptFunctionsApi.md#remove_versions) | **DELETE** /registry/v2/webscripts/{name} | Remove Webscript
*WebscriptFunctionsApi* | [**update_asset**](docs/WebscriptFunctionsApi.md#update_asset) | **PUT** /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard} | Update Webscript Asset
*WebscriptFunctionsApi* | [**update_assets**](docs/WebscriptFunctionsApi.md#update_assets) | **PUT** /registry/v2/webscripts/{name}/versions/{version}/content | Update Webscript Assets
*WebscriptFunctionsApi* | [**verify**](docs/WebscriptFunctionsApi.md#verify) | **POST** /registry/v2/webscripts/{name}/versions/{version}/verify | Verify Health Of Webscript
*DefaultApi* | [**get**](docs/DefaultApi.md#get) | **GET** /registry/v2/ | Version


## Documentation For Models

 - [ActiveEventData](docs/ActiveEventData.md)
 - [ActiveEventSSE](docs/ActiveEventSSE.md)
 - [ActiveEventSSEEvent](docs/ActiveEventSSEEvent.md)
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
 - [AsyncDeployQuery](docs/AsyncDeployQuery.md)
 - [AsyncDeployQueryV1](docs/AsyncDeployQueryV1.md)
 - [AsyncQueryDefaultFalse](docs/AsyncQueryDefaultFalse.md)
 - [AsyncQueryDefaultTrue](docs/AsyncQueryDefaultTrue.md)
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
 - [CreateKFServingAsyncResponse](docs/CreateKFServingAsyncResponse.md)
 - [CreatePlugAsyncResponse](docs/CreatePlugAsyncResponse.md)
 - [CreateWebscriptAsyncResponse](docs/CreateWebscriptAsyncResponse.md)
 - [DelayedEventData](docs/DelayedEventData.md)
 - [DelayedEventSSE](docs/DelayedEventSSE.md)
 - [DelayedEventSSEEvent](docs/DelayedEventSSEEvent.md)
 - [Deploy](docs/Deploy.md)
 - [Deploy1](docs/Deploy1.md)
 - [DeployArgs](docs/DeployArgs.md)
 - [DeployArgsDeploySpecOverrides](docs/DeployArgsDeploySpecOverrides.md)
 - [DeployAttributesFilter](docs/DeployAttributesFilter.md)
 - [DeployJobStatus](docs/DeployJobStatus.md)
 - [DeployResult](docs/DeployResult.md)
 - [DeploySpec](docs/DeploySpec.md)
 - [DeploySpecOpenfaasSpec](docs/DeploySpecOpenfaasSpec.md)
 - [DeployType](docs/DeployType.md)
 - [DeprecatePreviousPolicy](docs/DeprecatePreviousPolicy.md)
 - [DeprecatePreviousQuery](docs/DeprecatePreviousQuery.md)
 - [DeprecatedDraftFilter](docs/DeprecatedDraftFilter.md)
 - [Documentation](docs/Documentation.md)
 - [DocumentationProperty](docs/DocumentationProperty.md)
 - [DryRunQuery](docs/DryRunQuery.md)
 - [EntityResponse](docs/EntityResponse.md)
 - [ErrorAndStatusResponse](docs/ErrorAndStatusResponse.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [EventAck](docs/EventAck.md)
 - [EventClose](docs/EventClose.md)
 - [EventKeepAlive](docs/EventKeepAlive.md)
 - [EventSSE](docs/EventSSE.md)
 - [EventTypeSSE](docs/EventTypeSSE.md)
 - [EventWithCloseSSE](docs/EventWithCloseSSE.md)
 - [ExposedOpenfaasDeploySpec](docs/ExposedOpenfaasDeploySpec.md)
 - [FailedEventData](docs/FailedEventData.md)
 - [FailedEventSSE](docs/FailedEventSSE.md)
 - [FailedEventSSEEvent](docs/FailedEventSSEEvent.md)
 - [FailureReason](docs/FailureReason.md)
 - [FileUpload](docs/FileUpload.md)
 - [ForceDeleteQueryV1](docs/ForceDeleteQueryV1.md)
 - [FunctionDeleteQuery](docs/FunctionDeleteQuery.md)
 - [FunctionDeployOverrides](docs/FunctionDeployOverrides.md)
 - [FunctionDeployOverridesType](docs/FunctionDeployOverridesType.md)
 - [FunctionEntityQuery](docs/FunctionEntityQuery.md)
 - [FunctionJobArgs](docs/FunctionJobArgs.md)
 - [FunctionManifest](docs/FunctionManifest.md)
 - [FunctionMeta](docs/FunctionMeta.md)
 - [FunctionNameVersion](docs/FunctionNameVersion.md)
 - [FunctionRef](docs/FunctionRef.md)
 - [FunctionSpec](docs/FunctionSpec.md)
 - [FunctionType](docs/FunctionType.md)
 - [FunctionVersionQuery](docs/FunctionVersionQuery.md)
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
 - [LatestFunctionsQuery](docs/LatestFunctionsQuery.md)
 - [LatestModelsResponseV2](docs/LatestModelsResponseV2.md)
 - [LatestModelsResponseV2EntitiesInner](docs/LatestModelsResponseV2EntitiesInner.md)
 - [LatestPlugQuery](docs/LatestPlugQuery.md)
 - [LatestPlugVersionQueryV2](docs/LatestPlugVersionQueryV2.md)
 - [LatestPlugVersionsQuery](docs/LatestPlugVersionsQuery.md)
 - [LatestPlugVersionsQueryV2](docs/LatestPlugVersionsQueryV2.md)
 - [LatestPlugsQuery](docs/LatestPlugsQuery.md)
 - [LatestPlugsResponseV2](docs/LatestPlugsResponseV2.md)
 - [LatestPlugsResponseV2EntitiesInner](docs/LatestPlugsResponseV2EntitiesInner.md)
 - [LatestVersionLevel](docs/LatestVersionLevel.md)
 - [LatestWebscriptsResponseV2](docs/LatestWebscriptsResponseV2.md)
 - [LatestWebscriptsResponseV2EntitiesInner](docs/LatestWebscriptsResponseV2EntitiesInner.md)
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
 - [LimitQuery](docs/LimitQuery.md)
 - [MediaType](docs/MediaType.md)
 - [MessageAndStatusResponse](docs/MessageAndStatusResponse.md)
 - [MessageResponse](docs/MessageResponse.md)
 - [Model](docs/Model.md)
 - [Model1](docs/Model1.md)
 - [Model2](docs/Model2.md)
 - [ModelVersionsResponseV2](docs/ModelVersionsResponseV2.md)
 - [MultipartFileUpload](docs/MultipartFileUpload.md)
 - [Name](docs/Name.md)
 - [NameAndVersion](docs/NameAndVersion.md)
 - [NamedFunctionVersionsQuery](docs/NamedFunctionVersionsQuery.md)
 - [NamedKFServingVersionsQueryV2](docs/NamedKFServingVersionsQueryV2.md)
 - [NamedParametersTypeofAsJobReference](docs/NamedParametersTypeofAsJobReference.md)
 - [NamedParametersTypeofAsJobReferenceJobStatus](docs/NamedParametersTypeofAsJobReferenceJobStatus.md)
 - [NamedParametersTypeofFromLegacy](docs/NamedParametersTypeofFromLegacy.md)
 - [NamedParametersTypeofFromLegacyDocumentation](docs/NamedParametersTypeofFromLegacyDocumentation.md)
 - [NamedParametersTypeofIsNotLegacy](docs/NamedParametersTypeofIsNotLegacy.md)
 - [NamedPlugVersionsQueryV2](docs/NamedPlugVersionsQueryV2.md)
 - [NamedVersionsFilter](docs/NamedVersionsFilter.md)
 - [NamedWebscriptVersionsQueryV2](docs/NamedWebscriptVersionsQueryV2.md)
 - [OpenfaasDeployArgs](docs/OpenfaasDeployArgs.md)
 - [OpenfaasFunctionRef](docs/OpenfaasFunctionRef.md)
 - [Operation](docs/Operation.md)
 - [OperationStatus](docs/OperationStatus.md)
 - [OperationStatusError](docs/OperationStatusError.md)
 - [PagingQuery](docs/PagingQuery.md)
 - [PagingResponse](docs/PagingResponse.md)
 - [ParentKeys](docs/ParentKeys.md)
 - [PatchInterfaceQuery](docs/PatchInterfaceQuery.md)
 - [PatchMetadataQuery](docs/PatchMetadataQuery.md)
 - [PatchPlugRequestV1](docs/PatchPlugRequestV1.md)
 - [Plug](docs/Plug.md)
 - [Plug1](docs/Plug1.md)
 - [Plug2](docs/Plug2.md)
 - [PlugDeleteForceQuery](docs/PlugDeleteForceQuery.md)
 - [PlugDeleteQuery](docs/PlugDeleteQuery.md)
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
 - [PlugTypeQuery](docs/PlugTypeQuery.md)
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
 - [RebuildQueryParams](docs/RebuildQueryParams.md)
 - [RebuildQueryV2](docs/RebuildQueryV2.md)
 - [RebuildSubmittedResponse](docs/RebuildSubmittedResponse.md)
 - [RebuildWebscriptAsyncResponseV2](docs/RebuildWebscriptAsyncResponseV2.md)
 - [RebuildWebscriptSyncResponseV2](docs/RebuildWebscriptSyncResponseV2.md)
 - [RemoveFunctionQueryV2](docs/RemoveFunctionQueryV2.md)
 - [RemovePlugQueryV2](docs/RemovePlugQueryV2.md)
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
 - [Status](docs/Status.md)
 - [StatusAny](docs/StatusAny.md)
 - [StatusFilter](docs/StatusFilter.md)
 - [StatusInclude](docs/StatusInclude.md)
 - [StatusResponse](docs/StatusResponse.md)
 - [StreamClosing](docs/StreamClosing.md)
 - [StreamReady](docs/StreamReady.md)
 - [SupportedEvents](docs/SupportedEvents.md)
 - [Tag](docs/Tag.md)
 - [TagQuery](docs/TagQuery.md)
 - [TagsFilter](docs/TagsFilter.md)
 - [TagsQuery](docs/TagsQuery.md)
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
 - [UpdateComment](docs/UpdateComment.md)
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
 - [VersionsQuery](docs/VersionsQuery.md)
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
 - [WithEntityAttributes](docs/WithEntityAttributes.md)
 - [WithLimit](docs/WithLimit.md)
 - [WithPaging](docs/WithPaging.md)

