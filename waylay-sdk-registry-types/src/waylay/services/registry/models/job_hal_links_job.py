"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.job_hal_link import JobHALLink

JobHALLinksJob: TypeAlias = list[JobHALLink] | JobHALLink
"""Link to the job status page for the related entity.."""
