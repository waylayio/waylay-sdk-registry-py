# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.post_plug_job_async_response_v2 import PostPlugJobAsyncResponseV2


from .job_hal_links_stub import JobHALLinksStub

from .plug_response_v2_stub import PlugResponseV2Stub


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr
from pydantic import Field
from waylay.services.registry.models.job_hal_links import JobHALLinks
from waylay.services.registry.models.plug_response_v2 import PlugResponseV2


class PostPlugJobAsyncResponseV2Stub:
    """PostPlugJobAsyncResponseV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> PostPlugJobAsyncResponseV2:
        """Create PostPlugJobAsyncResponseV2 stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return PostPlugJobAsyncResponseV2(
                message='',
                links=JobHALLinksStub.create_instance(),
                entity=PlugResponseV2Stub.create_instance()
            )
        else:
            return PostPlugJobAsyncResponseV2(
                message='',
                links=JobHALLinksStub.create_instance(),
                entity=PlugResponseV2Stub.create_instance()
            )
