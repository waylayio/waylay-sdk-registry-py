# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
import re  # noqa: F401
from enum import Enum


class LatestVersionLevel(str, Enum):
    """Level of latest versions that should be included.."""

    MAJOR = "major"
    MINOR = "minor"
    PATCH = "patch"
    TRUE = "true"
    FALSE = "false"

    def __str__(self) -> str:
        return str(self.value)
