# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.kf_serving_delete_query_v2 import KFServingDeleteQueryV2


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class KFServingDeleteQueryV2Stub:
    """KFServingDeleteQueryV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> KFServingDeleteQueryV2:
        """Create KFServingDeleteQueryV2 stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return KFServingDeleteQueryV2(
                comment='',
                force=True,
                undeploy=True,
                var_async=True
            )
        else:
            return KFServingDeleteQueryV2(
            )
