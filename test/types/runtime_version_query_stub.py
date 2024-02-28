# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.runtime_version_query import RuntimeVersionQuery
from .semantic_version_range_stub import SemanticVersionRangeStub


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool
from pydantic import Field
from waylay.services.registry.models.latest_version_level import LatestVersionLevel
from waylay.services.registry.models.semantic_version_range import SemanticVersionRange


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class RuntimeVersionQueryStub:
    """RuntimeVersionQuery unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> RuntimeVersionQuery:
        """Create RuntimeVersionQuery stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return RuntimeVersionQuery(
                version=SemanticVersionRangeStub.create_instance(),
                latest='major',
                include_deprecated=True
            )
        else:
            return RuntimeVersionQuery(
            )
