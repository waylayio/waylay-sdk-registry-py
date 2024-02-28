# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.media_type import MediaType


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class MediaTypeStub:
    """MediaType unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> MediaType:
        """Create MediaType stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        return MediaType("application/javascript")
