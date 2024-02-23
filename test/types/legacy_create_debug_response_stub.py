# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.legacy_create_debug_response import LegacyCreateDebugResponse


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr
from pydantic import Field


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class LegacyCreateDebugResponseStub:
    """LegacyCreateDebugResponse unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> LegacyCreateDebugResponse:
        """Create LegacyCreateDebugResponse stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return LegacyCreateDebugResponse(
                function_name=''
            )
        else:
            return LegacyCreateDebugResponse(
                function_name=''
            )
