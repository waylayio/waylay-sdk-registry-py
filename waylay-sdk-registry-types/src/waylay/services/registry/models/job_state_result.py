"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.job_state import JobState
from ..models.job_state_unknown import JobStateUnknown

JobStateResult: TypeAlias = JobState | JobStateUnknown
"""All reported job states."""
