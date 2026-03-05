"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class RebuildPolicy(str, Enum):
    """The policy to select a new <em>runtime</em> version when a rebuild is issued.."""

    PATCH = "patch"
    MINOR = "minor"
    MAJOR = "major"
    SAME = "same"

    def __str__(self) -> str:
        return str(self.value)
