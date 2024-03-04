# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from waylay.services.registry.models.post_webscript_job_sync_response_v2 import (
    PostWebscriptJobSyncResponseV2,
)


from .webscript_response_v2_stub import WebscriptResponseV2Stub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class PostWebscriptJobSyncResponseV2Stub:
    """PostWebscriptJobSyncResponseV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> PostWebscriptJobSyncResponseV2:
        """Create PostWebscriptJobSyncResponseV2 stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return PostWebscriptJobSyncResponseV2(
                message="", entity=WebscriptResponseV2Stub.create_instance()
            )
        else:
            return PostWebscriptJobSyncResponseV2(
                message="", entity=WebscriptResponseV2Stub.create_instance()
            )
