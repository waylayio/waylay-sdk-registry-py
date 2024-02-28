# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.with_asset_hal_link import WithAssetHALLink
from .asset_summary_with_hal_link_links_stub import AssetSummaryWithHALLinkLinksStub

from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from pydantic import Field
from waylay.services.registry.models.asset_summary_with_hal_link_links import AssetSummaryWithHALLinkLinks


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class WithAssetHALLinkStub:
    """WithAssetHALLink unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> WithAssetHALLink:
        """Create WithAssetHALLink stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return WithAssetHALLink(
                links=AssetSummaryWithHALLinkLinksStub.create_instance()
            )
        else:
            return WithAssetHALLink(
                links=AssetSummaryWithHALLinkLinksStub.create_instance()
            )
