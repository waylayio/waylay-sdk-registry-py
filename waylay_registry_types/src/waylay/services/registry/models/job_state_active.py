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


try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class JobStateActive(str, Enum):
    """The job is running.."""

    """
    allowed enum values
    """
    ACTIVE = "active"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of JobStateActive from a JSON string."""
        return cls(json.loads(json_str))

    def to_json(self) -> str:
        """Get the JSON representation of JobStateActive."""
        return self.value

    def to_dict(self) -> str:
        """Get the dict representation of JobStateActive."""
        return self.value
