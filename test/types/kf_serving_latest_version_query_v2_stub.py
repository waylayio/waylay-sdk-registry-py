# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.kf_serving_latest_version_query_v2 import KFServingLatestVersionQueryV2


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool
from pydantic import Field


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class KFServingLatestVersionQueryV2Stub:
    """KFServingLatestVersionQueryV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> KFServingLatestVersionQueryV2:
        """Create KFServingLatestVersionQueryV2 stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return KFServingLatestVersionQueryV2(
                include_draft=True,
                include_deprecated=True
            )
        else:
            return KFServingLatestVersionQueryV2(
            )
