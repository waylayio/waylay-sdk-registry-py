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

from ..models.asset_condition import AssetCondition


class AssetsConditions(WaylayBaseModel):
    """Describes the assets that are required/allowed/supported for a function.."""

    conditions: List[AssetCondition] | None = Field(
        default=None,
        description="All files in a function archive are checked against these conditions. A file that is not matched is ignored.",
    )
    max_size: StrictStr | None = Field(
        default=None,
        description="The maximum size of the archive (in bytes, unless unit is provided)",
        alias="maxSize",
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )
