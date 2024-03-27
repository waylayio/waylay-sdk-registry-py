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
    StrictBytes,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class MultipartFileUpload(WaylayBaseModel):
    """A multi-part upload containing one or more file assets.."""

    filename: List[StrictBytes | StrictStr] | None = None

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )