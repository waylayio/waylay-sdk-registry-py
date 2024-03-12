# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
import re  # noqa: F401

from ..models.batch_result import BatchResult
from ..models.build_result import BuildResult
from ..models.cleanup_result import CleanupResult
from ..models.deploy_result import DeployResult
from ..models.undeploy_result import UndeployResult
from ..models.verify_result import VerifyResult

from typing import (
    Union,  # >=3.8
)
from typing_extensions import (
    Annotated,  # >=3.9
)


AnyJobResult = Union[
    Annotated[BuildResult, ""],
    Annotated[DeployResult, ""],
    Annotated[VerifyResult, ""],
    Annotated[UndeployResult, ""],
    Annotated[object, "The result data for a completed scale job."],
    Annotated[BatchResult, ""],
    Annotated[CleanupResult, ""],
]
"""AnyJobResult."""
