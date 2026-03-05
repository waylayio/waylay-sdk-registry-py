"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.deprecate_previous_policy_all import DeprecatePreviousPolicyAll
from ..models.deprecate_previous_policy_minor import DeprecatePreviousPolicyMinor
from ..models.deprecate_previous_policy_none import DeprecatePreviousPolicyNone
from ..models.deprecate_previous_policy_patch import DeprecatePreviousPolicyPatch

DeprecatePreviousPolicy: TypeAlias = DeprecatePreviousPolicyNone | DeprecatePreviousPolicyAll | DeprecatePreviousPolicyPatch | DeprecatePreviousPolicyMinor
"""DeprecatePreviousPolicy."""
