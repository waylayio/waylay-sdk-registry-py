# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.assets_conditions import AssetsConditions


from .asset_condition_stub import AssetConditionStub


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from waylay.services.registry.models.asset_condition import AssetCondition


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class AssetsConditionsStub:
    """AssetsConditions unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> AssetsConditions:
        """Create AssetsConditions stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return AssetsConditions(
                conditions=[AssetConditionStub.create_instance()],
                max_size=''
            )
        else:
            return AssetsConditions(
            )
