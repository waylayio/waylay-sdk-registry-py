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

from ..models.kfserving_response_v2 import KfservingResponseV2
from ..models.verify_result import VerifyResult


class VerifyModelSyncResponseV2(WaylayBaseModel):
    """Model Health Verified."""

    message: StrictStr
    entity: KfservingResponseV2
    result: VerifyResult

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )
