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
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.get_plug_response_v2_embedded import GetPlugResponseV2Embedded
from ..models.get_plug_response_v2_links import GetPlugResponseV2Links
from ..models.plug_with_invocation_response_v2 import PlugWithInvocationResponseV2


class GetPlugResponseV2(WaylayBaseModel):
    """Plug Found."""

    embedded: GetPlugResponseV2Embedded | None = Field(default=None, alias="_embedded")
    entity: PlugWithInvocationResponseV2
    links: GetPlugResponseV2Links = Field(alias="_links")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
