# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from waylay.services.registry.models.legacy_plug_script_meta import LegacyPlugScriptMeta


from .tag_stub import TagStub


from .legacy_plug_script_meta_raw_data_inner_stub import (
    LegacyPlugScriptMetaRawDataInnerStub,
)

from .legacy_required_properties_inner_stub import LegacyRequiredPropertiesInnerStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class LegacyPlugScriptMetaStub:
    """LegacyPlugScriptMeta unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> LegacyPlugScriptMeta:
        """Create LegacyPlugScriptMeta stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return LegacyPlugScriptMeta(
                author="",
                description="",
                category="",
                tags=[TagStub.create_instance()],
                icon_url="",
                friendly_name="",
                supported_states=[""],
                raw_data=[LegacyPlugScriptMetaRawDataInnerStub.create_instance()],
                required_properties=[
                    LegacyRequiredPropertiesInnerStub.create_instance()
                ],
            )
        else:
            return LegacyPlugScriptMeta(
                supported_states=[""],
                raw_data=[LegacyPlugScriptMetaRawDataInnerStub.create_instance()],
            )
