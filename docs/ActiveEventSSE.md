# ActiveEventSSE

A message that notifies a state change in a background job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**ActiveEventSSEEvent**](ActiveEventSSEEvent.md) |  | 
**data** | [**JobEventResponseActiveEventData**](JobEventResponseActiveEventData.md) |  | 

## Example

```python
from waylay.services.registry.models.active_event_sse import ActiveEventSSE

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveEventSSE from a JSON string
active_event_sse_instance = ActiveEventSSE.from_json(json)
# print the JSON string representation of the object
print ActiveEventSSE.to_json()

# convert the object into a dict
active_event_sse_dict = active_event_sse_instance.to_dict()
# create an instance of ActiveEventSSE from a dict
active_event_sse_form_dict = active_event_sse.from_dict(active_event_sse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


