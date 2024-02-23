# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.runtime_version_summary import RuntimeVersionSummary


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.function_type import FunctionType


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class RuntimeVersionSummaryStub:
    """RuntimeVersionSummary unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> RuntimeVersionSummary:
        """Create RuntimeVersionSummary stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return RuntimeVersionSummary(
                deprecated=True,
                upgradable=True,
                version='9072888001528021798096225500850762068629339333975650685139102691291.0.0',
                title='',
                description='',
                name='',
                function_type='plugs',
                archive_format='node'
            )
        else:
            return RuntimeVersionSummary(
                deprecated=True,
                upgradable=True,
                version='9072888001528021798096225500850762068629339333975650685139102691291.0.0',
                title='',
                name='',
                function_type='plugs',
                archive_format='node'
            )
