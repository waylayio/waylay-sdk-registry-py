# CompletedEventSSE

A message that notifies a state change in a background job.

**Source:** `waylay.services.registry.models.completed_event_sse`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**CompletedEventSSEEvent**](CompletedEventSSEEvent.md) |  | 
**data** | [**JobEventResponseCompletedEventData**](JobEventResponseCompletedEventData.md) |  | 


## Example

```python
from waylay.services.registry.models.completed_event_sse import CompletedEventSSE

completed_event_sse = CompletedEventSSE(event=..., data=...)

# Create from JSON
completed_event_sse = CompletedEventSSE.from_json('{ "event": ..., "data": ... }')

# Export to dictionary
completed_event_sse_dict = completed_event_sse.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


