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

from ..models.tag_or_tag_reference import TagOrTagReference


class UpdateTagsRequestV2(WaylayBaseModel):
    """UpdateTagsRequestV2."""

    tags: list[TagOrTagReference] = Field(
        description="During update, a (reference to a) tag - that does not yet exist, is created (using default attributes if not specified) - that does exist is **not** updated (even if tag attributes like `color` differ)"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
