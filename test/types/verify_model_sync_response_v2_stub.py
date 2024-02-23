# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""


import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.verify_model_sync_response_v2 import VerifyModelSyncResponseV2


from .kfserving_response_v2_stub import KfservingResponseV2Stub

from .verify_result_stub import VerifyResultStub


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr
from waylay.services.registry.models.kfserving_response_v2 import KfservingResponseV2
from waylay.services.registry.models.verify_result import VerifyResult


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class VerifyModelSyncResponseV2Stub:
    """VerifyModelSyncResponseV2 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> VerifyModelSyncResponseV2:
        """Create VerifyModelSyncResponseV2 stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return VerifyModelSyncResponseV2(
                message='',
                entity=KfservingResponseV2Stub.create_instance(),
                result=VerifyResultStub.create_instance()
            )
        else:
            return VerifyModelSyncResponseV2(
                message='',
                entity=KfservingResponseV2Stub.create_instance(),
                result=VerifyResultStub.create_instance()
            )
