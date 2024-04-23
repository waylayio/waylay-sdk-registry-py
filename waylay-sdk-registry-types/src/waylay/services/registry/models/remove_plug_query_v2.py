# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictBool,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class RemovePlugQueryV2(WaylayBaseModel):
    """RemovePlugQueryV2."""

    comment: StrictStr | None = Field(
        default=None,
        description="An optional user-specified comment corresponding to the operation.",
    )
    var_async: StrictBool | None = Field(
        default=True,
        description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs.",
        alias="async",
    )
    force: StrictBool | None = Field(
        default=None,
        description="If <code>true</code>, the plug version(s) will be undeployed and removed. Otherwise, the plug version(s) will only be <code>deprecated</code>, i.e removed from regular listings.",
    )
    undeploy: StrictBool | None = Field(
        default=None,
        description="If `true`, the `DELETE` operation * undeploys the (openfaas) function for the plug: it becomes no longer available for invocation. * does NOT remove the plug from registry: it stays in an `undeployed` status.  All assets and definitions are retained, so the plug can be restored later with a  _rebuild_ action.  If `false`, the `DELETE` operation * _only_ marks the plug version(s) as _deprecated_: the plug remains active but is removed from the default listings.   This also applies to _draft_ versions.  This parameter is incompatible with `force=true`.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only.",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
