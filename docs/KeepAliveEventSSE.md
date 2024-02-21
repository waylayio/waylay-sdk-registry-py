# KeepAliveEventSSE

A message that acknowledges that the stream is still alive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**EventKeepAlive**](EventKeepAlive.md) |  | 
**data** | **str** | A text message acknowledging that events will be forwarded. | [optional] 

## Example

```python
from waylay.services.registry.models.keep_alive_event_sse import KeepAliveEventSSE

# TODO update the JSON string below
json = "{}"
# create an instance of KeepAliveEventSSE from a JSON string
keep_alive_event_sse_instance = KeepAliveEventSSE.from_json(json)
# print the JSON string representation of the object
print KeepAliveEventSSE.to_json()

# convert the object into a dict
keep_alive_event_sse_dict = keep_alive_event_sse_instance.to_dict()
# create an instance of KeepAliveEventSSE from a dict
keep_alive_event_sse_form_dict = keep_alive_event_sse.from_dict(keep_alive_event_sse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


