# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import datetime
import json
import warnings

from typing import (
    Union,
    List,
    Dict,
    Literal,  # >=3.8
)
from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.with_embedded_alt_versions_i_kfserving_response_v2 import (
        WithEmbeddedAltVersionsIKfservingResponseV2,
    )

    WithEmbeddedAltVersionsIKfservingResponseV2Adapter = TypeAdapter(
        WithEmbeddedAltVersionsIKfservingResponseV2
    )
    MODELS_AVAILABLE = True
except ImportError as exc:
    MODELS_AVAILABLE = False

with_embedded_alt_versions_i_kfserving_response_v2__model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "_embedded" : {
      "$ref" : "#/components/schemas/AltEmbeddedVersion_IKfservingResponseV2_"
    }
  }
}
""",
    object_hook=with_example_provider,
)
with_embedded_alt_versions_i_kfserving_response_v2__model_schema.update(
    {"definitions": MODEL_DEFINITIONS}
)

with_embedded_alt_versions_i_kfserving_response_v2__faker = JSF(
    with_embedded_alt_versions_i_kfserving_response_v2__model_schema,
    allow_none_optionals=1,
)


class WithEmbeddedAltVersionsIKfservingResponseV2Stub:
    """WithEmbeddedAltVersionsIKfservingResponseV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return with_embedded_alt_versions_i_kfserving_response_v2__faker.generate()

    @classmethod
    def create_instance(cls) -> "WithEmbeddedAltVersionsIKfservingResponseV2":
        """Create WithEmbeddedAltVersionsIKfservingResponseV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return WithEmbeddedAltVersionsIKfservingResponseV2Adapter.validate_python(
            cls.create_json()
        )
