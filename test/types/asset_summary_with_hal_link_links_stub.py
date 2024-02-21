# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.asset_summary_with_hal_link_links import AssetSummaryWithHALLinkLinks

from .hal_link_stub import HALLinkStub


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from waylay.services.registry.models.hal_link import HALLink


class AssetSummaryWithHALLinkLinksStub:
    """AssetSummaryWithHALLinkLinks unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> AssetSummaryWithHALLinkLinks:
        """Create AssetSummaryWithHALLinkLinks stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return AssetSummaryWithHALLinkLinks(
                asset=HALLinkStub.create_instance()
            )
        else:
            return AssetSummaryWithHALLinkLinks(
                asset=HALLinkStub.create_instance()
            )
