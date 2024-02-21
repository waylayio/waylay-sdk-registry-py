# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.job_status_progress import JobStatusProgress


from typing import Any, Dict, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, ValidationError, field_validator


class JobStatusProgressStub:
    """JobStatusProgress unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> JobStatusProgress:
        """Create JobStatusProgress stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        # return instance of first type from `anyOf`
        return JobStatusProgress(float(1.337))
