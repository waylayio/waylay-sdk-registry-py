# FunctionTagResponse

Function Tag Found

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | [**Tag**](Tag.md) |  | 

## Example

```python
from waylay.services.registry.models.function_tag_response import FunctionTagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionTagResponse from a JSON string
function_tag_response_instance = FunctionTagResponse.from_json(json)
# print the JSON string representation of the object
print FunctionTagResponse.to_json()

# convert the object into a dict
function_tag_response_dict = function_tag_response_instance.to_dict()
# create an instance of FunctionTagResponse from a dict
function_tag_response_form_dict = function_tag_response.from_dict(function_tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


