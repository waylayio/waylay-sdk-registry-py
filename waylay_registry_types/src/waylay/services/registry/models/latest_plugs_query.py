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

from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from ..models.archive_format import ArchiveFormat
from ..models.plug_type import PlugType
from ..models.show_related_type import ShowRelatedType


class LatestPlugsQuery(BaseModel):
    """Latest plug versions listing query with latest links. A request that only uses these query parameters will include links to the _latest_ draft/published versions of the plug.."""

    type: Optional[PlugType] = None
    show_related: Optional[ShowRelatedType] = Field(default=None, alias="showRelated")
    limit: Optional[
        Union[
            Annotated[float, Field(strict=True, ge=0)],
            Annotated[int, Field(strict=True, ge=0)],
        ]
    ] = Field(
        default=None,
        description="The maximum number of items to be return from this query. Has a deployment-defined default and maximum value.",
    )
    page: Optional[
        Union[
            Annotated[float, Field(strict=True, ge=0)],
            Annotated[int, Field(strict=True, ge=0)],
        ]
    ] = Field(
        default=None,
        description="The number of pages to skip when returning result to this query.",
    )
    include_draft: Optional[StrictBool] = Field(
        default=None,
        description="Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**.",
        alias="includeDraft",
    )
    include_deprecated: Optional[StrictBool] = Field(
        default=None,
        description="Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**.",
        alias="includeDeprecated",
    )
    name: Optional[StrictStr] = Field(
        default=None,
        description="Filter on the name of the function. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters).",
    )
    archive_format: Optional[List[ArchiveFormat]] = Field(
        default=None,
        description="Filter on the archive format of the function.",
        alias="archiveFormat",
    )
    runtime: Optional[List[StrictStr]] = Field(
        default=None, description="Filter on the runtime of the function."
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
        """Create an instance of LatestPlugsQuery from a JSON string."""
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
        """Create an instance of LatestPlugsQuery from a dict."""
        if obj is None:
            return None
        return cls.model_validate(obj)
