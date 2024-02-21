# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.legacy_plug_response_metadata import LegacyPlugResponseMetadata

from .legacy_documentation_stub import LegacyDocumentationStub


from .tag_stub import TagStub


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from waylay.services.registry.models.legacy_documentation import LegacyDocumentation
from waylay.services.registry.models.tag import Tag


class LegacyPlugResponseMetadataStub:
    """LegacyPlugResponseMetadata unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> LegacyPlugResponseMetadata:
        """Create LegacyPlugResponseMetadata stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return LegacyPlugResponseMetadata(
                documentation=LegacyDocumentationStub.create_instance(),
                author='',
                description='',
                category='',
                tags=[TagStub.create_instance()],
                icon_url='',
                friendly_name=''
            )
        else:
            return LegacyPlugResponseMetadata(
            )
