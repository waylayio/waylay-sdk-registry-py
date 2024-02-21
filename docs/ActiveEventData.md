# ActiveEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev** | [**QueueEvents**](QueueEvents.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.active_event_data import ActiveEventData

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveEventData from a JSON string
active_event_data_instance = ActiveEventData.from_json(json)
# print the JSON string representation of the object
print ActiveEventData.to_json()

# convert the object into a dict
active_event_data_dict = active_event_data_instance.to_dict()
# create an instance of ActiveEventData from a dict
active_event_data_form_dict = active_event_data.from_dict(active_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


