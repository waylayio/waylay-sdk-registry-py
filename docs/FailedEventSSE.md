# FailedEventSSE

A message that notifies a state change in a background job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**FailedEventSSEEvent**](FailedEventSSEEvent.md) |  | 
**data** | [**JobEventResponseFailedEventData**](JobEventResponseFailedEventData.md) |  | 

## Example

```python
from waylay.services.registry.models.failed_event_sse import FailedEventSSE

# TODO update the JSON string below
json = "{}"
# create an instance of FailedEventSSE from a JSON string
failed_event_sse_instance = FailedEventSSE.from_json(json)
# print the JSON string representation of the object
print FailedEventSSE.to_json()

# convert the object into a dict
failed_event_sse_dict = failed_event_sse_instance.to_dict()
# create an instance of FailedEventSSE from a dict
failed_event_sse_form_dict = failed_event_sse.from_dict(failed_event_sse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


