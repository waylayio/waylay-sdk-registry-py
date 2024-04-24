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

from ..models.archive_format import ArchiveFormat
from ..models.function_type import FunctionType
from ..models.runtime_version_info import RuntimeVersionInfo


class RuntimeSummary(WaylayBaseModel):
    """A summary representation of the runtime, and (selected) versions of it.."""

    name: StrictStr
    title: StrictStr
    description: StrictStr | None = None
    function_type: FunctionType = Field(alias="functionType")
    archive_format: ArchiveFormat = Field(alias="archiveFormat")
    versions: List[RuntimeVersionInfo]

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
