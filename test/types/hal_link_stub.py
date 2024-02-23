# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.hal_link import HALLink


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class HALLinkStub:
    """HALLink unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> HALLink:
        """Create HALLink stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return HALLink(
                href=''
            )
        else:
            return HALLink(
                href=''
            )
