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
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from ..models.archive_format import ArchiveFormat
from ..models.assets_conditions import AssetsConditions
from ..models.build_spec import BuildSpec
from ..models.deploy_spec import DeploySpec
from ..models.function_type import FunctionType
from ..models.language_release import LanguageRelease
from ..models.provided_dependency import ProvidedDependency


try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class CompiledRuntimeVersion(BaseModel):
    """Compiled build and deployment information for a runtime version. Contains all defaults applied on the _global_, _functionType_, _archiveFormat_, _runtime_ and _runtime version_ level.."""

    deprecated: StrictBool = Field(description="If true, this runtime should no longer be used for new functions.")
    upgradable: StrictBool = Field(description="If true, a newer runtime for this function is available using the `rebuild` API.")
    name: StrictStr
    function_type: FunctionType = Field(alias="functionType")
    archive_format: ArchiveFormat = Field(alias="archiveFormat")
    build: Optional[BuildSpec] = None
    deploy: Optional[DeploySpec] = None
    language: Optional[LanguageRelease] = None
    provided_dependencies: Optional[List[ProvidedDependency]] = Field(default=None, description="Description of dependencies provided by this runtime version.", alias="providedDependencies")
    assets: Optional[AssetsConditions] = None
    title: StrictStr
    description: Optional[StrictStr] = None
    version: Annotated[str, Field(strict=True)] = Field(description="A semantic version with _exactly_ a `major`, `minor` and `patch` specifier. No `pre-release` or `build` identifiers are allowed. See https://semver.org")
    __properties: ClassVar[List[str]] = ["deprecated", "upgradable", "name", "functionType", "archiveFormat", "build", "deploy", "language", "providedDependencies", "assets", "title", "description", "version"]

    @field_validator('version')
    @classmethod
    def version_validate_regular_expression(cls, value):
        """Validate the regular expression."""
        if not re.match(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$", value):
            raise ValueError(r"must validate the regular expression /^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$/")
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
        """Create an instance of CompiledRuntimeVersion from a JSON string."""
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
        # override the default output from pydantic by calling `to_dict()` of language
        if self.language:
            _dict['language'] = self.language.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in provided_dependencies (list)
        _items = []
        if self.provided_dependencies:
            for _item in self.provided_dependencies:  # type: ignore
                if _item:
                    _items.append(_item.to_dict())
            _dict['providedDependencies'] = _items
        # override the default output from pydantic by calling `to_dict()` of assets
        if self.assets:
            _dict['assets'] = self.assets.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CompiledRuntimeVersion from a dict."""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "deprecated": obj.get("deprecated"),
            "upgradable": obj.get("upgradable"),
            "name": obj.get("name"),
            "functionType": obj.get("functionType"),
            "archiveFormat": obj.get("archiveFormat"),
            "build": BuildSpec.from_dict(obj.get("build")) if obj.get("build") is not None else None,    # type: ignore
            "deploy": DeploySpec.from_dict(obj.get("deploy")) if obj.get("deploy") is not None else None,    # type: ignore
            "language": LanguageRelease.from_dict(obj.get("language")) if obj.get("language") is not None else None,    # type: ignore
            "providedDependencies": [ProvidedDependency.from_dict(_item) for _item in obj.get("providedDependencies")] if obj.get("providedDependencies") is not None else None,  # type: ignore
            "assets": AssetsConditions.from_dict(obj.get("assets")) if obj.get("assets") is not None else None,    # type: ignore
            "title": obj.get("title"),
            "description": obj.get("description"),
            "version": obj.get("version")
        })
        return _obj
