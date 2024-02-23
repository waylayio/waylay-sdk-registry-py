# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.undeployed_response_v2 import UndeployedResponseV2


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class UndeployedResponseV2Stub:
    """UndeployedResponseV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> UndeployedResponseV2:
        """Create UndeployedResponseV2 stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return UndeployedResponseV2(
                message='',
                versions=['9072888001528021798096225500850762068629339333975650685139102691291.0.0']
            )
        else:
            return UndeployedResponseV2(
                message='',
                versions=['9072888001528021798096225500850762068629339333975650685139102691291.0.0']
            )
