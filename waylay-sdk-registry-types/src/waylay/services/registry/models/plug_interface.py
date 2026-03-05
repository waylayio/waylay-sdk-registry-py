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

from ..models.plug_property import PlugProperty


class PlugInterface(WaylayBaseModel):
    """PlugInterface."""

    states: list[StrictStr] | None = Field(
        default=None,
        description="The states of a plug as implemented in the plug code. Required and supported for `type=sensor` plugs _only_.",
    )
    input: list[PlugProperty] | None = Field(
        default=None,
        description="The named input parameters of a plug. Supported for `type=sensor` plugs; fixed with input attributes `data` and `resource` for `type=transformer`plugs.",
    )
    output: list[PlugProperty] | None = Field(
        default=None,
        description="The named output parameters of a plug. Supported for all plug types.",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
