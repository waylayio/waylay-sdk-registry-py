"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class JobTypeNotify(str, Enum):
    """A job to notify that an function version has changed.."""

    NOTIFY = "notify"

    def __str__(self) -> str:
        return str(self.value)
