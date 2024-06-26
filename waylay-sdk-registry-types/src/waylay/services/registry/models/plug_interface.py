# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import List

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.plug_property import PlugProperty


class PlugInterface(WaylayBaseModel):
    """PlugInterface."""

    states: List[StrictStr] | None = Field(
        default=None,
        description="The states of a plug as implemented in the plug code.",
    )
    input: List[PlugProperty] | None = Field(
        default=None, description="The named input parameters of a plug"
    )
    output: List[PlugProperty] | None = Field(
        default=None, description="The named output parameters of a plug"
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
