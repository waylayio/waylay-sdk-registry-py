# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.plug_delete_force_query import PlugDeleteForceQuery


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool
from pydantic import Field


class PlugDeleteForceQueryStub:
    """PlugDeleteForceQuery unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> PlugDeleteForceQuery:
        """Create PlugDeleteForceQuery stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return PlugDeleteForceQuery(
                force=True
            )
        else:
            return PlugDeleteForceQuery(
            )
