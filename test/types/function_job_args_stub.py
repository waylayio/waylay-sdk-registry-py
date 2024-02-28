# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.function_job_args import FunctionJobArgs


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class FunctionJobArgsStub:
    """FunctionJobArgs unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> FunctionJobArgs:
        """Create FunctionJobArgs stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return FunctionJobArgs(
                runtime_name='',
                runtime_version='9072888001528021798096225500850762068629339333975650685139102691291.0.0',
                revision=''
            )
        else:
            return FunctionJobArgs(
                runtime_name='',
                runtime_version='9072888001528021798096225500850762068629339333975650685139102691291.0.0',
            )
