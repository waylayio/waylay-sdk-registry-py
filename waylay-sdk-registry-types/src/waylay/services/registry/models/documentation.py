"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.documentation_example import DocumentationExample
from ..models.documentation_property import DocumentationProperty


class Documentation(WaylayBaseModel):
    """Documentation."""

    description: StrictStr | None = None
    states: list[DocumentationProperty] | None = Field(
        default=None, description="Documentation of the plug states."
    )
    input: list[DocumentationProperty] | None = Field(
        default=None, description="Documentation of the plug input parameters."
    )
    output: list[DocumentationProperty] | None = Field(
        default=None, description="Documentation of the plug response parameters."
    )
    examples: list[DocumentationExample] | None = Field(
        default=None, description="Example scenarios for testing the plug."
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
