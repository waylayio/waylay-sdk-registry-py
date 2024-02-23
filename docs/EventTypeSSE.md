# EventTypeSSE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.registry.models.event_type_sse import EventTypeSSE

# TODO update the JSON string below
json = "{}"
# create an instance of EventTypeSSE from a JSON string
event_type_sse_instance = EventTypeSSE.from_json(json)
# print the JSON string representation of the object
print EventTypeSSE.to_json()

# convert the object into a dict
event_type_sse_dict = event_type_sse_instance.to_dict()
# create an instance of EventTypeSSE from a dict
event_type_sse_form_dict = event_type_sse.from_dict(event_type_sse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


