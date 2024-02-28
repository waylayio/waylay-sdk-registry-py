# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.get_plug_response_v2_links_published import GetPlugResponseV2LinksPublished


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictBool, StrictStr


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class GetPlugResponseV2LinksPublishedStub:
    """GetPlugResponseV2LinksPublished unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> GetPlugResponseV2LinksPublished:
        """Create GetPlugResponseV2LinksPublished stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return GetPlugResponseV2LinksPublished(
                draft=True,
                href='',
                version='',
                deprecated=True
            )
        else:
            return GetPlugResponseV2LinksPublished(
                draft=True,
                href='',
                version='',
                deprecated=True
            )
