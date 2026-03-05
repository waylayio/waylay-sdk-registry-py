# KeepAliveEventSSE

A message that acknowledges that the stream is still alive.

**Source:** `waylay.services.registry.models.keep_alive_event_sse`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**EventKeepAlive**](EventKeepAlive.md) |  | 
**data** | **str** | A text message acknowledging that events will be forwarded. | [optional] 


## Example

```python
from waylay.services.registry.models.keep_alive_event_sse import KeepAliveEventSSE

keep_alive_event_sse = KeepAliveEventSSE(event=..., data=...)

# Create from JSON
keep_alive_event_sse = KeepAliveEventSSE.from_json('{ "event": ..., "data": ... }')

# Export to dictionary
keep_alive_event_sse_dict = keep_alive_event_sse.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


