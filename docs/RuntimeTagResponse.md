# RuntimeTagResponse

Runtime Tag Found

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | [**RuntimeTag**](RuntimeTag.md) |  | 

## Example

```python
from waylay.services.registry.models.runtime_tag_response import RuntimeTagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeTagResponse from a JSON string
runtime_tag_response_instance = RuntimeTagResponse.from_json(json)
# print the JSON string representation of the object
print RuntimeTagResponse.to_json()

# convert the object into a dict
runtime_tag_response_dict = runtime_tag_response_instance.to_dict()
# create an instance of RuntimeTagResponse from a dict
runtime_tag_response_form_dict = runtime_tag_response.from_dict(runtime_tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


