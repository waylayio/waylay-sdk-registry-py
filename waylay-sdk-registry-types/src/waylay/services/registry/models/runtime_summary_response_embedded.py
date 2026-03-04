"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.runtime_tag import RuntimeTag


class RuntimeSummaryResponseEmbedded(WaylayBaseModel):
    """Embedded representations of the referenced tags.."""

    tags: list[RuntimeTag] | None = Field(
        default=None, description="Record of <tag key, tag representation> pairs."
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
