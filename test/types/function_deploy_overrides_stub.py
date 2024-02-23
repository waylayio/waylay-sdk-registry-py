# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.function_deploy_overrides import FunctionDeployOverrides

from .function_deploy_overrides_type_stub import FunctionDeployOverridesTypeStub


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from waylay.services.registry.models.function_deploy_overrides_type import FunctionDeployOverridesType


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class FunctionDeployOverridesStub:
    """FunctionDeployOverrides unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> FunctionDeployOverrides:
        """Create FunctionDeployOverrides stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return FunctionDeployOverrides(
                deploy=FunctionDeployOverridesTypeStub.create_instance()
            )
        else:
            return FunctionDeployOverrides(
            )
