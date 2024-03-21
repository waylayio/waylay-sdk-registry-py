# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from pydantic import Field
from typing_extensions import Annotated

from typing import (
    Union,
    Any,
    List,
    TYPE_CHECKING,
    Optional,
    Dict,
    Literal,  # >=3.8
)
from typing_extensions import (
    Annotated,  # >=3.9
)

from pydantic import StrictStr, Field, ConfigDict

TimestampAge = Union[
    Annotated[str, "An ISO8601 period expression"],
    Annotated[
        str,
        "An duration expression. A numeric value without unit is interpreted as milliseconds.",
    ],
]
"""A timestamp expressed as a age relative to now."""