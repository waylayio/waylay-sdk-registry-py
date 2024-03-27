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

_alt_version_hal_link_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "draft" : {
      "$ref" : "#/components/schemas/GetPlugResponseV2__links_draft"
    },
    "published" : {
      "$ref" : "#/components/schemas/GetPlugResponseV2__links_published"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AltVersionHALLink": _alt_version_hal_link_model_schema})

_any_function_response_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/PlugResponseV2"
  }, {
    "$ref" : "#/components/schemas/KfservingResponseV2"
  }, {
    "$ref" : "#/components/schemas/WebscriptResponseV2"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AnyFunctionResponse": _any_function_response_model_schema})

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

_asset_path_params_v2_model_schema = json.loads(
    r"""{
  "required" : [ "*" ],
  "type" : "object",
  "properties" : {
    "*" : {
      "type" : "string",
      "description" : "Full path or path prefix of the asset within the archive"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AssetPathParamsV2": _asset_path_params_v2_model_schema})

_asset_role_model_schema = json.loads(
    r"""{
  "title" : "AssetRole",
  "type" : "string",
  "description" : "Classification of assets with regard to their role.",
  "enum" : [ "manifest", "project", "main", "lib", "script", "other" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AssetRole": _asset_role_model_schema})

_asset_summary_model_schema = json.loads(
    r"""{
  "required" : [ "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "description" : "File name"
    },
    "title" : {
      "type" : "string"
    },
    "description" : {
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
MODEL_DEFINITIONS.update({"AssetSummary": _asset_summary_model_schema})

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
      "$ref" : "#/components/schemas/HALLink"
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

_async_deploy_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "deprecatePrevious" : {
      "$ref" : "#/components/schemas/DeprecatePreviousPolicy"
    },
    "dryRun" : {
      "type" : "boolean",
      "description" : "If set to <code>true</code>, validates the deployment conditions, but does not change anything."
    },
    "async" : {
      "type" : "boolean",
      "description" : "Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs.",
      "default" : true
    },
    "scaleToZero" : {
      "type" : "boolean",
      "description" : "If set to <code>true</code>, after successful deployment, the deployed function will be scaled to zero. Saves computing resources when the function is not to be used immediately.",
      "default" : false
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AsyncDeployQuery": _async_deploy_query_model_schema})

_async_deploy_query_v1_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "scaleToZero" : {
      "type" : "boolean",
      "description" : "If set to <code>true</code>, after successful deployment, the deployed function will be scaled to zero. Saves computing resources when the function is not to be used immediately.",
      "default" : false
    },
    "async" : {
      "type" : "boolean",
      "description" : "Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs.",
      "default" : true
    },
    "dryRun" : {
      "type" : "boolean",
      "description" : "If set to <code>true</code>, validates the deployment conditions, but does not change anything."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AsyncDeployQueryV1": _async_deploy_query_v1_model_schema})

_async_query_default_false_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "async" : {
      "type" : "boolean",
      "description" : "If this is set to <code>true</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. Otherwise, the request will block until the job actions are completed, or a timeout occurs.",
      "default" : false
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "AsyncQueryDefaultFalse": _async_query_default_false_model_schema
})

_async_query_default_true_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "async" : {
      "type" : "boolean",
      "description" : "Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs.",
      "default" : true
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "AsyncQueryDefaultTrue": _async_query_default_true_model_schema
})

_async_verify_query_model_schema = json.loads(
    r"""{
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
    "scaleToZero" : {
      "type" : "boolean",
      "description" : "Indicates whether the function needs to be scaled down after successful verification. If not set, the function is scaled to zero only if it was not active before this command."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"AsyncVerifyQuery": _async_verify_query_model_schema})

_batch_model_schema = json.loads(
    r"""{
  "title" : "Batch",
  "required" : [ "_links", "createdAt", "createdBy", "id", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/BatchJobStatus_type"
    },
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "The operation name for the background task."
    },
    "id" : {
      "title" : "id",
      "type" : "string",
      "description" : "The id of the background job, or the constant `_unknown_`"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The creation time of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user that initiated this job"
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
    "createdAt" : {
      "type" : "string",
      "description" : "The timestamp of creation of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "The user that created this job"
    },
    "operation" : {
      "type" : "string",
      "description" : "Request operation"
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
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp of creation of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user that created this job"
    },
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "Request operation"
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
  "required" : [ "_links", "createdAt", "createdBy", "id", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/Build_type"
    },
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "The operation name for the background task."
    },
    "id" : {
      "title" : "id",
      "type" : "string",
      "description" : "The id of the background job, or the constant `_unknown_`"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The creation time of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user that initiated this job"
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
  "required" : [ "args", "imageName", "runtimeName", "runtimeVersion", "storageLocation" ],
  "type" : "object",
  "properties" : {
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
    "storageLocation" : {
      "title" : "storageLocation",
      "type" : "string",
      "description" : "Location of the function assets."
    },
    "imageName" : {
      "title" : "imageName",
      "type" : "string",
      "description" : "Provided (or defaulted) image name to publish the function image."
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
    "createdAt" : {
      "type" : "string",
      "description" : "The timestamp of creation of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "The user that created this job"
    },
    "operation" : {
      "type" : "string",
      "description" : "Request operation"
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
      "title" : "name",
      "type" : "string"
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
  "required" : [ "returnValue" ],
  "type" : "object",
  "properties" : {
    "prev" : {
      "$ref" : "#/components/schemas/QueueEvents"
    },
    "returnValue" : {
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

_content_query_v2_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "ls" : {
      "type" : "boolean",
      "description" : "If set to `true`, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime.",
      "default" : false
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ContentQueryV2": _content_query_v2_model_schema})

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

_create_function_query_v2_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "deprecatePrevious" : {
      "$ref" : "#/components/schemas/DeprecatePreviousPolicy"
    },
    "dryRun" : {
      "type" : "boolean",
      "description" : "If set to <code>true</code>, validates the deployment conditions, but does not change anything."
    },
    "async" : {
      "type" : "boolean",
      "description" : "Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs.",
      "default" : true
    },
    "scaleToZero" : {
      "type" : "boolean",
      "description" : "If set to <code>true</code>, after successful deployment, the deployed function will be scaled to zero. Saves computing resources when the function is not to be used immediately.",
      "default" : false
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "name" : {
      "type" : "string",
      "description" : "If set, the value will be used as the function name instead of the one specified in the manifest."
    },
    "draft" : {
      "type" : "boolean",
      "description" : "If set, the created function will be a draft function and its assets are still mutable. A build and deploy is initiated only in the case when all necessary assets are present and valid.",
      "default" : false
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "CreateFunctionQueryV2": _create_function_query_v2_model_schema
})

_create_kf_serving_async_response_model_schema = json.loads(
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
      "$ref" : "#/components/schemas/KFServingManifest"
    }
  },
  "description" : "Model Deployment Initiated"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "CreateKFServingAsyncResponse": _create_kf_serving_async_response_model_schema
})

_create_plug_async_response_model_schema = json.loads(
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
      "$ref" : "#/components/schemas/PlugManifest"
    }
  },
  "description" : "Successful Response"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "CreatePlugAsyncResponse": _create_plug_async_response_model_schema
})

_create_webscript_async_response_model_schema = json.loads(
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
      "$ref" : "#/components/schemas/WebscriptManifest"
    }
  },
  "description" : "Successful Response"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "CreateWebscriptAsyncResponse": _create_webscript_async_response_model_schema
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
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp of creation of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user that created this job"
    },
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "Request operation"
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
  "required" : [ "_links", "createdAt", "createdBy", "id", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/Deploy_type"
    },
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "The operation name for the background task."
    },
    "id" : {
      "title" : "id",
      "type" : "string",
      "description" : "The id of the background job, or the constant `_unknown_`"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The creation time of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user that initiated this job"
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
  "required" : [ "deploySpecOverrides", "endpoint", "imageName", "namespace", "runtimeName", "runtimeVersion" ],
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
    "envProcess" : {
      "title" : "envProcess",
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

_deploy_attributes_filter_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "endpoint" : {
      "type" : "string",
      "description" : "Filter on the openfaas endpoint. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "imageName" : {
      "type" : "string",
      "description" : "Filter on the container image name. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "storageLocation" : {
      "type" : "string",
      "description" : "Filter on the storageLocation. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "DeployAttributesFilter": _deploy_attributes_filter_model_schema
})

_deploy_job_status_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "job", "operation", "request", "state", "type" ],
  "type" : "object",
  "properties" : {
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
    "createdAt" : {
      "type" : "string",
      "description" : "The timestamp of creation of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "The user that created this job"
    },
    "operation" : {
      "type" : "string",
      "description" : "Request operation"
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
    "envProcess" : {
      "title" : "envProcess",
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
  "title" : "DeprecatePreviousPolicy",
  "type" : "string",
  "enum" : [ "none", "all", "patch", "minor" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "DeprecatePreviousPolicy": _deprecate_previous_policy_model_schema
})

_deprecate_previous_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "deprecatePrevious" : {
      "$ref" : "#/components/schemas/DeprecatePreviousPolicy"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "DeprecatePreviousQuery": _deprecate_previous_query_model_schema
})

_deprecated_draft_filter_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "deprecated" : {
      "type" : "boolean",
      "description" : "Filter on the deprecation status of the function."
    },
    "draft" : {
      "type" : "boolean",
      "description" : "Filter on the draft status of the function."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "DeprecatedDraftFilter": _deprecated_draft_filter_model_schema
})

_documentation_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "description" : {
      "type" : "string"
    },
    "states" : {
      "type" : "array",
      "description" : "Documentation of the plug states.",
      "items" : {
        "$ref" : "#/components/schemas/DocumentationProperty"
      }
    },
    "input" : {
      "type" : "array",
      "description" : "Documentation of the plug input parameters.",
      "items" : {
        "$ref" : "#/components/schemas/DocumentationProperty"
      }
    },
    "output" : {
      "type" : "array",
      "description" : "Documentation of the plug response parameters.",
      "items" : {
        "$ref" : "#/components/schemas/DocumentationProperty"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Documentation": _documentation_model_schema})

_documentation_property_model_schema = json.loads(
    r"""{
  "required" : [ "description", "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "description" : "Name of the documented property."
    },
    "description" : {
      "type" : "string",
      "description" : "Documentation of the property."
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "DocumentationProperty": _documentation_property_model_schema
})

_dry_run_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "dryRun" : {
      "type" : "boolean",
      "description" : "If set to <code>true</code>, validates the deployment conditions, but does not change anything."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"DryRunQuery": _dry_run_query_model_schema})

_entity_response_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "metadata", "name", "runtime", "status", "updatedAt", "updatedBy", "version" ],
  "type" : "object",
  "properties" : {
    "deploy" : {
      "$ref" : "#/components/schemas/FunctionDeployOverridesType"
    },
    "name" : {
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
    "status" : {
      "$ref" : "#/components/schemas/Status"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    },
    "_links" : {
      "type" : "array",
      "description" : "Links to related entities.",
      "items" : {
        "$ref" : "#/components/schemas/JobHALLinks"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"EntityResponse": _entity_response_model_schema})

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

_error_response_model_schema = json.loads(
    r"""{
  "required" : [ "error" ],
  "type" : "object",
  "properties" : {
    "error" : {
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ErrorResponse": _error_response_model_schema})

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

_event_sse_model_schema = json.loads(
    r"""{
  "description" : "SSE stream events without closing protocol",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/Stream_Ready"
  }, {
    "$ref" : "#/components/schemas/JobEventSSE"
  }, {
    "$ref" : "#/components/schemas/KeepAliveEventSSE"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"EventSSE": _event_sse_model_schema})

_event_type_sse_model_schema = json.loads(
    r"""{
  "anyOf" : [ {
    "$ref" : "#/components/schemas/SupportedEvents"
  }, {
    "$ref" : "#/components/schemas/EventAck"
  }, {
    "$ref" : "#/components/schemas/EventClose"
  }, {
    "$ref" : "#/components/schemas/EventKeepAlive"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"EventTypeSSE": _event_type_sse_model_schema})

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

_force_delete_query_v1_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "async" : {
      "type" : "boolean",
      "description" : "If this is set to <code>true</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. Otherwise, the request will block until the job actions are completed, or a timeout occurs.",
      "default" : false
    },
    "force" : {
      "type" : "boolean",
      "description" : "If <code>true</code>, the plug version(s) will be undeployed and removed. Otherwise, the plug version(s) will only be <code>deprecated</code>, i.e removed from regular listings."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"ForceDeleteQueryV1": _force_delete_query_v1_model_schema})

_function_delete_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "force" : {
      "type" : "boolean",
      "description" : "If <code>true</code>, the function version will be immediately undeployed and removed.\n\nOtherwise, the removal will be delayed to allow current invocations to end. During that period, the function is marked _deprecated_."
    },
    "undeploy" : {
      "type" : "boolean",
      "description" : "If `true`, the `DELETE` operation\n* undeploys the (openfaas) function: it becomes no longer available for invocation.\n* does NOT remove the function from registry: it stays in an `undeployed` status.  All assets and definitions are retained, so the version can be restored later with a  _rebuild_ action.\n\nIf `false`, the `DELETE` operation\n* _only_ marks the plug function as _deprecated_, the function remains active but is removed from the default listings.   This also applies to _draft_ versions.\n\nThis parameter is incompatible with `force=true`.\n\nIf not set the default behaviour applies:\n* _draft_ versions are _undeployed_ and _removed_ from registry.\n* non-_draft_ versions are marked _deprecated_ only."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"FunctionDeleteQuery": _function_delete_query_model_schema})

_function_deploy_overrides_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "deploy" : {
      "$ref" : "#/components/schemas/FunctionDeployOverridesType"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "FunctionDeployOverrides": _function_deploy_overrides_model_schema
})

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
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "FunctionDeployOverridesType": _function_deploy_overrides_type_model_schema
})

_function_entity_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "description" : "Filter on the name of the function. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "Filter on the archive format of the function.",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    },
    "runtime" : {
      "type" : "array",
      "description" : "Filter on the runtime of the function.",
      "items" : {
        "$ref" : "#/components/schemas/Runtime"
      }
    }
  },
  "additionalProperties" : false,
  "description" : "Filter on function attributes that do not change across function versions."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"FunctionEntityQuery": _function_entity_query_model_schema})

_function_job_args_model_schema = json.loads(
    r"""{
  "required" : [ "runtimeName", "runtimeVersion" ],
  "type" : "object",
  "properties" : {
    "runtimeName" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "revision" : {
      "type" : "string",
      "description" : "The revision hash of the current (draft) function revision"
    }
  },
  "description" : "Job arguments shared by all function jobs"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"FunctionJobArgs": _function_job_args_model_schema})

_function_manifest_model_schema = json.loads(
    r"""{
  "required" : [ "metadata", "name", "runtime", "version" ],
  "type" : "object",
  "properties" : {
    "deploy" : {
      "$ref" : "#/components/schemas/FunctionDeployOverridesType"
    },
    "name" : {
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
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"FunctionManifest": _function_manifest_model_schema})

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

_function_name_version_model_schema = json.loads(
    r"""{
  "required" : [ "name", "version" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "description" : "The logical name for the function."
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"FunctionNameVersion": _function_name_version_model_schema})

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

_function_spec_model_schema = json.loads(
    r"""{
  "required" : [ "name", "runtime", "version" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "description" : "The logical name for the function."
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "runtime" : {
      "$ref" : "#/components/schemas/Runtime"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"FunctionSpec": _function_spec_model_schema})

_function_type_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Type of functions supported by the registry service.",
  "enum" : [ "plugs", "webscripts", "kfserving" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"FunctionType": _function_type_model_schema})

_function_version_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "version" : {
      "type" : "string",
      "description" : "Filter on the version of the function (case-sensitive, supports wildcards)."
    },
    "status" : {
      "type" : "array",
      "description" : "Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions.",
      "items" : {
        "$ref" : "#/components/schemas/StatusFilter"
      }
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "createdBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "createdAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    }
  },
  "additionalProperties" : false,
  "description" : "Filter on function attributes that can change across function versions. When these query parameters are used, the query is considered a _function version_ listing and no HAL links to latest (_draft_, _published_) versions are included."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"FunctionVersionQuery": _function_version_query_model_schema})

_get_content_params_v2_model_schema = json.loads(
    r"""{
  "required" : [ "*", "name", "version" ],
  "type" : "object",
  "properties" : {
    "*" : {
      "type" : "string",
      "description" : "Full path or path prefix of the asset within the archive"
    },
    "name" : {
      "type" : "string",
      "description" : "The name of the function."
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"GetContentParamsV2": _get_content_params_v2_model_schema})

_get_invokable_webscript_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "includeDraft" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**."
    },
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**."
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "status" : {
      "type" : "array",
      "description" : "If set, filters on the `status` of the webscript.",
      "items" : {
        "$ref" : "#/components/schemas/StatusFilter"
      },
      "default" : [ "running", "deployed", "unhealthy" ]
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "GetInvokableWebscriptQuery": _get_invokable_webscript_query_model_schema
})

_get_model_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "entity" ],
  "type" : "object",
  "properties" : {
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
    "entity" : {
      "$ref" : "#/components/schemas/PlugResponseV2"
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

_get_plug_response_v2__links_model_schema = json.loads(
    r"""{
  "title" : "GetPlugResponseV2__links",
  "type" : "object",
  "properties" : {
    "draft" : {
      "$ref" : "#/components/schemas/GetPlugResponseV2__links_draft"
    },
    "published" : {
      "$ref" : "#/components/schemas/GetPlugResponseV2__links_published"
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

_get_plug_response_v2__links_draft_model_schema = json.loads(
    r"""{
  "title" : "GetPlugResponseV2__links_draft",
  "required" : [ "deprecated", "draft", "href", "version" ],
  "type" : "object",
  "properties" : {
    "draft" : {
      "type" : "boolean"
    },
    "href" : {
      "type" : "string"
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
    "GetPlugResponseV2__links_draft": _get_plug_response_v2__links_draft_model_schema
})

_get_plug_response_v2__links_published_model_schema = json.loads(
    r"""{
  "title" : "GetPlugResponseV2__links_published",
  "required" : [ "deprecated", "draft", "href", "version" ],
  "type" : "object",
  "properties" : {
    "draft" : {
      "type" : "boolean"
    },
    "href" : {
      "type" : "string"
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
    "GetPlugResponseV2__links_published": _get_plug_response_v2__links_published_model_schema
})

_get_runtime_by_name_and_version_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "If set to `true`, deprecated runtimes will be included in the query.",
      "default" : true
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "GetRuntimeByNameAndVersionQuery": _get_runtime_by_name_and_version_query_model_schema
})

_get_runtime_by_name_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "If set to `true`, deprecated runtimes will be included in the query.",
      "default" : false
    },
    "functionType" : {
      "type" : "array",
      "description" : "If set, filters on the <code>functionType</code> of a runtime. Uses an exact match.",
      "example" : "plugs",
      "items" : {
        "$ref" : "#/components/schemas/FunctionType"
      }
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "If set, filters on the <code>archiveFormat</code> of a runtime. Uses an exact match.",
      "example" : "node",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "GetRuntimeByNameQuery": _get_runtime_by_name_query_model_schema
})

_get_runtime_example_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "ls" : {
      "type" : "boolean",
      "description" : "If set to `true`, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime.",
      "default" : false
    },
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "If set to `true`, deprecated runtimes will be included in the query.",
      "default" : true
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "GetRuntimeExampleQuery": _get_runtime_example_query_model_schema
})

_get_runtime_versions_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "latest" : {
      "$ref" : "#/components/schemas/LatestVersionLevel"
    },
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "If set to `true`, deprecated runtimes will be included in the query.",
      "default" : false
    },
    "functionType" : {
      "type" : "array",
      "description" : "If set, filters on the <code>functionType</code> of a runtime. Uses an exact match.",
      "example" : "plugs",
      "items" : {
        "$ref" : "#/components/schemas/FunctionType"
      }
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "If set, filters on the <code>archiveFormat</code> of a runtime. Uses an exact match.",
      "example" : "node",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "GetRuntimeVersionsQuery": _get_runtime_versions_query_model_schema
})

_get_webscript_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "entity" ],
  "type" : "object",
  "properties" : {
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
    "invoke" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "jobs" : {
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
  "title" : "HALLink",
  "required" : [ "href" ],
  "type" : "object",
  "properties" : {
    "href" : {
      "title" : "href",
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"HALLink": _hal_link_model_schema})

_invokable_webscript_response_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "entity" ],
  "type" : "object",
  "properties" : {
    "entity" : {
      "$ref" : "#/components/schemas/InvokableWebscriptResponse_entity"
    },
    "_links" : {
      "$ref" : "#/components/schemas/InvokeInternalHALLink"
    }
  },
  "description" : "Webscript Found"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "InvokableWebscriptResponse": _invokable_webscript_response_model_schema
})

_invokable_webscript_response_entity_model_schema = json.loads(
    r"""{
  "title" : "InvokableWebscriptResponse_entity",
  "required" : [ "draft", "status", "webscript" ],
  "type" : "object",
  "properties" : {
    "status" : {
      "$ref" : "#/components/schemas/Status"
    },
    "draft" : {
      "title" : "draft",
      "type" : "boolean"
    },
    "webscript" : {
      "$ref" : "#/components/schemas/InvokableWebscriptResponse_entity_webscript"
    },
    "secret" : {
      "title" : "secret",
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "InvokableWebscriptResponse_entity": _invokable_webscript_response_entity_model_schema
})

_invokable_webscript_response_entity_webscript_model_schema = json.loads(
    r"""{
  "title" : "InvokableWebscriptResponse_entity_webscript",
  "required" : [ "allowHmac", "name", "private", "version" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "type" : "string"
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "private" : {
      "title" : "private",
      "type" : "boolean"
    },
    "allowHmac" : {
      "title" : "allowHmac",
      "type" : "boolean"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "InvokableWebscriptResponse_entity_webscript": _invokable_webscript_response_entity_webscript_model_schema
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

_invoke_internal_hal_link_model_schema = json.loads(
    r"""{
  "title" : "InvokeInternalHALLink",
  "type" : "object",
  "properties" : {
    "invoke-internal" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "InvokeInternalHALLink": _invoke_internal_hal_link_model_schema
})

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
      "type" : "string",
      "description" : "The new configuration value that causes the change."
    },
    "oldValue" : {
      "title" : "oldValue",
      "type" : "string",
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

_job_event_payload_active_event_data__model_schema = json.loads(
    r"""{
  "required" : [ "data", "job", "timestamp" ],
  "type" : "object",
  "properties" : {
    "job" : {
      "$ref" : "#/components/schemas/JobReference"
    },
    "data" : {
      "$ref" : "#/components/schemas/ActiveEventData"
    },
    "timestamp" : {
      "type" : "string",
      "description" : "Timestamp of the event",
      "format" : "date-time"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobEventPayload_ActiveEventData_": _job_event_payload_active_event_data__model_schema
})

_job_event_payload_completed_event_data__model_schema = json.loads(
    r"""{
  "required" : [ "data", "job", "timestamp" ],
  "type" : "object",
  "properties" : {
    "job" : {
      "$ref" : "#/components/schemas/JobReference"
    },
    "data" : {
      "$ref" : "#/components/schemas/CompletedEventData"
    },
    "timestamp" : {
      "type" : "string",
      "description" : "Timestamp of the event",
      "format" : "date-time"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobEventPayload_CompletedEventData_": _job_event_payload_completed_event_data__model_schema
})

_job_event_payload_delayed_event_data__model_schema = json.loads(
    r"""{
  "required" : [ "data", "job", "timestamp" ],
  "type" : "object",
  "properties" : {
    "job" : {
      "$ref" : "#/components/schemas/JobReference"
    },
    "data" : {
      "$ref" : "#/components/schemas/DelayedEventData"
    },
    "timestamp" : {
      "type" : "string",
      "description" : "Timestamp of the event",
      "format" : "date-time"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobEventPayload_DelayedEventData_": _job_event_payload_delayed_event_data__model_schema
})

_job_event_payload_failed_event_data__model_schema = json.loads(
    r"""{
  "required" : [ "data", "job", "timestamp" ],
  "type" : "object",
  "properties" : {
    "job" : {
      "$ref" : "#/components/schemas/JobReference"
    },
    "data" : {
      "$ref" : "#/components/schemas/FailedEventData"
    },
    "timestamp" : {
      "type" : "string",
      "description" : "Timestamp of the event",
      "format" : "date-time"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobEventPayload_FailedEventData_": _job_event_payload_failed_event_data__model_schema
})

_job_event_payload_waiting_children_event_data__model_schema = json.loads(
    r"""{
  "required" : [ "data", "job", "timestamp" ],
  "type" : "object",
  "properties" : {
    "job" : {
      "$ref" : "#/components/schemas/JobReference"
    },
    "data" : {
      "$ref" : "#/components/schemas/WaitingChildrenEventData"
    },
    "timestamp" : {
      "type" : "string",
      "description" : "Timestamp of the event",
      "format" : "date-time"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobEventPayload_WaitingChildrenEventData_": _job_event_payload_waiting_children_event_data__model_schema
})

_job_event_payload_waiting_event_data__model_schema = json.loads(
    r"""{
  "required" : [ "data", "job", "timestamp" ],
  "type" : "object",
  "properties" : {
    "job" : {
      "$ref" : "#/components/schemas/JobReference"
    },
    "data" : {
      "$ref" : "#/components/schemas/WaitingEventData"
    },
    "timestamp" : {
      "type" : "string",
      "description" : "Timestamp of the event",
      "format" : "date-time"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobEventPayload_WaitingEventData_": _job_event_payload_waiting_event_data__model_schema
})

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

_job_events_filter_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/JobType"
    },
    "id" : {
      "type" : "string",
      "description" : "The id of the job."
    },
    "children" : {
      "type" : "boolean",
      "description" : "If set to <code>true</code>, the event stream will include events of the job's dependants. E.g., when subscribing to a verify job with `children=true`, you will also receive the events of the underlying build and deploy jobs. Defaults to <code>false</code>."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "JobEventsFilterQuery": _job_events_filter_query_model_schema
})

_job_events_hal_link_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  },
  "description" : "HAL links to related actions."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobEventsHALLink": _job_events_hal_link_model_schema})

_job_hal_links_model_schema = json.loads(
    r"""{
  "title" : "JobHALLinks",
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "job" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  },
  "description" : "HAL links to related actions."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobHALLinks": _job_hal_links_model_schema})

_job_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    },
    "type" : {
      "type" : "array",
      "description" : "Filter on job type",
      "items" : {
        "$ref" : "#/components/schemas/JobTypeSchema"
      }
    },
    "state" : {
      "type" : "array",
      "description" : "Filter on job state",
      "items" : {
        "$ref" : "#/components/schemas/JobStateResult"
      }
    },
    "functionType" : {
      "type" : "array",
      "description" : "Filter on function type",
      "items" : {
        "$ref" : "#/components/schemas/FunctionType"
      }
    },
    "createdBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "createdAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobQuery": _job_query_model_schema})

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

_job_reference_params_model_schema = json.loads(
    r"""{
  "required" : [ "id", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/JobType"
    },
    "id" : {
      "type" : "string"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobReferenceParams": _job_reference_params_model_schema})

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

_job_state_result_model_schema = json.loads(
    r"""{
  "title" : "JobStateResult",
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
      "$ref" : "#/components/schemas/HALLink"
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

_job_submitted_response_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobSubmittedResponse": _job_submitted_response_model_schema})

_job_type_model_schema = json.loads(
    r"""{
  "title" : "JobType",
  "type" : "string",
  "enum" : [ "build", "deploy", "verify", "undeploy", "batch", "scale", "cleanup", "other" ]
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
  "title" : "JobTypeSchema",
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
      "$ref" : "#/components/schemas/HALLink"
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
      "$ref" : "#/components/schemas/HALLink"
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
      "$ref" : "#/components/schemas/HALLink"
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

_jobs_hal_link_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "jobs" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"JobsHALLink": _jobs_hal_link_model_schema})

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

_kf_serving_delete_multiple_response_model_schema = json.loads(
    r"""{
  "required" : [ "name", "versions" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string"
    },
    "versions" : {
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    }
  },
  "description" : "Models Deleted"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "KFServingDeleteMultipleResponse": _kf_serving_delete_multiple_response_model_schema
})

_kf_serving_delete_multiple_with_job_response_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "message", "name", "versions" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string"
    },
    "versions" : {
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "message" : {
      "type" : "string"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    }
  },
  "description" : "Model Deletions Initiated"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "KFServingDeleteMultipleWithJobResponse": _kf_serving_delete_multiple_with_job_response_model_schema
})

_kf_serving_delete_query_v1_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "async" : {
      "type" : "boolean",
      "description" : "If this is set to <code>true</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. Otherwise, the request will block until the job actions are completed, or a timeout occurs.",
      "default" : false
    },
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    },
    "page" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The number of pages to skip when returning result to this query."
    },
    "includeDraft" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**."
    },
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**."
    },
    "version" : {
      "type" : "string",
      "description" : "Filter on the version of the function (case-sensitive, supports wildcards)."
    },
    "status" : {
      "type" : "array",
      "description" : "Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions.",
      "items" : {
        "$ref" : "#/components/schemas/StatusFilter"
      }
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "createdBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "createdAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "name" : {
      "type" : "string",
      "description" : "Filter on the name of the function. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "Filter on the archive format of the function.",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    },
    "runtime" : {
      "type" : "array",
      "description" : "Filter on the runtime of the function.",
      "items" : {
        "$ref" : "#/components/schemas/Runtime"
      }
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "KFServingDeleteQueryV1": _kf_serving_delete_query_v1_model_schema
})

_kf_serving_delete_query_v2_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "comment" : {
      "type" : "string",
      "description" : "An optional user-specified comment corresponding to the operation."
    },
    "force" : {
      "type" : "boolean",
      "description" : "If <code>true</code>, the function version will be immediately undeployed and removed.\n\nOtherwise, the removal will be delayed to allow current invocations to end. During that period, the function is marked _deprecated_."
    },
    "undeploy" : {
      "type" : "boolean",
      "description" : "If `true`, the `DELETE` operation\n* undeploys the (openfaas) function: it becomes no longer available for invocation.\n* does NOT remove the function from registry: it stays in an `undeployed` status.  All assets and definitions are retained, so the version can be restored later with a  _rebuild_ action.\n\nIf `false`, the `DELETE` operation\n* _only_ marks the plug function as _deprecated_, the function remains active but is removed from the default listings.   This also applies to _draft_ versions.\n\nThis parameter is incompatible with `force=true`.\n\nIf not set the default behaviour applies:\n* _draft_ versions are _undeployed_ and _removed_ from registry.\n* non-_draft_ versions are marked _deprecated_ only."
    },
    "async" : {
      "type" : "boolean",
      "description" : "Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs.",
      "default" : true
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "KFServingDeleteQueryV2": _kf_serving_delete_query_v2_model_schema
})

_kf_serving_delete_response_model_schema = json.loads(
    r"""{
  "required" : [ "name", "version" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "description" : "The name of the function."
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    }
  },
  "description" : "Model Deleted"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "KFServingDeleteResponse": _kf_serving_delete_response_model_schema
})

_kf_serving_delete_with_job_response_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "message", "name", "version" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    },
    "name" : {
      "type" : "string",
      "description" : "The name of the function."
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    }
  },
  "description" : "Model Delete Initiated"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "KFServingDeleteWithJobResponse": _kf_serving_delete_with_job_response_model_schema
})

_kf_serving_latest_version_query_v2_model_schema = json.loads(
    r"""{
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
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "KFServingLatestVersionQueryV2": _kf_serving_latest_version_query_v2_model_schema
})

_kf_serving_latest_versions_query_v1_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    },
    "page" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The number of pages to skip when returning result to this query."
    },
    "includeDraft" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**."
    },
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**."
    },
    "version" : {
      "type" : "string",
      "description" : "Filter on the version of the function (case-sensitive, supports wildcards)."
    },
    "status" : {
      "type" : "array",
      "description" : "Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions.",
      "items" : {
        "$ref" : "#/components/schemas/StatusFilter"
      }
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "createdBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "createdAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "name" : {
      "type" : "string",
      "description" : "Filter on the name of the function. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "Filter on the archive format of the function.",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    },
    "runtime" : {
      "type" : "array",
      "description" : "Filter on the runtime of the function.",
      "items" : {
        "$ref" : "#/components/schemas/Runtime"
      }
    }
  },
  "additionalProperties" : false,
  "description" : "Model listing query"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "KFServingLatestVersionsQueryV1": _kf_serving_latest_versions_query_v1_model_schema
})

_kf_serving_latest_versions_query_v2_model_schema = json.loads(
    r"""{
  "description" : "Latest model versions listing query.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/LatestFunctionVersionsQuery"
  }, {
    "$ref" : "#/components/schemas/LatestFunctionsQuery"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "KFServingLatestVersionsQueryV2": _kf_serving_latest_versions_query_v2_model_schema
})

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
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"KFServingManifest": _kf_serving_manifest_model_schema})

_kf_serving_models_response_model_schema = json.loads(
    r"""{
  "required" : [ "models" ],
  "type" : "object",
  "properties" : {
    "models" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/KFServingResponse"
      }
    },
    "paging" : {
      "$ref" : "#/components/schemas/PagingResponse"
    }
  },
  "description" : "Successful Response"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "KFServingModelsResponse": _kf_serving_models_response_model_schema
})

_kf_serving_response_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "metadata", "name", "runtime", "status", "updatedAt", "updatedBy", "version" ],
  "type" : "object",
  "properties" : {
    "deploy" : {
      "$ref" : "#/components/schemas/FunctionDeployOverridesType"
    },
    "name" : {
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
    "status" : {
      "$ref" : "#/components/schemas/Status"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    },
    "_links" : {
      "type" : "array",
      "description" : "Links to related entities.",
      "items" : {
        "$ref" : "#/components/schemas/JobHALLinks"
      }
    }
  },
  "description" : "Successful Response"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"KFServingResponse": _kf_serving_response_model_schema})

_kf_serving_versions_query_v1_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    },
    "page" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The number of pages to skip when returning result to this query."
    },
    "version" : {
      "type" : "string",
      "description" : "Filter on the version of the function (case-sensitive, supports wildcards)."
    },
    "status" : {
      "type" : "array",
      "description" : "Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions.",
      "items" : {
        "$ref" : "#/components/schemas/StatusFilter"
      }
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "createdBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "createdAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "name" : {
      "type" : "string",
      "description" : "Filter on the name of the function. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "Filter on the archive format of the function.",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    },
    "runtime" : {
      "type" : "array",
      "description" : "Filter on the runtime of the function.",
      "items" : {
        "$ref" : "#/components/schemas/Runtime"
      }
    }
  },
  "additionalProperties" : false,
  "description" : "Named model versions query"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "KFServingVersionsQueryV1": _kf_serving_versions_query_v1_model_schema
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
  "required" : [ "createdAt", "createdBy", "deprecated", "draft", "model", "runtime", "status", "updatedAt", "updatedBy", "updates" ],
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
      "description" : "The audit logs corresponding to the latest modifying operations on this entity.",
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

_latest_function_versions_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    },
    "page" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The number of pages to skip when returning result to this query."
    },
    "includeDraft" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**."
    },
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**."
    },
    "deprecated" : {
      "type" : "boolean",
      "description" : "Filter on the deprecation status of the function."
    },
    "draft" : {
      "type" : "boolean",
      "description" : "Filter on the draft status of the function."
    },
    "nameVersion" : {
      "type" : "array",
      "description" : "Filter on exact `{name}@{version}` functions. Using this filter implies a `latest=false` default, returning multiple versions of the same named versions if they are filtered.",
      "items" : {
        "$ref" : "#/components/schemas/NamedVersion"
      }
    },
    "version" : {
      "type" : "string",
      "description" : "Filter on the version of the function (case-sensitive, supports wildcards)."
    },
    "status" : {
      "type" : "array",
      "description" : "Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions.",
      "items" : {
        "$ref" : "#/components/schemas/StatusFilter"
      }
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "createdBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "createdAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "name" : {
      "type" : "string",
      "description" : "Filter on the name of the function. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "Filter on the archive format of the function.",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    },
    "runtime" : {
      "type" : "array",
      "description" : "Filter on the runtime of the function.",
      "items" : {
        "$ref" : "#/components/schemas/Runtime"
      }
    },
    "latest" : {
      "type" : "boolean",
      "description" : "When `true`, only the latest version per function name is returned. If set to `false`, multiple versions per named function can be returned. Defaults to `true`, except when specific versions are selected with the `nameVersion` filter."
    }
  },
  "additionalProperties" : false,
  "description" : "Latest function versions listing query."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LatestFunctionVersionsQuery": _latest_function_versions_query_model_schema
})

_latest_functions_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    },
    "page" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The number of pages to skip when returning result to this query."
    },
    "includeDraft" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**."
    },
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**."
    },
    "name" : {
      "type" : "string",
      "description" : "Filter on the name of the function. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "Filter on the archive format of the function.",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    },
    "runtime" : {
      "type" : "array",
      "description" : "Filter on the runtime of the function.",
      "items" : {
        "$ref" : "#/components/schemas/Runtime"
      }
    }
  },
  "additionalProperties" : false,
  "description" : "Request to list latest function versions per named function. A request that only uses these query parameters will include links to the _latest_ draft/published versions."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"LatestFunctionsQuery": _latest_functions_query_model_schema})

_latest_models_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "count", "entities" ],
  "type" : "object",
  "properties" : {
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
        "$ref" : "#/components/schemas/LatestModelsResponseV2_entities_inner"
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

_latest_models_response_v2_entities_inner_model_schema = json.loads(
    r"""{
  "title" : "LatestModelsResponseV2_entities_inner",
  "required" : [ "_links", "createdAt", "createdBy", "deprecated", "draft", "model", "runtime", "status", "updatedAt", "updatedBy", "updates" ],
  "type" : "object",
  "properties" : {
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
      "description" : "The audit logs corresponding to the latest modifying operations on this entity.",
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
    "model" : {
      "$ref" : "#/components/schemas/KFServingManifest"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LatestModelsResponseV2_entities_inner": _latest_models_response_v2_entities_inner_model_schema
})

_latest_plug_query_model_schema = json.loads(
    r"""{
  "required" : [ "type" ],
  "type" : "object",
  "properties" : {
    "tags" : {
      "$ref" : "#/components/schemas/TagsFilter"
    },
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    },
    "page" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The number of pages to skip when returning result to this query."
    },
    "includeDraft" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**."
    },
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**."
    },
    "version" : {
      "type" : "string",
      "description" : "Filter on the version of the function (case-sensitive, supports wildcards)."
    },
    "status" : {
      "type" : "array",
      "description" : "Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions.",
      "items" : {
        "$ref" : "#/components/schemas/StatusFilter"
      }
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "createdBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "createdAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "name" : {
      "type" : "string",
      "description" : "Filter on the name of the function. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "Filter on the archive format of the function.",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    },
    "runtime" : {
      "type" : "array",
      "description" : "Filter on the runtime of the function.",
      "items" : {
        "$ref" : "#/components/schemas/Runtime"
      }
    },
    "type" : {
      "$ref" : "#/components/schemas/PlugType"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"LatestPlugQuery": _latest_plug_query_model_schema})

_latest_plug_version_query_v2_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/PlugType"
    },
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
  "description" : "Latest named plug version listing query"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LatestPlugVersionQueryV2": _latest_plug_version_query_v2_model_schema
})

_latest_plug_versions_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "tags" : {
      "$ref" : "#/components/schemas/TagsFilter"
    },
    "type" : {
      "$ref" : "#/components/schemas/PlugType"
    },
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    },
    "page" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The number of pages to skip when returning result to this query."
    },
    "includeDraft" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**."
    },
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**."
    },
    "deprecated" : {
      "type" : "boolean",
      "description" : "Filter on the deprecation status of the function."
    },
    "draft" : {
      "type" : "boolean",
      "description" : "Filter on the draft status of the function."
    },
    "nameVersion" : {
      "type" : "array",
      "description" : "Filter on exact `{name}@{version}` functions. Using this filter implies a `latest=false` default, returning multiple versions of the same named versions if they are filtered.",
      "items" : {
        "$ref" : "#/components/schemas/NamedVersion"
      }
    },
    "version" : {
      "type" : "string",
      "description" : "Filter on the version of the function (case-sensitive, supports wildcards)."
    },
    "status" : {
      "type" : "array",
      "description" : "Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions.",
      "items" : {
        "$ref" : "#/components/schemas/StatusFilter"
      }
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "createdBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "createdAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "name" : {
      "type" : "string",
      "description" : "Filter on the name of the function. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "Filter on the archive format of the function.",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    },
    "runtime" : {
      "type" : "array",
      "description" : "Filter on the runtime of the function.",
      "items" : {
        "$ref" : "#/components/schemas/Runtime"
      }
    },
    "latest" : {
      "type" : "boolean",
      "description" : "When `true`, only the latest version per function name is returned. If set to `false`, multiple versions per named function can be returned. Defaults to `true`, except when specific versions are selected with the `nameVersion` filter."
    }
  },
  "additionalProperties" : false,
  "description" : "Plug versions listing query."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LatestPlugVersionsQuery": _latest_plug_versions_query_model_schema
})

_latest_plug_versions_query_v2_model_schema = json.loads(
    r"""{
  "description" : "Latest plug versions listing query.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/LatestPlugVersionsQuery"
  }, {
    "$ref" : "#/components/schemas/LatestPlugsQuery"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LatestPlugVersionsQueryV2": _latest_plug_versions_query_v2_model_schema
})

_latest_plugs_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/PlugType"
    },
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    },
    "page" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The number of pages to skip when returning result to this query."
    },
    "includeDraft" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**."
    },
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**."
    },
    "name" : {
      "type" : "string",
      "description" : "Filter on the name of the function. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "Filter on the archive format of the function.",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    },
    "runtime" : {
      "type" : "array",
      "description" : "Filter on the runtime of the function.",
      "items" : {
        "$ref" : "#/components/schemas/Runtime"
      }
    }
  },
  "additionalProperties" : false,
  "description" : "Latest plug versions listing query with latest links. A request that only uses these query parameters will include links to the _latest_ draft/published versions of the plug."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"LatestPlugsQuery": _latest_plugs_query_model_schema})

_latest_plugs_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "count", "entities" ],
  "type" : "object",
  "properties" : {
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
        "$ref" : "#/components/schemas/LatestPlugsResponseV2_entities_inner"
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

_latest_plugs_response_v2_entities_inner_model_schema = json.loads(
    r"""{
  "title" : "LatestPlugsResponseV2_entities_inner",
  "required" : [ "_links", "createdAt", "createdBy", "deprecated", "draft", "plug", "runtime", "status", "updatedAt", "updatedBy", "updates" ],
  "type" : "object",
  "properties" : {
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
      "description" : "The audit logs corresponding to the latest modifying operations on this entity.",
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
    "plug" : {
      "$ref" : "#/components/schemas/PlugManifest"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LatestPlugsResponseV2_entities_inner": _latest_plugs_response_v2_entities_inner_model_schema
})

_latest_version_level_model_schema = json.loads(
    r"""{
  "title" : "LatestVersionLevel",
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
        "$ref" : "#/components/schemas/LatestWebscriptsResponseV2_entities_inner"
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

_latest_webscripts_response_v2_entities_inner_model_schema = json.loads(
    r"""{
  "title" : "LatestWebscriptsResponseV2_entities_inner",
  "required" : [ "_links", "createdAt", "createdBy", "deprecated", "draft", "runtime", "status", "updatedAt", "updatedBy", "updates", "webscript" ],
  "type" : "object",
  "properties" : {
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
      "description" : "The audit logs corresponding to the latest modifying operations on this entity.",
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
    "LatestWebscriptsResponseV2_entities_inner": _latest_webscripts_response_v2_entities_inner_model_schema
})

_legacy_configuration_object_model_schema = json.loads(
    r"""{
  "title" : "LegacyConfigurationObject",
  "required" : [ "name", "type" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "type" : "string"
    },
    "type" : {
      "$ref" : "#/components/schemas/PlugPropertyDataType"
    },
    "mandatory" : {
      "title" : "mandatory",
      "type" : "boolean"
    },
    "format" : {
      "$ref" : "#/components/schemas/LegacyConfigurationObject_format"
    },
    "defaultValue" : {
      "$ref" : "#/components/schemas/DefaultValue"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyConfigurationObject": _legacy_configuration_object_model_schema
})

_legacy_configuration_object_format_model_schema = json.loads(
    r"""{
  "title" : "LegacyConfigurationObject_format",
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/PlugPropertyFormatType"
    },
    "values" : {
      "title" : "values",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/EnumValue"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyConfigurationObject_format": _legacy_configuration_object_format_model_schema
})

_legacy_configuration_response_object_model_schema = json.loads(
    r"""{
  "title" : "LegacyConfigurationResponseObject",
  "required" : [ "name", "type" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "type" : "string"
    },
    "type" : {
      "$ref" : "#/components/schemas/PlugPropertyDataType"
    },
    "mandatory" : {
      "title" : "mandatory",
      "type" : "boolean"
    },
    "format" : {
      "$ref" : "#/components/schemas/LegacyConfigurationObject_format"
    },
    "defaultValue" : {
      "$ref" : "#/components/schemas/DefaultValue"
    },
    "sensitive" : {
      "title" : "sensitive",
      "type" : "boolean"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyConfigurationResponseObject": _legacy_configuration_response_object_model_schema
})

_legacy_create_debug_response_model_schema = json.loads(
    r"""{
  "required" : [ "functionName" ],
  "type" : "object",
  "properties" : {
    "functionName" : {
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyCreateDebugResponse": _legacy_create_debug_response_model_schema
})

_legacy_debug_plug_manifest_model_schema = json.loads(
    r"""{
  "required" : [ "metadata", "name", "runtime", "script", "tenant", "version" ],
  "type" : "object",
  "properties" : {
    "deploy" : {
      "$ref" : "#/components/schemas/FunctionDeployOverridesType"
    },
    "name" : {
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
    "tenant" : {
      "$ref" : "#/components/schemas/TenantId"
    },
    "dependencies" : {
      "$ref" : "#/components/schemas/LegacyPlugDependencies"
    },
    "script" : {
      "type" : "string"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyDebugPlugManifest": _legacy_debug_plug_manifest_model_schema
})

_legacy_debug_plug_request_model_schema = json.loads(
    r"""{
  "required" : [ "script" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/PlugType"
    },
    "script" : {
      "type" : "string"
    },
    "dependencies" : {
      "$ref" : "#/components/schemas/LegacyPlugDependencies"
    },
    "metadata" : {
      "$ref" : "#/components/schemas/FunctionMeta"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyDebugPlugRequest": _legacy_debug_plug_request_model_schema
})

_legacy_documentation_model_schema = json.loads(
    r"""{
  "required" : [ "configuration", "rawData", "supportedStates" ],
  "type" : "object",
  "properties" : {
    "supportedStates" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/DocumentationProperty"
      }
    },
    "configuration" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/DocumentationProperty"
      }
    },
    "rawData" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/DocumentationProperty"
      }
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"LegacyDocumentation": _legacy_documentation_model_schema})

_legacy_documentation_request_model_schema = json.loads(
    r"""{
  "required" : [ "configuration", "rawData", "supportedStates" ],
  "type" : "object",
  "properties" : {
    "description" : {
      "type" : "string"
    },
    "supportedStates" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/DocumentationProperty"
      }
    },
    "configuration" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/DocumentationProperty"
      }
    },
    "rawData" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/DocumentationProperty"
      }
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyDocumentationRequest": _legacy_documentation_request_model_schema
})

_legacy_function_meta_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "author" : {
      "type" : "string"
    },
    "description" : {
      "type" : "string"
    },
    "category" : {
      "type" : "string"
    },
    "tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Tag"
      }
    },
    "iconURL" : {
      "type" : "string"
    },
    "friendlyName" : {
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"LegacyFunctionMeta": _legacy_function_meta_model_schema})

_legacy_plug_create_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "async" : {
      "type" : "boolean",
      "description" : "If this is set to <code>true</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. Otherwise, the request will block until the job actions are completed, or a timeout occurs.",
      "default" : false
    },
    "dryRun" : {
      "type" : "boolean",
      "description" : "If set to <code>true</true>, only validates the incoming request."
    },
    "scaleToZero" : {
      "type" : "boolean",
      "description" : "If set to <code>true</true>, scales the function to zero after successful deployment."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyPlugCreateQuery": _legacy_plug_create_query_model_schema
})

_legacy_plug_create_request_model_schema = json.loads(
    r"""{
  "required" : [ "metadata", "name", "script", "version" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string"
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "script" : {
      "type" : "string"
    },
    "dependencies" : {
      "$ref" : "#/components/schemas/LegacyPlugDependencies"
    },
    "metadata" : {
      "$ref" : "#/components/schemas/LegacyPlugRequest_metadata"
    },
    "type" : {
      "$ref" : "#/components/schemas/PlugType"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyPlugCreateRequest": _legacy_plug_create_request_model_schema
})

_legacy_plug_create_response_model_schema = json.loads(
    r"""{
  "required" : [ "entity", "statusCode", "uri" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "type" : "number"
    },
    "uri" : {
      "type" : "string"
    },
    "entity" : {
      "$ref" : "#/components/schemas/LegacyPlugScriptResponse"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyPlugCreateResponse": _legacy_plug_create_response_model_schema
})

_legacy_plug_meta_request_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "author" : {
      "type" : "string"
    },
    "description" : {
      "type" : "string"
    },
    "category" : {
      "type" : "string"
    },
    "tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Tag"
      }
    },
    "iconURL" : {
      "type" : "string"
    },
    "friendlyName" : {
      "type" : "string"
    },
    "documentation" : {
      "$ref" : "#/components/schemas/LegacyPlugRequest_metadata_documentation"
    },
    "documentationURL" : {
      "type" : "string"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyPlugMetaRequest": _legacy_plug_meta_request_model_schema
})

_legacy_plug_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "description" : "Filter on the name of the function. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "Filter on the archive format of the function.",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    },
    "runtime" : {
      "type" : "array",
      "description" : "Filter on the runtime of the function.",
      "items" : {
        "$ref" : "#/components/schemas/Runtime"
      }
    },
    "version" : {
      "type" : "string",
      "description" : "Filter on the version of the function (case-sensitive, supports wildcards)."
    },
    "status" : {
      "type" : "array",
      "description" : "Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions.",
      "items" : {
        "$ref" : "#/components/schemas/StatusFilter"
      }
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "createdBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "createdAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "includeDraft" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**."
    },
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**."
    },
    "page" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The number of pages to skip when returning result to this query."
    },
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    },
    "tags" : {
      "$ref" : "#/components/schemas/TagsFilter"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"LegacyPlugQuery": _legacy_plug_query_model_schema})

_legacy_plug_request_model_schema = json.loads(
    r"""{
  "required" : [ "metadata", "name", "script", "type", "version" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string"
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "script" : {
      "type" : "string"
    },
    "dependencies" : {
      "$ref" : "#/components/schemas/LegacyPlugDependencies"
    },
    "metadata" : {
      "$ref" : "#/components/schemas/LegacyPlugRequest_metadata"
    },
    "type" : {
      "$ref" : "#/components/schemas/PlugType"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"LegacyPlugRequest": _legacy_plug_request_model_schema})

_legacy_plug_request_metadata_model_schema = json.loads(
    r"""{
  "title" : "LegacyPlugRequest_metadata",
  "type" : "object",
  "properties" : {
    "requiredProperties" : {
      "$ref" : "#/components/schemas/LegacyRequiredProperties"
    },
    "supportedStates" : {
      "title" : "supportedStates",
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "rawData" : {
      "title" : "rawData",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/LegacyPlugRequest_metadata_rawData_inner"
      }
    },
    "configuration" : {
      "$ref" : "#/components/schemas/LegacyConfiguration"
    },
    "author" : {
      "title" : "author",
      "type" : "string"
    },
    "description" : {
      "title" : "description",
      "type" : "string"
    },
    "category" : {
      "title" : "category",
      "type" : "string"
    },
    "tags" : {
      "title" : "tags",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Tag"
      }
    },
    "iconURL" : {
      "title" : "iconURL",
      "type" : "string"
    },
    "friendlyName" : {
      "title" : "friendlyName",
      "type" : "string"
    },
    "documentation" : {
      "$ref" : "#/components/schemas/LegacyPlugRequest_metadata_documentation"
    },
    "documentationURL" : {
      "title" : "documentationURL",
      "type" : "string"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyPlugRequest_metadata": _legacy_plug_request_metadata_model_schema
})

_legacy_plug_request_metadata_documentation_model_schema = json.loads(
    r"""{
  "title" : "LegacyPlugRequest_metadata_documentation",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/LegacyPlugRequest_metadata_documentation_anyOf"
  }, {
    "$ref" : "#/components/schemas/Documentation"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyPlugRequest_metadata_documentation": _legacy_plug_request_metadata_documentation_model_schema
})

_legacy_plug_request_metadata_documentation_any_of_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "supportedStates" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/DocumentationProperty"
      }
    },
    "configuration" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/DocumentationProperty"
      }
    },
    "rawData" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/DocumentationProperty"
      }
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyPlugRequest_metadata_documentation_anyOf": _legacy_plug_request_metadata_documentation_any_of_model_schema
})

_legacy_plug_request_metadata_raw_data_inner_model_schema = json.loads(
    r"""{
  "title" : "LegacyPlugRequest_metadata_rawData_inner",
  "required" : [ "parameter" ],
  "type" : "object",
  "properties" : {
    "parameter" : {
      "title" : "parameter",
      "type" : "string"
    },
    "dataType" : {
      "$ref" : "#/components/schemas/PlugPropertyDataType"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyPlugRequest_metadata_rawData_inner": _legacy_plug_request_metadata_raw_data_inner_model_schema
})

_legacy_plug_response_model_schema = json.loads(
    r"""{
  "required" : [ "commands", "isDeprecated", "mediaType", "metadata", "name", "status", "version" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string"
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "author" : {
      "type" : "string"
    },
    "category" : {
      "type" : "string"
    },
    "iconURL" : {
      "type" : "string"
    },
    "documentationURL" : {
      "type" : "string"
    },
    "isDeprecated" : {
      "type" : "boolean"
    },
    "description" : {
      "type" : "string"
    },
    "states" : {
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "rawData" : {
      "type" : "array",
      "items" : {
        "type" : "object"
      }
    },
    "mediaType" : {
      "$ref" : "#/components/schemas/MediaType"
    },
    "configuration" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/LegacyConfigurationResponseObject"
      }
    },
    "commands" : {
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "status" : {
      "$ref" : "#/components/schemas/Status"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    },
    "metadata" : {
      "$ref" : "#/components/schemas/LegacyPlugResponse_metadata"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"LegacyPlugResponse": _legacy_plug_response_model_schema})

_legacy_plug_response_metadata_model_schema = json.loads(
    r"""{
  "title" : "LegacyPlugResponse_metadata",
  "type" : "object",
  "properties" : {
    "documentation" : {
      "$ref" : "#/components/schemas/LegacyDocumentation"
    },
    "author" : {
      "title" : "author",
      "type" : "string"
    },
    "description" : {
      "title" : "description",
      "type" : "string"
    },
    "category" : {
      "title" : "category",
      "type" : "string"
    },
    "tags" : {
      "title" : "tags",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Tag"
      }
    },
    "iconURL" : {
      "title" : "iconURL",
      "type" : "string"
    },
    "friendlyName" : {
      "title" : "friendlyName",
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyPlugResponse_metadata": _legacy_plug_response_metadata_model_schema
})

_legacy_plug_script_meta_model_schema = json.loads(
    r"""{
  "title" : "LegacyPlugScriptMeta",
  "required" : [ "rawData", "supportedStates" ],
  "type" : "object",
  "properties" : {
    "author" : {
      "title" : "author",
      "type" : "string"
    },
    "description" : {
      "title" : "description",
      "type" : "string"
    },
    "category" : {
      "title" : "category",
      "type" : "string"
    },
    "tags" : {
      "title" : "tags",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/Tag"
      }
    },
    "iconURL" : {
      "title" : "iconURL",
      "type" : "string"
    },
    "friendlyName" : {
      "title" : "friendlyName",
      "type" : "string"
    },
    "supportedStates" : {
      "title" : "supportedStates",
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "rawData" : {
      "title" : "rawData",
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/LegacyPlugScriptMeta_rawData_inner"
      }
    },
    "requiredProperties" : {
      "$ref" : "#/components/schemas/LegacyRequiredProperties"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyPlugScriptMeta": _legacy_plug_script_meta_model_schema
})

_legacy_plug_script_meta_raw_data_inner_model_schema = json.loads(
    r"""{
  "title" : "LegacyPlugScriptMeta_rawData_inner",
  "required" : [ "parameter" ],
  "type" : "object",
  "properties" : {
    "parameter" : {
      "title" : "parameter",
      "type" : "string"
    },
    "dataType" : {
      "title" : "dataType",
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyPlugScriptMeta_rawData_inner": _legacy_plug_script_meta_raw_data_inner_model_schema
})

_legacy_plug_script_response_model_schema = json.loads(
    r"""{
  "title" : "LegacyPlugScriptResponse",
  "required" : [ "dependencies", "metadata", "name", "script", "type", "version" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "type" : "string"
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "type" : {
      "$ref" : "#/components/schemas/PlugType"
    },
    "script" : {
      "title" : "script",
      "type" : "string"
    },
    "metadata" : {
      "$ref" : "#/components/schemas/LegacyPlugScriptMeta"
    },
    "dependencies" : {
      "title" : "dependencies",
      "type" : "object"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyPlugScriptResponse": _legacy_plug_script_response_model_schema
})

_legacy_required_properties_inner_model_schema = json.loads(
    r"""{
  "title" : "LegacyRequiredProperties_inner",
  "anyOf" : [ {
    "type" : "string"
  }, {
    "$ref" : "#/components/schemas/LegacyRequiredPropertyObject"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyRequiredProperties_inner": _legacy_required_properties_inner_model_schema
})

_legacy_required_property_object_model_schema = json.loads(
    r"""{
  "required" : [ "mandatory", "name", "sensitive", "type" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string"
    },
    "type" : {
      "$ref" : "#/components/schemas/PlugPropertyDataType"
    },
    "mandatory" : {
      "type" : "boolean"
    },
    "sensitive" : {
      "type" : "boolean"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "LegacyRequiredPropertyObject": _legacy_required_property_object_model_schema
})

_limit_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"LimitQuery": _limit_query_model_schema})

_media_type_model_schema = json.loads(
    r"""{
  "title" : "MediaType",
  "type" : "string",
  "enum" : [ "application/javascript", "application/java-vm", "text/x-python", "text/x-golang" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"MediaType": _media_type_model_schema})

_message_and_status_response_model_schema = json.loads(
    r"""{
  "required" : [ "message", "statusCode" ],
  "type" : "object",
  "properties" : {
    "message" : {
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
    "MessageAndStatusResponse": _message_and_status_response_model_schema
})

_message_response_model_schema = json.loads(
    r"""{
  "required" : [ "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"MessageResponse": _message_response_model_schema})

_model_model_schema = json.loads(
    r"""{
  "title" : "Model",
  "required" : [ "model" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "model" : {
      "$ref" : "#/components/schemas/HALLink"
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
      "$ref" : "#/components/schemas/HALLink"
    },
    "job" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "model" : {
      "$ref" : "#/components/schemas/HALLink"
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
      "$ref" : "#/components/schemas/HALLink"
    },
    "model" : {
      "$ref" : "#/components/schemas/HALLink"
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

_multipart_file_upload__model_schema = json.loads(
    r"""{
  "title" : "Multipart file upload.",
  "type" : "object",
  "properties" : {
    "filename" : {
      "type" : "array",
      "items" : {
        "type" : "string",
        "format" : "binary"
      }
    }
  },
  "description" : "A multi-part upload containing one or more file assets.",
  "nullable" : true
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "Multipart_file_upload_": _multipart_file_upload__model_schema
})

_name_model_schema = json.loads(
    r"""{
  "required" : [ "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "description" : "The name of the function."
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Name": _name_model_schema})

_name_and_version_model_schema = json.loads(
    r"""{
  "required" : [ "name", "version" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "description" : "The name of the function."
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"NameAndVersion": _name_and_version_model_schema})

_named_function_versions_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    },
    "page" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The number of pages to skip when returning result to this query."
    },
    "deprecated" : {
      "type" : "boolean",
      "description" : "Filter on the deprecation status of the function."
    },
    "draft" : {
      "type" : "boolean",
      "description" : "Filter on the draft status of the function."
    },
    "version" : {
      "type" : "string",
      "description" : "Filter on the version of the function (case-sensitive, supports wildcards)."
    },
    "status" : {
      "type" : "array",
      "description" : "Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions.",
      "items" : {
        "$ref" : "#/components/schemas/StatusFilter"
      }
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "createdBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "createdAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "Filter on the archive format of the function.",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    },
    "runtime" : {
      "type" : "array",
      "description" : "Filter on the runtime of the function.",
      "items" : {
        "$ref" : "#/components/schemas/Runtime"
      }
    }
  },
  "additionalProperties" : false,
  "description" : "Named function versions listing query."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "NamedFunctionVersionsQuery": _named_function_versions_query_model_schema
})

_named_kf_serving_versions_query_v2_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    },
    "page" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The number of pages to skip when returning result to this query."
    },
    "deprecated" : {
      "type" : "boolean",
      "description" : "Filter on the deprecation status of the function."
    },
    "draft" : {
      "type" : "boolean",
      "description" : "Filter on the draft status of the function."
    },
    "version" : {
      "type" : "string",
      "description" : "Filter on the version of the function (case-sensitive, supports wildcards)."
    },
    "status" : {
      "type" : "array",
      "description" : "Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions.",
      "items" : {
        "$ref" : "#/components/schemas/StatusFilter"
      }
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "createdBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "createdAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "Filter on the archive format of the function.",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    },
    "runtime" : {
      "type" : "array",
      "description" : "Filter on the runtime of the function.",
      "items" : {
        "$ref" : "#/components/schemas/Runtime"
      }
    }
  },
  "additionalProperties" : false,
  "description" : "Named Model versions query."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "NamedKFServingVersionsQueryV2": _named_kf_serving_versions_query_v2_model_schema
})

_named_parameters_typeof_as_job_reference__model_schema = json.loads(
    r"""{
  "required" : [ "jobStatus" ],
  "type" : "object",
  "properties" : {
    "jobStatus" : {
      "$ref" : "#/components/schemas/NamedParameters_typeof_asJobReference__jobStatus"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "NamedParameters_typeof_asJobReference_": _named_parameters_typeof_as_job_reference__model_schema
})

_named_parameters_typeof_as_job_reference__job_status_model_schema = json.loads(
    r"""{
  "title" : "NamedParameters_typeof_asJobReference__jobStatus",
  "required" : [ "createdAt", "createdBy", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
    },
    "type" : {
      "title" : "type",
      "description" : "The type of the background task."
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "request" : {
      "title" : "request",
      "description" : "The request that initiated this job."
    },
    "result" : {
      "title" : "result",
      "description" : "The result of the job if completed."
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp of creation of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user that created this job"
    },
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "Request operation"
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
MODEL_DEFINITIONS.update({
    "NamedParameters_typeof_asJobReference__jobStatus": _named_parameters_typeof_as_job_reference__job_status_model_schema
})

_named_parameters_typeof_from_legacy__model_schema = json.loads(
    r"""{
  "required" : [ "metadata" ],
  "type" : "object",
  "properties" : {
    "metadata" : {
      "$ref" : "#/components/schemas/LegacyPlugMetaRequest"
    },
    "currentInterface" : {
      "$ref" : "#/components/schemas/PlugInterface"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "NamedParameters_typeof_fromLegacy_": _named_parameters_typeof_from_legacy__model_schema
})

_named_parameters_typeof_from_legacy_documentation__model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "legacyDocumentation" : {
      "$ref" : "#/components/schemas/LegacyPlugRequest_metadata_documentation"
    },
    "currentInterface" : {
      "$ref" : "#/components/schemas/PlugInterface"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "NamedParameters_typeof_fromLegacyDocumentation_": _named_parameters_typeof_from_legacy_documentation__model_schema
})

_named_parameters_typeof_is_not_legacy__model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "documentation" : {
      "$ref" : "#/components/schemas/LegacyPlugRequest_metadata_documentation"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "NamedParameters_typeof_isNotLegacy_": _named_parameters_typeof_is_not_legacy__model_schema
})

_named_plug_versions_query_v2_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "tags" : {
      "$ref" : "#/components/schemas/TagsFilter"
    },
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    },
    "page" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The number of pages to skip when returning result to this query."
    },
    "deprecated" : {
      "type" : "boolean",
      "description" : "Filter on the deprecation status of the function."
    },
    "draft" : {
      "type" : "boolean",
      "description" : "Filter on the draft status of the function."
    },
    "version" : {
      "type" : "string",
      "description" : "Filter on the version of the function (case-sensitive, supports wildcards)."
    },
    "status" : {
      "type" : "array",
      "description" : "Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions.",
      "items" : {
        "$ref" : "#/components/schemas/StatusFilter"
      }
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "createdBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "createdAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "Filter on the archive format of the function.",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    },
    "runtime" : {
      "type" : "array",
      "description" : "Filter on the runtime of the function.",
      "items" : {
        "$ref" : "#/components/schemas/Runtime"
      }
    }
  },
  "additionalProperties" : false,
  "description" : "Named plug version listing query"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "NamedPlugVersionsQueryV2": _named_plug_versions_query_v2_model_schema
})

_named_versions_filter_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "nameVersion" : {
      "type" : "array",
      "description" : "Filter on exact `{name}@{version}` functions. Using this filter implies a `latest=false` default, returning multiple versions of the same named versions if they are filtered.",
      "items" : {
        "$ref" : "#/components/schemas/NamedVersion"
      }
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"NamedVersionsFilter": _named_versions_filter_model_schema})

_named_webscript_versions_query_v2_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    },
    "page" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The number of pages to skip when returning result to this query."
    },
    "deprecated" : {
      "type" : "boolean",
      "description" : "Filter on the deprecation status of the function."
    },
    "draft" : {
      "type" : "boolean",
      "description" : "Filter on the draft status of the function."
    },
    "version" : {
      "type" : "string",
      "description" : "Filter on the version of the function (case-sensitive, supports wildcards)."
    },
    "status" : {
      "type" : "array",
      "description" : "Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions.",
      "items" : {
        "$ref" : "#/components/schemas/StatusFilter"
      }
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "createdBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "createdAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "Filter on the archive format of the function.",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    },
    "runtime" : {
      "type" : "array",
      "description" : "Filter on the runtime of the function.",
      "items" : {
        "$ref" : "#/components/schemas/Runtime"
      }
    }
  },
  "additionalProperties" : false,
  "description" : "Webscript named versions listing query."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "NamedWebscriptVersionsQueryV2": _named_webscript_versions_query_v2_model_schema
})

_openfaas_deploy_args_model_schema = json.loads(
    r"""{
  "required" : [ "endpoint", "imageName", "namespace" ],
  "type" : "object",
  "properties" : {
    "namespace" : {
      "type" : "string",
      "description" : "The (openfaas) namespace for the target function."
    },
    "endpoint" : {
      "type" : "string",
      "description" : "The (openfaas) endpoint service name"
    },
    "imageName" : {
      "type" : "string",
      "description" : "The image name to use for deploying this function"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"OpenfaasDeployArgs": _openfaas_deploy_args_model_schema})

_openfaas_function_ref_model_schema = json.loads(
    r"""{
  "required" : [ "endpoint", "namespace" ],
  "type" : "object",
  "properties" : {
    "namespace" : {
      "type" : "string",
      "description" : "The (openfaas) namespace for the target function."
    },
    "endpoint" : {
      "type" : "string",
      "description" : "The (openfaas) endpoint service name"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"OpenfaasFunctionRef": _openfaas_function_ref_model_schema})

_operation_model_schema = json.loads(
    r"""{
  "required" : [ "description", "id", "name", "type" ],
  "type" : "object",
  "properties" : {
    "id" : {
      "type" : "string"
    },
    "description" : {
      "type" : "string"
    },
    "name" : {
      "type" : "string",
      "deprecated" : true
    },
    "type" : {
      "$ref" : "#/components/schemas/JobType"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Operation": _operation_model_schema})

_operation_status_model_schema = json.loads(
    r"""{
  "required" : [ "description", "done", "id", "name", "type" ],
  "type" : "object",
  "properties" : {
    "id" : {
      "type" : "string"
    },
    "description" : {
      "type" : "string"
    },
    "name" : {
      "type" : "string",
      "deprecated" : true
    },
    "type" : {
      "$ref" : "#/components/schemas/JobType"
    },
    "done" : {
      "type" : "boolean"
    },
    "error" : {
      "$ref" : "#/components/schemas/OperationStatus_error"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"OperationStatus": _operation_status_model_schema})

_operation_status_error_model_schema = json.loads(
    r"""{
  "title" : "OperationStatus_error",
  "required" : [ "code", "message", "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "type" : "string"
    },
    "message" : {
      "title" : "message",
      "type" : "string"
    },
    "stack" : {
      "title" : "stack",
      "type" : "string"
    },
    "code" : {
      "title" : "code",
      "type" : "string"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "OperationStatus_error": _operation_status_error_model_schema
})

_paging_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    },
    "page" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The number of pages to skip when returning result to this query."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PagingQuery": _paging_query_model_schema})

_paging_response_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "count" : {
      "type" : "number",
      "description" : "The total count of matching items, from which this result is one page."
    },
    "limit" : {
      "type" : "number",
      "description" : "The page size used for this query result."
    },
    "page" : {
      "type" : "number",
      "description" : "The page number of a paged query result."
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PagingResponse": _paging_response_model_schema})

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

_patch_interface_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "comment" : {
      "type" : "string",
      "description" : "An optional user-specified comment corresponding to the operation."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PatchInterfaceQuery": _patch_interface_query_model_schema})

_patch_metadata_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "comment" : {
      "type" : "string",
      "description" : "An optional user-specified comment corresponding to the operation."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PatchMetadataQuery": _patch_metadata_query_model_schema})

_patch_plug_request_v1_model_schema = json.loads(
    r"""{
  "required" : [ "metadata" ],
  "type" : "object",
  "properties" : {
    "metadata" : {
      "$ref" : "#/components/schemas/UserPlugMeta"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PatchPlugRequestV1": _patch_plug_request_v1_model_schema})

_plug_model_schema = json.loads(
    r"""{
  "title" : "Plug",
  "required" : [ "plug" ],
  "type" : "object",
  "properties" : {
    "event" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "plug" : {
      "$ref" : "#/components/schemas/HALLink"
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
      "$ref" : "#/components/schemas/HALLink"
    },
    "job" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "plug" : {
      "$ref" : "#/components/schemas/HALLink"
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
      "$ref" : "#/components/schemas/HALLink"
    },
    "plug" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Plug_2": _plug_2_model_schema})

_plug_delete_force_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "force" : {
      "type" : "boolean",
      "description" : "If <code>true</code>, the plug version(s) will be undeployed and removed. Otherwise, the plug version(s) will only be <code>deprecated</code>, i.e removed from regular listings."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PlugDeleteForceQuery": _plug_delete_force_query_model_schema
})

_plug_delete_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
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
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PlugDeleteQuery": _plug_delete_query_model_schema})

_plug_interface_model_schema = json.loads(
    r"""{
  "title" : "PlugInterface",
  "type" : "object",
  "properties" : {
    "states" : {
      "title" : "states",
      "type" : "array",
      "description" : "The states of a plug as implemented in the plug code.",
      "items" : {
        "type" : "string"
      }
    },
    "input" : {
      "title" : "input",
      "type" : "array",
      "description" : "The named input parameters of a plug",
      "items" : {
        "$ref" : "#/components/schemas/PlugProperty"
      }
    },
    "output" : {
      "title" : "output",
      "type" : "array",
      "description" : "The named output parameters of a plug",
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

_plug_listing_and_query_response_model_schema = json.loads(
    r"""{
  "required" : [ "plugs" ],
  "type" : "object",
  "properties" : {
    "count" : {
      "type" : "number",
      "description" : "The total count of matching items, from which this result is one page."
    },
    "limit" : {
      "type" : "number",
      "description" : "The page size used for this query result."
    },
    "page" : {
      "type" : "number",
      "description" : "The page number of a paged query result."
    },
    "plugs" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/PlugResponse"
      }
    }
  },
  "description" : "Successful Response"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PlugListingAndQueryResponse": _plug_listing_and_query_response_model_schema
})

_plug_listing_response_model_schema = json.loads(
    r"""{
  "required" : [ "plugs" ],
  "type" : "object",
  "properties" : {
    "plugs" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/components/schemas/PlugResponse"
      }
    }
  },
  "description" : "Successful Response"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PlugListingResponse": _plug_listing_response_model_schema})

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
    "tags" : {
      "title" : "tags",
      "type" : "array",
      "description" : "Tags associated with this function.",
      "example" : [ {
        "name" : "awaiting-review",
        "color" : "#4153ea"
      }, {
        "name" : "demo",
        "color" : "#e639a4"
      } ],
      "items" : {
        "$ref" : "#/components/schemas/Tag"
      }
    },
    "friendlyName" : {
      "title" : "friendlyName",
      "type" : "string",
      "description" : "Display title for this function."
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
  "enum" : [ "string", "integer", "long", "float", "double", "boolean", "object" ]
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
  "enum" : [ "enum", "resource", "vault", "duration", "code", "url", "date", "template" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "PlugPropertyFormatType": _plug_property_format_type_model_schema
})

_plug_response_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "isDeprecated", "metadata", "name", "runtime", "status", "updatedAt", "updatedBy", "version" ],
  "type" : "object",
  "properties" : {
    "deploy" : {
      "$ref" : "#/components/schemas/FunctionDeployOverridesType"
    },
    "name" : {
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
    "status" : {
      "$ref" : "#/components/schemas/Status"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    },
    "_links" : {
      "type" : "array",
      "description" : "Links to related entities.",
      "items" : {
        "$ref" : "#/components/schemas/JobHALLinks"
      }
    },
    "isDeprecated" : {
      "type" : "boolean"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PlugResponse": _plug_response_model_schema})

_plug_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "deprecated", "draft", "plug", "runtime", "status", "updatedAt", "updatedBy", "updates" ],
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
      "description" : "The audit logs corresponding to the latest modifying operations on this entity.",
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
  "title" : "PlugType",
  "type" : "string",
  "enum" : [ "sensor", "actuator", "transformer" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PlugType": _plug_type_model_schema})

_plug_type_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/PlugType"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PlugTypeQuery": _plug_type_query_model_schema})

_plug_versions_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "count", "entities" ],
  "type" : "object",
  "properties" : {
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

_publish_function_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "comment" : {
      "type" : "string",
      "description" : "An optional user-specified comment corresponding to the operation."
    },
    "deprecatePrevious" : {
      "$ref" : "#/components/schemas/DeprecatePreviousPolicy"
    },
    "async" : {
      "type" : "boolean",
      "description" : "Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs.",
      "default" : true
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"PublishFunctionQuery": _publish_function_query_model_schema})

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

_rebuild_computed_response_model_schema = json.loads(
    r"""{
  "required" : [ "causes", "message" ],
  "type" : "object",
  "properties" : {
    "message" : {
      "type" : "string"
    },
    "causes" : {
      "$ref" : "#/components/schemas/JobCauses"
    }
  },
  "description" : "Rebuild Ignored"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "RebuildComputedResponse": _rebuild_computed_response_model_schema
})

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

_rebuild_query_params_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "upgrade" : {
      "$ref" : "#/components/schemas/RebuildPolicy"
    },
    "dryRun" : {
      "type" : "boolean",
      "description" : "If set to <code>true</code>, checks whether rebuild jobs are needed, but do not start any jobs."
    },
    "forceVersion" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "ignoreChecks" : {
      "type" : "boolean",
      "description" : "If set to true, checks that normally prevent a rebuild are overriden. These checks include:\n* function state in `pending`, `running`, `failed` or `undeployed`\n* backoff period due to recent failures\n* usage of deprecated dependencies\n* running jobs on entity\n* the `dryRun` option"
    },
    "scaleToZero" : {
      "type" : "boolean",
      "description" : "Indicates whether the function needs to be scaled down after successful (re-)deployment. If not set, the function is scaled to zero only if it was not active before this command."
    },
    "skipRebuild" : {
      "type" : "boolean",
      "description" : "If set, the function will not be rebuild. Always uses the current runtime version when re-deploying/re-verifying the function."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RebuildQueryParams": _rebuild_query_params_model_schema})

_rebuild_query_v2_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "comment" : {
      "type" : "string",
      "description" : "An optional user-specified comment corresponding to the operation."
    },
    "dryRun" : {
      "type" : "boolean",
      "description" : "If set to <code>true</code>, checks whether rebuild jobs are needed, but do not start any jobs."
    },
    "async" : {
      "type" : "boolean",
      "description" : "Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs.",
      "default" : true
    },
    "upgrade" : {
      "$ref" : "#/components/schemas/RebuildPolicy"
    },
    "forceVersion" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "ignoreChecks" : {
      "type" : "boolean",
      "description" : "If set to true, checks that normally prevent a rebuild are overriden. These checks include:\n* function state in `pending`, `running`, `failed` or `undeployed`\n* backoff period due to recent failures\n* usage of deprecated dependencies\n* running jobs on entity\n* the `dryRun` option"
    },
    "scaleToZero" : {
      "type" : "boolean",
      "description" : "Indicates whether the function needs to be scaled down after successful (re-)deployment. If not set, the function is scaled to zero only if it was not active before this command."
    },
    "skipRebuild" : {
      "type" : "boolean",
      "description" : "If set, the function will not be rebuild. Always uses the current runtime version when re-deploying/re-verifying the function."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RebuildQueryV2": _rebuild_query_v2_model_schema})

_rebuild_submitted_response_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "causes", "message" ],
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
    }
  },
  "description" : "Rebuild Initiated"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "RebuildSubmittedResponse": _rebuild_submitted_response_model_schema
})

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

_remove_function_query_v2_model_schema = json.loads(
    r"""{
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
      "description" : "If <code>true</code>, the function version will be immediately undeployed and removed.\n\nOtherwise, the removal will be delayed to allow current invocations to end. During that period, the function is marked _deprecated_."
    },
    "undeploy" : {
      "type" : "boolean",
      "description" : "If `true`, the `DELETE` operation\n* undeploys the (openfaas) function: it becomes no longer available for invocation.\n* does NOT remove the function from registry: it stays in an `undeployed` status.  All assets and definitions are retained, so the version can be restored later with a  _rebuild_ action.\n\nIf `false`, the `DELETE` operation\n* _only_ marks the plug function as _deprecated_, the function remains active but is removed from the default listings.   This also applies to _draft_ versions.\n\nThis parameter is incompatible with `force=true`.\n\nIf not set the default behaviour applies:\n* _draft_ versions are _undeployed_ and _removed_ from registry.\n* non-_draft_ versions are marked _deprecated_ only."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "RemoveFunctionQueryV2": _remove_function_query_v2_model_schema
})

_remove_plug_query_v2_model_schema = json.loads(
    r"""{
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
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RemovePlugQueryV2": _remove_plug_query_v2_model_schema})

_request_operation_model_schema = json.loads(
    r"""{
  "title" : "RequestOperation",
  "type" : "string",
  "description" : "A modifying operation on the function.",
  "enum" : [ "create", "metadata-update", "assets-update", "rebuild", "verify", "publish", "deprecate", "undeploy" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RequestOperation": _request_operation_model_schema})

_resource_limits_model_schema = json.loads(
    r"""{
  "title" : "ResourceLimits",
  "required" : [ "cpu", "memory" ],
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

_runtime_info_model_schema = json.loads(
    r"""{
  "required" : [ "archiveFormat", "functionType", "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string"
    },
    "functionType" : {
      "$ref" : "#/components/schemas/FunctionType"
    },
    "archiveFormat" : {
      "$ref" : "#/components/schemas/ArchiveFormat"
    }
  },
  "description" : "Runtime attributes that are the same for all versions of a runtime."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RuntimeInfo": _runtime_info_model_schema})

_runtime_name_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "description" : "If set, filters on the <code>name</code> of a runtime. Supports <code>*</code> and <code>?</code> wildcards and is case-insensitive.",
      "example" : "node*"
    },
    "functionType" : {
      "type" : "array",
      "description" : "If set, filters on the <code>functionType</code> of a runtime. Uses an exact match.",
      "example" : "plugs",
      "items" : {
        "$ref" : "#/components/schemas/FunctionType"
      }
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "If set, filters on the <code>archiveFormat</code> of a runtime. Uses an exact match.",
      "example" : "node",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RuntimeNameQuery": _runtime_name_query_model_schema})

_runtime_params_model_schema = json.loads(
    r"""{
  "required" : [ "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "$ref" : "#/components/schemas/Runtime"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RuntimeParams": _runtime_params_model_schema})

_runtime_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "latest" : {
      "$ref" : "#/components/schemas/LatestVersionLevel"
    },
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "If set to `true`, deprecated runtimes will be included in the query.",
      "default" : false
    },
    "name" : {
      "type" : "string",
      "description" : "If set, filters on the <code>name</code> of a runtime. Supports <code>*</code> and <code>?</code> wildcards and is case-insensitive.",
      "example" : "node*"
    },
    "functionType" : {
      "type" : "array",
      "description" : "If set, filters on the <code>functionType</code> of a runtime. Uses an exact match.",
      "example" : "plugs",
      "items" : {
        "$ref" : "#/components/schemas/FunctionType"
      }
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "If set, filters on the <code>archiveFormat</code> of a runtime. Uses an exact match.",
      "example" : "node",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RuntimeQuery": _runtime_query_model_schema})

_runtime_reference_model_schema = json.loads(
    r"""{
  "required" : [ "name", "version" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    }
  },
  "description" : "Reference to a runtime version."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RuntimeReference": _runtime_reference_model_schema})

_runtime_specification_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
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
      "type" : "array",
      "description" : "Description of dependencies provided by this runtime version.",
      "items" : {
        "$ref" : "#/components/schemas/ProvidedDependency"
      }
    },
    "assets" : {
      "$ref" : "#/components/schemas/AssetsConditions"
    },
    "deprecated" : {
      "type" : "boolean",
      "description" : "If true, this runtime should no longer be used for new functions."
    }
  },
  "description" : "Runtime (version) specification that says\n* what assets are required/allowed to build the function\n* what build parameters are used\n* what deployment parameters are used\n* which dependencies are provided by the runtime"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RuntimeSpecification": _runtime_specification_model_schema})

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

_runtime_summary_attrs_model_schema = json.loads(
    r"""{
  "required" : [ "archiveFormat", "functionType", "name", "title" ],
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
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RuntimeSummaryAttrs": _runtime_summary_attrs_model_schema})

_runtime_summary_response_model_schema = json.loads(
    r"""{
  "required" : [ "runtimes" ],
  "type" : "object",
  "properties" : {
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

_runtime_version_and_path_params_model_schema = json.loads(
    r"""{
  "required" : [ "*", "name", "version" ],
  "type" : "object",
  "properties" : {
    "*" : {
      "type" : "string",
      "description" : "Full path or path prefix of the asset within the archive"
    },
    "name" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "RuntimeVersionAndPathParams": _runtime_version_and_path_params_model_schema
})

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
    }
  },
  "description" : "A summary of a selected version for a runtime"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RuntimeVersionInfo": _runtime_version_info_model_schema})

_runtime_version_params_model_schema = json.loads(
    r"""{
  "required" : [ "name", "version" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RuntimeVersionParams": _runtime_version_params_model_schema})

_runtime_version_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "latest" : {
      "$ref" : "#/components/schemas/LatestVersionLevel"
    },
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "If set to `true`, deprecated runtimes will be included in the query.",
      "default" : false
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RuntimeVersionQuery": _runtime_version_query_model_schema})

_runtime_version_response_model_schema = json.loads(
    r"""{
  "required" : [ "runtime" ],
  "type" : "object",
  "properties" : {
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

_runtime_version_specification_model_schema = json.loads(
    r"""{
  "required" : [ "title", "version" ],
  "type" : "object",
  "properties" : {
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
      "type" : "array",
      "description" : "Description of dependencies provided by this runtime version.",
      "items" : {
        "$ref" : "#/components/schemas/ProvidedDependency"
      }
    },
    "assets" : {
      "$ref" : "#/components/schemas/AssetsConditions"
    },
    "deprecated" : {
      "type" : "boolean",
      "description" : "If true, this runtime should no longer be used for new functions."
    },
    "title" : {
      "type" : "string"
    },
    "description" : {
      "type" : "string"
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "RuntimeVersionSpecification": _runtime_version_specification_model_schema
})

_runtime_version_status_model_schema = json.loads(
    r"""{
  "required" : [ "deprecated", "upgradable" ],
  "type" : "object",
  "properties" : {
    "deprecated" : {
      "type" : "boolean",
      "description" : "If true, the function uses a deprecated runtime."
    },
    "upgradable" : {
      "type" : "boolean",
      "description" : "If true, a newer runtime for this function is available using the `rebuild` API."
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"RuntimeVersionStatus": _runtime_version_status_model_schema})

_runtime_version_summary_model_schema = json.loads(
    r"""{
  "required" : [ "archiveFormat", "deprecated", "functionType", "name", "title", "upgradable", "version" ],
  "type" : "object",
  "properties" : {
    "deprecated" : {
      "type" : "boolean",
      "description" : "If true, the function uses a deprecated runtime."
    },
    "upgradable" : {
      "type" : "boolean",
      "description" : "If true, a newer runtime for this function is available using the `rebuild` API."
    },
    "version" : {
      "$ref" : "#/components/schemas/SemanticVersion"
    },
    "title" : {
      "type" : "string"
    },
    "description" : {
      "type" : "string"
    },
    "name" : {
      "$ref" : "#/components/schemas/Runtime"
    },
    "functionType" : {
      "$ref" : "#/components/schemas/FunctionType"
    },
    "archiveFormat" : {
      "$ref" : "#/components/schemas/ArchiveFormat"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "RuntimeVersionSummary": _runtime_version_summary_model_schema
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
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp of creation of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user that created this job"
    },
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "Request operation"
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
  "required" : [ "_links", "createdAt", "createdBy", "id", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/Scale_type"
    },
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "The operation name for the background task."
    },
    "id" : {
      "title" : "id",
      "type" : "string",
      "description" : "The id of the background job, or the constant `_unknown_`"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The creation time of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user that initiated this job"
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
  "required" : [ "endpoint", "namespace", "replicas", "runtimeName", "runtimeVersion" ],
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
    "createdAt" : {
      "type" : "string",
      "description" : "The timestamp of creation of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "The user that created this job"
    },
    "operation" : {
      "type" : "string",
      "description" : "Request operation"
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

_schema_by_id_params_model_schema = json.loads(
    r"""{
  "required" : [ "schemaId" ],
  "type" : "object",
  "properties" : {
    "schemaId" : {
      "type" : "string",
      "description" : "Schema id"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SchemaByIdParams": _schema_by_id_params_model_schema})

_schema_params_model_schema = json.loads(
    r"""{
  "required" : [ "functionType", "role" ],
  "type" : "object",
  "properties" : {
    "functionType" : {
      "$ref" : "#/components/schemas/FunctionType"
    },
    "role" : {
      "$ref" : "#/components/schemas/AssetRole"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SchemaParams": _schema_params_model_schema})

_semantic_version_range_model_schema = json.loads(
    r"""{
  "title" : "SemanticVersionRange",
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

_status_model_schema = json.loads(
    r"""{
  "title" : "Status",
  "type" : "string",
  "description" : "Status for a deployed function.",
  "enum" : [ "registered", "running", "pending", "deployed", "unhealthy", "killed", "failed", "undeploying", "undeployed" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Status": _status_model_schema})

_status_any_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Includes *all* statuses (including `undeployed`) as a filter",
  "enum" : [ "any" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"StatusAny": _status_any_model_schema})

_status_filter_model_schema = json.loads(
    r"""{
  "description" : "Inclusion or exclusion filter on the `status` property.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/StatusInclude"
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

_status_include_model_schema = json.loads(
    r"""{
  "type" : "string",
  "description" : "Inlude a status as a filter.",
  "example" : "running",
  "enum" : [ "registered", "running", "pending", "deployed", "unhealthy", "failed", "undeploying", "undeployed" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"StatusInclude": _status_include_model_schema})

_status_response_model_schema = json.loads(
    r"""{
  "required" : [ "statusCode" ],
  "type" : "object",
  "properties" : {
    "statusCode" : {
      "type" : "number"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"StatusResponse": _status_response_model_schema})

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

_supported_events_model_schema = json.loads(
    r"""{
  "title" : "SupportedEvents",
  "type" : "string",
  "enum" : [ "completed", "failed", "active", "delayed", "waiting", "waiting-children" ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"SupportedEvents": _supported_events_model_schema})

_tag_model_schema = json.loads(
    r"""{
  "title" : "Tag",
  "required" : [ "color", "name" ],
  "type" : "object",
  "properties" : {
    "name" : {
      "title" : "name",
      "type" : "string",
      "description" : "Name of the tag"
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

_tag_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "name" : {
      "type" : "string",
      "description" : "If set, filters on the <code>name</code> of a tag. Supports <code>*</code> and <code>?</code> wildcards and is case-insensitive.",
      "example" : "*-demo-??"
    },
    "color" : {
      "type" : "string",
      "description" : "If set, filters on the <code>color</code> of a tag. Uses an exact match.",
      "example" : "#4153ea"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TagQuery": _tag_query_model_schema})

_tags_filter_model_schema = json.loads(
    r"""{
  "title" : "TagsFilter",
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

_tags_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "tags" : {
      "$ref" : "#/components/schemas/TagsFilter"
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"TagsQuery": _tags_query_model_schema})

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
  "title" : "TimestampSpec",
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
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp of creation of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user that created this job"
    },
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "Request operation"
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
  "required" : [ "_links", "createdAt", "createdBy", "id", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/Undeploy_type"
    },
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "The operation name for the background task."
    },
    "id" : {
      "title" : "id",
      "type" : "string",
      "description" : "The id of the background job, or the constant `_unknown_`"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The creation time of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user that initiated this job"
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
  "required" : [ "deleteEntity", "endpoint", "isNativePlug", "namespace", "runtimeName", "runtimeVersion" ],
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
    "isNativePlug" : {
      "title" : "isNativePlug",
      "type" : "boolean",
      "description" : "If true, the function is not expected to be deployed on openfaas."
    },
    "deleteEntity" : {
      "title" : "deleteEntity",
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
    "createdAt" : {
      "type" : "string",
      "description" : "The timestamp of creation of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "The user that created this job"
    },
    "operation" : {
      "type" : "string",
      "description" : "Request operation"
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
  "required" : [ "assets", "deployment", "registration" ],
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
      "description" : "The versions that where deprecated, undeployed and/or removed.",
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

_unhealthy_invokable_webscript_error_model_schema = json.loads(
    r"""{
  "required" : [ "_links", "code", "entity", "error" ],
  "type" : "object",
  "properties" : {
    "entity" : {
      "$ref" : "#/components/schemas/InvokableWebscriptResponse_entity"
    },
    "_links" : {
      "$ref" : "#/components/schemas/InvokeInternalHALLink"
    },
    "error" : {
      "type" : "string"
    },
    "code" : {
      "type" : "string"
    }
  },
  "description" : "Webscript Not Healthy"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "UnhealthyInvokableWebscriptError": _unhealthy_invokable_webscript_error_model_schema
})

_update_comment_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "comment" : {
      "type" : "string",
      "description" : "An optional user-specified comment corresponding to the operation."
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"UpdateComment": _update_comment_model_schema})

_update_draft_query_model_schema = json.loads(
    r"""{
  "required" : [ "chown" ],
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
    "chown" : {
      "type" : "boolean",
      "description" : "If set, ownership of the draft function is transferred to the current user.",
      "default" : false
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"UpdateDraftQuery": _update_draft_query_model_schema})

_update_metadata_request_v1_model_schema = json.loads(
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
    "tags" : {
      "type" : "array",
      "description" : "Tags associated with this function.",
      "example" : [ {
        "name" : "awaiting-review",
        "color" : "#4153ea"
      }, {
        "name" : "demo",
        "color" : "#e639a4"
      } ],
      "items" : {
        "$ref" : "#/components/schemas/Tag"
      }
    },
    "friendlyName" : {
      "type" : "string",
      "description" : "Display title for this function."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "UpdateMetadataRequestV1": _update_metadata_request_v1_model_schema
})

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
    "documentationURL" : {
      "type" : "string",
      "description" : "External url that document this function."
    },
    "tags" : {
      "type" : "array",
      "description" : "Tags associated with this function.",
      "example" : [ {
        "name" : "awaiting-review",
        "color" : "#4153ea"
      }, {
        "name" : "demo",
        "color" : "#e639a4"
      } ],
      "items" : {
        "$ref" : "#/components/schemas/Tag"
      }
    },
    "friendlyName" : {
      "type" : "string",
      "description" : "Display title for this function."
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

_user_plug_meta_model_schema = json.loads(
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
    "tags" : {
      "type" : "array",
      "description" : "Tags associated with this function.",
      "example" : [ {
        "name" : "awaiting-review",
        "color" : "#4153ea"
      }, {
        "name" : "demo",
        "color" : "#e639a4"
      } ],
      "items" : {
        "$ref" : "#/components/schemas/Tag"
      }
    },
    "friendlyName" : {
      "type" : "string",
      "description" : "Display title for this function."
    }
  },
  "description" : "Plug metadata that the user can update as `metadata`"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"UserPlugMeta": _user_plug_meta_model_schema})

_verify_model_schema = json.loads(
    r"""{
  "title" : "Verify",
  "required" : [ "createdAt", "createdBy", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/JobHALLinks"
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
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The timestamp of creation of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user that created this job"
    },
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "Request operation"
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
  "required" : [ "_links", "createdAt", "createdBy", "id", "operation", "state", "type" ],
  "type" : "object",
  "properties" : {
    "type" : {
      "$ref" : "#/components/schemas/Verify_type"
    },
    "operation" : {
      "title" : "operation",
      "type" : "string",
      "description" : "The operation name for the background task."
    },
    "id" : {
      "title" : "id",
      "type" : "string",
      "description" : "The id of the background job, or the constant `_unknown_`"
    },
    "state" : {
      "$ref" : "#/components/schemas/JobStateResult"
    },
    "createdAt" : {
      "title" : "createdAt",
      "type" : "string",
      "description" : "The creation time of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "title" : "createdBy",
      "type" : "string",
      "description" : "The user that initiated this job"
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
  "required" : [ "endpoint", "namespace", "runtimeName", "runtimeVersion" ],
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
    "createdAt" : {
      "type" : "string",
      "description" : "The timestamp of creation of this job",
      "format" : "date-time"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "The user that created this job"
    },
    "operation" : {
      "type" : "string",
      "description" : "Request operation"
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

_verify_query_v1_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "scaleToZero" : {
      "type" : "boolean",
      "description" : "Indicates whether the function needs to be scaled down after successful verification. If not set, the function is scaled to zero only if it was not active before this command."
    }
  },
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"VerifyQueryV1": _verify_query_v1_model_schema})

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

_version_includes_model_schema = json.loads(
    r"""{
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
  "additionalProperties" : false
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"VersionIncludes": _version_includes_model_schema})

_versions_query_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    },
    "page" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The number of pages to skip when returning result to this query."
    },
    "endpoint" : {
      "type" : "string",
      "description" : "Filter on the openfaas endpoint. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "imageName" : {
      "type" : "string",
      "description" : "Filter on the container image name. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "storageLocation" : {
      "type" : "string",
      "description" : "Filter on the storageLocation. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "deprecated" : {
      "type" : "boolean",
      "description" : "Filter on the deprecation status of the function."
    },
    "draft" : {
      "type" : "boolean",
      "description" : "Filter on the draft status of the function."
    },
    "nameVersion" : {
      "type" : "array",
      "description" : "Filter on exact `{name}@{version}` functions. Using this filter implies a `latest=false` default, returning multiple versions of the same named versions if they are filtered.",
      "items" : {
        "$ref" : "#/components/schemas/NamedVersion"
      }
    },
    "version" : {
      "type" : "string",
      "description" : "Filter on the version of the function (case-sensitive, supports wildcards)."
    },
    "status" : {
      "type" : "array",
      "description" : "Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions.",
      "items" : {
        "$ref" : "#/components/schemas/StatusFilter"
      }
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "createdBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "createdAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "name" : {
      "type" : "string",
      "description" : "Filter on the name of the function. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "Filter on the archive format of the function.",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    },
    "runtime" : {
      "type" : "array",
      "description" : "Filter on the runtime of the function.",
      "items" : {
        "$ref" : "#/components/schemas/Runtime"
      }
    }
  },
  "additionalProperties" : false,
  "description" : "Function versions paged query"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"VersionsQuery": _versions_query_model_schema})

_versions_query_v2_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    },
    "page" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The number of pages to skip when returning result to this query."
    },
    "endpoint" : {
      "type" : "string",
      "description" : "Filter on the openfaas endpoint. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "imageName" : {
      "type" : "string",
      "description" : "Filter on the container image name. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "storageLocation" : {
      "type" : "string",
      "description" : "Filter on the storageLocation. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "deprecated" : {
      "type" : "boolean",
      "description" : "Filter on the deprecation status of the function."
    },
    "draft" : {
      "type" : "boolean",
      "description" : "Filter on the draft status of the function."
    },
    "nameVersion" : {
      "type" : "array",
      "description" : "Filter on exact `{name}@{version}` functions. Using this filter implies a `latest=false` default, returning multiple versions of the same named versions if they are filtered.",
      "items" : {
        "$ref" : "#/components/schemas/NamedVersion"
      }
    },
    "version" : {
      "type" : "string",
      "description" : "Filter on the version of the function (case-sensitive, supports wildcards)."
    },
    "status" : {
      "type" : "array",
      "description" : "Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions.",
      "items" : {
        "$ref" : "#/components/schemas/StatusFilter"
      }
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "createdBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "createdAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "name" : {
      "type" : "string",
      "description" : "Filter on the name of the function. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "Filter on the archive format of the function.",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    },
    "runtime" : {
      "type" : "array",
      "description" : "Filter on the runtime of the function.",
      "items" : {
        "$ref" : "#/components/schemas/Runtime"
      }
    }
  },
  "additionalProperties" : false,
  "description" : "Function versions paged query"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"VersionsQueryV2": _versions_query_v2_model_schema})

_versions_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "count", "entities" ],
  "type" : "object",
  "properties" : {
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
        "$ref" : "#/components/schemas/AnyFunctionResponse"
      }
    }
  },
  "description" : "Version Listing Response"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"VersionsResponseV2": _versions_response_v2_model_schema})

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
      "$ref" : "#/components/schemas/HALLink"
    },
    "webscript" : {
      "$ref" : "#/components/schemas/HALLink"
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
      "$ref" : "#/components/schemas/HALLink"
    },
    "job" : {
      "$ref" : "#/components/schemas/HALLink"
    },
    "webscript" : {
      "$ref" : "#/components/schemas/HALLink"
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
      "$ref" : "#/components/schemas/HALLink"
    },
    "webscript" : {
      "$ref" : "#/components/schemas/HALLink"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"Webscript_2": _webscript_2_model_schema})

_webscript_latest_version_query_v2_model_schema = json.loads(
    r"""{
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
  "description" : "Webscript latest named version query."
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "WebscriptLatestVersionQueryV2": _webscript_latest_version_query_v2_model_schema
})

_webscript_latest_versions_query_v1_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "limit" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The maximum number of items to be return from this query. Has a deployment-defined default and maximum value."
    },
    "page" : {
      "minimum" : 0,
      "type" : "number",
      "description" : "The number of pages to skip when returning result to this query."
    },
    "includeDraft" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**."
    },
    "includeDeprecated" : {
      "type" : "boolean",
      "description" : "Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**."
    },
    "version" : {
      "type" : "string",
      "description" : "Filter on the version of the function (case-sensitive, supports wildcards)."
    },
    "status" : {
      "type" : "array",
      "description" : "Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions.",
      "items" : {
        "$ref" : "#/components/schemas/StatusFilter"
      }
    },
    "runtimeVersion" : {
      "$ref" : "#/components/schemas/SemanticVersionRange"
    },
    "createdBy" : {
      "type" : "string",
      "description" : "Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "updatedBy" : {
      "type" : "string",
      "description" : "Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs.",
      "example" : "@me"
    },
    "createdBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "createdAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedBefore" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "updatedAfter" : {
      "$ref" : "#/components/schemas/TimestampSpec"
    },
    "name" : {
      "type" : "string",
      "description" : "Filter on the name of the function. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters)."
    },
    "archiveFormat" : {
      "type" : "array",
      "description" : "Filter on the archive format of the function.",
      "items" : {
        "$ref" : "#/components/schemas/ArchiveFormat"
      }
    },
    "runtime" : {
      "type" : "array",
      "description" : "Filter on the runtime of the function.",
      "items" : {
        "$ref" : "#/components/schemas/Runtime"
      }
    }
  },
  "additionalProperties" : false,
  "description" : "Webscript lastest versions listing query"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "WebscriptLatestVersionsQueryV1": _webscript_latest_versions_query_v1_model_schema
})

_webscript_latest_versions_query_v2_model_schema = json.loads(
    r"""{
  "description" : "Webscript lastest versions listing query.",
  "anyOf" : [ {
    "$ref" : "#/components/schemas/LatestFunctionVersionsQuery"
  }, {
    "$ref" : "#/components/schemas/LatestFunctionsQuery"
  } ]
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({
    "WebscriptLatestVersionsQueryV2": _webscript_latest_versions_query_v2_model_schema
})

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

_webscript_response_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "metadata", "name", "runtime", "secret", "status", "updatedAt", "updatedBy", "version" ],
  "type" : "object",
  "properties" : {
    "deploy" : {
      "$ref" : "#/components/schemas/FunctionDeployOverridesType"
    },
    "name" : {
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
    "status" : {
      "$ref" : "#/components/schemas/Status"
    },
    "failureReason" : {
      "$ref" : "#/components/schemas/FailureReason"
    },
    "_links" : {
      "type" : "array",
      "description" : "Links to related entities.",
      "items" : {
        "$ref" : "#/components/schemas/JobHALLinks"
      }
    },
    "secret" : {
      "type" : "string",
      "nullable" : true
    }
  },
  "description" : "Successful Response"
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"WebscriptResponse": _webscript_response_model_schema})

_webscript_response_v2_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "deprecated", "draft", "runtime", "status", "updatedAt", "updatedBy", "updates", "webscript" ],
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
      "description" : "The audit logs corresponding to the latest modifying operations on this entity.",
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
  "required" : [ "createdAt", "createdBy", "deprecated", "draft", "runtime", "status", "updatedAt", "updatedBy", "updates", "webscript" ],
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
      "description" : "The audit logs corresponding to the latest modifying operations on this entity.",
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

_with_asset_hal_link_model_schema = json.loads(
    r"""{
  "required" : [ "_links" ],
  "type" : "object",
  "properties" : {
    "_links" : {
      "$ref" : "#/components/schemas/AssetSummaryWithHALLink__links"
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"WithAssetHALLink": _with_asset_hal_link_model_schema})

_with_entity_attributes_model_schema = json.loads(
    r"""{
  "required" : [ "createdAt", "createdBy", "deprecated", "draft", "runtime", "status", "updatedAt", "updatedBy", "updates" ],
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
      "description" : "The audit logs corresponding to the latest modifying operations on this entity.",
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
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"WithEntityAttributes": _with_entity_attributes_model_schema})

_with_limit_model_schema = json.loads(
    r"""{
  "type" : "object",
  "properties" : {
    "limit" : {
      "type" : "number",
      "description" : "The page size used for this query result."
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"WithLimit": _with_limit_model_schema})

_with_paging_model_schema = json.loads(
    r"""{
  "required" : [ "count" ],
  "type" : "object",
  "properties" : {
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
    }
  }
}
""",
    object_hook=with_example_provider,
)
MODEL_DEFINITIONS.update({"WithPaging": _with_paging_model_schema})
