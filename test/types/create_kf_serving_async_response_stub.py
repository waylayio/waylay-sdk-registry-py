# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.create_kf_serving_async_response import CreateKFServingAsyncResponse


from .job_hal_links_stub import JobHALLinksStub

from .kf_serving_manifest_stub import KFServingManifestStub

from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr
from pydantic import Field
from waylay.services.registry.models.job_hal_links import JobHALLinks
from waylay.services.registry.models.kf_serving_manifest import KFServingManifest


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class CreateKFServingAsyncResponseStub:
    """CreateKFServingAsyncResponse unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> CreateKFServingAsyncResponse:
        """Create CreateKFServingAsyncResponse stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return CreateKFServingAsyncResponse(
                message='',
                links=JobHALLinksStub.create_instance(),
                entity=KFServingManifestStub.create_instance()
            )
        else:
            return CreateKFServingAsyncResponse(
                message='',
                links=JobHALLinksStub.create_instance(),
                entity=KFServingManifestStub.create_instance()
            )
