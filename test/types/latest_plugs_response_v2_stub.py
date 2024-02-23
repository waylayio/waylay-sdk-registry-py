# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.latest_plugs_response_v2 import LatestPlugsResponseV2


from .latest_plugs_response_v2_entities_inner_stub import LatestPlugsResponseV2EntitiesInnerStub

from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt
from pydantic import Field
from waylay.services.registry.models.latest_plugs_response_v2_entities_inner import LatestPlugsResponseV2EntitiesInner


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class LatestPlugsResponseV2Stub:
    """LatestPlugsResponseV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> LatestPlugsResponseV2:
        """Create LatestPlugsResponseV2 stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return LatestPlugsResponseV2(
                limit=1.337,
                count=1.337,
                page=1.337,
                entities=[LatestPlugsResponseV2EntitiesInnerStub.create_instance()]
            )
        else:
            return LatestPlugsResponseV2(
                count=1.337,
                entities=[LatestPlugsResponseV2EntitiesInnerStub.create_instance()]
            )
