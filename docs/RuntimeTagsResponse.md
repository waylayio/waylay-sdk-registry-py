# RuntimeTagsResponse

Runtime Tags Found

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[RuntimeTag]**](RuntimeTag.md) |  | 

## Example

```python
from waylay.services.registry.models.runtime_tags_response import RuntimeTagsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeTagsResponse from a JSON string
runtime_tags_response_instance = RuntimeTagsResponse.from_json(json)
# print the JSON string representation of the object
print RuntimeTagsResponse.to_json()

# convert the object into a dict
runtime_tags_response_dict = runtime_tags_response_instance.to_dict()
# create an instance of RuntimeTagsResponse from a dict
runtime_tags_response_form_dict = runtime_tags_response.from_dict(runtime_tags_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


