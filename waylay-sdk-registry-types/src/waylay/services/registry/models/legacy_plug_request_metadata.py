# coding: utf-8
"""Waylay Function Registry models.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.

"""

from __future__ import annotations

from typing import List

from pydantic import (
    ConfigDict,
    Field,
    StrictStr,
)
from waylay.sdk.api._models import BaseModel as WaylayBaseModel

from ..models.legacy_configuration_object import LegacyConfigurationObject
from ..models.legacy_plug_request_metadata_documentation import (
    LegacyPlugRequestMetadataDocumentation,
)
from ..models.legacy_plug_request_metadata_raw_data_inner import (
    LegacyPlugRequestMetadataRawDataInner,
)
from ..models.legacy_required_properties_inner import LegacyRequiredPropertiesInner
from ..models.tag import Tag


class LegacyPlugRequestMetadata(WaylayBaseModel):
    """LegacyPlugRequestMetadata."""

    required_properties: List[LegacyRequiredPropertiesInner] | None = Field(
        default=None, alias="requiredProperties"
    )
    supported_states: List[StrictStr] | None = Field(
        default=None, alias="supportedStates"
    )
    raw_data: List[LegacyPlugRequestMetadataRawDataInner] | None = Field(
        default=None, alias="rawData"
    )
    configuration: List[LegacyConfigurationObject] | None = None
    author: StrictStr | None = None
    description: StrictStr | None = None
    category: StrictStr | None = None
    tags: List[Tag] | None = None
    icon_url: StrictStr | None = Field(default=None, alias="iconURL")
    friendly_name: StrictStr | None = Field(default=None, alias="friendlyName")
    documentation: LegacyPlugRequestMetadataDocumentation | None = None
    documentation_url: StrictStr | None = Field(default=None, alias="documentationURL")

    model_config = ConfigDict(
        populate_by_name=True, protected_namespaces=(), extra="ignore"
    )
