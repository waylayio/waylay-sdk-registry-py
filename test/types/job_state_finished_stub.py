# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.job_state_finished import JobStateFinished
from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from waylay.services.registry.models.job_state_completed import JobStateCompleted
from waylay.services.registry.models.job_state_failed import JobStateFailed


from .job_state_completed_stub import JobStateCompletedStub

from .job_state_failed_stub import JobStateFailedStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class JobStateFinishedStub:
    """JobStateFinished unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> JobStateFinished:
        """Create JobStateFinished stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        # return instance of first type from `anyOf`
        return JobStateFinished(JobStateCompletedStub.create_instance(include_optional=include_optional))
