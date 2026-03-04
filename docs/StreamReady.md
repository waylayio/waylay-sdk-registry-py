# StreamReady

A message that acknowledges that the server will sent job state changes.

**Source:** `waylay.services.registry.models.stream_ready`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**EventAck**](EventAck.md) |  | 
**data** | **str** | A text message acknowledging what events will be forwarded. | 


## Example

```python
from waylay.services.registry.models.stream_ready import StreamReady

stream_ready = StreamReady(event=..., data=...)

# Create from JSON
stream_ready = StreamReady.from_json('{ "event": ..., "data": ... }')

# Export to dictionary
stream_ready_dict = stream_ready.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


