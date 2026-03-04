"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

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

from ..models.resource_limits import ResourceLimits


class DeploySpecOpenfaasSpec(WaylayBaseModel):
    """If specified, it overrides the properties in `default`. Non-specified properties are taken from `default`."""

    service: StrictStr | None = None
    image: StrictStr | None = None
    namespace: StrictStr | None = None
    network: StrictStr | None = None
    env_vars: dict[str, StrictStr] | None = Field(default=None, alias="envVars")
    constraints: list[StrictStr] | None = None
    labels: dict[str, StrictStr] | None = None
    annotations: dict[str, StrictStr] | None = None
    secrets: list[StrictStr] | None = None
    registry_auth: StrictStr | None = Field(default=None, alias="registryAuth")
    limits: ResourceLimits | None = None
    requests: ResourceLimits | None = None
    read_only_root_filesystem: StrictBool | None = Field(
        default=None, alias="readOnlyRootFilesystem"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
