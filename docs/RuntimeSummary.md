# RuntimeSummary

A summary representation of the runtime, and (selected) versions of it.

**Source:** `waylay.services.registry.models.runtime_summary`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**function_type** | [**FunctionType**](FunctionType.md) |  | 
**archive_format** | [**ArchiveFormat**](ArchiveFormat.md) |  | 
**tags** | **List[str]** |  | [optional] 
**versions** | [**List[RuntimeVersionInfo]**](RuntimeVersionInfo.md) |  | 


## Example

```python
from waylay.services.registry.models.runtime_summary import RuntimeSummary

runtime_summary = RuntimeSummary(
    name=...,
    title=...,
    description=...,
    function_type=...,
    archive_format=...,
    tags=...,
    versions=...,
)

# Create from JSON
runtime_summary = RuntimeSummary.from_json(
    '{ "name": ..., "title": ..., "description": ..., "functionType": ..., "archiveFormat": ..., "tags": ..., "versions": ... }'
)

# Export to dictionary
runtime_summary_dict = runtime_summary.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


