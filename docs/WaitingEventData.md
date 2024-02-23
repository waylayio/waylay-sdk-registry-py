# WaitingEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev** | [**QueueEvents**](QueueEvents.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.waiting_event_data import WaitingEventData

# TODO update the JSON string below
json = "{}"
# create an instance of WaitingEventData from a JSON string
waiting_event_data_instance = WaitingEventData.from_json(json)
# print the JSON string representation of the object
print WaitingEventData.to_json()

# convert the object into a dict
waiting_event_data_dict = waiting_event_data_instance.to_dict()
# create an instance of WaitingEventData from a dict
waiting_event_data_form_dict = waiting_event_data.from_dict(waiting_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


