# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum


try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class FunctionType(str, Enum):
    """Type of functions supported by the registry service.."""

    """
    allowed enum values
    """
    PLUGS = 'plugs'
    WEBSCRIPTS = 'webscripts'
    KFSERVING = 'kfserving'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FunctionType from a JSON string."""
        return cls(json.loads(json_str))

    def to_json(self) -> str:
        """Get the JSON representation of FunctionType."""
        return self.value

    def to_dict(self) -> str:
        """Get the dict representation of FunctionType."""
        return self.value
