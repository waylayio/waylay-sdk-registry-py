# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.plug_listing_response import PlugListingResponse


from .plug_response_stub import PlugResponseStub

from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from waylay.services.registry.models.plug_response import PlugResponse


class PlugListingResponseStub:
    """PlugListingResponse unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> PlugListingResponse:
        """Create PlugListingResponse stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return PlugListingResponse(
                plugs=[PlugResponseStub.create_instance()]
            )
        else:
            return PlugListingResponse(
                plugs=[PlugResponseStub.create_instance()]
            )
