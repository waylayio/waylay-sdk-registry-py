# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from waylay.services.registry.models.post_webscript_job_async_response_v2 import (
    PostWebscriptJobAsyncResponseV2,
)


from .job_hal_links_stub import JobHALLinksStub

from .webscript_response_v2_stub import WebscriptResponseV2Stub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class PostWebscriptJobAsyncResponseV2Stub:
    """PostWebscriptJobAsyncResponseV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> PostWebscriptJobAsyncResponseV2:
        """Create PostWebscriptJobAsyncResponseV2 stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return PostWebscriptJobAsyncResponseV2(
                message="",
                links=JobHALLinksStub.create_instance(),
                entity=WebscriptResponseV2Stub.create_instance(),
            )
        else:
            return PostWebscriptJobAsyncResponseV2(
                message="",
                links=JobHALLinksStub.create_instance(),
                entity=WebscriptResponseV2Stub.create_instance(),
            )
