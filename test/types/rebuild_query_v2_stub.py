# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.rebuild_query_v2 import RebuildQueryV2


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from waylay.services.registry.models.rebuild_policy import RebuildPolicy


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class RebuildQueryV2Stub:
    """RebuildQueryV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> RebuildQueryV2:
        """Create RebuildQueryV2 stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return RebuildQueryV2(
                comment='',
                dry_run=True,
                var_async=True,
                upgrade='patch',
                force_version='9072888001528021798096225500850762068629339333975650685139102691291.0.0',
                ignore_checks=True,
                scale_to_zero=True,
                skip_rebuild=True
            )
        else:
            return RebuildQueryV2(
            )
