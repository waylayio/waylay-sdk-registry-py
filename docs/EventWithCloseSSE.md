# EventWithCloseSSE

SSE stream events with closing protocol

**Source:** `waylay.services.registry.models.event_with_close_sse`



## Union Type (Any Of)

This type allows any of the following:

Type | Description
------------ | -------------
[**StreamReady**](StreamReady.md) | -
[**JobEventSSE**](JobEventSSE.md) | -
[**KeepAliveEventSSE**](KeepAliveEventSSE.md) | -
[**StreamClosing**](StreamClosing.md) | -

## Example

```python
from waylay.services.registry.models.event_with_close_sse import EventWithCloseSSE

# Use any of the accepted types (see table above)
my_event_with_close_sse: EventWithCloseSSE = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


