"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.list_runtimes_tags import ListRuntimesTags

    ListRuntimesTagsAdapter = TypeAdapter(ListRuntimesTags)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

list_runtimes_tags_model_schema = json.loads(
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
list_runtimes_tags_model_schema.update({"definitions": MODEL_DEFINITIONS})

list_runtimes_tags_faker = JSF(list_runtimes_tags_model_schema, allow_none_optionals=1)


class ListRuntimesTagsStub:
    """ListRuntimesTags unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return list_runtimes_tags_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "ListRuntimesTags":
        """Create ListRuntimesTags stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(
                ListRuntimesTagsAdapter.json_schema(), allow_none_optionals=1
            )
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return ListRuntimesTagsAdapter.validate_python(
            json, context={"skip_validation": True}
        )
