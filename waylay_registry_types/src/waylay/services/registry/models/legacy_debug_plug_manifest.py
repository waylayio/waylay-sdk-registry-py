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
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from ..models.function_deploy_overrides_type import FunctionDeployOverridesType
from ..models.function_meta import FunctionMeta
from ..models.semantic_version_range import SemanticVersionRange


from typing import cast

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class LegacyDebugPlugManifest(BaseModel):
    """LegacyDebugPlugManifest."""

    deploy: Optional[FunctionDeployOverridesType] = None
    name: StrictStr = Field(description="The logical name for the function.")
    version: Annotated[str, Field(strict=True)] = Field(
        description="A semantic version with _exactly_ a `major`, `minor` and `patch` specifier. No `pre-release` or `build` identifiers are allowed. See https://semver.org"
    )
    runtime: StrictStr
    runtime_version: Optional[SemanticVersionRange] = Field(
        default=None, alias="runtimeVersion"
    )
    metadata: FunctionMeta
    tenant: StrictStr
    dependencies: Optional[Dict[str, StrictStr]] = None
    script: StrictStr
    __properties: ClassVar[List[str]] = [
        "deploy",
        "name",
        "version",
        "runtime",
        "runtimeVersion",
        "metadata",
        "tenant",
        "dependencies",
        "script",
    ]

    @field_validator("version")
    @classmethod
    def version_validate_regular_expression(cls, value):
        """Validate the regular expression."""
        if not re.match(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$", value):
            raise ValueError(
                r"must validate the regular expression /^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$/"
            )
        return value

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
        """Create an instance of LegacyDebugPlugManifest from a JSON string."""
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
        # override the default output from pydantic by calling `to_dict()` of deploy
        if self.deploy:
            _dict["deploy"] = self.deploy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of runtime_version
        if self.runtime_version:
            _dict["runtimeVersion"] = self.runtime_version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict["metadata"] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of LegacyDebugPlugManifest from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "deploy": (
                    FunctionDeployOverridesType.from_dict(cast(dict, obj.get("deploy")))
                    if obj.get("deploy") is not None
                    else None
                ),
                "name": obj.get("name"),
                "version": obj.get("version"),
                "runtime": obj.get("runtime"),
                "runtimeVersion": (
                    SemanticVersionRange.from_dict(
                        cast(dict, obj.get("runtimeVersion"))
                    )
                    if obj.get("runtimeVersion") is not None
                    else None
                ),
                "metadata": (
                    FunctionMeta.from_dict(cast(dict, obj.get("metadata")))
                    if obj.get("metadata") is not None
                    else None
                ),
                "tenant": obj.get("tenant"),
                "dependencies": obj.get("dependencies"),
                "script": obj.get("script"),
            }
        )
        return _obj
