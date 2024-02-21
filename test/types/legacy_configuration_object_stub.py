# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.legacy_configuration_object import LegacyConfigurationObject


from .legacy_configuration_object_format_stub import LegacyConfigurationObjectFormatStub


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from waylay.services.registry.models.legacy_configuration_object_format import LegacyConfigurationObjectFormat
from waylay.services.registry.models.plug_property_data_type import PlugPropertyDataType


class LegacyConfigurationObjectStub:
    """LegacyConfigurationObject unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> LegacyConfigurationObject:
        """Create LegacyConfigurationObject stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return LegacyConfigurationObject(
                name='',
                type='string',
                mandatory=True,
                format=LegacyConfigurationObjectFormatStub.create_instance(),
                default_value=object()
            )
        else:
            return LegacyConfigurationObject(
                name='',
                type='string',
            )
