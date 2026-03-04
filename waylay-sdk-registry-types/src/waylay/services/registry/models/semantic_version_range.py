"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

SemanticVersionRange: TypeAlias = str | Annotated[str, "A semantic version with _exactly_ a `major`, `minor` and `patch` specifier. No `pre-release` or `build` identifiers are allowed. See https://semver.org"]
"""A range of semantic versions. See https://devhints.io/semver."""
