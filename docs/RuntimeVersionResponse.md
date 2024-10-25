# RuntimeVersionResponse

: Runtime Version Found

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**RuntimeSummaryResponseEmbedded**](RuntimeSummaryResponseEmbedded.md) |  | [optional] 
**runtime** | [**CompiledRuntimeVersion**](CompiledRuntimeVersion.md) |  | 

## Example

```python
from waylay.services.registry.models.runtime_version_response import RuntimeVersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeVersionResponse from a JSON string
runtime_version_response_instance = RuntimeVersionResponse.from_json(json)
# print the JSON string representation of the object
print RuntimeVersionResponse.to_json()

# convert the object into a dict
runtime_version_response_dict = runtime_version_response_instance.to_dict()
# create an instance of RuntimeVersionResponse from a dict
runtime_version_response_form_dict = runtime_version_response.from_dict(runtime_version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


