# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.async_deploy_query import AsyncDeployQuery


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool
from pydantic import Field
from waylay.services.registry.models.deprecate_previous_policy import DeprecatePreviousPolicy


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class AsyncDeployQueryStub:
    """AsyncDeployQuery unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> AsyncDeployQuery:
        """Create AsyncDeployQuery stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return AsyncDeployQuery(
                deprecate_previous='none',
                dry_run=True,
                var_async=True,
                scale_to_zero=True
            )
        else:
            return AsyncDeployQuery(
            )
