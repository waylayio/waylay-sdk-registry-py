"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.status import Status
from ..models.status_any import StatusAny
from ..models.status_exclude import StatusExclude

StatusFilter: TypeAlias = Status | StatusExclude | StatusAny
"""Inclusion or exclusion filter on the `status` property.."""
