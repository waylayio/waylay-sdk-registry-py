"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class JobStateWaitingChildren(str, Enum):
    """The job is waiting for child jobs to be completed.."""

    WAITING_MINUS_CHILDREN = "waiting-children"

    def __str__(self) -> str:
        return str(self.value)
