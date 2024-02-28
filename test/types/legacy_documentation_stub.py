# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.legacy_documentation import LegacyDocumentation

from .documentation_property_stub import DocumentationPropertyStub

from .documentation_property_stub import DocumentationPropertyStub

from .documentation_property_stub import DocumentationPropertyStub
from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from pydantic import Field
from waylay.services.registry.models.documentation_property import DocumentationProperty


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class LegacyDocumentationStub:
    """LegacyDocumentation unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> LegacyDocumentation:
        """Create LegacyDocumentation stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return LegacyDocumentation(
                supported_states=[DocumentationPropertyStub.create_instance()],
                configuration=[DocumentationPropertyStub.create_instance()],
                raw_data=[DocumentationPropertyStub.create_instance()]
            )
        else:
            return LegacyDocumentation(
                supported_states=[DocumentationPropertyStub.create_instance()],
                configuration=[DocumentationPropertyStub.create_instance()],
                raw_data=[DocumentationPropertyStub.create_instance()]
            )
