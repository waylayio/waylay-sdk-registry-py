# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
import re  # noqa: F401
from pydantic import ConfigDict, SerializationInfo, model_serializer, StrictStr
from typing import Callable, Union
from typing_extensions import (
    Self,  # >=3.11
)

from typing import Any, Dict, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field


class TagQuery(BaseModel):
    """TagQuery."""

    name: Optional[StrictStr] = Field(
        default=None,
        description="If set, filters on the <code>name</code> of a tag. Supports <code>*</code> and <code>?</code> wildcards and is case-insensitive.",
    )
    color: Optional[StrictStr] = Field(
        default=None,
        description="If set, filters on the <code>color</code> of a tag. Uses an exact match.",
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
        """Convert the TagQuery instance to dict."""
        return self.model_dump(by_alias=True, exclude_unset=True, exclude_none=True)

    def to_json(self) -> str:
        """Convert the TagQuery instance to a JSON-encoded string."""
        return self.model_dump_json(
            by_alias=True, exclude_unset=True, exclude_none=True
        )

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create a TagQuery instance from a dict."""
        return cls.model_validate(obj)

    @classmethod
    def from_json(cls, json_data: Union[str, bytes, bytearray]) -> Self:
        """Create a TagQuery instance from a JSON-encoded string."""
        return cls.model_validate_json(json_data)
