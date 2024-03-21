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


class RequestOperation(str, Enum):
    """A modifying operation on the function.."""

    CREATE = "create"
    METADATA_MINUS_UPDATE = "metadata-update"
    ASSETS_MINUS_UPDATE = "assets-update"
    REBUILD = "rebuild"
    VERIFY = "verify"
    PUBLISH = "publish"
    DEPRECATE = "deprecate"
    UNDEPLOY = "undeploy"

    def __str__(self) -> str:
        return str(self.value)