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


class LanguageRelease(WaylayBaseModel):
    """Description of the language or framework release used by a runtime (version).."""

    name: StrictStr = Field(
        description="Short technical name of the language or framework used."
    )
    version: StrictStr = Field(
        description="Release version of the language or framework."
    )
    title: StrictStr = Field(description="Display title.")
    description: StrictStr | None = None

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )
