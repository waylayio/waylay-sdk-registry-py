# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.function_deploy_overrides_type import FunctionDeployOverridesType


from .resource_limits_stub import ResourceLimitsStub

from .resource_limits_stub import ResourceLimitsStub

from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from waylay.services.registry.models.resource_limits import ResourceLimits


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class FunctionDeployOverridesTypeStub:
    """FunctionDeployOverridesType unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> FunctionDeployOverridesType:
        """Create FunctionDeployOverridesType stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return FunctionDeployOverridesType(
                env_vars={
                    'key': ''
                },
                labels={
                    'key': ''
                },
                annotations={
                    'key': ''
                },
                limits=ResourceLimitsStub.create_instance(),
                requests=ResourceLimitsStub.create_instance()
            )
        else:
            return FunctionDeployOverridesType(
            )
