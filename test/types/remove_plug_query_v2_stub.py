# coding: utf-8
"""Waylay Function Registry model tests.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

import json

from jsf import JSF
from pydantic import TypeAdapter

from ..openapi import MODEL_DEFINITIONS

try:
    from waylay.services.registry.models.remove_plug_query_v2 import RemovePlugQueryV2

    RemovePlugQueryV2Adapter = TypeAdapter(RemovePlugQueryV2)
    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

remove_plug_query_v2_model_schema = json.loads(r"""{
  "type" : "object",
  "properties" : {
    "comment" : {
      "type" : "string",
      "description" : "An optional user-specified comment corresponding to the operation."
    },
    "async" : {
      "type" : "boolean",
      "description" : "Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs.",
      "default" : true
    },
    "force" : {
      "type" : "boolean",
      "description" : "If <code>true</code>, the plug version(s) will be undeployed and removed. Otherwise, the plug version(s) will only be <code>deprecated</code>, i.e removed from regular listings."
    },
    "undeploy" : {
      "type" : "boolean",
      "description" : "If `true`, the `DELETE` operation\n* undeploys the (openfaas) function for the plug: it becomes no longer available for invocation.\n* does NOT remove the plug from registry: it stays in an `undeployed` status.  All assets and definitions are retained, so the plug can be restored later with a  _rebuild_ action.\n\nIf `false`, the `DELETE` operation\n* _only_ marks the plug version(s) as _deprecated_: the plug remains active but is removed from the default listings.   This also applies to _draft_ versions.\n\nThis parameter is incompatible with `force=true`.\n\nIf not set the default behaviour applies:\n* _draft_ versions are _undeployed_ and _removed_ from registry.\n* non-_draft_ versions are marked _deprecated_ only."
    }
  },
  "additionalProperties" : false
}
""")
remove_plug_query_v2_model_schema.update({"definitions": MODEL_DEFINITIONS})

remove_plug_query_v2_faker = JSF(
    remove_plug_query_v2_model_schema, allow_none_optionals=1
)


class RemovePlugQueryV2Stub:
    """RemovePlugQueryV2 unit test stubs."""

    @classmethod
    def create_json(cls):
        """Create a dict stub instance."""
        return remove_plug_query_v2_faker.generate()

    @classmethod
    def create_instance(cls) -> "RemovePlugQueryV2":
        """Create RemovePlugQueryV2 stub instance."""
        if not MODELS_AVAILABLE:
            raise ImportError("Models must be installed to create class stubs")
        return RemovePlugQueryV2Adapter.validate_python(cls.create_json())
