# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.latest_plugs_response_v2_entities_inner import LatestPlugsResponseV2EntitiesInner

from .alt_version_hal_link_stub import AltVersionHALLinkStub


from .update_record_stub import UpdateRecordStub


from .failure_reason_stub import FailureReasonStub

from .runtime_attributes_stub import RuntimeAttributesStub


from .plug_manifest_stub import PlugManifestStub


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from waylay.services.registry.models.alt_version_hal_link import AltVersionHALLink
from waylay.services.registry.models.failure_reason import FailureReason
from waylay.services.registry.models.plug_manifest import PlugManifest
from waylay.services.registry.models.runtime_attributes import RuntimeAttributes
from waylay.services.registry.models.status import Status
from waylay.services.registry.models.update_record import UpdateRecord


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class LatestPlugsResponseV2EntitiesInnerStub:
    """LatestPlugsResponseV2EntitiesInner unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> LatestPlugsResponseV2EntitiesInner:
        """Create LatestPlugsResponseV2EntitiesInner stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return LatestPlugsResponseV2EntitiesInner(
                links=AltVersionHALLinkStub.create_instance(),
                created_by='',
                created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_by='',
                updated_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updates=[UpdateRecordStub.create_instance()],
                status='registered',
                failure_reason=FailureReasonStub.create_instance(),
                runtime=RuntimeAttributesStub.create_instance(),
                deprecated=True,
                draft=True,
                plug=PlugManifestStub.create_instance()
            )
        else:
            return LatestPlugsResponseV2EntitiesInner(
                links=AltVersionHALLinkStub.create_instance(),
                created_by='',
                created_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_by='',
                updated_at=datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updates=[UpdateRecordStub.create_instance()],
                status='registered',
                runtime=RuntimeAttributesStub.create_instance(),
                deprecated=True,
                draft=True,
                plug=PlugManifestStub.create_instance()
            )
