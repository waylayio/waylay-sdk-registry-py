# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.batch import Batch


from .job_state_result_stub import JobStateResultStub


from .function_ref_stub import FunctionRefStub

from .job_hal_links_stub import JobHALLinksStub


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from waylay.services.registry.models.function_ref import FunctionRef
from waylay.services.registry.models.job_hal_links import JobHALLinks
from waylay.services.registry.models.job_state_result import JobStateResult


class BatchStub:
    """Batch unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> Batch:
        """Create Batch stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return Batch(
                type='batch',
                operation='',
                id='',
                state=JobStateResultStub.create_instance(),
                created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by='',
                function=FunctionRefStub.create_instance(),
                links=JobHALLinksStub.create_instance()
            )
        else:
            return Batch(
                type='batch',
                operation='',
                id='',
                state=JobStateResultStub.create_instance(),
                created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by='',
                links=JobHALLinksStub.create_instance()
            )
