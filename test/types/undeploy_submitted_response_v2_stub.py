# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.undeploy_submitted_response_v2 import UndeploySubmittedResponseV2


from .job_hal_links_stub import JobHALLinksStub


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from waylay.services.registry.models.job_hal_links import JobHALLinks


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class UndeploySubmittedResponseV2Stub:
    """UndeploySubmittedResponseV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> UndeploySubmittedResponseV2:
        """Create UndeploySubmittedResponseV2 stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return UndeploySubmittedResponseV2(
                message='',
                links=JobHALLinksStub.create_instance(),
                versions=['9072888001528021798096225500850762068629339333975650685139102691291.0.0']
            )
        else:
            return UndeploySubmittedResponseV2(
                message='',
                links=JobHALLinksStub.create_instance(),
                versions=['9072888001528021798096225500850762068629339333975650685139102691291.0.0']
            )
