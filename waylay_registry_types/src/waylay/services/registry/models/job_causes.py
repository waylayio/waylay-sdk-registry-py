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
from ..models.job_cause import JobCause


try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class JobCauses(BaseModel):
    """The motivations for including or excluding a job in response to a <em>rebuild</em> request.."""

    build: Optional[JobCause] = None
    deploy: Optional[JobCause] = None
    verify: Optional[JobCause] = None
    undeploy: Optional[JobCause] = None
    scale: Optional[JobCause] = None
    __properties: ClassVar[List[str]] = ["build", "deploy", "verify", "undeploy", "scale"]

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
        """Create an instance of JobCauses from a JSON string."""
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
        # override the default output from pydantic by calling `to_dict()` of build
        if self.build:
            _dict['build'] = self.build.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deploy
        if self.deploy:
            _dict['deploy'] = self.deploy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of verify
        if self.verify:
            _dict['verify'] = self.verify.to_dict()
        # override the default output from pydantic by calling `to_dict()` of undeploy
        if self.undeploy:
            _dict['undeploy'] = self.undeploy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scale
        if self.scale:
            _dict['scale'] = self.scale.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of JobCauses from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "build": JobCause.from_dict(obj.get("build")) if obj.get("build") is not None else None,    # type: ignore
            "deploy": JobCause.from_dict(obj.get("deploy")) if obj.get("deploy") is not None else None,    # type: ignore
            "verify": JobCause.from_dict(obj.get("verify")) if obj.get("verify") is not None else None,    # type: ignore
            "undeploy": JobCause.from_dict(obj.get("undeploy")) if obj.get("undeploy") is not None else None,    # type: ignore
            "scale": JobCause.from_dict(obj.get("scale")) if obj.get("scale") is not None else None    # type: ignore
        })
        return _obj
