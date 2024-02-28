# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.verify import Verify
from .job_hal_links_stub import JobHALLinksStub


from .job_state_result_stub import JobStateResultStub

from .verify_args_stub import VerifyArgsStub

from .verify_result_stub import VerifyResultStub


from .function_ref_stub import FunctionRefStub

from .job_status_stub import JobStatusStub

from .failure_reason_stub import FailureReasonStub

from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from waylay.services.registry.models.failure_reason import FailureReason
from waylay.services.registry.models.function_ref import FunctionRef
from waylay.services.registry.models.job_hal_links import JobHALLinks
from waylay.services.registry.models.job_state_result import JobStateResult
from waylay.services.registry.models.job_status import JobStatus
from waylay.services.registry.models.verify_args import VerifyArgs
from waylay.services.registry.models.verify_result import VerifyResult


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class VerifyStub:
    """Verify unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> Verify:
        """Create Verify stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return Verify(
                links=JobHALLinksStub.create_instance(),
                type='verify',
                state=JobStateResultStub.create_instance(),
                request=VerifyArgsStub.create_instance(),
                result=VerifyResultStub.create_instance(),
                created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by='',
                operation='',
                function=FunctionRefStub.create_instance(),
                job=JobStatusStub.create_instance(),
                failure_reason=FailureReasonStub.create_instance()
            )
        else:
            return Verify(
                type='verify',
                state=JobStateResultStub.create_instance(),
                created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by='',
                operation='',
            )
