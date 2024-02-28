# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.runtime_attributes import RuntimeAttributes


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class RuntimeAttributesStub:
    """RuntimeAttributes unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> RuntimeAttributes:
        """Create RuntimeAttributes stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return RuntimeAttributes(
                deprecated=True,
                upgradable=True,
                name='',
                version='9072888001528021798096225500850762068629339333975650685139102691291.0.0'
            )
        else:
            return RuntimeAttributes(
                deprecated=True,
                upgradable=True,
                name='',
                version='9072888001528021798096225500850762068629339333975650685139102691291.0.0'
            )
