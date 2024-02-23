# FailureReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log** | **List[str]** | Log lines associated with this failure. | 
**events** | **List[str]** | Events associated with this failure. | 
**cause** | **str** | Main cause for the failure. | [optional] 

## Example

```python
from waylay.services.registry.models.failure_reason import FailureReason

# TODO update the JSON string below
json = "{}"
# create an instance of FailureReason from a JSON string
failure_reason_instance = FailureReason.from_json(json)
# print the JSON string representation of the object
print FailureReason.to_json()

# convert the object into a dict
failure_reason_dict = failure_reason_instance.to_dict()
# create an instance of FailureReason from a dict
failure_reason_form_dict = failure_reason.from_dict(failure_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


