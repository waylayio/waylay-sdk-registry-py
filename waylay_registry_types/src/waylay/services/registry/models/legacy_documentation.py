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

from typing import Any, Dict, List
from pydantic import BaseModel
from pydantic import Field
from ..models.documentation_property import DocumentationProperty


class LegacyDocumentation(BaseModel):
    """LegacyDocumentation."""

    supported_states: List[DocumentationProperty] = Field(alias="supportedStates")
    configuration: List[DocumentationProperty]
    raw_data: List[DocumentationProperty] = Field(alias="rawData")

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
        """Convert the LegacyDocumentation instance to dict."""
        return self.model_dump(by_alias=True, exclude_unset=True, exclude_none=True)

    def to_json(self) -> str:
        """Convert the LegacyDocumentation instance to a JSON-encoded string."""
        return self.model_dump_json(
            by_alias=True, exclude_unset=True, exclude_none=True
        )

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create a LegacyDocumentation instance from a dict."""
        return cls.model_validate(obj)

    @classmethod
    def from_json(cls, json_data: Union[str, bytes, bytearray]) -> Self:
        """Create a LegacyDocumentation instance from a JSON-encoded string."""
        return cls.model_validate_json(json_data)
