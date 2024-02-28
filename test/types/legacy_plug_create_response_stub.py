# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.legacy_plug_create_response import LegacyPlugCreateResponse


from .legacy_plug_script_response_stub import LegacyPlugScriptResponseStub

from typing import Any, ClassVar, Dict, List, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from waylay.services.registry.models.legacy_plug_script_response import LegacyPlugScriptResponse


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class LegacyPlugCreateResponseStub:
    """LegacyPlugCreateResponse unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> LegacyPlugCreateResponse:
        """Create LegacyPlugCreateResponse stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return LegacyPlugCreateResponse(
                status_code=1.337,
                uri='',
                entity=LegacyPlugScriptResponseStub.create_instance()
            )
        else:
            return LegacyPlugCreateResponse(
                status_code=1.337,
                uri='',
                entity=LegacyPlugScriptResponseStub.create_instance()
            )
