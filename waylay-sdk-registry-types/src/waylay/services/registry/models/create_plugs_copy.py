"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

from ..models.example_reference import ExampleReference

CreatePlugsCopy: TypeAlias = Annotated[str, "A name reference with optional version range: `<name>[@<versionRange>]`.  References (a version range of) a named and versioned entity like _function_ or _runtime_."] | ExampleReference
"""CreatePlugsCopy."""
