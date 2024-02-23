# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.update_metadata_request_v1 import UpdateMetadataRequestV1


from .tag_stub import TagStub


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from waylay.services.registry.models.tag import Tag


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class UpdateMetadataRequestV1Stub:
    """UpdateMetadataRequestV1 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> UpdateMetadataRequestV1:
        """Create UpdateMetadataRequestV1 stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return UpdateMetadataRequestV1(
                author='',
                description='',
                icon_url='',
                category='',
                documentation_url='',
                tags=[TagStub.create_instance()],
                friendly_name=''
            )
        else:
            return UpdateMetadataRequestV1(
            )
