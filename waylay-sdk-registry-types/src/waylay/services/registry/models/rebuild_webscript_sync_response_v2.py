# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    StrictStr,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.job_causes import JobCauses
from ..models.webscript_response_v2 import WebscriptResponseV2


class RebuildWebscriptSyncResponseV2(WaylayBaseModel):
    """Webscript Rebuild Ignored."""

    message: StrictStr
    causes: JobCauses
    entity: WebscriptResponseV2

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
