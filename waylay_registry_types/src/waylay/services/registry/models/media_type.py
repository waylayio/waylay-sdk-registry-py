# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
import re  # noqa: F401
from enum import Enum


class MediaType(str, Enum):
    """MediaType."""

    APPLICATION_SLASH_JAVASCRIPT = "application/javascript"
    APPLICATION_SLASH_JAVA_MINUS_VM = "application/java-vm"
    TEXT_SLASH_X_MINUS_PYTHON = "text/x-python"
    TEXT_SLASH_X_MINUS_GOLANG = "text/x-golang"

    def __str__(self) -> str:
        return str(self.value)
