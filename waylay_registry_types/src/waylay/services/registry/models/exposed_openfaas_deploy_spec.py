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
from pydantic import BaseModel, StrictStr
from ..models.resource_limits import ResourceLimits


from typing import cast

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ExposedOpenfaasDeploySpec(BaseModel):
    """ExposedOpenfaasDeploySpec."""

    service: StrictStr
    image: StrictStr
    namespace: StrictStr
    labels: Optional[Dict[str, StrictStr]] = None
    annotations: Optional[Dict[str, StrictStr]] = None
    limits: Optional[ResourceLimits] = None
    requests: Optional[ResourceLimits] = None
    __properties: ClassVar[List[str]] = [
        "service",
        "image",
        "namespace",
        "labels",
        "annotations",
        "limits",
        "requests",
    ]

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
        """Create an instance of ExposedOpenfaasDeploySpec from a JSON string."""
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
        # override the default output from pydantic by calling `to_dict()` of limits
        if self.limits:
            _dict["limits"] = self.limits.to_dict()
        # override the default output from pydantic by calling `to_dict()` of requests
        if self.requests:
            _dict["requests"] = self.requests.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ExposedOpenfaasDeploySpec from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "service": obj.get("service"),
                "image": obj.get("image"),
                "namespace": obj.get("namespace"),
                "labels": obj.get("labels"),
                "annotations": obj.get("annotations"),
                "limits": (
                    ResourceLimits.from_dict(cast(dict, obj.get("limits")))
                    if obj.get("limits") is not None
                    else None
                ),
                "requests": (
                    ResourceLimits.from_dict(cast(dict, obj.get("requests")))
                    if obj.get("requests") is not None
                    else None
                ),
            }
        )
        return _obj
