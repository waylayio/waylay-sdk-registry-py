"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.job_status_hal_link import JobStatusHALLink
from ..models.model2 import Model2
from ..models.plug2 import Plug2
from ..models.webscript2 import Webscript2

JobStatusAndEntityHALLinks: TypeAlias = Plug2 | Webscript2 | Model2 | JobStatusHALLink
"""HAL links to related actions.."""
