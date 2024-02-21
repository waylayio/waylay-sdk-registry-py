# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.error_and_status_response import ErrorAndStatusResponse


from typing import Any, ClassVar, Dict, List, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field


class ErrorAndStatusResponseStub:
    """ErrorAndStatusResponse unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> ErrorAndStatusResponse:
        """Create ErrorAndStatusResponse stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return ErrorAndStatusResponse(
                error='',
                status_code=1.337
            )
        else:
            return ErrorAndStatusResponse(
                error='',
                status_code=1.337
            )
