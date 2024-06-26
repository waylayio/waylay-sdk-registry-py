# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import (
    Union,
)

from typing_extensions import (
    Annotated,  # >=3.9
)

from ..models.batch import Batch
from ..models.build1 import Build1
from ..models.deploy1 import Deploy1
from ..models.scale1 import Scale1
from ..models.undeploy1 import Undeploy1
from ..models.verify1 import Verify1

AnyJobStatusSummary = Union[
    Annotated[Build1, ""],
    Annotated[Deploy1, ""],
    Annotated[Verify1, ""],
    Annotated[Undeploy1, ""],
    Annotated[Scale1, ""],
    Annotated[Batch, ""],
]
"""AnyJobStatusSummary."""
