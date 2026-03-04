# DelayedEventSSE

A message that notifies a state change in a background job.

**Source:** `waylay.services.registry.models.delayed_event_sse`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**DelayedEventSSEEvent**](DelayedEventSSEEvent.md) |  | 
**data** | [**JobEventResponseDelayedEventData**](JobEventResponseDelayedEventData.md) |  | 


## Example

```python
from waylay.services.registry.models.delayed_event_sse import DelayedEventSSE

delayed_event_sse = DelayedEventSSE(event=..., data=...)

# Create from JSON
delayed_event_sse = DelayedEventSSE.from_json('{ "event": ..., "data": ... }')

# Export to dictionary
delayed_event_sse_dict = delayed_event_sse.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


