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
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.job_causes import JobCauses
from ..models.job_hal_links import JobHALLinks


class RebuildSubmittedResponse(WaylayBaseModel):
    """Rebuild Initiated."""

    message: StrictStr
    links: JobHALLinks = Field(alias="_links")
    causes: JobCauses

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
