# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.jobs_for_webscript_response_v2_links import JobsForWebscriptResponseV2Links

from .hal_link_stub import HALLinkStub


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from waylay.services.registry.models.hal_link import HALLink


class JobsForWebscriptResponseV2LinksStub:
    """JobsForWebscriptResponseV2Links unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> JobsForWebscriptResponseV2Links:
        """Create JobsForWebscriptResponseV2Links stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return JobsForWebscriptResponseV2Links(
                webscript=HALLinkStub.create_instance()
            )
        else:
            return JobsForWebscriptResponseV2Links(
            )
