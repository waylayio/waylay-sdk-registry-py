# ErrorAndStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**status_code** | **float** |  | 

## Example

```python
from waylay.services.registry.models.error_and_status_response import ErrorAndStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorAndStatusResponse from a JSON string
error_and_status_response_instance = ErrorAndStatusResponse.from_json(json)
# print the JSON string representation of the object
print ErrorAndStatusResponse.to_json()

# convert the object into a dict
error_and_status_response_dict = error_and_status_response_instance.to_dict()
# create an instance of ErrorAndStatusResponse from a dict
error_and_status_response_form_dict = error_and_status_response.from_dict(error_and_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


