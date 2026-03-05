"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class AnyJobForFunctionDeploy(str, Enum):
    """The type of the background task.."""

    DEPLOY = "deploy"

    def __str__(self) -> str:
        return str(self.value)
