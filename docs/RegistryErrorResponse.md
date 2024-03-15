# RegistryErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**code** | **str** |  | 
**status_code** | **float** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from waylay.services.registry.models.registry_error_response import RegistryErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryErrorResponse from a JSON string
registry_error_response_instance = RegistryErrorResponse.from_json(json)
# print the JSON string representation of the object
print RegistryErrorResponse.to_json()

# convert the object into a dict
registry_error_response_dict = registry_error_response_instance.to_dict()
# create an instance of RegistryErrorResponse from a dict
registry_error_response_form_dict = registry_error_response.from_dict(registry_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


