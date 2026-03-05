"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class DeprecatePreviousPolicyMinor(str, Enum):
    """DeprecatePreviousPolicyMinor."""

    MINOR = "minor"

    def __str__(self) -> str:
        return str(self.value)
