# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json
import warnings

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS

try:
    from waylay.services.registry.models.kf_serving_latest_version_query_v2 import (
        KFServingLatestVersionQueryV2,
    )

    KFServingLatestVersionQueryV2Adapter = TypeAdapter(KFServingLatestVersionQueryV2)
    MODELS_AVAILABLE = True
except ImportError as exc:
    warnings.warn(
        f"Type adapter for KFServingLatestVersionQueryV2 not available: {exc}"
    )
    MODELS_AVAILABLE = False

kf_serving_latest_version_query_v2_model_schema = json.loads(r"""{
  "type" : "object",
  "properties" : {
    "includeDraft" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**."
    },
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**."
    }
  },
  "additionalProperties" : false,
  "description" : "Named Model latest version query."
}
""")
kf_serving_latest_version_query_v2_model_schema.update(
    {"definitions": MODEL_DEFINITIONS}
)

kf_serving_latest_version_query_v2_faker = JSF(
    kf_serving_latest_version_query_v2_model_schema, allow_none_optionals=1
)


class KFServingLatestVersionQueryV2Stub:
    """KFServingLatestVersionQueryV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return kf_serving_latest_version_query_v2_faker.generate()

    @classmethod
    def create_instance(cls) -> "KFServingLatestVersionQueryV2":
        """Create KFServingLatestVersionQueryV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return KFServingLatestVersionQueryV2Adapter.validate_python(cls.create_json())
