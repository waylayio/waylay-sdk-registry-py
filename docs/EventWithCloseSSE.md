# EventWithCloseSSE

SSE stream events with closing protocol

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**EventClose**](EventClose.md) |  | 
**data** | **str** | A text message describing the cause for closing the stream. | 

## Example

```python
from waylay.services.registry.models.event_with_close_sse import EventWithCloseSSE

# TODO update the JSON string below
json = "{}"
# create an instance of EventWithCloseSSE from a JSON string
event_with_close_sse_instance = EventWithCloseSSE.from_json(json)
# print the JSON string representation of the object
print EventWithCloseSSE.to_json()

# convert the object into a dict
event_with_close_sse_dict = event_with_close_sse_instance.to_dict()
# create an instance of EventWithCloseSSE from a dict
event_with_close_sse_form_dict = event_with_close_sse.from_dict(event_with_close_sse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


