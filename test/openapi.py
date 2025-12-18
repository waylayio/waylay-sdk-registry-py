import json

import yaml


def with_example_provider(dct):
    has_example = False
    if "example" in dct:
        example, has_example = dct["example"], True
    elif "examples" in dct:
        examples = dct["examples"]
        if isinstance(examples, list) and list:
            example, has_example = examples[0], True
    elif "default" in dct:
        example, has_example = dct["default"], True

    if has_example:
        provider = (
            example
            if example is None or isinstance(example, (dict, list, int, float, bool))
            else f"'{example}'"
        )
        dct.update({"$provider": f"lambda: {provider}"})
    return dct


with open("openapi/registry.transformed.openapi.yaml", "r") as file:
    OPENAPI_SPEC = yaml.safe_load(file)

MODEL_DEFINITIONS = OPENAPI_SPEC["components"]["schemas"]

_active_event_data_model_schema = json.loads(
    r"""{
  "title" : "ActiveEventData",
  "type" : "object",
  "properties" : {
    "prev" : {
      "$ref" : "#/components/schemas/QueueEvents"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ActiveEventData": _active_event_data_model_schema})

_active_event_sse_model_schema = json.loads(
    r"""{
  "required" : [ "data", "event" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/ActiveEventSSE_event"
    },
    "data" : {
      "$ref" : "#/components/schemas/JobEventResponse_ActiveEventData_"
    }
  },
  "description" : "A message that notifies a state change in a background job."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ActiveEventSSE": _active_event_sse_model_schema})

_active_event_sse_event_model_schema = json.loads(
    r"""{
  "title" : "ActiveEventSSE_event",
  "type" : "string",
  "description" : "The job queue event that trigged this message",
  "enum" : [ "active" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ActiveEventSSE_event": _active_event_sse_event_model_schema})

_alt_embedded_version_i_kfserving_response_v2__model_schema = json.loads(
    r"""{
  "title" : "AltEmbeddedVersion_IKfservingResponseV2_",
  "type" : "object",
  "properties" : {
    "draft" : {
      "$ref" : "#/components/schemas/KfservingResponseV2"
    },
    "published" : {
      "$ref" : "#/components/schemas/KfservingResponseV2"
    }
  },
  "description" : "Embedded representations of the _latest_ draft/published versions."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "AltEmbeddedVersion_IKfservingResponseV2_": _alt_embedded_version_i_kfserving_response_v2__model_schema
})

_alt_embedded_version_i_plug_response_v2__model_schema = json.loads(
    r"""{
  "title" : "AltEmbeddedVersion_IPlugResponseV2_",
  "type" : "object",
  "properties" : {
    "draft" : {
      "$ref" : "#/components/schemas/PlugResponseV2"
    },
    "published" : {
      "$ref" : "#/components/schemas/PlugResponseV2"
    }
  },
  "description" : "Embedded representations of the _latest_ draft/published versions."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "AltEmbeddedVersion_IPlugResponseV2_": _alt_embedded_version_i_plug_response_v2__model_schema
})

_alt_embedded_version_i_webscript_response_with_invoke_link_v2__model_schema = (
    json.loads(
        r"""{
  "title" : "AltEmbeddedVersion_IWebscriptResponseWithInvokeLinkV2_",
  "type" : "object",
  "properties" : {
    "draft" : {
      "$ref" : "#/components/schemas/WebscriptResponseWithInvokeLinkV2"
    },
    "published" : {
      "$ref" : "#/components/schemas/WebscriptResponseWithInvokeLinkV2"
    }
  },
  "description" : "Embedded representations of the _latest_ draft/published versions."
}
""",
        object_hook=with_example_provider,
    )
)
MODEL_DEFINITIONS.update({
    "AltEmbeddedVersion_IWebscriptResponseWithInvokeLinkV2_": _alt_embedded_version_i_webscript_response_with_invoke_link_v2__model_schema
})

_alt_version_hal_link_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "draft" : {
      "$ref" : "#/components/schemas/AltVersionHALLink_draft"
    },
    "published" : {
      "$ref" : "#/components/schemas/AltVersionHALLink_published"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AltVersionHALLink": _alt_version_hal_link_model_schema})

_alt_version_hal_link_draft_model_schema = json.loads(
    r"""{
  "title" : "AltVersionHALLink_draft",
  "required" : [ "deprecated", "draft", "href", "version" ],
  "type" : "object",
  "properties" : {
    "draft" : {
      "type" : "boolean"
    },
    "href" : {
      "$ref" : "#/components/schemas/HALLink_href"
    },
    "version" : {
      "type" : "string"
    },
    "deprecated" : {
      "type" : "boolean"
    }
  },
  "description" : "Link to the lastest draft version.",
  "example" : {
    "href" : "https://api.waylay.io/registry/v2/models/modelName/versions/1.0.1",
    "version" : "1.0.1",
    "draft" : true,
    "deprecated" : false
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "AltVersionHALLink_draft": _alt_version_hal_link_draft_model_schema
})

_alt_version_hal_link_published_model_schema = json.loads(
    r"""{
  "title" : "AltVersionHALLink_published",
  "required" : [ "deprecated", "draft", "href", "version" ],
  "type" : "object",
  "properties" : {
    "draft" : {
      "type" : "boolean"
    },
    "href" : {
      "$ref" : "#/components/schemas/HALLink_href"
    },
    "version" : {
      "type" : "string"
    },
    "deprecated" : {
      "type" : "boolean"
    }
  },
  "description" : "Link to the lastest published version.",
  "example" : {
    "href" : "https://api.waylay.io/registry/v2/models/modelName/versions/1.0.1",
    "version" : "1.2.0",
    "draft" : false,
    "deprecated" : false
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "AltVersionHALLink_published": _alt_version_hal_link_published_model_schema
})

_any_job_for_function_model_schema = json.loads(
    r"""{
  "title" : "AnyJobForFunction",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Build"
  }, {
    "$ref" : "#/components/schemas/Deploy"
  }, {
    "$ref" : "#/components/schemas/Verify"
  }, {
    "$ref" : "#/components/schemas/Undeploy"
  }, {
    "$ref" : "#/components/schemas/Scale"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AnyJobForFunction": _any_job_for_function_model_schema})

_any_job_result_model_schema = json.loads(
    r"""{
  "title" : "AnyJobResult",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/BuildResult"
  }, {
    "$ref" : "#/components/schemas/DeployResult"
  }, {
    "$ref" : "#/components/schemas/VerifyResult"
  }, {
    "$ref" : "#/components/schemas/UndeployResult"
  }, {
    "$ref" : "#/components/schemas/ScaleResult"
  }, {
    "$ref" : "#/components/schemas/BatchResult"
  }, {
    "$ref" : "#/components/schemas/CleanupResult"
  }, {
    "$ref" : "#/components/schemas/NotifyResult"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AnyJobResult": _any_job_result_model_schema})

_any_job_status_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/BuildJobStatus"
  }, {
    "$ref" : "#/components/schemas/DeployJobStatus"
  }, {
    "$ref" : "#/components/schemas/VerifyJobStatus"
  }, {
    "$ref" : "#/components/schemas/UndeployJobStatus"
  }, {
    "$ref" : "#/components/schemas/ScaleJobStatus"
  }, {
    "$ref" : "#/components/schemas/BatchJobStatus"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AnyJobStatus": _any_job_status_model_schema})

_any_job_status_summary_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Build_1"
  }, {
    "$ref" : "#/components/schemas/Deploy_1"
  }, {
    "$ref" : "#/components/schemas/Verify_1"
  }, {
    "$ref" : "#/components/schemas/Undeploy_1"
  }, {
    "$ref" : "#/components/schemas/Scale_1"
  }, {
    "$ref" : "#/components/schemas/Batch"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AnyJobStatusSummary": _any_job_status_summary_model_schema})

_archive_format_model_schema = json.loads(
    r"""{
  "title" : "ArchiveFormat",
  "type" : "string",
  "enum" : [ "node", "python", "golang", "byoml", "native" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ArchiveFormat": _archive_format_model_schema})

_archive_format_exclude_model_schema = json.loads(
    r"""{
  "title" : "ArchiveFormatExclude",
  "type" : "string",
  "enum" : [ "node-", "python-", "golang-", "byoml-", "native-" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ArchiveFormatExclude": _archive_format_exclude_model_schema})

_archive_format_filter_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/ArchiveFormat"
  }, {
    "$ref" : "#/components/schemas/ArchiveFormatExclude"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ArchiveFormatFilter": _archive_format_filter_model_schema})

_asset_condition_model_schema = json.loads(
    r"""{
  "title" : "AssetCondition",
  "required" : [ "pattern", "role" ],
  "type" : "object",
  "properties" : {
    "title" : {
      "title" : "title",
      "type" : "string"
    },
    "description" : {
      "title" : "description",
      "type" : "string"
    },
    "role" : {
      "$ref" : "#/components/schemas/AssetRole"
    },
    "pattern" : {
      "$ref" : "#/components/schemas/AssetCondition_pattern"
    },
    "contentType" : {
      "$ref" : "#/components/schemas/AssetCondition_contentType"
    },
    "min" : {
      "title" : "min",
      "type" : "number",
      "description" : "The minimal number of files that must match this pattern. Use `0` for an optional file.",
      "example" : 0
    },
    "max" : {
      "title" : "max",
      "type" : "number",
      "description" : "The maximal number of files that can match this pattern. Use `0` for a disallowed file. This condition only raises an error if there are no other conditions that",
      "example" : 1
    },
    "maxSize" : {
      "title" : "maxSize",
      "type" : "string",
      "description" : "The maximum size for each file matching this pattern (in bytes, unless unit is provided)"
    },
    "schema" : {
      "title" : "schema",
      "description" : "The json schema validator that applies (in case of `application/json` entries)."
    }
  },
  "description" : "Describes conditions on the set of files that match a file pattern."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AssetCondition": _asset_condition_model_schema})

_asset_condition_content_type_model_schema = json.loads(
    r"""{
  "title" : "AssetCondition_contentType",
  "description" : "Allowed content type(s) of matching files.",
  "anyOf" : [ {
    "type" : "string"
  }, {
    "type" : "array",
    "items" : {
      "type" : "string"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "AssetCondition_contentType": _asset_condition_content_type_model_schema
})

_asset_condition_pattern_model_schema = json.loads(
    r"""{
  "title" : "AssetCondition_pattern",
  "description" : "Pattern that selects a file in a function archive",
  "anyOf" : [ {
    "type" : "string"
  }, {
    "type" : "array",
    "items" : {
      "type" : "string"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "AssetCondition_pattern": _asset_condition_pattern_model_schema
})

_asset_role_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Classification of assets with regard to their role.",
  "enum" : [ "manifest", "project", "main", "lib", "script", "other" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AssetRole": _asset_role_model_schema})

_asset_summary_with_hal_link_model_schema = json.loads(
    r"""{
  "title" : "AssetSummaryWithHALLink",
  "required" : [ "_links", "name" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/AssetSummaryWithHALLink__links"
    },
    "name" : {
      "title" : "name",
      "type" : "string",
      "description" : "File name"
    },
    "title" : {
      "title" : "title",
      "type" : "string"
    },
    "description" : {
      "title" : "description",
      "type" : "string"
    },
    "role" : {
      "$ref" : "#/components/schemas/AssetRole"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "AssetSummaryWithHALLink": _asset_summary_with_hal_link_model_schema
})

_asset_summary_with_hal_link__links_model_schema = json.loads(
    r"""{
  "title" : "AssetSummaryWithHALLink__links",
  "required" : [ "asset" ],
  "type" : "object",
  "properties" : {
    "asset" : {
      "$ref" : "#/components/schemas/HALLinks"
    }
  },
  "description" : "HAL links to the asset"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "AssetSummaryWithHALLink__links": _asset_summary_with_hal_link__links_model_schema
})

_assets_conditions_model_schema = json.loads(
    r"""{
  "title" : "AssetsConditions",
  "type" : "object",
  "properties" : {
    "conditions" : {
      "title" : "conditions",
      "type" : "array",
      "description" : "All files in a function archive are checked against these conditions. A file that is not matched is ignored.",
      "items" : {
        "$ref" : "#/components/schemas/AssetCondition"
      }
    },
    "maxSize" : {
      "title" : "maxSize",
      "type" : "string",
      "description" : "The maximum size of the archive (in bytes, unless unit is provided)"
    }
  },
  "description" : "Describes the assets that are required/allowed/supported for a function."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AssetsConditions": _assets_conditions_model_schema})

_batch_model_schema = json.loads(
    r"""{
  "title" : "Batch",
  "required" : [ "createdAt", "createdBy", "id", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "The type of operation that was executed."
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user identity that was used to execute the job."
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp of when the job was created.",
      "format" : "date-time"
    },
    "processedAt" : {
      "title" : "processedAt",
      "type" : "string",
      "description" : "The timestamp of when the job has begun processing.",
      "format" : "date-time"
    },
    "finishedAt" : {
      "title" : "finishedAt",
      "description" : "The timestamp of when the job has finished processing."
    },
    "attemptsMade" : {
      "title" : "attemptsMade",
      "type" : "number",
      "description" : "The number of retries that were attempted."
    },
    "type" : {
      "$ref" : "#/components/schemas/BatchJobStatus_type"
    },
    "id" : {
      "title" : "id",
      "type" : "string",
      "description" : "The id of the background job, or the constant `_unknown_`"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Batch": _batch_model_schema})

_batch_args_model_schema = json.loads(
    r"""{
  "title" : "BatchArgs",
  "required" : [ "functionType", "plugName" ],
  "type" : "object",
  "properties" : {
    "plugName" : {
      "title" : "plugName",
      "type" : "string"
    },
    "functionType" : {
      "$ref" : "#/components/schemas/FunctionType"
    },
    "childType" : {
      "title" : "childType",
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BatchArgs": _batch_args_model_schema})

_batch_job_status_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "job", "operation", "request", "state", "type" ],
  "type" : "object",
  "properties" : {
    "operation" : {
      "type" : "string",
      "description" : "The type of operation that was executed."
    },
    "createdBy" : {
      "type" : "string",
      "description" : "The user identity that was used to execute the job."
    },
    "createdAt" : {
      "type" : "string",
      "description" : "The timestamp of when the job was created.",
      "format" : "date-time"
    },
    "processedAt" : {
      "type" : "string",
      "description" : "The timestamp of when the job has begun processing.",
      "format" : "date-time"
    },
    "finishedAt" : {
      "description" : "The timestamp of when the job has finished processing."
    },
    "attemptsMade" : {
      "type" : "number",
      "description" : "The number of retries that were attempted."
    },
    "type" : {
      "$ref" : "#/components/schemas/BatchJobStatus_type"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "request" : {
      "$ref" : "#/components/schemas/BatchArgs"
    },
    "result" : {
      "$ref" : "#/components/schemas/BatchResult"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobStatus"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BatchJobStatus": _batch_job_status_model_schema})

_batch_job_status_type_model_schema = json.loads(
    r"""{
  "title" : "BatchJobStatus_type",
  "type" : "string",
  "description" : "The type of the background task.",
  "enum" : [ "batch" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BatchJobStatus_type": _batch_job_status_type_model_schema})

_batch_result_model_schema = json.loads(
    r"""{
  "title" : "BatchResult",
  "type" : "object",
  "properties" : {
    "jobCount" : {
      "title" : "jobCount",
      "type" : "number"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BatchResult": _batch_result_model_schema})

_build_model_schema = json.loads(
    r"""{
  "title" : "Build",
  "required" : [ "createdAt", "createdBy", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    },
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "The type of operation that was executed."
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user identity that was used to execute the job."
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp of when the job was created.",
      "format" : "date-time"
    },
    "processedAt" : {
      "title" : "processedAt",
      "type" : "string",
      "description" : "The timestamp of when the job has begun processing.",
      "format" : "date-time"
    },
    "finishedAt" : {
      "title" : "finishedAt",
      "description" : "The timestamp of when the job has finished processing."
    },
    "attemptsMade" : {
      "title" : "attemptsMade",
      "type" : "number",
      "description" : "The number of retries that were attempted."
    },
    "type" : {
      "$ref" : "#/components/schemas/Build_type"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "request" : {
      "$ref" : "#/components/schemas/BuildArgs"
    },
    "result" : {
      "$ref" : "#/components/schemas/BuildResult"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobStatus"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Build": _build_model_schema})

_build_1_model_schema = json.loads(
    r"""{
  "title" : "Build",
  "required" : [ "createdAt", "createdBy", "id", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "The type of operation that was executed."
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user identity that was used to execute the job."
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp of when the job was created.",
      "format" : "date-time"
    },
    "processedAt" : {
      "title" : "processedAt",
      "type" : "string",
      "description" : "The timestamp of when the job has begun processing.",
      "format" : "date-time"
    },
    "finishedAt" : {
      "title" : "finishedAt",
      "description" : "The timestamp of when the job has finished processing."
    },
    "attemptsMade" : {
      "title" : "attemptsMade",
      "type" : "number",
      "description" : "The number of retries that were attempted."
    },
    "type" : {
      "$ref" : "#/components/schemas/Build_type"
    },
    "id" : {
      "title" : "id",
      "type" : "string",
      "description" : "The id of the background job, or the constant `_unknown_`"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobAndFunctionHALLink"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Build_1": _build_1_model_schema})

_build_args_model_schema = json.loads(
    r"""{
  "title" : "BuildArgs",
  "required" : [ "args", "imageName", "revision", "runtimeName", "runtimeVersion", "storageLocation" ],
  "type" : "object",
  "properties" : {
    "storageLocation" : {
      "title" : "storageLocation",
      "type" : "string",
      "description" : "Location of the function assets."
    },
    "imageName" : {
      "title" : "imageName",
      "type" : "string",
      "description" : "The container image name for the target function."
    },
    "runtimeName" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "revision" : {
      "title" : "revision",
      "type" : "string",
      "description" : "The revision hash of the current (draft) function revision"
    },
    "args" : {
      "title" : "args",
      "type" : "object",
      "additionalProperties" : {
        "type" : "string"
      },
      "description" : "Parameters to the runtime configuration."
    }
  },
  "description" : "Input arguments to a job that builds a function."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BuildArgs": _build_args_model_schema})

_build_job_status_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "job", "operation", "request", "state", "type" ],
  "type" : "object",
  "properties" : {
    "operation" : {
      "type" : "string",
      "description" : "The type of operation that was executed."
    },
    "createdBy" : {
      "type" : "string",
      "description" : "The user identity that was used to execute the job."
    },
    "createdAt" : {
      "type" : "string",
      "description" : "The timestamp of when the job was created.",
      "format" : "date-time"
    },
    "processedAt" : {
      "type" : "string",
      "description" : "The timestamp of when the job has begun processing.",
      "format" : "date-time"
    },
    "finishedAt" : {
      "description" : "The timestamp of when the job has finished processing."
    },
    "attemptsMade" : {
      "type" : "number",
      "description" : "The number of retries that were attempted."
    },
    "type" : {
      "$ref" : "#/components/schemas/Build_type"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "request" : {
      "$ref" : "#/components/schemas/BuildArgs"
    },
    "result" : {
      "$ref" : "#/components/schemas/BuildResult"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobStatus"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BuildJobStatus": _build_job_status_model_schema})

_build_result_model_schema = json.loads(
    r"""{
  "title" : "BuildResult",
  "required" : [ "digest" ],
  "type" : "object",
  "properties" : {
    "digest" : {
      "title" : "digest",
      "type" : "string",
      "description" : "SHA digest of the built image."
    },
    "log" : {
      "title" : "log",
      "type" : "array",
      "description" : "Detailed logs of the build steps.",
      "items" : {
        "type" : "string"
      }
    },
    "status" : {
      "title" : "status",
      "type" : "string",
      "description" : "Outcome of the build."
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BuildResult": _build_result_model_schema})

_build_spec_model_schema = json.loads(
    r"""{
  "title" : "BuildSpec",
  "required" : [ "args", "context" ],
  "type" : "object",
  "properties" : {
    "context" : {
      "title" : "context",
      "type" : "string"
    },
    "file" : {
      "title" : "file",
      "type" : "string"
    },
    "args" : {
      "title" : "args",
      "type" : "object",
      "additionalProperties" : {
        "type" : "string"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"BuildSpec": _build_spec_model_schema})

_build_type_model_schema = json.loads(
    r"""{
  "title" : "Build_type",
  "type" : "string",
  "description" : "The type of the background task.",
  "enum" : [ "build" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Build_type": _build_type_model_schema})

_cleanup_result_model_schema = json.loads(
    r"""{
  "title" : "CleanupResult",
  "type" : "object",
  "properties" : {
    "scheduledJob" : {
      "$ref" : "#/components/schemas/JobReference"
    }
  },
  "description" : "The result data for a completed cleanup job."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"CleanupResult": _cleanup_result_model_schema})

_compiled_runtime_version_model_schema = json.loads(
    r"""{
  "title" : "CompiledRuntimeVersion",
  "required" : [ "archiveFormat", "deprecated", "functionType", "name", "title", "upgradable", "version" ],
  "type" : "object",
  "properties" : {
    "deprecated" : {
      "title" : "deprecated",
      "type" : "boolean",
      "description" : "If true, this runtime should no longer be used for new functions."
    },
    "upgradable" : {
      "title" : "upgradable",
      "type" : "boolean",
      "description" : "If true, a newer runtime for this function is available using the `rebuild` API."
    },
    "name" : {
      "$ref" : "#/components/schemas/TagReference"
    },
    "functionType" : {
      "$ref" : "#/components/schemas/FunctionType"
    },
    "archiveFormat" : {
      "$ref" : "#/components/schemas/ArchiveFormat"
    },
    "build" : {
      "$ref" : "#/components/schemas/BuildSpec"
    },
    "deploy" : {
      "$ref" : "#/components/schemas/DeploySpec"
    },
    "language" : {
      "$ref" : "#/components/schemas/LanguageRelease"
    },
    "providedDependencies" : {
      "title" : "providedDependencies",
      "type" : "array",
      "description" : "Description of dependencies provided by this runtime version.",
      "items" : {
        "$ref" : "#/components/schemas/ProvidedDependency"
      }
    },
    "assets" : {
      "$ref" : "#/components/schemas/AssetsConditions"
    },
    "invocation" : {
      "$ref" : "#/components/schemas/InvocationAttributes"
    },
    "tags" : {
      "title" : "tags",
      "type" : "array",
      "description" : "Tags used for grouping or filtering.",
      "items" : {
        "$ref" : "#/components/schemas/TagReference"
      }
    },
    "title" : {
      "title" : "title",
      "type" : "string"
    },
    "description" : {
      "title" : "description",
      "type" : "string"
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    }
  },
  "description" : "Compiled build and deployment information for a runtime version. Contains all defaults applied on the _global_, _functionType_, _archiveFormat_, _runtime_ and _runtime version_ level."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "CompiledRuntimeVersion": _compiled_runtime_version_model_schema
})

_completed_event_data_model_schema = json.loads(
    r"""{
  "title" : "CompletedEventData",
  "required" : [ "returnvalue" ],
  "type" : "object",
  "properties" : {
    "prev" : {
      "$ref" : "#/components/schemas/QueueEvents"
    },
    "returnvalue" : {
      "$ref" : "#/components/schemas/AnyJobResult"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"CompletedEventData": _completed_event_data_model_schema})

_completed_event_sse_model_schema = json.loads(
    r"""{
  "required" : [ "data", "event" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/CompletedEventSSE_event"
    },
    "data" : {
      "$ref" : "#/components/schemas/JobEventResponse_CompletedEventData_"
    }
  },
  "description" : "A message that notifies a state change in a background job."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"CompletedEventSSE": _completed_event_sse_model_schema})

_completed_event_sse_event_model_schema = json.loads(
    r"""{
  "title" : "CompletedEventSSE_event",
  "type" : "string",
  "description" : "The job queue event that trigged this message",
  "enum" : [ "completed" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "CompletedEventSSE_event": _completed_event_sse_event_model_schema
})

_content_validation_listing_model_schema = json.loads(
    r"""{
  "required" : [ "assets" ],
  "type" : "object",
  "properties" : {
    "assets" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/AssetSummaryWithHALLink"
      }
    }
  },
  "description" : "Content listing"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ContentValidationListing": _content_validation_listing_model_schema
})

_create_models_copy_parameter_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/NamedVersionRange"
  }, {
    "$ref" : "#/components/schemas/ExampleReference"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "create_models_copy_parameter": _create_models_copy_parameter_model_schema
})

_delayed_event_data_model_schema = json.loads(
    r"""{
  "title" : "DelayedEventData",
  "required" : [ "delay" ],
  "type" : "object",
  "properties" : {
    "delay" : {
      "title" : "delay",
      "type" : "number"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"DelayedEventData": _delayed_event_data_model_schema})

_delayed_event_sse_model_schema = json.loads(
    r"""{
  "required" : [ "data", "event" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/DelayedEventSSE_event"
    },
    "data" : {
      "$ref" : "#/components/schemas/JobEventResponse_DelayedEventData_"
    }
  },
  "description" : "A message that notifies a state change in a background job."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"DelayedEventSSE": _delayed_event_sse_model_schema})

_delayed_event_sse_event_model_schema = json.loads(
    r"""{
  "title" : "DelayedEventSSE_event",
  "type" : "string",
  "description" : "The job queue event that trigged this message",
  "enum" : [ "delayed" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "DelayedEventSSE_event": _delayed_event_sse_event_model_schema
})

_deploy_model_schema = json.loads(
    r"""{
  "title" : "Deploy",
  "required" : [ "createdAt", "createdBy", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    },
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "The type of operation that was executed."
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user identity that was used to execute the job."
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp of when the job was created.",
      "format" : "date-time"
    },
    "processedAt" : {
      "title" : "processedAt",
      "type" : "string",
      "description" : "The timestamp of when the job has begun processing.",
      "format" : "date-time"
    },
    "finishedAt" : {
      "title" : "finishedAt",
      "description" : "The timestamp of when the job has finished processing."
    },
    "attemptsMade" : {
      "title" : "attemptsMade",
      "type" : "number",
      "description" : "The number of retries that were attempted."
    },
    "type" : {
      "$ref" : "#/components/schemas/Deploy_type"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "request" : {
      "$ref" : "#/components/schemas/DeployArgs"
    },
    "result" : {
      "$ref" : "#/components/schemas/DeployResult"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobStatus"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Deploy": _deploy_model_schema})

_deploy_1_model_schema = json.loads(
    r"""{
  "title" : "Deploy",
  "required" : [ "createdAt", "createdBy", "id", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "The type of operation that was executed."
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user identity that was used to execute the job."
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp of when the job was created.",
      "format" : "date-time"
    },
    "processedAt" : {
      "title" : "processedAt",
      "type" : "string",
      "description" : "The timestamp of when the job has begun processing.",
      "format" : "date-time"
    },
    "finishedAt" : {
      "title" : "finishedAt",
      "description" : "The timestamp of when the job has finished processing."
    },
    "attemptsMade" : {
      "title" : "attemptsMade",
      "type" : "number",
      "description" : "The number of retries that were attempted."
    },
    "type" : {
      "$ref" : "#/components/schemas/Deploy_type"
    },
    "id" : {
      "title" : "id",
      "type" : "string",
      "description" : "The id of the background job, or the constant `_unknown_`"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobAndFunctionHALLink"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Deploy_1": _deploy_1_model_schema})

_deploy_args_model_schema = json.loads(
    r"""{
  "title" : "DeployArgs",
  "required" : [ "deploySpecOverrides", "endpoint", "imageName", "namespace", "revision", "runtimeName", "runtimeVersion" ],
  "type" : "object",
  "properties" : {
    "namespace" : {
      "title" : "namespace",
      "type" : "string",
      "description" : "The (openfaas) namespace for the target function."
    },
    "endpoint" : {
      "title" : "endpoint",
      "type" : "string",
      "description" : "The (openfaas) endpoint service name"
    },
    "imageName" : {
      "title" : "imageName",
      "type" : "string",
      "description" : "The image name to use for deploying this function"
    },
    "runtimeName" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "revision" : {
      "title" : "revision",
      "type" : "string",
      "description" : "The revision hash of the current (draft) function revision"
    },
    "deploySpecOverrides" : {
      "$ref" : "#/components/schemas/DeployArgs_deploySpecOverrides"
    }
  },
  "description" : "Input argument to an (openfaas) deployment job for a function."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"DeployArgs": _deploy_args_model_schema})

_deploy_args_deploy_spec_overrides_model_schema = json.loads(
    r"""{
  "title" : "DeployArgs_deploySpecOverrides",
  "type" : "object",
  "properties" : {
    "service" : {
      "title" : "service",
      "type" : "string"
    },
    "image" : {
      "title" : "image",
      "type" : "string"
    },
    "namespace" : {
      "title" : "namespace",
      "type" : "string"
    },
    "network" : {
      "title" : "network",
      "type" : "string"
    },
    "envVars" : {
      "title" : "envVars",
      "type" : "object",
      "additionalProperties" : {
        "type" : "string"
      }
    },
    "constraints" : {
      "title" : "constraints",
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "labels" : {
      "title" : "labels",
      "type" : "object",
      "additionalProperties" : {
        "type" : "string"
      }
    },
    "annotations" : {
      "title" : "annotations",
      "type" : "object",
      "additionalProperties" : {
        "type" : "string"
      }
    },
    "secrets" : {
      "title" : "secrets",
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "registryAuth" : {
      "title" : "registryAuth",
      "type" : "string"
    },
    "limits" : {
      "$ref" : "#/components/schemas/ResourceLimits"
    },
    "requests" : {
      "$ref" : "#/components/schemas/ResourceLimits"
    },
    "readOnlyRootFilesystem" : {
      "title" : "readOnlyRootFilesystem",
      "type" : "boolean"
    }
  },
  "description" : "Overrides on the deployment specification."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "DeployArgs_deploySpecOverrides": _deploy_args_deploy_spec_overrides_model_schema
})

_deploy_job_status_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "job", "operation", "request", "state", "type" ],
  "type" : "object",
  "properties" : {
    "operation" : {
      "type" : "string",
      "description" : "The type of operation that was executed."
    },
    "createdBy" : {
      "type" : "string",
      "description" : "The user identity that was used to execute the job."
    },
    "createdAt" : {
      "type" : "string",
      "description" : "The timestamp of when the job was created.",
      "format" : "date-time"
    },
    "processedAt" : {
      "type" : "string",
      "description" : "The timestamp of when the job has begun processing.",
      "format" : "date-time"
    },
    "finishedAt" : {
      "description" : "The timestamp of when the job has finished processing."
    },
    "attemptsMade" : {
      "type" : "number",
      "description" : "The number of retries that were attempted."
    },
    "type" : {
      "$ref" : "#/components/schemas/Deploy_type"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "request" : {
      "$ref" : "#/components/schemas/DeployArgs"
    },
    "result" : {
      "$ref" : "#/components/schemas/DeployResult"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobStatus"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"DeployJobStatus": _deploy_job_status_model_schema})

_deploy_result_model_schema = json.loads(
    r"""{
  "title" : "DeployResult",
  "required" : [ "deploySpec" ],
  "type" : "object",
  "properties" : {
    "deploySpec" : {
      "$ref" : "#/components/schemas/ExposedOpenfaasDeploySpec"
    }
  },
  "description" : "The result data for a completed deployment job."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"DeployResult": _deploy_result_model_schema})

_deploy_spec_model_schema = json.loads(
    r"""{
  "title" : "DeploySpec",
  "type" : "object",
  "properties" : {
    "openfaasSpec" : {
      "$ref" : "#/components/schemas/DeploySpec_openfaasSpec"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"DeploySpec": _deploy_spec_model_schema})

_deploy_spec_openfaas_spec_model_schema = json.loads(
    r"""{
  "title" : "DeploySpec_openfaasSpec",
  "type" : "object",
  "properties" : {
    "service" : {
      "title" : "service",
      "type" : "string"
    },
    "image" : {
      "title" : "image",
      "type" : "string"
    },
    "namespace" : {
      "title" : "namespace",
      "type" : "string"
    },
    "network" : {
      "title" : "network",
      "type" : "string"
    },
    "envVars" : {
      "title" : "envVars",
      "type" : "object",
      "additionalProperties" : {
        "type" : "string"
      }
    },
    "constraints" : {
      "title" : "constraints",
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "labels" : {
      "title" : "labels",
      "type" : "object",
      "additionalProperties" : {
        "type" : "string"
      }
    },
    "annotations" : {
      "title" : "annotations",
      "type" : "object",
      "additionalProperties" : {
        "type" : "string"
      }
    },
    "secrets" : {
      "title" : "secrets",
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "registryAuth" : {
      "title" : "registryAuth",
      "type" : "string"
    },
    "limits" : {
      "$ref" : "#/components/schemas/ResourceLimits"
    },
    "requests" : {
      "$ref" : "#/components/schemas/ResourceLimits"
    },
    "readOnlyRootFilesystem" : {
      "title" : "readOnlyRootFilesystem",
      "type" : "boolean"
    }
  },
  "description" : "If specified, it overrides the properties in `default`. Non-specified properties are taken from `default`"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "DeploySpec_openfaasSpec": _deploy_spec_openfaas_spec_model_schema
})

_deploy_type_model_schema = json.loads(
    r"""{
  "title" : "Deploy_type",
  "type" : "string",
  "description" : "The type of the background task.",
  "enum" : [ "deploy" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Deploy_type": _deploy_type_model_schema})

_deprecate_previous_policy_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/DeprecatePreviousPolicy_anyOf"
  }, {
    "$ref" : "#/components/schemas/DeprecatePreviousPolicy_anyOf_1"
  }, {
    "$ref" : "#/components/schemas/DeprecatePreviousPolicy_anyOf_2"
  }, {
    "$ref" : "#/components/schemas/DeprecatePreviousPolicy_anyOf_3"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "DeprecatePreviousPolicy": _deprecate_previous_policy_model_schema
})

_deprecate_previous_policy_any_of_model_schema = json.loads(
    r"""{
  "title" : "DeprecatePreviousPolicy_anyOf",
  "type" : "string",
  "enum" : [ "none" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "DeprecatePreviousPolicy_anyOf": _deprecate_previous_policy_any_of_model_schema
})

_deprecate_previous_policy_any_of_1_model_schema = json.loads(
    r"""{
  "title" : "DeprecatePreviousPolicy_anyOf_1",
  "type" : "string",
  "enum" : [ "all" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "DeprecatePreviousPolicy_anyOf_1": _deprecate_previous_policy_any_of_1_model_schema
})

_deprecate_previous_policy_any_of_2_model_schema = json.loads(
    r"""{
  "title" : "DeprecatePreviousPolicy_anyOf_2",
  "type" : "string",
  "enum" : [ "patch" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "DeprecatePreviousPolicy_anyOf_2": _deprecate_previous_policy_any_of_2_model_schema
})

_deprecate_previous_policy_any_of_3_model_schema = json.loads(
    r"""{
  "title" : "DeprecatePreviousPolicy_anyOf_3",
  "type" : "string",
  "enum" : [ "minor" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "DeprecatePreviousPolicy_anyOf_3": _deprecate_previous_policy_any_of_3_model_schema
})

_documentation_model_schema = json.loads(
    r"""{
  "title" : "Documentation",
  "type" : "object",
  "properties" : {
    "description" : {
      "title" : "description",
      "type" : "string"
    },
    "states" : {
      "title" : "states",
      "type" : "array",
      "description" : "Documentation of the plug states.",
      "items" : {
        "$ref" : "#/components/schemas/DocumentationProperty"
      }
    },
    "input" : {
      "title" : "input",
      "type" : "array",
      "description" : "Documentation of the plug input parameters.",
      "items" : {
        "$ref" : "#/components/schemas/DocumentationProperty"
      }
    },
    "output" : {
      "title" : "output",
      "type" : "array",
      "description" : "Documentation of the plug response parameters.",
      "items" : {
        "$ref" : "#/components/schemas/DocumentationProperty"
      }
    },
    "examples" : {
      "title" : "examples",
      "type" : "array",
      "description" : "Example scenarios for testing the plug.",
      "items" : {
        "$ref" : "#/components/schemas/DocumentationExample"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Documentation": _documentation_model_schema})

_documentation_example_model_schema = json.loads(
    r"""{
  "title" : "DocumentationExample",
  "required" : [ "description" ],
  "type" : "object",
  "properties" : {
    "description" : {
      "title" : "description",
      "type" : "string",
      "description" : "Description of the example scenario."
    },
    "input" : {
      "title" : "input",
      "type" : "object",
      "description" : "Example input values."
    },
    "output" : {
      "title" : "output",
      "type" : "object",
      "description" : "Example output values."
    },
    "state" : {
      "title" : "state",
      "type" : "string",
      "description" : "Example state value."
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"DocumentationExample": _documentation_example_model_schema})

_documentation_property_model_schema = json.loads(
    r"""{
  "title" : "DocumentationProperty",
  "required" : [ "description", "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "type" : "string",
      "description" : "Name of the documented property."
    },
    "description" : {
      "title" : "description",
      "type" : "string",
      "description" : "Documentation of the property."
    },
    "examples" : {
      "title" : "examples",
      "type" : "array",
      "description" : "Example values for the property.",
      "items" : { }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "DocumentationProperty": _documentation_property_model_schema
})

_entity_with_links_i_kfserving_response_v2__model_schema = json.loads(
    r"""{
  "title" : "EntityWithLinks_IKfservingResponseV2_",
  "required" : [ "createdAt", "createdBy", "deprecated", "draft", "model", "runtime", "status", "updatedAt", "updatedBy" ],
  "type" : "object",
  "properties" : {
    "_embedded" : {
      "$ref" : "#/components/schemas/AltEmbeddedVersion_IKfservingResponseV2_"
    },
    "_links" : {
      "$ref" : "#/components/schemas/AltVersionHALLink"
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user that created this entity."
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp at which this entity was created.",
      "format" : "date-time"
    },
    "updatedBy" : {
      "title" : "updatedBy",
      "type" : "string",
      "description" : "The user that last updated this entity."
    },
    "updatedAt" : {
      "title" : "updatedAt",
      "type" : "string",
      "description" : "The timestamp at which this entity was last updated.",
      "format" : "date-time"
    },
    "updates" : {
      "title" : "updates",
      "type" : "array",
      "description" : "The audit logs corresponding to the latest modifying operations on this entity. Omitted in listing operations.",
      "items" : {
        "$ref" : "#/components/schemas/UpdateRecord"
      }
    },
    "status" : {
      "$ref" : "#/components/schemas/Status"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/RuntimeAttributes"
    },
    "deprecated" : {
      "title" : "deprecated",
      "type" : "boolean",
      "description" : "If <code>true</code> this function is deprecated and removed from regular listings."
    },
    "draft" : {
      "title" : "draft",
      "type" : "boolean",
      "description" : "If <code>true</code> this function is a draft function and it's assets are still mutable."
    },
    "revision" : {
      "title" : "revision",
      "type" : "string",
      "description" : "The revision of the function. This will be <code>undefined</code> when the plug is not a draft."
    },
    "model" : {
      "$ref" : "#/components/schemas/KFServingManifest"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "EntityWithLinks_IKfservingResponseV2_": _entity_with_links_i_kfserving_response_v2__model_schema
})

_entity_with_links_i_plug_response_v2__model_schema = json.loads(
    r"""{
  "title" : "EntityWithLinks_IPlugResponseV2_",
  "required" : [ "createdAt", "createdBy", "deprecated", "draft", "plug", "runtime", "status", "updatedAt", "updatedBy" ],
  "type" : "object",
  "properties" : {
    "_embedded" : {
      "$ref" : "#/components/schemas/AltEmbeddedVersion_IPlugResponseV2_"
    },
    "_links" : {
      "$ref" : "#/components/schemas/AltVersionHALLink"
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user that created this entity."
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp at which this entity was created.",
      "format" : "date-time"
    },
    "updatedBy" : {
      "title" : "updatedBy",
      "type" : "string",
      "description" : "The user that last updated this entity."
    },
    "updatedAt" : {
      "title" : "updatedAt",
      "type" : "string",
      "description" : "The timestamp at which this entity was last updated.",
      "format" : "date-time"
    },
    "updates" : {
      "title" : "updates",
      "type" : "array",
      "description" : "The audit logs corresponding to the latest modifying operations on this entity. Omitted in listing operations.",
      "items" : {
        "$ref" : "#/components/schemas/UpdateRecord"
      }
    },
    "status" : {
      "$ref" : "#/components/schemas/Status"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/RuntimeAttributes"
    },
    "deprecated" : {
      "title" : "deprecated",
      "type" : "boolean",
      "description" : "If <code>true</code> this plug is removed from regular listings, as a result of a <code>DELETE</code> with <code>force=false</code>."
    },
    "draft" : {
      "title" : "draft",
      "type" : "boolean",
      "description" : "If <code>true</code> this function is a draft function and it's assets are still mutable."
    },
    "revision" : {
      "title" : "revision",
      "type" : "string",
      "description" : "The revision of the function. This will be <code>undefined</code> when the plug is not a draft."
    },
    "plug" : {
      "$ref" : "#/components/schemas/PlugManifest"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "EntityWithLinks_IPlugResponseV2_": _entity_with_links_i_plug_response_v2__model_schema
})

_entity_with_links_i_webscript_response_with_invoke_link_v2__model_schema = json.loads(
    r"""{
  "title" : "EntityWithLinks_IWebscriptResponseWithInvokeLinkV2_",
  "required" : [ "createdAt", "createdBy", "deprecated", "draft", "runtime", "status", "updatedAt", "updatedBy", "webscript" ],
  "type" : "object",
  "properties" : {
    "_embedded" : {
      "$ref" : "#/components/schemas/AltEmbeddedVersion_IWebscriptResponseWithInvokeLinkV2_"
    },
    "_links" : {
      "$ref" : "#/components/schemas/InvokeHALLink"
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user that created this entity."
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp at which this entity was created.",
      "format" : "date-time"
    },
    "updatedBy" : {
      "title" : "updatedBy",
      "type" : "string",
      "description" : "The user that last updated this entity."
    },
    "updatedAt" : {
      "title" : "updatedAt",
      "type" : "string",
      "description" : "The timestamp at which this entity was last updated.",
      "format" : "date-time"
    },
    "updates" : {
      "title" : "updates",
      "type" : "array",
      "description" : "The audit logs corresponding to the latest modifying operations on this entity. Omitted in listing operations.",
      "items" : {
        "$ref" : "#/components/schemas/UpdateRecord"
      }
    },
    "status" : {
      "$ref" : "#/components/schemas/Status"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/RuntimeAttributes"
    },
    "deprecated" : {
      "title" : "deprecated",
      "type" : "boolean",
      "description" : "If <code>true</code> this function is deprecated and removed from regular listings."
    },
    "draft" : {
      "title" : "draft",
      "type" : "boolean",
      "description" : "If <code>true</code> this function is a draft function and it's assets are still mutable."
    },
    "revision" : {
      "title" : "revision",
      "type" : "string",
      "description" : "The revision of the function. This will be <code>undefined</code> when the plug is not a draft."
    },
    "webscript" : {
      "$ref" : "#/components/schemas/WebscriptManifest"
    },
    "secret" : {
      "title" : "secret",
      "type" : "string",
      "description" : "The secret for this webscript deployment. This is <code>null</code> when <code>allowHmac=false</code> in the webscript specificaton."
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "EntityWithLinks_IWebscriptResponseWithInvokeLinkV2_": _entity_with_links_i_webscript_response_with_invoke_link_v2__model_schema
})

_error_and_status_response_model_schema = json.loads(
    r"""{
  "required" : [ "error", "statusCode" ],
  "type" : "object",
  "properties" : {
    "error" : {
      "type" : "string"
    },
    "statusCode" : {
      "type" : "number"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ErrorAndStatusResponse": _error_and_status_response_model_schema
})

_event_ack_model_schema = json.loads(
    r"""{
  "type" : "string",
  "enum" : [ "ack" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"EventAck": _event_ack_model_schema})

_event_close_model_schema = json.loads(
    r"""{
  "type" : "string",
  "enum" : [ "close" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"EventClose": _event_close_model_schema})

_event_keep_alive_model_schema = json.loads(
    r"""{
  "type" : "string",
  "enum" : [ "keep-alive" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"EventKeepAlive": _event_keep_alive_model_schema})

_event_with_close_sse_model_schema = json.loads(
    r"""{
  "description" : "SSE stream events with closing protocol",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Stream_Ready"
  }, {
    "$ref" : "#/components/schemas/JobEventSSE"
  }, {
    "$ref" : "#/components/schemas/KeepAliveEventSSE"
  }, {
    "$ref" : "#/components/schemas/Stream_Closing"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"EventWithCloseSSE": _event_with_close_sse_model_schema})

_example_reference_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Example reference.\n\nReferences the example assets from the selected runtime.",
  "enum" : [ "!example" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ExampleReference": _example_reference_model_schema})

_exposed_openfaas_deploy_spec_model_schema = json.loads(
    r"""{
  "title" : "ExposedOpenfaasDeploySpec",
  "required" : [ "image", "namespace", "service" ],
  "type" : "object",
  "properties" : {
    "service" : {
      "title" : "service",
      "type" : "string"
    },
    "image" : {
      "title" : "image",
      "type" : "string"
    },
    "namespace" : {
      "title" : "namespace",
      "type" : "string"
    },
    "labels" : {
      "title" : "labels",
      "type" : "object",
      "additionalProperties" : {
        "type" : "string"
      }
    },
    "annotations" : {
      "title" : "annotations",
      "type" : "object",
      "additionalProperties" : {
        "type" : "string"
      }
    },
    "limits" : {
      "$ref" : "#/components/schemas/ResourceLimits"
    },
    "requests" : {
      "$ref" : "#/components/schemas/ResourceLimits"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ExposedOpenfaasDeploySpec": _exposed_openfaas_deploy_spec_model_schema
})

_failed_event_data_model_schema = json.loads(
    r"""{
  "title" : "FailedEventData",
  "required" : [ "failedReason" ],
  "type" : "object",
  "properties" : {
    "prev" : {
      "$ref" : "#/components/schemas/QueueEvents"
    },
    "failedReason" : {
      "title" : "failedReason",
      "type" : "string",
      "description" : "The failure reason of the job"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"FailedEventData": _failed_event_data_model_schema})

_failed_event_sse_model_schema = json.loads(
    r"""{
  "required" : [ "data", "event" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/FailedEventSSE_event"
    },
    "data" : {
      "$ref" : "#/components/schemas/JobEventResponse_FailedEventData_"
    }
  },
  "description" : "A message that notifies a state change in a background job."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"FailedEventSSE": _failed_event_sse_model_schema})

_failed_event_sse_event_model_schema = json.loads(
    r"""{
  "title" : "FailedEventSSE_event",
  "type" : "string",
  "description" : "The job queue event that trigged this message",
  "enum" : [ "failed" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"FailedEventSSE_event": _failed_event_sse_event_model_schema})

_failure_reason_model_schema = json.loads(
    r"""{
  "title" : "FailureReason",
  "required" : [ "events", "log" ],
  "type" : "object",
  "properties" : {
    "log" : {
      "title" : "log",
      "type" : "array",
      "description" : "Log lines associated with this failure.",
      "items" : {
        "type" : "string"
      }
    },
    "events" : {
      "title" : "events",
      "type" : "array",
      "description" : "Events associated with this failure.",
      "items" : {
        "type" : "string"
      }
    },
    "cause" : {
      "title" : "cause",
      "type" : "string",
      "description" : "Main cause for the failure."
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"FailureReason": _failure_reason_model_schema})

_file_upload_model_schema = json.loads(
    r"""{
  "title" : "File Upload",
  "type" : "object",
  "properties" : {
    "file" : {
      "type" : "string",
      "format" : "binary"
    }
  },
  "description" : "A single asset file."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"File_Upload": _file_upload_model_schema})

_function_deploy_overrides_type_model_schema = json.loads(
    r"""{
  "title" : "FunctionDeployOverridesType",
  "type" : "object",
  "properties" : {
    "envVars" : {
      "title" : "envVars",
      "type" : "object",
      "additionalProperties" : {
        "type" : "string"
      }
    },
    "labels" : {
      "title" : "labels",
      "type" : "object",
      "additionalProperties" : {
        "type" : "string"
      }
    },
    "annotations" : {
      "title" : "annotations",
      "type" : "object",
      "additionalProperties" : {
        "type" : "string"
      }
    },
    "limits" : {
      "$ref" : "#/components/schemas/ResourceLimits"
    },
    "requests" : {
      "$ref" : "#/components/schemas/ResourceLimits"
    },
    "secrets" : {
      "title" : "secrets",
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "FunctionDeployOverridesType": _function_deploy_overrides_type_model_schema
})

_function_meta_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "author" : {
      "type" : "string",
      "description" : "The author of the function."
    },
    "description" : {
      "type" : "string",
      "description" : "A description of the function"
    },
    "iconURL" : {
      "type" : "string",
      "description" : "An url to an icon that represents this function."
    },
    "category" : {
      "type" : "string",
      "description" : "A category for this function (Deprecated: use tags to categorise your functions)",
      "deprecated" : true
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"FunctionMeta": _function_meta_model_schema})

_function_ref_model_schema = json.loads(
    r"""{
  "title" : "FunctionRef",
  "required" : [ "functionType", "name" ],
  "type" : "object",
  "properties" : {
    "functionType" : {
      "$ref" : "#/components/schemas/FunctionType"
    },
    "name" : {
      "title" : "name",
      "type" : "string",
      "description" : "The logical name for the function."
    },
    "version" : {
      "title" : "version",
      "type" : "string",
      "description" : "The semantic version of the function (all versions if undefined)"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"FunctionRef": _function_ref_model_schema})

_function_tag_response_model_schema = json.loads(
    r"""{
  "required" : [ "tag" ],
  "type" : "object",
  "properties" : {
    "tag" : {
      "$ref" : "#/components/schemas/Tag"
    }
  },
  "description" : "Function Tag Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"FunctionTagResponse": _function_tag_response_model_schema})

_function_tags_response_model_schema = json.loads(
    r"""{
  "required" : [ "tags" ],
  "type" : "object",
  "properties" : {
    "tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Tag"
      }
    }
  },
  "description" : "Function Tags Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"FunctionTagsResponse": _function_tags_response_model_schema})

_function_type_model_schema = json.loads(
    r"""{
  "title" : "FunctionType",
  "type" : "string",
  "description" : "Type of functions supported by the registry service.",
  "enum" : [ "plugs", "webscripts", "kfserving" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"FunctionType": _function_type_model_schema})

_function_type_exclude_model_schema = json.loads(
    r"""{
  "title" : "FunctionTypeExclude",
  "type" : "string",
  "enum" : [ "plugs-", "webscripts-", "kfserving-" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"FunctionTypeExclude": _function_type_exclude_model_schema})

_function_type_filter_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/FunctionType"
  }, {
    "$ref" : "#/components/schemas/FunctionTypeExclude"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"FunctionTypeFilter": _function_type_filter_model_schema})

_get_asset_by_role_models_asset_role_parameter_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/getAssetByRole_models_assetRole_parameter_anyOf"
  }, {
    "$ref" : "#/components/schemas/getAssetByRole_models_assetRole_parameter_anyOf_1"
  }, {
    "$ref" : "#/components/schemas/getAssetByRole_models_assetRole_parameter_anyOf_2"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "getAssetByRole_models_assetRole_parameter": _get_asset_by_role_models_asset_role_parameter_model_schema
})

_get_asset_by_role_models_asset_role_parameter_any_of_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Metadata specification of the function for the waylay platform.",
  "enum" : [ "manifest" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "getAssetByRole_models_assetRole_parameter_anyOf": _get_asset_by_role_models_asset_role_parameter_any_of_model_schema
})

_get_asset_by_role_models_asset_role_parameter_any_of_1_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Main source code that implements the function entrypoint.",
  "enum" : [ "main" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "getAssetByRole_models_assetRole_parameter_anyOf_1": _get_asset_by_role_models_asset_role_parameter_any_of_1_model_schema
})

_get_asset_by_role_models_asset_role_parameter_any_of_2_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Metadata specification for the language runtime. E.g. to specify dependencies.",
  "enum" : [ "project" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "getAssetByRole_models_assetRole_parameter_anyOf_2": _get_asset_by_role_models_asset_role_parameter_any_of_2_model_schema
})

_get_model_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "entity" ],
  "type" : "object",
  "properties" : {
    "_embedded" : {
      "$ref" : "#/components/schemas/GetPlugResponseV2__embedded"
    },
    "entity" : {
      "$ref" : "#/components/schemas/KfservingResponseV2"
    },
    "_links" : {
      "$ref" : "#/components/schemas/GetPlugResponseV2__links"
    }
  },
  "description" : "Model Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"GetModelResponseV2": _get_model_response_v2_model_schema})

_get_plug_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "entity" ],
  "type" : "object",
  "properties" : {
    "_embedded" : {
      "$ref" : "#/components/schemas/GetPlugResponseV2__embedded"
    },
    "entity" : {
      "$ref" : "#/components/schemas/PlugWithInvocationResponseV2"
    },
    "_links" : {
      "$ref" : "#/components/schemas/GetPlugResponseV2__links"
    }
  },
  "description" : "Plug Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"GetPlugResponseV2": _get_plug_response_v2_model_schema})

_get_plug_response_v2__embedded_model_schema = json.loads(
    r"""{
  "title" : "GetPlugResponseV2__embedded",
  "type" : "object",
  "properties" : {
    "tags" : {
      "title" : "tags",
      "type" : "array",
      "description" : "Record of <tag key, tag representation> pairs.",
      "items" : {
        "$ref" : "#/components/schemas/Tag"
      }
    }
  },
  "description" : "Embedded representations of the referenced tags."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "GetPlugResponseV2__embedded": _get_plug_response_v2__embedded_model_schema
})

_get_plug_response_v2__links_model_schema = json.loads(
    r"""{
  "title" : "GetPlugResponseV2__links",
  "type" : "object",
  "properties" : {
    "job" : {
      "$ref" : "#/components/schemas/JobHALLinks_job"
    },
    "content" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "draft" : {
      "$ref" : "#/components/schemas/AltVersionHALLink_draft"
    },
    "published" : {
      "$ref" : "#/components/schemas/AltVersionHALLink_published"
    },
    "jobs" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  },
  "description" : "HAL links to related jobs and plugs"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "GetPlugResponseV2__links": _get_plug_response_v2__links_model_schema
})

_get_webscript_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "entity" ],
  "type" : "object",
  "properties" : {
    "_embedded" : {
      "$ref" : "#/components/schemas/GetPlugResponseV2__embedded"
    },
    "entity" : {
      "$ref" : "#/components/schemas/WebscriptResponseV2"
    },
    "_links" : {
      "$ref" : "#/components/schemas/GetWebscriptResponseV2__links"
    }
  },
  "description" : "Webscript Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "GetWebscriptResponseV2": _get_webscript_response_v2_model_schema
})

_get_webscript_response_v2__links_model_schema = json.loads(
    r"""{
  "title" : "GetWebscriptResponseV2__links",
  "type" : "object",
  "properties" : {
    "job" : {
      "$ref" : "#/components/schemas/JobHALLinks_job"
    },
    "content" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "draft" : {
      "$ref" : "#/components/schemas/AltVersionHALLink_draft"
    },
    "published" : {
      "$ref" : "#/components/schemas/AltVersionHALLink_published"
    },
    "jobs" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "invoke" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  },
  "description" : "HAL links to related actions."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "GetWebscriptResponseV2__links": _get_webscript_response_v2__links_model_schema
})

_hal_link_model_schema = json.loads(
    r"""{
  "required" : [ "href" ],
  "type" : "object",
  "properties" : {
    "href" : {
      "$ref" : "#/components/schemas/HALLink_href"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HALLink": _hal_link_model_schema})

_hal_link_href_model_schema = json.loads(
    r"""{
  "title" : "HALLink_href",
  "anyOf" : [ {
    "type" : "string",
    "format" : "uri"
  }, {
    "type" : "string"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HALLink_href": _hal_link_href_model_schema})

_hal_links_model_schema = json.loads(
    r"""{
  "description" : "One or more links of the same HAL collection.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/HALLink"
  }, {
    "type" : "array",
    "items" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HALLinks": _hal_links_model_schema})

_invocation_attributes_model_schema = json.loads(
    r"""{
  "title" : "InvocationAttributes",
  "required" : [ "auth", "callback", "nodeContext", "rawDataContext", "taskContext" ],
  "type" : "object",
  "properties" : {
    "auth" : {
      "$ref" : "#/components/schemas/InvocationAttributes_auth"
    },
    "taskContext" : {
      "title" : "taskContext",
      "type" : "boolean",
      "description" : "Indicates whether the task context attributes should be provided in `options.task`."
    },
    "nodeContext" : {
      "title" : "nodeContext",
      "type" : "boolean",
      "description" : "Indicates whether the node context attributes should be provided in `options.node`."
    },
    "rawDataContext" : {
      "title" : "rawDataContext",
      "type" : "boolean",
      "description" : "Indicates that the rawdata context attributes should be provided in `options.rawData`."
    },
    "callback" : {
      "title" : "callback",
      "type" : "boolean",
      "description" : "Indicates that the plug implementer intends to use the callback mechanism."
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"InvocationAttributes": _invocation_attributes_model_schema})

_invocation_attributes_auth_model_schema = json.loads(
    r"""{
  "title" : "InvocationAttributes_auth",
  "type" : "string",
  "description" : "Indicates what credentials are passed to provide a Waylay authorization context.",
  "enum" : [ "waylay", "none" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "InvocationAttributes_auth": _invocation_attributes_auth_model_schema
})

_invoke_hal_link_model_schema = json.loads(
    r"""{
  "title" : "InvokeHALLink",
  "type" : "object",
  "properties" : {
    "invoke" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"InvokeHALLink": _invoke_hal_link_model_schema})

_job_and_function_hal_link_model_schema = json.loads(
    r"""{
  "title" : "JobAndFunctionHALLink",
  "description" : "HAL links to related actions.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Plug_1"
  }, {
    "$ref" : "#/components/schemas/Webscript_1"
  }, {
    "$ref" : "#/components/schemas/Model_1"
  }, {
    "$ref" : "#/components/schemas/JobHALLinks"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobAndFunctionHALLink": _job_and_function_hal_link_model_schema
})

_job_cause_model_schema = json.loads(
    r"""{
  "title" : "JobCause",
  "required" : [ "changed", "reason" ],
  "type" : "object",
  "properties" : {
    "changed" : {
      "title" : "changed",
      "type" : "boolean",
      "description" : "If <code>true</code>, the argument configuration for this job has changed in comparison to the previous job execution. A <code>false</code> will prevent the job to be run. Use <code>forceVersion</code> or <code>upgrade</code> parameter to force a rebuild."
    },
    "reason" : {
      "title" : "reason",
      "type" : "string",
      "description" : "Human readable message describing the cause."
    },
    "backoff" : {
      "title" : "backoff",
      "type" : "boolean",
      "description" : "If <code>true</code>, recent failures of the job prevented the re-execution. Use <code>forceVersion</code> or <code>upgrade</code> parameter to force a rebuild."
    },
    "newValue" : {
      "title" : "newValue",
      "description" : "The new configuration value that causes the change."
    },
    "oldValue" : {
      "title" : "oldValue",
      "description" : "The old configuration value used by the last succeeded job."
    }
  },
  "description" : "The motivation for including or excluding a job (<em>build</em>, <em>deploy</em>, <em>verify</em>, ...) in response to a <em>rebuild</em> request."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobCause": _job_cause_model_schema})

_job_causes_model_schema = json.loads(
    r"""{
  "title" : "JobCauses",
  "type" : "object",
  "properties" : {
    "build" : {
      "$ref" : "#/components/schemas/JobCause"
    },
    "deploy" : {
      "$ref" : "#/components/schemas/JobCause"
    },
    "verify" : {
      "$ref" : "#/components/schemas/JobCause"
    },
    "undeploy" : {
      "$ref" : "#/components/schemas/JobCause"
    },
    "scale" : {
      "$ref" : "#/components/schemas/JobCause"
    }
  },
  "description" : "The motivations for including or excluding a job in response to a <em>rebuild</em> request."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobCauses": _job_causes_model_schema})

_job_event_response_active_event_data__model_schema = json.loads(
    r"""{
  "title" : "JobEventResponse_ActiveEventData_",
  "required" : [ "_links", "data", "function", "job", "timestamp" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/JobStatusAndEntityHALLinks"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobReference"
    },
    "data" : {
      "$ref" : "#/components/schemas/ActiveEventData"
    },
    "timestamp" : {
      "title" : "timestamp",
      "type" : "string",
      "description" : "Timestamp of the event",
      "format" : "date-time"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    }
  },
  "description" : "Event object describing a state change of a background job."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobEventResponse_ActiveEventData_": _job_event_response_active_event_data__model_schema
})

_job_event_response_completed_event_data__model_schema = json.loads(
    r"""{
  "title" : "JobEventResponse_CompletedEventData_",
  "required" : [ "_links", "data", "function", "job", "timestamp" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/JobStatusAndEntityHALLinks"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobReference"
    },
    "data" : {
      "$ref" : "#/components/schemas/CompletedEventData"
    },
    "timestamp" : {
      "title" : "timestamp",
      "type" : "string",
      "description" : "Timestamp of the event",
      "format" : "date-time"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    }
  },
  "description" : "Event object describing a state change of a background job."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobEventResponse_CompletedEventData_": _job_event_response_completed_event_data__model_schema
})

_job_event_response_delayed_event_data__model_schema = json.loads(
    r"""{
  "title" : "JobEventResponse_DelayedEventData_",
  "required" : [ "_links", "data", "function", "job", "timestamp" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/JobStatusAndEntityHALLinks"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobReference"
    },
    "data" : {
      "$ref" : "#/components/schemas/DelayedEventData"
    },
    "timestamp" : {
      "title" : "timestamp",
      "type" : "string",
      "description" : "Timestamp of the event",
      "format" : "date-time"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    }
  },
  "description" : "Event object describing a state change of a background job."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobEventResponse_DelayedEventData_": _job_event_response_delayed_event_data__model_schema
})

_job_event_response_failed_event_data__model_schema = json.loads(
    r"""{
  "title" : "JobEventResponse_FailedEventData_",
  "required" : [ "_links", "data", "function", "job", "timestamp" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/JobStatusAndEntityHALLinks"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobReference"
    },
    "data" : {
      "$ref" : "#/components/schemas/FailedEventData"
    },
    "timestamp" : {
      "title" : "timestamp",
      "type" : "string",
      "description" : "Timestamp of the event",
      "format" : "date-time"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    }
  },
  "description" : "Event object describing a state change of a background job."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobEventResponse_FailedEventData_": _job_event_response_failed_event_data__model_schema
})

_job_event_response_waiting_children_event_data__model_schema = json.loads(
    r"""{
  "title" : "JobEventResponse_WaitingChildrenEventData_",
  "required" : [ "_links", "data", "function", "job", "timestamp" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/JobStatusAndEntityHALLinks"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobReference"
    },
    "data" : {
      "$ref" : "#/components/schemas/WaitingChildrenEventData"
    },
    "timestamp" : {
      "title" : "timestamp",
      "type" : "string",
      "description" : "Timestamp of the event",
      "format" : "date-time"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    }
  },
  "description" : "Event object describing a state change of a background job."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobEventResponse_WaitingChildrenEventData_": _job_event_response_waiting_children_event_data__model_schema
})

_job_event_response_waiting_event_data__model_schema = json.loads(
    r"""{
  "title" : "JobEventResponse_WaitingEventData_",
  "required" : [ "_links", "data", "function", "job", "timestamp" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/JobStatusAndEntityHALLinks"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobReference"
    },
    "data" : {
      "$ref" : "#/components/schemas/WaitingEventData"
    },
    "timestamp" : {
      "title" : "timestamp",
      "type" : "string",
      "description" : "Timestamp of the event",
      "format" : "date-time"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    }
  },
  "description" : "Event object describing a state change of a background job."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobEventResponse_WaitingEventData_": _job_event_response_waiting_event_data__model_schema
})

_job_event_sse_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/ActiveEventSSE"
  }, {
    "$ref" : "#/components/schemas/CompletedEventSSE"
  }, {
    "$ref" : "#/components/schemas/FailedEventSSE"
  }, {
    "$ref" : "#/components/schemas/DelayedEventSSE"
  }, {
    "$ref" : "#/components/schemas/WaitingEventSSE"
  }, {
    "$ref" : "#/components/schemas/WaitingChildrenEventSSE"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobEventSSE": _job_event_sse_model_schema})

_job_events_and_function_hal_link_model_schema = json.loads(
    r"""{
  "title" : "JobEventsAndFunctionHALLink",
  "description" : "HAL links to related actions.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Plug"
  }, {
    "$ref" : "#/components/schemas/Webscript"
  }, {
    "$ref" : "#/components/schemas/Model"
  }, {
    "$ref" : "#/components/schemas/JobEventsHALLink"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobEventsAndFunctionHALLink": _job_events_and_function_hal_link_model_schema
})

_job_events_hal_link_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/HALLinks"
    }
  },
  "description" : "HAL links to related actions."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobEventsHALLink": _job_events_hal_link_model_schema})

_job_hal_link_model_schema = json.loads(
    r"""{
  "required" : [ "href", "jobType" ],
  "type" : "object",
  "properties" : {
    "href" : {
      "$ref" : "#/components/schemas/HALLink_href"
    },
    "jobType" : {
      "$ref" : "#/components/schemas/JobType"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobHALLink": _job_hal_link_model_schema})

_job_hal_links_model_schema = json.loads(
    r"""{
  "title" : "JobHALLinks",
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/HALLinks"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobHALLinks_job"
    }
  },
  "description" : "HAL links to related actions."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobHALLinks": _job_hal_links_model_schema})

_job_hal_links_job_model_schema = json.loads(
    r"""{
  "title" : "JobHALLinks_job",
  "description" : "Link to the job status page for the related entity.",
  "example" : {
    "href" : "https://api.waylay.io/registry/v2/jobs/undeploy/6ccc8843-d78d-49e8-84c4-3734a4af9929$IfM2FyNLQ8CEjQGA9w7Ht",
    "jobType" : "undeploy"
  },
  "anyOf" : [ {
    "type" : "array",
    "items" : {
      "$ref" : "#/components/schemas/JobHALLink"
    }
  }, {
    "$ref" : "#/components/schemas/JobHALLink"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobHALLinks_job": _job_hal_links_job_model_schema})

_job_reference_model_schema = json.loads(
    r"""{
  "title" : "JobReference",
  "required" : [ "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/JobType"
    },
    "id" : {
      "title" : "id",
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobReference": _job_reference_model_schema})

_job_response_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "job" ],
  "type" : "object",
  "properties" : {
    "job" : {
      "$ref" : "#/components/schemas/AnyJobStatus"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobEventsAndFunctionHALLink"
    }
  },
  "description" : "Job Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobResponse": _job_response_model_schema})

_job_state_model_schema = json.loads(
    r"""{
  "title" : "JobState",
  "description" : "Allowed job states",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/JobStateFinished"
  }, {
    "$ref" : "#/components/schemas/JobStateActive"
  }, {
    "$ref" : "#/components/schemas/JobStateDelayed"
  }, {
    "$ref" : "#/components/schemas/JobStateWaiting"
  }, {
    "$ref" : "#/components/schemas/JobStateWaitingChildren"
  }, {
    "$ref" : "#/components/schemas/JobStatePrioritized"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobState": _job_state_model_schema})

_job_state_active_model_schema = json.loads(
    r"""{
  "title" : "JobStateActive",
  "type" : "string",
  "description" : "The job is running.",
  "enum" : [ "active" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobStateActive": _job_state_active_model_schema})

_job_state_completed_model_schema = json.loads(
    r"""{
  "title" : "JobStateCompleted",
  "type" : "string",
  "description" : "The job has completed successfully.",
  "enum" : [ "completed" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobStateCompleted": _job_state_completed_model_schema})

_job_state_delayed_model_schema = json.loads(
    r"""{
  "title" : "JobStateDelayed",
  "type" : "string",
  "description" : "The job has been delayed for retry after a failure.",
  "enum" : [ "delayed" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobStateDelayed": _job_state_delayed_model_schema})

_job_state_failed_model_schema = json.loads(
    r"""{
  "title" : "JobStateFailed",
  "type" : "string",
  "description" : "The job failed in execution.",
  "enum" : [ "failed" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobStateFailed": _job_state_failed_model_schema})

_job_state_finished_model_schema = json.loads(
    r"""{
  "title" : "JobStateFinished",
  "description" : "The job completed successfully or with failure.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/JobStateCompleted"
  }, {
    "$ref" : "#/components/schemas/JobStateFailed"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobStateFinished": _job_state_finished_model_schema})

_job_state_prioritized_model_schema = json.loads(
    r"""{
  "title" : "JobStatePrioritized",
  "type" : "string",
  "description" : "The job has been queued for execution with priority, but might be waiting because of rate limiting.",
  "enum" : [ "prioritized" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobStatePrioritized": _job_state_prioritized_model_schema})

_job_state_result_model_schema = json.loads(
    r"""{
  "description" : "All reported job states",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/JobState"
  }, {
    "$ref" : "#/components/schemas/JobStateUnknown"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobStateResult": _job_state_result_model_schema})

_job_state_unknown_model_schema = json.loads(
    r"""{
  "title" : "JobStateUnknown",
  "type" : "string",
  "description" : "The job state is unknown (undocument or inconsistent).",
  "enum" : [ "unknown" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobStateUnknown": _job_state_unknown_model_schema})

_job_state_waiting_model_schema = json.loads(
    r"""{
  "title" : "JobStateWaiting",
  "type" : "string",
  "description" : "The job has been queued for execution, but might be waiting because of rate limiting.",
  "enum" : [ "waiting" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobStateWaiting": _job_state_waiting_model_schema})

_job_state_waiting_children_model_schema = json.loads(
    r"""{
  "title" : "JobStateWaitingChildren",
  "type" : "string",
  "description" : "The job is waiting for child jobs to be completed.",
  "enum" : [ "waiting-children" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobStateWaitingChildren": _job_state_waiting_children_model_schema
})

_job_status_model_schema = json.loads(
    r"""{
  "title" : "JobStatus",
  "required" : [ "attemptsMade", "id", "name", "progress" ],
  "type" : "object",
  "properties" : {
    "id" : {
      "title" : "id",
      "type" : "string"
    },
    "name" : {
      "title" : "name",
      "type" : "string"
    },
    "progress" : {
      "$ref" : "#/components/schemas/JobStatus_progress"
    },
    "attemptsMade" : {
      "title" : "attemptsMade",
      "type" : "number"
    },
    "finishedOn" : {
      "title" : "finishedOn",
      "type" : "string",
      "format" : "date-time"
    },
    "processedOn" : {
      "title" : "processedOn",
      "type" : "string",
      "format" : "date-time"
    },
    "failedReason" : {
      "title" : "failedReason",
      "type" : "string"
    },
    "parent" : {
      "$ref" : "#/components/schemas/ParentKeys"
    },
    "delay" : {
      "title" : "delay",
      "type" : "number"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobStatus": _job_status_model_schema})

_job_status_and_entity_hal_links_model_schema = json.loads(
    r"""{
  "title" : "JobStatusAndEntityHALLinks",
  "description" : "HAL links to related actions.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Plug_2"
  }, {
    "$ref" : "#/components/schemas/Webscript_2"
  }, {
    "$ref" : "#/components/schemas/Model_2"
  }, {
    "$ref" : "#/components/schemas/JobStatusHALLink"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobStatusAndEntityHALLinks": _job_status_and_entity_hal_links_model_schema
})

_job_status_hal_link_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "job" : {
      "$ref" : "#/components/schemas/JobHALLinks_job"
    }
  },
  "description" : "HAL links to related actions."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobStatusHALLink": _job_status_hal_link_model_schema})

_job_status_progress_model_schema = json.loads(
    r"""{
  "title" : "JobStatus_progress",
  "anyOf" : [ {
    "type" : "number"
  }, {
    "type" : "object"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobStatus_progress": _job_status_progress_model_schema})

_job_type_model_schema = json.loads(
    r"""{
  "type" : "string",
  "enum" : [ "build", "deploy", "verify", "undeploy", "batch", "scale", "cleanup", "notify" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobType": _job_type_model_schema})

_job_type_batch_model_schema = json.loads(
    r"""{
  "title" : "JobTypeBatch",
  "type" : "string",
  "description" : "A job that groups other jobs as a parent.",
  "enum" : [ "batch" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobTypeBatch": _job_type_batch_model_schema})

_job_type_build_model_schema = json.loads(
    r"""{
  "title" : "JobTypeBuild",
  "type" : "string",
  "description" : "Build",
  "enum" : [ "build" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobTypeBuild": _job_type_build_model_schema})

_job_type_deploy_model_schema = json.loads(
    r"""{
  "title" : "JobTypeDeploy",
  "type" : "string",
  "description" : "A job that deploys a function image to the openfaas runtime.",
  "enum" : [ "deploy" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobTypeDeploy": _job_type_deploy_model_schema})

_job_type_notify_model_schema = json.loads(
    r"""{
  "title" : "JobTypeNotify",
  "type" : "string",
  "description" : "A job to notify that an function version has changed.",
  "enum" : [ "notify" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobTypeNotify": _job_type_notify_model_schema})

_job_type_scale_model_schema = json.loads(
    r"""{
  "title" : "JobTypeScale",
  "type" : "string",
  "description" : "A job that scales a function to a target.",
  "enum" : [ "scale" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobTypeScale": _job_type_scale_model_schema})

_job_type_schema_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/JobTypeBuild"
  }, {
    "$ref" : "#/components/schemas/JobTypeDeploy"
  }, {
    "$ref" : "#/components/schemas/JobTypeVerify"
  }, {
    "$ref" : "#/components/schemas/JobTypeUndeploy"
  }, {
    "$ref" : "#/components/schemas/JobTypeScale"
  }, {
    "$ref" : "#/components/schemas/JobTypeBatch"
  }, {
    "$ref" : "#/components/schemas/JobTypeNotify"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobTypeSchema": _job_type_schema_model_schema})

_job_type_undeploy_model_schema = json.loads(
    r"""{
  "title" : "JobTypeUndeploy",
  "type" : "string",
  "description" : "A job that undeploys a deployed function and removes it from the registry.",
  "enum" : [ "undeploy" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobTypeUndeploy": _job_type_undeploy_model_schema})

_job_type_verify_model_schema = json.loads(
    r"""{
  "title" : "JobTypeVerify",
  "type" : "string",
  "description" : "A job that checks the health of a deployed function.",
  "enum" : [ "verify" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobTypeVerify": _job_type_verify_model_schema})

_jobs_for_model_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "function", "jobs" ],
  "type" : "object",
  "properties" : {
    "jobs" : {
      "type" : "array",
      "description" : "Listing of jobs related to the function deployment. This includes active jobs, and the most recently failed job (per type) that was archived on the entity.",
      "items" : {
        "$ref" : "#/components/schemas/AnyJobForFunction"
      }
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobsForModelResponseV2__links"
    }
  },
  "description" : "Model Jobs Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobsForModelResponseV2": _jobs_for_model_response_v2_model_schema
})

_jobs_for_model_response_v2__links_model_schema = json.loads(
    r"""{
  "title" : "JobsForModelResponseV2__links",
  "type" : "object",
  "properties" : {
    "model" : {
      "$ref" : "#/components/schemas/HALLinks"
    }
  },
  "additionalProperties" : false,
  "description" : "Link to the function entity."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobsForModelResponseV2__links": _jobs_for_model_response_v2__links_model_schema
})

_jobs_for_plug_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "function", "jobs" ],
  "type" : "object",
  "properties" : {
    "jobs" : {
      "type" : "array",
      "description" : "Listing of jobs related to the function deployment. This includes active jobs, and the most recently failed job (per type) that was archived on the entity.",
      "items" : {
        "$ref" : "#/components/schemas/AnyJobForFunction"
      }
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobsForPlugResponseV2__links"
    }
  },
  "description" : "Plug Jobs Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobsForPlugResponseV2": _jobs_for_plug_response_v2_model_schema
})

_jobs_for_plug_response_v2__links_model_schema = json.loads(
    r"""{
  "title" : "JobsForPlugResponseV2__links",
  "type" : "object",
  "properties" : {
    "plug" : {
      "$ref" : "#/components/schemas/HALLinks"
    }
  },
  "additionalProperties" : false,
  "description" : "Link to the function entity."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobsForPlugResponseV2__links": _jobs_for_plug_response_v2__links_model_schema
})

_jobs_for_webscript_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "function", "jobs" ],
  "type" : "object",
  "properties" : {
    "jobs" : {
      "type" : "array",
      "description" : "Listing of jobs related to the function deployment. This includes active jobs, and the most recently failed job (per type) that was archived on the entity.",
      "items" : {
        "$ref" : "#/components/schemas/AnyJobForFunction"
      }
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobsForWebscriptResponseV2__links"
    }
  },
  "description" : "Webscript Jobs Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobsForWebscriptResponseV2": _jobs_for_webscript_response_v2_model_schema
})

_jobs_for_webscript_response_v2__links_model_schema = json.loads(
    r"""{
  "title" : "JobsForWebscriptResponseV2__links",
  "type" : "object",
  "properties" : {
    "webscript" : {
      "$ref" : "#/components/schemas/HALLinks"
    }
  },
  "additionalProperties" : false,
  "description" : "Link to the function entity."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobsForWebscriptResponseV2__links": _jobs_for_webscript_response_v2__links_model_schema
})

_jobs_response_model_schema = json.loads(
    r"""{
  "required" : [ "jobs" ],
  "type" : "object",
  "properties" : {
    "limit" : {
      "type" : "number",
      "description" : "The page size used for this query result."
    },
    "jobs" : {
      "type" : "array",
      "description" : "Listing of jobs that satisfy the query.",
      "items" : {
        "$ref" : "#/components/schemas/AnyJobStatusSummary"
      }
    }
  },
  "description" : "Jobs Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobsResponse": _jobs_response_model_schema})

_kf_serving_manifest_model_schema = json.loads(
    r"""{
  "title" : "KFServingManifest",
  "required" : [ "metadata", "name", "runtime", "version" ],
  "type" : "object",
  "properties" : {
    "deploy" : {
      "$ref" : "#/components/schemas/FunctionDeployOverridesType"
    },
    "name" : {
      "title" : "name",
      "type" : "string",
      "description" : "The logical name for the function."
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "metadata" : {
      "$ref" : "#/components/schemas/FunctionMeta"
    },
    "protected" : {
      "title" : "protected",
      "type" : "boolean",
      "description" : "Indicates whether the function's script and other assets should be protected."
    },
    "tags" : {
      "title" : "tags",
      "type" : "array",
      "description" : "Tags associated with this entity.",
      "items" : {
        "$ref" : "#/components/schemas/TagOrTagReference"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"KFServingManifest": _kf_serving_manifest_model_schema})

_kf_serving_manifest_patch_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "metadata" : {
      "$ref" : "#/components/schemas/FunctionMeta"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "deploy" : {
      "$ref" : "#/components/schemas/FunctionDeployOverridesType"
    }
  },
  "additionalProperties" : false,
  "description" : "Patch attributes to merge into an existing model manifest."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "KFServingManifestPatch": _kf_serving_manifest_patch_model_schema
})

_keep_alive_event_sse_model_schema = json.loads(
    r"""{
  "required" : [ "event" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/EventKeepAlive"
    },
    "data" : {
      "type" : "string",
      "description" : "A text message acknowledging that events will be forwarded."
    }
  },
  "description" : "A message that acknowledges that the stream is still alive."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"KeepAliveEventSSE": _keep_alive_event_sse_model_schema})

_kfserving_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "deprecated", "draft", "model", "runtime", "status", "updatedAt", "updatedBy" ],
  "type" : "object",
  "properties" : {
    "createdBy" : {
      "type" : "string",
      "description" : "The user that created this entity."
    },
    "createdAt" : {
      "type" : "string",
      "description" : "The timestamp at which this entity was created.",
      "format" : "date-time"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "The user that last updated this entity."
    },
    "updatedAt" : {
      "type" : "string",
      "description" : "The timestamp at which this entity was last updated.",
      "format" : "date-time"
    },
    "updates" : {
      "type" : "array",
      "description" : "The audit logs corresponding to the latest modifying operations on this entity. Omitted in listing operations.",
      "items" : {
        "$ref" : "#/components/schemas/UpdateRecord"
      }
    },
    "status" : {
      "$ref" : "#/components/schemas/Status"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/RuntimeAttributes"
    },
    "deprecated" : {
      "type" : "boolean",
      "description" : "If <code>true</code> this function is deprecated and removed from regular listings."
    },
    "draft" : {
      "type" : "boolean",
      "description" : "If <code>true</code> this function is a draft function and it's assets are still mutable."
    },
    "revision" : {
      "type" : "string",
      "description" : "The revision of the function. This will be <code>undefined</code> when the plug is not a draft."
    },
    "model" : {
      "$ref" : "#/components/schemas/KFServingManifest"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"KfservingResponseV2": _kfserving_response_v2_model_schema})

_language_release_model_schema = json.loads(
    r"""{
  "title" : "LanguageRelease",
  "required" : [ "name", "title", "version" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "type" : "string",
      "description" : "Short technical name of the language or framework used."
    },
    "version" : {
      "title" : "version",
      "type" : "string",
      "description" : "Release version of the language or framework."
    },
    "title" : {
      "title" : "title",
      "type" : "string",
      "description" : "Display title."
    },
    "description" : {
      "title" : "description",
      "type" : "string"
    }
  },
  "description" : "Description of the language or framework release used by a runtime (version)."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"LanguageRelease": _language_release_model_schema})

_latest_models_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "count", "entities" ],
  "type" : "object",
  "properties" : {
    "_embedded" : {
      "$ref" : "#/components/schemas/GetPlugResponseV2__embedded"
    },
    "limit" : {
      "type" : "number",
      "description" : "The page size used for this query result."
    },
    "count" : {
      "type" : "number",
      "description" : "The total count of matching items, from which this result is one page."
    },
    "page" : {
      "type" : "number",
      "description" : "The page number of a paged query result."
    },
    "entities" : {
      "type" : "array",
      "description" : "The specification and deployment status of the queried functions",
      "items" : {
        "$ref" : "#/components/schemas/EntityWithLinks_IKfservingResponseV2_"
      }
    }
  },
  "description" : "Models Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LatestModelsResponseV2": _latest_models_response_v2_model_schema
})

_latest_plugs_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "count", "entities" ],
  "type" : "object",
  "properties" : {
    "_embedded" : {
      "$ref" : "#/components/schemas/GetPlugResponseV2__embedded"
    },
    "limit" : {
      "type" : "number",
      "description" : "The page size used for this query result."
    },
    "count" : {
      "type" : "number",
      "description" : "The total count of matching items, from which this result is one page."
    },
    "page" : {
      "type" : "number",
      "description" : "The page number of a paged query result."
    },
    "entities" : {
      "type" : "array",
      "description" : "The specification and deployment status of the queried functions",
      "items" : {
        "$ref" : "#/components/schemas/EntityWithLinks_IPlugResponseV2_"
      }
    }
  },
  "description" : "Plugs Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LatestPlugsResponseV2": _latest_plugs_response_v2_model_schema
})

_latest_version_level_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Level of latest versions that should be included.",
  "enum" : [ "major", "minor", "patch", "true", "false" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"LatestVersionLevel": _latest_version_level_model_schema})

_latest_webscripts_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "count", "entities" ],
  "type" : "object",
  "properties" : {
    "_embedded" : {
      "$ref" : "#/components/schemas/GetPlugResponseV2__embedded"
    },
    "limit" : {
      "type" : "number",
      "description" : "The page size used for this query result."
    },
    "count" : {
      "type" : "number",
      "description" : "The total count of matching items, from which this result is one page."
    },
    "page" : {
      "type" : "number",
      "description" : "The page number of a paged query result."
    },
    "entities" : {
      "type" : "array",
      "description" : "The specification and deployment status of the queried functions",
      "items" : {
        "$ref" : "#/components/schemas/EntityWithLinks_IWebscriptResponseWithInvokeLinkV2_"
      }
    }
  },
  "description" : "Webscripts Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LatestWebscriptsResponseV2": _latest_webscripts_response_v2_model_schema
})

_list_runtimes_tags_parameter_model_schema = json.loads(
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
MODEL_DEFINITIONS.update({
    "list_runtimes_tags_parameter": _list_runtimes_tags_parameter_model_schema
})

_model_model_schema = json.loads(
    r"""{
  "title" : "Model",
  "required" : [ "model" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/HALLinks"
    },
    "model" : {
      "$ref" : "#/components/schemas/HALLinks"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Model": _model_model_schema})

_model_1_model_schema = json.loads(
    r"""{
  "title" : "Model",
  "required" : [ "model" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/HALLinks"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobHALLinks_job"
    },
    "model" : {
      "$ref" : "#/components/schemas/HALLinks"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Model_1": _model_1_model_schema})

_model_2_model_schema = json.loads(
    r"""{
  "title" : "Model",
  "required" : [ "model" ],
  "type" : "object",
  "properties" : {
    "job" : {
      "$ref" : "#/components/schemas/JobHALLinks_job"
    },
    "model" : {
      "$ref" : "#/components/schemas/HALLinks"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Model_2": _model_2_model_schema})

_model_versions_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "count", "entities" ],
  "type" : "object",
  "properties" : {
    "_embedded" : {
      "$ref" : "#/components/schemas/GetPlugResponseV2__embedded"
    },
    "limit" : {
      "type" : "number",
      "description" : "The page size used for this query result."
    },
    "count" : {
      "type" : "number",
      "description" : "The total count of matching items, from which this result is one page."
    },
    "page" : {
      "type" : "number",
      "description" : "The page number of a paged query result."
    },
    "entities" : {
      "type" : "array",
      "description" : "The specification and deployment status of the queried functions",
      "items" : {
        "$ref" : "#/components/schemas/KfservingResponseV2"
      }
    }
  },
  "description" : "Model Versions Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ModelVersionsResponseV2": _model_versions_response_v2_model_schema
})

_notify_result_model_schema = json.loads(
    r"""{
  "title" : "NotifyResult",
  "required" : [ "operation" ],
  "type" : "object",
  "properties" : {
    "operation" : {
      "$ref" : "#/components/schemas/RequestOperation"
    }
  },
  "description" : "The result data for a change notification."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"NotifyResult": _notify_result_model_schema})

_parent_keys_model_schema = json.loads(
    r"""{
  "title" : "ParentKeys",
  "required" : [ "id" ],
  "type" : "object",
  "properties" : {
    "id" : {
      "title" : "id",
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ParentKeys": _parent_keys_model_schema})

_plug_model_schema = json.loads(
    r"""{
  "title" : "Plug",
  "required" : [ "plug" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/HALLinks"
    },
    "plug" : {
      "$ref" : "#/components/schemas/HALLinks"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Plug": _plug_model_schema})

_plug_1_model_schema = json.loads(
    r"""{
  "title" : "Plug",
  "required" : [ "plug" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/HALLinks"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobHALLinks_job"
    },
    "plug" : {
      "$ref" : "#/components/schemas/HALLinks"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Plug_1": _plug_1_model_schema})

_plug_2_model_schema = json.loads(
    r"""{
  "title" : "Plug",
  "required" : [ "plug" ],
  "type" : "object",
  "properties" : {
    "job" : {
      "$ref" : "#/components/schemas/JobHALLinks_job"
    },
    "plug" : {
      "$ref" : "#/components/schemas/HALLinks"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Plug_2": _plug_2_model_schema})

_plug_interface_model_schema = json.loads(
    r"""{
  "title" : "PlugInterface",
  "type" : "object",
  "properties" : {
    "states" : {
      "title" : "states",
      "type" : "array",
      "description" : "The states of a plug as implemented in the plug code. Required and supported for `type=sensor` plugs _only_.",
      "items" : {
        "type" : "string"
      }
    },
    "input" : {
      "title" : "input",
      "type" : "array",
      "description" : "The named input parameters of a plug. Supported for `type=sensor` plugs; fixed with input attributes `data` and `resource` for `type=transformer`plugs.",
      "items" : {
        "$ref" : "#/components/schemas/PlugProperty"
      }
    },
    "output" : {
      "title" : "output",
      "type" : "array",
      "description" : "The named output parameters of a plug. Supported for all plug types.",
      "items" : {
        "$ref" : "#/components/schemas/PlugProperty"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PlugInterface": _plug_interface_model_schema})

_plug_manifest_model_schema = json.loads(
    r"""{
  "title" : "PlugManifest",
  "required" : [ "interface", "metadata", "name", "runtime", "type", "version" ],
  "type" : "object",
  "properties" : {
    "deploy" : {
      "$ref" : "#/components/schemas/FunctionDeployOverridesType"
    },
    "name" : {
      "title" : "name",
      "type" : "string",
      "description" : "The logical name for the function."
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "metadata" : {
      "$ref" : "#/components/schemas/PlugMeta"
    },
    "protected" : {
      "title" : "protected",
      "type" : "boolean",
      "description" : "Indicates whether the function's script and other assets should be protected."
    },
    "tags" : {
      "title" : "tags",
      "type" : "array",
      "description" : "Tags associated with this entity.",
      "items" : {
        "$ref" : "#/components/schemas/TagOrTagReference"
      }
    },
    "type" : {
      "$ref" : "#/components/schemas/PlugType"
    },
    "interface" : {
      "$ref" : "#/components/schemas/PlugInterface"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PlugManifest": _plug_manifest_model_schema})

_plug_manifest_patch_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/PlugType"
    },
    "interface" : {
      "$ref" : "#/components/schemas/PlugInterface"
    },
    "metadata" : {
      "$ref" : "#/components/schemas/PlugMeta"
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "deploy" : {
      "$ref" : "#/components/schemas/FunctionDeployOverridesType"
    }
  },
  "additionalProperties" : false,
  "description" : "Patch attributes to merge into an existing plug manifest."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PlugManifestPatch": _plug_manifest_patch_model_schema})

_plug_meta_model_schema = json.loads(
    r"""{
  "title" : "PlugMeta",
  "type" : "object",
  "properties" : {
    "author" : {
      "title" : "author",
      "type" : "string",
      "description" : "The author of the function."
    },
    "description" : {
      "title" : "description",
      "type" : "string",
      "description" : "A description of the function"
    },
    "iconURL" : {
      "title" : "iconURL",
      "type" : "string",
      "description" : "An url to an icon that represents this function."
    },
    "category" : {
      "title" : "category",
      "type" : "string",
      "description" : "A category for this function (Deprecated: use tags to categorise your functions)",
      "deprecated" : true
    },
    "documentationURL" : {
      "title" : "documentationURL",
      "type" : "string",
      "description" : "External url that document this function."
    },
    "friendlyName" : {
      "title" : "friendlyName",
      "type" : "string",
      "description" : "Display title for this function."
    },
    "tags" : {
      "title" : "tags",
      "type" : "array",
      "description" : "Tag references or tag objects associated with this function. See `showTags` query parameter on how referenced tags are displayed. During update, a (reference to a) tag\n- that does not yet exist, is created (using default attributes if not specified)\n- that does exist is not updated (even if tag attributes like `color` differ)",
      "example" : [ "awaiting-review", {
        "name" : "demo",
        "color" : "#e639a4"
      } ],
      "deprecated" : false,
      "items" : {
        "$ref" : "#/components/schemas/TagOrTagReference"
      }
    },
    "documentation" : {
      "$ref" : "#/components/schemas/Documentation"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PlugMeta": _plug_meta_model_schema})

_plug_property_model_schema = json.loads(
    r"""{
  "title" : "PlugProperty",
  "required" : [ "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "type" : "string",
      "description" : "The name of a plug input or output property."
    },
    "dataType" : {
      "$ref" : "#/components/schemas/PlugPropertyDataType"
    },
    "mandatory" : {
      "title" : "mandatory",
      "type" : "boolean",
      "description" : "If <code>true</code> this property is required.",
      "example" : true
    },
    "format" : {
      "$ref" : "#/components/schemas/PlugPropertyFormat"
    },
    "defaultValue" : {
      "$ref" : "#/components/schemas/DefaultValue"
    }
  },
  "description" : "Interface specification of a plug property."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PlugProperty": _plug_property_model_schema})

_plug_property_data_type_model_schema = json.loads(
    r"""{
  "title" : "PlugPropertyDataType",
  "type" : "string",
  "description" : "Datatype supported in plug input or output properties.",
  "enum" : [ "string", "integer", "long", "float", "double", "boolean", "object", "array" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PlugPropertyDataType": _plug_property_data_type_model_schema
})

_plug_property_format_model_schema = json.loads(
    r"""{
  "title" : "PlugPropertyFormat",
  "required" : [ "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/PlugPropertyFormatType"
    },
    "values" : {
      "title" : "values",
      "type" : "array",
      "description" : "The enumerated value domain when <code>type=\"enum\"</code>",
      "example" : [ "low", "high" ],
      "items" : {
        "$ref" : "#/components/schemas/EnumValue"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PlugPropertyFormat": _plug_property_format_model_schema})

_plug_property_format_type_model_schema = json.loads(
    r"""{
  "title" : "PlugPropertyFormatType",
  "type" : "string",
  "description" : "Value domain for a plug input or output property.",
  "enum" : [ "enum", "resource", "vault", "duration", "code", "url", "date", "template", "aiPluginDescriptor", "aiTemplateDescriptor" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PlugPropertyFormatType": _plug_property_format_type_model_schema
})

_plug_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "deprecated", "draft", "plug", "runtime", "status", "updatedAt", "updatedBy" ],
  "type" : "object",
  "properties" : {
    "createdBy" : {
      "type" : "string",
      "description" : "The user that created this entity."
    },
    "createdAt" : {
      "type" : "string",
      "description" : "The timestamp at which this entity was created.",
      "format" : "date-time"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "The user that last updated this entity."
    },
    "updatedAt" : {
      "type" : "string",
      "description" : "The timestamp at which this entity was last updated.",
      "format" : "date-time"
    },
    "updates" : {
      "type" : "array",
      "description" : "The audit logs corresponding to the latest modifying operations on this entity. Omitted in listing operations.",
      "items" : {
        "$ref" : "#/components/schemas/UpdateRecord"
      }
    },
    "status" : {
      "$ref" : "#/components/schemas/Status"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/RuntimeAttributes"
    },
    "deprecated" : {
      "type" : "boolean",
      "description" : "If <code>true</code> this plug is removed from regular listings, as a result of a <code>DELETE</code> with <code>force=false</code>."
    },
    "draft" : {
      "type" : "boolean",
      "description" : "If <code>true</code> this function is a draft function and it's assets are still mutable."
    },
    "revision" : {
      "type" : "string",
      "description" : "The revision of the function. This will be <code>undefined</code> when the plug is not a draft."
    },
    "plug" : {
      "$ref" : "#/components/schemas/PlugManifest"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PlugResponseV2": _plug_response_v2_model_schema})

_plug_type_model_schema = json.loads(
    r"""{
  "type" : "string",
  "enum" : [ "sensor", "actuator", "transformer" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PlugType": _plug_type_model_schema})

_plug_versions_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "count", "entities" ],
  "type" : "object",
  "properties" : {
    "_embedded" : {
      "$ref" : "#/components/schemas/GetPlugResponseV2__embedded"
    },
    "limit" : {
      "type" : "number",
      "description" : "The page size used for this query result."
    },
    "count" : {
      "type" : "number",
      "description" : "The total count of matching items, from which this result is one page."
    },
    "page" : {
      "type" : "number",
      "description" : "The page number of a paged query result."
    },
    "entities" : {
      "type" : "array",
      "description" : "The specification and deployment status of the queried functions",
      "items" : {
        "$ref" : "#/components/schemas/PlugResponseV2"
      }
    }
  },
  "description" : "Plugs Versions Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PlugVersionsResponseV2": _plug_versions_response_v2_model_schema
})

_plug_with_invocation_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "deprecated", "draft", "invocation", "plug", "runtime", "status", "updatedAt", "updatedBy" ],
  "type" : "object",
  "properties" : {
    "createdBy" : {
      "type" : "string",
      "description" : "The user that created this entity."
    },
    "createdAt" : {
      "type" : "string",
      "description" : "The timestamp at which this entity was created.",
      "format" : "date-time"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "The user that last updated this entity."
    },
    "updatedAt" : {
      "type" : "string",
      "description" : "The timestamp at which this entity was last updated.",
      "format" : "date-time"
    },
    "updates" : {
      "type" : "array",
      "description" : "The audit logs corresponding to the latest modifying operations on this entity. Omitted in listing operations.",
      "items" : {
        "$ref" : "#/components/schemas/UpdateRecord"
      }
    },
    "status" : {
      "$ref" : "#/components/schemas/Status"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/RuntimeAttributes"
    },
    "deprecated" : {
      "type" : "boolean",
      "description" : "If <code>true</code> this plug is removed from regular listings, as a result of a <code>DELETE</code> with <code>force=false</code>."
    },
    "draft" : {
      "type" : "boolean",
      "description" : "If <code>true</code> this function is a draft function and it's assets are still mutable."
    },
    "revision" : {
      "type" : "string",
      "description" : "The revision of the function. This will be <code>undefined</code> when the plug is not a draft."
    },
    "plug" : {
      "$ref" : "#/components/schemas/PlugManifest"
    },
    "invocation" : {
      "$ref" : "#/components/schemas/InvocationAttributes"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PlugWithInvocationResponseV2": _plug_with_invocation_response_v2_model_schema
})

_post_model_job_async_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "entity", "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    },
    "entity" : {
      "$ref" : "#/components/schemas/KfservingResponseV2"
    }
  },
  "description" : "Model Deployment Initiated"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PostModelJobAsyncResponseV2": _post_model_job_async_response_v2_model_schema
})

_post_model_job_sync_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "entity", "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "entity" : {
      "$ref" : "#/components/schemas/KfservingResponseV2"
    }
  },
  "description" : "Model Deployed"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PostModelJobSyncResponseV2": _post_model_job_sync_response_v2_model_schema
})

_post_plug_job_async_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "entity", "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    },
    "entity" : {
      "$ref" : "#/components/schemas/PlugResponseV2"
    }
  },
  "description" : "Plug Deployment Initiated"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PostPlugJobAsyncResponseV2": _post_plug_job_async_response_v2_model_schema
})

_post_plug_job_sync_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "entity", "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "entity" : {
      "$ref" : "#/components/schemas/PlugResponseV2"
    }
  },
  "description" : "Plug Deployed"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PostPlugJobSyncResponseV2": _post_plug_job_sync_response_v2_model_schema
})

_post_webscript_job_async_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "entity", "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    },
    "entity" : {
      "$ref" : "#/components/schemas/WebscriptResponseV2"
    }
  },
  "description" : "Webscript Deployment Initiated"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PostWebscriptJobAsyncResponseV2": _post_webscript_job_async_response_v2_model_schema
})

_post_webscript_job_sync_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "entity", "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "entity" : {
      "$ref" : "#/components/schemas/WebscriptResponseV2"
    }
  },
  "description" : "Webscript Deployed"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PostWebscriptJobSyncResponseV2": _post_webscript_job_sync_response_v2_model_schema
})

_protect_by_name_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "message", "versions" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "versions" : {
      "type" : "array",
      "description" : "The versions that were protected or unprotected.",
      "items" : {
        "$ref" : "#/components/schemas/SemanticVersion"
      }
    }
  },
  "description" : "Protection changed."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ProtectByNameResponseV2": _protect_by_name_response_v2_model_schema
})

_provided_dependency_model_schema = json.loads(
    r"""{
  "title" : "ProvidedDependency",
  "required" : [ "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "type" : "string",
      "description" : "Name of a provided dependency."
    },
    "title" : {
      "title" : "title",
      "type" : "string",
      "description" : "Optional display title."
    },
    "description" : {
      "title" : "description",
      "type" : "string",
      "description" : "Optional description."
    },
    "version" : {
      "title" : "version",
      "type" : "string",
      "description" : "Versions specification of a provided dependency"
    },
    "deprecated" : {
      "title" : "deprecated",
      "type" : "boolean",
      "description" : "If true, this provided dependency is scheduled for removal (or incompatible upgrade) in a next runtime version.",
      "default" : false
    },
    "removed" : {
      "title" : "removed",
      "type" : "boolean",
      "description" : "If true, this dependency has been removed from the runtime (version)",
      "default" : false
    },
    "globals" : {
      "title" : "globals",
      "type" : "array",
      "description" : "Global variables that expose this library to the user code. As the usage of these globals is deprecated, any usage of such global will pose issues in an next runtime version.",
      "items" : {
        "type" : "string"
      }
    },
    "native" : {
      "title" : "native",
      "type" : "boolean",
      "description" : "If true, the library is provided natively by the runtime: e.g. node for javascript."
    }
  },
  "description" : "Library dependency that is provided by this runtime."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ProvidedDependency": _provided_dependency_model_schema})

_queue_events_model_schema = json.loads(
    r"""{
  "title" : "QueueEvents",
  "type" : "string",
  "enum" : [ "completed", "failed", "active", "delayed", "waiting", "waiting-children", "added", "cleaned", "drained", "error", "paused", "progress", "removed", "resumed", "retries-exhausted", "stalled" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"QueueEvents": _queue_events_model_schema})

_rebuild_model_async_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "causes", "entity", "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    },
    "causes" : {
      "$ref" : "#/components/schemas/JobCauses"
    },
    "entity" : {
      "$ref" : "#/components/schemas/KfservingResponseV2"
    }
  },
  "description" : "Model Rebuild Initiated"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "RebuildModelAsyncResponseV2": _rebuild_model_async_response_v2_model_schema
})

_rebuild_model_sync_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "causes", "entity", "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "causes" : {
      "$ref" : "#/components/schemas/JobCauses"
    },
    "entity" : {
      "$ref" : "#/components/schemas/KfservingResponseV2"
    }
  },
  "description" : "Model Rebuild Ignored"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "RebuildModelSyncResponseV2": _rebuild_model_sync_response_v2_model_schema
})

_rebuild_plug_async_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "causes", "entity", "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    },
    "causes" : {
      "$ref" : "#/components/schemas/JobCauses"
    },
    "entity" : {
      "$ref" : "#/components/schemas/PlugResponseV2"
    }
  },
  "description" : "Plug Rebuild Initiated"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "RebuildPlugAsyncResponseV2": _rebuild_plug_async_response_v2_model_schema
})

_rebuild_plug_sync_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "causes", "entity", "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "causes" : {
      "$ref" : "#/components/schemas/JobCauses"
    },
    "entity" : {
      "$ref" : "#/components/schemas/PlugResponseV2"
    }
  },
  "description" : "Plug Rebuild Ignored"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "RebuildPlugSyncResponseV2": _rebuild_plug_sync_response_v2_model_schema
})

_rebuild_policy_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "The policy to select a new <em>runtime</em> version when a rebuild is issued.",
  "enum" : [ "patch", "minor", "major", "same" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RebuildPolicy": _rebuild_policy_model_schema})

_rebuild_request_v2_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "deploy" : {
      "$ref" : "#/components/schemas/FunctionDeployOverridesType"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RebuildRequestV2": _rebuild_request_v2_model_schema})

_rebuild_webscript_async_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "causes", "entity", "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    },
    "causes" : {
      "$ref" : "#/components/schemas/JobCauses"
    },
    "entity" : {
      "$ref" : "#/components/schemas/WebscriptResponseV2"
    }
  },
  "description" : "Webscript Rebuild Initiated"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "RebuildWebscriptAsyncResponseV2": _rebuild_webscript_async_response_v2_model_schema
})

_rebuild_webscript_sync_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "causes", "entity", "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "causes" : {
      "$ref" : "#/components/schemas/JobCauses"
    },
    "entity" : {
      "$ref" : "#/components/schemas/WebscriptResponseV2"
    }
  },
  "description" : "Webscript Rebuild Ignored"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "RebuildWebscriptSyncResponseV2": _rebuild_webscript_sync_response_v2_model_schema
})

_registry_error_response_model_schema = json.loads(
    r"""{
  "required" : [ "code", "error", "statusCode" ],
  "type" : "object",
  "properties" : {
    "error" : {
      "type" : "string"
    },
    "code" : {
      "type" : "string"
    },
    "statusCode" : {
      "type" : "number"
    },
    "data" : {
      "type" : "object",
      "additionalProperties" : {
        "type" : "string"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "RegistryErrorResponse": _registry_error_response_model_schema
})

_request_operation_model_schema = json.loads(
    r"""{
  "title" : "RequestOperation",
  "type" : "string",
  "description" : "A modifying operation on the function.",
  "enum" : [ "create", "metadata-update", "assets-update", "rebuild", "verify", "publish", "deprecate", "undeploy", "undeprecate", "protect", "unprotect" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RequestOperation": _request_operation_model_schema})

_resource_limits_model_schema = json.loads(
    r"""{
  "title" : "ResourceLimits",
  "type" : "object",
  "properties" : {
    "memory" : {
      "title" : "memory",
      "type" : "string"
    },
    "cpu" : {
      "title" : "cpu",
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ResourceLimits": _resource_limits_model_schema})

_root_page_response_model_schema = json.loads(
    r"""{
  "required" : [ "enabled", "name", "revision", "version" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "description" : "Name of the service."
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "enabled" : {
      "type" : "object",
      "description" : "Description of the features enabled on this service deployment."
    },
    "revision" : {
      "type" : "string",
      "description" : "Revision of the service source code."
    }
  },
  "description" : "Status Page"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RootPageResponse": _root_page_response_model_schema})

_runtime_attributes_model_schema = json.loads(
    r"""{
  "title" : "RuntimeAttributes",
  "required" : [ "deprecated", "name", "upgradable", "version" ],
  "type" : "object",
  "properties" : {
    "deprecated" : {
      "title" : "deprecated",
      "type" : "boolean",
      "description" : "If true, the function uses a deprecated runtime."
    },
    "upgradable" : {
      "title" : "upgradable",
      "type" : "boolean",
      "description" : "If true, a newer runtime for this function is available using the `rebuild` API."
    },
    "name" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RuntimeAttributes": _runtime_attributes_model_schema})

_runtime_summary_model_schema = json.loads(
    r"""{
  "required" : [ "archiveFormat", "functionType", "name", "title", "versions" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "title" : {
      "type" : "string"
    },
    "description" : {
      "type" : "string"
    },
    "functionType" : {
      "$ref" : "#/components/schemas/FunctionType"
    },
    "archiveFormat" : {
      "$ref" : "#/components/schemas/ArchiveFormat"
    },
    "tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/TagReference"
      }
    },
    "versions" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/RuntimeVersionInfo"
      }
    }
  },
  "description" : "A summary representation of the runtime, and (selected) versions of it."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RuntimeSummary": _runtime_summary_model_schema})

_runtime_summary_response_model_schema = json.loads(
    r"""{
  "required" : [ "runtimes" ],
  "type" : "object",
  "properties" : {
    "_embedded" : {
      "$ref" : "#/components/schemas/RuntimeSummaryResponse__embedded"
    },
    "runtimes" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/RuntimeSummary"
      }
    }
  },
  "description" : "Runtimes Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "RuntimeSummaryResponse": _runtime_summary_response_model_schema
})

_runtime_summary_response__embedded_model_schema = json.loads(
    r"""{
  "title" : "RuntimeSummaryResponse__embedded",
  "type" : "object",
  "properties" : {
    "tags" : {
      "title" : "tags",
      "type" : "array",
      "description" : "Record of <tag key, tag representation> pairs.",
      "items" : {
        "$ref" : "#/components/schemas/RuntimeTag"
      }
    }
  },
  "description" : "Embedded representations of the referenced tags."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "RuntimeSummaryResponse__embedded": _runtime_summary_response__embedded_model_schema
})

_runtime_tag_model_schema = json.loads(
    r"""{
  "title" : "RuntimeTag",
  "required" : [ "color", "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "$ref" : "#/components/schemas/TagReference"
    },
    "color" : {
      "title" : "color",
      "type" : "string",
      "description" : "Color associated with the tag in an UI."
    },
    "description" : {
      "title" : "description",
      "type" : "string",
      "description" : "Description of the tag"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RuntimeTag": _runtime_tag_model_schema})

_runtime_tag_filter_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/RuntimeIncludeTag"
  }, {
    "$ref" : "#/components/schemas/RuntimeExcludeTag"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RuntimeTagFilter": _runtime_tag_filter_model_schema})

_runtime_tag_response_model_schema = json.loads(
    r"""{
  "required" : [ "tag" ],
  "type" : "object",
  "properties" : {
    "tag" : {
      "$ref" : "#/components/schemas/RuntimeTag"
    }
  },
  "description" : "Runtime Tag Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RuntimeTagResponse": _runtime_tag_response_model_schema})

_runtime_tags_response_model_schema = json.loads(
    r"""{
  "required" : [ "tags" ],
  "type" : "object",
  "properties" : {
    "tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/RuntimeTag"
      }
    }
  },
  "description" : "Runtime Tags Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RuntimeTagsResponse": _runtime_tags_response_model_schema})

_runtime_version_info_model_schema = json.loads(
    r"""{
  "title" : "RuntimeVersionInfo",
  "required" : [ "deprecated", "title", "upgradable", "version" ],
  "type" : "object",
  "properties" : {
    "deprecated" : {
      "title" : "deprecated",
      "type" : "boolean",
      "description" : "If true, the function uses a deprecated runtime."
    },
    "upgradable" : {
      "title" : "upgradable",
      "type" : "boolean",
      "description" : "If true, a newer runtime for this function is available using the `rebuild` API."
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "title" : {
      "title" : "title",
      "type" : "string"
    },
    "description" : {
      "title" : "description",
      "type" : "string"
    },
    "tags" : {
      "title" : "tags",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/TagReference"
      }
    }
  },
  "description" : "A summary of a selected version for a runtime"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RuntimeVersionInfo": _runtime_version_info_model_schema})

_runtime_version_response_model_schema = json.loads(
    r"""{
  "required" : [ "runtime" ],
  "type" : "object",
  "properties" : {
    "_embedded" : {
      "$ref" : "#/components/schemas/RuntimeSummaryResponse__embedded"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/CompiledRuntimeVersion"
    }
  },
  "description" : ": Runtime Version Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "RuntimeVersionResponse": _runtime_version_response_model_schema
})

_scale_model_schema = json.loads(
    r"""{
  "title" : "Scale",
  "required" : [ "createdAt", "createdBy", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    },
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "The type of operation that was executed."
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user identity that was used to execute the job."
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp of when the job was created.",
      "format" : "date-time"
    },
    "processedAt" : {
      "title" : "processedAt",
      "type" : "string",
      "description" : "The timestamp of when the job has begun processing.",
      "format" : "date-time"
    },
    "finishedAt" : {
      "title" : "finishedAt",
      "description" : "The timestamp of when the job has finished processing."
    },
    "attemptsMade" : {
      "title" : "attemptsMade",
      "type" : "number",
      "description" : "The number of retries that were attempted."
    },
    "type" : {
      "$ref" : "#/components/schemas/Scale_type"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "request" : {
      "$ref" : "#/components/schemas/ScaleArgs"
    },
    "result" : {
      "$ref" : "#/components/schemas/ScaleResult"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobStatus"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Scale": _scale_model_schema})

_scale_1_model_schema = json.loads(
    r"""{
  "title" : "Scale",
  "required" : [ "createdAt", "createdBy", "id", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "The type of operation that was executed."
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user identity that was used to execute the job."
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp of when the job was created.",
      "format" : "date-time"
    },
    "processedAt" : {
      "title" : "processedAt",
      "type" : "string",
      "description" : "The timestamp of when the job has begun processing.",
      "format" : "date-time"
    },
    "finishedAt" : {
      "title" : "finishedAt",
      "description" : "The timestamp of when the job has finished processing."
    },
    "attemptsMade" : {
      "title" : "attemptsMade",
      "type" : "number",
      "description" : "The number of retries that were attempted."
    },
    "type" : {
      "$ref" : "#/components/schemas/Scale_type"
    },
    "id" : {
      "title" : "id",
      "type" : "string",
      "description" : "The id of the background job, or the constant `_unknown_`"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobAndFunctionHALLink"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Scale_1": _scale_1_model_schema})

_scale_args_model_schema = json.loads(
    r"""{
  "title" : "ScaleArgs",
  "required" : [ "endpoint", "namespace", "replicas", "revision", "runtimeName", "runtimeVersion" ],
  "type" : "object",
  "properties" : {
    "namespace" : {
      "title" : "namespace",
      "type" : "string",
      "description" : "The (openfaas) namespace for the target function."
    },
    "endpoint" : {
      "title" : "endpoint",
      "type" : "string",
      "description" : "The (openfaas) endpoint service name"
    },
    "runtimeName" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "revision" : {
      "title" : "revision",
      "type" : "string",
      "description" : "The revision hash of the current (draft) function revision"
    },
    "replicas" : {
      "title" : "replicas",
      "type" : "number",
      "description" : "Number of target replicas"
    }
  },
  "description" : "Input argument to an (openfaas) scale job for a function."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ScaleArgs": _scale_args_model_schema})

_scale_job_status_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "job", "operation", "request", "state", "type" ],
  "type" : "object",
  "properties" : {
    "operation" : {
      "type" : "string",
      "description" : "The type of operation that was executed."
    },
    "createdBy" : {
      "type" : "string",
      "description" : "The user identity that was used to execute the job."
    },
    "createdAt" : {
      "type" : "string",
      "description" : "The timestamp of when the job was created.",
      "format" : "date-time"
    },
    "processedAt" : {
      "type" : "string",
      "description" : "The timestamp of when the job has begun processing.",
      "format" : "date-time"
    },
    "finishedAt" : {
      "description" : "The timestamp of when the job has finished processing."
    },
    "attemptsMade" : {
      "type" : "number",
      "description" : "The number of retries that were attempted."
    },
    "type" : {
      "$ref" : "#/components/schemas/Scale_type"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "request" : {
      "$ref" : "#/components/schemas/ScaleArgs"
    },
    "result" : {
      "$ref" : "#/components/schemas/ScaleResult"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobStatus"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ScaleJobStatus": _scale_job_status_model_schema})

_scale_type_model_schema = json.loads(
    r"""{
  "title" : "Scale_type",
  "type" : "string",
  "description" : "The type of the background task.",
  "enum" : [ "scale" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Scale_type": _scale_type_model_schema})

_semantic_version_range_model_schema = json.loads(
    r"""{
  "description" : "A range of semantic versions. See https://devhints.io/semver",
  "anyOf" : [ {
    "type" : "string"
  }, {
    "$ref" : "#/components/schemas/SemanticVersion"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SemanticVersionRange": _semantic_version_range_model_schema})

_show_embedding_model_schema = json.loads(
    r"""{
  "type" : "string",
  "enum" : [ "embed", "none" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ShowEmbedding": _show_embedding_model_schema})

_show_inline_or_embedding_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/ShowEmbedding"
  }, {
    "$ref" : "#/components/schemas/ShowInlineOrEmbedding_anyOf"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ShowInlineOrEmbedding": _show_inline_or_embedding_model_schema
})

_show_inline_or_embedding_any_of_model_schema = json.loads(
    r"""{
  "title" : "ShowInlineOrEmbedding_anyOf",
  "type" : "string",
  "enum" : [ "inline" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ShowInlineOrEmbedding_anyOf": _show_inline_or_embedding_any_of_model_schema
})

_show_link_or_embedding_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/ShowEmbedding"
  }, {
    "$ref" : "#/components/schemas/ShowLinkOrEmbedding_anyOf"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ShowLinkOrEmbedding": _show_link_or_embedding_model_schema})

_show_link_or_embedding_any_of_model_schema = json.loads(
    r"""{
  "title" : "ShowLinkOrEmbedding_anyOf",
  "type" : "string",
  "enum" : [ "link" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "ShowLinkOrEmbedding_anyOf": _show_link_or_embedding_any_of_model_schema
})

_status_model_schema = json.loads(
    r"""{
  "title" : "Status",
  "type" : "string",
  "description" : "Status for a deployed function.",
  "enum" : [ "registered", "running", "pending", "deployed", "unhealthy", "failed", "undeploying", "undeployed" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Status": _status_model_schema})

_status_any_model_schema = json.loads(
    r"""{
  "title" : "StatusAny",
  "type" : "string",
  "description" : "Includes *all* statuses (including `undeployed`) as a filter",
  "enum" : [ "any" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"StatusAny": _status_any_model_schema})

_status_exclude_model_schema = json.loads(
    r"""{
  "title" : "StatusExclude",
  "pattern" : "^(registered|pending|deployed|unhealthy|failed|running|undeploying|undeployed)-$",
  "type" : "string",
  "description" : "Any status value with a `-` postfix appended, excludes that status as a filter.",
  "example" : "running-",
  "enum" : [ "registered-", "running-", "pending-", "deployed-", "unhealthy-", "failed-", "undeploying-", "undeployed-" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"StatusExclude": _status_exclude_model_schema})

_status_filter_model_schema = json.loads(
    r"""{
  "description" : "Inclusion or exclusion filter on the `status` property.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Status"
  }, {
    "$ref" : "#/components/schemas/StatusExclude"
  }, {
    "$ref" : "#/components/schemas/StatusAny"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"StatusFilter": _status_filter_model_schema})

_stream_closing_model_schema = json.loads(
    r"""{
  "title" : "Stream Closing",
  "required" : [ "data", "event" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/EventClose"
    },
    "data" : {
      "title" : "data",
      "type" : "string",
      "description" : "A text message describing the cause for closing the stream."
    }
  },
  "description" : "A message that notifies that the server will not send more events, and that the client should close."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Stream_Closing": _stream_closing_model_schema})

_stream_ready_model_schema = json.loads(
    r"""{
  "title" : "Stream Ready",
  "required" : [ "data", "event" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/EventAck"
    },
    "data" : {
      "title" : "data",
      "type" : "string",
      "description" : "A text message acknowledging what events will be forwarded."
    }
  },
  "description" : "A message that acknowledges that the server will sent job state changes."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Stream_Ready": _stream_ready_model_schema})

_tag_model_schema = json.loads(
    r"""{
  "title" : "Tag",
  "required" : [ "color", "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "$ref" : "#/components/schemas/TagReference"
    },
    "color" : {
      "title" : "color",
      "type" : "string",
      "description" : "Color associated with the tag in an UI."
    }
  },
  "description" : "One or more tags can be assigned to a function entity to facilitate grouping and searching."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Tag": _tag_model_schema})

_tag_or_tag_reference_model_schema = json.loads(
    r"""{
  "title" : "TagOrTagReference",
  "description" : "A reference to a tag, or tag object.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/TagReference"
  }, {
    "$ref" : "#/components/schemas/Tag"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TagOrTagReference": _tag_or_tag_reference_model_schema})

_tagging_scope_option_model_schema = json.loads(
    r"""{
  "type" : "string",
  "enum" : [ "any", "all" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TaggingScopeOption": _tagging_scope_option_model_schema})

_tags_filter_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "type" : "array",
    "items" : {
      "type" : "string"
    }
  }, {
    "type" : "string"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TagsFilter": _tags_filter_model_schema})

_timestamp_absolute_model_schema = json.loads(
    r"""{
  "title" : "TimestampAbsolute",
  "description" : "An absolute timestamp as an ISO8601 string",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/SO8601DateTime"
  }, {
    "$ref" : "#/components/schemas/SO8601Date"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TimestampAbsolute": _timestamp_absolute_model_schema})

_timestamp_age_model_schema = json.loads(
    r"""{
  "title" : "TimestampAge",
  "description" : "A timestamp expressed as a age relative to now",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/SO8601Period"
  }, {
    "$ref" : "#/components/schemas/DurationSpec"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TimestampAge": _timestamp_age_model_schema})

_timestamp_spec_model_schema = json.loads(
    r"""{
  "description" : "A timestamp specification.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/TimestampAge"
  }, {
    "$ref" : "#/components/schemas/TimestampAbsolute"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TimestampSpec": _timestamp_spec_model_schema})

_undeploy_model_schema = json.loads(
    r"""{
  "title" : "Undeploy",
  "required" : [ "createdAt", "createdBy", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    },
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "The type of operation that was executed."
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user identity that was used to execute the job."
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp of when the job was created.",
      "format" : "date-time"
    },
    "processedAt" : {
      "title" : "processedAt",
      "type" : "string",
      "description" : "The timestamp of when the job has begun processing.",
      "format" : "date-time"
    },
    "finishedAt" : {
      "title" : "finishedAt",
      "description" : "The timestamp of when the job has finished processing."
    },
    "attemptsMade" : {
      "title" : "attemptsMade",
      "type" : "number",
      "description" : "The number of retries that were attempted."
    },
    "type" : {
      "$ref" : "#/components/schemas/Undeploy_type"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "request" : {
      "$ref" : "#/components/schemas/UndeployArgs"
    },
    "result" : {
      "$ref" : "#/components/schemas/UndeployResult"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobStatus"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Undeploy": _undeploy_model_schema})

_undeploy_1_model_schema = json.loads(
    r"""{
  "title" : "Undeploy",
  "required" : [ "createdAt", "createdBy", "id", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "The type of operation that was executed."
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user identity that was used to execute the job."
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp of when the job was created.",
      "format" : "date-time"
    },
    "processedAt" : {
      "title" : "processedAt",
      "type" : "string",
      "description" : "The timestamp of when the job has begun processing.",
      "format" : "date-time"
    },
    "finishedAt" : {
      "title" : "finishedAt",
      "description" : "The timestamp of when the job has finished processing."
    },
    "attemptsMade" : {
      "title" : "attemptsMade",
      "type" : "number",
      "description" : "The number of retries that were attempted."
    },
    "type" : {
      "$ref" : "#/components/schemas/Undeploy_type"
    },
    "id" : {
      "title" : "id",
      "type" : "string",
      "description" : "The id of the background job, or the constant `_unknown_`"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobAndFunctionHALLink"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Undeploy_1": _undeploy_1_model_schema})

_undeploy_args_model_schema = json.loads(
    r"""{
  "title" : "UndeployArgs",
  "required" : [ "deleteEntity", "deleteImage", "endpoint", "imageName", "namespace", "resetEntity", "revision", "runtimeName", "runtimeVersion", "storageLocation" ],
  "type" : "object",
  "properties" : {
    "storageLocation" : {
      "title" : "storageLocation",
      "type" : "string",
      "description" : "Location of the function assets."
    },
    "imageName" : {
      "title" : "imageName",
      "type" : "string",
      "description" : "The container image name for the target function."
    },
    "namespace" : {
      "title" : "namespace",
      "type" : "string",
      "description" : "The (openfaas) namespace for the target function."
    },
    "endpoint" : {
      "title" : "endpoint",
      "type" : "string",
      "description" : "The (openfaas) endpoint service name"
    },
    "runtimeName" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "revision" : {
      "title" : "revision",
      "type" : "string",
      "description" : "The revision hash of the current (draft) function revision"
    },
    "deleteEntity" : {
      "title" : "deleteEntity",
      "type" : "boolean"
    },
    "resetEntity" : {
      "title" : "resetEntity",
      "type" : "boolean"
    },
    "deleteImage" : {
      "title" : "deleteImage",
      "type" : "boolean"
    }
  },
  "description" : "Input argument to an (openfaas) undeployment job for a function."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"UndeployArgs": _undeploy_args_model_schema})

_undeploy_job_status_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "job", "operation", "request", "state", "type" ],
  "type" : "object",
  "properties" : {
    "operation" : {
      "type" : "string",
      "description" : "The type of operation that was executed."
    },
    "createdBy" : {
      "type" : "string",
      "description" : "The user identity that was used to execute the job."
    },
    "createdAt" : {
      "type" : "string",
      "description" : "The timestamp of when the job was created.",
      "format" : "date-time"
    },
    "processedAt" : {
      "type" : "string",
      "description" : "The timestamp of when the job has begun processing.",
      "format" : "date-time"
    },
    "finishedAt" : {
      "description" : "The timestamp of when the job has finished processing."
    },
    "attemptsMade" : {
      "type" : "number",
      "description" : "The number of retries that were attempted."
    },
    "type" : {
      "$ref" : "#/components/schemas/Undeploy_type"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "request" : {
      "$ref" : "#/components/schemas/UndeployArgs"
    },
    "result" : {
      "$ref" : "#/components/schemas/UndeployResult"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobStatus"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"UndeployJobStatus": _undeploy_job_status_model_schema})

_undeploy_result_model_schema = json.loads(
    r"""{
  "title" : "UndeployResult",
  "required" : [ "assets", "deployment", "image", "registration" ],
  "type" : "object",
  "properties" : {
    "deployment" : {
      "title" : "deployment",
      "type" : "boolean"
    },
    "assets" : {
      "title" : "assets",
      "type" : "boolean"
    },
    "registration" : {
      "title" : "registration",
      "type" : "boolean"
    },
    "image" : {
      "title" : "image",
      "type" : "boolean"
    }
  },
  "description" : "The result data for a completed undeployment job."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"UndeployResult": _undeploy_result_model_schema})

_undeploy_submitted_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "message", "versions" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    },
    "versions" : {
      "type" : "array",
      "description" : "The versions for which undeployment and/or removal is initiated.",
      "items" : {
        "$ref" : "#/components/schemas/SemanticVersion"
      }
    }
  },
  "description" : "Undeployment Initiated"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "UndeploySubmittedResponseV2": _undeploy_submitted_response_v2_model_schema
})

_undeploy_type_model_schema = json.loads(
    r"""{
  "title" : "Undeploy_type",
  "type" : "string",
  "description" : "The type of the background task.",
  "enum" : [ "undeploy" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Undeploy_type": _undeploy_type_model_schema})

_undeployed_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "message", "versions" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "versions" : {
      "type" : "array",
      "description" : "The versions that were deprecated, undeployed and/or removed.",
      "items" : {
        "$ref" : "#/components/schemas/SemanticVersion"
      }
    }
  },
  "description" : "Undeployed"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"UndeployedResponseV2": _undeployed_response_v2_model_schema})

_update_metadata_request_v2_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "author" : {
      "type" : "string",
      "description" : "The author of the function."
    },
    "description" : {
      "type" : "string",
      "description" : "A description of the function"
    },
    "iconURL" : {
      "type" : "string",
      "description" : "An url to an icon that represents this function."
    },
    "category" : {
      "type" : "string",
      "description" : "A category for this function (Deprecated: use tags to categorise your functions)",
      "deprecated" : true
    },
    "tags" : {
      "type" : "array",
      "description" : "During update, a (reference to a) tag\n- that does not yet exist, is created (using default attributes if not specified)\n- that does exist is not updated (even if tag attributes like `color` differ)",
      "example" : [ "awaiting-review", {
        "name" : "demo",
        "color" : "#e639a4"
      } ],
      "deprecated" : false,
      "items" : {
        "$ref" : "#/components/schemas/TagOrTagReference"
      }
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "UpdateMetadataRequestV2": _update_metadata_request_v2_model_schema
})

_update_plug_metadata_request_v2_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "author" : {
      "type" : "string",
      "description" : "The author of the function."
    },
    "description" : {
      "type" : "string",
      "description" : "A description of the function"
    },
    "iconURL" : {
      "type" : "string",
      "description" : "An url to an icon that represents this function."
    },
    "category" : {
      "type" : "string",
      "description" : "A category for this function (Deprecated: use tags to categorise your functions)",
      "deprecated" : true
    },
    "documentationURL" : {
      "type" : "string",
      "description" : "External url that document this function."
    },
    "friendlyName" : {
      "type" : "string",
      "description" : "Display title for this function."
    },
    "tags" : {
      "type" : "array",
      "description" : "During update, a (reference to a) tag\n- that does not yet exist, is created (using default attributes if not specified)\n- that does exist is not updated (even if tag attributes like `color` differ)",
      "example" : [ "awaiting-review", {
        "name" : "demo",
        "color" : "#e639a4"
      } ],
      "deprecated" : false,
      "items" : {
        "$ref" : "#/components/schemas/TagOrTagReference"
      }
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "UpdatePlugMetadataRequestV2": _update_plug_metadata_request_v2_model_schema
})

_update_record_model_schema = json.loads(
    r"""{
  "title" : "UpdateRecord",
  "required" : [ "at", "by", "operation" ],
  "type" : "object",
  "properties" : {
    "comment" : {
      "title" : "comment",
      "type" : "string",
      "description" : "An optional user-specified comment corresponding to the operation."
    },
    "operation" : {
      "$ref" : "#/components/schemas/RequestOperation"
    },
    "jobs" : {
      "title" : "jobs",
      "type" : "array",
      "description" : "The job id's of the corresponding jobs, if applicable.",
      "items" : {
        "type" : "string"
      }
    },
    "at" : {
      "title" : "at",
      "type" : "string",
      "format" : "date-time"
    },
    "by" : {
      "title" : "by",
      "type" : "string",
      "description" : "The user that initiated this operation."
    }
  },
  "description" : "An update report corresponding to a modifying operation initiated by a user/administrator on the entity."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"UpdateRecord": _update_record_model_schema})

_update_tags_request_v2_model_schema = json.loads(
    r"""{
  "required" : [ "tags" ],
  "type" : "object",
  "properties" : {
    "tags" : {
      "type" : "array",
      "description" : "During update, a (reference to a) tag\n- that does not yet exist, is created (using default attributes if not specified)\n- that does exist is **not** updated (even if tag attributes like `color` differ)",
      "example" : [ "awaiting-review", {
        "name" : "demo",
        "color" : "#e639a4"
      } ],
      "items" : {
        "$ref" : "#/components/schemas/TagOrTagReference"
      }
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"UpdateTagsRequestV2": _update_tags_request_v2_model_schema})

_verify_model_schema = json.loads(
    r"""{
  "title" : "Verify",
  "required" : [ "createdAt", "createdBy", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    },
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "The type of operation that was executed."
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user identity that was used to execute the job."
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp of when the job was created.",
      "format" : "date-time"
    },
    "processedAt" : {
      "title" : "processedAt",
      "type" : "string",
      "description" : "The timestamp of when the job has begun processing.",
      "format" : "date-time"
    },
    "finishedAt" : {
      "title" : "finishedAt",
      "description" : "The timestamp of when the job has finished processing."
    },
    "attemptsMade" : {
      "title" : "attemptsMade",
      "type" : "number",
      "description" : "The number of retries that were attempted."
    },
    "type" : {
      "$ref" : "#/components/schemas/Verify_type"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "request" : {
      "$ref" : "#/components/schemas/VerifyArgs"
    },
    "result" : {
      "$ref" : "#/components/schemas/VerifyResult"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobStatus"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Verify": _verify_model_schema})

_verify_1_model_schema = json.loads(
    r"""{
  "title" : "Verify",
  "required" : [ "createdAt", "createdBy", "id", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "The type of operation that was executed."
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user identity that was used to execute the job."
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp of when the job was created.",
      "format" : "date-time"
    },
    "processedAt" : {
      "title" : "processedAt",
      "type" : "string",
      "description" : "The timestamp of when the job has begun processing.",
      "format" : "date-time"
    },
    "finishedAt" : {
      "title" : "finishedAt",
      "description" : "The timestamp of when the job has finished processing."
    },
    "attemptsMade" : {
      "title" : "attemptsMade",
      "type" : "number",
      "description" : "The number of retries that were attempted."
    },
    "type" : {
      "$ref" : "#/components/schemas/Verify_type"
    },
    "id" : {
      "title" : "id",
      "type" : "string",
      "description" : "The id of the background job, or the constant `_unknown_`"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobAndFunctionHALLink"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Verify_1": _verify_1_model_schema})

_verify_args_model_schema = json.loads(
    r"""{
  "title" : "VerifyArgs",
  "required" : [ "endpoint", "namespace", "revision", "runtimeName", "runtimeVersion" ],
  "type" : "object",
  "properties" : {
    "namespace" : {
      "title" : "namespace",
      "type" : "string",
      "description" : "The (openfaas) namespace for the target function."
    },
    "endpoint" : {
      "title" : "endpoint",
      "type" : "string",
      "description" : "The (openfaas) endpoint service name"
    },
    "runtimeName" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "revision" : {
      "title" : "revision",
      "type" : "string",
      "description" : "The revision hash of the current (draft) function revision"
    }
  },
  "description" : "Input arguments for an (openfaas) deployment verification job."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"VerifyArgs": _verify_args_model_schema})

_verify_job_status_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "job", "operation", "request", "state", "type" ],
  "type" : "object",
  "properties" : {
    "operation" : {
      "type" : "string",
      "description" : "The type of operation that was executed."
    },
    "createdBy" : {
      "type" : "string",
      "description" : "The user identity that was used to execute the job."
    },
    "createdAt" : {
      "type" : "string",
      "description" : "The timestamp of when the job was created.",
      "format" : "date-time"
    },
    "processedAt" : {
      "type" : "string",
      "description" : "The timestamp of when the job has begun processing.",
      "format" : "date-time"
    },
    "finishedAt" : {
      "description" : "The timestamp of when the job has finished processing."
    },
    "attemptsMade" : {
      "type" : "number",
      "description" : "The number of retries that were attempted."
    },
    "type" : {
      "$ref" : "#/components/schemas/Verify_type"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "request" : {
      "$ref" : "#/components/schemas/VerifyArgs"
    },
    "result" : {
      "$ref" : "#/components/schemas/VerifyResult"
    },
    "function" : {
      "$ref" : "#/components/schemas/FunctionRef"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobStatus"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"VerifyJobStatus": _verify_job_status_model_schema})

_verify_model_sync_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "entity", "message", "result" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "entity" : {
      "$ref" : "#/components/schemas/KfservingResponseV2"
    },
    "result" : {
      "$ref" : "#/components/schemas/VerifyResult"
    }
  },
  "description" : "Model Health Verified"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "VerifyModelSyncResponseV2": _verify_model_sync_response_v2_model_schema
})

_verify_plug_sync_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "entity", "message", "result" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "entity" : {
      "$ref" : "#/components/schemas/PlugResponseV2"
    },
    "result" : {
      "$ref" : "#/components/schemas/VerifyResult"
    }
  },
  "description" : "Plug Health Verified"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "VerifyPlugSyncResponseV2": _verify_plug_sync_response_v2_model_schema
})

_verify_result_model_schema = json.loads(
    r"""{
  "title" : "VerifyResult",
  "required" : [ "healthy" ],
  "type" : "object",
  "properties" : {
    "healthy" : {
      "title" : "healthy",
      "type" : "boolean",
      "description" : "If true, the deployment check succeeded."
    },
    "replicas" : {
      "title" : "replicas",
      "type" : "number",
      "description" : "The number of replicas this function was running at the time of the check."
    }
  },
  "description" : "The result data for a completed verification job."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"VerifyResult": _verify_result_model_schema})

_verify_type_model_schema = json.loads(
    r"""{
  "title" : "Verify_type",
  "type" : "string",
  "description" : "The type of the background task.",
  "enum" : [ "verify" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Verify_type": _verify_type_model_schema})

_verify_webscript_sync_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "entity", "message", "result" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "entity" : {
      "$ref" : "#/components/schemas/WebscriptResponseV2"
    },
    "result" : {
      "$ref" : "#/components/schemas/VerifyResult"
    }
  },
  "description" : "Webscript Health Verified"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "VerifyWebscriptSyncResponseV2": _verify_webscript_sync_response_v2_model_schema
})

_waiting_children_event_sse_model_schema = json.loads(
    r"""{
  "required" : [ "data", "event" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/WaitingChildrenEventSSE_event"
    },
    "data" : {
      "$ref" : "#/components/schemas/JobEventResponse_WaitingChildrenEventData_"
    }
  },
  "description" : "A message that notifies a state change in a background job."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "WaitingChildrenEventSSE": _waiting_children_event_sse_model_schema
})

_waiting_children_event_sse_event_model_schema = json.loads(
    r"""{
  "title" : "WaitingChildrenEventSSE_event",
  "type" : "string",
  "description" : "The job queue event that trigged this message",
  "enum" : [ "waiting-children" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "WaitingChildrenEventSSE_event": _waiting_children_event_sse_event_model_schema
})

_waiting_event_data_model_schema = json.loads(
    r"""{
  "title" : "WaitingEventData",
  "type" : "object",
  "properties" : {
    "prev" : {
      "$ref" : "#/components/schemas/QueueEvents"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"WaitingEventData": _waiting_event_data_model_schema})

_waiting_event_sse_model_schema = json.loads(
    r"""{
  "required" : [ "data", "event" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/WaitingEventSSE_event"
    },
    "data" : {
      "$ref" : "#/components/schemas/JobEventResponse_WaitingEventData_"
    }
  },
  "description" : "A message that notifies a state change in a background job."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"WaitingEventSSE": _waiting_event_sse_model_schema})

_waiting_event_sse_event_model_schema = json.loads(
    r"""{
  "title" : "WaitingEventSSE_event",
  "type" : "string",
  "description" : "The job queue event that trigged this message",
  "enum" : [ "waiting" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "WaitingEventSSE_event": _waiting_event_sse_event_model_schema
})

_webscript_model_schema = json.loads(
    r"""{
  "title" : "Webscript",
  "required" : [ "webscript" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/HALLinks"
    },
    "webscript" : {
      "$ref" : "#/components/schemas/HALLinks"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Webscript": _webscript_model_schema})

_webscript_1_model_schema = json.loads(
    r"""{
  "title" : "Webscript",
  "required" : [ "webscript" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/HALLinks"
    },
    "job" : {
      "$ref" : "#/components/schemas/JobHALLinks_job"
    },
    "webscript" : {
      "$ref" : "#/components/schemas/HALLinks"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Webscript_1": _webscript_1_model_schema})

_webscript_2_model_schema = json.loads(
    r"""{
  "title" : "Webscript",
  "required" : [ "webscript" ],
  "type" : "object",
  "properties" : {
    "job" : {
      "$ref" : "#/components/schemas/JobHALLinks_job"
    },
    "webscript" : {
      "$ref" : "#/components/schemas/HALLinks"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Webscript_2": _webscript_2_model_schema})

_webscript_manifest_model_schema = json.loads(
    r"""{
  "title" : "WebscriptManifest",
  "required" : [ "allowHmac", "metadata", "name", "private", "runtime", "version" ],
  "type" : "object",
  "properties" : {
    "deploy" : {
      "$ref" : "#/components/schemas/FunctionDeployOverridesType"
    },
    "name" : {
      "title" : "name",
      "type" : "string",
      "description" : "The logical name for the function."
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "metadata" : {
      "$ref" : "#/components/schemas/FunctionMeta"
    },
    "protected" : {
      "title" : "protected",
      "type" : "boolean",
      "description" : "Indicates whether the function's script and other assets should be protected."
    },
    "tags" : {
      "title" : "tags",
      "type" : "array",
      "description" : "Tags associated with this entity.",
      "items" : {
        "$ref" : "#/components/schemas/TagOrTagReference"
      }
    },
    "private" : {
      "title" : "private",
      "type" : "boolean",
      "description" : "If <code>true</code> this webscript will require authentication."
    },
    "allowHmac" : {
      "title" : "allowHmac",
      "type" : "boolean",
      "description" : "If <code>true</code> this webscript will support authentication with a <em>HMAC</em> key, available as the <code>secret</code> attribute of the deployed webscript entity."
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"WebscriptManifest": _webscript_manifest_model_schema})

_webscript_manifest_patch_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "private" : {
      "type" : "boolean",
      "description" : "If <code>true</code> this webscript will require authentication."
    },
    "allowHmac" : {
      "type" : "boolean",
      "description" : "If <code>true</code> this webscript will support authentication with a <em>HMAC</em> key, available as the <code>secret</code> attribute of the deployed webscript entity."
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "metadata" : {
      "$ref" : "#/components/schemas/FunctionMeta"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "deploy" : {
      "$ref" : "#/components/schemas/FunctionDeployOverridesType"
    }
  },
  "additionalProperties" : false,
  "description" : "Patch attributes to merge into an existing webscript manifest."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "WebscriptManifestPatch": _webscript_manifest_patch_model_schema
})

_webscript_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "deprecated", "draft", "runtime", "status", "updatedAt", "updatedBy", "webscript" ],
  "type" : "object",
  "properties" : {
    "createdBy" : {
      "type" : "string",
      "description" : "The user that created this entity."
    },
    "createdAt" : {
      "type" : "string",
      "description" : "The timestamp at which this entity was created.",
      "format" : "date-time"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "The user that last updated this entity."
    },
    "updatedAt" : {
      "type" : "string",
      "description" : "The timestamp at which this entity was last updated.",
      "format" : "date-time"
    },
    "updates" : {
      "type" : "array",
      "description" : "The audit logs corresponding to the latest modifying operations on this entity. Omitted in listing operations.",
      "items" : {
        "$ref" : "#/components/schemas/UpdateRecord"
      }
    },
    "status" : {
      "$ref" : "#/components/schemas/Status"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/RuntimeAttributes"
    },
    "deprecated" : {
      "type" : "boolean",
      "description" : "If <code>true</code> this function is deprecated and removed from regular listings."
    },
    "draft" : {
      "type" : "boolean",
      "description" : "If <code>true</code> this function is a draft function and it's assets are still mutable."
    },
    "revision" : {
      "type" : "string",
      "description" : "The revision of the function. This will be <code>undefined</code> when the plug is not a draft."
    },
    "webscript" : {
      "$ref" : "#/components/schemas/WebscriptManifest"
    },
    "secret" : {
      "type" : "string",
      "description" : "The secret for this webscript deployment. This is <code>null</code> when <code>allowHmac=false</code> in the webscript specificaton."
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"WebscriptResponseV2": _webscript_response_v2_model_schema})

_webscript_response_with_invoke_link_v2_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "deprecated", "draft", "runtime", "status", "updatedAt", "updatedBy", "webscript" ],
  "type" : "object",
  "properties" : {
    "createdBy" : {
      "type" : "string",
      "description" : "The user that created this entity."
    },
    "createdAt" : {
      "type" : "string",
      "description" : "The timestamp at which this entity was created.",
      "format" : "date-time"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "The user that last updated this entity."
    },
    "updatedAt" : {
      "type" : "string",
      "description" : "The timestamp at which this entity was last updated.",
      "format" : "date-time"
    },
    "updates" : {
      "type" : "array",
      "description" : "The audit logs corresponding to the latest modifying operations on this entity. Omitted in listing operations.",
      "items" : {
        "$ref" : "#/components/schemas/UpdateRecord"
      }
    },
    "status" : {
      "$ref" : "#/components/schemas/Status"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/RuntimeAttributes"
    },
    "deprecated" : {
      "type" : "boolean",
      "description" : "If <code>true</code> this function is deprecated and removed from regular listings."
    },
    "draft" : {
      "type" : "boolean",
      "description" : "If <code>true</code> this function is a draft function and it's assets are still mutable."
    },
    "revision" : {
      "type" : "string",
      "description" : "The revision of the function. This will be <code>undefined</code> when the plug is not a draft."
    },
    "webscript" : {
      "$ref" : "#/components/schemas/WebscriptManifest"
    },
    "secret" : {
      "type" : "string",
      "description" : "The secret for this webscript deployment. This is <code>null</code> when <code>allowHmac=false</code> in the webscript specificaton."
    },
    "_links" : {
      "$ref" : "#/components/schemas/InvokeHALLink"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "WebscriptResponseWithInvokeLinkV2": _webscript_response_with_invoke_link_v2_model_schema
})

_webscript_versions_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "count", "entities" ],
  "type" : "object",
  "properties" : {
    "_embedded" : {
      "$ref" : "#/components/schemas/GetPlugResponseV2__embedded"
    },
    "limit" : {
      "type" : "number",
      "description" : "The page size used for this query result."
    },
    "count" : {
      "type" : "number",
      "description" : "The total count of matching items, from which this result is one page."
    },
    "page" : {
      "type" : "number",
      "description" : "The page number of a paged query result."
    },
    "entities" : {
      "type" : "array",
      "description" : "The specification and deployment status of the queried functions",
      "items" : {
        "$ref" : "#/components/schemas/WebscriptResponseWithInvokeLinkV2"
      }
    }
  },
  "description" : "Webscript Versions Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "WebscriptVersionsResponseV2": _webscript_versions_response_v2_model_schema
})
