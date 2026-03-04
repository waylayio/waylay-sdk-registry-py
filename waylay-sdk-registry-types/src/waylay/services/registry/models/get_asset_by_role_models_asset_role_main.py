"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class GetAssetByRoleModelsAssetRoleMain(str, Enum):
    """Main source code that implements the function entrypoint.."""

    MAIN = "main"

    def __str__(self) -> str:
        return str(self.value)
