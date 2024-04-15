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

from ..models.alt_embedded_version_i_plug_response_v2 import (
    AltEmbeddedVersionIPlugResponseV2,
)


class WithEmbeddedAltVersionsIPlugResponseV2(WaylayBaseModel):
    """WithEmbeddedAltVersionsIPlugResponseV2."""

    embedded: AltEmbeddedVersionIPlugResponseV2 | None = Field(
        default=None, alias="_embedded"
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )