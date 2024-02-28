# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.create_function_query_v2 import CreateFunctionQueryV2


from .semantic_version_range_stub import SemanticVersionRangeStub


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from waylay.services.registry.models.deprecate_previous_policy import DeprecatePreviousPolicy
from waylay.services.registry.models.semantic_version_range import SemanticVersionRange


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class CreateFunctionQueryV2Stub:
    """CreateFunctionQueryV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> CreateFunctionQueryV2:
        """Create CreateFunctionQueryV2 stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return CreateFunctionQueryV2(
                deprecate_previous='none',
                dry_run=True,
                var_async=True,
                scale_to_zero=True,
                version=SemanticVersionRangeStub.create_instance(),
                name='',
                draft=True
            )
        else:
            return CreateFunctionQueryV2(
            )
