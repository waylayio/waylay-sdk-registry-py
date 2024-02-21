# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.job_and_function_hal_link import JobAndFunctionHALLink

from .hal_link_stub import HALLinkStub

from .hal_link_stub import HALLinkStub

from .hal_link_stub import HALLinkStub

from .hal_link_stub import HALLinkStub

from .hal_link_stub import HALLinkStub


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from waylay.services.registry.models.job_hal_links import JobHALLinks
from waylay.services.registry.models.model1 import Model1
from waylay.services.registry.models.plug1 import Plug1
from waylay.services.registry.models.webscript1 import Webscript1


from .plug1_stub import Plug1Stub

from .webscript1_stub import Webscript1Stub

from .model1_stub import Model1Stub

from .job_hal_links_stub import JobHALLinksStub


class JobAndFunctionHALLinkStub:
    """JobAndFunctionHALLink unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> JobAndFunctionHALLink:
        """Create JobAndFunctionHALLink stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        # return instance of first type from `anyOf`
        return JobAndFunctionHALLink(Plug1Stub.create_instance(include_optional=include_optional))
