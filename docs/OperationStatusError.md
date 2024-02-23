# OperationStatusError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**message** | **str** |  | 
**stack** | **str** |  | [optional] 
**code** | **str** |  | 

## Example

```python
from waylay.services.registry.models.operation_status_error import OperationStatusError

# TODO update the JSON string below
json = "{}"
# create an instance of OperationStatusError from a JSON string
operation_status_error_instance = OperationStatusError.from_json(json)
# print the JSON string representation of the object
print OperationStatusError.to_json()

# convert the object into a dict
operation_status_error_dict = operation_status_error_instance.to_dict()
# create an instance of OperationStatusError from a dict
operation_status_error_form_dict = operation_status_error.from_dict(operation_status_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


