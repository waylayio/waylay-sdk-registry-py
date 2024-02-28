# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.function_meta import FunctionMeta


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class FunctionMetaStub:
    """FunctionMeta unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> FunctionMeta:
        """Create FunctionMeta stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return FunctionMeta(
                author='',
                description='',
                icon_url='',
                category=''
            )
        else:
            return FunctionMeta(
            )
