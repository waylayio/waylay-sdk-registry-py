# FailedEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev** | [**QueueEvents**](QueueEvents.md) |  | [optional] 
**failed_reason** | **str** | The failure reason of the job | 

## Example

```python
from waylay.services.registry.models.failed_event_data import FailedEventData

# TODO update the JSON string below
json = "{}"
# create an instance of FailedEventData from a JSON string
failed_event_data_instance = FailedEventData.from_json(json)
# print the JSON string representation of the object
print FailedEventData.to_json()

# convert the object into a dict
failed_event_data_dict = failed_event_data_instance.to_dict()
# create an instance of FailedEventData from a dict
failed_event_data_form_dict = failed_event_data.from_dict(failed_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


