# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.plug_type_query import PlugTypeQuery


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from waylay.services.registry.models.plug_type import PlugType


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class PlugTypeQueryStub:
    """PlugTypeQuery unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> PlugTypeQuery:
        """Create PlugTypeQuery stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return PlugTypeQuery(
                type='sensor'
            )
        else:
            return PlugTypeQuery(
            )
