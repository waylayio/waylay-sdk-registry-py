# StreamClosing

A message that notifies that the server will not send more events, and that the client should close.

**Source:** `waylay.services.registry.models.stream_closing`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**EventClose**](EventClose.md) |  | 
**data** | **str** | A text message describing the cause for closing the stream. | 


## Example

```python
from waylay.services.registry.models.stream_closing import StreamClosing

stream_closing = StreamClosing(event=..., data=...)

# Create from JSON
stream_closing = StreamClosing.from_json('{ "event": ..., "data": ... }')

# Export to dictionary
stream_closing_dict = stream_closing.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


