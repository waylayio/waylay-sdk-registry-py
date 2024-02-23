# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.job_type_verify import JobTypeVerify


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class JobTypeVerifyStub:
    """JobTypeVerify unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> JobTypeVerify:
        """Create JobTypeVerify stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        return JobTypeVerify("verify")
