"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.resource_limits import ResourceLimits


class ExposedOpenfaasDeploySpec(WaylayBaseModel):
    """ExposedOpenfaasDeploySpec."""

    service: StrictStr
    image: StrictStr
    namespace: StrictStr
    labels: dict[str, StrictStr] | None = None
    annotations: dict[str, StrictStr] | None = None
    limits: ResourceLimits | None = None
    requests: ResourceLimits | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
