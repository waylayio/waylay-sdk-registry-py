# RuntimeSummary

A summary representation of the runtime, and (selected) versions of it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**function_type** | [**FunctionType**](FunctionType.md) |  | 
**archive_format** | [**ArchiveFormat**](ArchiveFormat.md) |  | 
**versions** | [**List[RuntimeVersionInfo]**](RuntimeVersionInfo.md) |  | 

## Example

```python
from waylay.services.registry.models.runtime_summary import RuntimeSummary

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeSummary from a JSON string
runtime_summary_instance = RuntimeSummary.from_json(json)
# print the JSON string representation of the object
print RuntimeSummary.to_json()

# convert the object into a dict
runtime_summary_dict = runtime_summary_instance.to_dict()
# create an instance of RuntimeSummary from a dict
runtime_summary_form_dict = runtime_summary.from_dict(runtime_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


