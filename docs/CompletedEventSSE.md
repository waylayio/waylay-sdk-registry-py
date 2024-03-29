# CompletedEventSSE

A message that notifies a state change in a background job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**CompletedEventSSEEvent**](CompletedEventSSEEvent.md) |  | 
**data** | [**JobEventResponseCompletedEventData**](JobEventResponseCompletedEventData.md) |  | 

## Example

```python
from waylay.services.registry.models.completed_event_sse import CompletedEventSSE

# TODO update the JSON string below
json = "{}"
# create an instance of CompletedEventSSE from a JSON string
completed_event_sse_instance = CompletedEventSSE.from_json(json)
# print the JSON string representation of the object
print CompletedEventSSE.to_json()

# convert the object into a dict
completed_event_sse_dict = completed_event_sse_instance.to_dict()
# create an instance of CompletedEventSSE from a dict
completed_event_sse_form_dict = completed_event_sse.from_dict(completed_event_sse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


