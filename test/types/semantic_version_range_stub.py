# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


from waylay.services.registry.models.semantic_version_range import SemanticVersionRange


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class SemanticVersionRangeStub:
    """SemanticVersionRange unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> SemanticVersionRange:
        """Create SemanticVersionRange stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        # return instance of first type from `anyOf`
        return SemanticVersionRange(str(""))
