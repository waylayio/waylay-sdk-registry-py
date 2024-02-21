# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.job_state_delayed import JobStateDelayed


class JobStateDelayedStub:
    """JobStateDelayed unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> JobStateDelayed:
        """Create JobStateDelayed stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        return JobStateDelayed("delayed")
