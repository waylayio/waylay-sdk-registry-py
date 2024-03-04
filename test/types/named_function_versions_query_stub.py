# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from waylay.services.registry.models.named_function_versions_query import (
    NamedFunctionVersionsQuery,
)


from .status_filter_stub import StatusFilterStub
from .semantic_version_range_stub import SemanticVersionRangeStub


from .timestamp_spec_stub import TimestampSpecStub

from .timestamp_spec_stub import TimestampSpecStub

from .timestamp_spec_stub import TimestampSpecStub

from .timestamp_spec_stub import TimestampSpecStub


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class NamedFunctionVersionsQueryStub:
    """NamedFunctionVersionsQuery unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> NamedFunctionVersionsQuery:
        """Create NamedFunctionVersionsQuery stub instance.
        include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return NamedFunctionVersionsQuery(
                limit=0,
                page=0,
                deprecated=True,
                draft=True,
                version="",
                status=[StatusFilterStub.create_instance()],
                runtime_version=SemanticVersionRangeStub.create_instance(),
                created_by="@me",
                updated_by="@me",
                created_before=TimestampSpecStub.create_instance(),
                created_after=TimestampSpecStub.create_instance(),
                updated_before=TimestampSpecStub.create_instance(),
                updated_after=TimestampSpecStub.create_instance(),
                archive_format=["node"],
                runtime=[""],
            )
        else:
            return NamedFunctionVersionsQuery()
