# FailedEventSSE

A message that notifies a state change in a background job.

**Source:** `waylay.services.registry.models.failed_event_sse`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**FailedEventSSEEvent**](FailedEventSSEEvent.md) |  | 
**data** | [**JobEventResponseFailedEventData**](JobEventResponseFailedEventData.md) |  | 


## Example

```python
from waylay.services.registry.models.failed_event_sse import FailedEventSSE

failed_event_sse = FailedEventSSE(event=..., data=...)

# Create from JSON
failed_event_sse = FailedEventSSE.from_json('{ "event": ..., "data": ... }')

# Export to dictionary
failed_event_sse_dict = failed_event_sse.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


