"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.build import Build
from ..models.deploy import Deploy
from ..models.scale import Scale
from ..models.undeploy import Undeploy
from ..models.verify import Verify

AnyJobForFunction: TypeAlias = Build | Deploy | Verify | Undeploy | Scale
"""AnyJobForFunction."""
