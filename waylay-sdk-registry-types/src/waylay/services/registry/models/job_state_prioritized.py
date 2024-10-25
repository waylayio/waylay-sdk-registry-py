# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from enum import Enum


class JobStatePrioritized(str, Enum):
    """The job has been queued for execution with priority, but might be waiting because of rate limiting.."""

    PRIORITIZED = "prioritized"

    def __str__(self) -> str:
        return str(self.value)
