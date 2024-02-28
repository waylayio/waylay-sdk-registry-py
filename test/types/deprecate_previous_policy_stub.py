# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.deprecate_previous_policy import DeprecatePreviousPolicy


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class DeprecatePreviousPolicyStub:
    """DeprecatePreviousPolicy unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> DeprecatePreviousPolicy:
        """Create DeprecatePreviousPolicy stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        return DeprecatePreviousPolicy("none")
