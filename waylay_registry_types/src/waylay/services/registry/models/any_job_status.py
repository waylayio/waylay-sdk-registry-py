# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
import re  # noqa: F401

from ..models.batch_job_status import BatchJobStatus
from ..models.build_job_status import BuildJobStatus
from ..models.deploy_job_status import DeployJobStatus
from ..models.scale_job_status import ScaleJobStatus
from ..models.undeploy_job_status import UndeployJobStatus
from ..models.verify_job_status import VerifyJobStatus

from typing import (
    Union,  # >=3.8
)
from typing_extensions import (
    Annotated,  # >=3.9
)


AnyJobStatus = Union[
    Annotated[BuildJobStatus, ""],
    Annotated[DeployJobStatus, ""],
    Annotated[VerifyJobStatus, ""],
    Annotated[UndeployJobStatus, ""],
    Annotated[ScaleJobStatus, ""],
    Annotated[BatchJobStatus, ""],
]
"""AnyJobStatus."""
