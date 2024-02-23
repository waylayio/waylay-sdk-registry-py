# MessageAndStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**status_code** | **float** |  | 

## Example

```python
from waylay.services.registry.models.message_and_status_response import MessageAndStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageAndStatusResponse from a JSON string
message_and_status_response_instance = MessageAndStatusResponse.from_json(json)
# print the JSON string representation of the object
print MessageAndStatusResponse.to_json()

# convert the object into a dict
message_and_status_response_dict = message_and_status_response_instance.to_dict()
# create an instance of MessageAndStatusResponse from a dict
message_and_status_response_form_dict = message_and_status_response.from_dict(message_and_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


