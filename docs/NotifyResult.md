# NotifyResult

The result data for a change notification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**RequestOperation**](RequestOperation.md) |  | 

## Example

```python
from waylay.services.registry.models.notify_result import NotifyResult

# TODO update the JSON string below
json = "{}"
# create an instance of NotifyResult from a JSON string
notify_result_instance = NotifyResult.from_json(json)
# print the JSON string representation of the object
print NotifyResult.to_json()

# convert the object into a dict
notify_result_dict = notify_result_instance.to_dict()
# create an instance of NotifyResult from a dict
notify_result_form_dict = notify_result.from_dict(notify_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


