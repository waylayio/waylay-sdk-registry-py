"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.job_hal_links import JobHALLinks
from ..models.model1 import Model1
from ..models.plug1 import Plug1
from ..models.webscript1 import Webscript1

JobAndFunctionHALLink: TypeAlias = Plug1 | Webscript1 | Model1 | JobHALLinks
"""HAL links to related actions.."""
