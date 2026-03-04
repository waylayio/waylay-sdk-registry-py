"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.job_state_completed import JobStateCompleted
from ..models.job_state_failed import JobStateFailed

JobStateFinished: TypeAlias = JobStateCompleted | JobStateFailed
"""The job completed successfully or with failure.."""
