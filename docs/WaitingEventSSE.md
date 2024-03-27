# WaitingEventSSE

A message that notifies a state change in a background job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**WaitingEventSSEEvent**](WaitingEventSSEEvent.md) |  | 
**data** | [**JobEventResponseWaitingEventData**](JobEventResponseWaitingEventData.md) |  | 

## Example

```python
from waylay.services.registry.models.waiting_event_sse import WaitingEventSSE

# TODO update the JSON string below
json = "{}"
# create an instance of WaitingEventSSE from a JSON string
waiting_event_sse_instance = WaitingEventSSE.from_json(json)
# print the JSON string representation of the object
print WaitingEventSSE.to_json()

# convert the object into a dict
waiting_event_sse_dict = waiting_event_sse_instance.to_dict()
# create an instance of WaitingEventSSE from a dict
waiting_event_sse_form_dict = waiting_event_sse.from_dict(waiting_event_sse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


