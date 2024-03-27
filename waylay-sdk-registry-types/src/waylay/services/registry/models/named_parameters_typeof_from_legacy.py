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

from ..models.legacy_plug_meta_request import LegacyPlugMetaRequest
from ..models.plug_interface import PlugInterface


class NamedParametersTypeofFromLegacy(WaylayBaseModel):
    """NamedParametersTypeofFromLegacy."""

    metadata: LegacyPlugMetaRequest
    current_interface: PlugInterface | None = Field(
        default=None, alias="currentInterface"
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )
