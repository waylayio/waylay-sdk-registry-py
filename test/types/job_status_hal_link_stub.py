# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.job_status_hal_link import JobStatusHALLink

from .hal_link_stub import HALLinkStub


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from waylay.services.registry.models.hal_link import HALLink


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class JobStatusHALLinkStub:
    """JobStatusHALLink unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> JobStatusHALLink:
        """Create JobStatusHALLink stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return JobStatusHALLink(
                job=HALLinkStub.create_instance()
            )
        else:
            return JobStatusHALLink(
            )
