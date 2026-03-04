# WaitingEventSSE

A message that notifies a state change in a background job.

**Source:** `waylay.services.registry.models.waiting_event_sse`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**WaitingEventSSEEvent**](WaitingEventSSEEvent.md) |  | 
**data** | [**JobEventResponseWaitingEventData**](JobEventResponseWaitingEventData.md) |  | 


## Example

```python
from waylay.services.registry.models.waiting_event_sse import WaitingEventSSE

waiting_event_sse = WaitingEventSSE(event=..., data=...)

# Create from JSON
waiting_event_sse = WaitingEventSSE.from_json('{ "event": ..., "data": ... }')

# Export to dictionary
waiting_event_sse_dict = waiting_event_sse.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


