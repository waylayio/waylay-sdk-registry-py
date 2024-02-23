# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.plug_interface import PlugInterface


from .plug_property_stub import PlugPropertyStub

from .plug_property_stub import PlugPropertyStub

from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from waylay.services.registry.models.plug_property import PlugProperty


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class PlugInterfaceStub:
    """PlugInterface unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> PlugInterface:
        """Create PlugInterface stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return PlugInterface(
                states=[''],
                input=[PlugPropertyStub.create_instance()],
                output=[PlugPropertyStub.create_instance()]
            )
        else:
            return PlugInterface(
            )
