"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.ihal_link import IHALLink

HALLinks: TypeAlias = IHALLink | list[IHALLink]
"""One or more links of the same HAL collection.."""
