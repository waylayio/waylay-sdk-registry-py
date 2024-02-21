# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.rebuild_webscript_async_response_v2 import RebuildWebscriptAsyncResponseV2


from .job_hal_links_stub import JobHALLinksStub

from .job_causes_stub import JobCausesStub

from .webscript_response_v2_stub import WebscriptResponseV2Stub


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr
from pydantic import Field
from waylay.services.registry.models.job_causes import JobCauses
from waylay.services.registry.models.job_hal_links import JobHALLinks
from waylay.services.registry.models.webscript_response_v2 import WebscriptResponseV2


class RebuildWebscriptAsyncResponseV2Stub:
    """RebuildWebscriptAsyncResponseV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> RebuildWebscriptAsyncResponseV2:
        """Create RebuildWebscriptAsyncResponseV2 stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return RebuildWebscriptAsyncResponseV2(
                message='',
                links=JobHALLinksStub.create_instance(),
                causes=JobCausesStub.create_instance(),
                entity=WebscriptResponseV2Stub.create_instance()
            )
        else:
            return RebuildWebscriptAsyncResponseV2(
                message='',
                links=JobHALLinksStub.create_instance(),
                causes=JobCausesStub.create_instance(),
                entity=WebscriptResponseV2Stub.create_instance()
            )
