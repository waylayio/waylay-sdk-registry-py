"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

from ..models.tag import Tag

TagOrTagReference: TypeAlias = Annotated[str, "A string that references a tag"] | Tag
"""A reference to a tag, or tag object.."""
