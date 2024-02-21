# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.asset_condition import AssetCondition


from .asset_condition_pattern_stub import AssetConditionPatternStub

from .asset_condition_content_type_stub import AssetConditionContentTypeStub


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from waylay.services.registry.models.asset_condition_content_type import AssetConditionContentType
from waylay.services.registry.models.asset_condition_pattern import AssetConditionPattern
from waylay.services.registry.models.asset_role import AssetRole


class AssetConditionStub:
    """AssetCondition unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> AssetCondition:
        """Create AssetCondition stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return AssetCondition(
                title='',
                description='',
                role='manifest',
                pattern=AssetConditionPatternStub.create_instance(),
                content_type=AssetConditionContentTypeStub.create_instance(),
                min=0,
                max=1,
                max_size='',
                var_schema=object()
            )
        else:
            return AssetCondition(
                role='manifest',
                pattern=AssetConditionPatternStub.create_instance(),
            )
