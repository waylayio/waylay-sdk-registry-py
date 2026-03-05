"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from pydantic import (
    ConfigDict,
    Field,
    StrictBool,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class ProvidedDependency(WaylayBaseModel):
    """Library dependency that is provided by this runtime.."""

    name: StrictStr = Field(description="Name of a provided dependency.")
    title: StrictStr | None = Field(
        default=None, description="Optional display title."
    )
    description: StrictStr | None = Field(
        default=None, description="Optional description."
    )
    version: StrictStr | None = Field(
        default=None, description="Versions specification of a provided dependency"
    )
    deprecated: StrictBool | None = Field(
        default=False,
        description="If true, this provided dependency is scheduled for removal (or incompatible upgrade) in a next runtime version.",
    )
    removed: StrictBool | None = Field(
        default=False,
        description="If true, this dependency has been removed from the runtime (version)",
    )
    globals: list[StrictStr] | None = Field(
        default=None,
        description="Global variables that expose this library to the user code. As the usage of these globals is deprecated, any usage of such global will pose issues in an next runtime version.",
    )
    native: StrictBool | None = Field(
        default=None,
        description="If true, the library is provided natively by the runtime: e.g. node for javascript.",
    )

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="allow"
    )
