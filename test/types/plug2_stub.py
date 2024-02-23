# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.plug2 import Plug2

from .hal_link_stub import HALLinkStub

from .hal_link_stub import HALLinkStub


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from waylay.services.registry.models.hal_link import HALLink


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class Plug2Stub:
    """Plug2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> Plug2:
        """Create Plug2 stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return Plug2(
                job=HALLinkStub.create_instance(),
                plug=HALLinkStub.create_instance()
            )
        else:
            return Plug2(
                plug=HALLinkStub.create_instance()
            )
