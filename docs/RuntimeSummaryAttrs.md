# RuntimeSummaryAttrs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**function_type** | [**FunctionType**](FunctionType.md) |  | 
**archive_format** | [**ArchiveFormat**](ArchiveFormat.md) |  | 

## Example

```python
from waylay.services.registry.models.runtime_summary_attrs import RuntimeSummaryAttrs

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeSummaryAttrs from a JSON string
runtime_summary_attrs_instance = RuntimeSummaryAttrs.from_json(json)
# print the JSON string representation of the object
print RuntimeSummaryAttrs.to_json()

# convert the object into a dict
runtime_summary_attrs_dict = runtime_summary_attrs_instance.to_dict()
# create an instance of RuntimeSummaryAttrs from a dict
runtime_summary_attrs_form_dict = runtime_summary_attrs.from_dict(runtime_summary_attrs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


