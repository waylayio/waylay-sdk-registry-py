"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Any

from pydantic import (
    ConfigDict,
    Field,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.plug_property_format_type import PlugPropertyFormatType


class PlugPropertyFormat(WaylayBaseModel):
    """PlugPropertyFormat."""

    type: PlugPropertyFormatType
    values: list[Any] | None = Field(
        default=None,
        description='The enumerated value domain when <code>type="enum"</code>',
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
