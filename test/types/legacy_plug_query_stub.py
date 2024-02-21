# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.legacy_plug_query import LegacyPlugQuery


from .archive_format_stub import ArchiveFormatStub


from .status_filter_stub import StatusFilterStub
from .semantic_version_range_stub import SemanticVersionRangeStub


from .timestamp_spec_stub import TimestampSpecStub

from .timestamp_spec_stub import TimestampSpecStub

from .timestamp_spec_stub import TimestampSpecStub

from .timestamp_spec_stub import TimestampSpecStub


from .tags_filter_stub import TagsFilterStub


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.semantic_version_range import SemanticVersionRange
from waylay.services.registry.models.status_filter import StatusFilter
from waylay.services.registry.models.tags_filter import TagsFilter
from waylay.services.registry.models.timestamp_spec import TimestampSpec


class LegacyPlugQueryStub:
    """LegacyPlugQuery unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> LegacyPlugQuery:
        """Create LegacyPlugQuery stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return LegacyPlugQuery(
                name='',
                archive_format=['node'],
                runtime=[''],
                version='',
                status=[StatusFilterStub.create_instance()],
                runtime_version=SemanticVersionRangeStub.create_instance(),
                created_by='@me',
                updated_by='@me',
                created_before=TimestampSpecStub.create_instance(),
                created_after=TimestampSpecStub.create_instance(),
                updated_before=TimestampSpecStub.create_instance(),
                updated_after=TimestampSpecStub.create_instance(),
                include_draft=True,
                include_deprecated=True,
                page=0,
                limit=0,
                tags=TagsFilterStub.create_instance()
            )
        else:
            return LegacyPlugQuery(
            )
