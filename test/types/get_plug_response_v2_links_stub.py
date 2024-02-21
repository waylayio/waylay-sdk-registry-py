# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.get_plug_response_v2_links import GetPlugResponseV2Links

from .get_plug_response_v2_links_draft_stub import GetPlugResponseV2LinksDraftStub

from .get_plug_response_v2_links_published_stub import GetPlugResponseV2LinksPublishedStub

from .hal_link_stub import HALLinkStub


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from waylay.services.registry.models.get_plug_response_v2_links_draft import GetPlugResponseV2LinksDraft
from waylay.services.registry.models.get_plug_response_v2_links_published import GetPlugResponseV2LinksPublished
from waylay.services.registry.models.hal_link import HALLink


class GetPlugResponseV2LinksStub:
    """GetPlugResponseV2Links unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> GetPlugResponseV2Links:
        """Create GetPlugResponseV2Links stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return GetPlugResponseV2Links(
                draft=GetPlugResponseV2LinksDraftStub.create_instance(),
                published=GetPlugResponseV2LinksPublishedStub.create_instance(),
                jobs=HALLinkStub.create_instance()
            )
        else:
            return GetPlugResponseV2Links(
            )
