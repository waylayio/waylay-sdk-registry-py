# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.kf_serving_delete_query_v1 import KFServingDeleteQueryV1


from .status_filter_stub import StatusFilterStub
from .semantic_version_range_stub import SemanticVersionRangeStub


from .timestamp_spec_stub import TimestampSpecStub

from .timestamp_spec_stub import TimestampSpecStub

from .timestamp_spec_stub import TimestampSpecStub

from .timestamp_spec_stub import TimestampSpecStub


from .archive_format_stub import ArchiveFormatStub


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.semantic_version_range import SemanticVersionRange
from waylay.services.registry.models.status_filter import StatusFilter
from waylay.services.registry.models.timestamp_spec import TimestampSpec


class KFServingDeleteQueryV1Stub:
    """KFServingDeleteQueryV1 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> KFServingDeleteQueryV1:
        """Create KFServingDeleteQueryV1 stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return KFServingDeleteQueryV1(
                var_async=True,
                limit=0,
                page=0,
                include_draft=True,
                include_deprecated=True,
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
                runtime=['']
            )
        else:
            return KFServingDeleteQueryV1(
            )
