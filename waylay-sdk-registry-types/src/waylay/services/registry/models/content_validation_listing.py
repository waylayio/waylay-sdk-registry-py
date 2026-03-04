"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.asset_summary_with_hal_link import AssetSummaryWithHALLink


class ContentValidationListing(WaylayBaseModel):
    """Content listing."""

    assets: list[AssetSummaryWithHALLink]

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
