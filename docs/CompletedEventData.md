# CompletedEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev** | [**QueueEvents**](QueueEvents.md) |  | [optional] 
**returnvalue** | [**AnyJobResult**](AnyJobResult.md) |  | 

## Example

```python
from waylay.services.registry.models.completed_event_data import CompletedEventData

# TODO update the JSON string below
json = "{}"
# create an instance of CompletedEventData from a JSON string
completed_event_data_instance = CompletedEventData.from_json(json)
# print the JSON string representation of the object
print CompletedEventData.to_json()

# convert the object into a dict
completed_event_data_dict = completed_event_data_instance.to_dict()
# create an instance of CompletedEventData from a dict
completed_event_data_form_dict = completed_event_data.from_dict(completed_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


