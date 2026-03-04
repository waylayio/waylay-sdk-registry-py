"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.batch_job_status import BatchJobStatus
from ..models.build_job_status import BuildJobStatus
from ..models.deploy_job_status import DeployJobStatus
from ..models.scale_job_status import ScaleJobStatus
from ..models.undeploy_job_status import UndeployJobStatus
from ..models.verify_job_status import VerifyJobStatus

AnyJobStatus: TypeAlias = BuildJobStatus | DeployJobStatus | VerifyJobStatus | UndeployJobStatus | ScaleJobStatus | BatchJobStatus
"""AnyJobStatus."""
