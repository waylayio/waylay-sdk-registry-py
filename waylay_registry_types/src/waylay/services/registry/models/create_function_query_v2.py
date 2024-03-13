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

from typing import Any, Dict, Optional
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from ..models.create_function_query_v2_copy import CreateFunctionQueryV2Copy
from ..models.deprecate_previous_policy import DeprecatePreviousPolicy
from ..models.semantic_version_range import SemanticVersionRange


class CreateFunctionQueryV2(BaseModel):
    """CreateFunctionQueryV2."""

    author: Optional[StrictStr] = Field(
        default=None,
        description="Optionally changes the author metadata when updating a function.",
    )
    comment: Optional[StrictStr] = Field(
        default=None,
        description="An optional user-specified comment corresponding to the operation.",
    )
    deprecate_previous: Optional[DeprecatePreviousPolicy] = Field(
        default=None, alias="deprecatePrevious"
    )
    dry_run: Optional[StrictBool] = Field(
        default=None,
        description="If set to <code>true</code>, validates the deployment conditions, but does not change anything.",
        alias="dryRun",
    )
    var_async: Optional[StrictBool] = Field(
        default=True,
        description="Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs.",
        alias="async",
    )
    scale_to_zero: Optional[StrictBool] = Field(
        default=False,
        description="If set to <code>true</code>, after successful deployment, the deployed function will be scaled to zero. Saves computing resources when the function is not to be used immediately.",
        alias="scaleToZero",
    )
    version: Optional[SemanticVersionRange] = None
    name: Optional[StrictStr] = Field(
        default=None,
        description="If set, the value will be used as the function name instead of the one specified in the manifest.",
    )
    draft: Optional[StrictBool] = Field(
        default=False,
        description="If set, the created function will be a draft function and its assets are still mutable. A build and deploy is initiated only in the case when all necessary assets are present and valid.",
    )
    runtime: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None,
        description="A name reference with optional version range: `<name>[@<versionRange>]`.  References (a version range of) a named and versioned entity like _function_ or _runtime_.",
    )
    copy_from: Optional[CreateFunctionQueryV2Copy] = Field(default=None, alias="copy")

    @field_validator("runtime")
    @classmethod
    def runtime_validate_regular_expression(cls, value):
        """Validate the regular expression."""
        if value is None:
            return value

        if not re.match(r"^[^@]*(@.*)?$", value):
            raise ValueError(r"must validate the regular expression /^[^@]*(@.*)?$/")
        return value

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
        """Create an instance of CreateFunctionQueryV2 from a JSON string."""
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
        """Create an instance of CreateFunctionQueryV2 from a dict."""
        if obj is None:
            return None
        return cls.model_validate(obj)
