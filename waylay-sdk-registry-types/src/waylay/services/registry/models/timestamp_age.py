"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

TimestampAge: TypeAlias = Annotated[str, "An ISO8601 period expression"] | Annotated[str, "An duration expression. A numeric value without unit is interpreted as milliseconds."]
"""A timestamp expressed as a age relative to now."""
