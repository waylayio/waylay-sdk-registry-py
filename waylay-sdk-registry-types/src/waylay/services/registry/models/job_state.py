"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.job_state_active import JobStateActive
from ..models.job_state_delayed import JobStateDelayed
from ..models.job_state_finished import JobStateFinished
from ..models.job_state_prioritized import JobStatePrioritized
from ..models.job_state_waiting import JobStateWaiting
from ..models.job_state_waiting_children import JobStateWaitingChildren

JobState: TypeAlias = JobStateFinished | JobStateActive | JobStateDelayed | JobStateWaiting | JobStateWaitingChildren | JobStatePrioritized
"""Allowed job states."""
