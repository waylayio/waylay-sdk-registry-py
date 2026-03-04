"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class ProtectByNameResponseV2(WaylayBaseModel):
    """Protection changed.."""

    message: StrictStr
    versions: list[Annotated[str, Field(strict=True)]] = Field(
        description="The versions that were protected or unprotected."
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
