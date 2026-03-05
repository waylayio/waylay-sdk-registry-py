"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS, with_example_provider

try:
    from waylay.services.registry.models.ihal_link import IHALLink

    IHALLinkAdapter = TypeAdapter(IHALLink)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

ihal_link_model_schema = json.loads(
    r"""{
  "required" : [ "href" ],
  "type" : "object",
  "properties" : {
    "href" : {
      "$ref" : "#/components/schemas/IHALLink_href"
    }
  }
}
""",
    object_hook=with_example_provider,
)
ihal_link_model_schema.update({"definitions": MODEL_DEFINITIONS})

ihal_link_faker = JSF(ihal_link_model_schema, allow_none_optionals=1)


class IHALLinkStub:
    """IHALLink unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return ihal_link_faker.generate(use_defaults=True, use_examples=True)

    @classmethod
    def create_instance(cls) -> "IHALLink":
        """Create IHALLink stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        json = cls.create_json()
        if json is None:
            # use backup example based on the pydantic model schema
            backup_faker = JSF(IHALLinkAdapter.json_schema(), allow_none_optionals=1)
            json = backup_faker.generate(use_defaults=True, use_examples=True)
        return IHALLinkAdapter.validate_python(json, context={"skip_validation": True})
