# WaitingChildrenEventSSE

A message that notifies a state change in a background job.

**Source:** `waylay.services.registry.models.waiting_children_event_sse`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**WaitingChildrenEventSSEEvent**](WaitingChildrenEventSSEEvent.md) |  | 
**data** | [**JobEventResponseWaitingChildrenEventData**](JobEventResponseWaitingChildrenEventData.md) |  | 


## Example

```python
from waylay.services.registry.models.waiting_children_event_sse import (
    WaitingChildrenEventSSE,
)

waiting_children_event_sse = WaitingChildrenEventSSE(event=..., data=...)

# Create from JSON
waiting_children_event_sse = WaitingChildrenEventSSE.from_json(
    '{ "event": ..., "data": ... }'
)

# Export to dictionary
waiting_children_event_sse_dict = waiting_children_event_sse.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


