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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt
from pydantic import Field
from ..models.latest_webscripts_response_v2_entities_inner import LatestWebscriptsResponseV2EntitiesInner


try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class LatestWebscriptsResponseV2(BaseModel):
    """Webscripts Found."""

    limit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The page size used for this query result.")
    count: Union[StrictFloat, StrictInt] = Field(description="The total count of matching items, from which this result is one page.")
    page: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The page number of a paged query result.")
    entities: List[LatestWebscriptsResponseV2EntitiesInner] = Field(description="The specification and deployment status of the queried functions")
    __properties: ClassVar[List[str]] = ["limit", "count", "page", "entities"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def to_str(self) -> str:
        """Get the string representation of the model using alias."""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Get the JSON representation of the model using alias."""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict(), default=str)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LatestWebscriptsResponseV2 from a JSON string."""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        # pylint: disable=not-an-iterable, no-member, unsupported-membership-test
        # pylint has some issues with `field` https://github.com/pylint-dev/pylint/issues/7437, so disable some checks
        """Get the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in entities (list)
        _items = []
        if self.entities:
            for _item in self.entities:  # type: ignore
                if _item:
                    _items.append(_item.to_dict())
            _dict['entities'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of LatestWebscriptsResponseV2 from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "limit": obj.get("limit"),
            "count": obj.get("count"),
            "page": obj.get("page"),
            "entities": [LatestWebscriptsResponseV2EntitiesInner.from_dict(_item) for _item in obj.get("entities")] if obj.get("entities") is not None else None  # type: ignore
        })
        return _obj
