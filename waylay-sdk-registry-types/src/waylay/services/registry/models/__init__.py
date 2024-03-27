# coding: utf-8
"""Waylay Function Registry: REST Models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

version: 2.12.4

V2 API to build and deploy Waylay functions (plugs, webscripts, BYOML models).

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

__version__ = "2.12.4rc1"

# import models into model package
from .active_event_data import ActiveEventData
from .active_event_sse import ActiveEventSSE
from .active_event_sse_event import ActiveEventSSEEvent
from .alt_version_hal_link import AltVersionHALLink
from .any_function_response import AnyFunctionResponse
from .any_job_for_function import AnyJobForFunction
from .any_job_result import AnyJobResult
from .any_job_status import AnyJobStatus
from .any_job_status_summary import AnyJobStatusSummary
from .archive_format import ArchiveFormat
from .asset_condition import AssetCondition
from .asset_condition_content_type import AssetConditionContentType
from .asset_condition_pattern import AssetConditionPattern
from .asset_path_params_v2 import AssetPathParamsV2
from .asset_role import AssetRole
from .asset_summary import AssetSummary
from .asset_summary_with_hal_link import AssetSummaryWithHALLink
from .asset_summary_with_hal_link_links import AssetSummaryWithHALLinkLinks
from .assets_conditions import AssetsConditions
from .async_deploy_query import AsyncDeployQuery
from .async_deploy_query_v1 import AsyncDeployQueryV1
from .async_query_default_false import AsyncQueryDefaultFalse
from .async_query_default_true import AsyncQueryDefaultTrue
from .async_verify_query import AsyncVerifyQuery
from .batch import Batch
from .batch_args import BatchArgs
from .batch_job_status import BatchJobStatus
from .batch_job_status_type import BatchJobStatusType
from .batch_result import BatchResult
from .build import Build
from .build1 import Build1
from .build_args import BuildArgs
from .build_job_status import BuildJobStatus
from .build_result import BuildResult
from .build_spec import BuildSpec
from .build_type import BuildType
from .cleanup_result import CleanupResult
from .compiled_runtime_version import CompiledRuntimeVersion
from .completed_event_data import CompletedEventData
from .completed_event_sse import CompletedEventSSE
from .completed_event_sse_event import CompletedEventSSEEvent
from .content_query_v2 import ContentQueryV2
from .content_validation_listing import ContentValidationListing
from .create_function_query_v2 import CreateFunctionQueryV2
from .create_kf_serving_async_response import CreateKFServingAsyncResponse
from .create_plug_async_response import CreatePlugAsyncResponse
from .create_webscript_async_response import CreateWebscriptAsyncResponse
from .delayed_event_data import DelayedEventData
from .delayed_event_sse import DelayedEventSSE
from .delayed_event_sse_event import DelayedEventSSEEvent
from .deploy import Deploy
from .deploy1 import Deploy1
from .deploy_args import DeployArgs
from .deploy_args_deploy_spec_overrides import DeployArgsDeploySpecOverrides
from .deploy_attributes_filter import DeployAttributesFilter
from .deploy_job_status import DeployJobStatus
from .deploy_result import DeployResult
from .deploy_spec import DeploySpec
from .deploy_spec_openfaas_spec import DeploySpecOpenfaasSpec
from .deploy_type import DeployType
from .deprecate_previous_policy import DeprecatePreviousPolicy
from .deprecate_previous_query import DeprecatePreviousQuery
from .deprecated_draft_filter import DeprecatedDraftFilter
from .documentation import Documentation
from .documentation_property import DocumentationProperty
from .dry_run_query import DryRunQuery
from .entity_response import EntityResponse
from .error_and_status_response import ErrorAndStatusResponse
from .error_response import ErrorResponse
from .event_ack import EventAck
from .event_close import EventClose
from .event_keep_alive import EventKeepAlive
from .event_sse import EventSSE
from .event_type_sse import EventTypeSSE
from .event_with_close_sse import EventWithCloseSSE
from .exposed_openfaas_deploy_spec import ExposedOpenfaasDeploySpec
from .failed_event_data import FailedEventData
from .failed_event_sse import FailedEventSSE
from .failed_event_sse_event import FailedEventSSEEvent
from .failure_reason import FailureReason
from .file_upload import FileUpload
from .force_delete_query_v1 import ForceDeleteQueryV1
from .function_delete_query import FunctionDeleteQuery
from .function_deploy_overrides import FunctionDeployOverrides
from .function_deploy_overrides_type import FunctionDeployOverridesType
from .function_entity_query import FunctionEntityQuery
from .function_job_args import FunctionJobArgs
from .function_manifest import FunctionManifest
from .function_meta import FunctionMeta
from .function_name_version import FunctionNameVersion
from .function_ref import FunctionRef
from .function_spec import FunctionSpec
from .function_type import FunctionType
from .function_version_query import FunctionVersionQuery
from .get_content_params_v2 import GetContentParamsV2
from .get_invokable_webscript_query import GetInvokableWebscriptQuery
from .get_model_response_v2 import GetModelResponseV2
from .get_plug_response_v2 import GetPlugResponseV2
from .get_plug_response_v2_links import GetPlugResponseV2Links
from .get_plug_response_v2_links_draft import GetPlugResponseV2LinksDraft
from .get_plug_response_v2_links_published import GetPlugResponseV2LinksPublished
from .get_runtime_by_name_and_version_query import GetRuntimeByNameAndVersionQuery
from .get_runtime_by_name_query import GetRuntimeByNameQuery
from .get_runtime_example_query import GetRuntimeExampleQuery
from .get_runtime_versions_query import GetRuntimeVersionsQuery
from .get_webscript_response_v2 import GetWebscriptResponseV2
from .get_webscript_response_v2_links import GetWebscriptResponseV2Links
from .hal_link import HALLink
from .invokable_webscript_response import InvokableWebscriptResponse
from .invokable_webscript_response_entity import InvokableWebscriptResponseEntity
from .invokable_webscript_response_entity_webscript import (
    InvokableWebscriptResponseEntityWebscript,
)
from .invoke_hal_link import InvokeHALLink
from .invoke_internal_hal_link import InvokeInternalHALLink
from .job_and_function_hal_link import JobAndFunctionHALLink
from .job_cause import JobCause
from .job_causes import JobCauses
from .job_event_payload_active_event_data import JobEventPayloadActiveEventData
from .job_event_payload_completed_event_data import JobEventPayloadCompletedEventData
from .job_event_payload_delayed_event_data import JobEventPayloadDelayedEventData
from .job_event_payload_failed_event_data import JobEventPayloadFailedEventData
from .job_event_payload_waiting_children_event_data import (
    JobEventPayloadWaitingChildrenEventData,
)
from .job_event_payload_waiting_event_data import JobEventPayloadWaitingEventData
from .job_event_response_active_event_data import JobEventResponseActiveEventData
from .job_event_response_completed_event_data import JobEventResponseCompletedEventData
from .job_event_response_delayed_event_data import JobEventResponseDelayedEventData
from .job_event_response_failed_event_data import JobEventResponseFailedEventData
from .job_event_response_waiting_children_event_data import (
    JobEventResponseWaitingChildrenEventData,
)
from .job_event_response_waiting_event_data import JobEventResponseWaitingEventData
from .job_event_sse import JobEventSSE
from .job_events_and_function_hal_link import JobEventsAndFunctionHALLink
from .job_events_filter_query import JobEventsFilterQuery
from .job_events_hal_link import JobEventsHALLink
from .job_hal_links import JobHALLinks
from .job_query import JobQuery
from .job_reference import JobReference
from .job_reference_params import JobReferenceParams
from .job_response import JobResponse
from .job_state import JobState
from .job_state_active import JobStateActive
from .job_state_completed import JobStateCompleted
from .job_state_delayed import JobStateDelayed
from .job_state_failed import JobStateFailed
from .job_state_finished import JobStateFinished
from .job_state_result import JobStateResult
from .job_state_unknown import JobStateUnknown
from .job_state_waiting import JobStateWaiting
from .job_state_waiting_children import JobStateWaitingChildren
from .job_status import JobStatus
from .job_status_and_entity_hal_links import JobStatusAndEntityHALLinks
from .job_status_hal_link import JobStatusHALLink
from .job_status_progress import JobStatusProgress
from .job_submitted_response import JobSubmittedResponse
from .job_type import JobType
from .job_type_batch import JobTypeBatch
from .job_type_build import JobTypeBuild
from .job_type_deploy import JobTypeDeploy
from .job_type_scale import JobTypeScale
from .job_type_schema import JobTypeSchema
from .job_type_undeploy import JobTypeUndeploy
from .job_type_verify import JobTypeVerify
from .jobs_for_model_response_v2 import JobsForModelResponseV2
from .jobs_for_model_response_v2_links import JobsForModelResponseV2Links
from .jobs_for_plug_response_v2 import JobsForPlugResponseV2
from .jobs_for_plug_response_v2_links import JobsForPlugResponseV2Links
from .jobs_for_webscript_response_v2 import JobsForWebscriptResponseV2
from .jobs_for_webscript_response_v2_links import JobsForWebscriptResponseV2Links
from .jobs_hal_link import JobsHALLink
from .jobs_response import JobsResponse
from .keep_alive_event_sse import KeepAliveEventSSE
from .kf_serving_delete_multiple_response import KFServingDeleteMultipleResponse
from .kf_serving_delete_multiple_with_job_response import (
    KFServingDeleteMultipleWithJobResponse,
)
from .kf_serving_delete_query_v1 import KFServingDeleteQueryV1
from .kf_serving_delete_query_v2 import KFServingDeleteQueryV2
from .kf_serving_delete_response import KFServingDeleteResponse
from .kf_serving_delete_with_job_response import KFServingDeleteWithJobResponse
from .kf_serving_latest_version_query_v2 import KFServingLatestVersionQueryV2
from .kf_serving_latest_versions_query_v1 import KFServingLatestVersionsQueryV1
from .kf_serving_latest_versions_query_v2 import KFServingLatestVersionsQueryV2
from .kf_serving_manifest import KFServingManifest
from .kf_serving_models_response import KFServingModelsResponse
from .kf_serving_response import KFServingResponse
from .kf_serving_versions_query_v1 import KFServingVersionsQueryV1
from .kfserving_response_v2 import KfservingResponseV2
from .language_release import LanguageRelease
from .latest_function_versions_query import LatestFunctionVersionsQuery
from .latest_functions_query import LatestFunctionsQuery
from .latest_models_response_v2 import LatestModelsResponseV2
from .latest_models_response_v2_entities_inner import (
    LatestModelsResponseV2EntitiesInner,
)
from .latest_plug_query import LatestPlugQuery
from .latest_plug_version_query_v2 import LatestPlugVersionQueryV2
from .latest_plug_versions_query import LatestPlugVersionsQuery
from .latest_plug_versions_query_v2 import LatestPlugVersionsQueryV2
from .latest_plugs_query import LatestPlugsQuery
from .latest_plugs_response_v2 import LatestPlugsResponseV2
from .latest_plugs_response_v2_entities_inner import LatestPlugsResponseV2EntitiesInner
from .latest_version_level import LatestVersionLevel
from .latest_webscripts_response_v2 import LatestWebscriptsResponseV2
from .latest_webscripts_response_v2_entities_inner import (
    LatestWebscriptsResponseV2EntitiesInner,
)
from .legacy_configuration_object import LegacyConfigurationObject
from .legacy_configuration_object_format import LegacyConfigurationObjectFormat
from .legacy_configuration_response_object import LegacyConfigurationResponseObject
from .legacy_create_debug_response import LegacyCreateDebugResponse
from .legacy_debug_plug_manifest import LegacyDebugPlugManifest
from .legacy_debug_plug_request import LegacyDebugPlugRequest
from .legacy_documentation import LegacyDocumentation
from .legacy_documentation_request import LegacyDocumentationRequest
from .legacy_function_meta import LegacyFunctionMeta
from .legacy_plug_create_query import LegacyPlugCreateQuery
from .legacy_plug_create_request import LegacyPlugCreateRequest
from .legacy_plug_create_response import LegacyPlugCreateResponse
from .legacy_plug_meta_request import LegacyPlugMetaRequest
from .legacy_plug_query import LegacyPlugQuery
from .legacy_plug_request import LegacyPlugRequest
from .legacy_plug_request_metadata import LegacyPlugRequestMetadata
from .legacy_plug_request_metadata_documentation import (
    LegacyPlugRequestMetadataDocumentation,
)
from .legacy_plug_request_metadata_documentation_any_of import (
    LegacyPlugRequestMetadataDocumentationAnyOf,
)
from .legacy_plug_request_metadata_raw_data_inner import (
    LegacyPlugRequestMetadataRawDataInner,
)
from .legacy_plug_response import LegacyPlugResponse
from .legacy_plug_response_metadata import LegacyPlugResponseMetadata
from .legacy_plug_script_meta import LegacyPlugScriptMeta
from .legacy_plug_script_meta_raw_data_inner import LegacyPlugScriptMetaRawDataInner
from .legacy_plug_script_response import LegacyPlugScriptResponse
from .legacy_required_properties_inner import LegacyRequiredPropertiesInner
from .legacy_required_property_object import LegacyRequiredPropertyObject
from .limit_query import LimitQuery
from .media_type import MediaType
from .message_and_status_response import MessageAndStatusResponse
from .message_response import MessageResponse
from .model import Model
from .model1 import Model1
from .model2 import Model2
from .model_versions_response_v2 import ModelVersionsResponseV2
from .multipart_file_upload import MultipartFileUpload
from .name import Name
from .name_and_version import NameAndVersion
from .named_function_versions_query import NamedFunctionVersionsQuery
from .named_kf_serving_versions_query_v2 import NamedKFServingVersionsQueryV2
from .named_parameters_typeof_as_job_reference import (
    NamedParametersTypeofAsJobReference,
)
from .named_parameters_typeof_as_job_reference_job_status import (
    NamedParametersTypeofAsJobReferenceJobStatus,
)
from .named_parameters_typeof_from_legacy import NamedParametersTypeofFromLegacy
from .named_parameters_typeof_from_legacy_documentation import (
    NamedParametersTypeofFromLegacyDocumentation,
)
from .named_parameters_typeof_is_not_legacy import NamedParametersTypeofIsNotLegacy
from .named_plug_versions_query_v2 import NamedPlugVersionsQueryV2
from .named_versions_filter import NamedVersionsFilter
from .named_webscript_versions_query_v2 import NamedWebscriptVersionsQueryV2
from .openfaas_deploy_args import OpenfaasDeployArgs
from .openfaas_function_ref import OpenfaasFunctionRef
from .operation import Operation
from .operation_status import OperationStatus
from .operation_status_error import OperationStatusError
from .paging_query import PagingQuery
from .paging_response import PagingResponse
from .parent_keys import ParentKeys
from .patch_interface_query import PatchInterfaceQuery
from .patch_metadata_query import PatchMetadataQuery
from .patch_plug_request_v1 import PatchPlugRequestV1
from .plug import Plug
from .plug1 import Plug1
from .plug2 import Plug2
from .plug_delete_force_query import PlugDeleteForceQuery
from .plug_delete_query import PlugDeleteQuery
from .plug_interface import PlugInterface
from .plug_listing_and_query_response import PlugListingAndQueryResponse
from .plug_listing_response import PlugListingResponse
from .plug_manifest import PlugManifest
from .plug_meta import PlugMeta
from .plug_property import PlugProperty
from .plug_property_data_type import PlugPropertyDataType
from .plug_property_format import PlugPropertyFormat
from .plug_property_format_type import PlugPropertyFormatType
from .plug_response import PlugResponse
from .plug_response_v2 import PlugResponseV2
from .plug_type import PlugType
from .plug_type_query import PlugTypeQuery
from .plug_versions_response_v2 import PlugVersionsResponseV2
from .post_model_job_async_response_v2 import PostModelJobAsyncResponseV2
from .post_model_job_sync_response_v2 import PostModelJobSyncResponseV2
from .post_plug_job_async_response_v2 import PostPlugJobAsyncResponseV2
from .post_plug_job_sync_response_v2 import PostPlugJobSyncResponseV2
from .post_webscript_job_async_response_v2 import PostWebscriptJobAsyncResponseV2
from .post_webscript_job_sync_response_v2 import PostWebscriptJobSyncResponseV2
from .provided_dependency import ProvidedDependency
from .publish_function_query import PublishFunctionQuery
from .queue_events import QueueEvents
from .rebuild_computed_response import RebuildComputedResponse
from .rebuild_model_async_response_v2 import RebuildModelAsyncResponseV2
from .rebuild_model_sync_response_v2 import RebuildModelSyncResponseV2
from .rebuild_plug_async_response_v2 import RebuildPlugAsyncResponseV2
from .rebuild_plug_sync_response_v2 import RebuildPlugSyncResponseV2
from .rebuild_policy import RebuildPolicy
from .rebuild_query_params import RebuildQueryParams
from .rebuild_query_v2 import RebuildQueryV2
from .rebuild_submitted_response import RebuildSubmittedResponse
from .rebuild_webscript_async_response_v2 import RebuildWebscriptAsyncResponseV2
from .rebuild_webscript_sync_response_v2 import RebuildWebscriptSyncResponseV2
from .remove_function_query_v2 import RemoveFunctionQueryV2
from .remove_plug_query_v2 import RemovePlugQueryV2
from .request_operation import RequestOperation
from .resource_limits import ResourceLimits
from .root_page_response import RootPageResponse
from .runtime_attributes import RuntimeAttributes
from .runtime_info import RuntimeInfo
from .runtime_name_query import RuntimeNameQuery
from .runtime_params import RuntimeParams
from .runtime_query import RuntimeQuery
from .runtime_reference import RuntimeReference
from .runtime_specification import RuntimeSpecification
from .runtime_summary import RuntimeSummary
from .runtime_summary_attrs import RuntimeSummaryAttrs
from .runtime_summary_response import RuntimeSummaryResponse
from .runtime_version_and_path_params import RuntimeVersionAndPathParams
from .runtime_version_info import RuntimeVersionInfo
from .runtime_version_params import RuntimeVersionParams
from .runtime_version_query import RuntimeVersionQuery
from .runtime_version_response import RuntimeVersionResponse
from .runtime_version_specification import RuntimeVersionSpecification
from .runtime_version_status import RuntimeVersionStatus
from .runtime_version_summary import RuntimeVersionSummary
from .scale import Scale
from .scale1 import Scale1
from .scale_args import ScaleArgs
from .scale_job_status import ScaleJobStatus
from .scale_type import ScaleType
from .schema_by_id_params import SchemaByIdParams
from .schema_params import SchemaParams
from .semantic_version_range import SemanticVersionRange
from .status import Status
from .status_any import StatusAny
from .status_filter import StatusFilter
from .status_include import StatusInclude
from .status_response import StatusResponse
from .stream_closing import StreamClosing
from .stream_ready import StreamReady
from .supported_events import SupportedEvents
from .tag import Tag
from .tag_query import TagQuery
from .tags_filter import TagsFilter
from .tags_query import TagsQuery
from .timestamp_absolute import TimestampAbsolute
from .timestamp_age import TimestampAge
from .timestamp_spec import TimestampSpec
from .undeploy import Undeploy
from .undeploy1 import Undeploy1
from .undeploy_args import UndeployArgs
from .undeploy_job_status import UndeployJobStatus
from .undeploy_result import UndeployResult
from .undeploy_submitted_response_v2 import UndeploySubmittedResponseV2
from .undeploy_type import UndeployType
from .undeployed_response_v2 import UndeployedResponseV2
from .unhealthy_invokable_webscript_error import UnhealthyInvokableWebscriptError
from .update_comment import UpdateComment
from .update_draft_query import UpdateDraftQuery
from .update_metadata_request_v1 import UpdateMetadataRequestV1
from .update_metadata_request_v2 import UpdateMetadataRequestV2
from .update_record import UpdateRecord
from .user_plug_meta import UserPlugMeta
from .verify import Verify
from .verify1 import Verify1
from .verify_args import VerifyArgs
from .verify_job_status import VerifyJobStatus
from .verify_model_sync_response_v2 import VerifyModelSyncResponseV2
from .verify_plug_sync_response_v2 import VerifyPlugSyncResponseV2
from .verify_query_v1 import VerifyQueryV1
from .verify_result import VerifyResult
from .verify_type import VerifyType
from .verify_webscript_sync_response_v2 import VerifyWebscriptSyncResponseV2
from .version_includes import VersionIncludes
from .versions_query import VersionsQuery
from .versions_query_v2 import VersionsQueryV2
from .versions_response_v2 import VersionsResponseV2
from .waiting_children_event_sse import WaitingChildrenEventSSE
from .waiting_children_event_sse_event import WaitingChildrenEventSSEEvent
from .waiting_event_data import WaitingEventData
from .waiting_event_sse import WaitingEventSSE
from .waiting_event_sse_event import WaitingEventSSEEvent
from .webscript import Webscript
from .webscript1 import Webscript1
from .webscript2 import Webscript2
from .webscript_latest_version_query_v2 import WebscriptLatestVersionQueryV2
from .webscript_latest_versions_query_v1 import WebscriptLatestVersionsQueryV1
from .webscript_latest_versions_query_v2 import WebscriptLatestVersionsQueryV2
from .webscript_manifest import WebscriptManifest
from .webscript_response import WebscriptResponse
from .webscript_response_v2 import WebscriptResponseV2
from .webscript_response_with_invoke_link_v2 import WebscriptResponseWithInvokeLinkV2
from .webscript_versions_response_v2 import WebscriptVersionsResponseV2
from .with_asset_hal_link import WithAssetHALLink
from .with_entity_attributes import WithEntityAttributes
from .with_limit import WithLimit
from .with_paging import WithPaging

__all__ = [
    "__version__",
    "ActiveEventData",
    "ActiveEventSSE",
    "ActiveEventSSEEvent",
    "AltVersionHALLink",
    "AnyFunctionResponse",
    "AnyJobForFunction",
    "AnyJobResult",
    "AnyJobStatus",
    "AnyJobStatusSummary",
    "ArchiveFormat",
    "AssetCondition",
    "AssetConditionContentType",
    "AssetConditionPattern",
    "AssetPathParamsV2",
    "AssetRole",
    "AssetSummary",
    "AssetSummaryWithHALLink",
    "AssetSummaryWithHALLinkLinks",
    "AssetsConditions",
    "AsyncDeployQuery",
    "AsyncDeployQueryV1",
    "AsyncQueryDefaultFalse",
    "AsyncQueryDefaultTrue",
    "AsyncVerifyQuery",
    "Batch",
    "BatchArgs",
    "BatchJobStatus",
    "BatchJobStatusType",
    "BatchResult",
    "Build",
    "Build1",
    "BuildArgs",
    "BuildJobStatus",
    "BuildResult",
    "BuildSpec",
    "BuildType",
    "CleanupResult",
    "CompiledRuntimeVersion",
    "CompletedEventData",
    "CompletedEventSSE",
    "CompletedEventSSEEvent",
    "ContentQueryV2",
    "ContentValidationListing",
    "CreateFunctionQueryV2",
    "CreateKFServingAsyncResponse",
    "CreatePlugAsyncResponse",
    "CreateWebscriptAsyncResponse",
    "DelayedEventData",
    "DelayedEventSSE",
    "DelayedEventSSEEvent",
    "Deploy",
    "Deploy1",
    "DeployArgs",
    "DeployArgsDeploySpecOverrides",
    "DeployAttributesFilter",
    "DeployJobStatus",
    "DeployResult",
    "DeploySpec",
    "DeploySpecOpenfaasSpec",
    "DeployType",
    "DeprecatePreviousPolicy",
    "DeprecatePreviousQuery",
    "DeprecatedDraftFilter",
    "Documentation",
    "DocumentationProperty",
    "DryRunQuery",
    "EntityResponse",
    "ErrorAndStatusResponse",
    "ErrorResponse",
    "EventAck",
    "EventClose",
    "EventKeepAlive",
    "EventSSE",
    "EventTypeSSE",
    "EventWithCloseSSE",
    "ExposedOpenfaasDeploySpec",
    "FailedEventData",
    "FailedEventSSE",
    "FailedEventSSEEvent",
    "FailureReason",
    "FileUpload",
    "ForceDeleteQueryV1",
    "FunctionDeleteQuery",
    "FunctionDeployOverrides",
    "FunctionDeployOverridesType",
    "FunctionEntityQuery",
    "FunctionJobArgs",
    "FunctionManifest",
    "FunctionMeta",
    "FunctionNameVersion",
    "FunctionRef",
    "FunctionSpec",
    "FunctionType",
    "FunctionVersionQuery",
    "GetContentParamsV2",
    "GetInvokableWebscriptQuery",
    "GetModelResponseV2",
    "GetPlugResponseV2",
    "GetPlugResponseV2Links",
    "GetPlugResponseV2LinksDraft",
    "GetPlugResponseV2LinksPublished",
    "GetRuntimeByNameAndVersionQuery",
    "GetRuntimeByNameQuery",
    "GetRuntimeExampleQuery",
    "GetRuntimeVersionsQuery",
    "GetWebscriptResponseV2",
    "GetWebscriptResponseV2Links",
    "HALLink",
    "InvokableWebscriptResponse",
    "InvokableWebscriptResponseEntity",
    "InvokableWebscriptResponseEntityWebscript",
    "InvokeHALLink",
    "InvokeInternalHALLink",
    "JobAndFunctionHALLink",
    "JobCause",
    "JobCauses",
    "JobEventPayloadActiveEventData",
    "JobEventPayloadCompletedEventData",
    "JobEventPayloadDelayedEventData",
    "JobEventPayloadFailedEventData",
    "JobEventPayloadWaitingChildrenEventData",
    "JobEventPayloadWaitingEventData",
    "JobEventResponseActiveEventData",
    "JobEventResponseCompletedEventData",
    "JobEventResponseDelayedEventData",
    "JobEventResponseFailedEventData",
    "JobEventResponseWaitingChildrenEventData",
    "JobEventResponseWaitingEventData",
    "JobEventSSE",
    "JobEventsAndFunctionHALLink",
    "JobEventsFilterQuery",
    "JobEventsHALLink",
    "JobHALLinks",
    "JobQuery",
    "JobReference",
    "JobReferenceParams",
    "JobResponse",
    "JobState",
    "JobStateActive",
    "JobStateCompleted",
    "JobStateDelayed",
    "JobStateFailed",
    "JobStateFinished",
    "JobStateResult",
    "JobStateUnknown",
    "JobStateWaiting",
    "JobStateWaitingChildren",
    "JobStatus",
    "JobStatusAndEntityHALLinks",
    "JobStatusHALLink",
    "JobStatusProgress",
    "JobSubmittedResponse",
    "JobType",
    "JobTypeBatch",
    "JobTypeBuild",
    "JobTypeDeploy",
    "JobTypeScale",
    "JobTypeSchema",
    "JobTypeUndeploy",
    "JobTypeVerify",
    "JobsForModelResponseV2",
    "JobsForModelResponseV2Links",
    "JobsForPlugResponseV2",
    "JobsForPlugResponseV2Links",
    "JobsForWebscriptResponseV2",
    "JobsForWebscriptResponseV2Links",
    "JobsHALLink",
    "JobsResponse",
    "KFServingDeleteMultipleResponse",
    "KFServingDeleteMultipleWithJobResponse",
    "KFServingDeleteQueryV1",
    "KFServingDeleteQueryV2",
    "KFServingDeleteResponse",
    "KFServingDeleteWithJobResponse",
    "KFServingLatestVersionQueryV2",
    "KFServingLatestVersionsQueryV1",
    "KFServingLatestVersionsQueryV2",
    "KFServingManifest",
    "KFServingModelsResponse",
    "KFServingResponse",
    "KFServingVersionsQueryV1",
    "KeepAliveEventSSE",
    "KfservingResponseV2",
    "LanguageRelease",
    "LatestFunctionVersionsQuery",
    "LatestFunctionsQuery",
    "LatestModelsResponseV2",
    "LatestModelsResponseV2EntitiesInner",
    "LatestPlugQuery",
    "LatestPlugVersionQueryV2",
    "LatestPlugVersionsQuery",
    "LatestPlugVersionsQueryV2",
    "LatestPlugsQuery",
    "LatestPlugsResponseV2",
    "LatestPlugsResponseV2EntitiesInner",
    "LatestVersionLevel",
    "LatestWebscriptsResponseV2",
    "LatestWebscriptsResponseV2EntitiesInner",
    "LegacyConfigurationObject",
    "LegacyConfigurationObjectFormat",
    "LegacyConfigurationResponseObject",
    "LegacyCreateDebugResponse",
    "LegacyDebugPlugManifest",
    "LegacyDebugPlugRequest",
    "LegacyDocumentation",
    "LegacyDocumentationRequest",
    "LegacyFunctionMeta",
    "LegacyPlugCreateQuery",
    "LegacyPlugCreateRequest",
    "LegacyPlugCreateResponse",
    "LegacyPlugMetaRequest",
    "LegacyPlugQuery",
    "LegacyPlugRequest",
    "LegacyPlugRequestMetadata",
    "LegacyPlugRequestMetadataDocumentation",
    "LegacyPlugRequestMetadataDocumentationAnyOf",
    "LegacyPlugRequestMetadataRawDataInner",
    "LegacyPlugResponse",
    "LegacyPlugResponseMetadata",
    "LegacyPlugScriptMeta",
    "LegacyPlugScriptMetaRawDataInner",
    "LegacyPlugScriptResponse",
    "LegacyRequiredPropertiesInner",
    "LegacyRequiredPropertyObject",
    "LimitQuery",
    "MediaType",
    "MessageAndStatusResponse",
    "MessageResponse",
    "Model",
    "Model1",
    "Model2",
    "ModelVersionsResponseV2",
    "MultipartFileUpload",
    "Name",
    "NameAndVersion",
    "NamedFunctionVersionsQuery",
    "NamedKFServingVersionsQueryV2",
    "NamedParametersTypeofAsJobReference",
    "NamedParametersTypeofAsJobReferenceJobStatus",
    "NamedParametersTypeofFromLegacy",
    "NamedParametersTypeofFromLegacyDocumentation",
    "NamedParametersTypeofIsNotLegacy",
    "NamedPlugVersionsQueryV2",
    "NamedVersionsFilter",
    "NamedWebscriptVersionsQueryV2",
    "OpenfaasDeployArgs",
    "OpenfaasFunctionRef",
    "Operation",
    "OperationStatus",
    "OperationStatusError",
    "PagingQuery",
    "PagingResponse",
    "ParentKeys",
    "PatchInterfaceQuery",
    "PatchMetadataQuery",
    "PatchPlugRequestV1",
    "Plug",
    "Plug1",
    "Plug2",
    "PlugDeleteForceQuery",
    "PlugDeleteQuery",
    "PlugInterface",
    "PlugListingAndQueryResponse",
    "PlugListingResponse",
    "PlugManifest",
    "PlugMeta",
    "PlugProperty",
    "PlugPropertyDataType",
    "PlugPropertyFormat",
    "PlugPropertyFormatType",
    "PlugResponse",
    "PlugResponseV2",
    "PlugType",
    "PlugTypeQuery",
    "PlugVersionsResponseV2",
    "PostModelJobAsyncResponseV2",
    "PostModelJobSyncResponseV2",
    "PostPlugJobAsyncResponseV2",
    "PostPlugJobSyncResponseV2",
    "PostWebscriptJobAsyncResponseV2",
    "PostWebscriptJobSyncResponseV2",
    "ProvidedDependency",
    "PublishFunctionQuery",
    "QueueEvents",
    "RebuildComputedResponse",
    "RebuildModelAsyncResponseV2",
    "RebuildModelSyncResponseV2",
    "RebuildPlugAsyncResponseV2",
    "RebuildPlugSyncResponseV2",
    "RebuildPolicy",
    "RebuildQueryParams",
    "RebuildQueryV2",
    "RebuildSubmittedResponse",
    "RebuildWebscriptAsyncResponseV2",
    "RebuildWebscriptSyncResponseV2",
    "RemoveFunctionQueryV2",
    "RemovePlugQueryV2",
    "RequestOperation",
    "ResourceLimits",
    "RootPageResponse",
    "RuntimeAttributes",
    "RuntimeInfo",
    "RuntimeNameQuery",
    "RuntimeParams",
    "RuntimeQuery",
    "RuntimeReference",
    "RuntimeSpecification",
    "RuntimeSummary",
    "RuntimeSummaryAttrs",
    "RuntimeSummaryResponse",
    "RuntimeVersionAndPathParams",
    "RuntimeVersionInfo",
    "RuntimeVersionParams",
    "RuntimeVersionQuery",
    "RuntimeVersionResponse",
    "RuntimeVersionSpecification",
    "RuntimeVersionStatus",
    "RuntimeVersionSummary",
    "Scale",
    "Scale1",
    "ScaleArgs",
    "ScaleJobStatus",
    "ScaleType",
    "SchemaByIdParams",
    "SchemaParams",
    "SemanticVersionRange",
    "Status",
    "StatusAny",
    "StatusFilter",
    "StatusInclude",
    "StatusResponse",
    "StreamClosing",
    "StreamReady",
    "SupportedEvents",
    "Tag",
    "TagQuery",
    "TagsFilter",
    "TagsQuery",
    "TimestampAbsolute",
    "TimestampAge",
    "TimestampSpec",
    "Undeploy",
    "Undeploy1",
    "UndeployArgs",
    "UndeployJobStatus",
    "UndeployResult",
    "UndeploySubmittedResponseV2",
    "UndeployType",
    "UndeployedResponseV2",
    "UnhealthyInvokableWebscriptError",
    "UpdateComment",
    "UpdateDraftQuery",
    "UpdateMetadataRequestV1",
    "UpdateMetadataRequestV2",
    "UpdateRecord",
    "UserPlugMeta",
    "Verify",
    "Verify1",
    "VerifyArgs",
    "VerifyJobStatus",
    "VerifyModelSyncResponseV2",
    "VerifyPlugSyncResponseV2",
    "VerifyQueryV1",
    "VerifyResult",
    "VerifyType",
    "VerifyWebscriptSyncResponseV2",
    "VersionIncludes",
    "VersionsQuery",
    "VersionsQueryV2",
    "VersionsResponseV2",
    "WaitingChildrenEventSSE",
    "WaitingChildrenEventSSEEvent",
    "WaitingEventData",
    "WaitingEventSSE",
    "WaitingEventSSEEvent",
    "Webscript",
    "Webscript1",
    "Webscript2",
    "WebscriptLatestVersionQueryV2",
    "WebscriptLatestVersionsQueryV1",
    "WebscriptLatestVersionsQueryV2",
    "WebscriptManifest",
    "WebscriptResponse",
    "WebscriptResponseV2",
    "WebscriptResponseWithInvokeLinkV2",
    "WebscriptVersionsResponseV2",
    "WithAssetHALLink",
    "WithEntityAttributes",
    "WithLimit",
    "WithPaging",
]
