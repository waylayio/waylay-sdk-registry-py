"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.function_type import FunctionType
from ..models.function_type_exclude import FunctionTypeExclude

FunctionTypeFilter: TypeAlias = FunctionType | FunctionTypeExclude
"""FunctionTypeFilter."""
