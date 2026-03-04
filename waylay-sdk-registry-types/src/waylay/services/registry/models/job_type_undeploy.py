"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class JobTypeUndeploy(str, Enum):
    """A job that undeploys a deployed function and removes it from the registry.."""

    UNDEPLOY = "undeploy"

    def __str__(self) -> str:
        return str(self.value)
