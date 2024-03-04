# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from waylay.services.registry.models.legacy_plug_request_metadata import (
    LegacyPlugRequestMetadata,
)

from .legacy_required_properties_inner_stub import LegacyRequiredPropertiesInnerStub


from .legacy_plug_request_metadata_raw_data_inner_stub import (
    LegacyPlugRequestMetadataRawDataInnerStub,
)

from .legacy_configuration_object_stub import LegacyConfigurationObjectStub


from .tag_stub import TagStub


from .legacy_plug_request_metadata_documentation_stub import (
    LegacyPlugRequestMetadataDocumentationStub,
)


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class LegacyPlugRequestMetadataStub:
    """LegacyPlugRequestMetadata unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> LegacyPlugRequestMetadata:
        """Create LegacyPlugRequestMetadata stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return LegacyPlugRequestMetadata(
                required_properties=[
                    LegacyRequiredPropertiesInnerStub.create_instance()
                ],
                supported_states=[""],
                raw_data=[LegacyPlugRequestMetadataRawDataInnerStub.create_instance()],
                configuration=[LegacyConfigurationObjectStub.create_instance()],
                author="",
                description="",
                category="",
                tags=[TagStub.create_instance()],
                icon_url="",
                friendly_name="",
                documentation=LegacyPlugRequestMetadataDocumentationStub.create_instance(),
                documentation_url="",
            )
        else:
            return LegacyPlugRequestMetadata()
