"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictFloat,
    StrictInt,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class RegistryErrorResponse(WaylayBaseModel):
    """RegistryErrorResponse."""

    error: StrictStr
    code: StrictStr
    status_code: StrictFloat | StrictInt = Field(alias="statusCode")
    data: dict[str, StrictStr] | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
