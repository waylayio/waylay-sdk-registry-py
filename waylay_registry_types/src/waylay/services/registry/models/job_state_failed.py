# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
import json
import re  # noqa: F401
from enum import Enum


from typing_extensions import (
    Self,  # >=3.11
)


class JobStateFailed(str, Enum):
    """The job failed in execution.."""

    """
    allowed enum values
    """
    FAILED = "failed"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of JobStateFailed from a JSON string."""
        return cls(json.loads(json_str))

    def to_json(self) -> str:
        """Get the JSON representation of JobStateFailed."""
        return self.value

    def to_dict(self) -> str:
        """Get the dict representation of JobStateFailed."""
        return self.value
