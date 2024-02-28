# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""


from __future__ import annotations
import json
import re  # noqa: F401
from enum import Enum


try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class QueueEvents(str, Enum):
    """QueueEvents."""

    """
    allowed enum values
    """
    COMPLETED = "completed"
    FAILED = "failed"
    ACTIVE = "active"
    DELAYED = "delayed"
    WAITING = "waiting"
    WAITING_MINUS_CHILDREN = "waiting-children"
    ADDED = "added"
    CLEANED = "cleaned"
    DRAINED = "drained"
    ERROR = "error"
    PAUSED = "paused"
    PROGRESS = "progress"
    REMOVED = "removed"
    RESUMED = "resumed"
    RETRIES_MINUS_EXHAUSTED = "retries-exhausted"
    STALLED = "stalled"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of QueueEvents from a JSON string."""
        return cls(json.loads(json_str))

    def to_json(self) -> str:
        """Get the JSON representation of QueueEvents."""
        return self.value

    def to_dict(self) -> str:
        """Get the dict representation of QueueEvents."""
        return self.value
