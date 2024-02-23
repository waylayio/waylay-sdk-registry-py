# EventSSE

SSE stream events without closing protocol

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**EventKeepAlive**](EventKeepAlive.md) |  | 
**data** | **str** | A text message acknowledging that events will be forwarded. | 

## Example

```python
from waylay.services.registry.models.event_sse import EventSSE

# TODO update the JSON string below
json = "{}"
# create an instance of EventSSE from a JSON string
event_sse_instance = EventSSE.from_json(json)
# print the JSON string representation of the object
print EventSSE.to_json()

# convert the object into a dict
event_sse_dict = event_sse_instance.to_dict()
# create an instance of EventSSE from a dict
event_sse_form_dict = event_sse.from_dict(event_sse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


