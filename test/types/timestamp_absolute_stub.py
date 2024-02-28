# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.timestamp_absolute import TimestampAbsolute
from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from pydantic import Field


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class TimestampAbsoluteStub:
    """TimestampAbsolute unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> TimestampAbsolute:
        """Create TimestampAbsolute stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        # return instance of first type from `anyOf`
        return TimestampAbsolute(datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'))
