# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.legacy_plug_script_meta_raw_data_inner import LegacyPlugScriptMetaRawDataInner


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class LegacyPlugScriptMetaRawDataInnerStub:
    """LegacyPlugScriptMetaRawDataInner unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> LegacyPlugScriptMetaRawDataInner:
        """Create LegacyPlugScriptMetaRawDataInner stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return LegacyPlugScriptMetaRawDataInner(
                parameter='',
                data_type=''
            )
        else:
            return LegacyPlugScriptMetaRawDataInner(
                parameter='',
            )
