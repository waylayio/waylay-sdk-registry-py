# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    StrictBool,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.invokable_webscript_response_entity_webscript import (
    InvokableWebscriptResponseEntityWebscript,
)
from ..models.status import Status


class InvokableWebscriptResponseEntity(WaylayBaseModel):
    """InvokableWebscriptResponseEntity."""

    status: Status
    draft: StrictBool
    webscript: InvokableWebscriptResponseEntityWebscript
    secret: StrictStr | None = None

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
