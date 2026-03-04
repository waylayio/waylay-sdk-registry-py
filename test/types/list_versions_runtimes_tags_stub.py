"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.list_versions_runtimes_tags import (
        ListVersionsRuntimesTags,
    )

    ListVersionsRuntimesTagsAdapter = TypeAdapter(ListVersionsRuntimesTags)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

list_versions_runtimes_tags_model_schema = json.loads(
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
list_versions_runtimes_tags_model_schema.update({"definitions": MODEL_DEFINITIONS})

list_versions_runtimes_tags_faker = JSF(
    list_versions_runtimes_tags_model_schema, allow_none_optionals=1
)


class ListVersionsRuntimesTagsStub:
    """ListVersionsRuntimesTags unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return list_versions_runtimes_tags_faker.generate(
            use_defaults=True, use_examples=True
        )

    @classmethod
    def create_instance(cls) -> "ListVersionsRuntimesTags":
        """Create ListVersionsRuntimesTags stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ListVersionsRuntimesTagsAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ListVersionsRuntimesTagsAdapter.validate_python(
            json, context={"skip_validation": True}
        )
