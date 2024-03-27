# WaitingChildrenEventSSE

A message that notifies a state change in a background job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**WaitingChildrenEventSSEEvent**](WaitingChildrenEventSSEEvent.md) |  | 
**data** | [**JobEventResponseWaitingChildrenEventData**](JobEventResponseWaitingChildrenEventData.md) |  | 

## Example

```python
from waylay.services.registry.models.waiting_children_event_sse import WaitingChildrenEventSSE

# TODO update the JSON string below
json = "{}"
# create an instance of WaitingChildrenEventSSE from a JSON string
waiting_children_event_sse_instance = WaitingChildrenEventSSE.from_json(json)
# print the JSON string representation of the object
print WaitingChildrenEventSSE.to_json()

# convert the object into a dict
waiting_children_event_sse_dict = waiting_children_event_sse_instance.to_dict()
# create an instance of WaitingChildrenEventSSE from a dict
waiting_children_event_sse_form_dict = waiting_children_event_sse.from_dict(waiting_children_event_sse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


