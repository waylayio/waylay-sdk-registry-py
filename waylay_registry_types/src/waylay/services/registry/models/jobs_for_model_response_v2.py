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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from ..models.any_job_for_function import AnyJobForFunction
from ..models.function_ref import FunctionRef
from ..models.jobs_for_model_response_v2_links import JobsForModelResponseV2Links


from typing import cast

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class JobsForModelResponseV2(BaseModel):
    """Model Jobs Found."""

    jobs: List[AnyJobForFunction] = Field(
        description="Listing of jobs related to the function deployment. This includes active jobs, and the most recently failed job (per type) that was archived on the entity."
    )
    function: FunctionRef
    links: Optional[JobsForModelResponseV2Links] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["jobs", "function", "_links"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
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
        """Create an instance of JobsForModelResponseV2 from a JSON string."""
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
            exclude={},
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in jobs (list)
        _items = []
        if self.jobs:
            for _item in cast(list, self.jobs):
                if _item:
                    _items.append(_item.to_dict())
            _dict["jobs"] = _items
        # override the default output from pydantic by calling `to_dict()` of function
        if self.function:
            _dict["function"] = self.function.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict["_links"] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of JobsForModelResponseV2 from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "jobs": [
                    AnyJobForFunction.from_dict(cast(dict, _item))
                    for _item in cast(list, obj.get("jobs"))
                ]
                if obj.get("jobs") is not None
                else None,
                "function": (
                    FunctionRef.from_dict(cast(dict, obj.get("function")))
                    if obj.get("function") is not None
                    else None
                ),
                "_links": (
                    JobsForModelResponseV2Links.from_dict(cast(dict, obj.get("_links")))
                    if obj.get("_links") is not None
                    else None
                ),
            }
        )
        return _obj
