# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from datetime import date, datetime
from typing import (
    Union,
)

from typing_extensions import (
    Annotated,  # >=3.9
)

TimestampAbsolute = Union[
    Annotated[datetime, "An ISO8601 date-time expression."],
    Annotated[date, "An ISO8601 date expression."],
]
"""An absolute timestamp as an ISO8601 string."""
