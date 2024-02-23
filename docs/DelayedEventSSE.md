# DelayedEventSSE

A message that notifies a state change in a background job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** | The job queue event that trigged this message | 
**data** | [**JobEventResponseDelayedEventData**](JobEventResponseDelayedEventData.md) |  | 

## Example

```python
from waylay.services.registry.models.delayed_event_sse import DelayedEventSSE

# TODO update the JSON string below
json = "{}"
# create an instance of DelayedEventSSE from a JSON string
delayed_event_sse_instance = DelayedEventSSE.from_json(json)
# print the JSON string representation of the object
print DelayedEventSSE.to_json()

# convert the object into a dict
delayed_event_sse_dict = delayed_event_sse_instance.to_dict()
# create an instance of DelayedEventSSE from a dict
delayed_event_sse_form_dict = delayed_event_sse.from_dict(delayed_event_sse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


