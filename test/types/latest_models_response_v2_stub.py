# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.latest_models_response_v2 import LatestModelsResponseV2


from .latest_models_response_v2_entities_inner_stub import LatestModelsResponseV2EntitiesInnerStub
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt
from pydantic import Field
from waylay.services.registry.models.latest_models_response_v2_entities_inner import LatestModelsResponseV2EntitiesInner


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class LatestModelsResponseV2Stub:
    """LatestModelsResponseV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> LatestModelsResponseV2:
        """Create LatestModelsResponseV2 stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return LatestModelsResponseV2(
                limit=1.337,
                count=1.337,
                page=1.337,
                entities=[LatestModelsResponseV2EntitiesInnerStub.create_instance()]
            )
        else:
            return LatestModelsResponseV2(
                count=1.337,
                entities=[LatestModelsResponseV2EntitiesInnerStub.create_instance()]
            )
