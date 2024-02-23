# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.legacy_plug_script_response import LegacyPlugScriptResponse


from .legacy_plug_script_meta_stub import LegacyPlugScriptMetaStub


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from waylay.services.registry.models.legacy_plug_script_meta import LegacyPlugScriptMeta
from waylay.services.registry.models.plug_type import PlugType


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class LegacyPlugScriptResponseStub:
    """LegacyPlugScriptResponse unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> LegacyPlugScriptResponse:
        """Create LegacyPlugScriptResponse stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return LegacyPlugScriptResponse(
                name='',
                version='9072888001528021798096225500850762068629339333975650685139102691291.0.0',
                type='sensor',
                script='',
                metadata=LegacyPlugScriptMetaStub.create_instance(),
                dependencies={'key': 'value'}
            )
        else:
            return LegacyPlugScriptResponse(
                name='',
                version='9072888001528021798096225500850762068629339333975650685139102691291.0.0',
                type='sensor',
                script='',
                metadata=LegacyPlugScriptMetaStub.create_instance(),
                dependencies={'key': 'value'}
            )
