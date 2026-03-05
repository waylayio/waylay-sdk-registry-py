"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class JobStateWaiting(str, Enum):
    """The job has been queued for execution, but might be waiting because of rate limiting.."""

    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
