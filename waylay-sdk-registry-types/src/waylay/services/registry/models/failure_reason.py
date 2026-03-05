"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class FailureReason(WaylayBaseModel):
    """FailureReason."""

    log: list[StrictStr] = Field(description="Log lines associated with this failure.")
    events: list[StrictStr] = Field(description="Events associated with this failure.")
    cause: StrictStr | None = Field(
        default=None, description="Main cause for the failure."
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
