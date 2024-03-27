# coding: utf-8
"""Waylay Function Registry query parameters.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from __future__ import annotations  # for Python 3.7–3.9

from typing import Any, List

from pydantic import (
    ConfigDict,
    Field,
    StrictBool,
    StrictStr,
)
from typing_extensions import (
    Annotated,  # >=3.11
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.archive_format import ArchiveFormat
from ..models.deprecate_previous_policy import DeprecatePreviousPolicy
from ..models.function_type import FunctionType
from ..models.job_state_result import JobStateResult
from ..models.job_type_schema import JobTypeSchema
from ..models.rebuild_policy import RebuildPolicy
from ..models.status_filter import StatusFilter


def _create_query_alias_for(field_name: str) -> str:
    if field_name == "deprecate_previous":
        return "deprecatePrevious"
    if field_name == "dry_run":
        return "dryRun"
    if field_name == "var_async":
        return "async"
    if field_name == "scale_to_zero":
        return "scaleToZero"
    if field_name == "version":
        return "version"
    if field_name == "name":
        return "name"
    if field_name == "draft":
        return "draft"
    return field_name


class CreateQuery(WaylayBaseModel):
    """Model for `create` query parameters."""

    deprecate_previous: Annotated[
        DeprecatePreviousPolicy | None,
        Field(
            description="Set the cleanup policy used to automatically deprecate/delete previous versions."
        ),
    ] = None
    dry_run: Annotated[
        StrictBool | None,
        Field(
            description="If set to <code>true</code>, validates the deployment conditions, but does not change anything."
        ),
    ] = None
    var_async: Annotated[
        StrictBool | None,
        Field(
            description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs."
        ),
    ] = None
    scale_to_zero: Annotated[
        StrictBool | None,
        Field(
            description="If set to <code>true</code>, after successful deployment, the deployed function will be scaled to zero. Saves computing resources when the function is not to be used immediately."
        ),
    ] = None
    version: Annotated[
        Any | None,
        Field(
            description="If set, the function version will be an increment of the latest existing version that satisfies the `version` range. Note that this increment always takes precedence over an explicit `version` in the function manifest."
        ),
    ] = None
    name: Annotated[
        StrictStr | None,
        Field(
            description="If set, the value will be used as the function name instead of the one specified in the manifest."
        ),
    ] = None
    draft: Annotated[
        StrictBool | None,
        Field(
            description="If set, the created function will be a draft function and its assets are still mutable. A build and deploy is initiated only in the case when all necessary assets are present and valid."
        ),
    ] = None

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
        alias_generator=_create_query_alias_for,
        populate_by_name=True,
    )


def _delete_asset_query_alias_for(field_name: str) -> str:
    if field_name == "comment":
        return "comment"
    if field_name == "var_async":
        return "async"
    if field_name == "chown":
        return "chown"
    return field_name


class DeleteAssetQuery(WaylayBaseModel):
    """Model for `delete_asset` query parameters."""

    chown: Annotated[
        StrictBool,
        Field(
            description="If set, ownership of the draft function is transferred to the current user."
        ),
    ]
    comment: Annotated[
        StrictStr | None,
        Field(
            description="An optional user-specified comment corresponding to the operation."
        ),
    ] = None
    var_async: Annotated[
        StrictBool | None,
        Field(
            description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs."
        ),
    ] = None

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
        alias_generator=_delete_asset_query_alias_for,
        populate_by_name=True,
    )


def _get_archive_query_alias_for(field_name: str) -> str:
    if field_name == "ls":
        return "ls"
    return field_name


class GetArchiveQuery(WaylayBaseModel):
    """Model for `get_archive` query parameters."""

    ls: Annotated[
        StrictBool | None,
        Field(
            description="If set to `true`, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime."
        ),
    ] = None

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
        alias_generator=_get_archive_query_alias_for,
        populate_by_name=True,
    )


def _get_asset_query_alias_for(field_name: str) -> str:
    if field_name == "ls":
        return "ls"
    return field_name


class GetAssetQuery(WaylayBaseModel):
    """Model for `get_asset` query parameters."""

    ls: Annotated[
        StrictBool | None,
        Field(
            description="If set to `true`, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime."
        ),
    ] = None

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
        alias_generator=_get_asset_query_alias_for,
        populate_by_name=True,
    )


def _get_latest_query_alias_for(field_name: str) -> str:
    if field_name == "include_draft":
        return "includeDraft"
    if field_name == "include_deprecated":
        return "includeDeprecated"
    return field_name


class GetLatestQuery(WaylayBaseModel):
    """Model for `get_latest` query parameters."""

    include_draft: Annotated[
        StrictBool | None,
        Field(
            description="Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**."
        ),
    ] = None
    include_deprecated: Annotated[
        StrictBool | None,
        Field(
            description="Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**."
        ),
    ] = None

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
        alias_generator=_get_latest_query_alias_for,
        populate_by_name=True,
    )


def _get_query_alias_for(field_name: str) -> str:
    return field_name


class GetQuery(WaylayBaseModel):
    """Model for `get` query parameters."""

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
        alias_generator=_get_query_alias_for,
        populate_by_name=True,
    )


def _jobs_query_alias_for(field_name: str) -> str:
    if field_name == "limit":
        return "limit"
    if field_name == "type":
        return "type"
    if field_name == "state":
        return "state"
    if field_name == "function_type":
        return "functionType"
    if field_name == "created_before":
        return "createdBefore"
    if field_name == "created_after":
        return "createdAfter"
    return field_name


class JobsQuery(WaylayBaseModel):
    """Model for `jobs` query parameters."""

    limit: Annotated[
        Annotated[float, Field(strict=True, ge=0)]
        | Annotated[int, Field(strict=True, ge=0)]
        | None,
        Field(
            description="The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
        ),
    ] = None
    type: Annotated[
        List[JobTypeSchema] | None, Field(description="Filter on job type")
    ] = None
    state: Annotated[
        List[JobStateResult] | None, Field(description="Filter on job state")
    ] = None
    function_type: Annotated[
        List[FunctionType] | None, Field(description="Filter on function type")
    ] = None
    created_before: Annotated[
        Any | None,
        Field(
            description="Filter on jobs that created before the given timestamp or age"
        ),
    ] = None
    created_after: Annotated[
        Any | None,
        Field(
            description="Filter on jobs that created after the given timestamp or age"
        ),
    ] = None

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
        alias_generator=_jobs_query_alias_for,
        populate_by_name=True,
    )


def _list_versions_query_alias_for(field_name: str) -> str:
    if field_name == "limit":
        return "limit"
    if field_name == "page":
        return "page"
    if field_name == "deprecated":
        return "deprecated"
    if field_name == "draft":
        return "draft"
    if field_name == "version":
        return "version"
    if field_name == "status":
        return "status"
    if field_name == "runtime_version":
        return "runtimeVersion"
    if field_name == "created_by":
        return "createdBy"
    if field_name == "updated_by":
        return "updatedBy"
    if field_name == "created_before":
        return "createdBefore"
    if field_name == "created_after":
        return "createdAfter"
    if field_name == "updated_before":
        return "updatedBefore"
    if field_name == "updated_after":
        return "updatedAfter"
    if field_name == "archive_format":
        return "archiveFormat"
    if field_name == "runtime":
        return "runtime"
    return field_name


class ListVersionsQuery(WaylayBaseModel):
    """Model for `list_versions` query parameters."""

    limit: Annotated[
        Annotated[float, Field(strict=True, ge=0)]
        | Annotated[int, Field(strict=True, ge=0)]
        | None,
        Field(
            description="The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
        ),
    ] = None
    page: Annotated[
        Annotated[float, Field(strict=True, ge=0)]
        | Annotated[int, Field(strict=True, ge=0)]
        | None,
        Field(
            description="The number of pages to skip when returning result to this query."
        ),
    ] = None
    deprecated: Annotated[
        StrictBool | None,
        Field(description="Filter on the deprecation status of the function."),
    ] = None
    draft: Annotated[
        StrictBool | None,
        Field(description="Filter on the draft status of the function."),
    ] = None
    version: Annotated[
        StrictStr | None,
        Field(
            description="Filter on the version of the function (case-sensitive, supports wildcards)."
        ),
    ] = None
    status: Annotated[
        List[StatusFilter] | None,
        Field(
            description="Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions."
        ),
    ] = None
    runtime_version: Annotated[
        Any | None, Field(description="Filter on the runtime version.")
    ] = None
    created_by: Annotated[
        StrictStr | None,
        Field(
            description="Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs."
        ),
    ] = None
    updated_by: Annotated[
        StrictStr | None,
        Field(
            description="Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs."
        ),
    ] = None
    created_before: Annotated[
        Any | None,
        Field(
            description="Filter on funtions that were created before the given timestamp or age."
        ),
    ] = None
    created_after: Annotated[
        Any | None,
        Field(
            description="Filter on funtions that were created after the given timestamp or age."
        ),
    ] = None
    updated_before: Annotated[
        Any | None,
        Field(
            description="Filter on funtions that were updated before the given timestamp or age."
        ),
    ] = None
    updated_after: Annotated[
        Any | None,
        Field(
            description="Filter on funtions that were updated after the given timestamp or age."
        ),
    ] = None
    archive_format: Annotated[
        List[ArchiveFormat] | None,
        Field(description="Filter on the archive format of the function."),
    ] = None
    runtime: Annotated[
        List[StrictStr] | None,
        Field(description="Filter on the runtime of the function."),
    ] = None

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
        alias_generator=_list_versions_query_alias_for,
        populate_by_name=True,
    )


def _list_query_alias_for(field_name: str) -> str:
    if field_name == "limit":
        return "limit"
    if field_name == "page":
        return "page"
    if field_name == "include_draft":
        return "includeDraft"
    if field_name == "include_deprecated":
        return "includeDeprecated"
    if field_name == "deprecated":
        return "deprecated"
    if field_name == "draft":
        return "draft"
    if field_name == "name_version":
        return "nameVersion"
    if field_name == "version":
        return "version"
    if field_name == "status":
        return "status"
    if field_name == "runtime_version":
        return "runtimeVersion"
    if field_name == "created_by":
        return "createdBy"
    if field_name == "updated_by":
        return "updatedBy"
    if field_name == "created_before":
        return "createdBefore"
    if field_name == "created_after":
        return "createdAfter"
    if field_name == "updated_before":
        return "updatedBefore"
    if field_name == "updated_after":
        return "updatedAfter"
    if field_name == "name":
        return "name"
    if field_name == "archive_format":
        return "archiveFormat"
    if field_name == "runtime":
        return "runtime"
    if field_name == "latest":
        return "latest"
    return field_name


class ListQuery(WaylayBaseModel):
    """Model for `list` query parameters."""

    limit: Annotated[
        Annotated[float, Field(strict=True, ge=0)]
        | Annotated[int, Field(strict=True, ge=0)]
        | None,
        Field(
            description="The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
        ),
    ] = None
    page: Annotated[
        Annotated[float, Field(strict=True, ge=0)]
        | Annotated[int, Field(strict=True, ge=0)]
        | None,
        Field(
            description="The number of pages to skip when returning result to this query."
        ),
    ] = None
    include_draft: Annotated[
        StrictBool | None,
        Field(
            description="Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**."
        ),
    ] = None
    include_deprecated: Annotated[
        StrictBool | None,
        Field(
            description="Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**."
        ),
    ] = None
    deprecated: Annotated[
        StrictBool | None,
        Field(description="Filter on the deprecation status of the function."),
    ] = None
    draft: Annotated[
        StrictBool | None,
        Field(description="Filter on the draft status of the function."),
    ] = None
    name_version: Annotated[
        List[Annotated[str, Field(strict=True)]] | None,
        Field(
            description="Filter on exact `{name}@{version}` functions. Using this filter implies a `latest=false` default, returning multiple versions of the same named versions if they are filtered."
        ),
    ] = None
    version: Annotated[
        StrictStr | None,
        Field(
            description="Filter on the version of the function (case-sensitive, supports wildcards)."
        ),
    ] = None
    status: Annotated[
        List[StatusFilter] | None,
        Field(
            description="Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions."
        ),
    ] = None
    runtime_version: Annotated[
        Any | None, Field(description="Filter on the runtime version.")
    ] = None
    created_by: Annotated[
        StrictStr | None,
        Field(
            description="Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs."
        ),
    ] = None
    updated_by: Annotated[
        StrictStr | None,
        Field(
            description="Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs."
        ),
    ] = None
    created_before: Annotated[
        Any | None,
        Field(
            description="Filter on funtions that were created before the given timestamp or age."
        ),
    ] = None
    created_after: Annotated[
        Any | None,
        Field(
            description="Filter on funtions that were created after the given timestamp or age."
        ),
    ] = None
    updated_before: Annotated[
        Any | None,
        Field(
            description="Filter on funtions that were updated before the given timestamp or age."
        ),
    ] = None
    updated_after: Annotated[
        Any | None,
        Field(
            description="Filter on funtions that were updated after the given timestamp or age."
        ),
    ] = None
    name: Annotated[
        StrictStr | None,
        Field(
            description="Filter on the name of the function. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
        ),
    ] = None
    archive_format: Annotated[
        List[ArchiveFormat] | None,
        Field(description="Filter on the archive format of the function."),
    ] = None
    runtime: Annotated[
        List[StrictStr] | None,
        Field(description="Filter on the runtime of the function."),
    ] = None
    latest: Annotated[
        StrictBool | None,
        Field(
            description="When `true`, only the latest version per function name is returned. If set to `false`, multiple versions per named function can be returned. Defaults to `true`, except when specific versions are selected with the `nameVersion` filter."
        ),
    ] = None

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
        alias_generator=_list_query_alias_for,
        populate_by_name=True,
    )


def _patch_metadata_query_alias_for(field_name: str) -> str:
    if field_name == "comment":
        return "comment"
    return field_name


class PatchMetadataQuery(WaylayBaseModel):
    """Model for `patch_metadata` query parameters."""

    comment: Annotated[
        StrictStr | None,
        Field(
            description="An optional user-specified comment corresponding to the operation."
        ),
    ] = None

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
        alias_generator=_patch_metadata_query_alias_for,
        populate_by_name=True,
    )


def _publish_query_alias_for(field_name: str) -> str:
    if field_name == "comment":
        return "comment"
    if field_name == "deprecate_previous":
        return "deprecatePrevious"
    if field_name == "var_async":
        return "async"
    return field_name


class PublishQuery(WaylayBaseModel):
    """Model for `publish` query parameters."""

    comment: Annotated[
        StrictStr | None,
        Field(
            description="An optional user-specified comment corresponding to the operation."
        ),
    ] = None
    deprecate_previous: Annotated[
        DeprecatePreviousPolicy | None,
        Field(
            description="Set the cleanup policy used to automatically deprecate/delete previous versions."
        ),
    ] = None
    var_async: Annotated[
        StrictBool | None,
        Field(
            description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs."
        ),
    ] = None

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
        alias_generator=_publish_query_alias_for,
        populate_by_name=True,
    )


def _rebuild_query_alias_for(field_name: str) -> str:
    if field_name == "comment":
        return "comment"
    if field_name == "dry_run":
        return "dryRun"
    if field_name == "var_async":
        return "async"
    if field_name == "upgrade":
        return "upgrade"
    if field_name == "force_version":
        return "forceVersion"
    if field_name == "ignore_checks":
        return "ignoreChecks"
    if field_name == "scale_to_zero":
        return "scaleToZero"
    if field_name == "skip_rebuild":
        return "skipRebuild"
    return field_name


class RebuildQuery(WaylayBaseModel):
    """Model for `rebuild` query parameters."""

    comment: Annotated[
        StrictStr | None,
        Field(
            description="An optional user-specified comment corresponding to the operation."
        ),
    ] = None
    dry_run: Annotated[
        StrictBool | None,
        Field(
            description="If set to <code>true</code>, checks whether rebuild jobs are needed, but do not start any jobs."
        ),
    ] = None
    var_async: Annotated[
        StrictBool | None,
        Field(
            description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs."
        ),
    ] = None
    upgrade: Annotated[
        RebuildPolicy | None,
        Field(
            description="If set, force a rebuild with the given <em>runtime</em> version selection policy. <ul>  <li><code>same</code> <b>patch</b> version.   This should only include backward compatible upgrades.  </li>  <li><code>minor</code> <b>major</b> version.   This might include an upgrade of e.g. the language runtime and/or provided   dependencies that could break compatiblity with the function. .</li> </ul>"
        ),
    ] = None
    force_version: Annotated[
        Annotated[str, Field(strict=True)] | None,
        Field(
            description="If set, force a rebuild with the given runtime version (including downgrades). This parameter is mutually exclusive to the `upgrade` parameter."
        ),
    ] = None
    ignore_checks: Annotated[
        StrictBool | None,
        Field(
            description="If set to true, checks that normally prevent a rebuild are overriden. These checks include: * function state in `pending`, `running`, `failed` or `undeployed` * backoff period due to recent failures * usage of deprecated dependencies * running jobs on entity * the `dryRun` option"
        ),
    ] = None
    scale_to_zero: Annotated[
        StrictBool | None,
        Field(
            description="Indicates whether the function needs to be scaled down after successful (re-)deployment. If not set, the function is scaled to zero only if it was not active before this command."
        ),
    ] = None
    skip_rebuild: Annotated[
        StrictBool | None,
        Field(
            description="If set, the function will not be rebuild. Always uses the current runtime version when re-deploying/re-verifying the function."
        ),
    ] = None

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
        alias_generator=_rebuild_query_alias_for,
        populate_by_name=True,
    )


def _remove_version_query_alias_for(field_name: str) -> str:
    if field_name == "comment":
        return "comment"
    if field_name == "var_async":
        return "async"
    if field_name == "force":
        return "force"
    if field_name == "undeploy":
        return "undeploy"
    return field_name


class RemoveVersionQuery(WaylayBaseModel):
    """Model for `remove_version` query parameters."""

    comment: Annotated[
        StrictStr | None,
        Field(
            description="An optional user-specified comment corresponding to the operation."
        ),
    ] = None
    var_async: Annotated[
        StrictBool | None,
        Field(
            description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs."
        ),
    ] = None
    force: Annotated[
        StrictBool | None,
        Field(
            description="If <code>true</code>, the function version will be immediately undeployed and removed.  Otherwise, the removal will be delayed to allow current invocations to end. During that period, the function is marked _deprecated_."
        ),
    ] = None
    undeploy: Annotated[
        StrictBool | None,
        Field(
            description="If `true`, the `DELETE` operation * undeploys the (openfaas) function: it becomes no longer available for invocation. * does NOT remove the function from registry: it stays in an `undeployed` status.  All assets and definitions are retained, so the version can be restored later with a  _rebuild_ action.  If `false`, the `DELETE` operation * _only_ marks the plug function as _deprecated_, the function remains active but is removed from the default listings.   This also applies to _draft_ versions.  This parameter is incompatible with `force=true`.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only."
        ),
    ] = None

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
        alias_generator=_remove_version_query_alias_for,
        populate_by_name=True,
    )


def _remove_versions_query_alias_for(field_name: str) -> str:
    if field_name == "comment":
        return "comment"
    if field_name == "var_async":
        return "async"
    if field_name == "force":
        return "force"
    if field_name == "undeploy":
        return "undeploy"
    return field_name


class RemoveVersionsQuery(WaylayBaseModel):
    """Model for `remove_versions` query parameters."""

    comment: Annotated[
        StrictStr | None,
        Field(
            description="An optional user-specified comment corresponding to the operation."
        ),
    ] = None
    var_async: Annotated[
        StrictBool | None,
        Field(
            description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs."
        ),
    ] = None
    force: Annotated[
        StrictBool | None,
        Field(
            description="If <code>true</code>, the function version will be immediately undeployed and removed.  Otherwise, the removal will be delayed to allow current invocations to end. During that period, the function is marked _deprecated_."
        ),
    ] = None
    undeploy: Annotated[
        StrictBool | None,
        Field(
            description="If `true`, the `DELETE` operation * undeploys the (openfaas) function: it becomes no longer available for invocation. * does NOT remove the function from registry: it stays in an `undeployed` status.  All assets and definitions are retained, so the version can be restored later with a  _rebuild_ action.  If `false`, the `DELETE` operation * _only_ marks the plug function as _deprecated_, the function remains active but is removed from the default listings.   This also applies to _draft_ versions.  This parameter is incompatible with `force=true`.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only."
        ),
    ] = None

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
        alias_generator=_remove_versions_query_alias_for,
        populate_by_name=True,
    )


def _update_asset_query_alias_for(field_name: str) -> str:
    if field_name == "comment":
        return "comment"
    if field_name == "var_async":
        return "async"
    if field_name == "chown":
        return "chown"
    return field_name


class UpdateAssetQuery(WaylayBaseModel):
    """Model for `update_asset` query parameters."""

    chown: Annotated[
        StrictBool,
        Field(
            description="If set, ownership of the draft function is transferred to the current user."
        ),
    ]
    comment: Annotated[
        StrictStr | None,
        Field(
            description="An optional user-specified comment corresponding to the operation."
        ),
    ] = None
    var_async: Annotated[
        StrictBool | None,
        Field(
            description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs."
        ),
    ] = None

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
        alias_generator=_update_asset_query_alias_for,
        populate_by_name=True,
    )


def _update_assets_query_alias_for(field_name: str) -> str:
    if field_name == "comment":
        return "comment"
    if field_name == "var_async":
        return "async"
    if field_name == "chown":
        return "chown"
    return field_name


class UpdateAssetsQuery(WaylayBaseModel):
    """Model for `update_assets` query parameters."""

    chown: Annotated[
        StrictBool,
        Field(
            description="If set, ownership of the draft function is transferred to the current user."
        ),
    ]
    comment: Annotated[
        StrictStr | None,
        Field(
            description="An optional user-specified comment corresponding to the operation."
        ),
    ] = None
    var_async: Annotated[
        StrictBool | None,
        Field(
            description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs."
        ),
    ] = None

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
        alias_generator=_update_assets_query_alias_for,
        populate_by_name=True,
    )


def _verify_query_alias_for(field_name: str) -> str:
    if field_name == "comment":
        return "comment"
    if field_name == "var_async":
        return "async"
    if field_name == "scale_to_zero":
        return "scaleToZero"
    return field_name


class VerifyQuery(WaylayBaseModel):
    """Model for `verify` query parameters."""

    comment: Annotated[
        StrictStr | None,
        Field(
            description="An optional user-specified comment corresponding to the operation."
        ),
    ] = None
    var_async: Annotated[
        StrictBool | None,
        Field(
            description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs."
        ),
    ] = None
    scale_to_zero: Annotated[
        StrictBool | None,
        Field(
            description="Indicates whether the function needs to be scaled down after successful verification. If not set, the function is scaled to zero only if it was not active before this command."
        ),
    ] = None

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
        alias_generator=_verify_query_alias_for,
        populate_by_name=True,
    )
