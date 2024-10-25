# FunctionTagsResponse

Function Tags Found

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[Tag]**](Tag.md) |  | 

## Example

```python
from waylay.services.registry.models.function_tags_response import FunctionTagsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionTagsResponse from a JSON string
function_tags_response_instance = FunctionTagsResponse.from_json(json)
# print the JSON string representation of the object
print FunctionTagsResponse.to_json()

# convert the object into a dict
function_tags_response_dict = function_tags_response_instance.to_dict()
# create an instance of FunctionTagsResponse from a dict
function_tags_response_form_dict = function_tags_response.from_dict(function_tags_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


