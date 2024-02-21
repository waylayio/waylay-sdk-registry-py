# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.operation import Operation


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr
from waylay.services.registry.models.job_type import JobType


class OperationStub:
    """Operation unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> Operation:
        """Create Operation stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return Operation(
                id='',
                description='',
                name='',
                type='build'
            )
        else:
            return Operation(
                id='',
                description='',
                name='',
                type='build'
            )
