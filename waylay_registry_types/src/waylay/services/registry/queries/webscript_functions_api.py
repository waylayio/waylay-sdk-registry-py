# coding: utf-8
"""Waylay Function Registry query parameters.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from __future__ import annotations  # for Python 3.7–3.9

from pydantic import Field, StrictStr
from typing import List, Optional, Union, Any
from typing_extensions import NotRequired, TypedDict

from pydantic import Field
from typing_extensions import Annotated
from pydantic import StrictBool, StrictStr

from typing import Any, List, Optional, Union

from ..models.archive_format import ArchiveFormat
from ..models.deprecate_previous_policy import DeprecatePreviousPolicy
from ..models.function_type import FunctionType
from ..models.job_state_result import JobStateResult
from ..models.job_type_schema import JobTypeSchema
from ..models.rebuild_policy import RebuildPolicy
from ..models.status_filter import StatusFilter


class CreateQuery(TypedDict):
    """create query parameters."""

    deprecate_previous: NotRequired[
        Annotated[
            Optional[DeprecatePreviousPolicy],
            Field(
                description="Set the cleanup policy used to automatically deprecate/delete previous versions."
            ),
        ]
    ]
    dry_run: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="If set to <code>true</code>, validates the deployment conditions, but does not change anything."
            ),
        ]
    ]
    var_async: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs."
            ),
        ]
    ]
    scale_to_zero: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="If set to <code>true</code>, after successful deployment, the deployed function will be scaled to zero. Saves computing resources when the function is not to be used immediately."
            ),
        ]
    ]
    version: NotRequired[
        Annotated[
            Optional[Any],
            Field(
                description="If set, the function version will be an increment of the latest existing version that satisfies the `version` range. Note that this increment always takes precedence over an explicit `version` in the function manifest."
            ),
        ]
    ]
    name: NotRequired[
        Annotated[
            Optional[StrictStr],
            Field(
                description="If set, the value will be used as the function name instead of the one specified in the manifest."
            ),
        ]
    ]
    draft: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="If set, the created function will be a draft function and its assets are still mutable. A build and deploy is initiated only in the case when all necessary assets are present and valid."
            ),
        ]
    ]


class DeleteAssetQuery(TypedDict):
    """delete_asset query parameters."""

    chown: Annotated[
        StrictBool,
        Field(
            description="If set, ownership of the draft function is transferred to the current user."
        ),
    ]
    comment: NotRequired[
        Annotated[
            Optional[StrictStr],
            Field(
                description="An optional user-specified comment corresponding to the operation."
            ),
        ]
    ]
    var_async: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs."
            ),
        ]
    ]


class GetArchiveQuery(TypedDict):
    """get_archive query parameters."""

    ls: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="If set to `true`, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime."
            ),
        ]
    ]


class GetAssetQuery(TypedDict):
    """get_asset query parameters."""

    ls: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="If set to `true`, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime."
            ),
        ]
    ]


class GetLatestQuery(TypedDict):
    """get_latest query parameters."""

    include_draft: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**."
            ),
        ]
    ]
    include_deprecated: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**."
            ),
        ]
    ]


class GetQuery(TypedDict):
    """get query parameters."""


class JobsQuery(TypedDict):
    """jobs query parameters."""

    limit: NotRequired[
        Annotated[
            Optional[
                Union[
                    Annotated[float, Field(strict=True, ge=0)],
                    Annotated[int, Field(strict=True, ge=0)],
                ]
            ],
            Field(
                description="The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
            ),
        ]
    ]
    type: NotRequired[
        Annotated[
            Optional[List[JobTypeSchema]], Field(description="Filter on job type")
        ]
    ]
    state: NotRequired[
        Annotated[
            Optional[List[JobStateResult]], Field(description="Filter on job state")
        ]
    ]
    function_type: NotRequired[
        Annotated[
            Optional[List[FunctionType]], Field(description="Filter on function type")
        ]
    ]
    created_before: NotRequired[
        Annotated[
            Optional[Any],
            Field(
                description="Filter on jobs that created before the given timestamp or age"
            ),
        ]
    ]
    created_after: NotRequired[
        Annotated[
            Optional[Any],
            Field(
                description="Filter on jobs that created after the given timestamp or age"
            ),
        ]
    ]


class ListVersionsQuery(TypedDict):
    """list_versions query parameters."""

    limit: NotRequired[
        Annotated[
            Optional[
                Union[
                    Annotated[float, Field(strict=True, ge=0)],
                    Annotated[int, Field(strict=True, ge=0)],
                ]
            ],
            Field(
                description="The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
            ),
        ]
    ]
    page: NotRequired[
        Annotated[
            Optional[
                Union[
                    Annotated[float, Field(strict=True, ge=0)],
                    Annotated[int, Field(strict=True, ge=0)],
                ]
            ],
            Field(
                description="The number of pages to skip when returning result to this query."
            ),
        ]
    ]
    deprecated: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(description="Filter on the deprecation status of the function."),
        ]
    ]
    draft: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(description="Filter on the draft status of the function."),
        ]
    ]
    version: NotRequired[
        Annotated[
            Optional[StrictStr],
            Field(
                description="Filter on the version of the function (case-sensitive, supports wildcards)."
            ),
        ]
    ]
    status: NotRequired[
        Annotated[
            Optional[List[StatusFilter]],
            Field(
                description="Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions."
            ),
        ]
    ]
    runtime_version: NotRequired[
        Annotated[Optional[Any], Field(description="Filter on the runtime version.")]
    ]
    created_by: NotRequired[
        Annotated[
            Optional[StrictStr],
            Field(
                description="Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs."
            ),
        ]
    ]
    updated_by: NotRequired[
        Annotated[
            Optional[StrictStr],
            Field(
                description="Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs."
            ),
        ]
    ]
    created_before: NotRequired[
        Annotated[
            Optional[Any],
            Field(
                description="Filter on funtions that were created before the given timestamp or age."
            ),
        ]
    ]
    created_after: NotRequired[
        Annotated[
            Optional[Any],
            Field(
                description="Filter on funtions that were created after the given timestamp or age."
            ),
        ]
    ]
    updated_before: NotRequired[
        Annotated[
            Optional[Any],
            Field(
                description="Filter on funtions that were updated before the given timestamp or age."
            ),
        ]
    ]
    updated_after: NotRequired[
        Annotated[
            Optional[Any],
            Field(
                description="Filter on funtions that were updated after the given timestamp or age."
            ),
        ]
    ]
    archive_format: NotRequired[
        Annotated[
            Optional[List[ArchiveFormat]],
            Field(description="Filter on the archive format of the function."),
        ]
    ]
    runtime: NotRequired[
        Annotated[
            Optional[List[StrictStr]],
            Field(description="Filter on the runtime of the function."),
        ]
    ]


class ListQuery(TypedDict):
    """list query parameters."""

    limit: NotRequired[
        Annotated[
            Optional[
                Union[
                    Annotated[float, Field(strict=True, ge=0)],
                    Annotated[int, Field(strict=True, ge=0)],
                ]
            ],
            Field(
                description="The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
            ),
        ]
    ]
    page: NotRequired[
        Annotated[
            Optional[
                Union[
                    Annotated[float, Field(strict=True, ge=0)],
                    Annotated[int, Field(strict=True, ge=0)],
                ]
            ],
            Field(
                description="The number of pages to skip when returning result to this query."
            ),
        ]
    ]
    include_draft: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**."
            ),
        ]
    ]
    include_deprecated: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**."
            ),
        ]
    ]
    deprecated: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(description="Filter on the deprecation status of the function."),
        ]
    ]
    draft: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(description="Filter on the draft status of the function."),
        ]
    ]
    name_version: NotRequired[
        Annotated[
            Optional[List[Annotated[str, Field(strict=True)]]],
            Field(
                description="Filter on exact `{name}@{version}` functions. Using this filter implies a `latest=false` default, returning multiple versions of the same named versions if they are filtered."
            ),
        ]
    ]
    version: NotRequired[
        Annotated[
            Optional[StrictStr],
            Field(
                description="Filter on the version of the function (case-sensitive, supports wildcards)."
            ),
        ]
    ]
    status: NotRequired[
        Annotated[
            Optional[List[StatusFilter]],
            Field(
                description="Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions."
            ),
        ]
    ]
    runtime_version: NotRequired[
        Annotated[Optional[Any], Field(description="Filter on the runtime version.")]
    ]
    created_by: NotRequired[
        Annotated[
            Optional[StrictStr],
            Field(
                description="Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs."
            ),
        ]
    ]
    updated_by: NotRequired[
        Annotated[
            Optional[StrictStr],
            Field(
                description="Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs."
            ),
        ]
    ]
    created_before: NotRequired[
        Annotated[
            Optional[Any],
            Field(
                description="Filter on funtions that were created before the given timestamp or age."
            ),
        ]
    ]
    created_after: NotRequired[
        Annotated[
            Optional[Any],
            Field(
                description="Filter on funtions that were created after the given timestamp or age."
            ),
        ]
    ]
    updated_before: NotRequired[
        Annotated[
            Optional[Any],
            Field(
                description="Filter on funtions that were updated before the given timestamp or age."
            ),
        ]
    ]
    updated_after: NotRequired[
        Annotated[
            Optional[Any],
            Field(
                description="Filter on funtions that were updated after the given timestamp or age."
            ),
        ]
    ]
    name: NotRequired[
        Annotated[
            Optional[StrictStr],
            Field(
                description="Filter on the name of the function. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
            ),
        ]
    ]
    archive_format: NotRequired[
        Annotated[
            Optional[List[ArchiveFormat]],
            Field(description="Filter on the archive format of the function."),
        ]
    ]
    runtime: NotRequired[
        Annotated[
            Optional[List[StrictStr]],
            Field(description="Filter on the runtime of the function."),
        ]
    ]
    latest: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="When `true`, only the latest version per function name is returned. If set to `false`, multiple versions per named function can be returned. Defaults to `true`, except when specific versions are selected with the `nameVersion` filter."
            ),
        ]
    ]


class PatchMetadataQuery(TypedDict):
    """patch_metadata query parameters."""

    comment: NotRequired[
        Annotated[
            Optional[StrictStr],
            Field(
                description="An optional user-specified comment corresponding to the operation."
            ),
        ]
    ]


class PublishQuery(TypedDict):
    """publish query parameters."""

    comment: NotRequired[
        Annotated[
            Optional[StrictStr],
            Field(
                description="An optional user-specified comment corresponding to the operation."
            ),
        ]
    ]
    deprecate_previous: NotRequired[
        Annotated[
            Optional[DeprecatePreviousPolicy],
            Field(
                description="Set the cleanup policy used to automatically deprecate/delete previous versions."
            ),
        ]
    ]
    var_async: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs."
            ),
        ]
    ]


class RebuildQuery(TypedDict):
    """rebuild query parameters."""

    comment: NotRequired[
        Annotated[
            Optional[StrictStr],
            Field(
                description="An optional user-specified comment corresponding to the operation."
            ),
        ]
    ]
    dry_run: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="If set to <code>true</code>, checks whether rebuild jobs are needed, but do not start any jobs."
            ),
        ]
    ]
    var_async: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs."
            ),
        ]
    ]
    upgrade: NotRequired[
        Annotated[
            Optional[RebuildPolicy],
            Field(
                description="If set, force a rebuild with the given <em>runtime</em> version selection policy. <ul>  <li><code>same</code> <b>patch</b> version.   This should only include backward compatible upgrades.  </li>  <li><code>minor</code> <b>major</b> version.   This might include an upgrade of e.g. the language runtime and/or provided   dependencies that could break compatiblity with the function. .</li> </ul>"
            ),
        ]
    ]
    force_version: NotRequired[
        Annotated[
            Optional[Annotated[str, Field(strict=True)]],
            Field(
                description="If set, force a rebuild with the given runtime version (including downgrades). This parameter is mutually exclusive to the `upgrade` parameter."
            ),
        ]
    ]
    ignore_checks: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="If set to true, checks that normally prevent a rebuild are overriden. These checks include: * function state in `pending`, `running`, `failed` or `undeployed` * backoff period due to recent failures * usage of deprecated dependencies * running jobs on entity * the `dryRun` option"
            ),
        ]
    ]
    scale_to_zero: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="Indicates whether the function needs to be scaled down after successful (re-)deployment. If not set, the function is scaled to zero only if it was not active before this command."
            ),
        ]
    ]
    skip_rebuild: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="If set, the function will not be rebuild. Always uses the current runtime version when re-deploying/re-verifying the function."
            ),
        ]
    ]


class RemoveVersionQuery(TypedDict):
    """remove_version query parameters."""

    comment: NotRequired[
        Annotated[
            Optional[StrictStr],
            Field(
                description="An optional user-specified comment corresponding to the operation."
            ),
        ]
    ]
    var_async: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs."
            ),
        ]
    ]
    force: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="If <code>true</code>, the function version will be immediately undeployed and removed.  Otherwise, the removal will be delayed to allow current invocations to end. During that period, the function is marked _deprecated_."
            ),
        ]
    ]
    undeploy: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="If `true`, the `DELETE` operation * undeploys the (openfaas) function: it becomes no longer available for invocation. * does NOT remove the function from registry: it stays in an `undeployed` status.  All assets and definitions are retained, so the version can be restored later with a  _rebuild_ action.  If `false`, the `DELETE` operation * _only_ marks the plug function as _deprecated_, the function remains active but is removed from the default listings.   This also applies to _draft_ versions.  This parameter is incompatible with `force=true`.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only."
            ),
        ]
    ]


class RemoveVersionsQuery(TypedDict):
    """remove_versions query parameters."""

    comment: NotRequired[
        Annotated[
            Optional[StrictStr],
            Field(
                description="An optional user-specified comment corresponding to the operation."
            ),
        ]
    ]
    var_async: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs."
            ),
        ]
    ]
    force: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="If <code>true</code>, the function version will be immediately undeployed and removed.  Otherwise, the removal will be delayed to allow current invocations to end. During that period, the function is marked _deprecated_."
            ),
        ]
    ]
    undeploy: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="If `true`, the `DELETE` operation * undeploys the (openfaas) function: it becomes no longer available for invocation. * does NOT remove the function from registry: it stays in an `undeployed` status.  All assets and definitions are retained, so the version can be restored later with a  _rebuild_ action.  If `false`, the `DELETE` operation * _only_ marks the plug function as _deprecated_, the function remains active but is removed from the default listings.   This also applies to _draft_ versions.  This parameter is incompatible with `force=true`.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only."
            ),
        ]
    ]


class UpdateAssetQuery(TypedDict):
    """update_asset query parameters."""

    chown: Annotated[
        StrictBool,
        Field(
            description="If set, ownership of the draft function is transferred to the current user."
        ),
    ]
    comment: NotRequired[
        Annotated[
            Optional[StrictStr],
            Field(
                description="An optional user-specified comment corresponding to the operation."
            ),
        ]
    ]
    var_async: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs."
            ),
        ]
    ]


class UpdateAssetsQuery(TypedDict):
    """update_assets query parameters."""

    chown: Annotated[
        StrictBool,
        Field(
            description="If set, ownership of the draft function is transferred to the current user."
        ),
    ]
    comment: NotRequired[
        Annotated[
            Optional[StrictStr],
            Field(
                description="An optional user-specified comment corresponding to the operation."
            ),
        ]
    ]
    var_async: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs."
            ),
        ]
    ]


class VerifyQuery(TypedDict):
    """verify query parameters."""

    comment: NotRequired[
        Annotated[
            Optional[StrictStr],
            Field(
                description="An optional user-specified comment corresponding to the operation."
            ),
        ]
    ]
    var_async: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs."
            ),
        ]
    ]
    scale_to_zero: NotRequired[
        Annotated[
            Optional[StrictBool],
            Field(
                description="Indicates whether the function needs to be scaled down after successful verification. If not set, the function is scaled to zero only if it was not active before this command."
            ),
        ]
    ]
