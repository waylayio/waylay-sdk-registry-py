"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.job_events_hal_link import JobEventsHALLink
from ..models.model import Model
from ..models.plug import Plug
from ..models.webscript import Webscript

JobEventsAndFunctionHALLink: TypeAlias = Plug | Webscript | Model | JobEventsHALLink
"""HAL links to related actions.."""
