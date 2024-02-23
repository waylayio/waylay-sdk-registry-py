# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.latest_plug_versions_query import LatestPlugVersionsQuery

from .tags_filter_stub import TagsFilterStub


from .status_filter_stub import StatusFilterStub
from .semantic_version_range_stub import SemanticVersionRangeStub


from .timestamp_spec_stub import TimestampSpecStub

from .timestamp_spec_stub import TimestampSpecStub

from .timestamp_spec_stub import TimestampSpecStub

from .timestamp_spec_stub import TimestampSpecStub


from .archive_format_stub import ArchiveFormatStub


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.plug_type import PlugType
from waylay.services.registry.models.semantic_version_range import SemanticVersionRange
from waylay.services.registry.models.status_filter import StatusFilter
from waylay.services.registry.models.tags_filter import TagsFilter
from waylay.services.registry.models.timestamp_spec import TimestampSpec


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class LatestPlugVersionsQueryStub:
    """LatestPlugVersionsQuery unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> LatestPlugVersionsQuery:
        """Create LatestPlugVersionsQuery stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return LatestPlugVersionsQuery(
                tags=TagsFilterStub.create_instance(),
                type='sensor',
                limit=0,
                page=0,
                include_draft=True,
                include_deprecated=True,
                deprecated=True,
                draft=True,
                name_version=['jUR,rZ#UM/?R,Fp^l6$ARj@0.0.80085076206862933933397565068513910269129173272947860148202650912727550417577019298162864882916633'],
                version='',
                status=[StatusFilterStub.create_instance()],
                runtime_version=SemanticVersionRangeStub.create_instance(),
                created_by='@me',
                updated_by='@me',
                created_before=TimestampSpecStub.create_instance(),
                created_after=TimestampSpecStub.create_instance(),
                updated_before=TimestampSpecStub.create_instance(),
                updated_after=TimestampSpecStub.create_instance(),
                name='',
                archive_format=['node'],
                runtime=[''],
                latest=True
            )
        else:
            return LatestPlugVersionsQuery(
            )
