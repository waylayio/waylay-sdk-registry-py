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
    StrictFloat,
    StrictInt,
    StrictStr,
    field_validator,
)
from typing_extensions import (
    Annotated,  # >=3.11
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel


class ScaleArgs(WaylayBaseModel):
    """Input argument to an (openfaas) scale job for a function.."""

    namespace: StrictStr = Field(
        description="The (openfaas) namespace for the target function."
    )
    endpoint: StrictStr = Field(description="The (openfaas) endpoint service name")
    runtime_name: StrictStr = Field(alias="runtimeName")
    runtime_version: Annotated[str, Field(strict=True)] = Field(
        description="A semantic version with _exactly_ a `major`, `minor` and `patch` specifier. No `pre-release` or `build` identifiers are allowed. See https://semver.org",
        alias="runtimeVersion",
    )
    revision: StrictStr = Field(
        description="The revision hash of the current (draft) function revision"
    )
    replicas: StrictFloat | StrictInt = Field(description="Number of target replicas")

    @field_validator("runtime_version")
    @classmethod
    def runtime_version_validate_regular_expression(cls, value):
        """Validate the regular expression."""
        if not re.match(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$", value):
            raise ValueError(
                r"must validate the regular expression /^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$/"
            )
        return value

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
