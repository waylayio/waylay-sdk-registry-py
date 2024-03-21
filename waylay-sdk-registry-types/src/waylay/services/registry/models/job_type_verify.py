# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum


from typing_extensions import (
    Self,  # >=3.11
)


class JobTypeVerify(str, Enum):
    """A job that checks the health of a deployed function.."""

    VERIFY = "verify"

    def __str__(self) -> str:
        return str(self.value)