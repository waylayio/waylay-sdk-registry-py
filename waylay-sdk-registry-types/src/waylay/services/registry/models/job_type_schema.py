"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.job_type_batch import JobTypeBatch
from ..models.job_type_build import JobTypeBuild
from ..models.job_type_deploy import JobTypeDeploy
from ..models.job_type_notify import JobTypeNotify
from ..models.job_type_scale import JobTypeScale
from ..models.job_type_undeploy import JobTypeUndeploy
from ..models.job_type_verify import JobTypeVerify

JobTypeSchema: TypeAlias = JobTypeBuild | JobTypeDeploy | JobTypeVerify | JobTypeUndeploy | JobTypeScale | JobTypeBatch | JobTypeNotify
"""JobTypeSchema."""
