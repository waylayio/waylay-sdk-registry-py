# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
)

from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.runtime_tag import RuntimeTag


class RuntimeTagResponse(WaylayBaseModel):
    """Runtime Tag Found."""

    tag: RuntimeTag

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )