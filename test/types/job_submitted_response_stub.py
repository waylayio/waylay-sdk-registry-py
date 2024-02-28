# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.job_submitted_response import JobSubmittedResponse


from .job_hal_links_stub import JobHALLinksStub

from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr
from pydantic import Field
from waylay.services.registry.models.job_hal_links import JobHALLinks


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class JobSubmittedResponseStub:
    """JobSubmittedResponse unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> JobSubmittedResponse:
        """Create JobSubmittedResponse stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return JobSubmittedResponse(
                message='',
                links=JobHALLinksStub.create_instance()
            )
        else:
            return JobSubmittedResponse(
                message='',
                links=JobHALLinksStub.create_instance()
            )
