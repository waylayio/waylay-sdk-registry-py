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
from pydantic import ConfigDict
from typing_extensions import (
    Self,  # >=3.11
)

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, StrictBool
from pydantic import Field
from ..models.archive_format import ArchiveFormat
from ..models.function_type import FunctionType
from ..models.semantic_version_range import SemanticVersionRange


class GetRuntimeByNameQuery(BaseModel):
    """GetRuntimeByNameQuery."""

    version: Optional[SemanticVersionRange] = None
    include_deprecated: Optional[StrictBool] = Field(
        default=False,
        description="If set to `true`, deprecated runtimes will be included in the query.",
        alias="includeDeprecated",
    )
    function_type: Optional[List[FunctionType]] = Field(
        default=None,
        description="If set, filters on the <code>functionType</code> of a runtime. Uses an exact match.",
        alias="functionType",
    )
    archive_format: Optional[List[ArchiveFormat]] = Field(
        default=None,
        description="If set, filters on the <code>archiveFormat</code> of a runtime. Uses an exact match.",
        alias="archiveFormat",
    )

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="ignore",
    )

    def to_str(self) -> str:
        """Get the string representation of the model using alias."""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Get the JSON representation of the model using alias."""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict(), default=str)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GetRuntimeByNameQuery from a JSON string."""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Get the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={},
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetRuntimeByNameQuery from a dict."""
        if obj is None:
            return None
        return cls.model_validate(obj)
