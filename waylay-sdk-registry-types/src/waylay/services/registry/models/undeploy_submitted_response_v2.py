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
from typing_extensions import (
    Annotated,  # >=3.11
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.job_hal_links import JobHALLinks


class UndeploySubmittedResponseV2(WaylayBaseModel):
    """Undeployment Initiated."""

    message: StrictStr
    links: JobHALLinks = Field(alias="_links")
    versions: List[Annotated[str, Field(strict=True)]] = Field(
        description="The versions for which undeployment and/or removal is initiated."
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )
