"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.get_latest_runtimes_tags import (
        GetLatestRuntimesTags,
    )

    GetLatestRuntimesTagsAdapter = TypeAdapter(GetLatestRuntimesTags)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

get_latest_runtimes_tags_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/RuntimeTagFilter"
  }, {
    "type" : "array",
    "items" : {
      "$ref" : "#/components/schemas/RuntimeTagFilter"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
get_latest_runtimes_tags_model_schema.update({"definitions": MODEL_DEFINITIONS})

get_latest_runtimes_tags_faker = JSF(
    get_latest_runtimes_tags_model_schema, allow_none_optionals=1
)


class GetLatestRuntimesTagsStub:
    """GetLatestRuntimesTags unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return get_latest_runtimes_tags_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "GetLatestRuntimesTags":
        """Create GetLatestRuntimesTags stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                GetLatestRuntimesTagsAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return GetLatestRuntimesTagsAdapter.validate_python(
            json, context={"skip_validation": True}
        )
