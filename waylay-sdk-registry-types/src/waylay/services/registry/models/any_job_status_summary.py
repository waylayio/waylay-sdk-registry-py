"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.batch import Batch
from ..models.build1 import Build1
from ..models.deploy1 import Deploy1
from ..models.scale1 import Scale1
from ..models.undeploy1 import Undeploy1
from ..models.verify1 import Verify1

AnyJobStatusSummary: TypeAlias = Build1 | Deploy1 | Verify1 | Undeploy1 | Scale1 | Batch
"""AnyJobStatusSummary."""
