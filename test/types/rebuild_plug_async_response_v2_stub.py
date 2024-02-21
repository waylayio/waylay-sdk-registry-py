# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.rebuild_plug_async_response_v2 import RebuildPlugAsyncResponseV2


from .job_hal_links_stub import JobHALLinksStub

from .job_causes_stub import JobCausesStub

from .plug_response_v2_stub import PlugResponseV2Stub


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr
from pydantic import Field
from waylay.services.registry.models.job_causes import JobCauses
from waylay.services.registry.models.job_hal_links import JobHALLinks
from waylay.services.registry.models.plug_response_v2 import PlugResponseV2


class RebuildPlugAsyncResponseV2Stub:
    """RebuildPlugAsyncResponseV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> RebuildPlugAsyncResponseV2:
        """Create RebuildPlugAsyncResponseV2 stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return RebuildPlugAsyncResponseV2(
                message='',
                links=JobHALLinksStub.create_instance(),
                causes=JobCausesStub.create_instance(),
                entity=PlugResponseV2Stub.create_instance()
            )
        else:
            return RebuildPlugAsyncResponseV2(
                message='',
                links=JobHALLinksStub.create_instance(),
                causes=JobCausesStub.create_instance(),
                entity=PlugResponseV2Stub.create_instance()
            )
