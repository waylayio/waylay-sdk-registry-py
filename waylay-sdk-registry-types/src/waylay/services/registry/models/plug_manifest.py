# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

import re

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
    field_validator,
)
from typing_extensions import (
    Annotated,  # >=3.11
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.function_deploy_overrides_type import FunctionDeployOverridesType
from ..models.plug_interface import PlugInterface
from ..models.plug_meta import PlugMeta
from ..models.plug_type import PlugType
from ..models.semantic_version_range import SemanticVersionRange


class PlugManifest(WaylayBaseModel):
    """PlugManifest."""

    deploy: FunctionDeployOverridesType | None = None
    name: StrictStr = Field(description="The logical name for the function.")
    version: Annotated[str, Field(strict=True)] = Field(
        description="A semantic version with _exactly_ a `major`, `minor` and `patch` specifier. No `pre-release` or `build` identifiers are allowed. See https://semver.org"
    )
    runtime: StrictStr
    runtime_version: SemanticVersionRange | None = Field(
        default=None, alias="runtimeVersion"
    )
    metadata: PlugMeta
    type: PlugType
    interface: PlugInterface

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
        extra="ignore",
    )
