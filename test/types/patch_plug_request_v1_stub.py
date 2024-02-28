# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
from typing import Union, Literal, List, Dict

from waylay.services.registry.models.patch_plug_request_v1 import PatchPlugRequestV1
from .user_plug_meta_stub import UserPlugMetaStub

from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from waylay.services.registry.models.user_plug_meta import UserPlugMeta


# some mappings that are needed for some <example> interpolations
null, true, false = None, True, False


class PatchPlugRequestV1Stub:
    """PatchPlugRequestV1 unit test stubs."""

    @staticmethod
    def create_instance(
        include_optional: bool = False,
    ) -> PatchPlugRequestV1:
        """Create PatchPlugRequestV1 stub instance.
            include_optional -- if `True`, optional properties are included.
        """

        if include_optional:
            return PatchPlugRequestV1(
                metadata=UserPlugMetaStub.create_instance()
            )
        else:
            return PatchPlugRequestV1(
                metadata=UserPlugMetaStub.create_instance()
            )
