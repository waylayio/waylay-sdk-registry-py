# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.runtime_name_query import RuntimeNameQuery


from .function_type_stub import FunctionTypeStub

from .archive_format_stub import ArchiveFormatStub

from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.function_type import FunctionType


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class RuntimeNameQueryStub:
    """RuntimeNameQuery unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> RuntimeNameQuery:
        """Create RuntimeNameQuery stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return RuntimeNameQuery(
                name='node*',
                function_type=['plugs'],
                archive_format=['node']
            )
        else:
            return RuntimeNameQuery(
            )
