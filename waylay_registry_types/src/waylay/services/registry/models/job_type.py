# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations
import re  # noqa: F401
from enum import Enum


class JobType(str, Enum):
    """JobType."""

    BUILD = "build"
    DEPLOY = "deploy"
    VERIFY = "verify"
    UNDEPLOY = "undeploy"
    BATCH = "batch"
    SCALE = "scale"
    CLEANUP = "cleanup"
    NOTIFY = "notify"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
