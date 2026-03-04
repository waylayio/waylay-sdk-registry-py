# ActiveEventSSE

A message that notifies a state change in a background job.

**Source:** `waylay.services.registry.models.active_event_sse`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**ActiveEventSSEEvent**](ActiveEventSSEEvent.md) |  | 
**data** | [**JobEventResponseActiveEventData**](JobEventResponseActiveEventData.md) |  | 


## Example

```python
from waylay.services.registry.models.active_event_sse import ActiveEventSSE

active_event_sse = ActiveEventSSE(event=..., data=...)

# Create from JSON
active_event_sse = ActiveEventSSE.from_json('{ "event": ..., "data": ... }')

# Export to dictionary
active_event_sse_dict = active_event_sse.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


