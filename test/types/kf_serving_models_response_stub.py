# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.kf_serving_models_response import KFServingModelsResponse


from .kf_serving_response_stub import KFServingResponseStub
from .paging_response_stub import PagingResponseStub


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from waylay.services.registry.models.kf_serving_response import KFServingResponse
from waylay.services.registry.models.paging_response import PagingResponse


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class KFServingModelsResponseStub:
    """KFServingModelsResponse unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> KFServingModelsResponse:
        """Create KFServingModelsResponse stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return KFServingModelsResponse(
                models=[KFServingResponseStub.create_instance()],
                paging=PagingResponseStub.create_instance()
            )
        else:
            return KFServingModelsResponse(
                models=[KFServingResponseStub.create_instance()],
            )
