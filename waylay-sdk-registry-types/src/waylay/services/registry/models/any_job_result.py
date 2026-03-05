"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import Annotated, TypeAlias

from ..models.batch_result import BatchResult
from ..models.build_result import BuildResult
from ..models.cleanup_result import CleanupResult
from ..models.deploy_result import DeployResult
from ..models.notify_result import NotifyResult
from ..models.undeploy_result import UndeployResult
from ..models.verify_result import VerifyResult

AnyJobResult: TypeAlias = BuildResult | DeployResult | VerifyResult | UndeployResult | Annotated[object, "The result data for a completed scale job."] | BatchResult | CleanupResult | NotifyResult
"""AnyJobResult."""
