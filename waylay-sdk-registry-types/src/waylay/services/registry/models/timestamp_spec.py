"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.timestamp_absolute import TimestampAbsolute
from ..models.timestamp_age import TimestampAge

TimestampSpec: TypeAlias = TimestampAge | TimestampAbsolute
"""A timestamp specification.."""
