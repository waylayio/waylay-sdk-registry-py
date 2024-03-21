# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
import pprint
import re  # noqa: F401
import json
from pydantic import ConfigDict, SerializationInfo, model_serializer, StrictStr
from pydantic_core import from_json
from typing import Callable, Union
from typing import cast
from typing_extensions import (
    Self,  # >=3.11
)

from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field


class ProvidedDependency(BaseModel):
    """Library dependency that is provided by this runtime.."""

    name: StrictStr = Field(description="Name of a provided dependency.")
    title: StrictStr | None = Field(default=None, description="Optional display title.")
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
    globals: List[StrictStr] | None = Field(
        default=None,
        description="Global variables that expose this library to the user code. As the usage of these globals is deprecated, any usage of such global will pose issues in an next runtime version.",
    )
    native: StrictBool | None = Field(
        default=None,
        description="If true, the library is provided natively by the runtime: e.g. node for javascript.",
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )

    @model_serializer(mode="wrap")
    def serializer(
        self, handler: Callable, info: SerializationInfo
    ) -> Dict[StrictStr, Any]:
        """The default serializer of the model.

        * Excludes `None` fields that were not set at model initialization.
        """
        model_dict = handler(self, info)
        return {
            k: v
            for k, v in model_dict.items()
            if v is not None or k in self.model_fields_set
        }

    def to_dict(self) -> dict[str, Any]:
        """Convert the ProvidedDependency instance to dict."""
        return self.model_dump(by_alias=True, exclude_unset=True, exclude_none=True)

    def to_json(self) -> str:
        """Convert the ProvidedDependency instance to a JSON-encoded string."""
        return self.model_dump_json(
            by_alias=True, exclude_unset=True, exclude_none=True
        )

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create a ProvidedDependency instance from a dict."""
        return cls.model_validate(obj)

    @classmethod
    def from_json(cls, json_data: str | bytes | bytearray) -> Self:
        """Create a ProvidedDependency instance from a JSON-encoded string."""
        return cls.model_validate_json(json_data)