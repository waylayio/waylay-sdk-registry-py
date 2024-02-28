# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from waylay.services.registry.models.legacy_plug_request_metadata_documentation_any_of import (
    LegacyPlugRequestMetadataDocumentationAnyOf,
)

from .documentation_property_stub import DocumentationPropertyStub

from .documentation_property_stub import DocumentationPropertyStub

from .documentation_property_stub import DocumentationPropertyStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class LegacyPlugRequestMetadataDocumentationAnyOfStub:
    """LegacyPlugRequestMetadataDocumentationAnyOf unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> LegacyPlugRequestMetadataDocumentationAnyOf:
        """Create LegacyPlugRequestMetadataDocumentationAnyOf stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return LegacyPlugRequestMetadataDocumentationAnyOf(
                supported_states=[DocumentationPropertyStub.create_instance()],
                configuration=[DocumentationPropertyStub.create_instance()],
                raw_data=[DocumentationPropertyStub.create_instance()],
            )
        else:
            return LegacyPlugRequestMetadataDocumentationAnyOf()
