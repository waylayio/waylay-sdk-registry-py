# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
import re  # noqa: F401

from ..models.job_state_active import JobStateActive
from ..models.job_state_delayed import JobStateDelayed
from ..models.job_state_finished import JobStateFinished
from ..models.job_state_waiting import JobStateWaiting
from ..models.job_state_waiting_children import JobStateWaitingChildren

from typing import (
    Union,  # >=3.8
)
from typing_extensions import (
    Annotated,  # >=3.9
)


JobState = Union[
    Annotated[JobStateFinished, ""],
    Annotated[JobStateActive, ""],
    Annotated[JobStateDelayed, ""],
    Annotated[JobStateWaiting, ""],
    Annotated[JobStateWaitingChildren, ""],
]
"""Allowed job states."""
