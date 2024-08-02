# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

import re
from typing import List

from pydantic import (
    ConfigDict,
    Field,
    StrictBool,
    StrictStr,
    field_validator,
)
from typing_extensions import (
    Annotated,  # >=3.11
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.archive_format import ArchiveFormat
from ..models.assets_conditions import AssetsConditions
from ..models.build_spec import BuildSpec
from ..models.deploy_spec import DeploySpec
from ..models.function_type import FunctionType
from ..models.invocation_attributes import InvocationAttributes
from ..models.language_release import LanguageRelease
from ..models.provided_dependency import ProvidedDependency


class CompiledRuntimeVersion(WaylayBaseModel):
    """Compiled build and deployment information for a runtime version. Contains all defaults applied on the _global_, _functionType_, _archiveFormat_, _runtime_ and _runtime version_ level.."""

    deprecated: StrictBool = Field(
        description="If true, this runtime should no longer be used for new functions."
    )
    upgradable: StrictBool = Field(
        description="If true, a newer runtime for this function is available using the `rebuild` API."
    )
    name: StrictStr
    function_type: FunctionType = Field(alias="functionType")
    archive_format: ArchiveFormat = Field(alias="archiveFormat")
    build: BuildSpec | None = None
    deploy: DeploySpec | None = None
    language: LanguageRelease | None = None
    provided_dependencies: List[ProvidedDependency] | None = Field(
        default=None,
        description="Description of dependencies provided by this runtime version.",
        alias="providedDependencies",
    )
    assets: AssetsConditions | None = None
    invocation: InvocationAttributes | None = None
    title: StrictStr
    description: StrictStr | None = None
    version: Annotated[str, Field(strict=True)] = Field(
        description="A semantic version with _exactly_ a `major`, `minor` and `patch` specifier. No `pre-release` or `build` identifiers are allowed. See https://semver.org"
    )

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
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
